---
url: https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#how-to-view-and-update-state-in-subgraphs)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to view and update state in subgraphs 

[ ](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/?q= "Share")

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
          * Subgraphs  Subgraphs 
            * [ Subgraphs  ](https://langchain-ai.github.io/langgraph/how-tos#subgraphs)
            * [ How to use subgraphs  ](https://langchain-ai.github.io/langgraph/how-tos/subgraph/)
            * How to view and update state in subgraphs  [ How to view and update state in subgraphs  ](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#setup)
              * [ Define subgraph  ](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#define-subgraph)
              * [ Define parent graph  ](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#define-parent-graph)
              * [ Resuming from breakpoints  ](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#resuming-from-breakpoints)
                * [ Resuming from specific subgraph node  ](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#resuming-from-specific-subgraph-node)
              * [ Modifying state  ](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#modifying-state)
                * [ Update the state of a subgraph  ](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#update-the-state-of-a-subgraph)
                * [ Acting as a subgraph node  ](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#acting-as-a-subgraph-node)
                * [ Acting as the entire subgraph  ](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#acting-as-the-entire-subgraph)
              * [ Double nested subgraphs  ](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#double-nested-subgraphs)
            * [ How to transform inputs and outputs of a subgraph  ](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#setup)
  * [ Define subgraph  ](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#define-subgraph)
  * [ Define parent graph  ](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#define-parent-graph)
  * [ Resuming from breakpoints  ](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#resuming-from-breakpoints)
    * [ Resuming from specific subgraph node  ](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#resuming-from-specific-subgraph-node)
  * [ Modifying state  ](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#modifying-state)
    * [ Update the state of a subgraph  ](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#update-the-state-of-a-subgraph)
    * [ Acting as a subgraph node  ](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#acting-as-a-subgraph-node)
    * [ Acting as the entire subgraph  ](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#acting-as-the-entire-subgraph)
  * [ Double nested subgraphs  ](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#double-nested-subgraphs)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Subgraphs  ](https://langchain-ai.github.io/langgraph/how-tos#subgraphs)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/subgraphs-manage-state.ipynb "Edit this page")

# How to view and update state in subgraphs[¶](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#how-to-view-and-update-state-in-subgraphs "Permanent link")

Prerequisites

This guide assumes familiarity with the following: 

  * [ Subgraphs ](https://langchain-ai.github.io/langgraph/concepts/low_level/#subgraphs)
  * [ Human-in-the-loop ](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/)
  * [ State ](https://langchain-ai.github.io/langgraph/concepts/low_level/#state)



Once you add [persistence](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence), you can easily view and update the state of the subgraph at any point in time. This enables a lot of the human-in-the-loop interaction patterns:

  * You can surface a state during an interrupt to a user to let them accept an action.
  * You can rewind the subgraph to reproduce or avoid issues.
  * You can modify the state to let the user better control its actions.



This guide shows how you can do this.

## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#setup "Permanent link")

First, let's install the required packages

```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-0-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-0-2)%pip install -U langgraph

```


Next, we need to set API keys for OpenAI (the LLM we will use):

```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-1-1)importgetpass
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-1-2)importos
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-1-5)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-1-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-1-7)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-1-8)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-1-10)_set_env("OPENAI_API_KEY")

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Define subgraph[¶](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#define-subgraph "Permanent link")

First, let's set up our subgraph. For this, we will create a simple graph that can get the weather for a specific city. We will compile this graph with a [breakpoint](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/) before the `weather_node`:

```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-2-1)fromlanggraph.graphimport StateGraph, END, START, MessagesState
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-2-2)fromlangchain_core.toolsimport tool
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-2-3)fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-2-4)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-2-5)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-2-6)@tool
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-2-7)defget_weather(city: str):
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-2-8)"""Get the weather for a specific city"""
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-2-9)  return f"It's sunny in {city}!"
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-2-10)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-2-11)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-2-12)raw_model = ChatOpenAI(model="gpt-4o")
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-2-13)model = raw_model.with_structured_output(get_weather)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-2-14)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-2-15)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-2-16)classSubGraphState(MessagesState):
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-2-17)  city: str
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-2-18)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-2-19)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-2-20)defmodel_node(state: SubGraphState):
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-2-21)  result = model.invoke(state["messages"])
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-2-22)  return {"city": result["city"]}
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-2-23)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-2-24)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-2-25)defweather_node(state: SubGraphState):
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-2-26)  result = get_weather.invoke({"city": state["city"]})
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-2-27)  return {"messages": [{"role": "assistant", "content": result}]}
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-2-28)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-2-29)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-2-30)subgraph = StateGraph(SubGraphState)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-2-31)subgraph.add_node(model_node)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-2-32)subgraph.add_node(weather_node)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-2-33)subgraph.add_edge(START, "model_node")
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-2-34)subgraph.add_edge("model_node", "weather_node")
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-2-35)subgraph.add_edge("weather_node", END)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-2-36)subgraph = subgraph.compile(interrupt_before=["weather_node"])

