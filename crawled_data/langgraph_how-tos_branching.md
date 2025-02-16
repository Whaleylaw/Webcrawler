---
url: https://langchain-ai.github.io/langgraph/how-tos/branching/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/branching/#how-to-create-branches-for-parallel-node-execution)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to create branches for parallel node execution 

[ ](https://langchain-ai.github.io/langgraph/how-tos/branching/?q= "Share")

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
          * Graph API Basics  Graph API Basics 
            * [ Graph API Basics  ](https://langchain-ai.github.io/langgraph/how-tos#graph-api-basics)
            * [ How to update graph state from nodes  ](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/)
            * [ How to create a sequence of steps  ](https://langchain-ai.github.io/langgraph/how-tos/sequence/)
            * How to create branches for parallel node execution  [ How to create branches for parallel node execution  ](https://langchain-ai.github.io/langgraph/how-tos/branching/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/branching/#setup)
              * [ How to run graph nodes in parallel  ](https://langchain-ai.github.io/langgraph/how-tos/branching/#how-to-run-graph-nodes-in-parallel)
              * [ Parallel node fan-out and fan-in with extra steps  ](https://langchain-ai.github.io/langgraph/how-tos/branching/#parallel-node-fan-out-and-fan-in-with-extra-steps)
              * [ Conditional Branching  ](https://langchain-ai.github.io/langgraph/how-tos/branching/#conditional-branching)
              * [ Next steps  ](https://langchain-ai.github.io/langgraph/how-tos/branching/#next-steps)
            * [ How to create and control loops  ](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/branching/#setup)
  * [ How to run graph nodes in parallel  ](https://langchain-ai.github.io/langgraph/how-tos/branching/#how-to-run-graph-nodes-in-parallel)
  * [ Parallel node fan-out and fan-in with extra steps  ](https://langchain-ai.github.io/langgraph/how-tos/branching/#parallel-node-fan-out-and-fan-in-with-extra-steps)
  * [ Conditional Branching  ](https://langchain-ai.github.io/langgraph/how-tos/branching/#conditional-branching)
  * [ Next steps  ](https://langchain-ai.github.io/langgraph/how-tos/branching/#next-steps)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Graph API Basics  ](https://langchain-ai.github.io/langgraph/how-tos#graph-api-basics)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/branching.md "Edit this page")

# How to create branches for parallel node execution[¶](https://langchain-ai.github.io/langgraph/how-tos/branching/#how-to-create-branches-for-parallel-node-execution "Permanent link")

Prerequisites

This guide assumes familiarity with the following: 

  * [ Node ](https://langchain-ai.github.io/langgraph/concepts/low_level/#nodes)
  * [ Edge ](https://langchain-ai.github.io/langgraph/concepts/low_level/#edges)
  * [ Reducer ](https://langchain-ai.github.io/langgraph/concepts/low_level/#reducers)



Parallel execution of nodes is essential to speed up overall graph operation. LangGraph offers native support for parallel execution of nodes, which can significantly enhance the performance of graph-based workflows. This parallelization is achieved through fan-out and fan-in mechanisms, utilizing both standard edges and [conditional_edges](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.MessageGraph.add_conditional_edges). Below are some examples showing how to add create branching dataflows that work for you. 

![Screenshot 2024-07-09 at 2.55.56 PM.png]()

## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/branching/#setup "Permanent link")

First, let's install the required packages

```
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-1)pipinstall-Ulanggraph

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## How to run graph nodes in parallel[¶](https://langchain-ai.github.io/langgraph/how-tos/branching/#how-to-run-graph-nodes-in-parallel "Permanent link")

In this example, we fan out from `Node A` to `B and C` and then fan in to `D`. With our state, [we specify the reducer add operation](https://langchain-ai.github.io/langgraph/concepts/low_level/#reducers). This will combine or accumulate values for the specific key in the State, rather than simply overwriting the existing value. For lists, this means concatenating the new list with the existing list. See [this guide](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/) for more detail on updating state with reducers.

```
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-1)importoperator
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-2)fromtypingimport Annotated, Any
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-3)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-4)fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-5)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-6)fromlanggraph.graphimport StateGraph, START, END
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-7)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-8)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-9)classState(TypedDict):
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-10)  # The operator.add reducer fn makes this append-only
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-11)  aggregate: Annotated[list, operator.add]
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-12)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-13)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-14)defa(state: State):
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-15)  print(f'Adding "A" to {state["aggregate"]}')
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-16)  return {"aggregate": ["A"]}
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-17)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-18)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-19)defb(state: State):
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-20)  print(f'Adding "B" to {state["aggregate"]}')
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-21)  return {"aggregate": ["B"]}
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-22)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-23)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-24)defc(state: State):
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-25)  print(f'Adding "C" to {state["aggregate"]}')
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-26)  return {"aggregate": ["C"]}
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-27)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-28)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-29)defd(state: State):
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-30)  print(f'Adding "D" to {state["aggregate"]}')
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-31)  return {"aggregate": ["D"]}
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-32)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-33)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-34)builder = StateGraph(State)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-35)builder.add_node(a)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-36)builder.add_node(b)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-37)builder.add_node(c)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-38)builder.add_node(d)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-39)builder.add_edge(START, "a")
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-40)builder.add_edge("a", "b")
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-41)builder.add_edge("a", "c")
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-42)builder.add_edge("b", "d")
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-43)builder.add_edge("c", "d")
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-44)builder.add_edge("d", END)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-45)graph = builder.compile()

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-1)fromIPython.displayimport Image, display
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-2)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-3)display(Image(graph.get_graph().draw_mermaid_png()))

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-1-1)<IPython.core.display.Image object>

