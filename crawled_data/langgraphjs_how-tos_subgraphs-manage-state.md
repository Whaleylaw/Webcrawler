---
url: https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#how-to-view-and-update-state-in-subgraphs)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to view and update state in subgraphs 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/?q= "Share")

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
            * [ How to add and use subgraphs  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/)
            * How to view and update state in subgraphs  [ How to view and update state in subgraphs  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#setup)
              * [ Define subgraph  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#define-subgraph)
              * [ Define parent graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#define-parent-graph)
              * [ Resuming from breakpoints  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#resuming-from-breakpoints)
                * [ Resuming from specific subgraph node  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#resuming-from-specific-subgraph-node)
              * [ Modifying state  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#modifying-state)
                * [ Update the state of a subgraph  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#update-the-state-of-a-subgraph)
                * [ Acting as a subgraph node  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#acting-as-a-subgraph-node)
                * [ Acting as the entire subgraph  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#acting-as-the-entire-subgraph)
              * [ Double nested subgraphs  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#double-nested-subgraphs)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#setup)
  * [ Define subgraph  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#define-subgraph)
  * [ Define parent graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#define-parent-graph)
  * [ Resuming from breakpoints  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#resuming-from-breakpoints)
    * [ Resuming from specific subgraph node  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#resuming-from-specific-subgraph-node)
  * [ Modifying state  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#modifying-state)
    * [ Update the state of a subgraph  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#update-the-state-of-a-subgraph)
    * [ Acting as a subgraph node  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#acting-as-a-subgraph-node)
    * [ Acting as the entire subgraph  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#acting-as-the-entire-subgraph)
  * [ Double nested subgraphs  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#double-nested-subgraphs)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
  5. [ Subgraphs  ](https://langchain-ai.github.io/langgraphjs/how-tos#subgraphs)



# How to view and update state in subgraphs[¶](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#how-to-view-and-update-state-in-subgraphs "Permanent link")

Prerequisites

This guide assumes familiarity with the following: 

  * [ Subgraphs ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#subgraphs)
  * [ Human-in-the-loop ](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/)
  * [ State ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#state)



Once you add [persistence](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence), you can view and update the state of the subgraph at any point in time. This enables human-in-the-loop interaction patterns such as:

  * You can surface a state during an interrupt to a user to let them accept an action.
  * You can rewind the subgraph to reproduce or avoid issues.
  * You can modify the state to let the user better control its actions.



This guide shows how you can do this.

## Setup[¶](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#setup "Permanent link")

First we need to install required packages:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-0-1)npminstall@langchain/langgraph@langchain/core@langchain/openai

```


Next, we need to set API keys for OpenAI (the provider we'll use for this guide):

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-1-1)// process.env.OPENAI_API_KEY = "YOUR_API_KEY";

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Define subgraph[¶](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#define-subgraph "Permanent link")

First, let's set up our subgraph. For this, we will create a simple graph that can get the weather for a specific city. We will compile this graph with a [breakpoint](https://langchain-ai.github.io/langgraphjs/how-tos/human_in_the_loop/breakpoints/) before the `weather_node`:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-2-1)import{z}from"zod";
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-2-2)import{tool}from"@langchain/core/tools";
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-2-3)import{ChatOpenAI}from"@langchain/openai";
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-2-4)import{StateGraph,MessagesAnnotation,Annotation}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-2-5)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-2-6)constgetWeather=tool(async({city})=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-2-7)return`It's sunny in ${city}`;
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-2-8)},{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-2-9)name:"get_weather",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-2-10)description:"Get the weather for a specific city",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-2-11)schema:z.object({
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-2-12)city:z.string().describe("A city name")
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-2-13)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-2-14)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-2-15)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-2-16)constrawModel=newChatOpenAI({model:"gpt-4o-mini"});
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-2-17)constmodel=rawModel.withStructuredOutput(getWeather);
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-2-18)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-2-19)// Extend the base MessagesAnnotation state with another field
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-2-20)constSubGraphAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-2-21)...MessagesAnnotation.spec,
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-2-22)city:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-2-23)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-2-24)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-2-25)constmodelNode=async(state:typeofSubGraphAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-2-26)constresult=awaitmodel.invoke(state.messages);
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-2-27)return{city:result.city};
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-2-28)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-2-29)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-2-30)constweatherNode=async(state:typeofSubGraphAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-2-31)constresult=awaitgetWeather.invoke({city:state.city});
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-2-32)return{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-2-33)messages:[
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-2-34){
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-2-35)role:"assistant",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-2-36)content:result,
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-2-37)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-2-38)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-2-39)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-2-40)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-2-41)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-2-42)constsubgraph=newStateGraph(SubGraphAnnotation)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-2-43).addNode("modelNode",modelNode)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-2-44).addNode("weatherNode",weatherNode)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-2-45).addEdge("__start__","modelNode")
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-2-46).addEdge("modelNode","weatherNode")
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-2-47).addEdge("weatherNode","__end__")
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-2-48).compile({interruptBefore:["weatherNode"]});