```


API Reference: [tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html) | [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START)

## Define parent graph[¶](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#define-parent-graph "Permanent link")

We can now setup the overall graph. This graph will first route to the subgraph if it needs to get the weather, otherwise it will route to a normal LLM.

```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-3-1)fromtypingimport Literal
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-3-2)fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-3-3)fromlanggraph.checkpoint.memoryimport MemorySaver
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-3-4)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-3-5)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-3-6)memory = MemorySaver()
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-3-7)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-3-8)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-3-9)classRouterState(MessagesState):
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-3-10)  route: Literal["weather", "other"]
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-3-11)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-3-12)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-3-13)classRouter(TypedDict):
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-3-14)  route: Literal["weather", "other"]
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-3-15)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-3-16)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-3-17)router_model = raw_model.with_structured_output(Router)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-3-18)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-3-19)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-3-20)defrouter_node(state: RouterState):
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-3-21)  system_message = "Classify the incoming query as either about weather or not."
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-3-22)  messages = [{"role": "system", "content": system_message}] + state["messages"]
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-3-23)  route = router_model.invoke(messages)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-3-24)  return {"route": route["route"]}
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-3-25)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-3-26)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-3-27)defnormal_llm_node(state: RouterState):
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-3-28)  response = raw_model.invoke(state["messages"])
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-3-29)  return {"messages": [response]}
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-3-30)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-3-31)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-3-32)defroute_after_prediction(
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-3-33)  state: RouterState,
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-3-34)) -> Literal["weather_graph", "normal_llm_node"]:
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-3-35)  if state["route"] == "weather":
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-3-36)    return "weather_graph"
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-3-37)  else:
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-3-38)    return "normal_llm_node"
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-3-39)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-3-40)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-3-41)graph = StateGraph(RouterState)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-3-42)graph.add_node(router_node)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-3-43)graph.add_node(normal_llm_node)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-3-44)graph.add_node("weather_graph", subgraph)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-3-45)graph.add_edge(START, "router_node")
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-3-46)graph.add_conditional_edges("router_node", route_after_prediction)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-3-47)graph.add_edge("normal_llm_node", END)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-3-48)graph.add_edge("weather_graph", END)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-3-49)graph = graph.compile(checkpointer=memory)

```


API Reference: [MemorySaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.MemorySaver)

```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-4-1)fromIPython.displayimport Image, display
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-4-2)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-4-3)# Setting xray to 1 will show the internal structure of the nested graph
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-4-4)display(Image(graph.get_graph(xray=1).draw_mermaid_png()))

```


![]()

Let's test this out with a normal query to make sure it works as intended!

```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-5-1)config = {"configurable": {"thread_id": "1"}}
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-5-2)inputs = {"messages": [{"role": "user", "content": "hi!"}]}
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-5-3)for update in graph.stream(inputs, config=config, stream_mode="updates"):
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-5-4)  print(update)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-6-1){'router_node': {'route': 'other'}}
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-6-2){'normal_llm_node': {'messages': [AIMessage(content='Hello! How can I assist you today?', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 9, 'prompt_tokens': 9, 'total_tokens': 18, 'completion_tokens_details': {'reasoning_tokens': 0}}, 'model_name': 'gpt-3.5-turbo-0125', 'system_fingerprint': None, 'finish_reason': 'stop', 'logprobs': None}, id='run-35de4577-2117-40e4-ab3b-cd2ac6e27b4c-0', usage_metadata={'input_tokens': 9, 'output_tokens': 9, 'total_tokens': 18})]}}

```


Great! We didn't ask about the weather, so we got a normal response from the LLM. 

## Resuming from breakpoints[¶](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#resuming-from-breakpoints "Permanent link")

Let's now look at what happens with breakpoints. Let's invoke it with a query that should get routed to the weather subgraph where we have the interrupt node.

```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-7-1)config = {"configurable": {"thread_id": "2"}}
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-7-2)inputs = {"messages": [{"role": "user", "content": "what's the weather in sf"}]}
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-7-3)for update in graph.stream(inputs, config=config, stream_mode="updates"):
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-7-4)  print(update)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-8-1){'router_node': {'route': 'weather'}}

