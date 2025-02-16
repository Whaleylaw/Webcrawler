---
url: https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#how-to-add-multi-turn-conversation-in-a-multi-agent-application)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to add multi-turn conversation in a multi-agent application 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/?q= "Share")

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
            * How to add multi-turn conversation in a multi-agent application  [ How to add multi-turn conversation in a multi-agent application  ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#setup)
              * [ Travel Recommendations Example  ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#travel-recommendations-example)
                * [ Test multi-turn conversation  ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#test-multi-turn-conversation)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#setup)
  * [ Travel Recommendations Example  ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#travel-recommendations-example)
    * [ Test multi-turn conversation  ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#test-multi-turn-conversation)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
  5. [ Multi-agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/)



# How to add multi-turn conversation in a multi-agent application[¶](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#how-to-add-multi-turn-conversation-in-a-multi-agent-application "Permanent link")

Prerequisites

This guide assumes familiarity with the following:

  * [Node](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#nodes)
  * [Command](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#command)
  * [Multi-agent systems](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent)
  * [Human-in-the-loop](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop)



In this how-to guide, we’ll build an application that allows an end-user to engage in a _multi-turn conversation_ with one or more agents. We'll create a node that uses an `interrupt`[](https://langchain-ai.github.io/langgraphjs/reference/functions/langgraph.interrupt-1.html) to collect user input and routes back to the **active** agent.

The agents will be implemented as nodes in a graph that executes agent steps and determines the next action: 

  1. **Wait for user input** to continue the conversation, or 
  2. **Route to another agent** (or back to itself, such as in a loop) via a [**handoff**](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#handoffs).



```
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-1)functionhuman(state:typeofMessagesAnnotation.State):Command{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-2)constuserInput:string=interrupt("Ready for user input.");
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-4)// Determine the active agent
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-5)constactiveAgent=...;
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-7)returnnewCommand({
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-8)update:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-9)messages:[{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-10)role:"human",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-11)content:userInput,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-12)}]
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-13)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-14)goto:activeAgent,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-15)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-16)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-17)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-18)functionagent(state:typeofMessagesAnnotation.State):Command{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-19)// The condition for routing/halting can be anything, e.g. LLM tool call / structured output, etc.
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-20)constgoto=getNextAgent(...);// 'agent' / 'anotherAgent'
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-21)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-22)if(goto){
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-23)returnnewCommand({
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-24)goto,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-25)update:{myStateKey:"myStateValue"}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-26)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-27)}else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-28)returnnewCommand({
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-29)goto:"human"
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-30)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-31)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-32)}

```


## Setup[¶](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#setup "Permanent link")

First, let's install the required packages npm install [langchain/langgraph](https://github.com/langchain/langgraph "GitHub Repository: langchain/langgraph") [langchain/openai](https://github.com/langchain/openai "GitHub Repository: langchain/openai") [langchain/core](https://github.com/langchain/core "GitHub Repository: langchain/core") uuid zod

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-1-1)// process.env.OPENAI_API_KEY = "sk_...";
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-1-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-1-3)// Optional, add tracing in LangSmith
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-1-4)// process.env.LANGCHAIN_API_KEY = "ls__...";
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-1-5)process.env.LANGCHAIN_CALLBACKS_BACKGROUND="true";
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-1-6)process.env.LANGCHAIN_TRACING_V2="true";
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-1-7)process.env.LANGCHAIN_PROJECT="Time Travel: LangGraphJS";

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-2-1)Time Travel: LangGraphJS

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Travel Recommendations Example[¶](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#travel-recommendations-example "Permanent link")

In this example, we will build a team of travel assistant agents that can communicate with each other via handoffs.

We will create 3 agents:

  * `travelAdvisor`: can help with general travel destination recommendations. Can ask `sightseeingAdvisor` and `hotelAdvisor` for help.
  * `sightseeingAdvisor`: can help with sightseeing recommendations. Can ask `travelAdvisor` and `hotelAdvisor` for help.
  * `hotelAdvisor`: can help with hotel recommendations. Can ask `sightseeingAdvisor` and `hotelAdvisor` for help.



This is a fully-connected network - every agent can talk to any other agent. 

To implement the handoffs between the agents we'll be using LLMs with structured output. Each agent's LLM will return an output with both its text response (`response`) as well as which agent to route to next (`goto`). If the agent has enough information to respond to the user, the `goto` will be set to `human` to route back and collect information from a human.

Now, let's define our agent nodes and graph!

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-1)import{z}from"zod";
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-2)import{ChatOpenAI}from"@langchain/openai";
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-3)import{BaseMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-4)import{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-5)MessagesAnnotation,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-6)StateGraph,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-7)START,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-8)Command,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-9)interrupt,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-10)MemorySaver
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-11)}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-12)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-13)constmodel=newChatOpenAI({model:"gpt-4o"});
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-14)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-15)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-16)/**
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-17) * Call LLM with structured output to get a natural language response as well as a target agent (node) to go to next.
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-18) * @param messages list of messages to pass to the LLM
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-19) * @param targetAgentNodes list of the node names of the target agents to navigate to
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-20) */
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-21)functioncallLlm(messages:BaseMessage[],targetAgentNodes:string[]){
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-22)// define the schema for the structured output:
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-23)// - model's text response (`response`)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-24)// - name of the node to go to next (or 'finish')
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-25)constoutputSchema=z.object({
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-26)response:z.string().describe("A human readable response to the original question. Does not need to be a final response. Will be streamed back to the user."),
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-27)goto:z.enum(["finish",...targetAgentNodes]).describe("The next agent to call, or 'finish' if the user's query has been resolved. Must be one of the specified values."),
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-28)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-29)returnmodel.withStructuredOutput(outputSchema,{name:"Response"}).invoke(messages)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-30)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-31)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-32)asyncfunctiontravelAdvisor(
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-33)state:typeofMessagesAnnotation.State
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-34)):Promise<Command>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-35)constsystemPrompt=
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-36)"You are a general travel expert that can recommend travel destinations (e.g. countries, cities, etc). "+
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-37)"If you need specific sightseeing recommendations, ask 'sightseeingAdvisor' for help. "+
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-38)"If you need hotel recommendations, ask 'hotelAdvisor' for help. "+
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-39)"If you have enough information to respond to the user, return 'finish'. "+
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-40)"Never mention other agents by name.";
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-41)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-42)constmessages=[{"role":"system","content":systemPrompt},...state.messages]asBaseMessage[];
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-43)consttargetAgentNodes=["sightseeingAdvisor","hotelAdvisor"];
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-44)constresponse=awaitcallLlm(messages,targetAgentNodes);
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-45)constaiMsg={"role":"ai","content":response.response,"name":"travelAdvisor"};
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-46)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-47)letgoto=response.goto;
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-48)if(goto==="finish"){
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-49)goto="human";
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-50)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-51)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-52)returnnewCommand({goto,update:{"messages":[aiMsg]}});
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-53)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-54)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-55)asyncfunctionsightseeingAdvisor(
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-56)state:typeofMessagesAnnotation.State
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-57)):Promise<Command>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-58)constsystemPrompt=
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-59)"You are a travel expert that can provide specific sightseeing recommendations for a given destination. "+
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-60)"If you need general travel help, go to 'travelAdvisor' for help. "+
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-61)"If you need hotel recommendations, go to 'hotelAdvisor' for help. "+
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-62)"If you have enough information to respond to the user, return 'finish'. "+
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-63)"Never mention other agents by name.";
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-64)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-65)constmessages=[{"role":"system","content":systemPrompt},...state.messages]asBaseMessage[];
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-66)consttargetAgentNodes=["travelAdvisor","hotelAdvisor"];
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-67)constresponse=awaitcallLlm(messages,targetAgentNodes);
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-68)constaiMsg={"role":"ai","content":response.response,"name":"sightseeingAdvisor"};
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-69)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-70)letgoto=response.goto;
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-71)if(goto==="finish"){
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-72)goto="human";
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-73)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-74)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-75)returnnewCommand({goto,update:{"messages":[aiMsg]}});
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-76)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-77)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-78)asyncfunctionhotelAdvisor(
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-79)state:typeofMessagesAnnotation.State
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-80)):Promise<Command>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-81)constsystemPrompt=
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-82)"You are a travel expert that can provide hotel recommendations for a given destination. "+
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-83)"If you need general travel help, ask 'travelAdvisor' for help. "+
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-84)"If you need specific sightseeing recommendations, ask 'sightseeingAdvisor' for help. "+
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-85)"If you have enough information to respond to the user, return 'finish'. "+
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-86)"Never mention other agents by name.";
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-87)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-88)constmessages=[{"role":"system","content":systemPrompt},...state.messages]asBaseMessage[];
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-89)consttargetAgentNodes=["travelAdvisor","sightseeingAdvisor"];
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-90)constresponse=awaitcallLlm(messages,targetAgentNodes);
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-91)constaiMsg={"role":"ai","content":response.response,"name":"hotelAdvisor"};
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-92)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-93)letgoto=response.goto;
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-94)if(goto==="finish"){
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-95)goto="human";
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-96)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-97)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-98)returnnewCommand({goto,update:{"messages":[aiMsg]}});
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-99)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-100)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-101)functionhumanNode(
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-102)state:typeofMessagesAnnotation.State
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-103)):Command{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-104)constuserInput:string=interrupt("Ready for user input.");
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-105)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-106)letactiveAgent:string|undefined=undefined;
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-107)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-108)// Look up the active agent
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-109)for(leti=state.messages.length-1;i>=0;i--){
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-110)if(state.messages[i].name){
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-111)activeAgent=state.messages[i].name;
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-112)break;
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-113)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-114)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-115)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-116)if(!activeAgent){
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-117)thrownewError("Could not determine the active agent.");
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-118)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-119)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-120)returnnewCommand({
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-121)goto:activeAgent,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-122)update:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-123)"messages":[
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-124){
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-125)"role":"human",
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-126)"content":userInput,
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-127)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-128)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-129)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-130)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-131)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-132)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-133)constbuilder=newStateGraph(MessagesAnnotation)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-134).addNode("travelAdvisor",travelAdvisor,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-135)ends:["sightseeingAdvisor","hotelAdvisor"]
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-136)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-137).addNode("sightseeingAdvisor",sightseeingAdvisor,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-138)ends:["human","travelAdvisor","hotelAdvisor"]
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-139)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-140).addNode("hotelAdvisor",hotelAdvisor,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-141)ends:["human","travelAdvisor","sightseeingAdvisor"]
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-142)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-143)// This adds a node to collect human input, which will route
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-144)// back to the active agent.
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-145).addNode("human",humanNode,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-146)ends:["hotelAdvisor","sightseeingAdvisor","travelAdvisor","human"]
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-147)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-148)// We'll always start with a general travel advisor.
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-149).addEdge(START,"travelAdvisor")
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-150)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-151)constcheckpointer=newMemorySaver()
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-152)constgraph=builder.compile({checkpointer})

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-1)import*astslabfrom"tslab";
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-3)constdrawableGraph=graph.getGraph();
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-4)constimage=awaitdrawableGraph.drawMermaidPng();
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-5)constarrayBuffer=awaitimage.arrayBuffer();
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-7)awaittslab.display.png(newUint8Array(arrayBuffer));

