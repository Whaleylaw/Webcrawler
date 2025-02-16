---
url: https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#review-tool-calls)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

Review Tool Calls 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/?q= "Share")

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
            * Review Tool Calls  [ Review Tool Calls  ](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#setup)
              * [ Simple Usage  ](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#simple-usage)
              * [ Example with no review  ](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#example-with-no-review)
              * [ Example of approving tool  ](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#example-of-approving-tool)
              * [ Edit Tool Call  ](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#edit-tool-call)
              * [ Give feedback to a tool call  ](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#give-feedback-to-a-tool-call)
            * [ How to review tool calls (Functional API)  ](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#setup)
  * [ Simple Usage  ](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#simple-usage)
  * [ Example with no review  ](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#example-with-no-review)
  * [ Example of approving tool  ](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#example-of-approving-tool)
  * [ Edit Tool Call  ](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#edit-tool-call)
  * [ Give feedback to a tool call  ](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#give-feedback-to-a-tool-call)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
  5. [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraphjs/how-tos#human-in-the-loop)



# Review Tool Calls[¶](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#review-tool-calls "Permanent link")

Prerequisites

This guide assumes familiarity with the following concepts:

  * [Tool calling](https://js.langchain.com/docs/concepts/tool_calling/)
  * [Human-in-the-loop](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop)
  * [LangGraph Glossary](https://langchain-ai.github.io/langgraphjs/concepts/low_level)



Human-in-the-loop (HIL) interactions are crucial for [agentic systems](https://langchain-ai.github.io/langgraphjs/concepts/agentic_concepts/#human-in-the-loop). A common pattern is to add some human in the loop step after certain tool calls. These tool calls often lead to either a function call or saving of some information. Examples include:

  * A tool call to execute SQL, which will then be run by the tool
  * A tool call to generate a summary, which will then be saved to the State of the graph



Note that using tool calls is common **whether actually calling tools or not**.

There are typically a few different interactions you may want to do here:

  1. Approve the tool call and continue
  2. Modify the tool call manually and then continue
  3. Give natural language feedback, and then pass that back to the agent instead of continuing



We can implement these in LangGraph using the `interrupt()`[](https://langchain-ai.github.io/langgraphjs/reference/functions/langgraph.interrupt-1.html) function. `interrupt` allows us to stop graph execution to collect input from a user and continue execution with collected input:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-0-1)functionhumanReviewNode(state:typeofGraphAnnotation.State){
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-0-2)// this is the value we'll be providing via new Command({ resume: <human_review> })
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-0-3)consthumanReview=interrupt({
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-0-4)question:"Is this correct?",
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-0-5)// Surface tool calls for review
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-0-6)tool_call,
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-0-7)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-0-8)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-0-9)const[reviewAction,reviewData]=humanReview;
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-0-10)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-0-11)// Approve the tool call and continue
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-0-12)if(reviewAction==="continue"){
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-0-13)returnnewCommand({goto:"run_tool"});
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-0-14)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-0-15)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-0-16)// Modify the tool call manually and then continue
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-0-17)if(reviewAction==="update"){
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-0-18)constupdatedMsg=getUpdatedMsg(reviewData);
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-0-19)returnnewCommand({goto:"run_tool",update:{messages:[updatedMsg]}});
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-0-20)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-0-21)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-0-22)// Give natural language feedback, and then pass that back to the agent
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-0-23)if(reviewAction==="feedback"){
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-0-24)constfeedbackMsg=getFeedbackMsg(reviewData);
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-0-25)returnnewCommand({goto:"call_llm",update:{messages:[feedbackMsg]}});
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-0-26)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-0-27)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-0-28)thrownewError("Unreachable");
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-0-29)}

```


## Setup[¶](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#setup "Permanent link")

First we need to install the packages required

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-1-1)npminstall@langchain/langgraph@langchain/anthropic@langchain/core

```


Next, we need to set API keys for Anthropic (the LLM we will use)

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-2-1)exportANTHROPIC_API_KEY=your-api-key

```


Optionally, we can set API key for [LangSmith tracing](https://smith.langchain.com/), which will give us best-in-class observability.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-3-1)exportLANGCHAIN_TRACING_V2="true"
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-3-2)exportLANGCHAIN_CALLBACKS_BACKGROUND="true"
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-3-3)exportLANGCHAIN_API_KEY=your-api-key

```


## Simple Usage[¶](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#simple-usage "Permanent link")

