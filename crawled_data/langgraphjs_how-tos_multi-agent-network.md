---
url: https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#how-to-build-a-multi-agent-network)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to build a multi-agent network 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/?q= "Share")

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
            * How to build a multi-agent network  [ How to build a multi-agent network  ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#setup)
              * [ Travel Recommendations Example  ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#travel-recommendations-example)
              * [ Game NPCs Example  ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#game-npcs-example)
            * [ How to build a multi-agent network (functional API)  ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#setup)
  * [ Travel Recommendations Example  ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#travel-recommendations-example)
  * [ Game NPCs Example  ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#game-npcs-example)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
  5. [ Multi-agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/)



# How to build a multi-agent network[¶](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#how-to-build-a-multi-agent-network "Permanent link")

Prerequisites

This guide assumes familiarity with the following: 

  * [Nodes](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#nodes)
  * [Command](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#command)
  * [Multi-agent systems](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent)



This functionality also requires `@langchain/langgraph>=0.2.29`. 

In this how-to guide we will demonstrate how to implement a [multi-agent network](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent#network) architecture.

Each agent can be represented as a node in the graph that executes agent step(s) and decides what to do next - finish execution or route to another agent (including routing to itself, e.g. running in a loop). A common pattern for routing in multi-agent architectures is handoffs. Handoffs allow you to specify:

  1. which agent to navigate to next and (e.g. name of the node to go to)
  2. what information to pass to that agent (e.g. state update)



To implement handoffs, agent nodes can return `Command` object that allows you to [combine both control flow and state updates](https://langchain-ai.github.io/langgraphjs/how-tos/command/):

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-0-1)constagent=async(state)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-0-2)// the condition for routing/halting can be anything
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-0-3)// e.g. LLM tool call / structured output, etc.
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-0-4)constgoto=getNextAgent(...);// "agent" / "another_agent"
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-0-5)if(goto){
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-0-6)returnnewCommand({
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-0-7)goto,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-0-8)update:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-0-9)myStateKey:"my_state_value",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-0-10)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-0-11)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-0-12)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-0-13)...
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-0-14)}

