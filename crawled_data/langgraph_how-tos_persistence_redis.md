---
url: https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#how-to-create-a-custom-checkpointer-using-redis)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to create a custom checkpointer using Redis 

[ ](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/?q= "Share")

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
            * How to create a custom checkpointer using Redis  [ How to create a custom checkpointer using Redis  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#setup)
              * [ Checkpointer implementation  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#checkpointer-implementation)
                * [ Define imports and helper functions  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#define-imports-and-helper-functions)
                * [ RedisSaver  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#redissaver)
                * [ AsyncRedis  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#asyncredis)
              * [ Setup model and tools for the graph  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#setup-model-and-tools-for-the-graph)
              * [ Use sync connection  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#use-sync-connection)
              * [ Use async connection  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#use-async-connection)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#setup)
  * [ Checkpointer implementation  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#checkpointer-implementation)
    * [ Define imports and helper functions  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#define-imports-and-helper-functions)
    * [ RedisSaver  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#redissaver)
    * [ AsyncRedis  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#asyncredis)
  * [ Setup model and tools for the graph  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#setup-model-and-tools-for-the-graph)
  * [ Use sync connection  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#use-sync-connection)
  * [ Use async connection  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#use-async-connection)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Persistence  ](https://langchain-ai.github.io/langgraph/how-tos#persistence)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/persistence_redis.ipynb "Edit this page")

# How to create a custom checkpointer using Redis[¶](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#how-to-create-a-custom-checkpointer-using-redis "Permanent link")

Prerequisites

This guide assumes familiarity with the following: 

  * [ Persistence ](https://langchain-ai.github.io/langgraph/concepts/persistence/)
  * [ Redis ](https://redis.io/)



When creating LangGraph agents, you can also set them up so that they persist their state. This allows you to do things like interact with an agent multiple times and have it remember previous interactions.

This reference implementation shows how to use Redis as the backend for persisting checkpoint state. Make sure that you have Redis running on port `6379` for going through this guide.

Note

This is a **reference** implementation. You can implement your own checkpointer using a different database or modify this one as long as it conforms to the [BaseCheckpointSaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver) interface. 

For demonstration purposes we add persistence to the [pre-built create react agent](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent).

In general, you can add a checkpointer to any custom graph that you build like this:

```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-0-1)fromlanggraph.graphimport StateGraph
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-0-2)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-0-3)builder = StateGraph(....)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-0-4)# ... define the graph
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-0-5)checkpointer = # redis checkpointer (see examples below)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-0-6)graph = builder.compile(checkpointer=checkpointer)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-0-7)...

```


API Reference: [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph)

## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#setup "Permanent link")

First, let's install the required packages and set our API keys

```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-1-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-1-2)%pip install -U redis langgraph langchain_openai

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-2-1)importgetpass
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-2-2)importos
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-2-3)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-2-4)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-2-5)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-2-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-2-7)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-2-8)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-2-9)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-2-10)_set_env("OPENAI_API_KEY")

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Checkpointer implementation[¶](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#checkpointer-implementation "Permanent link")

### Define imports and helper functions[¶](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#define-imports-and-helper-functions "Permanent link")

First, let's define some imports and shared utilities for both `RedisSaver` and `AsyncRedisSaver`

```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-1)"""Implementation of a langgraph checkpoint saver using Redis."""
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-2)fromcontextlibimport asynccontextmanager, contextmanager
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-3)fromtypingimport (
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-4)  Any,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-5)  AsyncGenerator,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-6)  AsyncIterator,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-7)  Iterator,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-8)  List,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-9)  Optional,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-10)  Tuple,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-11))
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-12)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-13)fromlangchain_core.runnablesimport RunnableConfig
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-14)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-15)fromlanggraph.checkpoint.baseimport (
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-16)  WRITES_IDX_MAP,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-17)  BaseCheckpointSaver,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-18)  ChannelVersions,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-19)  Checkpoint,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-20)  CheckpointMetadata,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-21)  CheckpointTuple,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-22)  PendingWrite,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-23)  get_checkpoint_id,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-24))
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-25)fromlanggraph.checkpoint.serde.baseimport SerializerProtocol
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-26)fromredisimport Redis
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-27)fromredis.asyncioimport Redis as AsyncRedis
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-28)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-29)REDIS_KEY_SEPARATOR = "$"
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-30)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-31)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-32)# Utilities shared by both RedisSaver and AsyncRedisSaver
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-33)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-34)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-35)def_make_redis_checkpoint_key(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-36)  thread_id: str, checkpoint_ns: str, checkpoint_id: str
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-37)) -> str:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-38)  return REDIS_KEY_SEPARATOR.join(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-39)    ["checkpoint", thread_id, checkpoint_ns, checkpoint_id]
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-40)  )
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-41)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-42)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-43)def_make_redis_checkpoint_writes_key(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-44)  thread_id: str,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-45)  checkpoint_ns: str,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-46)  checkpoint_id: str,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-47)  task_id: str,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-48)  idx: Optional[int],
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-49)) -> str:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-50)  if idx is None:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-51)    return REDIS_KEY_SEPARATOR.join(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-52)      ["writes", thread_id, checkpoint_ns, checkpoint_id, task_id]
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-53)    )
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-54)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-55)  return REDIS_KEY_SEPARATOR.join(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-56)    ["writes", thread_id, checkpoint_ns, checkpoint_id, task_id, str(idx)]
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-57)  )
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-58)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-59)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-60)def_parse_redis_checkpoint_key(redis_key: str) -> dict:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-61)  namespace, thread_id, checkpoint_ns, checkpoint_id = redis_key.split(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-62)    REDIS_KEY_SEPARATOR
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-63)  )
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-64)  if namespace != "checkpoint":
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-65)    raise ValueError("Expected checkpoint key to start with 'checkpoint'")
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-66)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-67)  return {
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-68)    "thread_id": thread_id,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-69)    "checkpoint_ns": checkpoint_ns,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-70)    "checkpoint_id": checkpoint_id,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-71)  }
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-72)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-73)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-74)def_parse_redis_checkpoint_writes_key(redis_key: str) -> dict:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-75)  namespace, thread_id, checkpoint_ns, checkpoint_id, task_id, idx = redis_key.split(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-76)    REDIS_KEY_SEPARATOR
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-77)  )
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-78)  if namespace != "writes":
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-79)    raise ValueError("Expected checkpoint key to start with 'checkpoint'")
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-80)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-81)  return {
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-82)    "thread_id": thread_id,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-83)    "checkpoint_ns": checkpoint_ns,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-84)    "checkpoint_id": checkpoint_id,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-85)    "task_id": task_id,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-86)    "idx": idx,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-87)  }
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-88)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-89)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-90)def_filter_keys(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-91)  keys: List[str], before: Optional[RunnableConfig], limit: Optional[int]
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-92)) -> list:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-93)"""Filter and sort Redis keys based on optional criteria."""
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-94)  if before:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-95)    keys = [
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-96)      k
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-97)      for k in keys
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-98)      if _parse_redis_checkpoint_key(k.decode())["checkpoint_id"]
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-99)      < before["configurable"]["checkpoint_id"]
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-100)    ]
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-101)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-102)  keys = sorted(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-103)    keys,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-104)    key=lambda k: _parse_redis_checkpoint_key(k.decode())["checkpoint_id"],
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-105)    reverse=True,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-106)  )
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-107)  if limit:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-108)    keys = keys[:limit]
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-109)  return keys
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-110)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-111)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-112)def_load_writes(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-113)  serde: SerializerProtocol, task_id_to_data: dict[tuple[str, str], dict]
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-114)) -> list[PendingWrite]:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-115)"""Deserialize pending writes."""
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-116)  writes = [
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-117)    (
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-118)      task_id,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-119)      data[b"channel"].decode(),
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-120)      serde.loads_typed((data[b"type"].decode(), data[b"value"])),
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-121)    )
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-122)    for (task_id, _), data in task_id_to_data.items()
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-123)  ]
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-124)  return writes
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-125)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-126)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-127)def_parse_redis_checkpoint_data(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-128)  serde: SerializerProtocol,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-129)  key: str,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-130)  data: dict,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-131)  pending_writes: Optional[List[PendingWrite]] = None,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-132)) -> Optional[CheckpointTuple]:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-133)"""Parse checkpoint data retrieved from Redis."""
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-134)  if not data:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-135)    return None
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-136)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-137)  parsed_key = _parse_redis_checkpoint_key(key)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-138)  thread_id = parsed_key["thread_id"]
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-139)  checkpoint_ns = parsed_key["checkpoint_ns"]
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-140)  checkpoint_id = parsed_key["checkpoint_id"]
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-141)  config = {
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-142)    "configurable": {
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-143)      "thread_id": thread_id,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-144)      "checkpoint_ns": checkpoint_ns,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-145)      "checkpoint_id": checkpoint_id,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-146)    }
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-147)  }
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-148)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-149)  checkpoint = serde.loads_typed((data[b"type"].decode(), data[b"checkpoint"]))
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-150)  metadata = serde.loads(data[b"metadata"].decode())
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-151)  parent_checkpoint_id = data.get(b"parent_checkpoint_id", b"").decode()
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-152)  parent_config = (
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-153)    {
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-154)      "configurable": {
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-155)        "thread_id": thread_id,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-156)        "checkpoint_ns": checkpoint_ns,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-157)        "checkpoint_id": parent_checkpoint_id,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-158)      }
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-159)    }
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-160)    if parent_checkpoint_id
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-161)    else None
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-162)  )
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-163)  return CheckpointTuple(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-164)    config=config,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-165)    checkpoint=checkpoint,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-166)    metadata=metadata,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-167)    parent_config=parent_config,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-168)    pending_writes=pending_writes,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-3-169)  )

