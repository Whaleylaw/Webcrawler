---
url: https://langchain-ai.github.io/langgraphjs/how-tos/time-travel
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#how-to-view-and-update-past-graph-state)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to view and update past graph state 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/?q= "Share")

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
            * [ How to wait for user input  ](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/)
            * [ How to wait for user input (Functional API)  ](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/)
            * How to view and update past graph state  [ How to view and update past graph state  ](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/) Table of contents 
              * [ Define the state  ](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#define-the-state)
              * [ Set up the tools  ](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#set-up-the-tools)
              * [ Let's get it to execute a tool  ](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#lets-get-it-to-execute-a-tool)
                * [ Pause before tools  ](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#pause-before-tools)
              * [ Get State  ](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#get-state)
              * [ Set up the model  ](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#set-up-the-model)
              * [ Define the graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#define-the-graph)
                * [ Pause before tools  ](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#pause-before-tools_1)
              * [ Get State  ](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#get-state_1)
              * [ Interacting with the Agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#interacting-with-the-agent)
              * [ Let's get it to execute a tool  ](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#lets-get-it-to-execute-a-tool_1)
                * [ Pause before tools  ](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#pause-before-tools_2)
              * [ Get State  ](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#get-state_2)
              * [ Resume  ](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#resume)
              * [ Check full history  ](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#check-full-history)
              * [ Replay a past state  ](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#replay-a-past-state)
              * [ Branch off a past state  ](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#branch-off-a-past-state)
                * [ First, update a previous checkpoint  ](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#first-update-a-previous-checkpoint)
                * [ Now you can run from this branch  ](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#now-you-can-run-from-this-branch)
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

  * [ Define the state  ](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#define-the-state)
  * [ Set up the tools  ](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#set-up-the-tools)
  * [ Let's get it to execute a tool  ](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#lets-get-it-to-execute-a-tool)
    * [ Pause before tools  ](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#pause-before-tools)
  * [ Get State  ](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#get-state)
  * [ Set up the model  ](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#set-up-the-model)
  * [ Define the graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#define-the-graph)
    * [ Pause before tools  ](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#pause-before-tools_1)
  * [ Get State  ](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#get-state_1)
  * [ Interacting with the Agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#interacting-with-the-agent)
  * [ Let's get it to execute a tool  ](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#lets-get-it-to-execute-a-tool_1)
    * [ Pause before tools  ](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#pause-before-tools_2)
  * [ Get State  ](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#get-state_2)
  * [ Resume  ](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#resume)
  * [ Check full history  ](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#check-full-history)
  * [ Replay a past state  ](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#replay-a-past-state)
  * [ Branch off a past state  ](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#branch-off-a-past-state)
    * [ First, update a previous checkpoint  ](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#first-update-a-previous-checkpoint)
    * [ Now you can run from this branch  ](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#now-you-can-run-from-this-branch)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
  5. [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraphjs/how-tos#human-in-the-loop)



# How to view and update past graph state[¶](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#how-to-view-and-update-past-graph-state "Permanent link")

Prerequisites

This guide assumes familiarity with the following concepts:

  * [Time Travel](https://langchain-ai.github.io/langgraphjs/concepts/time-travel)
  * [Breakpoints](https://langchain-ai.github.io/langgraphjs/concepts/breakpoints)
  * [LangGraph Glossary](https://langchain-ai.github.io/langgraphjs/concepts/low_level)



Once you start [checkpointing](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/persistence.ipynb) your graphs, you can easily **get** or **update** the state of the agent at any point in time. This permits a few things:

  1. You can surface a state during an interrupt to a user to let them accept an action.
  2. You can **rewind** the graph to reproduce or avoid issues.
  3. You can **modify** the state to embed your agent into a larger system, or to let the user better control its actions.



The key methods used for this functionality are:

  * [getState](https://langchain-ai.github.io/langgraphjs/reference/classes/langgraph_pregel.Pregel.html#getState): fetch the values from the target config
  * [updateState](https://langchain-ai.github.io/langgraphjs/reference/classes/langgraph_pregel.Pregel.html#updateState): apply the given values to the target state



**Note:** this requires passing in a checkpointer.

<!-- Example: 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-0-1)TODO
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-0-2)...
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-0-3)``` -->
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-0-4)
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-0-5)This works for
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-0-6)<a href="/langgraphjs/reference/classes/langgraph.StateGraph.html">StateGraph</a>
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-0-7)and all its subclasses, such as
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-0-8)<a href="/langgraphjs/reference/classes/langgraph.MessageGraph.html">MessageGraph</a>.
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-0-9)
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-0-10)Below is an example.
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-0-11)
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-0-12)<div class="admonition tip">
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-0-13)  <p class="admonition-title">Note</p>
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-0-14)  <p>
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-0-15)    In this how-to, we will create our agent from scratch to be transparent (but verbose). You can accomplish similar functionality using the <code>createReactAgent(model, tools=tool, checkpointer=checkpointer)</code> (<a href="/langgraphjs/reference/functions/langgraph_prebuilt.createReactAgent.html">API doc</a>) constructor. This may be more appropriate if you are used to LangChain's <a href="https://js.langchain.com/docs/how_to/agent_executor">AgentExecutor</a> class.
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-0-16)  </p>
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-0-17)</div>
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-0-18)
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-0-19)## Setup
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-0-20)
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-0-21)This guide will use OpenAI's GPT-4o model. We will optionally set our API key
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-0-22)for [LangSmith tracing](https://smith.langchain.com/), which will give us
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-0-23)best-in-class observability.
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-0-24)
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-0-25)
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-0-26)```typescript
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-0-27)// process.env.OPENAI_API_KEY = "sk_...";
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-0-28)
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-0-29)// Optional, add tracing in LangSmith
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-0-30)// process.env.LANGCHAIN_API_KEY = "ls__...";
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-0-31)process.env.LANGCHAIN_CALLBACKS_BACKGROUND="true";
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-0-32)process.env.LANGCHAIN_TRACING_V2="true";
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-0-33)process.env.LANGCHAIN_PROJECT="Time Travel: LangGraphJS";

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-1-1)Time Travel: LangGraphJS

```


## Define the state[¶](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#define-the-state "Permanent link")

The state is the interface for all of the nodes in our graph.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-2-1)import{Annotation}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-2-2)import{BaseMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-2-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-2-4)constStateAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-2-5)messages:Annotation<BaseMessage[]>({
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-2-6)reducer:(x,y)=>x.concat(y),
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-2-7)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-2-8)});

```


## Set up the tools[¶](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#set-up-the-tools "Permanent link")

We will first define the tools we want to use. For this simple example, we will use create a placeholder search engine. However, it is really easy to create your own tools - see documentation [here](https://js.langchain.com/docs/how_to/custom_tools) on how to do that.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-3-1)import{tool}from"@langchain/core/tools";
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-3-2)import{z}from"zod";
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-3-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-3-4)constsearchTool=tool(async(_)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-3-5)// This is a placeholder for the actual implementation
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-3-6)return"Cold, with a low of 13 ℃";
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-3-7)},{
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-3-8)name:"search",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-3-9)description:
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-3-10)"Use to surf the web, fetch current information, check the weather, and retrieve other information.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-3-11)schema:z.object({
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-3-12)query:z.string().describe("The query to use in your search."),
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-3-13)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-3-14)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-3-15)
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-3-16)awaitsearchTool.invoke({query:"What's the weather like?"});
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-3-17)
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-3-18)consttools=[searchTool];

```


We can now wrap these tools in a simple [ToolNodee agent. Between interactions you can get and update state.](https://langchain-ai.github.io/langgraphjs/reference/classes/prebuilt.ToolNode.html)

[ ](https://langchain-ai.github.io/langgraphjs/reference/classes/prebuilt.ToolNode.html)

[](https://langchain-ai.github.io/langgraphjs/reference/classes/prebuilt.ToolNode.html)```
[](https://langchain-ai.github.io/langgraphjs/reference/classes/prebuilt.ToolNode.html)[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-8-1)letconfig={configurable:{thread_id:"conversation-num-1"}};
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-8-2)letinputs={messages:[{role:"user",content:"Hi I'm Jo."}]}asany;
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-8-3)forawait(
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-8-4)const{messages}ofawaitgraph.stream(inputs,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-8-5)...config,
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-8-6)streamMode:"values",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-8-7)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-8-8)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-8-9)letmsg=messages[messages?.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-8-10)if(msg?.content){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-8-11)console.log(msg.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-8-12)}elseif(msg?.tool_calls?.length>0){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-8-13)console.log(msg.tool_calls);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-8-14)}else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-8-15)console.log(msg);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-8-16)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-8-17)console.log("-----\n");
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-8-18)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-9-1)Hi I'm Jo.
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-9-2)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-9-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-9-4)Hello, Jo! How can I assist you today?
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-9-5)-----

```


See LangSmith example run here <https://smith.langchain.com/public/b3feb09b-bcd2-4ad5-ad1d-414106148448/r>

Here you can see the "agent" node ran, and then our edge returned `__end__` so the graph stopped execution there.

Let's check the current graph state.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-10-1)letcheckpoint=awaitgraph.getState(config);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-10-2)checkpoint.values;

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-11-1){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-11-2) messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-11-3)  { role: 'user', content: "Hi I'm Jo." },
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-11-4)  AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-11-5)   "id": "chatcmpl-A3FGf3k3QQo9q0QjT6Oc5h1XplkHr",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-11-6)   "content": "Hello, Jo! How can I assist you today?",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-11-7)   "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-11-8)   "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-11-9)    "tokenUsage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-11-10)     "completionTokens": 12,
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-11-11)     "promptTokens": 68,
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-11-12)     "totalTokens": 80
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-11-13)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-11-14)    "finish_reason": "stop",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-11-15)    "system_fingerprint": "fp_fde2829a40"
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-11-16)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-11-17)   "tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-11-18)   "invalid_tool_calls": []
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-11-19)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-11-20) ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-11-21)}

```


The current state is the two messages we've seen above, 1. the HumanMessage we sent in, 2. the AIMessage we got back from the model. 

The `next` values are empty since the graph has terminated (transitioned to the `__end__`).

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-12-1)checkpoint.next;

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-13-1)[]

```


## Let's get it to execute a tool[¶](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#lets-get-it-to-execute-a-tool "Permanent link")

When we call the graph again, it will create a checkpoint after each internal execution step. Let's get it to run a tool, then look at the checkpoint.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-1)inputs={messages:[{role:"user",content:"What's the weather like in SF currently?"}]}asany;
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-2)forawait(
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-3)const{messages}ofawaitgraph.stream(inputs,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-4)...config,
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-5)streamMode:"values",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-6)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-7)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-8)letmsg=messages[messages?.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-9)if(msg?.content){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-10)console.log(msg.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-11)}elseif(msg?.tool_calls?.length>0){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-12)console.log(msg.tool_calls);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-13)}else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-14)console.log(msg);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-15)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-16)console.log("-----\n");
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-17)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-1)What's the weather like in SF currently?
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-2)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-3)``````output
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-4)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-5) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-6)  name: 'search',
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-7)  args: { query: 'current weather in San Francisco' },
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-8)  type: 'tool_call',
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-9)  id: 'call_ZtmtDOyEXDCnXDgowlit5dSd'
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-10) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-11)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-12)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-13)
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-14)Cold, with a low of 13 ℃
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-15)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-16)
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-17)The current weather in San Francisco is cold, with a low of 13°C.
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-18)-----

```


See the trace of the above execution here: <https://smith.langchain.com/public/0ef426fd-0da1-4c02-a50b-64ae1e68338e/r> We can see it planned the tool execution (ie the "agent" node), then "should_continue" edge returned "continue" so we proceeded to "action" node, which executed the tool, and then "agent" node emitted the final response, which made "should_continue" edge return "end". Let's see how we can have more control over this. 

### Pause before tools[¶](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#pause-before-tools "Permanent link")

If you notice below, we now will add `interruptBefore=["action"]` - this means that before any actions are taken we pause. This is a great moment to allow the user to correct and update the state! This is very useful when you want to have a human-in-the-loop to validate (and potentially change) the action to take.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-1)memory=newMemorySaver();
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-2)constgraphWithInterrupt=workflow.compile({
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-3)checkpointer:memory,
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-4)interruptBefore:["tools"],
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-5)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-7)inputs={messages:[{role:"user",content:"What's the weather like in SF currently?"}]}asany;
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-8)forawait(
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-9)const{messages}ofawaitgraphWithInterrupt.stream(inputs,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-10)...config,
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-11)streamMode:"values",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-12)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-13)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-14)letmsg=messages[messages?.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-15)if(msg?.content){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-16)console.log(msg.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-17)}elseif(msg?.tool_calls?.length>0){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-18)console.log(msg.tool_calls);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-19)}else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-20)console.log(msg);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-21)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-22)console.log("-----\n");
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-23)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-1)What's the weather like in SF currently?
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-2)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-4)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-5) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-6)  name: 'search',
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-7)  args: { query: 'current weather in San Francisco' },
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-8)  type: 'tool_call',
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-9)  id: 'call_OsKnTv2psf879eeJ9vx5GeoY'
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-10) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-11)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-12)-----

