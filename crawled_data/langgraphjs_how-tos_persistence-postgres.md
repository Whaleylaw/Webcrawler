---
url: https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#how-to-use-postgres-checkpointer-for-persistence)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to use Postgres checkpointer for persistence 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/?q= "Share")

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
            * [ How to add cross-thread persistence (functional API)  ](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/)
            * How to use Postgres checkpointer for persistence  [ How to use Postgres checkpointer for persistence  ](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#setup)
              * [ Define model and tools for the graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#define-model-and-tools-for-the-graph)
              * [ With a connection pool  ](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#with-a-connection-pool)
                * [ With a connection string  ](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#with-a-connection-string)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#setup)
  * [ Define model and tools for the graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#define-model-and-tools-for-the-graph)
  * [ With a connection pool  ](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#with-a-connection-pool)
    * [ With a connection string  ](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#with-a-connection-string)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
  5. [ Persistence  ](https://langchain-ai.github.io/langgraphjs/how-tos#persistence)



# How to use Postgres checkpointer for persistence[¶](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#how-to-use-postgres-checkpointer-for-persistence "Permanent link")

Prerequisites

This guide assumes familiarity with the following: 

  * [ Persistence ](https://langchain-ai.github.io/langgraphjs/concepts/persistence/)
  * [ Postgresql ](https://www.postgresql.org/about/)



When creating LangGraph agents, you can set them up so that they persist their state across executions. This allows you to do things like interact with an agent multiple times and have it remember previous interactions.

This how-to guide shows how to use Postgres as the backend for persisting checkpoint state using the `@langchain/langgraph-checkpoint-postgres`[](https://github.com/langchain-ai/langgraphjs/tree/main/libs/checkpoint-postgres) library and the `PostgresSaver`[](https://langchain-ai.github.io/langgraphjs/reference/classes/checkpoint_postgres.PostgresSaver.html) class.

For demonstration purposes we will add persistence to the [pre-built create react agent](https://langchain-ai.github.io/langgraphjs/reference/functions/langgraph_prebuilt.createReactAgent.html). 

In general, you can add a checkpointer to any custom graph that you build like this:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-0-1)import{StateGraph}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-0-2)import{PostgresSaver}from"@langchain/langgraph-checkpoint-postgres";
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-0-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-0-4)constbuilder=newStateGraph(...);
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-0-5)
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-0-6)// ... define the graph
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-0-7)
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-0-8)constcheckpointer=PostgresSaver.fromConnString(...);// postgres checkpointer (see examples below)
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-0-9)
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-0-10)constgraph=builder.compile({checkpointer});
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-0-11)...

```


## Setup[¶](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#setup "Permanent link")

You will need access to a Postgres instance. This guide will also use OpenAI, so you will need an OpenAI API key.

First, install the required packages:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-1-1)npminstall@langchain/langgraph@langchain/core@langchain/langgraph-checkpoint-postgres

```


Then, set your OpenAI API key as `process.env.OPENAI_API_KEY`.

Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Define model and tools for the graph[¶](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#define-model-and-tools-for-the-graph "Permanent link")

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-2-1)import{z}from"zod";
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-2-2)import{tool}from"@langchain/core/tools";
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-2-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-2-4)constgetWeather=tool(async(input:{city:"sf"|"nyc"})=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-2-5)if(input.city==="nyc"){
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-2-6)return"It might be cloudy in nyc";
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-2-7)}elseif(input.city==="sf"){
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-2-8)return"It's always sunny in sf";
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-2-9)}else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-2-10)thrownewError("Unknown city");
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-2-11)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-2-12)},{
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-2-13)name:"get_weather",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-2-14)description:"Use this to get weather information.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-2-15)schema:z.object({
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-2-16)city:z.enum(["sf","nyc"])
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-2-17)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-2-18)});

