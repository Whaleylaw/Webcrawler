---
url: https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#how-to-review-tool-calls-functional-api)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to review tool calls (Functional API) 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/?q= "Share")

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
          * Human-in-the-loop  Human-in-the-loop 
            * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraphjs/how-tos#human-in-the-loop)
            * [ How to add breakpoints  ](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/)
            * [ How to add dynamic breakpoints  ](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/)
            * [ How to edit graph state  ](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/)
            * [ How to wait for user input  ](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/)
            * [ How to wait for user input (Functional API)  ](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/)
            * [ How to view and update past graph state  ](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/)
            * [ Review Tool Calls  ](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/)
            * How to review tool calls (Functional API)  [ How to review tool calls (Functional API)  ](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#setup)
              * [ Define model and tools  ](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#define-model-and-tools)
              * [ Define tasks  ](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#define-tasks)
              * [ Define entrypoint  ](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#define-entrypoint)
                * [ Usage  ](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#usage)
                * [ Accept a tool call  ](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#accept-a-tool-call)
                * [ Revise a tool call  ](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#revise-a-tool-call)
                * [ Generate a custom ToolMessage  ](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#generate-a-custom-toolmessage)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#setup)
  * [ Define model and tools  ](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#define-model-and-tools)
  * [ Define tasks  ](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#define-tasks)
  * [ Define entrypoint  ](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#define-entrypoint)
    * [ Usage  ](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#usage)
    * [ Accept a tool call  ](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#accept-a-tool-call)
    * [ Revise a tool call  ](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#revise-a-tool-call)
    * [ Generate a custom ToolMessage  ](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#generate-a-custom-toolmessage)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
  5. [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraphjs/how-tos#human-in-the-loop)



# How to review tool calls (Functional API)[¶](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#how-to-review-tool-calls-functional-api "Permanent link")

Prerequisites

This guide assumes familiarity with the following:

  * Implementing [human-in-the-loop](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop) workflows with [interrupt](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#interrupt)
  * [How to create a ReAct agent using the Functional API](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional)



This guide demonstrates how to implement human-in-the-loop workflows in a ReAct agent using the LangGraph [Functional API](https://langchain-ai.github.io/langgraphjs/concepts/functional_api).

We will build off of the agent created in the [How to create a ReAct agent using the Functional API](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional) guide.

Specifically, we will demonstrate how to review [tool calls](https://js.langchain.com/docs/concepts/tool_calling/) generated by a [chat model](https://js.langchain.com/docs/concepts/chat_models/) prior to their execution. This can be accomplished through use of the [interrupt](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#interrupt) function at key points in our application.

**Preview** :

We will implement a simple function that reviews tool calls generated from our chat model and call it from inside our application's [entrypoint](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#entrypoint):

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-0-1)functionreviewToolCall(toolCall:ToolCall):ToolCall|ToolMessage{
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-0-2)// Interrupt for human review
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-0-3)consthumanReview=interrupt({
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-0-4)question:"Is this correct?",
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-0-5)tool_call:toolCall,
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-0-6)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-0-7)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-0-8)const{action,data}=humanReview;
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-0-9)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-0-10)if(action==="continue"){
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-0-11)returntoolCall;
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-0-12)}elseif(action==="update"){
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-0-13)return{
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-0-14)...toolCall,
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-0-15)args:data,
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-0-16)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-0-17)}elseif(action==="feedback"){
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-0-18)returnnewToolMessage({
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-0-19)content:data,
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-0-20)name:toolCall.name,
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-0-21)tool_call_id:toolCall.id,
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-0-22)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-0-23)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-0-24)thrownewError(`Unsupported review action: ${action}`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-0-25)}

```


## Setup[¶](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#setup "Permanent link")

Note

This guide requires `@langchain/langgraph>=0.2.42`.

First, install the required dependencies for this example:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-1-1)npminstall@langchain/langgraph@langchain/openai@langchain/corezod

```


Next, we need to set API keys for OpenAI (the LLM we will use):

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-2-1)process.env.OPENAI_API_KEY="YOUR_API_KEY";

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com)

## Define model and tools[¶](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#define-model-and-tools "Permanent link")

Let's first define the tools and model we will use for our example. As in the [ReAct agent guide](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional), we will use a single place-holder tool that gets a description of the weather for a location.

