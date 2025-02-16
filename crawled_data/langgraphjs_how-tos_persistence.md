---
url: https://langchain-ai.github.io/langgraphjs/how-tos/persistence/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#persistence)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

Persistence 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/?q= "Share")

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
          * Persistence  Persistence 
            * [ Persistence  ](https://langchain-ai.github.io/langgraphjs/how-tos#persistence)
            * Persistence  [ Persistence  ](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#setup)
              * [ Define the state  ](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#define-the-state)
              * [ Set up the tools  ](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#set-up-the-tools)
              * [ Set up the model  ](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#set-up-the-model)
              * [ Define the graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#define-the-graph)
              * [ Add Memory  ](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#add-memory)
              * [ New Conversational Thread  ](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#new-conversational-thread)
            * [ How to add thread-level persistence (functional API)  ](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/)
            * [ How to add thread-level persistence to subgraphs  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/)
            * [ How to add cross-thread persistence to your graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/)
            * [ How to add cross-thread persistence (functional API)  ](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/)
            * [ How to use Postgres checkpointer for persistence  ](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/)
          * [ Memory  ](https://langchain-ai.github.io/langgraphjs/how-tos#memory)
          * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraphjs/how-tos#human-in-the-loop)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#setup)
  * [ Define the state  ](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#define-the-state)
  * [ Set up the tools  ](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#set-up-the-tools)
  * [ Set up the model  ](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#set-up-the-model)
  * [ Define the graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#define-the-graph)
  * [ Add Memory  ](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#add-memory)
  * [ New Conversational Thread  ](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#new-conversational-thread)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
  5. [ Persistence  ](https://langchain-ai.github.io/langgraphjs/how-tos#persistence)



# Persistence[¶](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#persistence "Permanent link")

Many AI applications need memory to share context across multiple interactions in a single conversational "thread." In LangGraph, this type of conversation-level memory can be added to any graph using [Checkpointers](https://langchain-ai.github.io/langgraphjs/reference/interfaces/index.Checkpoint.html).

Just compile the graph with a compatible checkpointer. Below is an example using a simple in-memory "MemorySaver":

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-0-1)import{MemorySaver}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-0-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-0-3)constcheckpointer=newMemorySaver();
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-0-4)constgraph=workflow.compile({checkpointer});

```


This guide shows how you can add thread-level persistence to your graph.

Note: multi-conversation memory

If you need memory that is **shared** across multiple conversations or users (cross-thread persistence), check out this [how-to guide](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/)). 

Note

In this how-to, we will create our agent from scratch to be transparent (but verbose). You can accomplish similar functionality using the `createReactAgent(model, tools=tool, checkpointer=checkpointer)` ([API doc](https://langchain-ai.github.io/langgraphjs/reference/functions/prebuilt.createReactAgent.html)) constructor. This may be more appropriate if you are used to LangChain's [AgentExecutor](https://js.langchain.com/docs/how_to/agent_executor) class. 

## Setup[¶](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#setup "Permanent link")

This guide will use OpenAI's GPT-4o model. We will optionally set our API key for [LangSmith tracing](https://smith.langchain.com/), which will give us best-in-class observability.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-1-1)// process.env.OPENAI_API_KEY = "sk_...";
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-1-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-1-3)// Optional, add tracing in LangSmith
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-1-4)// process.env.LANGCHAIN_API_KEY = "ls__...";
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-1-5)process.env.LANGCHAIN_CALLBACKS_BACKGROUND="true";
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-1-6)process.env.LANGCHAIN_TRACING_V2="true";
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-1-7)process.env.LANGCHAIN_PROJECT="Persistence: LangGraphJS";

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-2-1)Persistence: LangGraphJS

```


## Define the state[¶](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#define-the-state "Permanent link")

The state is the interface for all of the nodes in our graph.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-3-1)import{Annotation}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-3-2)import{BaseMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-3-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-3-4)constGraphState=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-3-5)messages:Annotation<BaseMessage[]>({
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-3-6)reducer:(x,y)=>x.concat(y),
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-3-7)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-3-8)});

```


## Set up the tools[¶](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#set-up-the-tools "Permanent link")

We will first define the tools we want to use. For this simple example, we will use create a placeholder search engine. However, it is really easy to create your own tools - see documentation [here](https://js.langchain.com/docs/how_to/custom_tools) on how to do that.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-4-1)import{tool}from"@langchain/core/tools";
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-4-2)import{z}from"zod";
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-4-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-4-4)constsearchTool=tool(async({}:{query:string})=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-4-5)// This is a placeholder for the actual implementation
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-4-6)return"Cold, with a low of 13 ℃";
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-4-7)},{
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-4-8)name:"search",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-4-9)description:
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-4-10)"Use to surf the web, fetch current information, check the weather, and retrieve other information.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-4-11)schema:z.object({
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-4-12)query:z.string().describe("The query to use in your search."),
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-4-13)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-4-14)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-4-15)
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-4-16)awaitsearchTool.invoke({query:"What's the weather like?"});
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-4-17)
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-4-18)consttools=[searchTool];

```


We can now wrap these tools in a simple [ToolNode](https://langchain-ai.github.io/langgraphjs/reference/classes/langgraph_prebuilt.ToolNode.html). This object will actually run the tools (functions) whenever they are invoked by our LLM.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-5-1)import{ToolNode}from"@langchain/langgraph/prebuilt";
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-5-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-5-3)consttoolNode=newToolNode(tools);

```


## Set up the model[¶](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#set-up-the-model "Permanent link")

Now we will load the [chat model](https://js.langchain.com/docs/concepts/#chat-models).

  1. It should work with messages. We will represent all agent state in the form of messages, so it needs to be able to work well with them.
  2. It should work with [tool calling](https://js.langchain.com/docs/how_to/tool_calling/#passing-tools-to-llms), meaning it can return function arguments in its response.



Note

These model requirements are not general requirements for using LangGraph - they are just requirements for this one example. 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-6-1)import{ChatOpenAI}from"@langchain/openai";
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-6-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-6-3)constmodel=newChatOpenAI({model:"gpt-4o"});

```


After we've done this, we should make sure the model knows that it has these tools available to call. We can do this by calling [bindTools](https://v01.api.js.langchain.com/classes/langchain_core_language_models_chat_models.BaseChatModel.html#bindTools).

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-7-1)constboundModel=model.bindTools(tools);

```


## Define the graph[¶](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#define-the-graph "Permanent link")

We can now put it all together. We will run it first without a checkpointer:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-8-1)import{END,START,StateGraph}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-8-2)import{AIMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-8-3)import{RunnableConfig}from"@langchain/core/runnables";
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-8-4)
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-8-5)constrouteMessage=(state:typeofGraphState.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-8-6)const{messages}=state;
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-8-7)constlastMessage=messages[messages.length-1]asAIMessage;
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-8-8)// If no tools are called, we can finish (respond to the user)
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-8-9)if(!lastMessage.tool_calls?.length){
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-8-10)returnEND;
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-8-11)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-8-12)// Otherwise if there is, we continue and call the tools
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-8-13)return"tools";
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-8-14)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-8-15)
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-8-16)constcallModel=async(
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-8-17)state:typeofGraphState.State,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-8-18)config?:RunnableConfig,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-8-19))=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-8-20)const{messages}=state;
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-8-21)constresponse=awaitboundModel.invoke(messages,config);
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-8-22)return{messages:[response]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-8-23)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-8-24)
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-8-25)constworkflow=newStateGraph(GraphState)
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-8-26).addNode("agent",callModel)
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-8-27).addNode("tools",toolNode)
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-8-28).addEdge(START,"agent")
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-8-29).addConditionalEdges("agent",routeMessage)
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-8-30).addEdge("tools","agent");
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-8-31)
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-8-32)constgraph=workflow.compile();

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-9-1)letinputs={messages:[{role:"user",content:"Hi I'm Yu, nice to meet you."}]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-9-2)forawait(
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-9-3)const{messages}ofawaitgraph.stream(inputs,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-9-4)streamMode:"values",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-9-5)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-9-6)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-9-7)letmsg=messages[messages?.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-9-8)if(msg?.content){
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-9-9)console.log(msg.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-9-10)}elseif(msg?.tool_calls?.length>0){
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-9-11)console.log(msg.tool_calls);
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-9-12)}else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-9-13)console.log(msg);
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-9-14)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-9-15)console.log("-----\n");
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-9-16)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-10-1)Hi I'm Yu, nice to meet you.
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-10-2)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-10-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-10-4)Hi Yu! Nice to meet you too. How can I assist you today?
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-10-5)-----

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-11-1)inputs={messages:[{role:"user",content:"Remember my name?"}]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-11-2)forawait(
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-11-3)const{messages}ofawaitgraph.stream(inputs,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-11-4)streamMode:"values",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-11-5)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-11-6)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-11-7)letmsg=messages[messages?.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-11-8)if(msg?.content){
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-11-9)console.log(msg.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-11-10)}elseif(msg?.tool_calls?.length>0){
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-11-11)console.log(msg.tool_calls);
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-11-12)}else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-11-13)console.log(msg);
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-11-14)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-11-15)console.log("-----\n");
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-11-16)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-12-1)Remember my name?
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-12-2)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-12-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-12-4)You haven't shared your name with me yet. What's your name?
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-12-5)-----

```


## Add Memory[¶](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#add-memory "Permanent link")

Let's try it again with a checkpointer. We will use the [MemorySaver](https://langchain-ai.github.io/langgraphjs/reference/classes/index.MemorySaver.html), which will "save" checkpoints in-memory.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-13-1)import{MemorySaver}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-13-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-13-3)// Here we only save in-memory
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-13-4)constmemory=newMemorySaver();
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-13-5)constpersistentGraph=workflow.compile({checkpointer:memory});

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-14-1)letconfig={configurable:{thread_id:"conversation-num-1"}};
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-14-2)inputs={messages:[{role:"user",content:"Hi I'm Jo, nice to meet you."}]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-14-3)forawait(
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-14-4)const{messages}ofawaitpersistentGraph.stream(inputs,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-14-5)...config,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-14-6)streamMode:"values",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-14-7)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-14-8)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-14-9)letmsg=messages[messages?.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-14-10)if(msg?.content){
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-14-11)console.log(msg.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-14-12)}elseif(msg?.tool_calls?.length>0){
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-14-13)console.log(msg.tool_calls);
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-14-14)}else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-14-15)console.log(msg);
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-14-16)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-14-17)console.log("-----\n");
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-14-18)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-15-1)Hi I'm Jo, nice to meet you.
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-15-2)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-15-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-15-4)Hello Jo, nice to meet you too! How can I assist you today?
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-15-5)-----

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-16-1)inputs={messages:[{role:"user",content:"Remember my name?"}]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-16-2)forawait(
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-16-3)const{messages}ofawaitpersistentGraph.stream(inputs,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-16-4)...config,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-16-5)streamMode:"values",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-16-6)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-16-7)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-16-8)letmsg=messages[messages?.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-16-9)if(msg?.content){
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-16-10)console.log(msg.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-16-11)}elseif(msg?.tool_calls?.length>0){
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-16-12)console.log(msg.tool_calls);
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-16-13)}else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-16-14)console.log(msg);
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-16-15)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-16-16)console.log("-----\n");
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-16-17)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-17-1)Remember my name?
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-17-2)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-17-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-17-4)Yes, I'll remember that your name is Jo. How can I assist you today?
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-17-5)-----

