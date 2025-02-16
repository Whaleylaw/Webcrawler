---
url: https://langchain-ai.github.io/langgraph/how-tos/streaming/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/streaming/#how-to-stream)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to stream 

[ ](https://langchain-ai.github.io/langgraph/how-tos/streaming/?q= "Share")

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
            * How to stream  [ How to stream  ](https://langchain-ai.github.io/langgraph/how-tos/streaming/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/streaming/#setup)
              * [ Define graph  ](https://langchain-ai.github.io/langgraph/how-tos/streaming/#define-graph)
              * [ Stream all values in the state (stream_mode="values")  ](https://langchain-ai.github.io/langgraph/how-tos/streaming/#values)
              * [ Stream state updates from the nodes (stream_mode="updates")  ](https://langchain-ai.github.io/langgraph/how-tos/streaming/#updates)
              * [ Stream debug events (stream_mode="debug")  ](https://langchain-ai.github.io/langgraph/how-tos/streaming/#debug)
              * [ Stream LLM tokens (stream_mode="messages")  ](https://langchain-ai.github.io/langgraph/how-tos/streaming/#messages)
              * [ Stream custom data (stream_mode="custom")  ](https://langchain-ai.github.io/langgraph/how-tos/streaming/#custom)
              * [ Configure multiple streaming modes  ](https://langchain-ai.github.io/langgraph/how-tos/streaming/#multiple)
            * [ How to stream LLM tokens from your graph  ](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/)
            * [ How to stream LLM tokens from specific nodes  ](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/)
            * [ How to stream data from within a tool  ](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/streaming/#setup)
  * [ Define graph  ](https://langchain-ai.github.io/langgraph/how-tos/streaming/#define-graph)
  * [ Stream all values in the state (stream_mode="values")  ](https://langchain-ai.github.io/langgraph/how-tos/streaming/#values)
  * [ Stream state updates from the nodes (stream_mode="updates")  ](https://langchain-ai.github.io/langgraph/how-tos/streaming/#updates)
  * [ Stream debug events (stream_mode="debug")  ](https://langchain-ai.github.io/langgraph/how-tos/streaming/#debug)
  * [ Stream LLM tokens (stream_mode="messages")  ](https://langchain-ai.github.io/langgraph/how-tos/streaming/#messages)
  * [ Stream custom data (stream_mode="custom")  ](https://langchain-ai.github.io/langgraph/how-tos/streaming/#custom)
  * [ Configure multiple streaming modes  ](https://langchain-ai.github.io/langgraph/how-tos/streaming/#multiple)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Streaming  ](https://langchain-ai.github.io/langgraph/how-tos#streaming)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/streaming.ipynb "Edit this page")

# How to stream[¶](https://langchain-ai.github.io/langgraph/how-tos/streaming/#how-to-stream "Permanent link")

Prerequisites

This guide assumes familiarity with the following:

  * [Streaming](https://langchain-ai.github.io/langgraph/concepts/streaming/)
  * [Chat Models](https://python.langchain.com/docs/concepts/chat_models/)



Streaming is crucial for enhancing the responsiveness of applications built on LLMs. By displaying output progressively, even before a complete response is ready, streaming significantly improves user experience (UX), particularly when dealing with the latency of LLMs.

LangGraph is built with first class support for streaming. There are several different ways to stream back outputs from a graph run:

  * `"values"`: Emit all values in the state after each step.
  * `"updates"`: Emit only the node names and updates returned by the nodes after each step. If multiple updates are made in the same step (e.g. multiple nodes are run) then those updates are emitted separately.
  * `"custom"`: Emit custom data from inside nodes using `StreamWriter`.
  * `"messages"`[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens): Emit LLM messages token-by-token together with metadata for any LLM invocations inside nodes.
  * `"debug"`: Emit debug events with as much information as possible for each step.



You can stream outputs from the graph by using `graph.stream(..., stream_mode=<stream_mode>)` method, e.g.:

[Sync](#__tabbed_1_1)[Async](#__tabbed_1_2)

```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-0-1)for chunk in graph.stream(inputs, stream_mode="updates"):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-0-2)  print(chunk)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-1-1)async for chunk in graph.astream(inputs, stream_mode="updates"):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-1-2)  print(chunk)

```


You can also combine multiple streaming mode by providing a list to `stream_mode` parameter:

[Sync](#__tabbed_2_1)[Async](#__tabbed_2_2)

```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-2-1)for chunk in graph.stream(inputs, stream_mode=["updates", "custom"]):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-2-2)  print(chunk)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-3-1)async for chunk in graph.astream(inputs, stream_mode=["updates", "custom"]):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-3-2)  print(chunk)

```


## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/streaming/#setup "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-4-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-4-2)%pip install --quiet -U langgraph langchain_openai

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-5-1)importgetpass
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-5-2)importos
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-5-3)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-5-4)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-5-5)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-5-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-5-7)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-5-8)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-5-9)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-5-10)_set_env("OPENAI_API_KEY")

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-6-1)OPENAI_API_KEY: ········

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

Let's define a simple graph with two nodes:

## Define graph[¶](https://langchain-ai.github.io/langgraph/how-tos/streaming/#define-graph "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-7-1)fromtypingimport TypedDict
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-7-2)fromlanggraph.graphimport StateGraph, START
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-7-3)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-7-4)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-7-5)classState(TypedDict):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-7-6)  topic: str
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-7-7)  joke: str
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-7-8)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-7-9)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-7-10)defrefine_topic(state: State):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-7-11)  return {"topic": state["topic"] + " and cats"}
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-7-12)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-7-13)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-7-14)defgenerate_joke(state: State):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-7-15)  return {"joke": f"This is a joke about {state['topic']}"}
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-7-16)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-7-17)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-7-18)graph = (
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-7-19)  StateGraph(State)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-7-20)  .add_node(refine_topic)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-7-21)  .add_node(generate_joke)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-7-22)  .add_edge(START, "refine_topic")
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-7-23)  .add_edge("refine_topic", "generate_joke")
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-7-24)  .compile()
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-7-25))

