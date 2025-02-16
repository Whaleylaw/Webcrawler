---
url: https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#how-to-add-cross-thread-persistence-to-your-graph)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to add cross-thread persistence to your graph 

[ ](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/?q= "Share")

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
            * How to add cross-thread persistence to your graph  [ How to add cross-thread persistence to your graph  ](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#setup)
              * [ Define store  ](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#define-store)
              * [ Create graph  ](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#create-graph)
              * [ Run the graph!  ](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#run-the-graph)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#setup)
  * [ Define store  ](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#define-store)
  * [ Create graph  ](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#create-graph)
  * [ Run the graph!  ](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#run-the-graph)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Persistence  ](https://langchain-ai.github.io/langgraph/how-tos#persistence)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/cross-thread-persistence.ipynb "Edit this page")

# How to add cross-thread persistence to your graph[¶](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#how-to-add-cross-thread-persistence-to-your-graph "Permanent link")

Prerequisites

This guide assumes familiarity with the following: 

  * [ Persistence ](https://langchain-ai.github.io/langgraph/concepts/persistence/)
  * [ Memory ](https://langchain-ai.github.io/langgraph/concepts/memory/)
  * [ Chat Models ](https://python.langchain.com/docs/concepts/#chat-models/)



In the [previous guide](https://langchain-ai.github.io/langgraph/how-tos/persistence/) you learned how to persist graph state across multiple interactions on a single [thread](). LangGraph also allows you to persist data across **multiple threads**. For instance, you can store information about users (their names or preferences) in a shared memory and reuse them in the new conversational threads.

In this guide, we will show how to construct and use a graph that has a shared memory implemented using the [Store](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore) interface.

Note

Support for the `Store[](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore)` API that is used in this guide was added in LangGraph `v0.2.32`. 

Support for **index** and **query** arguments of the `Store[](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore)` API that is used in this guide was added in LangGraph `v0.2.54`. 

## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#setup "Permanent link")

First, let's install the required packages and set our API keys

```
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-0-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-0-2)%pip install -U langchain_openai langgraph

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-1-1)importgetpass
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-1-2)importos
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-1-5)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-1-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-1-7)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-1-8)
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-1-10)_set_env("ANTHROPIC_API_KEY")
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-1-11)_set_env("OPENAI_API_KEY")

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com)

## Define store[¶](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#define-store "Permanent link")

In this example we will create a graph that will be able to retrieve information about a user's preferences. We will do so by defining an `InMemoryStore` - an object that can store data in memory and query that data. We will then pass the store object when compiling the graph. This allows each node in the graph to access the store: when you define node functions, you can define `store` keyword argument, and LangGraph will automatically pass the store object you compiled the graph with.

When storing objects using the `Store` interface you define two things:

  * the namespace for the object, a tuple (similar to directories)
  * the object key (similar to filenames)



In our example, we'll be using `("memories", <user_id>)` as namespace and random UUID as key for each new memory.

Importantly, to determine the user, we will be passing `user_id` via the config keyword argument of the node function.

Let's first define an `InMemoryStore` already populated with some memories about the users.

```
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-2-1)fromlanggraph.store.memoryimport InMemoryStore
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-2-2)fromlangchain_openaiimport OpenAIEmbeddings
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-2-3)
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-2-4)in_memory_store = InMemoryStore(
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-2-5)  index={
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-2-6)    "embed": OpenAIEmbeddings(model="text-embedding-3-small"),
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-2-7)    "dims": 1536,
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-2-8)  }
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-2-9))

```


API Reference: [OpenAIEmbeddings](https://python.langchain.com/api_reference/openai/embeddings/langchain_openai.embeddings.base.OpenAIEmbeddings.html)

## Create graph[¶](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#create-graph "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-3-1)importuuid
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-3-2)fromtypingimport Annotated
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-3-3)fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-3-4)
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-3-5)fromlangchain_anthropicimport ChatAnthropic
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-3-6)fromlangchain_core.runnablesimport RunnableConfig
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-3-7)fromlanggraph.graphimport StateGraph, MessagesState, START
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-3-8)fromlanggraph.checkpoint.memoryimport MemorySaver
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-3-9)fromlanggraph.store.baseimport BaseStore
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-3-10)
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-3-11)
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-3-12)model = ChatAnthropic(model="claude-3-5-sonnet-20240620")
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-3-13)
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-3-14)
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-3-15)# NOTE: we're passing the Store param to the node --
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-3-16)# this is the Store we compile the graph with
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-3-17)defcall_model(state: MessagesState, config: RunnableConfig, *, store: BaseStore):
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-3-18)  user_id = config["configurable"]["user_id"]
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-3-19)  namespace = ("memories", user_id)
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-3-20)  memories = store.search(namespace, query=str(state["messages"][-1].content))
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-3-21)  info = "\n".join([d.value["data"] for d in memories])
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-3-22)  system_msg = f"You are a helpful assistant talking to the user. User info: {info}"
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-3-23)
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-3-24)  # Store new memories if the user asks the model to remember
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-3-25)  last_message = state["messages"][-1]
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-3-26)  if "remember" in last_message.content.lower():
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-3-27)    memory = "User name is Bob"
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-3-28)    store.put(namespace, str(uuid.uuid4()), {"data": memory})
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-3-29)
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-3-30)  response = model.invoke(
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-3-31)    [{"role": "system", "content": system_msg}] + state["messages"]
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-3-32)  )
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-3-33)  return {"messages": response}
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-3-34)
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-3-35)
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-3-36)builder = StateGraph(MessagesState)
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-3-37)builder.add_node("call_model", call_model)
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-3-38)builder.add_edge(START, "call_model")
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-3-39)
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-3-40)# NOTE: we're passing the store object here when compiling the graph
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-3-41)graph = builder.compile(checkpointer=MemorySaver(), store=in_memory_store)
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-3-42)# If you're using LangGraph Cloud or LangGraph Studio, you don't need to pass the store or checkpointer when compiling the graph, since it's done automatically.

```


API Reference: [ChatAnthropic](https://python.langchain.com/api_reference/anthropic/chat_models/langchain_anthropic.chat_models.ChatAnthropic.html) | [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [MemorySaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.MemorySaver)

Note

If you're using LangGraph Cloud or LangGraph Studio, you **don't need** to pass store when compiling the graph, since it's done automatically. 

## Run the graph![¶](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#run-the-graph "Permanent link")

Now let's specify a user ID in the config and tell the model our name:

```
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-4-1)config = {"configurable": {"thread_id": "1", "user_id": "1"}}
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-4-2)input_message = {"role": "user", "content": "Hi! Remember: my name is Bob"}
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-4-3)for chunk in graph.stream({"messages": [input_message]}, config, stream_mode="values"):
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-4-4)  chunk["messages"][-1].pretty_print()

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-5-1)================================[1m Human Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-5-2)
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-5-3)Hi! Remember: my name is Bob
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-5-4)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-5-5)
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-5-6)Hello Bob! It's nice to meet you. I'll remember that your name is Bob. How can I assist you today?

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-6-1)config = {"configurable": {"thread_id": "2", "user_id": "1"}}
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-6-2)input_message = {"role": "user", "content": "what is my name?"}
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-6-3)for chunk in graph.stream({"messages": [input_message]}, config, stream_mode="values"):
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-6-4)  chunk["messages"][-1].pretty_print()

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-7-1)================================[1m Human Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-7-2)
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-7-3)what is my name?
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-7-4)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-7-5)
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-7-6)Your name is Bob.

```


We can now inspect our in-memory store and verify that we have in fact saved the memories for the user: 

```
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-8-1)for memory in in_memory_store.search(("memories", "1")):
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-8-2)  print(memory.value)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-9-1){'data': 'User name is Bob'}

```


Let's now run the graph for another user to verify that the memories about the first user are self contained: 

```
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-10-1)config = {"configurable": {"thread_id": "3", "user_id": "2"}}
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-10-2)input_message = {"role": "user", "content": "what is my name?"}
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-10-3)for chunk in graph.stream({"messages": [input_message]}, config, stream_mode="values"):
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-10-4)  chunk["messages"][-1].pretty_print()

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-11-1)================================[1m Human Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-11-2)
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-11-3)what is my name?
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-11-4)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-11-5)
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__codelineno-11-6)I apologize, but I don't have any information about your name. As an AI assistant, I don't have access to personal information about users unless it has been specifically shared in our conversation. If you'd like, you can tell me your name and I'll be happy to use it in our discussion.

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to add thread-level persistence to a subgraph  ](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/) [ Next  How to use Postgres checkpointer for persistence  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
