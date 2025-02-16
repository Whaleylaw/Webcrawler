---
url: https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#how-to-stream-llm-tokens-without-langchain-models)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to stream LLM tokens (without LangChain models) 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/?q= "Share")

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
            * How to stream LLM tokens (without LangChain models)  [ How to stream LLM tokens (without LangChain models)  ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#setup)
              * [ Defining a model and a tool schema  ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#defining-a-model-and-a-tool-schema)
              * [ Calling the model  ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#calling-the-model)
              * [ Define tools and a tool-calling node  ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#define-tools-and-a-tool-calling-node)
              * [ Build the graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#build-the-graph)
              * [ Streaming tokens  ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#streaming-tokens)
            * [ How to stream custom data  ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/)
            * [ How to configure multiple streaming modes at the same time  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#setup)
  * [ Defining a model and a tool schema  ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#defining-a-model-and-a-tool-schema)
  * [ Calling the model  ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#calling-the-model)
  * [ Define tools and a tool-calling node  ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#define-tools-and-a-tool-calling-node)
  * [ Build the graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#build-the-graph)
  * [ Streaming tokens  ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#streaming-tokens)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
  5. [ Streaming  ](https://langchain-ai.github.io/langgraphjs/how-tos#streaming)



# How to stream LLM tokens (without LangChain models)[¶](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#how-to-stream-llm-tokens-without-langchain-models "Permanent link")

In this guide, we will stream tokens from the language model powering an agent without using LangChain chat models. We'll be using the OpenAI client library directly in a ReAct agent as an example.

## Setup[¶](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#setup "Permanent link")

To get started, install the `openai` and `langgraph` packages separately:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-0-1)$npminstallopenai@langchain/langgraph@langchain/core

```


Compatibility

This guide requires `@langchain/core>=0.2.19`, and if you are using LangSmith, `langsmith>=0.1.39`. For help upgrading, see [this guide](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/). 

You'll also need to make sure you have your OpenAI key set as `process.env.OPENAI_API_KEY`.

## Defining a model and a tool schema[¶](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#defining-a-model-and-a-tool-schema "Permanent link")

First, initialize the OpenAI SDK and define a tool schema for the model to populate using [OpenAI's format](https://platform.openai.com/docs/api-reference/chat/create#chat-create-tools):

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-1-1)importOpenAIfrom"openai";
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-1-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-1-3)constopenaiClient=newOpenAI({});
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-1-5)consttoolSchema:OpenAI.ChatCompletionTool={
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-1-6)type:"function",
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-1-7)function:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-1-8)name:"get_items",
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-1-9)description:"Use this tool to look up which items are in the given place.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-1-10)parameters:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-1-11)type:"object",
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-1-12)properties:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-1-13)place:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-1-14)type:"string",
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-1-15)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-1-16)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-1-17)required:["place"],
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-1-18)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-1-19)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-1-20)};

```


## Calling the model[¶](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#calling-the-model "Permanent link")

Now, define a method for a LangGraph node that will call the model. It will handle formatting tool calls to and from the model, as well as streaming via [custom callback events](https://js.langchain.com/docs/how_to/callbacks_custom_events).

If you are using [LangSmith](https://docs.smith.langchain.com/), you can also wrap the OpenAI client for the same nice tracing you'd get with a LangChain chat model.

Here's what that looks like:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-1)import{dispatchCustomEvent}from"@langchain/core/callbacks/dispatch";
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-2)import{wrapOpenAI}from"langsmith/wrappers/openai";
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-3)import{Annotation}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-4)
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-5)constStateAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-6)messages:Annotation<OpenAI.ChatCompletionMessageParam[]>({
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-7)reducer:(x,y)=>x.concat(y),
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-8)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-9)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-10)
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-11)// If using LangSmith, use "wrapOpenAI" on the whole client or
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-12)// "traceable" to wrap a single method for nicer tracing:
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-13)// https://docs.smith.langchain.com/how_to_guides/tracing/annotate_code
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-14)constwrappedClient=wrapOpenAI(openaiClient);
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-15)
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-16)constcallModel=async(state:typeofStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-17)const{messages}=state;
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-18)conststream=awaitwrappedClient.chat.completions.create({
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-19)messages,
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-20)model:"gpt-4o-mini",
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-21)tools:[toolSchema],
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-22)stream:true,
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-23)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-24)letresponseContent="";
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-25)letrole:string="assistant";
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-26)lettoolCallId:string|undefined;
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-27)lettoolCallName:string|undefined;
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-28)lettoolCallArgs="";
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-29)forawait(constchunkofstream){
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-30)constdelta=chunk.choices[0].delta;
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-31)if(delta.role!==undefined){
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-32)role=delta.role;
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-33)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-34)if(delta.content){
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-35)responseContent+=delta.content;
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-36)awaitdispatchCustomEvent("streamed_token",{
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-37)content:delta.content,
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-38)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-39)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-40)if(delta.tool_calls!==undefined&&delta.tool_calls.length>0){
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-41)// note: for simplicity we're only handling a single tool call here
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-42)consttoolCall=delta.tool_calls[0];
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-43)if(toolCall.function?.name!==undefined){
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-44)toolCallName=toolCall.function.name;
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-45)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-46)if(toolCall.id!==undefined){
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-47)toolCallId=toolCall.id;
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-48)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-49)awaitdispatchCustomEvent("streamed_tool_call_chunk",toolCall);
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-50)toolCallArgs+=toolCall.function?.arguments??"";
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-51)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-52)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-53)letfinalToolCalls;
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-54)if(toolCallName!==undefined&&toolCallId!==undefined){
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-55)finalToolCalls=[{
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-56)id:toolCallId,
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-57)function:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-58)name:toolCallName,
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-59)arguments:toolCallArgs
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-60)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-61)type:"function"asconst,
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-62)}];
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-63)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-64)
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-65)constresponseMessage={
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-66)role:roleasany,
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-67)content:responseContent,
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-68)tool_calls:finalToolCalls,
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-69)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-70)return{messages:[responseMessage]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-2-71)}

