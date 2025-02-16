---
url: https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#how-to-call-tools-using-toolnode)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to call tools using ToolNode 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/?q= "Share")

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
          * Tool calling  Tool calling 
            * [ Tool calling  ](https://langchain-ai.github.io/langgraphjs/how-tos#tool-calling)
            * How to call tools using ToolNode  [ How to call tools using ToolNode  ](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#setup)
              * [ Define tools  ](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#define-tools)
              * [ Manually call ToolNode  ](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#manually-call-toolnode)
              * [ Using with chat models  ](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#using-with-chat-models)
              * [ ReAct Agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#react-agent)
            * [ How to force an agent to call a tool  ](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/)
            * [ How to handle tool calling errors  ](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/)
            * [ How to pass runtime values to tools  ](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/)
            * [ How to update graph state from tools  ](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#setup)
  * [ Define tools  ](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#define-tools)
  * [ Manually call ToolNode  ](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#manually-call-toolnode)
  * [ Using with chat models  ](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#using-with-chat-models)
  * [ ReAct Agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#react-agent)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
  5. [ Tool calling  ](https://langchain-ai.github.io/langgraphjs/how-tos#tool-calling)



# How to call tools using ToolNode[¶](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#how-to-call-tools-using-toolnode "Permanent link")

This guide covers how to use LangGraph's prebuilt `ToolNode`[](https://langchain-ai.github.io/langgraphjs/reference/classes/langgraph_prebuilt.ToolNode.html) for tool calling.

`ToolNode` is a LangChain Runnable that takes graph state (with a list of messages) as input and outputs state update with the result of tool calls. It is designed to work well out-of-box with LangGraph's prebuilt ReAct agent, but can also work with any `StateGraph` as long as its state has a `messages` key with an appropriate reducer (see `MessagesAnnotation`[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#messagesannotation)).

## Setup[¶](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#setup "Permanent link")

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-0-1)npminstall@langchain/langgraph@langchain/anthropic@langchain/corezod

```


Set env vars:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-1-1)process.env.ANTHROPIC_API_KEY='your-anthropic-api-key';

```


## Define tools[¶](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#define-tools "Permanent link")

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-2-1)import{tool}from'@langchain/core/tools';
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-2-2)import{z}from'zod';
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-2-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-2-4)constgetWeather=tool((input)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-2-5)if(['sf','san francisco'].includes(input.location.toLowerCase())){
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-2-6)return'It\'s 60 degrees and foggy.';
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-2-7)}else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-2-8)return'It\'s 90 degrees and sunny.';
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-2-9)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-2-10)},{
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-2-11)name:'get_weather',
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-2-12)description:'Call to get the current weather.',
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-2-13)schema:z.object({
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-2-14)location:z.string().describe("Location to get the weather for."),
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-2-15)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-2-16)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-2-17)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-2-18)constgetCoolestCities=tool(()=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-2-19)return'nyc, sf';
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-2-20)},{
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-2-21)name:'get_coolest_cities',
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-2-22)description:'Get a list of coolest cities',
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-2-23)schema:z.object({
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-2-24)noOp:z.string().optional().describe("No-op parameter."),
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-2-25)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-2-26)})

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-3-1)import{ToolNode}from'@langchain/langgraph/prebuilt';
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-3-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-3-3)consttools=[getWeather,getCoolestCities]
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-3-4)consttoolNode=newToolNode(tools)

