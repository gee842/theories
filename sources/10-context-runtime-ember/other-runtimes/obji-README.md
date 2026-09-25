# obji

A prompt/parse codec for typed LLM I/O.

Two functions. Zero dependencies. Works with any LLM client.

```typescript
import { prompt, parse } from "obji";

// Encode: schema + data + instruction → prompt string
const p = prompt("screen this applicant", candidate, CandidateSchema, DecisionSchema);

// ... send p to any LLM, any way you want ...

// Decode: LLM response string → typed, validated object
const result = parse(response, DecisionSchema);
if (result.success) {
  result.data.decision; // "advance" | "reject" | "hold"
}
```

Or use `build()` to wrap it all into a single typed function:

```typescript
import { build } from "obji";

const screen = build("screen this applicant", CandidateSchema, DecisionSchema, async (p) => {
  const r = await anthropic.messages.create({ model: "claude-opus-4-6", max_tokens: 1024,
    messages: [{ role: "user", content: p }] });
  return r.content[0].text;
});

const decision = await screen(candidate); // typed as Decision — retries automatically
```

---

## What it does

`obji` turns your TypeScript types into context-rich prompts, and parses LLM responses back into validated objects. It doesn't call LLMs — that's your LLM client's job.

```
prompt(instruction, data, InputSchema, OutputSchema)
    ↓ string
  [ Vercel AI SDK / Anthropic SDK / OpenAI / fetch / anything ]
    ↓ string
parse(response, OutputSchema)
    ↓ typed, validated object
```

The prompt includes field descriptions, enum constraints, and domain context from your schemas — the LLM understands *what it's looking at*, not just *what shape to produce*.

## Install

```bash
npm install obji
```

Zod is optional — install it if you want Zod schema support:

```bash
npm install zod
```

No build plugins. No config. No provider packages.

---

## build() — the one-liner

`build()` composes `prompt()` + your LLM + `parse()` into a single typed async function. It handles the encode → call → decode cycle and retries automatically on parse failure.

```typescript
import { build } from "obji";
import { z } from "zod";

const TicketSchema = z.object({
  subject: z.string(),
  priority: z.enum(["low", "medium", "high", "critical"]),
});

const RouteSchema = z.object({
  team: z.enum(["billing", "technical", "sales", "general"]).describe("Which team should handle this"),
  reason: z.string().describe("One sentence explaining the routing decision"),
});

// Define once — call many times
const routeTicket = build("route this support ticket to the correct team",
  TicketSchema, RouteSchema,
  async (p) => {
    const r = await openai.chat.completions.create({
      model: "gpt-4o",
      messages: [{ role: "user", content: p }],
    });
    return r.choices[0].message.content!;
  }
);

// Use it like any typed async function
const result = await routeTicket({ subject: "Can't access my invoice", priority: "medium" });
// result.team   → "billing"
// result.reason → "Invoice access issues are handled by the billing team"
```

On parse failure, `build()` appends the parse error as feedback and retries. Default: 2 retries (3 total attempts). Configure with `{ retries: N }`.

```typescript
// Never retries — throws immediately on failure
const strict = build("classify", InputSchema, OutputSchema, llm, { retries: 0 });

// Up to 5 retries (6 total attempts)
const lenient = build("classify", InputSchema, OutputSchema, llm, { retries: 5 });
```

---

## prompt() + parse() — the manual flow

When you need more control — custom retry logic, streaming, cost tracking, different models per attempt — use `prompt()` and `parse()` directly.

```typescript
import { prompt, parse } from "obji";

let p = prompt("screen this applicant", candidate, CandidateSchema, DecisionSchema);

for (let attempt = 0; attempt < 3; attempt++) {
  const response = await callLLM(p);
  const result = parse(response, DecisionSchema);

  if (result.success) return result.data; // typed Decision

  // Append parse error as feedback and retry
  p = p + "\n\n" + result.feedback;
}
```

### parse() result