```


## Get State[¶](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#get-state "Permanent link")

You can fetch the latest graph checkpoint using [. This object will actually run the tools (functions) whenever they are invoked by our LLM.](https://langchain-ai.github.io/langgraphjs/reference/classes/pregel.Pregel.html#getState)

[ ](https://langchain-ai.github.io/langgraphjs/reference/classes/pregel.Pregel.html#getState)

[](https://langchain-ai.github.io/langgraphjs/reference/classes/pregel.Pregel.html#getState)```
[](https://langchain-ai.github.io/langgraphjs/reference/classes/pregel.Pregel.html#getState)[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-4-1)import{ToolNode}from"@langchain/langgraph/prebuilt";
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-4-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-4-3)consttoolNode=newToolNode(tools);

```


## Set up the model[¶](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#set-up-the-model "Permanent link")

Now we will load the [chat model](https://js.langchain.com/docs/concepts/chat_models/).

  1. It should work with messages. We will represent all agent state in the form of messages, so it needs to be able to work well with them.
  2. It should work with [tool calling](https://js.langchain.com/docs/how_to/tool_calling/#passing-tools-to-llms), meaning it can return function arguments in its response.



Notet state is the two messages we've seen above, 1. the HumanMessage we sent in, 2. the AIMessage we got back from the model. The `next` values are empty since the graph has terminated (transitioned to the `__end__`). 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-12-1)checkpoint.next;

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-13-1)[]

```