Let's set up a very simple graph that facilitates this. First, we will have an LLM call that decides what action to take. Then we go to a human node. This node actually doesn't do anything - the idea is that we interrupt before this node and then apply any updates to the state. After that, we check the state and either route back to the LLM or to the correct tool.

Let's see this in action!

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-1)import{
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-2)MessagesAnnotation,
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-3)StateGraph,
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-4)START,
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-5)END,
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-6)MemorySaver,
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-7)Command,
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-8)interrupt
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-9)}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-10)import{ChatAnthropic}from"@langchain/anthropic";
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-11)import{tool}from'@langchain/core/tools';
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-12)import{z}from'zod';
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-13)import{AIMessage,ToolMessage}from'@langchain/core/messages';
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-14)import{ToolCall}from'@langchain/core/messages/tool';
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-15)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-16)constweatherSearch=tool((input:{city:string})=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-17)console.log("----");
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-18)console.log(`Searching for: ${input.city}`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-19)console.log("----");
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-20)return"Sunny!";
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-21)},{
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-22)name:'weather_search',
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-23)description:'Search for the weather',
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-24)schema:z.object({
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-25)city:z.string()
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-26)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-27)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-28)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-29)constmodel=newChatAnthropic({
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-30)model:"claude-3-5-sonnet-latest"
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-31)}).bindTools([weatherSearch]);
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-32)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-33)constcallLLM=async(state:typeofMessagesAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-34)constresponse=awaitmodel.invoke(state.messages);
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-35)return{messages:[response]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-36)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-37)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-38)consthumanReviewNode=async(state:typeofMessagesAnnotation.State):Promise<Command>=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-39)constlastMessage=state.messages[state.messages.length-1]asAIMessage;
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-40)consttoolCall=lastMessage.tool_calls![lastMessage.tool_calls!.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-41)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-42)consthumanReview=interrupt<
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-43){
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-44)question:string;
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-45)toolCall:ToolCall;
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-46)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-47){
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-48)action:string;
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-49)data:any;
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-50)}>({
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-51)question:"Is this correct?",
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-52)toolCall:toolCall
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-53)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-54)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-55)constreviewAction=humanReview.action;
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-56)constreviewData=humanReview.data;
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-57)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-58)if(reviewAction==="continue"){
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-59)returnnewCommand({goto:"run_tool"});
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-60)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-61)elseif(reviewAction==="update"){
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-62)constupdatedMessage={
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-63)role:"ai",
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-64)content:lastMessage.content,
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-65)tool_calls:[{
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-66)id:toolCall.id,
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-67)name:toolCall.name,
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-68)args:reviewData
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-69)}],
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-70)id:lastMessage.id
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-71)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-72)returnnewCommand({goto:"run_tool",update:{messages:[updatedMessage]}});
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-73)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-74)elseif(reviewAction==="feedback"){
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-75)consttoolMessage=newToolMessage({
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-76)name:toolCall.name,
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-77)content:reviewData,
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-78)tool_call_id:toolCall.id
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-79)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-80)returnnewCommand({goto:"call_llm",update:{messages:[toolMessage]}});
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-81)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-82)thrownewError("Invalid review action");
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-83)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-84)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-85)construnTool=async(state:typeofMessagesAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-86)constnewMessages:ToolMessage[]=[];
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-87)consttools={weather_search:weatherSearch};
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-88)constlastMessage=state.messages[state.messages.length-1]asAIMessage;
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-89)consttoolCalls=lastMessage.tool_calls!;
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-90)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-91)for(consttoolCalloftoolCalls){
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-92)consttool=tools[toolCall.nameaskeyoftypeoftools];
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-93)constresult=awaittool.invoke(toolCall.args);
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-94)newMessages.push(newToolMessage({
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-95)name:toolCall.name,
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-96)content:result,
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-97)tool_call_id:toolCall.id
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-98)}));
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-99)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-100)return{messages:newMessages};
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-101)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-102)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-103)constrouteAfterLLM=(state:typeofMessagesAnnotation.State):typeofEND|"human_review_node"=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-104)constlastMessage=state.messages[state.messages.length-1]asAIMessage;
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-105)if(!lastMessage.tool_calls?.length){
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-106)returnEND;
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-107)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-108)return"human_review_node";
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-109)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-110)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-111)constworkflow=newStateGraph(MessagesAnnotation)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-112).addNode("call_llm",callLLM)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-113).addNode("run_tool",runTool)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-114).addNode("human_review_node",humanReviewNode,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-115)ends:["run_tool","call_llm"]
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-116)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-117).addEdge(START,"call_llm")
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-118).addConditionalEdges(
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-119)"call_llm",
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-120)routeAfterLLM,
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-121)["human_review_node",END]
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-122))
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-123).addEdge("run_tool","call_llm");
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-124)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-125)constmemory=newMemorySaver();
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-126)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-4-127)constgraph=workflow.compile({checkpointer:memory});

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-5-1)import*astslabfrom"tslab";
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-5-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-5-3)constdrawableGraph=graph.getGraph();
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-5-4)constimage=awaitdrawableGraph.drawMermaidPng();
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-5-5)constarrayBuffer=awaitimage.arrayBuffer();
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-5-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-5-7)awaittslab.display.png(newUint8Array(arrayBuffer));