```


## Define parent graph[¶](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#define-parent-graph "Permanent link")

We can now setup the overall graph. This graph will first route to the subgraph if it needs to get the weather, otherwise it will route to a normal LLM.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-3-1)import{MemorySaver}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-3-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-3-3)constmemory=newMemorySaver();
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-3-4)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-3-5)constRouterStateAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-3-6)...MessagesAnnotation.spec,
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-3-7)route:Annotation<"weather"|"other">,
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-3-8)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-3-9)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-3-10)constrouterModel=rawModel.withStructuredOutput(
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-3-11)z.object({
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-3-12)route:z.enum(["weather","other"]).describe("A step that should execute next to based on the currnet input")
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-3-13)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-3-14){
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-3-15)name:"router"
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-3-16)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-3-17));
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-3-18)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-3-19)constrouterNode=async(state:typeofRouterStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-3-20)constsystemMessage={
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-3-21)role:"system",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-3-22)content:"Classify the incoming query as either about weather or not.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-3-23)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-3-24)constmessages=[systemMessage,...state.messages]
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-3-25)const{route}=awaitrouterModel.invoke(messages);
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-3-26)return{route};
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-3-27)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-3-28)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-3-29)constnormalLLMNode=async(state:typeofRouterStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-3-30)constresponseMessage=awaitrawModel.invoke(state.messages);
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-3-31)return{messages:[responseMessage]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-3-32)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-3-33)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-3-34)constrouteAfterPrediction=async(state:typeofRouterStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-3-35)if(state.route==="weather"){
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-3-36)return"weatherGraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-3-37)}else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-3-38)return"normalLLMNode";
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-3-39)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-3-40)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-3-41)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-3-42)constgraph=newStateGraph(RouterStateAnnotation)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-3-43).addNode("routerNode",routerNode)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-3-44).addNode("normalLLMNode",normalLLMNode)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-3-45).addNode("weatherGraph",subgraph)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-3-46).addEdge("__start__","routerNode")
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-3-47).addConditionalEdges("routerNode",routeAfterPrediction)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-3-48).addEdge("normalLLMNode","__end__")
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-3-49).addEdge("weatherGraph","__end__")
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-3-50).compile({checkpointer:memory});

```


Here's a diagram of the graph we just created:

![](https://langchain-ai.github.io/langgraphjs/how-tos/img/single-nested-subgraph.jpeg)

Let's test this out with a normal query to make sure it works as intended!

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-4-1)constconfig={configurable:{thread_id:"1"}};
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-4-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-4-3)constinputs={messages:[{role:"user",content:"hi!"}]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-4-4)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-4-5)conststream=awaitgraph.stream(inputs,{...config,streamMode:"updates"});
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-4-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-4-7)forawait(constupdateofstream){
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-4-8)console.log(update);
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-4-9)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-5-1){ routerNode: { route: 'other' } }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-5-2){
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-5-3) normalLLMNode: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-5-4)  messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-5-5)   AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-5-6)    "id": "chatcmpl-ABtbbiB5N3Uue85UNrFUjw5KhGaud",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-5-7)    "content": "Hello! How can I assist you today?",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-5-8)    "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-5-9)    "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-5-10)     "tokenUsage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-5-11)      "completionTokens": 9,
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-5-12)      "promptTokens": 9,
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-5-13)      "totalTokens": 18
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-5-14)     },
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-5-15)     "finish_reason": "stop",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-5-16)     "system_fingerprint": "fp_f85bea6784"
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-5-17)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-5-18)    "tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-5-19)    "invalid_tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-5-20)    "usage_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-5-21)     "input_tokens": 9,
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-5-22)     "output_tokens": 9,
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-5-23)     "total_tokens": 18
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-5-24)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-5-25)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-5-26)  ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-5-27) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-5-28)}

```


Great! We didn't ask about the weather, so we got a normal response from the LLM. 

## Resuming from breakpoints[¶](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#resuming-from-breakpoints "Permanent link")

Let's now look at what happens with breakpoints. Let's invoke it with a query that should get routed to the weather subgraph where we have the interrupt node.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-6-1)constconfig2={configurable:{thread_id:"2"}};
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-6-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-6-3)conststreamWithBreakpoint=awaitgraph.stream({
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-6-4)messages:[{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-6-5)role:"user",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-6-6)content:"what's the weather in sf"
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-6-7)}]
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-6-8)},{...config2,streamMode:"updates"});
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-6-9)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-6-10)forawait(constupdateofstreamWithBreakpoint){
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-6-11)console.log(update);
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-6-12)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-7-1){ routerNode: { route: 'weather' } }

```


Note that the graph stream doesn't include subgraph events. If we want to stream subgraph events, we can pass `subgraphs: True` in our config and get back subgraph events like so: 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-8-1)conststreamWithSubgraphs=awaitgraph.stream({
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-8-2)messages:[{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-8-3)role:"user",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-8-4)content:"what's the weather in sf"
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-8-5)}]
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-8-6)},{configurable:{thread_id:"3"},streamMode:"updates",subgraphs:true});
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-8-7)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-8-8)forawait(constupdateofstreamWithSubgraphs){
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-8-9)console.log(update);
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-8-10)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-9-1)[ [], { routerNode: { route: 'weather' } } ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-9-2)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-9-3) [ 'weatherGraph:ec67e50f-d29c-5dee-8a80-08723a937de0' ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-9-4) { modelNode: { city: 'San Francisco' } }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-9-5)]

```


This time, we see the format of the streamed updates has changed. It's now a tuple where the first item is a nested array with information about the subgraph and the second is the actual state update. If we get the state now, we can see that it's paused on `weatherGraph` as expected: 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-10-1)conststate=awaitgraph.getState({configurable:{thread_id:"3"}})
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-10-2)state.next

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-11-1)[ 'weatherGraph' ]

```


If we look at the pending tasks for our current state, we can see that we have one task named `weatherGraph`, which corresponds to the subgraph task. 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-12-1)JSON.stringify(state.tasks,null,2);

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-13-1)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-13-2) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-13-3)  "id": "ec67e50f-d29c-5dee-8a80-08723a937de0",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-13-4)  "name": "weatherGraph",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-13-5)  "path": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-13-6)   "__pregel_pull",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-13-7)   "weatherGraph"
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-13-8)  ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-13-9)  "interrupts": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-13-10)  "state": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-13-11)   "configurable": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-13-12)    "thread_id": "3",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-13-13)    "checkpoint_ns": "weatherGraph:ec67e50f-d29c-5dee-8a80-08723a937de0"
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-13-14)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-13-15)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-13-16) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-13-17)]