```


![]()

With the reducer, you can see that the values added in each node are accumulated.

```
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-1)graph.invoke({"aggregate": []}, {"configurable": {"thread_id": "foo"}})

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-1-1)Adding "A" to []
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-1-2)Adding "B" to ['A']
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-1-3)Adding "C" to ['A']
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-1-4)Adding "D" to ['A', 'B', 'C']
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-1-5)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-1-6){'aggregate': ['A', 'B', 'C', 'D']}

```


Note

In the above example, nodes `"b"` and `"c"` are executed concurrently in the same [superstep](https://langchain-ai.github.io/langgraph/concepts/low_level/#graphs). Because they are in the same step, node `"d"` executes after both `"b"` and `"c"` are finished.

Importantly, updates from a parallel superstep may not be ordered consistently. If you need a consistent, predetermined ordering of updates from a parallel superstep, you should write the outputs to a separate field in the state together with a value with which to order them.

Exception handling?

LangGraph executes nodes within ["supersteps"](https://langchain-ai.github.io/langgraph/concepts/low_level/#graphs), meaning that while parallel branches are executed in parallel, the entire superstep is **transactional**. If any of these branches raises an exception, **none** of the updates are applied to the state (the entire superstep errors).

Importantly, when using a [checkpointer](https://langchain-ai.github.io/langgraph/concepts/persistence/), results from successful nodes within a superstep are saved, and don't repeat when resumed.

If you have error-prone (perhaps want to handle flakey API calls), LangGraph provides two ways to address this: 

  1. You can write regular python code within your node to catch and handle exceptions.
  2. You can set a **[retry_policy](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.graph.CompiledGraph.retry_policy)** to direct the graph to retry nodes that raise certain types of exceptions. Only failing branches are retried, so you needn't worry about performing redundant work.

Together, these let you perform parallel execution and fully control exception handling. 

## Parallel node fan-out and fan-in with extra steps[¶](https://langchain-ai.github.io/langgraph/how-tos/branching/#parallel-node-fan-out-and-fan-in-with-extra-steps "Permanent link")

The above example showed how to fan-out and fan-in when each path was only one step. But what if one path had more than one step? Let's add a node `b_2` in the "b" branch:

```
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-1)defb_2(state: State):
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-2)  print(f'Adding "B_2" to {state["aggregate"]}')
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-3)  return {"aggregate": ["B_2"]}
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-4)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-5)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-6)builder = StateGraph(State)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-7)builder.add_node(a)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-8)builder.add_node(b)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-9)builder.add_node(b_2)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-10)builder.add_node(c)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-11)builder.add_node(d)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-12)builder.add_edge(START, "a")
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-13)builder.add_edge("a", "b")
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-14)builder.add_edge("a", "c")
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-15)builder.add_edge("b", "b_2")
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-16)builder.add_edge(["b_2", "c"], "d")
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-17)builder.add_edge("d", END)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-18)graph = builder.compile()

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-1)fromIPython.displayimport Image, display
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-2)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-3)display(Image(graph.get_graph().draw_mermaid_png()))

```


![]()

```
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-1)graph.invoke({"aggregate": []})

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-1-1)Adding "A" to []
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-1-2)Adding "B" to ['A']
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-1-3)Adding "C" to ['A']
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-1-4)Adding "B_2" to ['A', 'B', 'C']
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-1-5)Adding "D" to ['A', 'B', 'C', 'B_2']
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-1-6)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-1-7){'aggregate': ['A', 'B', 'C', 'B_2', 'D']}

