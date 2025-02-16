---
url: https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#how-to-add-and-use-subgraphs)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to add and use subgraphs 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/?q= "Share")

Type to start searching

[ GitHub  ](https://github.com/langchain-ai/langgraphjs "Go to repository")

  * [ Home ](https://langchain-ai.github.io/langgraphjs/)
  * [ API reference ](https://langchain-ai.github.io/langgraphjs/reference/)
  * [ Versions ](https://langchain-ai.github.io/langgraphjs/versions/)



[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

[ GitHub  ](https://github.com/langchain-ai/langgraphjs "Go to repository")

  * [ Home  ](https://langchain-ai.github.io/langgraphjs/)

Home 
    * Get started  Get started 
      * [ Learn the basics  ](https://langchain-ai.github.io/langgraphjs/tutorials/quickstart/)
      * [ Deployment  ](https://langchain-ai.github.io/langgraphjs/tutorials/deployment/)
    * Guides  Guides 
      * [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)

How-to Guides 
        * [ Installation  ](https://langchain-ai.github.io/langgraphjs/how-tos#installation)
        * LangGraph  LangGraph 
          * [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
          * [ Controllability  ](https://langchain-ai.github.io/langgraphjs/how-tos#controllability)
          * [ Persistence  ](https://langchain-ai.github.io/langgraphjs/how-tos#persistence)
          * [ Memory  ](https://langchain-ai.github.io/langgraphjs/how-tos#memory)
          * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraphjs/how-tos#human-in-the-loop)
          * [ Streaming  ](https://langchain-ai.github.io/langgraphjs/how-tos#streaming)
          * [ Tool calling  ](https://langchain-ai.github.io/langgraphjs/how-tos#tool-calling)
          * Subgraphs  Subgraphs 
            * [ Subgraphs  ](https://langchain-ai.github.io/langgraphjs/how-tos#subgraphs)
            * How to add and use subgraphs  [ How to add and use subgraphs  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#setup)
              * [ Add a node with the compiled subgraph  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#add-a-node-with-the-compiled-subgraph)
              * [ Add a node function that invokes the subgraph  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#add-a-node-function-that-invokes-the-subgraph)
            * [ How to view and update state in subgraphs  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/)
            * [ How to transform inputs and outputs of a subgraph  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/)
          * [ Multi-agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/)
          * [ State Management  ](https://langchain-ai.github.io/langgraphjs/how-tos#state-management)
          * [ Other  ](https://langchain-ai.github.io/langgraphjs/how-tos#other)
          * [ Prebuilt ReAct Agent  ](https://langchain-ai.github.io/langgraphjs/how-tos#prebuilt-react-agent)
        * [ LangGraph Platform  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph-platform)
      * [ Concepts  ](https://langchain-ai.github.io/langgraphjs/concepts/)
      * [ Tutorials  ](https://langchain-ai.github.io/langgraphjs/tutorials/)
    * Resources  Resources 
      * [ Adopters  ](https://langchain-ai.github.io/langgraphjs/adopters/)
      * [ FAQ  ](https://langchain-ai.github.io/langgraphjs/concepts/faq/)
      * [ Troubleshooting  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraphjs/reference/)
  * [ Versions  ](https://langchain-ai.github.io/langgraphjs/versions/)



Table of contents 

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#setup)
  * [ Add a node with the compiled subgraph  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#add-a-node-with-the-compiled-subgraph)
  * [ Add a node function that invokes the subgraph  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#add-a-node-function-that-invokes-the-subgraph)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
  5. [ Subgraphs  ](https://langchain-ai.github.io/langgraphjs/how-tos#subgraphs)



# How to add and use subgraphs[¶](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#how-to-add-and-use-subgraphs "Permanent link")

Prerequisites

This guide assumes familiarity with the following: 

  * [ Subgraphs ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#subgraphs)
  * [ State ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#state)



[Subgraphs](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#subgraphs) allow you to build complex systems with multiple components that are themselves graphs. A common use case for using subgraphs is building [multi-agent systems](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent).

The main question when adding subgraphs is how the parent graph and subgraph communicate, i.e. how they pass the [state](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#state) between each other during the graph execution. There are two scenarios:

  * parent graph and subgraph **share schema keys**. In this case, you can [add a node with the compiled subgraph](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#add-a-node-with-the-compiled-subgraph)
  * parent graph and subgraph have **different schemas**. In this case, you have to [add a node function that invokes the subgraph](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#add-a-node-function-that-invokes-the-subgraph): this is useful when the parent graph and the subgraph have different state schemas and you need to transform state before or after calling the subgraph



Below we show to to add subgraphs for each scenario.

![Screenshot 2024-07-11 at 1.01.28 PM.png]()

## Setup[¶](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#setup "Permanent link")

First, let's install the required packages

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-0-1)npminstall@langchain/langgraph@langchain/core

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Add a node with the compiled subgraph[¶](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#add-a-node-with-the-compiled-subgraph "Permanent link")

A common case is for the parent graph and subgraph to communicate over a shared state key (channel). For example, in [multi-agent](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent) systems, the agents often communicate over a shared [messages](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#why-use-messages) key.

If your subgraph shares state keys with the parent graph, you can follow these steps to add it to your graph:

  1. Define the subgraph workflow (`subgraphBuilder` in the example below) and compile it
  2. Pass compiled subgraph to the `.addNode` method when defining the parent graph workflow



Let's take a look at an example. 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-1-1)import{StateGraph,Annotation}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-1-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-1-3)constSubgraphStateAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-1-4)foo:Annotation<string>,// note that this key is shared with the parent graph state
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-1-5)bar:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-1-6)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-1-7)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-1-8)constsubgraphNode1=async(state:typeofSubgraphStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-1-9)return{bar:"bar"};
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-1-10)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-1-11)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-1-12)constsubgraphNode2=async(state:typeofSubgraphStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-1-13)// note that this node is using a state key ('bar') that is only available in the subgraph
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-1-14)// and is sending update on the shared state key ('foo')
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-1-15)return{foo:state.foo+state.bar};
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-1-16)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-1-17)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-1-18)constsubgraphBuilder=newStateGraph(SubgraphStateAnnotation)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-1-19).addNode("subgraphNode1",subgraphNode1)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-1-20).addNode("subgraphNode2",subgraphNode2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-1-21).addEdge("__start__","subgraphNode1")
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-1-22).addEdge("subgraphNode1","subgraphNode2")
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-1-23)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-1-24)constsubgraph=subgraphBuilder.compile();
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-1-25)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-1-26)// Define parent graph
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-1-27)constParentStateAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-1-28)foo:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-1-29)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-1-30)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-1-31)constnode1=async(state:typeofParentStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-1-32)return{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-1-33)foo:"hi! "+state.foo,
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-1-34)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-1-35)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-1-36)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-1-37)constbuilder=newStateGraph(ParentStateAnnotation)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-1-38).addNode("node1",node1)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-1-39)// note that we're adding the compiled subgraph as a node to the parent graph
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-1-40).addNode("node2",subgraph)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-1-41).addEdge("__start__","node1")
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-1-42).addEdge("node1","node2")
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-1-43)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-1-44)constgraph=builder.compile();

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-2-1)conststream=awaitgraph.stream({foo:"foo"});
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-2-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-2-3)forawait(constchunkofstream){
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-2-4)console.log(chunk);
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-2-5)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-3-1){ node1: { foo: 'hi! foo' } }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-3-2){ node2: { foo: 'hi! foobar' } }

