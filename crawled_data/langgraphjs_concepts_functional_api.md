---
url: https://langchain-ai.github.io/langgraphjs/concepts/functional_api/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#functional-api)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

Functional API 

[ ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/?q= "Share")

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
      * [ Concepts  ](https://langchain-ai.github.io/langgraphjs/concepts/)

Concepts 
        * LangGraph  LangGraph 
          * [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/concepts#langgraph)
          * [ Why LangGraph?  ](https://langchain-ai.github.io/langgraphjs/concepts/high_level/)
          * [ LangGraph Glossary  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/)
          * [ Agent architectures  ](https://langchain-ai.github.io/langgraphjs/concepts/agentic_concepts/)
          * [ Multi-agent Systems  ](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/)
          * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/)
          * [ Persistence  ](https://langchain-ai.github.io/langgraphjs/concepts/persistence/)
          * [ Memory  ](https://langchain-ai.github.io/langgraphjs/concepts/memory/)
          * [ Streaming  ](https://langchain-ai.github.io/langgraphjs/concepts/streaming/)
          * Functional API  [ Functional API  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/) Table of contents 
            * [ Overview  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#overview)
            * [ Example  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#example)
            * [ Entrypoint  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#entrypoint)
              * [ Definition  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#definition)
              * [ Injectable Parameters  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#injectable-parameters)
              * [ Executing  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#executing)
              * [ Resuming  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#resuming)
              * [ State Management  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#state-management)
                * [ entrypoint.final  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#entrypointfinal)
            * [ Task  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#task)
              * [ Definition  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#definition_1)
              * [ Execution  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#execution)
              * [ Retry Policy  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#retry-policy)
            * [ When to use a task  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#when-to-use-a-task)
            * [ Serialization  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#serialization)
            * [ Determinism  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#determinism)
            * [ Idempotency  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#idempotency)
            * [ Functional API vs. Graph API  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#functional-api-vs-graph-api)
            * [ Common Pitfalls  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#common-pitfalls)
              * [ Handling side effects  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#handling-side-effects)
              * [ Non-deterministic control flow  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#non-deterministic-control-flow)
            * [ Patterns  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#patterns)
              * [ Parallel execution  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#parallel-execution)
              * [ Calling subgraphs  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#calling-subgraphs)
              * [ Calling other entrypoints  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#calling-other-entrypoints)
              * [ Streaming custom data  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#streaming-custom-data)
              * [ Resuming after an error  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#resuming-after-an-error)
              * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#human-in-the-loop)
              * [ Short-term memory  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#short-term-memory)
              * [ Long-term memory  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#long-term-memory)
              * [ Workflows  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#workflows)
              * [ Agents  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#agents)
        * [ LangGraph Platform  ](https://langchain-ai.github.io/langgraphjs/concepts#langgraph-platform)
      * [ Tutorials  ](https://langchain-ai.github.io/langgraphjs/tutorials/)
    * Resources  Resources 
      * [ Adopters  ](https://langchain-ai.github.io/langgraphjs/adopters/)
      * [ FAQ  ](https://langchain-ai.github.io/langgraphjs/concepts/faq/)
      * [ Troubleshooting  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraphjs/reference/)
  * [ Versions  ](https://langchain-ai.github.io/langgraphjs/versions/)



Table of contents 

  * [ Overview  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#overview)
  * [ Example  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#example)
  * [ Entrypoint  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#entrypoint)
    * [ Definition  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#definition)
    * [ Injectable Parameters  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#injectable-parameters)
    * [ Executing  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#executing)
    * [ Resuming  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#resuming)
    * [ State Management  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#state-management)
      * [ entrypoint.final  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#entrypointfinal)
  * [ Task  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#task)
    * [ Definition  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#definition_1)
    * [ Execution  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#execution)
    * [ Retry Policy  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#retry-policy)
  * [ When to use a task  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#when-to-use-a-task)
  * [ Serialization  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#serialization)
  * [ Determinism  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#determinism)
  * [ Idempotency  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#idempotency)
  * [ Functional API vs. Graph API  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#functional-api-vs-graph-api)
  * [ Common Pitfalls  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#common-pitfalls)
    * [ Handling side effects  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#handling-side-effects)
    * [ Non-deterministic control flow  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#non-deterministic-control-flow)
  * [ Patterns  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#patterns)
    * [ Parallel execution  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#parallel-execution)
    * [ Calling subgraphs  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#calling-subgraphs)
    * [ Calling other entrypoints  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#calling-other-entrypoints)
    * [ Streaming custom data  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#streaming-custom-data)
    * [ Resuming after an error  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#resuming-after-an-error)
    * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#human-in-the-loop)
    * [ Short-term memory  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#short-term-memory)
    * [ Long-term memory  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#long-term-memory)
    * [ Workflows  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#workflows)
    * [ Agents  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#agents)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ Concepts  ](https://langchain-ai.github.io/langgraphjs/concepts/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/concepts#langgraph)



# Functional API[¶](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#functional-api "Permanent link")

Beta

The Functional API is currently in **beta** and is subject to change. Please [report any issues](https://github.com/langchain-ai/langgraphjs/issues) or feedback to the LangGraph team.

Note

The Functional API requires `@langchain/langgraph>=0.2.42`.

## Overview[¶](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#overview "Permanent link")

The **Functional API** allows you to add LangGraph's key features -- [persistence](https://langchain-ai.github.io/langgraphjs/concepts/persistence/), [memory](https://langchain-ai.github.io/langgraphjs/concepts/memory/), [human-in-the-loop](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/), and [streaming](https://langchain-ai.github.io/langgraphjs/concepts/streaming/) — to your applications with minimal changes to your existing code.

It is designed to integrate these features into existing code that may use standard language primitives for branching and control flow, such as `if` statements, `for` loops, and function calls. Unlike many data orchestration frameworks that require restructuring code into an explicit pipeline or DAG, the Functional API allows you to incorporate these capabilities without enforcing a rigid execution model. 

The **Functional API** uses two key building blocks: 

  * **`entrypoint`**– An**entrypoint** is a wrapper that takes a function as the starting point of a workflow. It encapsulates workflow logic and manages execution flow, including handling _long-running tasks_ and [interrupts](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/).
  * **`task`**– Represents a discrete unit of work, such as an API call or data processing step, that can be executed asynchronously within an entrypoint. Tasks return a future-like object that can be awaited or resolved synchronously.



This provides a minimal abstraction for building workflows with state management and streaming.

Tip

For users who prefer a more declarative approach, LangGraph's [Graph API](https://langchain-ai.github.io/langgraphjs/concepts/low_level/) allows you to define workflows using a Graph paradigm. Both APIs share the same underlying runtime, so you can use them together in the same application. Please see the [Functional API vs. Graph API](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#functional-api-vs-graph-api) section for a comparison of the two paradigms.

## Example[¶](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#example "Permanent link")

Below we demonstrate a simple application that writes an essay and [interrupts](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/) to request human review.

```
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-0-1)import{task,entrypoint,interrupt,MemorySaver}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-0-2)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-0-3)constwriteEssay=task("write_essay",(topic:string):string=>{
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-0-4)// A placeholder for a long-running task.
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-0-5)return`An essay about topic: ${topic}`;
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-0-6)});
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-0-7)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-0-8)constworkflow=entrypoint(
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-0-9){checkpointer:newMemorySaver(),name:"workflow"},
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-0-10)async(topic:string)=>{
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-0-11)constessay=awaitwriteEssay(topic);
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-0-12)constisApproved=interrupt({
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-0-13)// Any json-serializable payload provided to interrupt as argument.
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-0-14)// It will be surfaced on the client side as an Interrupt when streaming data
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-0-15)// from the workflow.
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-0-16)essay,// The essay we want reviewed.
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-0-17)// We can add any additional information that we need.
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-0-18)// For example, introduce a key called "action" with some instructions.
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-0-19)action:"Please approve/reject the essay",
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-0-20)});
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-0-21)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-0-22)return{
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-0-23)essay,// The essay that was generated
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-0-24)isApproved,// Response from HIL
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-0-25)};
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-0-26)}
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-0-27));

```


Detailed Explanation

This workflow will write an essay about the topic "cat" and then pause to get a review from a human. The workflow can be interrupted for an indefinite amount of time until a review is provided.

When the workflow is resumed, it executes from the very start, but because the result of the `writeEssay` task was already saved, the task result will be loaded from the checkpoint instead of being recomputed.

```
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-1-1)import{task,entrypoint,interrupt,MemorySaver,Command}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-1-2)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-1-3)constwriteEssay=task("write_essay",(topic:string):string=>{
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-1-4)return`An essay about topic: ${topic}`;
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-1-5)});
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-1-6)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-1-7)constworkflow=entrypoint(
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-1-8){checkpointer:newMemorySaver(),name:"workflow"},
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-1-9)async(topic:string)=>{
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-1-10)constessay=awaitwriteEssay(topic);
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-1-11)constisApproved=interrupt({
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-1-12)essay,// The essay we want reviewed.
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-1-13)action:"Please approve/reject the essay",
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-1-14)});
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-1-15)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-1-16)return{
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-1-17)essay,
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-1-18)isApproved,
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-1-19)};
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-1-20)}
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-1-21));
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-1-22)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-1-23)constthreadId=crypto.randomUUID();
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-1-24)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-1-25)constconfig={
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-1-26)configurable:{
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-1-27)thread_id:threadId,
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-1-28)},
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-1-29)};
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-1-30)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-1-31)forawait(constitemofawaitworkflow.stream("cat",config)){
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-1-32)console.log(item);
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-1-33)}

```


```
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-2-1){write_essay:'An essay about topic: cat'}
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-2-2){__interrupt__:[{
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-2-3)value:{essay:'An essay about topic: cat',action:'Please approve/reject the essay'},
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-2-4)resumable:true,
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-2-5)ns:['workflow:f7b8508b-21c0-8b4c-5958-4e8de74d2684'],
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-2-6)when:'during'
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-2-7)}]}

```


An essay has been written and is ready for review. Once the review is provided, we can resume the workflow:

```
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-3-1)// Get review from a user (e.g., via a UI)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-3-2)// In this case, we're using a bool, but this can be any json-serializable value.
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-3-3)consthumanReview=true;
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-3-4)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-3-5)forawait(constitemofawaitworkflow.stream(newCommand({resume:humanReview}),config)){
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-3-6)console.log(item);
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-3-7)}

```


```
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-4-1){workflow:{essay:'An essay about topic: cat',isApproved:true}}

```


The workflow has been completed and the review has been added to the essay.

## Entrypoint[¶](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#entrypoint "Permanent link")

The `entrypoint`[](https://langchain-ai.github.io/langgraphjs/reference/functions/langgraph.entrypoint-1.html) function can be used to create a workflow from a function. It encapsulates workflow logic and manages execution flow, including handling _long-running tasks_ and [interrupts](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#interrupt).

### Definition[¶](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#definition "Permanent link")

An **entrypoint** is defined by passing a function to the `entrypoint` function.

The function **must accept a single positional argument** , which serves as the workflow input. If you need to pass multiple pieces of data, use an object as the input type for the first argument.

You will often want to pass a **checkpointer** to the `entrypoint` function to enable persistence and use features like **human-in-the-loop**.

```
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-5-1)import{entrypoint,MemorySaver}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-5-2)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-5-3)constcheckpointer=newMemorySaver();
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-5-4)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-5-5)constmyWorkflow=entrypoint(
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-5-6){checkpointer,name:"myWorkflow"},
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-5-7)async(someInput:Record<string,any>):Promise<number>=>{
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-5-8)// some logic that may involve long-running tasks like API calls,
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-5-9)// and may be interrupted for human-in-the-loop.
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-5-10)returnresult;
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-5-11)}
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-5-12));

```


Serialization

The **inputs** and **outputs** of entrypoints must be JSON-serializable to support checkpointing. Please see the [serialization](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#serialization) section for more details.

### Injectable Parameters[¶](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#injectable-parameters "Permanent link")

When declaring an `entrypoint`, you can access additional parameters that will be injected automatically at run time by using the `getPreviousState`[](https://langchain-ai.github.io/langgraphjs/reference/functions/langgraph.getPreviousState.html) function and other utilities. These parameters include:

Parameter | Description  
---|---  
**config** | For accessing runtime configuration. Automatically populated as the second argument to the `entrypoint` function (but not `task`, since tasks can have a variable number of arguments). See [RunnableConfig](https://js.langchain.com/docs/concepts/runnables/#runnableconfig) for information.  
**config.store** | An instance of [BaseStore](https://langchain-ai.github.io/langgraphjs/reference/classes/checkpoint.BaseStore.html). Useful for [long-term memory](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#long-term-memory).  
**config.writer** | A `writer` used for streaming back custom data. See the [guide on streaming custom data](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/)  
**getPreviousState()** | Access the state associated with the previous `checkpoint` for the given thread using `getPreviousState`[](https://langchain-ai.github.io/langgraphjs/reference/functions/langgraph.getPreviousState.html). See [state management](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#state-management).  
  
Requesting Injectable Parameters

```
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-6-1)import{
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-6-2)entrypoint,
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-6-3)getPreviousState,
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-6-4)BaseStore,
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-6-5)InMemoryStore,
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-6-6)}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-6-7)import{RunnableConfig}from"@langchain/core/runnables";
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-6-8)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-6-9)constinMemoryStore=newInMemoryStore(...);// An instance of InMemoryStore for long-term memory
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-6-10)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-6-11)constmyWorkflow=entrypoint(
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-6-12){
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-6-13)checkpointer,// Specify the checkpointer
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-6-14)store:inMemoryStore,// Specify the store
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-6-15)name:"myWorkflow",
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-6-16)},
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-6-17)async(someInput:Record<string,any>)=>{
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-6-18)constprevious=getPreviousState<any>();// For short-term memory
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-6-19)// Rest of workflow logic...
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-6-20)}
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-6-21));

```


### Executing[¶](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#executing "Permanent link")

Using the `entrypoint`[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#entrypoint) function will return an object that can be executed using the `invoke` and `stream` methods.

[Invoke](#__tabbed_1_1)[Stream](#__tabbed_1_2)

```
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-7-1)constconfig={
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-7-2)configurable:{
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-7-3)thread_id:"some_thread_id",
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-7-4)},
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-7-5)};
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-7-6)awaitmyWorkflow.invoke(someInput,config);// Wait for the result

```


```
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-8-1)constconfig={
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-8-2)configurable:{
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-8-3)thread_id:"some_thread_id",
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-8-4)},
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-8-5)};
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-8-6)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-8-7)forawait(constchunkofawaitmyWorkflow.stream(someInput,config)){
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-8-8)console.log(chunk);
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-8-9)}

```


### Resuming[¶](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#resuming "Permanent link")

Resuming an execution after an [interrupt](https://langchain-ai.github.io/langgraphjs/reference/functions/langgraph.interrupt-1.html) can be done by passing a **resume** value to the [Command](https://langchain-ai.github.io/langgraphjs/reference/classes/langgraph.Command.html) primitive.

[Invoke](#__tabbed_2_1)[Stream](#__tabbed_2_2)

```
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-9-1)import{Command}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-9-2)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-9-3)constconfig={
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-9-4)configurable:{
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-9-5)thread_id:"some_thread_id",
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-9-6)},
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-9-7)};
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-9-8)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-9-9)awaitmyWorkflow.invoke(newCommand({resume:someResumeValue}),config);

```


```
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-10-1)import{Command}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-10-2)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-10-3)constconfig={
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-10-4)configurable:{
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-10-5)thread_id:"some_thread_id",
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-10-6)},
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-10-7)};
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-10-8)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-10-9)conststream=awaitmyWorkflow.stream(
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-10-10)newCommand({resume:someResumeValue}),
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-10-11)config,
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-10-12));
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-10-13)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-10-14)forawait(constchunkofstream){
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-10-15)console.log(chunk);
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-10-16)}

```


**Resuming after transient error**

To resume after a transient error (such as a model provider outage), run the `entrypoint` with a `null` and the same **thread id** (config).

This assumes that the underlying **error** has been resolved and execution can proceed successfully.

[Invoke](#__tabbed_3_1)[Stream](#__tabbed_3_2)

```
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-11-1)constconfig={
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-11-2)configurable:{
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-11-3)thread_id:"some_thread_id",
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-11-4)},
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-11-5)};
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-11-6)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-11-7)awaitmyWorkflow.invoke(null,config);

```


```
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-12-1)constconfig={
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-12-2)configurable:{
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-12-3)thread_id:"some_thread_id",
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-12-4)},
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-12-5)};
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-12-6)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-12-7)forawait(constchunkofawaitmyWorkflow.stream(null,config)){
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-12-8)console.log(chunk);
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-12-9)}

```


### State Management[¶](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#state-management "Permanent link")

When an `entrypoint` is defined with a `checkpointer`, it stores information between successive invocations on the same **thread id** in [checkpoints](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#checkpoints).

This allows accessing the state from the previous invocation using the `getPreviousState`[](https://langchain-ai.github.io/langgraphjs/reference/functions/langgraph.getPreviousState.html) function.

By default, the previous state is the return value of the previous invocation.

```
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-13-1)constmyWorkflow=entrypoint(
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-13-2){checkpointer,name:"myWorkflow"},
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-13-3)async(number:number)=>{
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-13-4)constprevious=getPreviousState<number>();
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-13-5)returnnumber+(previous??0);
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-13-6)}
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-13-7));
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-13-8)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-13-9)constconfig={
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-13-10)configurable:{
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-13-11)thread_id:"some_thread_id",
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-13-12)},
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-13-13)};
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-13-14)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-13-15)awaitmyWorkflow.invoke(1,config);// 1 (previous was undefined)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-13-16)awaitmyWorkflow.invoke(2,config);// 3 (previous was 1 from the previous invocation)

```


#### `entrypoint.final`[¶](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#entrypointfinal "Permanent link")

[entrypoint.final](https://langchain-ai.github.io/langgraphjs/reference/functions/langgraph.entrypoint.final.html) is a special primitive that can be returned from an entrypoint and allows **decoupling** the value that is **saved in the checkpoint** from the **return value of the entrypoint**.

The first value is the return value of the entrypoint, and the second value is the value that will be saved in the checkpoint.

```
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-14-1)constmyWorkflow=entrypoint(
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-14-2){checkpointer,name:"myWorkflow"},
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-14-3)async(number:number)=>{
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-14-4)constprevious=getPreviousState<number>();
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-14-5)// This will return the previous value to the caller, saving
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-14-6)// 2 * number to the checkpoint, which will be used in the next invocation
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-14-7)// for the previous state
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-14-8)returnentrypoint.final({
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-14-9)value:previous??0,
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-14-10)save:2*number,
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-14-11)});
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-14-12)}
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-14-13));
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-14-14)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-14-15)constconfig={
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-14-16)configurable:{
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-14-17)thread_id:"1",
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-14-18)},
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-14-19)};
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-14-20)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-14-21)awaitmyWorkflow.invoke(3,config);// 0 (previous was undefined)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-14-22)awaitmyWorkflow.invoke(1,config);// 6 (previous was 3 * 2 from the previous invocation)

```


## Task[¶](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#task "Permanent link")

A **task** represents a discrete unit of work, such as an API call or data processing step. It has three key characteristics:

  * **Asynchronous Execution** : Tasks are designed to be executed asynchronously, allowing multiple operations to run concurrently without blocking.
  * **Checkpointing** : Task results are saved to a checkpoint, enabling resumption of the workflow from the last saved state. (See [persistence](https://langchain-ai.github.io/langgraphjs/concepts/persistence/) for more details).
  * **Retries** : Tasks can be configured with a [retry policy](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#retry-policies) to handle transient errors.



### Definition[¶](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#definition_1 "Permanent link")

Tasks are defined using the `task` function, which wraps a regular function.

```
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-15-1)import{task}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-15-2)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-15-3)constslowComputation=task({"slowComputation",async(inputValue:any)=>{
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-15-4)// Simulate a long-running operation
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-15-5)...
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-15-6)returnresult;
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-15-7)});

```


Serialization

The **outputs** of tasks **must** be JSON-serializable to support checkpointing.

### Execution[¶](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#execution "Permanent link")

**Tasks** can only be called from within an **entrypoint** , another **task** , or a [state graph node](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#nodes).

Tasks _cannot_ be called directly from the main application code.

```
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-16-1)constmyWorkflow=entrypoint(
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-16-2){checkpointer,name:"myWorkflow"},
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-16-3)async(someInput:number)=>{
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-16-4)returnawaitslowComputation(someInput);
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-16-5)}
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-16-6));

```


### Retry Policy[¶](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#retry-policy "Permanent link")

You can specify a [retry policy](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#retry-policies) for a **task** by passing a `retry` parameter to the `task` function.

```
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-17-1)constslowComputation=task(
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-17-2){
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-17-3)name:"slowComputation",
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-17-4)// only attempt to run this task once before giving up
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-17-5)retry:{maxAttempts:1},
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-17-6)},
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-17-7)async(inputValue:any)=>{
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-17-8)// A long-running operation that may fail
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-17-9)returnresult;
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-17-10)}
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-17-11));

```


## When to use a task[¶](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#when-to-use-a-task "Permanent link")

**Tasks** are useful in the following scenarios:

  * **Checkpointing** : When you need to save the result of a long-running operation to a checkpoint, so you don't need to recompute it when resuming the workflow.
  * **Human-in-the-loop** : If you're building a workflow that requires human intervention, you MUST use **tasks** to encapsulate any randomness (e.g., API calls) to ensure that the workflow can be resumed correctly. See the [determinism](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#determinism) section for more details.
  * **Parallel Execution** : For I/O-bound tasks, **tasks** enable parallel execution, allowing multiple operations to run concurrently without blocking (e.g., calling multiple APIs).
  * **Observability** : Wrapping operations in **tasks** provides a way to track the progress of the workflow and monitor the execution of individual operations using [LangSmith](https://docs.smith.langchain.com/).
  * **Retryable Work** : When work needs to be retried to handle failures or inconsistencies, **tasks** provide a way to encapsulate and manage the retry logic.



## Serialization[¶](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#serialization "Permanent link")

There are two key aspects to serialization in LangGraph:

  1. `entrypoint` inputs and outputs must be JSON-serializable.
  2. `task` outputs must be JSON-serializable.



These requirements are necessary for enabling checkpointing and workflow resumption. Use JavaScript primitives like objects, arrays, strings, numbers, and booleans to ensure that your inputs and outputs are serializable.

Serialization ensures that workflow state, such as task results and intermediate values, can be reliably saved and restored. This is critical for enabling human-in-the-loop interactions, fault tolerance, and parallel execution.

Providing non-serializable inputs or outputs will result in a runtime error when a workflow is configured with a checkpointer.

## Determinism[¶](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#determinism "Permanent link")

To utilize features like **human-in-the-loop** , any randomness should be encapsulated inside of **tasks**. This guarantees that when execution is halted (e.g., for human in the loop) and then resumed, it will follow the same _sequence of steps_ , even if **task** results are non-deterministic.

LangGraph achieves this behavior by persisting **task** and [**subgraph**](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#subgraphs) results as they execute. A well-designed workflow ensures that resuming execution follows the _same sequence of steps_ , allowing previously computed results to be retrieved correctly without having to re-execute them. This is particularly useful for long-running **tasks** or **tasks** with non-deterministic results, as it avoids repeating previously done work and allows resuming from essentially the same

While different runs of a workflow can produce different results, resuming a **specific** run should always follow the same sequence of recorded steps. This allows LangGraph to efficiently look up **task** and **subgraph** results that were executed prior to the graph being interrupted and avoid recomputing them.

## Idempotency[¶](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#idempotency "Permanent link")

Idempotency ensures that running the same operation multiple times produces the same result. This helps prevent duplicate API calls and redundant processing if a step is rerun due to a failure. Always place API calls inside **tasks** functions for checkpointing, and design them to be idempotent in case of re-execution. Re-execution can occur if a **task** starts, but does not complete successfully. Then, if the workflow is resumed, the **task** will run again. Use idempotency keys or verify existing results to avoid duplication.

## Functional API vs. Graph API[¶](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#functional-api-vs-graph-api "Permanent link")

The **Functional API** and the [Graph APIs (StateGraph)](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#stategraph) provide two different paradigms to create in LangGraph. Here are some key differences:

  * **Control flow** : The Functional API does not require thinking about graph structure. You can use standard Python constructs to define workflows. This will usually trim the amount of code you need to write.
  * **State management** : The **GraphAPI** requires declaring a [**State**](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#state) and may require defining [**reducers**](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#reducers) to manage updates to the graph state. `@entrypoint` and `@tasks` do not require explicit state management as their state is scoped to the function and is not shared across functions.
  * **Checkpointing** : Both APIs generate and use checkpoints. In the **Graph API** a new checkpoint is generated after every [superstep](https://langchain-ai.github.io/langgraphjs/concepts/low_level/). In the **Functional API** , when tasks are executed, their results are saved to an existing checkpoint associated with the given entrypoint instead of creating a new checkpoint.
  * **Visualization** : The Graph API makes it easy to visualize the workflow as a graph which can be useful for debugging, understanding the workflow, and sharing with others. The Functional API does not support visualization as the graph is dynamically generated during runtime.



## Common Pitfalls[¶](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#common-pitfalls "Permanent link")

### Handling side effects[¶](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#handling-side-effects "Permanent link")

Encapsulate side effects (e.g., writing to a file, sending an email) in tasks to ensure they are not executed multiple times when resuming a workflow.

[Incorrect](#__tabbed_4_1)[Correct](#__tabbed_4_2)

In this example, a side effect (writing to a file) is directly included in the workflow, so it will be executed a second time when resuming the workflow.

```
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-18-1)constmyWorkflow=entrypoint(
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-18-2){checkpointer,name:"myWorkflow"},
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-18-3)async(inputs:Record<string,any>)=>{
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-18-4)// This code will be executed a second time when resuming the workflow.
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-18-5)// Which is likely not what you want.
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-18-6)awaitfs.writeFile("output.txt","Side effect executed");
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-18-7)constvalue=interrupt("question");
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-18-8)returnvalue;
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-18-9)}
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-18-10));

```


In this example, the side effect is encapsulated in a task, ensuring consistent execution upon resumption.

```
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-19-1)import{task}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-19-2)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-19-3)constwriteToFile=task("writeToFile",async()=>{
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-19-4)awaitfs.writeFile("output.txt","Side effect executed");
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-19-5)});
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-19-6)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-19-7)constmyWorkflow=entrypoint(
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-19-8){checkpointer,name:"myWorkflow"},
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-19-9)async(inputs:Record<string,any>)=>{
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-19-10)// The side effect is now encapsulated in a task.
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-19-11)awaitwriteToFile();
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-19-12)constvalue=interrupt("question");
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-19-13)returnvalue;
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-19-14)}
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-19-15));

```


### Non-deterministic control flow[¶](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#non-deterministic-control-flow "Permanent link")

Operations that might give different results each time (like getting current time or random numbers) should be encapsulated in tasks to ensure that on resume, the same result is returned.

  * In a task: Get random number (5) → interrupt → resume → (returns 5 again) → ...
  * Not in a task: Get random number (5) → interrupt → resume → get new random number (7) → ...



This is especially important when using **human-in-the-loop** workflows with multiple interrupts calls. LangGraph keeps a list of resume values for each task/entrypoint. When an interrupt is encountered, it's matched with the corresponding resume value. This matching is strictly **index-based** , so the order of the resume values should match the order of the interrupts.

If order of execution is not maintained when resuming, one `interrupt` call may be matched with the wrong `resume` value, leading to incorrect results.

Please read the section on [determinism](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#determinism) for more details.

[Incorrect](#__tabbed_5_1)[Correct](#__tabbed_5_2)

In this example, the workflow uses the current time to determine which task to execute. This is non-deterministic because the result of the workflow depends on the time at which it is executed.

```
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-20-1)constmyWorkflow=entrypoint(
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-20-2){checkpointer,name:"myWorkflow"},
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-20-3)async(inputs:{t0:number})=>{
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-20-4)constt1=Date.now();
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-20-5)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-20-6)constdeltaT=t1-inputs.t0;
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-20-7)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-20-8)if(deltaT>1000){
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-20-9)constresult=awaitslowTask(1);
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-20-10)constvalue=interrupt("question");
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-20-11)return{result,value};
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-20-12)}else{
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-20-13)constresult=awaitslowTask(2);
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-20-14)constvalue=interrupt("question");
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-20-15)return{result,value};
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-20-16)}
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-20-17)}
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-20-18));

```


In this example, the workflow uses the input `t0` to determine which task to execute. This is deterministic because the result of the workflow depends only on the input.

```
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-21-1)import{task}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-21-2)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-21-3)constgetTime=task("getTime",()=>Date.now());
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-21-4)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-21-5)constmyWorkflow=entrypoint(
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-21-6){checkpointer,name:"myWorkflow"},
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-21-7)async(inputs:{t0:number})=>{
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-21-8)constt1=awaitgetTime();
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-21-9)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-21-10)constdeltaT=t1-inputs.t0;
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-21-11)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-21-12)if(deltaT>1000){
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-21-13)constresult=awaitslowTask(1);
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-21-14)constvalue=interrupt("question");
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-21-15)return{result,value};
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-21-16)}else{
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-21-17)constresult=awaitslowTask(2);
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-21-18)constvalue=interrupt("question");
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-21-19)return{result,value};
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-21-20)}
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-21-21)}
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-21-22));

```


## Patterns[¶](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#patterns "Permanent link")

Below are a few simple patterns that show examples of **how to** use the **Functional API**.

When defining an `entrypoint`, input is restricted to the first argument of the function. To pass multiple inputs, you can use an object.

```
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-22-1)constmyWorkflow=entrypoint(
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-22-2){checkpointer,name:"myWorkflow"},
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-22-3)async(inputs:{value:number;anotherValue:number})=>{
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-22-4)constvalue=inputs.value;
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-22-5)constanotherValue=inputs.anotherValue;
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-22-6)...
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-22-7)}
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-22-8));
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-22-9)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-22-10)awaitmyWorkflow.invoke([{value:1,anotherValue:2}]);

```


### Parallel execution[¶](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#parallel-execution "Permanent link")

Tasks can be executed in parallel by invoking them concurrently and waiting for the results. This is useful for improving performance in IO bound tasks (e.g., calling APIs for LLMs).

```
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-23-1)constaddOne=task("addOne",(number:number)=>number+1);
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-23-2)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-23-3)constgraph=entrypoint(
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-23-4){checkpointer,name:"graph"},
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-23-5)async(numbers:number[])=>{
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-23-6)returnawaitPromise.all(numbers.map(addOne));
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-23-7)}
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-23-8));

```


### Calling subgraphs[¶](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#calling-subgraphs "Permanent link")

The **Functional API** and the [**Graph API**](https://langchain-ai.github.io/langgraphjs/concepts/low_level/) can be used together in the same application as they share the same underlying runtime.

```
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-24-1)import{entrypoint,StateGraph}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-24-2)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-24-3)constbuilder=newStateGraph();
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-24-4)...
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-24-5)constsomeGraph=builder.compile();
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-24-6)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-24-7)constsomeWorkflow=entrypoint(
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-24-8){name:"someWorkflow"},
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-24-9)async(someInput:Record<string,any>)=>{
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-24-10)// Call a graph defined using the graph API
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-24-11)constresult1=awaitsomeGraph.invoke(...);
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-24-12)// Call another graph defined using the graph API
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-24-13)constresult2=awaitanotherGraph.invoke(...);
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-24-14)return{
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-24-15)result1,
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-24-16)result2,
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-24-17)};
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-24-18)}
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-24-19));

```


### Calling other entrypoints[¶](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#calling-other-entrypoints "Permanent link")

You can call other **entrypoints** from within an **entrypoint** or a **task**.

```
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-25-1)constsomeOtherWorkflow=entrypoint(
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-25-2){name:"someOtherWorkflow"},// Will automatically use the checkpointer from the parent entrypoint
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-25-3)async(inputs:{value:number})=>{
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-25-4)returninputs.value;
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-25-5)}
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-25-6));
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-25-7)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-25-8)constmyWorkflow=entrypoint(
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-25-9){checkpointer,name:"myWorkflow"},
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-25-10)async(inputs:Record<string,any>)=>{
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-25-11)constvalue=awaitsomeOtherWorkflow.invoke([{value:1}]);
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-25-12)returnvalue;
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-25-13)}
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-25-14));

```


### Streaming custom data[¶](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#streaming-custom-data "Permanent link")

You can stream custom data from an **entrypoint** by using the `write` method on `config`. This allows you to write custom data to the `custom` stream.

```
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-26-1)import{
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-26-2)entrypoint,
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-26-3)task,
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-26-4)MemorySaver,
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-26-5)LangGraphRunnableConfig,
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-26-6)}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-26-7)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-26-8)constaddOne=task("addOne",(x:number)=>x+1);
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-26-9)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-26-10)constaddTwo=task("addTwo",(x:number)=>x+2);
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-26-11)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-26-12)constcheckpointer=newMemorySaver();
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-26-13)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-26-14)constmain=entrypoint(
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-26-15){checkpointer,name:"main"},
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-26-16)async(inputs:{number:number},config:LangGraphRunnableConfig)=>{
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-26-17)config.writer?.("hello");// Write some data to the `custom` stream
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-26-18)awaitaddOne(inputs.number);// Will write data to the `updates` stream
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-26-19)config.writer?.("world");// Write some more data to the `custom` stream
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-26-20)awaitaddTwo(inputs.number);// Will write data to the `updates` stream
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-26-21)return5;
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-26-22)}
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-26-23));
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-26-24)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-26-25)constconfig={
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-26-26)configurable:{
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-26-27)thread_id:"1",
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-26-28)},
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-26-29)};
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-26-30)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-26-31)conststream=awaitmain.stream(
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-26-32){number:1},
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-26-33){streamMode:["custom","updates"],...config}
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-26-34));
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-26-35)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-26-36)forawait(constchunkofstream){
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-26-37)console.log(chunk);
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-26-38)}

```


```
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-27-1)["updates",{addOne:2}][("updates",{addTwo:3})][("custom","hello")][
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-27-2)("custom","world")
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-27-3)][("updates",{main:5})];

```


### Resuming after an error[¶](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#resuming-after-an-error "Permanent link")

```
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-1)import{entrypoint,task,MemorySaver}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-2)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-3)// Global variable to track the number of attempts
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-4)letattempts=0;
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-5)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-6)constgetInfo=task("getInfo",()=>{
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-7)/*
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-8)  * Simulates a task that fails once before succeeding.
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-9)  * Throws an error on the first attempt, then returns "OK" on subsequent tries.
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-10)  */
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-11)attempts+=1;
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-12)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-13)if(attempts<2){
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-14)thrownewError("Failure");// Simulate a failure on the first attempt
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-15)}
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-16)return"OK";
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-17)});
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-18)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-19)// Initialize an in-memory checkpointer for persistence
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-20)constcheckpointer=newMemorySaver();
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-21)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-22)constslowTask=task("slowTask",async()=>{
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-23)/*
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-24)  * Simulates a slow-running task by introducing a 1-second delay.
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-25)  */
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-26)awaitnewPromise((resolve)=>setTimeout(resolve,1000));
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-27)return"Ran slow task.";
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-28)});
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-29)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-30)constmain=entrypoint(
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-31){checkpointer,name:"main"},
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-32)async(inputs:Record<string,any>)=>{
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-33)/*
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-34)   * Main workflow function that runs the slowTask and getInfo tasks sequentially.
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-35)   *
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-36)   * Parameters:
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-37)   * - inputs: Record<string, any> containing workflow input values.
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-38)   *
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-39)   * The workflow first executes `slowTask` and then attempts to execute `getInfo`,
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-40)   * which will fail on the first invocation.
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-41)   */
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-42)constslowTaskResult=awaitslowTask();// Blocking call to slowTask
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-43)awaitgetInfo();// Error will be thrown here on the first attempt
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-44)returnslowTaskResult;
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-45)}
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-46));
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-47)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-48)// Workflow execution configuration with a unique thread identifier
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-49)constconfig={
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-50)configurable:{
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-51)thread_id:"1",// Unique identifier to track workflow execution
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-52)},
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-53)};
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-54)
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-55)// This invocation will take ~1 second due to the slowTask execution
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-56)try{
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-57)// First invocation will throw an error due to the `getInfo` task failing
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-58)awaitmain.invoke({anyInput:"foobar"},config);
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-59)}catch(err){
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-60)// Handle the failure gracefully
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-28-61)}

```


When we resume execution, we won't need to re-run the `slowTask` as its result is already saved in the checkpoint.

```
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-29-1)awaitmain.invoke(null,config);

```


```
[](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__codelineno-30-1)"Ran slow task.";

```


### Human-in-the-loop[¶](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#human-in-the-loop "Permanent link")

The functional API supports [human-in-the-loop](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/) workflows using the `interrupt` function and the `Command` primitive.

Please see the following examples for more details:

  * [How to wait for user input (Functional API)](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/): Shows how to implement a simple human-in-the-loop workflow using the functional API.
  * [How to review tool calls (Functional API)](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/): Guide demonstrates how to implement human-in-the-loop workflows in a ReAct agent using the LangGraph Functional API.



### Short-term memory[¶](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#short-term-memory "Permanent link")

[State management](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#state-management) using the `getPreviousState`[](https://langchain-ai.github.io/langgraphjs/reference/functions/langgraph.getPreviousState.html) function and optionally using the `entrypoint.final` primitive can be used to implement [short term memory](https://langchain-ai.github.io/langgraphjs/concepts/memory/).

Please see the following how-to guides for more details:

  * [How to add thread-level persistence (functional API)](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/): Shows how to add thread-level persistence to a functional API workflow and implements a simple chatbot.



### Long-term memory[¶](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#long-term-memory "Permanent link")

[long-term memory](https://langchain-ai.github.io/langgraphjs/concepts/memory/#long-term-memory) allows storing information across different **thread ids**. This could be useful for learning information about a given user in one conversation and using it in another.

Please see the following how-to guides for more details:

  * [How to add cross-thread persistence (functional API)](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/): Shows how to add cross-thread persistence to a functional API workflow and implements a simple chatbot.



### Workflows[¶](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#workflows "Permanent link")

  * [Workflows and agent](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/) guide for more examples of how to build workflows using the Functional API.



### Agents[¶](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#agents "Permanent link")

  * [How to create a React agent from scratch (Functional API)](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/): Shows how to create a simple React agent from scratch using the functional API.
  * [How to build a multi-agent network](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/): Shows how to build a multi-agent network using the functional API.
  * [How to add multi-turn conversation in a multi-agent application (functional API)](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/): allow an end-user to engage in a multi-turn conversation with one or more agents.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  Streaming  ](https://langchain-ai.github.io/langgraphjs/concepts/streaming/) [ Next  LangGraph Platform  ](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_platform/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