```


However since we got the state using the config of the parent graph, we don't have access to the subgraph state. If you look at the `state` value of the task above you will note that it is simply the configuration of the parent graph. If we want to actually populate the subgraph state, we can pass in `subgraphs: True` to the second parameter of `getState` like so: 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-14-1)conststateWithSubgraphs=awaitgraph.getState({configurable:{thread_id:"3"}},{subgraphs:true})
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-14-2)JSON.stringify(stateWithSubgraphs.tasks,null,2)

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-1)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-2) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-3)  "id": "ec67e50f-d29c-5dee-8a80-08723a937de0",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-4)  "name": "weatherGraph",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-5)  "path": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-6)   "__pregel_pull",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-7)   "weatherGraph"
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-8)  ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-9)  "interrupts": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-10)  "state": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-11)   "values": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-12)    "messages": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-13)     {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-14)      "lc": 1,
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-15)      "type": "constructor",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-16)      "id": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-17)       "langchain_core",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-18)       "messages",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-19)       "HumanMessage"
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-20)      ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-21)      "kwargs": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-22)       "content": "what's the weather in sf",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-23)       "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-24)       "response_metadata": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-25)       "id": "094b6752-6bea-4b43-b837-c6b0bb6a4c44"
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-26)      }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-27)     }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-28)    ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-29)    "city": "San Francisco"
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-30)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-31)   "next": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-32)    "weatherNode"
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-33)   ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-34)   "tasks": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-35)    {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-36)     "id": "2f2f8b8f-6a99-5225-8ff2-b6c49c3e9caf",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-37)     "name": "weatherNode",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-38)     "path": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-39)      "__pregel_pull",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-40)      "weatherNode"
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-41)     ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-42)     "interrupts": []
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-43)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-44)   ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-45)   "metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-46)    "source": "loop",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-47)    "writes": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-48)     "modelNode": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-49)      "city": "San Francisco"
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-50)     }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-51)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-52)    "step": 1,
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-53)    "parents": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-54)     "": "1ef7c6ba-3d36-65e0-8001-adc1f8841274"
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-55)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-56)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-57)   "config": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-58)    "configurable": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-59)     "thread_id": "3",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-60)     "checkpoint_id": "1ef7c6ba-4503-6700-8001-61e828d1c772",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-61)     "checkpoint_ns": "weatherGraph:ec67e50f-d29c-5dee-8a80-08723a937de0",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-62)     "checkpoint_map": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-63)      "": "1ef7c6ba-3d36-65e0-8001-adc1f8841274",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-64)      "weatherGraph:ec67e50f-d29c-5dee-8a80-08723a937de0": "1ef7c6ba-4503-6700-8001-61e828d1c772"
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-65)     }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-66)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-67)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-68)   "createdAt": "2024-09-27T00:58:43.184Z",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-69)   "parentConfig": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-70)    "configurable": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-71)     "thread_id": "3",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-72)     "checkpoint_ns": "weatherGraph:ec67e50f-d29c-5dee-8a80-08723a937de0",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-73)     "checkpoint_id": "1ef7c6ba-3d3b-6400-8000-fe27ae37c785"
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-74)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-75)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-76)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-77) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-15-78)]

```


Now we have access to the subgraph state! 

To resume execution, we can just invoke the outer graph as normal:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-16-1)constresumedStream=awaitgraph.stream(null,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-16-2)configurable:{thread_id:"3"},
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-16-3)streamMode:"values",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-16-4)subgraphs:true,
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-16-5)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-16-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-16-7)forawait(constupdateofresumedStream){
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-16-8)console.log(update);
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-16-9)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-1)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-2) [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-3) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-4)  messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-5)   HumanMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-6)    "id": "094b6752-6bea-4b43-b837-c6b0bb6a4c44",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-7)    "content": "what's the weather in sf",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-8)    "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-9)    "response_metadata": {}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-10)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-11)  ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-12)  route: 'weather'
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-13) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-14)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-15)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-16) [ 'weatherGraph:ec67e50f-d29c-5dee-8a80-08723a937de0' ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-17) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-18)  messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-19)   HumanMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-20)    "id": "094b6752-6bea-4b43-b837-c6b0bb6a4c44",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-21)    "content": "what's the weather in sf",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-22)    "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-23)    "response_metadata": {}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-24)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-25)  ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-26)  city: 'San Francisco'
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-27) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-28)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-29)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-30) [ 'weatherGraph:ec67e50f-d29c-5dee-8a80-08723a937de0' ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-31) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-32)  messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-33)   HumanMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-34)    "id": "094b6752-6bea-4b43-b837-c6b0bb6a4c44",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-35)    "content": "what's the weather in sf",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-36)    "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-37)    "response_metadata": {}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-38)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-39)   AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-40)    "id": "55d7a03f-876a-4887-9418-027321e747c7",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-41)    "content": "It's sunny in San Francisco",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-42)    "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-43)    "response_metadata": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-44)    "tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-45)    "invalid_tool_calls": []
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-46)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-47)  ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-48)  city: 'San Francisco'
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-49) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-50)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-51)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-52) [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-53) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-54)  messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-55)   HumanMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-56)    "id": "094b6752-6bea-4b43-b837-c6b0bb6a4c44",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-57)    "content": "what's the weather in sf",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-58)    "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-59)    "response_metadata": {}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-60)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-61)   AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-62)    "id": "55d7a03f-876a-4887-9418-027321e747c7",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-63)    "content": "It's sunny in San Francisco",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-64)    "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-65)    "response_metadata": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-66)    "tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-67)    "invalid_tool_calls": []
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-68)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-69)  ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-70)  route: 'weather'
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-71) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-17-72)]