```


## Manually call `ToolNode`[¶](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#manually-call-toolnode "Permanent link")

`ToolNode` operates on graph state with a list of messages. It expects the last message in the list to be an `AIMessage` with `tool_calls` parameter. 

Let's first see how to invoke the tool node manually:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-4-1)import{AIMessage}from'@langchain/core/messages';
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-4-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-4-3)constmessageWithSingleToolCall=newAIMessage({
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-4-4)content:"",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-4-5)tool_calls:[
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-4-6){
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-4-7)name:"get_weather",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-4-8)args:{location:"sf"},
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-4-9)id:"tool_call_id",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-4-10)type:"tool_call",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-4-11)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-4-12)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-4-13)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-4-14)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-4-15)awaittoolNode.invoke({messages:[messageWithSingleToolCall]})

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-5-1){
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-5-2) messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-5-3)  ToolMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-5-4)   "content": "It's 60 degrees and foggy.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-5-5)   "name": "get_weather",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-5-6)   "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-5-7)   "response_metadata": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-5-8)   "tool_call_id": "tool_call_id"
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-5-9)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-5-10) ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-5-11)}

```


Note that typically you don't need to create `AIMessage` manually, and it will be automatically generated by any LangChain chat model that supports tool calling. 

You can also do parallel tool calling using `ToolNode` if you pass multiple tool calls to `AIMessage`'s `tool_calls` parameter:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-6-1)constmessageWithMultipleToolCalls=newAIMessage({
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-6-2)content:"",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-6-3)tool_calls:[
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-6-4){
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-6-5)name:"get_coolest_cities",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-6-6)args:{},
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-6-7)id:"tool_call_id",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-6-8)type:"tool_call",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-6-9)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-6-10){
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-6-11)name:"get_weather",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-6-12)args:{location:"sf"},
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-6-13)id:"tool_call_id_2",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-6-14)type:"tool_call",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-6-15)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-6-16)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-6-17)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-6-18)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-6-19)awaittoolNode.invoke({messages:[messageWithMultipleToolCalls]})

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-7-1){
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-7-2) messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-7-3)  ToolMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-7-4)   "content": "nyc, sf",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-7-5)   "name": "get_coolest_cities",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-7-6)   "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-7-7)   "response_metadata": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-7-8)   "tool_call_id": "tool_call_id"
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-7-9)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-7-10)  ToolMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-7-11)   "content": "It's 60 degrees and foggy.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-7-12)   "name": "get_weather",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-7-13)   "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-7-14)   "response_metadata": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-7-15)   "tool_call_id": "tool_call_id_2"
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-7-16)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-7-17) ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-7-18)}

```


## Using with chat models[¶](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#using-with-chat-models "Permanent link")

We'll be using a small chat model from Anthropic in our example. To use chat models with tool calling, we need to first ensure that the model is aware of the available tools. We do this by calling `.bindTools` method on `ChatAnthropic` model

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-8-1)import{ChatAnthropic}from"@langchain/anthropic";
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-8-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-8-3)constmodelWithTools=newChatAnthropic({
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-8-4)model:"claude-3-haiku-20240307",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-8-5)temperature:0
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-8-6)}).bindTools(tools);

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-9-1)constresponseMessage=awaitmodelWithTools.invoke("what's the weather in sf?");
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-9-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-9-3)responseMessage.tool_calls;

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-10-1)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-10-2) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-10-3)  name: 'get_weather',
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-10-4)  args: { location: 'sf' },
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-10-5)  id: 'toolu_01UAjv9Mmj9LRosAsrgKtqeR',
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-10-6)  type: 'tool_call'
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-10-7) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-10-8)]

```


As you can see, the AI message generated by the chat model already has `tool_calls` populated, so we can just pass it directly to `ToolNode`

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-11-1)awaittoolNode.invoke({messages:[awaitmodelWithTools.invoke("what's the weather in sf?")]})

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-12-1){
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-12-2) messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-12-3)  ToolMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-12-4)   "content": "It's 60 degrees and foggy.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-12-5)   "name": "get_weather",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-12-6)   "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-12-7)   "response_metadata": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-12-8)   "tool_call_id": "toolu_01HrJmUek2ninxDiLJrYpDpz"
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-12-9)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-12-10) ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-12-11)}