```


![]()

### Test multi-turn conversation[¶](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#test-multi-turn-conversation "Permanent link")

Let's test a multi turn conversation with this application.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-1)import{Command}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-2)import{v4asuuidv4}from"uuid";
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-4)constthreadConfig={configurable:{thread_id:uuidv4()},streamMode:"values"asconst};
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-5)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-6)constinputs=[
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-7)// 1st round of conversation
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-8){
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-9)messages:[
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-10){role:"user",content:"i wanna go somewhere warm in the caribbean"}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-11)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-12)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-13)// Since we're using `interrupt`, we'll need to resume using the Command primitive.
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-14)// 2nd round of conversation
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-15)newCommand({
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-16)resume:"could you recommend a nice hotel in one of the areas and tell me which area it is."
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-17)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-18)// Third round of conversation
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-19)newCommand({resume:"could you recommend something to do near the hotel?"}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-20)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-21)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-22)letiter=0;
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-23)forawait(constuserInputofinputs){
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-24)iter+=1;
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-25)console.log(`\n--- Conversation Turn ${iter} ---\n`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-26)console.log(`User: ${JSON.stringify(userInput)}\n`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-27)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-28)forawait(constupdateofawaitgraph.stream(userInput,threadConfig)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-29)constlastMessage=update.messages?update.messages[update.messages.length-1]:undefined;
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-30)if(lastMessage&&lastMessage._getType()==="ai"){
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-31)console.log(`${lastMessage.name}: ${lastMessage.content}`)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-32)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-33)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-34)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-6-1)--- Conversation Turn 1 ---
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-6-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-6-3)User: {"messages":[{"role":"user","content":"i wanna go somewhere warm in the caribbean"}]}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-6-4)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-6-5)travelAdvisor: The Caribbean is a fantastic choice for a warm getaway! Some popular destinations you might consider include Jamaica, the Dominican Republic, and the Bahamas. Each destination offers beautiful beaches, warm weather, and a plethora of activities to enjoy in a tropical setting. Aruba and Barbados are also great choices if you prefer lively beach towns with vibrant nightlife and cultural richness.
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-6-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-6-7)Would you like recommendations on sightseeing or places to stay in any of these Caribbean destinations?
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-6-8)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-6-9)--- Conversation Turn 2 ---
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-6-10)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-6-11)User: {"lg_name":"Command","lc_direct_tool_output":true,"resume":"could you recommend a nice hotel in one of the areas and tell me which area it is.","goto":[]}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-6-12)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-6-13)travelAdvisor: The Caribbean is a fantastic choice for a warm getaway! Some popular destinations you might consider include Jamaica, the Dominican Republic, and the Bahamas. Each destination offers beautiful beaches, warm weather, and a plethora of activities to enjoy in a tropical setting. Aruba and Barbados are also great choices if you prefer lively beach towns with vibrant nightlife and cultural richness.
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-6-14)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-6-15)Would you like recommendations on sightseeing or places to stay in any of these Caribbean destinations?
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-6-16)travelAdvisor: Let's focus on Jamaica, known for its beautiful beaches and vibrant culture, perfect for a warm Caribbean escape. I'll find a nice hotel for you there.
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-6-17)hotelAdvisor: In Jamaica, consider staying at the "Round Hill Hotel and Villas" located in Montego Bay. It's a luxurious resort offering a private beach, beautiful villas, and a spa. Montego Bay is known for its stunning beaches, lively nightlife, and rich history with plantations and cultural sites to explore.
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-6-18)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-6-19)--- Conversation Turn 3 ---
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-6-20)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-6-21)User: {"lg_name":"Command","lc_direct_tool_output":true,"resume":"could you recommend something to do near the hotel?","goto":[]}
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-6-22)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-6-23)hotelAdvisor: In Jamaica, consider staying at the "Round Hill Hotel and Villas" located in Montego Bay. It's a luxurious resort offering a private beach, beautiful villas, and a spa. Montego Bay is known for its stunning beaches, lively nightlife, and rich history with plantations and cultural sites to explore.
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-6-24)hotelAdvisor: Let's find some sightseeing recommendations or activities around Round Hill Hotel and Villas in Montego Bay, Jamaica for you.
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-6-25)sightseeingAdvisor: While staying at the Round Hill Hotel and Villas in Montego Bay, you can explore a variety of activities nearby:
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-6-26)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-6-27)1. **Doctor’s Cave Beach**: One of Montego Bay’s most famous beaches, it’s perfect for swimming and enjoying the sun.
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-6-28)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-6-29)2. **Rose Hall Great House**: Visit this historic plantation house, rumored to be haunted, for a tour of the beautiful grounds and a taste of Jamaican history.
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-6-30)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-6-31)3. **Martha Brae River**: Enjoy rafting on this beautiful river, surrounded by lush Jamaican flora. It's a peaceful and scenic way to experience the natural beauty of the area.
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-6-32)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-6-33)4. **Dunn’s River Falls**: Although a bit farther than the other attractions, these stunning waterfalls in Ocho Rios are worth the visit for a unique climbing experience.
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-6-34)
[](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__codelineno-6-35)5. **Montego Bay Marine Park**: Explore the coral reefs and marine life through snorkeling or diving adventures.

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to build a multi-agent network (functional API)  ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/) [ Next  How to add multi-turn conversation in a multi-agent application (functional API)  ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
