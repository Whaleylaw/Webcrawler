---
url: https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#how-to-add-multi-turn-conversation-in-a-multi-agent-application-functional-api)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to add multi-turn conversation in a multi-agent application (functional API) 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/?q= "Share")

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
            * [ How to build a multi-agent network (functional API)  ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/)
            * [ How to add multi-turn conversation in a multi-agent application  ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/)
            * How to add multi-turn conversation in a multi-agent application (functional API)  [ How to add multi-turn conversation in a multi-agent application (functional API)  ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#setup)
              * [ Test multi-turn conversation  ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#test-multi-turn-conversation)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#setup)
  * [ Test multi-turn conversation  ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#test-multi-turn-conversation)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
  5. [ Multi-agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/)



# How to add multi-turn conversation in a multi-agent application (functional API)[¶](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#how-to-add-multi-turn-conversation-in-a-multi-agent-application-functional-api "Permanent link")

Prerequisites

This guide assumes familiarity with the following:

  * [Multi-agent systems](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent)
  * [Human-in-the-loop](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop)
  * [Functional API](https://langchain-ai.github.io/langgraphjs/concepts/functional_api)
  * [Command](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#command)
  * [LangGraph Glossary](https://langchain-ai.github.io/langgraphjs/concepts/low_level/)



In this how-to guide, we’ll build an application that allows an end-user to engage in a _multi-turn conversation_ with one or more agents. We'll create a node that uses an `interrupt`[](https://langchain-ai.github.io/langgraphjs/reference/functions/langgraph.interrupt-1.html) to collect user input and routes back to the **active** agent.

The agents will be implemented as tasks in a workflow that executes agent steps and determines the next action:

  1. **Wait for user input** to continue the conversation, or
  2. **Route to another agent** (or back to itself, such as in a loop) via a [**handoff**](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#handoffs).



Note

This guide requires `@langchain/langgraph>=0.2.42` and `@langchain/core>=0.3.36`.

## Setup[¶](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#setup "Permanent link")

First, install the required dependencies for this example:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-0-1)npminstall@langchain/langgraph@langchain/anthropic@langchain/coreuuidzod

```


Next, we need to set API keys for Anthropic (the LLM we will use):

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-1-1)process.env.ANTHROPIC_API_KEY="YOUR_API_KEY";

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com)

In this example we will build a team of travel assistant agents that can communicate with each other.

We will create 2 agents:

  * `travelAdvisor`: can help with travel destination recommendations. Can ask `hotelAdvisor` for help.
  * `hotelAdvisor`: can help with hotel recommendations. Can ask `travelAdvisor` for help.



This is a fully-connected network - every agent can talk to any other agent. 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-1)import{tool}from"@langchain/core/tools";
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-2)import{z}from"zod";
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-4)// Tool for getting travel recommendations
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-5)constgetTravelRecommendations=tool(async()=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-6)constdestinations=["aruba","turks and caicos"];
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-7)returndestinations[Math.floor(Math.random()*destinations.length)];
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-8)},{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-9)name:"getTravelRecommendations",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-10)description:"Get recommendation for travel destinations",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-11)schema:z.object({}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-12)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-13)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-14)// Tool for getting hotel recommendations
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-15)constgetHotelRecommendations=tool(async(input:{location:"aruba"|"turks and caicos"})=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-16)constrecommendations={
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-17)"aruba":[
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-18)"The Ritz-Carlton, Aruba (Palm Beach)",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-19)"Bucuti & Tara Beach Resort (Eagle Beach)"
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-20)],
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-21)"turks and caicos":["Grace Bay Club","COMO Parrot Cay"]
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-22)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-23)returnrecommendations[input.location];
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-24)},{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-25)name:"getHotelRecommendations",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-26)description:"Get hotel recommendations for a given destination.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-27)schema:z.object({
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-28)location:z.enum(["aruba","turks and caicos"])
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-29)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-30)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-31)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-32)// Define a tool to signal intent to hand off to a different agent
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-33)// Note: this is not using Command(goto) syntax for navigating to different agents:
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-34)// `workflow()` below handles the handoffs explicitly
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-35)consttransferToHotelAdvisor=tool(async()=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-36)return"Successfully transferred to hotel advisor";
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-37)},{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-38)name:"transferToHotelAdvisor",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-39)description:"Ask hotel advisor agent for help.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-40)schema:z.object({}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-41)// Hint to our agent implementation that it should stop
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-42)// immediately after invoking this tool 
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-43)returnDirect:true,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-44)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-45)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-46)consttransferToTravelAdvisor=tool(async()=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-47)return"Successfully transferred to travel advisor";
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-48)},{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-49)name:"transferToTravelAdvisor",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-50)description:"Ask travel advisor agent for help.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-51)schema:z.object({}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-52)// Hint to our agent implementation that it should stop
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-53)// immediately after invoking this tool
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-54)returnDirect:true,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-55)});

```


Transfer tools

You might have noticed that we're using `tool(... { returnDirect: true })` in the transfer tools. This is done so that individual agents (e.g., `travelAdvisor`) can exit the ReAct loop early once these tools are called without calling the model a final time to process the result of the tool call. This is the desired behavior, as we want to detect when the agent calls this tool and hand control off _immediately_ to a different agent.

**NOTE** : This is meant to work with the prebuilt `createReactAgent`[](https://langchain-ai.github.io/langgraphjs/reference/functions/langgraph_prebuilt.createReactAgent.html) - if you are building a custom agent, make sure to manually add logic for handling early exit for tools that are marked with `returnDirect`.

Let's now create our agents using the the prebuilt `createReactAgent`[](https://langchain-ai.github.io/langgraphjs/reference/functions/langgraph_prebuilt.createReactAgent.html) and our multi-agent workflow. Note that will be calling `interrupt`[](https://langchain-ai.github.io/langgraphjs/reference/functions/langgraph.interrupt-1.html) every time after we get the final response from each of the agents.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-1)import{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-2)AIMessage,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-3)typeBaseMessage,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-4)typeBaseMessageLike
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-5)}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-6)import{ChatAnthropic}from"@langchain/anthropic";
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-7)import{createReactAgent}from"@langchain/langgraph/prebuilt";
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-8)import{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-9)addMessages,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-10)entrypoint,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-11)task,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-12)MemorySaver,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-13)interrupt,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-14)}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-15)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-16)constmodel=newChatAnthropic({
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-17)model:"claude-3-5-sonnet-latest",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-18)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-19)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-20)consttravelAdvisorTools=[
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-21)getTravelRecommendations,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-22)transferToHotelAdvisor,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-23)];
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-24)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-25)// Define travel advisor ReAct agent
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-26)consttravelAdvisor=createReactAgent({
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-27)llm:model,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-28)tools:travelAdvisorTools,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-29)stateModifier:[
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-30)"You are a general travel expert that can recommend travel destinations (e.g. countries, cities, etc).",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-31)"If you need hotel recommendations, ask 'hotel_advisor' for help.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-32)"You MUST include human-readable response before transferring to another agent.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-33)].join(" "),
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-34)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-35)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-36)// You can also add additional logic like changing the input to the agent / output from the agent, etc.
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-37)// NOTE: we're invoking the ReAct agent with the full history of messages in the state
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-38)constcallTravelAdvisor=task("callTravelAdvisor",async(messages:BaseMessageLike[])=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-39)constresponse=awaittravelAdvisor.invoke({messages});
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-40)returnresponse.messages;
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-41)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-42)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-43)consthotelAdvisorTools=[
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-44)getHotelRecommendations,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-45)transferToTravelAdvisor,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-46)];
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-47)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-48)// Define hotel advisor ReAct agent
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-49)consthotelAdvisor=createReactAgent({
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-50)llm:model,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-51)tools:hotelAdvisorTools,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-52)stateModifier:[
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-53)"You are a hotel expert that can provide hotel recommendations for a given destination.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-54)"If you need help picking travel destinations, ask 'travel_advisor' for help.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-55)"You MUST include a human-readable response before transferring to another agent."
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-56)].join(" "),
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-57)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-58)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-59)// Add task for hotel advisor
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-60)constcallHotelAdvisor=task("callHotelAdvisor",async(messages:BaseMessageLike[])=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-61)constresponse=awaithotelAdvisor.invoke({messages});
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-62)returnresponse.messages;
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-63)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-64)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-65)constcheckpointer=newMemorySaver();
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-66)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-67)constmultiTurnGraph=entrypoint({
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-68)name:"multiTurnGraph",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-69)checkpointer,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-70)},async(messages:BaseMessageLike[])=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-71)letcallActiveAgent=callTravelAdvisor;
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-72)letagentMessages:BaseMessage[];
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-73)letcurrentMessages=messages;
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-74)while(true){
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-75)agentMessages=awaitcallActiveAgent(currentMessages);
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-76)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-77)// Find the last AI message
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-78)// If one of the handoff tools is called, the last message returned
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-79)// by the agent will be a ToolMessages because we set them to have
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-80)// "returnDirect: true". This means that the last AIMessage will
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-81)// have tool calls.
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-82)// Otherwise, the last returned message will be an AIMessage with
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-83)// no tool calls, which means we are ready for new input.
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-84)constreversedMessages=[...agentMessages].reverse();
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-85)constaiMsgIndex=reversedMessages
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-86).findIndex((m):misAIMessage=>m.getType()==="ai");
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-87)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-88)constaiMsg:AIMessage=reversedMessages[aiMsgIndex];
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-89)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-90)// We append all messages up to the last AI message to the current messages.
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-91)// This may include ToolMessages (if the handoff tool was called)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-92)constmessagesToAdd=reversedMessages.slice(0,aiMsgIndex+1).reverse();
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-93)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-94)// Add the agent's responses
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-95)currentMessages=addMessages(currentMessages,messagesToAdd);
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-96)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-97)if(!aiMsg?.tool_calls?.length){
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-98)constuserInput=awaitinterrupt("Ready for user input.");
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-99)if(typeofuserInput!=="string"){
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-100)thrownewError("User input must be a string.");
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-101)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-102)if(userInput.toLowerCase()==="done"){
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-103)break;
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-104)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-105)currentMessages=addMessages(currentMessages,[{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-106)role:"human",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-107)content:userInput,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-108)}]);
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-109)continue;
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-110)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-111)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-112)consttoolCall=aiMsg.tool_calls.at(-1)!;
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-113)if(toolCall.name==="transferToHotelAdvisor"){
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-114)callActiveAgent=callHotelAdvisor;
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-115)}elseif(toolCall.name==="transferToTravelAdvisor"){
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-116)callActiveAgent=callTravelAdvisor;
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-117)}else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-118)thrownewError(`Expected transfer tool, got '${toolCall.name}'`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-119)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-120)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-121)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-122)returnentrypoint.final({
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-123)value:agentMessages[agentMessages.length-1],
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-124)save:currentMessages,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-125)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-126)});