```


## Setup[¶](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#setup "Permanent link")

First, let's install the required packages:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-1-1)yarnadd@langchain/langgraph@langchain/openai@langchain/corezod

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Travel Recommendations Example[¶](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#travel-recommendations-example "Permanent link")

In this example we will build a team of travel assistant agents that can communicate with each other via handoffs.

We will create 3 agents:

  * `travel_advisor`: can help with general travel destination recommendations. Can ask `sightseeing_advisor` and `hotel_advisor` for help.
  * `sightseeing_advisor`: can help with sightseeing recommendations. Can ask `travel_advisor` and `hotel_advisor` for help.
  * `hotel_advisor`: can help with hotel recommendations. Can ask `sightseeing_advisor` and `hotel_advisor` for help.



This is a fully-connected network - every agent can talk to any other agent. 

To implement the handoffs between the agents we'll be using LLMs with structured output. Each agent's LLM will return an output with both its text response (`response`) as well as which agent to route to next (`goto`). If the agent has enough information to respond to the user, `goto` will contain `finish`.

Now, let's define our agent nodes and graph!

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-1)import{ChatOpenAI}from"@langchain/openai";
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-2)import{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-3)Command,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-4)MessagesAnnotation,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-5)StateGraph
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-6)}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-7)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-8)import{z}from"zod";
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-9)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-10)constmodel=newChatOpenAI({
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-11)model:"gpt-4o",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-12)temperature:0.1,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-13)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-14)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-15)constmakeAgentNode=(params:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-16)name:string,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-17)destinations:string[],
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-18)systemPrompt:string
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-19)})=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-20)returnasync(state:typeofMessagesAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-21)constpossibleDestinations=["__end__",...params.destinations]asconst;
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-22)// define schema for the structured output:
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-23)// - model's text response (`response`)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-24)// - name of the node to go to next (or '__end__')
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-25)constresponseSchema=z.object({
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-26)response:z.string().describe(
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-27)"A human readable response to the original question. Does not need to be a final response. Will be streamed back to the user."
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-28)),
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-29)goto:z.enum(possibleDestinations).describe("The next agent to call, or __end__ if the user's query has been resolved. Must be one of the specified values."),
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-30)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-31)constmessages=[
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-32){
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-33)role:"system",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-34)content:params.systemPrompt
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-35)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-36)...state.messages,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-37)];
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-38)constresponse=awaitmodel.withStructuredOutput(responseSchema,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-39)name:"router",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-40)}).invoke(messages);
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-41)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-42)// handoff to another agent or halt
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-43)constaiMessage={
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-44)role:"assistant",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-45)content:response.response,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-46)name:params.name,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-47)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-48)returnnewCommand({
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-49)goto:response.goto,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-50)update:{messages:aiMessage}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-51)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-52)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-53)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-54)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-55)consttravelAdvisor=makeAgentNode({
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-56)name:"travel_advisor",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-57)destinations:["sightseeing_advisor","hotel_advisor"],
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-58)systemPrompt:[
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-59)"You are a general travel expert that can recommend travel destinations (e.g. countries, cities, etc). ",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-60)"If you need specific sightseeing recommendations, ask 'sightseeing_advisor' for help. ",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-61)"If you need hotel recommendations, ask 'hotel_advisor' for help. ",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-62)"If you have enough information to respond to the user, return '__end__'. ",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-63)"Never mention other agents by name."
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-64)].join(""),
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-65)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-66)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-67)constsightseeingAdvisor=makeAgentNode({
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-68)name:"sightseeing_advisor",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-69)destinations:["travel_advisor","hotel_advisor"],
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-70)systemPrompt:[
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-71)"You are a travel expert that can provide specific sightseeing recommendations for a given destination. ",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-72)"If you need general travel help, go to 'travel_advisor' for help. ",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-73)"If you need hotel recommendations, go to 'hotel_advisor' for help. ",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-74)"If you have enough information to respond to the user, return 'finish'. ",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-75)"Never mention other agents by name."
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-76)].join(""),
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-77)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-78)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-79)consthotelAdvisor=makeAgentNode({
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-80)name:"hotel_advisor",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-81)destinations:["travel_advisor","sightseeing_advisor"],
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-82)systemPrompt:[
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-83)"You are a booking expert that provides hotel recommendations for a given destination. ",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-84)"If you need general travel help, ask 'travel_advisor' for help. ",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-85)"If you need specific sightseeing recommendations, ask 'sightseeing_advisor' for help. ",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-86)"If you have enough information to respond to the user, return 'finish'. ",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-87)"Never mention other agents by name.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-88)].join(""),
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-89)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-90)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-91)constgraph=newStateGraph(MessagesAnnotation)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-92).addNode("travel_advisor",travelAdvisor,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-93)ends:["sightseeing_advisor","hotel_advisor","__end__"],
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-94)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-95).addNode("sightseeing_advisor",sightseeingAdvisor,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-96)ends:["travel_advisor","hotel_advisor","__end__"],
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-97)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-98).addNode("hotel_advisor",hotelAdvisor,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-99)ends:["travel_advisor","sightseeing_advisor","__end__"],
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-100)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-101)// we'll always start with a general travel advisor
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-102).addEdge("__start__","travel_advisor")
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-2-103).compile();

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-3-1)import*astslabfrom"tslab";
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-3-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-3-3)constdrawableGraph=awaitgraph.getGraphAsync();
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-3-4)constimage=awaitdrawableGraph.drawMermaidPng();
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-3-5)constarrayBuffer=awaitimage.arrayBuffer();
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-3-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-3-7)awaittslab.display.png(newUint8Array(arrayBuffer));

```


![]()

First, let's invoke it with a generic input:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-4-1)constsimpleStream=awaitgraph.stream({
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-4-2)messages:[{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-4-3)role:"user",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-4-4)content:"i wanna go somewhere warm in the caribbean",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-4-5)}],
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-4-6)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-4-7)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-4-8)forawait(constchunkofsimpleStream){
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-4-9)console.log(chunk);
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-4-10)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-5-1){
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-5-2) travel_advisor: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-5-3)  messages: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-5-4)   role: 'assistant',
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-5-5)   content: 'The Caribbean is a fantastic choice for warm weather and beautiful beaches. Some popular destinations include Jamaica, the Bahamas, the Dominican Republic, and Barbados. Each offers unique experiences, from vibrant culture and music to stunning natural landscapes.',
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-5-6)   name: 'travel_advisor'
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-5-7)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-5-8) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-5-9)}

