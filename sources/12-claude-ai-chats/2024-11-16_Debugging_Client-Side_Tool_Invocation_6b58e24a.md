# Debugging Client-Side Tool Invocation

created: 2024-11-16T16:10:50.515341Z  uuid: 6b58e24a-e27e-4a63-8b3b-c6fe30270ec4  export: old
messages: 6  total_chars: 17077  human_chars: 2712


---
**HUMAN** (2024-11-16T16:11):

'use client';

import { ToolInvocation } from 'ai';
import { Message, useChat } from 'ai/react';
export default function Chat() {
const { messages, input, handleInputChange, handleSubmit, addToolResult } =
useChat({
 maxSteps: 5,
// run client-side tools that are automatically executed:
async onToolCall({ toolCall }) {
if (toolCall.toolName === 'getLocation') {
const cities = [
'New York',
'Los Angeles',
'Chicago',
'San Francisco',
];
return cities[Math.floor(Math.random() * cities.length)];
}
},
});
return (
<>
{messages?.map((m: Message) => (
<div key={m.id}>
<strong>{m.role}:</strong>
{m.content}
{m.toolInvocations?.map((toolInvocation: ToolInvocation) => {
const toolCallId = toolInvocation.toolCallId;
const addResult = (result: string) =>
addToolResult({ toolCallId, result });
// render confirmation tool (client-side tool with user interaction)
if (toolInvocation.toolName === 'askForConfirmation') {
return (
<div key={toolCallId}>
{toolInvocation.args.message}
<div>
{'result' in toolInvocation ? (
<b>{toolInvocation.result}</b>
) : (
<>
<button onClick={() => addResult('Yes')}>Yes</button>
<button onClick={() => addResult('No')}>No</button>
</>
)}
</div>
</div>
);
}
// other tools:
return 'result' in toolInvocation ? (
<div key={toolCallId}>
Tool call {`${toolInvocation.toolName}: `}
{toolInvocation.result}
</div>
) : (
<div key={toolCallId}>Calling {toolInvocation.toolName}...</div>
);
})}
<br />
</div>
))}
<form onSubmit={handleSubmit}>
<input value={input} onChange={handleInputChange} />
</form>
</>
);
}

why my onToolCall is never called?

---
**ASSISTANT** (2024-11-16T16:11):

 Let me help you debug why the `onToolCall` function isn't being triggered. There are a few potential reasons and steps needed to make tool calls work with the AI SDK:

1. First, you need to define the available tools when initializing `useChat`. The tools property is missing in your configuration:



<antArtifact identifier="chat-with-tools" type="application/vnd.ant.code" language="typescript" title="Chat Component with Tool Configuration">
'use client';

import { ToolInvocation } from 'ai';
import { Message, useChat } from 'ai/react';

export default function Chat() {
  const { messages, input, handleInputChange, handleSubmit, addToolResult } = useChat({
    maxSteps: 5,
    // Define the available tools
    tools: [
      {
        name: 'getLocation',
        description: 'Get a random city location',
        parameters: {
          type: 'object',
          properties: {},
          required: []
        }
      },
      {
        name: 'askForConfirmation',
        description: 'Ask the user for confirmation',
        parameters: {
          type: 'object',
          properties: {
            message: {
              type: 'string',
              description: 'The message to show to the user'
            }
          },
          required: ['message']
        }
      }
    ],
    // Tool handlers
    async onToolCall({ toolCall }) {
      console.log('Tool called:', toolCall.toolName); // Debug log
      
      if (toolCall.toolName === 'getLocation') {
        const cities = [
          'New York',
          'Los Angeles',
          'Chicago',
          'San Francisco',
        ];
        return cities[Math.floor(Math.random() * cities.length)];
      }
    },
  });

  return (
    <>
      {messages?.map((m: Message) => (
        <div key={m.id}>
          <strong>{m.role}:</strong>
          {m.content}
          {m.toolInvocations?.map((toolInvocation: ToolInvocation) => {
            const toolCallId = toolInvocation.toolCallId;
            const addResult = (result: string) =>
              addToolResult({ toolCallId, result });

            // render confirmation tool
            if (toolInvocation.toolName === 'askForConfirmation') {
              return (
                <div key={toolCallId}>
                  {toolInvocation.args.message}
                  <div>
                    {'result' in toolInvocation ? (
                      <b>{toolInvocation.result}</b>
                    ) : (
                      <>
                        <button onClick={() => addResult('Yes')}>Yes</button>
                        <button onClick={() => addResult('No')}>No</button>
                      </>
                    )}
                  </div>
                </div>
              );
            }

            // other tools:
            return 'result' in toolInvocation ? (
              <div key={toolCallId}>
                Tool call {`${toolInvocation.toolName}: `}
                {toolInvocation.result}
              </div>
            ) : (
              <div key={toolCallId}>Calling {toolInvocation.toolName}...</div>
            );
          })}
          <br />
        </div>
      ))}
      <form onSubmit={handleSubmit}>
        <input 
          value={input} 
          onChange={handleInputChange}
          placeholder="Type a message..."
          className="w-full p-2 border rounded"
        />
      </form>
    </>
  );
}
</antArtifact>

