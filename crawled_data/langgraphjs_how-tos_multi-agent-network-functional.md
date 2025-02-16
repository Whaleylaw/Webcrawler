---
url: https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#how-to-build-a-multi-agent-network-functional-api)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to build a multi-agent network (functional API) 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/?q= "Share")

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
          * Multi-agent  Multi-agent 
            * [ How to build a multi-agent network  ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/)
            * How to build a multi-agent network (functional API)  [ How to build a multi-agent network (functional API)  ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#setup)
              * [ Travel agent example  ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#travel-agent-example)
            * [ How to add multi-turn conversation in a multi-agent application  ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/)
            * [ How to add multi-turn conversation in a multi-agent application (functional API)  ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#setup)
  * [ Travel agent example  ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#travel-agent-example)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
  5. [ Multi-agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/)



# How to build a multi-agent network (functional API)[¶](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#how-to-build-a-multi-agent-network-functional-api "Permanent link")

Prerequisites

This guide assumes familiarity with the following:

  * [Multi-agent systems](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent)
  * [Functional API](https://langchain-ai.github.io/langgraphjs/concepts/functional_api)
  * [Command](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#command)
  * [LangGraph Glossary](https://langchain-ai.github.io/langgraphjs/concepts/low_level/)



In this how-to guide we will demonstrate how to implement a [multi-agent network](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent#network) architecture where each agent can communicate with every other agent (many-to-many connections) and can decide which agent to call next. We will be using LangGraph's [functional API](https://langchain-ai.github.io/langgraphjs/concepts/functional_api) — individual agents will be defined as tasks and the agent handoffs will be defined in the main [entrypoint()](https://langchain-ai.github.io/langgraphjs/reference/functions/langgraph.entrypoint-1.html):

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-0-1)import{entrypoint,task}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-0-2)import{createReactAgent}from"@langchain/langgraph/prebuilt";
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-0-3)import{tool}from"@langchain/core/tools";
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-0-4)import{z}from"zod";
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-0-5)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-0-6)// Define a tool to signal intent to hand off to a different agent
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-0-7)consttransferToHotelAdvisor=tool(async()=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-0-8)return"Successfully transferred to hotel advisor";
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-0-9)},{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-0-10)name:"transferToHotelAdvisor",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-0-11)description:"Ask hotel advisor agent for help.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-0-12)schema:z.object({}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-0-13)returnDirect:true,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-0-14)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-0-15)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-0-16)// define an agent
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-0-17)consttravelAdvisorTools=[transferToHotelAdvisor,...];
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-0-18)consttravelAdvisor=createReactAgent({
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-0-19)llm:model,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-0-20)tools:travelAdvisorTools,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-0-21)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-0-22)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-0-23)// define a task that calls an agent
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-0-24)constcallTravelAdvisor=task("callTravelAdvisor",async(messages:BaseMessage[])=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-0-25)constresponse=travelAdvisor.invoke({messages});
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-0-26)returnresponse.messages;
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-0-27)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-0-28)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-0-29)constnetworkGraph=entrypoint(
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-0-30){name:"networkGraph"},
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-0-31)async(messages:BaseMessageLike[])=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-0-32)letcallActiveAgent=callTravelAdvisor;
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-0-33)letagentMessages;
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-0-34)while(true){
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-0-35)agentMessages=awaitcallActiveAgent(messages);
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-0-36)messages=addMessages(messages,agentMessages);
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-0-37)callActiveAgent=getNextAgent(messages);
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-0-38)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-0-39)returnmessages;
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-0-40)});

```


## Setup[¶](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#setup "Permanent link")

Note

This guide requires `@langchain/langgraph>=0.2.42`.

First, install the required dependencies for this example:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-1-1)npminstall@langchain/langgraph@langchain/anthropic@langchain/corezod

```


Next, we need to set API keys for Anthropic (the LLM we will use):

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-2-1)process.env.ANTHROPIC_API_KEY="YOUR_API_KEY";

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com)

## Travel agent example[¶](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#travel-agent-example "Permanent link")

In this example we will build a team of travel assistant agents that can communicate with each other.

We will create 2 agents:

  * `travelAdvisor`: can help with travel destination recommendations. Can ask `hotelAdvisor` for help.
  * `hotelAdvisor`: can help with hotel recommendations. Can ask `travelAdvisor` for help.



This is a fully-connected network - every agent can talk to any other agent. 

