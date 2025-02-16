---
url: https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#how-to-pass-runtime-values-to-tools)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to pass runtime values to tools 

[ ](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/?q= "Share")

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
          * Tool calling  Tool calling 
            * [ Tool calling  ](https://langchain-ai.github.io/langgraph/how-tos#tool-calling)
            * [ How to call tools using ToolNode  ](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/)
            * [ How to handle tool calling errors  ](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/)
            * How to pass runtime values to tools  [ How to pass runtime values to tools  ](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#setup)
              * [ Pass graph state to tools  ](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#pass-graph-state-to-tools)
                * [ Define the tools  ](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#define-the-tools)
                * [ Define the graph  ](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#define-the-graph)
                * [ Use it!  ](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#use-it)
              * [ Pass shared memory (store) to the graph  ](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#pass-shared-memory-store-to-the-graph)
                * [ Define the tools  ](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#define-the-tools_1)
                * [ Define the graph  ](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#define-the-graph_1)
                * [ Use it!  ](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#use-it_1)
            * [ How to update graph state from tools  ](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/)
            * [ How to pass config to tools  ](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/)
            * [ How to handle large numbers of tools  ](https://langchain-ai.github.io/langgraph/how-tos/many-tools/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#setup)
  * [ Pass graph state to tools  ](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#pass-graph-state-to-tools)
    * [ Define the tools  ](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#define-the-tools)
    * [ Define the graph  ](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#define-the-graph)
    * [ Use it!  ](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#use-it)
  * [ Pass shared memory (store) to the graph  ](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#pass-shared-memory-store-to-the-graph)
    * [ Define the tools  ](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#define-the-tools_1)
    * [ Define the graph  ](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#define-the-graph_1)
    * [ Use it!  ](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#use-it_1)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Tool calling  ](https://langchain-ai.github.io/langgraph/how-tos#tool-calling)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/pass-run-time-values-to-tools.ipynb "Edit this page")

# How to pass runtime values to tools[¶](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#how-to-pass-runtime-values-to-tools "Permanent link")

Sometimes, you want to let a tool-calling LLM populate a _subset_ of the tool functions' arguments and provide the other values for the other arguments at runtime. If you're using LangChain-style [tools](https://python.langchain.com/docs/concepts/#tools), an easy way to handle this is by annotating function parameters with [InjectedArg](https://python.langchain.com/docs/how_to/tool_runtime/). This annotation excludes that parameter from being shown to the LLM.

In LangGraph applications you might want to pass the graph state or [shared memory](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/) (store) to the tools at runtime. This type of stateful tools is useful when a tool's output is affected by past agent steps (e.g. if you're using a sub-agent as a tool, and want to pass the message history in to the sub-agent), or when a tool's input needs to be validated given context from past agent steps.

In this guide we'll demonstrate how to do so using LangGraph's prebuilt [ToolNode](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/).

Prerequisites

This guide targets **LangChain tool calling** assumes familiarity with the following: 

  * [ Tools ](https://python.langchain.com/docs/concepts/#tools)
  * [ State ](https://langchain-ai.github.io/langgraph/concepts/low_level/#state)
  * [ Tool-calling ](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#tool-calling-agent)

You can still use tool calling in LangGraph using your provider SDK without losing any of LangGraph's core features. 

The core technique the examples below is to **annotate** a parameter as "injected", meaning it will be injected by your program and should not be seen or populated by the LLM. Let the following codesnippet serve as a tl;dr:

```
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-0-1)fromtypingimport Annotated
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-0-2)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-0-3)fromlangchain_core.runnablesimport RunnableConfig
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-0-4)fromlangchain_core.toolsimport InjectedToolArg
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-0-5)fromlanggraph.store.baseimport BaseStore
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-0-6)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-0-7)fromlanggraph.prebuiltimport InjectedState, InjectedStore
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-0-8)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-0-9)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-0-10)# Can be sync or async; @tool decorator not required
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-0-11)async defmy_tool(
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-0-12)  # These arguments are populated by the LLM
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-0-13)  some_arg: str,
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-0-14)  another_arg: float,
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-0-15)  # The config: RunnableConfig is always available in LangChain calls
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-0-16)  # This is not exposed to the LLM
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-0-17)  config: RunnableConfig,
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-0-18)  # The following three are specific to the prebuilt ToolNode
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-0-19)  # (and `create_react_agent` by extension). If you are invoking the
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-0-20)  # tool on its own (in your own node), then you would need to provide these yourself.
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-0-21)  store: Annotated[BaseStore, InjectedStore],
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-0-22)  # This passes in the full state.
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-0-23)  state: Annotated[State, InjectedState],
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-0-24)  # You can also inject single fields from your state if you
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-0-25)  messages: Annotated[list, InjectedState("messages")]
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-0-26)  # The following is not compatible with create_react_agent or ToolNode
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-0-27)  # You can also exclude other arguments from being shown to the model.
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-0-28)  # These must be provided manually and are useful if you call the tools/functions in your own node
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-0-29)  # some_other_arg=Annotated["MyPrivateClass", InjectedToolArg],
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-0-30)):
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-0-31)"""Call my_tool to have an impact on the real world.
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-0-32)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-0-33)  Args:
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-0-34)    some_arg: a very important argument
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-0-35)    another_arg: another argument the LLM will provide
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-0-36)  """ # The docstring becomes the description for your tool and is passed to the model
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-0-37)  print(some_arg, another_arg, config, store, state, messages)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-0-38)  # Config, some_other_rag, store, and state are all "hidden" from
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-0-39)  # LangChain models when passed to bind_tools or with_structured_output
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-0-40)  return "... some response"

```


API Reference: [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html) | [InjectedToolArg](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.InjectedToolArg.html) | [InjectedState](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.InjectedState)

```
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-1-1)

```


## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#setup "Permanent link")

First we need to install the packages required

```
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-2-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-2-2)%pip install --quiet -U langgraph langchain-openai

```


Next, we need to set API keys for OpenAI (the chat model we will use).

```
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-3-1)importgetpass
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-3-2)importos
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-3-3)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-3-4)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-3-5)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-3-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-3-7)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-3-8)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-3-9)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-3-10)_set_env("OPENAI_API_KEY")

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-4-1)OPENAI_API_KEY: ········

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Pass graph state to tools[¶](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#pass-graph-state-to-tools "Permanent link")

Let's first take a look at how to give our tools access to the graph state. We'll need to define our graph state:

```
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-5-1)fromtypingimport List
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-5-2)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-5-3)# this is the state schema used by the prebuilt create_react_agent we'll be using below
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-5-4)fromlanggraph.prebuilt.chat_agent_executorimport AgentState
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-5-5)fromlangchain_core.documentsimport Document
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-5-6)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-5-7)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-5-8)classState(AgentState):
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-5-9)  docs: List[str]

```


API Reference: [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html)

### Define the tools[¶](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#define-the-tools "Permanent link")

We'll want our tool to take graph state as an input, but we don't want the model to try to generate this input when calling the tool. We can use the `InjectedState` annotation to mark arguments as required graph state (or some field of graph state. These arguments will not be generated by the model. When using `ToolNode`, graph state will automatically be passed in to the relevant tools and arguments.

In this example we'll create a tool that returns Documents and then another tool that actually cites the Documents that justify a claim.

Using Pydantic with LangChain

This notebook uses Pydantic v2 `BaseModel`, which requires `langchain-core >= 0.3`. Using `langchain-core < 0.3` will result in errors due to mixing of Pydantic v1 and v2 `BaseModels`. 

```
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-6-1)fromtypingimport List, Tuple
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-6-2)fromtyping_extensionsimport Annotated
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-6-3)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-6-4)fromlangchain_core.messagesimport ToolMessage
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-6-5)fromlangchain_core.toolsimport tool
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-6-6)fromlanggraph.prebuiltimport InjectedState
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-6-7)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-6-8)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-6-9)@tool
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-6-10)defget_context(question: str, state: Annotated[dict, InjectedState]):
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-6-11)"""Get relevant context for answering the question."""
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-6-12)  return "\n\n".join(doc for doc in state["docs"])

```


API Reference: [ToolMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.tool.ToolMessage.html) | [tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html) | [InjectedState](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.InjectedState)

If we look at the input schemas for these tools, we'll see that `state` is still listed:

```
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-7-1)get_context.get_input_schema().schema()

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-8-1){'description': 'Get relevant context for answering the question.',
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-8-2) 'properties': {'question': {'title': 'Question', 'type': 'string'},
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-8-3) 'state': {'title': 'State', 'type': 'object'}},
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-8-4) 'required': ['question', 'state'],
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-8-5) 'title': 'get_context',
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-8-6) 'type': 'object'}

