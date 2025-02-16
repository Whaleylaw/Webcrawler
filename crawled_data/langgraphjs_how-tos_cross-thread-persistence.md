---
url: https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#how-to-add-cross-thread-persistence-to-your-graph)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to add cross-thread persistence to your graph 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/?q= "Share")

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
          * Persistence  Persistence 
            * [ Persistence  ](https://langchain-ai.github.io/langgraphjs/how-tos#persistence)
            * [ Persistence  ](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/)
            * [ How to add thread-level persistence (functional API)  ](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/)
            * [ How to add thread-level persistence to subgraphs  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/)
            * How to add cross-thread persistence to your graph  [ How to add cross-thread persistence to your graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#setup)
              * [ Define store  ](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#define-store)
              * [ Create graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#create-graph)
              * [ Run the graph!  ](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#run-the-graph)
            * [ How to add cross-thread persistence (functional API)  ](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/)
            * [ How to use Postgres checkpointer for persistence  ](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#setup)
  * [ Define store  ](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#define-store)
  * [ Create graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#create-graph)
  * [ Run the graph!  ](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#run-the-graph)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
  5. [ Persistence  ](https://langchain-ai.github.io/langgraphjs/how-tos#persistence)



# How to add cross-thread persistence to your graph[¶](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#how-to-add-cross-thread-persistence-to-your-graph "Permanent link")

Prerequisites

This guide assumes familiarity with the following: 

  * [ Persistence ](https://langchain-ai.github.io/langgraphjs/concepts/persistence/)
  * [ Memory ](https://langchain-ai.github.io/langgraphjs/concepts/memory/)
  * [ Chat Models ](https://js.langchain.com/docs/concepts/#chat-models)



In the [previous guide](https://langchain-ai.github.io/langgraphjs/how-tos/persistence.ipynb) you learned how to persist graph state across multiple interactions on a single [thread](). LangGraph.js also allows you to persist data across **multiple threads**. For instance, you can store information about users (their names or preferences) in a shared memory and reuse them in the new conversational threads.

In this guide, we will show how to construct and use a graph that has a shared memory implemented using the [Store](https://langchain-ai.github.io/langgraphjs/reference/classes/checkpoint.BaseStore.html) interface.

Note

Support for the `Store[](https://langchain-ai.github.io/langgraphjs/reference/classes/checkpoint.BaseStore.html)` API that is used in this guide was added in LangGraph.js `v0.2.10`. 

## Setup[¶](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#setup "Permanent link")

First, let's install the required packages and set our API keys.

Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-0-1)// process.env.OPENAI_API_KEY = "sk_...";
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-0-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-0-3)// Optional, add tracing in LangSmith
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-0-4)// process.env.LANGCHAIN_API_KEY = "lsv2__...";
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-0-5)// process.env.ANTHROPIC_API_KEY = "your api key";
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-0-6)// process.env.LANGCHAIN_TRACING_V2 = "true";
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-0-7)// process.env.LANGCHAIN_PROJECT = "Cross-thread persistence: LangGraphJS";

```


## Define store[¶](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#define-store "Permanent link")

In this example we will create a graph that will be able to retrieve information about a user's preferences. We will do so by defining an `InMemoryStore` - an object that can store data in memory and query that data. We will then pass the store object when compiling the graph. This allows each node in the graph to access the store: when you define node functions, you can define `store` keyword argument, and LangGraph will automatically pass the store object you compiled the graph with.

When storing objects using the `Store` interface you define two things:

  * the namespace for the object, a tuple (similar to directories)
  * the object key (similar to filenames)



In our example, we'll be using `("memories", <userId>)` as namespace and random UUID as key for each new memory.

Importantly, to determine the user, we will be passing `userId` via the config keyword argument of the node function.

Let's first define an `InMemoryStore` which is already populated with some memories about the users.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-1-1)import{InMemoryStore}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-1-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-1-3)constinMemoryStore=newInMemoryStore();

```


## Create graph[¶](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#create-graph "Permanent link")

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-1)import{v4asuuidv4}from"uuid";
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-2)import{ChatAnthropic}from"@langchain/anthropic";
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-3)import{BaseMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-4)import{
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-5)Annotation,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-6)StateGraph,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-7)START,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-8)MemorySaver,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-9)LangGraphRunnableConfig,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-10)messagesStateReducer,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-11)}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-12)
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-13)constStateAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-14)messages:Annotation<BaseMessage[]>({
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-15)reducer:messagesStateReducer,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-16)default:()=>[],
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-17)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-18)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-19)
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-20)constmodel=newChatAnthropic({modelName:"claude-3-5-sonnet-20240620"});
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-21)
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-22)// NOTE: we're passing the Store param to the node --
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-23)// this is the Store we compile the graph with
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-24)constcallModel=async(
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-25)state:typeofStateAnnotation.State,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-26)config:LangGraphRunnableConfig
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-27)):Promise<{messages:any}>=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-28)conststore=config.store;
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-29)if(!store){
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-30)if(!store){
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-31)thrownewError("store is required when compiling the graph");
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-32)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-33)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-34)if(!config.configurable?.userId){
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-35)thrownewError("userId is required in the config");
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-36)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-37)constnamespace=["memories",config.configurable?.userId];
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-38)constmemories=awaitstore.search(namespace);
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-39)constinfo=memories.map((d)=>d.value.data).join("\n");
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-40)constsystemMsg=`You are a helpful assistant talking to the user. User info: ${info}`;
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-41)
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-42)// Store new memories if the user asks the model to remember
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-43)constlastMessage=state.messages[state.messages.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-44)if(
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-45)typeoflastMessage.content==="string"&&
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-46)lastMessage.content.toLowerCase().includes("remember")
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-47)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-48)awaitstore.put(namespace,uuidv4(),{data:lastMessage.content});
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-49)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-50)
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-51)constresponse=awaitmodel.invoke([
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-52){type:"system",content:systemMsg},
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-53)...state.messages,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-54)]);
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-55)return{messages:response};
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-56)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-57)
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-58)constbuilder=newStateGraph(StateAnnotation)
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-59).addNode("call_model",callModel)
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-60).addEdge(START,"call_model");
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-61)
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-62)// NOTE: we're passing the store object here when compiling the graph
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-63)constgraph=builder.compile({
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-64)checkpointer:newMemorySaver(),
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-65)store:inMemoryStore,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-66)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-2-67)// If you're using LangGraph Cloud or LangGraph Studio, you don't need to pass the store or checkpointer when compiling the graph, since it's done automatically.

