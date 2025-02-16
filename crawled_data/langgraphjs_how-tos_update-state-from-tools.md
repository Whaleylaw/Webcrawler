---
url: https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#how-to-update-graph-state-from-tools)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to update graph state from tools 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/?q= "Share")

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
            * [ How to call tools using ToolNode  ](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/)
            * [ How to force an agent to call a tool  ](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/)
            * [ How to handle tool calling errors  ](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/)
            * [ How to pass runtime values to tools  ](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/)
            * How to update graph state from tools  [ How to update graph state from tools  ](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#setup)
              * [ Define tool  ](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#define-tool)
              * [ Define prompt  ](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#define-prompt)
              * [ Define graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#define-graph)
              * [ Use it!  ](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#use-it)
              * [ Custom components  ](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#custom-components)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#setup)
  * [ Define tool  ](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#define-tool)
  * [ Define prompt  ](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#define-prompt)
  * [ Define graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#define-graph)
  * [ Use it!  ](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#use-it)
  * [ Custom components  ](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#custom-components)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
  5. [ Tool calling  ](https://langchain-ai.github.io/langgraphjs/how-tos#tool-calling)



# How to update graph state from tools[¶](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#how-to-update-graph-state-from-tools "Permanent link")

Prerequisites

This guide assumes familiarity with the following: 

  * [ Command ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#command)



A common use case is updating graph state from inside a tool. For example, in a customer support application you might want to look up customer account number or ID in the beginning of the conversation. To update the graph state from the tool, you can return a `Command`[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#command) object from the tool:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-0-1)import{tool}from"@langchain/core/tools";
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-0-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-0-3)constlookupUserInfo=tool(async(input,config)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-0-4)constuserInfo=getUserInfo(config);
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-0-5)returnnewCommand({
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-0-6)// update state keys
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-0-7)update:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-0-8)user_info:userInfo,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-0-9)messages:[
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-0-10)newToolMessage({
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-0-11)content:"Successfully looked up user information",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-0-12)tool_call_id:config.toolCall.id,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-0-13)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-0-14)],
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-0-15)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-0-16)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-0-17)},{
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-0-18)name:"lookup_user_info",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-0-19)description:"Use this to look up user information to better assist them with their questions.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-0-20)schema:z.object(...)
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-0-21)});

```


Important

If you want to use tools that return `Command` instances and update graph state, you can either use prebuilt `createReactAgent`[](https://langchain-ai.github.io/langgraphjs/reference/functions/langgraph_prebuilt.createReactAgent.html) / `ToolNode`[](https://langchain-ai.github.io/langgraphjs/reference/classes/langgraph_prebuilt.ToolNode.html) components, or implement your own tool-executing node that identifies `Command` objects returned by your tools and returns a mixed array of traditional state updates and `Commands`. See [this section](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#custom-components) for an example. 

This guide shows how you can do this using LangGraph's prebuilt components (`createReactAgent`[](https://langchain-ai.github.io/langgraphjs/reference/functions/langgraph_prebuilt.createReactAgent.html) and `ToolNode`[](https://langchain-ai.github.io/langgraphjs/reference/classes/langgraph_prebuilt.ToolNode.html)).

Compatibility

This guide requires `@langchain/langgraph>=0.2.33` and `@langchain/core@0.3.23`. For help upgrading, see [this guide](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/). 

## Setup[¶](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#setup "Permanent link")

Install the following to run this guide:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-1-1)npminstall@langchain/langgraph@langchain/openai@langchain/core

```


Next, configure your environment to connect to your model provider.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-2-1)exportOPENAI_API_KEY=your-api-key

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

Let's create a simple ReAct style agent that can look up user information and personalize the response based on the user info.

## Define tool[¶](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#define-tool "Permanent link")