First, let's create some of the tools that the agents will be using:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-3-1)import{tool}from"@langchain/core/tools";
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-3-2)import{z}from"zod";
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-3-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-3-4)// Tool for getting travel recommendations
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-3-5)constgetTravelRecommendations=tool(async()=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-3-6)constdestinations=["aruba","turks and caicos"];
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-3-7)returndestinations[Math.floor(Math.random()*destinations.length)];
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-3-8)},{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-3-9)name:"getTravelRecommendations",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-3-10)description:"Get recommendation for travel destinations",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-3-11)schema:z.object({}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-3-12)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-3-13)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-3-14)// Tool for getting hotel recommendations
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-3-15)constgetHotelRecommendations=tool(async(input:{location:"aruba"|"turks and caicos"})=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-3-16)constrecommendations={
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-3-17)"aruba":[
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-3-18)"The Ritz-Carlton, Aruba (Palm Beach)",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-3-19)"Bucuti & Tara Beach Resort (Eagle Beach)"
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-3-20)],
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-3-21)"turks and caicos":["Grace Bay Club","COMO Parrot Cay"]
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-3-22)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-3-23)returnrecommendations[input.location];
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-3-24)},{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-3-25)name:"getHotelRecommendations",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-3-26)description:"Get hotel recommendations for a given destination.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-3-27)schema:z.object({
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-3-28)location:z.enum(["aruba","turks and caicos"])
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-3-29)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-3-30)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-3-31)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-3-32)// Define a tool to signal intent to hand off to a different agent
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-3-33)// Note: this is not using Command(goto) syntax for navigating to different agents:
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-3-34)// `workflow()` below handles the handoffs explicitly
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-3-35)consttransferToHotelAdvisor=tool(async()=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-3-36)return"Successfully transferred to hotel advisor";
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-3-37)},{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-3-38)name:"transferToHotelAdvisor",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-3-39)description:"Ask hotel advisor agent for help.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-3-40)schema:z.object({}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-3-41)// Hint to our agent implementation that it should stop
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-3-42)// immediately after invoking this tool 
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-3-43)returnDirect:true,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-3-44)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-3-45)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-3-46)consttransferToTravelAdvisor=tool(async()=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-3-47)return"Successfully transferred to travel advisor";
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-3-48)},{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-3-49)name:"transferToTravelAdvisor",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-3-50)description:"Ask travel advisor agent for help.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-3-51)schema:z.object({}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-3-52)// Hint to our agent implementation that it should stop
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-3-53)// immediately after invoking this tool
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-3-54)returnDirect:true,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-3-55)});