## Let's get it to execute a tool When we call the graph again, it will create a checkpoint after each internal execution step. Let's get it to run a tool, then look at the checkpoint. 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-1)inputs={messages:[{role:"user",content:"What's the weather like in SF currently?"}]}asany;
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-2)forawait(
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-3)const{messages}ofawaitgraph.stream(inputs,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-4)...config,
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-5)streamMode:"values",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-6)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-7)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-8)letmsg=messages[messages?.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-9)if(msg?.content){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-10)console.log(msg.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-11)}elseif(msg?.tool_calls?.length>0){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-12)console.log(msg.tool_calls);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-13)}else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-14)console.log(msg);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-15)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-16)console.log("-----\n");
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-17)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-1)What's the weather like in SF currently?
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-2)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-3)``````output
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-4)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-5) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-6)  name: 'search',
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-7)  args: { query: 'current weather in San Francisco' },
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-8)  type: 'tool_call',
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-9)  id: 'call_ZtmtDOyEXDCnXDgowlit5dSd'
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-10) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-11)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-12)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-13)
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-14)Cold, with a low of 13 ℃
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-15)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-16)
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-17)The current weather in San Francisco is cold, with a low of 13°C.
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-18)-----

```


See the trace of the above execution here: https://smith.langchain.com/public/0ef426fd-0da1-4c02-a50b-64ae1e68338e/r We can see it planned the tool execution (ie the "agent" node), then "should_continue" edge returned "continue" so we proceeded to "action" node, which executed the tool, and then "agent" node emitted the final response, which made "should_continue" edge return "end". Let's see how we can have more control over this. ### Pause before tools If you notice below, we now will add `interruptBefore=["action"]` - this means that before any actions are taken we pause. This is a great moment to allow the user to correct and update the state! This is very useful when you want to have a human-in-the-loop to validate (and potentially change) the action to take. 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-1)memory=newMemorySaver();
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-2)constgraphWithInterrupt=workflow.compile({
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-3)checkpointer:memory,
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-4)interruptBefore:["tools"],
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-5)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-7)inputs={messages:[{role:"user",content:"What's the weather like in SF currently?"}]}asany;
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-8)forawait(
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-9)const{messages}ofawaitgraphWithInterrupt.stream(inputs,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-10)...config,
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-11)streamMode:"values",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-12)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-13)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-14)letmsg=messages[messages?.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-15)if(msg?.content){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-16)console.log(msg.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-17)}elseif(msg?.tool_calls?.length>0){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-18)console.log(msg.tool_calls);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-19)}else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-20)console.log(msg);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-21)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-22)console.log("-----\n");
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-23)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-1)What's the weather like in SF currently?
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-2)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-4)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-5) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-6)  name: 'search',
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-7)  args: { query: 'current weather in San Francisco' },
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-8)  type: 'tool_call',
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-9)  id: 'call_OsKnTv2psf879eeJ9vx5GeoY'
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-10) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-11)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-12)-----

```


## Get State You can fetch the latest graph checkpoint using [ These model requirements are not general requirements for using LangGraph - they are just requirements for this one example. in, 2. the AIMessage we got back from the model. The `next` values are empty since the graph has terminated (transitioned to the `__end__`). ](https://langchain-ai.github.io/langgraphjs/reference/classes/pregel.Pregel.html#getState)