```


Note that the graph stream doesn't include subgraph events. If we want to stream subgraph events, we can pass `subgraphs=True` and get back subgraph events like so: 

```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-9-1)config = {"configurable": {"thread_id": "3"}}
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-9-2)inputs = {"messages": [{"role": "user", "content": "what's the weather in sf"}]}
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-9-3)for update in graph.stream(inputs, config=config, stream_mode="values", subgraphs=True):
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-9-4)  print(update)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-10-1)((), {'messages': [HumanMessage(content="what's the weather in sf", additional_kwargs={}, response_metadata={}, id='108eb27a-2cbf-48d2-a6e7-6e07e82eafbc')]})
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-10-2)((), {'messages': [HumanMessage(content="what's the weather in sf", additional_kwargs={}, response_metadata={}, id='108eb27a-2cbf-48d2-a6e7-6e07e82eafbc')], 'route': 'weather'})
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-10-3)(('weather_graph:0c47aeb3-6f4d-5e68-ccf4-42bd48e8ef20',), {'messages': [HumanMessage(content="what's the weather in sf", additional_kwargs={}, response_metadata={}, id='108eb27a-2cbf-48d2-a6e7-6e07e82eafbc')]})
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-10-4)(('weather_graph:0c47aeb3-6f4d-5e68-ccf4-42bd48e8ef20',), {'messages': [HumanMessage(content="what's the weather in sf", additional_kwargs={}, response_metadata={}, id='108eb27a-2cbf-48d2-a6e7-6e07e82eafbc')], 'city': 'San Francisco'})

```


If we get the state now, we can see that it's paused on `weather_graph`

```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-11-1)state = graph.get_state(config)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-11-2)state.next

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-12-1)('weather_graph',)

```


If we look at the pending tasks for our current state, we can see that we have one task named `weather_graph`, which corresponds to the subgraph task.

```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-13-1)state.tasks

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-14-1)(PregelTask(id='0c47aeb3-6f4d-5e68-ccf4-42bd48e8ef20', name='weather_graph', path=('__pregel_pull', 'weather_graph'), error=None, interrupts=(), state={'configurable': {'thread_id': '3', 'checkpoint_ns': 'weather_graph:0c47aeb3-6f4d-5e68-ccf4-42bd48e8ef20'}}),)

```


However since we got the state using the config of the parent graph, we don't have access to the subgraph state. If you look at the `state` value of the `PregelTask` above you will note that it is simply the configuration of the parent graph. If we want to actually populate the subgraph state, we can pass in `subgraphs=True` to `get_state` like so:

```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-15-1)state = graph.get_state(config, subgraphs=True)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-15-2)state.tasks[0]

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-16-1)PregelTask(id='0c47aeb3-6f4d-5e68-ccf4-42bd48e8ef20', name='weather_graph', path=('__pregel_pull', 'weather_graph'), error=None, interrupts=(), state=StateSnapshot(values={'messages': [HumanMessage(content="what's the weather in sf", additional_kwargs={}, response_metadata={}, id='108eb27a-2cbf-48d2-a6e7-6e07e82eafbc')], 'city': 'San Francisco'}, next=('weather_node',), config={'configurable': {'thread_id': '3', 'checkpoint_ns': 'weather_graph:0c47aeb3-6f4d-5e68-ccf4-42bd48e8ef20', 'checkpoint_id': '1ef75ee0-d9c3-6242-8001-440e7a3fb19f', 'checkpoint_map': {'': '1ef75ee0-d4e8-6ede-8001-2542067239ef', 'weather_graph:0c47aeb3-6f4d-5e68-ccf4-42bd48e8ef20': '1ef75ee0-d9c3-6242-8001-440e7a3fb19f'}}}, metadata={'source': 'loop', 'writes': {'model_node': {'city': 'San Francisco'}}, 'step': 1, 'parents': {'': '1ef75ee0-d4e8-6ede-8001-2542067239ef'}}, created_at='2024-09-18T18:44:36.278105+00:00', parent_config={'configurable': {'thread_id': '3', 'checkpoint_ns': 'weather_graph:0c47aeb3-6f4d-5e68-ccf4-42bd48e8ef20', 'checkpoint_id': '1ef75ee0-d4ef-6dec-8000-5d5724f3ef73'}}, tasks=(PregelTask(id='26f4384a-41d7-5ca9-cb94-4001de62e8aa', name='weather_node', path=('__pregel_pull', 'weather_node'), error=None, interrupts=(), state=None),)))

