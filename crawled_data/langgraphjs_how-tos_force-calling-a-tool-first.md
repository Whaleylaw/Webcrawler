---
url: https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#how-to-force-an-agent-to-call-a-tool)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to force an agent to call a tool 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/?q= "Share")

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
          * Tool calling  Tool calling 
            * [ Tool calling  ](https://langchain-ai.github.io/langgraphjs/how-tos#tool-calling)
            * [ How to call tools using ToolNode  ](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/)
            * How to force an agent to call a tool  [ How to force an agent to call a tool  ](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#setup)
              * [ Set up the tools  ](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#set-up-the-tools)
              * [ Set up the model  ](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#set-up-the-model)
              * [ Define the agent state  ](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#define-the-agent-state)
              * [ Define the nodes  ](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#define-the-nodes)
              * [ Define the graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#define-the-graph)
              * [ Use it!  ](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#use-it)
            * [ How to handle tool calling errors  ](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/)
            * [ How to pass runtime values to tools  ](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/)
            * [ How to update graph state from tools  ](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#setup)
  * [ Set up the tools  ](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#set-up-the-tools)
  * [ Set up the model  ](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#set-up-the-model)
  * [ Define the agent state  ](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#define-the-agent-state)
  * [ Define the nodes  ](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#define-the-nodes)
  * [ Define the graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#define-the-graph)
  * [ Use it!  ](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#use-it)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
  5. [ Tool calling  ](https://langchain-ai.github.io/langgraphjs/how-tos#tool-calling)



# How to force an agent to call a tool[¶](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#how-to-force-an-agent-to-call-a-tool "Permanent link")

In this example we will build a ReAct agent that **always** calls a certain tool first, before making any plans. In this example, we will create an agent with a search tool. However, at the start we will force the agent to call the search tool (and then let it do whatever it wants after). This is useful when you know you want to execute specific actions in your application but also want the flexibility of letting the LLM follow up on the user's query after going through that fixed sequence.

## Setup[¶](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#setup "Permanent link")

First we need to install the packages required

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-0-1)yarnadd@langchain/langgraph@langchain/openai@langchain/core

```


Next, we need to set API keys for OpenAI (the LLM we will use). Optionally, we can set API key for [LangSmith tracing](https://smith.langchain.com/), which will give us best-in-class observability.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-1-1)// process.env.OPENAI_API_KEY = "sk_...";
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-1-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-1-3)// Optional, add tracing in LangSmith
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-1-4)// process.env.LANGCHAIN_API_KEY = "ls__...";
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-1-5)// process.env.LANGCHAIN_CALLBACKS_BACKGROUND = "true";
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-1-6)process.env.LANGCHAIN_TRACING_V2="true";
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-1-7)process.env.LANGCHAIN_PROJECT="Force Calling a Tool First: LangGraphJS";

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-2-1)Force Calling a Tool First: LangGraphJS

```


## Set up the tools[¶](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#set-up-the-tools "Permanent link")

We will first define the tools we want to use. For this simple example, we will use a built-in search tool via Tavily. However, it is really easy to create your own tools - see documentation [here](https://js.langchain.com/docs/modules/agents/tools/dynamic) on how to do that.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-3-1)import{DynamicStructuredTool}from"@langchain/core/tools";
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-3-2)import{z}from"zod";
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-3-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-3-4)constsearchTool=newDynamicStructuredTool({
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-3-5)name:"search",
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-3-6)description:
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-3-7)"Use to surf the web, fetch current information, check the weather, and retrieve other information.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-3-8)schema:z.object({
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-3-9)query:z.string().describe("The query to use in your search."),
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-3-10)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-3-11)func:async({}:{query:string})=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-3-12)// This is a placeholder for the actual implementation
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-3-13)return"Cold, with a low of 13 ℃";
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-3-14)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-3-15)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-3-16)
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-3-17)awaitsearchTool.invoke({query:"What's the weather like?"});
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-3-18)
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-3-19)consttools=[searchTool];

```


We can now wrap these tools in a `ToolNode`. This is a prebuilt node that takes in a LangChain chat model's generated tool call and calls that tool, returning the output.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-4-1)import{ToolNode}from"@langchain/langgraph/prebuilt";
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-4-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-4-3)consttoolNode=newToolNode(tools);

```


## Set up the model[¶](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#set-up-the-model "Permanent link")

Now we need to load the chat model we want to use.\ Importantly, this should satisfy two criteria:

  1. It should work with messages. We will represent all agent state in the form of messages, so it needs to be able to work well with them.
  2. It should work with OpenAI function calling. This means it should either be an OpenAI model or a model that exposes a similar interface.



Note: these model requirements are not requirements for using LangGraph - they are just requirements for this one example.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-5-1)import{ChatOpenAI}from"@langchain/openai";
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-5-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-5-3)constmodel=newChatOpenAI({
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-5-4)temperature:0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-5-5)model:"gpt-4o",
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-5-6)});