[](https://langchain-ai.github.io/langgraphjs/reference/classes/pregel.Pregel.html#getState)```
[](https://langchain-ai.github.io/langgraphjs/reference/classes/pregel.Pregel.html#getState)[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-12-1)checkpoint.next;

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-13-1)[]

```


## Let's get it to execute a tool When we call the graph again, it will create a checkpoint after each internal execution step. Let's get it to run a tool, then look at the checkpoint. 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-1)inputs={messages:[{role:"user",content:"What's the weather like in SF currently?"}]}asany;
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-2)forawait(
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-3)const{messages}ofawaitgraph.stream(inputs,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-4)...config,
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-5)streamMode:"values",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-6)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-7)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-8)letmsg=messages[messages?.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-9)if(msg?.content){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-10)console.log(msg.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-11)}elseif(msg?.tool_calls?.length>0){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-12)console.log(msg.tool_calls);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-13)}else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-14)console.log(msg);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-15)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-16)console.log("-----\n");
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-17)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-1)What's the weather like in SF currently?
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-2)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-3)``````output
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-4)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-5) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-6)  name: 'search',
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-7)  args: { query: 'current weather in San Francisco' },
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-8)  type: 'tool_call',
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-9)  id: 'call_ZtmtDOyEXDCnXDgowlit5dSd'
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-10) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-11)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-12)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-13)
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-14)Cold, with a low of 13 ℃
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-15)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-16)
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-17)The current weather in San Francisco is cold, with a low of 13°C.
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-18)-----

```


See the trace of the above execution here: https://smith.langchain.com/public/0ef426fd-0da1-4c02-a50b-64ae1e68338e/r We can see it planned the tool execution (ie the "agent" node), then "should_continue" edge returned "continue" so we proceeded to "action" node, which executed the tool, and then "agent" node emitted the final response, which made "should_continue" edge return "end". Let's see how we can have more control over this. ### Pause before tools If you notice below, we now will add `interruptBefore=["action"]` - this means that before any actions are taken we pause. This is a great moment to allow the user to correct and update the state! This is very useful when you want to have a human-in-the-loop to validate (and potentially change) the action to take. 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-1)memory=newMemorySaver();
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-2)constgraphWithInterrupt=workflow.compile({
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-3)checkpointer:memory,
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-4)interruptBefore:["tools"],
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-5)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-7)inputs={messages:[{role:"user",content:"What's the weather like in SF currently?"}]}asany;
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-8)forawait(
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-9)const{messages}ofawaitgraphWithInterrupt.stream(inputs,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-10)...config,
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-11)streamMode:"values",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-12)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-13)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-14)letmsg=messages[messages?.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-15)if(msg?.content){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-16)console.log(msg.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-17)}elseif(msg?.tool_calls?.length>0){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-18)console.log(msg.tool_calls);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-19)}else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-20)console.log(msg);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-21)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-22)console.log("-----\n");
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-23)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-1)What's the weather like in SF currently?
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-2)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-4)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-5) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-6)  name: 'search',
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-7)  args: { query: 'current weather in San Francisco' },
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-8)  type: 'tool_call',
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-9)  id: 'call_OsKnTv2psf879eeJ9vx5GeoY'
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-10) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-11)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-12)-----

```


## Get State You can fetch the latest graph checkpoint using [ The `next` values are empty since the graph has terminated (transitioned to the `__end__`). ](https://langchain-ai.github.io/langgraphjs/reference/classes/pregel.Pregel.html#getState)

[](https://langchain-ai.github.io/langgraphjs/reference/classes/pregel.Pregel.html#getState)```
[](https://langchain-ai.github.io/langgraphjs/reference/classes/pregel.Pregel.html#getState)[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-12-1)checkpoint.next;

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-13-1)[]

```


## Let's get it to execute a tool When we call the graph again, it will create a checkpoint after each internal execution step. Let's get it to run a tool, then look at the checkpoint. 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-1)inputs={messages:[{role:"user",content:"What's the weather like in SF currently?"}]}asany;
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-2)forawait(
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-3)const{messages}ofawaitgraph.stream(inputs,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-4)...config,
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-5)streamMode:"values",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-6)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-7)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-8)letmsg=messages[messages?.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-9)if(msg?.content){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-10)console.log(msg.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-11)}elseif(msg?.tool_calls?.length>0){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-12)console.log(msg.tool_calls);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-13)}else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-14)console.log(msg);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-15)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-16)console.log("-----\n");
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-17)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-1)What's the weather like in SF currently?
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-2)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-3)``````output
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-4)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-5) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-6)  name: 'search',
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-7)  args: { query: 'current weather in San Francisco' },
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-8)  type: 'tool_call',
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-9)  id: 'call_ZtmtDOyEXDCnXDgowlit5dSd'
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-10) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-11)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-12)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-13)
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-14)Cold, with a low of 13 ℃
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-15)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-16)
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-17)The current weather in San Francisco is cold, with a low of 13°C.
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-18)-----

```


See the trace of the above execution here: https://smith.langchain.com/public/0ef426fd-0da1-4c02-a50b-64ae1e68338e/r We can see it planned the tool execution (ie the "agent" node), then "should_continue" edge returned "continue" so we proceeded to "action" node, which executed the tool, and then "agent" node emitted the final response, which made "should_continue" edge return "end". Let's see how we can have more control over this. ### Pause before tools If you notice below, we now will add `interruptBefore=["action"]` - this means that before any actions are taken we pause. This is a great moment to allow the user to correct and update the state! This is very useful when you want to have a human-in-the-loop to validate (and potentially change) the action to take. 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-1)memory=newMemorySaver();
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-2)constgraphWithInterrupt=workflow.compile({
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-3)checkpointer:memory,
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-4)interruptBefore:["tools"],
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-5)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-7)inputs={messages:[{role:"user",content:"What's the weather like in SF currently?"}]}asany;
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-8)forawait(
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-9)const{messages}ofawaitgraphWithInterrupt.stream(inputs,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-10)...config,
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-11)streamMode:"values",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-12)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-13)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-14)letmsg=messages[messages?.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-15)if(msg?.content){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-16)console.log(msg.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-17)}elseif(msg?.tool_calls?.length>0){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-18)console.log(msg.tool_calls);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-19)}else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-20)console.log(msg);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-21)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-22)console.log("-----\n");
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-23)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-1)What's the weather like in SF currently?
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-2)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-4)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-5) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-6)  name: 'search',
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-7)  args: { query: 'current weather in San Francisco' },
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-8)  type: 'tool_call',
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-9)  id: 'call_OsKnTv2psf879eeJ9vx5GeoY'
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-10) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-11)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-12)-----

```


## Get State You can fetch the latest graph checkpoint using [ ](https://langchain-ai.github.io/langgraphjs/reference/classes/pregel.Pregel.html#getState)

[](https://langchain-ai.github.io/langgraphjs/reference/classes/pregel.Pregel.html#getState)```
[](https://langchain-ai.github.io/langgraphjs/reference/classes/pregel.Pregel.html#getState)[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-5-1)import{ChatOpenAI}from"@langchain/openai";
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-5-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-5-3)constmodel=newChatOpenAI({model:"gpt-4o"});

```


After we've done this, we should make sure the model knows that it has these tools available to call. We can do this by calling [bindTools](https://v01.api.js.langchain.com/classes/langchain_core_language_models_chat_models.BaseChatModel.html#bindTools).

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-6-1)constboundModel=model.bindTools(tools);

```


## Define the graph[¶](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#define-the-graph "Permanent link")