```


API Reference: [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START)

## Stream all values in the state (stream_mode="values")[¶](https://langchain-ai.github.io/langgraph/how-tos/streaming/#values "Permanent link")

Use this to stream **all values** in the state after each step.

```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-8-1)for chunk in graph.stream(
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-8-2)  {"topic": "ice cream"},
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-8-3)  stream_mode="values",
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-8-4)):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-8-5)  print(chunk)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-9-1){'topic': 'ice cream'}
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-9-2){'topic': 'ice cream and cats'}
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-9-3){'topic': 'ice cream and cats', 'joke': 'This is a joke about ice cream and cats'}

```


## Stream state updates from the nodes (stream_mode="updates")[¶](https://langchain-ai.github.io/langgraph/how-tos/streaming/#updates "Permanent link")

Use this to stream only the **state updates** returned by the nodes after each step. The streamed outputs include the name of the node as well as the update.

```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-10-1)for chunk in graph.stream(
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-10-2)  {"topic": "ice cream"},
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-10-3)  stream_mode="updates",
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-10-4)):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-10-5)  print(chunk)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-11-1){'refine_topic': {'topic': 'ice cream and cats'}}
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-11-2){'generate_joke': {'joke': 'This is a joke about ice cream and cats'}}

```


## Stream debug events (stream_mode="debug")[¶](https://langchain-ai.github.io/langgraph/how-tos/streaming/#debug "Permanent link")

Use this to stream **debug events** with as much information as possible for each step. Includes information about tasks that were scheduled to be executed as well as the results of the task executions.

```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-12-1)for chunk in graph.stream(
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-12-2)  {"topic": "ice cream"},
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-12-3)  stream_mode="debug",
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-12-4)):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-12-5)  print(chunk)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-13-1){'type': 'task', 'timestamp': '2025-01-28T22:06:34.789803+00:00', 'step': 1, 'payload': {'id': 'eb305d74-3460-9510-d516-beed71a63414', 'name': 'refine_topic', 'input': {'topic': 'ice cream'}, 'triggers': ['start:refine_topic']}}
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-13-2){'type': 'task_result', 'timestamp': '2025-01-28T22:06:34.790013+00:00', 'step': 1, 'payload': {'id': 'eb305d74-3460-9510-d516-beed71a63414', 'name': 'refine_topic', 'error': None, 'result': [('topic', 'ice cream and cats')], 'interrupts': []}}
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-13-3){'type': 'task', 'timestamp': '2025-01-28T22:06:34.790165+00:00', 'step': 2, 'payload': {'id': '74355cb8-6284-25e0-579f-430493c1bdab', 'name': 'generate_joke', 'input': {'topic': 'ice cream and cats'}, 'triggers': ['refine_topic']}}
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-13-4){'type': 'task_result', 'timestamp': '2025-01-28T22:06:34.790337+00:00', 'step': 2, 'payload': {'id': '74355cb8-6284-25e0-579f-430493c1bdab', 'name': 'generate_joke', 'error': None, 'result': [('joke', 'This is a joke about ice cream and cats')], 'interrupts': []}}