```


## With a connection pool[¶](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#with-a-connection-pool "Permanent link")

Under the hood, `PostgresSaver` uses the `node-postgres`[](https://www.npmjs.com/package/pg) (`pg`) package to connect to your Postgres instance. You can pass in a [connection pool](https://node-postgres.com/apis/pool) that you've instantiated like this:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-3-1)import{ChatOpenAI}from"@langchain/openai";
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-3-2)import{PostgresSaver}from"@langchain/langgraph-checkpoint-postgres";
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-3-3)import{createReactAgent}from"@langchain/langgraph/prebuilt";
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-3-4)
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-3-5)importpgfrom"pg";
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-3-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-3-7)const{Pool}=pg;
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-3-8)
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-3-9)constpool=newPool({
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-3-10)connectionString:"postgresql://user:password@localhost:5434/testdb"
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-3-11)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-3-12)
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-3-13)constcheckpointer=newPostgresSaver(pool);
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-3-14)
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-3-15)// NOTE: you need to call .setup() the first time you're using your checkpointer
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-3-16)
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-3-17)awaitcheckpointer.setup();
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-3-18)
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-3-19)constgraph=createReactAgent({
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-3-20)tools:[getWeather],
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-3-21)llm:newChatOpenAI({
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-3-22)model:"gpt-4o-mini",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-3-23)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-3-24)checkpointSaver:checkpointer,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-3-25)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-3-26)constconfig={configurable:{thread_id:"1"}};
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-3-27)
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-3-28)awaitgraph.invoke({
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-3-29)messages:[{
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-3-30)role:"user",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-3-31)content:"what's the weather in sf"
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-3-32)}],
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-3-33)},config);

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-1){
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-2) messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-3)  HumanMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-4)   "id": "ac832b73-242d-4d0b-80d7-5d06a908787e",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-5)   "content": "what's the weather in sf",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-6)   "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-7)   "response_metadata": {}
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-8)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-9)  AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-10)   "id": "chatcmpl-AGC3tgRXInGLo0qzrD5u3gNqNOegf",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-11)   "content": "",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-12)   "additional_kwargs": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-13)    "tool_calls": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-14)     {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-15)      "id": "call_I2Ceef2LoxjeaR9m8ZkY7U1R",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-16)      "type": "function",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-17)      "function": "[Object]"
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-18)     }
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-19)    ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-20)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-21)   "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-22)    "tokenUsage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-23)     "completionTokens": 14,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-24)     "promptTokens": 57,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-25)     "totalTokens": 71
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-26)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-27)    "finish_reason": "tool_calls",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-28)    "system_fingerprint": "fp_f85bea6784"
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-29)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-30)   "tool_calls": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-31)    {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-32)     "name": "get_weather",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-33)     "args": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-34)      "city": "sf"
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-35)     },
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-36)     "type": "tool_call",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-37)     "id": "call_I2Ceef2LoxjeaR9m8ZkY7U1R"
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-38)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-39)   ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-40)   "invalid_tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-41)   "usage_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-42)    "input_tokens": 57,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-43)    "output_tokens": 14,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-44)    "total_tokens": 71
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-45)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-46)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-47)  ToolMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-48)   "id": "6533d271-6126-40af-b5d0-23a484853a97",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-49)   "content": "It's always sunny in sf",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-50)   "name": "get_weather",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-51)   "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-52)   "response_metadata": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-53)   "tool_call_id": "call_I2Ceef2LoxjeaR9m8ZkY7U1R"
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-54)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-55)  AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-56)   "id": "chatcmpl-AGC3ttvB69pQu0atw0lUzTpNePlPn",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-57)   "content": "The weather in San Francisco (SF) is always sunny!",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-58)   "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-59)   "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-60)    "tokenUsage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-61)     "completionTokens": 13,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-62)     "promptTokens": 84,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-63)     "totalTokens": 97
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-64)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-65)    "finish_reason": "stop",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-66)    "system_fingerprint": "fp_f85bea6784"
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-67)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-68)   "tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-69)   "invalid_tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-70)   "usage_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-71)    "input_tokens": 84,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-72)    "output_tokens": 13,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-73)    "total_tokens": 97
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-74)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-75)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-76) ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-4-77)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-5-1)awaitcheckpointer.get(config);

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-1){
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-2) v: 1,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-3) id: '1ef85bc6-bd28-67c1-8003-5cb7dab561b0',
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-4) ts: '2024-10-08T21:29:38.109Z',
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-5) pending_sends: [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-6) versions_seen: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-7)  agent: { tools: 4, '__start__:agent': 2 },
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-8)  tools: { 'branch:agent:shouldContinue:tools': 3 },
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-9)  __input__: {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-10)  __start__: { __start__: 1 }
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-11) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-12) channel_versions: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-13)  agent: 5,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-14)  tools: 5,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-15)  messages: 5,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-16)  __start__: 2,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-17)  '__start__:agent': 3,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-18)  'branch:agent:shouldContinue:tools': 4
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-19) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-20) channel_values: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-21)  agent: 'agent',
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-22)  messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-23)   HumanMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-24)    "id": "ac832b73-242d-4d0b-80d7-5d06a908787e",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-25)    "content": "what's the weather in sf",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-26)    "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-27)    "response_metadata": {}
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-28)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-29)   AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-30)    "id": "chatcmpl-AGC3tgRXInGLo0qzrD5u3gNqNOegf",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-31)    "content": "",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-32)    "additional_kwargs": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-33)     "tool_calls": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-34)      {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-35)       "id": "call_I2Ceef2LoxjeaR9m8ZkY7U1R",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-36)       "type": "function",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-37)       "function": "[Object]"
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-38)      }
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-39)     ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-40)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-41)    "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-42)     "tokenUsage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-43)      "completionTokens": 14,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-44)      "promptTokens": 57,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-45)      "totalTokens": 71
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-46)     },
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-47)     "finish_reason": "tool_calls",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-48)     "system_fingerprint": "fp_f85bea6784"
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-49)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-50)    "tool_calls": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-51)     {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-52)      "name": "get_weather",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-53)      "args": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-54)       "city": "sf"
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-55)      },
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-56)      "type": "tool_call",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-57)      "id": "call_I2Ceef2LoxjeaR9m8ZkY7U1R"
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-58)     }
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-59)    ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-60)    "invalid_tool_calls": []
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-61)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-62)   ToolMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-63)    "id": "6533d271-6126-40af-b5d0-23a484853a97",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-64)    "content": "It's always sunny in sf",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-65)    "name": "get_weather",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-66)    "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-67)    "response_metadata": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-68)    "tool_call_id": "call_I2Ceef2LoxjeaR9m8ZkY7U1R"
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-69)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-70)   AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-71)    "id": "chatcmpl-AGC3ttvB69pQu0atw0lUzTpNePlPn",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-72)    "content": "The weather in San Francisco (SF) is always sunny!",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-73)    "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-74)    "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-75)     "tokenUsage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-76)      "completionTokens": 13,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-77)      "promptTokens": 84,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-78)      "totalTokens": 97
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-79)     },
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-80)     "finish_reason": "stop",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-81)     "system_fingerprint": "fp_f85bea6784"
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-82)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-83)    "tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-84)    "invalid_tool_calls": []
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-85)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-86)  ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-87) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-6-88)}

```