```


Note

In the above example, nodes `"b"` and `"c"` are executed concurrently in the same [superstep](https://langchain-ai.github.io/langgraph/concepts/low_level/#graphs). What happens in the next step?

We use `add_edge(["b_2", "c"], "d")` here to force node `"d"` to only run when both nodes `"b_2"` and `"c"` have finished execution. If we added two separate edges, node `"d"` would run twice: after node `b2` finishes and once again after node `c` (in whichever order those nodes finish).

## Conditional Branching[¶](https://langchain-ai.github.io/langgraph/how-tos/branching/#conditional-branching "Permanent link")

If your fan-out is not deterministic, you can use [add_conditional_edges](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.StateGraph.add_conditional_edges) directly.

```
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-1)importoperator
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-2)fromtypingimport Annotated, Sequence
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-3)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-4)fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-5)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-6)fromlanggraph.graphimport StateGraph, START, END
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-7)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-8)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-9)classState(TypedDict):
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-10)  aggregate: Annotated[list, operator.add]
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-11)  # Add a key to the state. We will set this key to determine
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-12)  # how we branch.
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-13)  which: str
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-14)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-15)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-16)defa(state: State):
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-17)  print(f'Adding "A" to {state["aggregate"]}')
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-18)  return {"aggregate": ["A"]}
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-19)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-20)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-21)defb(state: State):
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-22)  print(f'Adding "B" to {state["aggregate"]}')
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-23)  return {"aggregate": ["B"]}
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-24)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-25)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-26)defc(state: State):
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-27)  print(f'Adding "C" to {state["aggregate"]}')
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-28)  return {"aggregate": ["C"]}
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-29)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-30)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-31)defd(state: State):
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-32)  print(f'Adding "D" to {state["aggregate"]}')
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-33)  return {"aggregate": ["D"]}
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-34)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-35)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-36)defe(state: State):
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-37)  print(f'Adding "E" to {state["aggregate"]}')
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-38)  return {"aggregate": ["E"]}
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-39)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-40)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-41)builder = StateGraph(State)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-42)builder.add_node(a)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-43)builder.add_node(b)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-44)builder.add_node(c)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-45)builder.add_node(d)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-46)builder.add_node(e)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-47)builder.add_edge(START, "a")
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-48)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-49)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-50)defroute_bc_or_cd(state: State) -> Sequence[str]:
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-51)  if state["which"] == "cd":
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-52)    return ["c", "d"]
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-53)  return ["b", "c"]
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-54)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-55)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-56)intermediates = ["b", "c", "d"]
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-57)builder.add_conditional_edges(
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-58)  "a",
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-59)  route_bc_or_cd,
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-60)  intermediates,
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-61))
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-62)for node in intermediates:
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-63)  builder.add_edge(node, "e")
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-64)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-65)builder.add_edge("e", END)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-66)graph = builder.compile()

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-1)fromIPython.displayimport Image, display
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-2)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-3)display(Image(graph.get_graph().draw_mermaid_png()))

```


![]()

```
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-1)graph.invoke({"aggregate": [], "which": "bc"})

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-1-1)Adding "A" to []
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-1-2)Adding "B" to ['A']
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-1-3)Adding "C" to ['A']
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-1-4)Adding "E" to ['A', 'B', 'C']
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-1-5)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-1-6){'aggregate': ['A', 'B', 'C', 'E'], 'which': 'bc'}

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-0-1)graph.invoke({"aggregate": [], "which": "cd"})

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-1-1)Adding "A" to []
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-1-2)Adding "C" to ['A']
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-1-3)Adding "D" to ['A']
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-1-4)Adding "E" to ['A', 'C', 'D']
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-1-5)
[](https://langchain-ai.github.io/langgraph/how-tos/branching/#__codelineno-1-6){'aggregate': ['A', 'C', 'D', 'E'], 'which': 'cd'}

```


## Next steps[¶](https://langchain-ai.github.io/langgraph/how-tos/branching/#next-steps "Permanent link")

  * Continue with the [Graph API Basics](https://langchain-ai.github.io/langgraph/how-tos/#graph-api-basics) guides.
  * Learn how to create [map-reduce](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/) branches in which different states can be distributed to multiple instances of a node.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to create a sequence of steps  ](https://langchain-ai.github.io/langgraph/how-tos/sequence/) [ Next  How to create and control loops  ](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/branching/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
