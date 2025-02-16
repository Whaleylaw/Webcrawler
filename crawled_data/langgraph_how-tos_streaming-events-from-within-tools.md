---
url: https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#how-to-stream-data-from-within-a-tool)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to stream data from within a tool 

[ ](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/?q= "Share")

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
          * [ Persistence  ](https://langchain-ai.github.io/langgraph/how-tos#persistence)
          * [ Memory  ](https://langchain-ai.github.io/langgraph/how-tos#memory)
          * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraph/how-tos#human-in-the-loop)
          * Streaming  Streaming 
            * [ Streaming  ](https://langchain-ai.github.io/langgraph/how-tos#streaming)
            * [ How to stream  ](https://langchain-ai.github.io/langgraph/how-tos/streaming/)
            * [ How to stream LLM tokens from your graph  ](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/)
            * [ How to stream LLM tokens from specific nodes  ](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/)
            * How to stream data from within a tool  [ How to stream data from within a tool  ](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#setup)
              * [ Streaming custom data  ](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#streaming-custom-data)
              * [ Streaming LLM tokens  ](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#streaming-llm-tokens)
              * [ Example without LangChain  ](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#example-without-langchain)
            * [ How to stream from subgraphs  ](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/)
            * [ How to disable streaming for models that don't support it  ](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#setup)
  * [ Streaming custom data  ](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#streaming-custom-data)
  * [ Streaming LLM tokens  ](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#streaming-llm-tokens)
  * [ Example without LangChain  ](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#example-without-langchain)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Streaming  ](https://langchain-ai.github.io/langgraph/how-tos#streaming)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/streaming-events-from-within-tools.ipynb "Edit this page")

# How to stream data from within a tool[¶](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#how-to-stream-data-from-within-a-tool "Permanent link")

Prerequisites

This guide assumes familiarity with the following:

  * [Streaming](https://langchain-ai.github.io/langgraph/concepts/streaming/)
  * [Chat Models](https://python.langchain.com/docs/concepts/chat_models/)
  * [Tools](https://python.langchain.com/docs/concepts/tools/)



If your graph calls tools that use LLMs or any other streaming APIs, you might want to surface partial results during the execution of the tool, especially if the tool takes a longer time to run.

  1. To stream **arbitrary** data from inside a tool you can use `stream_mode="custom"`[](https://langchain-ai.github.io/langgraph/how-tos/streaming#custom) and `get_stream_writer()`:

```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-0-1)fromlanggraph.configimport get_stream_writer
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-0-2)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-0-3)deftool(tool_arg: str):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-0-4)  writer = get_stream_writer()
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-0-5)  for chunk in custom_data_stream():
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-0-6)    # stream any arbitrary data
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-0-7)    writer(chunk)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-0-8)  ...
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-0-9)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-0-10)for chunk in graph.stream(
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-0-11)  inputs,
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-0-12)  stream_mode="custom"
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-0-13)):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-0-14)  print(chunk)

```


  2. To stream LLM tokens generated by a tool calling an LLM you can use `stream_mode="messages"`[](https://langchain-ai.github.io/langgraph/how-tos/streaming#messages):

```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-1-1)fromlanggraph.graphimport StateGraph, MessagesState
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-1-2)fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-1-4)model = ChatOpenAI()
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-1-5)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-1-6)deftool(tool_arg: str):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-1-7)  model.invoke(tool_arg)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-1-8)  ...
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-1-10)defcall_tools(state: MessagesState):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-1-11)  tool_call = get_tool_call(state)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-1-12)  tool_result = tool(**tool_call["args"])
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-1-13)  ...
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-1-14)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-1-15)graph = (
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-1-16)  StateGraph(MessagesState)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-1-17)  .add_node(call_tools)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-1-18)  ...
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-1-19)  .compile()
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-1-20)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-1-21)for msg, metadata in graph.stream(
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-1-22)  inputs,
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-1-23)  stream_mode="messages"
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-1-24)):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-1-25)  print(msg)

```


API Reference: [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph)




Using without LangChain

If you need to stream data from inside tools **without using LangChain** , you can use `stream_mode="custom"`[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#custom). Check out the [example below](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#example-without-langchain) to learn more.

Async in Python < 3.11

When using Python < 3.11 with async code, please ensure you manually pass the `RunnableConfig` through to the chat model when invoking it like so: `model.ainvoke(..., config)`. The stream method collects all events from your nested code using a streaming tracer passed as a callback. In 3.11 and above, this is automatically handled via [contextvars](https://docs.python.org/3/library/contextvars.html); prior to 3.11, [asyncio's tasks](https://docs.python.org/3/library/asyncio-task.html#asyncio.create_task) lacked proper `contextvar` support, meaning that the callbacks will only propagate if you manually pass the config through. We do this in the `call_model` function below.

## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#setup "Permanent link")

First, let's install the required packages and set our API keys

```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-2-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-2-2)%pip install -U langgraph langchain-openai

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-3-1)importgetpass
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-3-2)importos
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-3-3)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-3-4)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-3-5)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-3-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-3-7)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-3-8)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-3-9)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-3-10)_set_env("OPENAI_API_KEY")

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-4-1)OPENAI_API_KEY: ········

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Streaming custom data[¶](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#streaming-custom-data "Permanent link")

We'll use a [prebuilt ReAct agent](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent) for this guide:

```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-5-1)fromlangchain_core.toolsimport tool
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-5-2)fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-5-3)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-5-4)fromlanggraph.prebuiltimport create_react_agent
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-5-5)fromlanggraph.configimport get_stream_writer
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-5-6)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-5-7)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-5-8)@tool
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-5-9)async defget_items(place: str) -> str:
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-5-10)"""Use this tool to list items one might find in a place you're asked about."""
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-5-11)  writer = get_stream_writer()
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-5-12)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-5-13)  # this can be replaced with any actual streaming logic that you might have
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-5-14)  items = ["books", "penciles", "pictures"]
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-5-15)  for chunk in items:
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-5-16)    writer({"custom_tool_data": chunk})
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-5-17)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-5-18)  return ", ".join(items)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-5-19)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-5-20)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-5-21)llm = ChatOpenAI(model_name="gpt-4o-mini")
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-5-22)tools = [get_items]
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-5-23)# contains `agent` (tool-calling LLM) and `tools` (tool executor) nodes
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-5-24)agent = create_react_agent(llm, tools=tools)

