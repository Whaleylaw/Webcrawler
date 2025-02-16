---
url: https://langchain-ai.github.io/langgraph/how-tos/sequence/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/sequence/#how-to-create-a-sequence-of-steps)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to create a sequence of steps 

[ ](https://langchain-ai.github.io/langgraph/how-tos/sequence/?q= "Share")

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
            * [ How to create branches for parallel node execution  ](https://langchain-ai.github.io/langgraph/how-tos/branching/)
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



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Graph API Basics  ](https://langchain-ai.github.io/langgraph/how-tos#graph-api-basics)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/sequence.md "Edit this page")

# How to create a sequence of steps[¶](https://langchain-ai.github.io/langgraph/how-tos/sequence/#how-to-create-a-sequence-of-steps "Permanent link")

Prerequisites

This guide assumes familiarity with the following:

  * [How to define and update graph state](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/)



This guide demonstrates how to construct a simple sequence of steps. We will demonstrate:

  1. How to build a sequential graph
  2. Built-in short-hand for constructing similar graphs.



# Summary[¶](https://langchain-ai.github.io/langgraph/how-tos/sequence/#summary "Permanent link")

To add a sequence of nodes, we use the `.add_node` and `.add_edge` methods of our [graph](https://langchain-ai.github.io/langgraph/concepts/low_level/#stategraph):

```
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-0-1)fromlanggraph.graphimport START, StateGraph
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-0-2)
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-0-3)graph_builder = StateGraph(State)
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-0-4)
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-0-5)# Add nodes
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-0-6)graph_builder.add_node(step_1)
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-0-7)graph_builder.add_node(step_2)
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-0-8)graph_builder.add_node(step_3)
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-0-9)
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-0-10)# Add edges
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-0-11)graph_builder.add_edge(START, "step_1")
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-0-12)graph_builder.add_edge("step_1", "step_2")
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-0-13)graph_builder.add_edge("step_2", "step_3")

```


API Reference: [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph)

We can also use the built-in shorthand `.add_sequence`:

```
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-1-1)graph_builder = StateGraph(State).add_sequence([step_1, step_2, step_3])
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-1-2)graph_builder.add_edge(START, "step_1")

```


Why split application steps into a sequence with LangGraph? LangGraph makes it easy to add an underlying persistence layer to your application. This allows state to be checkpointed in between the execution of nodes, so your LangGraph nodes govern: 

  * How state updates are [checkpointed](../concepts/persistence/.md)
  * How interruptions are resumed in [human-in-the-loop](../concepts/human_in_the_loop/.md) workflows
  * How we can "rewind" and branch-off executions using LangGraph's [time travel](../concepts/time-travel/.md) features

They also determine how execution steps are [streamed](../concepts/streaming.md), and how your application is visualized and debugged using [LangGraph Studio](../concepts/langgraph_studio.md). 

## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/sequence/#setup "Permanent link")

First, let's install langgraph:

```
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-2-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-2-2)%pip install -U langgraph

```


Set up [LangSmith](https://smith.langchain.com) for better debugging

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM aps built with LangGraph — read more about how to get started in the [docs](https://docs.smith.langchain.com). 

## Build the graph[¶](https://langchain-ai.github.io/langgraph/how-tos/sequence/#build-the-graph "Permanent link")

Let's demonstrate a simple usage example. We will create a sequence of three steps:

  1. Populate a value in a key of the state
  2. Update the same value
  3. Populate a different value



### Define state[¶](https://langchain-ai.github.io/langgraph/how-tos/sequence/#define-state "Permanent link")

Let's first define our [state](https://langchain-ai.github.io/langgraph/concepts/low_level/#state). This governs the [schema of the graph](https://langchain-ai.github.io/langgraph/concepts/low_level/#schema), and can also specify how to apply updates. See [this guide](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/) for more detail.

In our case, we will just keep track of two values:

```
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-0-1)fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-0-2)
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-0-3)
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-0-4)classState(TypedDict):
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-0-5)  value_1: str
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-0-6)  value_2: int

```


### Define nodes[¶](https://langchain-ai.github.io/langgraph/how-tos/sequence/#define-nodes "Permanent link")

Our [nodes](https://langchain-ai.github.io/langgraph/concepts/low_level/#nodes) are just Python functions that read our graph's state and make updates to it. The first argument to this function will always be the state:

```
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-0-1)defstep_1(state: State):
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-0-2)  return {"value_1": "a"}
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-0-3)
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-0-4)
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-0-5)defstep_2(state: State):
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-0-6)  current_value_1 = state["value_1"]
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-0-7)  return {"value_1": f"{current_value_1} b"}
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-0-8)
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-0-9)
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-0-10)defstep_3(state: State):
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-0-11)  return {"value_2": 10}

```


Note

Note that when issuing updates to the state, each node can just specify the value of the key it wishes to update.

By default, this will **overwrite** the value of the corresponding key. You can also use [reducers](https://langchain-ai.github.io/langgraph/concepts/low_level/#reducers) to control how updates are processed— for example, you can append successive updates to a key instead. See [this guide](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/) for more detail.

### Define graph[¶](https://langchain-ai.github.io/langgraph/how-tos/sequence/#define-graph "Permanent link")

We use [StateGraph](https://langchain-ai.github.io/langgraph/concepts/low_level/#stategraph) to define a graph that operates on this state.

We will then use [add_node](https://langchain-ai.github.io/langgraph/concepts/low_level/#messagesstate) and [add_edge](https://langchain-ai.github.io/langgraph/concepts/low_level/#edges) to populate our graph and define its control flow.

```
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-0-1)fromlanggraph.graphimport START, StateGraph
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-0-2)
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-0-3)graph_builder = StateGraph(State)
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-0-4)
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-0-5)# Add nodes
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-0-6)graph_builder.add_node(step_1)
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-0-7)graph_builder.add_node(step_2)
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-0-8)graph_builder.add_node(step_3)
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-0-9)
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-0-10)# Add edges
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-0-11)graph_builder.add_edge(START, "step_1")
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-0-12)graph_builder.add_edge("step_1", "step_2")
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-0-13)graph_builder.add_edge("step_2", "step_3")

```


Specifying custom names

You can specify custom names for nodes using `.add_node`:

```
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-3-1)graph_builder.add_node("my_node", step_1)

```


Note that:

  * `.add_edge` takes the names of nodes, which for functions defaults to `node.__name__`.
  * We must specify the entry point of the graph. For this we add an edge with the [START node](https://langchain-ai.github.io/langgraph/concepts/low_level/#start-node).
  * The graph halts when there are no more nodes to execute.



We next [compile](https://langchain-ai.github.io/langgraph/concepts/low_level/#compiling-your-graph) our graph. This provides a few basic checks on the structure of the graph (e.g., identifying orphaned nodes). If we were adding persistence to our application via a [checkpointer](https://langchain-ai.github.io/langgraph/concepts/persistence/), it would also be passed in here.

```
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-0-1)graph = graph_builder.compile()

```


LangGraph provides built-in utilities for visualizing your graph. Let's inspect our sequence. See [this guide](https://langchain-ai.github.io/langgraph/how-tos/visualization/) for detail on visualization.

```
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-0-1)fromIPython.displayimport Image, display
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-0-2)
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-0-3)display(Image(graph.get_graph().draw_mermaid_png()))

```


![]()

### Usage[¶](https://langchain-ai.github.io/langgraph/how-tos/sequence/#usage "Permanent link")

Let's proceed with a simple invocation:

```
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-0-1)graph.invoke({"value_1": "c"})

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-1-1){'value_1': 'a b', 'value_2': 10}

```


Note that:

  * We kicked off invocation by providing a value for a single state key. We must always provide a value for at least one key.
  * The value we passed in was overwritten by the first node.
  * The second node updated the value.
  * The third node populated a different value.



## Built-in shorthand[¶](https://langchain-ai.github.io/langgraph/how-tos/sequence/#built-in-shorthand "Permanent link")

Prerequisites

`.add_sequence` requires `langgraph>=0.2.46`

LangGraph includes a built-in shorthand `.add_sequence` for convenience:

```
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-0-1)graph_builder = StateGraph(State).add_sequence([step_1, step_2, step_3])
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-0-2)graph_builder.add_edge(START, "step_1")
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-0-3)
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-0-4)graph = graph_builder.compile()
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-0-5)
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-0-6)graph.invoke({"value_1": "c"})

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__codelineno-1-1){'value_1': 'a b', 'value_2': 10}

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to update graph state from nodes  ](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/) [ Next  How to create branches for parallel node execution  ](https://langchain-ai.github.io/langgraph/how-tos/branching/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/sequence/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
