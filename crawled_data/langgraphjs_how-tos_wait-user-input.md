---
url: https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#how-to-wait-for-user-input)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to wait for user input 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/?q= "Share")

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
            * [ How to add dynamic breakpoints  ](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/)
            * [ How to edit graph state  ](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/)
            * How to wait for user input  [ How to wait for user input  ](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#setup)
              * [ Simple Usage  ](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#simple-usage)
              * [ Agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#agent)
              * [ Interacting with the Agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#interacting-with-the-agent)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#setup)
  * [ Simple Usage  ](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#simple-usage)
  * [ Agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#agent)
  * [ Interacting with the Agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#interacting-with-the-agent)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
  5. [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraphjs/how-tos#human-in-the-loop)



# How to wait for user input[¶](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#how-to-wait-for-user-input "Permanent link")

Prerequisites

This guide assumes familiarity with the following concepts:

  * [Human-in-the-loop](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop)
  * [Breakpoints](https://langchain-ai.github.io/langgraphjs/concepts/breakpoints)
  * [LangGraph Glossary](https://langchain-ai.github.io/langgraphjs/concepts/low_level)



Human-in-the-loop (HIL) interactions are crucial for [agentic systems](https://langchain-ai.github.io/langgraphjs/concepts/agentic_concepts/#human-in-the-loop). Waiting for human input is a common HIL interaction pattern, allowing the agent to ask the user clarifying questions and await input before proceeding. 

We can implement these in LangGraph using the `interrupt()`[](https://langchain-ai.github.io/langgraphjs/reference/functions/langgraph.interrupt-1.html) function. `interrupt` allows us to stop graph execution to collect input from a user and continue execution with collected input.

![Screenshot 2024-07-08 at 5.26.26 PM.png]()

## Setup[¶](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#setup "Permanent link")

First we need to install the packages required

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-0-1)npminstall@langchain/langgraph@langchain/anthropic@langchain/corezod

```


Next, we need to set API keys for Anthropic (the LLM we will use)

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-1-1)exportANTHROPIC_API_KEY=your-api-key

```


Optionally, we can set API key for [LangSmith tracing](https://smith.langchain.com/), which will give us best-in-class observability.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-2-1)exportLANGCHAIN_TRACING_V2="true"
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-2-2)exportLANGCHAIN_CALLBACKS_BACKGROUND="true"
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-2-3)exportLANGCHAIN_API_KEY=your-api-key

```


## Simple Usage[¶](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#simple-usage "Permanent link")

Let's explore a basic example of using human feedback. A straightforward approach is to create a node, **`human_feedback`**, designed specifically to collect user input. This allows us to gather feedback at a specific, chosen point in our graph.

Steps:

  1. **Call`interrupt()`** inside the **`human_feedback`**node.
  2. We set up a [checkpointer](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#persistence) to save the state of the graph up until this node.
  3. **Use`new Command({ resume: ... })`** to provide the requested value to the **`human_feedback`**node and resume execution.



```
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-3-1)import{StateGraph,Annotation,START,END,interrupt,MemorySaver}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-3-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-3-3)constStateAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-3-4)input:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-3-5)userFeedback:Annotation<string>
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-3-6)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-3-7)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-3-8)conststep1=(_state:typeofStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-3-9)console.log("---Step 1---");
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-3-10)return{};
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-3-11)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-3-12)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-3-13)consthumanFeedback=(_state:typeofStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-3-14)console.log("--- humanFeedback ---");
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-3-15)constfeedback:string=interrupt("Please provide feedback");
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-3-16)return{
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-3-17)userFeedback:feedback
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-3-18)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-3-19)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-3-20)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-3-21)conststep3=(_state:typeofStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-3-22)console.log("---Step 3---");
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-3-23)return{};
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-3-24)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-3-25)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-3-26)constbuilder=newStateGraph(StateAnnotation)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-3-27).addNode("step1",step1)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-3-28).addNode("humanFeedback",humanFeedback)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-3-29).addNode("step3",step3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-3-30).addEdge(START,"step1")
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-3-31).addEdge("step1","humanFeedback")
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-3-32).addEdge("humanFeedback","step3")
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-3-33).addEdge("step3",END);
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-3-34)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-3-35)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-3-36)// Set up memory
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-3-37)constmemory=newMemorySaver()
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-3-38)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-3-39)// Add 
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-3-40)constgraph=builder.compile({
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-3-41)checkpointer:memory,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-3-42)});

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-4-1)import*astslabfrom"tslab";
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-4-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-4-3)constdrawableGraph=graph.getGraph();
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-4-4)constimage=awaitdrawableGraph.drawMermaidPng();
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-4-5)constarrayBuffer=awaitimage.arrayBuffer();
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-4-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-4-7)awaittslab.display.png(newUint8Array(arrayBuffer));

