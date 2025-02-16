---
url: https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#how-to-add-dynamic-breakpoints)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to add dynamic breakpoints 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/?q= "Share")

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
          * Human-in-the-loop  Human-in-the-loop 
            * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraphjs/how-tos#human-in-the-loop)
            * [ How to add breakpoints  ](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/)
            * How to add dynamic breakpoints  [ How to add dynamic breakpoints  ](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/) Table of contents 
              * [ Define the graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#define-the-graph)
              * [ Run the graph with dynamic interrupt  ](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#run-the-graph-with-dynamic-interrupt)
              * [ Update the graph state  ](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#update-the-graph-state)
            * [ How to edit graph state  ](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/)
            * [ How to wait for user input  ](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/)
            * [ How to wait for user input (Functional API)  ](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/)
            * [ How to view and update past graph state  ](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/)
            * [ Review Tool Calls  ](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/)
            * [ How to review tool calls (Functional API)  ](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/)
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

  * [ Define the graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#define-the-graph)
  * [ Run the graph with dynamic interrupt  ](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#run-the-graph-with-dynamic-interrupt)
  * [ Update the graph state  ](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#update-the-graph-state)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
  5. [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraphjs/how-tos#human-in-the-loop)



# How to add dynamic breakpoints[¶](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#how-to-add-dynamic-breakpoints "Permanent link")

Note

For **human-in-the-loop** workflows use the new `interrupt()`[](https://langchain-ai.github.io/langgraphjs/reference/functions/langgraph.interrupt-1.html) function for **human-in-the-loop** workflows. Please review the [Human-in-the-loop conceptual guide](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop) for more information about design patterns with `interrupt`.

Prerequisites

This guide assumes familiarity with the following concepts:

  * [Breakpoints](https://langchain-ai.github.io/langgraphjs/concepts/breakpoints)
  * [LangGraph Glossary](https://langchain-ai.github.io/langgraphjs/concepts/low_level)



Human-in-the-loop (HIL) interactions are crucial for [agentic systems](https://langchain-ai.github.io/langgraphjs/concepts/agentic_concepts/#human-in-the-loop). [Breakpoints](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#breakpoints) are a common HIL interaction pattern, allowing the graph to stop at specific steps and seek human approval before proceeding (e.g., for sensitive actions).

In LangGraph you can add breakpoints before / after a node is executed. But oftentimes it may be helpful to **dynamically** interrupt the graph from inside a given node based on some condition. When doing so, it may also be helpful to include information about **why** that interrupt was raised.

This guide shows how you can dynamically interrupt the graph using `NodeInterupt` -- a special exception that can be raised from inside a node. Let's see it in action!

### Define the graph[¶](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#define-the-graph "Permanent link")

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-0-1)import{
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-0-2)Annotation,
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-0-3)MemorySaver,
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-0-4)NodeInterrupt,
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-0-5)StateGraph,
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-0-6)}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-0-7)
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-0-8)constStateAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-0-9)input:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-0-10)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-0-11)
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-0-12)conststep1=async(state:typeofStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-0-13)console.log("---Step 1---");
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-0-14)returnstate;
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-0-15)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-0-16)
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-0-17)conststep2=async(state:typeofStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-0-18)// Let's optionally raise a NodeInterrupt
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-0-19)// if the length of the input is longer than 5 characters
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-0-20)if(state.input?.length>5){
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-0-21)thrownewNodeInterrupt(`Received input that is longer than 5 characters: ${state.input}`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-0-22)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-0-23)console.log("---Step 2---");
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-0-24)returnstate;
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-0-25)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-0-26)
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-0-27)conststep3=async(state:typeofStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-0-28)console.log("---Step 3---");
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-0-29)returnstate;
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-0-30)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-0-31)
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-0-32)constcheckpointer=newMemorySaver();
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-0-33)
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-0-34)constgraph=newStateGraph(StateAnnotation)
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-0-35).addNode("step1",step1)
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-0-36).addNode("step2",step2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-0-37).addNode("step3",step3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-0-38).addEdge("__start__","step1")
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-0-39).addEdge("step1","step2")
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-0-40).addEdge("step2","step3")
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-0-41).addEdge("step3","__end__")
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-0-42).compile({checkpointer});

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-1-1)import*astslabfrom"tslab";
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-1-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-1-3)constrepresentation=graph.getGraph();
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-1-4)constimage=awaitrepresentation.drawMermaidPng();
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-1-5)constarrayBuffer=awaitimage.arrayBuffer();
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-1-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-1-7)awaittslab.display.png(newUint8Array(arrayBuffer));

```


![]()

### Run the graph with dynamic interrupt[¶](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#run-the-graph-with-dynamic-interrupt "Permanent link")

First, let's run the graph with an input that's <= 5 characters long. This should safely ignore the interrupt condition we defined and return the original input at the end of the graph execution.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-2-1)constinitialInput={input:"hello"};
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-2-2)constconfig={
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-2-3)configurable:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-2-4)thread_id:"1",
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-2-5)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-2-6)streamMode:"values"asconst,
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-2-7)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-2-8)
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-2-9)conststream=awaitgraph.stream(initialInput,config);
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-2-10)
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-2-11)forawait(consteventofstream){
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-2-12)console.log(event);
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-2-13)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-3-1){ input: 'hello' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-3-2)---Step 1---
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-3-3){ input: 'hello' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-3-4)---Step 2---
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-3-5){ input: 'hello' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-3-6)---Step 3---
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-3-7){ input: 'hello' }

```