We can now put it all together. Time travel requires a checkpointer to save the state - otherwise you wouldn't have anything go `get` or `update`. We will use the [MemorySaverhe tool, and then "agent" node emitted the final response, which made "should_continue" edge return "end". Let's see how we can have more control over this.](https://langchain-ai.github.io/langgraphjs/reference/classes/index.MemorySaver.html)

[ ](https://langchain-ai.github.io/langgraphjs/reference/classes/index.MemorySaver.html)

### [Pause before tools](https://langchain-ai.github.io/langgraphjs/reference/classes/index.MemorySaver.html)[¶](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#pause-before-tools_1 "Permanent link")

If you notice below, we now will add `interruptBefore=["action"]` - this means that before any actions are taken we pause. This is a great moment to allow the user to correct and update the state! This is very useful when you want to have a human-in-the-loop to validate (and potentially change) the action to take.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-1)memory=newMemorySaver();
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-2)constgraphWithInterrupt=workflow.compile({
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-3)checkpointer:memory,
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-4)interruptBefore:["tools"],
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-5)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-7)inputs={messages:[{role:"user",content:"What's the weather like in SF currently?"}]}asany;
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-8)forawait(
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-9)const{messages}ofawaitgraphWithInterrupt.stream(inputs,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-10)...config,
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-11)streamMode:"values",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-12)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-13)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-14)letmsg=messages[messages?.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-15)if(msg?.content){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-16)console.log(msg.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-17)}elseif(msg?.tool_calls?.length>0){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-18)console.log(msg.tool_calls);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-19)}else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-20)console.log(msg);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-21)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-22)console.log("-----\n");
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-23)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-1)What's the weather like in SF currently?
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-2)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-4)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-5) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-6)  name: 'search',
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-7)  args: { query: 'current weather in San Francisco' },
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-8)  type: 'tool_call',
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-9)  id: 'call_OsKnTv2psf879eeJ9vx5GeoY'
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-10) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-11)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-12)-----

```


## Get State[¶](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#get-state_1 "Permanent link")

You can fetch the latest graph checkpoint using [, which "saves" checkpoints in-memory.](https://langchain-ai.github.io/langgraphjs/reference/classes/pregel.Pregel.html#getState)

[ ](https://langchain-ai.github.io/langgraphjs/reference/classes/pregel.Pregel.html#getState)

[](https://langchain-ai.github.io/langgraphjs/reference/classes/pregel.Pregel.html#getState)```
[](https://langchain-ai.github.io/langgraphjs/reference/classes/pregel.Pregel.html#getState)[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-7-1)import{END,START,StateGraph}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-7-2)import{AIMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-7-3)import{RunnableConfig}from"@langchain/core/runnables";
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-7-4)import{MemorySaver}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-7-5)
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-7-6)constrouteMessage=(state:typeofStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-7-7)const{messages}=state;
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-7-8)constlastMessage=messages[messages.length-1]asAIMessage;
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-7-9)// If no tools are called, we can finish (respond to the user)
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-7-10)if(!lastMessage?.tool_calls?.length){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-7-11)returnEND;
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-7-12)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-7-13)// Otherwise if there is, we continue and call the tools
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-7-14)return"tools";
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-7-15)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-7-16)
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-7-17)constcallModel=async(
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-7-18)state:typeofStateAnnotation.State,
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-7-19)config?:RunnableConfig,
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-7-20)):Promise<Partial<typeofStateAnnotation.State>>=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-7-21)const{messages}=state;
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-7-22)constresponse=awaitboundModel.invoke(messages,config);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-7-23)return{messages:[response]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-7-24)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-7-25)
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-7-26)constworkflow=newStateGraph(StateAnnotation)
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-7-27).addNode("agent",callModel)
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-7-28).addNode("tools",toolNode)
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-7-29).addEdge(START,"agent")
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-7-30).addConditionalEdges("agent",routeMessage)
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-7-31).addEdge("tools","agent");
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-7-32)
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-7-33)// Here we only save in-memory
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-7-34)letmemory=newMemorySaver();
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-7-35)constgraph=workflow.compile({checkpointer:memory});

```


## Interacting with the Agent[¶](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#interacting-with-the-agent "Permanent link")

We can now interact with the agent. Between interactions you can get and update state.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-8-1)letconfig={configurable:{thread_id:"conversation-num-1"}};
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-8-2)letinputs={messages:[{role:"user",content:"Hi I'm Jo."}]}asany;
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-8-3)forawait(
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-8-4)const{messages}ofawaitgraph.stream(inputs,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-8-5)...config,
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-8-6)streamMode:"values",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-8-7)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-8-8)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-8-9)letmsg=messages[messages?.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-8-10)if(msg?.content){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-8-11)console.log(msg.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-8-12)}elseif(msg?.tool_calls?.length>0){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-8-13)console.log(msg.tool_calls);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-8-14)}else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-8-15)console.log(msg);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-8-16)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-8-17)console.log("-----\n");
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-8-18)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-9-1)Hi I'm Jo.
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-9-2)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-9-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-9-4)Hello, Jo! How can I assist you today?
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-9-5)-----

```


See LangSmith example run here <https://smith.langchain.com/public/b3feb09b-bcd2-4ad5-ad1d-414106148448/r>

Here you can see the "agent" node ran, and then our edge returned `__end__` so the graph stopped execution there.

Let's check the current graph state.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-10-1)letcheckpoint=awaitgraph.getState(config);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-10-2)checkpoint.values;

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-11-1){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-11-2) messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-11-3)  { role: 'user', content: "Hi I'm Jo." },
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-11-4)  AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-11-5)   "id": "chatcmpl-A3FGf3k3QQo9q0QjT6Oc5h1XplkHr",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-11-6)   "content": "Hello, Jo! How can I assist you today?",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-11-7)   "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-11-8)   "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-11-9)    "tokenUsage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-11-10)     "completionTokens": 12,
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-11-11)     "promptTokens": 68,
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-11-12)     "totalTokens": 80
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-11-13)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-11-14)    "finish_reason": "stop",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-11-15)    "system_fingerprint": "fp_fde2829a40"
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-11-16)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-11-17)   "tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-11-18)   "invalid_tool_calls": []
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-11-19)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-11-20) ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-11-21)}

