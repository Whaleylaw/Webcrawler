---
url: https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#how-to-add-thread-level-persistence-functional-api)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to add thread-level persistence (functional API) 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/?q= "Share")

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
            * [ Persistence  ](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/)
            * How to add thread-level persistence (functional API)  [ How to add thread-level persistence (functional API)  ](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#setup)
              * [ Example: simple chatbot with short-term memory  ](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#example-simple-chatbot-with-short-term-memory)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#setup)
  * [ Example: simple chatbot with short-term memory  ](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#example-simple-chatbot-with-short-term-memory)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
  5. [ Persistence  ](https://langchain-ai.github.io/langgraphjs/how-tos#persistence)



# How to add thread-level persistence (functional API)[¶](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#how-to-add-thread-level-persistence-functional-api "Permanent link")

Prerequisites

This guide assumes familiarity with the following:

  * [Functional API](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/)
  * [Persistence](https://langchain-ai.github.io/langgraphjs/concepts/persistence/)
  * [Memory](https://langchain-ai.github.io/langgraphjs/concepts/memory/)
  * [Chat Models](https://js.langchain.com/docs/concepts/chat_models/)



Many AI applications need memory to share context across multiple interactions on the same [thread](https://langchain-ai.github.io/langgraphjs/concepts/persistence#threads) (e.g., multiple turns of a conversation). In LangGraph functional API, this kind of memory can be added to any [entrypoint()](https://langchain-ai.github.io/langgraphjs/reference/functions/langgraph.entrypoint-1.html) workflow using [thread-level persistence](https://langchain-ai.github.io/langgraphjs/concepts/persistence).

When creating a LangGraph workflow, you can set it up to persist its results by using a [checkpointer](https://langchain-ai.github.io/langgraphjs/reference/classes/checkpoint.BaseCheckpointSaver.html):

  1. Create an instance of a checkpointer:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-0-1)import{MemorySaver}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-0-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-0-3)constcheckpointer=newMemorySaver();

```


  2. Pass `checkpointer` instance to the `entrypoint()` wrapper function:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-1-1)import{entrypoint}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-1-2)constworkflow=entrypoint({
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-1-3)name:"workflow",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-1-4)checkpointer,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-1-5)},async(inputs)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-1-6)...
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-1-7)});

```


  3. Retrieve `previous` state from the prior execution within the workflow:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-2-1)import{entrypoint,getPreviousState}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-2-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-2-3)constworkflow=entrypoint({
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-2-4)name:"workflow",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-2-5)checkpointer,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-2-6)},async(inputs)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-2-7)constprevious=getPreviousState();
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-2-8)constresult=doSomething(previous,inputs);
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-2-9)...
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-2-10)});

```


  4. Optionally choose which values will be returned from the workflow and which will be saved by the checkpointer as `previous`:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-3-1)import{entrypoint,getPreviousState}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-3-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-3-3)constworkflow=entrypoint({
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-3-4)name:"workflow",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-3-5)checkpointer,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-3-6)},async(inputs)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-3-7)constprevious=getPreviousState();
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-3-8)constresult=doSomething(previous,inputs);
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-3-9)...
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-3-10)returnentrypoint.final({
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-3-11)value:result,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-3-12)save:combineState(inputs,result),
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-3-13)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-3-14)});

```





This guide shows how you can add thread-level persistence to your workflow.

Note

If you need memory that is **shared** across multiple conversations or users (cross-thread persistence), check out this [how-to guide](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional).

Note

If you need to add thread-level persistence to a `StateGraph`, check out this [how-to guide](https://langchain-ai.github.io/langgraphjs/how-tos/persistence).

## Setup[¶](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#setup "Permanent link")

Note

This guide requires `@langchain/langgraph>=0.2.42`.

First, install the required dependencies for this example:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-4-1)npminstall@langchain/langgraph@langchain/anthropic@langchain/corezod

