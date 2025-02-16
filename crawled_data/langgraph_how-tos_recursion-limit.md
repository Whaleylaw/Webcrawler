---
url: https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#how-to-create-and-control-loops)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to create and control loops 

[ ](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/?q= "Share")

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
          * Graph API Basics  Graph API Basics 
            * [ Graph API Basics  ](https://langchain-ai.github.io/langgraph/how-tos#graph-api-basics)
            * [ How to update graph state from nodes  ](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/)
            * [ How to create a sequence of steps  ](https://langchain-ai.github.io/langgraph/how-tos/sequence/)
            * [ How to create branches for parallel node execution  ](https://langchain-ai.github.io/langgraph/how-tos/branching/)
            * How to create and control loops  [ How to create and control loops  ](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/) Table of contents 
              * [ Summary  ](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#summary)
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#setup)
              * [ Define the graph  ](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#define-the-graph)
              * [ Impose a recursion limit  ](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#impose-a-recursion-limit)
              * [ Loops with branches  ](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#loops-with-branches)
            * [ How to visualize your graph  ](https://langchain-ai.github.io/langgraph/how-tos/visualization/)
          * [ Controllability  ](https://langchain-ai.github.io/langgraph/how-tos#controllability)
          * [ Persistence  ](https://langchain-ai.github.io/langgraph/how-tos#persistence)
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

  * [ Summary  ](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#summary)
  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#setup)
  * [ Define the graph  ](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#define-the-graph)
  * [ Impose a recursion limit  ](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#impose-a-recursion-limit)
  * [ Loops with branches  ](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#loops-with-branches)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Graph API Basics  ](https://langchain-ai.github.io/langgraph/how-tos#graph-api-basics)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/recursion-limit.ipynb "Edit this page")

# How to create and control loops[¶](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#how-to-create-and-control-loops "Permanent link")

Prerequisites

This guide assumes familiarity with the following: 

  * [ Graphs ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#graphs)
  * [ Recursion Limit ](https://langchain-ai.github.io/langgraph/concepts/low_level/#recursion-limit)
  * [ Nodes ](https://langchain-ai.github.io/langgraph/concepts/low_level/#nodes)



When creating a graph with a loop, we require a mechanism for terminating execution. This is most commonly done by adding a [conditional edge](https://langchain-ai.github.io/langgraph/concepts/low_level/#conditional-edges) that routes to the [END](https://langchain-ai.github.io/langgraph/concepts/low_level/#end-node) node once we reach some termination condition.

You can also set the graph recursion limit when invoking or streaming the graph. The recursion limit sets the number of [supersteps](https://langchain-ai.github.io/langgraph/concepts/low_level/#graphs) that the graph is allowed to execute before it raises an error. Read more about the concept of recursion limits [here](https://langchain-ai.github.io/langgraph/concepts/low_level/#recursion-limit). 

Let's consider a simple graph with a loop to better understand how these mechanisms work.

Tip

To return the last value of your state instead of receiving a recursion limit error, read [this how-to](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/).

## Summary[¶](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#summary "Permanent link")

When creating a loop, you can include a conditional edge that specifies a termination condition: 

```
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-0-1)builder = StateGraph(State)
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-0-2)builder.add_node(a)
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-0-3)builder.add_node(b)
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-0-4)
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-0-5)defroute(state: State) -> Literal["b", END]:
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-0-6)  if termination_condition(state):
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-0-7)    return END
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-0-8)  else:
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-0-9)    return "a"
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-0-10)
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-0-11)builder.add_edge(START, "a")
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-0-12)builder.add_conditional_edges("a", route)
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-0-13)builder.add_edge("b", "a")
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-0-14)graph = builder.compile()

```


To control the recursion limit, specify `"recursion_limit"` in the config. This will raise a `GraphRecursionError`, which you can catch and handle: 

```
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-1-1)fromlanggraph.errorsimport GraphRecursionError
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-1-2)
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-1-3)try:
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-1-4)  graph.invoke(inputs, {"recursion_limit": 3})
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-1-5)except GraphRecursionError:
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-1-6)  print("Recursion Error")

```


## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#setup "Permanent link")

First, let's install the required packages

```
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-2-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-2-2)%pip install -U langgraph

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Define the graph[¶](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#define-the-graph "Permanent link")

Let's define a graph with a simple loop. Note that we use a conditional edge to implement a termination condition.

```
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-3-1)importoperator
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-3-2)fromtypingimport Annotated, Literal
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-3-3)
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-3-4)fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-3-5)
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-3-6)fromlanggraph.graphimport StateGraph, START, END
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-3-7)
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-3-8)
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-3-9)classState(TypedDict):
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-3-10)  # The operator.add reducer fn makes this append-only
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-3-11)  aggregate: Annotated[list, operator.add]
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-3-12)
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-3-13)
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-3-14)defa(state: State):
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-3-15)  print(f'Node A sees {state["aggregate"]}')
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-3-16)  return {"aggregate": ["A"]}
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-3-17)
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-3-18)
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-3-19)defb(state: State):
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-3-20)  print(f'Node B sees {state["aggregate"]}')
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-3-21)  return {"aggregate": ["B"]}
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-3-22)
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-3-23)
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-3-24)# Define nodes
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-3-25)builder = StateGraph(State)
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-3-26)builder.add_node(a)
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-3-27)builder.add_node(b)
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-3-28)
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-3-29)
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-3-30)# Define edges
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-3-31)defroute(state: State) -> Literal["b", END]:
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-3-32)  if len(state["aggregate"]) < 7:
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-3-33)    return "b"
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-3-34)  else:
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-3-35)    return END
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-3-36)
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-3-37)
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-3-38)builder.add_edge(START, "a")
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-3-39)builder.add_conditional_edges("a", route)
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-3-40)builder.add_edge("b", "a")
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-3-41)graph = builder.compile()