```


API Reference: [tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html) | [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html) | [create_react_agent](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent)

Let's now invoke our agent with an input that requires a tool call:

```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-6-1)inputs = {
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-6-2)  "messages": [ 
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-6-3)    {"role": "user", "content": "what items are in the office?"}
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-6-4)  ]
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-6-5)}
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-6-6)async for chunk in agent.astream(
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-6-7)  inputs,
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-6-8)  stream_mode="custom",
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-6-9)):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-6-10)  print(chunk)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-7-1){'custom_tool_data': 'books'}
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-7-2){'custom_tool_data': 'penciles'}
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-7-3){'custom_tool_data': 'pictures'}

```


## Streaming LLM tokens[¶](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#streaming-llm-tokens "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-8-1)fromlangchain_core.messagesimport AIMessageChunk
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-8-2)fromlangchain_core.runnablesimport RunnableConfig
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-8-3)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-8-4)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-8-5)@tool
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-8-6)async defget_items(
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-8-7)  place: str,
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-8-8)  # Manually accept config (needed for Python <= 3.10)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-8-9)  config: RunnableConfig,
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-8-10)) -> str:
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-8-11)"""Use this tool to list items one might find in a place you're asked about."""
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-8-12)  # Attention: when using async, you should be invoking the LLM using ainvoke!
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-8-13)  # If you fail to do so, streaming will NOT work.
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-8-14)  response = await llm.ainvoke(
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-8-15)    [
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-8-16)      {
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-8-17)        "role": "user",
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-8-18)        "content": (
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-8-19)          f"Can you tell me what kind of items i might find in the following place: '{place}'. "
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-8-20)          "List at least 3 such items separating them by a comma. And include a brief description of each item."
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-8-21)        ),
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-8-22)      }
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-8-23)    ],
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-8-24)    config,
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-8-25)  )
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-8-26)  return response.content
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-8-27)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-8-28)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-8-29)tools = [get_items]
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-8-30)# contains `agent` (tool-calling LLM) and `tools` (tool executor) nodes
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-8-31)agent = create_react_agent(llm, tools=tools)

```