```


### Resuming from specific subgraph node[¶](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#resuming-from-specific-subgraph-node "Permanent link")

In the example above, we were replaying from the outer graph - which automatically replayed the subgraph from whatever state it was in previously (paused before the `weatherNode` in our case), but it is also possible to replay from inside a subgraph. In order to do so, we need to get the configuration from the exact subgraph state that we want to replay from.

We can do this by exploring the state history of the subgraph, and selecting the state before `modelNode` - which we can do by filtering on the `.next` parameter.

To get the state history of the subgraph, we need to first pass in the parent graph state before the subgraph:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-18-1)letparentGraphStateBeforeSubgraph;
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-18-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-18-3)consthistories=awaitgraph.getStateHistory({configurable:{thread_id:"3"}});
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-18-4)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-18-5)forawait(consthistoryEntryofhistories){
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-18-6)if(historyEntry.next[0]==="weatherGraph"){
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-18-7)parentGraphStateBeforeSubgraph=historyEntry;
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-18-8)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-18-9)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-19-1)letsubgraphStateBeforeModelNode;
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-19-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-19-3)constsubgraphHistories=awaitgraph.getStateHistory(parentGraphStateBeforeSubgraph.tasks[0].state);
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-19-4)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-19-5)forawait(constsubgraphHistoryEntryofsubgraphHistories){
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-19-6)if(subgraphHistoryEntry.next[0]==="modelNode"){
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-19-7)subgraphStateBeforeModelNode=subgraphHistoryEntry;
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-19-8)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-19-9)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-19-10)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-19-11)console.log(subgraphStateBeforeModelNode);

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-20-1){
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-20-2) values: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-20-3)  messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-20-4)   HumanMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-20-5)    "id": "094b6752-6bea-4b43-b837-c6b0bb6a4c44",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-20-6)    "content": "what's the weather in sf",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-20-7)    "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-20-8)    "response_metadata": {}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-20-9)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-20-10)  ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-20-11) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-20-12) next: [ 'modelNode' ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-20-13) tasks: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-20-14)  {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-20-15)   id: '6d0d44fd-279b-56b0-8160-8f4929f9bfe6',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-20-16)   name: 'modelNode',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-20-17)   path: [Array],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-20-18)   interrupts: [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-20-19)   state: undefined
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-20-20)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-20-21) ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-20-22) metadata: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-20-23)  source: 'loop',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-20-24)  writes: null,
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-20-25)  step: 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-20-26)  parents: { '': '1ef7c6ba-3d36-65e0-8001-adc1f8841274' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-20-27) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-20-28) config: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-20-29)  configurable: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-20-30)   thread_id: '3',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-20-31)   checkpoint_ns: 'weatherGraph:ec67e50f-d29c-5dee-8a80-08723a937de0',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-20-32)   checkpoint_id: '1ef7c6ba-3d3b-6400-8000-fe27ae37c785',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-20-33)   checkpoint_map: [Object]
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-20-34)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-20-35) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-20-36) createdAt: '2024-09-27T00:58:42.368Z',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-20-37) parentConfig: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-20-38)  configurable: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-20-39)   thread_id: '3',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-20-40)   checkpoint_ns: 'weatherGraph:ec67e50f-d29c-5dee-8a80-08723a937de0',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-20-41)   checkpoint_id: '1ef7c6ba-3d38-6cf1-ffff-b3912beb00b9'
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-20-42)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-20-43) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-20-44)}

```


This pattern can be extended no matter how many levels deep. 

We can confirm that we have gotten the correct state by comparing the `.next` parameter of the `subgraphStateBeforeModelNode`.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-21-1)subgraphStateBeforeModelNode.next;

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-22-1)[ 'modelNode' ]

```


Perfect! We have gotten the correct state snaphshot, and we can now resume from the `modelNode` inside of our subgraph: 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-23-1)constresumeSubgraphStream=awaitgraph.stream(null,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-23-2)...subgraphStateBeforeModelNode.config,
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-23-3)streamMode:"updates",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-23-4)subgraphs:true
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-23-5)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-23-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-23-7)forawait(constvalueofresumeSubgraphStream){
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-23-8)console.log(value);
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-23-9)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-24-1)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-24-2) [ 'weatherGraph:ec67e50f-d29c-5dee-8a80-08723a937de0' ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-24-3) { modelNode: { city: 'San Francisco' } }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-24-4)]

```


We can see that it reruns the `modelNode` and breaks right before the `weatherNode` as expected. 

This subsection has shown how you can replay from any node, no matter how deeply nested it is inside your graph - a powerful tool for testing how deterministic your agent is.

## Modifying state[¶](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#modifying-state "Permanent link")

### Update the state of a subgraph[¶](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#update-the-state-of-a-subgraph "Permanent link")

What if we want to modify the state of a subgraph? We can do this similarly to how we [update the state of normal graphs](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/). We just need to ensure we pass the config of the subgraph to `updateState`. Let's run our graph as before:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-25-1)constgraphStream=awaitgraph.stream({
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-25-2)messages:[{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-25-3)role:"user",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-25-4)content:"what's the weather in sf"
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-25-5)}],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-25-6)},{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-25-7)configurable:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-25-8)thread_id:"4",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-25-9)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-25-10)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-25-11)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-25-12)forawait(constupdateofgraphStream){
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-25-13)console.log(update);
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-25-14)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-26-1){ routerNode: { route: 'weather' } }

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-27-1)constouterGraphState=awaitgraph.getState({
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-27-2)configurable:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-27-3)thread_id:"4",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-27-4)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-27-5)},{subgraphs:true})
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-27-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-27-7)console.log(outerGraphState.tasks[0].state);

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-28-1){
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-28-2) values: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-28-3)  messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-28-4)   HumanMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-28-5)    "id": "07ed1a38-13a9-4ec2-bc88-c4f6b713ec85",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-28-6)    "content": "what's the weather in sf",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-28-7)    "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-28-8)    "response_metadata": {}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-28-9)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-28-10)  ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-28-11)  city: 'San Francisco'
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-28-12) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-28-13) next: [ 'weatherNode' ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-28-14) tasks: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-28-15)  {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-28-16)   id: 'eabfbb82-6cf4-5ecd-932e-ed994ea44f23',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-28-17)   name: 'weatherNode',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-28-18)   path: [Array],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-28-19)   interrupts: [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-28-20)   state: undefined
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-28-21)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-28-22) ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-28-23) metadata: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-28-24)  source: 'loop',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-28-25)  writes: { modelNode: [Object] },
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-28-26)  step: 1,
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-28-27)  parents: { '': '1ef7c6ba-563f-60f0-8001-4fce0e78ef56' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-28-28) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-28-29) config: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-28-30)  configurable: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-28-31)   thread_id: '4',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-28-32)   checkpoint_id: '1ef7c6ba-5c71-6f90-8001-04f60f3c8173',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-28-33)   checkpoint_ns: 'weatherGraph:8d8c9278-bd2a-566a-b9e1-e72286634681',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-28-34)   checkpoint_map: [Object]
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-28-35)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-28-36) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-28-37) createdAt: '2024-09-27T00:58:45.641Z',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-28-38) parentConfig: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-28-39)  configurable: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-28-40)   thread_id: '4',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-28-41)   checkpoint_ns: 'weatherGraph:8d8c9278-bd2a-566a-b9e1-e72286634681',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-28-42)   checkpoint_id: '1ef7c6ba-5641-6800-8000-96bcde048fa6'
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-28-43)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-28-44) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-28-45)}

