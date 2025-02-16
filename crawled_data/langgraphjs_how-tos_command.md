---
url: https://langchain-ai.github.io/langgraphjs/how-tos/command/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/command/#how-to-combine-control-flow-and-state-updates-with-command)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to combine control flow and state updates with Command 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/command/?q= "Share")

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
          * Controllability  Controllability 
            * [ Controllability  ](https://langchain-ai.github.io/langgraphjs/how-tos#controllability)
            * [ How to create map-reduce branches for parallel execution  ](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/)
            * [ How to create branches for parallel node execution  ](https://langchain-ai.github.io/langgraphjs/how-tos/branching/)
            * How to combine control flow and state updates with Command  [ How to combine control flow and state updates with Command  ](https://langchain-ai.github.io/langgraphjs/how-tos/command/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/command/#setup)
              * [ Define graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/command/#define-graph)
              * [ Navigating to a node in a parent graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/command/#navigating-to-a-node-in-a-parent-graph)
          * [ Persistence  ](https://langchain-ai.github.io/langgraphjs/how-tos#persistence)
          * [ Memory  ](https://langchain-ai.github.io/langgraphjs/how-tos#memory)
          * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraphjs/how-tos#human-in-the-loop)
          * [ Streaming  ](https://langchain-ai.github.io/langgraphjs/how-tos#streaming)
          * [ Tool calling  ](https://langchain-ai.github.io/langgraphjs/how-tos#tool-calling)
          * [ Subgraphs  ](https://langchain-ai.github.io/langgraphjs/how-tos#subgraphs)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/command/#setup)
  * [ Define graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/command/#define-graph)
  * [ Navigating to a node in a parent graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/command/#navigating-to-a-node-in-a-parent-graph)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
  5. [ Controllability  ](https://langchain-ai.github.io/langgraphjs/how-tos#controllability)



# How to combine control flow and state updates with Command[¶](https://langchain-ai.github.io/langgraphjs/how-tos/command/#how-to-combine-control-flow-and-state-updates-with-command "Permanent link")

Prerequisites

This guide assumes familiarity with the following: 

  * [State](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#state)
  * [Nodes](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#nodes)
  * [Edges](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#edges)
  * [Command](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#command)



This functionality also requires `@langchain/langgraph>=0.2.29`. 

It can be useful to combine control flow (edges) and state updates (nodes). For example, you might want to BOTH perform state updates AND decide which node to go to next in the SAME node. LangGraph provides a way to do so by returning a `Command` object from node functions:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-0-1)constmyNode=(state:typeofStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-0-2)returnnewCommand({
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-0-3)// state update
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-0-4)update:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-0-5)foo:"bar",
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-0-6)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-0-7)// control flow
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-0-8)goto:"myOtherNode",
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-0-9)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-0-10)};

```


If you are using [subgraphs](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#subgraphs), you might want to navigate from a node a subgraph to a different subgraph (i.e. a different node in the parent graph). To do so, you can specify `graph: Command.PARENT` in Command:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-1-1)constmyNode=(state:typeofStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-1-2)returnnewCommand({
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-1-3)update:{foo:"bar"},
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-1-4)goto:"other_subgraph",// where `other_subgraph` is a node in the parent graph
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-1-5)graph:Command.PARENT,
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-1-6)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-1-7)};

```


This guide shows how you can use `Command` to add dynamic control flow in your LangGraph app.

## Setup[¶](https://langchain-ai.github.io/langgraphjs/how-tos/command/#setup "Permanent link")

First, let's install the required packages:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-2-1)yarnadd@langchain/langgraph@langchain/core

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

Let's create a simple graph with 3 nodes: A, B and C. We will first execute node A, and then decide whether to go to Node B or Node C next based on the output of node A.

## Define graph[¶](https://langchain-ai.github.io/langgraphjs/how-tos/command/#define-graph "Permanent link")

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-3-1)import{Annotation,Command}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-3-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-3-3)// Define graph state
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-3-4)constStateAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-3-5)foo:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-3-6)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-3-7)
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-3-8)// Define the nodes
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-3-9)constnodeA=async(_state:typeofStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-3-10)console.log("Called A");
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-3-11)// this is a replacement for a real conditional edge function
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-3-12)constgoto=Math.random()>.5?"nodeB":"nodeC";
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-3-13)// note how Command allows you to BOTH update the graph state AND route to the next node
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-3-14)returnnewCommand({
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-3-15)// this is the state update
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-3-16)update:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-3-17)foo:"a",
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-3-18)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-3-19)// this is a replacement for an edge
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-3-20)goto,
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-3-21)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-3-22)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-3-23)
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-3-24)// Nodes B and C are unchanged
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-3-25)constnodeB=async(state:typeofStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-3-26)console.log("Called B");
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-3-27)return{
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-3-28)foo:state.foo+"|b",
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-3-29)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-3-30)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-3-31)
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-3-32)constnodeC=async(state:typeofStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-3-33)console.log("Called C");
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-3-34)return{
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-3-35)foo:state.foo+"|c",
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-3-36)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-3-37)}