```


You can see that in this case only the first agent (`travel_advisor`) ran. Let's now ask for more recommendations: 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-6-1)constrecommendationStream=awaitgraph.stream({
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-6-2)messages:[{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-6-3)role:"user",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-6-4)content:"i wanna go somewhere warm in the caribbean. pick one destination, give me some things to do and hotel recommendations",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-6-5)}],
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-6-6)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-6-7)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-6-8)forawait(constchunkofrecommendationStream){
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-6-9)console.log(chunk);
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-6-10)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-7-1){
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-7-2) travel_advisor: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-7-3)  messages: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-7-4)   role: 'assistant',
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-7-5)   content: 'I recommend visiting Aruba, a beautiful Caribbean island known for its stunning beaches and warm climate.',
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-7-6)   name: 'travel_advisor'
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-7-7)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-7-8) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-7-9)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-7-10){
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-7-11) sightseeing_advisor: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-7-12)  messages: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-7-13)   role: 'assistant',
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-7-14)   content: 'Aruba is a fantastic choice for a warm Caribbean getaway. Here are some activities you can enjoy:\n' +
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-7-15)    '\n' +
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-7-16)    "1. **Eagle Beach**: Relax on one of the world's most beautiful beaches, known for its pristine white sand and clear turquoise waters.\n" +
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-7-17)    '\n' +
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-7-18)    '2. **Arikok National Park**: Explore this national park that covers nearly 20% of the island, offering hiking trails, caves, and unique wildlife.\n' +
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-7-19)    '\n' +
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-7-20)    '3. **Palm Beach**: Enjoy water sports, beach bars, and vibrant nightlife along this bustling beach area.\n' +
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-7-21)    '\n' +
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-7-22)    '4. **Oranjestad**: Visit the colorful capital city for shopping, dining, and exploring local culture and history.\n' +
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-7-23)    '\n' +
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-7-24)    '5. **Snorkeling and Diving**: Discover the vibrant marine life and coral reefs around the island.\n' +
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-7-25)    '\n' +
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-7-26)    '6. **California Lighthouse**: Take a trip to this iconic lighthouse for panoramic views of the island.\n' +
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-7-27)    '\n' +
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-7-28)    "Now, let's find some hotel recommendations for your stay in Aruba.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-7-29)   name: 'sightseeing_advisor'
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-7-30)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-7-31) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-7-32)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-7-33){
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-7-34) hotel_advisor: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-7-35)  messages: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-7-36)   role: 'assistant',
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-7-37)   content: 'For your stay in Aruba, here are some hotel recommendations:\n' +
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-7-38)    '\n' +
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-7-39)    '1. **Renaissance Aruba Resort & Casino**: Located in Oranjestad, this resort offers a private island, luxurious accommodations, and a casino.\n' +
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-7-40)    '\n' +
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-7-41)    '2. **Hilton Aruba Caribbean Resort & Casino**: Situated on Palm Beach, this resort features beautiful gardens, a spa, and multiple dining options.\n' +
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-7-42)    '\n' +
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-7-43)    '3. **The Ritz-Carlton, Aruba**: A luxury beachfront resort offering elegant rooms, a spa, and fine dining.\n' +
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-7-44)    '\n' +
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-7-45)    '4. **Divi Aruba All Inclusive**: Enjoy an all-inclusive experience with multiple restaurants, pools, and activities right on Druif Beach.\n' +
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-7-46)    '\n' +
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-7-47)    '5. **Bucuti & Tara Beach Resort**: An adults-only resort on Eagle Beach, known for its romantic setting and eco-friendly practices.\n' +
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-7-48)    '\n' +
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-7-49)    'These options provide a range of experiences from luxury to all-inclusive, ensuring a comfortable and enjoyable stay in Aruba.',
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-7-50)   name: 'hotel_advisor'
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-7-51)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-7-52) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-7-53)}

```