```


![]()

Run until our breakpoint in the `humanFeedback` node:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-5-1)// Input
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-5-2)constinitialInput={input:"hello world"};
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-5-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-5-4)// Thread
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-5-5)constconfig={configurable:{thread_id:"1"}};
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-5-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-5-7)// Run the graph until the first interruption
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-5-8)forawait(consteventofawaitgraph.stream(initialInput,config)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-5-9)console.log(event);
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-5-10)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-5-11)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-5-12)// Will log when the graph is interrupted, after step 2.
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-5-13)console.log("--- GRAPH INTERRUPTED ---");

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-6-1)---Step 1---
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-6-2){}
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-6-3)--- humanFeedback ---
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-6-4){
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-6-5) __interrupt__: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-6-6)  {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-6-7)   value: 'Please provide feedback',
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-6-8)   when: 'during',
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-6-9)   resumable: true,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-6-10)   ns: [Array]
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-6-11)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-6-12) ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-6-13)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-6-14)--- GRAPH INTERRUPTED ---

```


Now, we can just manually update our graph state with with the user input - 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-7-1)import{Command}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-7-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-7-3)// Continue the graph execution
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-7-4)forawait(consteventofawaitgraph.stream(
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-7-5)newCommand({resume:"go to step 3! "}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-7-6)config,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-7-7))){
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-7-8)console.log(event);
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-7-9)console.log("\n====\n");
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-7-10)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-8-1)--- humanFeedback ---
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-8-2){ humanFeedback: { userFeedback: 'go to step 3! ' } }
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-8-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-8-4)====
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-8-5)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-8-6)---Step 3---
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-8-7){}
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-8-8)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-8-9)====

```


We can see our feedback was added to state - 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-9-1)(awaitgraph.getState(config)).values

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-10-1){ input: 'hello world', userFeedback: 'go to step 3! ' }

```


## Agent[¶](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#agent "Permanent link")

In the context of agents, waiting for user feedback is useful to ask clarifying questions.

To show this, we will build a relatively simple ReAct-style agent that does tool calling. 

