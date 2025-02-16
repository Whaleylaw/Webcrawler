---
url: https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#how-to-edit-graph-state)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to edit graph state 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/?q= "Share")

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
            * How to edit graph state  [ How to edit graph state  ](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#setup)
              * [ Simple Usage  ](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#simple-usage)
              * [ Agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#agent)
              * [ Interacting with the Agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#interacting-with-the-agent)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#setup)
  * [ Simple Usage  ](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#simple-usage)
  * [ Agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#agent)
  * [ Interacting with the Agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#interacting-with-the-agent)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
  5. [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraphjs/how-tos#human-in-the-loop)



# How to edit graph state[¶](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#how-to-edit-graph-state "Permanent link")

Prerequisites

  * [Human-in-the-loop](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop)
  * [Breakpoints](https://langchain-ai.github.io/langgraphjs/concepts/breakpoints)
  * [LangGraph Glossary](https://langchain-ai.github.io/langgraphjs/concepts/low_level)



Human-in-the-loop (HIL) interactions are crucial for [agentic systems](https://langchain-ai.github.io/langgraphjs/concepts/agentic_concepts/#human-in-the-loop). Manually updating the graph state a common HIL interaction pattern, allowing the human to edit actions (e.g., what tool is being called or how it is being called).

We can implement this in LangGraph using a [breakpoint](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/): breakpoints allow us to interrupt graph execution before a specific step. At this breakpoint, we can manually update the graph state and then resume from that spot to continue. 

![image.png]()

## Setup[¶](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#setup "Permanent link")

First we need to install the packages required

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-0-1)npminstall@langchain/langgraph@langchain/anthropic@langchain/corezod

```


Next, we need to set API keys for Anthropic (the LLM we will use)

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-1-1)exportANTHROPIC_API_KEY=your-api-key

```


Optionally, we can set API key for LangSmith tracing, which will give us best-in-class observability.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-2-1)exportLANGCHAIN_TRACING_V2="true"
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-2-2)exportLANGCHAIN_CALLBACKS_BACKGROUND="true"
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-2-3)exportLANGCHAIN_API_KEY=your-api-key

```


## Simple Usage[¶](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#simple-usage "Permanent link")

Let's look at very basic usage of this.

Below, we do two things:

1) We specify the [breakpoint](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#breakpoints) using `interruptBefore` a specified step (node).

2) We set up a [checkpointer](https://langchain-ai.github.io/langgraphjs/concepts/#checkpoints) to save the state of the graph up until this node.

3) We use `.updateState` to update the state of the graph.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-3-1)import{StateGraph,START,END,Annotation}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-3-2)import{MemorySaver}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-3-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-3-4)constGraphState=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-3-5)input:Annotation<string>
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-3-6)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-3-7)
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-3-8)conststep1=(state:typeofGraphState.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-3-9)console.log("---Step 1---");
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-3-10)returnstate;
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-3-11)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-3-12)
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-3-13)conststep2=(state:typeofGraphState.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-3-14)console.log("---Step 2---");
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-3-15)returnstate;
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-3-16)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-3-17)
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-3-18)conststep3=(state:typeofGraphState.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-3-19)console.log("---Step 3---");
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-3-20)returnstate;
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-3-21)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-3-22)
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-3-23)
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-3-24)constbuilder=newStateGraph(GraphState)
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-3-25).addNode("step1",step1)
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-3-26).addNode("step2",step2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-3-27).addNode("step3",step3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-3-28).addEdge(START,"step1")
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-3-29).addEdge("step1","step2")
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-3-30).addEdge("step2","step3")
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-3-31).addEdge("step3",END);
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-3-32)
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-3-33)
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-3-34)// Set up memory
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-3-35)constgraphStateMemory=newMemorySaver()
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-3-36)
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-3-37)constgraph=builder.compile({
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-3-38)checkpointer:graphStateMemory,
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-3-39)interruptBefore:["step2"]
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-3-40)});

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-4-1)import*astslabfrom"tslab";
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-4-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-4-3)constdrawableGraphGraphState=graph.getGraph();
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-4-4)constgraphStateImage=awaitdrawableGraphGraphState.drawMermaidPng();
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-4-5)constgraphStateArrayBuffer=awaitgraphStateImage.arrayBuffer();
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-4-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-4-7)awaittslab.display.png(newUint8Array(graphStateArrayBuffer));

```


![]()

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-5-1)// Input
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-5-2)constinitialInput={input:"hello world"};
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-5-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-5-4)// Thread
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-5-5)constgraphStateConfig={configurable:{thread_id:"1"},streamMode:"values"asconst};
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-5-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-5-7)// Run the graph until the first interruption
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-5-8)forawait(consteventofawaitgraph.stream(initialInput,graphStateConfig)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-5-9)console.log(`--- ${event.input} ---`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-5-10)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-5-11)
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-5-12)// Will log when the graph is interrupted, after step 2.
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-5-13)console.log("--- GRAPH INTERRUPTED ---");

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-6-1)--- hello world ---
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-6-2)---Step 1---
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-6-3)--- hello world ---
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-6-4)--- GRAPH INTERRUPTED ---