```


In order to update the state of the **inner** graph, we need to pass the config for the **inner** graph, which we can get by accessing calling `state.tasks[0].state.config` - since we interrupted inside the subgraph, the state of the task is just the state of the subgraph. 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-29-1)importtype{StateSnapshot}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-29-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-29-3)awaitgraph.updateState((outerGraphState.tasks[0].stateasStateSnapshot).config,{city:"la"});

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-30-1){
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-30-2) configurable: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-30-3)  thread_id: '4',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-30-4)  checkpoint_ns: 'weatherGraph:8d8c9278-bd2a-566a-b9e1-e72286634681',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-30-5)  checkpoint_id: '1ef7c6ba-5de0-62f0-8002-3618a75d1fce',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-30-6)  checkpoint_map: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-30-7)   '': '1ef7c6ba-563f-60f0-8001-4fce0e78ef56',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-30-8)   'weatherGraph:8d8c9278-bd2a-566a-b9e1-e72286634681': '1ef7c6ba-5de0-62f0-8002-3618a75d1fce'
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-30-9)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-30-10) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-30-11)}

```


We can now resume streaming the outer graph (which will resume the subgraph!) and check that we updated our search to use LA instead of SF. 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-31-1)constresumedStreamWithUpdatedState=awaitgraph.stream(null,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-31-2)configurable:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-31-3)thread_id:"4",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-31-4)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-31-5)streamMode:"updates",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-31-6)subgraphs:true,
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-31-7)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-31-8)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-31-9)forawait(constupdateofresumedStreamWithUpdatedState){
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-31-10)console.log(JSON.stringify(update,null,2));
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-31-11)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-1)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-2) [
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-3)  "weatherGraph:8d8c9278-bd2a-566a-b9e1-e72286634681"
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-4) ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-5) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-6)  "weatherNode": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-7)   "messages": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-8)    {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-9)     "role": "assistant",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-10)     "content": "It's sunny in la"
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-11)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-12)   ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-13)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-14) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-15)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-16)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-17) [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-18) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-19)  "weatherGraph": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-20)   "messages": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-21)    {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-22)     "lc": 1,
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-23)     "type": "constructor",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-24)     "id": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-25)      "langchain_core",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-26)      "messages",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-27)      "HumanMessage"
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-28)     ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-29)     "kwargs": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-30)      "content": "what's the weather in sf",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-31)      "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-32)      "response_metadata": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-33)      "id": "07ed1a38-13a9-4ec2-bc88-c4f6b713ec85"
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-34)     }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-35)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-36)    {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-37)     "lc": 1,
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-38)     "type": "constructor",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-39)     "id": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-40)      "langchain_core",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-41)      "messages",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-42)      "AIMessage"
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-43)     ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-44)     "kwargs": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-45)      "content": "It's sunny in la",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-46)      "tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-47)      "invalid_tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-48)      "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-49)      "response_metadata": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-50)      "id": "94c29f6c-38b3-420f-a9fb-bd85548f0c03"
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-51)     }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-52)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-53)   ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-54)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-55) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-32-56)]

```


Fantastic! The AI responded with "It's sunny in LA!" as we expected. 

### Acting as a subgraph node[¶](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#acting-as-a-subgraph-node "Permanent link")

Instead of editing the state before `weatherNode` in the `weatherGraph` subgraph, another way we could update the state is by acting as the `weatherNode` ourselves. We can do this by passing the subgraph config along with a node name passed as a third positional argument, which allows us to update the state as if we are the node we specify.

We will set an interrupt before the `weatherNode` and then using the update state function as the `weatherNode`, the graph itself never calls `weatherNode` directly but instead we decide what the output of `weatherNode` should be.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-33-1)conststreamWithAsNode=awaitgraph.stream({
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-33-2)messages:[{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-33-3)role:"user",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-33-4)content:"What's the weather in sf",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-33-5)}]
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-33-6)},{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-33-7)configurable:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-33-8)thread_id:"14",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-33-9)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-33-10)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-33-11)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-33-12)forawait(constupdateofstreamWithAsNode){
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-33-13)console.log(update);
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-33-14)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-33-15)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-33-16)// Graph execution should stop before the weather node
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-33-17)console.log("interrupted!");
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-33-18)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-33-19)constinterruptedState=awaitgraph.getState({
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-33-20)configurable:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-33-21)thread_id:"14",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-33-22)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-33-23)},{subgraphs:true});
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-33-24)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-33-25)console.log(interruptedState);
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-33-26)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-33-27)// We update the state by passing in the message we want returned from the weather node
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-33-28)// and make sure to pass `"weatherNode"` to signify that we want to act as this node.
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-33-29)awaitgraph.updateState((interruptedState.tasks[0].stateasStateSnapshot).config,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-33-30)messages:[{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-33-31)"role":"assistant",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-33-32)"content":"rainy"
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-33-33)}]
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-33-34)},"weatherNode");
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-33-35)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-33-36)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-33-37)constresumedStreamWithAsNode=awaitgraph.stream(null,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-33-38)configurable:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-33-39)thread_id:"14",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-33-40)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-33-41)streamMode:"updates",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-33-42)subgraphs:true,
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-33-43)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-33-44)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-33-45)forawait(constupdateofresumedStreamWithAsNode){
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-33-46)console.log(update);
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-33-47)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-33-48)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-33-49)console.log(awaitgraph.getState({
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-33-50)configurable:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-33-51)thread_id:"14",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-33-52)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-33-53)},{subgraphs:true}));

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-1){ routerNode: { route: 'weather' } }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-2)interrupted!
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-3){
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-4) values: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-5)  messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-6)   HumanMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-7)    "id": "90e9ff28-5b13-4e10-819a-31999efe303c",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-8)    "content": "What's the weather in sf",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-9)    "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-10)    "response_metadata": {}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-11)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-12)  ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-13)  route: 'weather'
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-14) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-15) next: [ 'weatherGraph' ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-16) tasks: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-17)  {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-18)   id: 'f421fca8-de9e-5683-87ab-6ea9bb8d6275',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-19)   name: 'weatherGraph',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-20)   path: [Array],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-21)   interrupts: [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-22)   state: [Object]
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-23)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-24) ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-25) metadata: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-26)  source: 'loop',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-27)  writes: { routerNode: [Object] },
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-28)  step: 1,
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-29)  parents: {}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-30) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-31) config: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-32)  configurable: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-33)   thread_id: '14',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-34)   checkpoint_id: '1ef7c6ba-63ac-68f1-8001-5f7ada5f98e8',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-35)   checkpoint_ns: ''
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-36)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-37) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-38) createdAt: '2024-09-27T00:58:46.399Z',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-39) parentConfig: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-40)  configurable: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-41)   thread_id: '14',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-42)   checkpoint_ns: '',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-43)   checkpoint_id: '1ef7c6ba-5f20-6020-8000-1ff649773a32'
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-44)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-45) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-46)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-47)[ [], { weatherGraph: { messages: [Array] } } ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-48){
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-49) values: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-50)  messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-51)   HumanMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-52)    "id": "90e9ff28-5b13-4e10-819a-31999efe303c",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-53)    "content": "What's the weather in sf",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-54)    "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-55)    "response_metadata": {}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-56)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-57)   AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-58)    "id": "af761e6d-9f6a-4467-9a3c-489bed3fbad7",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-59)    "content": "rainy",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-60)    "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-61)    "response_metadata": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-62)    "tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-63)    "invalid_tool_calls": []
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-64)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-65)  ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-66)  route: 'weather'
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-67) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-68) next: [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-69) tasks: [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-70) metadata: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-71)  source: 'loop',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-72)  writes: { weatherGraph: [Object] },
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-73)  step: 2,
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-74)  parents: {}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-75) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-76) config: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-77)  configurable: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-78)   thread_id: '14',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-79)   checkpoint_id: '1ef7c6ba-69e6-6cc0-8002-1751fc5bdd8f',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-80)   checkpoint_ns: ''
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-81)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-82) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-83) createdAt: '2024-09-27T00:58:47.052Z',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-84) parentConfig: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-85)  configurable: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-86)   thread_id: '14',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-87)   checkpoint_ns: '',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-88)   checkpoint_id: '1ef7c6ba-63ac-68f1-8001-5f7ada5f98e8'
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-89)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-90) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-34-91)}

```