```


## ReAct Agent[¶](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#react-agent "Permanent link")

Next, let's see how to use `ToolNode` inside a LangGraph graph. Let's set up a graph implementation of the [ReAct agent](https://langchain-ai.github.io/langgraphjs/concepts/agentic_concepts/#react-agent). This agent takes some query as input, then repeatedly call tools until it has enough information to resolve the query. We'll be using `ToolNode` and the Anthropic model with tools we just defined

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-13-1)import{
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-13-2)StateGraph,
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-13-3)MessagesAnnotation,
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-13-4)END,
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-13-5)START
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-13-6)}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-13-7)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-13-8)consttoolNodeForGraph=newToolNode(tools)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-13-9)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-13-10)constshouldContinue=(state:typeofMessagesAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-13-11)const{messages}=state;
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-13-12)constlastMessage=messages[messages.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-13-13)if("tool_calls"inlastMessage&&Array.isArray(lastMessage.tool_calls)&&lastMessage.tool_calls?.length){
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-13-14)return"tools";
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-13-15)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-13-16)returnEND;
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-13-17)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-13-18)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-13-19)constcallModel=async(state:typeofMessagesAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-13-20)const{messages}=state;
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-13-21)constresponse=awaitmodelWithTools.invoke(messages);
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-13-22)return{messages:response};
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-13-23)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-13-24)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-13-25)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-13-26)constworkflow=newStateGraph(MessagesAnnotation)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-13-27)// Define the two nodes we will cycle between
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-13-28).addNode("agent",callModel)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-13-29).addNode("tools",toolNodeForGraph)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-13-30).addEdge(START,"agent")
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-13-31).addConditionalEdges("agent",shouldContinue,["tools",END])
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-13-32).addEdge("tools","agent");
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-13-33)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-13-34)constapp=workflow.compile()

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-14-1)import*astslabfrom"tslab";
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-14-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-14-3)constdrawableGraph=app.getGraph();
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-14-4)constimage=awaitdrawableGraph.drawMermaidPng();
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-14-5)constarrayBuffer=awaitimage.arrayBuffer();
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-14-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-14-7)awaittslab.display.png(newUint8Array(arrayBuffer));

```


![]()

