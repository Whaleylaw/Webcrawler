---
url: https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#how-to-let-agent-return-tool-results-directly)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to let agent return tool results directly 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/?q= "Share")

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
            * How to let agent return tool results directly  [ How to let agent return tool results directly  ](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#setup)
              * [ Set up the tools  ](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#set-up-the-tools)
              * [ Set up the model  ](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#set-up-the-model)
              * [ Define the agent state  ](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#define-the-agent-state)
              * [ Define the nodes  ](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#define-the-nodes)
              * [ Define the graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#define-the-graph)
              * [ Use it!  ](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#use-it)
            * [ How to have agent respond in structured format  ](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#setup)
  * [ Set up the tools  ](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#set-up-the-tools)
  * [ Set up the model  ](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#set-up-the-model)
  * [ Define the agent state  ](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#define-the-agent-state)
  * [ Define the nodes  ](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#define-the-nodes)
  * [ Define the graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#define-the-graph)
  * [ Use it!  ](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#use-it)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
  5. [ Other  ](https://langchain-ai.github.io/langgraphjs/how-tos#other)



# How to let agent return tool results directly[¶](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#how-to-let-agent-return-tool-results-directly "Permanent link")

A typical ReAct loop follows user -> assistant -> tool -> assistant ..., -> user. In some cases, you don't need to call the LLM after the tool completes, the user can view the results directly themselves.

In this example we will build a conversational ReAct agent where the LLM can optionally decide to return the result of a tool call as the final answer. This is useful in cases where you have tools that can sometimes generate responses that are acceptable as final answers, and you want to use the LLM to determine when that is the case

## Setup[¶](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#setup "Permanent link")

First we need to install the required packages:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-0-1)yarnadd@langchain/langgraph@langchain/openai@langchain/core

```


Next, we need to set API keys for OpenAI (the LLM we will use). Optionally, we can set API key for [LangSmith tracing](https://smith.langchain.com/), which will give us best-in-class observability.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-1-1)// process.env.OPENAI_API_KEY = "sk_...";
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-1-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-1-3)// Optional, add tracing in LangSmith
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-1-4)// process.env.LANGCHAIN_API_KEY = "ls__..."
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-1-5)process.env.LANGCHAIN_CALLBACKS_BACKGROUND="true";
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-1-6)process.env.LANGCHAIN_TRACING_V2="true";
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-1-7)process.env.LANGCHAIN_PROJECT="Direct Return: LangGraphJS";

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-2-1)Direct Return: LangGraphJS

```


## Set up the tools[¶](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#set-up-the-tools "Permanent link")

We will first define the tools we want to use. For this simple example, we will use a simple placeholder "search engine". However, it is really easy to create your own tools - see documentation [here](https://js.langchain.com/docs/modules/agents/tools/dynamic) on how to do that.

To add a 'return_direct' option, we will create a custom zod schema to use **instead of** the schema that would be automatically inferred by the tool.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-3-1)import{DynamicStructuredTool}from"@langchain/core/tools";
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-3-2)import{z}from"zod";
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-3-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-3-4)constSearchTool=z.object({
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-3-5)query:z.string().describe("query to look up online"),
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-3-6)// **IMPORTANT** We are adding an **extra** field here
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-3-7)// that isn't used directly by the tool - it's used by our
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-3-8)// graph instead to determine whether or not to return the
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-3-9)// result directly to the user
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-3-10)return_direct:z.boolean()
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-3-11).describe(
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-3-12)"Whether or not the result of this should be returned directly to the user without you seeing what it is",
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-3-13))
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-3-14).default(false),
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-3-15)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-3-16)
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-3-17)constsearchTool=newDynamicStructuredTool({
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-3-18)name:"search",
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-3-19)description:"Call to surf the web.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-3-20)// We are overriding the default schema here to
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-3-21)// add an extra field
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-3-22)schema:SearchTool,
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-3-23)func:async({}:{query:string})=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-3-24)// This is a placeholder for the actual implementation
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-3-25)// Don't let the LLM know this though 😊
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-3-26)return"It's sunny in San Francisco, but you better look out if you're a Gemini 😈.";
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-3-27)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-3-28)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-3-29)
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-3-30)consttools=[searchTool];