We will use Anthropic's models and a mock tool (purely for demonstration purposes).

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-1)// Set up the tool
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-2)import{ChatAnthropic}from"@langchain/anthropic";
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-3)import{tool}from"@langchain/core/tools";
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-4)import{StateGraph,MessagesAnnotation,START,END,MemorySaver}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-5)import{ToolNode}from"@langchain/langgraph/prebuilt";
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-6)import{AIMessage,ToolMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-7)import{z}from"zod";
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-8)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-9)constsearch=tool((_)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-10)return"It's sunny in San Francisco, but you better look out if you're a Gemini 😈.";
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-11)},{
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-12)name:"search",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-13)description:"Call to surf the web.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-14)schema:z.string(),
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-15)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-16)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-17)consttools=[search]
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-18)consttoolNode=newToolNode<typeofMessagesAnnotation.State>(tools)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-19)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-20)// Set up the model
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-21)constmodel=newChatAnthropic({model:"claude-3-5-sonnet-20240620"})
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-22)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-23)constaskHumanTool=tool((_)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-24)return"The human said XYZ";
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-25)},{
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-26)name:"askHuman",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-27)description:"Ask the human for input.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-28)schema:z.string(),
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-29)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-30)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-31)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-32)constmodelWithTools=model.bindTools([...tools,askHumanTool])
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-33)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-34)// Define nodes and conditional edges
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-35)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-36)// Define the function that determines whether to continue or not
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-37)functionshouldContinue(state:typeofMessagesAnnotation.State):"action"|"askHuman"|typeofEND{
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-38)constlastMessage=state.messages[state.messages.length-1]asAIMessage;
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-39)// If there is no function call, then we finish
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-40)if(lastMessage&&!lastMessage.tool_calls?.length){
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-41)returnEND;
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-42)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-43)// If tool call is askHuman, we return that node
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-44)// You could also add logic here to let some system know that there's something that requires Human input
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-45)// For example, send a slack message, etc
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-46)if(lastMessage.tool_calls?.[0]?.name==="askHuman"){
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-47)console.log("--- ASKING HUMAN ---")
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-48)return"askHuman";
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-49)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-50)// Otherwise if it isn't, we continue with the action node
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-51)return"action";
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-52)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-53)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-54)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-55)// Define the function that calls the model
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-56)asyncfunctioncallModel(state:typeofMessagesAnnotation.State):Promise<Partial<typeofMessagesAnnotation.State>>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-57)constmessages=state.messages;
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-58)constresponse=awaitmodelWithTools.invoke(messages);
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-59)// We return an object with a messages property, because this will get added to the existing list
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-60)return{messages:[response]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-61)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-62)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-63)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-64)// We define a fake node to ask the human
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-65)functionaskHuman(state:typeofMessagesAnnotation.State):Partial<typeofMessagesAnnotation.State>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-66)constlastMessage=state.messages[state.messages.length-1]asAIMessage;
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-67)consttoolCallId=lastMessage.tool_calls?.[0].id;
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-68)constlocation:string=interrupt("Please provide your location:");
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-69)constnewToolMessage=newToolMessage({
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-70)tool_call_id:toolCallId!,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-71)content:location,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-72)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-73)return{messages:[newToolMessage]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-74)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-75)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-76)// Define a new graph
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-77)constmessagesWorkflow=newStateGraph(MessagesAnnotation)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-78)// Define the two nodes we will cycle between
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-79).addNode("agent",callModel)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-80).addNode("action",toolNode)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-81).addNode("askHuman",askHuman)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-82)// We now add a conditional edge
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-83).addConditionalEdges(
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-84)// First, we define the start node. We use `agent`.
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-85)// This means these are the edges taken after the `agent` node is called.
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-86)"agent",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-87)// Next, we pass in the function that will determine which node is called next.
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-88)shouldContinue
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-89))
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-90)// We now add a normal edge from `action` to `agent`.
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-91)// This means that after `action` is called, `agent` node is called next.
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-92).addEdge("action","agent")
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-93)// After we get back the human response, we go back to the agent
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-94).addEdge("askHuman","agent")
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-95)// Set the entrypoint as `agent`
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-96)// This means that this node is the first one called
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-97).addEdge(START,"agent");
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-98)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-99)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-100)// Setup memory
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-101)constmessagesMemory=newMemorySaver();
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-102)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-103)// Finally, we compile it!
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-104)// This compiles it into a LangChain Runnable,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-105)// meaning you can use it as you would any other runnable
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-106)constmessagesApp=messagesWorkflow.compile({
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-107)checkpointer:messagesMemory,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-11-108)});

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-12-1)import*astslabfrom"tslab";
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-12-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-12-3)constdrawableGraph2=messagesApp.getGraph();
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-12-4)constimage2=awaitdrawableGraph2.drawMermaidPng();
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-12-5)constarrayBuffer2=awaitimage2.arrayBuffer();
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-12-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-12-7)awaittslab.display.png(newUint8Array(arrayBuffer2));

```


![]()

## Interacting with the Agent[¶](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#interacting-with-the-agent "Permanent link")

We can now interact with the agent. Let's ask it to ask the user where they are, then tell them the weather. 

This should make it use the `askHuman` tool first, then use the normal tool. Note that we switch to use `streamMode: "values"` to just return the update messages at each point:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-13-1)// Input
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-13-2)constinput={
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-13-3)role:"user",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-13-4)content:"Use the search tool to ask the user where they are, then look up the weather there",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-13-5)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-13-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-13-7)// Thread
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-13-8)constconfig2={configurable:{thread_id:"3"},streamMode:"values"asconst};
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-13-9)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-13-10)forawait(consteventofawaitmessagesApp.stream({
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-13-11)messages:[input]
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-13-12)},config2)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-13-13)constrecentMsg=event.messages[event.messages.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-13-14)console.log(`================================ ${recentMsg.getType()} Message (1) =================================`)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-13-15)console.log(recentMsg.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-13-16)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-14-1)================================ human Message (1) =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-14-2)Use the search tool to ask the user where they are, then look up the weather there
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-14-3)--- ASKING HUMAN ---
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-14-4)================================ ai Message (1) =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-14-5)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-14-6) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-14-7)  type: 'text',
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-14-8)  text: "Certainly! I'll use the askHuman tool to ask the user about their location, and then use the search tool to look up the weather for that location. Let's start by asking the user where they are."
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-14-9) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-14-10) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-14-11)  type: 'tool_use',
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-14-12)  id: 'toolu_015UDVFoXcMV7KjRqPY78Umk',
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-14-13)  name: 'askHuman',
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-14-14)  input: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-14-15)   input: 'Where are you currently located? Please provide a city and country or region.'
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-14-16)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-14-17) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-14-18)]

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-15-1)console.log("next: ",(awaitmessagesApp.getState(config2)).next)

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-16-1)next: [ 'askHuman' ]

```


