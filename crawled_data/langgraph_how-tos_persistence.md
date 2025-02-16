---
url: https://langchain-ai.github.io/langgraph/how-tos/persistence/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/persistence/#how-to-add-thread-level-persistence-to-your-graph)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to add thread-level persistence to your graph 

[ ](https://langchain-ai.github.io/langgraph/how-tos/persistence/?q= "Share")

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
            * How to add thread-level persistence to your graph  [ How to add thread-level persistence to your graph  ](https://langchain-ai.github.io/langgraph/how-tos/persistence/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/persistence/#setup)
              * [ Define graph  ](https://langchain-ai.github.io/langgraph/how-tos/persistence/#define-graph)
              * [ Add persistence  ](https://langchain-ai.github.io/langgraph/how-tos/persistence/#add-persistence)
            * [ How to add thread-level persistence to a subgraph  ](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/)
            * [ How to add cross-thread persistence to your graph  ](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/)
            * [ How to use Postgres checkpointer for persistence  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/)
            * [ How to use MongoDB checkpointer for persistence  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/)
            * [ How to create a custom checkpointer using Redis  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/)
            * [ How to add thread-level persistence (functional API)  ](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/persistence/#setup)
  * [ Define graph  ](https://langchain-ai.github.io/langgraph/how-tos/persistence/#define-graph)
  * [ Add persistence  ](https://langchain-ai.github.io/langgraph/how-tos/persistence/#add-persistence)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Persistence  ](https://langchain-ai.github.io/langgraph/how-tos#persistence)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/persistence.ipynb "Edit this page")

# How to add thread-level persistence to your graph[¶](https://langchain-ai.github.io/langgraph/how-tos/persistence/#how-to-add-thread-level-persistence-to-your-graph "Permanent link")

Prerequisites

This guide assumes familiarity with the following: 

  * [ Persistence ](https://langchain-ai.github.io/langgraph/concepts/persistence/)
  * [ Memory ](https://langchain-ai.github.io/langgraph/concepts/memory/)
  * [ Chat Models ](https://python.langchain.com/docs/concepts/#chat-models/)



Many AI applications need memory to share context across multiple interactions. In LangGraph, this kind of memory can be added to any [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.StateGraph) using [thread-level persistence](https://langchain-ai.github.io/langgraph/concepts/persistence) .

When creating any LangGraph graph, you can set it up to persist its state by adding a [checkpointer](https://langchain-ai.github.io/langgraph/reference/checkpoints/#basecheckpointsaver) when compiling the graph:

```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-0-1)fromlanggraph.checkpoint.memoryimport MemorySaver
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-0-2)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-0-3)checkpointer = MemorySaver()
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-0-4)graph.compile(checkpointer=checkpointer)

```


API Reference: [MemorySaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.MemorySaver)

This guide shows how you can add thread-level persistence to your graph.

Note

If you need memory that is **shared** across multiple conversations or users (cross-thread persistence), check out this [how-to guide](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/). 

## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/persistence/#setup "Permanent link")

First we need to install the packages required

```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-1-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-1-2)%pip install --quiet -U langgraph langchain_anthropic

```


Next, we need to set API key for Anthropic (the LLM we will use).

```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-2-1)importgetpass
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-2-2)importos
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-2-3)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-2-4)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-2-5)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-2-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-2-7)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-2-8)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-2-9)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-2-10)_set_env("ANTHROPIC_API_KEY")

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-3-1)ANTHROPIC_API_KEY: ········

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Define graph[¶](https://langchain-ai.github.io/langgraph/how-tos/persistence/#define-graph "Permanent link")

We will be using a single-node graph that calls a [chat model](https://python.langchain.com/docs/concepts/#chat-models).

Let's first define the model we'll be using:

```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-4-1)fromlangchain_anthropicimport ChatAnthropic
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-4-2)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-4-3)model = ChatAnthropic(model="claude-3-5-sonnet-20240620")

```


API Reference: [ChatAnthropic](https://python.langchain.com/api_reference/anthropic/chat_models/langchain_anthropic.chat_models.ChatAnthropic.html)

Now we can define our `StateGraph` and add our model-calling node:

```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-5-1)fromtypingimport Annotated
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-5-2)fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-5-3)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-5-4)fromlanggraph.graphimport StateGraph, MessagesState, START
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-5-5)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-5-6)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-5-7)defcall_model(state: MessagesState):
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-5-8)  response = model.invoke(state["messages"])
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-5-9)  return {"messages": response}
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-5-10)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-5-11)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-5-12)builder = StateGraph(MessagesState)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-5-13)builder.add_node("call_model", call_model)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-5-14)builder.add_edge(START, "call_model")
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-5-15)graph = builder.compile()

