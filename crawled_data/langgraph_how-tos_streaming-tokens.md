---
url: https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#how-to-stream-llm-tokens-from-your-graph)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to stream LLM tokens from your graph 

[ ](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/?q= "Share")

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
            * How to stream LLM tokens from your graph  [ How to stream LLM tokens from your graph  ](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#setup)
              * [ Example  ](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#example)
                * [ Filter to specific LLM invocation  ](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#filter-to-specific-llm-invocation)
              * [ Example without LangChain  ](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#example-without-langchain)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#setup)
  * [ Example  ](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#example)
    * [ Filter to specific LLM invocation  ](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#filter-to-specific-llm-invocation)
  * [ Example without LangChain  ](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#example-without-langchain)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Streaming  ](https://langchain-ai.github.io/langgraph/how-tos#streaming)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/streaming-tokens.ipynb "Edit this page")

# How to stream LLM tokens from your graph[¶](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#how-to-stream-llm-tokens-from-your-graph "Permanent link")

Prerequisites

This guide assumes familiarity with the following:

  * [Streaming](https://langchain-ai.github.io/langgraph/concepts/streaming/)
  * [Chat Models](https://python.langchain.com/docs/concepts/chat_models/)



When building LLM applications with LangGraph, you might want to stream individual LLM tokens from the LLM calls inside LangGraph nodes. You can do so via `graph.stream(..., stream_mode="messages")`:

```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-0-1)fromlanggraph.graphimport StateGraph
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-0-2)fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-0-3)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-0-4)model = ChatOpenAI()
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-0-5)defcall_model(state: State):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-0-6)  model.invoke(...)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-0-7)  ...
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-0-8)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-0-9)graph = (
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-0-10)  StateGraph(State)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-0-11)  .add_node(call_model)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-0-12)  ...
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-0-13)  .compile()
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-0-14)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-0-15)for msg, metadata in graph.stream(inputs, stream_mode="messages"):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-0-16)  print(msg)

```


API Reference: [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph)

The streamed outputs will be tuples of `(message chunk, metadata)`:

  * message chunk is the token streamed by the LLM
  * metadata is a dictionary with information about the graph node where the LLM was called as well as the LLM invocation metadata



Using without LangChain

If you need to stream LLM tokens **without using LangChain** , you can use `stream_mode="custom"`[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#custom) to stream the outputs from LLM provider clients directly. Check out the [example below](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#example-without-langchain) to learn more.

Async in Python < 3.11

When using Python < 3.11 with async code, please ensure you manually pass the `RunnableConfig` through to the chat model when invoking it like so: `model.ainvoke(..., config)`. The stream method collects all events from your nested code using a streaming tracer passed as a callback. In 3.11 and above, this is automatically handled via [contextvars](https://docs.python.org/3/library/contextvars.html); prior to 3.11, [asyncio's tasks](https://docs.python.org/3/library/asyncio-task.html#asyncio.create_task) lacked proper `contextvar` support, meaning that the callbacks will only propagate if you manually pass the config through. We do this in the `call_model` function below.

## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#setup "Permanent link")

First we need to install the packages required

```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-1-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-1-2)%pip install --quiet -U langgraph langchain_openai

```


Next, we need to set API keys for OpenAI (the LLM we will use).

```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-2-1)importgetpass
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-2-2)importos
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-2-3)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-2-4)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-2-5)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-2-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-2-7)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-2-8)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-2-9)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-2-10)_set_env("OPENAI_API_KEY")

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

Note

Note that in `call_model(state: State, config: RunnableConfig):` below, we a) accept the `RunnableConfig`[](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig) in the node function and b) pass it in as the second arg for `model.ainvoke(..., config)`. This is optional for python >= 3.11.

## Example[¶](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#example "Permanent link")

Below we demonstrate an example with two LLM calls in a single node.

```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-3-1)fromtypingimport TypedDict
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-3-2)fromlanggraph.graphimport START, StateGraph, MessagesState
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-3-3)fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-3-4)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-3-5)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-3-6)# Note: we're adding the tags here to be able to filter the model outputs down the line
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-3-7)joke_model = ChatOpenAI(model="gpt-4o-mini", tags=["joke"])
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-3-8)poem_model = ChatOpenAI(model="gpt-4o-mini", tags=["poem"])
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-3-9)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-3-10)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-3-11)classState(TypedDict):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-3-12)  topic: str
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-3-13)  joke: str
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-3-14)  poem: str
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-3-15)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-3-16)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-3-17)async defcall_model(state, config):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-3-18)  topic = state["topic"]
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-3-19)  print("Writing joke...")
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-3-20)  # Note: Passing the config through explicitly is required for python < 3.11
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-3-21)  # Since context var support wasn't added before then: https://docs.python.org/3/library/asyncio-task.html#creating-tasks
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-3-22)  joke_response = await joke_model.ainvoke(
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-3-23)    [{"role": "user", "content": f"Write a joke about {topic}"}],
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-3-24)    config,
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-3-25)  )
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-3-26)  print("\n\nWriting poem...")
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-3-27)  poem_response = await poem_model.ainvoke(
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-3-28)    [{"role": "user", "content": f"Write a short poem about {topic}"}],
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-3-29)    config,
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-3-30)  )
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-3-31)  return {"joke": joke_response.content, "poem": poem_response.content}
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-3-32)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-3-33)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-3-34)graph = StateGraph(State).add_node(call_model).add_edge(START, "call_model").compile()