```


API Reference: [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END)

```
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-4-1)fromIPython.displayimport Image, display
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-4-2)
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-4-3)display(Image(graph.get_graph().draw_mermaid_png()))

```


![]()

This architecture is similar to a [ReAct agent](https://langchain-ai.github.io/langgraph/how-tos/#prebuilt-react-agent) in which node `"a"` is a tool-calling model, and node `"b"` represents the tools.

In our `route` conditional edge, we specify that we should end after the `"aggregate"` list in the state passes a threshold length.

Invoking the graph, we see that we alternate between nodes `"a"` and `"b"` before terminating once we reach the termination condition.

```
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-5-1)graph.invoke({"aggregate": []})

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-6-1)Node A sees []
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-6-2)Node B sees ['A']
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-6-3)Node A sees ['A', 'B']
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-6-4)Node B sees ['A', 'B', 'A']
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-6-5)Node A sees ['A', 'B', 'A', 'B']
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-6-6)Node B sees ['A', 'B', 'A', 'B', 'A']
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-6-7)Node A sees ['A', 'B', 'A', 'B', 'A', 'B']

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-7-1){'aggregate': ['A', 'B', 'A', 'B', 'A', 'B', 'A']}

```


## Impose a recursion limit[¶](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#impose-a-recursion-limit "Permanent link")

In some applications, we may not have a guarantee that we will reach a given termination condition. In these cases, we can set the graph's [recursion limit](https://langchain-ai.github.io/langgraph/concepts/low_level/#recursion-limit). This will raise a `GraphRecursionError` after a given number of [supersteps](https://langchain-ai.github.io/langgraph/concepts/low_level/#graphs). We can then catch and handle this exception:

```
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-8-1)fromlanggraph.errorsimport GraphRecursionError
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-8-2)
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-8-3)try:
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-8-4)  graph.invoke({"aggregate": []}, {"recursion_limit": 4})
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-8-5)except GraphRecursionError:
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-8-6)  print("Recursion Error")

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-9-1)Node A sees []
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-9-2)Node B sees ['A']
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-9-3)Node A sees ['A', 'B']
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-9-4)Node B sees ['A', 'B', 'A']
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-9-5)Recursion Error

