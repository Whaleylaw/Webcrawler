---
url: https://langchain-ai.github.io/langgraphjs/how-tos/stream-values
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#how-to-stream-full-state-of-your-graph)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to stream full state of your graph 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/?q= "Share")

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
          * Streaming  Streaming 
            * [ Streaming  ](https://langchain-ai.github.io/langgraphjs/how-tos#streaming)
            * How to stream full state of your graph  [ How to stream full state of your graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/) Table of contents 
              * [ Define the state  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#define-the-state)
              * [ Set up the tools  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#set-up-the-tools)
              * [ Set up the model  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#set-up-the-model)
              * [ Define the graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#define-the-graph)
              * [ Stream values  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#stream-values)
            * [ How to stream state updates of your graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-updates/)
            * [ How to stream LLM tokens from your graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/)
            * [ How to stream LLM tokens (without LangChain models)  ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/)
            * [ How to stream custom data  ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/)
            * [ How to configure multiple streaming modes at the same time  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/)
            * [ How to stream events from within a tool  ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/)
            * [ How to stream from the final node  ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-from-final-node/)
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

  * [ Define the state  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#define-the-state)
  * [ Set up the tools  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#set-up-the-tools)
  * [ Set up the model  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#set-up-the-model)
  * [ Define the graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#define-the-graph)
  * [ Stream values  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#stream-values)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
  5. [ Streaming  ](https://langchain-ai.github.io/langgraphjs/how-tos#streaming)



# How to stream full state of your graph[¶](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#how-to-stream-full-state-of-your-graph "Permanent link")

LangGraph supports multiple streaming modes. The main ones are:

  * `values`: This streaming mode streams back values of the graph. This is the **full state of the graph** after each node is called.
  * `updates`: This streaming mode streams back updates to the graph. This is the **update to the state of the graph** after each node is called.



This guide covers `streamMode="values"`.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-0-1)// process.env.OPENAI_API_KEY = "sk-...";

```


## Define the state[¶](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#define-the-state "Permanent link")

The state is the interface for all of the nodes in our graph.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-1-1)import{Annotation}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-1-2)import{BaseMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-1-4)constStateAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-1-5)messages:Annotation<BaseMessage[]>({
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-1-6)reducer:(x,y)=>x.concat(y),
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-1-7)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-1-8)});

```


## Set up the tools[¶](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#set-up-the-tools "Permanent link")

We will first define the tools we want to use. For this simple example, we will use create a placeholder search engine. However, it is really easy to create your own tools - see documentation [here](https://js.langchain.com/docs/how_to/custom_tools) on how to do that.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-2-1)import{tool}from"@langchain/core/tools";
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-2-2)import{z}from"zod";
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-2-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-2-4)constsearchTool=tool(async({query:_query}:{query:string})=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-2-5)// This is a placeholder for the actual implementation
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-2-6)return"Cold, with a low of 3℃";
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-2-7)},{
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-2-8)name:"search",
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-2-9)description:
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-2-10)"Use to surf the web, fetch current information, check the weather, and retrieve other information.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-2-11)schema:z.object({
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-2-12)query:z.string().describe("The query to use in your search."),
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-2-13)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-2-14)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-2-15)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-2-16)awaitsearchTool.invoke({query:"What's the weather like?"});
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-2-17)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-2-18)consttools=[searchTool];

```


We can now wrap these tools in a simple [ToolNode](https://langchain-ai.github.io/langgraphjs/reference/classes/langgraph_prebuilt.ToolNode.html). This object will actually run the tools (functions) whenever they are invoked by our LLM.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-3-1)import{ToolNode}from"@langchain/langgraph/prebuilt";
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-3-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-3-3)consttoolNode=newToolNode(tools);

```


## Set up the model[¶](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#set-up-the-model "Permanent link")

