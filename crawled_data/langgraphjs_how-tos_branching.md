---
url: https://langchain-ai.github.io/langgraphjs/how-tos/branching/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#how-to-create-branches-for-parallel-node-execution)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to create branches for parallel node execution 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/branching/?q= "Share")

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
            * How to create branches for parallel node execution  [ How to create branches for parallel node execution  ](https://langchain-ai.github.io/langgraphjs/how-tos/branching/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#setup)
              * [ Fan out, fan in  ](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#fan-out-fan-in)
              * [ Conditional Branching  ](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#conditional-branching)
              * [ Stable Sorting  ](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#stable-sorting)
            * [ How to combine control flow and state updates with Command  ](https://langchain-ai.github.io/langgraphjs/how-tos/command/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#setup)
  * [ Fan out, fan in  ](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#fan-out-fan-in)
  * [ Conditional Branching  ](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#conditional-branching)
  * [ Stable Sorting  ](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#stable-sorting)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
  5. [ Controllability  ](https://langchain-ai.github.io/langgraphjs/how-tos#controllability)



# How to create branches for parallel node execution[¶](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#how-to-create-branches-for-parallel-node-execution "Permanent link")

LangGraph natively supports fan-out and fan-in using either regular edges or [conditionalEdges](https://langchain-ai.github.io/langgraphjs/reference/classes/langgraph.StateGraph.html#addConditionalEdges).

This lets you run nodes in parallel to speed up your total graph execution.

Below are some examples showing how to add create branching dataflows that work for you.

## Setup[¶](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#setup "Permanent link")

First, install LangGraph.js

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-0-1)yarnadd@langchain/langgraph@langchain/core

```


This guide will use OpenAI's GPT-4o model. We will optionally set our API key for [LangSmith tracing](https://smith.langchain.com/), which will give us best-in-class observability.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-1-1)// process.env.OPENAI_API_KEY = "sk_...";
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-1-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-1-3)// Optional, add tracing in LangSmith
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-1-4)// process.env.LANGCHAIN_API_KEY = "ls__..."
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-1-5)// process.env.LANGCHAIN_CALLBACKS_BACKGROUND = "true";
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-1-6)process.env.LANGCHAIN_CALLBACKS_BACKGROUND="true";
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-1-7)process.env.LANGCHAIN_TRACING_V2="true";
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-1-8)process.env.LANGCHAIN_PROJECT="Branching: LangGraphJS";

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-2-1)Branching: LangGraphJS

```


## Fan out, fan in[¶](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#fan-out-fan-in "Permanent link")

First, we will make a simple graph that branches out and back in. When merging back in, the state updates from all branches are applied by your **reducer** (the `aggregate` method below).

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-3-1)import{END,START,StateGraph,Annotation}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-3-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-3-3)constStateAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-3-4)aggregate:Annotation<string[]>({
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-3-5)reducer:(x,y)=>x.concat(y),
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-3-6)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-3-7)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-3-8)
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-3-9)// Create the graph
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-3-10)constnodeA=(state:typeofStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-3-11)console.log(`Adding I'm A to ${state.aggregate}`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-3-12)return{aggregate:[`I'm A`]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-3-13)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-3-14)constnodeB=(state:typeofStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-3-15)console.log(`Adding I'm B to ${state.aggregate}`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-3-16)return{aggregate:[`I'm B`]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-3-17)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-3-18)constnodeC=(state:typeofStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-3-19)console.log(`Adding I'm C to ${state.aggregate}`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-3-20)return{aggregate:[`I'm C`]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-3-21)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-3-22)constnodeD=(state:typeofStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-3-23)console.log(`Adding I'm D to ${state.aggregate}`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-3-24)return{aggregate:[`I'm D`]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-3-25)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-3-26)
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-3-27)constbuilder=newStateGraph(StateAnnotation)
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-3-28).addNode("a",nodeA)
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-3-29).addEdge(START,"a")
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-3-30).addNode("b",nodeB)
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-3-31).addNode("c",nodeC)
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-3-32).addNode("d",nodeD)
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-3-33).addEdge("a","b")
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-3-34).addEdge("a","c")
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-3-35).addEdge("b","d")
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-3-36).addEdge("c","d")
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-3-37).addEdge("d",END);
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-3-38)
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-3-39)constgraph=builder.compile();

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-4-1)import*astslabfrom"tslab";
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-4-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-4-3)constrepresentation=graph.getGraph();
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-4-4)constimage=awaitrepresentation.drawMermaidPng();
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-4-5)constarrayBuffer=awaitimage.arrayBuffer();
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-4-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-4-7)awaittslab.display.png(newUint8Array(arrayBuffer));