Voila - `travel_advisor` makes a decision to first get some sightseeing recommendations from `sightseeing_advisor`, and then `sightseeing_advisor` in turn calls `hotel_advisor` for more info. Notice that we never explicitly defined the order in which the agents should be executed! 

## Game NPCs Example[¶](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#game-npcs-example "Permanent link")

In this example we will create a team of [non-player characters (NPCs)](https://en.wikipedia.org/wiki/Non-player_character) that all run at the same time and share game state (resources). At each step, each NPC will inspect the state and decide whether to halt or continue acting at the next step. If it continues, it will update the shared game state (produce or consume resources).

We will create 4 NPC agents:

  * `villager`: produces wood and food until there is enough, then halts
  * `guard`: protects gold and consumes food. When there is not enough food, leaves duty and halts
  * `merchant`: trades wood for gold. When there is not enough wood, halts
  * `thief`: checks if the guard is on duty and steals all of the gold when the guard leaves, then halts



Our NPC agents will be simple node functions (`villager`, `guard`, etc.). At each step of the graph execution, the agent function will inspect the resource values in the state and decide whether it should halt or continue. If it decides to continue, it will update the resource values in the state and loop back to itself to run at the next step.

Now, let's define our agent nodes and graph!

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-1)import{Command,StateGraph,Annotation}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-3)constGameStateAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-4)// note that we're defining a reducer (operator.add) here.
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-5)// This will allow all agents to write their updates for resources concurrently.
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-6)wood:Annotation<number>({
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-7)default:()=>0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-8)reducer:(a,b)=>a+b,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-9)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-10)food:Annotation<number>({
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-11)default:()=>0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-12)reducer:(a,b)=>a+b,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-13)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-14)gold:Annotation<number>({
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-15)default:()=>0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-16)reducer:(a,b)=>a+b,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-17)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-18)guardOnDuty:Annotation<boolean>,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-19)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-20)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-21)/** Villager NPC that gathers wood and food. */
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-22)constvillager=async(state:typeofGameStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-23)constcurrentResources=state.wood+state.food;
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-24)// Continue gathering until we have enough resources
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-25)if(currentResources<15){
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-26)console.log("Villager gathering resources.");
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-27)returnnewCommand({
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-28)goto:"villager",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-29)update:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-30)wood:3,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-31)food:1,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-32)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-33)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-34)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-35)// NOTE: Returning Command({goto: "__end__"}) is not necessary for the graph to run correctly
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-36)// but it's useful for visualization, to show that the agent actually halts
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-37)returnnewCommand({
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-38)goto:"__end__",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-39)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-40)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-41)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-42)/** Guard NPC that protects gold and consumes food. */
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-43)constguard=async(state:typeofGameStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-44)if(!state.guardOnDuty){
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-45)returnnewCommand({
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-46)goto:"__end__",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-47)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-48)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-49)// Guard needs food to keep patrolling
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-50)if(state.food>0){
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-51)console.log("Guard patrolling.");
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-52)// Loop back to the 'guard' agent
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-53)returnnewCommand({
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-54)goto:"guard",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-55)update:{food:-1},
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-56)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-57)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-58)console.log("Guard leaving to get food.");
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-59)returnnewCommand({
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-60)goto:"__end__",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-61)update:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-62)guardOnDuty:false,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-63)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-64)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-65)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-66)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-67)/** Merchant NPC that trades wood for gold. */
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-68)constmerchant=async(state:typeofGameStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-69)// Trade wood for gold when available
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-70)if(state.wood>=5){
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-71)console.log("Merchant trading wood for gold.");
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-72)returnnewCommand({
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-73)goto:"merchant",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-74)update:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-75)wood:-5,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-76)gold:1
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-77)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-78)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-79)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-80)returnnewCommand({
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-81)goto:"__end__"
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-82)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-83)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-84)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-85)/** Thief NPC that steals gold if the guard leaves to get food. */
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-86)constthief=async(state:typeofGameStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-87)if(!state.guardOnDuty){
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-88)console.log("Thief stealing gold.");
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-89)returnnewCommand({
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-90)goto:"__end__",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-91)update:{gold:-state.gold}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-92)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-93)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-94)// keep thief on standby (loop back to the 'thief' agent)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-95)returnnewCommand({
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-96)goto:"thief"
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-97)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-98)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-99)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-100)constgameGraph=newStateGraph(GameStateAnnotation)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-101).addNode("villager",villager,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-102)ends:["villager","__end__"],
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-103)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-104).addNode("guard",guard,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-105)ends:["guard","__end__"],
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-106)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-107).addNode("merchant",merchant,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-108)ends:["merchant","__end__"],
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-109)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-110).addNode("thief",thief,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-111)ends:["thief","__end__"],
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-112)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-113).addEdge("__start__","villager")
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-114).addEdge("__start__","guard")
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-115).addEdge("__start__","merchant")
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-116).addEdge("__start__","thief")
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-8-117).compile();

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-9-1)import*astslabfrom"tslab";
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-9-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-9-3)constdrawableGameGraph=awaitgameGraph.getGraphAsync();
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-9-4)constgameImage=awaitdrawableGameGraph.drawMermaidPng();
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-9-5)constgameArrayBuffer=awaitgameImage.arrayBuffer();
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-9-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-9-7)awaittslab.display.png(newUint8Array(gameArrayBuffer));

