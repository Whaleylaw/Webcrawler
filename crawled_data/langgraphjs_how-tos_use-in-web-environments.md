---
url: https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#how-to-use-langgraphjs-in-web-environments)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to use LangGraph.js in web environments 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/?q= "Share")

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
        * Installation  Installation 
          * [ Installation  ](https://langchain-ai.github.io/langgraphjs/how-tos#installation)
          * [ How to install and manage dependencies  ](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/)
          * How to use LangGraph.js in web environments  [ How to use LangGraph.js in web environments  ](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/) Table of contents 
            * [ Passing config  ](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#passing-config)
            * [ Next steps  ](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#next-steps)
        * [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
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

  * [ Passing config  ](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#passing-config)
  * [ Next steps  ](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#next-steps)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ Installation  ](https://langchain-ai.github.io/langgraphjs/how-tos#installation)



# How to use LangGraph.js in web environments[¶](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#how-to-use-langgraphjs-in-web-environments "Permanent link")

LangGraph.js uses the `async_hooks`[](https://nodejs.org/api/async_hooks.html) API to more conveniently allow for tracing and callback propagation within nodes. This API is supported in many environments, such as [Node.js](https://nodejs.org/api/async_hooks.html), [Deno](https://deno.land/std@0.177.0/node/internal/async_hooks.ts), [Cloudflare Workers](https://developers.cloudflare.com/workers/runtime-apis/nodejs/asynclocalstorage/), and the [Edge runtime](https://vercel.com/docs/functions/runtimes/edge-runtime#compatible-node.js-modules), but not all, such as within web browsers.

To allow usage of LangGraph.js in environments that do not have the `async_hooks` API available, we've added a separate `@langchain/langgraph/web` entrypoint. This entrypoint exports everything that the primary `@langchain/langgraph` exports, but will not initialize or even import `async_hooks`. Here's a simple example:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-0-1)// Import from "@langchain/langgraph/web"
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-0-2)import{
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-0-3)END,
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-0-4)START,
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-0-5)StateGraph,
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-0-6)Annotation,
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-0-7)}from"@langchain/langgraph/web";
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-0-8)import{BaseMessage,HumanMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-0-9)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-0-10)constGraphState=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-0-11)messages:Annotation<BaseMessage[]>({
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-0-12)reducer:(x,y)=>x.concat(y),
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-0-13)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-0-14)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-0-15)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-0-16)constnodeFn=async(_state:typeofGraphState.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-0-17)return{messages:[newHumanMessage("Hello from the browser!")]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-0-18)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-0-19)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-0-20)// Define a new graph
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-0-21)constworkflow=newStateGraph(GraphState)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-0-22).addNode("node",nodeFn)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-0-23).addEdge(START,"node")
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-0-24).addEdge("node",END);
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-0-25)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-0-26)constapp=workflow.compile({});
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-0-27)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-0-28)// Use the Runnable
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-0-29)constfinalState=awaitapp.invoke(
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-0-30){messages:[]},
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-0-31));
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-0-32)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-0-33)console.log(finalState.messages[finalState.messages.length-1].content);

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-1-1)Hello from the browser!

```


Other entrypoints, such as `@langchain/langgraph/prebuilt`, can be used in either environment. 

Caution

If you are using LangGraph.js on the frontend, make sure you are not exposing any private keys! For chat models, this means you need to use something like [WebLLM](https://js.langchain.com/docs/integrations/chat/web_llm) that can run client-side without authentication. 

## Passing config[¶](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#passing-config "Permanent link")

The lack of `async_hooks` support in web browsers means that if you are calling a `Runnable`[](https://js.langchain.com/docs/concepts/runnables/) within a node (for example, when calling a chat model), you need to manually pass a `config` object through to properly support tracing, `.streamEvents()`[](https://js.langchain.com/docs/how_to/streaming#using-stream-events) to stream intermediate steps, and other callback related functionality. This config object will passed in as the second argument of each node, and should be used as the second parameter of any `Runnable` method.

To illustrate this, let's set up our graph again as before, but with a `Runnable` within our node. First, we'll avoid passing `config` through into the nested function, then try to use `.streamEvents()` to see the intermediate results of the nested function:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-2-1)// Import from "@langchain/langgraph/web"
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-2-2)import{
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-2-3)END,
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-2-4)START,
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-2-5)StateGraph,
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-2-6)Annotation,
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-2-7)}from"@langchain/langgraph/web";
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-2-8)import{BaseMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-2-9)import{RunnableLambda}from"@langchain/core/runnables";
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-2-10)import{typeStreamEvent}from"@langchain/core/tracers/log_stream";
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-2-11)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-2-12)constGraphState2=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-2-13)messages:Annotation<BaseMessage[]>({
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-2-14)reducer:(x,y)=>x.concat(y),
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-2-15)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-2-16)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-2-17)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-2-18)constnodeFn2=async(_state:typeofGraphState2.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-2-19)// Note that we do not pass any `config` through here
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-2-20)constnestedFn=RunnableLambda.from(async(input:string)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-2-21)returnnewHumanMessage(`Hello from ${input}!`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-2-22)}).withConfig({runName:"nested"});
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-2-23)constresponseMessage=awaitnestedFn.invoke("a nested function");
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-2-24)return{messages:[responseMessage]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-2-25)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-2-26)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-2-27)// Define a new graph
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-2-28)constworkflow2=newStateGraph(GraphState2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-2-29).addNode("node",nodeFn2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-2-30).addEdge(START,"node")
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-2-31).addEdge("node",END);
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-2-32)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-2-33)constapp2=workflow2.compile({});
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-2-34)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-2-35)// Stream intermediate steps from the graph
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-2-36)consteventStream2=app2.streamEvents(
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-2-37){messages:[]},
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-2-38){version:"v2"},
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-2-39){includeNames:["nested"]},
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-2-40));
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-2-41)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-2-42)constevents2:StreamEvent[]=[];
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-2-43)forawait(consteventofeventStream2){
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-2-44)console.log(event);
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-2-45)events2.push(event);
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-2-46)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-2-47)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-2-48)console.log(`Received ${events2.length} events from the nested function`);

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-3-1)Received 0 events from the nested function

```


