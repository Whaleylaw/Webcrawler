---
url: https://langchain-ai.github.io/langgraph/reference/config/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/reference/config/#langgraph.config.get_store)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Config 

[ ](https://langchain-ai.github.io/langgraph/reference/config/?q= "Share")

Type to start searching

[ GitHub  ](https://github.com/langchain-ai/langgraph "Go to repository")

  * [ Home ](https://langchain-ai.github.io/langgraph/)
  * [ API reference ](https://langchain-ai.github.io/langgraph/reference/graphs/)



[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

[ GitHub  ](https://github.com/langchain-ai/langgraph "Go to repository")

  * [ Home  ](https://langchain-ai.github.io/langgraph/)
  * API reference  API reference 
    * Library  Library 
      * [ Graphs  ](https://langchain-ai.github.io/langgraph/reference/graphs/)
      * [ Checkpointing  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/)
      * [ Storage  ](https://langchain-ai.github.io/langgraph/reference/store/)
      * [ Prebuilt components  ](https://langchain-ai.github.io/langgraph/reference/prebuilt/)
      * [ Channels  ](https://langchain-ai.github.io/langgraph/reference/channels/)
      * [ Errors  ](https://langchain-ai.github.io/langgraph/reference/errors/)
      * [ Types  ](https://langchain-ai.github.io/langgraph/reference/types/)
      * [ Constants  ](https://langchain-ai.github.io/langgraph/reference/constants/)
      * [ Pregel  ](https://langchain-ai.github.io/langgraph/reference/pregel/)
      * Config  [ Config  ](https://langchain-ai.github.io/langgraph/reference/config/) Table of contents 
        * [ get_store  ](https://langchain-ai.github.io/langgraph/reference/config/#langgraph.config.get_store)
        * [ get_stream_writer  ](https://langchain-ai.github.io/langgraph/reference/config/#langgraph.config.get_stream_writer)
      * [ Functional API  ](https://langchain-ai.github.io/langgraph/reference/func/)
    * LangGraph Platform  LangGraph Platform 
      * [ Server API  ](https://langchain-ai.github.io/langgraph/cloud/reference/api/api_ref/)
      * [ CLI  ](https://langchain-ai.github.io/langgraph/cloud/reference/cli/)
      * [ SDK (Python)  ](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/)
      * [ SDK (JS/TS)  ](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/)
      * [ RemoteGraph  ](https://langchain-ai.github.io/langgraph/reference/remote_graph/)
      * [ Environment variables  ](https://langchain-ai.github.io/langgraph/cloud/reference/env_var/)



Table of contents 

  * [ get_store  ](https://langchain-ai.github.io/langgraph/reference/config/#langgraph.config.get_store)
  * [ get_stream_writer  ](https://langchain-ai.github.io/langgraph/reference/config/#langgraph.config.get_stream_writer)



  1. [ API reference  ](https://langchain-ai.github.io/langgraph/reference/graphs/)
  2. [ Library  ](https://langchain-ai.github.io/langgraph/reference/graphs/)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/reference/config.md "Edit this page")

# Config

##  `get_store() -> BaseStore` [¶](https://langchain-ai.github.io/langgraph/reference/config/#langgraph.config.get_store "Permanent link")

Access LangGraph store from inside a graph node or entrypoint task at runtime.

Can be called from inside any [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) node or functional API [task](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.task), as long as the StateGraph or the [entrypoint](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint) was initialized with a store, e.g.:

```
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-1)# with StateGraph
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-2)graph = (
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-3)  StateGraph(...)
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-4)  ...
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-5)  .compile(store=store)
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-6))
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-7)
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-8)# or with entrypoint
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-9)@entrypoint(store=store)
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-10)defworkflow(inputs):
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-11)  ...

```


Async with Python < 3.11

If you are using Python < 3.11 and are running LangGraph asynchronously, `get_store()` won't work since it uses [contextvar](https://docs.python.org/3/library/contextvars.html) propagation (only available in [Python >= 3.11](https://docs.python.org/3/library/asyncio-task.html#asyncio.create_task)).

Using with StateGraph

```
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-1)fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-2)fromlanggraph.graphimport StateGraph, START
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-3)fromlanggraph.store.memoryimport InMemoryStore
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-4)fromlanggraph.configimport get_store
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-5)
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-6)store = InMemoryStore()
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-7)store.put(("values",), "foo", {"bar": 2})
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-8)
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-9)classState(TypedDict):
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-10)  foo: int
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-11)
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-12)defmy_node(state: State):
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-13)  my_store = get_store()
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-14)  stored_value = my_store.get(("values",), "foo").value["bar"]
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-15)  return {"foo": stored_value + 1}
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-16)
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-17)graph = (
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-18)  StateGraph(State)
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-19)  .add_node(my_node)
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-20)  .add_edge(START, "my_node")
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-21)  .compile(store=store)
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-22))
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-23)
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-24)graph.invoke({"foo": 1})

```


```
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-1-1){'foo': 3}

```


Using with functional API

```
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-1)fromlanggraph.funcimport entrypoint, task
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-2)fromlanggraph.store.memoryimport InMemoryStore
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-3)fromlanggraph.configimport get_store
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-4)
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-5)store = InMemoryStore()
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-6)store.put(("values",), "foo", {"bar": 2})
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-7)
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-8)@task
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-9)defmy_task(value: int):
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-10)  my_store = get_store()
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-11)  stored_value = my_store.get(("values",), "foo").value["bar"]
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-12)  return stored_value + 1
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-13)
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-14)@entrypoint(store=store)
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-15)defworkflow(value: int):
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-16)  return my_task(value).result()
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-17)
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-18)workflow.invoke(1)

```


```
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-1-1)3

```


##  `get_stream_writer() -> StreamWriter` [¶](https://langchain-ai.github.io/langgraph/reference/config/#langgraph.config.get_stream_writer "Permanent link")

Access LangGraph [StreamWriter](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.StreamWriter) from inside a graph node or entrypoint task at runtime.

Can be called from inside any [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) node or functional API [task](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.task).

Async with Python < 3.11

If you are using Python < 3.11 and are running LangGraph asynchronously, `get_stream_writer()` won't work since it uses [contextvar](https://docs.python.org/3/library/contextvars.html) propagation (only available in [Python >= 3.11](https://docs.python.org/3/library/asyncio-task.html#asyncio.create_task)).

Using with StateGraph

```
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-1)fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-2)fromlanggraph.graphimport StateGraph, START
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-3)fromlanggraph.configimport get_stream_writer
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-4)
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-5)classState(TypedDict):
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-6)  foo: int
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-7)
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-8)defmy_node(state: State):
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-9)  my_stream_writer = get_stream_writer()
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-10)  my_stream_writer({"custom_data": "Hello!"})
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-11)  return {"foo": state["foo"] + 1}
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-12)
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-13)graph = (
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-14)  StateGraph(State)
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-15)  .add_node(my_node)
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-16)  .add_edge(START, "my_node")
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-17)  .compile(store=store)
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-18))
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-19)
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-20)for chunk in graph.stream({"foo": 1}, stream_mode="custom"):
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-21)  print(chunk)

```


```
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-1-1){'custom_data': 'Hello!'}

```


Using with functional API

```
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-1)fromlanggraph.funcimport entrypoint, task
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-2)fromlanggraph.configimport get_stream_writer
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-3)
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-4)@task
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-5)defmy_task(value: int):
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-6)  my_stream_writer = get_stream_writer()
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-7)  my_stream_writer({"custom_data": "Hello!"})
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-8)  return value + 1
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-9)
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-10)@entrypoint(store=store)
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-11)defworkflow(value: int):
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-12)  return my_task(value).result()
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-13)
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-14)for chunk in workflow.stream(1, stream_mode="custom"):
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-0-15)  print(chunk)

```


```
[](https://langchain-ai.github.io/langgraph/reference/config/#__codelineno-1-1){'custom_data': 'Hello!'}

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Pregel  ](https://langchain-ai.github.io/langgraph/reference/pregel/) [ Next  Functional API  ](https://langchain-ai.github.io/langgraph/reference/func/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/reference/config/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