If we inspect the graph at this point, we can see that there are no more tasks left to run and that the graph indeed finished execution. 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-4-1)conststate=awaitgraph.getState(config);
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-4-2)console.log(state.next);
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-4-3)console.log(state.tasks);

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-5-1)[]
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-5-2)[]

```


Now, let's run the graph with an input that's longer than 5 characters. This should trigger the dynamic interrupt we defined via raising a `NodeInterrupt` error inside the `step2` node. 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-6-1)constlongInput={input:"hello world"};
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-6-2)constconfig2={
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-6-3)configurable:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-6-4)thread_id:"2",
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-6-5)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-6-6)streamMode:"values"asconst,
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-6-7)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-6-8)
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-6-9)conststreamWithInterrupt=awaitgraph.stream(longInput,config2);
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-6-10)
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-6-11)forawait(consteventofstreamWithInterrupt){
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-6-12)console.log(event);
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-6-13)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-7-1){ input: 'hello world' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-7-2)---Step 1---
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-7-3){ input: 'hello world' }

```


We can see that the graph now stopped while executing `step2`. If we inspect the graph state at this point, we can see the information on what node is set to execute next (`step2`), as well as what node raised the interrupt (also `step2`), and additional information about the interrupt. 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-8-1)conststate2=awaitgraph.getState(config2);
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-8-2)console.log(state2.next);
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-8-3)console.log(JSON.stringify(state2.tasks,null,2));

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-9-1)[ 'step2' ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-9-2)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-9-3) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-9-4)  "id": "c91a38f7-2aec-5c38-a3f0-60fba6efe73c",
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-9-5)  "name": "step2",
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-9-6)  "interrupts": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-9-7)   {
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-9-8)    "value": "Received input that is longer than 5 characters: hello world",
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-9-9)    "when": "during"
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-9-10)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-9-11)  ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-9-12) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-9-13)]

```


If we try to resume the graph from the breakpoint, we will simply interrupt again as our inputs & graph state haven't changed. 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-10-1)// NOTE: to resume the graph from a dynamic interrupt we use the same syntax as
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-10-2)// regular interrupts -- we pass null as the input
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-10-3)constresumedStream=awaitgraph.stream(null,config2);
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-10-4)
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-10-5)forawait(consteventofresumedStream){
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-10-6)console.log(event);
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-10-7)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-11-1)conststate3=awaitgraph.getState(config2);
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-11-2)console.log(state3.next);
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-11-3)console.log(JSON.stringify(state2.tasks,null,2));

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-12-1)[ 'step2' ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-12-2)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-12-3) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-12-4)  "id": "c91a38f7-2aec-5c38-a3f0-60fba6efe73c",
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-12-5)  "name": "step2",
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-12-6)  "interrupts": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-12-7)   {
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-12-8)    "value": "Received input that is longer than 5 characters: hello world",
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-12-9)    "when": "during"
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-12-10)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-12-11)  ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-12-12) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-12-13)]

```


### Update the graph state[¶](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#update-the-graph-state "Permanent link")

To get around it, we can do several things. 

First, we could simply run the graph on a different thread with a shorter input, like we did in the beginning. Alternatively, if we want to resume the graph execution from the breakpoint, we can update the state to have an input that's shorter than 5 characters (the condition for our interrupt).

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-13-1)// NOTE: this update will be applied as of the last successful node before the interrupt,
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-13-2)// i.e. `step1`, right before the node with an interrupt
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-13-3)awaitgraph.updateState(config2,{input:"short"});
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-13-4)
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-13-5)constupdatedStream=awaitgraph.stream(null,config2);
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-13-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-13-7)forawait(consteventofupdatedStream){
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-13-8)console.log(event);
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-13-9)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-13-10)
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-13-11)conststate4=awaitgraph.getState(config2);
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-13-12)console.log(state4.next);
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-13-13)console.log(state4.values);

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-14-1)---Step 2---
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-14-2){ input: 'short' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-14-3)---Step 3---
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-14-4){ input: 'short' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-14-5)[]
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-14-6){ input: 'short' }

```


You can also update the state **as node`step2`** (interrupted node) which would skip over that node altogether 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-15-1)constconfig3={
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-15-2)configurable:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-15-3)thread_id:"3",
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-15-4)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-15-5)streamMode:"values"asconst,
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-15-6)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-15-7)
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-15-8)constskipStream=awaitgraph.stream({input:"hello world"},config3);
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-15-9)
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-15-10)// Run the graph until the first interruption
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-15-11)forawait(consteventofskipStream){
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-15-12)console.log(event);
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-15-13)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-16-1){ input: 'hello world' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-16-2)---Step 1---
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-16-3){ input: 'hello world' }

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-17-1)// NOTE: this update will skip the node `step2` entirely
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-17-2)awaitgraph.updateState(config3,undefined,"step2");
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-17-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-17-4)// Resume the stream
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-17-5)forawait(consteventofawaitgraph.stream(null,config3)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-17-6)console.log(event);
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-17-7)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-17-8)
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-17-9)conststate5=awaitgraph.getState(config3);
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-17-10)console.log(state5.next);
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-17-11)console.log(state5.values);

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-18-1)---Step 3---
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-18-2){ input: 'hello world' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-18-3)[]
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__codelineno-18-4){ input: 'hello world' }

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to add breakpoints  ](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/) [ Next  How to edit graph state  ](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
