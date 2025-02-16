---
url: https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#how-to-wait-for-user-input-functional-api)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to wait for user input (Functional API) 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/?q= "Share")

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
          * Human-in-the-loop  Human-in-the-loop 
            * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraphjs/how-tos#human-in-the-loop)
            * [ How to add breakpoints  ](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/)
            * [ How to add dynamic breakpoints  ](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/)
            * [ How to edit graph state  ](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/)
            * [ How to wait for user input  ](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/)
            * How to wait for user input (Functional API)  [ How to wait for user input (Functional API)  ](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#setup)
              * [ Simple usage  ](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#simple-usage)
              * [ Agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#agent)
                * [ Define model and tools  ](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#define-model-and-tools)
                * [ Define tasks  ](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#define-tasks)
                * [ Define entrypoint  ](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#define-entrypoint)
                * [ Usage  ](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#usage)
            * [ How to view and update past graph state  ](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/)
            * [ Review Tool Calls  ](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/)
            * [ How to review tool calls (Functional API)  ](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#setup)
  * [ Simple usage  ](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#simple-usage)
  * [ Agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#agent)
    * [ Define model and tools  ](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#define-model-and-tools)
    * [ Define tasks  ](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#define-tasks)
    * [ Define entrypoint  ](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#define-entrypoint)
    * [ Usage  ](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#usage)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
  5. [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraphjs/how-tos#human-in-the-loop)



# How to wait for user input (Functional API)[¶](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#how-to-wait-for-user-input-functional-api "Permanent link")

Prerequisites

This guide assumes familiarity with the following:

  * Implementing [human-in-the-loop](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop) workflows with [interrupt](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#interrupt)
  * [How to create a ReAct agent using the Functional API](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional)



**Human-in-the-loop (HIL)** interactions are crucial for [agentic systems](https://langchain-ai.github.io/langgraphjs/concepts/agentic_concepts/#human-in-the-loop). Waiting for human input is a common HIL interaction pattern, allowing the agent to ask the user clarifying questions and await input before proceeding. 

We can implement this in LangGraph using the [interrupt()](https://langchain-ai.github.io/langgraphjs/reference/functions/langgraph.interrupt-1.html) function. `interrupt` allows us to stop graph execution to collect input from a user and continue execution with collected input.

This guide demonstrates how to implement human-in-the-loop workflows using LangGraph's [Functional API](https://langchain-ai.github.io/langgraphjs/concepts/functional_api). Specifically, we will demonstrate:

  1. [A simple usage example](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#simple-usage)
  2. [How to use with a ReAct agent](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#agent)



## Setup[¶](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#setup "Permanent link")

Note

This guide requires `@langchain/langgraph>=0.2.42`.

First, install the required dependencies for this example:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-0-1)npminstall@langchain/langgraph@langchain/openai@langchain/corezod

```


Next, we need to set API keys for OpenAI (the LLM we will use):

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-1-1)process.env.OPENAI_API_KEY="YOUR_API_KEY";

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com)

## Simple usage[¶](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#simple-usage "Permanent link")

Let's demonstrate a simple usage example. We will create three [tasks](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#task):

  1. Append `"bar"`.
  2. Pause for human input. When resuming, append human input.
  3. Append `"qux"`.



```
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-2-1)import{task,interrupt}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-2-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-2-3)conststep1=task("step1",async(inputQuery:string)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-2-4)return`${inputQuery} bar`;
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-2-5)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-2-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-2-7)consthumanFeedback=task(
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-2-8)"humanFeedback",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-2-9)async(inputQuery:string)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-2-10)constfeedback=interrupt(`Please provide feedback: ${inputQuery}`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-2-11)return`${inputQuery}${feedback}`;
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-2-12)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-2-13)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-2-14)conststep3=task("step3",async(inputQuery:string)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-2-15)return`${inputQuery} qux`;
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-2-16)});

```


We can now compose these tasks in a simple [entrypoint](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#entrypoint):

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-3-1)import{MemorySaver,entrypoint}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-3-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-3-3)constcheckpointer=newMemorySaver();
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-3-4)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-3-5)constgraph=entrypoint({
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-3-6)name:"graph",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-3-7)checkpointer,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-3-8)},async(inputQuery:string)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-3-9)constresult1=awaitstep1(inputQuery);
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-3-10)constresult2=awaithumanFeedback(result1);
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-3-11)constresult3=awaitstep3(result2);
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-3-12)returnresult3;
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-3-13)});

```


All we have done to enable human-in-the-loop workflows is call [interrupt()](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#interrupt) inside a task.

Tip

The results of prior tasks - in this case `step1 -- are persisted, so that they are not run again following the`interrupt`.

Let's send in a query string:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-4-1)constconfig={
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-4-2)configurable:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-4-3)thread_id:"1"
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-4-4)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-4-5)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-4-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-4-7)conststream=awaitgraph.stream("foo",config);
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-4-8)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-4-9)forawait(consteventofstream){
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-4-10)console.log(event);
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-4-11)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-5-1){ step1: 'foo bar' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-5-2){
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-5-3) __interrupt__: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-5-4)  {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-5-5)   value: 'Please provide feedback: foo bar',
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-5-6)   when: 'during',
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-5-7)   resumable: true,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-5-8)   ns: [Array]
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-5-9)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-5-10) ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-5-11)}

```


Note that we've paused with an `interrupt` after `step1`. The interrupt provides instructions to resume the run. To resume, we issue a [Command](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#the-command-primitive) containing the data expected by the `humanFeedback` task. 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-6-1)import{Command}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-6-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-6-3)constresumeStream=awaitgraph.stream(newCommand({
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-6-4)resume:"baz"
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-6-5)}),config);
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-6-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-6-7)// Continue execution
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-6-8)forawait(consteventofresumeStream){
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-6-9)if(event.__metadata__?.cached){
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-6-10)continue;
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-6-11)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-6-12)console.log(event);
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-6-13)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-7-1){ humanFeedback: 'foo bar baz' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-7-2){ step3: 'foo bar baz qux' }
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-7-3){ graph: 'foo bar baz qux' }