```


Now we have access to the subgraph state! If you look at the `state` value of the `PregelTask` you can see that it has all the information we need, like the next node (`weather_node`) and the current state values (e.g. `city`).

To resume execution, we can just invoke the outer graph as normal:

```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-17-1)for update in graph.stream(None, config=config, stream_mode="values", subgraphs=True):
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-17-2)  print(update)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-18-1)((), {'messages': [HumanMessage(content="what's the weather in sf", additional_kwargs={}, response_metadata={}, id='108eb27a-2cbf-48d2-a6e7-6e07e82eafbc')], 'route': 'weather'})
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-18-2)(('weather_graph:0c47aeb3-6f4d-5e68-ccf4-42bd48e8ef20',), {'messages': [HumanMessage(content="what's the weather in sf", additional_kwargs={}, response_metadata={}, id='108eb27a-2cbf-48d2-a6e7-6e07e82eafbc')], 'city': 'San Francisco'})
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-18-3)(('weather_graph:0c47aeb3-6f4d-5e68-ccf4-42bd48e8ef20',), {'messages': [HumanMessage(content="what's the weather in sf", additional_kwargs={}, response_metadata={}, id='108eb27a-2cbf-48d2-a6e7-6e07e82eafbc'), AIMessage(content="It's sunny in San Francisco!", additional_kwargs={}, response_metadata={}, id='c996ce37-438c-44f4-9e60-5aed8bcdae8a')], 'city': 'San Francisco'})
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-18-4)((), {'messages': [HumanMessage(content="what's the weather in sf", additional_kwargs={}, response_metadata={}, id='108eb27a-2cbf-48d2-a6e7-6e07e82eafbc'), AIMessage(content="It's sunny in San Francisco!", additional_kwargs={}, response_metadata={}, id='c996ce37-438c-44f4-9e60-5aed8bcdae8a')], 'route': 'weather'})

```


### Resuming from specific subgraph node[¶](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#resuming-from-specific-subgraph-node "Permanent link")

In the example above, we were replaying from the outer graph - which automatically replayed the subgraph from whatever state it was in previously (paused before the `weather_node` in our case), but it is also possible to replay from inside a subgraph. In order to do so, we need to get the configuration from the exact subgraph state that we want to replay from.

We can do this by exploring the state history of the subgraph, and selecting the state before `model_node` - which we can do by filtering on the `.next` parameter.

To get the state history of the subgraph, we need to first pass in 

```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-19-1)parent_graph_state_before_subgraph = next(
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-19-2)  h for h in graph.get_state_history(config) if h.next == ("weather_graph",)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-19-3))

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-20-1)subgraph_state_before_model_node = next(
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-20-2)  h
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-20-3)  for h in graph.get_state_history(parent_graph_state_before_subgraph.tasks[0].state)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-20-4)  if h.next == ("model_node",)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-20-5))
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-20-6)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-20-7)# This pattern can be extended no matter how many levels deep
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-20-8)# subsubgraph_stat_history = next(h for h in graph.get_state_history(subgraph_state_before_model_node.tasks[0].state) if h.next == ('my_subsubgraph_node',))

```


We can confirm that we have gotten the correct state by comparing the `.next` parameter of the `subgraph_state_before_model_node`.

```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-21-1)subgraph_state_before_model_node.next

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-22-1)('model_node',)

```


Perfect! We have gotten the correct state snaphshot, and we can now resume from the `model_node` inside of our subgraph:

```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-23-1)for value in graph.stream(
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-23-2)  None,
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-23-3)  config=subgraph_state_before_model_node.config,
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-23-4)  stream_mode="values",
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-23-5)  subgraphs=True,
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-23-6)):
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-23-7)  print(value)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-24-1)((), {'messages': [HumanMessage(content="what's the weather in sf", additional_kwargs={}, response_metadata={}, id='108eb27a-2cbf-48d2-a6e7-6e07e82eafbc')], 'route': 'weather'})
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-24-2)(('weather_graph:0c47aeb3-6f4d-5e68-ccf4-42bd48e8ef20',), {'messages': [HumanMessage(content="what's the weather in sf", additional_kwargs={}, response_metadata={}, id='108eb27a-2cbf-48d2-a6e7-6e07e82eafbc')]})
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-24-3)(('weather_graph:0c47aeb3-6f4d-5e68-ccf4-42bd48e8ef20',), {'messages': [HumanMessage(content="what's the weather in sf", additional_kwargs={}, response_metadata={}, id='108eb27a-2cbf-48d2-a6e7-6e07e82eafbc')], 'city': 'San Francisco'})