```


The current state is the two messages we've seen above, 1. the HumanMessage we sent in, 2. the AIMessage we got back from the model. 

The `next` values are empty since the graph has terminated (transitioned to the `__end__`).

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-12-1)checkpoint.next;

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-13-1)[]

```


## Let's get it to execute a tool[¶](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#lets-get-it-to-execute-a-tool_1 "Permanent link")

When we call the graph again, it will create a checkpoint after each internal execution step. Let's get it to run a tool, then look at the checkpoint.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-1)inputs={messages:[{role:"user",content:"What's the weather like in SF currently?"}]}asany;
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-2)forawait(
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-3)const{messages}ofawaitgraph.stream(inputs,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-4)...config,
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-5)streamMode:"values",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-6)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-7)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-8)letmsg=messages[messages?.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-9)if(msg?.content){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-10)console.log(msg.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-11)}elseif(msg?.tool_calls?.length>0){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-12)console.log(msg.tool_calls);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-13)}else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-14)console.log(msg);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-15)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-16)console.log("-----\n");
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-14-17)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-1)What's the weather like in SF currently?
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-2)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-3)``````output
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-4)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-5) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-6)  name: 'search',
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-7)  args: { query: 'current weather in San Francisco' },
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-8)  type: 'tool_call',
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-9)  id: 'call_ZtmtDOyEXDCnXDgowlit5dSd'
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-10) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-11)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-12)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-13)
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-14)Cold, with a low of 13 ℃
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-15)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-16)
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-17)The current weather in San Francisco is cold, with a low of 13°C.
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-15-18)-----

```


See the trace of the above execution here: <https://smith.langchain.com/public/0ef426fd-0da1-4c02-a50b-64ae1e68338e/r> We can see it planned the tool execution (ie the "agent" node), then "should_continue" edge returned "continue" so we proceeded to "action" node, which executed the tool, and then "agent" node emitted the final response, which made "should_continue" edge return "end". Let's see how we can have more control over this. 

### Pause before tools[¶](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#pause-before-tools_2 "Permanent link")

If you notice below, we now will add `interruptBefore=["action"]` - this means that before any actions are taken we pause. This is a great moment to allow the user to correct and update the state! This is very useful when you want to have a human-in-the-loop to validate (and potentially change) the action to take.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-1)memory=newMemorySaver();
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-2)constgraphWithInterrupt=workflow.compile({
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-3)checkpointer:memory,
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-4)interruptBefore:["tools"],
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-5)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-7)inputs={messages:[{role:"user",content:"What's the weather like in SF currently?"}]}asany;
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-8)forawait(
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-9)const{messages}ofawaitgraphWithInterrupt.stream(inputs,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-10)...config,
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-11)streamMode:"values",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-12)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-13)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-14)letmsg=messages[messages?.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-15)if(msg?.content){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-16)console.log(msg.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-17)}elseif(msg?.tool_calls?.length>0){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-18)console.log(msg.tool_calls);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-19)}else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-20)console.log(msg);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-21)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-22)console.log("-----\n");
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-16-23)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-1)What's the weather like in SF currently?
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-2)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-4)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-5) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-6)  name: 'search',
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-7)  args: { query: 'current weather in San Francisco' },
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-8)  type: 'tool_call',
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-9)  id: 'call_OsKnTv2psf879eeJ9vx5GeoY'
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-10) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-11)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-17-12)-----

```


## Get State[¶](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#get-state_2 "Permanent link")

You can fetch the latest graph checkpoint using `getState(config)`[](https://langchain-ai.github.io/langgraphjs/reference/classes/pregel.Pregel.html#getState).

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-18-1)letsnapshot=awaitgraphWithInterrupt.getState(config);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-18-2)snapshot.next;

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-19-1)[ 'tools' ]

```


## Resume[¶](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#resume "Permanent link")

You can resume by running the graph with a `null` input. The checkpoint is loaded, and with no new inputs, it will execute as if no interrupt had occurred.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-20-1)forawait(
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-20-2)const{messages}ofawaitgraphWithInterrupt.stream(null,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-20-3)...snapshot.config,
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-20-4)streamMode:"values",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-20-5)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-20-6)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-20-7)letmsg=messages[messages?.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-20-8)if(msg?.content){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-20-9)console.log(msg.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-20-10)}elseif(msg?.tool_calls?.length>0){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-20-11)console.log(msg.tool_calls);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-20-12)}else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-20-13)console.log(msg);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-20-14)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-20-15)console.log("-----\n");
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-20-16)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-21-1)Cold, with a low of 13 ℃
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-21-2)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-21-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-21-4)Currently, it is cold in San Francisco, with a temperature around 13°C (55°F).
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-21-5)-----

```


## Check full history[¶](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#check-full-history "Permanent link")