```


But if we look at the tool call schema, which is what is passed to the model for tool-calling, `state` has been removed:

```
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-9-1)get_context.tool_call_schema.schema()

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-10-1){'description': 'Get relevant context for answering the question.',
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-10-2) 'properties': {'question': {'title': 'Question', 'type': 'string'}},
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-10-3) 'required': ['question'],
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-10-4) 'title': 'get_context',
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-10-5) 'type': 'object'}

```


### Define the graph[¶](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#define-the-graph "Permanent link")

In this example we will be using a [prebuilt ReAct agent](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/). We'll first need to define our model and a tool-calling node ([ToolNode](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.ToolNode)):

```
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-11-1)fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-11-2)fromlanggraph.prebuiltimport ToolNode, create_react_agent
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-11-3)fromlanggraph.checkpoint.memoryimport MemorySaver
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-11-4)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-11-5)model = ChatOpenAI(model="gpt-4o", temperature=0)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-11-6)tools = [get_context]
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-11-7)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-11-8)# ToolNode will automatically take care of injecting state into tools
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-11-9)tool_node = ToolNode(tools)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-11-10)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-11-11)checkpointer = MemorySaver()
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-11-12)graph = create_react_agent(model, tools, state_schema=State, checkpointer=checkpointer)

```


API Reference: [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html) | [ToolNode](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.ToolNode) | [create_react_agent](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent) | [MemorySaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.MemorySaver)

### Use it![¶](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#use-it "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-12-1)docs = [
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-12-2)  "FooBar company just raised 1 Billion dollars!",
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-12-3)  "FooBar company was founded in 2019",
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-12-4)]
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-12-5)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-12-6)inputs = {
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-12-7)  "messages": [{"type": "user", "content": "what's the latest news about FooBar"}],
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-12-8)  "docs": docs,
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-12-9)}
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-12-10)config = {"configurable": {"thread_id": "1"}}
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-12-11)for chunk in graph.stream(inputs, config, stream_mode="values"):
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-12-12)  chunk["messages"][-1].pretty_print()

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-13-1)================================[1m Human Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-13-2)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-13-3)what's the latest news about FooBar
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-13-4)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-13-5)Tool Calls:
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-13-6) get_context (call_UkqfR7z2cLJQjhatUpDeEa5H)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-13-7) Call ID: call_UkqfR7z2cLJQjhatUpDeEa5H
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-13-8) Args:
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-13-9)  question: latest news about FooBar
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-13-10)=================================[1m Tool Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-13-11)Name: get_context
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-13-12)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-13-13)FooBar company just raised 1 Billion dollars!
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-13-14)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-13-15)FooBar company was founded in 2019
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-13-16)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-13-17)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-13-18)The latest news about FooBar is that the company has just raised 1 billion dollars.

```


