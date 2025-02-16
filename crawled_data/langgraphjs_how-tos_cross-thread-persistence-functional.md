---
url: https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#how-to-add-cross-thread-persistence-functional-api)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to add cross-thread persistence (functional API) 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/?q= "Share")

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
            * [ How to add cross-thread persistence to your graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/)
            * How to add cross-thread persistence (functional API)  [ How to add cross-thread persistence (functional API)  ](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#setup)
              * [ Example: simple chatbot with long-term memory  ](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#example-simple-chatbot-with-long-term-memory)
                * [ Define store  ](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#define-store)
                * [ Create workflow  ](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#create-workflow)
                * [ Run the workflow!  ](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#run-the-workflow)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#setup)
  * [ Example: simple chatbot with long-term memory  ](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#example-simple-chatbot-with-long-term-memory)
    * [ Define store  ](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#define-store)
    * [ Create workflow  ](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#create-workflow)
    * [ Run the workflow!  ](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#run-the-workflow)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
  5. [ Persistence  ](https://langchain-ai.github.io/langgraphjs/how-tos#persistence)



# How to add cross-thread persistence (functional API)[¶](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#how-to-add-cross-thread-persistence-functional-api "Permanent link")

Prerequisites

This guide assumes familiarity with the following:

  * [Functional API](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/)
  * [Persistence](https://langchain-ai.github.io/langgraphjs/concepts/persistence/)
  * [Memory](https://langchain-ai.github.io/langgraphjs/concepts/memory/)
  * [Chat Models](https://js.langchain.com/docs/concepts/chat_models/)



LangGraph allows you to persist data across **different[threads](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#threads)**. For instance, you can store information about users (their names or preferences) in a shared (cross-thread) memory and reuse them in the new threads (e.g., new conversations).

When using the [functional API](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/), you can set it up to store and retrieve memories by using the [Store](https://langchain-ai.github.io/langgraphjs/reference/classes/checkpoint.BaseStore.html) interface:

  1. Create an instance of a `Store`

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-0-1)import{InMemoryStore}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-0-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-0-3)conststore=newInMemoryStore();

```


  2. Pass the `store` instance to the `entrypoint()` wrapper function. It will be passed to the workflow as `config.store`.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-1-1)import{entrypoint}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-1-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-1-3)constworkflow=entrypoint({
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-1-4)store,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-1-5)name:"myWorkflow",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-1-6)},async(input,config)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-1-7)constfoo=awaitmyTask({input,store:config.store});
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-1-8)...
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-1-9)});

```





In this guide, we will show how to construct and use a workflow that has a shared memory implemented using the [Store](https://langchain-ai.github.io/langgraphjs/reference/classes/checkpoint.BaseStore.html) interface.

Note

If you need to add cross-thread persistence to a `StateGraph`, check out this [how-to guide](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence).

## Setup[¶](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#setup "Permanent link")

Note

This guide requires `@langchain/langgraph>=0.2.42`.

First, install the required dependencies for this example:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-2-1)npminstall@langchain/langgraph@langchain/openai@langchain/anthropic@langchain/coreuuid

```


Next, we need to set API keys for Anthropic and OpenAI (the LLM and embeddings we will use):

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-3-1)process.env.OPENAI_API_KEY="YOUR_API_KEY";
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-3-2)process.env.ANTHROPIC_API_KEY="YOUR_API_KEY";

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com)

## Example: simple chatbot with long-term memory[¶](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#example-simple-chatbot-with-long-term-memory "Permanent link")

### Define store[¶](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#define-store "Permanent link")

In this example we will create a workflow that will be able to retrieve information about a user's preferences. We will do so by defining an `InMemoryStore` - an object that can store data in memory and query that data.

When storing objects using the `Store` interface you define two things:

  * the namespace for the object, a tuple (similar to directories)
  * the object key (similar to filenames)



In our example, we'll be using `["memories", <user_id>]` as namespace and random UUID as key for each new memory.

Let's first define our store:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-4-1)import{InMemoryStore}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-4-2)import{OpenAIEmbeddings}from"@langchain/openai";
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-4-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-4-4)constinMemoryStore=newInMemoryStore({
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-4-5)index:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-4-6)embeddings:newOpenAIEmbeddings({
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-4-7)model:"text-embedding-3-small",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-4-8)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-4-9)dims:1536,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-4-10)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-4-11)});

```


### Create workflow[¶](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#create-workflow "Permanent link")

Now let's create our workflow:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-1)import{v4}from"uuid";
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-2)import{ChatAnthropic}from"@langchain/anthropic";
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-3)import{
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-4)entrypoint,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-5)task,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-6)MemorySaver,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-7)addMessages,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-8)typeBaseStore,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-9)getStore,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-10)}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-11)importtype{BaseMessage,BaseMessageLike}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-12)
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-13)constmodel=newChatAnthropic({
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-14)model:"claude-3-5-sonnet-latest",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-15)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-16)
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-17)constcallModel=task("callModel",async(
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-18)messages:BaseMessage[],
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-19)memoryStore:BaseStore,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-20)userId:string
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-21))=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-22)constnamespace=["memories",userId];
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-23)constlastMessage=messages.at(-1);
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-24)if(typeoflastMessage?.content!=="string"){
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-25)thrownewError("Received non-string message content.");
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-26)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-27)constmemories=awaitmemoryStore.search(namespace,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-28)query:lastMessage.content,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-29)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-30)constinfo=memories.map((memory)=>memory.value.data).join("\n");
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-31)constsystemMessage=`You are a helpful assistant talking to the user. User info: ${info}`;
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-32)
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-33)// Store new memories if the user asks the model to remember
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-34)if(lastMessage.content.toLowerCase().includes("remember")){
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-35)// Hard-coded for demo
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-36)constmemory=`Username is Bob`;
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-37)awaitmemoryStore.put(namespace,v4(),{data:memory});
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-38)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-39)constresponse=awaitmodel.invoke([
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-40){
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-41)role:"system",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-42)content:systemMessage
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-43)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-44)...messages
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-45)]);
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-46)returnresponse;
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-47)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-48)
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-49)// NOTE: we're passing the store object here when creating a workflow via entrypoint()
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-50)constworkflow=entrypoint({
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-51)checkpointer:newMemorySaver(),
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-52)store:inMemoryStore,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-53)name:"workflow",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-54)},async(params:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-55)messages:BaseMessageLike[];
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-56)userId:string;
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-57)},config)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-58)constmessages=addMessages([],params.messages)
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-59)constresponse=awaitcallModel(messages,config.store,params.userId);
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-60)returnentrypoint.final({
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-61)value:response,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-62)save:addMessages(messages,response),
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-63)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-5-64)});