```


After we've done this, we should make sure the model knows that it has these tools available to call. We can do this by converting the LangChain tools into the format for OpenAI function calling, and then bind them to the model class.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-6-1)constboundModel=model.bindTools(tools);

```


## Define the agent state[¶](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#define-the-agent-state "Permanent link")

The main type of graph in `langgraph` is the `StateGraph`. This graph is parameterized by a state object that it passes around to each node. Each node then returns operations to update that state.

For this example, the state we will track will just be a list of messages. We want each node to just add messages to that list. Therefore, we will define the agent state as an object with one key (`messages`) with the value specifying how to update the state.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-7-1)import{Annotation}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-7-2)import{BaseMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-7-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-7-4)constAgentState=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-7-5)messages:Annotation<BaseMessage[]>({
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-7-6)reducer:(x,y)=>x.concat(y),
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-7-7)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-7-8)});

```


## Define the nodes[¶](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#define-the-nodes "Permanent link")

We now need to define a few different nodes in our graph. In `langgraph`, a node can be either a function or a [runnable](https://js.langchain.com/docs/expression_language/). There are two main nodes we need for this:

  1. The agent: responsible for deciding what (if any) actions to take.
  2. A function to invoke tools: if the agent decides to take an action, this node will then execute that action.



We will also need to define some edges. Some of these edges may be conditional. The reason they are conditional is that based on the output of a node, one of several paths may be taken. The path that is taken is not known until that node is run (the LLM decides).

  1. Conditional Edge: after the agent is called, we should either: a. If the agent said to take an action, then the function to invoke tools should be called\ b. If the agent said that it was finished, then it should finish
  2. Normal Edge: after the tools are invoked, it should always go back to the agent to decide what to do next



Let's define the nodes, as well as a function to decide how what conditional edge to take.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-8-1)import{AIMessage,AIMessageChunk}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-8-2)import{RunnableConfig}from"@langchain/core/runnables";
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-8-3)import{concat}from"@langchain/core/utils/stream";
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-8-4)
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-8-5)// Define logic that will be used to determine which conditional edge to go down
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-8-6)constshouldContinue=(state:typeofAgentState.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-8-7)const{messages}=state;
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-8-8)constlastMessage=messages[messages.length-1]asAIMessage;
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-8-9)// If there is no function call, then we finish
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-8-10)if(!lastMessage.tool_calls||lastMessage.tool_calls.length===0){
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-8-11)return"end";
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-8-12)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-8-13)// Otherwise if there is, we continue
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-8-14)return"continue";
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-8-15)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-8-16)
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-8-17)// Define the function that calls the model
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-8-18)constcallModel=async(
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-8-19)state:typeofAgentState.State,
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-8-20)config?:RunnableConfig,
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-8-21))=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-8-22)const{messages}=state;
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-8-23)letresponse:AIMessageChunk|undefined;
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-8-24)forawait(constmessageofawaitboundModel.stream(messages,config)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-8-25)if(!response){
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-8-26)response=message;
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-8-27)}else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-8-28)response=concat(response,message);
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-8-29)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-8-30)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-8-31)// We return an object, because this will get added to the existing list
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-8-32)return{
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-8-33)messages:response?[responseasAIMessage]:[],
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-8-34)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-8-35)};

```


**MODIFICATION**

Here we create a node that returns an AIMessage with a tool call - we will use this at the start to force it call a tool

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-9-1)// This is the new first - the first call of the model we want to explicitly hard-code some action
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-9-2)constfirstModel=async(state:typeofAgentState.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-9-3)consthumanInput=state.messages[state.messages.length-1].content||"";
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-9-4)return{
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-9-5)messages:[
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-9-6)newAIMessage({
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-9-7)content:"",
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-9-8)tool_calls:[
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-9-9){
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-9-10)name:"search",
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-9-11)args:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-9-12)query:humanInput,
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-9-13)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-9-14)id:"tool_abcd123",
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-9-15)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-9-16)],
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-9-17)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-9-18)],
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-9-19)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-9-20)};

