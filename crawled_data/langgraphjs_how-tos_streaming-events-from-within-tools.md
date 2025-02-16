---
url: https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#how-to-stream-events-from-within-a-tool)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to stream events from within a tool 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/?q= "Share")

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
            * [ How to configure multiple streaming modes at the same time  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/)
            * How to stream events from within a tool  [ How to stream events from within a tool  ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#setup)
              * [ Define graph and tools  ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#define-graph-and-tools)
              * [ Stream events from the graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#stream-events-from-the-graph)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#setup)
  * [ Define graph and tools  ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#define-graph-and-tools)
  * [ Stream events from the graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#stream-events-from-the-graph)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
  5. [ Streaming  ](https://langchain-ai.github.io/langgraphjs/how-tos#streaming)



# How to stream events from within a tool[¶](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#how-to-stream-events-from-within-a-tool "Permanent link")

If your LangGraph graph needs to use tools that call LLMs (or any other LangChain `Runnable` objects -- other graphs, LCEL chains, retrievers, etc.), you might want to stream events from the underlying `Runnable`. This guide shows how you can do that.

## Setup[¶](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#setup "Permanent link")

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-0-1)npminstall@langchain/langgraph@langchain/anthropic@langchain/corezod

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-1-1)process.env.ANTHROPIC_API_KEY='YOUR_API_KEY'

```


## Define graph and tools[¶](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#define-graph-and-tools "Permanent link")

We'll use a prebuilt ReAct agent for this guide

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-2-1)import{z}from"zod";
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-2-2)import{tool}from"@langchain/core/tools";
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-2-3)import{ChatPromptTemplate}from"@langchain/core/prompts";
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-2-4)import{ChatAnthropic}from"@langchain/anthropic";
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-2-5)
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-2-6)constmodel=newChatAnthropic({
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-2-7)model:"claude-3-5-sonnet-20240620",
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-2-8)temperature:0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-2-9)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-2-10)
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-2-11)constgetItems=tool(
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-2-12)async(input,config)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-2-13)consttemplate=ChatPromptTemplate.fromMessages([
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-2-14)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-2-15)"human",
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-2-16)"Can you tell me what kind of items i might find in the following place: '{place}'. "+
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-2-17)"List at least 3 such items separating them by a comma. And include a brief description of each item..",
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-2-18)],
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-2-19)]);
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-2-20)
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-2-21)constmodelWithConfig=model.withConfig({
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-2-22)runName:"Get Items LLM",
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-2-23)tags:["tool_llm"],
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-2-24)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-2-25)
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-2-26)constchain=template.pipe(modelWithConfig);
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-2-27)constresult=awaitchain.invoke(input,config);
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-2-28)returnresult.content;
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-2-29)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-2-30){
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-2-31)name:"get_items",
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-2-32)description:"Use this tool to look up which items are in the given place.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-2-33)schema:z.object({
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-2-34)place:z.string().describe("The place to look up items for. E.g 'shelf'"),
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-2-35)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-2-36)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-2-37));

```


We're adding a custom tag (`tool_llm`) to our LLM runnable within the tool. This will allow us to filter events that we'll stream from the compiled graph (`agent`) Runnable below

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-3-1)import{createReactAgent}from"@langchain/langgraph/prebuilt";
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-3-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-3-3)constagent=createReactAgent({
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-3-4)llm:model,
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-3-5)tools:[getItems],
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-3-6)});

```


## Stream events from the graph[¶](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#stream-events-from-the-graph "Permanent link")

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-4-1)letfinalEvent;
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-4-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-4-3)forawait(consteventofagent.streamEvents(
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-4-4){
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-4-5)messages:[
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-4-6)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-4-7)"human",
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-4-8)"what items are on the shelf? You should call the get_items tool.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-4-9)],
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-4-10)],
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-4-11)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-4-12){
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-4-13)version:"v2",
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-4-14)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-4-15){
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-4-16)includeTags:["tool_llm"],
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-4-17)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-4-18))){
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-4-19)if("chunk"inevent.data){
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-4-20)console.dir({
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-4-21)type:event.data.chunk._getType(),
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-4-22)content:event.data.chunk.content,
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-4-23)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-4-24)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-4-25)finalEvent=event;
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-4-26)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-5-1){ type: 'ai', content: 'Here' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-5-2){ type: 'ai', content: ' are three items you might' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-5-3){ type: 'ai', content: ' find on a shelf,' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-5-4){ type: 'ai', content: ' along with brief' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-5-5){ type: 'ai', content: ' descriptions:\n\n1.' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-5-6){ type: 'ai', content: ' Books' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-5-7){ type: 'ai', content: ': Boun' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-5-8){ type: 'ai', content: 'd collections of printe' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-5-9){ type: 'ai', content: 'd pages' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-5-10){ type: 'ai', content: ' containing' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-5-11){ type: 'ai', content: ' various' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-5-12){ type: 'ai', content: ' forms' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-5-13){ type: 'ai', content: ' of literature, information' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-5-14){ type: 'ai', content: ', or reference' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-5-15){ type: 'ai', content: ' material.\n\n2.' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-5-16){ type: 'ai', content: ' Picture' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-5-17){ type: 'ai', content: ' frames: Decorative' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-5-18){ type: 'ai', content: ' borders' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-5-19){ type: 'ai', content: ' used to display an' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-5-20){ type: 'ai', content: 'd protect photographs, artwork' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-5-21){ type: 'ai', content: ', or other visual memor' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-5-22){ type: 'ai', content: 'abilia.\n\n3' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-5-23){ type: 'ai', content: '. Pot' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-5-24){ type: 'ai', content: 'ted plants: Small' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-5-25){ type: 'ai', content: ' indoor' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-5-26){ type: 'ai', content: ' plants in' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-5-27){ type: 'ai', content: ' containers, often used for' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-5-28){ type: 'ai', content: ' decoration or to add a' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-5-29){ type: 'ai', content: ' touch of nature to indoor' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-5-30){ type: 'ai', content: ' spaces.' }

```


Let's inspect the last event to get the final list of messages from the agent 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-6-1)constfinalMessage=finalEvent?.data.output;
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-6-2)console.dir(
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-6-3){
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-6-4)type:finalMessage._getType(),
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-6-5)content:finalMessage.content,
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-6-6)tool_calls:finalMessage.tool_calls,
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-6-7)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-6-8){depth:null}
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-6-9));

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-7-1){
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-7-2) type: 'ai',
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-7-3) content: 'Here are three items you might find on a shelf, along with brief descriptions:\n' +
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-7-4)  '\n' +
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-7-5)  '1. Books: Bound collections of printed pages containing various forms of literature, information, or reference material.\n' +
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-7-6)  '\n' +
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-7-7)  '2. Picture frames: Decorative borders used to display and protect photographs, artwork, or other visual memorabilia.\n' +
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-7-8)  '\n' +
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-7-9)  '3. Potted plants: Small indoor plants in containers, often used for decoration or to add a touch of nature to indoor spaces.',
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-7-10) tool_calls: []
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__codelineno-7-11)}

```


You can see that the content of the `ToolMessage` is the same as the output we streamed above  Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to configure multiple streaming modes at the same time  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/) [ Next  How to stream from the final node  ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-from-final-node/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