```


We can now create the `StateGraph` with the above nodes. Notice that the graph doesn't have [conditional edges](https://langchain-ai.github.io/langgraphjs/concepts/low_level#conditional-edges) for routing! This is because control flow is defined with `Command` inside `nodeA`.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-4-1)import{StateGraph}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-4-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-4-3)// NOTE: there are no edges between nodes A, B and C!
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-4-4)constgraph=newStateGraph(StateAnnotation)
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-4-5).addNode("nodeA",nodeA,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-4-6)ends:["nodeB","nodeC"],
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-4-7)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-4-8).addNode("nodeB",nodeB)
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-4-9).addNode("nodeC",nodeC)
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-4-10).addEdge("__start__","nodeA")
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-4-11).compile();

```


Important

You might have noticed that we add an `ends` field as an extra param to the node where we use `Command`. This is necessary for graph compilation and validation, and tells LangGraph that `nodeA` can navigate to `nodeB` and `nodeC`. 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-5-1)import*astslabfrom"tslab";
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-5-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-5-3)constdrawableGraph=awaitgraph.getGraphAsync();
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-5-4)constimage=awaitdrawableGraph.drawMermaidPng();
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-5-5)constarrayBuffer=awaitimage.arrayBuffer();
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-5-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-5-7)awaittslab.display.png(newUint8Array(arrayBuffer));

```


![]()

If we run the graph multiple times, we'd see it take different paths (A -> B or A -> C) based on the random choice in node A.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-6-1)awaitgraph.invoke({foo:""});

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-7-1)Called A
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-7-2)Called B
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-7-3){ foo: 'a|b' }

```


## Navigating to a node in a parent graph[¶](https://langchain-ai.github.io/langgraphjs/how-tos/command/#navigating-to-a-node-in-a-parent-graph "Permanent link")

Now let's demonstrate how you can navigate from inside a subgraph to a different node in a parent graph. We'll do so by changing `node_a` in the above example into a single-node graph that we'll add as a subgraph to our parent graph.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-8-1)// Define the nodes
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-8-2)constnodeASubgraph=async(_state:typeofStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-8-3)console.log("Called A");
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-8-4)// this is a replacement for a real conditional edge function
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-8-5)constgoto=Math.random()>.5?"nodeB":"nodeC";
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-8-6)// note how Command allows you to BOTH update the graph state AND route to the next node
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-8-7)returnnewCommand({
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-8-8)update:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-8-9)foo:"a",
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-8-10)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-8-11)goto,
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-8-12)// this tells LangGraph to navigate to node_b or node_c in the parent graph
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-8-13)// NOTE: this will navigate to the closest parent graph relative to the subgraph
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-8-14)graph:Command.PARENT,
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-8-15)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-8-16)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-8-17)
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-8-18)constsubgraph=newStateGraph(StateAnnotation)
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-8-19).addNode("nodeA",nodeASubgraph)
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-8-20).addEdge("__start__","nodeA")
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-8-21).compile();
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-8-22)
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-8-23)constparentGraph=newStateGraph(StateAnnotation)
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-8-24).addNode("subgraph",subgraph,{ends:["nodeB","nodeC"]})
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-8-25).addNode("nodeB",nodeB)
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-8-26).addNode("nodeC",nodeC)
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-8-27).addEdge("__start__","subgraph")
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-8-28).compile();
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-8-29)
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-8-30)awaitparentGraph.invoke({foo:""});

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-9-1)Called A
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-9-2)Called C
[](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__codelineno-9-3){ foo: 'a|c' }

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to create branches for parallel node execution  ](https://langchain-ai.github.io/langgraphjs/how-tos/branching/) [ Next  Persistence  ](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/command/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