Key changes and requirements to make tools work:

1. You must define the `tools` array in the `useChat` configuration - this tells the AI which tools are available and their specifications.

2. Make sure your API route (likely `/api/chat`) is properly configured to handle tools. In your API route, you need something like:

```typescript
import { OpenAIStream, StreamingTextResponse } from 'ai'
import OpenAI from 'openai'

export const runtime = 'edge'

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY!
})

export async function POST(req: Request) {
  const { messages, tools } = await req.json()

  const response = await openai.chat.completions.create({
    model: 'gpt-4-1106-preview',
    stream: true,
    messages,
    tools, // Pass the tools configuration
    tool_choice: 'auto'
  })

  const stream = OpenAIStream(response)
  return new StreamingTextResponse(stream)
}
```

3. Add a debug log in your `onToolCall` function to verify if it's being called.

4. Make sure you're using a model that supports function calling (like GPT-4 or GPT-3.5-turbo).

To test if it's working:
1. Send a message that would trigger the getLocation tool, like "What city should I visit?"
2. Check your browser console for the debug log
3. Verify the API is correctly configured with tools support

Would you like me to help you debug any specific part of the implementation?

---
**HUMAN** (2024-11-16T16:33):

"<|python_tag|>{"name": "getWeatherInformation", "parameters": {"city": "user's location"}}<|eom_id|><|start_header_id|>assistant<|end_header_id|> <|python_tag|>{"name": "getLocation", "parameters": {}}<|eom_id|><|start_header_id|>assistant<|end_header_id|> <|python_tag|>{"name": "getWeatherInformation", "parameters": {"city": "New York"}}<|eom_id|><|start_header_id|>assistant<|end_header_id|> <|python_tag|>{"name": "askForConfirmation", "parameters": {"message": "Do you want to know the weather in New York?"}}<|eom_id|><|start_header_id|>assistant<|end_header_id|> <|python_tag|>{"name": "getWeatherInformation", "parameters": {"city": "London"}}<|eom_id|><|start_header_id|>assistant<|end_header_id|> <|python_tag|>{"name": "askForConfirmation", "parameters": {"message": "Do you want to know"

the content i get from the message is like this, no toolInvocations

---
**ASSISTANT** (2024-11-16T16:33):

 Ah, I see the issue. The message content you're receiving contains the tool calls embedded in a custom format with `<|python_tag|>` and other tags, rather than as proper `toolInvocations` in the message object. This suggests there might be an issue with how the AI response is being parsed or streamed.

Let's modify the code to handle this:

<antArtifact identifier="chat-with-tools-fixed" type="application/vnd.ant.code" language="typescript" title="Fixed Chat Component with Tool Parsing">
'use client';

import { ToolInvocation } from 'ai';
import { Message, useChat } from 'ai/react';

