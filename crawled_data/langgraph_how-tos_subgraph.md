---
url: https://langchain-ai.github.io/langgraph/how-tos/subgraph
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#how-to-use-subgraphs)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to use subgraphs 

[ ](https://langchain-ai.github.io/langgraph/how-tos/subgraph/?q= "Share")

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
            * How to use subgraphs  [ How to use subgraphs  ](https://langchain-ai.github.io/langgraph/how-tos/subgraph/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#setup)
              * [ Add a node with the compiled subgraph  ](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#add-a-node-with-the-compiled-subgraph)
              * [ Add a node function that invokes the subgraph  ](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#add-a-node-function-that-invokes-the-subgraph)
            * [ How to view and update state in subgraphs  ](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#setup)
  * [ Add a node with the compiled subgraph  ](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#add-a-node-with-the-compiled-subgraph)
  * [ Add a node function that invokes the subgraph  ](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#add-a-node-function-that-invokes-the-subgraph)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Subgraphs  ](https://langchain-ai.github.io/langgraph/how-tos#subgraphs)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/subgraph.ipynb "Edit this page")

# How to use subgraphs[¶](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#how-to-use-subgraphs "Permanent link")

Prerequisites

This guide assumes familiarity with the following: 

  * [ Subgraphs ](https://langchain-ai.github.io/langgraph/concepts/low_level/#subgraphs)
  * [ State ](https://langchain-ai.github.io/langgraph/concepts/low_level/#state)



[Subgraphs](https://langchain-ai.github.io/langgraph/concepts/low_level/#subgraphs) allow you to build complex systems with multiple components that are themselves graphs. A common use case for using subgraphs is building [multi-agent systems](https://langchain-ai.github.io/langgraph/concepts/multi_agent).

The main question when adding subgraphs is how the parent graph and subgraph communicate, i.e. how they pass the [state](https://langchain-ai.github.io/langgraph/concepts/low_level/#state) between each other during the graph execution. There are two scenarios:

  * parent graph and subgraph **share schema keys**. In this case, you can [add a node with the compiled subgraph](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#add-a-node-with-the-compiled-subgraph)
  * parent graph and subgraph have **different schemas**. In this case, you have to [add a node function that invokes the subgraph](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#add-a-node-function-that-invokes-the-subgraph): this is useful when the parent graph and the subgraph have different state schemas and you need to transform state before or after calling the subgraph



Below we show to to add subgraphs for each scenario.

![Screenshot 2024-07-11 at 1.01.28 PM.png]()

## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#setup "Permanent link")

First, let's install the required packages

```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-0-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-0-2)%pip install -U langgraph

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Add a node with the compiled subgraph[¶](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#add-a-node-with-the-compiled-subgraph "Permanent link")

A common case is for the parent graph and subgraph to communicate over a shared state key (channel). For example, in [multi-agent](https://langchain-ai.github.io/langgraph/concepts/multi_agent) systems, the agents often communicate over a shared [messages](https://langchain-ai.github.io/langgraph/concepts/low_level/#why-use-messages) key.

If your subgraph shares state keys with the parent graph, you can follow these steps to add it to your graph:

  1. Define the subgraph workflow (`subgraph_builder` in the example below) and compile it
  2. Pass compiled subgraph to the `.add_node` method when defining the parent graph workflow



Let's take a look at a simple example. 

```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-1-1)fromlanggraph.graphimport START, StateGraph
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-1-2)fromtypingimport TypedDict
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-1-5)# Define subgraph
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-1-6)classSubgraphState(TypedDict):
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-1-7)  foo: str # note that this key is shared with the parent graph state
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-1-8)  bar: str
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-1-10)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-1-11)defsubgraph_node_1(state: SubgraphState):
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-1-12)  return {"bar": "bar"}
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-1-13)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-1-14)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-1-15)defsubgraph_node_2(state: SubgraphState):
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-1-16)  # note that this node is using a state key ('bar') that is only available in the subgraph
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-1-17)  # and is sending update on the shared state key ('foo')
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-1-18)  return {"foo": state["foo"] + state["bar"]}
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-1-19)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-1-20)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-1-21)subgraph_builder = StateGraph(SubgraphState)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-1-22)subgraph_builder.add_node(subgraph_node_1)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-1-23)subgraph_builder.add_node(subgraph_node_2)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-1-24)subgraph_builder.add_edge(START, "subgraph_node_1")
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-1-25)subgraph_builder.add_edge("subgraph_node_1", "subgraph_node_2")
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-1-26)subgraph = subgraph_builder.compile()
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-1-27)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-1-28)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-1-29)# Define parent graph
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-1-30)classParentState(TypedDict):
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-1-31)  foo: str
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-1-32)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-1-33)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-1-34)defnode_1(state: ParentState):
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-1-35)  return {"foo": "hi! " + state["foo"]}
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-1-36)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-1-37)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-1-38)builder = StateGraph(ParentState)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-1-39)builder.add_node("node_1", node_1)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-1-40)# note that we're adding the compiled subgraph as a node to the parent graph
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-1-41)builder.add_node("node_2", subgraph)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-1-42)builder.add_edge(START, "node_1")
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-1-43)builder.add_edge("node_1", "node_2")
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-1-44)graph = builder.compile()

