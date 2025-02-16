---
url: https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#how-to-add-memory-to-the-prebuilt-react-agent)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to add memory to the prebuilt ReAct agent 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/?q= "Share")

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
            * How to add memory to the prebuilt ReAct agent  [ How to add memory to the prebuilt ReAct agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#setup)
              * [ Code  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#code)
              * [ Usage  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#usage)
            * [ How to add a custom system prompt to the prebuilt ReAct agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/)
            * [ How to add human-in-the-loop processes to the prebuilt ReAct agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#setup)
  * [ Code  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#code)
  * [ Usage  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#usage)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
  5. [ Prebuilt ReAct Agent  ](https://langchain-ai.github.io/langgraphjs/how-tos#prebuilt-react-agent)



# How to add memory to the prebuilt ReAct agent[¶](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#how-to-add-memory-to-the-prebuilt-react-agent "Permanent link")

This tutorial will show how to add memory to the prebuilt ReAct agent. Please see [this tutorial](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/create-react-agent.ipynb) for how to get started with the prebuilt ReAct agent

All we need to do to enable memory is pass in a checkpointer to `createReactAgent`

## Setup[¶](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#setup "Permanent link")

First, we need to install the required packages.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-0-1)yarnadd@langchain/langgraph@langchain/openai@langchain/core

```


This guide will use OpenAI's GPT-4o model. We will optionally set our API key for [LangSmith tracing](https://smith.langchain.com/), which will give us best-in-class observability.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-1-1)// process.env.OPENAI_API_KEY = "sk_...";
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-1-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-1-3)// Optional, add tracing in LangSmith
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-1-4)// process.env.LANGCHAIN_API_KEY = "ls__..."
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-1-5)// process.env.LANGCHAIN_CALLBACKS_BACKGROUND = "true";
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-1-6)process.env.LANGCHAIN_CALLBACKS_BACKGROUND="true";
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-1-7)process.env.LANGCHAIN_TRACING_V2="true";
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-1-8)process.env.LANGCHAIN_PROJECT="ReAct Agent with memory: LangGraphJS";

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-2-1)ReAct Agent with memory: LangGraphJS

```


## Code[¶](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#code "Permanent link")

Now we can use the prebuilt `createReactAgent` function to setup our agent with memory:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-3-1)import{ChatOpenAI}from"@langchain/openai";
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-3-2)import{tool}from'@langchain/core/tools';
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-3-3)import{z}from'zod';
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-3-4)import{createReactAgent}from"@langchain/langgraph/prebuilt";
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-3-5)import{MemorySaver}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-3-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-3-7)constmodel=newChatOpenAI({
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-3-8)model:"gpt-4o",
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-3-9)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-3-10)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-3-11)constgetWeather=tool((input)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-3-12)if(input.location==='sf'){
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-3-13)return'It\'s always sunny in sf';
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-3-14)}else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-3-15)return'It might be cloudy in nyc';
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-3-16)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-3-17)},{
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-3-18)name:'get_weather',
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-3-19)description:'Call to get the current weather.',
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-3-20)schema:z.object({
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-3-21)location:z.enum(['sf','nyc']).describe("Location to get the weather for."),
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-3-22)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-3-23)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-3-24)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-3-25)// Here we only save in-memory
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-3-26)constmemory=newMemorySaver();
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-3-27)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-3-28)constagent=createReactAgent({llm:model,tools:[getWeather],checkpointSaver:memory});

```


## Usage[¶](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#usage "Permanent link")

Let's interact with it multiple times to show that it can remember prior information

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-4-1)letinputs={messages:[{role:"user",content:"what is the weather in NYC?"}]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-4-2)letconfig={configurable:{thread_id:"1"}};
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-4-3)letstream=awaitagent.stream(inputs,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-4-4)...config,
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-4-5)streamMode:"values",
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-4-6)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-4-7)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-4-8)forawait(
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-4-9)const{messages}ofstream
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-4-10)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-4-11)letmsg=messages[messages?.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-4-12)if(msg?.content){
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-4-13)console.log(msg.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-4-14)}elseif(msg?.tool_calls?.length>0){
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-4-15)console.log(msg.tool_calls);
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-4-16)}else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-4-17)console.log(msg);
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-4-18)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-4-19)console.log("-----\n");
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-4-20)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-5-1)what is the weather in NYC?
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-5-2)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-5-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-5-4)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-5-5) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-5-6)  name: 'get_weather',
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-5-7)  args: { location: 'nyc' },
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-5-8)  type: 'tool_call',
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-5-9)  id: 'call_m0zEI6sidPPH81G6ygMsKYs1'
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-5-10) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-5-11)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-5-12)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-5-13)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-5-14)It might be cloudy in nyc
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-5-15)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-5-16)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-5-17)The weather in NYC appears to be cloudy.
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-5-18)-----

```


