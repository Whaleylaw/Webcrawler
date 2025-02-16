---
url: https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#how-to-pass-runtime-values-to-tools)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to pass runtime values to tools 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/?q= "Share")

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
            * [ How to force an agent to call a tool  ](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/)
            * [ How to handle tool calling errors  ](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/)
            * How to pass runtime values to tools  [ How to pass runtime values to tools  ](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#setup)
              * [ Context variables  ](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#context-variables)
                * [ Define the agent state  ](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#define-the-agent-state)
              * [ Define the nodes  ](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#define-the-nodes)
              * [ Use it!  ](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#use-it)
              * [ Closures  ](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#closures)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#setup)
  * [ Context variables  ](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#context-variables)
    * [ Define the agent state  ](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#define-the-agent-state)
  * [ Define the nodes  ](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#define-the-nodes)
  * [ Use it!  ](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#use-it)
  * [ Closures  ](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#closures)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
  5. [ Tool calling  ](https://langchain-ai.github.io/langgraphjs/how-tos#tool-calling)



# How to pass runtime values to tools[¶](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#how-to-pass-runtime-values-to-tools "Permanent link")

This guide shows how to define tools that depend on dynamically defined variables. These values are provided by your program, not by the LLM.

Tools can access the [config.configurable](https://langchain-ai.github.io/langgraphjs/reference/interfaces/langgraph.LangGraphRunnableConfig.html) field for values like user IDs that are known when a graph is initially executed, as well as managed values from the [store](https://langchain-ai.github.io/langgraphjs/reference/classes/checkpoint.BaseStore.html) for persistence across threads.

However, it can be convenient to access intermediate runtime values which are not known ahead of time, but are progressively generated as a graph executes, such as the current graph state. This guide will cover two techniques for this: context variables and closures.

## Setup[¶](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#setup "Permanent link")

Install the following to run this guide:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-0-1)npminstall@langchain/langgraph@langchain/openai@langchain/core

```


Next, configure your environment to connect to your model provider.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-1-1)exportOPENAI_API_KEY=your-api-key

```


Optionally, set your API key for [LangSmith tracing](https://smith.langchain.com/), which will give us best-in-class observability.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-2-1)exportLANGCHAIN_TRACING_V2="true"
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-2-2)exportLANGCHAIN_CALLBACKS_BACKGROUND="true"
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-2-3)exportLANGCHAIN_API_KEY=your-api-key

```


## Context variables[¶](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#context-variables "Permanent link")

[Context variables](https://js.langchain.com/docs/how_to/tool_runtime#using-context-variables) are a powerful feature that allows you to set values at one level of your application, then access them within any child runnables (such as tools) nested within.

They are convenient in that you don’t need to have a direct reference to the declared variable to access it from a child, just a string with the variable name.

Compatibility

This functionality was added in `@langchain/core>=0.3.10`. If you are using the LangSmith SDK separately in your project, we also recommend upgrading to `langsmith>=0.1.65`. For help upgrading, see [this guide](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/). 

It also requires `async_hooks`[](https://nodejs.org/api/async_hooks.html) support, which is supported in many popular JavaScript environments (such as Node.js, Deno, and Cloudflare Workers), but not all of them (mainly web browsers). 

Let's define a tool that an LLM can use to update pet preferences for a user. The tool will retrieve the current state of the graph from the current context.

### Define the agent state[¶](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#define-the-agent-state "Permanent link")

For this example, the state we will track will just be a list of messages:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-3-1)import{Annotation}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-3-2)import{BaseMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-3-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-3-4)constStateAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-3-5)messages:Annotation<BaseMessage[]>({
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-3-6)reducer:(x,y)=>x.concat(y),
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-3-7)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-3-8)});

```


Now, declare a tool as shown below. The tool receives values in three different ways:

  1. It will receive a generated list of `pets` from the LLM in its `input`.
  2. It will pull a `userId` populated from the initial graph invocation.
  3. It will get the current state of the graph at runtime from a context variable.



It will then use LangGraph's [cross-thread persistence](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/) to save preferences:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-4-1)import{z}from"zod";
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-4-2)import{tool}from"@langchain/core/tools";
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-4-3)import{getContextVariable}from"@langchain/core/context";
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-4-4)import{LangGraphRunnableConfig}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-4-5)
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-4-6)constupdateFavoritePets=tool(async(input,config:LangGraphRunnableConfig)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-4-7)// Some arguments are populated by the LLM; these are included in the schema below
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-4-8)const{pets}=input;
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-4-9)// Fetch a context variable named "currentState".
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-4-10)// We must set this variable explicitly in each node that calls this tool.
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-4-11)constcurrentState=getContextVariable("currentState");
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-4-12)// Other information (such as a UserID) are most easily provided via the config
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-4-13)// This is set when when invoking or streaming the graph
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-4-14)constuserId=config.configurable?.userId;
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-4-15)// LangGraph's managed key-value store is also accessible from the config
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-4-16)conststore=config.store;
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-4-17)awaitstore.put([userId,"pets"],"names",pets);
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-4-18)// Store the initial input message from the user as a note.
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-4-19)// Using the same key will override previous values - you could
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-4-20)// use something different if you wanted to store many interactions.
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-4-21)awaitstore.put([userId,"pets"],"context",currentState.messages[0].content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-4-22)
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-4-23)return"update_favorite_pets called.";
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-4-24)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-4-25){
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-4-26)// The LLM "sees" the following schema:
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-4-27)name:"update_favorite_pets",
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-4-28)description:"add to the list of favorite pets.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-4-29)schema:z.object({
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-4-30)pets:z.array(z.string()),
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-4-31)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-4-32)});