```


API Reference: [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html)

### RedisSaver[¶](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#redissaver "Permanent link")

Below is an implementation of RedisSaver (for synchronous use of graph, i.e. `.invoke()`, `.stream()`). RedisSaver implements four methods that are required for any checkpointer:

  * `.put` - Store a checkpoint with its configuration and metadata.
  * `.put_writes` - Store intermediate writes linked to a checkpoint (i.e. pending writes).
  * `.get_tuple` - Fetch a checkpoint tuple using for a given configuration (`thread_id` and `checkpoint_id`).
  * `.list` - List checkpoints that match a given configuration and filter criteria.



```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-1)classRedisSaver(BaseCheckpointSaver):
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-2)"""Redis-based checkpoint saver implementation."""
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-3)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-4)  conn: Redis
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-5)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-6)  def__init__(self, conn: Redis):
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-7)    super().__init__()
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-8)    self.conn = conn
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-9)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-10)  @classmethod
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-11)  @contextmanager
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-12)  deffrom_conn_info(cls, *, host: str, port: int, db: int) -> Iterator["RedisSaver"]:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-13)    conn = None
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-14)    try:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-15)      conn = Redis(host=host, port=port, db=db)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-16)      yield RedisSaver(conn)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-17)    finally:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-18)      if conn:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-19)        conn.close()
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-20)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-21)  defput(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-22)    self,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-23)    config: RunnableConfig,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-24)    checkpoint: Checkpoint,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-25)    metadata: CheckpointMetadata,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-26)    new_versions: ChannelVersions,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-27)  ) -> RunnableConfig:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-28)"""Save a checkpoint to Redis.
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-29)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-30)    Args:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-31)      config (RunnableConfig): The config to associate with the checkpoint.
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-32)      checkpoint (Checkpoint): The checkpoint to save.
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-33)      metadata (CheckpointMetadata): Additional metadata to save with the checkpoint.
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-34)      new_versions (ChannelVersions): New channel versions as of this write.
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-35)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-36)    Returns:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-37)      RunnableConfig: Updated configuration after storing the checkpoint.
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-38)    """
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-39)    thread_id = config["configurable"]["thread_id"]
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-40)    checkpoint_ns = config["configurable"]["checkpoint_ns"]
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-41)    checkpoint_id = checkpoint["id"]
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-42)    parent_checkpoint_id = config["configurable"].get("checkpoint_id")
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-43)    key = _make_redis_checkpoint_key(thread_id, checkpoint_ns, checkpoint_id)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-44)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-45)    type_, serialized_checkpoint = self.serde.dumps_typed(checkpoint)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-46)    serialized_metadata = self.serde.dumps(metadata)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-47)    data = {
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-48)      "checkpoint": serialized_checkpoint,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-49)      "type": type_,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-50)      "metadata": serialized_metadata,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-51)      "parent_checkpoint_id": parent_checkpoint_id
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-52)      if parent_checkpoint_id
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-53)      else "",
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-54)    }
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-55)    self.conn.hset(key, mapping=data)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-56)    return {
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-57)      "configurable": {
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-58)        "thread_id": thread_id,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-59)        "checkpoint_ns": checkpoint_ns,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-60)        "checkpoint_id": checkpoint_id,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-61)      }
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-62)    }
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-63)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-64)  defput_writes(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-65)    self,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-66)    config: RunnableConfig,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-67)    writes: List[Tuple[str, Any]],
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-68)    task_id: str,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-69)  ) -> None:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-70)"""Store intermediate writes linked to a checkpoint.
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-71)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-72)    Args:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-73)      config (RunnableConfig): Configuration of the related checkpoint.
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-74)      writes (Sequence[Tuple[str, Any]]): List of writes to store, each as (channel, value) pair.
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-75)      task_id (str): Identifier for the task creating the writes.
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-76)    """
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-77)    thread_id = config["configurable"]["thread_id"]
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-78)    checkpoint_ns = config["configurable"]["checkpoint_ns"]
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-79)    checkpoint_id = config["configurable"]["checkpoint_id"]
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-80)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-81)    for idx, (channel, value) in enumerate(writes):
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-82)      key = _make_redis_checkpoint_writes_key(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-83)        thread_id,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-84)        checkpoint_ns,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-85)        checkpoint_id,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-86)        task_id,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-87)        WRITES_IDX_MAP.get(channel, idx),
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-88)      )
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-89)      type_, serialized_value = self.serde.dumps_typed(value)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-90)      data = {"channel": channel, "type": type_, "value": serialized_value}
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-91)      if all(w[0] in WRITES_IDX_MAP for w in writes):
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-92)        # Use HSET which will overwrite existing values
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-93)        self.conn.hset(key, mapping=data)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-94)      else:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-95)        # Use HSETNX which will not overwrite existing values
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-96)        for field, value in data.items():
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-97)          self.conn.hsetnx(key, field, value)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-98)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-99)  defget_tuple(self, config: RunnableConfig) -> Optional[CheckpointTuple]:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-100)"""Get a checkpoint tuple from Redis.
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-101)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-102)    This method retrieves a checkpoint tuple from Redis based on the
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-103)    provided config. If the config contains a "checkpoint_id" key, the checkpoint with
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-104)    the matching thread ID and checkpoint ID is retrieved. Otherwise, the latest checkpoint
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-105)    for the given thread ID is retrieved.
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-106)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-107)    Args:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-108)      config (RunnableConfig): The config to use for retrieving the checkpoint.
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-109)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-110)    Returns:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-111)      Optional[CheckpointTuple]: The retrieved checkpoint tuple, or None if no matching checkpoint was found.
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-112)    """
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-113)    thread_id = config["configurable"]["thread_id"]
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-114)    checkpoint_id = get_checkpoint_id(config)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-115)    checkpoint_ns = config["configurable"].get("checkpoint_ns", "")
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-116)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-117)    checkpoint_key = self._get_checkpoint_key(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-118)      self.conn, thread_id, checkpoint_ns, checkpoint_id
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-119)    )
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-120)    if not checkpoint_key:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-121)      return None
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-122)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-123)    checkpoint_data = self.conn.hgetall(checkpoint_key)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-124)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-125)    # load pending writes
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-126)    checkpoint_id = (
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-127)      checkpoint_id
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-128)      or _parse_redis_checkpoint_key(checkpoint_key)["checkpoint_id"]
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-129)    )
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-130)    pending_writes = self._load_pending_writes(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-131)      thread_id, checkpoint_ns, checkpoint_id
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-132)    )
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-133)    return _parse_redis_checkpoint_data(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-134)      self.serde, checkpoint_key, checkpoint_data, pending_writes=pending_writes
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-135)    )
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-136)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-137)  deflist(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-138)    self,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-139)    config: Optional[RunnableConfig],
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-140)    *,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-141)    # TODO: implement filtering
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-142)    filter: Optional[dict[str, Any]] = None,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-143)    before: Optional[RunnableConfig] = None,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-144)    limit: Optional[int] = None,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-145)  ) -> Iterator[CheckpointTuple]:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-146)"""List checkpoints from the database.
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-147)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-148)    This method retrieves a list of checkpoint tuples from Redis based
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-149)    on the provided config. The checkpoints are ordered by checkpoint ID in descending order (newest first).
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-150)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-151)    Args:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-152)      config (RunnableConfig): The config to use for listing the checkpoints.
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-153)      filter (Optional[Dict[str, Any]]): Additional filtering criteria for metadata. Defaults to None.
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-154)      before (Optional[RunnableConfig]): If provided, only checkpoints before the specified checkpoint ID are returned. Defaults to None.
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-155)      limit (Optional[int]): The maximum number of checkpoints to return. Defaults to None.
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-156)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-157)    Yields:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-158)      Iterator[CheckpointTuple]: An iterator of checkpoint tuples.
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-159)    """
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-160)    thread_id = config["configurable"]["thread_id"]
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-161)    checkpoint_ns = config["configurable"].get("checkpoint_ns", "")
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-162)    pattern = _make_redis_checkpoint_key(thread_id, checkpoint_ns, "*")
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-163)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-164)    keys = _filter_keys(self.conn.keys(pattern), before, limit)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-165)    for key in keys:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-166)      data = self.conn.hgetall(key)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-167)      if data and b"checkpoint" in data and b"metadata" in data:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-168)        # load pending writes
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-169)        checkpoint_id = _parse_redis_checkpoint_key(key.decode())[
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-170)          "checkpoint_id"
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-171)        ]
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-172)        pending_writes = self._load_pending_writes(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-173)          thread_id, checkpoint_ns, checkpoint_id
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-174)        )
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-175)        yield _parse_redis_checkpoint_data(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-176)          self.serde, key.decode(), data, pending_writes=pending_writes
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-177)        )
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-178)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-179)  def_load_pending_writes(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-180)    self, thread_id: str, checkpoint_ns: str, checkpoint_id: str
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-181)  ) -> List[PendingWrite]:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-182)    writes_key = _make_redis_checkpoint_writes_key(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-183)      thread_id, checkpoint_ns, checkpoint_id, "*", None
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-184)    )
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-185)    matching_keys = self.conn.keys(pattern=writes_key)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-186)    parsed_keys = [
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-187)      _parse_redis_checkpoint_writes_key(key.decode()) for key in matching_keys
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-188)    ]
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-189)    pending_writes = _load_writes(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-190)      self.serde,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-191)      {
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-192)        (parsed_key["task_id"], parsed_key["idx"]): self.conn.hgetall(key)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-193)        for key, parsed_key in sorted(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-194)          zip(matching_keys, parsed_keys), key=lambda x: x[1]["idx"]
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-195)        )
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-196)      },
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-197)    )
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-198)    return pending_writes
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-199)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-200)  def_get_checkpoint_key(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-201)    self, conn, thread_id: str, checkpoint_ns: str, checkpoint_id: Optional[str]
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-202)  ) -> Optional[str]:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-203)"""Determine the Redis key for a checkpoint."""
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-204)    if checkpoint_id:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-205)      return _make_redis_checkpoint_key(thread_id, checkpoint_ns, checkpoint_id)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-206)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-207)    all_keys = conn.keys(_make_redis_checkpoint_key(thread_id, checkpoint_ns, "*"))
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-208)    if not all_keys:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-209)      return None
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-210)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-211)    latest_key = max(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-212)      all_keys,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-213)      key=lambda k: _parse_redis_checkpoint_key(k.decode())["checkpoint_id"],
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-214)    )
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-4-215)    return latest_key.decode()