```


![]()

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-5-1)// Invoke the graph
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-5-2)constbaseResult=awaitgraph.invoke({aggregate:[]});
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-5-3)console.log("Base Result: ",baseResult);

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-6-1)Adding I'm A to 
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-6-2)Adding I'm B to I'm A
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-6-3)Adding I'm C to I'm A
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-6-4)Adding I'm D to I'm A,I'm B,I'm C
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-6-5)Base Result: { aggregate: [ "I'm A", "I'm B", "I'm C", "I'm D" ] }

```


## Conditional Branching[¶](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#conditional-branching "Permanent link")

If your fan-out is not deterministic, you can use [addConditionalEdges](https://langchain-ai.github.io/langgraphjs/reference/classes/index.StateGraph.html#addConditionalEdges) directly like this:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-7-1)constConditionalBranchingAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-7-2)aggregate:Annotation<string[]>({
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-7-3)reducer:(x,y)=>x.concat(y),
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-7-4)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-7-5)which:Annotation<string>({
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-7-6)reducer:(x:string,y:string)=>(y??x),
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-7-7)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-7-8)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-7-9)
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-7-10)// Create the graph
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-7-11)constnodeA2=(state:typeofConditionalBranchingAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-7-12)console.log(`Adding I'm A to ${state.aggregate}`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-7-13)return{aggregate:[`I'm A`]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-7-14)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-7-15)constnodeB2=(state:typeofConditionalBranchingAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-7-16)console.log(`Adding I'm B to ${state.aggregate}`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-7-17)return{aggregate:[`I'm B`]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-7-18)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-7-19)constnodeC2=(state:typeofConditionalBranchingAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-7-20)console.log(`Adding I'm C to ${state.aggregate}`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-7-21)return{aggregate:[`I'm C`]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-7-22)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-7-23)constnodeD2=(state:typeofConditionalBranchingAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-7-24)console.log(`Adding I'm D to ${state.aggregate}`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-7-25)return{aggregate:[`I'm D`]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-7-26)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-7-27)constnodeE2=(state:typeofConditionalBranchingAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-7-28)console.log(`Adding I'm E to ${state.aggregate}`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-7-29)return{aggregate:[`I'm E`]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-7-30)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-7-31)
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-7-32)// Define the route function
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-7-33)functionrouteCDorBC(state:typeofConditionalBranchingAnnotation.State):string[]{
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-7-34)if(state.which==="cd"){
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-7-35)return["c","d"];
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-7-36)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-7-37)return["b","c"];
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-7-38)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-7-39)
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-7-40)constbuilder2=newStateGraph(ConditionalBranchingAnnotation)
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-7-41).addNode("a",nodeA2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-7-42).addEdge(START,"a")
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-7-43).addNode("b",nodeB2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-7-44).addNode("c",nodeC2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-7-45).addNode("d",nodeD2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-7-46).addNode("e",nodeE2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-7-47)// Add conditional edges
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-7-48)// Third parameter is to support visualizing the graph
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-7-49).addConditionalEdges("a",routeCDorBC,["b","c","d"])
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-7-50).addEdge("b","e")
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-7-51).addEdge("c","e")
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-7-52).addEdge("d","e")
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-7-53).addEdge("e",END);
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-7-54)
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-7-55)constgraph2=builder2.compile();

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-8-1)import*astslabfrom"tslab";
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-8-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-8-3)constrepresentation2=graph2.getGraph();
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-8-4)constimage2=awaitrepresentation2.drawMermaidPng();
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-8-5)constarrayBuffer2=awaitimage2.arrayBuffer();
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-8-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-8-7)awaittslab.display.png(newUint8Array(arrayBuffer2));

```


![]()

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-9-1)// Invoke the graph
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-9-2)letg2result=awaitgraph2.invoke({aggregate:[],which:"bc"});
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-9-3)console.log("Result 1: ",g2result);

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-10-1)Adding I'm A to 
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-10-2)Adding I'm B to I'm A
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-10-3)Adding I'm C to I'm A
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-10-4)Adding I'm E to I'm A,I'm B,I'm C
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-10-5)Result 1: { aggregate: [ "I'm A", "I'm B", "I'm C", "I'm E" ], which: 'bc' }

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-11-1)g2result=awaitgraph2.invoke({aggregate:[],which:"cd"});
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-11-2)console.log("Result 2: ",g2result);

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-12-1)Adding I'm A to 
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-12-2)Adding I'm C to I'm A
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-12-3)Adding I'm D to I'm A
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-12-4)Adding I'm E to I'm A,I'm C,I'm D
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-12-5)``````output
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-12-6)Result 2: { aggregate: [ "I'm A", "I'm C", "I'm D", "I'm E" ], which: 'cd' }

```


## Stable Sorting[¶](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#stable-sorting "Permanent link")

When fanned out, nodes are run in parallel as a single "superstep". The updates from each superstep are all applied to the state in sequence once the superstep has completed.

If you need consistent, predetermined ordering of updates from a parallel superstep, you should write the outputs (along with an identifying key) to a separate field in your state, then combine them in the "sink" node by adding regular `edge`s from each of the fanout nodes to the rendezvous point.