`parse()` returns a discriminated union — no try/catch needed:

```typescript
const result = parse(response, DecisionSchema);

if (result.success) {
  result.data      // typed Decision object
} else {
  result.error     // human-readable description of what went wrong
  result.feedback  // pre-formatted string to append to your prompt for retry
  result.raw       // the original response text
}
```

The `feedback` string is designed to be read by an LLM:

```
## Previous Attempt Failed

Your previous response could not be parsed. Here are the errors:

decision: "maybe" is not one of: advance, reject, hold

Your previous response was:
{"decision":"maybe","score":72}

Please fix these issues and respond again with valid JSON matching the required schema.
```

---

## Schema formats

Both `prompt()` and `parse()` accept any of these — mix them freely:

```typescript
// Zod — .describe() for fields, .meta({ context }) for domain knowledge
const CandidateSchema = z.object({
  name: z.string().describe("Full name"),
  skills: z.array(z.string()).describe("Self-reported technical skills"),
  remote: z.boolean().describe("Open to fully remote work"),
}).meta({ context: "Skills are self-reported and unverified at this stage" });

// Decorated class — @schema, @context, @field
@schema("A job applicant")
@context("Skills are self-reported and unverified at this stage")
class Candidate {
  @field("Full name") name!: string;
  @field("Self-reported technical skills", { array: true }) skills!: string[];
  @field("Open to fully remote work", { type: "boolean" }) remote!: boolean;
}

// Raw JSON Schema
const schema = {
  type: "object",
  context: "Skills are self-reported and unverified at this stage",
  properties: {
    name: { type: "string", description: "Full name" },
    skills: { type: "array", items: { type: "string" }, description: "Self-reported technical skills" },
    remote: { type: "boolean", description: "Open to fully remote work" },
  },
  required: ["name", "skills", "remote"],
};

// String description — lightweight, no validation
"a job applicant with name, skills array, and remote preference"

// Omitted — no schema, best-effort JSON parse
undefined
```

Mix formats freely:

```typescript
prompt("screen", data, CandidateZod, DecisionClass)    // Zod in, class out
prompt("draft email", data, CandidateClass, "a short personalized email") // class in, string out
prompt("extract", html, "raw HTML page", StructuredZod) // string in, Zod out
```

---

## Array and enum output modes

### Array of objects

Pass a single-element array to get an array of validated objects back:

```typescript
const ReviewSchema = z.object({
  id: z.string(),
  sentiment: z.enum(["positive", "negative", "neutral"]),
  summary: z.string(),
});

// prompt() tells the LLM to respond with a JSON array
const p = prompt("analyze each review", reviews, null, [ReviewSchema]);

// parse() validates every item and reports per-item errors
const result = parse(response, [ReviewSchema]);
// result.data → ReviewSchema[]
// On failure: "Item 2: $.sentiment: \"meh\" is not one of: positive, negative, neutral"
```

Works with `build()` too:

```typescript
const analyzeReviews = build("analyze each review", null, [ReviewSchema], llm);
const results = await analyzeReviews(reviews); // typed as Review[]
```

### Enum (pick one)

Pass an array of strings to get a single validated value back:

```typescript
// prompt() tells the LLM to respond with exactly one value
const p = prompt("classify the sentiment", review, null, ["positive", "negative", "neutral"]);

// parse() strips whitespace and quotes, validates membership
const result = parse(response, ["positive", "negative", "neutral"]);
// result.data → "positive" | "negative" | "neutral"
```

---

## promptSplit() — system/user separation

Some APIs (Anthropic, OpenAI) accept a separate system message. `promptSplit()` has the same signature as `prompt()` but returns `{ system, user }`:

