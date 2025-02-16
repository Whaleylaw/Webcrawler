---
url: https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#how-to-add-cross-thread-persistence-functional-api)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to add cross-thread persistence (functional API) 

[ ](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/?q= "Share")

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
            * [ How to add thread-level persistence (functional API)  ](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/)
            * How to add cross-thread persistence (functional API)  [ How to add cross-thread persistence (functional API)  ](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#setup)
              * [ Example: simple chatbot with long-term memory  ](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#example-simple-chatbot-with-long-term-memory)
                * [ Define store  ](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#define-store)
                * [ Create workflow  ](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#create-workflow)
                * [ Run the workflow!  ](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#run-the-workflow)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#setup)
  * [ Example: simple chatbot with long-term memory  ](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#example-simple-chatbot-with-long-term-memory)
    * [ Define store  ](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#define-store)
    * [ Create workflow  ](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#create-workflow)
    * [ Run the workflow!  ](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#run-the-workflow)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Persistence  ](https://langchain-ai.github.io/langgraph/how-tos#persistence)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/cross-thread-persistence-functional.ipynb "Edit this page")

# How to add cross-thread persistence (functional API)[¶](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#how-to-add-cross-thread-persistence-functional-api "Permanent link")

Prerequisites

This guide assumes familiarity with the following:

  * [Functional API](https://langchain-ai.github.io/langgraph/concepts/functional_api/)
  * [Persistence](https://langchain-ai.github.io/langgraph/concepts/persistence/)
  * [Memory](https://langchain-ai.github.io/langgraph/concepts/memory/)
  * [Chat Models](https://python.langchain.com/docs/concepts/chat_models/)



LangGraph allows you to persist data across **different[threads](https://langchain-ai.github.io/langgraph/concepts/persistence/#threads)**. For instance, you can store information about users (their names or preferences) in a shared (cross-thread) memory and reuse them in the new threads (e.g., new conversations).

When using the [functional API](https://langchain-ai.github.io/langgraph/concepts/functional_api/), you can set it up to store and retrieve memories by using the [Store](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore) interface:

  1. Create an instance of a `Store`

```
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-0-1)fromlanggraph.store.memoryimport InMemoryStore, BaseStore
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-0-2)
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-0-3)store = InMemoryStore()

```


  2. Pass the `store` instance to the `entrypoint()` decorator and expose `store` parameter in the function signature:

```
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-1-1)fromlanggraph.funcimport entrypoint
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-1-2)
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-1-3)@entrypoint(store=store)
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-1-4)defworkflow(inputs: dict, store: BaseStore):
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-1-5)  my_task(inputs).result()
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-1-6)  ...

```


API Reference: [entrypoint](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint)




In this guide, we will show how to construct and use a workflow that has a shared memory implemented using the [Store](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore) interface.

Note

Support for the `Store`[](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore) API that is used in this guide was added in LangGraph `v0.2.32`.

Support for **index** and **query** arguments of the `Store`[](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore) API that is used in this guide was added in LangGraph `v0.2.54`.

Note

If you need to add cross-thread persistence to a `StateGraph`, check out this [how-to guide](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence).

## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#setup "Permanent link")

First, let's install the required packages and set our API keys

```
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-2-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-2-2)%pip install -U langchain_anthropic langchain_openai langgraph

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-3-1)importgetpass
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-3-2)importos
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-3-3)
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-3-4)
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-3-5)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-3-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-3-7)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-3-8)
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-3-9)
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-3-10)_set_env("ANTHROPIC_API_KEY")
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-3-11)_set_env("OPENAI_API_KEY")

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com)

## Example: simple chatbot with long-term memory[¶](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#example-simple-chatbot-with-long-term-memory "Permanent link")

### Define store[¶](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#define-store "Permanent link")

In this example we will create a workflow that will be able to retrieve information about a user's preferences. We will do so by defining an `InMemoryStore` - an object that can store data in memory and query that data.

When storing objects using the `Store` interface you define two things:

  * the namespace for the object, a tuple (similar to directories)
  * the object key (similar to filenames)



In our example, we'll be using `("memories", <user_id>)` as namespace and random UUID as key for each new memory.

Importantly, to determine the user, we will be passing `user_id` via the config keyword argument of the node function.

Let's first define our store!

```
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-4-1)fromlanggraph.store.memoryimport InMemoryStore
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-4-2)fromlangchain_openaiimport OpenAIEmbeddings
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-4-3)
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-4-4)in_memory_store = InMemoryStore(
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-4-5)  index={
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-4-6)    "embed": OpenAIEmbeddings(model="text-embedding-3-small"),
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-4-7)    "dims": 1536,
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-4-8)  }
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-4-9))

```


API Reference: [OpenAIEmbeddings](https://python.langchain.com/api_reference/openai/embeddings/langchain_openai.embeddings.base.OpenAIEmbeddings.html)

### Create workflow[¶](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#create-workflow "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-5-1)importuuid
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-5-2)
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-5-3)fromlangchain_anthropicimport ChatAnthropic
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-5-4)fromlangchain_core.runnablesimport RunnableConfig
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-5-5)fromlangchain_core.messagesimport BaseMessage
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-5-6)fromlanggraph.funcimport entrypoint, task
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-5-7)fromlanggraph.graphimport add_messages
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-5-8)fromlanggraph.checkpoint.memoryimport MemorySaver
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-5-9)fromlanggraph.store.baseimport BaseStore
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-5-10)
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-5-11)
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-5-12)model = ChatAnthropic(model="claude-3-5-sonnet-latest")
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-5-13)
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-5-14)
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-5-15)@task
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-5-16)defcall_model(messages: list[BaseMessage], memory_store: BaseStore, user_id: str):
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-5-17)  namespace = ("memories", user_id)
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-5-18)  last_message = messages[-1]
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-5-19)  memories = memory_store.search(namespace, query=str(last_message.content))
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-5-20)  info = "\n".join([d.value["data"] for d in memories])
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-5-21)  system_msg = f"You are a helpful assistant talking to the user. User info: {info}"
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-5-22)
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-5-23)  # Store new memories if the user asks the model to remember
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-5-24)  if "remember" in last_message.content.lower():
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-5-25)    memory = "User name is Bob"
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-5-26)    memory_store.put(namespace, str(uuid.uuid4()), {"data": memory})
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-5-27)
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-5-28)  response = model.invoke([{"role": "system", "content": system_msg}] + messages)
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-5-29)  return response
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-5-30)
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-5-31)
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-5-32)# NOTE: we're passing the store object here when creating a workflow via entrypoint()
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-5-33)@entrypoint(checkpointer=MemorySaver(), store=in_memory_store)
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-5-34)defworkflow(
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-5-35)  inputs: list[BaseMessage],
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-5-36)  *,
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-5-37)  previous: list[BaseMessage],
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-5-38)  config: RunnableConfig,
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-5-39)  store: BaseStore,
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-5-40)):
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-5-41)  user_id = config["configurable"]["user_id"]
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-5-42)  previous = previous or []
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-5-43)  inputs = add_messages(previous, inputs)
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-5-44)  response = call_model(inputs, store, user_id).result()
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-5-45)  return entrypoint.final(value=response, save=add_messages(inputs, response))

```


API Reference: [ChatAnthropic](https://python.langchain.com/api_reference/anthropic/chat_models/langchain_anthropic.chat_models.ChatAnthropic.html) | [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html) | [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html) | [entrypoint](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint) | [task](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.task) | [add_messages](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.message.add_messages) | [MemorySaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.MemorySaver)

Note

If you're using LangGraph Cloud or LangGraph Studio, you **don't need** to pass store to the entrypoint decorator, since it's done automatically.

### Run the workflow![¶](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#run-the-workflow "Permanent link")

Now let's specify a user ID in the config and tell the model our name:

```
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-6-1)config = {"configurable": {"thread_id": "1", "user_id": "1"}}
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-6-2)input_message = {"role": "user", "content": "Hi! Remember: my name is Bob"}
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-6-3)for chunk in workflow.stream([input_message], config, stream_mode="values"):
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-6-4)  chunk.pretty_print()

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-7-1)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-7-2)
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-7-3)Hello Bob! Nice to meet you. I'll remember that your name is Bob. How can I help you today?

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-8-1)config = {"configurable": {"thread_id": "2", "user_id": "1"}}
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-8-2)input_message = {"role": "user", "content": "what is my name?"}
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-8-3)for chunk in workflow.stream([input_message], config, stream_mode="values"):
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-8-4)  chunk.pretty_print()

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-9-1)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-9-2)
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-9-3)Your name is Bob.

```


We can now inspect our in-memory store and verify that we have in fact saved the memories for the user: 

```
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-10-1)for memory in in_memory_store.search(("memories", "1")):
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-10-2)  print(memory.value)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-11-1){'data': 'User name is Bob'}

```


Let's now run the workflow for another user to verify that the memories about the first user are self contained: 

```
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-12-1)config = {"configurable": {"thread_id": "3", "user_id": "2"}}
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-12-2)input_message = {"role": "user", "content": "what is my name?"}
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-12-3)for chunk in workflow.stream([input_message], config, stream_mode="values"):
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-12-4)  chunk.pretty_print()

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-13-1)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-13-2)
[](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__codelineno-13-3)I don't have any information about your name. I can only see our current conversation without any prior context or personal details about you. If you'd like me to know your name, feel free to tell me!

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to add thread-level persistence (functional API)  ](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/) [ Next  How to manage conversation history  ](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