Now we will load the [chat model](https://js.langchain.com/docs/concepts/chat_models/).

  1. It should work with messages. We will represent all agent state in the form of messages, so it needs to be able to work well with them.
  2. It should work with [tool calling](https://js.langchain.com/docs/how_to/tool_calling/#passing-tools-to-llms), meaning it can return function arguments in its response.



Note

These model requirements are not general requirements for using LangGraph - they are just requirements for this one example. 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-4-1)import{ChatOpenAI}from"@langchain/openai";
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-4-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-4-3)constmodel=newChatOpenAI({model:"gpt-4o"});

```


After we've done this, we should make sure the model knows that it has these tools available to call. We can do this by calling [bindTools](https://v01.api.js.langchain.com/classes/langchain_core_language_models_chat_models.BaseChatModel.html#bindTools).

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-5-1)constboundModel=model.bindTools(tools);

```


## Define the graph[¶](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#define-the-graph "Permanent link")

We can now put it all together.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-6-1)import{END,START,StateGraph}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-6-2)import{AIMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-6-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-6-4)constrouteMessage=(state:typeofStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-6-5)const{messages}=state;
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-6-6)constlastMessage=messages[messages.length-1]asAIMessage;
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-6-7)// If no tools are called, we can finish (respond to the user)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-6-8)if(!lastMessage?.tool_calls?.length){
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-6-9)returnEND;
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-6-10)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-6-11)// Otherwise if there is, we continue and call the tools
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-6-12)return"tools";
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-6-13)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-6-14)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-6-15)constcallModel=async(
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-6-16)state:typeofStateAnnotation.State,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-6-17))=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-6-18)// For versions of @langchain/core < 0.2.3, you must call `.stream()`
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-6-19)// and aggregate the message from chunks instead of calling `.invoke()`.
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-6-20)const{messages}=state;
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-6-21)constresponseMessage=awaitboundModel.invoke(messages);
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-6-22)return{messages:[responseMessage]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-6-23)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-6-24)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-6-25)constworkflow=newStateGraph(StateAnnotation)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-6-26).addNode("agent",callModel)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-6-27).addNode("tools",toolNode)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-6-28).addEdge(START,"agent")
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-6-29).addConditionalEdges("agent",routeMessage)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-6-30).addEdge("tools","agent");
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-6-31)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-6-32)constgraph=workflow.compile();