```


Great, this subsection has shown how you can replay from any node, no matter how deeply nested it is inside your graph - a powerful tool for testing how deterministic your agent is. 

## Modifying state[¶](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#modifying-state "Permanent link")

### Update the state of a subgraph[¶](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#update-the-state-of-a-subgraph "Permanent link")

What if we want to modify the state of a subgraph? We can do this similarly to how we [update the state of normal graphs](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/), just being careful to pass in the config of the subgraph to `update_state`.

```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-25-1)config = {"configurable": {"thread_id": "4"}}
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-25-2)inputs = {"messages": [{"role": "user", "content": "what's the weather in sf"}]}
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-25-3)for update in graph.stream(inputs, config=config, stream_mode="updates"):
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-25-4)  print(update)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-26-1){'router_node': {'route': 'weather'}}

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-27-1)state = graph.get_state(config, subgraphs=True)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-27-2)state.values["messages"]

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-28-1)[HumanMessage(content="what's the weather in sf", additional_kwargs={}, response_metadata={}, id='05ee2159-3b25-4d6c-97d6-82beda3cabd4')]

```


In order to update the state of the **inner** graph, we need to pass the config for the **inner** graph, which we can get by accessing calling `state.tasks[0].state.config` - since we interrupted inside the subgraph, the state of the task is just the state of the subgraph.

```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-29-1)graph.update_state(state.tasks[0].state.config, {"city": "la"})

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-30-1){'configurable': {'thread_id': '4',
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-30-2) 'checkpoint_ns': 'weather_graph:67f32ef7-aee0-8a20-0eb0-eeea0fd6de6e',
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-30-3) 'checkpoint_id': '1ef75e5a-0b00-6bc0-8002-5726e210fef4',
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-30-4) 'checkpoint_map': {'': '1ef75e59-1b13-6ffe-8001-0844ae748fd5',
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-30-5)  'weather_graph:67f32ef7-aee0-8a20-0eb0-eeea0fd6de6e': '1ef75e5a-0b00-6bc0-8002-5726e210fef4'}}}

```


We can now resume streaming the outer graph (which will resume the subgraph!) and check that we updated our search to use LA instead of SF.

```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-31-1)for update in graph.stream(None, config=config, stream_mode="updates", subgraphs=True):
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-31-2)  print(update)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-32-1)(('weather_graph:9e512e8e-bac5-5412-babe-fe5c12a47cc2',), {'weather_node': {'messages': [{'role': 'assistant', 'content': "It's sunny in la!"}]}})
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-32-2)((), {'weather_graph': {'messages': [HumanMessage(content="what's the weather in sf", id='35e331c6-eb47-483c-a63c-585877b12f5d'), AIMessage(content="It's sunny in la!", id='c3d6b224-9642-4b21-94d5-eef8dc3f2cc9')]}})

```


Fantastic! The AI responded with "It's sunny in LA!" as we expected. 

### Acting as a subgraph node[¶](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#acting-as-a-subgraph-node "Permanent link")

Another way we could update the state is by acting as the `weather_node` ourselves instead of editing the state before `weather_node` is ran as we did above. We can do this by passing the subgraph config and also the `as_node` argument, which allows us to update the state as if we are the node we specify. Thus by setting an interrupt before the `weather_node` and then using the update state function as the `weather_node`, the graph itself never calls `weather_node` directly but instead we decide what the output of `weather_node` should be.

```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-33-1)config = {"configurable": {"thread_id": "14"}}
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-33-2)inputs = {"messages": [{"role": "user", "content": "what's the weather in sf"}]}
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-33-3)for update in graph.stream(
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-33-4)  inputs, config=config, stream_mode="updates", subgraphs=True
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-33-5)):
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-33-6)  print(update)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-33-7)# Graph execution should stop before the weather node
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-33-8)print("interrupted!")
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-33-9)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-33-10)state = graph.get_state(config, subgraphs=True)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-33-11)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-33-12)# We update the state by passing in the message we want returned from the weather node, and make sure to use as_node
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-33-13)graph.update_state(
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-33-14)  state.tasks[0].state.config,
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-33-15)  {"messages": [{"role": "assistant", "content": "rainy"}]},
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-33-16)  as_node="weather_node",
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-33-17))
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-33-18)for update in graph.stream(None, config=config, stream_mode="updates", subgraphs=True):
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-33-19)  print(update)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-33-20)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-33-21)print(graph.get_state(config).values["messages"])

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-34-1)((), {'router_node': {'route': 'weather'}})
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-34-2)(('weather_graph:c7eb1fc7-efab-b0e3-12ed-8586f37bc7a2',), {'model_node': {'city': 'San Francisco'}})
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-34-3)interrupted!
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-34-4)((), {'weather_graph': {'messages': [HumanMessage(content="what's the weather in sf", additional_kwargs={}, response_metadata={}, id='ad694c4e-8aac-4e1f-b5ca-790c60c1775b'), AIMessage(content='rainy', additional_kwargs={}, response_metadata={}, id='98a73aaf-3524-482a-9d07-971407df0389')]}})
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-34-5)[HumanMessage(content="what's the weather in sf", additional_kwargs={}, response_metadata={}, id='ad694c4e-8aac-4e1f-b5ca-790c60c1775b'), AIMessage(content='rainy', additional_kwargs={}, response_metadata={}, id='98a73aaf-3524-482a-9d07-971407df0389')]