```


If we look at the tool call schema, which is what is passed to the model for tool-calling, only `pets` is being passed:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-5-1)import{zodToJsonSchema}from"zod-to-json-schema";
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-5-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-5-3)console.log(zodToJsonSchema(updateFavoritePets.schema));

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-6-1){
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-6-2) type: 'object',
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-6-3) properties: { pets: { type: 'array', items: [Object] } },
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-6-4) required: [ 'pets' ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-6-5) additionalProperties: false,
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-6-6) '$schema': 'http://json-schema.org/draft-07/schema#'
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-6-7)}

```


Let's also declare another tool so that our agent can retrieve previously set preferences: 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-7-1)constgetFavoritePets=tool(
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-7-2)async(_,config:LangGraphRunnableConfig)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-7-3)constuserId=config.configurable?.userId;
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-7-4)// LangGraph's managed key-value store is also accessible via the config
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-7-5)conststore=config.store;
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-7-6)constpetNames=awaitstore.get([userId,"pets"],"names");
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-7-7)constcontext=awaitstore.get([userId,"pets"],"context");
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-7-8)returnJSON.stringify({
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-7-9)pets:petNames.value,
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-7-10)context:context.value,
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-7-11)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-7-12)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-7-13){
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-7-14)// The LLM "sees" the following schema:
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-7-15)name:"get_favorite_pets",
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-7-16)description:"retrieve the list of favorite pets for the given user.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-7-17)schema:z.object({}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-7-18)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-7-19));

