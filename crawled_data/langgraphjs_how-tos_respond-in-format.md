---
url: https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#how-to-have-agent-respond-in-structured-format)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to have agent respond in structured format 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/?q= "Share")

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
          * Other  Other 
            * [ Other  ](https://langchain-ai.github.io/langgraphjs/how-tos#other)
            * [ How to add runtime configuration to your graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/)
            * [ How to add node retry policies  ](https://langchain-ai.github.io/langgraphjs/how-tos/node-retry-policies/)
            * [ How to let agent return tool results directly  ](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/)
            * How to have agent respond in structured format  [ How to have agent respond in structured format  ](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#setup)
              * [ Set up the State  ](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#set-up-the-state)
              * [ Set up the tools  ](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#set-up-the-tools)
              * [ Set up the model  ](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#set-up-the-model)
              * [ Define the nodes  ](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#define-the-nodes)
              * [ Define the graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#define-the-graph)
              * [ Use it!  ](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#use-it)
              * [ Partially streaming JSON  ](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#partially-streaming-json)
            * [ How to manage agent steps  ](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#setup)
  * [ Set up the State  ](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#set-up-the-state)
  * [ Set up the tools  ](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#set-up-the-tools)
  * [ Set up the model  ](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#set-up-the-model)
  * [ Define the nodes  ](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#define-the-nodes)
  * [ Define the graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#define-the-graph)
  * [ Use it!  ](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#use-it)
  * [ Partially streaming JSON  ](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#partially-streaming-json)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
  5. [ Other  ](https://langchain-ai.github.io/langgraphjs/how-tos#other)



# How to have agent respond in structured format[¶](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#how-to-have-agent-respond-in-structured-format "Permanent link")

The typical ReAct agent prompts the LLM to respond in 1 of two formats: a function call (~ JSON) to use a tool, or conversational text to respond to the user.

If your agent is connected to a structured (or even generative) UI, or if it is communicating with another agent or software process, you may want it to resopnd in a specific structured format.

In this example we will build a conversational ReAct agent that responds in a specific format. We will do this by using [tool calling](https://js.langchain.com/docs/modules/model_io/models/chat/function-calling/). This is useful when you want to enforce that an agent's response is in a specific format. In this example, we will ask it respond as if it were a weatherman, returning the temperature and additional info in separate, machine-readable fields.

## Setup[¶](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#setup "Permanent link")

First we need to install the packages required

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-0-1)yarnaddlangchain@langchain/anthropic@langchain/langgraph@langchain/core

```


Next, we need to set API keys for OpenAI (the LLM we will use).

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-1-1)// process.env.OPENAI_API_KEY = "sk_...";

```


Optionally, we can set API key for [LangSmith tracing](https://smith.langchain.com/), which will give us best-in-class observability.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-2-1)// process.env.LANGCHAIN_API_KEY = "ls...";
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-2-2)process.env.LANGCHAIN_CALLBACKS_BACKGROUND="true";
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-2-3)process.env.LANGCHAIN_TRACING_V2="true";
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-2-4)process.env.LANGCHAIN_PROJECT="Respond in Format: LangGraphJS";

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-3-1)Respond in Format: LangGraphJS

```


## Set up the State[¶](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#set-up-the-state "Permanent link")

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-4-1)import{Annotation,messagesStateReducer}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-4-2)import{BaseMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-4-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-4-4)constGraphState=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-4-5)messages:Annotation<BaseMessage[]>({
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-4-6)reducer:messagesStateReducer,
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-4-7)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-4-8)});

```


## Set up the tools[¶](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#set-up-the-tools "Permanent link")

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-5-1)import{tool}from"@langchain/core/tools";
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-5-2)import{z}from"zod";
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-5-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-5-4)constsearchTool=tool((_)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-5-5)// This is a placeholder, but don't tell the LLM that...
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-5-6)return"67 degrees. Cloudy with a chance of rain.";
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-5-7)},{
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-5-8)name:"search",
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-5-9)description:"Call to surf the web.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-5-10)schema:z.object({
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-5-11)query:z.string().describe("The query to use in your search."),
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-5-12)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-5-13)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-5-14)
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-5-15)consttools=[searchTool];

```


We can now wrap these tools in a [ToolNode](https://langchain-ai.github.io/langgraphjs/reference/classes/langgraph_prebuilt.ToolNode.html).

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-6-1)import{ToolNode}from"@langchain/langgraph/prebuilt";
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-6-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-6-3)consttoolNode=newToolNode<typeofGraphState.State>(tools);

```


## Set up the model[¶](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#set-up-the-model "Permanent link")

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-7-1)import{ChatOpenAI}from"@langchain/openai";
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-7-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-7-3)constmodel=newChatOpenAI({
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-7-4)temperature:0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-7-5)model:"gpt-4o",
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-7-6)});