```


Transfer tools

You might have noticed that we're using `tool(... { returnDirect: true })` in the transfer tools. This is done so that individual agents (e.g., `travelAdvisor`) can exit the ReAct loop early once these tools are called without calling the model a final time to process the result of the tool call. This is the desired behavior, as we want to detect when the agent calls this tool and hand control off _immediately_ to a different agent.

**NOTE** : This is meant to work with the prebuilt `createReactAgent`[](https://langchain-ai.github.io/langgraphjs/reference/functions/langgraph_prebuilt.createReactAgent.html) - if you are building a custom agent, make sure to manually add logic for handling early exit for tools that are marked with `returnDirect`.

Now let's define our agent tasks and combine them into a single multi-agent network workflow:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-1)import{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-2)AIMessage,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-3)typeBaseMessageLike
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-4)}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-5)import{ChatAnthropic}from"@langchain/anthropic";
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-6)import{createReactAgent}from"@langchain/langgraph/prebuilt";
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-7)import{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-8)addMessages,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-9)entrypoint,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-10)task,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-11)}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-12)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-13)constmodel=newChatAnthropic({
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-14)model:"claude-3-5-sonnet-latest",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-15)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-16)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-17)consttravelAdvisorTools=[
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-18)getTravelRecommendations,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-19)transferToHotelAdvisor,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-20)];
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-21)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-22)// Define travel advisor ReAct agent
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-23)consttravelAdvisor=createReactAgent({
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-24)llm:model,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-25)tools:travelAdvisorTools,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-26)stateModifier:[
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-27)"You are a general travel expert that can recommend travel destinations (e.g. countries, cities, etc).",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-28)"If you need hotel recommendations, ask 'hotel_advisor' for help.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-29)"You MUST include human-readable response before transferring to another agent.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-30)].join(" "),
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-31)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-32)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-33)// You can also add additional logic like changing the input to the agent / output from the agent, etc.
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-34)// NOTE: we're invoking the ReAct agent with the full history of messages in the state
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-35)constcallTravelAdvisor=task("callTravelAdvisor",async(messages:BaseMessageLike[])=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-36)constresponse=awaittravelAdvisor.invoke({messages});
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-37)returnresponse.messages;
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-38)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-39)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-40)consthotelAdvisorTools=[
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-41)getHotelRecommendations,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-42)transferToTravelAdvisor,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-43)];
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-44)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-45)// Define hotel advisor ReAct agent
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-46)consthotelAdvisor=createReactAgent({
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-47)llm:model,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-48)tools:hotelAdvisorTools,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-49)stateModifier:[
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-50)"You are a hotel expert that can provide hotel recommendations for a given destination.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-51)"If you need help picking travel destinations, ask 'travel_advisor' for help.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-52)"You MUST include a human-readable response before transferring to another agent."
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-53)].join(" "),
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-54)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-55)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-56)// Add task for hotel advisor
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-57)constcallHotelAdvisor=task("callHotelAdvisor",async(messages:BaseMessageLike[])=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-58)constresponse=awaithotelAdvisor.invoke({messages});
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-59)returnresponse.messages;
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-60)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-61)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-62)constnetworkGraph=entrypoint(
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-63)"networkGraph",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-64)async(messages:BaseMessageLike[])=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-65)// Converts inputs to LangChain messages as a side-effect
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-66)letcurrentMessages=addMessages([],messages);
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-67)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-68)letcallActiveAgent=callTravelAdvisor;
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-69)while(true){
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-70)constagentMessages=awaitcallActiveAgent(currentMessages);
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-71)currentMessages=addMessages(currentMessages,agentMessages);
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-72)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-73)// Find the last AI message
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-74)// If one of the handoff tools is called, the last message returned
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-75)// by the agent will be a ToolMessage because we set them to have
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-76)// "returnDirect: true". This means that the last AIMessage will
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-77)// have tool calls.
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-78)// Otherwise, the last returned message will be an AIMessage with
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-79)// no tool calls, which means we are ready for new input.
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-80)constaiMsg=[...agentMessages].reverse()
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-81).find((m):misAIMessage=>m.getType()==="ai");
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-82)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-83)// If no tool calls, we're done
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-84)if(!aiMsg?.tool_calls?.length){
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-85)break;
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-86)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-87)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-88)// Get the last tool call and determine next agent
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-89)consttoolCall=aiMsg.tool_calls.at(-1)!;
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-90)if(toolCall.name==="transferToTravelAdvisor"){
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-91)callActiveAgent=callTravelAdvisor;
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-92)}elseif(toolCall.name==="transferToHotelAdvisor"){
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-93)callActiveAgent=callHotelAdvisor;
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-94)}else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-95)thrownewError(`Expected transfer tool, got '${toolCall.name}'`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-96)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-97)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-98)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-99)returnmessages;
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-4-100)});

```


Lastly, let's define a helper to render the agent outputs:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-5-1)constprettyPrintMessages=(update:Record<string,any>)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-5-2)// Handle tuple case with namespace
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-5-3)if(Array.isArray(update)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-5-4)const[ns,updateData]=update;
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-5-5)// Skip parent graph updates in the printouts
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-5-6)if(ns.length===0){
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-5-7)return;
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-5-8)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-5-9)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-5-10)constgraphId=ns[ns.length-1].split(":")[0];
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-5-11)console.log(`Update from subgraph ${graphId}:\n`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-5-12)update=updateData;
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-5-13)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-5-14)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-5-15)if(update.__metadata__?.cached){
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-5-16)return;
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-5-17)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-5-18)// Print updates for each node
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-5-19)for(const[nodeName,updateValue]ofObject.entries(update)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-5-20)console.log(`Update from node ${nodeName}:\n`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-5-21)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-5-22)constcoercedMessages=addMessages([],updateValue.messages);
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-5-23)for(constmessageofcoercedMessages){
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-5-24)consttextContent=typeofmessage.content==="string"
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-5-25)?message.content
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-5-26):JSON.stringify(message.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-5-27)// Print message content based on role
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-5-28)if(message.getType()==="ai"){
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-5-29)console.log("=".repeat(33)+" Assistant Message "+"=".repeat(33));
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-5-30)console.log(textContent);
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-5-31)console.log();
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-5-32)}elseif(message.getType()==="human"){
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-5-33)console.log("=".repeat(33)+" Human Message "+"=".repeat(33));
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-5-34)console.log(textContent);
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-5-35)console.log();
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-5-36)}elseif(message.getType()==="tool"){
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-5-37)console.log("=".repeat(33)+" Tool Message "+"=".repeat(33));
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-5-38)console.log(textContent);
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-5-39)console.log();
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-5-40)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-5-41)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-5-42)console.log("\n");
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-5-43)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-5-44)};