```


Now, we can just manually update our graph state - 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-7-1)console.log("Current state!")
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-7-2)constcurrState=awaitgraph.getState(graphStateConfig);
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-7-3)console.log(currState.values)
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-7-4)
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-7-5)awaitgraph.updateState(graphStateConfig,{input:"hello universe!"})
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-7-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-7-7)console.log("---\n---\nUpdated state!")
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-7-8)constupdatedState=awaitgraph.getState(graphStateConfig);
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-7-9)console.log(updatedState.values)

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-8-1)Current state!
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-8-2){ input: 'hello world' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-8-3)---
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-8-4)---
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-8-5)Updated state!
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-8-6){ input: 'hello universe!' }

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-9-1)// Continue the graph execution
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-9-2)forawait(consteventofawaitgraph.stream(null,graphStateConfig)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-9-3)console.log(`--- ${event.input} ---`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-9-4)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-10-1)---Step 2---
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-10-2)--- hello universe! ---
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-10-3)---Step 3---
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-10-4)--- hello universe! ---

```


## Agent[¶](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#agent "Permanent link")

In the context of agents, updating state is useful for things like editing tool calls.

To show this, we will build a relatively simple ReAct-style agent that does tool calling. 

We will use Anthropic's models and a fake tool (just for demo purposes).

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-1)// Set up the tool
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-2)import{ChatAnthropic}from"@langchain/anthropic";
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-3)import{tool}from"@langchain/core/tools";
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-4)import{StateGraph,START,END,MessagesAnnotation}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-5)import{MemorySaver}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-6)import{ToolNode}from"@langchain/langgraph/prebuilt";
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-7)import{AIMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-8)import{z}from"zod";
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-9)
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-10)constsearch=tool((_)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-11)return"It's sunny in San Francisco, but you better look out if you're a Gemini 😈.";
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-12)},{
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-13)name:"search",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-14)description:"Call to surf the web.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-15)schema:z.string(),
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-16)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-17)
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-18)consttools=[search]
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-19)consttoolNode=newToolNode(tools)
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-20)
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-21)// Set up the model
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-22)constmodel=newChatAnthropic({model:"claude-3-5-sonnet-20240620"})
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-23)constmodelWithTools=model.bindTools(tools)
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-24)
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-25)
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-26)// Define nodes and conditional edges
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-27)
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-28)// Define the function that determines whether to continue or not
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-29)functionshouldContinue(state:typeofMessagesAnnotation.State):"action"|typeofEND{
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-30)constlastMessage=state.messages[state.messages.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-31)// If there is no function call, then we finish
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-32)if(lastMessage&&!(lastMessageasAIMessage).tool_calls?.length){
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-33)returnEND;
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-34)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-35)// Otherwise if there is, we continue
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-36)return"action";
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-37)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-38)
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-39)// Define the function that calls the model
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-40)asyncfunctioncallModel(state:typeofMessagesAnnotation.State):Promise<Partial<typeofMessagesAnnotation.State>>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-41)constmessages=state.messages;
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-42)constresponse=awaitmodelWithTools.invoke(messages);
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-43)// We return an object with a messages property, because this will get added to the existing list
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-44)return{messages:[response]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-45)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-46)
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-47)// Define a new graph
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-48)constworkflow=newStateGraph(MessagesAnnotation)
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-49)// Define the two nodes we will cycle between
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-50).addNode("agent",callModel)
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-51).addNode("action",toolNode)
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-52)// We now add a conditional edge
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-53).addConditionalEdges(
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-54)// First, we define the start node. We use `agent`.
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-55)// This means these are the edges taken after the `agent` node is called.
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-56)"agent",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-57)// Next, we pass in the function that will determine which node is called next.
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-58)shouldContinue
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-59))
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-60)// We now add a normal edge from `action` to `agent`.
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-61)// This means that after `action` is called, `agent` node is called next.
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-62).addEdge("action","agent")
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-63)// Set the entrypoint as `agent`
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-64)// This means that this node is the first one called
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-65).addEdge(START,"agent");
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-66)
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-67)// Setup memory
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-68)constmemory=newMemorySaver();
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-69)
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-70)// Finally, we compile it!
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-71)// This compiles it into a LangChain Runnable,
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-72)// meaning you can use it as you would any other runnable
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-73)constapp=workflow.compile({
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-74)checkpointer:memory,
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-75)interruptBefore:["action"]
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-11-76)});

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-12-1)import*astslabfrom"tslab";
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-12-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-12-3)constdrawableGraph=app.getGraph();
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-12-4)constimage=awaitdrawableGraph.drawMermaidPng();
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-12-5)constarrayBuffer=awaitimage.arrayBuffer();
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-12-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-12-7)awaittslab.display.png(newUint8Array(arrayBuffer));