```


After resuming, the run proceeds through the remaining step and terminates as expected. 

## Agent[¶](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#agent "Permanent link")

We will build off of the agent created in the [How to create a ReAct agent using the Functional API](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional) guide.

Here we will extend the agent by allowing it to reach out to a human for assistance when needed.

### Define model and tools[¶](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#define-model-and-tools "Permanent link")

Let's first define the tools and model we will use for our example. As in the [ReAct agent guide](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional), we will use a single place-holder tool that gets a description of the weather for a location.

We will use an [OpenAI](https://js.langchain.com/docs/integrations/providers/openai/) chat model for this example, but any model [supporting tool-calling](https://js.langchain.com/docs/integrations/chat/) will suffice.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-8-1)import{ChatOpenAI}from"@langchain/openai";
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-8-2)import{tool}from"@langchain/core/tools";
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-8-3)import{z}from"zod";
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-8-4)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-8-5)constmodel=newChatOpenAI({
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-8-6)model:"gpt-4o-mini",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-8-7)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-8-8)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-8-9)constgetWeather=tool(async({location})=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-8-10)// This is a placeholder for the actual implementation
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-8-11)constlowercaseLocation=location.toLowerCase();
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-8-12)if(lowercaseLocation.includes("sf")||lowercaseLocation.includes("san francisco")){
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-8-13)return"It's sunny!";
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-8-14)}elseif(lowercaseLocation.includes("boston")){
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-8-15)return"It's rainy!";
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-8-16)}else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-8-17)return`I am not sure what the weather is in ${location}`;
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-8-18)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-8-19)},{
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-8-20)name:"getWeather",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-8-21)schema:z.object({
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-8-22)location:z.string().describe("Location to get the weather for"),
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-8-23)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-8-24)description:"Call to get the weather from a specific location.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-8-25)});

```