```


You can see that the final output from the parent graph includes the results of subgraph invocation (the string `"bar"`). 

If you would like to see streaming output from the subgraph, you can specify `subgraphs: True` when streaming. See more on streaming from subgraphs in this [how-to guide](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-subgraphs/#stream-subgraph).

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-4-1)conststreamWithSubgraphs=awaitgraph.stream({foo:"foo"},{subgraphs:true});
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-4-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-4-3)forawait(constchunkofstreamWithSubgraphs){
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-4-4)console.log(chunk);
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-4-5)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-5-1)[ [], { node1: { foo: 'hi! foo' } } ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-5-2)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-5-3) [ 'node2:22f27b01-fa9f-5f46-9b5b-166a80d96791' ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-5-4) { subgraphNode1: { bar: 'bar' } }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-5-5)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-5-6)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-5-7) [ 'node2:22f27b01-fa9f-5f46-9b5b-166a80d96791' ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-5-8) { subgraphNode2: { foo: 'hi! foobar' } }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-5-9)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-5-10)[ [], { node2: { foo: 'hi! foobar' } } ]

```


You'll notice that the chunk output format has changed to include some additional information about the subgraph it came from. 

## Add a node function that invokes the subgraph[¶](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#add-a-node-function-that-invokes-the-subgraph "Permanent link")