```


After we've done this, we should make sure the model knows that it has these tools available to call. We can do this by binding the LangChain tools to the model class.

We also want to define a response schema for the language model and bind it to the model as a tool. The idea is that when the model is ready to respond, it'll call this final tool and populate arguments for it according to the schema we want. Rather than calling a tool, we'll instead return from the graph.

Because we only intend to use this final tool to guide the schema of the model's final response, we'll declare it with a mocked out function:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-8-1)import{tool}from"@langchain/core/tools";
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-8-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-8-3)constResponse=z.object({
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-8-4)temperature:z.number().describe("the temperature"),
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-8-5)other_notes:z.string().describe("any other notes about the weather"),
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-8-6)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-8-7)
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-8-8)constfinalResponseTool=tool(async()=>"mocked value",{
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-8-9)name:"Response",
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-8-10)description:"Always respond to the user using this tool.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-8-11)schema:Response
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-8-12)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-8-13)
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-8-14)constboundModel=model.bindTools([
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-8-15)...tools,
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-8-16)finalResponseTool
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-8-17)]);

```


## Define the nodes[¶](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#define-the-nodes "Permanent link")

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-9-1)import{AIMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-9-2)import{RunnableConfig}from"@langchain/core/runnables";
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-9-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-9-4)// Define the function that determines whether to continue or not
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-9-5)constroute=(state:typeofGraphState.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-9-6)const{messages}=state;
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-9-7)constlastMessage=messages[messages.length-1]asAIMessage;
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-9-8)// If there is no function call, then we finish
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-9-9)if(!lastMessage.tool_calls||lastMessage.tool_calls.length===0){
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-9-10)return"__end__";
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-9-11)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-9-12)// Otherwise if there is, we need to check what type of function call it is
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-9-13)if(lastMessage.tool_calls[0].name==="Response"){
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-9-14)return"__end__";
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-9-15)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-9-16)// Otherwise we continue
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-9-17)return"tools";
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-9-18)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-9-19)
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-9-20)// Define the function that calls the model
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-9-21)constcallModel=async(
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-9-22)state:typeofGraphState.State,
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-9-23)config?:RunnableConfig,
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-9-24))=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-9-25)const{messages}=state;
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-9-26)constresponse=awaitboundModel.invoke(messages,config);
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-9-27)// We return an object, because this will get added to the existing list
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-9-28)return{messages:[response]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-9-29)};

```


## Define the graph[¶](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#define-the-graph "Permanent link")

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-10-1)import{StateGraph}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-10-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-10-3)// Define a new graph
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-10-4)constworkflow=newStateGraph(GraphState)
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-10-5).addNode("agent",callModel)
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-10-6).addNode("tools",toolNode)
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-10-7).addEdge("__start__","agent")
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-10-8).addConditionalEdges(
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-10-9)// First, we define the start node. We use `agent`.
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-10-10)// This means these are the edges taken after the `agent` node is called.
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-10-11)"agent",
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-10-12)// Next, we pass in the function that will determine which node is called next.
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-10-13)route,
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-10-14)// We supply a map of possible response values to the conditional edge
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-10-15)// to make it possible to draw a visualization of the graph.
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-10-16){
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-10-17)__end__:"__end__",
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-10-18)tools:"tools",
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-10-19)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-10-20))
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-10-21)// We now add a normal edge from `tools` to `agent`.
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-10-22)// This means that after `tools` is called, `agent` node is called next.
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-10-23).addEdge("tools","agent");
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-10-24)
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-10-25)// Finally, we compile it!
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-10-26)// This compiles it into a LangChain Runnable,
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-10-27)// meaning you can use it as you would any other runnable
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-10-28)constapp=workflow.compile();

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-11-1)import*astslabfrom"tslab";
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-11-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-11-3)constgraph=app.getGraph();
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-11-4)constimage=awaitgraph.drawMermaidPng();
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-11-5)constarrayBuffer=awaitimage.arrayBuffer();
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-11-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-11-7)awaittslab.display.png(newUint8Array(arrayBuffer));

```


![]()

## Use it![¶](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#use-it "Permanent link")