```


API Reference: [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START)

If we try to use this graph, the context of the conversation will not be persisted across interactions:

```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-6-1)input_message = {"role": "user", "content": "hi! I'm bob"}
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-6-2)for chunk in graph.stream({"messages": [input_message]}, stream_mode="values"):
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-6-3)  chunk["messages"][-1].pretty_print()
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-6-4)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-6-5)input_message = {"role": "user", "content": "what's my name?"}
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-6-6)for chunk in graph.stream({"messages": [input_message]}, stream_mode="values"):
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-6-7)  chunk["messages"][-1].pretty_print()

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-7-1)================================[1m Human Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-7-2)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-7-3)hi! I'm bob
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-7-4)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-7-5)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-7-6)Hello Bob! It's nice to meet you. How are you doing today? Is there anything I can help you with or would you like to chat about something in particular?
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-7-7)================================[1m Human Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-7-8)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-7-9)what's my name?
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-7-10)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-7-11)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-7-12)I apologize, but I don't have access to your personal information, including your name. I'm an AI language model designed to provide general information and answer questions to the best of my ability based on my training data. I don't have any information about individual users or their personal details. If you'd like to share your name, you're welcome to do so, but I won't be able to recall it in future conversations.

```


## Add persistence[¶](https://langchain-ai.github.io/langgraph/how-tos/persistence/#add-persistence "Permanent link")

To add in persistence, we need to pass in a [Checkpointer](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver) when compiling the graph.

```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-8-1)fromlanggraph.checkpoint.memoryimport MemorySaver
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-8-2)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-8-3)memory = MemorySaver()
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-8-4)graph = builder.compile(checkpointer=memory)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-8-5)# If you're using LangGraph Cloud or LangGraph Studio, you don't need to pass the checkpointer when compiling the graph, since it's done automatically.

```


API Reference: [MemorySaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.MemorySaver)

Note

If you're using LangGraph Cloud or LangGraph Studio, you **don't need** to pass checkpointer when compiling the graph, since it's done automatically. 

We can now interact with the agent and see that it remembers previous messages!

```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-9-1)config = {"configurable": {"thread_id": "1"}}
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-9-2)input_message = {"role": "user", "content": "hi! I'm bob"}
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-9-3)for chunk in graph.stream({"messages": [input_message]}, config, stream_mode="values"):
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-9-4)  chunk["messages"][-1].pretty_print()

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-10-1)================================[1m Human Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-10-2)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-10-3)hi! I'm bob
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-10-4)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-10-5)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-10-6)Hello Bob! It's nice to meet you. How are you doing today? Is there anything in particular you'd like to chat about or any questions you have that I can help you with?

```


You can always resume previous threads: 

```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-11-1)input_message = {"role": "user", "content": "what's my name?"}
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-11-2)for chunk in graph.stream({"messages": [input_message]}, config, stream_mode="values"):
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-11-3)  chunk["messages"][-1].pretty_print()

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-12-1)================================[1m Human Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-12-2)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-12-3)what's my name?
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-12-4)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-12-5)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-12-6)Your name is Bob, as you introduced yourself at the beginning of our conversation.

```


If we want to start a new conversation, we can pass in a different `thread_id`. Poof! All the memories are gone! 

```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-13-1)input_message = {"role": "user", "content": "what's my name?"}
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-13-2)for chunk in graph.stream(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-13-3)  {"messages": [input_message]},
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-13-4)  {"configurable": {"thread_id": "2"}},
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-13-5)  stream_mode="values",
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-13-6)):
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-13-7)  chunk["messages"][-1].pretty_print()

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-14-1)================================[1m Human Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-14-2)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-14-3)what's is my name?
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-14-4)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-14-5)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__codelineno-14-6)I apologize, but I don't have access to your personal information, including your name. As an AI language model, I don't have any information about individual users unless it's provided within the conversation. If you'd like to share your name, you're welcome to do so, but otherwise, I won't be able to know or guess it.

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to return state before hitting recursion limit  ](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/) [ Next  How to add thread-level persistence to a subgraph  ](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/persistence/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