```


![]()

## Interacting with the Agent[¶](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#interacting-with-the-agent "Permanent link")

We can now interact with the agent and see that it stops before calling a tool.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-13-1)// Thread
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-13-2)constconfig={configurable:{thread_id:"3"},streamMode:"values"asconst};
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-13-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-13-4)forawait(consteventofawaitapp.stream({
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-13-5)messages:[{role:"human",content:"search for the weather in sf now"}]
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-13-6)},config)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-13-7)constrecentMsg=event.messages[event.messages.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-13-8)console.log(`================================ ${recentMsg._getType()} Message (1) =================================`)
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-13-9)console.log(recentMsg.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-13-10)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-14-1)================================ human Message (1) =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-14-2)search for the weather in sf now
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-14-3)================================ ai Message (1) =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-14-4)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-14-5) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-14-6)  type: 'text',
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-14-7)  text: 'Certainly! I can help you search for the current weather in San Francisco. Let me use the search function to find that information for you.'
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-14-8) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-14-9) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-14-10)  type: 'tool_use',
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-14-11)  id: 'toolu_0141zTpknasyWkrjTV6eKeT6',
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-14-12)  name: 'search',
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-14-13)  input: { input: 'current weather in San Francisco' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-14-14) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-14-15)]

```


**Edit**

We can now update the state accordingly. Let's modify the tool call to have the query `"current weather in SF"`.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-15-1)// First, lets get the current state
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-15-2)constcurrentState=awaitapp.getState(config);
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-15-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-15-4)// Let's now get the last message in the state
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-15-5)// This is the one with the tool calls that we want to update
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-15-6)letlastMessage=currentState.values.messages[currentState.values.messages.length-1]
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-15-7)
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-15-8)// Let's now update the args for that tool call
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-15-9)lastMessage.tool_calls[0].args={query:"current weather in SF"}
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-15-10)
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-15-11)// Let's now call `updateState` to pass in this message in the `messages` key
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-15-12)// This will get treated as any other update to the state
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-15-13)// It will get passed to the reducer function for the `messages` key
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-15-14)// That reducer function will use the ID of the message to update it
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-15-15)// It's important that it has the right ID! Otherwise it would get appended
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-15-16)// as a new message
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-15-17)awaitapp.updateState(config,{messages:lastMessage});

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-16-1){
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-16-2) configurable: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-16-3)  thread_id: '3',
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-16-4)  checkpoint_id: '1ef5e785-4298-6b71-8002-4a6ceca964db'
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-16-5) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-16-6)}

```


Let's now check the current state of the app to make sure it got updated accordingly 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-17-1)constnewState=awaitapp.getState(config);
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-17-2)constupdatedStateToolCalls=newState.values.messages[newState.values.messages.length-1].tool_calls
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-17-3)console.log(updatedStateToolCalls)

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-18-1)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-18-2) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-18-3)  name: 'search',
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-18-4)  args: { query: 'current weather in SF' },
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-18-5)  id: 'toolu_0141zTpknasyWkrjTV6eKeT6',
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-18-6)  type: 'tool_call'
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-18-7) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-18-8)]

```


