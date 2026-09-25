# Integrating OpenAI SDK with Streaming Responses

created: 2024-11-16T14:57:19.548192Z  uuid: 1d93df60-7c11-424a-a8d9-1fc1e70097e2  export: old
messages: 2  total_chars: 4509  human_chars: 1064


---
**HUMAN** (2024-11-16T14:57):

import { z } from 'zod';
import { createOpenAI } from "@ai-sdk/openai";
import { streamText, tool } from "ai";

// Allow streaming responses up to 30 seconds
export const maxDuration = 30;

const openai = createOpenAI({
  compatibility: "compatible",
  baseURL: process.env.NEXT_PUBLIC_REDPILL_BASE_URL,
  apiKey: process.env.NEXT_PUBLIC_REDPILL_API_KEY,
});

export async function POST(req: Request) {
  const { messages } = await req.json();

  const result = await streamText({
    model: openai("meta-llama/llama-3.2-90b-vision-instruct"),
    system: "You are a helpful assistant.",
    tools: {
      weather: tool({
        description: 'Get the weather in a location',
        parameters: z.object({
          location: z.string().describe('The location to get the weather for'),
        }),
        execute: async ({ location }) => ({
          location,
          temperature: 72 + Math.floor(Math.random() * 21) - 10,
        }),
      }),
    },
    messages,
  });

  return result.toDataStreamResponse();
}

I want to use the tool but it doesn't work

---
**ASSISTANT** (2024-11-16T14:57):

 I notice you're trying to use a tool function with the AI SDK. Let me help you create a working example that demonstrates how to properly use the weather tool.



<antArtifact identifier="weather-tool-example" type="application/vnd.ant.code" language="typescript" title="Weather Tool Implementation with AI SDK">
// weather-route.ts
import { z } from 'zod';
import { createOpenAI } from "@ai-sdk/openai";
import { streamText, tool } from "ai";

// Allow streaming responses up to 30 seconds
export const maxDuration = 30;

const openai = createOpenAI({
  compatibility: "compatible",
  baseURL: process.env.NEXT_PUBLIC_REDPILL_BASE_URL,
  apiKey: process.env.NEXT_PUBLIC_REDPILL_API_KEY,
});

export async function POST(req: Request) {
  const { messages } = await req.json();

  // Define the weather tool
  const weatherTool = tool({
    name: 'get_weather', // Adding name is important for the model to identify the tool
    description: 'Get the weather in a location',
    parameters: z.object({
      location: z.string().describe('The location to get the weather for'),
    }),
    execute: async ({ location }) => ({
      location,
      temperature: 72 + Math.floor(Math.random() * 21) - 10,
    }),
  });

  try {
    const result = await streamText({
      model: openai("meta-llama/llama-3.2-90b-vision-instruct"),
      system: `You are a helpful assistant that can check the weather. 
               When asked about weather, always use the weather tool to get accurate information.`,
      messages,
      tools: [weatherTool], // Pass tools as an array
    });

    return result.toDataStreamResponse();
  } catch (error) {
    console.error('Error:', error);
    return new Response(JSON.stringify({ error: 'Failed to process request' }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' },
    });
  }
}

// Example of how to call the API (client-side)
const messages = [
  { role: 'user', content: 'What\'s the weather like in New York?' }
];

const response = await fetch('/api/weather', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({ messages }),
});

// Handle streaming response
const reader = response.body?.getReader();
while (reader) {
  const { done, value } = await reader.read();
  if (done) break;
  // Process the streamed chunks
  console.log(new TextDecoder().decode(value));
}
</antArtifact>

Here are the key changes I made to fix the tool implementation:

1. Added a `name` property to the tool definition - this is crucial for the model to identify and use the tool correctly
2. Passed the tool in an array to the `tools` parameter instead of an object
3. Enhanced the system prompt to specifically instruct the model to use the weather tool
4. Added error handling
5. Included example client-side code showing how to call and handle the streaming response

The tool should now work when you ask about weather in any location. For example, if you ask "What's the weather like in New York?", the model will use the weather tool to fetch the temperature.

A few things to note:
1. Make sure your environment variables are properly set
2. The temperature calculation is just a random example - you'd want to replace this with real weather data in production
3. The streaming response needs to be properly handled on the client side

Would you like me to explain any part of this implementation in more detail or help you test it?