```


![]()

## Example with no review[¶](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#example-with-no-review "Permanent link")

Let's look at an example when no review is required (because no tools are called)

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-6-1)letinputs={messages:[{role:"user",content:"hi!"}]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-6-2)letconfig={configurable:{thread_id:"1"},streamMode:"values"asconst};
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-6-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-6-4)letstream=awaitgraph.stream(inputs,config);
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-6-5)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-6-6)forawait(consteventofstream){
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-6-7)constrecentMsg=event.messages[event.messages.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-6-8)console.log(`================================ ${recentMsg._getType()} Message (1) =================================`)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-6-9)console.log(recentMsg.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-6-10)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-7-1)================================ human Message (1) =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-7-2)hi!
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-7-3)================================ ai Message (1) =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-7-4)Hello! I'm here to help you. I can assist you with checking the weather for different cities. Would you like to know the weather for a specific location? Just let me know which city you're interested in and I'll look that up for you.

```


If we check the state, we can see that it is finished, since there are no next steps to take: 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-8-1)letstate=awaitgraph.getState(config);
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-8-2)console.log(state.next);

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-9-1)[]

```


## Example of approving tool[¶](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#example-of-approving-tool "Permanent link")

Let's now look at what it looks like to approve a tool call

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-10-1)inputs={messages:[{role:"user",content:"what's the weather in SF?"}]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-10-2)config={configurable:{thread_id:"2"},streamMode:"values"asconst};
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-10-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-10-4)stream=awaitgraph.stream(inputs,config);
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-10-5)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-10-6)forawait(consteventofstream){
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-10-7)constrecentMsg=event.messages[event.messages.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-10-8)console.log(`================================ ${recentMsg._getType()} Message (1) =================================`)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-10-9)console.log(recentMsg.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-10-10)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-11-1)================================ human Message (1) =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-11-2)what's the weather in SF?
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-11-3)================================ ai Message (1) =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-11-4)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-11-5) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-11-6)  type: 'text',
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-11-7)  text: 'Let me check the weather in San Francisco for you.'
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-11-8) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-11-9) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-11-10)  type: 'tool_use',
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-11-11)  id: 'toolu_01PTn9oqTP6EdFabfhfvELuy',
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-11-12)  name: 'weather_search',
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-11-13)  input: { city: 'San Francisco' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-11-14) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-11-15)]

```


If we now check, we can see that it is waiting on human review 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-12-1)state=awaitgraph.getState(config);
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-12-2)console.log(state.next);

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-13-1)[ 'human_review_node' ]

```


To approve the tool call, we can just continue the thread with no edits. To do so, we need to let `human_review_node` know what value to use for the `human_review` variable we defined inside the node. We can provide this value by invoking the graph with a `new Command({ resume: <human_review> })` input. Since we're approving the tool call, we'll provide `resume` value of `{ action: "continue" }` to navigate to `run_tool` node: 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-14-1)import{Command}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-14-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-14-3)forawait(consteventofawaitgraph.stream(
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-14-4)newCommand({resume:{action:"continue"}}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-14-5)config
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-14-6))){
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-14-7)constrecentMsg=event.messages[event.messages.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-14-8)console.log(`================================ ${recentMsg._getType()} Message (1) =================================`)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-14-9)console.log(recentMsg.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-14-10)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-15-1)================================ ai Message (1) =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-15-2)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-15-3) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-15-4)  type: 'text',
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-15-5)  text: 'Let me check the weather in San Francisco for you.'
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-15-6) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-15-7) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-15-8)  type: 'tool_use',
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-15-9)  id: 'toolu_01PTn9oqTP6EdFabfhfvELuy',
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-15-10)  name: 'weather_search',
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-15-11)  input: { city: 'San Francisco' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-15-12) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-15-13)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-15-14)----
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-15-15)Searching for: San Francisco
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-15-16)----
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-15-17)================================ tool Message (1) =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-15-18)Sunny!
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-15-19)================================ ai Message (1) =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-15-20)It's sunny in San Francisco right now!

```