For more complex systems you might want to define subgraphs that have a completely different schema from the parent graph (no shared keys). For example, in a multi-agent RAG system, a search agent might only need to keep track of queries and retrieved documents.

If that's the case for your application, you need to define a node **function that invokes the subgraph**. This function needs to transform the input (parent) state to the subgraph state before invoking the subgraph, and transform the results back to the parent state before returning the state update from the node.

Below we show how to modify our original example to call a subgraph from inside the node.

Note

You **cannot** invoke more than one subgraph inside the same node if you have checkpointing enabled for the subgraphs. See [this page](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence#define-the-graph-with-persistence) for more information. 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-6-1)import{StateGraph,Annotation}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-6-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-6-3)constSubgraphAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-6-4)bar:Annotation<string>,// note that this key is shared with the parent graph state
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-6-5)baz:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-6-6)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-6-7)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-6-8)constsubgraphNodeOne=async(state:typeofSubgraphAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-6-9)return{baz:"baz"};
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-6-10)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-6-11)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-6-12)constsubgraphNodeTwo=async(state:typeofSubgraphAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-6-13)return{bar:state.bar+state.baz}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-6-14)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-6-15)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-6-16)constsubgraphCalledInFunction=newStateGraph(SubgraphAnnotation)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-6-17).addNode("subgraphNode1",subgraphNodeOne)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-6-18).addNode("subgraphNode2",subgraphNodeTwo)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-6-19).addEdge("__start__","subgraphNode1")
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-6-20).addEdge("subgraphNode1","subgraphNode2")
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-6-21).compile();
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-6-22)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-6-23)// Define parent graph
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-6-24)constParentAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-6-25)foo:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-6-26)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-6-27)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-6-28)constnodeOne=async(state:typeofParentAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-6-29)return{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-6-30)foo:"hi! "+state.foo,
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-6-31)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-6-32)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-6-33)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-6-34)constnodeTwo=async(state:typeofParentAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-6-35)constresponse=awaitsubgraphCalledInFunction.invoke({
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-6-36)bar:state.foo,
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-6-37)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-6-38)return{foo:response.bar}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-6-39)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-6-40)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-6-41)constgraphWithFunction=newStateGraph(ParentStateAnnotation)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-6-42).addNode("node1",nodeOne)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-6-43)// note that we're adding the compiled subgraph as a node to the parent graph
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-6-44).addNode("node2",nodeTwo)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-6-45).addEdge("__start__","node1")
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-6-46).addEdge("node1","node2")
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-6-47).compile();

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-7-1)constgraphWithFunctionStream=awaitgraphWithFunction.stream({foo:"foo"},{subgraphs:true});
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-7-2)forawait(constchunkofgraphWithFunctionStream){
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-7-3)console.log(chunk);
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-7-4)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-8-1)[ [], { node1: { foo: 'hi! foo' } } ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-8-2)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-8-3) [ 'node2:1d2bb11a-3ed1-5c58-9b6f-c7af36a1eeb7' ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-8-4) { subgraphNode1: { baz: 'baz' } }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-8-5)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-8-6)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-8-7) [ 'node2:1d2bb11a-3ed1-5c58-9b6f-c7af36a1eeb7' ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-8-8) { subgraphNode2: { bar: 'hi! foobaz' } }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-8-9)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__codelineno-8-10)[ [], { node2: { foo: 'hi! foobaz' } } ]

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to update graph state from tools  ](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/) [ Next  How to view and update state in subgraphs  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