```


We use a while loop to enable continuous conversation between agents and the user. The loop allows for:

  1. Getting agent responses
  2. Handling agent-to-agent transfers
  3. Collecting user input via interrupts
  4. Resuming using special inputs (see `Command` below)



## Test multi-turn conversation[¶](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#test-multi-turn-conversation "Permanent link")

Let's test a multi turn conversation with this application.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-1)import{v4asuuidv4}from'uuid';
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-2)import{Command}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-3)import{isBaseMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-4)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-5)constthreadConfig={
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-6)configurable:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-7)thread_id:uuidv4()
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-8)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-9)streamMode:"updates"asconst,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-10)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-11)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-12)constinputs=[
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-13)// 1st round of conversation
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-14)[{role:"user",content:"i wanna go somewhere warm in the caribbean"}],
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-15)// Since we're using `interrupt`, we'll need to resume using the Command primitive
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-16)// 2nd round of conversation
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-17)newCommand({
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-18)resume:"could you recommend a nice hotel in one of the areas and tell me which area it is."
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-19)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-20)// 3rd round of conversation
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-21)newCommand({
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-22)resume:"i like the first one. could you recommend something to do near the hotel?"
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-23)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-24)];
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-25)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-26)construnConversation=async()=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-27)for(const[idx,userInput]ofinputs.entries()){
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-28)console.log();
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-29)console.log(`--- Conversation Turn ${idx+1} ---`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-30)console.log();
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-31)console.log(`User: ${JSON.stringify(userInput,null,2)}`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-32)console.log();
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-33)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-34)conststream=awaitmultiTurnGraph.stream(
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-35)userInputasany,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-36)threadConfig,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-37));
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-38)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-39)forawait(constupdateofstream){
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-40)if(update.__metadata__?.cached){
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-41)continue;
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-42)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-43)for(const[nodeId,value]ofObject.entries(update)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-44)if(Array.isArray(value)&&value.length>0){
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-45)constlastMessage=value.at(-1);
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-46)if(isBaseMessage(lastMessage)&&lastMessage?.getType()==="ai"){
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-47)console.log(`${nodeId}: ${lastMessage.content}`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-48)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-49)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-50)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-51)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-52)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-53)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-54)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-55)// Execute the conversation
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-56)try{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-57)awaitrunConversation();
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-58)}catch(e){
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-59)console.error(e);
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-60)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-1)--- Conversation Turn 1 ---
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-3)User: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-4) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-5)  "role": "user",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-6)  "content": "i wanna go somewhere warm in the caribbean"
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-7) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-8)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-9)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-10)callTravelAdvisor: Based on the recommendations, Turks and Caicos would be an excellent choice for your Caribbean getaway! This British Overseas Territory is known for its stunning white-sand beaches, crystal-clear turquoise waters, and year-round warm weather. Grace Bay Beach in Providenciales is consistently rated as one of the world's best beaches.
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-11)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-12)You can enjoy:
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-13)- World-class snorkeling and diving
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-14)- Luxury resorts and spas
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-15)- Fresh seafood cuisine
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-16)- Water sports like kayaking and paddleboarding
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-17)- Beautiful coral reefs
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-18)- Average temperatures between 75-85°F (24-29°C) year-round
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-19)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-20)Would you like me to connect you with our hotel advisor to help you find the perfect place to stay in Turks and Caicos?
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-21)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-22)--- Conversation Turn 2 ---
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-23)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-24)User: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-25) "resume": "could you recommend a nice hotel in one of the areas and tell me which area it is.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-26) "goto": []
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-27)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-28)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-29)callHotelAdvisor: I can recommend two excellent options in Turks and Caicos:
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-30)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-31)1. Grace Bay Club - This luxury resort is located on the world-famous Grace Bay Beach in Providenciales (often called "Provo"). This area is the most developed and popular island in Turks and Caicos, known for its 12-mile stretch of pristine beach, excellent restaurants, and shopping. The resort offers all-oceanfront suites and is perfect if you want to be close to amenities while enjoying luxury beachfront accommodations.
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-32)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-33)2. COMO Parrot Cay - This is an exclusive private island resort located on Parrot Cay, a secluded island accessible by boat from Providenciales. This is the ultimate luxury escape if you're looking for privacy and seclusion. The resort is set on 1,000 unspoiled acres with pristine white beaches. This location is perfect for those who want to truly get away from it all while enjoying world-class service and amenities.
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-34)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-35)Would you like more specific information about either of these properties or their locations?
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-36)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-37)--- Conversation Turn 3 ---
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-38)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-39)User: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-40) "resume": "i like the first one. could you recommend something to do near the hotel?",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-41) "goto": []
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-42)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-43)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-44)callHotelAdvisor: Grace Bay Club is perfectly situated to enjoy many activities in Providenciales! Since the hotel is located on Grace Bay Beach in Provo, here are some excellent activities nearby:
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-45)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-46)1. Beach Activities (right at your doorstep):
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-47)- Swimming and sunbathing on Grace Bay Beach
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-48)- Snorkeling right off the beach
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-49)- Beach walks along the pristine 12-mile stretch
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-50)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-51)2. Within Walking Distance:
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-52)- Salt Mills Plaza (shopping center with local boutiques and restaurants)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-53)- Graceway Gourmet (upscale grocery store)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-54)- Several beachfront restaurants and bars
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-55)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-56)3. Very Close By (5-10 minute drive):
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-57)- Princess Alexandra National Park (great for snorkeling)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-58)- Leeward Marina (for boat tours and fishing trips)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-59)- Provo Golf Club (18-hole championship golf course)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-60)- Thursday Night Fish Fry at Bight Park (local culture and food)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-61)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-62)4. Water Activities (operators will pick you up):
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-63)- Snorkeling or diving trips to the barrier reef
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-64)- Sunset sailing cruises
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-65)- Half-day trips to Iguana Island
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-66)- Whale watching (in season - January to April)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-67)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-68)Would you like me to connect you with our travel advisor for more specific activity recommendations or help with booking any excursions?

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-6-1)

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to add multi-turn conversation in a multi-agent application  ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/) [ Next  How to define graph state  ](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
