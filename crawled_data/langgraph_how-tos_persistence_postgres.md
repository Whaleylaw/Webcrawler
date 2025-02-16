---
url: https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#how-to-use-postgres-checkpointer-for-persistence)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to use Postgres checkpointer for persistence 

[ ](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/?q= "Share")

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
            * How to use Postgres checkpointer for persistence  [ How to use Postgres checkpointer for persistence  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#setup)
              * [ Define model and tools for the graph  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#define-model-and-tools-for-the-graph)
              * [ Use sync connection  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#use-sync-connection)
                * [ With a connection pool  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#with-a-connection-pool)
                * [ With a connection  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#with-a-connection)
                * [ With a connection string  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#with-a-connection-string)
              * [ Use async connection  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#use-async-connection)
                * [ With a connection pool  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#with-a-connection-pool_1)
                * [ With a connection  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#with-a-connection_1)
                * [ With a connection string  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#with-a-connection-string_1)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#setup)
  * [ Define model and tools for the graph  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#define-model-and-tools-for-the-graph)
  * [ Use sync connection  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#use-sync-connection)
    * [ With a connection pool  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#with-a-connection-pool)
    * [ With a connection  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#with-a-connection)
    * [ With a connection string  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#with-a-connection-string)
  * [ Use async connection  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#use-async-connection)
    * [ With a connection pool  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#with-a-connection-pool_1)
    * [ With a connection  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#with-a-connection_1)
    * [ With a connection string  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#with-a-connection-string_1)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Persistence  ](https://langchain-ai.github.io/langgraph/how-tos#persistence)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/persistence_postgres.ipynb "Edit this page")

# How to use Postgres checkpointer for persistence[¶](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#how-to-use-postgres-checkpointer-for-persistence "Permanent link")

Prerequisites

This guide assumes familiarity with the following: 

  * [ Persistence ](https://langchain-ai.github.io/langgraph/concepts/persistence/)
  * [ Postgresql ](https://www.postgresql.org/about/)



When creating LangGraph agents, you can also set them up so that they persist their state. This allows you to do things like interact with an agent multiple times and have it remember previous interactions.

This how-to guide shows how to use `Postgres` as the backend for persisting checkpoint state using the `langgraph-checkpoint-postgres`[](https://github.com/langchain-ai/langgraph/tree/main/libs/checkpoint-postgres) library.

For demonstration purposes we add persistence to the [pre-built create react agent](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent). 

In general, you can add a checkpointer to any custom graph that you build like this:

```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-0-1)fromlanggraph.graphimport StateGraph
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-0-2)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-0-3)builder = StateGraph(....)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-0-4)# ... define the graph
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-0-5)checkpointer = # postgres checkpointer (see examples below)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-0-6)graph = builder.compile(checkpointer=checkpointer)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-0-7)...

```


API Reference: [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph)

Setup

You need to run `.setup()` once on your checkpointer to initialize the database before you can use it.

## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#setup "Permanent link")

You will need access to a postgres instance. There are many resources online that can help you set up a postgres instance.

Next, let's install the required packages and set our API keys

```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-1-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-1-2)%pip install -U psycopg psycopg-pool langgraph langgraph-checkpoint-postgres

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-2-1)importgetpass
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-2-2)importos
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-2-3)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-2-4)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-2-5)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-2-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-2-7)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-2-8)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-2-9)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-2-10)_set_env("OPENAI_API_KEY")

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Define model and tools for the graph[¶](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#define-model-and-tools-for-the-graph "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-3-1)fromtypingimport Literal
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-3-2)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-3-3)fromlangchain_core.toolsimport tool
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-3-4)fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-3-5)fromlanggraph.prebuiltimport create_react_agent
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-3-6)fromlanggraph.checkpoint.postgresimport PostgresSaver
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-3-7)fromlanggraph.checkpoint.postgres.aioimport AsyncPostgresSaver
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-3-8)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-3-9)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-3-10)@tool
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-3-11)defget_weather(city: Literal["nyc", "sf"]):
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-3-12)"""Use this to get weather information."""
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-3-13)  if city == "nyc":
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-3-14)    return "It might be cloudy in nyc"
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-3-15)  elif city == "sf":
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-3-16)    return "It's always sunny in sf"
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-3-17)  else:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-3-18)    raise AssertionError("Unknown city")
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-3-19)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-3-20)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-3-21)tools = [get_weather]
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-3-22)model = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

```


API Reference: [tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html) | [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html) | [create_react_agent](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent) | [PostgresSaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.PostgresSaver) | [AsyncPostgresSaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncPostgresSaver)

## Use sync connection[¶](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#use-sync-connection "Permanent link")

This sets up a synchronous connection to the database. 

Synchronous connections execute operations in a blocking manner, meaning each operation waits for completion before moving to the next one. The `DB_URI` is the database connection URI, with the protocol used for connecting to a PostgreSQL database, authentication, and host where database is running. The connection_kwargs dictionary defines additional parameters for the database connection.

```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-4-1)DB_URI = "postgresql://postgres:postgres@localhost:5442/postgres?sslmode=disable"

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-5-1)connection_kwargs = {
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-5-2)  "autocommit": True,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-5-3)  "prepare_threshold": 0,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-5-4)}

```


### With a connection pool[¶](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#with-a-connection-pool "Permanent link")

This manages a pool of reusable database connections: - Advantages: Efficient resource utilization, improved performance for frequent connections - Best for: Applications with many short-lived database operations

```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-6-1)frompsycopg_poolimport ConnectionPool
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-6-2)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-6-3)with ConnectionPool(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-6-4)  # Example configuration
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-6-5)  conninfo=DB_URI,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-6-6)  max_size=20,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-6-7)  kwargs=connection_kwargs,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-6-8)) as pool:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-6-9)  checkpointer = PostgresSaver(pool)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-6-10)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-6-11)  # NOTE: you need to call .setup() the first time you're using your checkpointer
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-6-12)  checkpointer.setup()
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-6-13)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-6-14)  graph = create_react_agent(model, tools=tools, checkpointer=checkpointer)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-6-15)  config = {"configurable": {"thread_id": "1"}}
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-6-16)  res = graph.invoke({"messages": [("human", "what's the weather in sf")]}, config)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-6-17)  checkpoint = checkpointer.get(config)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-7-1)res

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-8-1){'messages': [HumanMessage(content="what's the weather in sf", id='735b7deb-b0fe-4ad5-8920-2a3c69bbe9f7'),
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-8-2) AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_lJHMDYgfgRdiEAGfFsEhqqKV', 'function': {'arguments': '{"city":"sf"}', 'name': 'get_weather'}, 'type': 'function'}]}, response_metadata={'token_usage': {'completion_tokens': 14, 'prompt_tokens': 57, 'total_tokens': 71}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_48196bc67a', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-c56b3e04-08a9-4a59-b3f5-ee52d0ef0656-0', tool_calls=[{'name': 'get_weather', 'args': {'city': 'sf'}, 'id': 'call_lJHMDYgfgRdiEAGfFsEhqqKV', 'type': 'tool_call'}], usage_metadata={'input_tokens': 57, 'output_tokens': 14, 'total_tokens': 71}),
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-8-3) ToolMessage(content="It's always sunny in sf", name='get_weather', id='0644bf7b-4d1b-4ebe-afa1-d2169ccce582', tool_call_id='call_lJHMDYgfgRdiEAGfFsEhqqKV'),
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-8-4) AIMessage(content='The weather in San Francisco is always sunny!', response_metadata={'token_usage': {'completion_tokens': 10, 'prompt_tokens': 84, 'total_tokens': 94}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_48196bc67a', 'finish_reason': 'stop', 'logprobs': None}, id='run-1ed9b8d0-9b50-4b87-b3a2-9860f51e9fd1-0', usage_metadata={'input_tokens': 84, 'output_tokens': 10, 'total_tokens': 94})]}

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-9-1)checkpoint

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-10-1){'v': 1,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-10-2) 'id': '1ef559b7-3b19-6ce8-8003-18d0f60634be',
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-10-3) 'ts': '2024-08-08T15:32:42.108605+00:00',
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-10-4) 'current_tasks': {},
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-10-5) 'pending_sends': [],
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-10-6) 'versions_seen': {'agent': {'tools': '00000000000000000000000000000004.022986cd20ae85c77ea298a383f69ba8',
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-10-7)  'start:agent': '00000000000000000000000000000002.d6f25946c3108fc12f27abbcf9b4cedc'},
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-10-8) 'tools': {'branch:agent:should_continue:tools': '00000000000000000000000000000003.065d90dd7f7cd091f0233855210bb2af'},
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-10-9) '__input__': {},
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-10-10) '__start__': {'__start__': '00000000000000000000000000000001.ab89befb52cc0e91e106ef7f500ea033'}},
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-10-11) 'channel_versions': {'agent': '00000000000000000000000000000005.065d90dd7f7cd091f0233855210bb2af',
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-10-12) 'tools': '00000000000000000000000000000005.',
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-10-13) 'messages': '00000000000000000000000000000005.b9adc75836c78af94af1d6811340dd13',
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-10-14) '__start__': '00000000000000000000000000000002.',
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-10-15) 'start:agent': '00000000000000000000000000000003.',
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-10-16) 'branch:agent:should_continue:tools': '00000000000000000000000000000004.'},
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-10-17) 'channel_values': {'agent': 'agent',
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-10-18) 'messages': [HumanMessage(content="what's the weather in sf", id='735b7deb-b0fe-4ad5-8920-2a3c69bbe9f7'),
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-10-19)  AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_lJHMDYgfgRdiEAGfFsEhqqKV', 'function': {'arguments': '{"city":"sf"}', 'name': 'get_weather'}, 'type': 'function'}]}, response_metadata={'token_usage': {'completion_tokens': 14, 'prompt_tokens': 57, 'total_tokens': 71}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_48196bc67a', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-c56b3e04-08a9-4a59-b3f5-ee52d0ef0656-0', tool_calls=[{'name': 'get_weather', 'args': {'city': 'sf'}, 'id': 'call_lJHMDYgfgRdiEAGfFsEhqqKV', 'type': 'tool_call'}], usage_metadata={'input_tokens': 57, 'output_tokens': 14, 'total_tokens': 71}),
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-10-20)  ToolMessage(content="It's always sunny in sf", name='get_weather', id='0644bf7b-4d1b-4ebe-afa1-d2169ccce582', tool_call_id='call_lJHMDYgfgRdiEAGfFsEhqqKV'),
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-10-21)  AIMessage(content='The weather in San Francisco is always sunny!', response_metadata={'token_usage': {'completion_tokens': 10, 'prompt_tokens': 84, 'total_tokens': 94}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_48196bc67a', 'finish_reason': 'stop', 'logprobs': None}, id='run-1ed9b8d0-9b50-4b87-b3a2-9860f51e9fd1-0', usage_metadata={'input_tokens': 84, 'output_tokens': 10, 'total_tokens': 94})]}}

```


### With a connection[¶](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#with-a-connection "Permanent link")

This creates a single, dedicated connection to the database: - Advantages: Simple to use, suitable for longer transactions - Best for: Applications with fewer, longer-lived database operations

```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-11-1)frompsycopgimport Connection
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-11-2)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-11-3)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-11-4)with Connection.connect(DB_URI, **connection_kwargs) as conn:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-11-5)  checkpointer = PostgresSaver(conn)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-11-6)  # NOTE: you need to call .setup() the first time you're using your checkpointer
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-11-7)  # checkpointer.setup()
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-11-8)  graph = create_react_agent(model, tools=tools, checkpointer=checkpointer)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-11-9)  config = {"configurable": {"thread_id": "2"}}
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-11-10)  res = graph.invoke({"messages": [("human", "what's the weather in sf")]}, config)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-11-11)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-11-12)  checkpoint_tuple = checkpointer.get_tuple(config)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-12-1)checkpoint_tuple

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-13-1)CheckpointTuple(config={'configurable': {'thread_id': '2', 'checkpoint_ns': '', 'checkpoint_id': '1ef559b7-4650-6bfc-8003-1c5488f19318'}}, checkpoint={'v': 1, 'id': '1ef559b7-4650-6bfc-8003-1c5488f19318', 'ts': '2024-08-08T15:32:43.284551+00:00', 'current_tasks': {}, 'pending_sends': [], 'versions_seen': {'agent': {'tools': '00000000000000000000000000000004.022986cd20ae85c77ea298a383f69ba8', 'start:agent': '00000000000000000000000000000002.d6f25946c3108fc12f27abbcf9b4cedc'}, 'tools': {'branch:agent:should_continue:tools': '00000000000000000000000000000003.065d90dd7f7cd091f0233855210bb2af'}, '__input__': {}, '__start__': {'__start__': '00000000000000000000000000000001.ab89befb52cc0e91e106ef7f500ea033'}}, 'channel_versions': {'agent': '00000000000000000000000000000005.065d90dd7f7cd091f0233855210bb2af', 'tools': '00000000000000000000000000000005.', 'messages': '00000000000000000000000000000005.af9f229d2c4e14f4866eb37f72ec39f6', '__start__': '00000000000000000000000000000002.', 'start:agent': '00000000000000000000000000000003.', 'branch:agent:should_continue:tools': '00000000000000000000000000000004.'}, 'channel_values': {'agent': 'agent', 'messages': [HumanMessage(content="what's the weather in sf", id='7a14f96c-2d88-454f-9520-0e0287a4abbb'), AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_NcL4dBTYu4kSPGMKdxztdpjN', 'function': {'arguments': '{"city":"sf"}', 'name': 'get_weather'}, 'type': 'function'}]}, response_metadata={'token_usage': {'completion_tokens': 14, 'prompt_tokens': 57, 'total_tokens': 71}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_48196bc67a', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-39adbf2c-36ef-40f6-9cad-8e1f8167fc19-0', tool_calls=[{'name': 'get_weather', 'args': {'city': 'sf'}, 'id': 'call_NcL4dBTYu4kSPGMKdxztdpjN', 'type': 'tool_call'}], usage_metadata={'input_tokens': 57, 'output_tokens': 14, 'total_tokens': 71}), ToolMessage(content="It's always sunny in sf", name='get_weather', id='c9f82354-3225-40a8-bf54-81f3e199043b', tool_call_id='call_NcL4dBTYu4kSPGMKdxztdpjN'), AIMessage(content='The weather in San Francisco is always sunny!', response_metadata={'token_usage': {'completion_tokens': 10, 'prompt_tokens': 84, 'total_tokens': 94}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_48196bc67a', 'finish_reason': 'stop', 'logprobs': None}, id='run-83888be3-d681-42ca-ad67-e2f5ee8550de-0', usage_metadata={'input_tokens': 84, 'output_tokens': 10, 'total_tokens': 94})]}}, metadata={'step': 3, 'source': 'loop', 'writes': {'agent': {'messages': [AIMessage(content='The weather in San Francisco is always sunny!', response_metadata={'logprobs': None, 'model_name': 'gpt-4o-mini-2024-07-18', 'token_usage': {'total_tokens': 94, 'prompt_tokens': 84, 'completion_tokens': 10}, 'finish_reason': 'stop', 'system_fingerprint': 'fp_48196bc67a'}, id='run-83888be3-d681-42ca-ad67-e2f5ee8550de-0', usage_metadata={'input_tokens': 84, 'output_tokens': 10, 'total_tokens': 94})]}}}, parent_config={'configurable': {'thread_id': '2', 'checkpoint_ns': '', 'checkpoint_id': '1ef559b7-4087-681a-8002-88a5738f76f1'}}, pending_writes=[])

```


### With a connection string[¶](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#with-a-connection-string "Permanent link")

This creates a connection based on a connection string: - Advantages: Simplicity, encapsulates connection details - Best for: Quick setup or when connection details are provided as a string

```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-14-1)with PostgresSaver.from_conn_string(DB_URI) as checkpointer:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-14-2)  graph = create_react_agent(model, tools=tools, checkpointer=checkpointer)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-14-3)  config = {"configurable": {"thread_id": "3"}}
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-14-4)  res = graph.invoke({"messages": [("human", "what's the weather in sf")]}, config)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-14-5)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-14-6)  checkpoint_tuples = list(checkpointer.list(config))

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-15-1)checkpoint_tuples

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-16-1)[CheckpointTuple(config={'configurable': {'thread_id': '3', 'checkpoint_ns': '', 'checkpoint_id': '1ef559b7-5024-6476-8003-cf0a750e6b37'}}, checkpoint={'v': 1, 'id': '1ef559b7-5024-6476-8003-cf0a750e6b37', 'ts': '2024-08-08T15:32:44.314900+00:00', 'current_tasks': {}, 'pending_sends': [], 'versions_seen': {'agent': {'tools': '00000000000000000000000000000004.022986cd20ae85c77ea298a383f69ba8', 'start:agent': '00000000000000000000000000000002.d6f25946c3108fc12f27abbcf9b4cedc'}, 'tools': {'branch:agent:should_continue:tools': '00000000000000000000000000000003.065d90dd7f7cd091f0233855210bb2af'}, '__input__': {}, '__start__': {'__start__': '00000000000000000000000000000001.ab89befb52cc0e91e106ef7f500ea033'}}, 'channel_versions': {'agent': '00000000000000000000000000000005.065d90dd7f7cd091f0233855210bb2af', 'tools': '00000000000000000000000000000005.', 'messages': '00000000000000000000000000000005.3f8b8d9923575b911e17157008ab75ac', '__start__': '00000000000000000000000000000002.', 'start:agent': '00000000000000000000000000000003.', 'branch:agent:should_continue:tools': '00000000000000000000000000000004.'}, 'channel_values': {'agent': 'agent', 'messages': [HumanMessage(content="what's the weather in sf", id='5bf79d15-6332-4bf5-89bd-ee192b31ed84'), AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_9y3q1BiwW7zGh2gk2faInTRk', 'function': {'arguments': '{"city":"sf"}', 'name': 'get_weather'}, 'type': 'function'}]}, response_metadata={'token_usage': {'completion_tokens': 14, 'prompt_tokens': 57, 'total_tokens': 71}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_507c9469a1', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-2958adc7-f6a4-415d-ade1-5ee77e0b9276-0', tool_calls=[{'name': 'get_weather', 'args': {'city': 'sf'}, 'id': 'call_9y3q1BiwW7zGh2gk2faInTRk', 'type': 'tool_call'}], usage_metadata={'input_tokens': 57, 'output_tokens': 14, 'total_tokens': 71}), ToolMessage(content="It's always sunny in sf", name='get_weather', id='cac4f90a-dc3e-4bfa-940f-1c630289a583', tool_call_id='call_9y3q1BiwW7zGh2gk2faInTRk'), AIMessage(content='The weather in San Francisco is always sunny!', response_metadata={'token_usage': {'completion_tokens': 10, 'prompt_tokens': 84, 'total_tokens': 94}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_48196bc67a', 'finish_reason': 'stop', 'logprobs': None}, id='run-97d3fb7a-3d2e-4090-84f4-dafdfe44553f-0', usage_metadata={'input_tokens': 84, 'output_tokens': 10, 'total_tokens': 94})]}}, metadata={'step': 3, 'source': 'loop', 'writes': {'agent': {'messages': [AIMessage(content='The weather in San Francisco is always sunny!', response_metadata={'logprobs': None, 'model_name': 'gpt-4o-mini-2024-07-18', 'token_usage': {'total_tokens': 94, 'prompt_tokens': 84, 'completion_tokens': 10}, 'finish_reason': 'stop', 'system_fingerprint': 'fp_48196bc67a'}, id='run-97d3fb7a-3d2e-4090-84f4-dafdfe44553f-0', usage_metadata={'input_tokens': 84, 'output_tokens': 10, 'total_tokens': 94})]}}}, parent_config={'configurable': {'thread_id': '3', 'checkpoint_ns': '', 'checkpoint_id': '1ef559b7-4b3d-6430-8002-b5c99d2eb4db'}}, pending_writes=None),
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-16-2) CheckpointTuple(config={'configurable': {'thread_id': '3', 'checkpoint_ns': '', 'checkpoint_id': '1ef559b7-4b3d-6430-8002-b5c99d2eb4db'}}, checkpoint={'v': 1, 'id': '1ef559b7-4b3d-6430-8002-b5c99d2eb4db', 'ts': '2024-08-08T15:32:43.800857+00:00', 'current_tasks': {}, 'pending_sends': [], 'versions_seen': {'agent': {'start:agent': '00000000000000000000000000000002.d6f25946c3108fc12f27abbcf9b4cedc'}, 'tools': {'branch:agent:should_continue:tools': '00000000000000000000000000000003.065d90dd7f7cd091f0233855210bb2af'}, '__input__': {}, '__start__': {'__start__': '00000000000000000000000000000001.ab89befb52cc0e91e106ef7f500ea033'}}, 'channel_versions': {'agent': '00000000000000000000000000000004.', 'tools': '00000000000000000000000000000004.022986cd20ae85c77ea298a383f69ba8', 'messages': '00000000000000000000000000000004.1195f50946feaedb0bae1fdbfadc806b', '__start__': '00000000000000000000000000000002.', 'start:agent': '00000000000000000000000000000003.', 'branch:agent:should_continue:tools': '00000000000000000000000000000004.'}, 'channel_values': {'tools': 'tools', 'messages': [HumanMessage(content="what's the weather in sf", id='5bf79d15-6332-4bf5-89bd-ee192b31ed84'), AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_9y3q1BiwW7zGh2gk2faInTRk', 'function': {'arguments': '{"city":"sf"}', 'name': 'get_weather'}, 'type': 'function'}]}, response_metadata={'token_usage': {'completion_tokens': 14, 'prompt_tokens': 57, 'total_tokens': 71}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_507c9469a1', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-2958adc7-f6a4-415d-ade1-5ee77e0b9276-0', tool_calls=[{'name': 'get_weather', 'args': {'city': 'sf'}, 'id': 'call_9y3q1BiwW7zGh2gk2faInTRk', 'type': 'tool_call'}], usage_metadata={'input_tokens': 57, 'output_tokens': 14, 'total_tokens': 71}), ToolMessage(content="It's always sunny in sf", name='get_weather', id='cac4f90a-dc3e-4bfa-940f-1c630289a583', tool_call_id='call_9y3q1BiwW7zGh2gk2faInTRk')]}}, metadata={'step': 2, 'source': 'loop', 'writes': {'tools': {'messages': [ToolMessage(content="It's always sunny in sf", name='get_weather', id='cac4f90a-dc3e-4bfa-940f-1c630289a583', tool_call_id='call_9y3q1BiwW7zGh2gk2faInTRk')]}}}, parent_config={'configurable': {'thread_id': '3', 'checkpoint_ns': '', 'checkpoint_id': '1ef559b7-4b30-6078-8001-eaf8c9bd8844'}}, pending_writes=None),
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-16-3) CheckpointTuple(config={'configurable': {'thread_id': '3', 'checkpoint_ns': '', 'checkpoint_id': '1ef559b7-4b30-6078-8001-eaf8c9bd8844'}}, checkpoint={'v': 1, 'id': '1ef559b7-4b30-6078-8001-eaf8c9bd8844', 'ts': '2024-08-08T15:32:43.795440+00:00', 'current_tasks': {}, 'pending_sends': [], 'versions_seen': {'agent': {'start:agent': '00000000000000000000000000000002.d6f25946c3108fc12f27abbcf9b4cedc'}, '__input__': {}, '__start__': {'__start__': '00000000000000000000000000000001.ab89befb52cc0e91e106ef7f500ea033'}}, 'channel_versions': {'agent': '00000000000000000000000000000003.065d90dd7f7cd091f0233855210bb2af', 'messages': '00000000000000000000000000000003.bab5fb3a70876f600f5f2fd46945ce5f', '__start__': '00000000000000000000000000000002.', 'start:agent': '00000000000000000000000000000003.', 'branch:agent:should_continue:tools': '00000000000000000000000000000003.065d90dd7f7cd091f0233855210bb2af'}, 'channel_values': {'agent': 'agent', 'messages': [HumanMessage(content="what's the weather in sf", id='5bf79d15-6332-4bf5-89bd-ee192b31ed84'), AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_9y3q1BiwW7zGh2gk2faInTRk', 'function': {'arguments': '{"city":"sf"}', 'name': 'get_weather'}, 'type': 'function'}]}, response_metadata={'token_usage': {'completion_tokens': 14, 'prompt_tokens': 57, 'total_tokens': 71}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_507c9469a1', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-2958adc7-f6a4-415d-ade1-5ee77e0b9276-0', tool_calls=[{'name': 'get_weather', 'args': {'city': 'sf'}, 'id': 'call_9y3q1BiwW7zGh2gk2faInTRk', 'type': 'tool_call'}], usage_metadata={'input_tokens': 57, 'output_tokens': 14, 'total_tokens': 71})], 'branch:agent:should_continue:tools': 'agent'}}, metadata={'step': 1, 'source': 'loop', 'writes': {'agent': {'messages': [AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_9y3q1BiwW7zGh2gk2faInTRk', 'type': 'function', 'function': {'name': 'get_weather', 'arguments': '{"city":"sf"}'}}]}, response_metadata={'logprobs': None, 'model_name': 'gpt-4o-mini-2024-07-18', 'token_usage': {'total_tokens': 71, 'prompt_tokens': 57, 'completion_tokens': 14}, 'finish_reason': 'tool_calls', 'system_fingerprint': 'fp_507c9469a1'}, id='run-2958adc7-f6a4-415d-ade1-5ee77e0b9276-0', tool_calls=[{'name': 'get_weather', 'args': {'city': 'sf'}, 'id': 'call_9y3q1BiwW7zGh2gk2faInTRk', 'type': 'tool_call'}], usage_metadata={'input_tokens': 57, 'output_tokens': 14, 'total_tokens': 71})]}}}, parent_config={'configurable': {'thread_id': '3', 'checkpoint_ns': '', 'checkpoint_id': '1ef559b7-46d7-6116-8000-8976b7c89a2f'}}, pending_writes=None),
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-16-4) CheckpointTuple(config={'configurable': {'thread_id': '3', 'checkpoint_ns': '', 'checkpoint_id': '1ef559b7-46d7-6116-8000-8976b7c89a2f'}}, checkpoint={'v': 1, 'id': '1ef559b7-46d7-6116-8000-8976b7c89a2f', 'ts': '2024-08-08T15:32:43.339573+00:00', 'current_tasks': {}, 'pending_sends': [], 'versions_seen': {'__input__': {}, '__start__': {'__start__': '00000000000000000000000000000001.ab89befb52cc0e91e106ef7f500ea033'}}, 'channel_versions': {'messages': '00000000000000000000000000000002.ba0c90d32863686481f7fe5eab9ecdf0', '__start__': '00000000000000000000000000000002.', 'start:agent': '00000000000000000000000000000002.d6f25946c3108fc12f27abbcf9b4cedc'}, 'channel_values': {'messages': [HumanMessage(content="what's the weather in sf", id='5bf79d15-6332-4bf5-89bd-ee192b31ed84')], 'start:agent': '__start__'}}, metadata={'step': 0, 'source': 'loop', 'writes': None}, parent_config={'configurable': {'thread_id': '3', 'checkpoint_ns': '', 'checkpoint_id': '1ef559b7-46ce-6c64-bfff-ef7fe2663573'}}, pending_writes=None),
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-16-5) CheckpointTuple(config={'configurable': {'thread_id': '3', 'checkpoint_ns': '', 'checkpoint_id': '1ef559b7-46ce-6c64-bfff-ef7fe2663573'}}, checkpoint={'v': 1, 'id': '1ef559b7-46ce-6c64-bfff-ef7fe2663573', 'ts': '2024-08-08T15:32:43.336188+00:00', 'current_tasks': {}, 'pending_sends': [], 'versions_seen': {'__input__': {}}, 'channel_versions': {'__start__': '00000000000000000000000000000001.ab89befb52cc0e91e106ef7f500ea033'}, 'channel_values': {'__start__': {'messages': [['human', "what's the weather in sf"]]}}}, metadata={'step': -1, 'source': 'input', 'writes': {'messages': [['human', "what's the weather in sf"]]}}, parent_config=None, pending_writes=None)]

```


## Use async connection[¶](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#use-async-connection "Permanent link")

This sets up an asynchronous connection to the database. 

Async connections allow non-blocking database operations. This means other parts of your application can continue running while waiting for database operations to complete. It's particularly useful in high-concurrency scenarios or when dealing with I/O-bound operations.

### With a connection pool[¶](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#with-a-connection-pool_1 "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-17-1)frompsycopg_poolimport AsyncConnectionPool
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-17-2)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-17-3)async with AsyncConnectionPool(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-17-4)  # Example configuration
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-17-5)  conninfo=DB_URI,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-17-6)  max_size=20,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-17-7)  kwargs=connection_kwargs,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-17-8)) as pool:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-17-9)  checkpointer = AsyncPostgresSaver(pool)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-17-10)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-17-11)  # NOTE: you need to call .setup() the first time you're using your checkpointer
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-17-12)  await checkpointer.setup()
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-17-13)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-17-14)  graph = create_react_agent(model, tools=tools, checkpointer=checkpointer)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-17-15)  config = {"configurable": {"thread_id": "4"}}
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-17-16)  res = await graph.ainvoke(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-17-17)    {"messages": [("human", "what's the weather in nyc")]}, config
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-17-18)  )
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-17-19)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-17-20)  checkpoint = await checkpointer.aget(config)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-18-1)checkpoint

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-19-1){'v': 1,
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-19-2) 'id': '1ef559b7-5cc9-6460-8003-8655824c0944',
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-19-3) 'ts': '2024-08-08T15:32:45.640793+00:00',
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-19-4) 'current_tasks': {},
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-19-5) 'pending_sends': [],
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-19-6) 'versions_seen': {'agent': {'tools': '00000000000000000000000000000004.022986cd20ae85c77ea298a383f69ba8',
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-19-7)  'start:agent': '00000000000000000000000000000002.d6f25946c3108fc12f27abbcf9b4cedc'},
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-19-8) 'tools': {'branch:agent:should_continue:tools': '00000000000000000000000000000003.065d90dd7f7cd091f0233855210bb2af'},
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-19-9) '__input__': {},
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-19-10) '__start__': {'__start__': '00000000000000000000000000000001.0e148ae3debe753278387e84f786e863'}},
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-19-11) 'channel_versions': {'agent': '00000000000000000000000000000005.065d90dd7f7cd091f0233855210bb2af',
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-19-12) 'tools': '00000000000000000000000000000005.',
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-19-13) 'messages': '00000000000000000000000000000005.d869fc7231619df0db74feed624efe41',
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-19-14) '__start__': '00000000000000000000000000000002.',
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-19-15) 'start:agent': '00000000000000000000000000000003.',
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-19-16) 'branch:agent:should_continue:tools': '00000000000000000000000000000004.'},
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-19-17) 'channel_values': {'agent': 'agent',
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-19-18) 'messages': [HumanMessage(content="what's the weather in nyc", id='d883b8a0-99de-486d-91a2-bcfa7f25dc05'),
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-19-19)  AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_H6TAYfyd6AnaCrkQGs6Q2fVp', 'function': {'arguments': '{"city":"nyc"}', 'name': 'get_weather'}, 'type': 'function'}]}, response_metadata={'token_usage': {'completion_tokens': 15, 'prompt_tokens': 58, 'total_tokens': 73}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_48196bc67a', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-6f542f84-ad73-444c-8ef7-b5ea75a2e09b-0', tool_calls=[{'name': 'get_weather', 'args': {'city': 'nyc'}, 'id': 'call_H6TAYfyd6AnaCrkQGs6Q2fVp', 'type': 'tool_call'}], usage_metadata={'input_tokens': 58, 'output_tokens': 15, 'total_tokens': 73}),
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-19-20)  ToolMessage(content='It might be cloudy in nyc', name='get_weather', id='c0e52254-77a4-4ea9-a2b7-61dd2d65ec68', tool_call_id='call_H6TAYfyd6AnaCrkQGs6Q2fVp'),
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-19-21)  AIMessage(content='The weather in NYC might be cloudy.', response_metadata={'token_usage': {'completion_tokens': 9, 'prompt_tokens': 88, 'total_tokens': 97}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_48196bc67a', 'finish_reason': 'stop', 'logprobs': None}, id='run-977140d4-7582-40c3-b2b6-31b542c430a3-0', usage_metadata={'input_tokens': 88, 'output_tokens': 9, 'total_tokens': 97})]}}

```


### With a connection[¶](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#with-a-connection_1 "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-20-1)frompsycopgimport AsyncConnection
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-20-2)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-20-3)async with await AsyncConnection.connect(DB_URI, **connection_kwargs) as conn:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-20-4)  checkpointer = AsyncPostgresSaver(conn)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-20-5)  graph = create_react_agent(model, tools=tools, checkpointer=checkpointer)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-20-6)  config = {"configurable": {"thread_id": "5"}}
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-20-7)  res = await graph.ainvoke(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-20-8)    {"messages": [("human", "what's the weather in nyc")]}, config
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-20-9)  )
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-20-10)  checkpoint_tuple = await checkpointer.aget_tuple(config)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-21-1)checkpoint_tuple

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-22-1)CheckpointTuple(config={'configurable': {'thread_id': '5', 'checkpoint_ns': '', 'checkpoint_id': '1ef559b7-65b4-60ca-8003-1ef4b620559a'}}, checkpoint={'v': 1, 'id': '1ef559b7-65b4-60ca-8003-1ef4b620559a', 'ts': '2024-08-08T15:32:46.575814+00:00', 'current_tasks': {}, 'pending_sends': [], 'versions_seen': {'agent': {'tools': '00000000000000000000000000000004.022986cd20ae85c77ea298a383f69ba8', 'start:agent': '00000000000000000000000000000002.d6f25946c3108fc12f27abbcf9b4cedc'}, 'tools': {'branch:agent:should_continue:tools': '00000000000000000000000000000003.065d90dd7f7cd091f0233855210bb2af'}, '__input__': {}, '__start__': {'__start__': '00000000000000000000000000000001.0e148ae3debe753278387e84f786e863'}}, 'channel_versions': {'agent': '00000000000000000000000000000005.065d90dd7f7cd091f0233855210bb2af', 'tools': '00000000000000000000000000000005.', 'messages': '00000000000000000000000000000005.1557a6006d58f736d5cb2dd5c5f10111', '__start__': '00000000000000000000000000000002.', 'start:agent': '00000000000000000000000000000003.', 'branch:agent:should_continue:tools': '00000000000000000000000000000004.'}, 'channel_values': {'agent': 'agent', 'messages': [HumanMessage(content="what's the weather in nyc", id='935e7732-b288-49bd-9ec2-1f7610cc38cb'), AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_94KtjtPmsiaj7T8yXvL7Ef31', 'function': {'arguments': '{"city":"nyc"}', 'name': 'get_weather'}, 'type': 'function'}]}, response_metadata={'token_usage': {'completion_tokens': 15, 'prompt_tokens': 58, 'total_tokens': 73}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_48196bc67a', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-790c929a-7982-49e7-af67-2cbe4a86373b-0', tool_calls=[{'name': 'get_weather', 'args': {'city': 'nyc'}, 'id': 'call_94KtjtPmsiaj7T8yXvL7Ef31', 'type': 'tool_call'}], usage_metadata={'input_tokens': 58, 'output_tokens': 15, 'total_tokens': 73}), ToolMessage(content='It might be cloudy in nyc', name='get_weather', id='b2dc1073-abc4-4492-8982-434a7e32e445', tool_call_id='call_94KtjtPmsiaj7T8yXvL7Ef31'), AIMessage(content='The weather in NYC might be cloudy.', response_metadata={'token_usage': {'completion_tokens': 9, 'prompt_tokens': 88, 'total_tokens': 97}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_48196bc67a', 'finish_reason': 'stop', 'logprobs': None}, id='run-7e8a7f16-d8e1-457a-89f3-192102396449-0', usage_metadata={'input_tokens': 88, 'output_tokens': 9, 'total_tokens': 97})]}}, metadata={'step': 3, 'source': 'loop', 'writes': {'agent': {'messages': [AIMessage(content='The weather in NYC might be cloudy.', response_metadata={'logprobs': None, 'model_name': 'gpt-4o-mini-2024-07-18', 'token_usage': {'total_tokens': 97, 'prompt_tokens': 88, 'completion_tokens': 9}, 'finish_reason': 'stop', 'system_fingerprint': 'fp_48196bc67a'}, id='run-7e8a7f16-d8e1-457a-89f3-192102396449-0', usage_metadata={'input_tokens': 88, 'output_tokens': 9, 'total_tokens': 97})]}}}, parent_config={'configurable': {'thread_id': '5', 'checkpoint_ns': '', 'checkpoint_id': '1ef559b7-62ae-6128-8002-c04af82bcd41'}}, pending_writes=[])

```


### With a connection string[¶](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#with-a-connection-string_1 "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-23-1)async with AsyncPostgresSaver.from_conn_string(DB_URI) as checkpointer:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-23-2)  graph = create_react_agent(model, tools=tools, checkpointer=checkpointer)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-23-3)  config = {"configurable": {"thread_id": "6"}}
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-23-4)  res = await graph.ainvoke(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-23-5)    {"messages": [("human", "what's the weather in nyc")]}, config
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-23-6)  )
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-23-7)  checkpoint_tuples = [c async for c in checkpointer.alist(config)]

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-24-1)checkpoint_tuples

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-25-1)[CheckpointTuple(config={'configurable': {'thread_id': '6', 'checkpoint_ns': '', 'checkpoint_id': '1ef559b7-723c-67de-8003-63bd4eab35af'}}, checkpoint={'v': 1, 'id': '1ef559b7-723c-67de-8003-63bd4eab35af', 'ts': '2024-08-08T15:32:47.890003+00:00', 'current_tasks': {}, 'pending_sends': [], 'versions_seen': {'agent': {'tools': '00000000000000000000000000000004.022986cd20ae85c77ea298a383f69ba8', 'start:agent': '00000000000000000000000000000002.d6f25946c3108fc12f27abbcf9b4cedc'}, 'tools': {'branch:agent:should_continue:tools': '00000000000000000000000000000003.065d90dd7f7cd091f0233855210bb2af'}, '__input__': {}, '__start__': {'__start__': '00000000000000000000000000000001.0e148ae3debe753278387e84f786e863'}}, 'channel_versions': {'agent': '00000000000000000000000000000005.065d90dd7f7cd091f0233855210bb2af', 'tools': '00000000000000000000000000000005.', 'messages': '00000000000000000000000000000005.b6fe2a26011590cfe8fd6a39151a9e92', '__start__': '00000000000000000000000000000002.', 'start:agent': '00000000000000000000000000000003.', 'branch:agent:should_continue:tools': '00000000000000000000000000000004.'}, 'channel_values': {'agent': 'agent', 'messages': [HumanMessage(content="what's the weather in nyc", id='977ddb90-9991-44cb-9f73-361c6dd21396'), AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_QIFCuh4zfP9owpjToycJiZf7', 'function': {'arguments': '{"city":"nyc"}', 'name': 'get_weather'}, 'type': 'function'}]}, response_metadata={'token_usage': {'completion_tokens': 15, 'prompt_tokens': 58, 'total_tokens': 73}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_48196bc67a', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-47b10c48-4db3-46d8-b4fa-e021818e01c5-0', tool_calls=[{'name': 'get_weather', 'args': {'city': 'nyc'}, 'id': 'call_QIFCuh4zfP9owpjToycJiZf7', 'type': 'tool_call'}], usage_metadata={'input_tokens': 58, 'output_tokens': 15, 'total_tokens': 73}), ToolMessage(content='It might be cloudy in nyc', name='get_weather', id='798c520f-4f9a-4f6d-a389-da721eb4d4ce', tool_call_id='call_QIFCuh4zfP9owpjToycJiZf7'), AIMessage(content='The weather in NYC might be cloudy.', response_metadata={'token_usage': {'completion_tokens': 9, 'prompt_tokens': 88, 'total_tokens': 97}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_48196bc67a', 'finish_reason': 'stop', 'logprobs': None}, id='run-4a34e05d-8bcf-41ad-adc3-715919fde64c-0', usage_metadata={'input_tokens': 88, 'output_tokens': 9, 'total_tokens': 97})]}}, metadata={'step': 3, 'source': 'loop', 'writes': {'agent': {'messages': [AIMessage(content='The weather in NYC might be cloudy.', response_metadata={'logprobs': None, 'model_name': 'gpt-4o-mini-2024-07-18', 'token_usage': {'total_tokens': 97, 'prompt_tokens': 88, 'completion_tokens': 9}, 'finish_reason': 'stop', 'system_fingerprint': 'fp_48196bc67a'}, id='run-4a34e05d-8bcf-41ad-adc3-715919fde64c-0', usage_metadata={'input_tokens': 88, 'output_tokens': 9, 'total_tokens': 97})]}}}, parent_config={'configurable': {'thread_id': '6', 'checkpoint_ns': '', 'checkpoint_id': '1ef559b7-6bf5-63c6-8002-ed990dbbc96e'}}, pending_writes=None),
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-25-2) CheckpointTuple(config={'configurable': {'thread_id': '6', 'checkpoint_ns': '', 'checkpoint_id': '1ef559b7-6bf5-63c6-8002-ed990dbbc96e'}}, checkpoint={'v': 1, 'id': '1ef559b7-6bf5-63c6-8002-ed990dbbc96e', 'ts': '2024-08-08T15:32:47.231667+00:00', 'current_tasks': {}, 'pending_sends': [], 'versions_seen': {'agent': {'start:agent': '00000000000000000000000000000002.d6f25946c3108fc12f27abbcf9b4cedc'}, 'tools': {'branch:agent:should_continue:tools': '00000000000000000000000000000003.065d90dd7f7cd091f0233855210bb2af'}, '__input__': {}, '__start__': {'__start__': '00000000000000000000000000000001.0e148ae3debe753278387e84f786e863'}}, 'channel_versions': {'agent': '00000000000000000000000000000004.', 'tools': '00000000000000000000000000000004.022986cd20ae85c77ea298a383f69ba8', 'messages': '00000000000000000000000000000004.c9074f2a41f05486b5efb86353dc75c0', '__start__': '00000000000000000000000000000002.', 'start:agent': '00000000000000000000000000000003.', 'branch:agent:should_continue:tools': '00000000000000000000000000000004.'}, 'channel_values': {'tools': 'tools', 'messages': [HumanMessage(content="what's the weather in nyc", id='977ddb90-9991-44cb-9f73-361c6dd21396'), AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_QIFCuh4zfP9owpjToycJiZf7', 'function': {'arguments': '{"city":"nyc"}', 'name': 'get_weather'}, 'type': 'function'}]}, response_metadata={'token_usage': {'completion_tokens': 15, 'prompt_tokens': 58, 'total_tokens': 73}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_48196bc67a', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-47b10c48-4db3-46d8-b4fa-e021818e01c5-0', tool_calls=[{'name': 'get_weather', 'args': {'city': 'nyc'}, 'id': 'call_QIFCuh4zfP9owpjToycJiZf7', 'type': 'tool_call'}], usage_metadata={'input_tokens': 58, 'output_tokens': 15, 'total_tokens': 73}), ToolMessage(content='It might be cloudy in nyc', name='get_weather', id='798c520f-4f9a-4f6d-a389-da721eb4d4ce', tool_call_id='call_QIFCuh4zfP9owpjToycJiZf7')]}}, metadata={'step': 2, 'source': 'loop', 'writes': {'tools': {'messages': [ToolMessage(content='It might be cloudy in nyc', name='get_weather', id='798c520f-4f9a-4f6d-a389-da721eb4d4ce', tool_call_id='call_QIFCuh4zfP9owpjToycJiZf7')]}}}, parent_config={'configurable': {'thread_id': '6', 'checkpoint_ns': '', 'checkpoint_id': '1ef559b7-6be0-6926-8001-1a8ce73baf9e'}}, pending_writes=None),
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-25-3) CheckpointTuple(config={'configurable': {'thread_id': '6', 'checkpoint_ns': '', 'checkpoint_id': '1ef559b7-6be0-6926-8001-1a8ce73baf9e'}}, checkpoint={'v': 1, 'id': '1ef559b7-6be0-6926-8001-1a8ce73baf9e', 'ts': '2024-08-08T15:32:47.223198+00:00', 'current_tasks': {}, 'pending_sends': [], 'versions_seen': {'agent': {'start:agent': '00000000000000000000000000000002.d6f25946c3108fc12f27abbcf9b4cedc'}, '__input__': {}, '__start__': {'__start__': '00000000000000000000000000000001.0e148ae3debe753278387e84f786e863'}}, 'channel_versions': {'agent': '00000000000000000000000000000003.065d90dd7f7cd091f0233855210bb2af', 'messages': '00000000000000000000000000000003.097b5407d709b297591f1ef5d50c8368', '__start__': '00000000000000000000000000000002.', 'start:agent': '00000000000000000000000000000003.', 'branch:agent:should_continue:tools': '00000000000000000000000000000003.065d90dd7f7cd091f0233855210bb2af'}, 'channel_values': {'agent': 'agent', 'messages': [HumanMessage(content="what's the weather in nyc", id='977ddb90-9991-44cb-9f73-361c6dd21396'), AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_QIFCuh4zfP9owpjToycJiZf7', 'function': {'arguments': '{"city":"nyc"}', 'name': 'get_weather'}, 'type': 'function'}]}, response_metadata={'token_usage': {'completion_tokens': 15, 'prompt_tokens': 58, 'total_tokens': 73}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_48196bc67a', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-47b10c48-4db3-46d8-b4fa-e021818e01c5-0', tool_calls=[{'name': 'get_weather', 'args': {'city': 'nyc'}, 'id': 'call_QIFCuh4zfP9owpjToycJiZf7', 'type': 'tool_call'}], usage_metadata={'input_tokens': 58, 'output_tokens': 15, 'total_tokens': 73})], 'branch:agent:should_continue:tools': 'agent'}}, metadata={'step': 1, 'source': 'loop', 'writes': {'agent': {'messages': [AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_QIFCuh4zfP9owpjToycJiZf7', 'type': 'function', 'function': {'name': 'get_weather', 'arguments': '{"city":"nyc"}'}}]}, response_metadata={'logprobs': None, 'model_name': 'gpt-4o-mini-2024-07-18', 'token_usage': {'total_tokens': 73, 'prompt_tokens': 58, 'completion_tokens': 15}, 'finish_reason': 'tool_calls', 'system_fingerprint': 'fp_48196bc67a'}, id='run-47b10c48-4db3-46d8-b4fa-e021818e01c5-0', tool_calls=[{'name': 'get_weather', 'args': {'city': 'nyc'}, 'id': 'call_QIFCuh4zfP9owpjToycJiZf7', 'type': 'tool_call'}], usage_metadata={'input_tokens': 58, 'output_tokens': 15, 'total_tokens': 73})]}}}, parent_config={'configurable': {'thread_id': '6', 'checkpoint_ns': '', 'checkpoint_id': '1ef559b7-663d-60b4-8000-10a8922bffbf'}}, pending_writes=None),
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-25-4) CheckpointTuple(config={'configurable': {'thread_id': '6', 'checkpoint_ns': '', 'checkpoint_id': '1ef559b7-663d-60b4-8000-10a8922bffbf'}}, checkpoint={'v': 1, 'id': '1ef559b7-663d-60b4-8000-10a8922bffbf', 'ts': '2024-08-08T15:32:46.631935+00:00', 'current_tasks': {}, 'pending_sends': [], 'versions_seen': {'__input__': {}, '__start__': {'__start__': '00000000000000000000000000000001.0e148ae3debe753278387e84f786e863'}}, 'channel_versions': {'messages': '00000000000000000000000000000002.2a79db8da664e437bdb25ea804457ca7', '__start__': '00000000000000000000000000000002.', 'start:agent': '00000000000000000000000000000002.d6f25946c3108fc12f27abbcf9b4cedc'}, 'channel_values': {'messages': [HumanMessage(content="what's the weather in nyc", id='977ddb90-9991-44cb-9f73-361c6dd21396')], 'start:agent': '__start__'}}, metadata={'step': 0, 'source': 'loop', 'writes': None}, parent_config={'configurable': {'thread_id': '6', 'checkpoint_ns': '', 'checkpoint_id': '1ef559b7-6637-6d4e-bfff-6cecf690c3cb'}}, pending_writes=None),
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__codelineno-25-5) CheckpointTuple(config={'configurable': {'thread_id': '6', 'checkpoint_ns': '', 'checkpoint_id': '1ef559b7-6637-6d4e-bfff-6cecf690c3cb'}}, checkpoint={'v': 1, 'id': '1ef559b7-6637-6d4e-bfff-6cecf690c3cb', 'ts': '2024-08-08T15:32:46.629806+00:00', 'current_tasks': {}, 'pending_sends': [], 'versions_seen': {'__input__': {}}, 'channel_versions': {'__start__': '00000000000000000000000000000001.0e148ae3debe753278387e84f786e863'}, 'channel_values': {'__start__': {'messages': [['human', "what's the weather in nyc"]]}}}, metadata={'step': -1, 'source': 'input', 'writes': {'messages': [['human', "what's the weather in nyc"]]}}, parent_config=None, pending_writes=None)]

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to add cross-thread persistence to your graph  ](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/) [ Next  How to use MongoDB checkpointer for persistence  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