```


## Define the graph[¶](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#define-the-graph "Permanent link")

We can now put it all together and define the graph!

**MODIFICATION**

We will define a `firstModel` node which we will set as the entrypoint.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-10-1)import{END,START,StateGraph}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-10-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-10-3)// Define a new graph
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-10-4)constworkflow=newStateGraph(AgentState)
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-10-5)// Define the new entrypoint
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-10-6).addNode("first_agent",firstModel)
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-10-7)// Define the two nodes we will cycle between
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-10-8).addNode("agent",callModel)
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-10-9).addNode("action",toolNode)
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-10-10)// Set the entrypoint as `first_agent`
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-10-11)// by creating an edge from the virtual __start__ node to `first_agent`
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-10-12).addEdge(START,"first_agent")
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-10-13)// We now add a conditional edge
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-10-14).addConditionalEdges(
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-10-15)// First, we define the start node. We use `agent`.
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-10-16)// This means these are the edges taken after the `agent` node is called.
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-10-17)"agent",
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-10-18)// Next, we pass in the function that will determine which node is called next.
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-10-19)shouldContinue,
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-10-20)// Finally we pass in a mapping.
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-10-21)// The keys are strings, and the values are other nodes.
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-10-22)// END is a special node marking that the graph should finish.
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-10-23)// What will happen is we will call `should_continue`, and then the output of that
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-10-24)// will be matched against the keys in this mapping.
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-10-25)// Based on which one it matches, that node will then be called.
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-10-26){
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-10-27)// If `tools`, then we call the tool node.
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-10-28)continue:"action",
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-10-29)// Otherwise we finish.
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-10-30)end:END,
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-10-31)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-10-32))
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-10-33)// We now add a normal edge from `tools` to `agent`.
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-10-34)// This means that after `tools` is called, `agent` node is called next.
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-10-35).addEdge("action","agent")
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-10-36)// After we call the first agent, we know we want to go to action
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-10-37).addEdge("first_agent","action");
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-10-38)
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-10-39)// Finally, we compile it!
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-10-40)// This compiles it into a LangChain Runnable,
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-10-41)// meaning you can use it as you would any other runnable
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-10-42)constapp=workflow.compile();

```


## Use it![¶](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#use-it "Permanent link")

We can now use it! This now exposes the [same interface](https://js.langchain.com/docs/expression_language/) as all other LangChain runnables.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-11-1)import{HumanMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-11-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-11-3)constinputs={
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-11-4)messages:[newHumanMessage("what is the weather in sf")],
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-11-5)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-11-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-11-7)forawait(constoutputofawaitapp.stream(inputs)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-11-8)console.log(output);
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-11-9)console.log("-----\n");
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-11-10)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-1){
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-2) first_agent: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-3)  messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-4)   AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-5)    "content": "",
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-6)    "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-7)    "response_metadata": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-8)    "tool_calls": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-9)     {
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-10)      "name": "search",
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-11)      "args": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-12)       "query": "what is the weather in sf"
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-13)      },
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-14)      "id": "tool_abcd123"
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-15)     }
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-16)    ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-17)    "invalid_tool_calls": []
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-18)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-19)  ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-20) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-21)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-22)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-23)
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-24){
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-25) action: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-26)  messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-27)   ToolMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-28)    "content": "Cold, with a low of 13 ℃",
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-29)    "name": "search",
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-30)    "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-31)    "response_metadata": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-32)    "tool_call_id": "tool_abcd123"
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-33)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-34)  ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-35) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-36)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-37)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-38)
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-39){
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-40) agent: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-41)  messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-42)   AIMessageChunk {
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-43)    "id": "chatcmpl-9y562g16z0MUNBJcS6nKMsDuFMRsS",
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-44)    "content": "The current weather in San Francisco is cold, with a low of 13°C.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-45)    "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-46)    "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-47)     "prompt": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-48)     "completion": 0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-49)     "finish_reason": "stop",
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-50)     "system_fingerprint": "fp_3aa7262c27fp_3aa7262c27fp_3aa7262c27fp_3aa7262c27fp_3aa7262c27fp_3aa7262c27fp_3aa7262c27fp_3aa7262c27fp_3aa7262c27fp_3aa7262c27fp_3aa7262c27fp_3aa7262c27fp_3aa7262c27fp_3aa7262c27fp_3aa7262c27fp_3aa7262c27fp_3aa7262c27fp_3aa7262c27fp_3aa7262c27"
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-51)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-52)    "tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-53)    "tool_call_chunks": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-54)    "invalid_tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-55)    "usage_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-56)     "input_tokens": 104,
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-57)     "output_tokens": 18,
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-58)     "total_tokens": 122
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-59)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-60)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-61)  ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-62) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-63)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__codelineno-12-64)-----

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to call tools using ToolNode  ](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/) [ Next  How to handle tool calling errors  ](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