API Reference: [AIMessageChunk](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.AIMessageChunk.html) | [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html)

```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-9-1)inputs = {
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-9-2)  "messages": [ 
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-9-3)    {"role": "user", "content": "what items are in the bedroom?"}
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-9-4)  ]
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-9-5)}
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-9-6)async for msg, metadata in agent.astream(
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-9-7)  inputs,
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-9-8)  stream_mode="messages",
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-9-9)):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-9-10)  if (
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-9-11)    isinstance(msg, AIMessageChunk)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-9-12)    and msg.content
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-9-13)    # Stream all messages from the tool node
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-9-14)    and metadata["langgraph_node"] == "tools"
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-9-15)  ):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-9-16)    print(msg.content, end="|", flush=True)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-10-1)Certainly|!| Here| are| three| items| you| might| find| in| a| bedroom|:
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-10-2)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-10-3)|1|.| **|Bed|**|:| The| central| piece| of| furniture| in| a| bedroom|,| typically| consisting| of| a| mattress| supported| by| a| frame|.| It| is| designed| for| sleeping| and| can| vary| in| size| from| twin| to| king|.| Beds| often| have| bedding|,| including| sheets|,| pillows|,| and| comfort|ers|,| to| enhance| comfort|.
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-10-4)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-10-5)|2|.| **|D|resser|**|:| A| piece| of| furniture| with| drawers| used| for| storing| clothing| and| personal| items|.| Dress|ers| often| have| a| flat| surface| on| top|,| which| can| be| used| for| decorative| items|,| a| mirror|,| or| personal| accessories|.| They| help| keep| the| bedroom| organized| and| clutter|-free|.
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-10-6)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-10-7)|3|.| **|Night|stand|**|:| A| small| table| or| cabinet| placed| beside| the| bed|,| used| for| holding| items| such| as| a| lamp|,| alarm| clock|,| books|,| or| personal| items|.| Night|stands| provide| convenience| for| easy| access| to| essentials| during| the| night|,| adding| functionality| and| style| to| the| bedroom| decor|.|

```


## Example without LangChain[¶](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#example-without-langchain "Permanent link")

You can also stream data from within tool invocations **without using LangChain**. Below example demonstrates how to do it for a graph with a single tool-executing node. We'll leave it as an exercise for the reader to [implement ReAct agent from scratch](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch) without using LangChain.