```


### AsyncRedis[¶](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#asyncredis "Permanent link")

Below is a reference implementation of AsyncRedisSaver (for asynchronous use of graph, i.e. `.ainvoke()`, `.astream()`). AsyncRedisSaver implements four methods that are required for any async checkpointer:

  * `.aput` - Store a checkpoint with its configuration and metadata.
  * `.aput_writes` - Store intermediate writes linked to a checkpoint (i.e. pending writes).
  * `.aget_tuple` - Fetch a checkpoint tuple using for a given configuration (`thread_id` and `checkpoint_id`).
  * `.alist` - List checkpoints that match a given configuration and filter criteria.



```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-1)classAsyncRedisSaver(BaseCheckpointSaver):
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-2)"""Async redis-based checkpoint saver implementation."""
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-3)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-4)  conn: AsyncRedis
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-5)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-6)  def__init__(self, conn: AsyncRedis):
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-7)    super().__init__()
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-8)    self.conn = conn
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-9)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-10)  @classmethod
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-11)  @asynccontextmanager
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-12)  async deffrom_conn_info(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-13)    cls, *, host: str, port: int, db: int
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-14)  ) -> AsyncIterator["AsyncRedisSaver"]:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-15)    conn = None
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-16)    try:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-17)      conn = AsyncRedis(host=host, port=port, db=db)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-18)      yield AsyncRedisSaver(conn)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-19)    finally:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-20)      if conn:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-21)        await conn.aclose()
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-22)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-23)  async defaput(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-24)    self,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-25)    config: RunnableConfig,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-26)    checkpoint: Checkpoint,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-27)    metadata: CheckpointMetadata,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-28)    new_versions: ChannelVersions,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-29)  ) -> RunnableConfig:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-30)"""Save a checkpoint to the database asynchronously.
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-31)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-32)    This method saves a checkpoint to Redis. The checkpoint is associated
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-33)    with the provided config and its parent config (if any).
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-34)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-35)    Args:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-36)      config (RunnableConfig): The config to associate with the checkpoint.
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-37)      checkpoint (Checkpoint): The checkpoint to save.
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-38)      metadata (CheckpointMetadata): Additional metadata to save with the checkpoint.
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-39)      new_versions (ChannelVersions): New channel versions as of this write.
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-40)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-41)    Returns:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-42)      RunnableConfig: Updated configuration after storing the checkpoint.
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-43)    """
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-44)    thread_id = config["configurable"]["thread_id"]
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-45)    checkpoint_ns = config["configurable"]["checkpoint_ns"]
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-46)    checkpoint_id = checkpoint["id"]
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-47)    parent_checkpoint_id = config["configurable"].get("checkpoint_id")
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-48)    key = _make_redis_checkpoint_key(thread_id, checkpoint_ns, checkpoint_id)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-49)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-50)    type_, serialized_checkpoint = self.serde.dumps_typed(checkpoint)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-51)    serialized_metadata = self.serde.dumps(metadata)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-52)    data = {
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-53)      "checkpoint": serialized_checkpoint,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-54)      "type": type_,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-55)      "checkpoint_id": checkpoint_id,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-56)      "metadata": serialized_metadata,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-57)      "parent_checkpoint_id": parent_checkpoint_id
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-58)      if parent_checkpoint_id
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-59)      else "",
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-60)    }
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-61)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-62)    await self.conn.hset(key, mapping=data)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-63)    return {
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-64)      "configurable": {
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-65)        "thread_id": thread_id,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-66)        "checkpoint_ns": checkpoint_ns,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-67)        "checkpoint_id": checkpoint_id,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-68)      }
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-69)    }
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-70)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-71)  async defaput_writes(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-72)    self,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-73)    config: RunnableConfig,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-74)    writes: List[Tuple[str, Any]],
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-75)    task_id: str,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-76)  ) -> None:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-77)"""Store intermediate writes linked to a checkpoint asynchronously.
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-78)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-79)    This method saves intermediate writes associated with a checkpoint to the database.
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-80)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-81)    Args:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-82)      config (RunnableConfig): Configuration of the related checkpoint.
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-83)      writes (Sequence[Tuple[str, Any]]): List of writes to store, each as (channel, value) pair.
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-84)      task_id (str): Identifier for the task creating the writes.
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-85)    """
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-86)    thread_id = config["configurable"]["thread_id"]
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-87)    checkpoint_ns = config["configurable"]["checkpoint_ns"]
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-88)    checkpoint_id = config["configurable"]["checkpoint_id"]
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-89)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-90)    for idx, (channel, value) in enumerate(writes):
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-91)      key = _make_redis_checkpoint_writes_key(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-92)        thread_id,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-93)        checkpoint_ns,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-94)        checkpoint_id,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-95)        task_id,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-96)        WRITES_IDX_MAP.get(channel, idx),
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-97)      )
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-98)      type_, serialized_value = self.serde.dumps_typed(value)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-99)      data = {"channel": channel, "type": type_, "value": serialized_value}
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-100)      if all(w[0] in WRITES_IDX_MAP for w in writes):
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-101)        # Use HSET which will overwrite existing values
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-102)        await self.conn.hset(key, mapping=data)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-103)      else:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-104)        # Use HSETNX which will not overwrite existing values
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-105)        for field, value in data.items():
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-106)          await self.conn.hsetnx(key, field, value)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-107)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-108)  async defaget_tuple(self, config: RunnableConfig) -> Optional[CheckpointTuple]:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-109)"""Get a checkpoint tuple from Redis asynchronously.
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-110)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-111)    This method retrieves a checkpoint tuple from Redis based on the
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-112)    provided config. If the config contains a "checkpoint_id" key, the checkpoint with
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-113)    the matching thread ID and checkpoint ID is retrieved. Otherwise, the latest checkpoint
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-114)    for the given thread ID is retrieved.
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-115)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-116)    Args:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-117)      config (RunnableConfig): The config to use for retrieving the checkpoint.
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-118)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-119)    Returns:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-120)      Optional[CheckpointTuple]: The retrieved checkpoint tuple, or None if no matching checkpoint was found.
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-121)    """
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-122)    thread_id = config["configurable"]["thread_id"]
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-123)    checkpoint_id = get_checkpoint_id(config)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-124)    checkpoint_ns = config["configurable"].get("checkpoint_ns", "")
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-125)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-126)    checkpoint_key = await self._aget_checkpoint_key(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-127)      self.conn, thread_id, checkpoint_ns, checkpoint_id
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-128)    )
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-129)    if not checkpoint_key:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-130)      return None
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-131)    checkpoint_data = await self.conn.hgetall(checkpoint_key)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-132)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-133)    # load pending writes
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-134)    checkpoint_id = (
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-135)      checkpoint_id
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-136)      or _parse_redis_checkpoint_key(checkpoint_key)["checkpoint_id"]
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-137)    )
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-138)    pending_writes = await self._aload_pending_writes(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-139)      thread_id, checkpoint_ns, checkpoint_id
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-140)    )
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-141)    return _parse_redis_checkpoint_data(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-142)      self.serde, checkpoint_key, checkpoint_data, pending_writes=pending_writes
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-143)    )
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-144)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-145)  async defalist(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-146)    self,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-147)    config: Optional[RunnableConfig],
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-148)    *,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-149)    # TODO: implement filtering
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-150)    filter: Optional[dict[str, Any]] = None,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-151)    before: Optional[RunnableConfig] = None,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-152)    limit: Optional[int] = None,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-153)  ) -> AsyncGenerator[CheckpointTuple, None]:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-154)"""List checkpoints from Redis asynchronously.
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-155)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-156)    This method retrieves a list of checkpoint tuples from Redis based
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-157)    on the provided config. The checkpoints are ordered by checkpoint ID in descending order (newest first).
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-158)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-159)    Args:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-160)      config (Optional[RunnableConfig]): Base configuration for filtering checkpoints.
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-161)      filter (Optional[Dict[str, Any]]): Additional filtering criteria for metadata.
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-162)      before (Optional[RunnableConfig]): If provided, only checkpoints before the specified checkpoint ID are returned. Defaults to None.
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-163)      limit (Optional[int]): Maximum number of checkpoints to return.
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-164)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-165)    Yields:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-166)      AsyncIterator[CheckpointTuple]: An asynchronous iterator of matching checkpoint tuples.
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-167)    """
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-168)    thread_id = config["configurable"]["thread_id"]
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-169)    checkpoint_ns = config["configurable"].get("checkpoint_ns", "")
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-170)    pattern = _make_redis_checkpoint_key(thread_id, checkpoint_ns, "*")
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-171)    keys = _filter_keys(await self.conn.keys(pattern), before, limit)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-172)    for key in keys:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-173)      data = await self.conn.hgetall(key)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-174)      if data and b"checkpoint" in data and b"metadata" in data:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-175)        checkpoint_id = _parse_redis_checkpoint_key(key.decode())[
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-176)          "checkpoint_id"
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-177)        ]
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-178)        pending_writes = await self._aload_pending_writes(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-179)          thread_id, checkpoint_ns, checkpoint_id
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-180)        )
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-181)        yield _parse_redis_checkpoint_data(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-182)          self.serde, key.decode(), data, pending_writes=pending_writes
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-183)        )
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-184)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-185)  async def_aload_pending_writes(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-186)    self, thread_id: str, checkpoint_ns: str, checkpoint_id: str
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-187)  ) -> List[PendingWrite]:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-188)    writes_key = _make_redis_checkpoint_writes_key(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-189)      thread_id, checkpoint_ns, checkpoint_id, "*", None
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-190)    )
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-191)    matching_keys = await self.conn.keys(pattern=writes_key)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-192)    parsed_keys = [
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-193)      _parse_redis_checkpoint_writes_key(key.decode()) for key in matching_keys
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-194)    ]
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-195)    pending_writes = _load_writes(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-196)      self.serde,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-197)      {
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-198)        (parsed_key["task_id"], parsed_key["idx"]): await self.conn.hgetall(key)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-199)        for key, parsed_key in sorted(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-200)          zip(matching_keys, parsed_keys), key=lambda x: x[1]["idx"]
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-201)        )
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-202)      },
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-203)    )
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-204)    return pending_writes
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-205)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-206)  async def_aget_checkpoint_key(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-207)    self, conn, thread_id: str, checkpoint_ns: str, checkpoint_id: Optional[str]
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-208)  ) -> Optional[str]:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-209)"""Asynchronously determine the Redis key for a checkpoint."""
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-210)    if checkpoint_id:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-211)      return _make_redis_checkpoint_key(thread_id, checkpoint_ns, checkpoint_id)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-212)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-213)    all_keys = await conn.keys(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-214)      _make_redis_checkpoint_key(thread_id, checkpoint_ns, "*")
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-215)    )
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-216)    if not all_keys:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-217)      return None
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-218)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-219)    latest_key = max(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-220)      all_keys,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-221)      key=lambda k: _parse_redis_checkpoint_key(k.decode())["checkpoint_id"],
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-222)    )
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-5-223)    return latest_key.decode()