```


We can now wrap these tools in a `ToolNode`. This is a prebuilt node that takes in a LangChain chat model's generated tool call and calls that tool, returning the output.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-4-1)import{ToolNode}from"@langchain/langgraph/prebuilt";
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-4-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-4-3)consttoolNode=newToolNode(tools);

```


## Set up the model[¶](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#set-up-the-model "Permanent link")

Now we need to load the chat model we want to use.\ Importantly, this should satisfy two criteria:

  1. It should work with messages. We will represent all agent state in the form of messages, so it needs to be able to work well with them.
  2. It should support [tool calling](https://js.langchain.com/docs/concepts/tool_calling/).



Note: these model requirements are not requirements for using LangGraph - they are just requirements for this one example.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-5-1)import{ChatOpenAI}from"@langchain/openai";
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-5-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-5-3)constmodel=newChatOpenAI({
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-5-4)temperature:0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-5-5)model:"gpt-3.5-turbo",
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-5-6)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-5-7)// This formats the tools as json schema for the model API.
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-5-8)// The model then uses this like a system prompt.
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-5-9)constboundModel=model.bindTools(tools);

```


## Define the agent state[¶](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#define-the-agent-state "Permanent link")

The main type of graph in `langgraph` is the [StateGraph](https://langchain-ai.github.io/langgraphjs/reference/classes/langgraph.StateGraph.html).

This graph is parameterized by a state object that it passes around to each node. Each node then returns operations to update that state. These operations can either SET specific attributes on the state (e.g. overwrite the existing values) or ADD to the existing attribute. Whether to set or add is denoted in the state object you construct the graph with.

For this example, the state we will track will just be a list of messages. We want each node to just add messages to that list. Therefore, we will define the state as follows:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-6-1)import{Annotation}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-6-2)import{BaseMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-6-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-6-4)constAgentState=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-6-5)messages:Annotation<BaseMessage[]>({
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-6-6)reducer:(x,y)=>x.concat(y),
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-6-7)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-6-8)});

```


## Define the nodes[¶](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#define-the-nodes "Permanent link")

We now need to define a few different nodes in our graph. In `langgraph`, a node can be either a function or a [runnable](https://js.langchain.com/docs/expression_language/). There are two main nodes we need for this:

  1. The agent: responsible for deciding what (if any) actions to take.
  2. A function to invoke tools: if the agent decides to take an action, this node will then execute that action.



We will also need to define some edges. Some of these edges may be conditional. The reason they are conditional is that based on the output of a node, one of several paths may be taken. The path that is taken is not known until that node is run (the LLM decides).

  1. Conditional Edge: after the agent is called, we should either: a. If the agent said to take an action, then the function to invoke tools should be called b. If the agent said that it was finished, then it should finish
  2. Normal Edge: after the tools are invoked, it should always go back to the agent to decide what to do next



Let's define the nodes, as well as a function to decide how what conditional edge to take.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-7-1)import{RunnableConfig}from"@langchain/core/runnables";
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-7-2)import{END}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-7-3)import{AIMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-7-4)
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-7-5)// Define the function that determines whether to continue or not
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-7-6)constshouldContinue=(state:typeofAgentState.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-7-7)const{messages}=state;
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-7-8)constlastMessage=messages[messages.length-1]asAIMessage;
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-7-9)// If there is no function call, then we finish
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-7-10)if(!lastMessage?.tool_calls?.length){
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-7-11)returnEND;
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-7-12)}// Otherwise if there is, we check if it's suppose to return direct
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-7-13)else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-7-14)constargs=lastMessage.tool_calls[0].args;
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-7-15)if(args?.return_direct){
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-7-16)return"final";
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-7-17)}else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-7-18)return"tools";
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-7-19)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-7-20)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-7-21)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-7-22)
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-7-23)// Define the function that calls the model
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-7-24)constcallModel=async(state:typeofAgentState.State,config?:RunnableConfig)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-7-25)constmessages=state.messages;
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-7-26)constresponse=awaitboundModel.invoke(messages,config);
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-7-27)// We return an object, because this will get added to the existing list
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-7-28)return{messages:[response]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-7-29)};

