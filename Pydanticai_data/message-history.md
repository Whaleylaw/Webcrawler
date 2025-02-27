---
url: https://ai.pydantic.dev/message-history/
title: Untitled
date_crawled: 
---

[ Skip to content ](#messages-and-chat-history)

[ ![logo](../img/logo-white.svg) ](.. "PydanticAI")

PydanticAI 

Messages and chat history 

Type to start searching

[ pydantic/pydantic-ai  ](https://github.com/pydantic/pydantic-ai "Go to repository")

[ ![logo](../img/logo-white.svg) ](.. "PydanticAI") PydanticAI 

[ pydantic/pydantic-ai  ](https://github.com/pydantic/pydantic-ai "Go to repository")

  * [ Introduction  ](..)
  * [ Installation  ](../install/)
  * [ Getting Help  ](../help/)
  * [ Contributing  ](../contributing/)
  * [ Troubleshooting  ](../troubleshooting/)
  * Documentation  Documentation 
    * [ Agents  ](../agents/)
    * [ Models  ](../models/)
    * [ Dependencies  ](../dependencies/)
    * [ Function Tools  ](../tools/)
    * [ Results  ](../results/)
    * Messages and chat history  [ Messages and chat history  ](./) Table of contents 
      * [ Accessing Messages from Results  ](#accessing-messages-from-results)
      * [ Using Messages as Input for Further Agent Runs  ](#using-messages-as-input-for-further-agent-runs)
      * [ Other ways of using messages  ](#other-ways-of-using-messages)
      * [ Examples  ](#examples)
    * [ Testing and Evals  ](../testing-evals/)
    * [ Debugging and Monitoring  ](../logfire/)
    * [ Multi-agent Applications  ](../multi-agent-applications/)
    * [ Graphs  ](../graph/)
  * [ Examples  ](../examples/)

Examples 
    * [ Pydantic Model  ](../examples/pydantic-model/)
    * [ Weather agent  ](../examples/weather-agent/)
    * [ Bank support  ](../examples/bank-support/)
    * [ SQL Generation  ](../examples/sql-gen/)
    * [ Flight booking  ](../examples/flight-booking/)
    * [ RAG  ](../examples/rag/)
    * [ Stream markdown  ](../examples/stream-markdown/)
    * [ Stream whales  ](../examples/stream-whales/)
    * [ Chat App with FastAPI  ](../examples/chat-app/)
    * [ Question Graph  ](../examples/question-graph/)
  * API Reference  API Reference 
    * [ pydantic_ai.agent  ](../api/agent/)
    * [ pydantic_ai.tools  ](../api/tools/)
    * [ pydantic_ai.result  ](../api/result/)
    * [ pydantic_ai.messages  ](../api/messages/)
    * [ pydantic_ai.exceptions  ](../api/exceptions/)
    * [ pydantic_ai.settings  ](../api/settings/)
    * [ pydantic_ai.usage  ](../api/usage/)
    * [ pydantic_ai.format_as_xml  ](../api/format_as_xml/)
    * [ pydantic_ai.models  ](../api/models/base/)
    * [ pydantic_ai.models.openai  ](../api/models/openai/)
    * [ pydantic_ai.models.anthropic  ](../api/models/anthropic/)
    * [ pydantic_ai.models.cohere  ](../api/models/cohere/)
    * [ pydantic_ai.models.gemini  ](../api/models/gemini/)
    * [ pydantic_ai.models.vertexai  ](../api/models/vertexai/)
    * [ pydantic_ai.models.groq  ](../api/models/groq/)
    * [ pydantic_ai.models.mistral  ](../api/models/mistral/)
    * [ pydantic_ai.models.test  ](../api/models/test/)
    * [ pydantic_ai.models.function  ](../api/models/function/)
    * [ pydantic_graph  ](../api/pydantic_graph/graph/)
    * [ pydantic_graph.nodes  ](../api/pydantic_graph/nodes/)
    * [ pydantic_graph.state  ](../api/pydantic_graph/state/)
    * [ pydantic_graph.mermaid  ](../api/pydantic_graph/mermaid/)
    * [ pydantic_graph.exceptions  ](../api/pydantic_graph/exceptions/)



Table of contents 

  * [ Accessing Messages from Results  ](#accessing-messages-from-results)
  * [ Using Messages as Input for Further Agent Runs  ](#using-messages-as-input-for-further-agent-runs)
  * [ Other ways of using messages  ](#other-ways-of-using-messages)
  * [ Examples  ](#examples)



  1. [ Introduction  ](..)
  2. [ Documentation  ](../agents/)



Version Notice

This documentation is ahead of the last release by [6 commits](https://github.com/pydantic/pydantic-ai/compare/v0.0.24...main). You may see documentation for features not yet supported in the latest release [v0.0.24 2025-02-12](https://github.com/pydantic/pydantic-ai/releases/tag/v0.0.24). 

# Messages and chat history

PydanticAI provides access to messages exchanged during an agent run. These messages can be used both to continue a coherent conversation, and to understand how an agent performed.

### Accessing Messages from Results

After running an agent, you can access the messages exchanged during that run from the `result` object.

Both `RunResult`[](../api/result/#pydantic_ai.result.RunResult) (returned by `Agent.run`[](../api/agent/#pydantic_ai.agent.Agent.run), `Agent.run_sync`[](../api/agent/#pydantic_ai.agent.Agent.run_sync)) and `StreamedRunResult`[](../api/result/#pydantic_ai.result.StreamedRunResult) (returned by `Agent.run_stream`[](../api/agent/#pydantic_ai.agent.Agent.run_stream)) have the following methods:

  * `all_messages()`[](../api/result/#pydantic_ai.result.RunResult.all_messages): returns all messages, including messages from prior runs. There's also a variant that returns JSON bytes, `all_messages_json()`[](../api/result/#pydantic_ai.result.RunResult.all_messages_json).
  * `new_messages()`[](../api/result/#pydantic_ai.result.RunResult.new_messages): returns only the messages from the current run. There's also a variant that returns JSON bytes, `new_messages_json()`[](../api/result/#pydantic_ai.result.RunResult.new_messages_json).



StreamedRunResult and complete messages

On `StreamedRunResult`[](../api/result/#pydantic_ai.result.StreamedRunResult), the messages returned from these methods will only include the final result message once the stream has finished.

E.g. you've awaited one of the following coroutines:

  * `StreamedRunResult.stream()`[](../api/result/#pydantic_ai.result.StreamedRunResult.stream)
  * `StreamedRunResult.stream_text()`[](../api/result/#pydantic_ai.result.StreamedRunResult.stream_text)
  * `StreamedRunResult.stream_structured()`[](../api/result/#pydantic_ai.result.StreamedRunResult.stream_structured)
  * `StreamedRunResult.get_data()`[](../api/result/#pydantic_ai.result.StreamedRunResult.get_data)



**Note:** The final result message will NOT be added to result messages if you use `.stream_text(delta=True)`[](../api/result/#pydantic_ai.result.StreamedRunResult.stream_text) since in this case the result content is never built as one string.

Example of accessing methods on a `RunResult`[](../api/result/#pydantic_ai.result.RunResult) :

run_result_messages.py```
from pydantic_ai import Agent
agent = Agent('openai:gpt-4o', system_prompt='Be a helpful assistant.')
result = agent.run_sync('Tell me a joke.')
print(result.data)
#> Did you hear about the toothpaste scandal? They called it Colgate.
# all messages from the run
print(result.all_messages())
"""
[
  ModelRequest(
    parts=[
      SystemPromptPart(
        content='Be a helpful assistant.',
        dynamic_ref=None,
        part_kind='system-prompt',
      ),
      UserPromptPart(
        content='Tell me a joke.',
        timestamp=datetime.datetime(...),
        part_kind='user-prompt',
      ),
    ],
    kind='request',
  ),
  ModelResponse(
    parts=[
      TextPart(
        content='Did you hear about the toothpaste scandal? They called it Colgate.',
        part_kind='text',
      )
    ],
    model_name='function:model_logic',
    timestamp=datetime.datetime(...),
    kind='response',
  ),
]
"""

```


_(This example is complete, it can be run "as is")_

Example of accessing methods on a `StreamedRunResult`[](../api/result/#pydantic_ai.result.StreamedRunResult) :

streamed_run_result_messages.py```
from pydantic_ai import Agent
agent = Agent('openai:gpt-4o', system_prompt='Be a helpful assistant.')

async def main():
  async with agent.run_stream('Tell me a joke.') as result:
    # incomplete messages before the stream finishes
    print(result.all_messages())
"""
    [
      ModelRequest(
        parts=[
          SystemPromptPart(
            content='Be a helpful assistant.',
            dynamic_ref=None,
            part_kind='system-prompt',
          ),
          UserPromptPart(
            content='Tell me a joke.',
            timestamp=datetime.datetime(...),
            part_kind='user-prompt',
          ),
        ],
        kind='request',
      )
    ]
    """
    async for text in result.stream_text():
      print(text)
      #> Did you hear
      #> Did you hear about the toothpaste
      #> Did you hear about the toothpaste scandal? They called
      #> Did you hear about the toothpaste scandal? They called it Colgate.
    # complete messages once the stream finishes
    print(result.all_messages())
"""
    [
      ModelRequest(
        parts=[
          SystemPromptPart(
            content='Be a helpful assistant.',
            dynamic_ref=None,
            part_kind='system-prompt',
          ),
          UserPromptPart(
            content='Tell me a joke.',
            timestamp=datetime.datetime(...),
            part_kind='user-prompt',
          ),
        ],
        kind='request',
      ),
      ModelResponse(
        parts=[
          TextPart(
            content='Did you hear about the toothpaste scandal? They called it Colgate.',
            part_kind='text',
          )
        ],
        model_name='function:stream_model_logic',
        timestamp=datetime.datetime(...),
        kind='response',
      ),
    ]
    """

```


_(This example is complete, it can be run "as is" — you'll need to add`asyncio.run(main())` to run `main`)_

### Using Messages as Input for Further Agent Runs

The primary use of message histories in PydanticAI is to maintain context across multiple agent runs.

To use existing messages in a run, pass them to the `message_history` parameter of `Agent.run`[](../api/agent/#pydantic_ai.agent.Agent.run), `Agent.run_sync`[](../api/agent/#pydantic_ai.agent.Agent.run_sync) or `Agent.run_stream`[](../api/agent/#pydantic_ai.agent.Agent.run_stream).

If `message_history` is set and not empty, a new system prompt is not generated — we assume the existing message history includes a system prompt.

Reusing messages in a conversation```
from pydantic_ai import Agent
agent = Agent('openai:gpt-4o', system_prompt='Be a helpful assistant.')
result1 = agent.run_sync('Tell me a joke.')
print(result1.data)
#> Did you hear about the toothpaste scandal? They called it Colgate.
result2 = agent.run_sync('Explain?', message_history=result1.new_messages())
print(result2.data)
#> This is an excellent joke invented by Samuel Colvin, it needs no explanation.
print(result2.all_messages())
"""
[
  ModelRequest(
    parts=[
      SystemPromptPart(
        content='Be a helpful assistant.',
        dynamic_ref=None,
        part_kind='system-prompt',
      ),
      UserPromptPart(
        content='Tell me a joke.',
        timestamp=datetime.datetime(...),
        part_kind='user-prompt',
      ),
    ],
    kind='request',
  ),
  ModelResponse(
    parts=[
      TextPart(
        content='Did you hear about the toothpaste scandal? They called it Colgate.',
        part_kind='text',
      )
    ],
    model_name='function:model_logic',
    timestamp=datetime.datetime(...),
    kind='response',
  ),
  ModelRequest(
    parts=[
      UserPromptPart(
        content='Explain?',
        timestamp=datetime.datetime(...),
        part_kind='user-prompt',
      )
    ],
    kind='request',
  ),
  ModelResponse(
    parts=[
      TextPart(
        content='This is an excellent joke invented by Samuel Colvin, it needs no explanation.',
        part_kind='text',
      )
    ],
    model_name='function:model_logic',
    timestamp=datetime.datetime(...),
    kind='response',
  ),
]
"""

```


_(This example is complete, it can be run "as is")_

## Other ways of using messages

Since messages are defined by simple dataclasses, you can manually create and manipulate, e.g. for testing.

The message format is independent of the model used, so you can use messages in different agents, or the same agent with different models.

In the example below, we reuse the message from the first agent run, which uses the `openai:gpt-4o` model, in a second agent run using the `google-gla:gemini-1.5-pro` model.

Reusing messages with a different model```
from pydantic_ai import Agent
agent = Agent('openai:gpt-4o', system_prompt='Be a helpful assistant.')
result1 = agent.run_sync('Tell me a joke.')
print(result1.data)
#> Did you hear about the toothpaste scandal? They called it Colgate.
result2 = agent.run_sync(
  'Explain?',
  model='google-gla:gemini-1.5-pro',
  message_history=result1.new_messages(),
)
print(result2.data)
#> This is an excellent joke invented by Samuel Colvin, it needs no explanation.
print(result2.all_messages())
"""
[
  ModelRequest(
    parts=[
      SystemPromptPart(
        content='Be a helpful assistant.',
        dynamic_ref=None,
        part_kind='system-prompt',
      ),
      UserPromptPart(
        content='Tell me a joke.',
        timestamp=datetime.datetime(...),
        part_kind='user-prompt',
      ),
    ],
    kind='request',
  ),
  ModelResponse(
    parts=[
      TextPart(
        content='Did you hear about the toothpaste scandal? They called it Colgate.',
        part_kind='text',
      )
    ],
    model_name='function:model_logic',
    timestamp=datetime.datetime(...),
    kind='response',
  ),
  ModelRequest(
    parts=[
      UserPromptPart(
        content='Explain?',
        timestamp=datetime.datetime(...),
        part_kind='user-prompt',
      )
    ],
    kind='request',
  ),
  ModelResponse(
    parts=[
      TextPart(
        content='This is an excellent joke invented by Samuel Colvin, it needs no explanation.',
        part_kind='text',
      )
    ],
    model_name='function:model_logic',
    timestamp=datetime.datetime(...),
    kind='response',
  ),
]
"""

```


## Examples

For a more complete example of using messages in conversations, see the [chat app](../examples/chat-app/) example.

© Pydantic Services Inc. 2024 to present 
