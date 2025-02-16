---
url: https://langchain-ai.github.io/langgraphjs/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/#langgraphjs)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

Introduction 

[ ](https://langchain-ai.github.io/langgraphjs/?q= "Share")

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

  * [ Overview  ](https://langchain-ai.github.io/langgraphjs/#overview)
    * [ Why use LangGraph?  ](https://langchain-ai.github.io/langgraphjs/#why-use-langgraph)
    * [ LangGraph Platform  ](https://langchain-ai.github.io/langgraphjs/#langgraph-platform)
  * [ Installation  ](https://langchain-ai.github.io/langgraphjs/#installation)
  * [ Example  ](https://langchain-ai.github.io/langgraphjs/#example)
  * [ Documentation  ](https://langchain-ai.github.io/langgraphjs/#documentation)
  * [ Resources  ](https://langchain-ai.github.io/langgraphjs/#resources)
  * [ Contributing  ](https://langchain-ai.github.io/langgraphjs/#contributing)



# 🦜🕸️LangGraph.js[¶](https://langchain-ai.github.io/langgraphjs/#langgraphjs "Permanent link")

[![Docs](https://img.shields.io/badge/docs-latest-blue)](https://langchain-ai.github.io/langgraphjs/) ![Version](https://img.shields.io/npm/v/@langchain/langgraph?logo=npm) [![Downloads](https://img.shields.io/npm/dm/@langchain/langgraph)](https://www.npmjs.com/package/@langchain/langgraph) [![Open Issues](https://img.shields.io/github/issues-raw/langchain-ai/langgraphjs)](https://github.com/langchain-ai/langgraphjs/issues)

⚡ Building language agents as graphs ⚡

Note

Looking for the Python version? See the [Python repo](https://github.com/langchain-ai/langgraph) and the [Python docs](https://langchain-ai.github.io/langgraph/).

## Overview[¶](https://langchain-ai.github.io/langgraphjs/#overview "Permanent link")

[LangGraph](https://langchain-ai.github.io/langgraphjs/) is a library for building stateful, multi-actor applications with LLMs, used to create agent and multi-agent workflows. Check out an introductory tutorial [here](https://langchain-ai.github.io/langgraphjs/tutorials/quickstart/).

LangGraph is inspired by [Pregel](https://research.google/pubs/pub37252/) and [Apache Beam](https://beam.apache.org/). The public interface draws inspiration from [NetworkX](https://networkx.org/documentation/latest/). LangGraph is built by LangChain Inc, the creators of LangChain, but can be used without LangChain.

### Why use LangGraph?[¶](https://langchain-ai.github.io/langgraphjs/#why-use-langgraph "Permanent link")

LangGraph powers [production-grade agents](https://www.langchain.com/built-with-langgraph), trusted by Linkedin, Uber, Klarna, GitLab, and many more. LangGraph provides fine-grained control over both the flow and state of your agent applications. It implements a central [persistence layer](https://langchain-ai.github.io/langgraphjs/concepts/persistence/), enabling features that are common to most agent architectures:

  * **Memory** : LangGraph persists arbitrary aspects of your application's state, supporting memory of conversations and other updates within and across user interactions;
  * **Human-in-the-loop** : Because state is checkpointed, execution can be interrupted and resumed, allowing for decisions, validation, and corrections at key stages via human input.



Standardizing these components allows individuals and teams to focus on the behavior of their agent, instead of its supporting infrastructure.

Through [LangGraph Platform](https://langchain-ai.github.io/langgraphjs/#langgraph-platform), LangGraph also provides tooling for the development, deployment, debugging, and monitoring of your applications.

LangGraph integrates seamlessly with [LangChain](https://js.langchain.com/docs/introduction/) and [LangSmith](https://docs.smith.langchain.com/) (but does not require them).

To learn more about LangGraph, check out our first LangChain Academy course, _Introduction to LangGraph_ , available for free [here](https://academy.langchain.com/courses/intro-to-langgraph).

### LangGraph Platform[¶](https://langchain-ai.github.io/langgraphjs/#langgraph-platform "Permanent link")

[LangGraph Platform](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_platform) is infrastructure for deploying LangGraph agents. It is a commercial solution for deploying agentic applications to production, built on the open-source LangGraph framework. The LangGraph Platform consists of several components that work together to support the development, deployment, debugging, and monitoring of LangGraph applications: [LangGraph Server](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_server) (APIs), [LangGraph SDKs](https://langchain-ai.github.io/langgraphjs/concepts/sdk) (clients for the APIs), [LangGraph CLI](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_cli) (command line tool for building the server), and [LangGraph Studio](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_studio) (UI/debugger).

See deployment options [here](https://langchain-ai.github.io/langgraphjs/concepts/deployment_options/) (includes a free tier).

Here are some common issues that arise in complex deployments, which LangGraph Platform addresses:

  * **Streaming support** : LangGraph Server provides [multiple streaming modes](https://langchain-ai.github.io/langgraphjs/concepts/streaming) optimized for various application needs
  * **Background runs** : Runs agents asynchronously in the background
  * **Support for long running agents** : Infrastructure that can handle long running processes
  * **[Double texting](https://langchain-ai.github.io/langgraphjs/concepts/double_texting)** : Handle the case where you get two messages from the user before the agent can respond
  * **Handle burstiness** : Task queue for ensuring requests are handled consistently without loss, even under heavy loads



## Installation[¶](https://langchain-ai.github.io/langgraphjs/#installation "Permanent link")

```
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-0-1)npminstall@langchain/langgraph@langchain/core

```


## Example[¶](https://langchain-ai.github.io/langgraphjs/#example "Permanent link")

Let's build a tool-calling [ReAct-style](https://langchain-ai.github.io/langgraphjs/concepts/agentic_concepts/#react-implementation) agent that uses a search tool!

```
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-1-1)npminstall@langchain/anthropiczod

```


```
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-2-1)exportANTHROPIC_API_KEY=sk-...

```


Optionally, we can set up [LangSmith](https://docs.smith.langchain.com/) for best-in-class observability.

```
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-3-1)exportLANGSMITH_TRACING=true
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-3-2)exportLANGSMITH_API_KEY=lsv2_sk_...

```


The simplest way to create a tool-calling agent in LangGraph is to use `createReactAgent`[](https://langchain-ai.github.io/langgraphjs/reference/functions/langgraph_prebuilt.createReactAgent.html):

High-level implementation

```
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-4-1)import{createReactAgent}from"@langchain/langgraph/prebuilt";
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-4-2)import{MemorySaver}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-4-3)import{ChatAnthropic}from"@langchain/anthropic";
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-4-4)import{tool}from"@langchain/core/tools";
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-4-5)
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-4-6)import{z}from"zod";
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-4-7)
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-4-8)// Define the tools for the agent to use
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-4-9)constsearch=tool(async({query})=>{
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-4-10)// This is a placeholder, but don't tell the LLM that...
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-4-11)if(query.toLowerCase().includes("sf")||query.toLowerCase().includes("san francisco")){
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-4-12)return"It's 60 degrees and foggy."
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-4-13)}
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-4-14)return"It's 90 degrees and sunny."
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-4-15)},{
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-4-16)name:"search",
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-4-17)description:"Call to surf the web.",
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-4-18)schema:z.object({
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-4-19)query:z.string().describe("The query to use in your search."),
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-4-20)}),
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-4-21)});
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-4-22)
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-4-23)consttools=[search];
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-4-24)constmodel=newChatAnthropic({
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-4-25)model:"claude-3-5-sonnet-latest"
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-4-26)});
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-4-27)
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-4-28)// Initialize memory to persist state between graph runs
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-4-29)constcheckpointer=newMemorySaver();
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-4-30)
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-4-31)constapp=createReactAgent({
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-4-32)llm:model,
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-4-33)tools,
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-4-34)checkpointSaver:checkpointer,
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-4-35)});
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-4-36)
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-4-37)// Use the agent
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-4-38)constresult=awaitapp.invoke(
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-4-39){
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-4-40)messages:[{
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-4-41)role:"user",
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-4-42)content:"what is the weather in sf"
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-4-43)}]
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-4-44)},
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-4-45){configurable:{thread_id:42}}
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-4-46));
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-4-47)console.log(result.messages.at(-1)?.content);

```


```
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-5-1)"Based on the search results, it's currently 60 degrees Fahrenheit and foggy in San Francisco, which is quite typical weather for the city."

```


Now when we pass the same `"thread_id"`, the conversation context is retained via the saved state (i.e. stored list of messages) 

```
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-6-1)constfollowup=awaitapp.invoke(
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-6-2){
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-6-3)messages:[{
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-6-4)role:"user",
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-6-5)content:"what about ny"
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-6-6)}]
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-6-7)},
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-6-8){configurable:{thread_id:42}}
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-6-9));
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-6-10)
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-6-11)console.log(followup.messages.at(-1)?.content);

```


```
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-7-1)"According to the search results, it's currently 90 degrees Fahrenheit and sunny in New York City. That's quite a warm day for New York!"

```


Tip

LangGraph is a **low-level** framework that allows you to implement any custom agent architectures. Click on the low-level implementation below to see how to implement a tool-calling agent from scratch.

Low-level implementation

```
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-1)import{AIMessage,BaseMessage,HumanMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-2)import{tool}from"@langchain/core/tools";
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-3)import{z}from"zod";
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-4)import{ChatAnthropic}from"@langchain/anthropic";
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-5)import{StateGraph}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-6)import{MemorySaver,Annotation,messagesStateReducer}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-7)import{ToolNode}from"@langchain/langgraph/prebuilt";
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-8)
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-9)// Define the graph state
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-10)// See here for more info: https://langchain-ai.github.io/langgraphjs/how-tos/define-state/
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-11)constStateAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-12)messages:Annotation<BaseMessage[]>({
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-13)// `messagesStateReducer` function defines how `messages` state key should be updated
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-14)// (in this case it appends new messages to the list and overwrites messages with the same ID)
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-15)reducer:messagesStateReducer,
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-16)}),
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-17)});
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-18)
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-19)// Define the tools for the agent to use
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-20)constweatherTool=tool(async({query})=>{
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-21)// This is a placeholder for the actual implementation
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-22)if(query.toLowerCase().includes("sf")||query.toLowerCase().includes("san francisco")){
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-23)return"It's 60 degrees and foggy."
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-24)}
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-25)return"It's 90 degrees and sunny."
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-26)},{
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-27)name:"weather",
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-28)description:
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-29)"Call to get the current weather for a location.",
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-30)schema:z.object({
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-31)query:z.string().describe("The query to use in your search."),
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-32)}),
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-33)});
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-34)
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-35)consttools=[weatherTool];
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-36)consttoolNode=newToolNode(tools);
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-37)
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-38)constmodel=newChatAnthropic({
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-39)model:"claude-3-5-sonnet-20240620",
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-40)temperature:0,
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-41)}).bindTools(tools);
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-42)
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-43)// Define the function that determines whether to continue or not
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-44)// We can extract the state typing via `StateAnnotation.State`
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-45)functionshouldContinue(state:typeofStateAnnotation.State){
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-46)constmessages=state.messages;
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-47)constlastMessage=messages[messages.length-1]asAIMessage;
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-48)
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-49)// If the LLM makes a tool call, then we route to the "tools" node
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-50)if(lastMessage.tool_calls?.length){
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-51)return"tools";
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-52)}
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-53)// Otherwise, we stop (reply to the user)
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-54)return"__end__";
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-55)}
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-56)
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-57)// Define the function that calls the model
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-58)asyncfunctioncallModel(state:typeofStateAnnotation.State){
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-59)constmessages=state.messages;
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-60)constresponse=awaitmodel.invoke(messages);
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-61)
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-62)// We return a list, because this will get added to the existing list
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-63)return{messages:[response]};
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-64)}
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-65)
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-66)// Define a new graph
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-67)constworkflow=newStateGraph(StateAnnotation)
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-68).addNode("agent",callModel)
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-69).addNode("tools",toolNode)
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-70).addEdge("__start__","agent")
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-71).addConditionalEdges("agent",shouldContinue)
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-72).addEdge("tools","agent");
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-73)
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-74)// Initialize memory to persist state between graph runs
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-75)constcheckpointer=newMemorySaver();
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-76)
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-77)// Finally, we compile it!
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-78)// This compiles it into a LangChain Runnable.
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-79)// Note that we're (optionally) passing the memory when compiling the graph
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-80)constapp=workflow.compile({checkpointer});
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-81)
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-82)// Use the Runnable
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-83)constfinalState=awaitapp.invoke(
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-84){messages:[newHumanMessage("what is the weather in sf")]},
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-85){configurable:{thread_id:"42"}}
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-86));
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-87)
[](https://langchain-ai.github.io/langgraphjs/#__codelineno-8-88)console.log(finalState.messages[finalState.messages.length-1].content);

```


**Step-by-step Breakdown** :  Initialize the model and tools.

  * We use `ChatAnthropic` as our LLM. **NOTE:** we need to make sure the model knows that it has these tools available to call. We can do this by converting the LangChain tools into the format for OpenAI tool calling using the `.bindTools()` method. 
  * We define the tools we want to use - a search tool in our case. It is really easy to create your own tools - see documentation here on how to do that [here](https://js.langchain.com/docs/how_to/custom_tools). 

Initialize graph with state.

  * We initialize the graph (`StateGraph`) by passing state schema with a reducer that defines how the state should be updated. In our case, we want to append new messages to the list and overwrite messages with the same ID, so we use the prebuilt `messagesStateReducer`.

Define graph nodes. There are two main nodes we need: 

  * The `agent` node: responsible for deciding what (if any) actions to take.
  * The `tools` node that invokes tools: if the agent decides to take an action, this node will then execute that action.

Define entry point and graph edges. First, we need to set the entry point for graph execution - `agent` node. Then we define one normal and one conditional edge. Conditional edge means that the destination depends on the contents of the graph's state. In our case, the destination is not known until the agent (LLM) decides. 

  * Conditional edge: after the agent is called, we should either: 
    * a. Run tools if the agent said to take an action, OR
    * b. Finish (respond to the user) if the agent did not ask to run tools
  * Normal edge: after the tools are invoked, the graph should always return to the agent to decide what to do next

Compile the graph.

  * When we compile the graph, we turn it into a LangChain [Runnable](https://js.langchain.com/docs/concepts/runnables), which automatically enables calling `.invoke()`, `.stream()` and `.batch()` with your inputs 
  * We can also optionally pass checkpointer object for persisting state between graph runs, and enabling memory, human-in-the-loop workflows, time travel and more. In our case we use `MemorySaver` - a simple in-memory checkpointer 

Execute the graph.

  1. LangGraph adds the input message to the internal state, then passes the state to the entrypoint node, `"agent"`.
  2. The `"agent"` node executes, invoking the chat model.
  3. The chat model returns an `AIMessage`. LangGraph adds this to the state.
  4. Graph cycles the following steps until there are no more `tool_calls` on `AIMessage`: 
     * If `AIMessage` has `tool_calls`, `"tools"` node executes
     * The `"agent"` node executes again and returns `AIMessage`
  5. Execution progresses to the special `END` value and outputs the final state. And as a result, we get a list of all our chat messages as output.



## Documentation[¶](https://langchain-ai.github.io/langgraphjs/#documentation "Permanent link")

  * [Tutorials](https://langchain-ai.github.io/langgraphjs/tutorials/): Learn to build with LangGraph through guided examples.
  * [How-to Guides](https://langchain-ai.github.io/langgraphjs/how-tos/): Accomplish specific things within LangGraph, from streaming, to adding memory & persistence, to common design patterns (branching, subgraphs, etc.), these are the place to go if you want to copy and run a specific code snippet.
  * [Conceptual Guides](https://langchain-ai.github.io/langgraphjs/concepts/high_level/): In-depth explanations of the key concepts and principles behind LangGraph, such as nodes, edges, state and more.
  * [API Reference](https://langchain-ai.github.io/langgraphjs/reference/): Review important classes and methods, simple examples of how to use the graph and checkpointing APIs, higher-level prebuilt components and more.
  * [LangGraph Platform](https://langchain-ai.github.io/langgraphjs/concepts/#langgraph-platform): LangGraph Platform is a commercial solution for deploying agentic applications in production, built on the open-source LangGraph framework.



## Resources[¶](https://langchain-ai.github.io/langgraphjs/#resources "Permanent link")

  * [Built with LangGraph](https://www.langchain.com/built-with-langgraph): Hear how industry leaders use LangGraph to ship powerful, production-ready AI applications.



## Contributing[¶](https://langchain-ai.github.io/langgraphjs/#contributing "Permanent link")

For more information on how to contribute, see [here](https://github.com/langchain-ai/langgraphjs/blob/main/CONTRIBUTING.md).

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Next  Learn the basics  ](https://langchain-ai.github.io/langgraphjs/tutorials/quickstart/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