```


Next, we need to set API keys for Anthropic (the LLM we will use):

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-5-1)process.env.ANTHROPIC_API_KEY="YOUR_API_KEY";

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com)

## Example: simple chatbot with short-term memory[¶](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#example-simple-chatbot-with-short-term-memory "Permanent link")

We will be using a workflow with a single task that calls a [chat model](https://js.langchain.com/docs/concepts/chat_models/).

Let's first define the model we'll be using:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-6-1)import{ChatAnthropic}from"@langchain/anthropic";
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-6-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-6-3)constmodel=newChatAnthropic({
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-6-4)model:"claude-3-5-sonnet-latest",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-6-5)});

```


Now we can define our task and workflow. To add in persistence, we need to pass in a [Checkpointer](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver) to the [entrypoint()](https://langchain-ai.github.io/langgraphjs/reference/functions/langgraph.entrypoint-1.html) wrapper function.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-7-1)importtype{BaseMessage,BaseMessageLike}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-7-2)import{
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-7-3)addMessages,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-7-4)entrypoint,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-7-5)task,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-7-6)getPreviousState,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-7-7)MemorySaver,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-7-8)}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-7-9)
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-7-10)constcallModel=task("callModel",async(messages:BaseMessageLike[])=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-7-11)constresponse=model.invoke(messages);
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-7-12)returnresponse;
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-7-13)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-7-14)
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-7-15)constcheckpointer=newMemorySaver();
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-7-16)
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-7-17)constworkflow=entrypoint({
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-7-18)name:"workflow",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-7-19)checkpointer,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-7-20)},async(inputs:BaseMessageLike[])=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-7-21)constprevious=getPreviousState<BaseMessage>()??[];
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-7-22)constmessages=addMessages(previous,inputs);
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-7-23)constresponse=awaitcallModel(messages);
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-7-24)returnentrypoint.final({
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-7-25)value:response,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-7-26)save:addMessages(messages,response),
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-7-27)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-7-28)});

```


If we try to use this workflow, the context of the conversation will be persisted across interactions.

Note

If you're using LangGraph Cloud or LangGraph Studio, you **don't need** to pass checkpointer to the `entrypoint` wrapper, since it's done automatically.

Here's how this works in practice:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-8-1)constconfig={
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-8-2)configurable:{thread_id:"1"},
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-8-3)streamMode:"values"asconst,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-8-4)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-8-5)constinputMessage={role:"user",content:"hi! I'm bob"};
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-8-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-8-7)conststream=awaitworkflow.stream(
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-8-8)[inputMessage],
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-8-9)config,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-8-10));
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-8-11)
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-8-12)forawait(constchunkofstream){
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-8-13)console.log("=".repeat(30),`${chunk.getType()} message`,"=".repeat(30));
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-8-14)console.log(chunk.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-8-15)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-9-1)============================== ai message ==============================
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-9-2)Hi Bob! I'm Claude. Nice to meet you! How can I help you today?

```


You can always resume previous threads: 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-10-1)constfollowupStream=awaitworkflow.stream(
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-10-2)[{role:"user",content:"what's my name?"}],
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-10-3)config,
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-10-4));
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-10-5)
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-10-6)forawait(constchunkoffollowupStream){
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-10-7)console.log("=".repeat(30),`${chunk.getType()} message`,"=".repeat(30));
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-10-8)console.log(chunk.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-10-9)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-11-1)============================== ai message ==============================
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-11-2)Your name is Bob - you just told me that in your first message.

```


If we want to start a new conversation, we can pass in a different `thread_id`. Poof! All the memories are gone! 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-12-1)constnewStream=awaitworkflow.stream(
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-12-2)[{role:"user",content:"what's my name?"}],
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-12-3){
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-12-4)configurable:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-12-5)thread_id:"2",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-12-6)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-12-7)streamMode:"values",
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-12-8)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-12-9));
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-12-10)
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-12-11)forawait(constchunkofnewStream){
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-12-12)console.log("=".repeat(30),`${chunk.getType()} message`,"=".repeat(30));
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-12-13)console.log(chunk.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-12-14)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-13-1)============================== ai message ==============================
[](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__codelineno-13-2)I don't know your name as we just started chatting. Would you like to introduce yourself?

```


Streaming tokens

If you would like to stream LLM tokens from your chatbot, you can use `streamMode: "messages"`. Check out this [how-to guide](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens) to learn more.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  Persistence  ](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/) [ Next  How to add thread-level persistence to subgraphs  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