```


![]()

Let's run it with some initial state!

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-10-1)constgameStream=awaitgameGraph.stream({
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-10-2)wood:10,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-10-3)food:3,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-10-4)gold:10,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-10-5)guardOnDuty:true,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-10-6)},{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-10-7)streamMode:"values",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-10-8)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-10-9)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-10-10)forawait(conststateofgameStream){
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-10-11)console.log("Game state",state);
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-10-12)console.log("-".repeat(50));
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-10-13)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-11-1)Game state { wood: 10, food: 3, gold: 10, guardOnDuty: true }
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-11-2)--------------------------------------------------
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-11-3)Villager gathering resources.
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-11-4)Guard patrolling.
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-11-5)Merchant trading wood for gold.
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-11-6)Game state { wood: 8, food: 3, gold: 11, guardOnDuty: true }
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-11-7)--------------------------------------------------
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-11-8)Villager gathering resources.
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-11-9)Guard patrolling.
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-11-10)Merchant trading wood for gold.
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-11-11)Game state { wood: 6, food: 3, gold: 12, guardOnDuty: true }
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-11-12)--------------------------------------------------
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-11-13)Villager gathering resources.
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-11-14)Guard patrolling.
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-11-15)Merchant trading wood for gold.
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-11-16)Game state { wood: 4, food: 3, gold: 13, guardOnDuty: true }
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-11-17)--------------------------------------------------
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-11-18)Villager gathering resources.
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-11-19)Guard patrolling.
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-11-20)Game state { wood: 7, food: 3, gold: 13, guardOnDuty: true }
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-11-21)--------------------------------------------------
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-11-22)Villager gathering resources.
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-11-23)Guard patrolling.
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-11-24)Game state { wood: 10, food: 3, gold: 13, guardOnDuty: true }
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-11-25)--------------------------------------------------
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-11-26)Villager gathering resources.
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-11-27)Guard patrolling.
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-11-28)Game state { wood: 13, food: 3, gold: 13, guardOnDuty: true }
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-11-29)--------------------------------------------------
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-11-30)Guard patrolling.
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-11-31)Game state { wood: 13, food: 2, gold: 13, guardOnDuty: true }
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-11-32)--------------------------------------------------
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-11-33)Guard patrolling.
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-11-34)Game state { wood: 13, food: 1, gold: 13, guardOnDuty: true }
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-11-35)--------------------------------------------------
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-11-36)Guard patrolling.
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-11-37)Game state { wood: 13, food: 0, gold: 13, guardOnDuty: true }
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-11-38)--------------------------------------------------
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-11-39)Guard leaving to get food.
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-11-40)Game state { wood: 13, food: 0, gold: 13, guardOnDuty: false }
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-11-41)--------------------------------------------------
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-11-42)Thief stealing gold.
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-11-43)Game state { wood: 13, food: 0, gold: 0, guardOnDuty: false }
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-11-44)--------------------------------------------------

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__codelineno-12-1)

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to transform inputs and outputs of a subgraph  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/) [ Next  How to build a multi-agent network (functional API)  ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