**Resume**

We can now call the agent again with no inputs to continue, ie. run the tool as requested. We can see from the logs that it passes in the update args to the tool.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-19-1)forawait(consteventofawaitapp.stream(null,config)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-19-2)console.log(event)
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-19-3)constrecentMsg=event.messages[event.messages.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-19-4)console.log(`================================ ${recentMsg._getType()} Message (1) =================================`)
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-19-5)if(recentMsg._getType()==="tool"){
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-19-6)console.log({
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-19-7)name:recentMsg.name,
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-19-8)content:recentMsg.content
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-19-9)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-19-10)}elseif(recentMsg._getType()==="ai"){
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-19-11)console.log(recentMsg.content)
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-19-12)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-19-13)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-1){
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-2) messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-3)  HumanMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-4)   "id": "7c69c1f3-914b-4236-b2ca-ef250e72cb7a",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-5)   "content": "search for the weather in sf now",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-6)   "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-7)   "response_metadata": {}
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-8)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-9)  AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-10)   "id": "msg_0152mx7AweoRWa67HFsfyaif",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-11)   "content": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-12)    {
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-13)     "type": "text",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-14)     "text": "Certainly! I can help you search for the current weather in San Francisco. Let me use the search function to find that information for you."
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-15)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-16)    {
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-17)     "type": "tool_use",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-18)     "id": "toolu_0141zTpknasyWkrjTV6eKeT6",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-19)     "name": "search",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-20)     "input": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-21)      "input": "current weather in San Francisco"
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-22)     }
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-23)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-24)   ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-25)   "additional_kwargs": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-26)    "id": "msg_0152mx7AweoRWa67HFsfyaif",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-27)    "type": "message",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-28)    "role": "assistant",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-29)    "model": "claude-3-5-sonnet-20240620",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-30)    "stop_reason": "tool_use",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-31)    "stop_sequence": null,
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-32)    "usage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-33)     "input_tokens": 380,
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-34)     "output_tokens": 84
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-35)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-36)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-37)   "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-38)    "id": "msg_0152mx7AweoRWa67HFsfyaif",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-39)    "model": "claude-3-5-sonnet-20240620",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-40)    "stop_reason": "tool_use",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-41)    "stop_sequence": null,
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-42)    "usage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-43)     "input_tokens": 380,
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-44)     "output_tokens": 84
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-45)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-46)    "type": "message",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-47)    "role": "assistant"
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-48)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-49)   "tool_calls": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-50)    {
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-51)     "name": "search",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-52)     "args": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-53)      "query": "current weather in SF"
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-54)     },
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-55)     "id": "toolu_0141zTpknasyWkrjTV6eKeT6",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-56)     "type": "tool_call"
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-57)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-58)   ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-59)   "invalid_tool_calls": []
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-60)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-61)  ToolMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-62)   "id": "ccf0d56f-477f-408a-b809-6900a48379e0",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-63)   "content": "It's sunny in San Francisco, but you better look out if you're a Gemini 😈.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-64)   "name": "search",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-65)   "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-66)   "response_metadata": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-67)   "tool_call_id": "toolu_0141zTpknasyWkrjTV6eKeT6"
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-68)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-69) ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-70)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-71)================================ tool Message (1) =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-72){
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-73) name: 'search',
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-74) content: "It's sunny in San Francisco, but you better look out if you're a Gemini 😈."
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-75)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-76){
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-77) messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-78)  HumanMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-79)   "id": "7c69c1f3-914b-4236-b2ca-ef250e72cb7a",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-80)   "content": "search for the weather in sf now",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-81)   "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-82)   "response_metadata": {}
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-83)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-84)  AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-85)   "id": "msg_0152mx7AweoRWa67HFsfyaif",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-86)   "content": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-87)    {
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-88)     "type": "text",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-89)     "text": "Certainly! I can help you search for the current weather in San Francisco. Let me use the search function to find that information for you."
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-90)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-91)    {
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-92)     "type": "tool_use",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-93)     "id": "toolu_0141zTpknasyWkrjTV6eKeT6",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-94)     "name": "search",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-95)     "input": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-96)      "input": "current weather in San Francisco"
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-97)     }
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-98)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-99)   ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-100)   "additional_kwargs": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-101)    "id": "msg_0152mx7AweoRWa67HFsfyaif",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-102)    "type": "message",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-103)    "role": "assistant",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-104)    "model": "claude-3-5-sonnet-20240620",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-105)    "stop_reason": "tool_use",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-106)    "stop_sequence": null,
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-107)    "usage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-108)     "input_tokens": 380,
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-109)     "output_tokens": 84
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-110)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-111)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-112)   "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-113)    "id": "msg_0152mx7AweoRWa67HFsfyaif",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-114)    "model": "claude-3-5-sonnet-20240620",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-115)    "stop_reason": "tool_use",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-116)    "stop_sequence": null,
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-117)    "usage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-118)     "input_tokens": 380,
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-119)     "output_tokens": 84
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-120)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-121)    "type": "message",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-122)    "role": "assistant"
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-123)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-124)   "tool_calls": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-125)    {
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-126)     "name": "search",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-127)     "args": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-128)      "query": "current weather in SF"
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-129)     },
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-130)     "id": "toolu_0141zTpknasyWkrjTV6eKeT6",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-131)     "type": "tool_call"
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-132)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-133)   ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-134)   "invalid_tool_calls": []
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-135)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-136)  ToolMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-137)   "id": "ccf0d56f-477f-408a-b809-6900a48379e0",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-138)   "content": "It's sunny in San Francisco, but you better look out if you're a Gemini 😈.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-139)   "name": "search",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-140)   "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-141)   "response_metadata": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-142)   "tool_call_id": "toolu_0141zTpknasyWkrjTV6eKeT6"
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-143)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-144)  AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-145)   "id": "msg_01YJXesUpaB5PfhgmRBCwnnb",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-146)   "content": "Based on the search results, I can provide you with information about the current weather in San Francisco:\n\nThe weather in San Francisco is currently sunny. This means it's a clear day with plenty of sunshine. It's a great day to be outdoors or engage in activities that benefit from good weather.\n\nHowever, I should note that the search result included an unusual comment about Gemini zodiac signs. This appears to be unrelated to the weather and might be part of a joke or a reference to something else. For accurate and detailed weather information, I would recommend checking a reliable weather service or website for San Francisco.\n\nIs there anything else you'd like to know about the weather in San Francisco or any other information you need?",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-147)   "additional_kwargs": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-148)    "id": "msg_01YJXesUpaB5PfhgmRBCwnnb",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-149)    "type": "message",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-150)    "role": "assistant",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-151)    "model": "claude-3-5-sonnet-20240620",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-152)    "stop_reason": "end_turn",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-153)    "stop_sequence": null,
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-154)    "usage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-155)     "input_tokens": 498,
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-156)     "output_tokens": 154
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-157)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-158)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-159)   "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-160)    "id": "msg_01YJXesUpaB5PfhgmRBCwnnb",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-161)    "model": "claude-3-5-sonnet-20240620",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-162)    "stop_reason": "end_turn",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-163)    "stop_sequence": null,
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-164)    "usage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-165)     "input_tokens": 498,
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-166)     "output_tokens": 154
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-167)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-168)    "type": "message",
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-169)    "role": "assistant"
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-170)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-171)   "tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-172)   "invalid_tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-173)   "usage_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-174)    "input_tokens": 498,
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-175)    "output_tokens": 154,
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-176)    "total_tokens": 652
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-177)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-178)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-179) ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-180)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-181)================================ ai Message (1) =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-182)Based on the search results, I can provide you with information about the current weather in San Francisco:
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-183)
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-184)The weather in San Francisco is currently sunny. This means it's a clear day with plenty of sunshine. It's a great day to be outdoors or engage in activities that benefit from good weather.
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-185)
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-186)However, I should note that the search result included an unusual comment about Gemini zodiac signs. This appears to be unrelated to the weather and might be part of a joke or a reference to something else. For accurate and detailed weather information, I would recommend checking a reliable weather service or website for San Francisco.
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-187)
[](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__codelineno-20-188)Is there anything else you'd like to know about the weather in San Francisco or any other information you need?

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to add dynamic breakpoints  ](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/) [ Next  How to wait for user input  ](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
