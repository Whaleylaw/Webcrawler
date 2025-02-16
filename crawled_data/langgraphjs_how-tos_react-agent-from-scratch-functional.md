---
url: https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#how-to-create-a-react-agent-from-scratch-functional-api)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to create a ReAct agent from scratch (Functional API) 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/?q= "Share")

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
          * [ Multi-agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/)
          * [ State Management  ](https://langchain-ai.github.io/langgraphjs/how-tos#state-management)
          * [ Other  ](https://langchain-ai.github.io/langgraphjs/how-tos#other)
          * Prebuilt ReAct Agent  Prebuilt ReAct Agent 
            * [ Prebuilt ReAct Agent  ](https://langchain-ai.github.io/langgraphjs/how-tos#prebuilt-react-agent)
            * [ How to use the prebuilt ReAct agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/)
            * [ How to add memory to the prebuilt ReAct agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/)
            * [ How to add a custom system prompt to the prebuilt ReAct agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/)
            * [ How to add human-in-the-loop processes to the prebuilt ReAct agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/)
            * How to create a ReAct agent from scratch (Functional API)  [ How to create a ReAct agent from scratch (Functional API)  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#setup)
              * [ Create ReAct agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#create-react-agent)
                * [ Define model and tools  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#define-model-and-tools)
                * [ Define tasks  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#define-tasks)
                * [ Define entrypoint  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#define-entrypoint)
              * [ Usage  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#usage)
              * [ Add thread-level persistence  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#add-thread-level-persistence)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#setup)
  * [ Create ReAct agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#create-react-agent)
    * [ Define model and tools  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#define-model-and-tools)
    * [ Define tasks  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#define-tasks)
    * [ Define entrypoint  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#define-entrypoint)
  * [ Usage  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#usage)
  * [ Add thread-level persistence  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#add-thread-level-persistence)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
  5. [ Prebuilt ReAct Agent  ](https://langchain-ai.github.io/langgraphjs/how-tos#prebuilt-react-agent)



# How to create a ReAct agent from scratch (Functional API)[¶](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#how-to-create-a-react-agent-from-scratch-functional-api "Permanent link")

Prerequisites

This guide assumes familiarity with the following:

  * [Chat Models](https://js.langchain.com/docs/concepts/chat_models)
  * [Messages](https://js.langchain.com/docs/concepts/messages)
  * [Tool Calling](https://js.langchain.com/docs/concepts/tool_calling/)
  * [Entrypoints](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#entrypoint) and [Tasks](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#task)



This guide demonstrates how to implement a ReAct agent using the LangGraph [Functional API](https://langchain-ai.github.io/langgraphjs/concepts/functional_api).

The ReAct agent is a [tool-calling agent](https://langchain-ai.github.io/langgraphjs/concepts/agentic_concepts/#tool-calling-agent) that operates as follows:

  1. Queries are issued to a chat model;
  2. If the model generates no [tool calls](https://langchain-ai.github.io/langgraphjs/concepts/agentic_concepts/#tool-calling), we return the model response.
  3. If the model generates tool calls, we execute the tool calls with available tools, append them as [tool messages](https://js.langchain.com/docs/concepts/messages/) to our message list, and repeat the process.



This is a simple and versatile set-up that can be extended with memory, human-in-the-loop capabilities, and other features. See the dedicated [how-to guides](https://langchain-ai.github.io/langgraphjs/how-tos/#prebuilt-react-agent) for examples.

## Setup[¶](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#setup "Permanent link")

Note

This guide requires `@langchain/langgraph>=0.2.42`.

First, install the required dependencies for this example:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-0-1)npminstall@langchain/langgraph@langchain/openai@langchain/corezod

```


Next, we need to set API keys for OpenAI (the LLM we will use):

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-1-1)process.env.OPENAI_API_KEY="YOUR_API_KEY";

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com)

## Create ReAct agent[¶](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#create-react-agent "Permanent link")

Now that you have installed the required packages and set your environment variables, we can create our agent.

### Define model and tools[¶](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#define-model-and-tools "Permanent link")

Let's first define the tools and model we will use for our example. Here we will use a single place-holder tool that gets a description of the weather for a location.

We will use an [OpenAI](https://js.langchain.com/docs/integrations/providers/openai/) chat model for this example, but any model [supporting tool-calling](https://js.langchain.com/docs/integrations/chat/) will suffice.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-2-1)import{ChatOpenAI}from"@langchain/openai";
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-2-2)import{tool}from"@langchain/core/tools";
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-2-3)import{z}from"zod";
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-2-4)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-2-5)constmodel=newChatOpenAI({
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-2-6)model:"gpt-4o-mini",
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-2-7)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-2-8)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-2-9)constgetWeather=tool(async({location})=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-2-10)constlowercaseLocation=location.toLowerCase();
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-2-11)if(lowercaseLocation.includes("sf")||lowercaseLocation.includes("san francisco")){
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-2-12)return"It's sunny!";
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-2-13)}elseif(lowercaseLocation.includes("boston")){
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-2-14)return"It's rainy!";
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-2-15)}else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-2-16)return`I am not sure what the weather is in ${location}`;
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-2-17)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-2-18)},{
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-2-19)name:"getWeather",
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-2-20)schema:z.object({
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-2-21)location:z.string().describe("location to get the weather for"),
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-2-22)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-2-23)description:"Call to get the weather from a specific location."
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-2-24)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-2-25)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-2-26)consttools=[getWeather];

```


### Define tasks[¶](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#define-tasks "Permanent link")

We next define the [tasks](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#task) we will execute. Here there are two different tasks:

  1. **Call model** : We want to query our chat model with a list of messages.
  2. **Call tool** : If our model generates tool calls, we want to execute them.



```
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-3-1)import{
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-3-2)typeBaseMessageLike,
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-3-3)AIMessage,
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-3-4)ToolMessage,
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-3-5)}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-3-6)import{typeToolCall}from"@langchain/core/messages/tool";
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-3-7)import{task}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-3-8)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-3-9)consttoolsByName=Object.fromEntries(tools.map((tool)=>[tool.name,tool]));
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-3-10)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-3-11)constcallModel=task("callModel",async(messages:BaseMessageLike[])=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-3-12)constresponse=awaitmodel.bindTools(tools).invoke(messages);
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-3-13)returnresponse;
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-3-14)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-3-15)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-3-16)constcallTool=task(
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-3-17)"callTool",
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-3-18)async(toolCall:ToolCall):Promise<AIMessage>=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-3-19)consttool=toolsByName[toolCall.name];
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-3-20)constobservation=awaittool.invoke(toolCall.args);
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-3-21)returnnewToolMessage({content:observation,tool_call_id:toolCall.id});
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-3-22)// Can also pass toolCall directly into the tool to return a ToolMessage
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-3-23)// return tool.invoke(toolCall);
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-3-24)});

```


### Define entrypoint[¶](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#define-entrypoint "Permanent link")

Our [entrypoint](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#entrypoint) will handle the orchestration of these two tasks. As described above, when our `callModel` task generates tool calls, the `callTool` task will generate responses for each. We append all messages to a single messages list.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-4-1)import{entrypoint,addMessages}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-4-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-4-3)constagent=entrypoint(
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-4-4)"agent",
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-4-5)async(messages:BaseMessageLike[])=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-4-6)letcurrentMessages=messages;
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-4-7)letllmResponse=awaitcallModel(currentMessages);
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-4-8)while(true){
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-4-9)if(!llmResponse.tool_calls?.length){
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-4-10)break;
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-4-11)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-4-12)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-4-13)// Execute tools
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-4-14)consttoolResults=awaitPromise.all(
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-4-15)llmResponse.tool_calls.map((toolCall)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-4-16)returncallTool(toolCall);
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-4-17)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-4-18));
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-4-19)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-4-20)// Append to message list
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-4-21)currentMessages=addMessages(currentMessages,[llmResponse,...toolResults]);
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-4-22)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-4-23)// Call model again
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-4-24)llmResponse=awaitcallModel(currentMessages);
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-4-25)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-4-26)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-4-27)returnllmResponse;
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-4-28)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-4-29));

```


## Usage[¶](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#usage "Permanent link")

To use our agent, we invoke it with a messages list. Based on our implementation, these can be LangChain [message](https://js.langchain.com/docs/concepts/messages/) objects or OpenAI-style objects:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-5-1)import{BaseMessage,isAIMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-5-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-5-3)constprettyPrintMessage=(message:BaseMessage)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-5-4)console.log("=".repeat(30),`${message.getType()} message`,"=".repeat(30));
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-5-5)console.log(message.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-5-6)if(isAIMessage(message)&&message.tool_calls?.length){
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-5-7)console.log(JSON.stringify(message.tool_calls,null,2));
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-5-8)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-5-9)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-5-10)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-5-11)// Usage example
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-5-12)constuserMessage={role:"user",content:"What's the weather in san francisco?"};
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-5-13)console.log(userMessage);
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-5-14)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-5-15)conststream=awaitagent.stream([userMessage]);
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-5-16)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-5-17)forawait(conststepofstream){
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-5-18)for(const[taskName,update]ofObject.entries(step)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-5-19)constmessage=updateasBaseMessage;
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-5-20)// Only print task updates
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-5-21)if(taskName==="agent")continue;
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-5-22)console.log(`\n${taskName}:`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-5-23)prettyPrintMessage(message);
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-5-24)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-5-25)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-6-1){ role: 'user', content: "What's the weather in san francisco?" }
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-6-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-6-3)callModel:
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-6-4)============================== ai message ==============================
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-6-5)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-6-6)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-6-7) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-6-8)  "name": "getWeather",
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-6-9)  "args": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-6-10)   "location": "San Francisco"
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-6-11)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-6-12)  "type": "tool_call",
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-6-13)  "id": "call_m5jZoH1HUtH6wA2QvexOHutj"
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-6-14) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-6-15)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-6-16)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-6-17)callTool:
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-6-18)============================== tool message ==============================
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-6-19)It's sunny!
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-6-20)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-6-21)callModel:
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-6-22)============================== ai message ==============================
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-6-23)The weather in San Francisco is sunny!

```


Perfect! The graph correctly calls the `getWeather` tool and responds to the user after receiving the information from the tool. Check out the LangSmith trace [here](https://smith.langchain.com/public/8132d3b8-2c91-40fc-b660-b766ca33e9cb/r). 

## Add thread-level persistence[¶](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#add-thread-level-persistence "Permanent link")

Adding [thread-level persistence](https://langchain-ai.github.io/langgraphjs/concepts/persistence#threads) lets us support conversational experiences with our agent: subsequent invocations will append to the prior messages list, retaining the full conversational context.

To add thread-level persistence to our agent:

  1. Select a [checkpointer](https://langchain-ai.github.io/langgraphjs/concepts/persistence#checkpointer-libraries): here we will use [MemorySaver](https://langchain-ai.github.io/langgraphjs/reference/classes/checkpoint.MemorySaver.html), a simple in-memory checkpointer.
  2. Update our entrypoint to accept the previous messages state as a second argument. Here, we simply append the message updates to the previous sequence of messages.
  3. Choose which values will be returned from the workflow and which will be saved by the checkpointer. We will be able to access it as `getPreviousState()` if we return it from `entrypoint.final` (optional)



```
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-7-1)import{
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-7-2)MemorySaver,
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-7-3)getPreviousState,
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-7-4)}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-7-5)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-7-6)constcheckpointer=newMemorySaver();
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-7-7)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-7-8)constagentWithMemory=entrypoint({
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-7-9)name:"agentWithMemory",
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-7-10)checkpointer,
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-7-11)},async(messages:BaseMessageLike[])=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-7-12)constprevious=getPreviousState<BaseMessage>()??[];
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-7-13)letcurrentMessages=addMessages(previous,messages);
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-7-14)letllmResponse=awaitcallModel(currentMessages);
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-7-15)while(true){
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-7-16)if(!llmResponse.tool_calls?.length){
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-7-17)break;
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-7-18)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-7-19)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-7-20)// Execute tools
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-7-21)consttoolResults=awaitPromise.all(
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-7-22)llmResponse.tool_calls.map((toolCall)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-7-23)returncallTool(toolCall);
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-7-24)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-7-25));
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-7-26)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-7-27)// Append to message list
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-7-28)currentMessages=addMessages(currentMessages,[llmResponse,...toolResults]);
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-7-29)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-7-30)// Call model again
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-7-31)llmResponse=awaitcallModel(currentMessages);
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-7-32)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-7-33)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-7-34)// Append final response for storage
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-7-35)currentMessages=addMessages(currentMessages,llmResponse);
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-7-36)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-7-37)returnentrypoint.final({
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-7-38)value:llmResponse,
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-7-39)save:currentMessages,
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-7-40)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-7-41)});

```


We will now need to pass in a config when running our application. The config will specify an identifier for the conversational thread.

Tip

Read more about thread-level persistence in our [concepts page](https://langchain-ai.github.io/langgraphjs/concepts/persistence/) and [how-to guides](https://langchain-ai.github.io/langgraphjs/how-tos/#persistence).

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-8-1)constconfig={configurable:{thread_id:"1"}};

```


We start a thread the same way as before, this time passing in the config:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-9-1)conststreamWithMemory=awaitagentWithMemory.stream([{
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-9-2)role:"user",
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-9-3)content:"What's the weather in san francisco?",
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-9-4)}],config);
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-9-5)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-9-6)forawait(conststepofstreamWithMemory){
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-9-7)for(const[taskName,update]ofObject.entries(step)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-9-8)constmessage=updateasBaseMessage;
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-9-9)// Only print task updates
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-9-10)if(taskName==="agentWithMemory")continue;
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-9-11)console.log(`\n${taskName}:`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-9-12)prettyPrintMessage(message);
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-9-13)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-9-14)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-10-1)callModel:
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-10-2)============================== ai message ==============================
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-10-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-10-4)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-10-5) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-10-6)  "name": "getWeather",
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-10-7)  "args": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-10-8)   "location": "san francisco"
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-10-9)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-10-10)  "type": "tool_call",
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-10-11)  "id": "call_4vaZqAxUabthejqKPRMq0ngY"
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-10-12) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-10-13)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-10-14)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-10-15)callTool:
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-10-16)============================== tool message ==============================
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-10-17)It's sunny!
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-10-18)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-10-19)callModel:
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-10-20)============================== ai message ==============================
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-10-21)The weather in San Francisco is sunny!

```


When we ask a follow-up conversation, the model uses the prior context to infer that we are asking about the weather: 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-11-1)constfollowupStreamWithMemory=awaitagentWithMemory.stream([{
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-11-2)role:"user",
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-11-3)content:"How does it compare to Boston, MA?",
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-11-4)}],config);
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-11-5)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-11-6)forawait(conststepoffollowupStreamWithMemory){
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-11-7)for(const[taskName,update]ofObject.entries(step)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-11-8)constmessage=updateasBaseMessage;
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-11-9)// Only print task updates
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-11-10)if(taskName==="agentWithMemory")continue;
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-11-11)console.log(`\n${taskName}:`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-11-12)prettyPrintMessage(message);
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-11-13)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-11-14)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-12-1)callModel:
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-12-2)============================== ai message ==============================
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-12-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-12-4)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-12-5) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-12-6)  "name": "getWeather",
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-12-7)  "args": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-12-8)   "location": "boston, ma"
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-12-9)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-12-10)  "type": "tool_call",
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-12-11)  "id": "call_YDrNfZr5XnuBBq5jlIXaxC5v"
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-12-12) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-12-13)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-12-14)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-12-15)callTool:
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-12-16)============================== tool message ==============================
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-12-17)It's rainy!
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-12-18)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-12-19)callModel:
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-12-20)============================== ai message ==============================
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__codelineno-12-21)In comparison, while San Francisco is sunny, Boston, MA is experiencing rain.

```


In the [LangSmith trace](https://smith.langchain.com/public/ec803712-ecfc-49b6-8f54-92252d1e5e33/r), we can see that the full conversational context is retained in each model call.  Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to add human-in-the-loop processes to the prebuilt ReAct agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/) [ Next  How to Set Up a LangGraph Application for Deployment  ](https://langchain-ai.github.io/langgraphjs/cloud/deployment/setup/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