First, let's define the tool that we'll be using to look up user information. We'll use a naive implementation that simply looks user information up using a dictionary:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-3-1)constUSER_ID_TO_USER_INFO={
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-3-2)abc123:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-3-3)user_id:"abc123",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-3-4)name:"Bob Dylan",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-3-5)location:"New York, NY",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-3-6)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-3-7)zyx987:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-3-8)user_id:"zyx987",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-3-9)name:"Taylor Swift",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-3-10)location:"Beverly Hills, CA",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-3-11)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-3-12)};

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-4-1)import{Annotation,Command,MessagesAnnotation}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-4-2)import{tool}from"@langchain/core/tools";
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-4-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-4-4)import{z}from"zod";
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-4-5)
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-4-6)constStateAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-4-7)...MessagesAnnotation.spec,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-4-8)// user provided
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-4-9)lastName:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-4-10)// updated by the tool
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-4-11)userInfo:Annotation<Record<string,any>>,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-4-12)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-4-13)
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-4-14)constlookupUserInfo=tool(async(_,config)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-4-15)constuserId=config.configurable?.user_id;
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-4-16)if(userId===undefined){
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-4-17)thrownewError("Please provide a user id in config.configurable");
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-4-18)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-4-19)if(USER_ID_TO_USER_INFO[userId]===undefined){
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-4-20)thrownewError(`User "${userId}" not found`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-4-21)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-4-22)// Populated when a tool is called with a tool call from a model as input
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-4-23)consttoolCallId=config.toolCall.id;
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-4-24)returnnewCommand({
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-4-25)update:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-4-26)// update the state keys
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-4-27)userInfo:USER_ID_TO_USER_INFO[userId],
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-4-28)// update the message history
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-4-29)messages:[
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-4-30){
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-4-31)role:"tool",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-4-32)content:"Successfully looked up user information",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-4-33)tool_call_id:toolCallId,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-4-34)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-4-35)],
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-4-36)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-4-37)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-4-38)},{
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-4-39)name:"lookup_user_info",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-4-40)description:"Always use this to look up information about the user to better assist them with their questions.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-4-41)schema:z.object({}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-4-42)});

```


## Define prompt[¶](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#define-prompt "Permanent link")

Let's now add personalization: we'll respond differently to the user based on the state values AFTER the state has been updated from the tool. To achieve this, let's define a function that will dynamically construct the system prompt based on the graph state. It will be called ever time the LLM is called and the function output will be passed to the LLM:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-5-1)conststateModifier=(state:typeofStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-5-2)constuserInfo=state.userInfo;
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-5-3)if(userInfo==null){
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-5-4)returnstate.messages;
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-5-5)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-5-6)constsystemMessage=`User name is ${userInfo.name}. User lives in ${userInfo.location}`;
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-5-7)return[{
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-5-8)role:"system",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-5-9)content:systemMessage,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-5-10)},...state.messages];
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-5-11)};

```


## Define graph[¶](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#define-graph "Permanent link")

Finally, let's combine this into a single graph using the prebuilt `createReactAgent` and the components we declared earlier:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-6-1)import{createReactAgent}from"@langchain/langgraph/prebuilt";
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-6-2)import{ChatOpenAI}from"@langchain/openai";
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-6-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-6-4)constmodel=newChatOpenAI({
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-6-5)model:"gpt-4o",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-6-6)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-6-7)
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-6-8)constagent=createReactAgent({
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-6-9)llm:model,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-6-10)tools:[lookupUserInfo],
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-6-11)stateSchema:StateAnnotation,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-6-12)stateModifier:stateModifier,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-6-13)})