```


Note that you can't call this method outside of a LangGraph node since `dispatchCustomEvent` will fail if it is called outside the proper context.

## Define tools and a tool-calling node[¶](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#define-tools-and-a-tool-calling-node "Permanent link")

Next, set up the actual tool function and the node that will call it when the model populates a tool call:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-3-1)constgetItems=async({place}:{place:string})=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-3-2)if(place.toLowerCase().includes("bed")){// For under the bed
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-3-3)return"socks, shoes and dust bunnies";
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-3-4)}elseif(place.toLowerCase().includes("shelf")){// For 'shelf'
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-3-5)return"books, pencils and pictures";
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-3-6)}else{// if the agent decides to ask about a different place
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-3-7)return"cat snacks";
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-3-8)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-3-9)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-3-10)
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-3-11)constcallTools=async(state:typeofStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-3-12)const{messages}=state;
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-3-13)constmostRecentMessage=messages[messages.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-3-14)consttoolCalls=(mostRecentMessageasOpenAI.ChatCompletionAssistantMessageParam).tool_calls;
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-3-15)if(toolCalls===undefined||toolCalls.length===0){
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-3-16)thrownewError("No tool calls passed to node.");
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-3-17)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-3-18)consttoolNameMap={
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-3-19)get_items:getItems,
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-3-20)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-3-21)constfunctionName=toolCalls[0].function.name;
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-3-22)constfunctionArguments=JSON.parse(toolCalls[0].function.arguments);
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-3-23)constresponse=awaittoolNameMap[functionName](functionArguments);
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-3-24)consttoolMessage={
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-3-25)tool_call_id:toolCalls[0].id,
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-3-26)role:"tool"asconst,
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-3-27)name:functionName,
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-3-28)content:response,
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-3-29)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-3-30)return{messages:[toolMessage]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-3-31)}

```


## Build the graph[¶](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#build-the-graph "Permanent link")