We will use an [OpenAI](https://js.langchain.com/docs/integrations/providers/openai/) chat model for this example, but any model [supporting tool-calling](https://js.langchain.com/docs/integrations/chat/) will suffice.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-3-1)import{ChatOpenAI}from"@langchain/openai";
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-3-2)import{tool}from"@langchain/core/tools";
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-3-3)import{z}from"zod";
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-3-4)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-3-5)constmodel=newChatOpenAI({
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-3-6)model:"gpt-4o-mini",
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-3-7)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-3-8)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-3-9)constgetWeather=tool(async({location})=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-3-10)// This is a placeholder for the actual implementation
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-3-11)constlowercaseLocation=location.toLowerCase();
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-3-12)if(lowercaseLocation.includes("sf")||lowercaseLocation.includes("san francisco")){
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-3-13)return"It's sunny!";
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-3-14)}elseif(lowercaseLocation.includes("boston")){
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-3-15)return"It's rainy!";
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-3-16)}else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-3-17)return`I am not sure what the weather is in ${location}`;
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-3-18)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-3-19)},{
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-3-20)name:"getWeather",
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-3-21)schema:z.object({
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-3-22)location:z.string().describe("Location to get the weather for"),
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-3-23)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-3-24)description:"Call to get the weather from a specific location.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-3-25)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-3-26)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-3-27)consttools=[getWeather];

```


## Define tasks[¶](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#define-tasks "Permanent link")

Our [tasks](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#task) are unchanged from the [ReAct agent guide](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional):

  1. **Call model** : We want to query our chat model with a list of messages.
  2. **Call tool** : If our model generates tool calls, we want to execute them.



```
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-4-1)import{
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-4-2)typeBaseMessageLike,
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-4-3)AIMessage,
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-4-4)ToolMessage,
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-4-5)}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-4-6)import{typeToolCall}from"@langchain/core/messages/tool";
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-4-7)import{task}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-4-8)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-4-9)consttoolsByName=Object.fromEntries(tools.map((tool)=>[tool.name,tool]));
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-4-10)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-4-11)constcallModel=task("callModel",async(messages:BaseMessageLike[])=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-4-12)constresponse=awaitmodel.bindTools(tools).invoke(messages);
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-4-13)returnresponse;
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-4-14)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-4-15)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-4-16)constcallTool=task(
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-4-17)"callTool",
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-4-18)async(toolCall:ToolCall):Promise<AIMessage>=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-4-19)consttool=toolsByName[toolCall.name];
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-4-20)constobservation=awaittool.invoke(toolCall.args);
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-4-21)returnnewToolMessage({content:observation,tool_call_id:toolCall.id});
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-4-22)// Can also pass toolCall directly into the tool to return a ToolMessage
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-4-23)// return tool.invoke(toolCall);
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-4-24)});

```


## Define entrypoint[¶](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#define-entrypoint "Permanent link")

To review tool calls before execution, we add a `reviewToolCalls` function that calls [interrupt](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#interrupt). When this function is called, execution will be paused until we issue a command to resume it.

Given a tool call, our function will `interrupt` for human review. At that point we can either:

  * Accept the tool call;
  * Revise the tool call and continue;
  * Generate a custom tool message (e.g., instructing the model to re-format its tool call).



We will demonstrate these three cases in the [usage examples](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#usage) below.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-5-1)import{interrupt}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-5-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-5-3)functionreviewToolCall(toolCall:ToolCall):ToolCall|ToolMessage{
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-5-4)// Interrupt for human review
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-5-5)consthumanReview=interrupt({
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-5-6)question:"Is this correct?",
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-5-7)tool_call:toolCall,
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-5-8)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-5-9)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-5-10)const{action,data}=humanReview;
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-5-11)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-5-12)if(action==="continue"){
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-5-13)returntoolCall;
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-5-14)}elseif(action==="update"){
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-5-15)return{
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-5-16)...toolCall,
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-5-17)args:data,
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-5-18)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-5-19)}elseif(action==="feedback"){
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-5-20)returnnewToolMessage({
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-5-21)content:data,
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-5-22)name:toolCall.name,
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-5-23)tool_call_id:toolCall.id,
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-5-24)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-5-25)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-5-26)thrownewError(`Unsupported review action: ${action}`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-5-27)}

```