### With a connection string[¶](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#with-a-connection-string "Permanent link")

You can also create a pool internally by passing a connection string to the `.fromConnString` static method:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-7-1)constcheckpointerFromConnString=PostgresSaver.fromConnString(
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-7-2)"postgresql://user:password@localhost:5434/testdb"
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-7-3));
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-7-4)
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-7-5)constgraph2=createReactAgent({
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-7-6)tools:[getWeather],
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-7-7)llm:newChatOpenAI({
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-7-8)model:"gpt-4o-mini",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-7-9)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-7-10)checkpointSaver:checkpointerFromConnString,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-7-11)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-7-12)constconfig2={configurable:{thread_id:"2"}};
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-7-13)
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-7-14)awaitgraph2.invoke({
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-7-15)messages:[{
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-7-16)role:"user",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-7-17)content:"what's the weather in sf"
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-7-18)}],
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-7-19)},config2);

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-1){
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-2) messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-3)  HumanMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-4)   "id": "c17b65af-6ac5-411e-ab5c-8003dc53755d",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-5)   "content": "what's the weather in sf",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-6)   "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-7)   "response_metadata": {}
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-8)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-9)  AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-10)   "id": "chatcmpl-AGC6n8XO05i1Z7f4GnOqpayLPxgoF",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-11)   "content": "",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-12)   "additional_kwargs": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-13)    "tool_calls": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-14)     {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-15)      "id": "call_n9QCrJ4QbmgFkr5fHEsQHCCO",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-16)      "type": "function",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-17)      "function": "[Object]"
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-18)     }
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-19)    ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-20)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-21)   "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-22)    "tokenUsage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-23)     "completionTokens": 14,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-24)     "promptTokens": 57,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-25)     "totalTokens": 71
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-26)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-27)    "finish_reason": "tool_calls",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-28)    "system_fingerprint": "fp_f85bea6784"
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-29)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-30)   "tool_calls": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-31)    {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-32)     "name": "get_weather",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-33)     "args": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-34)      "city": "sf"
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-35)     },
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-36)     "type": "tool_call",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-37)     "id": "call_n9QCrJ4QbmgFkr5fHEsQHCCO"
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-38)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-39)   ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-40)   "invalid_tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-41)   "usage_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-42)    "input_tokens": 57,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-43)    "output_tokens": 14,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-44)    "total_tokens": 71
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-45)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-46)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-47)  ToolMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-48)   "id": "779c26b0-6b75-454e-98ef-ecca79e50e8c",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-49)   "content": "It's always sunny in sf",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-50)   "name": "get_weather",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-51)   "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-52)   "response_metadata": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-53)   "tool_call_id": "call_n9QCrJ4QbmgFkr5fHEsQHCCO"
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-54)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-55)  AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-56)   "id": "chatcmpl-AGC6ngqEV0EBZbPwHf2JgTw0n16D8",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-57)   "content": "The weather in San Francisco (SF) is described as always sunny.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-58)   "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-59)   "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-60)    "tokenUsage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-61)     "completionTokens": 15,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-62)     "promptTokens": 84,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-63)     "totalTokens": 99
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-64)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-65)    "finish_reason": "stop",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-66)    "system_fingerprint": "fp_74ba47b4ac"
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-67)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-68)   "tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-69)   "invalid_tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-70)   "usage_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-71)    "input_tokens": 84,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-72)    "output_tokens": 15,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-73)    "total_tokens": 99
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-74)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-75)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-76) ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-8-77)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-9-1)awaitcheckpointerFromConnString.get(config2);

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-1){
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-2) v: 1,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-3) id: '1ef85bcd-71b9-6671-8003-6e734c8e9679',
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-4) ts: '2024-10-08T21:32:38.103Z',
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-5) pending_sends: [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-6) versions_seen: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-7)  agent: { tools: 4, '__start__:agent': 2 },
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-8)  tools: { 'branch:agent:shouldContinue:tools': 3 },
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-9)  __input__: {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-10)  __start__: { __start__: 1 }
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-11) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-12) channel_versions: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-13)  agent: 5,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-14)  tools: 5,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-15)  messages: 5,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-16)  __start__: 2,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-17)  '__start__:agent': 3,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-18)  'branch:agent:shouldContinue:tools': 4
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-19) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-20) channel_values: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-21)  agent: 'agent',
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-22)  messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-23)   HumanMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-24)    "id": "c17b65af-6ac5-411e-ab5c-8003dc53755d",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-25)    "content": "what's the weather in sf",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-26)    "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-27)    "response_metadata": {}
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-28)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-29)   AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-30)    "id": "chatcmpl-AGC6n8XO05i1Z7f4GnOqpayLPxgoF",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-31)    "content": "",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-32)    "additional_kwargs": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-33)     "tool_calls": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-34)      {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-35)       "id": "call_n9QCrJ4QbmgFkr5fHEsQHCCO",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-36)       "type": "function",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-37)       "function": "[Object]"
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-38)      }
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-39)     ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-40)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-41)    "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-42)     "tokenUsage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-43)      "completionTokens": 14,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-44)      "promptTokens": 57,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-45)      "totalTokens": 71
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-46)     },
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-47)     "finish_reason": "tool_calls",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-48)     "system_fingerprint": "fp_f85bea6784"
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-49)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-50)    "tool_calls": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-51)     {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-52)      "name": "get_weather",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-53)      "args": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-54)       "city": "sf"
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-55)      },
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-56)      "type": "tool_call",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-57)      "id": "call_n9QCrJ4QbmgFkr5fHEsQHCCO"
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-58)     }
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-59)    ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-60)    "invalid_tool_calls": []
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-61)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-62)   ToolMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-63)    "id": "779c26b0-6b75-454e-98ef-ecca79e50e8c",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-64)    "content": "It's always sunny in sf",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-65)    "name": "get_weather",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-66)    "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-67)    "response_metadata": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-68)    "tool_call_id": "call_n9QCrJ4QbmgFkr5fHEsQHCCO"
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-69)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-70)   AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-71)    "id": "chatcmpl-AGC6ngqEV0EBZbPwHf2JgTw0n16D8",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-72)    "content": "The weather in San Francisco (SF) is described as always sunny.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-73)    "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-74)    "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-75)     "tokenUsage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-76)      "completionTokens": 15,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-77)      "promptTokens": 84,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-78)      "totalTokens": 99
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-79)     },
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-80)     "finish_reason": "stop",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-81)     "system_fingerprint": "fp_74ba47b4ac"
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-82)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-83)    "tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-84)    "invalid_tool_calls": []
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-85)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-86)  ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-87) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-10-88)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__codelineno-11-1)

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to add cross-thread persistence (functional API)  ](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/) [ Next  How to manage conversation history  ](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
