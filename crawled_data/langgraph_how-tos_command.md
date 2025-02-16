---
url: https://langchain-ai.github.io/langgraph/how-tos/command/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/command/#how-to-combine-control-flow-and-state-updates-with-command)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to combine control flow and state updates with Command 

[ ](https://langchain-ai.github.io/langgraph/how-tos/command/?q= "Share")

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
          * Controllability  Controllability 
            * [ Controllability  ](https://langchain-ai.github.io/langgraph/how-tos#controllability)
            * [ How to create map-reduce branches for parallel execution  ](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/)
            * How to combine control flow and state updates with Command  [ How to combine control flow and state updates with Command  ](https://langchain-ai.github.io/langgraph/how-tos/command/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/command/#setup)
              * [ Basic usage  ](https://langchain-ai.github.io/langgraph/how-tos/command/#basic-usage)
              * [ Navigating to a node in a parent graph  ](https://langchain-ai.github.io/langgraph/how-tos/command/#navigating-to-a-node-in-a-parent-graph)
            * [ How to add runtime configuration to your graph  ](https://langchain-ai.github.io/langgraph/how-tos/configuration/)
            * [ How to add node retry policies  ](https://langchain-ai.github.io/langgraph/how-tos/node-retries/)
            * [ How to return state before hitting recursion limit  ](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/command/#setup)
  * [ Basic usage  ](https://langchain-ai.github.io/langgraph/how-tos/command/#basic-usage)
  * [ Navigating to a node in a parent graph  ](https://langchain-ai.github.io/langgraph/how-tos/command/#navigating-to-a-node-in-a-parent-graph)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Controllability  ](https://langchain-ai.github.io/langgraph/how-tos#controllability)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/command.ipynb "Edit this page")

# How to combine control flow and state updates with Command[¶](https://langchain-ai.github.io/langgraph/how-tos/command/#how-to-combine-control-flow-and-state-updates-with-command "Permanent link")

Prerequisites

This guide assumes familiarity with the following:

  * [State](https://langchain-ai.github.io/langgraph/concepts/low_level#state)
  * [Nodes](https://langchain-ai.github.io/langgraph/concepts/low_level#nodes)
  * [Edges](https://langchain-ai.github.io/langgraph/concepts/low_level#edges)
  * [Command](https://langchain-ai.github.io/langgraph/concepts/low_level#command)



It can be useful to combine control flow (edges) and state updates (nodes). For example, you might want to BOTH perform state updates AND decide which node to go to next in the SAME node. LangGraph provides a way to do so by returning a `Command` object from node functions:

```
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-0-1)defmy_node(state: State) -> Command[Literal["my_other_node"]]:
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-0-2)  return Command(
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-0-3)    # state update
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-0-4)    update={"foo": "bar"},
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-0-5)    # control flow
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-0-6)    goto="my_other_node"
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-0-7)  )

```


If you are using [subgraphs](https://langchain-ai.github.io/langgraph/how-tos/command/#subgraphs), you might want to navigate from a node a subgraph to a different subgraph (i.e. a different node in the parent graph). To do so, you can specify `graph=Command.PARENT` in `Command`:

```
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-1-1)defmy_node(state: State) -> Command[Literal["my_other_node"]]:
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-1-2)  return Command(
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-1-3)    update={"foo": "bar"},
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-1-4)    goto="other_subgraph", # where `other_subgraph` is a node in the parent graph
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-1-5)    graph=Command.PARENT
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-1-6)  )

```


State updates with `Command.PARENT`

When you send updates from a subgraph node to a parent graph node for a key that's shared by both parent and subgraph [state schemas](https://langchain-ai.github.io/langgraph/concepts/low_level#schema), you **must** define a [reducer](https://langchain-ai.github.io/langgraph/concepts/low_level#reducers) for the key you're updating in the parent graph state. See this [example](https://langchain-ai.github.io/langgraph/how-tos/command/#navigating-to-a-node-in-a-parent-graph) below.

This guide shows how you can do use `Command` to add dynamic control flow in your LangGraph app.

## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/command/#setup "Permanent link")

First, let's install the required packages

```
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-2-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-2-2)%pip install -U langgraph

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

Let's create a simple graph with 3 nodes: A, B and C. We will first execute node A, and then decide whether to go to Node B or Node C next based on the output of node A.

## Basic usage[¶](https://langchain-ai.github.io/langgraph/how-tos/command/#basic-usage "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-3-1)importrandom
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-3-2)fromtyping_extensionsimport TypedDict, Literal
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-3-3)
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-3-4)fromlanggraph.graphimport StateGraph, START
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-3-5)fromlanggraph.typesimport Command
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-3-6)
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-3-7)
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-3-8)# Define graph state
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-3-9)classState(TypedDict):
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-3-10)  foo: str
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-3-11)
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-3-12)
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-3-13)# Define the nodes
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-3-14)
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-3-15)
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-3-16)defnode_a(state: State) -> Command[Literal["node_b", "node_c"]]:
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-3-17)  print("Called A")
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-3-18)  value = random.choice(["a", "b"])
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-3-19)  # this is a replacement for a conditional edge function
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-3-20)  if value == "a":
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-3-21)    goto = "node_b"
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-3-22)  else:
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-3-23)    goto = "node_c"
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-3-24)
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-3-25)  # note how Command allows you to BOTH update the graph state AND route to the next node
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-3-26)  return Command(
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-3-27)    # this is the state update
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-3-28)    update={"foo": value},
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-3-29)    # this is a replacement for an edge
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-3-30)    goto=goto,
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-3-31)  )
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-3-32)
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-3-33)
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-3-34)defnode_b(state: State):
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-3-35)  print("Called B")
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-3-36)  return {"foo": state["foo"] + "b"}
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-3-37)
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-3-38)
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-3-39)defnode_c(state: State):
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-3-40)  print("Called C")
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-3-41)  return {"foo": state["foo"] + "c"}

```


API Reference: [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [Command](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Command)

We can now create the `StateGraph` with the above nodes. Notice that the graph doesn't have [conditional edges](https://langchain-ai.github.io/langgraph/concepts/low_level#conditional-edges) for routing! This is because control flow is defined with `Command` inside `node_a`.

```
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-4-1)builder = StateGraph(State)
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-4-2)builder.add_edge(START, "node_a")
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-4-3)builder.add_node(node_a)
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-4-4)builder.add_node(node_b)
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-4-5)builder.add_node(node_c)
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-4-6)# NOTE: there are no edges between nodes A, B and C!
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-4-7)
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-4-8)graph = builder.compile()

```


Important

You might have noticed that we used `Command` as a return type annotation, e.g. `Command[Literal["node_b", "node_c"]]`. This is necessary for the graph rendering and tells LangGraph that `node_a` can navigate to `node_b` and `node_c`.

```
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-5-1)fromIPython.displayimport display, Image
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-5-2)
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-5-3)display(Image(graph.get_graph().draw_mermaid_png()))

```


![]()

If we run the graph multiple times, we'd see it take different paths (A -> B or A -> C) based on the random choice in node A.

```
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-6-1)graph.invoke({"foo": ""})

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-7-1)Called A
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-7-2)Called C

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-8-1){'foo': 'bc'}

```


## Navigating to a node in a parent graph[¶](https://langchain-ai.github.io/langgraph/how-tos/command/#navigating-to-a-node-in-a-parent-graph "Permanent link")

Now let's demonstrate how you can navigate from inside a subgraph to a different node in a parent graph. We'll do so by changing `node_a` in the above example into a single-node graph that we'll add as a subgraph to our parent graph.

State updates with `Command.PARENT`

When you send updates from a subgraph node to a parent graph node for a key that's shared by both parent and subgraph [state schemas](https://langchain-ai.github.io/langgraph/concepts/low_level#schema), you **must** define a [reducer](https://langchain-ai.github.io/langgraph/concepts/low_level#reducers) for the key you're updating in the parent graph state.

```
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-9-1)importoperator
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-9-2)fromtyping_extensionsimport Annotated
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-9-3)
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-9-4)
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-9-5)classState(TypedDict):
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-9-6)  # NOTE: we define a reducer here
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-9-7)  foo: Annotated[str, operator.add]
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-9-8)
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-9-9)
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-9-10)defnode_a(state: State):
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-9-11)  print("Called A")
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-9-12)  value = random.choice(["a", "b"])
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-9-13)  # this is a replacement for a conditional edge function
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-9-14)  if value == "a":
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-9-15)    goto = "node_b"
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-9-16)  else:
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-9-17)    goto = "node_c"
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-9-18)
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-9-19)  # note how Command allows you to BOTH update the graph state AND route to the next node
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-9-20)  return Command(
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-9-21)    update={"foo": value},
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-9-22)    goto=goto,
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-9-23)    # this tells LangGraph to navigate to node_b or node_c in the parent graph
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-9-24)    # NOTE: this will navigate to the closest parent graph relative to the subgraph
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-9-25)    graph=Command.PARENT,
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-9-26)  )
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-9-27)
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-9-28)
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-9-29)subgraph = StateGraph(State).add_node(node_a).add_edge(START, "node_a").compile()
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-9-30)
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-9-31)
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-9-32)defnode_b(state: State):
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-9-33)  print("Called B")
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-9-34)  # NOTE: since we've defined a reducer, we don't need to manually append
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-9-35)  # new characters to existing 'foo' value. instead, reducer will append these
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-9-36)  # automatically (via operator.add)
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-9-37)  return {"foo": "b"}
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-9-38)
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-9-39)
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-9-40)defnode_c(state: State):
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-9-41)  print("Called C")
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-9-42)  return {"foo": "c"}

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-10-1)builder = StateGraph(State)
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-10-2)builder.add_edge(START, "subgraph")
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-10-3)builder.add_node("subgraph", subgraph)
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-10-4)builder.add_node(node_b)
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-10-5)builder.add_node(node_c)
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-10-6)
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-10-7)graph = builder.compile()

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-11-1)graph.invoke({"foo": ""})

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-12-1)Called A
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-12-2)Called C

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/command/#__codelineno-13-1){'foo': 'bc'}

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to create map-reduce branches for parallel execution  ](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/) [ Next  How to add runtime configuration to your graph  ](https://langchain-ai.github.io/langgraph/how-tos/configuration/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/command/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