```


Note

If you're using LangGraph Cloud or LangGraph Studio, you **don't need** to pass store when compiling the graph, since it's done automatically. 

## Run the graph![¶](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#run-the-graph "Permanent link")

Now let's specify a user ID in the config and tell the model our name:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-3-1)letconfig={configurable:{thread_id:"1",userId:"1"}};
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-3-2)letinputMessage={type:"user",content:"Hi! Remember: my name is Bob"};
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-3-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-3-4)forawait(constchunkofawaitgraph.stream(
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-3-5){messages:[inputMessage]},
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-3-6){...config,streamMode:"values"}
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-3-7))){
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-3-8)console.log(chunk.messages[chunk.messages.length-1]);
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-3-9)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-4-1)HumanMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-4-2) "id": "ef28a40a-fd75-4478-929a-5413f2a6b044",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-4-3) "content": "Hi! Remember: my name is Bob",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-4-4) "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-4-5) "response_metadata": {}
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-4-6)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-4-7)AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-4-8) "id": "msg_01UcHJnSAuVDFuDmqaYkxWAf",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-4-9) "content": "Hello Bob! It's nice to meet you. I'll remember that your name is Bob. How can I assist you today?",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-4-10) "additional_kwargs": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-4-11)  "id": "msg_01UcHJnSAuVDFuDmqaYkxWAf",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-4-12)  "type": "message",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-4-13)  "role": "assistant",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-4-14)  "model": "claude-3-5-sonnet-20240620",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-4-15)  "stop_reason": "end_turn",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-4-16)  "stop_sequence": null,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-4-17)  "usage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-4-18)   "input_tokens": 28,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-4-19)   "output_tokens": 29
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-4-20)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-4-21) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-4-22) "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-4-23)  "id": "msg_01UcHJnSAuVDFuDmqaYkxWAf",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-4-24)  "model": "claude-3-5-sonnet-20240620",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-4-25)  "stop_reason": "end_turn",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-4-26)  "stop_sequence": null,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-4-27)  "usage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-4-28)   "input_tokens": 28,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-4-29)   "output_tokens": 29
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-4-30)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-4-31)  "type": "message",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-4-32)  "role": "assistant"
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-4-33) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-4-34) "tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-4-35) "invalid_tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-4-36) "usage_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-4-37)  "input_tokens": 28,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-4-38)  "output_tokens": 29,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-4-39)  "total_tokens": 57
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-4-40) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-4-41)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-5-1)config={configurable:{thread_id:"2",userId:"1"}};
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-5-2)inputMessage={type:"user",content:"what is my name?"};
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-5-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-5-4)forawait(constchunkofawaitgraph.stream(
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-5-5){messages:[inputMessage]},
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-5-6){...config,streamMode:"values"}
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-5-7))){
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-5-8)console.log(chunk.messages[chunk.messages.length-1]);
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-5-9)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-6-1)HumanMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-6-2) "id": "eaaa4e1c-1560-4b0a-9c2d-396313cb000c",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-6-3) "content": "what is my name?",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-6-4) "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-6-5) "response_metadata": {}
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-6-6)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-6-7)AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-6-8) "id": "msg_01VfqUerYCND1JuWGvbnAacP",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-6-9) "content": "Your name is Bob. It's nice to meet you, Bob!",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-6-10) "additional_kwargs": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-6-11)  "id": "msg_01VfqUerYCND1JuWGvbnAacP",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-6-12)  "type": "message",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-6-13)  "role": "assistant",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-6-14)  "model": "claude-3-5-sonnet-20240620",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-6-15)  "stop_reason": "end_turn",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-6-16)  "stop_sequence": null,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-6-17)  "usage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-6-18)   "input_tokens": 33,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-6-19)   "output_tokens": 17
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-6-20)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-6-21) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-6-22) "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-6-23)  "id": "msg_01VfqUerYCND1JuWGvbnAacP",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-6-24)  "model": "claude-3-5-sonnet-20240620",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-6-25)  "stop_reason": "end_turn",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-6-26)  "stop_sequence": null,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-6-27)  "usage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-6-28)   "input_tokens": 33,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-6-29)   "output_tokens": 17
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-6-30)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-6-31)  "type": "message",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-6-32)  "role": "assistant"
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-6-33) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-6-34) "tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-6-35) "invalid_tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-6-36) "usage_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-6-37)  "input_tokens": 33,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-6-38)  "output_tokens": 17,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-6-39)  "total_tokens": 50
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-6-40) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-6-41)}

```