```


The current store is passed in as part of the entrypoint's second argument, as `config.store`.

Note

If you're using LangGraph Cloud or LangGraph Studio, you **don't need** to pass store into the entrypoint, since it's done automatically.

### Run the workflow![¶](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#run-the-workflow "Permanent link")

Now let's specify a user ID in the config and tell the model our name:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-6-1)constconfig={
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-6-2)configurable:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-6-3)thread_id:"1",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-6-4)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-6-5)streamMode:"values"asconst,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-6-6)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-6-7)
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-6-8)constinputMessage={
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-6-9)role:"user",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-6-10)content:"Hi! Remember: my name is Bob",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-6-11)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-6-12)
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-6-13)conststream=awaitworkflow.stream({messages:[inputMessage],userId:"1"},config);
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-6-14)
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-6-15)forawait(constchunkofstream){
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-6-16)console.log(chunk);
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-6-17)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-7-1)AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-7-2) "id": "msg_01U4xHvf4REPSCGWzpLeh1qJ",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-7-3) "content": "Hi Bob! Nice to meet you. I'll remember that your name is Bob. How can I help you today?",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-7-4) "additional_kwargs": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-7-5)  "id": "msg_01U4xHvf4REPSCGWzpLeh1qJ",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-7-6)  "type": "message",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-7-7)  "role": "assistant",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-7-8)  "model": "claude-3-5-sonnet-20241022",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-7-9)  "stop_reason": "end_turn",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-7-10)  "stop_sequence": null,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-7-11)  "usage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-7-12)   "input_tokens": 28,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-7-13)   "cache_creation_input_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-7-14)   "cache_read_input_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-7-15)   "output_tokens": 27
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-7-16)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-7-17) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-7-18) "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-7-19)  "id": "msg_01U4xHvf4REPSCGWzpLeh1qJ",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-7-20)  "model": "claude-3-5-sonnet-20241022",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-7-21)  "stop_reason": "end_turn",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-7-22)  "stop_sequence": null,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-7-23)  "usage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-7-24)   "input_tokens": 28,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-7-25)   "cache_creation_input_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-7-26)   "cache_read_input_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-7-27)   "output_tokens": 27
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-7-28)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-7-29)  "type": "message",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-7-30)  "role": "assistant"
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-7-31) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-7-32) "tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-7-33) "invalid_tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-7-34) "usage_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-7-35)  "input_tokens": 28,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-7-36)  "output_tokens": 27,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-7-37)  "total_tokens": 55,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-7-38)  "input_token_details": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-7-39)   "cache_creation": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-7-40)   "cache_read": 0
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-7-41)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-7-42) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-7-43)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-8-1)constconfig2={
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-8-2)configurable:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-8-3)thread_id:"2",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-8-4)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-8-5)streamMode:"values"asconst,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-8-6)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-8-7)
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-8-8)constfollowupStream=awaitworkflow.stream({
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-8-9)messages:[{
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-8-10)role:"user",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-8-11)content:"what is my name?",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-8-12)}],
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-8-13)userId:"1"
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-8-14)},config2);
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-8-15)
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-8-16)forawait(constchunkoffollowupStream){
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-8-17)console.log(chunk);
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-8-18)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-9-1)AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-9-2) "id": "msg_01LB4YapkFawBUbpiu3oeWbF",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-9-3) "content": "Your name is Bob.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-9-4) "additional_kwargs": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-9-5)  "id": "msg_01LB4YapkFawBUbpiu3oeWbF",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-9-6)  "type": "message",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-9-7)  "role": "assistant",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-9-8)  "model": "claude-3-5-sonnet-20241022",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-9-9)  "stop_reason": "end_turn",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-9-10)  "stop_sequence": null,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-9-11)  "usage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-9-12)   "input_tokens": 28,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-9-13)   "cache_creation_input_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-9-14)   "cache_read_input_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-9-15)   "output_tokens": 8
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-9-16)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-9-17) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-9-18) "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-9-19)  "id": "msg_01LB4YapkFawBUbpiu3oeWbF",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-9-20)  "model": "claude-3-5-sonnet-20241022",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-9-21)  "stop_reason": "end_turn",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-9-22)  "stop_sequence": null,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-9-23)  "usage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-9-24)   "input_tokens": 28,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-9-25)   "cache_creation_input_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-9-26)   "cache_read_input_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-9-27)   "output_tokens": 8
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-9-28)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-9-29)  "type": "message",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-9-30)  "role": "assistant"
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-9-31) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-9-32) "tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-9-33) "invalid_tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-9-34) "usage_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-9-35)  "input_tokens": 28,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-9-36)  "output_tokens": 8,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-9-37)  "total_tokens": 36,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-9-38)  "input_token_details": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-9-39)   "cache_creation": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-9-40)   "cache_read": 0
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-9-41)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-9-42) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-9-43)}

```


