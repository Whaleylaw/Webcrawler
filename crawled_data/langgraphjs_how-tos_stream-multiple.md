---
url: https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#how-to-configure-multiple-streaming-modes-at-the-same-time)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to configure multiple streaming modes at the same time 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/?q= "Share")

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
          * Streaming  Streaming 
            * [ Streaming  ](https://langchain-ai.github.io/langgraphjs/how-tos#streaming)
            * [ How to stream full state of your graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/)
            * [ How to stream state updates of your graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-updates/)
            * [ How to stream LLM tokens from your graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/)
            * [ How to stream LLM tokens (without LangChain models)  ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/)
            * [ How to stream custom data  ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/)
            * How to configure multiple streaming modes at the same time  [ How to configure multiple streaming modes at the same time  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#setup)
              * [ Define the graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#define-the-graph)
              * [ Stream Multiple  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#stream-multiple)
            * [ How to stream events from within a tool  ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/)
            * [ How to stream from the final node  ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-from-final-node/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#setup)
  * [ Define the graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#define-the-graph)
  * [ Stream Multiple  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#stream-multiple)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
  5. [ Streaming  ](https://langchain-ai.github.io/langgraphjs/how-tos#streaming)



# How to configure multiple streaming modes at the same time[¶](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#how-to-configure-multiple-streaming-modes-at-the-same-time "Permanent link")

This guide covers how to configure multiple streaming modes at the same time.

## Setup[¶](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#setup "Permanent link")

First we need to install the packages required

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-0-1)npminstall@langchain/langgraph@langchain/openai@langchain/core

```


Next, we need to set API keys for OpenAI (the LLM we will use)

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-1-1)exportOPENAI_API_KEY=your-api-key

```


Optionally, we can set API key for [LangSmith tracing](https://smith.langchain.com/), which will give us best-in-class observability.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-2-1)exportLANGCHAIN_TRACING_V2="true"
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-2-2)exportLANGCHAIN_CALLBACKS_BACKGROUND="true"
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-2-3)exportLANGCHAIN_API_KEY=your-api-key

```


## Define the graph[¶](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#define-the-graph "Permanent link")

We'll be using a prebuilt ReAct agent for this guide.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-3-1)import{ChatOpenAI}from"@langchain/openai";
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-3-2)import{tool}from'@langchain/core/tools';
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-3-3)import{z}from'zod';
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-3-4)import{createReactAgent}from"@langchain/langgraph/prebuilt";
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-3-5)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-3-6)constmodel=newChatOpenAI({
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-3-7)model:"gpt-4o",
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-3-8)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-3-9)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-3-10)constgetWeather=tool((input)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-3-11)if(["sf","san francisco","san francisco, ca"].includes(input.location.toLowerCase())){
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-3-12)return"It's 60 degrees and foggy.";
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-3-13)}else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-3-14)return"It's 90 degrees and sunny.";
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-3-15)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-3-16)},{
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-3-17)name:"get_weather",
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-3-18)description:"Call to get the current weather.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-3-19)schema:z.object({
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-3-20)location:z.string().describe("Location to get the weather for."),
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-3-21)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-3-22)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-3-23)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-3-24)constgraph=createReactAgent({llm:model,tools:[getWeather]});

```


## Stream Multiple[¶](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#stream-multiple "Permanent link")

To get multiple types of streamed chunks, pass an array of values under the `streamMode` key in the second argument to `.stream()`:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-4-1)letinputs={messages:[{role:"user",content:"what's the weather in sf?"}]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-4-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-4-3)letstream=awaitgraph.stream(inputs,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-4-4)streamMode:["updates","debug"],
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-4-5)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-4-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-4-7)forawait(constchunkofstream){
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-4-8)console.log(`Receiving new event of type: ${chunk[0]}`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-4-9)console.log(chunk[1]);
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-4-10)console.log("\n====\n");
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-4-11)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-1)Receiving new event of type: debug
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-2){
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-3) type: 'task',
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-4) timestamp: '2024-08-30T20:58:58.404Z',
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-5) step: 1,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-6) payload: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-7)  id: '768110dd-6004-59f3-8671-6ca699cccd71',
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-8)  name: 'agent',
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-9)  input: { messages: [Array] },
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-10)  triggers: [ 'start:agent' ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-11)  interrupts: []
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-12) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-13)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-14)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-15)====
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-16)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-17)Receiving new event of type: updates
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-18){
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-19) agent: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-20)  messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-21)   AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-22)    "id": "chatcmpl-A22zqTwumhtW8TMjQ1FxlzCEMBk0R",
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-23)    "content": "",
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-24)    "additional_kwargs": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-25)     "tool_calls": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-26)      {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-27)       "id": "call_HAfilebE1q9E9OQHOlL3JYHP",
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-28)       "type": "function",
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-29)       "function": "[Object]"
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-30)      }
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-31)     ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-32)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-33)    "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-34)     "tokenUsage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-35)      "completionTokens": 15,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-36)      "promptTokens": 59,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-37)      "totalTokens": 74
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-38)     },
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-39)     "finish_reason": "tool_calls",
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-40)     "system_fingerprint": "fp_157b3831f5"
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-41)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-42)    "tool_calls": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-43)     {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-44)      "name": "get_weather",
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-45)      "args": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-46)       "location": "San Francisco"
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-47)      },
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-48)      "type": "tool_call",
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-49)      "id": "call_HAfilebE1q9E9OQHOlL3JYHP"
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-50)     }
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-51)    ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-52)    "invalid_tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-53)    "usage_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-54)     "input_tokens": 59,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-55)     "output_tokens": 15,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-56)     "total_tokens": 74
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-57)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-58)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-59)  ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-60) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-61)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-62)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-63)====
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-64)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-65)Receiving new event of type: debug
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-66){
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-67) type: 'task_result',
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-68) timestamp: '2024-08-30T20:58:59.072Z',
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-69) step: 1,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-70) payload: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-71)  id: '768110dd-6004-59f3-8671-6ca699cccd71',
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-72)  name: 'agent',
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-73)  result: [ [Array] ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-74) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-75)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-76)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-77)====
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-78)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-79)Receiving new event of type: debug
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-80){
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-81) type: 'task',
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-82) timestamp: '2024-08-30T20:58:59.074Z',
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-83) step: 2,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-84) payload: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-85)  id: '76459c18-5621-5893-9b93-13bc1db3ba6d',
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-86)  name: 'tools',
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-87)  input: { messages: [Array] },
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-88)  triggers: [ 'branch:agent:shouldContinue:tools' ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-89)  interrupts: []
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-90) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-91)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-92)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-93)====
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-94)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-95)Receiving new event of type: updates
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-96){
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-97) tools: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-98)  messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-99)   ToolMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-100)    "content": "It's 60 degrees and foggy.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-101)    "name": "get_weather",
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-102)    "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-103)    "response_metadata": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-104)    "tool_call_id": "call_HAfilebE1q9E9OQHOlL3JYHP"
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-105)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-106)  ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-107) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-108)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-109)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-110)====
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-111)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-112)Receiving new event of type: debug
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-113){
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-114) type: 'task_result',
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-115) timestamp: '2024-08-30T20:58:59.076Z',
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-116) step: 2,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-117) payload: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-118)  id: '76459c18-5621-5893-9b93-13bc1db3ba6d',
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-119)  name: 'tools',
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-120)  result: [ [Array] ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-121) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-122)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-123)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-124)====
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-125)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-126)Receiving new event of type: debug
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-127){
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-128) type: 'task',
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-129) timestamp: '2024-08-30T20:58:59.077Z',
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-130) step: 3,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-131) payload: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-132)  id: '565d8a53-1057-5d83-bda8-ba3fada24b70',
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-133)  name: 'agent',
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-134)  input: { messages: [Array] },
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-135)  triggers: [ 'tools' ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-136)  interrupts: []
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-137) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-138)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-139)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-140)====
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-141)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-142)Receiving new event of type: updates
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-143){
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-144) agent: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-145)  messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-146)   AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-147)    "id": "chatcmpl-A22zrdeobsBzkiES0C6Twh3p7I344",
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-148)    "content": "The weather in San Francisco right now is 60 degrees and foggy.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-149)    "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-150)    "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-151)     "tokenUsage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-152)      "completionTokens": 16,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-153)      "promptTokens": 90,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-154)      "totalTokens": 106
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-155)     },
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-156)     "finish_reason": "stop",
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-157)     "system_fingerprint": "fp_157b3831f5"
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-158)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-159)    "tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-160)    "invalid_tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-161)    "usage_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-162)     "input_tokens": 90,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-163)     "output_tokens": 16,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-164)     "total_tokens": 106
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-165)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-166)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-167)  ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-168) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-169)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-170)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-171)====
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-172)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-173)Receiving new event of type: debug
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-174){
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-175) type: 'task_result',
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-176) timestamp: '2024-08-30T20:58:59.640Z',
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-177) step: 3,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-178) payload: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-179)  id: '565d8a53-1057-5d83-bda8-ba3fada24b70',
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-180)  name: 'agent',
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-181)  result: [ [Array] ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-182) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-183)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-184)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__codelineno-5-185)====

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to stream custom data  ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/) [ Next  How to stream events from within a tool  ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