To reach out to a human for assistance, we can simply add a tool that calls [interrupt](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#interrupt):

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-9-1)import{interrupt}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-9-2)import{z}from"zod";
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-9-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-9-4)consthumanAssistance=tool(async({query})=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-9-5)consthumanResponse=interrupt({query});
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-9-6)returnhumanResponse.data;
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-9-7)},{
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-9-8)name:"humanAssistance",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-9-9)description:"Request assistance from a human.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-9-10)schema:z.object({
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-9-11)query:z.string().describe("Human readable question for the human")
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-9-12)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-9-13)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-9-14)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-9-15)consttools=[getWeather,humanAssistance];

```


### Define tasks[¶](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#define-tasks "Permanent link")

Our tasks are otherwise unchanged from the [ReAct agent guide](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional):

  1. **Call model** : We want to query our chat model with a list of messages.
  2. **Call tool** : If our model generates tool calls, we want to execute them.



We just have one more tool accessible to the model.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-10-1)import{
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-10-2)typeBaseMessageLike,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-10-3)AIMessage,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-10-4)ToolMessage,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-10-5)}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-10-6)import{typeToolCall}from"@langchain/core/messages/tool";
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-10-7)import{task}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-10-8)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-10-9)consttoolsByName=Object.fromEntries(tools.map((tool)=>[tool.name,tool]));
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-10-10)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-10-11)constcallModel=task("callModel",async(messages:BaseMessageLike[])=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-10-12)constresponse=awaitmodel.bindTools(tools).invoke(messages);
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-10-13)returnresponse;
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-10-14)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-10-15)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-10-16)constcallTool=task(
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-10-17)"callTool",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-10-18)async(toolCall:ToolCall):Promise<AIMessage>=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-10-19)consttool=toolsByName[toolCall.name];
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-10-20)constobservation=awaittool.invoke(toolCall.args);
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-10-21)returnnewToolMessage({content:observation,tool_call_id:toolCall.id});
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-10-22)// Can also pass toolCall directly into the tool to return a ToolMessage
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-10-23)// return tool.invoke(toolCall);
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-10-24)});

```


### Define entrypoint[¶](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#define-entrypoint "Permanent link")

Our [entrypoint](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#entrypoint) is also unchanged from the [ReAct agent guide](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional):

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-11-1)import{entrypoint,addMessages,MemorySaver}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-11-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-11-3)constagent=entrypoint({
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-11-4)name:"agent",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-11-5)checkpointer:newMemorySaver(),
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-11-6)},async(messages:BaseMessageLike[])=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-11-7)letcurrentMessages=messages;
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-11-8)letllmResponse=awaitcallModel(currentMessages);
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-11-9)while(true){
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-11-10)if(!llmResponse.tool_calls?.length){
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-11-11)break;
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-11-12)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-11-13)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-11-14)// Execute tools
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-11-15)consttoolResults=awaitPromise.all(
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-11-16)llmResponse.tool_calls.map((toolCall)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-11-17)returncallTool(toolCall);
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-11-18)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-11-19));
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-11-20)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-11-21)// Append to message list
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-11-22)currentMessages=addMessages(currentMessages,[llmResponse,...toolResults]);
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-11-23)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-11-24)// Call model again
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-11-25)llmResponse=awaitcallModel(currentMessages);
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-11-26)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-11-27)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-11-28)returnllmResponse;
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-11-29)});