Perfect! The agent responded with the message we passed in ourselves, and identified the weather in SF as `rainy` instead of `sunny`. 

### Acting as the entire subgraph[¶](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#acting-as-the-entire-subgraph "Permanent link")

Lastly, we could also update the graph just acting as the **entire** subgraph. This is similar to the case above but instead of acting as just the `weatherNode` we are acting as the entire `weatherGraph` subgraph. This is done by passing in the normal graph config as well as the `asNode` argument, where we specify the we are acting as the entire subgraph node.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-35-1)constentireSubgraphExampleStream=awaitgraph.stream({
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-35-2)messages:[
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-35-3){
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-35-4)role:"user",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-35-5)content:"what's the weather in sf"
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-35-6)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-35-7)],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-35-8)},{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-35-9)configurable:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-35-10)thread_id:"8",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-35-11)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-35-12)streamMode:"updates",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-35-13)subgraphs:true,
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-35-14)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-35-15)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-35-16)forawait(constupdateofentireSubgraphExampleStream){
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-35-17)console.log(update);
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-35-18)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-35-19)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-35-20)// Graph execution should stop before the weather node
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-35-21)console.log("interrupted!");
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-35-22)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-35-23)// We update the state by passing in the message we want returned from the weather graph.
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-35-24)// Note that we don't need to pass in the subgraph config, since we aren't updating the state inside the subgraph
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-35-25)awaitgraph.updateState({
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-35-26)configurable:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-35-27)thread_id:"8",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-35-28)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-35-29)},{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-35-30)messages:[{role:"assistant",content:"rainy"}]
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-35-31)},"weatherGraph");
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-35-32)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-35-33)constresumedEntireSubgraphExampleStream=awaitgraph.stream(null,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-35-34)configurable:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-35-35)thread_id:"8",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-35-36)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-35-37)streamMode:"updates",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-35-38)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-35-39)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-35-40)forawait(constupdateofresumedEntireSubgraphExampleStream){
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-35-41)console.log(update);
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-35-42)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-35-43)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-35-44)constcurrentStateAfterUpdate=awaitgraph.getState({
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-35-45)configurable:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-35-46)thread_id:"8",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-35-47)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-35-48)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-35-49)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-35-50)console.log(currentStateAfterUpdate.values.messages);

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-36-1)[ [], { routerNode: { route: 'weather' } } ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-36-2)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-36-3) [ 'weatherGraph:db9c3bb2-5d27-5dae-a724-a8d702b33e86' ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-36-4) { modelNode: { city: 'San Francisco' } }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-36-5)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-36-6)interrupted!
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-36-7)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-36-8) HumanMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-36-9)  "id": "001282b0-ca2e-443f-b6ee-8cb16c81bf59",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-36-10)  "content": "what's the weather in sf",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-36-11)  "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-36-12)  "response_metadata": {}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-36-13) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-36-14) AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-36-15)  "id": "4b5d49cf-0f87-4ee8-b96f-eaa8716b9e9c",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-36-16)  "content": "rainy",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-36-17)  "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-36-18)  "response_metadata": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-36-19)  "tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-36-20)  "invalid_tool_calls": []
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-36-21) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-36-22)]