We can see that we get no events. 

Next, let's try redeclaring the graph with a node that passes config through correctly:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-4-1)// Import from "@langchain/langgraph/web"
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-4-2)import{
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-4-3)END,
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-4-4)START,
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-4-5)StateGraph,
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-4-6)Annotation,
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-4-7)}from"@langchain/langgraph/web";
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-4-8)import{BaseMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-4-9)import{typeRunnableConfig,RunnableLambda}from"@langchain/core/runnables";
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-4-10)import{typeStreamEvent}from"@langchain/core/tracers/log_stream";
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-4-11)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-4-12)constGraphState3=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-4-13)messages:Annotation<BaseMessage[]>({
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-4-14)reducer:(x,y)=>x.concat(y),
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-4-15)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-4-16)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-4-17)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-4-18)// Note the second argument here.
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-4-19)constnodeFn3=async(_state:typeofGraphState3.State,config?:RunnableConfig)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-4-20)// If you need to nest deeper, remember to pass `_config` when invoking
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-4-21)constnestedFn=RunnableLambda.from(
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-4-22)async(input:string,_config?:RunnableConfig)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-4-23)returnnewHumanMessage(`Hello from ${input}!`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-4-24)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-4-25)).withConfig({runName:"nested"});
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-4-26)constresponseMessage=awaitnestedFn.invoke("a nested function",config);
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-4-27)return{messages:[responseMessage]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-4-28)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-4-29)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-4-30)// Define a new graph
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-4-31)constworkflow3=newStateGraph(GraphState3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-4-32).addNode("node",nodeFn3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-4-33).addEdge(START,"node")
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-4-34).addEdge("node",END);
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-4-35)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-4-36)constapp3=workflow3.compile({});
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-4-37)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-4-38)// Stream intermediate steps from the graph
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-4-39)consteventStream3=app3.streamEvents(
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-4-40){messages:[]},
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-4-41){version:"v2"},
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-4-42){includeNames:["nested"]},
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-4-43));
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-4-44)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-4-45)constevents3:StreamEvent[]=[];
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-4-46)forawait(consteventofeventStream3){
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-4-47)console.log(event);
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-4-48)events3.push(event);
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-4-49)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-4-50)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-4-51)console.log(`Received ${events3.length} events from the nested function`);

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-5-1){
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-5-2) event: "on_chain_start",
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-5-3) data: { input: { messages: [] } },
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-5-4) name: "nested",
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-5-5) tags: [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-5-6) run_id: "22747451-a2fa-447b-b62f-9da19a539b2f",
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-5-7) metadata: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-5-8)  langgraph_step: 1,
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-5-9)  langgraph_node: "node",
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-5-10)  langgraph_triggers: [ "start:node" ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-5-11)  langgraph_task_idx: 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-5-12)  __pregel_resuming: false,
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-5-13)  checkpoint_id: "1ef62793-f065-6840-fffe-cdfb4cbb1248",
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-5-14)  checkpoint_ns: "node"
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-5-15) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-5-16)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-5-17){
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-5-18) event: "on_chain_end",
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-5-19) data: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-5-20)  output: HumanMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-5-21)   "content": "Hello from a nested function!",
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-5-22)   "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-5-23)   "response_metadata": {}
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-5-24)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-5-25) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-5-26) run_id: "22747451-a2fa-447b-b62f-9da19a539b2f",
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-5-27) name: "nested",
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-5-28) tags: [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-5-29) metadata: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-5-30)  langgraph_step: 1,
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-5-31)  langgraph_node: "node",
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-5-32)  langgraph_triggers: [ "start:node" ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-5-33)  langgraph_task_idx: 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-5-34)  __pregel_resuming: false,
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-5-35)  checkpoint_id: "1ef62793-f065-6840-fffe-cdfb4cbb1248",
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-5-36)  checkpoint_ns: "node"
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-5-37) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-5-38)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__codelineno-5-39)Received 2 events from the nested function

```


You can see that we get events from the nested function as expected. 

## Next steps[¶](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#next-steps "Permanent link")

You've now learned about some special considerations around using LangGraph.js in web environments.

Next, check out [some how-to guides on core functionality](https://langchain-ai.github.io/langgraphjs/how-tos/#core).

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to install and manage dependencies  ](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/) [ Next  How to create map-reduce branches for parallel execution  ](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