```


### Usage[¶](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#usage "Permanent link")

Let's invoke our model with a question that requires human assistance. Our question will also require an invocation of the `getWeather` tool:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-12-1)import{BaseMessage,isAIMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-12-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-12-3)constprettyPrintMessage=(message:BaseMessage)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-12-4)console.log("=".repeat(30),`${message.getType()} message`,"=".repeat(30));
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-12-5)console.log(message.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-12-6)if(isAIMessage(message)&&message.tool_calls?.length){
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-12-7)console.log(JSON.stringify(message.tool_calls,null,2));
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-12-8)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-12-9)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-12-10)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-12-11)constprettyPrintStep=(step:Record<string,any>)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-12-12)if(step.__metadata__?.cached){
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-12-13)return;
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-12-14)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-12-15)for(const[taskName,update]ofObject.entries(step)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-12-16)constmessage=updateasBaseMessage;
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-12-17)// Only print task updates
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-12-18)if(taskName==="agent")continue;
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-12-19)console.log(`\n${taskName}:`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-12-20)if(taskName==="__interrupt__"){
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-12-21)console.log(update);
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-12-22)}else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-12-23)prettyPrintMessage(message);
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-12-24)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-12-25)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-12-26)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-13-1)constuserMessage={
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-13-2)role:"user",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-13-3)content:[
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-13-4)"Can you reach out for human assistance: what should I feed my cat?",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-13-5)"Separately, can you check the weather in San Francisco?"
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-13-6)].join(" "),
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-13-7)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-13-8)console.log(userMessage);
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-13-9)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-13-10)constagentStream=awaitagent.stream([userMessage],{
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-13-11)configurable:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-13-12)thread_id:"1",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-13-13)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-13-14)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-13-15)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-13-16)letlastStep;
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-13-17)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-13-18)forawait(conststepofagentStream){
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-13-19)prettyPrintStep(step);
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-13-20)lastStep=step;
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-13-21)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-14-1){
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-14-2) role: 'user',
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-14-3) content: 'Can you reach out for human assistance: what should I feed my cat? Separately, can you check the weather in San Francisco?'
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-14-4)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-14-5)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-14-6)callModel:
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-14-7)============================== ai message ==============================
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-14-8)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-14-9)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-14-10) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-14-11)  "name": "humanAssistance",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-14-12)  "args": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-14-13)   "query": "What should I feed my cat?"
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-14-14)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-14-15)  "type": "tool_call",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-14-16)  "id": "call_TwrNq6tGI61cDCJEpj175h7J"
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-14-17) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-14-18) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-14-19)  "name": "getWeather",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-14-20)  "args": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-14-21)   "location": "San Francisco"
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-14-22)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-14-23)  "type": "tool_call",
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-14-24)  "id": "call_fMzUBvc0SpZpXxM2LQLXfbke"
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-14-25) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-14-26)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-14-27)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-14-28)callTool:
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-14-29)============================== tool message ==============================
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-14-30)It's sunny!
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-14-31)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-14-32)__interrupt__:
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-14-33)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-14-34) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-14-35)  value: { query: 'What should I feed my cat?' },
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-14-36)  when: 'during',
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-14-37)  resumable: true,
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-14-38)  ns: [ 'callTool:2e0c6c40-9541-57ef-a7af-24213a10d5a4' ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-14-39) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-14-40)]

```


Note that we generate two tool calls, and although our run is interrupted, we did not block the execution of the `get_weather` tool. 

Let's inspect where we're interrupted:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-15-1)console.log(JSON.stringify(lastStep));

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-16-1){"__interrupt__":[{"value":{"query":"What should I feed my cat?"},"when":"during","resumable":true,"ns":["callTool:2e0c6c40-9541-57ef-a7af-24213a10d5a4"]}]}

```


We can resume execution by issuing a [Command](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#the-command-primitive). Note that the data we supply in the `Command` can be customized to your needs based on the implementation of `humanAssistance`. 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-17-1)import{Command}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-17-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-17-3)consthumanResponse="You should feed your cat a fish.";
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-17-4)consthumanCommand=newCommand({
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-17-5)resume:{data:humanResponse},
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-17-6)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-17-7)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-17-8)constresumeStream2=awaitagent.stream(humanCommand,config);
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-17-9)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-17-10)forawait(conststepofresumeStream2){
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-17-11)prettyPrintStep(step);
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-17-12)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-18-1)callTool:
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-18-2)============================== tool message ==============================
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-18-3)You should feed your cat a fish.
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-18-4)
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-18-5)callModel:
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-18-6)============================== ai message ==============================
[](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__codelineno-18-7)For your cat, it is suggested that you feed it fish. As for the weather in San Francisco, it's currently sunny!

```


Above, when we resume we provide the final tool message, allowing the model to generate its response. Check out the LangSmith traces to see a full breakdown of the runs: 

  1. [Trace from initial query](https://smith.langchain.com/public/c007b042-fdd3-49e7-acbe-cadf6969de4b/r)
  2. [Trace after resuming](https://smith.langchain.com/public/1cea310a-13f5-4de9-ae1c-045b8b33015e/r)

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to wait for user input  ](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/) [ Next  How to view and update past graph state  ](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