## Pass shared memory (store) to the graph[¶](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#pass-shared-memory-store-to-the-graph "Permanent link")

You might also want to give tools access to memory that is shared across multiple conversations or users. We can do it by passing LangGraph [Store](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/) to the tools using a different annotation -- `InjectedStore`.

Let's modify our example to save the documents in an in-memory store and retrieve them using `get_context` tool. We'll also make the documents accessible based on a user ID, so that some documents are only visible to certain users. The tool will then use the `user_id` provided in the [config](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/) to retrieve a correct set of documents.

Note

* Support for `Store` API and `InjectedStore` used in this notebook was added in LangGraph `v0.2.34`. 
* `InjectedStore` annotation requires `langchain-core >= 0.3.8`

```
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-14-1)fromlanggraph.store.memoryimport InMemoryStore
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-14-2)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-14-3)doc_store = InMemoryStore()
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-14-4)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-14-5)namespace = ("documents", "1") # user ID
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-14-6)doc_store.put(
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-14-7)  namespace, "doc_0", {"doc": "FooBar company just raised 1 Billion dollars!"}
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-14-8))
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-14-9)namespace = ("documents", "2") # user ID
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-14-10)doc_store.put(namespace, "doc_1", {"doc": "FooBar company was founded in 2019"})

```


### Define the tools[¶](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#define-the-tools_1 "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-15-1)fromlanggraph.store.baseimport BaseStore
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-15-2)fromlangchain_core.runnablesimport RunnableConfig
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-15-3)fromlanggraph.prebuiltimport InjectedStore
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-15-4)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-15-5)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-15-6)@tool
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-15-7)defget_context(
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-15-8)  question: str,
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-15-9)  config: RunnableConfig,
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-15-10)  store: Annotated[BaseStore, InjectedStore()],
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-15-11)) -> Tuple[str, List[Document]]:
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-15-12)"""Get relevant context for answering the question."""
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-15-13)  user_id = config.get("configurable", {}).get("user_id")
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-15-14)  docs = [item.value["doc"] for item in store.search(("documents", user_id))]
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-15-15)  return "\n\n".join(doc for doc in docs)