```


## Use it![¶](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#use-it "Permanent link")

Let's now try running our agent. We'll need to provide user ID in the config so that our tool knows what information to look up:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-7-1)conststream=awaitagent.stream({
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-7-2)messages:[{
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-7-3)role:"user",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-7-4)content:"hi, what should i do this weekend?",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-7-5)}],
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-7-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-7-7)},{
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-7-8)// provide user ID in the config
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-7-9)configurable:{user_id:"abc123"}
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-7-10)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-7-11)
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-7-12)forawait(constchunkofstream){
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-7-13)console.log(chunk);
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-7-14)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-1){
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-2) agent: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-3)  messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-4)   AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-5)    "id": "chatcmpl-AdmOZdrZy3aUgNimCIjq8ZW5js6ln",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-6)    "content": "",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-7)    "additional_kwargs": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-8)     "tool_calls": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-9)      {
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-10)       "id": "call_kLXWJYbabxWpj7vykXD6ZMx0",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-11)       "type": "function",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-12)       "function": "[Object]"
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-13)      }
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-14)     ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-15)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-16)    "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-17)     "tokenUsage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-18)      "promptTokens": 59,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-19)      "completionTokens": 11,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-20)      "totalTokens": 70
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-21)     },
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-22)     "finish_reason": "tool_calls",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-23)     "usage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-24)      "prompt_tokens": 59,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-25)      "completion_tokens": 11,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-26)      "total_tokens": 70,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-27)      "prompt_tokens_details": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-28)       "cached_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-29)       "audio_tokens": 0
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-30)      },
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-31)      "completion_tokens_details": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-32)       "reasoning_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-33)       "audio_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-34)       "accepted_prediction_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-35)       "rejected_prediction_tokens": 0
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-36)      }
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-37)     },
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-38)     "system_fingerprint": "fp_f785eb5f47"
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-39)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-40)    "tool_calls": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-41)     {
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-42)      "name": "lookup_user_info",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-43)      "args": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-44)      "type": "tool_call",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-45)      "id": "call_kLXWJYbabxWpj7vykXD6ZMx0"
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-46)     }
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-47)    ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-48)    "invalid_tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-49)    "usage_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-50)     "output_tokens": 11,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-51)     "input_tokens": 59,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-52)     "total_tokens": 70,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-53)     "input_token_details": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-54)      "audio": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-55)      "cache_read": 0
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-56)     },
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-57)     "output_token_details": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-58)      "audio": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-59)      "reasoning": 0
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-60)     }
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-61)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-62)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-63)  ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-64) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-65)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-66){
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-67) tools: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-68)  userInfo: { user_id: 'abc123', name: 'Bob Dylan', location: 'New York, NY' },
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-69)  messages: [ [Object] ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-70) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-71)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-72){
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-73) agent: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-74)  messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-75)   AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-76)    "id": "chatcmpl-AdmOZJ0gSQ7VVCUfcadhOeqq4HxWa",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-77)    "content": "Hi Bob! Since you're in New York, NY, there are plenty of exciting things you can do this weekend. Here are a few suggestions:\n\n1. **Visit Central Park**: Enjoy a leisurely walk, rent a bike, or have a picnic. The park is beautiful in the fall.\n\n2. **Explore Museums**: Check out The Met, MoMA, or The American Museum of Natural History if you're interested in art or history.\n\n3. **Broadway Show**: Catch a Broadway show or a musical for an entertaining evening.\n\n4. **Visit Times Square**: Experience the vibrant lights and energy of Times Square. There are plenty of shops and restaurants to explore.\n\n5. **Brooklyn Bridge Walk**: Walk across the iconic Brooklyn Bridge and enjoy stunning views of Manhattan and Brooklyn.\n\n6. **Cultural Festivals or Events**: Check local listings for any cultural festivals or events happening in the city this weekend.\n\nIf you have specific interests, let me know, and I can suggest something more tailored to your preferences!",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-78)    "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-79)    "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-80)     "tokenUsage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-81)      "promptTokens": 98,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-82)      "completionTokens": 209,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-83)      "totalTokens": 307
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-84)     },
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-85)     "finish_reason": "stop",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-86)     "usage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-87)      "prompt_tokens": 98,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-88)      "completion_tokens": 209,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-89)      "total_tokens": 307,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-90)      "prompt_tokens_details": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-91)       "cached_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-92)       "audio_tokens": 0
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-93)      },
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-94)      "completion_tokens_details": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-95)       "reasoning_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-96)       "audio_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-97)       "accepted_prediction_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-98)       "rejected_prediction_tokens": 0
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-99)      }
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-100)     },
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-101)     "system_fingerprint": "fp_cc5cf1c6e3"
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-102)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-103)    "tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-104)    "invalid_tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-105)    "usage_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-106)     "output_tokens": 209,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-107)     "input_tokens": 98,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-108)     "total_tokens": 307,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-109)     "input_token_details": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-110)      "audio": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-111)      "cache_read": 0
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-112)     },
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-113)     "output_token_details": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-114)      "audio": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-115)      "reasoning": 0
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-116)     }
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-117)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-118)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-119)  ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-120) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-8-121)}

```


