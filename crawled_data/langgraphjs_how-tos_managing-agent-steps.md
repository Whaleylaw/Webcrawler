---
url: https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#how-to-manage-agent-steps)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to manage agent steps 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/?q= "Share")

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
            * [ How to have agent respond in structured format  ](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/)
            * How to manage agent steps  [ How to manage agent steps  ](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#setup)
              * [ Set up the State  ](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#set-up-the-state)
              * [ Set up the tools  ](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#set-up-the-tools)
              * [ Set up the model  ](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#set-up-the-model)
              * [ Define the nodes  ](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#define-the-nodes)
              * [ Define the graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#define-the-graph)
              * [ Use it!  ](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#use-it)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#setup)
  * [ Set up the State  ](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#set-up-the-state)
  * [ Set up the tools  ](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#set-up-the-tools)
  * [ Set up the model  ](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#set-up-the-model)
  * [ Define the nodes  ](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#define-the-nodes)
  * [ Define the graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#define-the-graph)
  * [ Use it!  ](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#use-it)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
  5. [ Other  ](https://langchain-ai.github.io/langgraphjs/how-tos#other)



# How to manage agent steps[¶](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#how-to-manage-agent-steps "Permanent link")

In this example we will build a ReAct Agent that explicitly manages intermediate steps.

The previous examples just put all messages into the model, but that extra context can distract the agent and add latency to the API calls. In this example we will only include the `N` most recent messages in the chat history. Note that this is meant to be illustrative of general state management.

## Setup[¶](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#setup "Permanent link")

First we need to install required packages:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-0-1)yarnadd@langchain/langgraph@langchain/openai@langchain/core

```


Next, we need to set API keys for Anthropic (the LLM we will use).

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-1-1)// process.env.OPENAI_API_KEY = "sk_...";

```


Optionally, we can set API key for [LangSmith tracing](https://smith.langchain.com/), which will give us best-in-class observability.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-2-1)// Optional, add tracing in LangSmith
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-2-2)// process.env.LANGCHAIN_API_KEY = "ls__...";
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-2-3)process.env.LANGCHAIN_CALLBACKS_BACKGROUND="true";
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-2-4)process.env.LANGCHAIN_TRACING_V2="true";
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-2-5)process.env.LANGCHAIN_PROJECT="Managing Agent Steps: LangGraphJS";

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-3-1)Managing Agent Steps: LangGraphJS

```


## Set up the State[¶](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#set-up-the-state "Permanent link")

The main type of graph in `langgraph` is the [StateGraph](https://langchain-ai.github.io/langgraphjs/reference/classes/langgraph.StateGraph.html). This graph is parameterized by a state object that it passes around to each node. Each node then returns operations to update that state. These operations can either SET specific attributes on the state (e.g. overwrite the existing values) or ADD to the existing attribute. Whether to set or add is denoted in the state object you construct the graph with.

For this example, the state we will track will just be a list of messages. We want each node to just add messages to that list. Therefore, we will define the state as follows:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-4-1)import{Annotation}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-4-2)import{BaseMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-4-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-4-4)constAgentState=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-4-5)messages:Annotation<BaseMessage[]>({
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-4-6)reducer:(x,y)=>x.concat(y),
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-4-7)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-4-8)});

```


## Set up the tools[¶](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#set-up-the-tools "Permanent link")

We will first define the tools we want to use. For this simple example, we will create a placeholder search engine. It is really easy to create your own tools - see documentation [here](https://js.langchain.com/docs/modules/agents/tools/dynamic) on how to do that.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-5-1)import{DynamicStructuredTool}from"@langchain/core/tools";
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-5-2)import{z}from"zod";
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-5-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-5-4)constsearchTool=newDynamicStructuredTool({
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-5-5)name:"search",
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-5-6)description:"Call to surf the web.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-5-7)schema:z.object({
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-5-8)query:z.string().describe("The query to use in your search."),
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-5-9)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-5-10)func:async({}:{query:string})=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-5-11)// This is a placeholder, but don't tell the LLM that...
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-5-12)return"Try again in a few seconds! Checking with the weathermen... Call be again next.";
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-5-13)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-5-14)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-5-15)
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-5-16)consttools=[searchTool];