```


Let's test it out:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-6-1)conststream=awaitnetworkGraph.stream([{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-6-2)role:"user",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-6-3)content:"i wanna go somewhere warm in the caribbean. pick one destination and give me hotel recommendations"
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-6-4)}],{subgraphs:true})
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-6-5)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-6-6)forawait(constchunkofstream){
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-6-7)prettyPrintMessages(chunk);
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-6-8)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-1)Update from subgraph callTravelAdvisor:
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-3)Update from node agent:
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-4)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-5)================================= Assistant Message =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-6)[{"type":"text","text":"I'll help you find a warm Caribbean destination and then get specific hotel recommendations for you.\n\nLet me first get some destination recommendations for the Caribbean region."},{"type":"tool_use","id":"toolu_019fN1etkqtCSausSv8XufhL","name":"getTravelRecommendations","input":{}}]
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-7)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-8)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-9)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-10)Update from subgraph callTravelAdvisor:
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-11)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-12)Update from node tools:
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-13)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-14)================================= Tool Message =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-15)turks and caicos
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-16)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-17)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-18)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-19)Update from subgraph callTravelAdvisor:
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-20)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-21)Update from node agent:
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-22)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-23)================================= Assistant Message =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-24)[{"type":"text","text":"Great! I recommend Turks and Caicos for your Caribbean getaway. This beautiful British Overseas Territory is known for its stunning white-sand beaches, crystal-clear turquoise waters, and perfect warm weather year-round. Grace Bay Beach in Providenciales (often called \"Provo\") is consistently ranked among the world's best beaches. The islands offer excellent snorkeling, diving, and water sports opportunities, plus a relaxed Caribbean atmosphere.\n\nNow, let me connect you with our hotel advisor to get specific accommodation recommendations for Turks and Caicos."},{"type":"tool_use","id":"toolu_01UHAnBBK9zm2nAEh7brR7TY","name":"transferToHotelAdvisor","input":{}}]
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-25)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-26)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-27)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-28)Update from subgraph callTravelAdvisor:
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-29)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-30)Update from node tools:
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-31)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-32)================================= Tool Message =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-33)Successfully transferred to hotel advisor
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-34)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-35)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-36)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-37)Update from subgraph callHotelAdvisor:
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-38)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-39)Update from node agent:
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-40)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-41)================================= Assistant Message =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-42)[{"type":"text","text":"Let me get some hotel recommendations for Turks and Caicos:"},{"type":"tool_use","id":"toolu_012GUHBGXxyzwE5dY6nePq9s","name":"getHotelRecommendations","input":{"location":"turks and caicos"}}]
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-43)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-44)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-45)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-46)Update from subgraph callHotelAdvisor:
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-47)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-48)Update from node tools:
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-49)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-50)================================= Tool Message =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-51)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-52) "Grace Bay Club",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-53) "COMO Parrot Cay"
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-54)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-55)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-56)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-57)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-58)Update from subgraph callHotelAdvisor:
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-59)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-60)Update from node agent:
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-61)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-62)================================= Assistant Message =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-63)Based on the recommendations, here are two excellent options in Turks and Caicos:
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-64)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-65)1. Grace Bay Club: This luxurious resort is located on the world-famous Grace Bay Beach. It offers all-oceanfront suites, exceptional dining options, and top-notch amenities including multiple pools, a spa, and various water sports activities. The resort is perfect for both couples and families, with adult-only and family-friendly sections.
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-66)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-67)2. COMO Parrot Cay: This exclusive private island resort offers the ultimate luxury experience. Located on its own island, it features pristine beaches, world-class spa treatments, and exceptional dining. The resort is known for its privacy, making it a favorite among celebrities. The rooms and villas offer sophisticated design with private pools and direct beach access.
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-68)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__codelineno-7-69)Would you like more specific information about either of these properties or shall I search for additional options?

```


Voila - `travelAdvisor` picks a destination and then makes a decision to call `hotelAdvisor` for more info!  Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to build a multi-agent network  ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/) [ Next  How to add multi-turn conversation in a multi-agent application  ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
