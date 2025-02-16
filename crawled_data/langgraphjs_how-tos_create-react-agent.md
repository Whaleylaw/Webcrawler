---
url: https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#how-to-use-the-prebuilt-react-agent)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to use the prebuilt ReAct agent 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/?q= "Share")

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
            * How to use the prebuilt ReAct agent  [ How to use the prebuilt ReAct agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#setup)
              * [ Code  ](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#code)
              * [ Usage  ](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#usage)
            * [ How to add memory to the prebuilt ReAct agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#setup)
  * [ Code  ](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#code)
  * [ Usage  ](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#usage)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
  5. [ Prebuilt ReAct Agent  ](https://langchain-ai.github.io/langgraphjs/how-tos#prebuilt-react-agent)



# How to use the prebuilt ReAct agent[¶](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#how-to-use-the-prebuilt-react-agent "Permanent link")

In this how-to we'll create a simple [ReAct](https://arxiv.org/abs/2210.03629) agent app that can check the weather. The app consists of an agent (LLM) and tools. As we interact with the app, we will first call the agent (LLM) to decide if we should use tools. Then we will run a loop: 

  1. If the agent said to take an action (i.e. call tool), we'll run the tools and pass the results back to the agent
  2. If the agent did not ask to run tools, we will finish (respond to the user)



Prebuilt Agent

Please note that here will we use a prebuilt agent. One of the big benefits of LangGraph is that you can easily create your own agent architectures. So while it's fine to start here to build an agent quickly, we would strongly recommend learning how to build your own agent so that you can take full advantage of LangGraph. Read [ this guide ](https://langchain-ai.github.io/langgraphjs/tutorials/quickstart/#quickstart) to learn how to create your own ReAct agent from scratch. 

## Setup[¶](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#setup "Permanent link")

First, we need to install the required packages.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-0-1)yarnadd@langchain/langgraph@langchain/openai@langchain/core

```


This guide will use OpenAI's GPT-4o model. We will optionally set our API key for [LangSmith tracing](https://smith.langchain.com/), which will give us best-in-class observability.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-1-1)// process.env.OPENAI_API_KEY = "sk_...";
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-1-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-1-3)// Optional, add tracing in LangSmith
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-1-4)// process.env.LANGCHAIN_API_KEY = "ls__..."
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-1-5)// process.env.LANGCHAIN_CALLBACKS_BACKGROUND = "true";
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-1-6)process.env.LANGCHAIN_CALLBACKS_BACKGROUND="true";
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-1-7)process.env.LANGCHAIN_TRACING_V2="true";
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-1-8)process.env.LANGCHAIN_PROJECT="ReAct Agent: LangGraphJS";

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-2-1)ReAct Agent: LangGraphJS

```


## Code[¶](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#code "Permanent link")

Now we can use the prebuilt `createReactAgent` function to setup our agent:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-3-1)import{ChatOpenAI}from"@langchain/openai";
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-3-2)import{tool}from'@langchain/core/tools';
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-3-3)import{z}from'zod';
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-3-4)import{createReactAgent}from"@langchain/langgraph/prebuilt";
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-3-5)
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-3-6)constmodel=newChatOpenAI({
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-3-7)model:"gpt-4o",
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-3-8)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-3-9)
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-3-10)constgetWeather=tool((input)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-3-11)if(['sf','san francisco','san francisco, ca'].includes(input.location.toLowerCase())){
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-3-12)return'It\'s 60 degrees and foggy.';
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-3-13)}else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-3-14)return'It\'s 90 degrees and sunny.';
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-3-15)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-3-16)},{
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-3-17)name:'get_weather',
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-3-18)description:'Call to get the current weather.',
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-3-19)schema:z.object({
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-3-20)location:z.string().describe("Location to get the weather for."),
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-3-21)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-3-22)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-3-23)
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-3-24)constagent=createReactAgent({llm:model,tools:[getWeather]});

```


## Usage[¶](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#usage "Permanent link")

First, let's visualize the graph we just created

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-4-1)import*astslabfrom"tslab";
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-4-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-4-3)constgraph=agent.getGraph();
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-4-4)constimage=awaitgraph.drawMermaidPng();
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-4-5)constarrayBuffer=awaitimage.arrayBuffer();
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-4-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-4-7)awaittslab.display.png(newUint8Array(arrayBuffer));

```


![]()

Let's run the app with an input that needs a tool call

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-5-1)letinputs={messages:[{role:"user",content:"what is the weather in SF?"}]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-5-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-5-3)letstream=awaitagent.stream(inputs,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-5-4)streamMode:"values",
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-5-5)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-5-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-5-7)forawait(const{messages}ofstream){
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-5-8)letmsg=messages[messages?.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-5-9)if(msg?.content){
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-5-10)console.log(msg.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-5-11)}elseif(msg?.tool_calls?.length>0){
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-5-12)console.log(msg.tool_calls);
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-5-13)}else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-5-14)console.log(msg);
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-5-15)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-5-16)console.log("-----\n");
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-5-17)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-6-1)what is the weather in sf?
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-6-2)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-6-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-6-4)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-6-5) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-6-6)  name: 'get_weather',
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-6-7)  args: { location: 'San Francisco, CA' },
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-6-8)  type: 'tool_call',
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-6-9)  id: 'call_wfXCh5IhSp1C0Db3gaJWDbRP'
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-6-10) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-6-11)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-6-12)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-6-13)
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-6-14)It's 60 degrees and foggy.
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-6-15)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-6-16)
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-6-17)The weather in San Francisco is currently 60 degrees and foggy.
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-6-18)-----

```


Now let's try a question that doesn't need tools 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-7-1)inputs={messages:[{role:"user",content:"who built you?"}]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-7-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-7-3)stream=awaitagent.stream(inputs,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-7-4)streamMode:"values",
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-7-5)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-7-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-7-7)forawait(
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-7-8)const{messages}ofstream
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-7-9)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-7-10)letmsg=messages[messages?.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-7-11)if(msg?.content){
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-7-12)console.log(msg.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-7-13)}elseif(msg?.tool_calls?.length>0){
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-7-14)console.log(msg.tool_calls);
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-7-15)}else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-7-16)console.log(msg);
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-7-17)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-7-18)console.log("-----\n");
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-7-19)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-8-1)who built you?
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-8-2)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-8-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-8-4)I was developed by OpenAI, an AI research and deployment company.
[](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__codelineno-8-5)-----

```


Perfect! The agent correctly didn't call any tools and instead directly responded to the user.  Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to manage agent steps  ](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/) [ Next  How to add memory to the prebuilt ReAct agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