```


## Stream values[¶](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#stream-values "Permanent link")

We can now interact with the agent. Between interactions you can get and update state.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-7-1)letinputs={messages:[{role:"user",content:"what's the weather in sf"}]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-7-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-7-3)forawait(
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-7-4)constchunkofawaitgraph.stream(inputs,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-7-5)streamMode:"values",
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-7-6)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-7-7)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-7-8)console.log(chunk["messages"]);
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-7-9)console.log("\n====\n");
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-7-10)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-1)[ [ 'user', "what's the weather in sf" ] ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-3)====
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-4)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-5)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-6) [ 'user', "what's the weather in sf" ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-7) AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-8)  "id": "chatcmpl-9y660d49eLzT7DZeBk2ZmX8C5f0LU",
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-9)  "content": "",
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-10)  "additional_kwargs": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-11)   "tool_calls": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-12)    {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-13)     "id": "call_iD5Wk4vPsTckffDKJpEQaMkg",
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-14)     "type": "function",
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-15)     "function": "[Object]"
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-16)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-17)   ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-18)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-19)  "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-20)   "tokenUsage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-21)    "completionTokens": 17,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-22)    "promptTokens": 70,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-23)    "totalTokens": 87
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-24)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-25)   "finish_reason": "tool_calls",
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-26)   "system_fingerprint": "fp_3aa7262c27"
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-27)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-28)  "tool_calls": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-29)   {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-30)    "name": "search",
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-31)    "args": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-32)     "query": "current weather in San Francisco"
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-33)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-34)    "type": "tool_call",
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-35)    "id": "call_iD5Wk4vPsTckffDKJpEQaMkg"
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-36)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-37)  ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-38)  "invalid_tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-39)  "usage_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-40)   "input_tokens": 70,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-41)   "output_tokens": 17,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-42)   "total_tokens": 87
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-43)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-44) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-45)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-46)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-47)====
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-48)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-49)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-50) [ 'user', "what's the weather in sf" ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-51) AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-52)  "id": "chatcmpl-9y660d49eLzT7DZeBk2ZmX8C5f0LU",
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-53)  "content": "",
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-54)  "additional_kwargs": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-55)   "tool_calls": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-56)    {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-57)     "id": "call_iD5Wk4vPsTckffDKJpEQaMkg",
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-58)     "type": "function",
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-59)     "function": "[Object]"
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-60)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-61)   ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-62)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-63)  "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-64)   "tokenUsage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-65)    "completionTokens": 17,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-66)    "promptTokens": 70,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-67)    "totalTokens": 87
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-68)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-69)   "finish_reason": "tool_calls",
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-70)   "system_fingerprint": "fp_3aa7262c27"
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-71)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-72)  "tool_calls": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-73)   {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-74)    "name": "search",
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-75)    "args": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-76)     "query": "current weather in San Francisco"
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-77)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-78)    "type": "tool_call",
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-79)    "id": "call_iD5Wk4vPsTckffDKJpEQaMkg"
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-80)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-81)  ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-82)  "invalid_tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-83)  "usage_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-84)   "input_tokens": 70,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-85)   "output_tokens": 17,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-86)   "total_tokens": 87
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-87)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-88) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-89) ToolMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-90)  "content": "Cold, with a low of 3℃",
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-91)  "name": "search",
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-92)  "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-93)  "response_metadata": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-94)  "tool_call_id": "call_iD5Wk4vPsTckffDKJpEQaMkg"
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-95) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-96)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-97)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-98)====
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-99)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-100)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-101) [ 'user', "what's the weather in sf" ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-102) AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-103)  "id": "chatcmpl-9y660d49eLzT7DZeBk2ZmX8C5f0LU",
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-104)  "content": "",
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-105)  "additional_kwargs": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-106)   "tool_calls": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-107)    {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-108)     "id": "call_iD5Wk4vPsTckffDKJpEQaMkg",
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-109)     "type": "function",
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-110)     "function": "[Object]"
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-111)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-112)   ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-113)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-114)  "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-115)   "tokenUsage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-116)    "completionTokens": 17,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-117)    "promptTokens": 70,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-118)    "totalTokens": 87
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-119)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-120)   "finish_reason": "tool_calls",
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-121)   "system_fingerprint": "fp_3aa7262c27"
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-122)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-123)  "tool_calls": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-124)   {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-125)    "name": "search",
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-126)    "args": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-127)     "query": "current weather in San Francisco"
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-128)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-129)    "type": "tool_call",
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-130)    "id": "call_iD5Wk4vPsTckffDKJpEQaMkg"
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-131)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-132)  ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-133)  "invalid_tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-134)  "usage_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-135)   "input_tokens": 70,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-136)   "output_tokens": 17,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-137)   "total_tokens": 87
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-138)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-139) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-140) ToolMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-141)  "content": "Cold, with a low of 3℃",
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-142)  "name": "search",
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-143)  "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-144)  "response_metadata": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-145)  "tool_call_id": "call_iD5Wk4vPsTckffDKJpEQaMkg"
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-146) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-147) AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-148)  "id": "chatcmpl-9y660ZKNXvziVJze0X5aTlZ5IoN35",
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-149)  "content": "Currently, in San Francisco, it's cold with a temperature of around 3℃ (37.4°F).",
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-150)  "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-151)  "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-152)   "tokenUsage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-153)    "completionTokens": 23,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-154)    "promptTokens": 103,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-155)    "totalTokens": 126
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-156)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-157)   "finish_reason": "stop",
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-158)   "system_fingerprint": "fp_3aa7262c27"
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-159)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-160)  "tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-161)  "invalid_tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-162)  "usage_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-163)   "input_tokens": 103,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-164)   "output_tokens": 23,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-165)   "total_tokens": 126
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-166)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-167) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-168)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-169)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__codelineno-8-170)====

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to review tool calls (Functional API)  ](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/) [ Next  How to stream state updates of your graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-updates/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