Finally, it's time to build your graph:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-4-1)import{StateGraph}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-4-2)importOpenAIfrom"openai";
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-4-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-4-4)// We can reuse the same `GraphState` from above as it has not changed.
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-4-5)constshouldContinue=(state:typeofStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-4-6)const{messages}=state;
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-4-7)constlastMessage=
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-4-8)messages[messages.length-1]asOpenAI.ChatCompletionAssistantMessageParam;
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-4-9)if(lastMessage?.tool_calls!==undefined&&lastMessage?.tool_calls.length>0){
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-4-10)return"tools";
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-4-11)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-4-12)return"__end__";
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-4-13)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-4-14)
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-4-15)constgraph=newStateGraph(StateAnnotation)
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-4-16).addNode("model",callModel)
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-4-17).addNode("tools",callTools)
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-4-18).addEdge("__start__","model")
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-4-19).addConditionalEdges("model",shouldContinue,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-4-20)tools:"tools",
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-4-21)__end__:"__end__",
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-4-22)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-4-23).addEdge("tools","model")
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-4-24).compile();

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-5-1)import*astslabfrom"tslab";
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-5-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-5-3)constrepresentation=graph.getGraph();
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-5-4)constimage=awaitrepresentation.drawMermaidPng();
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-5-5)constarrayBuffer=awaitimage.arrayBuffer();
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-5-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-5-7)awaittslab.display.png(newUint8Array(arrayBuffer));

```


![]()

## Streaming tokens[¶](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#streaming-tokens "Permanent link")

And now we can use the `.streamEvents`[](https://js.langchain.com/docs/how_to/streaming#using-stream-events) method to get the streamed tokens and tool calls from the OpenAI model:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-6-1)consteventStream=awaitgraph.streamEvents(
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-6-2){messages:[{role:"user",content:"what's in the bedroom?"}]},
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-6-3){version:"v2"},
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-6-4));
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-6-5)
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-6-6)forawait(const{event,name,data}ofeventStream){
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-6-7)if(event==="on_custom_event"){
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-6-8)console.log(name,data);
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-6-9)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-6-10)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-7-1)streamed_tool_call_chunk {
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-7-2) index: 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-7-3) id: 'call_v99reml4gZvvUypPgOpLgxM2',
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-7-4) type: 'function',
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-7-5) function: { name: 'get_items', arguments: '' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-7-6)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-7-7)streamed_tool_call_chunk { index: 0, function: { arguments: '{"' } }
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-7-8)streamed_tool_call_chunk { index: 0, function: { arguments: 'place' } }
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-7-9)streamed_tool_call_chunk { index: 0, function: { arguments: '":"' } }
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-7-10)streamed_tool_call_chunk { index: 0, function: { arguments: 'bed' } }
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-7-11)streamed_tool_call_chunk { index: 0, function: { arguments: 'room' } }
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-7-12)streamed_tool_call_chunk { index: 0, function: { arguments: '"}' } }
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-7-13)streamed_token { content: 'In' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-7-14)streamed_token { content: ' the' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-7-15)streamed_token { content: ' bedroom' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-7-16)streamed_token { content: ',' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-7-17)streamed_token { content: ' you' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-7-18)streamed_token { content: ' can' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-7-19)streamed_token { content: ' find' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-7-20)streamed_token { content: ' socks' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-7-21)streamed_token { content: ',' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-7-22)streamed_token { content: ' shoes' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-7-23)streamed_token { content: ',' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-7-24)streamed_token { content: ' and' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-7-25)streamed_token { content: ' dust' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-7-26)streamed_token { content: ' b' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-7-27)streamed_token { content: 'unnies' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__codelineno-7-28)streamed_token { content: '.' }

```


And if you've set up LangSmith tracing, you'll also see [a trace like this one](https://smith.langchain.com/public/ddb1af36-ebe5-4ba6-9a57-87a296dc801f/r).  Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to stream LLM tokens from your graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/) [ Next  How to stream custom data  ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