```


API Reference: [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph)

```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-4-1)async for msg, metadata in graph.astream(
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-4-2)  {"topic": "cats"},
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-4-3)  stream_mode="messages",
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-4-4)):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-4-5)  if msg.content:
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-4-6)    print(msg.content, end="|", flush=True)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-5-1)Writing joke...
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-5-2)Why| was| the| cat| sitting| on| the| computer|?
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-5-3)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-5-4)|Because| it| wanted| to| keep| an| eye| on| the| mouse|!|
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-5-5)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-5-6)Writing poem...
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-5-7)In| sun|lit| patches|,| sleek| and| sly|,| 
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-5-8)|Wh|isk|ers| twitch| as| shadows| fly|.| 
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-5-9)|With| velvet| paws| and| eyes| so| bright|,| 
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-5-10)|They| dance| through| dreams|,| both| day| and| night|.| 
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-5-11)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-5-12)|A| playful| p|ounce|,| a| gentle| p|urr|,| 
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-5-13)|In| every| leap|,| a| soft| allure|.| 
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-5-14)|Cur|led| in| warmth|,| a| silent| grace|,| 
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-5-15)|Each| furry| friend|,| a| warm| embrace|.| 
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-5-16)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-5-17)|Myst|ery| wrapped| in| fur| and| charm|,| 
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-5-18)|A| soothing| presence|,| a| gentle| balm|.| 
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-5-19)|In| their| gaze|,| the| world| slows| down|,| 
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-5-20)|For| in| their| realm|,| we're| all| ren|own|.|

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-6-1)metadata

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-7-1){'langgraph_step': 1,
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-7-2) 'langgraph_node': 'call_model',
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-7-3) 'langgraph_triggers': ['start:call_model'],
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-7-4) 'langgraph_path': ('__pregel_pull', 'call_model'),
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-7-5) 'langgraph_checkpoint_ns': 'call_model:6ddc5f0f-1dd0-325d-3014-f949286ce595',
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-7-6) 'checkpoint_ns': 'call_model:6ddc5f0f-1dd0-325d-3014-f949286ce595',
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-7-7) 'ls_provider': 'openai',
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-7-8) 'ls_model_name': 'gpt-4o-mini',
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-7-9) 'ls_model_type': 'chat',
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-7-10) 'ls_temperature': 0.7,
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-7-11) 'tags': ['poem']}

```


### Filter to specific LLM invocation[¶](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#filter-to-specific-llm-invocation "Permanent link")

You can see that we're streaming tokens from all of the LLM invocations. Let's now filter the streamed tokens to include only a specific LLM invocation. We can use the streamed metadata and filter events using the tags we've added to the LLMs previously:

```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-8-1)async for msg, metadata in graph.astream(
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-8-2)  {"topic": "cats"},
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-8-3)  stream_mode="messages",
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-8-4)):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-8-5)  if msg.content and "joke" in metadata.get("tags", []):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-8-6)    print(msg.content, end="|", flush=True)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-9-1)Writing joke...
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-9-2)Why| was| the| cat| sitting| on| the| computer|?
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-9-3)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-9-4)|Because| it| wanted| to| keep| an| eye| on| the| mouse|!|
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-9-5)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-9-6)Writing poem...

```


## Example without LangChain[¶](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#example-without-langchain "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-10-1)fromopenaiimport AsyncOpenAI
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-10-2)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-10-3)openai_client = AsyncOpenAI()
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-10-4)model_name = "gpt-4o-mini"
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-10-5)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-10-6)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-10-7)async defstream_tokens(model_name: str, messages: list[dict]):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-10-8)  response = await openai_client.chat.completions.create(
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-10-9)    messages=messages, model=model_name, stream=True
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-10-10)  )
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-10-11)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-10-12)  role = None
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-10-13)  async for chunk in response:
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-10-14)    delta = chunk.choices[0].delta
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-10-15)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-10-16)    if delta.role is not None:
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-10-17)      role = delta.role
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-10-18)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-10-19)    if delta.content:
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-10-20)      yield {"role": role, "content": delta.content}
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-10-21)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-10-22)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-10-23)async defcall_model(state, config, writer):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-10-24)  topic = state["topic"]
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-10-25)  joke = ""
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-10-26)  poem = ""
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-10-27)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-10-28)  print("Writing joke...")
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-10-29)  async for msg_chunk in stream_tokens(
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-10-30)    model_name, [{"role": "user", "content": f"Write a joke about {topic}"}]
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-10-31)  ):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-10-32)    joke += msg_chunk["content"]
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-10-33)    metadata = {**config["metadata"], "tags": ["joke"]}
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-10-34)    chunk_to_stream = (msg_chunk, metadata)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-10-35)    writer(chunk_to_stream)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-10-36)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-10-37)  print("\n\nWriting poem...")
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-10-38)  async for msg_chunk in stream_tokens(
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-10-39)    model_name, [{"role": "user", "content": f"Write a short poem about {topic}"}]
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-10-40)  ):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-10-41)    poem += msg_chunk["content"]
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-10-42)    metadata = {**config["metadata"], "tags": ["poem"]}
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-10-43)    chunk_to_stream = (msg_chunk, metadata)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-10-44)    writer(chunk_to_stream)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-10-45)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-10-46)  return {"joke": joke, "poem": poem}
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-10-47)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-10-48)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-10-49)graph = StateGraph(State).add_node(call_model).add_edge(START, "call_model").compile()

```