You can see that our graph got interrupted inside the `askHuman` node, which is now waiting for a `location` to be provided. We can provide this value by invoking the graph with a `new Command({ resume: "<location>" })` input: 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-17-1)import{Command}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-17-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-17-3)// Continue the graph execution
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-17-4)forawait(consteventofawaitmessagesApp.stream(
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-17-5)newCommand({resume:"San Francisco"}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-17-6)config2,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-17-7))){
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-17-8)console.log(event);
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-17-9)console.log("\n====\n");
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-17-10)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-1){
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-2) messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-3)  HumanMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-4)   "id": "cfb461cb-0da1-48b4-acef-e3bf0d3a4e6c",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-5)   "content": "Use the search tool to ask the user where they are, then look up the weather there",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-6)   "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-7)   "response_metadata": {}
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-8)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-9)  AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-10)   "id": "msg_01TA2zHbbrenm7KXSUdcFdXD",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-11)   "content": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-12)    {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-13)     "type": "text",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-14)     "text": "Certainly! I'll use the askHuman tool to ask the user about their location, and then use the search tool to look up the weather for that location. Let's start by asking the user where they are."
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-15)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-16)    {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-17)     "type": "tool_use",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-18)     "id": "toolu_015UDVFoXcMV7KjRqPY78Umk",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-19)     "name": "askHuman",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-20)     "input": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-21)      "input": "Where are you currently located? Please provide a city and country or region."
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-22)     }
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-23)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-24)   ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-25)   "additional_kwargs": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-26)    "id": "msg_01TA2zHbbrenm7KXSUdcFdXD",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-27)    "type": "message",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-28)    "role": "assistant",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-29)    "model": "claude-3-5-sonnet-20240620",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-30)    "stop_reason": "tool_use",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-31)    "stop_sequence": null,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-32)    "usage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-33)     "input_tokens": 465,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-34)     "cache_creation_input_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-35)     "cache_read_input_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-36)     "output_tokens": 112
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-37)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-38)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-39)   "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-40)    "id": "msg_01TA2zHbbrenm7KXSUdcFdXD",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-41)    "model": "claude-3-5-sonnet-20240620",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-42)    "stop_reason": "tool_use",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-43)    "stop_sequence": null,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-44)    "usage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-45)     "input_tokens": 465,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-46)     "cache_creation_input_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-47)     "cache_read_input_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-48)     "output_tokens": 112
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-49)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-50)    "type": "message",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-51)    "role": "assistant"
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-52)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-53)   "tool_calls": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-54)    {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-55)     "name": "askHuman",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-56)     "args": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-57)      "input": "Where are you currently located? Please provide a city and country or region."
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-58)     },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-59)     "id": "toolu_015UDVFoXcMV7KjRqPY78Umk",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-60)     "type": "tool_call"
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-61)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-62)   ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-63)   "invalid_tool_calls": []
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-64)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-65) ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-66)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-67)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-68)====
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-69)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-70){
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-71) messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-72)  HumanMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-73)   "id": "cfb461cb-0da1-48b4-acef-e3bf0d3a4e6c",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-74)   "content": "Use the search tool to ask the user where they are, then look up the weather there",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-75)   "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-76)   "response_metadata": {}
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-77)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-78)  AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-79)   "id": "msg_01TA2zHbbrenm7KXSUdcFdXD",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-80)   "content": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-81)    {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-82)     "type": "text",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-83)     "text": "Certainly! I'll use the askHuman tool to ask the user about their location, and then use the search tool to look up the weather for that location. Let's start by asking the user where they are."
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-84)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-85)    {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-86)     "type": "tool_use",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-87)     "id": "toolu_015UDVFoXcMV7KjRqPY78Umk",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-88)     "name": "askHuman",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-89)     "input": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-90)      "input": "Where are you currently located? Please provide a city and country or region."
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-91)     }
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-92)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-93)   ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-94)   "additional_kwargs": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-95)    "id": "msg_01TA2zHbbrenm7KXSUdcFdXD",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-96)    "type": "message",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-97)    "role": "assistant",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-98)    "model": "claude-3-5-sonnet-20240620",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-99)    "stop_reason": "tool_use",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-100)    "stop_sequence": null,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-101)    "usage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-102)     "input_tokens": 465,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-103)     "cache_creation_input_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-104)     "cache_read_input_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-105)     "output_tokens": 112
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-106)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-107)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-108)   "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-109)    "id": "msg_01TA2zHbbrenm7KXSUdcFdXD",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-110)    "model": "claude-3-5-sonnet-20240620",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-111)    "stop_reason": "tool_use",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-112)    "stop_sequence": null,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-113)    "usage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-114)     "input_tokens": 465,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-115)     "cache_creation_input_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-116)     "cache_read_input_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-117)     "output_tokens": 112
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-118)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-119)    "type": "message",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-120)    "role": "assistant"
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-121)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-122)   "tool_calls": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-123)    {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-124)     "name": "askHuman",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-125)     "args": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-126)      "input": "Where are you currently located? Please provide a city and country or region."
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-127)     },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-128)     "id": "toolu_015UDVFoXcMV7KjRqPY78Umk",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-129)     "type": "tool_call"
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-130)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-131)   ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-132)   "invalid_tool_calls": []
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-133)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-134)  ToolMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-135)   "id": "0225d971-1756-468e-996d-9af93e608a95",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-136)   "content": "San Francisco",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-137)   "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-138)   "response_metadata": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-139)   "tool_call_id": "toolu_015UDVFoXcMV7KjRqPY78Umk"
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-140)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-141) ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-142)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-143)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-144)====
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-145)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-146){
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-147) messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-148)  HumanMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-149)   "id": "cfb461cb-0da1-48b4-acef-e3bf0d3a4e6c",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-150)   "content": "Use the search tool to ask the user where they are, then look up the weather there",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-151)   "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-152)   "response_metadata": {}
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-153)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-154)  AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-155)   "id": "msg_01TA2zHbbrenm7KXSUdcFdXD",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-156)   "content": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-157)    {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-158)     "type": "text",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-159)     "text": "Certainly! I'll use the askHuman tool to ask the user about their location, and then use the search tool to look up the weather for that location. Let's start by asking the user where they are."
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-160)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-161)    {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-162)     "type": "tool_use",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-163)     "id": "toolu_015UDVFoXcMV7KjRqPY78Umk",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-164)     "name": "askHuman",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-165)     "input": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-166)      "input": "Where are you currently located? Please provide a city and country or region."
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-167)     }
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-168)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-169)   ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-170)   "additional_kwargs": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-171)    "id": "msg_01TA2zHbbrenm7KXSUdcFdXD",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-172)    "type": "message",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-173)    "role": "assistant",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-174)    "model": "claude-3-5-sonnet-20240620",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-175)    "stop_reason": "tool_use",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-176)    "stop_sequence": null,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-177)    "usage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-178)     "input_tokens": 465,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-179)     "cache_creation_input_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-180)     "cache_read_input_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-181)     "output_tokens": 112
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-182)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-183)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-184)   "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-185)    "id": "msg_01TA2zHbbrenm7KXSUdcFdXD",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-186)    "model": "claude-3-5-sonnet-20240620",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-187)    "stop_reason": "tool_use",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-188)    "stop_sequence": null,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-189)    "usage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-190)     "input_tokens": 465,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-191)     "cache_creation_input_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-192)     "cache_read_input_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-193)     "output_tokens": 112
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-194)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-195)    "type": "message",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-196)    "role": "assistant"
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-197)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-198)   "tool_calls": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-199)    {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-200)     "name": "askHuman",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-201)     "args": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-202)      "input": "Where are you currently located? Please provide a city and country or region."
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-203)     },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-204)     "id": "toolu_015UDVFoXcMV7KjRqPY78Umk",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-205)     "type": "tool_call"
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-206)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-207)   ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-208)   "invalid_tool_calls": []
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-209)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-210)  ToolMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-211)   "id": "0225d971-1756-468e-996d-9af93e608a95",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-212)   "content": "San Francisco",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-213)   "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-214)   "response_metadata": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-215)   "tool_call_id": "toolu_015UDVFoXcMV7KjRqPY78Umk"
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-216)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-217)  AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-218)   "id": "msg_01QDw6TTXvFXKPEX4mYjzU8Y",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-219)   "content": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-220)    {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-221)     "type": "text",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-222)     "text": "Thank you for providing your location. Now, I'll use the search tool to look up the weather in San Francisco."
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-223)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-224)    {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-225)     "type": "tool_use",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-226)     "id": "toolu_01AzffiwYncLArNb9SbKHK2a",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-227)     "name": "search",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-228)     "input": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-229)      "input": "current weather in San Francisco"
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-230)     }
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-231)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-232)   ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-233)   "additional_kwargs": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-234)    "id": "msg_01QDw6TTXvFXKPEX4mYjzU8Y",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-235)    "type": "message",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-236)    "role": "assistant",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-237)    "model": "claude-3-5-sonnet-20240620",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-238)    "stop_reason": "tool_use",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-239)    "stop_sequence": null,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-240)    "usage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-241)     "input_tokens": 590,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-242)     "cache_creation_input_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-243)     "cache_read_input_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-244)     "output_tokens": 81
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-245)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-246)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-247)   "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-248)    "id": "msg_01QDw6TTXvFXKPEX4mYjzU8Y",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-249)    "model": "claude-3-5-sonnet-20240620",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-250)    "stop_reason": "tool_use",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-251)    "stop_sequence": null,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-252)    "usage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-253)     "input_tokens": 590,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-254)     "cache_creation_input_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-255)     "cache_read_input_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-256)     "output_tokens": 81
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-257)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-258)    "type": "message",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-259)    "role": "assistant"
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-260)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-261)   "tool_calls": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-262)    {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-263)     "name": "search",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-264)     "args": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-265)      "input": "current weather in San Francisco"
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-266)     },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-267)     "id": "toolu_01AzffiwYncLArNb9SbKHK2a",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-268)     "type": "tool_call"
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-269)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-270)   ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-271)   "invalid_tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-272)   "usage_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-273)    "input_tokens": 590,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-274)    "output_tokens": 81,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-275)    "total_tokens": 671
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-276)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-277)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-278) ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-279)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-280)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-281)====
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-282)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-283){
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-284) messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-285)  HumanMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-286)   "id": "cfb461cb-0da1-48b4-acef-e3bf0d3a4e6c",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-287)   "content": "Use the search tool to ask the user where they are, then look up the weather there",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-288)   "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-289)   "response_metadata": {}
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-290)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-291)  AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-292)   "id": "msg_01TA2zHbbrenm7KXSUdcFdXD",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-293)   "content": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-294)    {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-295)     "type": "text",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-296)     "text": "Certainly! I'll use the askHuman tool to ask the user about their location, and then use the search tool to look up the weather for that location. Let's start by asking the user where they are."
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-297)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-298)    {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-299)     "type": "tool_use",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-300)     "id": "toolu_015UDVFoXcMV7KjRqPY78Umk",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-301)     "name": "askHuman",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-302)     "input": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-303)      "input": "Where are you currently located? Please provide a city and country or region."
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-304)     }
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-305)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-306)   ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-307)   "additional_kwargs": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-308)    "id": "msg_01TA2zHbbrenm7KXSUdcFdXD",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-309)    "type": "message",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-310)    "role": "assistant",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-311)    "model": "claude-3-5-sonnet-20240620",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-312)    "stop_reason": "tool_use",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-313)    "stop_sequence": null,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-314)    "usage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-315)     "input_tokens": 465,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-316)     "cache_creation_input_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-317)     "cache_read_input_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-318)     "output_tokens": 112
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-319)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-320)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-321)   "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-322)    "id": "msg_01TA2zHbbrenm7KXSUdcFdXD",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-323)    "model": "claude-3-5-sonnet-20240620",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-324)    "stop_reason": "tool_use",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-325)    "stop_sequence": null,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-326)    "usage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-327)     "input_tokens": 465,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-328)     "cache_creation_input_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-329)     "cache_read_input_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-330)     "output_tokens": 112
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-331)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-332)    "type": "message",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-333)    "role": "assistant"
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-334)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-335)   "tool_calls": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-336)    {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-337)     "name": "askHuman",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-338)     "args": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-339)      "input": "Where are you currently located? Please provide a city and country or region."
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-340)     },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-341)     "id": "toolu_015UDVFoXcMV7KjRqPY78Umk",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-342)     "type": "tool_call"
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-343)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-344)   ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-345)   "invalid_tool_calls": []
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-346)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-347)  ToolMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-348)   "id": "0225d971-1756-468e-996d-9af93e608a95",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-349)   "content": "San Francisco",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-350)   "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-351)   "response_metadata": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-352)   "tool_call_id": "toolu_015UDVFoXcMV7KjRqPY78Umk"
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-353)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-354)  AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-355)   "id": "msg_01QDw6TTXvFXKPEX4mYjzU8Y",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-356)   "content": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-357)    {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-358)     "type": "text",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-359)     "text": "Thank you for providing your location. Now, I'll use the search tool to look up the weather in San Francisco."
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-360)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-361)    {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-362)     "type": "tool_use",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-363)     "id": "toolu_01AzffiwYncLArNb9SbKHK2a",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-364)     "name": "search",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-365)     "input": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-366)      "input": "current weather in San Francisco"
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-367)     }
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-368)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-369)   ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-370)   "additional_kwargs": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-371)    "id": "msg_01QDw6TTXvFXKPEX4mYjzU8Y",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-372)    "type": "message",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-373)    "role": "assistant",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-374)    "model": "claude-3-5-sonnet-20240620",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-375)    "stop_reason": "tool_use",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-376)    "stop_sequence": null,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-377)    "usage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-378)     "input_tokens": 590,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-379)     "cache_creation_input_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-380)     "cache_read_input_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-381)     "output_tokens": 81
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-382)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-383)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-384)   "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-385)    "id": "msg_01QDw6TTXvFXKPEX4mYjzU8Y",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-386)    "model": "claude-3-5-sonnet-20240620",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-387)    "stop_reason": "tool_use",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-388)    "stop_sequence": null,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-389)    "usage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-390)     "input_tokens": 590,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-391)     "cache_creation_input_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-392)     "cache_read_input_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-393)     "output_tokens": 81
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-394)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-395)    "type": "message",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-396)    "role": "assistant"
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-397)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-398)   "tool_calls": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-399)    {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-400)     "name": "search",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-401)     "args": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-402)      "input": "current weather in San Francisco"
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-403)     },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-404)     "id": "toolu_01AzffiwYncLArNb9SbKHK2a",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-405)     "type": "tool_call"
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-406)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-407)   ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-408)   "invalid_tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-409)   "usage_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-410)    "input_tokens": 590,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-411)    "output_tokens": 81,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-412)    "total_tokens": 671
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-413)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-414)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-415)  ToolMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-416)   "id": "1c52e9b5-1d0b-4889-abd0-10572053e1d8",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-417)   "content": "It's sunny in San Francisco, but you better look out if you're a Gemini 😈.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-418)   "name": "search",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-419)   "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-420)   "response_metadata": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-421)   "tool_call_id": "toolu_01AzffiwYncLArNb9SbKHK2a"
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-422)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-423) ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-424)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-425)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-426)====
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-427)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-428){
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-429) messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-430)  HumanMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-431)   "id": "cfb461cb-0da1-48b4-acef-e3bf0d3a4e6c",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-432)   "content": "Use the search tool to ask the user where they are, then look up the weather there",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-433)   "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-434)   "response_metadata": {}
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-435)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-436)  AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-437)   "id": "msg_01TA2zHbbrenm7KXSUdcFdXD",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-438)   "content": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-439)    {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-440)     "type": "text",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-441)     "text": "Certainly! I'll use the askHuman tool to ask the user about their location, and then use the search tool to look up the weather for that location. Let's start by asking the user where they are."
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-442)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-443)    {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-444)     "type": "tool_use",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-445)     "id": "toolu_015UDVFoXcMV7KjRqPY78Umk",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-446)     "name": "askHuman",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-447)     "input": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-448)      "input": "Where are you currently located? Please provide a city and country or region."
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-449)     }
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-450)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-451)   ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-452)   "additional_kwargs": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-453)    "id": "msg_01TA2zHbbrenm7KXSUdcFdXD",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-454)    "type": "message",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-455)    "role": "assistant",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-456)    "model": "claude-3-5-sonnet-20240620",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-457)    "stop_reason": "tool_use",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-458)    "stop_sequence": null,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-459)    "usage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-460)     "input_tokens": 465,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-461)     "cache_creation_input_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-462)     "cache_read_input_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-463)     "output_tokens": 112
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-464)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-465)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-466)   "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-467)    "id": "msg_01TA2zHbbrenm7KXSUdcFdXD",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-468)    "model": "claude-3-5-sonnet-20240620",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-469)    "stop_reason": "tool_use",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-470)    "stop_sequence": null,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-471)    "usage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-472)     "input_tokens": 465,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-473)     "cache_creation_input_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-474)     "cache_read_input_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-475)     "output_tokens": 112
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-476)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-477)    "type": "message",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-478)    "role": "assistant"
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-479)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-480)   "tool_calls": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-481)    {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-482)     "name": "askHuman",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-483)     "args": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-484)      "input": "Where are you currently located? Please provide a city and country or region."
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-485)     },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-486)     "id": "toolu_015UDVFoXcMV7KjRqPY78Umk",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-487)     "type": "tool_call"
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-488)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-489)   ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-490)   "invalid_tool_calls": []
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-491)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-492)  ToolMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-493)   "id": "0225d971-1756-468e-996d-9af93e608a95",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-494)   "content": "San Francisco",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-495)   "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-496)   "response_metadata": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-497)   "tool_call_id": "toolu_015UDVFoXcMV7KjRqPY78Umk"
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-498)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-499)  AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-500)   "id": "msg_01QDw6TTXvFXKPEX4mYjzU8Y",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-501)   "content": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-502)    {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-503)     "type": "text",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-504)     "text": "Thank you for providing your location. Now, I'll use the search tool to look up the weather in San Francisco."
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-505)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-506)    {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-507)     "type": "tool_use",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-508)     "id": "toolu_01AzffiwYncLArNb9SbKHK2a",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-509)     "name": "search",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-510)     "input": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-511)      "input": "current weather in San Francisco"
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-512)     }
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-513)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-514)   ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-515)   "additional_kwargs": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-516)    "id": "msg_01QDw6TTXvFXKPEX4mYjzU8Y",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-517)    "type": "message",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-518)    "role": "assistant",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-519)    "model": "claude-3-5-sonnet-20240620",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-520)    "stop_reason": "tool_use",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-521)    "stop_sequence": null,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-522)    "usage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-523)     "input_tokens": 590,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-524)     "cache_creation_input_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-525)     "cache_read_input_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-526)     "output_tokens": 81
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-527)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-528)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-529)   "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-530)    "id": "msg_01QDw6TTXvFXKPEX4mYjzU8Y",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-531)    "model": "claude-3-5-sonnet-20240620",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-532)    "stop_reason": "tool_use",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-533)    "stop_sequence": null,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-534)    "usage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-535)     "input_tokens": 590,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-536)     "cache_creation_input_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-537)     "cache_read_input_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-538)     "output_tokens": 81
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-539)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-540)    "type": "message",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-541)    "role": "assistant"
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-542)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-543)   "tool_calls": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-544)    {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-545)     "name": "search",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-546)     "args": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-547)      "input": "current weather in San Francisco"
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-548)     },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-549)     "id": "toolu_01AzffiwYncLArNb9SbKHK2a",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-550)     "type": "tool_call"
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-551)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-552)   ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-553)   "invalid_tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-554)   "usage_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-555)    "input_tokens": 590,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-556)    "output_tokens": 81,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-557)    "total_tokens": 671
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-558)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-559)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-560)  ToolMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-561)   "id": "1c52e9b5-1d0b-4889-abd0-10572053e1d8",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-562)   "content": "It's sunny in San Francisco, but you better look out if you're a Gemini 😈.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-563)   "name": "search",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-564)   "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-565)   "response_metadata": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-566)   "tool_call_id": "toolu_01AzffiwYncLArNb9SbKHK2a"
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-567)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-568)  AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-569)   "id": "msg_01UAbWbZ9RVV3L6ABgQWsy9f",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-570)   "content": "Based on the search results, I can provide you with information about the current weather in San Francisco:\n\nThe weather in San Francisco is currently sunny. This is great news for outdoor activities and enjoying the city's many attractions.\n\nHowever, I should note that the search result included an unusual comment about Geminis. This appears to be unrelated to the weather and might be a joke or reference included in the search results. It's not typical for weather reports to include astrological information, so I'd recommend focusing on the factual weather information provided.\n\nIs there anything else you'd like to know about the weather in San Francisco or any other information you need?",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-571)   "additional_kwargs": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-572)    "id": "msg_01UAbWbZ9RVV3L6ABgQWsy9f",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-573)    "type": "message",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-574)    "role": "assistant",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-575)    "model": "claude-3-5-sonnet-20240620",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-576)    "stop_reason": "end_turn",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-577)    "stop_sequence": null,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-578)    "usage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-579)     "input_tokens": 704,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-580)     "cache_creation_input_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-581)     "cache_read_input_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-582)     "output_tokens": 140
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-583)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-584)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-585)   "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-586)    "id": "msg_01UAbWbZ9RVV3L6ABgQWsy9f",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-587)    "model": "claude-3-5-sonnet-20240620",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-588)    "stop_reason": "end_turn",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-589)    "stop_sequence": null,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-590)    "usage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-591)     "input_tokens": 704,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-592)     "cache_creation_input_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-593)     "cache_read_input_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-594)     "output_tokens": 140
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-595)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-596)    "type": "message",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-597)    "role": "assistant"
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-598)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-599)   "tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-600)   "invalid_tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-601)   "usage_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-602)    "input_tokens": 704,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-603)    "output_tokens": 140,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-604)    "total_tokens": 844
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-605)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-606)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-607) ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-608)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-609)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__codelineno-18-610)====

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to edit graph state  ](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/) [ Next  How to wait for user input (Functional API)  ](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
