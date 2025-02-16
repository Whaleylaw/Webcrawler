---
url: https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#how-to-stream-llm-tokens-from-your-graph)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to stream LLM tokens from your graph 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/?q= "Share")

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
            * [ How to stream full state of your graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/)
            * [ How to stream state updates of your graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-updates/)
            * How to stream LLM tokens from your graph  [ How to stream LLM tokens from your graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#setup)
              * [ Define the state  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#define-the-state)
              * [ Set up the tools  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#set-up-the-tools)
              * [ Set up the model  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#set-up-the-model)
              * [ Define the graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#define-the-graph)
              * [ Streaming LLM Tokens  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#streaming-llm-tokens)
                * [ The stream method  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#the-stream-method)
                * [ Disabling streaming  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#disabling-streaming)
                * [ The streamEvents method  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#the-streamevents-method)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#setup)
  * [ Define the state  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#define-the-state)
  * [ Set up the tools  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#set-up-the-tools)
  * [ Set up the model  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#set-up-the-model)
  * [ Define the graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#define-the-graph)
  * [ Streaming LLM Tokens  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#streaming-llm-tokens)
    * [ The stream method  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#the-stream-method)
    * [ Disabling streaming  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#disabling-streaming)
    * [ The streamEvents method  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#the-streamevents-method)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
  5. [ Streaming  ](https://langchain-ai.github.io/langgraphjs/how-tos#streaming)



# How to stream LLM tokens from your graph[¶](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#how-to-stream-llm-tokens-from-your-graph "Permanent link")

In this example, we will stream tokens from the language model powering an agent. We will use a ReAct agent as an example.

Note

If you are using a version of `@langchain/core` < 0.2.3, when calling chat models or LLMs you need to call `await model.stream()` within your nodes to get token-by-token streaming events, and aggregate final outputs if needed to update the graph state. In later versions of `@langchain/core`, this occurs automatically, and you can call `await model.invoke()`. For more on how to upgrade `@langchain/core`, check out [the instructions here](https://js.langchain.com/docs/how_to/installation/#installing-integration-packages). 

This how-to guide closely follows the others in this directory, showing how to incorporate the functionality into a prototypical agent in LangGraph.

Streaming Support

Token streaming is supported by many, but not all chat models. Check to see if your LLM integration supports token streaming [here (doc)](https://js.langchain.com/docs/integrations/chat/). Note that some integrations may support _general_ token streaming but lack support for streaming tool calls. 

Note

In this how-to, we will create our agent from scratch to be transparent (but verbose). You can accomplish similar functionality using the `createReactAgent({ llm, tools })` ([API doc](https://langchain-ai.github.io/langgraphjs/reference/functions/langgraph_prebuilt.createReactAgent.html)) constructor. This may be more appropriate if you are used to LangChain's [AgentExecutor](https://js.langchain.com/docs/how_to/agent_executor) class. 

## Setup[¶](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#setup "Permanent link")

This guide will use OpenAI's GPT-4o model. We will optionally set our API key for [LangSmith tracing](https://smith.langchain.com/), which will give us best-in-class observability.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-0-1)// process.env.OPENAI_API_KEY = "sk_...";
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-0-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-0-3)// Optional, add tracing in LangSmith
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-0-4)// process.env.LANGCHAIN_API_KEY = "ls__...";
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-0-5)// process.env.LANGCHAIN_CALLBACKS_BACKGROUND = "true";
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-0-6)// process.env.LANGCHAIN_TRACING = "true";
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-0-7)// process.env.LANGCHAIN_PROJECT = "Stream Tokens: LangGraphJS";

```


## Define the state[¶](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#define-the-state "Permanent link")

The state is the interface for all of the nodes in our graph.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-1-1)import{Annotation}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-1-2)importtype{BaseMessageLike}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-1-4)constStateAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-1-5)messages:Annotation<BaseMessageLike[]>({
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-1-6)reducer:(x,y)=>x.concat(y),
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-1-7)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-1-8)});

```


## Set up the tools[¶](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#set-up-the-tools "Permanent link")

First define the tools you want to use. For this simple example, we'll create a placeholder search engine, but see the documentation [here](https://js.langchain.com/docs/how_to/custom_tools) on how to create your own custom tools.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-2-1)import{tool}from"@langchain/core/tools";
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-2-2)import{z}from"zod";
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-2-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-2-4)constsearchTool=tool((_)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-2-5)// This is a placeholder for the actual implementation
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-2-6)return"Cold, with a low of 3℃";
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-2-7)},{
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-2-8)name:"search",
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-2-9)description:
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-2-10)"Use to surf the web, fetch current information, check the weather, and retrieve other information.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-2-11)schema:z.object({
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-2-12)query:z.string().describe("The query to use in your search."),
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-2-13)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-2-14)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-2-15)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-2-16)awaitsearchTool.invoke({query:"What's the weather like?"});
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-2-17)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-2-18)consttools=[searchTool];

```


We can now wrap these tools in a prebuilt [ToolNode](https://langchain-ai.github.io/langgraphjs/reference/classes/langgraph_prebuilt.ToolNode.html). This object will actually run the tools (functions) whenever they are invoked by our LLM.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-3-1)import{ToolNode}from"@langchain/langgraph/prebuilt";
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-3-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-3-3)consttoolNode=newToolNode(tools);

```


## Set up the model[¶](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#set-up-the-model "Permanent link")

Now load the [chat model](https://js.langchain.com/docs/concepts/#chat-models).

  1. It should work with messages. We will represent all agent state in the form of messages, so it needs to be able to work well with them.
  2. It should work with [tool calling](https://js.langchain.com/docs/how_to/tool_calling/#passing-tools-to-llms), meaning it can return function arguments in its response.



Note

These model requirements are not general requirements for using LangGraph - they are just requirements for this one example. 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-4-1)import{ChatOpenAI}from"@langchain/openai";
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-4-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-4-3)constmodel=newChatOpenAI({
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-4-4)model:"gpt-4o-mini",
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-4-5)temperature:0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-4-6)});