```


We can now wrap these tools in a simple [ToolNode](https://langchain-ai.github.io/langgraphjs/reference/classes/langgraph_prebuilt.ToolNode.html).\ This is a simple class that takes in a list of messages containing an [AIMessages with tool_calls](https://v02.api.js.langchain.com/classes/langchain_core_messages_ai.AIMessage.html), runs the tools, and returns the output as [ToolMessage](https://v02.api.js.langchain.com/classes/langchain_core_messages_tool.ToolMessage.html)s.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-6-1)import{ToolNode}from"@langchain/langgraph/prebuilt";
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-6-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-6-3)consttoolNode=newToolNode<typeofAgentState.State>(tools);

```


## Set up the model[¶](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#set-up-the-model "Permanent link")

Now we need to load the chat model we want to use. This should satisfy two criteria:

  1. It should work with messages, since our state is primarily a list of messages (chat history).
  2. It should work with tool calling, since we are using a prebuilt [ToolNode](https://langchain-ai.github.io/langgraphjs/reference/classes/langgraph_prebuilt.ToolNode.html)



**Note:** these model requirements are not requirements for using LangGraph - they are just requirements for this particular example.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-7-1)import{ChatOpenAI}from"@langchain/openai";
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-7-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-7-3)constmodel=newChatOpenAI({
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-7-4)model:"gpt-4o",
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-7-5)temperature:0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-7-6)});

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-8-1)// After we've done this, we should make sure the model knows that it has these tools available to call.
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-8-2)// We can do this by binding the tools to the model class.
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-8-3)constboundModel=model.bindTools(tools);

```


## Define the nodes[¶](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#define-the-nodes "Permanent link")

We now need to define a few different nodes in our graph. In `langgraph`, a node can be either a function or a [runnable](https://js.langchain.com/docs/expression_language/). There are two main nodes we need for this:

  1. The agent: responsible for deciding what (if any) actions to take.
  2. A function to invoke tools: if the agent decides to take an action, this node will then execute that action.



We will also need to define some edges. Some of these edges may be conditional. The reason they are conditional is that based on the output of a node, one of several paths may be taken. The path that is taken is not known until that node is run (the LLM decides).

  1. Conditional Edge: after the agent is called, we should either: a. If the agent said to take an action, then the function to invoke tools should be called\ b. If the agent said that it was finished, then it should finish
  2. Normal Edge: after the tools are invoked, it should always go back to the agent to decide what to do next



Let's define the nodes, as well as a function to decide how what conditional edge to take.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-9-1)import{END}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-9-2)import{AIMessage,ToolMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-9-3)import{RunnableConfig}from"@langchain/core/runnables";
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-9-4)
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-9-5)// Define the function that determines whether to continue or not
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-9-6)constshouldContinue=(state:typeofAgentState.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-9-7)const{messages}=state;
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-9-8)constlastMessage=messages[messages.length-1]asAIMessage;
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-9-9)// If there is no function call, then we finish
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-9-10)if(!lastMessage.tool_calls||lastMessage.tool_calls.length===0){
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-9-11)returnEND;
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-9-12)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-9-13)// Otherwise if there is, we continue
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-9-14)return"tools";
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-9-15)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-9-16)
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-9-17)// **MODIFICATION**
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-9-18)//
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-9-19)// Here we don't pass all messages to the model but rather only pass the `N` most recent. Note that this is a terribly simplistic way to handle messages meant as an illustration, and there may be other methods you may want to look into depending on your use case. We also have to make sure we don't truncate the chat history to include the tool message first, as this would cause an API error.
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-9-20)constcallModel=async(
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-9-21)state:typeofAgentState.State,
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-9-22)config?:RunnableConfig,
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-9-23))=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-9-24)letmodelMessages=[];
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-9-25)for(leti=state.messages.length-1;i>=0;i--){
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-9-26)modelMessages.push(state.messages[i]);
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-9-27)if(modelMessages.length>=5){
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-9-28)if(!ToolMessage.isInstance(modelMessages[modelMessages.length-1])){
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-9-29)break;
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-9-30)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-9-31)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-9-32)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-9-33)modelMessages.reverse();
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-9-34)
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-9-35)constresponse=awaitboundModel.invoke(modelMessages,config);
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-9-36)// We return an object, because this will get added to the existing list
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-9-37)return{messages:[response]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-9-38)};

```


## Define the graph[¶](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#define-the-graph "Permanent link")

