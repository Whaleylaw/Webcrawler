---
url: https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#how-to-use-mongodb-checkpointer-for-persistence)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to use MongoDB checkpointer for persistence 

[ ](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/?q= "Share")

Initializing search 

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
            * How to use MongoDB checkpointer for persistence  [ How to use MongoDB checkpointer for persistence  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#setup)
              * [ Define model and tools for the graph  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#define-model-and-tools-for-the-graph)
              * [ MongoDB checkpointer usage  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#mongodb-checkpointer-usage)
                * [ With a connection string  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#with-a-connection-string)
                * [ Using the MongoDB client  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#using-the-mongodb-client)
                * [ Using an async connection  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#using-an-async-connection)
                * [ Using the async MongoDB client  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#using-the-async-mongodb-client)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#setup)
  * [ Define model and tools for the graph  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#define-model-and-tools-for-the-graph)
  * [ MongoDB checkpointer usage  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#mongodb-checkpointer-usage)
    * [ With a connection string  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#with-a-connection-string)
    * [ Using the MongoDB client  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#using-the-mongodb-client)
    * [ Using an async connection  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#using-an-async-connection)
    * [ Using the async MongoDB client  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#using-the-async-mongodb-client)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Persistence  ](https://langchain-ai.github.io/langgraph/how-tos#persistence)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/persistence_mongodb.ipynb "Edit this page")

# How to use MongoDB checkpointer for persistence[¶](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#how-to-use-mongodb-checkpointer-for-persistence "Permanent link")

Prerequisites

This guide assumes familiarity with the following: 

  * [ Persistence ](https://langchain-ai.github.io/langgraph/concepts/persistence/)
  * [ MongoDB ](https://www.mongodb.com/)



When creating LangGraph agents, you can also set them up so that they persist their state. This allows you to do things like interact with an agent multiple times and have it remember previous interactions. 

This reference implementation shows how to use MongoDB as the backend for persisting checkpoint state using the `langgraph-checkpoint-mongodb` library.

For demonstration purposes we add persistence to a [prebuilt ReAct agent](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/).

In general, you can add a checkpointer to any custom graph that you build like this:

```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-0-1)fromlanggraph.graphimport StateGraph
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-0-2)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-0-3)builder = StateGraph(...)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-0-4)# ... define the graph
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-0-5)checkpointer = # mongodb checkpointer (see examples below)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-0-6)graph = builder.compile(checkpointer=checkpointer)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-0-7)...

```


API Reference: [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph)

## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#setup "Permanent link")

To use the MongoDB checkpointer, you will need a MongoDB cluster. Follow [this guide](https://www.mongodb.com/docs/guides/atlas/cluster/) to create a cluster if you don't already have one.

Next, let's install the required packages and set our API keys

```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-1-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-1-2)%pip install -U pymongo langgraph langgraph-checkpoint-mongodb

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-2-1)importgetpass
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-2-2)importos
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-2-3)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-2-4)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-2-5)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-2-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-2-7)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-2-8)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-2-9)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-2-10)_set_env("OPENAI_API_KEY")

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-3-1)OPENAI_API_KEY: ········

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Define model and tools for the graph[¶](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#define-model-and-tools-for-the-graph "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-4-1)fromtypingimport Literal
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-4-2)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-4-3)fromlangchain_core.toolsimport tool
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-4-4)fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-4-5)fromlanggraph.prebuiltimport create_react_agent
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-4-6)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-4-7)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-4-8)@tool
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-4-9)defget_weather(city: Literal["nyc", "sf"]):
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-4-10)"""Use this to get weather information."""
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-4-11)  if city == "nyc":
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-4-12)    return "It might be cloudy in nyc"
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-4-13)  elif city == "sf":
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-4-14)    return "It's always sunny in sf"
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-4-15)  else:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-4-16)    raise AssertionError("Unknown city")
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-4-17)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-4-18)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-4-19)tools = [get_weather]
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-4-20)model = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

```


API Reference: [tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html) | [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html) | [create_react_agent](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent)

## MongoDB checkpointer usage[¶](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#mongodb-checkpointer-usage "Permanent link")

### With a connection string[¶](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#with-a-connection-string "Permanent link")

This creates a connection to MongoDB directly using the connection string of your cluster. This is ideal for use in scripts, one-off operations and short-lived applications.

```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-5-1)fromlanggraph.checkpoint.mongodbimport MongoDBSaver
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-5-2)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-5-3)MONGODB_URI = "localhost:27017" # replace this with your connection string
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-5-4)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-5-5)with MongoDBSaver.from_conn_string(MONGODB_URI) as checkpointer:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-5-6)  graph = create_react_agent(model, tools=tools, checkpointer=checkpointer)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-5-7)  config = {"configurable": {"thread_id": "1"}}
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-5-8)  response = graph.invoke(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-5-9)    {"messages": [("human", "what's the weather in sf")]}, config
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-5-10)  )

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-6-1)response

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-7-1){'messages': [HumanMessage(content="what's the weather in sf", additional_kwargs={}, response_metadata={}, id='729afd6a-fdc0-4192-a255-1dac065c79b2'),
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-7-2) AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_YqaO8oU3BhGmIz9VHTxqGyyN', 'function': {'arguments': '{"city":"sf"}', 'name': 'get_weather'}, 'type': 'function'}], 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 14, 'prompt_tokens': 57, 'total_tokens': 71, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_39a40c96a0', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-b45c0c12-c68e-4392-92dd-5d325d0a9f60-0', tool_calls=[{'name': 'get_weather', 'args': {'city': 'sf'}, 'id': 'call_YqaO8oU3BhGmIz9VHTxqGyyN', 'type': 'tool_call'}], usage_metadata={'input_tokens': 57, 'output_tokens': 14, 'total_tokens': 71, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}),
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-7-3) ToolMessage(content="It's always sunny in sf", name='get_weather', id='0c72eb29-490b-44df-898f-8454c314eac1', tool_call_id='call_YqaO8oU3BhGmIz9VHTxqGyyN'),
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-7-4) AIMessage(content='The weather in San Francisco is always sunny!', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 10, 'prompt_tokens': 84, 'total_tokens': 94, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_818c284075', 'finish_reason': 'stop', 'logprobs': None}, id='run-33f54c91-0ba9-48b7-9b25-5a972bbdeea9-0', usage_metadata={'input_tokens': 84, 'output_tokens': 10, 'total_tokens': 94, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}})]}

```


### Using the MongoDB client[¶](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#using-the-mongodb-client "Permanent link")

This creates a connection to MongoDB using the MongoDB client. This is ideal for long-running applications since it allows you to reuse the client instance for multiple database operations without needing to reinitialize the connection each time.

```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-8-1)frompymongoimport MongoClient
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-8-2)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-8-3)mongodb_client = MongoClient(MONGODB_URI)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-8-4)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-8-5)checkpointer = MongoDBSaver(mongodb_client)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-8-6)graph = create_react_agent(model, tools=tools, checkpointer=checkpointer)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-8-7)config = {"configurable": {"thread_id": "2"}}
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-8-8)response = graph.invoke({"messages": [("user", "What's the weather in sf?")]}, config)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-9-1)response

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-10-1){'messages': [HumanMessage(content="What's the weather in sf?", additional_kwargs={}, response_metadata={}, id='4ce68bee-a843-4b08-9c02-7a0e3b010110'),
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-10-2) AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_MvGxq9IU9wvW9mfYKSALHtGu', 'function': {'arguments': '{"city":"sf"}', 'name': 'get_weather'}, 'type': 'function'}], 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 14, 'prompt_tokens': 57, 'total_tokens': 71, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_6fc10e10eb', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-9712c5a4-376c-4812-a0c4-1b522334a59d-0', tool_calls=[{'name': 'get_weather', 'args': {'city': 'sf'}, 'id': 'call_MvGxq9IU9wvW9mfYKSALHtGu', 'type': 'tool_call'}], usage_metadata={'input_tokens': 57, 'output_tokens': 14, 'total_tokens': 71, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}),
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-10-3) ToolMessage(content="It's always sunny in sf", name='get_weather', id='b4eed38d-bcaf-4497-ad08-f21ccd6a8c30', tool_call_id='call_MvGxq9IU9wvW9mfYKSALHtGu'),
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-10-4) AIMessage(content='The weather in San Francisco is always sunny!', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 10, 'prompt_tokens': 84, 'total_tokens': 94, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_6fc10e10eb', 'finish_reason': 'stop', 'logprobs': None}, id='run-c6c4ad75-89ef-4b4f-9ca4-bd52ccb0729b-0', usage_metadata={'input_tokens': 84, 'output_tokens': 10, 'total_tokens': 94, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}})]}

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-11-1)# Retrieve the latest checkpoint for the given thread ID
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-11-2)# To retrieve a specific checkpoint, pass the checkpoint_id in the config
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-11-3)checkpointer.get_tuple(config)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-12-1)CheckpointTuple(config={'configurable': {'thread_id': '2', 'checkpoint_ns': '', 'checkpoint_id': '1efb8c75-9262-68b4-8003-1ac1ef198757'}}, checkpoint={'v': 1, 'ts': '2024-12-12T20:26:20.545003+00:00', 'id': '1efb8c75-9262-68b4-8003-1ac1ef198757', 'channel_values': {'messages': [HumanMessage(content="What's the weather in sf?", additional_kwargs={}, response_metadata={}, id='4ce68bee-a843-4b08-9c02-7a0e3b010110'), AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_MvGxq9IU9wvW9mfYKSALHtGu', 'function': {'arguments': '{"city":"sf"}', 'name': 'get_weather'}, 'type': 'function'}], 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 14, 'prompt_tokens': 57, 'total_tokens': 71, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_6fc10e10eb', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-9712c5a4-376c-4812-a0c4-1b522334a59d-0', tool_calls=[{'name': 'get_weather', 'args': {'city': 'sf'}, 'id': 'call_MvGxq9IU9wvW9mfYKSALHtGu', 'type': 'tool_call'}], usage_metadata={'input_tokens': 57, 'output_tokens': 14, 'total_tokens': 71, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}), ToolMessage(content="It's always sunny in sf", name='get_weather', id='b4eed38d-bcaf-4497-ad08-f21ccd6a8c30', tool_call_id='call_MvGxq9IU9wvW9mfYKSALHtGu'), AIMessage(content='The weather in San Francisco is always sunny!', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 10, 'prompt_tokens': 84, 'total_tokens': 94, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_6fc10e10eb', 'finish_reason': 'stop', 'logprobs': None}, id='run-c6c4ad75-89ef-4b4f-9ca4-bd52ccb0729b-0', usage_metadata={'input_tokens': 84, 'output_tokens': 10, 'total_tokens': 94, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}})], 'agent': 'agent'}, 'channel_versions': {'__start__': 2, 'messages': 5, 'start:agent': 3, 'agent': 5, 'branch:agent:should_continue:tools': 4, 'tools': 5}, 'versions_seen': {'__input__': {}, '__start__': {'__start__': 1}, 'agent': {'start:agent': 2, 'tools': 4}, 'tools': {'branch:agent:should_continue:tools': 3}}, 'pending_sends': []}, metadata={'source': 'loop', 'writes': {'agent': {'messages': [AIMessage(content='The weather in San Francisco is always sunny!', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 10, 'prompt_tokens': 84, 'total_tokens': 94, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_6fc10e10eb', 'finish_reason': 'stop', 'logprobs': None}, id='run-c6c4ad75-89ef-4b4f-9ca4-bd52ccb0729b-0', usage_metadata={'input_tokens': 84, 'output_tokens': 10, 'total_tokens': 94, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}})]}}, 'thread_id': '2', 'step': 3, 'parents': {}}, parent_config={'configurable': {'thread_id': '2', 'checkpoint_ns': '', 'checkpoint_id': '1efb8c75-8d89-6ffe-8002-84a4312c4fed'}}, pending_writes=[])

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-13-1)# Remember to close the connection after you're done
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-13-2)mongodb_client.close()

```


### Using an async connection[¶](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#using-an-async-connection "Permanent link")

This creates a short-lived asynchronous connection to MongoDB. 

Async connections allow non-blocking database operations. This means other parts of your application can continue running while waiting for database operations to complete. It's particularly useful in high-concurrency scenarios or when dealing with I/O-bound operations.

```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-14-1)fromlanggraph.checkpoint.mongodb.aioimport AsyncMongoDBSaver
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-14-2)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-14-3)async with AsyncMongoDBSaver.from_conn_string(MONGODB_URI) as checkpointer:
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-14-4)  graph = create_react_agent(model, tools=tools, checkpointer=checkpointer)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-14-5)  config = {"configurable": {"thread_id": "3"}}
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-14-6)  response = await graph.ainvoke(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-14-7)    {"messages": [("user", "What's the weather in sf?")]}, config
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-14-8)  )

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-15-1)response

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-16-1){'messages': [HumanMessage(content="What's the weather in sf?", additional_kwargs={}, response_metadata={}, id='fed70fe6-1b2e-4481-9bfc-063df3b587dc'),
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-16-2) AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_miRiF3vPQv98wlDHl6CeRxBy', 'function': {'arguments': '{"city":"sf"}', 'name': 'get_weather'}, 'type': 'function'}], 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 14, 'prompt_tokens': 57, 'total_tokens': 71, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_6fc10e10eb', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-7f2d5153-973e-4a9e-8b71-a77625c342cf-0', tool_calls=[{'name': 'get_weather', 'args': {'city': 'sf'}, 'id': 'call_miRiF3vPQv98wlDHl6CeRxBy', 'type': 'tool_call'}], usage_metadata={'input_tokens': 57, 'output_tokens': 14, 'total_tokens': 71, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}),
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-16-3) ToolMessage(content="It's always sunny in sf", name='get_weather', id='49035e8e-8aee-4d9d-88ab-9a1bc10ecbd3', tool_call_id='call_miRiF3vPQv98wlDHl6CeRxBy'),
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-16-4) AIMessage(content='The weather in San Francisco is always sunny!', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 10, 'prompt_tokens': 84, 'total_tokens': 94, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_6fc10e10eb', 'finish_reason': 'stop', 'logprobs': None}, id='run-9403d502-391e-4407-99fd-eec8ed184e50-0', usage_metadata={'input_tokens': 84, 'output_tokens': 10, 'total_tokens': 94, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}})]}

```


### Using the async MongoDB client[¶](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#using-the-async-mongodb-client "Permanent link")

This routes connections to MongoDB through an asynchronous MongoDB client.

```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-17-1)frompymongoimport AsyncMongoClient
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-17-2)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-17-3)async_mongodb_client = AsyncMongoClient(MONGODB_URI)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-17-4)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-17-5)checkpointer = AsyncMongoDBSaver(async_mongodb_client)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-17-6)graph = create_react_agent(model, tools=tools, checkpointer=checkpointer)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-17-7)config = {"configurable": {"thread_id": "4"}}
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-17-8)response = await graph.ainvoke(
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-17-9)  {"messages": [("user", "What's the weather in sf?")]}, config
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-17-10))

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-18-1)response

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-19-1){'messages': [HumanMessage(content="What's the weather in sf?", additional_kwargs={}, response_metadata={}, id='58282e2b-4cc1-40a1-8e65-420a2177bbd6'),
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-19-2) AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_SJFViVHl1tYTZDoZkNN3ePhJ', 'function': {'arguments': '{"city":"sf"}', 'name': 'get_weather'}, 'type': 'function'}], 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 14, 'prompt_tokens': 57, 'total_tokens': 71, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_bba3c8e70b', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-131af8c1-d388-4d7f-9137-da59ebd5fefd-0', tool_calls=[{'name': 'get_weather', 'args': {'city': 'sf'}, 'id': 'call_SJFViVHl1tYTZDoZkNN3ePhJ', 'type': 'tool_call'}], usage_metadata={'input_tokens': 57, 'output_tokens': 14, 'total_tokens': 71, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}),
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-19-3) ToolMessage(content="It's always sunny in sf", name='get_weather', id='6090a56f-177b-4d3f-b16a-9c05f23800e3', tool_call_id='call_SJFViVHl1tYTZDoZkNN3ePhJ'),
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-19-4) AIMessage(content='The weather in San Francisco is always sunny!', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 10, 'prompt_tokens': 84, 'total_tokens': 94, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_6fc10e10eb', 'finish_reason': 'stop', 'logprobs': None}, id='run-6ff5ddf5-6e13-4126-8df9-81c8638355fc-0', usage_metadata={'input_tokens': 84, 'output_tokens': 10, 'total_tokens': 94, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}})]}

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-20-1)# Retrieve the latest checkpoint for the given thread ID
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-20-2)# To retrieve a specific checkpoint, pass the checkpoint_id in the config
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-20-3)latest_checkpoint = await checkpointer.aget_tuple(config)
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-20-4)print(latest_checkpoint)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-21-1)CheckpointTuple(config={'configurable': {'thread_id': '4', 'checkpoint_ns': '', 'checkpoint_id': '1efb8c76-21f4-6d10-8003-9496e1754e93'}}, checkpoint={'v': 1, 'ts': '2024-12-12T20:26:35.599560+00:00', 'id': '1efb8c76-21f4-6d10-8003-9496e1754e93', 'channel_values': {'messages': [HumanMessage(content="What's the weather in sf?", additional_kwargs={}, response_metadata={}, id='58282e2b-4cc1-40a1-8e65-420a2177bbd6'), AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_SJFViVHl1tYTZDoZkNN3ePhJ', 'function': {'arguments': '{"city":"sf"}', 'name': 'get_weather'}, 'type': 'function'}], 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 14, 'prompt_tokens': 57, 'total_tokens': 71, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_bba3c8e70b', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-131af8c1-d388-4d7f-9137-da59ebd5fefd-0', tool_calls=[{'name': 'get_weather', 'args': {'city': 'sf'}, 'id': 'call_SJFViVHl1tYTZDoZkNN3ePhJ', 'type': 'tool_call'}], usage_metadata={'input_tokens': 57, 'output_tokens': 14, 'total_tokens': 71, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}), ToolMessage(content="It's always sunny in sf", name='get_weather', id='6090a56f-177b-4d3f-b16a-9c05f23800e3', tool_call_id='call_SJFViVHl1tYTZDoZkNN3ePhJ'), AIMessage(content='The weather in San Francisco is always sunny!', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 10, 'prompt_tokens': 84, 'total_tokens': 94, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_6fc10e10eb', 'finish_reason': 'stop', 'logprobs': None}, id='run-6ff5ddf5-6e13-4126-8df9-81c8638355fc-0', usage_metadata={'input_tokens': 84, 'output_tokens': 10, 'total_tokens': 94, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}})], 'agent': 'agent'}, 'channel_versions': {'__start__': 2, 'messages': 5, 'start:agent': 3, 'agent': 5, 'branch:agent:should_continue:tools': 4, 'tools': 5}, 'versions_seen': {'__input__': {}, '__start__': {'__start__': 1}, 'agent': {'start:agent': 2, 'tools': 4}, 'tools': {'branch:agent:should_continue:tools': 3}}, 'pending_sends': []}, metadata={'source': 'loop', 'writes': {'agent': {'messages': [AIMessage(content='The weather in San Francisco is always sunny!', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 10, 'prompt_tokens': 84, 'total_tokens': 94, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_6fc10e10eb', 'finish_reason': 'stop', 'logprobs': None}, id='run-6ff5ddf5-6e13-4126-8df9-81c8638355fc-0', usage_metadata={'input_tokens': 84, 'output_tokens': 10, 'total_tokens': 94, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}})]}}, 'thread_id': '4', 'step': 3, 'parents': {}}, parent_config={'configurable': {'thread_id': '4', 'checkpoint_ns': '', 'checkpoint_id': '1efb8c76-1c6c-6474-8002-9c2595cd481c'}}, pending_writes=[])

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-22-1)# Remember to close the connection after you're done
[](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__codelineno-22-2)await async_mongodb_client.close()

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to use Postgres checkpointer for persistence  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/) [ Next  How to create a custom checkpointer using Redis  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