```


After you've done this, we should make sure the model knows that it has these tools available to call. We can do this by calling [bindTools](https://v01.api.js.langchain.com/classes/langchain_core_language_models_chat_models.BaseChatModel.html#bindTools).

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-5-1)constboundModel=model.bindTools(tools);

```


## Define the graph[¶](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#define-the-graph "Permanent link")

We can now put it all together.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-6-1)import{StateGraph,END}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-6-2)import{AIMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-6-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-6-4)constrouteMessage=(state:typeofStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-6-5)const{messages}=state;
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-6-6)constlastMessage=messages[messages.length-1]asAIMessage;
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-6-7)// If no tools are called, we can finish (respond to the user)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-6-8)if(!lastMessage?.tool_calls?.length){
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-6-9)returnEND;
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-6-10)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-6-11)// Otherwise if there is, we continue and call the tools
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-6-12)return"tools";
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-6-13)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-6-14)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-6-15)constcallModel=async(
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-6-16)state:typeofStateAnnotation.State,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-6-17))=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-6-18)// For versions of @langchain/core < 0.2.3, you must call `.stream()`
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-6-19)// and aggregate the message from chunks instead of calling `.invoke()`.
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-6-20)const{messages}=state;
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-6-21)constresponseMessage=awaitboundModel.invoke(messages);
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-6-22)return{messages:[responseMessage]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-6-23)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-6-24)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-6-25)constworkflow=newStateGraph(StateAnnotation)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-6-26).addNode("agent",callModel)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-6-27).addNode("tools",toolNode)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-6-28).addEdge("__start__","agent")
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-6-29).addConditionalEdges("agent",routeMessage)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-6-30).addEdge("tools","agent");
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-6-31)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-6-32)constagent=workflow.compile();

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-7-1)import*astslabfrom"tslab";
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-7-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-7-3)construnnableGraph=agent.getGraph();
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-7-4)constimage=awaitrunnableGraph.drawMermaidPng();
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-7-5)constarrayBuffer=awaitimage.arrayBuffer();
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-7-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-7-7)awaittslab.display.png(newUint8Array(arrayBuffer));