```


API Reference: [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph)

```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-2-1)for chunk in graph.stream({"foo": "foo"}):
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-2-2)  print(chunk)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-3-1){'node_1': {'foo': 'hi! foo'}}
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-3-2){'node_2': {'foo': 'hi! foobar'}}

```


You can see that the final output from the parent graph includes the results of subgraph invocation (i.e. string `"bar"`). If you would like to see outputs from the subgraph, you can specify `subgraphs=True` when streaming. See more on streaming from subgraphs in this [how-to guide](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#stream-subgraph). 

```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-4-1)for chunk in graph.stream({"foo": "foo"}, subgraphs=True):
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-4-2)  print(chunk)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-5-1)((), {'node_1': {'foo': 'hi! foo'}})
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-5-2)(('node_2:e58e5673-a661-ebb0-70d4-e298a7fc28b7',), {'subgraph_node_1': {'bar': 'bar'}})
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-5-3)(('node_2:e58e5673-a661-ebb0-70d4-e298a7fc28b7',), {'subgraph_node_2': {'foo': 'hi! foobar'}})
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-5-4)((), {'node_2': {'foo': 'hi! foobar'}})

```


## Add a node function that invokes the subgraph[¶](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#add-a-node-function-that-invokes-the-subgraph "Permanent link")

For more complex systems you might want to define subgraphs that have a completely different schema from the parent graph (no shared keys). For example, in a multi-agent RAG system, a search agent might only need to keep track of queries and retrieved documents.

If that's the case for your application, you need to define a node **function that invokes the subgraph**. This function needs to transform the input (parent) state to the subgraph state before invoking the subgraph, and transform the results back to the parent state before returning the state update from the node.

Below we show how to modify our original example to call a subgraph from inside the node.

Warning

You **cannot** invoke more than one subgraph inside the same node.

```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-6-1)# Define subgraph
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-6-2)classSubgraphState(TypedDict):
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-6-3)  # note that none of these keys are shared with the parent graph state
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-6-4)  bar: str
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-6-5)  baz: str
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-6-6)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-6-7)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-6-8)defsubgraph_node_1(state: SubgraphState):
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-6-9)  return {"baz": "baz"}
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-6-10)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-6-11)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-6-12)defsubgraph_node_2(state: SubgraphState):
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-6-13)  return {"bar": state["bar"] + state["baz"]}
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-6-14)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-6-15)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-6-16)subgraph_builder = StateGraph(SubgraphState)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-6-17)subgraph_builder.add_node(subgraph_node_1)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-6-18)subgraph_builder.add_node(subgraph_node_2)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-6-19)subgraph_builder.add_edge(START, "subgraph_node_1")
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-6-20)subgraph_builder.add_edge("subgraph_node_1", "subgraph_node_2")
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-6-21)subgraph = subgraph_builder.compile()
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-6-22)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-6-23)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-6-24)# Define parent graph
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-6-25)classParentState(TypedDict):
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-6-26)  foo: str
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-6-27)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-6-28)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-6-29)defnode_1(state: ParentState):
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-6-30)  return {"foo": "hi! " + state["foo"]}
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-6-31)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-6-32)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-6-33)defnode_2(state: ParentState):
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-6-34)  # transform the state to the subgraph state
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-6-35)  response = subgraph.invoke({"bar": state["foo"]})
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-6-36)  # transform response back to the parent state
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-6-37)  return {"foo": response["bar"]}
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-6-38)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-6-39)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-6-40)builder = StateGraph(ParentState)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-6-41)builder.add_node("node_1", node_1)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-6-42)# note that instead of using the compiled subgraph we are using `node_2` function that is calling the subgraph
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-6-43)builder.add_node("node_2", node_2)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-6-44)builder.add_edge(START, "node_1")
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-6-45)builder.add_edge("node_1", "node_2")
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-6-46)graph = builder.compile()

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-7-1)for chunk in graph.stream({"foo": "foo"}, subgraphs=True):
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-7-2)  print(chunk)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-8-1)((), {'node_1': {'foo': 'hi! foo'}})
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-8-2)(('node_2:c47d7ea3-7798-87c4-adf4-2543a91d6891',), {'subgraph_node_1': {'baz': 'baz'}})
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-8-3)(('node_2:c47d7ea3-7798-87c4-adf4-2543a91d6891',), {'subgraph_node_2': {'bar': 'hi! foobaz'}})
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__codelineno-8-4)((), {'node_2': {'foo': 'hi! foobaz'}})

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to handle large numbers of tools  ](https://langchain-ai.github.io/langgraph/how-tos/many-tools/) [ Next  How to view and update state in subgraphs  ](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/subgraph/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