```


## Define the nodes[¶](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#define-the-nodes "Permanent link")

We now need to define a few different nodes in our graph.

  1. The agent: responsible for deciding what (if any) actions to take.
  2. A function to invoke tools: if the agent decides to take an action, this node will then execute that action. It will also set the current state as a context variable.



We will also need to define some edges.

  1. After the agent is called, we should either invoke the tool node or finish.
  2. After the tool node have been invoked, it should always go back to the agent to decide what to do next



```
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-1)import{
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-2)END,
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-3)START,
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-4)StateGraph,
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-5)MemorySaver,
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-6)InMemoryStore,
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-7)}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-8)import{AIMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-9)import{ToolNode}from"@langchain/langgraph/prebuilt";
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-10)import{ChatOpenAI}from"@langchain/openai";
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-11)
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-12)import{setContextVariable}from"@langchain/core/context";
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-13)
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-14)constmodel=newChatOpenAI({model:"gpt-4o"});
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-15)
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-16)consttools=[getFavoritePets,updateFavoritePets];
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-17)
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-18)constrouteMessage=(state:typeofStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-19)const{messages}=state;
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-20)constlastMessage=messages[messages.length-1]asAIMessage;
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-21)// If no tools are called, we can finish (respond to the user)
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-22)if(!lastMessage?.tool_calls?.length){
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-23)returnEND;
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-24)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-25)// Otherwise if there is, we continue and call the tools
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-26)return"tools";
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-27)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-28)
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-29)constcallModel=async(state:typeofStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-30)const{messages}=state;
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-31)constmodelWithTools=model.bindTools(tools);
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-32)constresponseMessage=awaitmodelWithTools.invoke([
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-33){
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-34)role:"system",
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-35)content:"You are a personal assistant. Store any preferences the user tells you about."
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-36)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-37)...messages
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-38)]);
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-39)return{messages:[responseMessage]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-40)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-41)
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-42)consttoolNodeWithGraphState=async(state:typeofStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-43)// We set a context variable before invoking the tool node and running our tool.
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-44)setContextVariable("currentState",state);
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-45)consttoolNodeWithConfig=newToolNode(tools);
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-46)returntoolNodeWithConfig.invoke(state);
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-47)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-48)
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-49)constworkflow=newStateGraph(StateAnnotation)
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-50).addNode("agent",callModel)
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-51).addNode("tools",toolNodeWithGraphState)
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-52).addEdge(START,"agent")
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-53).addConditionalEdges("agent",routeMessage)
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-54).addEdge("tools","agent");
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-55)
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-56)constmemory=newMemorySaver();
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-57)conststore=newInMemoryStore();
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-58)
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-8-59)constgraph=workflow.compile({checkpointer:memory,store:store});

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-9-1)import*astslabfrom"tslab";
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-9-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-9-3)constgraphViz=graph.getGraph();
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-9-4)constimage=awaitgraphViz.drawMermaidPng();
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-9-5)constarrayBuffer=awaitimage.arrayBuffer();
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-9-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-9-7)awaittslab.display.png(newUint8Array(arrayBuffer));