```


![]()

## Streaming LLM Tokens[¶](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#streaming-llm-tokens "Permanent link")

You can access the LLM tokens as they are produced by each node with two methods:

  * The `stream` method along with `streamMode: "messages"`
  * The `streamEvents` method



### The stream method[¶](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#the-stream-method "Permanent link")

Compatibility

This section requires `@langchain/langgraph>=0.2.20`. For help upgrading, see [this guide](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/). 

For this method, you must be using an LLM that supports streaming as well (e.g. `new ChatOpenAI({ model: "gpt-4o-mini" })`) or call `.stream` on the internal LLM call.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-8-1)import{isAIMessageChunk}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-8-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-8-3)conststream=awaitagent.stream(
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-8-4){messages:[{role:"user",content:"What's the current weather in Nepal?"}]},
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-8-5){streamMode:"messages"},
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-8-6));
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-8-7)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-8-8)forawait(const[message,_metadata]ofstream){
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-8-9)if(isAIMessageChunk(message)&&message.tool_call_chunks?.length){
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-8-10)console.log(`${message.getType()} MESSAGE TOOL CALL CHUNK: ${message.tool_call_chunks[0].args}`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-8-11)}else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-8-12)console.log(`${message.getType()} MESSAGE CONTENT: ${message.content}`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-8-13)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-8-14)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-9-1)ai MESSAGE TOOL CALL CHUNK: 
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-9-2)ai MESSAGE TOOL CALL CHUNK: {"
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-9-3)ai MESSAGE TOOL CALL CHUNK: query
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-9-4)ai MESSAGE TOOL CALL CHUNK: ":"
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-9-5)ai MESSAGE TOOL CALL CHUNK: current
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-9-6)ai MESSAGE TOOL CALL CHUNK: weather
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-9-7)ai MESSAGE TOOL CALL CHUNK: in
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-9-8)ai MESSAGE TOOL CALL CHUNK: Nepal
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-9-9)ai MESSAGE TOOL CALL CHUNK: "}
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-9-10)ai MESSAGE CONTENT: 
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-9-11)tool MESSAGE CONTENT: Cold, with a low of 3℃
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-9-12)ai MESSAGE CONTENT: 
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-9-13)ai MESSAGE CONTENT: The
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-9-14)ai MESSAGE CONTENT: current
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-9-15)ai MESSAGE CONTENT: weather
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-9-16)ai MESSAGE CONTENT: in
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-9-17)ai MESSAGE CONTENT: Nepal
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-9-18)ai MESSAGE CONTENT: is
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-9-19)ai MESSAGE CONTENT: cold
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-9-20)ai MESSAGE CONTENT: ,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-9-21)ai MESSAGE CONTENT: with
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-9-22)ai MESSAGE CONTENT: a
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-9-23)ai MESSAGE CONTENT: low
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-9-24)ai MESSAGE CONTENT: temperature
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-9-25)ai MESSAGE CONTENT: of
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-9-26)ai MESSAGE CONTENT: 
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-9-27)ai MESSAGE CONTENT: 3
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-9-28)ai MESSAGE CONTENT: ℃
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-9-29)ai MESSAGE CONTENT: .
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-9-30)ai MESSAGE CONTENT:

```


### Disabling streaming[¶](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#disabling-streaming "Permanent link")

If you wish to disable streaming for a given node or model call, you can add a `"nostream"` tag. Here's an example where we add an initial node with an LLM call that will not be streamed in the final output:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-10-1)import{RunnableLambda}from"@langchain/core/runnables";
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-10-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-10-3)constunstreamed=async(_:typeofStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-10-4)constmodel=newChatOpenAI({
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-10-5)model:"gpt-4o-mini",
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-10-6)temperature:0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-10-7)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-10-8)constres=awaitmodel.invoke("How are you?");
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-10-9)console.log("LOGGED UNSTREAMED MESSAGE",res.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-10-10)// Don't update the state, this is just to show a call that won't be streamed
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-10-11)return{};
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-10-12)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-10-13)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-10-14)constagentWithNoStream=newStateGraph(StateAnnotation)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-10-15).addNode("unstreamed",
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-10-16)// Add a "nostream" tag to the entire node
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-10-17)RunnableLambda.from(unstreamed).withConfig({
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-10-18)tags:["nostream"]
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-10-19)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-10-20))
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-10-21).addNode("agent",callModel)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-10-22).addNode("tools",toolNode)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-10-23)// Run the unstreamed node before the agent
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-10-24).addEdge("__start__","unstreamed")
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-10-25).addEdge("unstreamed","agent")
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-10-26).addConditionalEdges("agent",routeMessage)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-10-27).addEdge("tools","agent")
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-10-28).compile();
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-10-29)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-10-30)conststream=awaitagentWithNoStream.stream(
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-10-31){messages:[{role:"user",content:"What's the current weather in Nepal?"}]},
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-10-32){streamMode:"messages"},
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-10-33));
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-10-34)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-10-35)forawait(const[message,_metadata]ofstream){
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-10-36)if(isAIMessageChunk(message)&&message.tool_call_chunks?.length){
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-10-37)console.log(`${message.getType()} MESSAGE TOOL CALL CHUNK: ${message.tool_call_chunks[0].args}`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-10-38)}else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-10-39)console.log(`${message.getType()} MESSAGE CONTENT: ${message.content}`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-10-40)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-10-41)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-11-1)LOGGED UNSTREAMED MESSAGE I'm just a computer program, so I don't have feelings, but I'm here and ready to help you! How can I assist you today?
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-11-2)ai MESSAGE TOOL CALL CHUNK: 
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-11-3)ai MESSAGE TOOL CALL CHUNK: {"
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-11-4)ai MESSAGE TOOL CALL CHUNK: query
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-11-5)ai MESSAGE TOOL CALL CHUNK: ":"
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-11-6)ai MESSAGE TOOL CALL CHUNK: current
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-11-7)ai MESSAGE TOOL CALL CHUNK: weather
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-11-8)ai MESSAGE TOOL CALL CHUNK: in
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-11-9)ai MESSAGE TOOL CALL CHUNK: Nepal
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-11-10)ai MESSAGE TOOL CALL CHUNK: "}
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-11-11)ai MESSAGE CONTENT: 
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-11-12)tool MESSAGE CONTENT: Cold, with a low of 3℃
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-11-13)ai MESSAGE CONTENT: 
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-11-14)ai MESSAGE CONTENT: The
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-11-15)ai MESSAGE CONTENT: current
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-11-16)ai MESSAGE CONTENT: weather
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-11-17)ai MESSAGE CONTENT: in
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-11-18)ai MESSAGE CONTENT: Nepal
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-11-19)ai MESSAGE CONTENT: is
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-11-20)ai MESSAGE CONTENT: cold
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-11-21)ai MESSAGE CONTENT: ,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-11-22)ai MESSAGE CONTENT: with
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-11-23)ai MESSAGE CONTENT: a
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-11-24)ai MESSAGE CONTENT: low
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-11-25)ai MESSAGE CONTENT: temperature
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-11-26)ai MESSAGE CONTENT: of
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-11-27)ai MESSAGE CONTENT: 
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-11-28)ai MESSAGE CONTENT: 3
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-11-29)ai MESSAGE CONTENT: ℃
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-11-30)ai MESSAGE CONTENT: .
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-11-31)ai MESSAGE CONTENT:

