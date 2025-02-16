---
url: https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#how-to-add-breakpoints)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to add breakpoints 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/?q= "Share")

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
            * How to add breakpoints  [ How to add breakpoints  ](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#setup)
              * [ Simple Usage  ](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#simple-usage)
              * [ Agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#agent)
              * [ Interacting with the Agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#interacting-with-the-agent)
            * [ How to add dynamic breakpoints  ](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#setup)
  * [ Simple Usage  ](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#simple-usage)
  * [ Agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#agent)
  * [ Interacting with the Agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#interacting-with-the-agent)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
  5. [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraphjs/how-tos#human-in-the-loop)



# How to add breakpoints[¶](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#how-to-add-breakpoints "Permanent link")

Prerequisites

This guide assumes familiarity with the following concepts:ddd

  * [Breakpoints](https://langchain-ai.github.io/langgraphjs/concepts/breakpoints)
  * [LangGraph Glossary](https://langchain-ai.github.io/langgraphjs/concepts/low_level)



Human-in-the-loop (HIL) interactions are crucial for [agentic systems](https://langchain-ai.github.io/langgraphjs/concepts/agentic_concepts/#human-in-the-loop). [Breakpoints](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#breakpoints) are a common HIL interaction pattern, allowing the graph to stop at specific steps and seek human approval before proceeding (e.g., for sensitive actions).

Breakpoints are built on top of LangGraph [checkpoints](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#checkpointer), which save the graph's state after each node execution. Checkpoints are saved in [threads](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#threads) that preserve graph state and can be accessed after a graph has finished execution. This allows for graph execution to pause at specific points, await human approval, and then resume execution from the last checkpoint.

![Screenshot 2024-07-03 at 1.32.19 PM.png]()

## Setup[¶](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#setup "Permanent link")

First we need to install the packages required

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-0-1)npminstall@langchain/langgraph@langchain/anthropic@langchain/core

```


Next, we need to set API keys for Anthropic (the LLM we will use)

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-1-1)exportANTHROPIC_API_KEY=your-api-key

```


Optionally, we can set API key for [LangSmith tracing](https://smith.langchain.com/), which will give us best-in-class observability.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-2-1)exportLANGCHAIN_TRACING_V2="true"
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-2-2)exportLANGCHAIN_CALLBACKS_BACKGROUND="true"
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-2-3)exportLANGCHAIN_API_KEY=your-api-key

```


## Simple Usage[¶](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#simple-usage "Permanent link")

Let's look at very basic usage of this.

Below, we do two things:

1) We specify the [breakpoint](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#breakpoints) using `interruptBefore` the specified step.

2) We set up a [checkpointer](https://langchain-ai.github.io/langgraphjs/concepts/#checkpoints) to save the state of the graph.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-3-1)import{StateGraph,START,END,Annotation}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-3-2)import{MemorySaver}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-3-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-3-4)constGraphState=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-3-5)input:Annotation<string>
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-3-6)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-3-7)
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-3-8)conststep1=(state:typeofGraphState.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-3-9)console.log("---Step 1---");
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-3-10)returnstate;
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-3-11)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-3-12)
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-3-13)conststep2=(state:typeofGraphState.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-3-14)console.log("---Step 2---");
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-3-15)returnstate;
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-3-16)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-3-17)
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-3-18)conststep3=(state:typeofGraphState.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-3-19)console.log("---Step 3---");
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-3-20)returnstate;
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-3-21)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-3-22)
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-3-23)
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-3-24)constbuilder=newStateGraph(GraphState)
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-3-25).addNode("step1",step1)
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-3-26).addNode("step2",step2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-3-27).addNode("step3",step3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-3-28).addEdge(START,"step1")
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-3-29).addEdge("step1","step2")
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-3-30).addEdge("step2","step3")
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-3-31).addEdge("step3",END);
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-3-32)
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-3-33)
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-3-34)// Set up memory
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-3-35)constgraphStateMemory=newMemorySaver()
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-3-36)
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-3-37)constgraph=builder.compile({
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-3-38)checkpointer:graphStateMemory,
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-3-39)interruptBefore:["step3"]
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-3-40)});

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-4-1)import*astslabfrom"tslab";
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-4-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-4-3)constdrawableGraphGraphState=graph.getGraph();
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-4-4)constgraphStateImage=awaitdrawableGraphGraphState.drawMermaidPng();
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-4-5)constgraphStateArrayBuffer=awaitgraphStateImage.arrayBuffer();
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-4-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-4-7)awaittslab.display.png(newUint8Array(graphStateArrayBuffer));

```


![]()

We create a [thread ID](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#threads) for the checkpointer.

We run until step 3, as defined with `interruptBefore`. 

After the user input / approval, [we resume execution](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#breakpoints) by invoking the graph with `null`. 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-5-1)// Input
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-5-2)constinitialInput={input:"hello world"};
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-5-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-5-4)// Thread
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-5-5)constgraphStateConfig={configurable:{thread_id:"1"},streamMode:"values"asconst};
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-5-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-5-7)// Run the graph until the first interruption
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-5-8)forawait(consteventofawaitgraph.stream(initialInput,graphStateConfig)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-5-9)console.log(`--- ${event.input} ---`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-5-10)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-5-11)
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-5-12)// Will log when the graph is interrupted, after step 2.
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-5-13)console.log("---GRAPH INTERRUPTED---");
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-5-14)
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-5-15)// If approved, continue the graph execution. We must pass `null` as
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-5-16)// the input here, or the graph will
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-5-17)forawait(consteventofawaitgraph.stream(null,graphStateConfig)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-5-18)console.log(`--- ${event.input} ---`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-5-19)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-6-1)--- hello world ---
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-6-2)---Step 1---
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-6-3)--- hello world ---
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-6-4)---Step 2---
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-6-5)--- hello world ---
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-6-6)---GRAPH INTERRUPTED---
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-6-7)---Step 3---
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-6-8)--- hello world ---