We can now update our [entrypoint](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#entrypoint) to review the generated tool calls. If a tool call is accepted or revised, we execute in the same way as before. Otherwise, we just append the `ToolMessage` supplied by the human.

Tip

The results of prior tasks — in this case the initial model call — are persisted, so that they are not run again following the `interrupt`.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-1)import{
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-2)MemorySaver,
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-3)addMessages,
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-4)entrypoint,
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-5)getPreviousState,
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-6)}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-7)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-8)constcheckpointer=newMemorySaver();
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-9)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-10)constagent=entrypoint({
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-11)checkpointer,
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-12)name:"agent",
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-13)},async(messages:BaseMessageLike[])=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-14)constprevious=getPreviousState<BaseMessageLike[]>()??[];
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-15)letcurrentMessages=addMessages(previous,messages);
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-16)letllmResponse=awaitcallModel(currentMessages);
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-17)while(true){
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-18)if(!llmResponse.tool_calls?.length){
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-19)break;
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-20)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-21)// Review tool calls
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-22)consttoolResults:ToolMessage[]=[];
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-23)consttoolCalls:ToolCall[]=[];
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-24)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-25)for(leti=0;i<llmResponse.tool_calls.length;i++){
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-26)constreview=awaitreviewToolCall(llmResponse.tool_calls[i]);
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-27)if(reviewinstanceofToolMessage){
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-28)toolResults.push(review);
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-29)}else{// is a validated tool call
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-30)toolCalls.push(review);
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-31)if(review!==llmResponse.tool_calls[i]){
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-32)llmResponse.tool_calls[i]=review;
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-33)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-34)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-35)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-36)// Execute remaining tool calls
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-37)constremainingToolResults=awaitPromise.all(
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-38)toolCalls.map((toolCall)=>callTool(toolCall))
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-39));
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-40)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-41)// Append to message list
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-42)currentMessages=addMessages(
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-43)currentMessages,
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-44)[llmResponse,...toolResults,...remainingToolResults]
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-45));
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-46)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-47)// Call model again
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-48)llmResponse=awaitcallModel(currentMessages);
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-49)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-50)// Generate final response
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-51)currentMessages=addMessages(currentMessages,llmResponse);
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-52)returnentrypoint.final({
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-53)value:llmResponse,
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-54)save:currentMessages
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-55)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-6-56)});

```


### Usage[¶](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#usage "Permanent link")

Let's demonstrate some scenarios.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-7-1)import{BaseMessage,isAIMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-7-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-7-3)constprettyPrintMessage=(message:BaseMessage)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-7-4)console.log("=".repeat(30),`${message.getType()} message`,"=".repeat(30));
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-7-5)console.log(message.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-7-6)if(isAIMessage(message)&&message.tool_calls?.length){
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-7-7)console.log(JSON.stringify(message.tool_calls,null,2));
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-7-8)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-7-9)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-7-10)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-7-11)constprintStep=(step:Record<string,any>)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-7-12)if(step.__metadata__?.cached){
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-7-13)return;
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-7-14)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-7-15)for(const[taskName,result]ofObject.entries(step)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-7-16)if(taskName==="agent"){
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-7-17)continue;// just stream from tasks
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-7-18)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-7-19)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-7-20)console.log(`\n${taskName}:`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-7-21)if(taskName==="__interrupt__"||taskName==="reviewToolCall"){
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-7-22)console.log(JSON.stringify(result,null,2));
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-7-23)}else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-7-24)prettyPrintMessage(result);
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-7-25)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-7-26)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-7-27)};

```


### Accept a tool call[¶](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#accept-a-tool-call "Permanent link")