```


If you removed the tag from the `"unstreamed"` node, the result of the model call within would also be in the final stream. 

### The streamEvents method[¶](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#the-streamevents-method "Permanent link")

You can also use the `streamEvents` method like this:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-12-1)consteventStream=awaitagent.streamEvents(
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-12-2){messages:[{role:"user",content:"What's the weather like today?"}]},
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-12-3){
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-12-4)version:"v2",
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-12-5)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-12-6));
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-12-7)
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-12-8)forawait(const{event,data}ofeventStream){
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-12-9)if(event==="on_chat_model_stream"&&isAIMessageChunk(data.chunk)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-12-10)if(data.chunk.tool_call_chunks!==undefined&&data.chunk.tool_call_chunks.length>0){
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-12-11)console.log(data.chunk.tool_call_chunks);
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-12-12)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-12-13)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-12-14)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-1)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-2) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-3)  name: 'search',
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-4)  args: '',
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-5)  id: 'call_Qpd6frHt0yUYWynRbZEXF3le',
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-6)  index: 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-7)  type: 'tool_call_chunk'
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-8) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-9)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-10)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-11) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-12)  name: undefined,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-13)  args: '{"',
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-14)  id: undefined,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-15)  index: 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-16)  type: 'tool_call_chunk'
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-17) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-18)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-19)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-20) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-21)  name: undefined,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-22)  args: 'query',
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-23)  id: undefined,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-24)  index: 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-25)  type: 'tool_call_chunk'
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-26) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-27)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-28)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-29) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-30)  name: undefined,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-31)  args: '":"',
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-32)  id: undefined,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-33)  index: 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-34)  type: 'tool_call_chunk'
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-35) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-36)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-37)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-38) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-39)  name: undefined,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-40)  args: 'current',
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-41)  id: undefined,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-42)  index: 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-43)  type: 'tool_call_chunk'
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-44) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-45)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-46)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-47) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-48)  name: undefined,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-49)  args: ' weather',
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-50)  id: undefined,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-51)  index: 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-52)  type: 'tool_call_chunk'
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-53) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-54)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-55)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-56) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-57)  name: undefined,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-58)  args: ' today',
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-59)  id: undefined,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-60)  index: 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-61)  type: 'tool_call_chunk'
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-62) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-63)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-64)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-65) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-66)  name: undefined,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-67)  args: '"}',
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-68)  id: undefined,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-69)  index: 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-70)  type: 'tool_call_chunk'
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-71) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__codelineno-13-72)]

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to stream state updates of your graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-updates/) [ Next  How to stream LLM tokens (without LangChain models)  ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