```


## Agent[¶](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#agent "Permanent link")

In the context of agents, breakpoints are useful to manually approve certain agent actions.

To show this, we will build a relatively simple ReAct-style agent that does tool calling. 

We'll add a breakpoint before the `action` node is called. 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-1)// Set up the tool
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-2)import{ChatAnthropic}from"@langchain/anthropic";
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-3)import{tool}from"@langchain/core/tools";
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-4)import{StateGraph,START,END}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-5)import{MemorySaver,Annotation}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-6)import{ToolNode}from"@langchain/langgraph/prebuilt";
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-7)import{BaseMessage,AIMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-8)import{z}from"zod";
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-9)
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-10)constAgentState=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-11)messages:Annotation<BaseMessage[]>({
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-12)reducer:(x,y)=>x.concat(y),
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-13)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-14)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-15)
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-16)constsearch=tool((_)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-17)return"It's sunny in San Francisco, but you better look out if you're a Gemini 😈.";
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-18)},{
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-19)name:"search",
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-20)description:"Call to surf the web.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-21)schema:z.string(),
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-22)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-23)
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-24)consttools=[search]
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-25)consttoolNode=newToolNode<typeofAgentState.State>(tools)
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-26)
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-27)// Set up the model
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-28)constmodel=newChatAnthropic({model:"claude-3-5-sonnet-20240620"})
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-29)constmodelWithTools=model.bindTools(tools)
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-30)
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-31)
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-32)// Define nodes and conditional edges
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-33)
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-34)// Define the function that determines whether to continue or not
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-35)functionshouldContinue(state:typeofAgentState.State):"action"|typeofEND{
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-36)constlastMessage=state.messages[state.messages.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-37)// If there is no function call, then we finish
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-38)if(lastMessage&&!(lastMessageasAIMessage).tool_calls?.length){
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-39)returnEND;
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-40)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-41)// Otherwise if there is, we continue
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-42)return"action";
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-43)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-44)
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-45)// Define the function that calls the model
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-46)asyncfunctioncallModel(state:typeofAgentState.State):Promise<Partial<typeofAgentState.State>>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-47)constmessages=state.messages;
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-48)constresponse=awaitmodelWithTools.invoke(messages);
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-49)// We return an object with a messages property, because this will get added to the existing list
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-50)return{messages:[response]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-51)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-52)
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-53)// Define a new graph
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-54)constworkflow=newStateGraph(AgentState)
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-55)// Define the two nodes we will cycle between
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-56).addNode("agent",callModel)
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-57).addNode("action",toolNode)
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-58)// We now add a conditional edge
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-59).addConditionalEdges(
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-60)// First, we define the start node. We use `agent`.
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-61)// This means these are the edges taken after the `agent` node is called.
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-62)"agent",
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-63)// Next, we pass in the function that will determine which node is called next.
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-64)shouldContinue
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-65))
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-66)// We now add a normal edge from `action` to `agent`.
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-67)// This means that after `action` is called, `agent` node is called next.
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-68).addEdge("action","agent")
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-69)// Set the entrypoint as `agent`
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-70)// This means that this node is the first one called
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-71).addEdge(START,"agent");
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-72)
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-73)
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-74)// Setup memory
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-75)constmemory=newMemorySaver();
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-76)
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-77)// Finally, we compile it!
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-78)// This compiles it into a LangChain Runnable,
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-79)// meaning you can use it as you would any other runnable
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-80)constapp=workflow.compile({
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-81)checkpointer:memory,
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-82)interruptBefore:["action"]
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-7-83)});

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-8-1)import*astslabfrom"tslab";
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-8-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-8-3)constdrawableGraph=app.getGraph();
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-8-4)constimage=awaitdrawableGraph.drawMermaidPng();
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-8-5)constarrayBuffer=awaitimage.arrayBuffer();
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-8-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-8-7)awaittslab.display.png(newUint8Array(arrayBuffer));

```