We can see that the model correctly recommended some New York activities for Bob Dylan! Let's try getting recommendations for Taylor Swift: 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-9-1)consttaylorStream=awaitagent.stream({
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-9-2)messages:[{
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-9-3)role:"user",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-9-4)content:"hi, what should i do this weekend?",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-9-5)}],
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-9-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-9-7)},{
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-9-8)// provide user ID in the config
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-9-9)configurable:{user_id:"zyx987"}
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-9-10)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-9-11)
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-9-12)forawait(constchunkoftaylorStream){
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-9-13)console.log(chunk);
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-9-14)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-1){
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-2) agent: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-3)  messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-4)   AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-5)    "id": "chatcmpl-AdmQGANyXPTAkMnQ86hGWB5XY5hGL",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-6)    "content": "",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-7)    "additional_kwargs": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-8)     "tool_calls": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-9)      {
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-10)       "id": "call_IvyfreezvohjGgUx9DrwfS5O",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-11)       "type": "function",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-12)       "function": "[Object]"
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-13)      }
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-14)     ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-15)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-16)    "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-17)     "tokenUsage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-18)      "promptTokens": 59,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-19)      "completionTokens": 11,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-20)      "totalTokens": 70
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-21)     },
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-22)     "finish_reason": "tool_calls",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-23)     "usage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-24)      "prompt_tokens": 59,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-25)      "completion_tokens": 11,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-26)      "total_tokens": 70,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-27)      "prompt_tokens_details": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-28)       "cached_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-29)       "audio_tokens": 0
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-30)      },
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-31)      "completion_tokens_details": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-32)       "reasoning_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-33)       "audio_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-34)       "accepted_prediction_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-35)       "rejected_prediction_tokens": 0
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-36)      }
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-37)     },
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-38)     "system_fingerprint": "fp_cc5cf1c6e3"
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-39)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-40)    "tool_calls": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-41)     {
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-42)      "name": "lookup_user_info",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-43)      "args": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-44)      "type": "tool_call",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-45)      "id": "call_IvyfreezvohjGgUx9DrwfS5O"
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-46)     }
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-47)    ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-48)    "invalid_tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-49)    "usage_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-50)     "output_tokens": 11,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-51)     "input_tokens": 59,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-52)     "total_tokens": 70,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-53)     "input_token_details": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-54)      "audio": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-55)      "cache_read": 0
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-56)     },
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-57)     "output_token_details": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-58)      "audio": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-59)      "reasoning": 0
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-60)     }
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-61)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-62)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-63)  ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-64) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-65)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-66){
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-67) tools: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-68)  userInfo: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-69)   user_id: 'zyx987',
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-70)   name: 'Taylor Swift',
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-71)   location: 'Beverly Hills, CA'
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-72)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-73)  messages: [ [Object] ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-74) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-75)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-76){
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-77) agent: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-78)  messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-79)   AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-80)    "id": "chatcmpl-AdmQHMYj613jksQJruNMVP6DfAagd",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-81)    "content": "This weekend, there are plenty of exciting things you can do around Beverly Hills, CA. Here are some options:\n\n1. **Explore Rodeo Drive**: Enjoy high-end shopping and dining experiences in this iconic shopping district.\n  \n2. **Visit a Museum**: Check out The Getty Center or Los Angeles County Museum of Art (LACMA) for a dose of culture and art.\n\n3. **Hiking**: Take a scenic hike in the nearby Santa Monica Mountains or Griffith Park for beautiful views of the city.\n\n4. **Spa Day**: Treat yourself to a relaxing spa day at one of Beverly Hills' luxurious spas.\n\n5. **Restaurant Tour**: Dine at some of Beverly Hills' finest restaurants, such as Spago or The Penthouse.\n\n6. **Take a Scenic Drive**: Drive along Mulholland Drive for stunning views of Los Angeles and the surrounding areas.\n\n7. **Catch a Show**: See if there are any live performances or concerts happening at The Hollywood Bowl or other nearby venues.\n\nEnjoy your weekend!",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-82)    "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-83)    "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-84)     "tokenUsage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-85)      "promptTokens": 98,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-86)      "completionTokens": 214,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-87)      "totalTokens": 312
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-88)     },
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-89)     "finish_reason": "stop",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-90)     "usage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-91)      "prompt_tokens": 98,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-92)      "completion_tokens": 214,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-93)      "total_tokens": 312,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-94)      "prompt_tokens_details": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-95)       "cached_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-96)       "audio_tokens": 0
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-97)      },
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-98)      "completion_tokens_details": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-99)       "reasoning_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-100)       "audio_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-101)       "accepted_prediction_tokens": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-102)       "rejected_prediction_tokens": 0
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-103)      }
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-104)     },
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-105)     "system_fingerprint": "fp_9d50cd990b"
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-106)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-107)    "tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-108)    "invalid_tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-109)    "usage_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-110)     "output_tokens": 214,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-111)     "input_tokens": 98,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-112)     "total_tokens": 312,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-113)     "input_token_details": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-114)      "audio": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-115)      "cache_read": 0
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-116)     },
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-117)     "output_token_details": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-118)      "audio": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-119)      "reasoning": 0
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-120)     }
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-121)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-122)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-123)  ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-124) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-10-125)}