```


![]()

## Use it![¶](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#use-it "Permanent link")

Let's use our graph now!

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-10-1)letinputs={messages:[{role:"user",content:"My favorite pet is a terrier. I saw a cute one on Twitter."}]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-10-2)letconfig={
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-10-3)configurable:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-10-4)thread_id:"1",
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-10-5)userId:"a-user"
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-10-6)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-10-7)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-10-8)letstream=awaitgraph.stream(inputs,config);
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-10-9)
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-10-10)forawait(constchunkofstream){
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-10-11)for(const[node,values]ofObject.entries(chunk)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-10-12)console.log(`Output from node: ${node}`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-10-13)console.log("---");
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-10-14)console.log(values);
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-10-15)console.log("\n====\n");
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-10-16)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-10-17)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-1)Output from node: agent
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-2)---
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-3){
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-4) messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-5)  AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-6)   "id": "chatcmpl-AHcDfVrNHLi0DVBtW84UapOoeAP1t",
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-7)   "content": "",
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-8)   "additional_kwargs": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-9)    "tool_calls": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-10)     {
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-11)      "id": "call_L3pw6ipwtBxdudekgCymgcBt",
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-12)      "type": "function",
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-13)      "function": "[Object]"
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-14)     }
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-15)    ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-16)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-17)   "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-18)    "tokenUsage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-19)     "completionTokens": 19,
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-20)     "promptTokens": 102,
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-21)     "totalTokens": 121
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-22)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-23)    "finish_reason": "tool_calls",
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-24)    "system_fingerprint": "fp_6b68a8204b"
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-25)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-26)   "tool_calls": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-27)    {
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-28)     "name": "update_favorite_pets",
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-29)     "args": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-30)      "pets": "[Array]"
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-31)     },
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-32)     "type": "tool_call",
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-33)     "id": "call_L3pw6ipwtBxdudekgCymgcBt"
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-34)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-35)   ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-36)   "invalid_tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-37)   "usage_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-38)    "input_tokens": 102,
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-39)    "output_tokens": 19,
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-40)    "total_tokens": 121
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-41)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-42)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-43) ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-44)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-45)
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-46)====
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-47)
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-48)Output from node: tools
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-49)---
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-50){
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-51) messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-52)  ToolMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-53)   "content": "update_favorite_pets called.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-54)   "name": "update_favorite_pets",
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-55)   "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-56)   "response_metadata": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-57)   "tool_call_id": "call_L3pw6ipwtBxdudekgCymgcBt"
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-58)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-59) ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-60)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-61)
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-62)====
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-63)
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-64)Output from node: agent
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-65)---
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-66){
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-67) messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-68)  AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-69)   "id": "chatcmpl-AHcDfhVBJjGpk3Bdxw1tDQCZxqci5",
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-70)   "content": "I've added \"terrier\" to your list of favorite pets! If there's anything else you would like to share or update, feel free to let me know.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-71)   "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-72)   "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-73)    "tokenUsage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-74)     "completionTokens": 33,
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-75)     "promptTokens": 139,
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-76)     "totalTokens": 172
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-77)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-78)    "finish_reason": "stop",
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-79)    "system_fingerprint": "fp_6b68a8204b"
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-80)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-81)   "tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-82)   "invalid_tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-83)   "usage_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-84)    "input_tokens": 139,
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-85)    "output_tokens": 33,
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-86)    "total_tokens": 172
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-87)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-88)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-89) ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-90)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-91)
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-11-92)====

```