```


## New Conversational Thread[¶](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#new-conversational-thread "Permanent link")

If we want to start a new conversation, we can pass in a different **`thread_id`**. Poof! All the memories are gone (just kidding, they'll always live in that other thread)!

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-18-1)config={configurable:{thread_id:"conversation-2"}};

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-19-1){ configurable: { thread_id: 'conversation-2' } }

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-20-1)inputs={messages:[{role:"user",content:"you forgot?"}]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-20-2)forawait(
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-20-3)const{messages}ofawaitpersistentGraph.stream(inputs,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-20-4)...config,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-20-5)streamMode:"values",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-20-6)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-20-7)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-20-8)letmsg=messages[messages?.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-20-9)if(msg?.content){
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-20-10)console.log(msg.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-20-11)}elseif(msg?.tool_calls?.length>0){
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-20-12)console.log(msg.tool_calls);
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-20-13)}else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-20-14)console.log(msg);
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-20-15)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-20-16)console.log("-----\n");
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-20-17)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-21-1)you forgot?
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-21-2)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-21-3)``````output
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-21-4)Could you please provide more context or details about what you are referring to? This will help me assist you better.
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__codelineno-21-5)-----

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to combine control flow and state updates with Command  ](https://langchain-ai.github.io/langgraphjs/how-tos/command/) [ Next  How to add thread-level persistence (functional API)  ](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