```


Note that this time we terminate after the fourth step. 

## Loops with branches[¶](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#loops-with-branches "Permanent link")

To better understand how the recursion limit works, let's consider a more complex example. Below we implement a loop, but one step fans out into two nodes:

```
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-10-1)importoperator
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-10-2)fromtypingimport Annotated, Literal
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-10-3)
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-10-4)fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-10-5)
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-10-6)fromlanggraph.graphimport StateGraph, START, END
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-10-7)
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-10-8)
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-10-9)classState(TypedDict):
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-10-10)  aggregate: Annotated[list, operator.add]
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-10-11)
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-10-12)
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-10-13)defa(state: State):
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-10-14)  print(f'Node A sees {state["aggregate"]}')
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-10-15)  return {"aggregate": ["A"]}
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-10-16)
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-10-17)
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-10-18)defb(state: State):
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-10-19)  print(f'Node B sees {state["aggregate"]}')
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-10-20)  return {"aggregate": ["B"]}
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-10-21)
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-10-22)
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-10-23)defc(state: State):
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-10-24)  print(f'Node C sees {state["aggregate"]}')
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-10-25)  return {"aggregate": ["C"]}
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-10-26)
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-10-27)
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-10-28)defd(state: State):
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-10-29)  print(f'Node D sees {state["aggregate"]}')
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-10-30)  return {"aggregate": ["D"]}
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-10-31)
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-10-32)
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-10-33)# Define nodes
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-10-34)builder = StateGraph(State)
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-10-35)builder.add_node(a)
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-10-36)builder.add_node(b)
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-10-37)builder.add_node(c)
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-10-38)builder.add_node(d)
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-10-39)
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-10-40)
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-10-41)# Define edges
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-10-42)defroute(state: State) -> Literal["b", END]:
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-10-43)  if len(state["aggregate"]) < 7:
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-10-44)    return "b"
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-10-45)  else:
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-10-46)    return END
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-10-47)
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-10-48)
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-10-49)builder.add_edge(START, "a")
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-10-50)builder.add_conditional_edges("a", route)
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-10-51)builder.add_edge("b", "c")
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-10-52)builder.add_edge("b", "d")
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-10-53)builder.add_edge(["c", "d"], "a")
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-10-54)graph = builder.compile()

```


API Reference: [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END)

```
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-11-1)fromIPython.displayimport Image, display
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-11-2)
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-11-3)display(Image(graph.get_graph().draw_mermaid_png()))

```


![]()

This graph looks complex, but can be conceptualized as loop of [supersteps](https://langchain-ai.github.io/langgraph/concepts/low_level/#graphs):

  1. Node A
  2. Node B
  3. Nodes C and D
  4. Node A
  5. ...



We have a loop of four supersteps, where nodes C and D are executed concurrently.

Invoking the graph as before, we see that we complete two full "laps" before hitting the termination condition:

```
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-12-1)result = graph.invoke({"aggregate": []})

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-13-1)Node A sees []
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-13-2)Node B sees ['A']
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-13-3)Node D sees ['A', 'B']
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-13-4)Node C sees ['A', 'B']
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-13-5)Node A sees ['A', 'B', 'C', 'D']
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-13-6)Node B sees ['A', 'B', 'C', 'D', 'A']
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-13-7)Node D sees ['A', 'B', 'C', 'D', 'A', 'B']
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-13-8)Node C sees ['A', 'B', 'C', 'D', 'A', 'B']
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-13-9)Node A sees ['A', 'B', 'C', 'D', 'A', 'B', 'C', 'D']

```


However, if we set the recursion limit to four, we only complete one lap because each lap is four supersteps: 

```
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-14-1)fromlanggraph.errorsimport GraphRecursionError
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-14-2)
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-14-3)try:
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-14-4)  result = graph.invoke({"aggregate": []}, {"recursion_limit": 4})
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-14-5)except GraphRecursionError:
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-14-6)  print("Recursion Error")

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-15-1)Node A sees []
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-15-2)Node B sees ['A']
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-15-3)Node C sees ['A', 'B']
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-15-4)Node D sees ['A', 'B']
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-15-5)Node A sees ['A', 'B', 'C', 'D']
[](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__codelineno-15-6)Recursion Error

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to create branches for parallel node execution  ](https://langchain-ai.github.io/langgraph/how-tos/branching/) [ Next  How to visualize your graph  ](https://langchain-ai.github.io/langgraph/how-tos/visualization/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