We can now inspect our in-memory store and verify that we have in fact saved the memories for the user: 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-10-1)constmemories=awaitinMemoryStore.search(["memories","1"]);
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-10-2)for(constmemoryofmemories){
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-10-3)console.log(memory.value);
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-10-4)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-11-1){ data: 'Username is Bob' }

```


Let's now run the workflow for another user to verify that the memories about the first user are self contained: 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-12-1)constconfig3={
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-12-2)configurable:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-12-3)thread_id:"3",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-12-4)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-12-5)streamMode:"values"asconst,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-12-6)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-12-7)
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-12-8)constotherUserStream=awaitworkflow.stream({
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-12-9)messages:[{
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-12-10)role:"user",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-12-11)content:"what is my name?",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-12-12)}],
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-12-13)userId:"2"
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-12-14)},config3);
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-12-15)
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-12-16)forawait(constchunkofotherUserStream){
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-12-17)console.log(chunk);
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-12-18)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-13-1)AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-13-2) "id": "msg_01KK7CweVY4ZdHxU5bPa4skv",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-13-3) "content": "I don't have any information about your name. While I aim to be helpful, I can only know what you directly tell me during our conversation.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-13-4) "additional_kwargs": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-13-5)  "id": "msg_01KK7CweVY4ZdHxU5bPa4skv",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-13-6)  "type": "message",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-13-7)  "role": "assistant",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-13-8)  "model": "claude-3-5-sonnet-20241022",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-13-9)  "stop_reason": "end_turn",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-13-10)  "stop_sequence": null,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-13-11)  "usage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-13-12)   "input_tokens": 25,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-13-13)   "cache_creation_input_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-13-14)   "cache_read_input_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-13-15)   "output_tokens": 33
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-13-16)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-13-17) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-13-18) "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-13-19)  "id": "msg_01KK7CweVY4ZdHxU5bPa4skv",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-13-20)  "model": "claude-3-5-sonnet-20241022",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-13-21)  "stop_reason": "end_turn",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-13-22)  "stop_sequence": null,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-13-23)  "usage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-13-24)   "input_tokens": 25,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-13-25)   "cache_creation_input_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-13-26)   "cache_read_input_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-13-27)   "output_tokens": 33
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-13-28)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-13-29)  "type": "message",
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-13-30)  "role": "assistant"
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-13-31) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-13-32) "tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-13-33) "invalid_tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-13-34) "usage_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-13-35)  "input_tokens": 25,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-13-36)  "output_tokens": 33,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-13-37)  "total_tokens": 58,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-13-38)  "input_token_details": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-13-39)   "cache_creation": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-13-40)   "cache_read": 0
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-13-41)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-13-42) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__codelineno-13-43)}

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to add cross-thread persistence to your graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/) [ Next  How to use Postgres checkpointer for persistence  ](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
