---
url: https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#how-to-add-thread-level-persistence-functional-api)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to add thread-level persistence (functional API) 

[ ](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/?q= "Share")

Type to start searching

[ GitHub  ](https://github.com/langchain-ai/langgraph "Go to repository")

  * [ Home ](https://langchain-ai.github.io/langgraph/)
  * [ API reference ](https://langchain-ai.github.io/langgraph/reference/graphs/)



[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

[ GitHub  ](https://github.com/langchain-ai/langgraph "Go to repository")

  * [ Home  ](https://langchain-ai.github.io/langgraph/)

Home 
    * Get started  Get started 
      * [ Learn the basics  ](https://langchain-ai.github.io/langgraph/tutorials/introduction/)
      * [ Deployment  ](https://langchain-ai.github.io/langgraph/tutorials/deployment/)
    * Guides  Guides 
      * [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)

How-to Guides 
        * LangGraph  LangGraph 
          * [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
          * [ Graph API Basics  ](https://langchain-ai.github.io/langgraph/how-tos#graph-api-basics)
          * [ Controllability  ](https://langchain-ai.github.io/langgraph/how-tos#controllability)
          * Persistence  Persistence 
            * [ Persistence  ](https://langchain-ai.github.io/langgraph/how-tos#persistence)
            * [ How to add thread-level persistence to your graph  ](https://langchain-ai.github.io/langgraph/how-tos/persistence/)
            * [ How to add thread-level persistence to a subgraph  ](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/)
            * [ How to add cross-thread persistence to your graph  ](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/)
            * [ How to use Postgres checkpointer for persistence  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/)
            * [ How to use MongoDB checkpointer for persistence  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/)
            * [ How to create a custom checkpointer using Redis  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/)
            * How to add thread-level persistence (functional API)  [ How to add thread-level persistence (functional API)  ](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#setup)
              * [ Example: simple chatbot with short-term memory  ](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#example-simple-chatbot-with-short-term-memory)
            * [ How to add cross-thread persistence (functional API)  ](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/)
          * [ Memory  ](https://langchain-ai.github.io/langgraph/how-tos#memory)
          * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraph/how-tos#human-in-the-loop)
          * [ Streaming  ](https://langchain-ai.github.io/langgraph/how-tos#streaming)
          * [ Tool calling  ](https://langchain-ai.github.io/langgraph/how-tos#tool-calling)
          * [ Subgraphs  ](https://langchain-ai.github.io/langgraph/how-tos#subgraphs)
          * [ Multi-agent  ](https://langchain-ai.github.io/langgraph/how-tos#multi-agent)
          * [ State Management  ](https://langchain-ai.github.io/langgraph/how-tos#state-management)
          * [ Other  ](https://langchain-ai.github.io/langgraph/how-tos#other)
          * [ Prebuilt ReAct Agent  ](https://langchain-ai.github.io/langgraph/how-tos#prebuilt-react-agent)
        * [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph-platform)
      * [ Concepts  ](https://langchain-ai.github.io/langgraph/concepts/)
      * [ Tutorials  ](https://langchain-ai.github.io/langgraph/tutorials/)
    * Resources  Resources 
      * [ Prebuilt Agents  ](https://langchain-ai.github.io/langgraph/prebuilt/)
      * [ Adopters  ](https://langchain-ai.github.io/langgraph/adopters/)
      * [ FAQ  ](https://langchain-ai.github.io/langgraph/concepts/faq/)
      * [ Troubleshooting  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraph/reference/graphs/)



Table of contents 

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#setup)
  * [ Example: simple chatbot with short-term memory  ](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#example-simple-chatbot-with-short-term-memory)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Persistence  ](https://langchain-ai.github.io/langgraph/how-tos#persistence)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/persistence-functional.ipynb "Edit this page")

# How to add thread-level persistence (functional API)[¶](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#how-to-add-thread-level-persistence-functional-api "Permanent link")

Prerequisites

This guide assumes familiarity with the following:

  * [Functional API](https://langchain-ai.github.io/langgraph/concepts/functional_api/)
  * [Persistence](https://langchain-ai.github.io/langgraph/concepts/persistence/)
  * [Memory](https://langchain-ai.github.io/langgraph/concepts/memory/)
  * [Chat Models](https://python.langchain.com/docs/concepts/chat_models/)



Many AI applications need memory to share context across multiple interactions on the same [thread](https://langchain-ai.github.io/langgraph/concepts/persistence#threads) (e.g., multiple turns of a conversation). In LangGraph functional API, this kind of memory can be added to any [entrypoint()](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint) workflow using [thread-level persistence](https://langchain-ai.github.io/langgraph/concepts/persistence).

When creating a LangGraph workflow, you can set it up to persist its results by using a [checkpointer](https://langchain-ai.github.io/langgraph/reference/checkpoints/#basecheckpointsaver):

  1. Create an instance of a checkpointer:

```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-0-1)fromlanggraph.checkpoint.memoryimport MemorySaver
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-0-2)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-0-3)checkpointer = MemorySaver()    

```


API Reference: [MemorySaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.MemorySaver)

  2. Pass `checkpointer` instance to the `entrypoint()` decorator:

```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-1-1)fromlanggraph.funcimport entrypoint
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-1-2)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-1-3)@entrypoint(checkpointer=checkpointer)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-1-4)defworkflow(inputs)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-1-5)  ...

```


API Reference: [entrypoint](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint)

  3. Optionally expose `previous` parameter in the workflow function signature:

```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-2-1)@entrypoint(checkpointer=checkpointer)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-2-2)defworkflow(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-2-3)  inputs,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-2-4)  *,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-2-5)  # you can optionally specify `previous` in the workflow function signature
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-2-6)  # to access the return value from the workflow as of the last execution
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-2-7)  previous
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-2-8)):
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-2-9)  previous = previous or []
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-2-10)  combined_inputs = previous + inputs
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-2-11)  result = do_something(combined_inputs)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-2-12)  ...

```


  4. Optionally choose which values will be returned from the workflow and which will be saved by the checkpointer as `previous`:

```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-3-1)@entrypoint(checkpointer=checkpointer)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-3-2)defworkflow(inputs, *, previous):
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-3-3)  ...
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-3-4)  result = do_something(...)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-3-5)  return entrypoint.final(value=result, save=combine(inputs, result))

```





This guide shows how you can add thread-level persistence to your workflow.

Note

If you need memory that is **shared** across multiple conversations or users (cross-thread persistence), check out this [how-to guide](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional).

Note

If you need to add thread-level persistence to a `StateGraph`, check out this [how-to guide](https://langchain-ai.github.io/langgraph/how-tos/persistence).

## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#setup "Permanent link")

First we need to install the packages required

```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-4-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-4-2)%pip install --quiet -U langgraph langchain_anthropic

```


Next, we need to set API key for Anthropic (the LLM we will use).

```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-5-1)importgetpass
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-5-2)importos
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-5-3)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-5-4)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-5-5)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-5-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-5-7)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-5-8)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-5-9)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-5-10)_set_env("ANTHROPIC_API_KEY")

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Example: simple chatbot with short-term memory[¶](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#example-simple-chatbot-with-short-term-memory "Permanent link")

We will be using a workflow with a single task that calls a [chat model](https://python.langchain.com/docs/concepts/chat_models/).

Let's first define the model we'll be using:

```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-6-1)fromlangchain_anthropicimport ChatAnthropic
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-6-2)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-6-3)model = ChatAnthropic(model="claude-3-5-sonnet-latest")

```


API Reference: [ChatAnthropic](https://python.langchain.com/api_reference/anthropic/chat_models/langchain_anthropic.chat_models.ChatAnthropic.html)

Now we can define our task and workflow. To add in persistence, we need to pass in a [Checkpointer](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver) to the [entrypoint()](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint) decorator.

```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-7-1)fromlangchain_core.messagesimport BaseMessage
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-7-2)fromlanggraph.graphimport add_messages
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-7-3)fromlanggraph.funcimport entrypoint, task
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-7-4)fromlanggraph.checkpoint.memoryimport MemorySaver
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-7-5)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-7-6)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-7-7)@task
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-7-8)defcall_model(messages: list[BaseMessage]):
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-7-9)  response = model.invoke(messages)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-7-10)  return response
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-7-11)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-7-12)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-7-13)checkpointer = MemorySaver()
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-7-14)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-7-15)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-7-16)@entrypoint(checkpointer=checkpointer)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-7-17)defworkflow(inputs: list[BaseMessage], *, previous: list[BaseMessage]):
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-7-18)  if previous:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-7-19)    inputs = add_messages(previous, inputs)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-7-20)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-7-21)  response = call_model(inputs).result()
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-7-22)  return entrypoint.final(value=response, save=add_messages(inputs, response))

```


API Reference: [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html) | [add_messages](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.message.add_messages) | [entrypoint](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint) | [task](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.task) | [MemorySaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.MemorySaver)

If we try to use this workflow, the context of the conversation will be persisted across interactions:

Note

If you're using LangGraph Cloud or LangGraph Studio, you **don't need** to pass checkpointer to the entrypoint decorator, since it's done automatically.

We can now interact with the agent and see that it remembers previous messages!

```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-8-1)config = {"configurable": {"thread_id": "1"}}
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-8-2)input_message = {"role": "user", "content": "hi! I'm bob"}
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-8-3)for chunk in workflow.stream([input_message], config, stream_mode="values"):
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-8-4)  chunk.pretty_print()

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-9-1)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-9-2)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-9-3)Hi Bob! I'm Claude. Nice to meet you! How are you today?

```


You can always resume previous threads: 

```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-10-1)input_message = {"role": "user", "content": "what's my name?"}
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-10-2)for chunk in workflow.stream([input_message], config, stream_mode="values"):
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-10-3)  chunk.pretty_print()

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-11-1)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-11-2)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-11-3)Your name is Bob.

```


If we want to start a new conversation, we can pass in a different `thread_id`. Poof! All the memories are gone! 

```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-12-1)input_message = {"role": "user", "content": "what's my name?"}
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-12-2)for chunk in workflow.stream(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-12-3)  [input_message],
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-12-4)  {"configurable": {"thread_id": "2"}},
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-12-5)  stream_mode="values",
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-12-6)):
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-12-7)  chunk.pretty_print()

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-13-1)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-13-2)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__codelineno-13-3)I don't know your name unless you tell me. Each conversation I have starts fresh, so I don't have access to any previous interactions or personal information unless you share it with me.

```


Streaming tokens

If you would like to stream LLM tokens from your chatbot, you can use `stream_mode="messages"`. Check out this [how-to guide](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens) to learn more.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to create a custom checkpointer using Redis  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/) [ Next  How to add cross-thread persistence (functional API)  ](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
