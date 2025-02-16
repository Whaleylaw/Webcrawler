---
url: https://langchain-ai.github.io/langgraph/concepts/functional_api/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#functional-api)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Functional API 

[ ](https://langchain-ai.github.io/langgraph/concepts/functional_api/?q= "Share")

Type to start searching

[ GitHub  ](https://github.com/langchain-ai/langgraph "Go to repository")

  * [ Home ](https://langchain-ai.github.io/langgraph/)
  * [ API reference ](https://langchain-ai.github.io/langgraph/reference/graphs/)



[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

[ GitHub  ](https://github.com/langchain-ai/langgraph "Go to repository")

  * [ Home  ](https://langchain-ai.github.io/langgraph/)

Home 
    * Get started  Get started 
      * [ Learn the basics  ](https://langchain-ai.github.io/langgraph/tutorials/introduction/)
      * [ Deployment  ](https://langchain-ai.github.io/langgraph/tutorials/deployment/)
    * Guides  Guides 
      * [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
      * [ Concepts  ](https://langchain-ai.github.io/langgraph/concepts/)

Concepts 
        * LangGraph  LangGraph 
          * [ LangGraph  ](https://langchain-ai.github.io/langgraph/concepts#langgraph)
          * [ Why LangGraph?  ](https://langchain-ai.github.io/langgraph/concepts/high_level/)
          * [ LangGraph Glossary  ](https://langchain-ai.github.io/langgraph/concepts/low_level/)
          * [ Agent architectures  ](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/)
          * [ Multi-agent Systems  ](https://langchain-ai.github.io/langgraph/concepts/multi_agent/)
          * [ None  ](https://langchain-ai.github.io/langgraph/concepts/breakpoints)
          * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/)
          * [ Time Travel ⏱️  ](https://langchain-ai.github.io/langgraph/concepts/time-travel/)
          * [ Persistence  ](https://langchain-ai.github.io/langgraph/concepts/persistence/)
          * [ Memory  ](https://langchain-ai.github.io/langgraph/concepts/memory/)
          * [ Streaming  ](https://langchain-ai.github.io/langgraph/concepts/streaming/)
          * Functional API  [ Functional API  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/) Table of contents 
            * [ Overview  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#overview)
            * [ Example  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#example)
            * [ Entrypoint  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#entrypoint)
              * [ Definition  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#definition)
              * [ Injectable Parameters  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#injectable-parameters)
              * [ Executing  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#executing)
              * [ Resuming  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#resuming)
              * [ State Management  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#state-management)
                * [ entrypoint.final  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#entrypointfinal)
            * [ Task  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#task)
              * [ Definition  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#definition_1)
              * [ Execution  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#execution)
            * [ When to use a task  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#when-to-use-a-task)
            * [ Serialization  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#serialization)
            * [ Determinism  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#determinism)
            * [ Idempotency  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#idempotency)
            * [ Functional API vs. Graph API  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#functional-api-vs-graph-api)
            * [ Common Pitfalls  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#common-pitfalls)
              * [ Handling side effects  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#handling-side-effects)
              * [ Non-deterministic control flow  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#non-deterministic-control-flow)
            * [ Patterns  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#patterns)
              * [ Parallel execution  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#parallel-execution)
              * [ Calling subgraphs  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#calling-subgraphs)
              * [ Calling other entrypoints  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#calling-other-entrypoints)
              * [ Streaming custom data  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#streaming-custom-data)
              * [ Retry policy  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#retry-policy)
              * [ Resuming after an error  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#resuming-after-an-error)
              * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#human-in-the-loop)
              * [ Short-term memory  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#short-term-memory)
              * [ Long-term memory  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#long-term-memory)
              * [ Workflows  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#workflows)
              * [ Agents  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#agents)
        * [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/concepts#langgraph-platform)
      * [ Tutorials  ](https://langchain-ai.github.io/langgraph/tutorials/)
    * Resources  Resources 
      * [ Prebuilt Agents  ](https://langchain-ai.github.io/langgraph/prebuilt/)
      * [ Adopters  ](https://langchain-ai.github.io/langgraph/adopters/)
      * [ FAQ  ](https://langchain-ai.github.io/langgraph/concepts/faq/)
      * [ Troubleshooting  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraph/reference/graphs/)



Table of contents 

  * [ Overview  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#overview)
  * [ Example  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#example)
  * [ Entrypoint  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#entrypoint)
    * [ Definition  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#definition)
    * [ Injectable Parameters  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#injectable-parameters)
    * [ Executing  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#executing)
    * [ Resuming  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#resuming)
    * [ State Management  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#state-management)
      * [ entrypoint.final  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#entrypointfinal)
  * [ Task  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#task)
    * [ Definition  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#definition_1)
    * [ Execution  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#execution)
  * [ When to use a task  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#when-to-use-a-task)
  * [ Serialization  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#serialization)
  * [ Determinism  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#determinism)
  * [ Idempotency  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#idempotency)
  * [ Functional API vs. Graph API  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#functional-api-vs-graph-api)
  * [ Common Pitfalls  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#common-pitfalls)
    * [ Handling side effects  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#handling-side-effects)
    * [ Non-deterministic control flow  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#non-deterministic-control-flow)
  * [ Patterns  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#patterns)
    * [ Parallel execution  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#parallel-execution)
    * [ Calling subgraphs  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#calling-subgraphs)
    * [ Calling other entrypoints  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#calling-other-entrypoints)
    * [ Streaming custom data  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#streaming-custom-data)
    * [ Retry policy  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#retry-policy)
    * [ Resuming after an error  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#resuming-after-an-error)
    * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#human-in-the-loop)
    * [ Short-term memory  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#short-term-memory)
    * [ Long-term memory  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#long-term-memory)
    * [ Workflows  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#workflows)
    * [ Agents  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/#agents)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ Concepts  ](https://langchain-ai.github.io/langgraph/concepts/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/concepts#langgraph)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/concepts/functional_api.md "Edit this page")

# Functional API[¶](https://langchain-ai.github.io/langgraph/concepts/functional_api/#functional-api "Permanent link")

Beta

The Functional API is currently in **beta** and is subject to change. Please [report any issues](https://github.com/langchain-ai/langgraph/issues) or feedback to the LangGraph team.

## Overview[¶](https://langchain-ai.github.io/langgraph/concepts/functional_api/#overview "Permanent link")

The **Functional API** allows you to add LangGraph's key features -- [persistence](https://langchain-ai.github.io/langgraph/concepts/persistence/), [memory](https://langchain-ai.github.io/langgraph/concepts/memory/), [human-in-the-loop](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/), and [streaming](https://langchain-ai.github.io/langgraph/concepts/streaming/) — to your applications with minimal changes to your existing code.

It is designed to integrate these features into existing code that may use standard language primitives for branching and control flow, such as `if` statements, `for` loops, and function calls. Unlike many data orchestration frameworks that require restructuring code into an explicit pipeline or DAG, the Functional API allows you to incorporate these capabilities without enforcing a rigid execution model. 

The Functional API uses two key building blocks: 

  * **`@entrypoint`**– Marks a function as the starting point of a workflow, encapsulating logic and managing execution flow, including handling long-running tasks and interrupts.
  * **`@task`**– Represents a discrete unit of work, such as an API call or data processing step, that can be executed asynchronously within an entrypoint. Tasks return a future-like object that can be awaited or resolved synchronously.



This provides a minimal abstraction for building workflows with state management and streaming.

Tip

For users who prefer a more declarative approach, LangGraph's [Graph API](https://langchain-ai.github.io/langgraph/concepts/low_level/) allows you to define workflows using a Graph paradigm. Both APIs share the same underlying runtime, so you can use them together in the same application. Please see the [Functional API vs. Graph API](https://langchain-ai.github.io/langgraph/concepts/functional_api/#functional-api-vs-graph-api) section for a comparison of the two paradigms.

## Example[¶](https://langchain-ai.github.io/langgraph/concepts/functional_api/#example "Permanent link")

Below we demonstrate a simple application that writes an essay and [interrupts](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/) to request human review.

```
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-0-1)fromlanggraph.funcimport entrypoint, task
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-0-2)fromlanggraph.typesimport interrupt
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-0-3)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-0-4)@task
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-0-5)defwrite_essay(topic: str) -> str:
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-0-6)"""Write an essay about the given topic."""
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-0-7)  time.sleep(1) # A placeholder for a long-running task.
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-0-8)  return f"An essay about topic: {topic}"
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-0-9)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-0-10)@entrypoint(checkpointer=MemorySaver())
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-0-11)defworkflow(topic: str) -> dict:
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-0-12)"""A simple workflow that writes an essay and asks for a review."""
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-0-13)  essay = write_essay("cat").result()
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-0-14)  is_approved = interrupt({
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-0-15)    # Any json-serializable payload provided to interrupt as argument.
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-0-16)    # It will be surfaced on the client side as an Interrupt when streaming data
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-0-17)    # from the workflow.
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-0-18)    "essay": essay, # The essay we want reviewed.
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-0-19)    # We can add any additional information that we need.
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-0-20)    # For example, introduce a key called "action" with some instructions.
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-0-21)    "action": "Please approve/reject the essay",
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-0-22)  })
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-0-23)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-0-24)  return {
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-0-25)    "essay": essay, # The essay that was generated
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-0-26)    "is_approved": is_approved, # Response from HIL
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-0-27)  }

```


API Reference: [entrypoint](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint) | [task](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.task) | [interrupt](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.interrupt)

Detailed Explanation

This workflow will write an essay about the topic "cat" and then pause to get a review from a human. The workflow can be interrupted for an indefinite amount of time until a review is provided.

When the workflow is resumed, it executes from the very start, but because the result of the `write_essay` task was already saved, the task result will be loaded from the checkpoint instead of being recomputed.

```
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-1-1)importtime
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-1-2)importuuid
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-1-4)fromlanggraph.funcimport entrypoint, task
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-1-5)fromlanggraph.typesimport interrupt
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-1-6)fromlanggraph.checkpoint.memoryimport MemorySaver
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-1-7)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-1-8)@task
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-1-9)defwrite_essay(topic: str) -> str:
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-1-10)"""Write an essay about the given topic."""
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-1-11)  time.sleep(1) # This is a placeholder for a long-running task.
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-1-12)  return f"An essay about topic: {topic}"
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-1-13)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-1-14)@entrypoint(checkpointer=MemorySaver())
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-1-15)defworkflow(topic: str) -> dict:
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-1-16)"""A simple workflow that writes an essay and asks for a review."""
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-1-17)  essay = write_essay("cat").result()
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-1-18)  is_approved = interrupt({
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-1-19)    # Any json-serializable payload provided to interrupt as argument.
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-1-20)    # It will be surfaced on the client side as an Interrupt when streaming data
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-1-21)    # from the workflow.
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-1-22)    "essay": essay, # The essay we want reviewed.
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-1-23)    # We can add any additional information that we need.
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-1-24)    # For example, introduce a key called "action" with some instructions.
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-1-25)    "action": "Please approve/reject the essay",
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-1-26)  })
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-1-27)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-1-28)  return {
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-1-29)    "essay": essay, # The essay that was generated
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-1-30)    "is_approved": is_approved, # Response from HIL
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-1-31)  }
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-1-32)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-1-33)thread_id = str(uuid.uuid4())
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-1-34)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-1-35)config = {
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-1-36)  "configurable": {
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-1-37)    "thread_id": thread_id
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-1-38)  }
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-1-39)}
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-1-40)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-1-41)for item in workflow.stream("cat", config):
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-1-42)  print(item)

```


API Reference: [entrypoint](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint) | [task](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.task) | [interrupt](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.interrupt) | [MemorySaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.MemorySaver)

```
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-2-1){'write_essay': 'An essay about topic: cat'}
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-2-2){'__interrupt__': (Interrupt(value={'essay': 'An essay about topic: cat', 'action': 'Please approve/reject the essay'}, resumable=True, ns=['workflow:f7b8508b-21c0-8b4c-5958-4e8de74d2684'], when='during'),)}

```


An essay has been written and is ready for review. Once the review is provided, we can resume the workflow:

```
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-3-1)fromlanggraph.typesimport Command
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-3-2)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-3-3)# Get review from a user (e.g., via a UI)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-3-4)# In this case, we're using a bool, but this can be any json-serializable value.
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-3-5)human_review = True
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-3-6)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-3-7)for item in workflow.stream(Command(resume=human_review), config):
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-3-8)  print(item)

```


API Reference: [Command](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Command)

```
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-4-1){'workflow': {'essay': 'An essay about topic: cat', 'is_approved': False}}

```


The workflow has been completed and the review has been added to the essay.

## Entrypoint[¶](https://langchain-ai.github.io/langgraph/concepts/functional_api/#entrypoint "Permanent link")

The `@entrypoint`[](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint) decorator can be used to create a workflow from a function. It encapsulates workflow logic and manages execution flow, including handling _long-running tasks_ and [interrupts](https://langchain-ai.github.io/langgraph/concepts/low_level/#interrupt).

### Definition[¶](https://langchain-ai.github.io/langgraph/concepts/functional_api/#definition "Permanent link")

An **entrypoint** is defined by decorating a function with the `@entrypoint` decorator. 

The function **must accept a single positional argument** , which serves as the workflow input. If you need to pass multiple pieces of data, use a dictionary as the input type for the first argument.

Decorating a function with an `entrypoint` produces a `Pregel`[](https://langchain-ai.github.io/langgraph/reference/pregel/#langgraph.pregel.Pregel.stream) instance which helps to manage the execution of the workflow (e.g., handles streaming, resumption, and checkpointing).

You will usually want to pass a **checkpointer** to the `@entrypoint` decorator to enable persistence and use features like **human-in-the-loop**.

[Sync](#__tabbed_1_1)[Async](#__tabbed_1_2)

```
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-5-1)fromlanggraph.funcimport entrypoint
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-5-2)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-5-3)@entrypoint(checkpointer=checkpointer)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-5-4)defmy_workflow(some_input: dict) -> int:
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-5-5)  # some logic that may involve long-running tasks like API calls,
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-5-6)  # and may be interrupted for human-in-the-loop.
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-5-7)  ...
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-5-8)  return result

```


API Reference: [entrypoint](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint)

```
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-6-1)fromlanggraph.funcimport entrypoint
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-6-2)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-6-3)@entrypoint(checkpointer=checkpointer)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-6-4)async defmy_workflow(some_input: dict) -> int:
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-6-5)  # some logic that may involve long-running tasks like API calls,
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-6-6)  # and may be interrupted for human-in-the-loop
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-6-7)  ...
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-6-8)  return result 

```


API Reference: [entrypoint](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint)

Serialization

The **inputs** and **outputs** of entrypoints must be JSON-serializable to support checkpointing. Please see the [serialization](https://langchain-ai.github.io/langgraph/concepts/functional_api/#serialization) section for more details.

### Injectable Parameters[¶](https://langchain-ai.github.io/langgraph/concepts/functional_api/#injectable-parameters "Permanent link")

When declaring an `entrypoint`, you can request access to additional parameters that will be injected automatically at run time. These parameters include:

Parameter | Description  
---|---  
**previous** | Access the the state associated with the previous `checkpoint` for the given thread. See [state management](https://langchain-ai.github.io/langgraph/concepts/functional_api/#state-management).  
**store** | An instance of [BaseStore](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore). Useful for [long-term memory](https://langchain-ai.github.io/langgraph/concepts/functional_api/#long-term-memory).  
**writer** | For streaming custom data, to write custom data to the `custom` stream. Useful for [streaming custom data](https://langchain-ai.github.io/langgraph/concepts/functional_api/#streaming-custom-data).  
**config** | For accessing run time configuration. See [RunnableConfig](https://python.langchain.com/docs/concepts/runnables/#runnableconfig) for information.  
  
Important

Declare the parameters with the appropriate name and type annotation.

Requesting Injectable Parameters

```
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-7-1)fromlangchain_core.runnablesimport RunnableConfig
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-7-2)fromlanggraph.funcimport entrypoint
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-7-3)fromlanggraph.store.baseimport BaseStore
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-7-4)fromlanggraph.store.memoryimport InMemoryStore
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-7-5)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-7-6)in_memory_store = InMemoryStore(...) # An instance of InMemoryStore for long-term memory
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-7-7)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-7-8)@entrypoint(
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-7-9)  checkpointer=checkpointer, # Specify the checkpointer
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-7-10)  store=in_memory_store # Specify the store
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-7-11)) 
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-7-12)defmy_workflow(
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-7-13)  some_input: dict, # The input (e.g., passed via `invoke`)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-7-14)  *,
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-7-15)  previous: Any = None, # For short-term memory
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-7-16)  store: BaseStore, # For long-term memory
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-7-17)  writer: StreamWriter, # For streaming custom data
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-7-18)  config: RunnableConfig # For accessing the configuration passed to the entrypoint
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-7-19)) -> ...:

```


API Reference: [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html) | [entrypoint](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint)

### Executing[¶](https://langchain-ai.github.io/langgraph/concepts/functional_api/#executing "Permanent link")

Using the `@entrypoint`[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#entrypoint) yields a `Pregel`[](https://langchain-ai.github.io/langgraph/reference/pregel/#langgraph.pregel.Pregel.stream) object that can be executed using the `invoke`, `ainvoke`, `stream`, and `astream` methods.

[Invoke](#__tabbed_2_1)[Async Invoke](#__tabbed_2_2)[Stream](#__tabbed_2_3)[Async Stream](#__tabbed_2_4)

```
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-8-1)config = {
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-8-2)  "configurable": {
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-8-3)    "thread_id": "some_thread_id"
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-8-4)  }
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-8-5)}
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-8-6)my_workflow.invoke(some_input, config) # Wait for the result synchronously

```


```
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-9-1)config = {
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-9-2)  "configurable": {
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-9-3)    "thread_id": "some_thread_id"
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-9-4)  }
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-9-5)}
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-9-6)await my_workflow.ainvoke(some_input, config) # Await result asynchronously

```


```
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-10-1)config = {
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-10-2)  "configurable": {
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-10-3)    "thread_id": "some_thread_id"
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-10-4)  }
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-10-5)}
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-10-6)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-10-7)for chunk in my_workflow.stream(some_input, config):
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-10-8)  print(chunk)

```


```
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-11-1)config = {
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-11-2)  "configurable": {
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-11-3)    "thread_id": "some_thread_id"
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-11-4)  }
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-11-5)}
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-11-6)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-11-7)async for chunk in my_workflow.astream(some_input, config):
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-11-8)  print(chunk)

```


### Resuming[¶](https://langchain-ai.github.io/langgraph/concepts/functional_api/#resuming "Permanent link")

Resuming an execution after an [interrupt](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.interrupt) can be done by passing a **resume** value to the [Command](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Command) primitive.

[Invoke](#__tabbed_3_1)[Async Invoke](#__tabbed_3_2)[Stream](#__tabbed_3_3)[Async Stream](#__tabbed_3_4)

```
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-12-1)fromlanggraph.typesimport Command
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-12-2)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-12-3)config = {
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-12-4)  "configurable": {
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-12-5)    "thread_id": "some_thread_id"
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-12-6)  }
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-12-7)}
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-12-8)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-12-9)my_workflow.invoke(Command(resume=some_resume_value), config)

```


API Reference: [Command](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Command)

```
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-13-1)fromlanggraph.typesimport Command
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-13-2)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-13-3)config = {
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-13-4)  "configurable": {
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-13-5)    "thread_id": "some_thread_id"
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-13-6)  }
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-13-7)}
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-13-8)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-13-9)await my_workflow.ainvoke(Command(resume=some_resume_value), config)

```


API Reference: [Command](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Command)

```
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-14-1)fromlanggraph.typesimport Command
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-14-2)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-14-3)config = {
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-14-4)  "configurable": {
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-14-5)    "thread_id": "some_thread_id"
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-14-6)  }
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-14-7)}
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-14-8)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-14-9)for chunk in my_workflow.stream(Command(resume=some_resume_value), config):
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-14-10)  print(chunk)

```


API Reference: [Command](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Command)

```
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-15-1)fromlanggraph.typesimport Command
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-15-2)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-15-3)config = {
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-15-4)  "configurable": {
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-15-5)    "thread_id": "some_thread_id"
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-15-6)  }
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-15-7)}
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-15-8)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-15-9)async for chunk in my_workflow.astream(Command(resume=some_resume_value), config):
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-15-10)  print(chunk)

```


API Reference: [Command](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Command)

**Resuming after an error**

To resume after an error, run the `entrypoint` with a `None` and the same **thread id** (config).

This assumes that the underlying **error** has been resolved and execution can proceed successfully.

[Invoke](#__tabbed_4_1)[Async Invoke](#__tabbed_4_2)[Stream](#__tabbed_4_3)[Async Stream](#__tabbed_4_4)

```
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-16-1)config = {
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-16-2)  "configurable": {
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-16-3)    "thread_id": "some_thread_id"
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-16-4)  }
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-16-5)}
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-16-6)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-16-7)my_workflow.invoke(None, config)

```


```
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-17-1)config = {
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-17-2)  "configurable": {
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-17-3)    "thread_id": "some_thread_id"
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-17-4)  }
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-17-5)}
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-17-6)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-17-7)await my_workflow.ainvoke(None, config)

```


```
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-18-1)config = {
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-18-2)  "configurable": {
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-18-3)    "thread_id": "some_thread_id"
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-18-4)  }
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-18-5)}
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-18-6)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-18-7)for chunk in my_workflow.stream(None, config):
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-18-8)  print(chunk)

```


```
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-19-1)config = {
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-19-2)  "configurable": {
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-19-3)    "thread_id": "some_thread_id"
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-19-4)  }
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-19-5)}
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-19-6)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-19-7)async for chunk in my_workflow.astream(None, config):
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-19-8)  print(chunk)

```


### State Management[¶](https://langchain-ai.github.io/langgraph/concepts/functional_api/#state-management "Permanent link")

When an `entrypoint` is defined with a `checkpointer`, it stores information between successive invocations on the same **thread id** in [checkpoints](https://langchain-ai.github.io/langgraph/concepts/persistence/#checkpoints). 

This allows accessing the state from the previous invocation using the `previous` parameter.

By default, the `previous` parameter is the return value of the previous invocation.

```
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-20-1)@entrypoint(checkpointer=checkpointer)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-20-2)defmy_workflow(number: int, *, previous: Any = None) -> int:
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-20-3)  previous = previous or 0
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-20-4)  return number + previous
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-20-5)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-20-6)config = {
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-20-7)  "configurable": {
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-20-8)    "thread_id": "some_thread_id"
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-20-9)  }
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-20-10)}
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-20-11)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-20-12)my_workflow.invoke(1, config) # 1 (previous was None)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-20-13)my_workflow.invoke(2, config) # 3 (previous was 1 from the previous invocation)

```


#### `entrypoint.final`[¶](https://langchain-ai.github.io/langgraph/concepts/functional_api/#entrypointfinal "Permanent link")

[entrypoint.final](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint.final) is a special primitive that can be returned from an entrypoint and allows **decoupling** the value that is **saved in the checkpoint** from the **return value of the entrypoint**.

The first value is the return value of the entrypoint, and the second value is the value that will be saved in the checkpoint. The type annotation is `entrypoint.final[return_type, save_type]`.

```
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-21-1)@entrypoint(checkpointer=checkpointer)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-21-2)defmy_workflow(number: int, *, previous: Any = None) -> entrypoint.final[int, int]:
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-21-3)  previous = previous or 0
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-21-4)  # This will return the previous value to the caller, saving
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-21-5)  # 2 * number to the checkpoint, which will be used in the next invocation 
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-21-6)  # for the `previous` parameter.
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-21-7)  return entrypoint.final(value=previous, save=2 * number)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-21-8)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-21-9)config = {
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-21-10)  "configurable": {
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-21-11)    "thread_id": "1"
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-21-12)  }
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-21-13)}
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-21-14)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-21-15)my_workflow.invoke(3, config) # 0 (previous was None)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-21-16)my_workflow.invoke(1, config) # 6 (previous was 3 * 2 from the previous invocation)

```


## Task[¶](https://langchain-ai.github.io/langgraph/concepts/functional_api/#task "Permanent link")

A **task** represents a discrete unit of work, such as an API call or data processing step. It has two key characteristics:

  * **Asynchronous Execution** : Tasks are designed to be executed asynchronously, allowing multiple operations to run concurrently without blocking.
  * **Checkpointing** : Task results are saved to a checkpoint, enabling resumption of the workflow from the last saved state. (See [persistence](https://langchain-ai.github.io/langgraph/concepts/persistence/) for more details).



### Definition[¶](https://langchain-ai.github.io/langgraph/concepts/functional_api/#definition_1 "Permanent link")

Tasks are defined using the `@task` decorator, which wraps a regular Python function.

```
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-22-1)fromlanggraph.funcimport task
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-22-2)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-22-3)@task()
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-22-4)defslow_computation(input_value):
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-22-5)  # Simulate a long-running operation
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-22-6)  ...
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-22-7)  return result

```


API Reference: [task](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.task)

Serialization

The **outputs** of tasks must be JSON-serializable to support checkpointing.

### Execution[¶](https://langchain-ai.github.io/langgraph/concepts/functional_api/#execution "Permanent link")

**Tasks** can only be called from within an **entrypoint** , another **task** , or a [state graph node](https://langchain-ai.github.io/langgraph/concepts/low_level/#nodes). 

Tasks _cannot_ be called directly from the main application code. 

When you call a **task** , it returns _immediately_ with a future object. A future is a placeholder for a result that will be available later.

To obtain the result of a **task** , you can either wait for it synchronously (using `result()`) or await it asynchronously (using `await`).

[Synchronous Invocation](#__tabbed_5_1)[Asynchronous Invocation](#__tabbed_5_2)

```
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-23-1)@entrypoint(checkpointer=checkpointer)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-23-2)defmy_workflow(some_input: int) -> int:
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-23-3)  future = slow_computation(some_input)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-23-4)  return future.result() # Wait for the result synchronously

```


```
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-24-1)@entrypoint(checkpointer=checkpointer)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-24-2)async defmy_workflow(some_input: int) -> int:
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-24-3)  return await slow_computation(some_input) # Await result asynchronously

```


## When to use a task[¶](https://langchain-ai.github.io/langgraph/concepts/functional_api/#when-to-use-a-task "Permanent link")

**Tasks** are useful in the following scenarios:

  * **Checkpointing** : When you need to save the result of a long-running operation to a checkpoint, so you don't need to recompute it when resuming the workflow.
  * **Human-in-the-loop** : If you're building a workflow that requires human intervention, you MUST use **tasks** to encapsulate any randomness (e.g., API calls) to ensure that the workflow can be resumed correctly. See the [determinism](https://langchain-ai.github.io/langgraph/concepts/functional_api/#determinism) section for more details.
  * **Parallel Execution** : For I/O-bound tasks, **tasks** enable parallel execution, allowing multiple operations to run concurrently without blocking (e.g., calling multiple APIs).
  * **Observability** : Wrapping operations in **tasks** provides a way to track the progress of the workflow and monitor the execution of individual operations using [LangSmith](https://docs.smith.langchain.com/).
  * **Retryable Work** : When work needs to be retried to handle failures or inconsistencies, **tasks** provide a way to encapsulate and manage the retry logic.



## Serialization[¶](https://langchain-ai.github.io/langgraph/concepts/functional_api/#serialization "Permanent link")

There are two key aspects to serialization in LangGraph:

  1. `@entrypoint` inputs and outputs must be JSON-serializable.
  2. `@task` outputs must be JSON-serializable.



These requirements are necessary for enabling checkpointing and workflow resumption. Use python primitives like dictionaries, lists, strings, numbers, and booleans to ensure that your inputs and outputs are serializable.

Serialization ensures that workflow state, such as task results and intermediate values, can be reliably saved and restored. This is critical for enabling human-in-the-loop interactions, fault tolerance, and parallel execution.

Providing non-serializable inputs or outputs will result in a runtime error when a workflow is configured with a checkpointer.

## Determinism[¶](https://langchain-ai.github.io/langgraph/concepts/functional_api/#determinism "Permanent link")

To utilize features like **human-in-the-loop** , any randomness should be encapsulated inside of **tasks**. This guarantees that when execution is halted (e.g., for human in the loop) and then resumed, it will follow the same _sequence of steps_ , even if **task** results are non-deterministic.

LangGraph achieves this behavior by persisting **task** and [**subgraph**](https://langchain-ai.github.io/langgraph/concepts/low_level/#subgraphs) results as they execute. A well-designed workflow ensures that resuming execution follows the _same sequence of steps_ , allowing previously computed results to be retrieved correctly without having to re-execute them. This is particularly useful for long-running **tasks** or **tasks** with non-deterministic results, as it avoids repeating previously done work and allows resuming from essentially the same 

While different runs of a workflow can produce different results, resuming a **specific** run should always follow the same sequence of recorded steps. This allows LangGraph to efficiently look up **task** and **subgraph** results that were executed prior to the graph being interrupted and avoid recomputing them.

## Idempotency[¶](https://langchain-ai.github.io/langgraph/concepts/functional_api/#idempotency "Permanent link")

Idempotency ensures that running the same operation multiple times produces the same result. This helps prevent duplicate API calls and redundant processing if a step is rerun due to a failure. Always place API calls inside **tasks** functions for checkpointing, and design them to be idempotent in case of re-execution. Re-execution can occur if a **task** starts, but does not complete successfully. Then, if the workflow is resumed, the **task** will run again. Use idempotency keys or verify existing results to avoid duplication.

## Functional API vs. Graph API[¶](https://langchain-ai.github.io/langgraph/concepts/functional_api/#functional-api-vs-graph-api "Permanent link")

The **Functional API** and the [Graph APIs (StateGraph)](https://langchain-ai.github.io/langgraph/concepts/low_level/#stategraph) provide two different paradigms to create applications with LangGraph. Here are some key differences:

  * **Control flow** : The Functional API does not require thinking about graph structure. You can use standard Python constructs to define workflows. This will usually trim the amount of code you need to write.
  * **State management** : The **GraphAPI** requires declaring a [**State**](https://langchain-ai.github.io/langgraph/concepts/low_level/#state) and may require defining [**reducers**](https://langchain-ai.github.io/langgraph/concepts/low_level/#reducers) to manage updates to the graph state. `@entrypoint` and `@tasks` do not require explicit state management as their state is scoped to the function and is not shared across functions.
  * **Checkpointing** : Both APIs generate and use checkpoints. In the **Graph API** a new checkpoint is generated after every [superstep](https://langchain-ai.github.io/langgraph/concepts/low_level/). In the **Functional API** , when tasks are executed, their results are saved to an existing checkpoint associated with the given entrypoint instead of creating a new checkpoint.
  * **Visualization** : The Graph API makes it easy to visualize the workflow as a graph which can be useful for debugging, understanding the workflow, and sharing with others. The Functional API does not support visualization as the graph is dynamically generated during runtime.



## Common Pitfalls[¶](https://langchain-ai.github.io/langgraph/concepts/functional_api/#common-pitfalls "Permanent link")

### Handling side effects[¶](https://langchain-ai.github.io/langgraph/concepts/functional_api/#handling-side-effects "Permanent link")

Encapsulate side effects (e.g., writing to a file, sending an email) in tasks to ensure they are not executed multiple times when resuming a workflow.

[Incorrect](#__tabbed_6_1)[Correct](#__tabbed_6_2)

In this example, a side effect (writing to a file) is directly included in the workflow, so it will be executed a second time when resuming the workflow.

```
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-25-1)@entrypoint(checkpointer=checkpointer)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-25-2)defmy_workflow(inputs: dict) -> int:
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-25-3)  # This code will be executed a second time when resuming the workflow.
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-25-4)  # Which is likely not what you want.
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-25-5)  with open("output.txt", "w") as f:
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-25-6)    f.write("Side effect executed")
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-25-7)  value = interrupt("question")
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-25-8)  return value

```


In this example, the side effect is encapsulated in a task, ensuring consistent execution upon resumption.

```
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-26-1)fromlanggraph.funcimport task
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-26-2)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-26-3)@task
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-26-4)defwrite_to_file():
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-26-5)  with open("output.txt", "w") as f:
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-26-6)    f.write("Side effect executed")
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-26-7)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-26-8)@entrypoint(checkpointer=checkpointer)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-26-9)defmy_workflow(inputs: dict) -> int:
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-26-10)  # The side effect is now encapsulated in a task.
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-26-11)  write_to_file().result()
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-26-12)  value = interrupt("question")
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-26-13)  return value

```


API Reference: [task](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.task)

### Non-deterministic control flow[¶](https://langchain-ai.github.io/langgraph/concepts/functional_api/#non-deterministic-control-flow "Permanent link")

Operations that might give different results each time (like getting current time or random numbers) should be encapsulated in tasks to ensure that on resume, the same result is returned.

  * In a task: Get random number (5) → interrupt → resume → (returns 5 again) → ...
  * Not in a task: Get random number (5) → interrupt → resume → get new random number (7) → ...



This is especially important when using **human-in-the-loop** workflows with multiple interrupts calls. LangGraph keeps a list of resume values for each task/entrypoint. When an interrupt is encountered, it's matched with the corresponding resume value. This matching is strictly **index-based** , so the order of the resume values should match the order of the interrupts.

If order of execution is not maintained when resuming, one `interrupt` call may be matched with the wrong `resume` value, leading to incorrect results.

Please read the section on [determinism](https://langchain-ai.github.io/langgraph/concepts/functional_api/#determinism) for more details.

[Incorrect](#__tabbed_7_1)[Correct](#__tabbed_7_2)

In this example, the workflow uses the current time to determine which task to execute. This is non-deterministic because the result of the workflow depends on the time at which it is executed.

```
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-27-1)fromlanggraph.funcimport entrypoint
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-27-2)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-27-3)@entrypoint(checkpointer=checkpointer)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-27-4)defmy_workflow(inputs: dict) -> int:
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-27-5)  t0 = inputs["t0"]
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-27-6)  t1 = time.time()
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-27-7)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-27-8)  delta_t = t1 - t0
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-27-9)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-27-10)  if delta_t > 1:
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-27-11)    result = slow_task(1).result()
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-27-12)    value = interrupt("question")
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-27-13)  else:
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-27-14)    result = slow_task(2).result()
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-27-15)    value = interrupt("question")
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-27-16)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-27-17)  return {
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-27-18)    "result": result,
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-27-19)    "value": value
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-27-20)  }

```


API Reference: [entrypoint](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint)

In this example, the workflow uses the input `t0` to determine which task to execute. This is deterministic because the result of the workflow depends only on the input.

```
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-28-1)importtime
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-28-2)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-28-3)fromlanggraph.funcimport task
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-28-4)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-28-5)@task
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-28-6)defget_time() -> float:
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-28-7)  return time.time()
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-28-8)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-28-9)@entrypoint(checkpointer=checkpointer)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-28-10)defmy_workflow(inputs: dict) -> int:
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-28-11)  t0 = inputs["t0"]
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-28-12)  t1 = get_time().result()
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-28-13)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-28-14)  delta_t = t1 - t0
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-28-15)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-28-16)  if delta_t > 1:
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-28-17)    result = slow_task(1).result()
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-28-18)    value = interrupt("question")
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-28-19)  else:
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-28-20)    result = slow_task(2).result()
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-28-21)    value = interrupt("question")
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-28-22)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-28-23)  return {
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-28-24)    "result": result,
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-28-25)    "value": value
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-28-26)  }

```


API Reference: [task](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.task)

## Patterns[¶](https://langchain-ai.github.io/langgraph/concepts/functional_api/#patterns "Permanent link")

Below are a few simple patterns that show examples of **how to** use the **Functional API**.

When defining an `entrypoint`, input is restricted to the first argument of the function. To pass multiple inputs, you can use a dictionary.

```
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-29-1)@entrypoint(checkpointer=checkpointer)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-29-2)defmy_workflow(inputs: dict) -> int:
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-29-3)  value = inputs["value"]
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-29-4)  another_value = inputs["another_value"]
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-29-5)  ...
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-29-6)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-29-7)my_workflow.invoke({"value": 1, "another_value": 2}) 

```


### Parallel execution[¶](https://langchain-ai.github.io/langgraph/concepts/functional_api/#parallel-execution "Permanent link")

Tasks can be executed in parallel by invoking them concurrently and waiting for the results. This is useful for improving performance in IO bound tasks (e.g., calling APIs for LLMs).

```
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-30-1)@task
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-30-2)defadd_one(number: int) -> int:
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-30-3)  return number + 1
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-30-4)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-30-5)@entrypoint(checkpointer=checkpointer)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-30-6)defgraph(numbers: list[int]) -> list[str]:
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-30-7)  futures = [add_one(i) for i in numbers]
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-30-8)  return [f.result() for f in futures]

```


### Calling subgraphs[¶](https://langchain-ai.github.io/langgraph/concepts/functional_api/#calling-subgraphs "Permanent link")

The **Functional API** and the [**Graph API**](https://langchain-ai.github.io/langgraph/concepts/low_level/) can be used together in the same application as they share the same underlying runtime.

```
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-31-1)fromlanggraph.funcimport entrypoint
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-31-2)fromlanggraph.graphimport StateGraph
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-31-3)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-31-4)builder = StateGraph()
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-31-5)...
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-31-6)some_graph = builder.compile()
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-31-7)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-31-8)@entrypoint()
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-31-9)defsome_workflow(some_input: dict) -> int:
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-31-10)  # Call a graph defined using the graph API
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-31-11)  result_1 = some_graph.invoke(...)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-31-12)  # Call another graph defined using the graph API
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-31-13)  result_2 = another_graph.invoke(...)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-31-14)  return {
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-31-15)    "result_1": result_1,
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-31-16)    "result_2": result_2
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-31-17)  }

```


API Reference: [entrypoint](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph)

### Calling other entrypoints[¶](https://langchain-ai.github.io/langgraph/concepts/functional_api/#calling-other-entrypoints "Permanent link")

You can call other **entrypoints** from within an **entrypoint** or a **task**.

```
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-32-1)@entrypoint() # Will automatically use the checkpointer from the parent entrypoint
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-32-2)defsome_other_workflow(inputs: dict) -> int:
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-32-3)  return inputs["value"]
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-32-4)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-32-5)@entrypoint(checkpointer=checkpointer)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-32-6)defmy_workflow(inputs: dict) -> int:
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-32-7)  value = some_other_workflow.invoke({"value": 1})
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-32-8)  return value

```


### Streaming custom data[¶](https://langchain-ai.github.io/langgraph/concepts/functional_api/#streaming-custom-data "Permanent link")

You can stream custom data from an **entrypoint** by using the `StreamWriter` type. This allows you to write custom data to the `custom` stream.

```
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-33-1)fromlanggraph.checkpoint.memoryimport MemorySaver
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-33-2)fromlanggraph.funcimport entrypoint, task
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-33-3)fromlanggraph.typesimport StreamWriter
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-33-4)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-33-5)@task
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-33-6)defadd_one(x):
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-33-7)  return x + 1
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-33-8)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-33-9)@task
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-33-10)defadd_two(x):
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-33-11)  return x + 2
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-33-12)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-33-13)checkpointer = MemorySaver()
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-33-14)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-33-15)@entrypoint(checkpointer=checkpointer)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-33-16)defmain(inputs, writer: StreamWriter) -> int:
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-33-17)"""A simple workflow that adds one and two to a number."""
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-33-18)  writer("hello") # Write some data to the `custom` stream
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-33-19)  add_one(inputs['number']).result() # Will write data to the `updates` stream
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-33-20)  writer("world") # Write some more data to the `custom` stream
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-33-21)  add_two(inputs['number']).result() # Will write data to the `updates` stream
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-33-22)  return 5 
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-33-23)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-33-24)config = {
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-33-25)  "configurable": {
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-33-26)    "thread_id": "1"
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-33-27)  }
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-33-28)}
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-33-29)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-33-30)for chunk in main.stream({"number": 1}, stream_mode=["custom", "updates"], config=config):
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-33-31)  print(chunk)

```


API Reference: [MemorySaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.MemorySaver) | [entrypoint](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint) | [task](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.task)

```
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-34-1)('updates', {'add_one': 2})
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-34-2)('updates', {'add_two': 3})
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-34-3)('custom', 'hello')
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-34-4)('custom', 'world')
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-34-5)('updates', {'main': 5})

```


Important

The `writer` parameter is automatically injected at run time. It will only be injected if the parameter name appears in the function signature with that _exact_ name.

### Retry policy[¶](https://langchain-ai.github.io/langgraph/concepts/functional_api/#retry-policy "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-35-1)fromlanggraph.checkpoint.memoryimport MemorySaver
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-35-2)fromlanggraph.funcimport entrypoint, task
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-35-3)fromlanggraph.typesimport RetryPolicy
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-35-4)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-35-5)attempts = 0
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-35-6)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-35-7)# Let's configure the RetryPolicy to retry on ValueError.
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-35-8)# The default RetryPolicy is optimized for retrying specific network errors.
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-35-9)retry_policy = RetryPolicy(retry_on=ValueError)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-35-10)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-35-11)@task(retry=retry_policy) 
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-35-12)defget_info():
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-35-13)  global attempts
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-35-14)  attempts += 1
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-35-15)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-35-16)  if attempts < 2:
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-35-17)    raise ValueError('Failure')
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-35-18)  return "OK"
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-35-19)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-35-20)checkpointer = MemorySaver()
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-35-21)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-35-22)@entrypoint(checkpointer=checkpointer)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-35-23)defmain(inputs, writer):
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-35-24)  return get_info().result()
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-35-25)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-35-26)config = {
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-35-27)  "configurable": {
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-35-28)    "thread_id": "1"
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-35-29)  }
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-35-30)}
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-35-31)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-35-32)main.invoke({'any_input': 'foobar'}, config=config)

```


API Reference: [MemorySaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.MemorySaver) | [entrypoint](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint) | [task](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.task) | [RetryPolicy](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.RetryPolicy)

```
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-36-1)'OK'

```


### Resuming after an error[¶](https://langchain-ai.github.io/langgraph/concepts/functional_api/#resuming-after-an-error "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-1)importtime
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-2)fromlanggraph.checkpoint.memoryimport MemorySaver
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-3)fromlanggraph.funcimport entrypoint, task
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-4)fromlanggraph.typesimport StreamWriter
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-5)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-6)# Global variable to track the number of attempts
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-7)attempts = 0
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-8)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-9)@task()
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-10)defget_info():
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-11)"""
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-12)  Simulates a task that fails once before succeeding.
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-13)  Raises an exception on the first attempt, then returns "OK" on subsequent tries.
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-14)  """
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-15)  global attempts
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-16)  attempts += 1
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-17)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-18)  if attempts < 2:
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-19)    raise ValueError("Failure") # Simulate a failure on the first attempt
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-20)  return "OK"
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-21)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-22)# Initialize an in-memory checkpointer for persistence
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-23)checkpointer = MemorySaver()
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-24)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-25)@task
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-26)defslow_task():
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-27)"""
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-28)  Simulates a slow-running task by introducing a 1-second delay.
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-29)  """
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-30)  time.sleep(1)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-31)  return "Ran slow task."
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-32)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-33)@entrypoint(checkpointer=checkpointer)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-34)defmain(inputs, writer: StreamWriter):
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-35)"""
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-36)  Main workflow function that runs the slow_task and get_info tasks sequentially.
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-37)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-38)  Parameters:
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-39)  - inputs: Dictionary containing workflow input values.
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-40)  - writer: StreamWriter for streaming custom data.
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-41)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-42)  The workflow first executes `slow_task` and then attempts to execute `get_info`,
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-43)  which will fail on the first invocation.
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-44)  """
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-45)  slow_task_result = slow_task().result() # Blocking call to slow_task
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-46)  get_info().result() # Exception will be raised here on the first attempt
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-47)  return slow_task_result
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-48)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-49)# Workflow execution configuration with a unique thread identifier
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-50)config = {
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-51)  "configurable": {
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-52)    "thread_id": "1" # Unique identifier to track workflow execution
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-53)  }
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-54)}
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-55)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-56)# This invocation will take ~1 second due to the slow_task execution
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-57)try:
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-58)  # First invocation will raise an exception due to the `get_info` task failing
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-59)  main.invoke({'any_input': 'foobar'}, config=config)
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-60)except ValueError:
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-37-61)  pass # Handle the failure gracefully

```


API Reference: [MemorySaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.MemorySaver) | [entrypoint](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint) | [task](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.task)

When we resume execution, we won't need to re-run the `slow_task` as its result is already saved in the checkpoint.

```
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-38-1)main.invoke(None, config=config)

```


```
[](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__codelineno-39-1)'Ran slow task.'

```


### Human-in-the-loop[¶](https://langchain-ai.github.io/langgraph/concepts/functional_api/#human-in-the-loop "Permanent link")

The functional API supports [human-in-the-loop](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/) workflows using the `interrupt` function and the `Command` primitive.

Please see the following examples for more details:

  * [How to wait for user input (Functional API)](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/): Shows how to implement a simple human-in-the-loop workflow using the functional API.
  * [How to review tool calls (Functional API)](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/): Guide demonstrates how to implement human-in-the-loop workflows in a ReAct agent using the LangGraph Functional API.



### Short-term memory[¶](https://langchain-ai.github.io/langgraph/concepts/functional_api/#short-term-memory "Permanent link")

[State management](https://langchain-ai.github.io/langgraph/concepts/functional_api/#state-management) using the **previous** parameter and optionally using the `entrypoint.final` primitive can be used to implement [short term memory](https://langchain-ai.github.io/langgraph/concepts/memory/).

Please see the following how-to guides for more details:

  * [How to add thread-level persistence (functional API)](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/): Shows how to add thread-level persistence to a functional API workflow and implements a simple chatbot.



### Long-term memory[¶](https://langchain-ai.github.io/langgraph/concepts/functional_api/#long-term-memory "Permanent link")

[long-term memory](https://langchain-ai.github.io/langgraph/concepts/memory/#long-term-memory) allows storing information across different **thread ids**. This could be useful for learning information about a given user in one conversation and using it in another.

Please see the following how-to guides for more details:

  * [How to add cross-thread persistence (functional API)](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/): Shows how to add cross-thread persistence to a functional API workflow and implements a simple chatbot.



### Workflows[¶](https://langchain-ai.github.io/langgraph/concepts/functional_api/#workflows "Permanent link")

  * [Workflows and agent](https://langchain-ai.github.io/langgraph/tutorials/workflows/) guide for more examples of how to build workflows using the Functional API.



### Agents[¶](https://langchain-ai.github.io/langgraph/concepts/functional_api/#agents "Permanent link")

  * [How to create a React agent from scratch (Functional API)](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/): Shows how to create a simple React agent from scratch using the functional API.
  * [How to build a multi-agent network](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/): Shows how to build a multi-agent network using the functional API.
  * [How to add multi-turn conversation in a multi-agent application (functional API)](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/): allow an end-user to engage in a multi-turn conversation with one or more agents. 

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Streaming  ](https://langchain-ai.github.io/langgraph/concepts/streaming/) [ Next  LangGraph Platform  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_platform/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/concepts/functional_api/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