Notice that when we pass the same the same thread ID, the chat history is preserved 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-6-1)inputs={messages:[{role:"user",content:"What's it known for?"}]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-6-2)stream=awaitagent.stream(inputs,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-6-3)...config,
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-6-4)streamMode:"values",
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-6-5)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-6-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-6-7)forawait(
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-6-8)const{messages}ofstream
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-6-9)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-6-10)letmsg=messages[messages?.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-6-11)if(msg?.content){
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-6-12)console.log(msg.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-6-13)}elseif(msg?.tool_calls?.length>0){
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-6-14)console.log(msg.tool_calls);
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-6-15)}else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-6-16)console.log(msg);
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-6-17)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-6-18)console.log("-----\n");
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-6-19)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-7-1)What's it known for?
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-7-2)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-7-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-7-4)New York City (NYC) is known for many things, including:
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-7-5)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-7-6)1. **Landmarks and Attractions:**
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-7-7)  - **Statue of Liberty**: An iconic symbol of freedom.
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-7-8)  - **Empire State Building**: A famous skyscraper offering panoramic views.
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-7-9)  - **Times Square**: Known for its neon lights and bustling atmosphere.
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-7-10)  - **Central Park**: A large, urban park offering a natural oasis.
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-7-11)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-7-12)2. **Cultural Institutions:**
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-7-13)  - **Broadway**: Famous for its theatre productions.
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-7-14)  - **Metropolitan Museum of Art (The Met)**: One of the largest and most prestigious art museums.
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-7-15)  - **Museum of Modern Art (MoMA) and American Museum of Natural History**: Other significant museums.
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-7-16)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-7-17)3. **Economy and Business:**
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-7-18)  - **Wall Street**: The financial hub of the world, home to the New York Stock Exchange.
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-7-19)  - **Headquarters of major corporations**: NYC hosts the headquarters of many large multinational companies.
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-7-20)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-7-21)4. **Diversity and Neighborhoods:**
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-7-22)  - **Cultural Melting Pot**: NYC is known for its diverse population with a wide range of ethnicities and cultures.
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-7-23)  - **Distinct Neighborhoods**: Each borough and neighborhood (like Brooklyn, The Bronx, Queens, Staten Island, and Manhattan) has its unique character.
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-7-24)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-7-25)5. **Food and Cuisine:**
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-7-26)  - **Culinary Capital**: Known for diverse food options from street food like hot dogs and pretzels to high-end dining.
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-7-27)  - **Cultural Cuisine**: Offers a variety of world cuisines due to its diverse population.
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-7-28)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-7-29)6. **Media and Entertainment:**
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-7-30)  - **Media Headquarters**: Home to major media companies and news networks.
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-7-31)  - **Film and Television**: A popular setting and production location for films and TV shows.
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-7-32)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-7-33)7. **Events and Festivities:**
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-7-34)  - **Macy's Thanksgiving Day Parade**: A famous annual parade.
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-7-35)  - **New Year's Eve in Times Square**: Known for the ball drop and celebrations.
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-7-36)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-7-37)NYC is a dynamic and vibrant city with a rich history and an influence that extends globally in various sectors.
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-7-38)-----

```


When we pass it a new thread ID, all the history is lost and their is no memory to speak of: 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-8-1)inputs={messages:[{role:"user",content:"how close is it to boston?"}]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-8-2)config={configurable:{thread_id:"2"}};
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-8-3)stream=awaitagent.stream(inputs,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-8-4)...config,
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-8-5)streamMode:"values",
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-8-6)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-8-7)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-8-8)forawait(
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-8-9)const{messages}ofstream
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-8-10)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-8-11)letmsg=messages[messages?.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-8-12)if(msg?.content){
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-8-13)console.log(msg.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-8-14)}elseif(msg?.tool_calls?.length>0){
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-8-15)console.log(msg.tool_calls);
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-8-16)}else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-8-17)console.log(msg);
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-8-18)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-8-19)console.log("-----\n");
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-8-20)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-9-1)how close is it to boston?
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-9-2)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-9-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-9-4)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-9-5) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-9-6)  name: 'get_weather',
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-9-7)  args: { location: 'nyc' },
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-9-8)  type: 'tool_call',
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-9-9)  id: 'call_CKgDJqHiadzNLGhB8T8pHQWM'
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-9-10) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-9-11)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-9-12)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-9-13)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-9-14)It might be cloudy in nyc
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-9-15)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-9-16)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-9-17)To determine how close "it" is to Boston, could you please specify which location you're referring to? For instance, are you asking about the distance from New York City, San Francisco, or another location? This detail will help me provide an accurate answer.
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__codelineno-9-18)-----

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to use the prebuilt ReAct agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/) [ Next  How to add a custom system prompt to the prebuilt ReAct agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