```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-1)importoperator
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-2)importjson
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-3)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-4)fromtypingimport TypedDict
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-5)fromtyping_extensionsimport Annotated
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-6)fromlanggraph.graphimport StateGraph, START
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-7)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-8)fromopenaiimport AsyncOpenAI
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-9)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-10)openai_client = AsyncOpenAI()
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-11)model_name = "gpt-4o-mini"
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-12)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-13)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-14)async defstream_tokens(model_name: str, messages: list[dict]):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-15)  response = await openai_client.chat.completions.create(
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-16)    messages=messages, model=model_name, stream=True
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-17)  )
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-18)  role = None
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-19)  async for chunk in response:
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-20)    delta = chunk.choices[0].delta
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-21)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-22)    if delta.role is not None:
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-23)      role = delta.role
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-24)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-25)    if delta.content:
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-26)      yield {"role": role, "content": delta.content}
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-27)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-28)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-29)# this is our tool
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-30)async defget_items(place: str) -> str:
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-31)"""Use this tool to list items one might find in a place you're asked about."""
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-32)  writer = get_stream_writer()
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-33)  response = ""
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-34)  async for msg_chunk in stream_tokens(
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-35)    model_name,
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-36)    [
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-37)      {
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-38)        "role": "user",
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-39)        "content": (
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-40)          "Can you tell me what kind of items "
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-41)          f"i might find in the following place: '{place}'. "
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-42)          "List at least 3 such items separating them by a comma. "
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-43)          "And include a brief description of each item."
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-44)        ),
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-45)      }
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-46)    ],
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-47)  ):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-48)    response += msg_chunk["content"]
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-49)    writer(msg_chunk)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-50)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-51)  return response
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-52)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-53)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-54)classState(TypedDict):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-55)  messages: Annotated[list[dict], operator.add]
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-56)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-57)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-58)# this is the tool-calling graph node
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-59)async defcall_tool(state: State):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-60)  ai_message = state["messages"][-1]
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-61)  tool_call = ai_message["tool_calls"][-1]
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-62)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-63)  function_name = tool_call["function"]["name"]
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-64)  if function_name != "get_items":
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-65)    raise ValueError(f"Tool {function_name} not supported")
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-66)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-67)  function_arguments = tool_call["function"]["arguments"]
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-68)  arguments = json.loads(function_arguments)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-69)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-70)  function_response = await get_items(**arguments)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-71)  tool_message = {
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-72)    "tool_call_id": tool_call["id"],
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-73)    "role": "tool",
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-74)    "name": function_name,
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-75)    "content": function_response,
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-76)  }
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-77)  return {"messages": [tool_message]}
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-78)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-79)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-80)graph = (
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-81)  StateGraph(State) 
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-82)  .add_node(call_tool)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-83)  .add_edge(START, "call_tool")
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-84)  .compile()
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-11-85))

```


API Reference: [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START)

Let's now invoke our graph with an AI message that contains a tool call:

```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-12-1)inputs = {
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-12-2)  "messages": [
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-12-3)    {
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-12-4)      "content": None,
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-12-5)      "role": "assistant",
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-12-6)      "tool_calls": [
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-12-7)        {
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-12-8)          "id": "1",
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-12-9)          "function": {
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-12-10)            "arguments": '{"place":"bedroom"}',
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-12-11)            "name": "get_items",
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-12-12)          },
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-12-13)          "type": "function",
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-12-14)        }
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-12-15)      ],
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-12-16)    }
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-12-17)  ]
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-12-18)}
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-12-19)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-12-20)async for chunk in graph.astream(
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-12-21)  inputs,
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-12-22)  stream_mode="custom",
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-12-23)):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-12-24)  print(chunk["content"], end="|", flush=True)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-13-1)Sure|!| Here| are| three| common| items| you| might| find| in| a| bedroom|:
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-13-2)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-13-3)|1|.| **|Bed|**|:| The| focal| point| of| the| bedroom|,| a| bed| typically| consists| of| a| mattress| resting| on| a| frame|,| and| it| may| include| pillows| and| bedding|.| It| provides| a| comfortable| place| for| sleeping| and| resting|.
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-13-4)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-13-5)|2|.| **|D|resser|**|:| A| piece| of| furniture| with| multiple| drawers|,| a| dresser| is| used| for| storing| clothes|,| accessories|,| and| personal| items|.| It| often| has| a| flat| surface| that| may| be| used| to| display| decorative| items| or| a| mirror|.
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-13-6)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-13-7)|3|.| **|Night|stand|**|:| Also| known| as| a| bedside| table|,| a| night|stand| is| placed| next| to| the| bed| and| typically| holds| items| like| lamps|,| books|,| alarm| clocks|,| and| personal| belongings| for| convenience| during| the| night|.
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-13-8)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__codelineno-13-9)|These| items| contribute| to| the| functionality| and| comfort| of| the| bedroom| environment|.|

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to stream LLM tokens from specific nodes  ](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/) [ Next  How to stream from subgraphs  ](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
