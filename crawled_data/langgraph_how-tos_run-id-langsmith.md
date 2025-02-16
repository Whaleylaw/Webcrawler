---
url: https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#how-to-pass-custom-run-id-or-set-tags-and-metadata-for-graph-runs-in-langsmith)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to pass custom run ID or set tags and metadata for graph runs in LangSmith 

[ ](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/?q= "Share")

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
          * [ Streaming  ](https://langchain-ai.github.io/langgraph/how-tos#streaming)
          * [ Tool calling  ](https://langchain-ai.github.io/langgraph/how-tos#tool-calling)
          * [ Subgraphs  ](https://langchain-ai.github.io/langgraph/how-tos#subgraphs)
          * [ Multi-agent  ](https://langchain-ai.github.io/langgraph/how-tos#multi-agent)
          * [ State Management  ](https://langchain-ai.github.io/langgraph/how-tos#state-management)
          * Other  Other 
            * [ Other  ](https://langchain-ai.github.io/langgraph/how-tos#other)
            * [ How to run a graph asynchronously  ](https://langchain-ai.github.io/langgraph/how-tos/async/)
            * [ How to force tool-calling agent to structure output  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/)
            * How to pass custom run ID or set tags and metadata for graph runs in LangSmith  [ How to pass custom run ID or set tags and metadata for graph runs in LangSmith  ](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/) Table of contents 
              * [ TLDR  ](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#tldr)
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#setup)
              * [ Define the graph  ](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#define-the-graph)
              * [ Run your graph  ](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#run-your-graph)
              * [ View the trace in LangSmith  ](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#view-the-trace-in-langsmith)
            * [ How to integrate LangGraph with AutoGen, CrewAI, and other frameworks  ](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/)
            * [ How to integrate LangGraph (functional API) with AutoGen, CrewAI, and other frameworks  ](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration-functional/)
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

  * [ TLDR  ](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#tldr)
  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#setup)
  * [ Define the graph  ](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#define-the-graph)
  * [ Run your graph  ](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#run-your-graph)
  * [ View the trace in LangSmith  ](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#view-the-trace-in-langsmith)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Other  ](https://langchain-ai.github.io/langgraph/how-tos#other)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/run-id-langsmith.ipynb "Edit this page")

# How to pass custom run ID or set tags and metadata for graph runs in LangSmith[¶](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#how-to-pass-custom-run-id-or-set-tags-and-metadata-for-graph-runs-in-langsmith "Permanent link")

Prerequisites

This guide assumes familiarity with the following: 

  * [ LangSmith Documentation ](https://docs.smith.langchain.com)
  * [ LangSmith Platform ](https://smith.langchain.com)
  * [ RunnableConfig ](https://api.python.langchain.com/en/latest/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig)
  * [ Add metadata and tags to traces ](https://docs.smith.langchain.com/how_to_guides/tracing/trace_with_langchain#add-metadata-and-tags-to-traces)
  * [ Customize run name ](https://docs.smith.langchain.com/how_to_guides/tracing/trace_with_langchain#customize-run-name)



Debugging graph runs can sometimes be difficult to do in an IDE or terminal. [LangSmith](https://docs.smith.langchain.com) lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read the [LangSmith documentation](https://docs.smith.langchain.com) for more information on how to get started.

To make it easier to identify and analyzed traces generated during graph invocation, you can set additional configuration at run time (see [RunnableConfig](https://api.python.langchain.com/en/latest/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig)):

**Field** | **Type** | **Description**  
---|---|---  
run_name | `str` | Name for the tracer run for this call. Defaults to the name of the class.  
run_id | `UUID` | Unique identifier for the tracer run for this call. If not provided, a new UUID will be generated.  
tags | `List[str]` | Tags for this call and any sub-calls (e.g., a Chain calling an LLM). You can use these to filter calls.  
metadata | `Dict[str, Any]` | Metadata for this call and any sub-calls (e.g., a Chain calling an LLM). Keys should be strings, values should be JSON-serializable.  
  
LangGraph graphs implement the [LangChain Runnable Interface](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html) and accept a second argument (`RunnableConfig`) in methods like `invoke`, `ainvoke`, `stream` etc.

The LangSmith platform will allow you to search and filter traces based on `run_name`, `run_id`, `tags` and `metadata`.

## TLDR[¶](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#tldr "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-0-1)importuuid
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-0-2)# Generate a random UUID -- it must be a UUID
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-0-3)config = {"run_id": uuid.uuid4()}, "tags": ["my_tag1"], "metadata": {"a": 5}}
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-0-4)# Works with all standard Runnable methods 
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-0-5)# like invoke, batch, ainvoke, astream_events etc
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-0-6)graph.stream(inputs, config, stream_mode="values")

```


The rest of the how to guide will show a full agent.

## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#setup "Permanent link")

First, let's install the required packages and set our API keys

```
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-1-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-1-2)%pip install --quiet -U langgraph langchain_openai

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-2-1)importgetpass
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-2-2)importos
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-2-3)
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-2-4)
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-2-5)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-2-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-2-7)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-2-8)
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-2-9)
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-2-10)_set_env("OPENAI_API_KEY")
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-2-11)_set_env("LANGSMITH_API_KEY")

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Define the graph[¶](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#define-the-graph "Permanent link")

For this example we will use the [prebuilt ReAct agent](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/).

```
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-3-1)fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-3-2)fromtypingimport Literal
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-3-3)fromlanggraph.prebuiltimport create_react_agent
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-3-4)fromlangchain_core.toolsimport tool
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-3-5)
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-3-6)# First we initialize the model we want to use.
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-3-7)model = ChatOpenAI(model="gpt-4o", temperature=0)
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-3-8)
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-3-9)
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-3-10)# For this tutorial we will use custom tool that returns pre-defined values for weather in two cities (NYC & SF)
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-3-11)@tool
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-3-12)defget_weather(city: Literal["nyc", "sf"]):
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-3-13)"""Use this to get weather information."""
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-3-14)  if city == "nyc":
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-3-15)    return "It might be cloudy in nyc"
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-3-16)  elif city == "sf":
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-3-17)    return "It's always sunny in sf"
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-3-18)  else:
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-3-19)    raise AssertionError("Unknown city")
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-3-20)
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-3-21)
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-3-22)tools = [get_weather]
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-3-23)
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-3-24)
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-3-25)# Define the graph
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-3-26)graph = create_react_agent(model, tools=tools)

```


API Reference: [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html) | [tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html) | [create_react_agent](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent)

## Run your graph[¶](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#run-your-graph "Permanent link")

Now that we've defined our graph let's run it once and view the trace in LangSmith. In order for our trace to be easily accessible in LangSmith, we will pass in a custom `run_id` in the config.

This assumes that you have set your `LANGSMITH_API_KEY` environment variable.

Note that you can also configure what project to trace to by setting the `LANGCHAIN_PROJECT` environment variable, by default runs will be traced to the `default` project.

```
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-4-1)importuuid
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-4-2)
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-4-3)
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-4-4)defprint_stream(stream):
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-4-5)  for s in stream:
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-4-6)    message = s["messages"][-1]
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-4-7)    if isinstance(message, tuple):
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-4-8)      print(message)
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-4-9)    else:
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-4-10)      message.pretty_print()
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-4-11)
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-4-12)
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-4-13)inputs = {"messages": [("user", "what is the weather in sf")]}
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-4-14)
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-4-15)config = {"run_name": "agent_007", "tags": ["cats are awesome"]}
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-4-16)
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-4-17)print_stream(graph.stream(inputs, config, stream_mode="values"))

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-5-1)================================[1m Human Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-5-2)
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-5-3)what is the weather in sf
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-5-4)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-5-5)Tool Calls:
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-5-6) get_weather (call_9ZudXyMAdlUjptq9oMGtQo8o)
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-5-7) Call ID: call_9ZudXyMAdlUjptq9oMGtQo8o
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-5-8) Args:
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-5-9)  city: sf
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-5-10)=================================[1m Tool Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-5-11)Name: get_weather
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-5-12)
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-5-13)It's always sunny in sf
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-5-14)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-5-15)
[](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__codelineno-5-16)The weather in San Francisco is currently sunny.

```


## View the trace in LangSmith[¶](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#view-the-trace-in-langsmith "Permanent link")

Now that we've ran our graph, let's head over to LangSmith and view our trace. First click into the project that you traced to (in our case the default project). You should see a run with the custom run name "agent_007".

![image.png]()

In addition, you will be able to filter traces after the fact using the tags or metadata provided. For example,

![image.png]()

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to force tool-calling agent to structure output  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/) [ Next  How to integrate LangGraph with AutoGen, CrewAI, and other frameworks  ](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