Let's browse the history of this thread, from newest to oldest.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-22-1)lettoReplay;
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-22-2)conststates=awaitgraphWithInterrupt.getStateHistory(config);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-22-3)forawait(conststateofstates){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-22-4)console.log(state);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-22-5)console.log("--");
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-22-6)if(state.values?.messages?.length===2){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-22-7)toReplay=state;
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-22-8)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-22-9)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-22-10)if(!toReplay){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-22-11)thrownewError("No state to replay");
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-22-12)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-1){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-2) values: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-3)  messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-4)   [Object],
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-5)   AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-6)    "id": "chatcmpl-A3FGhKzOZs0GYZ2yalNOCQZyPgbcp",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-7)    "content": "",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-8)    "additional_kwargs": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-9)     "tool_calls": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-10)      {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-11)       "id": "call_OsKnTv2psf879eeJ9vx5GeoY",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-12)       "type": "function",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-13)       "function": "[Object]"
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-14)      }
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-15)     ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-16)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-17)    "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-18)     "tokenUsage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-19)      "completionTokens": 17,
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-20)      "promptTokens": 72,
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-21)      "totalTokens": 89
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-22)     },
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-23)     "finish_reason": "tool_calls",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-24)     "system_fingerprint": "fp_fde2829a40"
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-25)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-26)    "tool_calls": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-27)     {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-28)      "name": "search",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-29)      "args": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-30)       "query": "current weather in San Francisco"
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-31)      },
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-32)      "type": "tool_call",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-33)      "id": "call_OsKnTv2psf879eeJ9vx5GeoY"
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-34)     }
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-35)    ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-36)    "invalid_tool_calls": []
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-37)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-38)   ToolMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-39)    "content": "Cold, with a low of 13 ℃",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-40)    "name": "search",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-41)    "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-42)    "response_metadata": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-43)    "tool_call_id": "call_OsKnTv2psf879eeJ9vx5GeoY"
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-44)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-45)   AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-46)    "id": "chatcmpl-A3FGiYripPKtQLnAK1H3hWLSXQfOD",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-47)    "content": "Currently, it is cold in San Francisco, with a temperature around 13°C (55°F).",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-48)    "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-49)    "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-50)     "tokenUsage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-51)      "completionTokens": 21,
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-52)      "promptTokens": 105,
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-53)      "totalTokens": 126
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-54)     },
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-55)     "finish_reason": "stop",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-56)     "system_fingerprint": "fp_fde2829a40"
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-57)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-58)    "tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-59)    "invalid_tool_calls": []
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-60)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-61)  ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-62) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-63) next: [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-64) tasks: [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-65) metadata: { source: 'loop', writes: { agent: [Object] }, step: 3 },
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-66) config: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-67)  configurable: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-68)   thread_id: 'conversation-num-1',
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-69)   checkpoint_ns: '',
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-70)   checkpoint_id: '1ef69ab6-9c3a-6bd1-8003-d7f030ff72b2'
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-71)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-72) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-73) createdAt: '2024-09-03T04:17:20.653Z',
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-74) parentConfig: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-75)  configurable: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-76)   thread_id: 'conversation-num-1',
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-77)   checkpoint_ns: '',
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-78)   checkpoint_id: '1ef69ab6-9516-6200-8002-43d2c6dc603f'
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-79)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-80) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-81)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-82)--
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-83){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-84) values: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-85)  messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-86)   [Object],
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-87)   AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-88)    "id": "chatcmpl-A3FGhKzOZs0GYZ2yalNOCQZyPgbcp",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-89)    "content": "",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-90)    "additional_kwargs": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-91)     "tool_calls": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-92)      {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-93)       "id": "call_OsKnTv2psf879eeJ9vx5GeoY",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-94)       "type": "function",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-95)       "function": "[Object]"
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-96)      }
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-97)     ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-98)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-99)    "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-100)     "tokenUsage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-101)      "completionTokens": 17,
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-102)      "promptTokens": 72,
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-103)      "totalTokens": 89
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-104)     },
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-105)     "finish_reason": "tool_calls",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-106)     "system_fingerprint": "fp_fde2829a40"
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-107)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-108)    "tool_calls": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-109)     {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-110)      "name": "search",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-111)      "args": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-112)       "query": "current weather in San Francisco"
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-113)      },
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-114)      "type": "tool_call",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-115)      "id": "call_OsKnTv2psf879eeJ9vx5GeoY"
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-116)     }
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-117)    ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-118)    "invalid_tool_calls": []
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-119)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-120)   ToolMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-121)    "content": "Cold, with a low of 13 ℃",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-122)    "name": "search",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-123)    "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-124)    "response_metadata": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-125)    "tool_call_id": "call_OsKnTv2psf879eeJ9vx5GeoY"
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-126)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-127)  ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-128) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-129) next: [ 'agent' ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-130) tasks: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-131)  {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-132)   id: '612efffa-3b16-530f-8a39-fd01c31e7b8b',
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-133)   name: 'agent',
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-134)   interrupts: []
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-135)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-136) ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-137) metadata: { source: 'loop', writes: { tools: [Object] }, step: 2 },
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-138) config: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-139)  configurable: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-140)   thread_id: 'conversation-num-1',
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-141)   checkpoint_ns: '',
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-142)   checkpoint_id: '1ef69ab6-9516-6200-8002-43d2c6dc603f'
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-143)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-144) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-145) createdAt: '2024-09-03T04:17:19.904Z',
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-146) parentConfig: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-147)  configurable: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-148)   thread_id: 'conversation-num-1',
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-149)   checkpoint_ns: '',
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-150)   checkpoint_id: '1ef69ab6-9455-6410-8001-1c78a97f63e6'
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-151)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-152) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-153)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-154)--
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-155){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-156) values: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-157)  messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-158)   [Object],
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-159)   AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-160)    "id": "chatcmpl-A3FGhKzOZs0GYZ2yalNOCQZyPgbcp",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-161)    "content": "",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-162)    "additional_kwargs": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-163)     "tool_calls": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-164)      {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-165)       "id": "call_OsKnTv2psf879eeJ9vx5GeoY",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-166)       "type": "function",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-167)       "function": "[Object]"
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-168)      }
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-169)     ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-170)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-171)    "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-172)     "tokenUsage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-173)      "completionTokens": 17,
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-174)      "promptTokens": 72,
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-175)      "totalTokens": 89
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-176)     },
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-177)     "finish_reason": "tool_calls",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-178)     "system_fingerprint": "fp_fde2829a40"
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-179)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-180)    "tool_calls": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-181)     {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-182)      "name": "search",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-183)      "args": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-184)       "query": "current weather in San Francisco"
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-185)      },
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-186)      "type": "tool_call",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-187)      "id": "call_OsKnTv2psf879eeJ9vx5GeoY"
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-188)     }
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-189)    ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-190)    "invalid_tool_calls": []
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-191)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-192)  ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-193) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-194) next: [ 'tools' ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-195) tasks: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-196)  {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-197)   id: '767116b0-55b6-5af4-8f74-ce45fb6e31ed',
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-198)   name: 'tools',
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-199)   interrupts: []
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-200)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-201) ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-202) metadata: { source: 'loop', writes: { agent: [Object] }, step: 1 },
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-203) config: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-204)  configurable: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-205)   thread_id: 'conversation-num-1',
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-206)   checkpoint_ns: '',
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-207)   checkpoint_id: '1ef69ab6-9455-6410-8001-1c78a97f63e6'
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-208)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-209) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-210) createdAt: '2024-09-03T04:17:19.825Z',
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-211) parentConfig: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-212)  configurable: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-213)   thread_id: 'conversation-num-1',
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-214)   checkpoint_ns: '',
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-215)   checkpoint_id: '1ef69ab6-8c4b-6261-8000-c51e5807fbcd'
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-216)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-217) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-218)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-219)--
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-220){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-221) values: { messages: [ [Object] ] },
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-222) next: [ 'agent' ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-223) tasks: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-224)  {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-225)   id: '5b0ed7d1-1bb7-5d78-b4fc-7a8ed40e7291',
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-226)   name: 'agent',
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-227)   interrupts: []
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-228)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-229) ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-230) metadata: { source: 'loop', writes: null, step: 0 },
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-231) config: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-232)  configurable: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-233)   thread_id: 'conversation-num-1',
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-234)   checkpoint_ns: '',
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-235)   checkpoint_id: '1ef69ab6-8c4b-6261-8000-c51e5807fbcd'
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-236)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-237) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-238) createdAt: '2024-09-03T04:17:18.982Z',
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-239) parentConfig: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-240)  configurable: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-241)   thread_id: 'conversation-num-1',
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-242)   checkpoint_ns: '',
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-243)   checkpoint_id: '1ef69ab6-8c4b-6260-ffff-6ec582916c42'
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-244)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-245) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-246)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-247)--
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-248){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-249) values: {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-250) next: [ '__start__' ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-251) tasks: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-252)  {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-253)   id: 'a4250d5c-d025-5da1-b588-cae2b3f4a8c7',
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-254)   name: '__start__',
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-255)   interrupts: []
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-256)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-257) ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-258) metadata: { source: 'input', writes: { messages: [Array] }, step: -1 },
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-259) config: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-260)  configurable: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-261)   thread_id: 'conversation-num-1',
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-262)   checkpoint_ns: '',
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-263)   checkpoint_id: '1ef69ab6-8c4b-6260-ffff-6ec582916c42'
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-264)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-265) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-266) createdAt: '2024-09-03T04:17:18.982Z',
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-267) parentConfig: undefined
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-268)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-23-269)--