```


API Reference: [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html)

We can also verify that the tool-calling model will ignore `store` arg of `get_context` tool:

```
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-16-1)get_context.tool_call_schema.schema()

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-17-1){'description': 'Get relevant context for answering the question.',
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-17-2) 'properties': {'question': {'title': 'Question', 'type': 'string'}},
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-17-3) 'required': ['question'],
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-17-4) 'title': 'get_context',
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-17-5) 'type': 'object'}

```


### Define the graph[¶](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#define-the-graph_1 "Permanent link")

Let's update our ReAct agent:

```
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-18-1)tools = [get_context]
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-18-2)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-18-3)# ToolNode will automatically take care of injecting Store into tools
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-18-4)tool_node = ToolNode(tools)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-18-5)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-18-6)checkpointer = MemorySaver()
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-18-7)# NOTE: we need to pass our store to `create_react_agent` to make sure our graph is aware of it
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-18-8)graph = create_react_agent(model, tools, checkpointer=checkpointer, store=doc_store)

```


### Use it![¶](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#use-it_1 "Permanent link")

Let's try running our graph with a `"user_id"` in the config.

```
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-19-1)messages = [{"type": "user", "content": "what's the latest news about FooBar"}]
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-19-2)config = {"configurable": {"thread_id": "1", "user_id": "1"}}
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-19-3)for chunk in graph.stream({"messages": messages}, config, stream_mode="values"):
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-19-4)  chunk["messages"][-1].pretty_print()

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-20-1)================================[1m Human Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-20-2)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-20-3)what's the latest news about FooBar
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-20-4)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-20-5)Tool Calls:
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-20-6) get_context (call_ocyHBpGgF3LPFOgRKURBfkGG)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-20-7) Call ID: call_ocyHBpGgF3LPFOgRKURBfkGG
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-20-8) Args:
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-20-9)  question: latest news about FooBar
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-20-10)=================================[1m Tool Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-20-11)Name: get_context
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-20-12)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-20-13)FooBar company just raised 1 Billion dollars!
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-20-14)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-20-15)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-20-16)The latest news about FooBar is that the company has just raised 1 billion dollars.

```


We can see that the tool only retrieved the correct document for user "1" when looking up the information in the store. Let's now try it again for a different user: 

```
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-21-1)messages = [{"type": "user", "content": "what's the latest news about FooBar"}]
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-21-2)config = {"configurable": {"thread_id": "2", "user_id": "2"}}
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-21-3)for chunk in graph.stream({"messages": messages}, config, stream_mode="values"):
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-21-4)  chunk["messages"][-1].pretty_print()

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-22-1)================================[1m Human Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-22-2)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-22-3)what's the latest news about FooBar
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-22-4)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-22-5)Tool Calls:
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-22-6) get_context (call_zxO9KVlL8UxFQUMb8ETeHNvs)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-22-7) Call ID: call_zxO9KVlL8UxFQUMb8ETeHNvs
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-22-8) Args:
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-22-9)  question: latest news about FooBar
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-22-10)=================================[1m Tool Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-22-11)Name: get_context
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-22-12)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-22-13)FooBar company was founded in 2019
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-22-14)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-22-15)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__codelineno-22-16)FooBar company was founded in 2019. If you need more specific or recent news, please let me know!

```


We can see that the tool pulled in a different document this time.  Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to handle tool calling errors  ](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/) [ Next  How to update graph state from tools  ](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