// Helper function to parse tool calls from message content
function parseToolCalls(content: string): ToolInvocation[] {
  const toolCalls: ToolInvocation[] = [];
  const regex = /<\|python_tag\|>(.+?)<\|eom_id\|>/g;
  let match;
  let id = 0;

  while ((match = regex.exec(content)) !== null) {
    try {
      const toolData = JSON.parse(match[1]);
      toolCalls.push({
        toolCallId: `call_${id++}`,
        toolName: toolData.name,
        args: toolData.parameters
      });
    } catch (e) {
      console.error('Failed to parse tool call:', e);
    }
  }

  return toolCalls;
}

export default function Chat() {
  const { messages, input, handleInputChange, handleSubmit, addToolResult } = useChat({
    maxSteps: 5,
    tools: [
      {
        name: 'getLocation',
        description: 'Get a random city location',
        parameters: {
          type: 'object',
          properties: {},
          required: []
        }
      },
      {
        name: 'getWeatherInformation',
        description: 'Get weather information for a city',
        parameters: {
          type: 'object',
          properties: {
            city: {
              type: 'string',
              description: 'The city to get weather for'
            }
          },
          required: ['city']
        }
      },
      {
        name: 'askForConfirmation',
        description: 'Ask the user for confirmation',
        parameters: {
          type: 'object',
          properties: {
            message: {
              type: 'string',
              description: 'The message to show to the user'
            }
          },
          required: ['message']
        }
      }
    ],
    async onToolCall({ toolCall }) {
      console.log('Tool called:', toolCall.toolName, toolCall.args);
      
      if (toolCall.toolName === 'getLocation') {
        const cities = ['New York', 'Los Angeles', 'Chicago', 'San Francisco'];
        return cities[Math.floor(Math.random() * cities.length)];
      }
      
      if (toolCall.toolName === 'getWeatherInformation') {
        // Mock weather data
        return `The weather in ${toolCall.args.city} is sunny and 72°F`;
      }
    },
  });

  return (
    <>
      {messages?.map((m: Message) => {
        // Parse tool calls from the message content
        const toolInvocations = parseToolCalls(m.content);
        
        return (
          <div key={m.id}>
            <strong>{m.role}:</strong>
            {/* Clean the content by removing tool call tags */}
            {m.content.replace(/<\|python_tag\|>(.+?)<\|eom_id\|>/g, '')}
            {toolInvocations.map((toolInvocation: ToolInvocation) => {
              const toolCallId = toolInvocation.toolCallId;
              const addResult = (result: string) =>
                addToolResult({ toolCallId, result });

              // render confirmation tool
              if (toolInvocation.toolName === 'askForConfirmation') {
                return (
                  <div key={toolCallId} className="my-2 p-2 border rounded">
                    {toolInvocation.args.message}
                    <div className="mt-2">
                      {'result' in toolInvocation ? (
                        <b>{toolInvocation.result}</b>
                      ) : (
                        <>
                          <button 
                            onClick={() => addResult('Yes')}
                            className="mr-2 px-3 py-1 bg-blue-500 text-white rounded"
                          >
                            Yes
                          </button>
                          <button 
                            onClick={() => addResult('No')}
                            className="px-3 py-1 bg-gray-500 text-white rounded"
                          >
                            No
                          </button>
                        </>
                      )}
                    </div>
                  </div>
                );
              }

              // other tools:
              return 'result' in toolInvocation ? (
                <div key={toolCallId} className="my-2">
                  Tool call {`${toolInvocation.toolName}: `}
                  {toolInvocation.result}
                </div>
              ) : (
                <div key={toolCallId} className="my-2">
                  Calling {toolInvocation.toolName}...
                </div>
              );
            })}
            <br />
          </div>
        );
      })}
      <form onSubmit={handleSubmit}>
        <input 
          value={input} 
          onChange={handleInputChange}
          placeholder="Type a message..."
          className="w-full p-2 border rounded"
        />
      </form>
    </>
  );
}
</antArtifact>

Key changes made:

1. Added a `parseToolCalls` helper function that extracts tool calls from the message content using regex
2. Modified the render logic to parse tool calls from each message's content
3. Added the `getWeatherInformation` tool to the tools configuration
4. Cleaned up the displayed message content by removing the tool call tags
5. Added some basic styling for better visual presentation