We can now put it all together and define the graph!

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-10-1)import{START,StateGraph}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-10-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-10-3)// Define a new graph
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-10-4)constworkflow=newStateGraph(AgentState)
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-10-5).addNode("agent",callModel)
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-10-6).addNode("tools",toolNode)
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-10-7).addEdge(START,"agent")
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-10-8).addConditionalEdges(
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-10-9)"agent",
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-10-10)shouldContinue,
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-10-11))
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-10-12).addEdge("tools","agent");
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-10-13)
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-10-14)// Finally, we compile it!
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-10-15)// This compiles it into a LangChain Runnable,
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-10-16)// meaning you can use it as you would any other runnable
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-10-17)constapp=workflow.compile();

```


## Use it![¶](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#use-it "Permanent link")

We can now use it! This now exposes the [same interface](https://js.langchain.com/docs/expression_language/) as all other LangChain runnables.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-11-1)import{HumanMessage,isAIMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-11-2)import{GraphRecursionError}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-11-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-11-4)constprettyPrint=(message:BaseMessage)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-11-5)lettxt=`[${message._getType()}]: ${message.content}`;
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-11-6)if(
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-11-7)(isAIMessage(message)&&(messageasAIMessage)?.tool_calls?.length)||
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-11-8)0>0
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-11-9)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-11-10)consttool_calls=(messageasAIMessage)?.tool_calls
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-11-11)?.map((tc)=>`- ${tc.name}(${JSON.stringify(tc.args)})`)
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-11-12).join("\n");
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-11-13)txt+=` \nTools: \n${tool_calls}`;
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-11-14)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-11-15)console.log(txt);
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-11-16)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-11-17)
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-11-18)constinputs={
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-11-19)messages:[
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-11-20)newHumanMessage(
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-11-21)"what is the weather in sf? Don't give up! Keep using your tools.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-11-22)),
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-11-23)],
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-11-24)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-11-25)// Setting the recursionLimit will set a max number of steps. We expect this to endlessly loop :)
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-11-26)try{
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-11-27)forawait(
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-11-28)constoutputofawaitapp.stream(inputs,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-11-29)streamMode:"values",
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-11-30)recursionLimit:10,
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-11-31)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-11-32)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-11-33)constlastMessage=output.messages[output.messages.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-11-34)prettyPrint(lastMessage);
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-11-35)console.log("-----\n");
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-11-36)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-11-37)}catch(e){
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-11-38)// Since we are truncating the chat history, the agent never gets the chance
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-11-39)// to see enough information to know to stop, so it will keep looping until we hit the
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-11-40)// maximum recursion limit.
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-11-41)if((easGraphRecursionError).name==="GraphRecursionError"){
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-11-42)console.log("As expected, maximum steps reached. Exiting.");
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-11-43)}else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-11-44)console.error(e);
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-11-45)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-11-46)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-12-1)[human]: what is the weather in sf? Don't give up! Keep using your tools.
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-12-2)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-12-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-12-4)[ai]: 
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-12-5)Tools: 
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-12-6)- search({"query":"current weather in San Francisco"})
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-12-7)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-12-8)
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-12-9)[tool]: Try again in a few seconds! Checking with the weathermen... Call be again next.
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-12-10)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-12-11)
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-12-12)[ai]: 
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-12-13)Tools: 
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-12-14)- search({"query":"current weather in San Francisco"})
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-12-15)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-12-16)
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-12-17)[tool]: Try again in a few seconds! Checking with the weathermen... Call be again next.
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-12-18)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-12-19)
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-12-20)[ai]: 
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-12-21)Tools: 
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-12-22)- search({"query":"current weather in San Francisco"})
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-12-23)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-12-24)
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-12-25)[tool]: Try again in a few seconds! Checking with the weathermen... Call be again next.
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-12-26)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-12-27)
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-12-28)[ai]: 
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-12-29)Tools: 
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-12-30)- search({"query":"current weather in San Francisco"})
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-12-31)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-12-32)
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-12-33)[tool]: Try again in a few seconds! Checking with the weathermen... Call be again next.
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-12-34)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-12-35)
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-12-36)[ai]: 
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-12-37)Tools: 
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-12-38)- search({"query":"current weather in San Francisco"})
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-12-39)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-12-40)
[](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__codelineno-12-41)As expected, maximum steps reached. Exiting.

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to have agent respond in structured format  ](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/) [ Next  How to use the prebuilt ReAct agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