```


## Stream LLM tokens ([stream_mode="messages"](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens))[¶](https://langchain-ai.github.io/langgraph/how-tos/streaming/#messages "Permanent link")

Use this to stream **LLM messages token-by-token** together with metadata for any LLM invocations inside nodes or tasks. Let's modify the above example to include LLM calls:

```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-14-1)fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-14-2)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-14-3)llm = ChatOpenAI(model="gpt-4o-mini")
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-14-4)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-14-5)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-14-6)defgenerate_joke(state: State):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-14-7)  llm_response = llm.invoke(
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-14-8)    [
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-14-9)      {"role": "user", "content": f"Generate a joke about {state['topic']}"}
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-14-10)    ]
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-14-11)  )
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-14-12)  return {"joke": llm_response.content}
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-14-13)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-14-14)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-14-15)graph = (
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-14-16)  StateGraph(State)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-14-17)  .add_node(refine_topic)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-14-18)  .add_node(generate_joke)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-14-19)  .add_edge(START, "refine_topic")
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-14-20)  .add_edge("refine_topic", "generate_joke")
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-14-21)  .compile()
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-14-22))

```


API Reference: [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html)

```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-15-1)for message_chunk, metadata in graph.stream(
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-15-2)  {"topic": "ice cream"},
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-15-3)  stream_mode="messages",
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-15-4)):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-15-5)  if message_chunk.content:
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-15-6)    print(message_chunk.content, end="|", flush=True)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-16-1)Why| did| the| cat| sit| on| the| ice| cream| cone|?
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-16-2)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-16-3)|Because| it| wanted| to| be| a| "|p|urr|-f|ect|"| scoop|!| 🍦|🐱|

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-17-1)metadata

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-18-1){'langgraph_step': 2,
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-18-2) 'langgraph_node': 'generate_joke',
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-18-3) 'langgraph_triggers': ['refine_topic'],
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-18-4) 'langgraph_path': ('__pregel_pull', 'generate_joke'),
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-18-5) 'langgraph_checkpoint_ns': 'generate_joke:568879bc-8800-2b0d-a5b5-059526a4bebf',
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-18-6) 'checkpoint_ns': 'generate_joke:568879bc-8800-2b0d-a5b5-059526a4bebf',
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-18-7) 'ls_provider': 'openai',
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-18-8) 'ls_model_name': 'gpt-4o-mini',
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-18-9) 'ls_model_type': 'chat',
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-18-10) 'ls_temperature': 0.7}

```


## Stream custom data (stream_mode="custom")[¶](https://langchain-ai.github.io/langgraph/how-tos/streaming/#custom "Permanent link")

Use this to stream custom data from inside nodes using `StreamWriter`[](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.StreamWriter).

```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-19-1)fromlanggraph.typesimport StreamWriter
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-19-2)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-19-3)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-19-4)defgenerate_joke(state: State, writer: StreamWriter):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-19-5)  writer({"custom_key": "Writing custom data while generating a joke"})
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-19-6)  return {"joke": f"This is a joke about {state['topic']}"}
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-19-7)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-19-8)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-19-9)graph = (
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-19-10)  StateGraph(State)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-19-11)  .add_node(refine_topic)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-19-12)  .add_node(generate_joke)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-19-13)  .add_edge(START, "refine_topic")
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-19-14)  .add_edge("refine_topic", "generate_joke")
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-19-15)  .compile()
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-19-16))

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-20-1)for chunk in graph.stream(
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-20-2)  {"topic": "ice cream"},
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-20-3)  stream_mode="custom",
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-20-4)):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-20-5)  print(chunk)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-21-1){'custom_key': 'Writing custom data while generating a joke'}

```


## Configure multiple streaming modes[¶](https://langchain-ai.github.io/langgraph/how-tos/streaming/#multiple "Permanent link")

Use this to combine multiple streaming modes. The outputs are streamed as tuples `(stream_mode, streamed_output)`.

```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-22-1)for stream_mode, chunk in graph.stream(
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-22-2)  {"topic": "ice cream"},
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-22-3)  stream_mode=["updates", "custom"],
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-22-4)):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-22-5)  print(f"Stream mode: {stream_mode}")
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-22-6)  print(chunk)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-22-7)  print("\n")

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-23-1)Stream mode: updates
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-23-2){'refine_topic': {'topic': 'ice cream and cats'}}
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-23-3)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-23-4)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-23-5)Stream mode: custom
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-23-6){'custom_key': 'Writing custom data while generating a joke'}
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-23-7)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-23-8)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-23-9)Stream mode: updates
[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__codelineno-23-10){'generate_joke': {'joke': 'This is a joke about ice cream and cats'}}

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to review tool calls (Functional API)  ](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/) [ Next  How to stream LLM tokens from your graph  ](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/streaming/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