![]()

## Interacting with the Agent[¶](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#interacting-with-the-agent "Permanent link")

We can now interact with the agent.

We see that it stops before calling a tool, because `interruptBefore` is set before the `action` node.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-9-1)import{HumanMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-9-2)// Input
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-9-3)constinputs=newHumanMessage("search for the weather in sf now");
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-9-4)
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-9-5)// Thread
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-9-6)constconfig={configurable:{thread_id:"3"},streamMode:"values"asconst};
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-9-7)
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-9-8)forawait(consteventofawaitapp.stream({
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-9-9)messages:[inputs]
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-9-10)},config)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-9-11)constrecentMsg=event.messages[event.messages.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-9-12)console.log(`================================ ${recentMsg._getType()} Message (1) =================================`)
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-9-13)console.log(recentMsg.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-9-14)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-10-1)================================ human Message (1) =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-10-2)search for the weather in sf now
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-10-3)================================ ai Message (1) =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-10-4)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-10-5) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-10-6)  type: 'text',
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-10-7)  text: "Certainly! I'll search for the current weather in San Francisco for you. Let me use the search function to find this information."
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-10-8) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-10-9) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-10-10)  type: 'tool_use',
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-10-11)  id: 'toolu_01R524BmxkEm7Rf5Ss53cqkM',
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-10-12)  name: 'search',
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-10-13)  input: { input: 'current weather in San Francisco' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-10-14) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-10-15)]

```


**Resume**

We can now call the agent again with no inputs to continue.

This will run the tool as requested.

Running an interrupted graph with `null` in the inputs means to `proceed as if the interruption didn't occur.`

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-11-1)forawait(consteventofawaitapp.stream(null,config)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-11-2)constrecentMsg=event.messages[event.messages.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-11-3)console.log(`================================ ${recentMsg._getType()} Message (1) =================================`)
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-11-4)console.log(recentMsg.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-11-5)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-12-1)================================ tool Message (1) =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-12-2)It's sunny in San Francisco, but you better look out if you're a Gemini 😈.
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-12-3)================================ ai Message (1) =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-12-4)Based on the search results, I can provide you with information about the current weather in San Francisco:
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-12-5)
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-12-6)The weather in San Francisco is currently sunny. This means it's a clear day with plenty of sunshine, which is great for outdoor activities or simply enjoying the city.
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-12-7)
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-12-8)However, I should note that the search result included an unusual comment about Geminis. This appears to be unrelated to the weather and might be a quirk of the search engine or a reference to something else entirely. For accurate and detailed weather information, it would be best to check a reliable weather service or website.
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-12-9)
[](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__codelineno-12-10)Is there anything else you'd like to know about the weather in San Francisco or any other location?

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to add semantic search to your agent's memory  ](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/) [ Next  How to add dynamic breakpoints  ](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