```


## Setup model and tools for the graph[¶](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#setup-model-and-tools-for-the-graph "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-6-1)fromtypingimport Literal
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-6-2)fromlangchain_core.runnablesimport ConfigurableField
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-6-3)fromlangchain_core.toolsimport tool
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-6-4)fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-6-5)fromlanggraph.prebuiltimport create_react_agent
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-6-6)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-6-7)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-6-8)@tool
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-6-9)defget_weather(city: Literal["nyc", "sf"]):
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-6-10)"""Use this to get weather information."""
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-6-11)  if city == "nyc":
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-6-12)    return "It might be cloudy in nyc"
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-6-13)  elif city == "sf":
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-6-14)    return "It's always sunny in sf"
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-6-15)  else:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-6-16)    raise AssertionError("Unknown city")
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-6-17)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-6-18)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-6-19)tools = [get_weather]
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-6-20)model = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

```


API Reference: [ConfigurableField](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.ConfigurableField.html) | [tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html) | [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html) | [create_react_agent](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent)

## Use sync connection[¶](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#use-sync-connection "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-7-1)with RedisSaver.from_conn_info(host="localhost", port=6379, db=0) as checkpointer:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-7-2)  graph = create_react_agent(model, tools=tools, checkpointer=checkpointer)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-7-3)  config = {"configurable": {"thread_id": "1"}}
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-7-4)  res = graph.invoke({"messages": [("human", "what's the weather in sf")]}, config)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-7-5)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-7-6)  latest_checkpoint = checkpointer.get(config)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-7-7)  latest_checkpoint_tuple = checkpointer.get_tuple(config)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-7-8)  checkpoint_tuples = list(checkpointer.list(config))

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-8-1)latest_checkpoint

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-9-1){'v': 1,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-9-2) 'ts': '2024-08-09T01:56:48.328315+00:00',
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-9-3) 'id': '1ef55f2a-3614-69b4-8003-2181cff935cc',
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-9-4) 'channel_values': {'messages': [HumanMessage(content="what's the weather in sf", id='f911e000-75a1-41f6-8e38-77bb086c2ecf'),
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-9-5)  AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_l5e5YcTJDJYOdvi4scBy9n2I', 'function': {'arguments': '{"city":"sf"}', 'name': 'get_weather'}, 'type': 'function'}]}, response_metadata={'token_usage': {'completion_tokens': 14, 'prompt_tokens': 57, 'total_tokens': 71}, 'model_name': 'gpt-4o-mini', 'system_fingerprint': 'fp_48196bc67a', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-4f1531f1-067c-4e16-8b62-7a6b663e93bd-0', tool_calls=[{'name': 'get_weather', 'args': {'city': 'sf'}, 'id': 'call_l5e5YcTJDJYOdvi4scBy9n2I', 'type': 'tool_call'}], usage_metadata={'input_tokens': 57, 'output_tokens': 14, 'total_tokens': 71}),
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-9-6)  ToolMessage(content="It's always sunny in sf", name='get_weather', id='e27bb3a1-1798-494a-b4ad-2deadda8b2bf', tool_call_id='call_l5e5YcTJDJYOdvi4scBy9n2I'),
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-9-7)  AIMessage(content='The weather in San Francisco is always sunny!', response_metadata={'token_usage': {'completion_tokens': 10, 'prompt_tokens': 84, 'total_tokens': 94}, 'model_name': 'gpt-4o-mini', 'system_fingerprint': 'fp_48196bc67a', 'finish_reason': 'stop', 'logprobs': None}, id='run-ad546b5a-70ce-404e-9656-dcc6ecd482d3-0', usage_metadata={'input_tokens': 84, 'output_tokens': 10, 'total_tokens': 94})],
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-9-8) 'agent': 'agent'},
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-9-9) 'channel_versions': {'__start__': '00000000000000000000000000000002.',
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-9-10) 'messages': '00000000000000000000000000000005.16e98d6f7ece7598829eddf1b33a33c4',
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-9-11) 'start:agent': '00000000000000000000000000000003.',
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-9-12) 'agent': '00000000000000000000000000000005.065d90dd7f7cd091f0233855210bb2af',
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-9-13) 'branch:agent:should_continue:tools': '00000000000000000000000000000004.',
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-9-14) 'tools': '00000000000000000000000000000005.'},
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-9-15) 'versions_seen': {'__input__': {},
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-9-16) '__start__': {'__start__': '00000000000000000000000000000001.ab89befb52cc0e91e106ef7f500ea033'},
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-9-17) 'agent': {'start:agent': '00000000000000000000000000000002.d6f25946c3108fc12f27abbcf9b4cedc',
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-9-18)  'tools': '00000000000000000000000000000004.022986cd20ae85c77ea298a383f69ba8'},
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-9-19) 'tools': {'branch:agent:should_continue:tools': '00000000000000000000000000000003.065d90dd7f7cd091f0233855210bb2af'}},
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-9-20) 'pending_sends': [],
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-9-21) 'current_tasks': {}}

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-10-1)latest_checkpoint_tuple

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-11-1)CheckpointTuple(config={'configurable': {'thread_id': '1', 'checkpoint_ns': '', 'checkpoint_id': '1ef55f2a-3614-69b4-8003-2181cff935cc'}}, checkpoint={'v': 1, 'ts': '2024-08-09T01:56:48.328315+00:00', 'id': '1ef55f2a-3614-69b4-8003-2181cff935cc', 'channel_values': {'messages': [HumanMessage(content="what's the weather in sf", id='f911e000-75a1-41f6-8e38-77bb086c2ecf'), AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_l5e5YcTJDJYOdvi4scBy9n2I', 'function': {'arguments': '{"city":"sf"}', 'name': 'get_weather'}, 'type': 'function'}]}, response_metadata={'token_usage': {'completion_tokens': 14, 'prompt_tokens': 57, 'total_tokens': 71}, 'model_name': 'gpt-4o-mini', 'system_fingerprint': 'fp_48196bc67a', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-4f1531f1-067c-4e16-8b62-7a6b663e93bd-0', tool_calls=[{'name': 'get_weather', 'args': {'city': 'sf'}, 'id': 'call_l5e5YcTJDJYOdvi4scBy9n2I', 'type': 'tool_call'}], usage_metadata={'input_tokens': 57, 'output_tokens': 14, 'total_tokens': 71}), ToolMessage(content="It's always sunny in sf", name='get_weather', id='e27bb3a1-1798-494a-b4ad-2deadda8b2bf', tool_call_id='call_l5e5YcTJDJYOdvi4scBy9n2I'), AIMessage(content='The weather in San Francisco is always sunny!', response_metadata={'token_usage': {'completion_tokens': 10, 'prompt_tokens': 84, 'total_tokens': 94}, 'model_name': 'gpt-4o-mini', 'system_fingerprint': 'fp_48196bc67a', 'finish_reason': 'stop', 'logprobs': None}, id='run-ad546b5a-70ce-404e-9656-dcc6ecd482d3-0', usage_metadata={'input_tokens': 84, 'output_tokens': 10, 'total_tokens': 94})], 'agent': 'agent'}, 'channel_versions': {'__start__': '00000000000000000000000000000002.', 'messages': '00000000000000000000000000000005.16e98d6f7ece7598829eddf1b33a33c4', 'start:agent': '00000000000000000000000000000003.', 'agent': '00000000000000000000000000000005.065d90dd7f7cd091f0233855210bb2af', 'branch:agent:should_continue:tools': '00000000000000000000000000000004.', 'tools': '00000000000000000000000000000005.'}, 'versions_seen': {'__input__': {}, '__start__': {'__start__': '00000000000000000000000000000001.ab89befb52cc0e91e106ef7f500ea033'}, 'agent': {'start:agent': '00000000000000000000000000000002.d6f25946c3108fc12f27abbcf9b4cedc', 'tools': '00000000000000000000000000000004.022986cd20ae85c77ea298a383f69ba8'}, 'tools': {'branch:agent:should_continue:tools': '00000000000000000000000000000003.065d90dd7f7cd091f0233855210bb2af'}}, 'pending_sends': [], 'current_tasks': {}}, metadata={'source': 'loop', 'writes': {'agent': {'messages': [AIMessage(content='The weather in San Francisco is always sunny!', response_metadata={'token_usage': {'completion_tokens': 10, 'prompt_tokens': 84, 'total_tokens': 94}, 'model_name': 'gpt-4o-mini', 'system_fingerprint': 'fp_48196bc67a', 'finish_reason': 'stop', 'logprobs': None}, id='run-ad546b5a-70ce-404e-9656-dcc6ecd482d3-0', usage_metadata={'input_tokens': 84, 'output_tokens': 10, 'total_tokens': 94})]}}, 'step': 3}, parent_config={'configurable': {'thread_id': '1', 'checkpoint_ns': '', 'checkpoint_id': '1ef55f2a-306f-6252-8002-47c2374ec1f2'}}, pending_writes=[])

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-12-1)checkpoint_tuples

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-13-1)[CheckpointTuple(config={'configurable': {'thread_id': '1', 'checkpoint_ns': '', 'checkpoint_id': '1ef55f2a-3614-69b4-8003-2181cff935cc'}}, checkpoint={'v': 1, 'ts': '2024-08-09T01:56:48.328315+00:00', 'id': '1ef55f2a-3614-69b4-8003-2181cff935cc', 'channel_values': {'messages': [HumanMessage(content="what's the weather in sf", id='f911e000-75a1-41f6-8e38-77bb086c2ecf'), AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_l5e5YcTJDJYOdvi4scBy9n2I', 'function': {'arguments': '{"city":"sf"}', 'name': 'get_weather'}, 'type': 'function'}]}, response_metadata={'token_usage': {'completion_tokens': 14, 'prompt_tokens': 57, 'total_tokens': 71}, 'model_name': 'gpt-4o-mini', 'system_fingerprint': 'fp_48196bc67a', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-4f1531f1-067c-4e16-8b62-7a6b663e93bd-0', tool_calls=[{'name': 'get_weather', 'args': {'city': 'sf'}, 'id': 'call_l5e5YcTJDJYOdvi4scBy9n2I', 'type': 'tool_call'}], usage_metadata={'input_tokens': 57, 'output_tokens': 14, 'total_tokens': 71}), ToolMessage(content="It's always sunny in sf", name='get_weather', id='e27bb3a1-1798-494a-b4ad-2deadda8b2bf', tool_call_id='call_l5e5YcTJDJYOdvi4scBy9n2I'), AIMessage(content='The weather in San Francisco is always sunny!', response_metadata={'token_usage': {'completion_tokens': 10, 'prompt_tokens': 84, 'total_tokens': 94}, 'model_name': 'gpt-4o-mini', 'system_fingerprint': 'fp_48196bc67a', 'finish_reason': 'stop', 'logprobs': None}, id='run-ad546b5a-70ce-404e-9656-dcc6ecd482d3-0', usage_metadata={'input_tokens': 84, 'output_tokens': 10, 'total_tokens': 94})], 'agent': 'agent'}, 'channel_versions': {'__start__': '00000000000000000000000000000002.', 'messages': '00000000000000000000000000000005.16e98d6f7ece7598829eddf1b33a33c4', 'start:agent': '00000000000000000000000000000003.', 'agent': '00000000000000000000000000000005.065d90dd7f7cd091f0233855210bb2af', 'branch:agent:should_continue:tools': '00000000000000000000000000000004.', 'tools': '00000000000000000000000000000005.'}, 'versions_seen': {'__input__': {}, '__start__': {'__start__': '00000000000000000000000000000001.ab89befb52cc0e91e106ef7f500ea033'}, 'agent': {'start:agent': '00000000000000000000000000000002.d6f25946c3108fc12f27abbcf9b4cedc', 'tools': '00000000000000000000000000000004.022986cd20ae85c77ea298a383f69ba8'}, 'tools': {'branch:agent:should_continue:tools': '00000000000000000000000000000003.065d90dd7f7cd091f0233855210bb2af'}}, 'pending_sends': [], 'current_tasks': {}}, metadata={'source': 'loop', 'writes': {'agent': {'messages': [AIMessage(content='The weather in San Francisco is always sunny!', response_metadata={'token_usage': {'completion_tokens': 10, 'prompt_tokens': 84, 'total_tokens': 94}, 'model_name': 'gpt-4o-mini', 'system_fingerprint': 'fp_48196bc67a', 'finish_reason': 'stop', 'logprobs': None}, id='run-ad546b5a-70ce-404e-9656-dcc6ecd482d3-0', usage_metadata={'input_tokens': 84, 'output_tokens': 10, 'total_tokens': 94})]}}, 'step': 3}, parent_config={'configurable': {'thread_id': '1', 'checkpoint_ns': '', 'checkpoint_id': '1ef55f2a-306f-6252-8002-47c2374ec1f2'}}, pending_writes=None),
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-13-2) CheckpointTuple(config={'configurable': {'thread_id': '1', 'checkpoint_ns': '', 'checkpoint_id': '1ef55f2a-306f-6252-8002-47c2374ec1f2'}}, checkpoint={'v': 1, 'ts': '2024-08-09T01:56:47.736251+00:00', 'id': '1ef55f2a-306f-6252-8002-47c2374ec1f2', 'channel_values': {'messages': [HumanMessage(content="what's the weather in sf", id='f911e000-75a1-41f6-8e38-77bb086c2ecf'), AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_l5e5YcTJDJYOdvi4scBy9n2I', 'function': {'arguments': '{"city":"sf"}', 'name': 'get_weather'}, 'type': 'function'}]}, response_metadata={'token_usage': {'completion_tokens': 14, 'prompt_tokens': 57, 'total_tokens': 71}, 'model_name': 'gpt-4o-mini', 'system_fingerprint': 'fp_48196bc67a', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-4f1531f1-067c-4e16-8b62-7a6b663e93bd-0', tool_calls=[{'name': 'get_weather', 'args': {'city': 'sf'}, 'id': 'call_l5e5YcTJDJYOdvi4scBy9n2I', 'type': 'tool_call'}], usage_metadata={'input_tokens': 57, 'output_tokens': 14, 'total_tokens': 71}), ToolMessage(content="It's always sunny in sf", name='get_weather', id='e27bb3a1-1798-494a-b4ad-2deadda8b2bf', tool_call_id='call_l5e5YcTJDJYOdvi4scBy9n2I')], 'tools': 'tools'}, 'channel_versions': {'__start__': '00000000000000000000000000000002.', 'messages': '00000000000000000000000000000004.b16eb718f179ac1dcde54c5652768cf5', 'start:agent': '00000000000000000000000000000003.', 'agent': '00000000000000000000000000000004.', 'branch:agent:should_continue:tools': '00000000000000000000000000000004.', 'tools': '00000000000000000000000000000004.022986cd20ae85c77ea298a383f69ba8'}, 'versions_seen': {'__input__': {}, '__start__': {'__start__': '00000000000000000000000000000001.ab89befb52cc0e91e106ef7f500ea033'}, 'agent': {'start:agent': '00000000000000000000000000000002.d6f25946c3108fc12f27abbcf9b4cedc'}, 'tools': {'branch:agent:should_continue:tools': '00000000000000000000000000000003.065d90dd7f7cd091f0233855210bb2af'}}, 'pending_sends': [], 'current_tasks': {}}, metadata={'source': 'loop', 'writes': {'tools': {'messages': [ToolMessage(content="It's always sunny in sf", name='get_weather', id='e27bb3a1-1798-494a-b4ad-2deadda8b2bf', tool_call_id='call_l5e5YcTJDJYOdvi4scBy9n2I')]}}, 'step': 2}, parent_config={'configurable': {'thread_id': '1', 'checkpoint_ns': '', 'checkpoint_id': '1ef55f2a-305f-61cc-8001-efac33022ef7'}}, pending_writes=None),
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-13-3) CheckpointTuple(config={'configurable': {'thread_id': '1', 'checkpoint_ns': '', 'checkpoint_id': '1ef55f2a-305f-61cc-8001-efac33022ef7'}}, checkpoint={'v': 1, 'ts': '2024-08-09T01:56:47.729689+00:00', 'id': '1ef55f2a-305f-61cc-8001-efac33022ef7', 'channel_values': {'messages': [HumanMessage(content="what's the weather in sf", id='f911e000-75a1-41f6-8e38-77bb086c2ecf'), AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_l5e5YcTJDJYOdvi4scBy9n2I', 'function': {'arguments': '{"city":"sf"}', 'name': 'get_weather'}, 'type': 'function'}]}, response_metadata={'token_usage': {'completion_tokens': 14, 'prompt_tokens': 57, 'total_tokens': 71}, 'model_name': 'gpt-4o-mini', 'system_fingerprint': 'fp_48196bc67a', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-4f1531f1-067c-4e16-8b62-7a6b663e93bd-0', tool_calls=[{'name': 'get_weather', 'args': {'city': 'sf'}, 'id': 'call_l5e5YcTJDJYOdvi4scBy9n2I', 'type': 'tool_call'}], usage_metadata={'input_tokens': 57, 'output_tokens': 14, 'total_tokens': 71})], 'agent': 'agent', 'branch:agent:should_continue:tools': 'agent'}, 'channel_versions': {'__start__': '00000000000000000000000000000002.', 'messages': '00000000000000000000000000000003.4dd312547dcca1cf91a19adb620a18d6', 'start:agent': '00000000000000000000000000000003.', 'agent': '00000000000000000000000000000003.065d90dd7f7cd091f0233855210bb2af', 'branch:agent:should_continue:tools': '00000000000000000000000000000003.065d90dd7f7cd091f0233855210bb2af'}, 'versions_seen': {'__input__': {}, '__start__': {'__start__': '00000000000000000000000000000001.ab89befb52cc0e91e106ef7f500ea033'}, 'agent': {'start:agent': '00000000000000000000000000000002.d6f25946c3108fc12f27abbcf9b4cedc'}}, 'pending_sends': [], 'current_tasks': {}}, metadata={'source': 'loop', 'writes': {'agent': {'messages': [AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_l5e5YcTJDJYOdvi4scBy9n2I', 'function': {'arguments': '{"city":"sf"}', 'name': 'get_weather'}, 'type': 'function'}]}, response_metadata={'token_usage': {'completion_tokens': 14, 'prompt_tokens': 57, 'total_tokens': 71}, 'model_name': 'gpt-4o-mini', 'system_fingerprint': 'fp_48196bc67a', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-4f1531f1-067c-4e16-8b62-7a6b663e93bd-0', tool_calls=[{'name': 'get_weather', 'args': {'city': 'sf'}, 'id': 'call_l5e5YcTJDJYOdvi4scBy9n2I', 'type': 'tool_call'}], usage_metadata={'input_tokens': 57, 'output_tokens': 14, 'total_tokens': 71})]}}, 'step': 1}, parent_config={'configurable': {'thread_id': '1', 'checkpoint_ns': '', 'checkpoint_id': '1ef55f2a-2a52-6a7c-8000-27624d954d15'}}, pending_writes=None),
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-13-4) CheckpointTuple(config={'configurable': {'thread_id': '1', 'checkpoint_ns': '', 'checkpoint_id': '1ef55f2a-2a52-6a7c-8000-27624d954d15'}}, checkpoint={'v': 1, 'ts': '2024-08-09T01:56:47.095456+00:00', 'id': '1ef55f2a-2a52-6a7c-8000-27624d954d15', 'channel_values': {'messages': [HumanMessage(content="what's the weather in sf", id='f911e000-75a1-41f6-8e38-77bb086c2ecf')], 'start:agent': '__start__'}, 'channel_versions': {'__start__': '00000000000000000000000000000002.', 'messages': '00000000000000000000000000000002.52e8b0c387f50c28345585c088150464', 'start:agent': '00000000000000000000000000000002.d6f25946c3108fc12f27abbcf9b4cedc'}, 'versions_seen': {'__input__': {}, '__start__': {'__start__': '00000000000000000000000000000001.ab89befb52cc0e91e106ef7f500ea033'}}, 'pending_sends': [], 'current_tasks': {}}, metadata={'source': 'loop', 'writes': None, 'step': 0}, parent_config={'configurable': {'thread_id': '1', 'checkpoint_ns': '', 'checkpoint_id': '1ef55f2a-2a50-6812-bfff-34e3be35d6f2'}}, pending_writes=None),
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-13-5) CheckpointTuple(config={'configurable': {'thread_id': '1', 'checkpoint_ns': '', 'checkpoint_id': '1ef55f2a-2a50-6812-bfff-34e3be35d6f2'}}, checkpoint={'v': 1, 'ts': '2024-08-09T01:56:47.094575+00:00', 'id': '1ef55f2a-2a50-6812-bfff-34e3be35d6f2', 'channel_values': {'messages': [], '__start__': {'messages': [['human', "what's the weather in sf"]]}}, 'channel_versions': {'__start__': '00000000000000000000000000000001.ab89befb52cc0e91e106ef7f500ea033'}, 'versions_seen': {'__input__': {}}, 'pending_sends': [], 'current_tasks': {}}, metadata={'source': 'input', 'writes': {'messages': [['human', "what's the weather in sf"]]}, 'step': -1}, parent_config=None, pending_writes=None)]