stream_mode="custom"

When streaming LLM tokens without LangChain, we recommend using `stream_mode="custom"`[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#stream-modecustom). This allows you to explicitly control which data from the LLM provider APIs to include in LangGraph streamed outputs, including any additional metadata.

```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-11-1)async for msg, metadata in graph.astream(
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-11-2)  {"topic": "cats"},
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-11-3)  stream_mode="custom",
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-11-4)):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-11-5)  print(msg["content"], end="|", flush=True)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-12-1)Writing joke...
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-12-2)Why| was| the| cat| sitting| on| the| computer|?
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-12-3)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-12-4)|Because| it| wanted| to| keep| an| eye| on| the|
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-12-5)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-12-6)Writing poem...
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-12-7) mouse|!|In| sun|lit| patches|,| they| stretch| and| y|awn|,| 
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-12-8)|With| whispered| paws| at| the| break| of| dawn|.| 
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-12-9)|Wh|isk|ers| twitch| in| the| morning| light|,| 
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-12-10)|Sil|ken| shadows|,| a| graceful| sight|.| 
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-12-11)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-12-12)|The| gentle| p|urr|s|,| a| soothing| song|,| 
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-12-13)|In| a| world| of| comfort|,| where| they| belong|.| 
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-12-14)|M|yster|ious| hearts| wrapped| in| soft|est| fur|,| 
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-12-15)|F|eline| whispers| in| every| p|urr|.| 
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-12-16)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-12-17)|Ch|asing| dreams| on| a| moon|lit| chase|,| 
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-12-18)|With| a| flick| of| a| tail|,| they| glide| with| grace|.| 
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-12-19)|Oh|,| playful| spirits| of| whisk|ered| cheer|,| 
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-12-20)|In| your| quiet| company|,| the| world| feels| near|.| |

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-13-1)metadata

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-14-1){'langgraph_step': 1,
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-14-2) 'langgraph_node': 'call_model',
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-14-3) 'langgraph_triggers': ['start:call_model'],
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-14-4) 'langgraph_path': ('__pregel_pull', 'call_model'),
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-14-5) 'langgraph_checkpoint_ns': 'call_model:3fa3fbe1-39d8-5209-dd77-0da38d4cc1c9',
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-14-6) 'tags': ['poem']}

```


To filter to the specific LLM invocation, you can use the streamed metadata:

```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-15-1)async for msg, metadata in graph.astream(
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-15-2)  {"topic": "cats"},
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-15-3)  stream_mode="custom",
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-15-4)):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-15-5)  if "poem" in metadata.get("tags", []):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-15-6)    print(msg["content"], end="|", flush=True)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-16-1)Writing joke...
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-16-2)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-16-3)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-16-4)Writing poem...
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-16-5)In| shadows| soft|,| they| weave| and| play|,| 
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-16-6)|With| whispered| paws|,| they| greet| the| day|.| 
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-16-7)|Eyes| like| lantern|s|,| bright| and| keen|,| 
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-16-8)|Guard|ians| of| secrets|,| unseen|,| serene|.| 
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-16-9)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-16-10)|They| twist| and| stretch| in| sun|lit| beams|,| 
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-16-11)|Ch|asing| the| echoes| of| half|-|formed| dreams|.| 
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-16-12)|With| p|urring| songs| that| soothe| the| night|,| 
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-16-13)|F|eline| spirits|,| pure| delight|.| 
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-16-14)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-16-15)|On| windows|ills|,| they| perch| and| stare|,| 
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-16-16)|Ad|vent|urers| bold| with| a| graceful| flair|.| 
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-16-17)|In| every| leap| and| playful| bound|,| 
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__codelineno-16-18)|The| magic| of| cats|—|where| love| is| found|.|

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to stream  ](https://langchain-ai.github.io/langgraph/how-tos/streaming/) [ Next  How to stream LLM tokens from specific nodes  ](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