```


## Replay a past state[¶](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#replay-a-past-state "Permanent link")

To replay from this place we just need to pass its config back to the agent.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-24-1)forawait(
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-24-2)const{messages}ofawaitgraphWithInterrupt.stream(null,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-24-3)...toReplay.config,
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-24-4)streamMode:"values",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-24-5)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-24-6)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-24-7)letmsg=messages[messages?.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-24-8)if(msg?.content){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-24-9)console.log(msg.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-24-10)}elseif(msg?.tool_calls?.length>0){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-24-11)console.log(msg.tool_calls);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-24-12)}else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-24-13)console.log(msg);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-24-14)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-24-15)console.log("-----\n");
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-24-16)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-25-1)Cold, with a low of 13 ℃
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-25-2)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-25-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-25-4)The current weather in San Francisco is cold, with a low of 13°C.
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-25-5)-----

```


## Branch off a past state[¶](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#branch-off-a-past-state "Permanent link")

Using LangGraph's checkpointing, you can do more than just replay past states. You can branch off previous locations to let the agent explore alternate trajectories or to let a user "version control" changes in a workflow.

#### First, update a previous checkpoint[¶](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#first-update-a-previous-checkpoint "Permanent link")

Updating the state will create a **new** snapshot by applying the update to the previous checkpoint. Let's **add a tool message** to simulate calling the tool.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-26-1)consttool_calls=
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-26-2)toReplay.values.messages[toReplay.values.messages.length-1].tool_calls;
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-26-3)constbranchConfig=awaitgraphWithInterrupt.updateState(
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-26-4)toReplay.config,
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-26-5){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-26-6)messages:[
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-26-7){role:"tool",content:"It's sunny out, with a high of 38 ℃.",tool_call_id:tool_calls[0].id},
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-26-8)],
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-26-9)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-26-10)// Updates are applied "as if" they were coming from a node. By default,
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-26-11)// the updates will come from the last node to run. In our case, we want to treat
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-26-12)// this update as if it came from the tools node, so that the next node to run will be
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-26-13)// the agent.
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-26-14)"tools",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-26-15));
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-26-16)
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-26-17)constbranchState=awaitgraphWithInterrupt.getState(branchConfig);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-26-18)console.log(branchState.values);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-26-19)console.log(branchState.next);

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-27-1){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-27-2) messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-27-3)  {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-27-4)   role: 'user',
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-27-5)   content: "What's the weather like in SF currently?"
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-27-6)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-27-7)  AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-27-8)   "id": "chatcmpl-A3FGhKzOZs0GYZ2yalNOCQZyPgbcp",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-27-9)   "content": "",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-27-10)   "additional_kwargs": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-27-11)    "tool_calls": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-27-12)     {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-27-13)      "id": "call_OsKnTv2psf879eeJ9vx5GeoY",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-27-14)      "type": "function",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-27-15)      "function": "[Object]"
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-27-16)     }
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-27-17)    ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-27-18)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-27-19)   "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-27-20)    "tokenUsage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-27-21)     "completionTokens": 17,
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-27-22)     "promptTokens": 72,
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-27-23)     "totalTokens": 89
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-27-24)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-27-25)    "finish_reason": "tool_calls",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-27-26)    "system_fingerprint": "fp_fde2829a40"
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-27-27)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-27-28)   "tool_calls": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-27-29)    {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-27-30)     "name": "search",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-27-31)     "args": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-27-32)      "query": "current weather in San Francisco"
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-27-33)     },
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-27-34)     "type": "tool_call",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-27-35)     "id": "call_OsKnTv2psf879eeJ9vx5GeoY"
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-27-36)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-27-37)   ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-27-38)   "invalid_tool_calls": []
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-27-39)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-27-40)  {
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-27-41)   role: 'tool',
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-27-42)   content: "It's sunny out, with a high of 38 ℃.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-27-43)   tool_call_id: 'call_OsKnTv2psf879eeJ9vx5GeoY'
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-27-44)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-27-45) ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-27-46)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-27-47)[ 'agent' ]

```


#### Now you can run from this branch[¶](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#now-you-can-run-from-this-branch "Permanent link")

Just use the updated config (containing the new checkpoint ID). The trajectory will follow the new branch.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-28-1)forawait(
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-28-2)const{messages}ofawaitgraphWithInterrupt.stream(null,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-28-3)...branchConfig,
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-28-4)streamMode:"values",
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-28-5)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-28-6)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-28-7)letmsg=messages[messages?.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-28-8)if(msg?.content){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-28-9)console.log(msg.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-28-10)}elseif(msg?.tool_calls?.length>0){
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-28-11)console.log(msg.tool_calls);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-28-12)}else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-28-13)console.log(msg);
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-28-14)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-28-15)console.log("-----\n");
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-28-16)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-29-1)The current weather in San Francisco is sunny, with a high of 38°C.
[](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__codelineno-29-2)-----

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to wait for user input (Functional API)  ](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/) [ Next  Review Tool Calls  ](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