```


## Use async connection[¶](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#use-async-connection "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-14-1)async with AsyncRedisSaver.from_conn_info(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-14-2)  host="localhost", port=6379, db=0
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-14-3)) as checkpointer:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-14-4)  graph = create_react_agent(model, tools=tools, checkpointer=checkpointer)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-14-5)  config = {"configurable": {"thread_id": "2"}}
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-14-6)  res = await graph.ainvoke(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-14-7)    {"messages": [("human", "what's the weather in nyc")]}, config
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-14-8)  )
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-14-9)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-14-10)  latest_checkpoint = await checkpointer.aget(config)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-14-11)  latest_checkpoint_tuple = await checkpointer.aget_tuple(config)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-14-12)  checkpoint_tuples = [c async for c in checkpointer.alist(config)]

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-15-1)latest_checkpoint

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-16-1){'v': 1,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-16-2) 'ts': '2024-08-09T01:56:49.503241+00:00',
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-16-3) 'id': '1ef55f2a-4149-61ea-8003-dc5506862287',
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-16-4) 'channel_values': {'messages': [HumanMessage(content="what's the weather in nyc", id='5a106e79-a617-4707-839f-134d4e4b762a'),
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-16-5)  AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_TvPLLyhuQQN99EcZc8SzL8x9', 'function': {'arguments': '{"city":"nyc"}', 'name': 'get_weather'}, 'type': 'function'}]}, response_metadata={'token_usage': {'completion_tokens': 15, 'prompt_tokens': 58, 'total_tokens': 73}, 'model_name': 'gpt-4o-mini', 'system_fingerprint': 'fp_48196bc67a', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-0d6fa3b4-cace-41a8-b025-d01d16f6bbe9-0', tool_calls=[{'name': 'get_weather', 'args': {'city': 'nyc'}, 'id': 'call_TvPLLyhuQQN99EcZc8SzL8x9', 'type': 'tool_call'}], usage_metadata={'input_tokens': 58, 'output_tokens': 15, 'total_tokens': 73}),
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-16-6)  ToolMessage(content='It might be cloudy in nyc', name='get_weather', id='922124bd-d3b0-4929-a996-a75d842b8b44', tool_call_id='call_TvPLLyhuQQN99EcZc8SzL8x9'),
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-16-7)  AIMessage(content='The weather in NYC might be cloudy.', response_metadata={'token_usage': {'completion_tokens': 9, 'prompt_tokens': 88, 'total_tokens': 97}, 'model_name': 'gpt-4o-mini', 'system_fingerprint': 'fp_48196bc67a', 'finish_reason': 'stop', 'logprobs': None}, id='run-69a10e66-d61f-475e-b7de-a1ecd08a6c3a-0', usage_metadata={'input_tokens': 88, 'output_tokens': 9, 'total_tokens': 97})],
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-16-8) 'agent': 'agent'},
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-16-9) 'channel_versions': {'__start__': '00000000000000000000000000000002.',
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-16-10) 'messages': '00000000000000000000000000000005.2cb29d082da6435a7528b4c917fd0c28',
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-16-11) 'start:agent': '00000000000000000000000000000003.',
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-16-12) 'agent': '00000000000000000000000000000005.065d90dd7f7cd091f0233855210bb2af',
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-16-13) 'branch:agent:should_continue:tools': '00000000000000000000000000000004.',
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-16-14) 'tools': '00000000000000000000000000000005.'},
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-16-15) 'versions_seen': {'__input__': {},
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-16-16) '__start__': {'__start__': '00000000000000000000000000000001.0e148ae3debe753278387e84f786e863'},
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-16-17) 'agent': {'start:agent': '00000000000000000000000000000002.d6f25946c3108fc12f27abbcf9b4cedc',
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-16-18)  'tools': '00000000000000000000000000000004.022986cd20ae85c77ea298a383f69ba8'},
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-16-19) 'tools': {'branch:agent:should_continue:tools': '00000000000000000000000000000003.065d90dd7f7cd091f0233855210bb2af'}},
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-16-20) 'pending_sends': [],
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-16-21) 'current_tasks': {}}

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-17-1)latest_checkpoint_tuple

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-18-1)CheckpointTuple(config={'configurable': {'thread_id': '2', 'checkpoint_ns': '', 'checkpoint_id': '1ef55f2a-4149-61ea-8003-dc5506862287'}}, checkpoint={'v': 1, 'ts': '2024-08-09T01:56:49.503241+00:00', 'id': '1ef55f2a-4149-61ea-8003-dc5506862287', 'channel_values': {'messages': [HumanMessage(content="what's the weather in nyc", id='5a106e79-a617-4707-839f-134d4e4b762a'), AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_TvPLLyhuQQN99EcZc8SzL8x9', 'function': {'arguments': '{"city":"nyc"}', 'name': 'get_weather'}, 'type': 'function'}]}, response_metadata={'token_usage': {'completion_tokens': 15, 'prompt_tokens': 58, 'total_tokens': 73}, 'model_name': 'gpt-4o-mini', 'system_fingerprint': 'fp_48196bc67a', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-0d6fa3b4-cace-41a8-b025-d01d16f6bbe9-0', tool_calls=[{'name': 'get_weather', 'args': {'city': 'nyc'}, 'id': 'call_TvPLLyhuQQN99EcZc8SzL8x9', 'type': 'tool_call'}], usage_metadata={'input_tokens': 58, 'output_tokens': 15, 'total_tokens': 73}), ToolMessage(content='It might be cloudy in nyc', name='get_weather', id='922124bd-d3b0-4929-a996-a75d842b8b44', tool_call_id='call_TvPLLyhuQQN99EcZc8SzL8x9'), AIMessage(content='The weather in NYC might be cloudy.', response_metadata={'token_usage': {'completion_tokens': 9, 'prompt_tokens': 88, 'total_tokens': 97}, 'model_name': 'gpt-4o-mini', 'system_fingerprint': 'fp_48196bc67a', 'finish_reason': 'stop', 'logprobs': None}, id='run-69a10e66-d61f-475e-b7de-a1ecd08a6c3a-0', usage_metadata={'input_tokens': 88, 'output_tokens': 9, 'total_tokens': 97})], 'agent': 'agent'}, 'channel_versions': {'__start__': '00000000000000000000000000000002.', 'messages': '00000000000000000000000000000005.2cb29d082da6435a7528b4c917fd0c28', 'start:agent': '00000000000000000000000000000003.', 'agent': '00000000000000000000000000000005.065d90dd7f7cd091f0233855210bb2af', 'branch:agent:should_continue:tools': '00000000000000000000000000000004.', 'tools': '00000000000000000000000000000005.'}, 'versions_seen': {'__input__': {}, '__start__': {'__start__': '00000000000000000000000000000001.0e148ae3debe753278387e84f786e863'}, 'agent': {'start:agent': '00000000000000000000000000000002.d6f25946c3108fc12f27abbcf9b4cedc', 'tools': '00000000000000000000000000000004.022986cd20ae85c77ea298a383f69ba8'}, 'tools': {'branch:agent:should_continue:tools': '00000000000000000000000000000003.065d90dd7f7cd091f0233855210bb2af'}}, 'pending_sends': [], 'current_tasks': {}}, metadata={'source': 'loop', 'writes': {'agent': {'messages': [AIMessage(content='The weather in NYC might be cloudy.', response_metadata={'token_usage': {'completion_tokens': 9, 'prompt_tokens': 88, 'total_tokens': 97}, 'model_name': 'gpt-4o-mini', 'system_fingerprint': 'fp_48196bc67a', 'finish_reason': 'stop', 'logprobs': None}, id='run-69a10e66-d61f-475e-b7de-a1ecd08a6c3a-0', usage_metadata={'input_tokens': 88, 'output_tokens': 9, 'total_tokens': 97})]}}, 'step': 3}, parent_config={'configurable': {'thread_id': '2', 'checkpoint_ns': '', 'checkpoint_id': '1ef55f2a-3d07-647e-8002-b5e4d28c00c9'}}, pending_writes=[])

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-19-1)checkpoint_tuples

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-20-1)[CheckpointTuple(config={'configurable': {'thread_id': '2', 'checkpoint_ns': '', 'checkpoint_id': '1ef55f2a-4149-61ea-8003-dc5506862287'}}, checkpoint={'v': 1, 'ts': '2024-08-09T01:56:49.503241+00:00', 'id': '1ef55f2a-4149-61ea-8003-dc5506862287', 'channel_values': {'messages': [HumanMessage(content="what's the weather in nyc", id='5a106e79-a617-4707-839f-134d4e4b762a'), AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_TvPLLyhuQQN99EcZc8SzL8x9', 'function': {'arguments': '{"city":"nyc"}', 'name': 'get_weather'}, 'type': 'function'}]}, response_metadata={'token_usage': {'completion_tokens': 15, 'prompt_tokens': 58, 'total_tokens': 73}, 'model_name': 'gpt-4o-mini', 'system_fingerprint': 'fp_48196bc67a', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-0d6fa3b4-cace-41a8-b025-d01d16f6bbe9-0', tool_calls=[{'name': 'get_weather', 'args': {'city': 'nyc'}, 'id': 'call_TvPLLyhuQQN99EcZc8SzL8x9', 'type': 'tool_call'}], usage_metadata={'input_tokens': 58, 'output_tokens': 15, 'total_tokens': 73}), ToolMessage(content='It might be cloudy in nyc', name='get_weather', id='922124bd-d3b0-4929-a996-a75d842b8b44', tool_call_id='call_TvPLLyhuQQN99EcZc8SzL8x9'), AIMessage(content='The weather in NYC might be cloudy.', response_metadata={'token_usage': {'completion_tokens': 9, 'prompt_tokens': 88, 'total_tokens': 97}, 'model_name': 'gpt-4o-mini', 'system_fingerprint': 'fp_48196bc67a', 'finish_reason': 'stop', 'logprobs': None}, id='run-69a10e66-d61f-475e-b7de-a1ecd08a6c3a-0', usage_metadata={'input_tokens': 88, 'output_tokens': 9, 'total_tokens': 97})], 'agent': 'agent'}, 'channel_versions': {'__start__': '00000000000000000000000000000002.', 'messages': '00000000000000000000000000000005.2cb29d082da6435a7528b4c917fd0c28', 'start:agent': '00000000000000000000000000000003.', 'agent': '00000000000000000000000000000005.065d90dd7f7cd091f0233855210bb2af', 'branch:agent:should_continue:tools': '00000000000000000000000000000004.', 'tools': '00000000000000000000000000000005.'}, 'versions_seen': {'__input__': {}, '__start__': {'__start__': '00000000000000000000000000000001.0e148ae3debe753278387e84f786e863'}, 'agent': {'start:agent': '00000000000000000000000000000002.d6f25946c3108fc12f27abbcf9b4cedc', 'tools': '00000000000000000000000000000004.022986cd20ae85c77ea298a383f69ba8'}, 'tools': {'branch:agent:should_continue:tools': '00000000000000000000000000000003.065d90dd7f7cd091f0233855210bb2af'}}, 'pending_sends': [], 'current_tasks': {}}, metadata={'source': 'loop', 'writes': {'agent': {'messages': [AIMessage(content='The weather in NYC might be cloudy.', response_metadata={'token_usage': {'completion_tokens': 9, 'prompt_tokens': 88, 'total_tokens': 97}, 'model_name': 'gpt-4o-mini', 'system_fingerprint': 'fp_48196bc67a', 'finish_reason': 'stop', 'logprobs': None}, id='run-69a10e66-d61f-475e-b7de-a1ecd08a6c3a-0', usage_metadata={'input_tokens': 88, 'output_tokens': 9, 'total_tokens': 97})]}}, 'step': 3}, parent_config={'configurable': {'thread_id': '2', 'checkpoint_ns': '', 'checkpoint_id': '1ef55f2a-3d07-647e-8002-b5e4d28c00c9'}}, pending_writes=None),
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-20-2) CheckpointTuple(config={'configurable': {'thread_id': '2', 'checkpoint_ns': '', 'checkpoint_id': '1ef55f2a-3d07-647e-8002-b5e4d28c00c9'}}, checkpoint={'v': 1, 'ts': '2024-08-09T01:56:49.056860+00:00', 'id': '1ef55f2a-3d07-647e-8002-b5e4d28c00c9', 'channel_values': {'messages': [HumanMessage(content="what's the weather in nyc", id='5a106e79-a617-4707-839f-134d4e4b762a'), AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_TvPLLyhuQQN99EcZc8SzL8x9', 'function': {'arguments': '{"city":"nyc"}', 'name': 'get_weather'}, 'type': 'function'}]}, response_metadata={'token_usage': {'completion_tokens': 15, 'prompt_tokens': 58, 'total_tokens': 73}, 'model_name': 'gpt-4o-mini', 'system_fingerprint': 'fp_48196bc67a', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-0d6fa3b4-cace-41a8-b025-d01d16f6bbe9-0', tool_calls=[{'name': 'get_weather', 'args': {'city': 'nyc'}, 'id': 'call_TvPLLyhuQQN99EcZc8SzL8x9', 'type': 'tool_call'}], usage_metadata={'input_tokens': 58, 'output_tokens': 15, 'total_tokens': 73}), ToolMessage(content='It might be cloudy in nyc', name='get_weather', id='922124bd-d3b0-4929-a996-a75d842b8b44', tool_call_id='call_TvPLLyhuQQN99EcZc8SzL8x9')], 'tools': 'tools'}, 'channel_versions': {'__start__': '00000000000000000000000000000002.', 'messages': '00000000000000000000000000000004.07964a3a545f9ff95545db45a9753d11', 'start:agent': '00000000000000000000000000000003.', 'agent': '00000000000000000000000000000004.', 'branch:agent:should_continue:tools': '00000000000000000000000000000004.', 'tools': '00000000000000000000000000000004.022986cd20ae85c77ea298a383f69ba8'}, 'versions_seen': {'__input__': {}, '__start__': {'__start__': '00000000000000000000000000000001.0e148ae3debe753278387e84f786e863'}, 'agent': {'start:agent': '00000000000000000000000000000002.d6f25946c3108fc12f27abbcf9b4cedc'}, 'tools': {'branch:agent:should_continue:tools': '00000000000000000000000000000003.065d90dd7f7cd091f0233855210bb2af'}}, 'pending_sends': [], 'current_tasks': {}}, metadata={'source': 'loop', 'writes': {'tools': {'messages': [ToolMessage(content='It might be cloudy in nyc', name='get_weather', id='922124bd-d3b0-4929-a996-a75d842b8b44', tool_call_id='call_TvPLLyhuQQN99EcZc8SzL8x9')]}}, 'step': 2}, parent_config={'configurable': {'thread_id': '2', 'checkpoint_ns': '', 'checkpoint_id': '1ef55f2a-3cf9-6996-8001-88dab066840d'}}, pending_writes=None),
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-20-3) CheckpointTuple(config={'configurable': {'thread_id': '2', 'checkpoint_ns': '', 'checkpoint_id': '1ef55f2a-3cf9-6996-8001-88dab066840d'}}, checkpoint={'v': 1, 'ts': '2024-08-09T01:56:49.051234+00:00', 'id': '1ef55f2a-3cf9-6996-8001-88dab066840d', 'channel_values': {'messages': [HumanMessage(content="what's the weather in nyc", id='5a106e79-a617-4707-839f-134d4e4b762a'), AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_TvPLLyhuQQN99EcZc8SzL8x9', 'function': {'arguments': '{"city":"nyc"}', 'name': 'get_weather'}, 'type': 'function'}]}, response_metadata={'token_usage': {'completion_tokens': 15, 'prompt_tokens': 58, 'total_tokens': 73}, 'model_name': 'gpt-4o-mini', 'system_fingerprint': 'fp_48196bc67a', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-0d6fa3b4-cace-41a8-b025-d01d16f6bbe9-0', tool_calls=[{'name': 'get_weather', 'args': {'city': 'nyc'}, 'id': 'call_TvPLLyhuQQN99EcZc8SzL8x9', 'type': 'tool_call'}], usage_metadata={'input_tokens': 58, 'output_tokens': 15, 'total_tokens': 73})], 'agent': 'agent', 'branch:agent:should_continue:tools': 'agent'}, 'channel_versions': {'__start__': '00000000000000000000000000000002.', 'messages': '00000000000000000000000000000003.cc96d93b1afbd1b69d53851320670b97', 'start:agent': '00000000000000000000000000000003.', 'agent': '00000000000000000000000000000003.065d90dd7f7cd091f0233855210bb2af', 'branch:agent:should_continue:tools': '00000000000000000000000000000003.065d90dd7f7cd091f0233855210bb2af'}, 'versions_seen': {'__input__': {}, '__start__': {'__start__': '00000000000000000000000000000001.0e148ae3debe753278387e84f786e863'}, 'agent': {'start:agent': '00000000000000000000000000000002.d6f25946c3108fc12f27abbcf9b4cedc'}}, 'pending_sends': [], 'current_tasks': {}}, metadata={'source': 'loop', 'writes': {'agent': {'messages': [AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_TvPLLyhuQQN99EcZc8SzL8x9', 'function': {'arguments': '{"city":"nyc"}', 'name': 'get_weather'}, 'type': 'function'}]}, response_metadata={'token_usage': {'completion_tokens': 15, 'prompt_tokens': 58, 'total_tokens': 73}, 'model_name': 'gpt-4o-mini', 'system_fingerprint': 'fp_48196bc67a', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-0d6fa3b4-cace-41a8-b025-d01d16f6bbe9-0', tool_calls=[{'name': 'get_weather', 'args': {'city': 'nyc'}, 'id': 'call_TvPLLyhuQQN99EcZc8SzL8x9', 'type': 'tool_call'}], usage_metadata={'input_tokens': 58, 'output_tokens': 15, 'total_tokens': 73})]}}, 'step': 1}, parent_config={'configurable': {'thread_id': '2', 'checkpoint_ns': '', 'checkpoint_id': '1ef55f2a-36a6-6788-8000-9efe1769f8c1'}}, pending_writes=None),
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-20-4) CheckpointTuple(config={'configurable': {'thread_id': '2', 'checkpoint_ns': '', 'checkpoint_id': '1ef55f2a-36a6-6788-8000-9efe1769f8c1'}}, checkpoint={'v': 1, 'ts': '2024-08-09T01:56:48.388067+00:00', 'id': '1ef55f2a-36a6-6788-8000-9efe1769f8c1', 'channel_values': {'messages': [HumanMessage(content="what's the weather in nyc", id='5a106e79-a617-4707-839f-134d4e4b762a')], 'start:agent': '__start__'}, 'channel_versions': {'__start__': '00000000000000000000000000000002.', 'messages': '00000000000000000000000000000002.a6994b785a651d88df51020401745af8', 'start:agent': '00000000000000000000000000000002.d6f25946c3108fc12f27abbcf9b4cedc'}, 'versions_seen': {'__input__': {}, '__start__': {'__start__': '00000000000000000000000000000001.0e148ae3debe753278387e84f786e863'}}, 'pending_sends': [], 'current_tasks': {}}, metadata={'source': 'loop', 'writes': None, 'step': 0}, parent_config={'configurable': {'thread_id': '2', 'checkpoint_ns': '', 'checkpoint_id': '1ef55f2a-36a3-6614-bfff-05dafa02b4d7'}}, pending_writes=None),
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__codelineno-20-5) CheckpointTuple(config={'configurable': {'thread_id': '2', 'checkpoint_ns': '', 'checkpoint_id': '1ef55f2a-36a3-6614-bfff-05dafa02b4d7'}}, checkpoint={'v': 1, 'ts': '2024-08-09T01:56:48.386807+00:00', 'id': '1ef55f2a-36a3-6614-bfff-05dafa02b4d7', 'channel_values': {'messages': [], '__start__': {'messages': [['human', "what's the weather in nyc"]]}}, 'channel_versions': {'__start__': '00000000000000000000000000000001.0e148ae3debe753278387e84f786e863'}, 'versions_seen': {'__input__': {}}, 'pending_sends': [], 'current_tasks': {}}, metadata={'source': 'input', 'writes': {'messages': [['human', "what's the weather in nyc"]]}, 'step': -1}, parent_config=None, pending_writes=None)]

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to use MongoDB checkpointer for persistence  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/) [ Next  How to add thread-level persistence (functional API)  ](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