We can now use it! This now exposes the [same interface](https://v02.api.js.langchain.com/classes/langchain_core_runnables.Runnable.html) as all other LangChain runnables.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-12-1)import{HumanMessage,isAIMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-12-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-12-3)constprettyPrint=(message:BaseMessage)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-12-4)lettxt=`[${message._getType()}]: ${message.content}`;
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-12-5)if(
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-12-6)isAIMessage(message)&&message?.tool_calls?.length
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-12-7)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-12-8)consttool_calls=message?.tool_calls
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-12-9)?.map((tc)=>`- ${tc.name}(${JSON.stringify(tc.args)})`)
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-12-10).join("\n");
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-12-11)txt+=` \nTools: \n${tool_calls}`;
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-12-12)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-12-13)console.log(txt);
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-12-14)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-12-15)
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-12-16)constinputs={
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-12-17)messages:[newHumanMessage("what is the weather in sf")],
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-12-18)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-12-19)
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-12-20)conststream=awaitapp.stream(inputs,{streamMode:"values"});
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-12-21)
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-12-22)forawait(constoutputofstream){
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-12-23)const{messages}=output;
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-12-24)prettyPrint(messages[messages.length-1]);
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-12-25)console.log("\n---\n");
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-12-26)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-13-1)[human]: what is the weather in sf
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-13-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-13-3)---
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-13-4)
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-13-5)[ai]: 
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-13-6)Tools: 
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-13-7)- search({"query":"current weather in San Francisco"})
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-13-8)
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-13-9)---
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-13-10)
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-13-11)[tool]: 67 degrees. Cloudy with a chance of rain.
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-13-12)
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-13-13)---
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-13-14)
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-13-15)[ai]: 
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-13-16)Tools: 
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-13-17)- Response({"temperature":67,"other_notes":"Cloudy with a chance of rain."})
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-13-18)
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-13-19)---

```


## Partially streaming JSON[¶](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#partially-streaming-json "Permanent link")

If we want to stream the structured output as soon as it's available, we can use the `.streamEvents()`[](https://js.langchain.com/docs/how_to/streaming#using-stream-events) method. We'll aggregate emitted `on_chat_model_events` and inspect the name field. As soon as we detect that the model is calling the final output tool, we can start logging the relevant chunks.

Here's an example:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-14-1)import{concat}from"@langchain/core/utils/stream";
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-14-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-14-3)consteventStream=awaitapp.streamEvents(inputs,{version:"v2"});
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-14-4)
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-14-5)letaggregatedChunk;
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-14-6)forawait(const{event,data}ofeventStream){
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-14-7)if(event==="on_chat_model_stream"){
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-14-8)const{chunk}=data;
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-14-9)if(aggregatedChunk===undefined){
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-14-10)aggregatedChunk=chunk;
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-14-11)}else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-14-12)aggregatedChunk=concat(aggregatedChunk,chunk);
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-14-13)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-14-14)constcurrentToolCalls=aggregatedChunk.tool_calls;
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-14-15)if(
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-14-16)currentToolCalls.length===0||
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-14-17)currentToolCalls[0].name===""||
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-14-18)!finalResponseTool.name.startsWith(currentToolCalls[0].name)
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-14-19)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-14-20)// No tool calls or a different tool call in the message,
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-14-21)// so drop what's currently aggregated and start over
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-14-22)aggregatedChunk=undefined;
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-14-23)}elseif(currentToolCalls[0].name===finalResponseTool.name){
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-14-24)// Now we're sure that this event is part of the final output!
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-14-25)// Log the partially aggregated args.
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-14-26)console.log(aggregatedChunk.tool_call_chunks[0].args);
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-14-27)
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-14-28)// You can also log the raw args instead:
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-14-29)// console.log(chunk.tool_call_chunks);
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-14-30)
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-14-31)console.log("---");
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-14-32)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-14-33)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-14-34)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-14-35)// Final aggregated tool call
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-14-36)console.log(aggregatedChunk.tool_calls);

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-15-1)---
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-15-2){"
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-15-3)---
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-15-4){"temperature
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-15-5)---
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-15-6){"temperature":
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-15-7)---
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-15-8){"temperature":67
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-15-9)---
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-15-10){"temperature":67,"
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-15-11)---
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-15-12){"temperature":67,"other
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-15-13)---
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-15-14){"temperature":67,"other_notes
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-15-15)---
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-15-16){"temperature":67,"other_notes":"
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-15-17)---
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-15-18){"temperature":67,"other_notes":"Cloud
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-15-19)---
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-15-20){"temperature":67,"other_notes":"Cloudy
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-15-21)---
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-15-22){"temperature":67,"other_notes":"Cloudy with
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-15-23)---
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-15-24){"temperature":67,"other_notes":"Cloudy with a
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-15-25)---
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-15-26){"temperature":67,"other_notes":"Cloudy with a chance
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-15-27)---
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-15-28){"temperature":67,"other_notes":"Cloudy with a chance of
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-15-29)---
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-15-30){"temperature":67,"other_notes":"Cloudy with a chance of rain
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-15-31)---
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-15-32){"temperature":67,"other_notes":"Cloudy with a chance of rain."
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-15-33)---
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-15-34){"temperature":67,"other_notes":"Cloudy with a chance of rain."}
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-15-35)---
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-15-36){"temperature":67,"other_notes":"Cloudy with a chance of rain."}
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-15-37)---
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-15-38)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-15-39) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-15-40)  name: 'Response',
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-15-41)  args: { temperature: 67, other_notes: 'Cloudy with a chance of rain.' },
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-15-42)  id: 'call_oOhNx2SdeelXn6tbenokDtkO',
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-15-43)  type: 'tool_call'
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-15-44) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__codelineno-15-45)]

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to let agent return tool results directly  ](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/) [ Next  How to manage agent steps  ](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