```typescript
import { promptSplit } from "obji";

const { system, user } = promptSplit("screen this applicant", candidate, CandidateSchema, DecisionSchema);
// system: schemas, context, output format instructions (stable — cache-friendly)
// user:   instruction + data (changes per request)

// Anthropic SDK
await anthropic.messages.create({
  model: "claude-opus-4-6",
  system,
  messages: [{ role: "user", content: user }],
});

// OpenAI SDK
await openai.chat.completions.create({
  model: "gpt-4o",
  messages: [
    { role: "system", content: system },
    { role: "user", content: user },
  ],
});
```

---

## Usage with Vercel AI SDK

When using `generateObject`, Vercel handles the output schema natively — only pass the input schema to `prompt()`:

```typescript
import { prompt } from "obji";
import { generateObject } from "ai";
import { openai } from "@ai-sdk/openai";

const { object } = await generateObject({
  model: openai("gpt-4o"),
  schema: DecisionSchema,             // Vercel handles output structure
  prompt: prompt(                     // obji handles input context
    "Screen this applicant",
    candidate,
    CandidateSchema                   // no output schema — Vercel owns that
  ),
});
// object.decision → "advance" | "reject" | "hold"
```

When using `generateText`, use both schemas through `prompt()` and `parse()` the response:

```typescript
import { prompt, parse } from "obji";
import { generateText } from "ai";
import { anthropic } from "@ai-sdk/anthropic";

const { text } = await generateText({
  model: anthropic("claude-opus-4-6"),
  prompt: prompt("Screen this applicant", candidate, CandidateSchema, DecisionSchema),
});

const result = parse(text, DecisionSchema);
if (result.success) console.log(result.data.decision);
```

---

## The `context` field

Field descriptions tell the LLM *what* each field is. `context` tells it *why fields matter and how they relate* — this is what makes prompts better than hand-written ones.

```typescript
// Without context: the LLM sees field names and types and guesses intent
const CandidateSchema = z.object({
  remote: z.boolean(),
  skills: z.array(z.string()),
});

// With context: the LLM has the reasoning it needs to make good decisions
const CandidateSchema = z.object({
  remote: z.boolean().describe("Open to fully remote work"),
  skills: z.array(z.string()).describe("Self-reported, unverified"),
}).meta({
  context: `remote is a hard requirement — all open roles are distributed.
Candidates with remote: false should not advance regardless of skills.
Skills are self-reported; weight them lower than verified experience.`
});
```

Context attaches via `.meta({ context })` (Zod v4), `.describe()` on the object (Zod v3 workaround), or the `@context()` decorator. It appears in the prompt as its own section — not inside the schema JSON, which keeps both readable.

---

## API

### `build(instruction, inputSchema, outputSchema, llm, options?) → (input) => Promise<output>`

Creates a typed async function that handles prompt → LLM → parse → retry automatically.

- `llm`: `(prompt: string) => Promise<string>` — your LLM caller, any SDK
- `options.retries`: number of retry attempts on parse failure (default: `2`)
- Throws `Error` if all attempts fail

### `prompt(instruction, input?, inputSchema?, outputSchema?) → string`

Builds a context-rich prompt string. Pure function, no side effects.

### `parse(response, outputSchema?) → ParseResult<T>`

Parses and validates an LLM response string. Returns `{ success, data }` or `{ success, error, feedback, raw }`.

### `promptSplit(instruction, input?, inputSchema?, outputSchema?) → { system, user }`

Same as `prompt()` but splits the output into a stable `system` part (schemas, context, format instructions) and a dynamic `user` part (instruction + data).

### `validate(value, schema) → string[]`

Validates a value against a JSON Schema. Returns array of error strings (empty = valid). Exported for reuse.

### `resolveSchema(arg) → ResolvedSchema`

Resolves any schema format to a canonical internal representation. Useful for debugging schema detection.

### `extractSchema(cls) → JsonSchema`

Extracts JSON Schema from a decorated class. Useful for inspection.

### Decorators

```typescript
@schema("description")                                       // class-level description
@context("domain knowledge that guides LLM reasoning")      // class-level context
@field("description", { type?, enum?, optional?, array?, of? }) // property-level
```

---

## License

MIT
