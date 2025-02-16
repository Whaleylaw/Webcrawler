---
url: https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#how-to-add-human-in-the-loop-processes-to-the-prebuilt-react-agent)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to add human-in-the-loop processes to the prebuilt ReAct agent 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/?q= "Share")

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
          * [ Subgraphs  ](https://langchain-ai.github.io/langgraphjs/how-tos#subgraphs)
          * [ Multi-agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/)
          * [ State Management  ](https://langchain-ai.github.io/langgraphjs/how-tos#state-management)
          * [ Other  ](https://langchain-ai.github.io/langgraphjs/how-tos#other)
          * Prebuilt ReAct Agent  Prebuilt ReAct Agent 
            * [ Prebuilt ReAct Agent  ](https://langchain-ai.github.io/langgraphjs/how-tos#prebuilt-react-agent)
            * [ How to use the prebuilt ReAct agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/)
            * [ How to add memory to the prebuilt ReAct agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/)
            * [ How to add a custom system prompt to the prebuilt ReAct agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/)
            * How to add human-in-the-loop processes to the prebuilt ReAct agent  [ How to add human-in-the-loop processes to the prebuilt ReAct agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#setup)
              * [ Code  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#code)
              * [ Usage  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#usage)
            * [ How to create a ReAct agent from scratch (Functional API)  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#setup)
  * [ Code  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#code)
  * [ Usage  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#usage)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
  5. [ Prebuilt ReAct Agent  ](https://langchain-ai.github.io/langgraphjs/how-tos#prebuilt-react-agent)



# How to add human-in-the-loop processes to the prebuilt ReAct agent[¶](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#how-to-add-human-in-the-loop-processes-to-the-prebuilt-react-agent "Permanent link")

This tutorial will show how to add human-in-the-loop processes to the prebuilt ReAct agent. Please see [this tutorial](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/create-react-agent.ipynb) for how to get started with the prebuilt ReAct agent

You can add a a breakpoint before tools are called by passing `interruptBefore: ["tools"]` to `createReactAgent`. Note that you need to be using a checkpointer for this to work.

## Setup[¶](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#setup "Permanent link")

First, we need to install the required packages.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-0-1)yarnadd@langchain/langgraph@langchain/openai@langchain/core

```


This guide will use OpenAI's GPT-4o model. We will optionally set our API key for [LangSmith tracing](https://smith.langchain.com/), which will give us best-in-class observability.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-1-1)// process.env.OPENAI_API_KEY = "sk_...";
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-1-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-1-3)// Optional, add tracing in LangSmith
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-1-4)// process.env.LANGCHAIN_API_KEY = "ls__..."
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-1-5)// process.env.LANGCHAIN_CALLBACKS_BACKGROUND = "true";
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-1-6)process.env.LANGCHAIN_CALLBACKS_BACKGROUND="true";
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-1-7)process.env.LANGCHAIN_TRACING_V2="true";
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-1-8)process.env.LANGCHAIN_PROJECT="ReAct Agent with human-in-the-loop: LangGraphJS";

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-2-1)ReAct Agent with human-in-the-loop: LangGraphJS

```


## Code[¶](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#code "Permanent link")

Now we can use the prebuilt `createReactAgent` function to setup our agent with human-in-the-loop interactions:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-3-1)import{ChatOpenAI}from"@langchain/openai";
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-3-2)import{tool}from'@langchain/core/tools';
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-3-3)import{z}from'zod';
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-3-4)import{createReactAgent}from"@langchain/langgraph/prebuilt";
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-3-5)import{MemorySaver}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-3-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-3-7)constmodel=newChatOpenAI({
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-3-8)model:"gpt-4o",
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-3-9)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-3-10)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-3-11)constgetWeather=tool((input)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-3-12)if(['sf','san francisco'].includes(input.location.toLowerCase())){
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-3-13)return'It\'s always sunny in sf';
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-3-14)}elseif(['nyc','new york city'].includes(input.location.toLowerCase())){
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-3-15)return'It might be cloudy in nyc';
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-3-16)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-3-17)else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-3-18)thrownewError("Unknown Location");
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-3-19)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-3-20)},{
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-3-21)name:'get_weather',
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-3-22)description:'Call to get the current weather in a given location.',
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-3-23)schema:z.object({
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-3-24)location:z.string().describe("Location to get the weather for."),
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-3-25)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-3-26)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-3-27)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-3-28)// Here we only save in-memory
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-3-29)constmemory=newMemorySaver();
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-3-30)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-3-31)constagent=createReactAgent({llm:model,tools:[getWeather],interruptBefore:["tools"],checkpointSaver:memory});