```


Again, the agent responded with "rainy" as we expected. 

## Double nested subgraphs[¶](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#double-nested-subgraphs "Permanent link")

This same functionality continues to work no matter the level of nesting. Here is an example of doing the same things with a double nested subgraph (although any level of nesting will work). We add another router on top of our already defined graphs.

First, let's recreate the graph we've been using above. This time we will compile it with no checkpointer, since it itself will be a subgraph!

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-37-1)constparentGraph=newStateGraph(RouterStateAnnotation)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-37-2).addNode("routerNode",routerNode)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-37-3).addNode("normalLLMNode",normalLLMNode)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-37-4).addNode("weatherGraph",subgraph)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-37-5).addEdge("__start__","routerNode")
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-37-6).addConditionalEdges("routerNode",routeAfterPrediction)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-37-7).addEdge("normalLLMNode","__end__")
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-37-8).addEdge("weatherGraph","__end__")
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-37-9).compile();

```


Now let's declare a "grandparent" graph that uses this graph as a subgraph:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-38-1)constcheckpointer=newMemorySaver();
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-38-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-38-3)constGrandfatherStateAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-38-4)...MessagesAnnotation.spec,
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-38-5)toContinue:Annotation<boolean>,
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-38-6)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-38-7)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-38-8)constgrandparentRouterNode=async(_state:typeofGrandfatherStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-38-9)// Dummy logic that will always continue
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-38-10)return{toContinue:true};
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-38-11)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-38-12)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-38-13)constgrandparentConditionalEdge=async(state:typeofGrandfatherStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-38-14)if(state.toContinue){
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-38-15)return"parentGraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-38-16)}else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-38-17)return"__end__";
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-38-18)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-38-19)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-38-20)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-38-21)constgrandparentGraph=newStateGraph(GrandfatherStateAnnotation)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-38-22).addNode("routerNode",grandparentRouterNode)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-38-23).addNode("parentGraph",parentGraph)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-38-24).addEdge("__start__","routerNode")
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-38-25).addConditionalEdges("routerNode",grandparentConditionalEdge)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-38-26).addEdge("parentGraph","__end__")
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-38-27).compile({checkpointer});

```


Here's a diagram showing what this looks like:

![](https://langchain-ai.github.io/langgraphjs/how-tos/img/doubly-nested-subgraph.jpeg)

If we run until the interrupt, we can now see that there are snapshots of the state of all three graphs

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-39-1)constgrandparentConfig={
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-39-2)configurable:{thread_id:"123"},
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-39-3)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-39-4)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-39-5)constgrandparentGraphStream=awaitgrandparentGraph.stream({
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-39-6)messages:[{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-39-7)role:"user",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-39-8)content:"what's the weather in SF"
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-39-9)}],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-39-10)},{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-39-11)...grandparentConfig,
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-39-12)streamMode:"updates",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-39-13)subgraphs:true
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-39-14)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-39-15)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-39-16)forawait(constupdateofgrandparentGraphStream){
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-39-17)console.log(update);
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-39-18)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-40-1)[ [], { routerNode: { toContinue: true } } ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-40-2)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-40-3) [ 'parentGraph:095bb8a9-77d3-5a0c-9a23-e1390dcf36bc' ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-40-4) { routerNode: { route: 'weather' } }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-40-5)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-40-6)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-40-7) [
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-40-8)  'parentGraph:095bb8a9-77d3-5a0c-9a23-e1390dcf36bc',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-40-9)  'weatherGraph:b1da376c-25a5-5aae-82da-4ff579f05d43'
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-40-10) ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-40-11) { modelNode: { city: 'San Francisco' } }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-40-12)]

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-41-1)constgrandparentGraphState=awaitgrandparentGraph.getState(
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-41-2)grandparentConfig,
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-41-3){subgraphs:true}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-41-4));
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-41-5)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-41-6)constparentGraphState=grandparentGraphState.tasks[0].stateasStateSnapshot;
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-41-7)constsubgraphState=parentGraphState.tasks[0].stateasStateSnapshot;
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-41-8)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-41-9)console.log("Grandparent State:");
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-41-10)console.log(grandparentGraphState.values);
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-41-11)console.log("---------------");
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-41-12)console.log("Parent Graph State:");
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-41-13)console.log(parentGraphState.values);
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-41-14)console.log("---------------");
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-41-15)console.log("Subgraph State:");
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-41-16)console.log(subgraphState.values);

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-42-1)Grandparent State:
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-42-2){
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-42-3) messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-42-4)  HumanMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-42-5)   "id": "5788e436-a756-4ff5-899a-82117a5c59c7",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-42-6)   "content": "what's the weather in SF",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-42-7)   "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-42-8)   "response_metadata": {}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-42-9)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-42-10) ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-42-11) toContinue: true
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-42-12)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-42-13)---------------
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-42-14)Parent Graph State:
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-42-15){
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-42-16) messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-42-17)  HumanMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-42-18)   "id": "5788e436-a756-4ff5-899a-82117a5c59c7",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-42-19)   "content": "what's the weather in SF",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-42-20)   "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-42-21)   "response_metadata": {}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-42-22)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-42-23) ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-42-24) route: 'weather'
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-42-25)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-42-26)---------------
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-42-27)Subgraph State:
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-42-28){
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-42-29) messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-42-30)  HumanMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-42-31)   "id": "5788e436-a756-4ff5-899a-82117a5c59c7",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-42-32)   "content": "what's the weather in SF",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-42-33)   "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-42-34)   "response_metadata": {}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-42-35)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-42-36) ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-42-37) city: 'San Francisco'
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-42-38)}

```


We can now continue, acting as the node three levels down 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-43-1)awaitgrandparentGraph.updateState(subgraphState.config,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-43-2)messages:[{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-43-3)role:"assistant",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-43-4)content:"rainy"
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-43-5)}]
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-43-6)},"weatherNode");
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-43-7)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-43-8)constupdatedGrandparentGraphStream=awaitgrandparentGraph.stream(null,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-43-9)...grandparentConfig,
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-43-10)streamMode:"updates",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-43-11)subgraphs:true,
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-43-12)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-43-13)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-43-14)forawait(constupdateofupdatedGrandparentGraphStream){
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-43-15)console.log(update);
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-43-16)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-43-17)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-43-18)console.log((awaitgrandparentGraph.getState(grandparentConfig)).values.messages)

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-44-1)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-44-2) [ 'parentGraph:095bb8a9-77d3-5a0c-9a23-e1390dcf36bc' ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-44-3) { weatherGraph: { messages: [Array] } }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-44-4)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-44-5)[ [], { parentGraph: { messages: [Array] } } ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-44-6)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-44-7) HumanMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-44-8)  "id": "5788e436-a756-4ff5-899a-82117a5c59c7",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-44-9)  "content": "what's the weather in SF",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-44-10)  "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-44-11)  "response_metadata": {}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-44-12) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-44-13) AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-44-14)  "id": "1c161973-9a9d-414d-b631-56791d85e2fb",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-44-15)  "content": "rainy",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-44-16)  "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-44-17)  "response_metadata": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-44-18)  "tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-44-19)  "invalid_tool_calls": []
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-44-20) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-44-21)]