```


## Define the graph[¶](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#define-the-graph "Permanent link")

We can now put it all together and define the graph!

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-8-1)import{START,StateGraph}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-8-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-8-3)// Define a new graph
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-8-4)constworkflow=newStateGraph(AgentState)
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-8-5)// Define the two nodes we will cycle between
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-8-6).addNode("agent",callModel)
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-8-7)// Note the "action" and "final" nodes are identical!
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-8-8).addNode("tools",toolNode)
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-8-9).addNode("final",toolNode)
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-8-10)// Set the entrypoint as `agent`
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-8-11).addEdge(START,"agent")
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-8-12)// We now add a conditional edge
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-8-13).addConditionalEdges(
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-8-14)// First, we define the start node. We use `agent`.
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-8-15)"agent",
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-8-16)// Next, we pass in the function that will determine which node is called next.
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-8-17)shouldContinue,
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-8-18))
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-8-19)// We now add a normal edge from `tools` to `agent`.
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-8-20).addEdge("tools","agent")
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-8-21).addEdge("final",END);
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-8-22)
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-8-23)// Finally, we compile it!
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-8-24)constapp=workflow.compile();

```


## Use it![¶](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#use-it "Permanent link")

We can now use it! This now exposes the [same interface](https://js.langchain.com/docs/expression_language/) as all other LangChain runnables.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-9-1)import{HumanMessage,isAIMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-9-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-9-3)constprettyPrint=(message:BaseMessage)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-9-4)lettxt=`[${message._getType()}]: ${message.content}`;
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-9-5)if(
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-9-6)isAIMessage(message)&&(messageasAIMessage)?.tool_calls?.length||0>0
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-9-7)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-9-8)consttool_calls=(messageasAIMessage)?.tool_calls
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-9-9)?.map((tc)=>`- ${tc.name}(${JSON.stringify(tc.args)})`)
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-9-10).join("\n");
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-9-11)txt+=` \nTools: \n${tool_calls}`;
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-9-12)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-9-13)console.log(txt);
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-9-14)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-9-15)
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-9-16)constinputs={messages:[newHumanMessage("what is the weather in sf")]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-9-17)forawait(constoutputofawaitapp.stream(inputs,{streamMode:"values"})){
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-9-18)constlastMessage=output.messages[output.messages.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-9-19)prettyPrint(lastMessage);
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-9-20)console.log("-----\n");
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-9-21)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-10-1)[human]: what is the weather in sf
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-10-2)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-10-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-10-4)[ai]: 
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-10-5)Tools: 
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-10-6)- search({"query":"weather in San Francisco"})
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-10-7)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-10-8)
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-10-9)[tool]: It's sunny in San Francisco, but you better look out if you're a Gemini 😈.
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-10-10)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-10-11)
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-10-12)[ai]: The weather in San Francisco is sunny.
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-10-13)-----

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-11-1)constinputs2={
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-11-2)messages:[
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-11-3)newHumanMessage(
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-11-4)"what is the weather in sf? return this result directly by setting return_direct = True",
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-11-5)),
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-11-6)],
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-11-7)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-11-8)forawait(
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-11-9)constoutputofawaitapp.stream(inputs2,{streamMode:"values"})
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-11-10)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-11-11)constlastMessage=output.messages[output.messages.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-11-12)prettyPrint(lastMessage);
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-11-13)console.log("-----\n");
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-11-14)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-12-1)[human]: what is the weather in sf? return this result directly by setting return_direct = True
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-12-2)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-12-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-12-4)[ai]: 
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-12-5)Tools: 
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-12-6)- search({"query":"weather in San Francisco","return_direct":true})
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-12-7)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-12-8)
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-12-9)[tool]: It's sunny in San Francisco, but you better look out if you're a Gemini 😈.
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-12-10)-----

```


Done! The graph **stopped** after running the `tools` node! 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__codelineno-13-1)

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to add node retry policies  ](https://langchain-ai.github.io/langgraphjs/how-tos/node-retry-policies/) [ Next  How to have agent respond in structured format  ](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