To accept a tool call, we just indicate in the data we provide in the `Command` that the tool call should pass through.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-8-1)constconfig={
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-8-2)configurable:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-8-3)thread_id:"1"
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-8-4)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-8-5)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-8-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-8-7)constuserMessage={
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-8-8)role:"user",
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-8-9)content:"What's the weather in san francisco?"
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-8-10)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-8-11)console.log(userMessage);
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-8-12)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-8-13)conststream=awaitagent.stream([userMessage],config);
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-8-14)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-8-15)forawait(conststepofstream){
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-8-16)printStep(step);
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-8-17)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-9-1){ role: 'user', content: "What's the weather in san francisco?" }
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-9-2)``````output
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-9-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-9-4)callModel:
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-9-5)============================== ai message ==============================
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-9-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-9-7)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-9-8) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-9-9)  "name": "getWeather",
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-9-10)  "args": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-9-11)   "location": "San Francisco"
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-9-12)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-9-13)  "type": "tool_call",
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-9-14)  "id": "call_pe7ee3A4lOO4Llr2NcfRukyp"
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-9-15) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-9-16)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-9-17)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-9-18)__interrupt__:
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-9-19)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-9-20) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-9-21)  "value": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-9-22)   "question": "Is this correct?",
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-9-23)   "tool_call": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-9-24)    "name": "getWeather",
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-9-25)    "args": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-9-26)     "location": "San Francisco"
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-9-27)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-9-28)    "type": "tool_call",
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-9-29)    "id": "call_pe7ee3A4lOO4Llr2NcfRukyp"
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-9-30)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-9-31)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-9-32)  "when": "during",
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-9-33)  "resumable": true,
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-9-34)  "ns": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-9-35)   "agent:dcee519a-80f5-5950-9e1c-e8bb85ed436f"
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-9-36)  ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-9-37) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-9-38)]

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-10-1)import{Command}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-10-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-10-3)consthumanInput=newCommand({
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-10-4)resume:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-10-5)action:"continue",
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-10-6)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-10-7)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-10-8)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-10-9)constresumedStream=awaitagent.stream(humanInput,config)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-10-10)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-10-11)forawait(conststepofresumedStream){
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-10-12)printStep(step);
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-10-13)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-11-1)callTool:
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-11-2)============================== tool message ==============================
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-11-3)It's sunny!
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-11-4)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-11-5)callModel:
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-11-6)============================== ai message ==============================
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-11-7)The weather in San Francisco is sunny!

```


### Revise a tool call[¶](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#revise-a-tool-call "Permanent link")

To revise a tool call, we can supply updated arguments.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-12-1)constconfig2={
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-12-2)configurable:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-12-3)thread_id:"2"
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-12-4)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-12-5)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-12-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-12-7)constuserMessage2={
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-12-8)role:"user",
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-12-9)content:"What's the weather in san francisco?"
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-12-10)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-12-11)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-12-12)console.log(userMessage2);
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-12-13)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-12-14)conststream2=awaitagent.stream([userMessage2],config2);
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-12-15)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-12-16)forawait(conststepofstream2){
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-12-17)printStep(step);
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-12-18)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-13-1){ role: 'user', content: "What's the weather in san francisco?" }
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-13-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-13-3)callModel:
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-13-4)============================== ai message ==============================
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-13-5)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-13-6)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-13-7) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-13-8)  "name": "getWeather",
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-13-9)  "args": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-13-10)   "location": "San Francisco"
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-13-11)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-13-12)  "type": "tool_call",
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-13-13)  "id": "call_JEOqaUEvYJ4pzMtVyCQa6H2H"
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-13-14) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-13-15)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-13-16)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-13-17)__interrupt__:
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-13-18)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-13-19) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-13-20)  "value": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-13-21)   "question": "Is this correct?",
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-13-22)   "tool_call": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-13-23)    "name": "getWeather",
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-13-24)    "args": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-13-25)     "location": "San Francisco"
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-13-26)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-13-27)    "type": "tool_call",
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-13-28)    "id": "call_JEOqaUEvYJ4pzMtVyCQa6H2H"
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-13-29)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-13-30)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-13-31)  "when": "during",
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-13-32)  "resumable": true,
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-13-33)  "ns": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-13-34)   "agent:d5c54c67-483a-589a-a1e7-2a8465b3ef13"
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-13-35)  ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-13-36) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-13-37)]

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-14-1)consthumanInput2=newCommand({
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-14-2)resume:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-14-3)action:"update",
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-14-4)data:{location:"SF, CA"},
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-14-5)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-14-6)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-14-7)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-14-8)constresumedStream2=awaitagent.stream(humanInput2,config2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-14-9)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-14-10)forawait(conststepofresumedStream2){
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-14-11)printStep(step);
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-14-12)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-15-1)callTool:
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-15-2)============================== tool message ==============================
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-15-3)It's sunny!
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-15-4)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-15-5)callModel:
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-15-6)============================== ai message ==============================
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-15-7)The weather in San Francisco is sunny!

```