Now verify it can properly fetch the stored preferences and cite where it got the information from: 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-12-1)inputs={messages:[{role:"user",content:"What're my favorite pets and what did I say when I told you about them?"}]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-12-2)config={
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-12-3)configurable:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-12-4)thread_id:"2",// New thread ID, so the conversation history isn't present.
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-12-5)userId:"a-user"
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-12-6)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-12-7)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-12-8)
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-12-9)stream=awaitgraph.stream(inputs,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-12-10)...config
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-12-11)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-12-12)
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-12-13)forawait(
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-12-14)constchunkofstream
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-12-15)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-12-16)for(const[node,values]ofObject.entries(chunk)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-12-17)console.log(`Output from node: ${node}`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-12-18)console.log("---");
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-12-19)console.log(values);
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-12-20)console.log("\n====\n");
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-12-21)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-12-22)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-1)Output from node: agent
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-2)---
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-3){
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-4) messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-5)  AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-6)   "id": "chatcmpl-AHcDgeIcrobhGEwsuuH0yI4YoEKbo",
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-7)   "content": "",
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-8)   "additional_kwargs": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-9)    "tool_calls": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-10)     {
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-11)      "id": "call_1vtxWaH6Xhg8uwWo1M2Y5gOg",
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-12)      "type": "function",
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-13)      "function": "[Object]"
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-14)     }
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-15)    ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-16)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-17)   "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-18)    "tokenUsage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-19)     "completionTokens": 13,
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-20)     "promptTokens": 103,
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-21)     "totalTokens": 116
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-22)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-23)    "finish_reason": "tool_calls",
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-24)    "system_fingerprint": "fp_6b68a8204b"
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-25)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-26)   "tool_calls": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-27)    {
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-28)     "name": "get_favorite_pets",
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-29)     "args": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-30)     "type": "tool_call",
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-31)     "id": "call_1vtxWaH6Xhg8uwWo1M2Y5gOg"
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-32)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-33)   ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-34)   "invalid_tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-35)   "usage_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-36)    "input_tokens": 103,
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-37)    "output_tokens": 13,
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-38)    "total_tokens": 116
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-39)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-40)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-41) ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-42)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-43)
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-44)====
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-45)
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-46)Output from node: tools
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-47)---
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-48){
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-49) messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-50)  ToolMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-51)   "content": "{\"pets\":[\"terrier\"],\"context\":\"My favorite pet is a terrier. I saw a cute one on Twitter.\"}",
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-52)   "name": "get_favorite_pets",
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-53)   "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-54)   "response_metadata": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-55)   "tool_call_id": "call_1vtxWaH6Xhg8uwWo1M2Y5gOg"
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-56)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-57) ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-58)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-59)
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-60)====
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-61)
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-62)Output from node: agent
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-63)---
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-64){
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-65) messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-66)  AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-67)   "id": "chatcmpl-AHcDhsL27h4nI441ZPRBs8FDPoo5a",
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-68)   "content": "Your favorite pet is a terrier. You mentioned this when you said, \"My favorite pet is a terrier. I saw a cute one on Twitter.\"",
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-69)   "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-70)   "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-71)    "tokenUsage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-72)     "completionTokens": 33,
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-73)     "promptTokens": 153,
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-74)     "totalTokens": 186
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-75)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-76)    "finish_reason": "stop",
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-77)    "system_fingerprint": "fp_6b68a8204b"
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-78)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-79)   "tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-80)   "invalid_tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-81)   "usage_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-82)    "input_tokens": 153,
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-83)    "output_tokens": 33,
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-84)    "total_tokens": 186
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-85)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-86)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-87) ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-88)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-89)
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-13-90)====

```


As you can see the agent is able to properly cite that the information came from Twitter! 

## Closures[¶](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#closures "Permanent link")

If you cannot use context variables in your environment, you can use [closures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures) to create tools with access to dynamic content. Here is a high-level example:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-14-1)functiongenerateTools(state:typeofStateAnnotation.State){
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-14-2)constupdateFavoritePets=tool(
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-14-3)async(input,config:LangGraphRunnableConfig)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-14-4)// Some arguments are populated by the LLM; these are included in the schema below
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-14-5)const{pets}=input;
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-14-6)// Others (such as a UserID) are best provided via the config
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-14-7)// This is set when when invoking or streaming the graph
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-14-8)constuserId=config.configurable?.userId;
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-14-9)// LangGraph's managed key-value store is also accessible via the config
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-14-10)conststore=config.store;
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-14-11)awaitstore.put([userId,"pets"],"names",pets)
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-14-12)awaitstore.put([userId,"pets"],"context",{content:state.messages[0].content})
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-14-13)
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-14-14)return"update_favorite_pets called.";
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-14-15)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-14-16){
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-14-17)// The LLM "sees" the following schema:
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-14-18)name:"update_favorite_pets",
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-14-19)description:"add to the list of favorite pets.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-14-20)schema:z.object({
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-14-21)pets:z.array(z.string()),
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-14-22)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-14-23)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-14-24));
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-14-25)return[updateFavoritePets];
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-14-26)};

```


Then, when laying out your graph, you will need to call the above method whenever you bind or invoke tools. For example:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-15-1)consttoolNodeWithClosure=async(state:typeofStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-15-2)// We fetch the tools any time this node is reached to
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-15-3)// form a closure and let it access the latest messages
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-15-4)consttools=generateTools(state);
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-15-5)consttoolNodeWithConfig=newToolNode(tools);
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-15-6)returntoolNodeWithConfig.invoke(state);
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__codelineno-15-7)};

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to handle tool calling errors  ](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/) [ Next  How to update graph state from tools  ](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
