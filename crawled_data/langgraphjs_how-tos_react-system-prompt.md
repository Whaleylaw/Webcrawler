---
url: https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#how-to-add-a-custom-system-prompt-to-the-prebuilt-react-agent)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to add a custom system prompt to the prebuilt ReAct agent 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/?q= "Share")

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
            * How to add a custom system prompt to the prebuilt ReAct agent  [ How to add a custom system prompt to the prebuilt ReAct agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#setup)
              * [ Code  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#code)
              * [ Usage  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#usage)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#setup)
  * [ Code  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#code)
  * [ Usage  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#usage)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
  5. [ Prebuilt ReAct Agent  ](https://langchain-ai.github.io/langgraphjs/how-tos#prebuilt-react-agent)



# How to add a custom system prompt to the prebuilt ReAct agent[¶](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#how-to-add-a-custom-system-prompt-to-the-prebuilt-react-agent "Permanent link")

This tutorial will show how to add a custom system prompt to the prebuilt ReAct agent. Please see [this tutorial](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/create-react-agent.ipynb) for how to get started with the prebuilt ReAct agent

You can add a custom system prompt by passing a string to the `stateModifier` param.

Compatibility

The `stateModifier`[](https://langchain-ai.github.io/langgraphjs/reference/types/langgraph_prebuilt.CreateReactAgentParams.html) parameter was added in `@langchain/langgraph>=0.2.27`. If you are on an older version, you will need to use the deprecated `messageModifier` parameter. For help upgrading, see [this guide](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/). 

## Setup[¶](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#setup "Permanent link")

First, we need to install the required packages.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-0-1)yarnadd@langchain/langgraph@langchain/openai@langchain/core

```


This guide will use OpenAI's GPT-4o model. We will optionally set our API key for [LangSmith tracing](https://smith.langchain.com/), which will give us best-in-class observability.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-1-1)// process.env.OPENAI_API_KEY = "sk_...";
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-1-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-1-3)// Optional, add tracing in LangSmith
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-1-4)// process.env.LANGCHAIN_API_KEY = "ls__..."
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-1-5)// process.env.LANGCHAIN_CALLBACKS_BACKGROUND = "true";
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-1-6)process.env.LANGCHAIN_CALLBACKS_BACKGROUND="true";
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-1-7)process.env.LANGCHAIN_TRACING_V2="true";
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-1-8)process.env.LANGCHAIN_PROJECT="ReAct Agent with system prompt: LangGraphJS";

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-2-1)ReAct Agent with system prompt: LangGraphJS

```


## Code[¶](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#code "Permanent link")

Now we can use the prebuilt `createReactAgent` function to setup our agent with a system prompt:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-3-1)import{ChatOpenAI}from"@langchain/openai";
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-3-2)import{tool}from'@langchain/core/tools';
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-3-3)import{z}from'zod';
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-3-4)import{createReactAgent}from"@langchain/langgraph/prebuilt";
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-3-5)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-3-6)constmodel=newChatOpenAI({
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-3-7)model:"gpt-4o",
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-3-8)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-3-9)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-3-10)constgetWeather=tool((input)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-3-11)if(input.location==='sf'){
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-3-12)return'It\'s always sunny in sf';
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-3-13)}else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-3-14)return'It might be cloudy in nyc';
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-3-15)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-3-16)},{
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-3-17)name:'get_weather',
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-3-18)description:'Call to get the current weather.',
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-3-19)schema:z.object({
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-3-20)location:z.enum(['sf','nyc']).describe("Location to get the weather for."),
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-3-21)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-3-22)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-3-23)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-3-24)// We can add our system prompt here
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-3-25)constprompt="Respond in Italian"
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-3-26)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-3-27)constagent=createReactAgent({llm:model,tools:[getWeather],stateModifier:prompt});

```


## Usage[¶](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#usage "Permanent link")

Let's verify that the agent does indeed respond in Italian!

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-4-1)letinputs={messages:[{role:"user",content:"what is the weather in NYC?"}]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-4-2)letstream=awaitagent.stream(inputs,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-4-3)streamMode:"values",
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-4-4)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-4-5)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-4-6)forawait(
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-4-7)const{messages}ofstream
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-4-8)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-4-9)letmsg=messages[messages?.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-4-10)if(msg?.content){
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-4-11)console.log(msg.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-4-12)}elseif(msg?.tool_calls?.length>0){
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-4-13)console.log(msg.tool_calls);
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-4-14)}else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-4-15)console.log(msg);
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-4-16)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-4-17)console.log("-----\n");
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-4-18)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-5-1)what is the weather in NYC?
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-5-2)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-5-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-5-4)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-5-5) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-5-6)  name: 'get_weather',
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-5-7)  args: { location: 'nyc' },
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-5-8)  type: 'tool_call',
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-5-9)  id: 'call_PqmKDQrefHQLmGsZSSr4C7Fc'
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-5-10) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-5-11)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-5-12)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-5-13)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-5-14)It might be cloudy in nyc
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-5-15)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-5-16)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-5-17)A New York potrebbe essere nuvoloso. Hai altre domande o posso aiutarti in qualcos'altro?
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__codelineno-5-18)-----

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to add memory to the prebuilt ReAct agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/) [ Next  How to add human-in-the-loop processes to the prebuilt ReAct agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