```


Perfect! The AI responded with the message we passed in ourselves. 

### Acting as the entire subgraph[¶](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#acting-as-the-entire-subgraph "Permanent link")

Lastly, we could also update the graph just acting as the **entire** subgraph. This is similar to the case above but instead of acting as just the `weather_node` we are acting as the entire subgraph. This is done by passing in the normal graph config as well as the `as_node` argument, where we specify the we are acting as the entire subgraph node.

```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-35-1)config = {"configurable": {"thread_id": "8"}}
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-35-2)inputs = {"messages": [{"role": "user", "content": "what's the weather in sf"}]}
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-35-3)for update in graph.stream(
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-35-4)  inputs, config=config, stream_mode="updates", subgraphs=True
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-35-5)):
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-35-6)  print(update)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-35-7)# Graph execution should stop before the weather node
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-35-8)print("interrupted!")
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-35-9)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-35-10)# We update the state by passing in the message we want returned from the weather graph, making sure to use as_node
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-35-11)# Note that we don't need to pass in the subgraph config, since we aren't updating the state inside the subgraph
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-35-12)graph.update_state(
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-35-13)  config,
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-35-14)  {"messages": [{"role": "assistant", "content": "rainy"}]},
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-35-15)  as_node="weather_graph",
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-35-16))
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-35-17)for update in graph.stream(None, config=config, stream_mode="updates"):
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-35-18)  print(update)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-35-19)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-35-20)print(graph.get_state(config).values["messages"])

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-36-1)((), {'router_node': {'route': 'weather'}})
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-36-2)(('weather_graph:53ab3fb1-23e8-5de0-acc6-9fb904fd4dc4',), {'model_node': {'city': 'San Francisco'}})
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-36-3)interrupted!
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-36-4)[HumanMessage(content="what's the weather in sf", id='64b1b683-778b-4623-b783-4a8f81322ec8'), AIMessage(content='rainy', id='c1d1a2f3-c117-41e9-8c1f-8fb0a02a3b70')]

```


Again, the AI responded with "rainy" as we expected. 

## Double nested subgraphs[¶](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#double-nested-subgraphs "Permanent link")

This same functionality continues to work no matter the level of nesting. Here is an example of doing the same things with a double nested subgraph (although any level of nesting will work). We add another router on top of our already defined graphs.

```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-37-1)fromtypingimport Literal
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-37-2)fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-37-3)fromlanggraph.checkpoint.memoryimport MemorySaver
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-37-4)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-37-5)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-37-6)memory = MemorySaver()
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-37-7)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-37-8)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-37-9)classRouterState(MessagesState):
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-37-10)  route: Literal["weather", "other"]
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-37-11)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-37-12)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-37-13)classRouter(TypedDict):
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-37-14)  route: Literal["weather", "other"]
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-37-15)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-37-16)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-37-17)router_model = raw_model.with_structured_output(Router)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-37-18)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-37-19)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-37-20)defrouter_node(state: RouterState):
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-37-21)  system_message = "Classify the incoming query as either about weather or not."
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-37-22)  messages = [{"role": "system", "content": system_message}] + state["messages"]
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-37-23)  route = router_model.invoke(messages)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-37-24)  return {"route": route["route"]}
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-37-25)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-37-26)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-37-27)defnormal_llm_node(state: RouterState):
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-37-28)  response = raw_model.invoke(state["messages"])
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-37-29)  return {"messages": [response]}
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-37-30)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-37-31)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-37-32)defroute_after_prediction(
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-37-33)  state: RouterState,
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-37-34)) -> Literal["weather_graph", "normal_llm_node"]:
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-37-35)  if state["route"] == "weather":
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-37-36)    return "weather_graph"
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-37-37)  else:
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-37-38)    return "normal_llm_node"
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-37-39)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-37-40)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-37-41)graph = StateGraph(RouterState)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-37-42)graph.add_node(router_node)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-37-43)graph.add_node(normal_llm_node)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-37-44)graph.add_node("weather_graph", subgraph)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-37-45)graph.add_edge(START, "router_node")
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-37-46)graph.add_conditional_edges("router_node", route_after_prediction)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-37-47)graph.add_edge("normal_llm_node", END)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-37-48)graph.add_edge("weather_graph", END)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-37-49)graph = graph.compile()