Let's try it out!

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-15-1)import{HumanMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-15-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-15-3)// example with a single tool call
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-15-4)conststream=awaitapp.stream(
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-15-5){
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-15-6)messages:[{role:"user",content:"what's the weather in sf?"}],
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-15-7)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-15-8){
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-15-9)streamMode:"values"
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-15-10)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-15-11))
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-15-12)forawait(constchunkofstream){
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-15-13)constlastMessage=chunk.messages[chunk.messages.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-15-14)consttype=lastMessage._getType();
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-15-15)constcontent=lastMessage.content;
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-15-16)consttoolCalls=lastMessage.tool_calls;
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-15-17)console.dir({
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-15-18)type,
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-15-19)content,
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-15-20)toolCalls
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-15-21)},{depth:null});
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-15-22)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-16-1){
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-16-2) type: 'human',
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-16-3) content: "what's the weather in sf?",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-16-4) toolCalls: undefined
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-16-5)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-16-6){
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-16-7) type: 'ai',
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-16-8) content: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-16-9)  { type: 'text', text: "Okay, let's check the weather in SF:" },
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-16-10)  {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-16-11)   type: 'tool_use',
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-16-12)   id: 'toolu_01X5yTzVrGZqNz9vf1w2MCna',
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-16-13)   name: 'get_weather',
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-16-14)   input: { location: 'sf' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-16-15)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-16-16) ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-16-17) toolCalls: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-16-18)  {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-16-19)   name: 'get_weather',
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-16-20)   args: { location: 'sf' },
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-16-21)   id: 'toolu_01X5yTzVrGZqNz9vf1w2MCna',
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-16-22)   type: 'tool_call'
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-16-23)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-16-24) ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-16-25)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-16-26){
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-16-27) type: 'tool',
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-16-28) content: "It's 60 degrees and foggy.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-16-29) toolCalls: undefined
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-16-30)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-16-31){
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-16-32) type: 'ai',
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-16-33) content: 'The current weather in San Francisco is 60 degrees and foggy.',
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-16-34) toolCalls: []
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-16-35)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-17-1)// example with a multiple tool calls in succession
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-17-2)conststreamWithMultiToolCalls=awaitapp.stream(
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-17-3){
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-17-4)messages:[{role:"user",content:"what's the weather in the coolest cities?"}],
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-17-5)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-17-6){
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-17-7)streamMode:"values"
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-17-8)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-17-9))
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-17-10)forawait(constchunkofstreamWithMultiToolCalls){
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-17-11)constlastMessage=chunk.messages[chunk.messages.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-17-12)consttype=lastMessage._getType();
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-17-13)constcontent=lastMessage.content;
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-17-14)consttoolCalls=lastMessage.tool_calls;
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-17-15)console.dir({
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-17-16)type,
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-17-17)content,
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-17-18)toolCalls
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-17-19)},{depth:null});
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-17-20)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-1){
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-2) type: 'human',
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-3) content: "what's the weather in the coolest cities?",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-4) toolCalls: undefined
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-5)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-6){
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-7) type: 'ai',
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-8) content: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-9)  {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-10)   type: 'text',
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-11)   text: "Okay, let's find out the weather in the coolest cities:"
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-12)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-13)  {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-14)   type: 'tool_use',
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-15)   id: 'toolu_017RHcsJFeo7w6kDnZ6TAa19',
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-16)   name: 'get_coolest_cities',
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-17)   input: { noOp: 'dummy' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-18)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-19) ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-20) toolCalls: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-21)  {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-22)   name: 'get_coolest_cities',
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-23)   args: { noOp: 'dummy' },
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-24)   id: 'toolu_017RHcsJFeo7w6kDnZ6TAa19',
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-25)   type: 'tool_call'
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-26)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-27) ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-28)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-29){ type: 'tool', content: 'nyc, sf', toolCalls: undefined }
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-30){
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-31) type: 'ai',
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-32) content: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-33)  {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-34)   type: 'text',
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-35)   text: "Now let's get the weather for those cities:"
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-36)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-37)  {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-38)   type: 'tool_use',
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-39)   id: 'toolu_01ML1jW5u5aVCFkZhihzLv24',
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-40)   name: 'get_weather',
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-41)   input: { location: 'nyc' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-42)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-43) ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-44) toolCalls: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-45)  {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-46)   name: 'get_weather',
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-47)   args: { location: 'nyc' },
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-48)   id: 'toolu_01ML1jW5u5aVCFkZhihzLv24',
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-49)   type: 'tool_call'
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-50)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-51) ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-52)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-53){
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-54) type: 'tool',
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-55) content: "It's 90 degrees and sunny.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-56) toolCalls: undefined
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-57)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-58){
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-59) type: 'ai',
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-60) content: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-61)  {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-62)   type: 'tool_use',
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-63)   id: 'toolu_0187eWumoCgxjnCjq4RGHyun',
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-64)   name: 'get_weather',
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-65)   input: { location: 'sf' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-66)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-67) ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-68) toolCalls: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-69)  {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-70)   name: 'get_weather',
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-71)   args: { location: 'sf' },
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-72)   id: 'toolu_0187eWumoCgxjnCjq4RGHyun',
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-73)   type: 'tool_call'
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-74)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-75) ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-76)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-77){
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-78) type: 'tool',
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-79) content: "It's 60 degrees and foggy.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-80) toolCalls: undefined
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-81)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-82){
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-83) type: 'ai',
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-84) content: 'Based on the weather results, it looks like San Francisco is the coolest of the coolest cities, with a temperature of 60 degrees and foggy conditions. New York City is warmer at 90 degrees and sunny.',
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-85) toolCalls: []
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__codelineno-18-86)}

```


`ToolNode` can also handle errors during tool execution. See our guide on handling errors in `ToolNode` [here](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/).  Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to stream from the final node  ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-from-final-node/) [ Next  How to force an agent to call a tool  ](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