```


## Usage[¶](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#usage "Permanent link")

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-4-1)letinputs={messages:[{role:"user",content:"what is the weather in SF california?"}]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-4-2)letconfig={configurable:{thread_id:"1"}};
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-4-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-4-4)letstream=awaitagent.stream(inputs,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-4-5)...config,
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-4-6)streamMode:"values",
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-4-7)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-4-8)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-4-9)forawait(
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-4-10)const{messages}ofstream
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-4-11)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-4-12)letmsg=messages[messages?.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-4-13)if(msg?.content){
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-4-14)console.log(msg.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-4-15)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-4-16)if(msg?.tool_calls?.length>0){
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-4-17)console.log(msg.tool_calls);
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-4-18)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-4-19)console.log("-----\n");
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-4-20)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-5-1)what is the weather in SF california?
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-5-2)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-5-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-5-4)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-5-5) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-5-6)  name: 'get_weather',
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-5-7)  args: { location: 'SF, California' },
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-5-8)  type: 'tool_call',
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-5-9)  id: 'call_AWgaSjqaYVQN73kL0H4BNn1Q'
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-5-10) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-5-11)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-5-12)-----

```


We can verify that our graph stopped at the right place: 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-6-1)conststate=awaitagent.getState(config)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-6-2)console.log(state.next)

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-7-1)[ 'tools' ]

```


Now we can either approve or edit the tool call before proceeding to the next node. If we wanted to approve the tool call, we would simply continue streaming the graph with `null` input. If we wanted to edit the tool call we need to update the state to have the correct tool call, and then after the update has been applied we can continue. 

We can try resuming and we will see an error arise:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-8-1)stream=awaitagent.stream(null,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-8-2)...config,
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-8-3)streamMode:"values",
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-8-4)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-8-5)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-8-6)forawait(
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-8-7)const{messages}ofstream
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-8-8)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-8-9)letmsg=messages[messages?.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-8-10)if(msg?.content){
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-8-11)console.log(msg.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-8-12)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-8-13)if(msg?.tool_calls?.length>0){
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-8-14)console.log(msg.tool_calls);
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-8-15)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-8-16)console.log("-----\n");
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-8-17)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-9-1)Error: Unknown Location
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-9-2) Please fix your mistakes.
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-9-3)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-9-4)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-9-5)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-9-6) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-9-7)  name: 'get_weather',
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-9-8)  args: { location: 'San Francisco, California' },
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-9-9)  type: 'tool_call',
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-9-10)  id: 'call_MfIPKpRDXRL4LcHm1BxwcSTk'
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-9-11) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-9-12)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-9-13)-----

```


This error arose because our tool argument of "SF, California" is not a location our tool recognizes. 

Let's show how we would edit the tool call to search for "San Francisco" instead of "SF, California" - since our tool as written treats "San Francisco, CA" as an unknown location. We will update the state and then resume streaming the graph and should see no errors arise. Note that the reducer we use for our `messages` channel will replace a messaege only if a message with the exact same ID is used. For that reason we can do `new AiMessage(...)` and instead have to directly modify the last message from the `messages` channel, making sure not to edit its ID.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-10-1)// First, lets get the current state
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-10-2)constcurrentState=awaitagent.getState(config);
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-10-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-10-4)// Let's now get the last message in the state
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-10-5)// This is the one with the tool calls that we want to update
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-10-6)letlastMessage=currentState.values.messages[currentState.values.messages.length-1]
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-10-7)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-10-8)// Let's now update the args for that tool call
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-10-9)lastMessage.tool_calls[0].args={location:"San Francisco"}
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-10-10)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-10-11)// Let's now call `updateState` to pass in this message in the `messages` key
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-10-12)// This will get treated as any other update to the state
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-10-13)// It will get passed to the reducer function for the `messages` key
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-10-14)// That reducer function will use the ID of the message to update it
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-10-15)// It's important that it has the right ID! Otherwise it would get appended
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-10-16)// as a new message
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-10-17)awaitagent.updateState(config,{messages:lastMessage});

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-11-1){
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-11-2) configurable: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-11-3)  thread_id: '1',
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-11-4)  checkpoint_ns: '',
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-11-5)  checkpoint_id: '1ef6638d-bfbd-61d0-8004-2751c8c3f226'
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-11-6) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-11-7)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-12-1)stream=awaitagent.stream(null,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-12-2)...config,
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-12-3)streamMode:"values",
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-12-4)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-12-5)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-12-6)forawait(
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-12-7)const{messages}ofstream
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-12-8)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-12-9)letmsg=messages[messages?.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-12-10)if(msg?.content){
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-12-11)console.log(msg.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-12-12)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-12-13)if(msg?.tool_calls?.length>0){
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-12-14)console.log(msg.tool_calls);
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-12-15)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-12-16)console.log("-----\n");
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-12-17)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-13-1)It's always sunny in sf
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-13-2)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-13-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-13-4)The climate in San Francisco is sunny right now. If you need more specific details, feel free to ask!
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__codelineno-13-5)-----

```


Fantastic! Our graph updated properly to query the weather in San Francisco and got the correct "The weather in San Francisco is sunny today! " response from the tool.  Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to add a custom system prompt to the prebuilt ReAct agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/) [ Next  How to create a ReAct agent from scratch (Functional API)  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