```


As in the cases above, we can see that the AI responds with "rainy" as we expect. 

We can explore the state history to see how the state of the grandparent graph was updated at each step.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-45-1)constgrandparentStateHistories=awaitgrandparentGraph.getStateHistory(grandparentConfig);
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-45-2)forawait(conststateofgrandparentStateHistories){
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-45-3)console.log(state);
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-45-4)console.log("-----");
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-45-5)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-1){
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-2) values: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-3)  messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-4)   HumanMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-5)    "id": "5788e436-a756-4ff5-899a-82117a5c59c7",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-6)    "content": "what's the weather in SF",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-7)    "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-8)    "response_metadata": {}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-9)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-10)   AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-11)    "id": "1c161973-9a9d-414d-b631-56791d85e2fb",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-12)    "content": "rainy",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-13)    "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-14)    "response_metadata": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-15)    "tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-16)    "invalid_tool_calls": []
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-17)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-18)  ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-19)  toContinue: true
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-20) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-21) next: [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-22) tasks: [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-23) metadata: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-24)  source: 'loop',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-25)  writes: { parentGraph: [Object] },
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-26)  step: 2,
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-27)  parents: {}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-28) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-29) config: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-30)  configurable: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-31)   thread_id: '123',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-32)   checkpoint_ns: '',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-33)   checkpoint_id: '1ef7c6ba-8560-67d0-8002-2e2cedd7de18'
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-34)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-35) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-36) createdAt: '2024-09-27T00:58:49.933Z',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-37) parentConfig: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-38)  configurable: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-39)   thread_id: '123',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-40)   checkpoint_ns: '',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-41)   checkpoint_id: '1ef7c6ba-7977-62c0-8001-13e89cb2bbab'
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-42)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-43) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-44)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-45)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-46){
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-47) values: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-48)  messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-49)   HumanMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-50)    "id": "5788e436-a756-4ff5-899a-82117a5c59c7",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-51)    "content": "what's the weather in SF",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-52)    "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-53)    "response_metadata": {}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-54)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-55)  ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-56)  toContinue: true
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-57) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-58) next: [ 'parentGraph' ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-59) tasks: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-60)  {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-61)   id: '095bb8a9-77d3-5a0c-9a23-e1390dcf36bc',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-62)   name: 'parentGraph',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-63)   path: [Array],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-64)   interrupts: [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-65)   state: [Object]
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-66)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-67) ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-68) metadata: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-69)  source: 'loop',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-70)  writes: { routerNode: [Object] },
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-71)  step: 1,
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-72)  parents: {}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-73) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-74) config: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-75)  configurable: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-76)   thread_id: '123',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-77)   checkpoint_ns: '',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-78)   checkpoint_id: '1ef7c6ba-7977-62c0-8001-13e89cb2bbab'
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-79)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-80) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-81) createdAt: '2024-09-27T00:58:48.684Z',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-82) parentConfig: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-83)  configurable: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-84)   thread_id: '123',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-85)   checkpoint_ns: '',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-86)   checkpoint_id: '1ef7c6ba-7972-64a0-8000-243575e3244f'
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-87)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-88) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-89)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-90)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-91){
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-92) values: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-93)  messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-94)   HumanMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-95)    "id": "5788e436-a756-4ff5-899a-82117a5c59c7",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-96)    "content": "what's the weather in SF",
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-97)    "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-98)    "response_metadata": {}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-99)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-100)  ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-101) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-102) next: [ 'routerNode' ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-103) tasks: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-104)  {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-105)   id: '00ed334c-47b5-5693-92b4-a5b83373e2a0',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-106)   name: 'routerNode',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-107)   path: [Array],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-108)   interrupts: [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-109)   state: undefined
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-110)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-111) ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-112) metadata: { source: 'loop', writes: null, step: 0, parents: {} },
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-113) config: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-114)  configurable: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-115)   thread_id: '123',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-116)   checkpoint_ns: '',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-117)   checkpoint_id: '1ef7c6ba-7972-64a0-8000-243575e3244f'
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-118)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-119) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-120) createdAt: '2024-09-27T00:58:48.682Z',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-121) parentConfig: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-122)  configurable: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-123)   thread_id: '123',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-124)   checkpoint_ns: '',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-125)   checkpoint_id: '1ef7c6ba-796f-6d90-ffff-25ed0eb5bb38'
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-126)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-127) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-128)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-129)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-130){
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-131) values: { messages: [] },
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-132) next: [ '__start__' ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-133) tasks: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-134)  {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-135)   id: 'ea62628e-881d-558d-bafc-e8b6a734e8aa',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-136)   name: '__start__',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-137)   path: [Array],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-138)   interrupts: [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-139)   state: undefined
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-140)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-141) ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-142) metadata: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-143)  source: 'input',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-144)  writes: { __start__: [Object] },
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-145)  step: -1,
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-146)  parents: {}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-147) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-148) config: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-149)  configurable: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-150)   thread_id: '123',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-151)   checkpoint_ns: '',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-152)   checkpoint_id: '1ef7c6ba-796f-6d90-ffff-25ed0eb5bb38'
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-153)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-154) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-155) createdAt: '2024-09-27T00:58:48.681Z',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-156) parentConfig: undefined
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-157)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-46-158)-----

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__codelineno-47-1)

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to add and use subgraphs  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/) [ Next  How to transform inputs and outputs of a subgraph  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