Also, make sure your API route is properly configured to handle the OpenAI response format. Here's how your API route should look:

```typescript
import { OpenAIStream, StreamingTextResponse } from 'ai'
import OpenAI from 'openai'

export const runtime = 'edge'

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY!
})

export async function POST(req: Request) {
  const { messages, tools } = await req.json()

  const response = await openai.chat.completions.create({
    model: 'gpt-4-1106-preview',
    stream: true,
    messages,
    tools,
    tool_choice: 'auto',
    response_format: { type: "text" }  // This might help with the formatting
  })

  const stream = OpenAIStream(response)
  return new StreamingTextResponse(stream)
}
```

This solution should now:
1. Properly parse and display tool calls from the message content
2. Handle the custom format you're receiving
3. Support all the tools mentioned in your example
4. Maintain the interactive confirmation dialogs
5. Clean up the display by removing the tool call tags from the visible content

Would you like me to explain any part of this implementation in more detail?

---
**HUMAN** (2024-11-16T16:36):

type ToolInvocation = ({
    state: 'partial-call';
} & ToolCall$1<string, any>) | ({
    state: 'call';
} & ToolCall$1<string, any>) | ({
    state: 'result';
} & ToolResult<string, any, any>);

can you rewrite function parseToolCalls(content: string): ToolInvocation[]

---
**ASSISTANT** (2024-11-16T16:36):

 Ah yes, let me adjust the `parseToolCalls` function to match the correct `ToolInvocation` type with the proper state handling:

<antArtifact identifier="parse-tool-calls" type="application/vnd.ant.code" language="typescript" title="Updated parseToolCalls Function">
type ToolCall<TName extends string = string, TParameters = any> = {
  toolCallId: string;
  toolName: TName;
  args: TParameters;
};

type ToolResult<TName extends string = string, TParameters = any, TResult = any> = {
  toolCallId: string;
  toolName: TName;
  args: TParameters;
  result: TResult;
};

type ToolInvocation = 
  | ({ state: 'partial-call' } & ToolCall)
  | ({ state: 'call' } & ToolCall)
  | ({ state: 'result' } & ToolResult);

function parseToolCalls(content: string): ToolInvocation[] {
  const toolCalls: ToolInvocation[] = [];
  const regex = /<\|python_tag\|>(.+?)<\|eom_id\|>/g;
  let match;
  let id = 0;

  while ((match = regex.exec(content)) !== null) {
    try {
      const toolData = JSON.parse(match[1]);
      
      // Create a basic tool call structure
      const baseToolCall: ToolCall = {
        toolCallId: `call_${id++}`,
        toolName: toolData.name,
        args: toolData.parameters
      };

      // For simplicity, we'll consider all parsed tools as in 'call' state
      // You might want to adjust this based on your specific needs
      const toolInvocation: ToolInvocation = {
        ...baseToolCall,
        state: 'call'
      };

      toolCalls.push(toolInvocation);
    } catch (e) {
      console.error('Failed to parse tool call:', e);
    }
  }

  return toolCalls;
}

// Example usage:
const exampleContent = `<|python_tag|>{"name": "getWeatherInformation", "parameters": {"city": "New York"}}<|eom_id|>`;
const toolCalls = parseToolCalls(exampleContent);
</antArtifact>

Key changes made:

1. Added proper type definitions for `ToolCall` and `ToolResult`
2. Updated the `ToolInvocation` type to match the union type you provided
3. Modified the function to set the appropriate `state` property for each tool invocation
4. Maintained the same parsing logic but with stricter typing

The function now returns tool invocations with the correct state. I've set them all to 'call' state by default, but you might want to adjust this based on your specific needs. For example:

1. You might want to detect 'partial-call' state based on incomplete parameters
2. You might want to detect 'result' state if there's result data in the message
3. You might want to track the state based on previous messages or context

Would you like me to modify the function further to handle any of these cases or explain any part in more detail?