We can now inspect our in-memory store and verify that we have in fact saved the memories for the user: 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-7-1)constmemories=awaitinMemoryStore.search(["memories","1"]);
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-7-2)for(constmemoryofmemories){
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-7-3)console.log(awaitmemory.value);
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-7-4)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-8-1){ data: 'Hi! Remember: my name is Bob' }

```


Let's now run the graph for another user to verify that the memories about the first user are self contained: 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-9-1)config={configurable:{thread_id:"3",userId:"2"}};
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-9-2)inputMessage={type:"user",content:"what is my name?"};
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-9-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-9-4)forawait(constchunkofawaitgraph.stream(
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-9-5){messages:[inputMessage]},
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-9-6){...config,streamMode:"values"}
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-9-7))){
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-9-8)console.log(chunk.messages[chunk.messages.length-1]);
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-9-9)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-10-1)HumanMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-10-2) "id": "1006b149-de8d-4d8e-81f4-c78c51a7144b",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-10-3) "content": "what is my name?",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-10-4) "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-10-5) "response_metadata": {}
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-10-6)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-10-7)AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-10-8) "id": "msg_01MjpYZ65NjwZMYq42BWa2Ze",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-10-9) "content": "I apologize, but I don't have any information about your name or personal details. As an AI assistant, I don't have access to personal information about individual users unless it's specifically provided in our conversation. Is there something else I can help you with?",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-10-10) "additional_kwargs": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-10-11)  "id": "msg_01MjpYZ65NjwZMYq42BWa2Ze",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-10-12)  "type": "message",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-10-13)  "role": "assistant",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-10-14)  "model": "claude-3-5-sonnet-20240620",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-10-15)  "stop_reason": "end_turn",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-10-16)  "stop_sequence": null,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-10-17)  "usage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-10-18)   "input_tokens": 25,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-10-19)   "output_tokens": 56
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-10-20)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-10-21) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-10-22) "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-10-23)  "id": "msg_01MjpYZ65NjwZMYq42BWa2Ze",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-10-24)  "model": "claude-3-5-sonnet-20240620",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-10-25)  "stop_reason": "end_turn",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-10-26)  "stop_sequence": null,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-10-27)  "usage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-10-28)   "input_tokens": 25,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-10-29)   "output_tokens": 56
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-10-30)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-10-31)  "type": "message",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-10-32)  "role": "assistant"
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-10-33) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-10-34) "tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-10-35) "invalid_tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-10-36) "usage_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-10-37)  "input_tokens": 25,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-10-38)  "output_tokens": 56,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-10-39)  "total_tokens": 81
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-10-40) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__codelineno-10-41)}

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to add thread-level persistence to subgraphs  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/) [ Next  How to add cross-thread persistence (functional API)  ](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