For instance, suppose I want to order the outputs of the parallel step by "reliability".

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-1)typeScoredValue={
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-2)value:string;
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-3)score:number;
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-4)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-5)
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-6)constreduceFanouts=(left?:ScoredValue[],right?:ScoredValue[])=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-7)if(!left){
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-8)left=[];
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-9)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-10)if(!right||right?.length===0){
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-11)// Overwrite. Similar to redux.
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-12)return[];
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-13)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-14)returnleft.concat(right);
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-15)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-16)
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-17)constStableSortingAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-18)aggregate:Annotation<string[]>({
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-19)reducer:(x,y)=>x.concat(y),
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-20)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-21)which:Annotation<string>({
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-22)reducer:(x:string,y:string)=>(y??x),
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-23)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-24)fanoutValues:Annotation<ScoredValue[]>({
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-25)reducer:reduceFanouts,
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-26)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-27)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-28)
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-29)
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-30)classParallelReturnNodeValue{
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-31)private_value:string;
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-32)private_score:number;
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-33)
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-34)constructor(nodeSecret:string,score:number){
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-35)this._value=nodeSecret;
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-36)this._score=score;
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-37)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-38)
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-39)publiccall(state:typeofStableSortingAnnotation.State){
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-40)console.log(`Adding ${this._value} to ${state.aggregate}`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-41)return{fanoutValues:[{value:this._value,score:this._score}]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-42)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-43)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-44)
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-45)// Create the graph
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-46)
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-47)constnodeA3=(state:typeofStableSortingAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-48)console.log(`Adding I'm A to ${state.aggregate}`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-49)return{aggregate:["I'm A"]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-50)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-51)
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-52)constnodeB3=newParallelReturnNodeValue("I'm B",0.1);
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-53)constnodeC3=newParallelReturnNodeValue("I'm C",0.9);
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-54)constnodeD3=newParallelReturnNodeValue("I'm D",0.3);
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-55)
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-56)constaggregateFanouts=(state:typeofStableSortingAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-57)// Sort by score (reversed)
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-58)state.fanoutValues.sort((a,b)=>b.score-a.score);
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-59)return{
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-60)aggregate:state.fanoutValues.map((v)=>v.value).concat(["I'm E"]),
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-61)fanoutValues:[],
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-62)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-63)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-64)
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-65)// Define the route function
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-66)functionrouteBCOrCD(state:typeofStableSortingAnnotation.State):string[]{
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-67)if(state.which==="cd"){
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-68)return["c","d"];
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-69)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-70)return["b","c"];
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-71)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-72)
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-73)constbuilder3=newStateGraph(StableSortingAnnotation)
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-74).addNode("a",nodeA3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-75).addEdge(START,"a")
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-76).addNode("b",nodeB3.call.bind(nodeB3))
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-77).addNode("c",nodeC3.call.bind(nodeC3))
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-78).addNode("d",nodeD3.call.bind(nodeD3))
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-79).addNode("e",aggregateFanouts)
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-80).addConditionalEdges("a",routeBCOrCD,["b","c","d"])
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-81).addEdge("b","e")
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-82).addEdge("c","e")
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-83).addEdge("d","e")
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-84).addEdge("e",END);
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-85)
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-86)constgraph3=builder3.compile();
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-87)
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-88)// Invoke the graph
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-89)letg3result=awaitgraph3.invoke({aggregate:[],which:"bc"});
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-13-90)console.log("Result 1: ",g3result);

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-14-1)Adding I'm A to 
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-14-2)Adding I'm B to I'm A
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-14-3)Adding I'm C to I'm A
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-14-4)Result 1: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-14-5) aggregate: [ "I'm A", "I'm C", "I'm B", "I'm E" ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-14-6) which: 'bc',
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-14-7) fanoutValues: []
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-14-8)}

```


Our aggregateFanouts "sink" node in this case took the mapped values and then sorted them in a consistent way. Notice that, because it returns an empty array for `fanoutValues`, our `reduceFanouts` reducer function decided to overwrite the previous values in the state. 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-15-1)letg3result2=awaitgraph3.invoke({aggregate:[],which:"cd"});
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-15-2)console.log("Result 2: ",g3result2);

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-16-1)Adding I'm A to 
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-16-2)Adding I'm C to I'm A
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-16-3)Adding I'm D to I'm A
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-16-4)Result 2: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-16-5) aggregate: [ "I'm A", "I'm C", "I'm D", "I'm E" ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-16-6) which: 'cd',
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-16-7) fanoutValues: []
[](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__codelineno-16-8)}

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to create map-reduce branches for parallel execution  ](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/) [ Next  How to combine control flow and state updates with Command  ](https://langchain-ai.github.io/langgraphjs/how-tos/command/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/branching/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