```


API Reference: [MemorySaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.MemorySaver)

```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-38-1)fromlanggraph.checkpoint.memoryimport MemorySaver
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-38-2)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-38-3)memory = MemorySaver()
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-38-4)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-38-5)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-38-6)classGrandfatherState(MessagesState):
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-38-7)  to_continue: bool
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-38-8)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-38-9)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-38-10)defrouter_node(state: GrandfatherState):
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-38-11)  # Dummy logic that will always continue
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-38-12)  return {"to_continue": True}
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-38-13)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-38-14)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-38-15)defroute_after_prediction(state: GrandfatherState):
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-38-16)  if state["to_continue"]:
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-38-17)    return "graph"
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-38-18)  else:
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-38-19)    return END
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-38-20)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-38-21)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-38-22)grandparent_graph = StateGraph(GrandfatherState)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-38-23)grandparent_graph.add_node(router_node)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-38-24)grandparent_graph.add_node("graph", graph)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-38-25)grandparent_graph.add_edge(START, "router_node")
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-38-26)grandparent_graph.add_conditional_edges(
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-38-27)  "router_node", route_after_prediction, ["graph", END]
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-38-28))
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-38-29)grandparent_graph.add_edge("graph", END)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-38-30)grandparent_graph = grandparent_graph.compile(checkpointer=MemorySaver())

```


API Reference: [MemorySaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.MemorySaver)

```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-39-1)fromIPython.displayimport Image, display
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-39-2)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-39-3)# Setting xray to 1 will show the internal structure of the nested graph
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-39-4)display(Image(grandparent_graph.get_graph(xray=2).draw_mermaid_png()))

```


![]()

If we run until the interrupt, we can now see that there are snapshots of the state of all three graphs

```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-40-1)config = {"configurable": {"thread_id": "2"}}
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-40-2)inputs = {"messages": [{"role": "user", "content": "what's the weather in sf"}]}
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-40-3)for update in grandparent_graph.stream(
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-40-4)  inputs, config=config, stream_mode="updates", subgraphs=True
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-40-5)):
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-40-6)  print(update)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-41-1)((), {'router_node': {'to_continue': True}})
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-41-2)(('graph:e18ecd45-5dfb-53b0-bcb7-db793924e9a8',), {'router_node': {'route': 'weather'}})
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-41-3)(('graph:e18ecd45-5dfb-53b0-bcb7-db793924e9a8', 'weather_graph:12bd3069-de24-5bc6-b4f1-f39527605781'), {'model_node': {'city': 'San Francisco'}})

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-42-1)state = grandparent_graph.get_state(config, subgraphs=True)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-42-2)print("Grandparent State:")
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-42-3)print(state.values)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-42-4)print("---------------")
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-42-5)print("Parent Graph State:")
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-42-6)print(state.tasks[0].state.values)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-42-7)print("---------------")
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-42-8)print("Subgraph State:")
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-42-9)print(state.tasks[0].state.tasks[0].state.values)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-43-1)Grandparent State:
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-43-2){'messages': [HumanMessage(content="what's the weather in sf", id='3bb28060-3d30-49a7-9f84-c90b6ada7848')], 'to_continue': True}
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-43-3)---------------
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-43-4)Parent Graph State:
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-43-5){'messages': [HumanMessage(content="what's the weather in sf", id='3bb28060-3d30-49a7-9f84-c90b6ada7848')], 'route': 'weather'}
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-43-6)---------------
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-43-7)Subgraph State:
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-43-8){'messages': [HumanMessage(content="what's the weather in sf", id='3bb28060-3d30-49a7-9f84-c90b6ada7848')], 'city': 'San Francisco'}

```


We can now continue, acting as the node three levels down 

```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-44-1)grandparent_graph_state = state
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-44-2)parent_graph_state = grandparent_graph_state.tasks[0].state
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-44-3)subgraph_state = parent_graph_state.tasks[0].state
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-44-4)grandparent_graph.update_state(
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-44-5)  subgraph_state.config,
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-44-6)  {"messages": [{"role": "assistant", "content": "rainy"}]},
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-44-7)  as_node="weather_node",
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-44-8))
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-44-9)for update in grandparent_graph.stream(
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-44-10)  None, config=config, stream_mode="updates", subgraphs=True
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-44-11)):
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-44-12)  print(update)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-44-13)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-44-14)print(grandparent_graph.get_state(config).values["messages"])

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-45-1)(('graph:e18ecd45-5dfb-53b0-bcb7-db793924e9a8',), {'weather_graph': {'messages': [HumanMessage(content="what's the weather in sf", id='3bb28060-3d30-49a7-9f84-c90b6ada7848'), AIMessage(content='rainy', id='be926b59-c647-4355-88fd-a429b9e2b420')]}})
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-45-2)((), {'graph': {'messages': [HumanMessage(content="what's the weather in sf", id='3bb28060-3d30-49a7-9f84-c90b6ada7848'), AIMessage(content='rainy', id='be926b59-c647-4355-88fd-a429b9e2b420')]}})
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-45-3)[HumanMessage(content="what's the weather in sf", id='3bb28060-3d30-49a7-9f84-c90b6ada7848'), AIMessage(content='rainy', id='be926b59-c647-4355-88fd-a429b9e2b420')]

