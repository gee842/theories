# Debugging onToolCall Callback in Chat App

created: 2024-11-16T15:46:23.774111Z  uuid: f4c15aa5-dcb7-434e-8e8f-54dd90eba94a  export: old
messages: 4  total_chars: 7449  human_chars: 1551


---
**HUMAN** (2024-11-16T15:46):

const chat: ChatResult = useChat({
    maxSteps: 5,

    // run client-side tools that are automatically executed:
    async onToolCall({ toolCall }) {
      console.log(toolCall.toolName);
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

onToolCall is never called, what could be wrong?

---
**ASSISTANT** (2024-11-16T15:46):

 Let me help you debug why the `onToolCall` callback isn't being triggered. Looking at your code, there are a few potential issues to check:



<antArtifact identifier="chat-tool-example" type="application/vnd.ant.code" language="typescript" title="Complete Chat Tool Implementation">
import { useChat } from 'ai/react';
import type { Tool } from 'ai';

// Define the tool schema
const tools: Tool[] = [
  {
    name: 'getLocation',
    description: 'Get a random city location',
    parameters: {
      type: 'object',
      properties: {},
      required: []
    }
  }
];

// Setup the chat with proper configuration
const ChatComponent = () => {
  const chat = useChat({
    maxSteps: 5,
    tools: tools, // Add the tools configuration
    
    async onToolCall({ toolCall }) {
      console.log(toolCall.toolName);
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
    // Chat UI implementation
    <div>
      {chat.messages.map((message) => (
        <div key={message.id}>
          {message.content}
        </div>
      ))}
      <input 
        value={chat.input}
        onChange={(e) => chat.setInput(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === 'Enter') {
            chat.handleSubmit(e);
          }
        }}
      />
    </div>
  );
};

export default ChatComponent;
</antArtifact>

The main issue is that you're missing the `tools` configuration in the `useChat` hook. To get the `onToolCall` callback to work, you need to:

1. Define the tool schema that specifies what tools are available
2. Pass this tools configuration to the `useChat` hook

Key changes needed:
- Add the `tools` array that defines your available tools
- Include the `tools` property in the `useChat` configuration
- Make sure your chat messages include function calls that would trigger the tool

Now when you send a message that requires location information, the AI should call the `getLocation` tool through the `onToolCall` callback.

Would you also like me to show an example of how to structure messages to trigger the tool call?

---
**HUMAN** (2024-11-16T15:48):

but tool call is on the server side:
export async function POST(req: Request) {
 const { messages } = await req.json();
const result = streamText({
 model: openai('gpt-4-turbo'),
 messages,
 tools: {
// server-side tool with execute function:
 getWeatherInformation: {
 description: 'show the weather in a given city to the user',
 parameters: z.object({ city: z.string() }),
execute: async ({}: { city: string }) => {
const weatherOptions = ['sunny', 'cloudy', 'rainy', 'snowy', 'windy'];
return weatherOptions[
Math.floor(Math.random() * weatherOptions.length)
];
},
},
// client-side tool that starts user interaction:
 askForConfirmation: {
 description: 'Ask the user for confirmation.',
 parameters: z.object({
 message: z.string().describe('The message to ask for confirmation.'),
}),
},
// client-side tool that is automatically executed on the client:
 getLocation: {
 description:
'Get the user location. Always ask for confirmation before using this tool.',
 parameters: z.object({}),
},
},
});
return result.toDataStreamResponse();
}

---
**ASSISTANT** (2024-11-16T15:48):

 Ah, I see the issue now. You're mixing client-side and server-side tool implementations. For client-side tools that are automatically executed (like `getLocation`), you need to handle them differently:

<antArtifact identifier="chat-api-route" type="application/vnd.ant.code" language="typescript" title="Complete Chat API Implementation">
// app/api/chat/route.ts
import { streamText } from 'ai';
import { openai } from '@/lib/openai';
import { z } from 'zod';

export async function POST(req: Request) {
  const { messages, toolResults } = await req.json();
  
  const result = streamText({
    model: openai('gpt-4-turbo'),
    messages,
    // Get the previous tool results from the client
    previousToolResults: toolResults,
    tools: {
      // server-side tool with execute function:
      getWeatherInformation: {
        description: 'show the weather in a given city to the user',
        parameters: z.object({ city: z.string() }),
        execute: async ({ city }: { city: string }) => {
          const weatherOptions = ['sunny', 'cloudy', 'rainy', 'snowy', 'windy'];
          return weatherOptions[Math.floor(Math.random() * weatherOptions.length)];
        },
      },
      // client-side tool that starts user interaction:
      askForConfirmation: {
        description: 'Ask the user for confirmation.',
        parameters: z.object({
          message: z.string().describe('The message to ask for confirmation.'),
        }),
      },
      // client-side tool that is automatically executed:
      getLocation: {
        description: 'Get the user location. Always ask for confirmation before using this tool.',
        parameters: z.object({}),
        // Remove execute function for client-side tools
      },
    },
  });

  return result.toDataStreamResponse();
}
</antArtifact>

And here's how to handle it on the client side:

<antArtifact identifier="chat-client" type="application/vnd.ant.code" language="typescript" title="Client-side Chat Implementation">
// app/page.tsx
import { useChat } from 'ai/react';

export default function Chat() {
  const { messages, handleSubmit, input, setInput } = useChat({
    api: '/api/chat',
    // Handle client-side tool calls
    body: {
      // Send tool results back to the server
      toolResults: {
        getLocation: async () => {
          const cities = ['New York', 'Los Angeles', 'Chicago', 'San Francisco'];
          return cities[Math.floor(Math.random() * cities.length)];
        },
      },
    },
  });

  return (
    <div>
      {messages.map((m) => (
        <div key={m.id}>{m.content}</div>
      ))}
      <form onSubmit={handleSubmit}>
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Say something..."
        />
      </form>
    </div>
  );
}
</antArtifact>

The key changes needed are:

1. On the server side:
   - Remove the `execute` function from client-side tools like `getLocation`
   - Handle `previousToolResults` from the client

2. On the client side:
   - Provide tool implementations in the `body.toolResults` object
   - Each tool function should return a value that will be sent back to the server

The flow works like this:
1. Server defines the tools available
2. When LLM calls a client-side tool, the request is made to the client
3. Client executes the tool function from `toolResults`
4. Result is sent back to the server in the next request
5. Server continues the conversation with the tool result

This structure ensures that client-side tools are properly executed and their results are incorporated into the conversation.