## Edit Tool Call[¶](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#edit-tool-call "Permanent link")

Let's now say we want to edit the tool call. E.g. change some of the parameters (or even the tool called!) but then execute that tool.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-16-1)inputs={messages:[{role:"user",content:"what's the weather in SF?"}]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-16-2)config={configurable:{thread_id:"3"},streamMode:"values"asconst};
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-16-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-16-4)stream=awaitgraph.stream(inputs,config);
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-16-5)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-16-6)forawait(consteventofstream){
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-16-7)constrecentMsg=event.messages[event.messages.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-16-8)console.log(`================================ ${recentMsg._getType()} Message (1) =================================`)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-16-9)console.log(recentMsg.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-16-10)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-17-1)================================ human Message (1) =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-17-2)what's the weather in SF?
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-17-3)================================ ai Message (1) =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-17-4)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-17-5) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-17-6)  type: 'text',
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-17-7)  text: 'Let me check the weather in San Francisco for you.'
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-17-8) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-17-9) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-17-10)  type: 'tool_use',
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-17-11)  id: 'toolu_01T7ykQ45XyGpzRB7MkPtSAE',
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-17-12)  name: 'weather_search',
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-17-13)  input: { city: 'San Francisco' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-17-14) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-17-15)]

```


If we now check, we can see that it is waiting on human review 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-18-1)state=awaitgraph.getState(config);
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-18-2)console.log(state.next);

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-19-1)[ 'human_review_node' ]

```


To edit the tool call, we will use `Command` with a different resume value of `{ action: "update", data: <tool call args> }`. This will do the following: 

  * combine existing tool call with user-provided tool call arguments and update the existing AI message with the new tool call
  * navigate to `run_tool` node with the updated AI message and continue execution



```
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-20-1)forawait(consteventofawaitgraph.stream(
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-20-2)newCommand({
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-20-3)resume:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-20-4)action:"update",
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-20-5)data:{city:"San Francisco"}
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-20-6)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-20-7)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-20-8)config
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-20-9))){
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-20-10)constrecentMsg=event.messages[event.messages.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-20-11)console.log(`================================ ${recentMsg._getType()} Message (1) =================================`)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-20-12)console.log(recentMsg.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-20-13)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-21-1)================================ ai Message (1) =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-21-2)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-21-3) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-21-4)  type: 'text',
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-21-5)  text: 'Let me check the weather in San Francisco for you.'
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-21-6) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-21-7) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-21-8)  type: 'tool_use',
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-21-9)  id: 'toolu_01T7ykQ45XyGpzRB7MkPtSAE',
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-21-10)  name: 'weather_search',
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-21-11)  input: { city: 'San Francisco' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-21-12) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-21-13)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-21-14)================================ ai Message (1) =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-21-15)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-21-16) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-21-17)  type: 'text',
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-21-18)  text: 'Let me check the weather in San Francisco for you.'
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-21-19) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-21-20) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-21-21)  type: 'tool_use',
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-21-22)  id: 'toolu_01T7ykQ45XyGpzRB7MkPtSAE',
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-21-23)  name: 'weather_search',
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-21-24)  input: { city: 'San Francisco' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-21-25) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-21-26)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-21-27)----
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-21-28)Searching for: San Francisco
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-21-29)----
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-21-30)================================ tool Message (1) =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-21-31)Sunny!
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-21-32)================================ ai Message (1) =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-21-33)It's sunny in San Francisco right now!

```


## Give feedback to a tool call[¶](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#give-feedback-to-a-tool-call "Permanent link")

Sometimes, you may not want to execute a tool call, but you also may not want to ask the user to manually modify the tool call. In that case it may be better to get natural language feedback from the user. You can then insert these feedback as a mock **RESULT** of the tool call.

There are multiple ways to do this:

  1. You could add a new message to the state (representing the "result" of a tool call)
  2. You could add TWO new messages to the state - one representing an "error" from the tool call, other HumanMessage representing the feedback



Both are similar in that they involve adding messages to the state. The main difference lies in the logic AFTER the `human_node` and how it handles different types of messages.