```


As in the cases above, we can see that the AI responds with "rainy" as we expect. 

We can explore the state history to see how the state of the grandparent graph was updated at each step.

```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-46-1)for state in grandparent_graph.get_state_history(config):
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-46-2)  print(state)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-46-3)  print("-----")

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-47-1)StateSnapshot(values={'messages': [HumanMessage(content="what's the weather in sf", id='5ff89e4d-8255-4d23-8b55-01633c112720'), AIMessage(content='rainy', id='7c80f847-248d-4b8f-8238-633ed757b353')], 'to_continue': True}, next=(), config={'configurable': {'thread_id': '2', 'checkpoint_ns': '', 'checkpoint_id': '1ef66f40-7a2c-6f9e-8002-a37a61b26709'}}, metadata={'source': 'loop', 'writes': {'graph': {'messages': [HumanMessage(content="what's the weather in sf", id='5ff89e4d-8255-4d23-8b55-01633c112720'), AIMessage(content='rainy', id='7c80f847-248d-4b8f-8238-633ed757b353')]}}, 'step': 2, 'parents': {}}, created_at='2024-08-30T17:19:35.793847+00:00', parent_config={'configurable': {'thread_id': '2', 'checkpoint_ns': '', 'checkpoint_id': '1ef66f3f-f312-6338-8001-766acddc781e'}}, tasks=())
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-47-2)-----
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-47-3)StateSnapshot(values={'messages': [HumanMessage(content="what's the weather in sf", id='5ff89e4d-8255-4d23-8b55-01633c112720')], 'to_continue': True}, next=('graph',), config={'configurable': {'thread_id': '2', 'checkpoint_ns': '', 'checkpoint_id': '1ef66f3f-f312-6338-8001-766acddc781e'}}, metadata={'source': 'loop', 'writes': {'router_node': {'to_continue': True}}, 'step': 1, 'parents': {}}, created_at='2024-08-30T17:19:21.627097+00:00', parent_config={'configurable': {'thread_id': '2', 'checkpoint_ns': '', 'checkpoint_id': '1ef66f3f-f303-61d0-8000-1945c8a74e9e'}}, tasks=(PregelTask(id='b59fe96f-fdce-5afe-aa58-bd2876a0d592', name='graph', error=None, interrupts=(), state={'configurable': {'thread_id': '2', 'checkpoint_ns': 'graph:b59fe96f-fdce-5afe-aa58-bd2876a0d592'}}),))
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-47-4)-----
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-47-5)StateSnapshot(values={'messages': [HumanMessage(content="what's the weather in sf", id='5ff89e4d-8255-4d23-8b55-01633c112720')]}, next=('router_node',), config={'configurable': {'thread_id': '2', 'checkpoint_ns': '', 'checkpoint_id': '1ef66f3f-f303-61d0-8000-1945c8a74e9e'}}, metadata={'source': 'loop', 'writes': None, 'step': 0, 'parents': {}}, created_at='2024-08-30T17:19:21.620923+00:00', parent_config={'configurable': {'thread_id': '2', 'checkpoint_ns': '', 'checkpoint_id': '1ef66f3f-f2f9-6d6a-bfff-c8b76e5b2462'}}, tasks=(PregelTask(id='e3d4a97a-f4ca-5260-801e-e65b02907825', name='router_node', error=None, interrupts=(), state=None),))
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-47-6)-----
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-47-7)StateSnapshot(values={'messages': []}, next=('__start__',), config={'configurable': {'thread_id': '2', 'checkpoint_ns': '', 'checkpoint_id': '1ef66f3f-f2f9-6d6a-bfff-c8b76e5b2462'}}, metadata={'source': 'input', 'writes': {'messages': [{'role': 'user', 'content': "what's the weather in sf"}]}, 'step': -1, 'parents': {}}, created_at='2024-08-30T17:19:21.617127+00:00', parent_config=None, tasks=(PregelTask(id='f0538638-b794-58fc-a406-980d2fea28a1', name='__start__', error=None, interrupts=(), state=None),))
[](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__codelineno-47-8)-----

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to use subgraphs  ](https://langchain-ai.github.io/langgraph/how-tos/subgraph/) [ Next  How to transform inputs and outputs of a subgraph  ](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