The LangSmith traces for this run are particularly informative: 

  * In the trace [before the interrupt](https://smith.langchain.com/public/abf80a16-3e15-484b-bbbb-23017593bd39/r), we generate a tool call for location `"San Francisco"`.
  * In the trace [after resuming](https://smith.langchain.com/public/233a7e32-a43e-4939-9c04-96fd4254ce65/r), we see that the tool call in the message has been updated to `"SF, CA"`.



### Generate a custom ToolMessage[¶](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#generate-a-custom-toolmessage "Permanent link")

To Generate a custom `ToolMessage`, we supply the content of the message. In this case we will ask the model to reformat its tool call.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-16-1)constconfig3={
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-16-2)configurable:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-16-3)thread_id:"3"
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-16-4)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-16-5)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-16-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-16-7)constuserMessage3={
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-16-8)role:"user",
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-16-9)content:"What's the weather in san francisco?"
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-16-10)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-16-11)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-16-12)console.log(userMessage3);
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-16-13)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-16-14)conststream3=awaitagent.stream([userMessage3],config3);
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-16-15)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-16-16)forawait(conststepofstream3){
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-16-17)printStep(step);
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-16-18)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-17-1){ role: 'user', content: "What's the weather in san francisco?" }
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-17-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-17-3)callModel:
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-17-4)============================== ai message ==============================
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-17-5)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-17-6)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-17-7) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-17-8)  "name": "getWeather",
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-17-9)  "args": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-17-10)   "location": "San Francisco"
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-17-11)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-17-12)  "type": "tool_call",
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-17-13)  "id": "call_HNRjJLJo4U78dtk0uJ9YZF6V"
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-17-14) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-17-15)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-17-16)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-17-17)__interrupt__:
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-17-18)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-17-19) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-17-20)  "value": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-17-21)   "question": "Is this correct?",
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-17-22)   "tool_call": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-17-23)    "name": "getWeather",
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-17-24)    "args": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-17-25)     "location": "San Francisco"
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-17-26)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-17-27)    "type": "tool_call",
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-17-28)    "id": "call_HNRjJLJo4U78dtk0uJ9YZF6V"
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-17-29)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-17-30)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-17-31)  "when": "during",
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-17-32)  "resumable": true,
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-17-33)  "ns": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-17-34)   "agent:6f313de8-c19e-5c3e-bdff-f90cdd68d0de"
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-17-35)  ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-17-36) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-17-37)]

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-18-1)consthumanInput3=newCommand({
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-18-2)resume:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-18-3)action:"feedback",
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-18-4)data:"Please format as <City>, <State>.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-18-5)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-18-6)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-18-7)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-18-8)constresumedStream3=awaitagent.stream(humanInput3,config3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-18-9)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-18-10)forawait(conststepofresumedStream3){
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-18-11)printStep(step);
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-18-12)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-19-1)callModel:
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-19-2)============================== ai message ==============================
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-19-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-19-4)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-19-5) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-19-6)  "name": "getWeather",
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-19-7)  "args": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-19-8)   "location": "San Francisco, CA"
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-19-9)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-19-10)  "type": "tool_call",
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-19-11)  "id": "call_5V4Oj4JV2DVfeteM4Aaf2ieD"
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-19-12) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-19-13)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-19-14)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-19-15)__interrupt__:
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-19-16)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-19-17) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-19-18)  "value": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-19-19)   "question": "Is this correct?",
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-19-20)   "tool_call": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-19-21)    "name": "getWeather",
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-19-22)    "args": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-19-23)     "location": "San Francisco, CA"
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-19-24)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-19-25)    "type": "tool_call",
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-19-26)    "id": "call_5V4Oj4JV2DVfeteM4Aaf2ieD"
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-19-27)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-19-28)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-19-29)  "when": "during",
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-19-30)  "resumable": true,
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-19-31)  "ns": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-19-32)   "agent:6f313de8-c19e-5c3e-bdff-f90cdd68d0de"
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-19-33)  ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-19-34) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-19-35)]

```


Once it is re-formatted, we can accept it: 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-20-1)constcontinueCommand=newCommand({
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-20-2)resume:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-20-3)action:"continue",
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-20-4)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-20-5)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-20-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-20-7)constcontinueStream=awaitagent.stream(continueCommand,config3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-20-8)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-20-9)forawait(conststepofcontinueStream){
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-20-10)printStep(step);
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-20-11)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-21-1)callTool:
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-21-2)============================== tool message ==============================
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-21-3)It's sunny!
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-21-4)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-21-5)callModel:
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-21-6)============================== ai message ==============================
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-21-7)The weather in San Francisco, CA is sunny!

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__codelineno-22-1)

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  Review Tool Calls  ](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/) [ Next  How to stream full state of your graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