For this example we will just add a single tool call representing the feedback. Let's see this in action!

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-22-1)inputs={messages:[{role:"user",content:"what's the weather in SF?"}]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-22-2)config={configurable:{thread_id:"4"},streamMode:"values"asconst};
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-22-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-22-4)stream=awaitgraph.stream(inputs,config);
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-22-5)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-22-6)forawait(consteventofstream){
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-22-7)constrecentMsg=event.messages[event.messages.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-22-8)console.log(`================================ ${recentMsg._getType()} Message (1) =================================`)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-22-9)console.log(recentMsg.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-22-10)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-23-1)================================ human Message (1) =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-23-2)what's the weather in SF?
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-23-3)================================ ai Message (1) =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-23-4)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-23-5) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-23-6)  type: 'text',
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-23-7)  text: "I'll help you check the weather in San Francisco."
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-23-8) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-23-9) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-23-10)  type: 'tool_use',
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-23-11)  id: 'toolu_014cwxD65wDwQdNg6xqsticF',
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-23-12)  name: 'weather_search',
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-23-13)  input: { city: 'SF' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-23-14) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-23-15)]

```


If we now check, we can see that it is waiting on human review 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-24-1)state=awaitgraph.getState(config);
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-24-2)console.log(state.next);

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-25-1)[ 'human_review_node' ]

```


To give feedback about the tool call, we will use `Command` with a different resume value of `{ action: "feedback", data: <feedback string> }`. This will do the following: 

  * create a new tool message that combines existing tool call from LLM with the with user-provided feedback as content
  * navigate to `call_llm` node with the updated tool message and continue execution



```
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-26-1)forawait(consteventofawaitgraph.stream(
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-26-2)newCommand({
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-26-3)resume:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-26-4)action:"feedback",
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-26-5)data:"User requested changes: use <city, country> format for location"
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-26-6)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-26-7)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-26-8)config
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-26-9))){
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-26-10)constrecentMsg=event.messages[event.messages.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-26-11)console.log(`================================ ${recentMsg._getType()} Message (1) =================================`)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-26-12)console.log(recentMsg.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-26-13)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-27-1)================================ ai Message (1) =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-27-2)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-27-3) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-27-4)  type: 'text',
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-27-5)  text: "I'll help you check the weather in San Francisco."
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-27-6) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-27-7) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-27-8)  type: 'tool_use',
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-27-9)  id: 'toolu_014cwxD65wDwQdNg6xqsticF',
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-27-10)  name: 'weather_search',
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-27-11)  input: { city: 'SF' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-27-12) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-27-13)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-27-14)================================ tool Message (1) =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-27-15)User requested changes: use <city, country> format for location
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-27-16)================================ ai Message (1) =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-27-17)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-27-18) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-27-19)  type: 'text',
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-27-20)  text: 'I apologize for the error. Let me search again with the proper format.'
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-27-21) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-27-22) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-27-23)  type: 'tool_use',
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-27-24)  id: 'toolu_01Jnm7sSZsiwv65YM4KsvfXk',
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-27-25)  name: 'weather_search',
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-27-26)  input: { city: 'San Francisco, USA' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-27-27) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-27-28)]

```


We can see that we now get to another breakpoint - because it went back to the model and got an entirely new prediction of what to call. Let's now approve this one and continue. 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-28-1)state=awaitgraph.getState(config);
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-28-2)console.log(state.next);

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-29-1)[ 'human_review_node' ]

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-30-1)forawait(consteventofawaitgraph.stream(
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-30-2)newCommand({
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-30-3)resume:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-30-4)action:"continue",
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-30-5)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-30-6)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-30-7)config
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-30-8))){
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-30-9)constrecentMsg=event.messages[event.messages.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-30-10)console.log(`================================ ${recentMsg._getType()} Message (1) =================================`)
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-30-11)console.log(recentMsg.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-30-12)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-31-1)================================ ai Message (1) =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-31-2)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-31-3) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-31-4)  type: 'text',
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-31-5)  text: 'I apologize for the error. Let me search again with the proper format.'
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-31-6) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-31-7) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-31-8)  type: 'tool_use',
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-31-9)  id: 'toolu_01Jnm7sSZsiwv65YM4KsvfXk',
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-31-10)  name: 'weather_search',
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-31-11)  input: { city: 'San Francisco, USA' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-31-12) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-31-13)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-31-14)----
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-31-15)Searching for: San Francisco, USA
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-31-16)----
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-31-17)================================ tool Message (1) =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-31-18)Sunny!
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-31-19)================================ ai Message (1) =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__codelineno-31-20)The weather in San Francisco is currently sunny!

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to view and update past graph state  ](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/) [ Next  How to review tool calls (Functional API)  ](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