```


## Custom components[¶](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#custom-components "Permanent link")

If you do not wish to use prebuilt components, you will need to have special logic in your custom tool executor to handle commands. Here's an example:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-1)import{
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-2)MessagesAnnotation,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-3)isCommand,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-4)Command,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-5)StateGraph,
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-6)}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-7)import{tool}from"@langchain/core/tools";
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-8)import{isAIMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-9)
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-10)import{z}from"zod";
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-11)
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-12)constmyTool=tool(async()=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-13)returnnewCommand({
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-14)update:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-15)messages:[
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-16){
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-17)role:"assistant",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-18)content:"hi there!",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-19)name:"Greeter",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-20)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-21)],
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-22)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-23)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-24)},{
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-25)name:"greeting",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-26)description:"Updates the current state with a greeting",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-27)schema:z.object({}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-28)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-29)
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-30)consttoolExecutor=async(state:typeofMessagesAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-31)constmessage=state.messages.at(-1);
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-32)if(!isAIMessage(message)||message.tool_calls===undefined||message.tool_calls.length===0){
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-33)thrownewError("Most recent message must be an AIMessage with a tool call.")
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-34)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-35)constoutputs=awaitPromise.all(
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-36)message.tool_calls.map(async(toolCall)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-37)// Using a single tool for simplicity, would need to select tools by toolCall.name
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-38)// in practice.
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-39)consttoolResult=awaitmyTool.invoke(toolCall);
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-40)returntoolResult;
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-41)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-42));
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-43)// Handle mixed Command and non-Command outputs
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-44)constcombinedOutputs=outputs.map((output)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-45)if(isCommand(output)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-46)returnoutput;
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-47)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-48)// Tool invocation result is a ToolMessage, return a normal state update
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-49)return{messages:[output]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-50)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-51)// Return an array of values instead of an object
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-52)returncombinedOutputs;
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-53)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-54)
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-55)// Simple one node graph
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-56)constcustomGraph=newStateGraph(MessagesAnnotation)
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-57).addNode("runTools",toolExecutor)
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-58).addEdge("__start__","runTools")
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-59).compile();
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-60)
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-61)awaitcustomGraph.invoke({
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-62)messages:[{
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-63)role:"user",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-64)content:"how are you?",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-65)},{
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-66)role:"assistant",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-67)content:"Let me call the greeting tool and find out!",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-68)tool_calls:[{
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-69)id:"123",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-70)args:{},
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-71)name:"greeting",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-72)}],
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-73)}],
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-11-74)});

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-12-1){
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-12-2) messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-12-3)  HumanMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-12-4)   "id": "801308df-c702-49f4-99c1-da4116f6bbc8",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-12-5)   "content": "how are you?",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-12-6)   "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-12-7)   "response_metadata": {}
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-12-8)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-12-9)  AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-12-10)   "id": "8ea07329-a73a-4de4-a4d4-4453fbef32e0",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-12-11)   "content": "Let me call the greeting tool and find out!",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-12-12)   "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-12-13)   "response_metadata": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-12-14)   "tool_calls": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-12-15)    {
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-12-16)     "id": "123",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-12-17)     "args": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-12-18)     "name": "greeting"
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-12-19)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-12-20)   ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-12-21)   "invalid_tool_calls": []
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-12-22)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-12-23)  AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-12-24)   "id": "4ecba93a-77c0-44a6-8dc9-8b27d9615c15",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-12-25)   "content": "hi there!",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-12-26)   "name": "Greeter",
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-12-27)   "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-12-28)   "response_metadata": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-12-29)   "tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-12-30)   "invalid_tool_calls": []
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-12-31)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-12-32) ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-12-33)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__codelineno-13-1)

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to pass runtime values to tools  ](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/) [ Next  How to add and use subgraphs  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
