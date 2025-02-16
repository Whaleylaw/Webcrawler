---
url: https://langchain-ai.github.io/langgraph/reference/func/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Functional API 

[ ](https://langchain-ai.github.io/langgraph/reference/func/?q= "Share")

Type to start searching

[ GitHub  ](https://github.com/langchain-ai/langgraph "Go to repository")

  * [ Home ](https://langchain-ai.github.io/langgraph/)
  * [ API reference ](https://langchain-ai.github.io/langgraph/reference/graphs/)



[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

[ GitHub  ](https://github.com/langchain-ai/langgraph "Go to repository")

  * [ Home  ](https://langchain-ai.github.io/langgraph/)
  * API reference  API reference 
    * Library  Library 
      * [ Graphs  ](https://langchain-ai.github.io/langgraph/reference/graphs/)
      * [ Checkpointing  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/)
      * [ Storage  ](https://langchain-ai.github.io/langgraph/reference/store/)
      * [ Prebuilt components  ](https://langchain-ai.github.io/langgraph/reference/prebuilt/)
      * [ Channels  ](https://langchain-ai.github.io/langgraph/reference/channels/)
      * [ Errors  ](https://langchain-ai.github.io/langgraph/reference/errors/)
      * [ Types  ](https://langchain-ai.github.io/langgraph/reference/types/)
      * [ Constants  ](https://langchain-ai.github.io/langgraph/reference/constants/)
      * [ Pregel  ](https://langchain-ai.github.io/langgraph/reference/pregel/)
      * [ Config  ](https://langchain-ai.github.io/langgraph/reference/config/)
      * Functional API  [ Functional API  ](https://langchain-ai.github.io/langgraph/reference/func/) Table of contents 
        * [ entrypoint  ](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint)
          * [ Function signature  ](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint--function-signature)
          * [ Injectable parameters  ](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint--injectable-parameters)
          * [ State management  ](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint--state-management)
          * [ final  ](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint.final)
            * [ value  ](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint.final.value)
            * [ save  ](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint.final.save)
          * [ __init__  ](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint.__init__)
          * [ __call__  ](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint.__call__)
        * [ task  ](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.task)
    * LangGraph Platform  LangGraph Platform 
      * [ Server API  ](https://langchain-ai.github.io/langgraph/cloud/reference/api/api_ref/)
      * [ CLI  ](https://langchain-ai.github.io/langgraph/cloud/reference/cli/)
      * [ SDK (Python)  ](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/)
      * [ SDK (JS/TS)  ](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/)
      * [ RemoteGraph  ](https://langchain-ai.github.io/langgraph/reference/remote_graph/)
      * [ Environment variables  ](https://langchain-ai.github.io/langgraph/cloud/reference/env_var/)



Table of contents 

  * [ entrypoint  ](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint)
    * [ Function signature  ](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint--function-signature)
    * [ Injectable parameters  ](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint--injectable-parameters)
    * [ State management  ](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint--state-management)
    * [ final  ](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint.final)
      * [ value  ](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint.final.value)
      * [ save  ](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint.final.save)
    * [ __init__  ](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint.__init__)
    * [ __call__  ](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint.__call__)
  * [ task  ](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.task)



  1. [ API reference  ](https://langchain-ai.github.io/langgraph/reference/graphs/)
  2. [ Library  ](https://langchain-ai.github.io/langgraph/reference/graphs/)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/reference/func.md "Edit this page")

# Functional API

##  `entrypoint` [¶](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint "Permanent link")

Define a LangGraph workflow using the `entrypoint` decorator.

Beta

The Functional API is currently in beta and is subject to change.

##### Function signature[¶](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint--function-signature "Permanent link")

The decorated function must accept a **single parameter** , which serves as the input to the function. This input parameter can be of any type. Use a dictionary to pass **multiple parameters** to the function.

##### Injectable parameters[¶](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint--injectable-parameters "Permanent link")

The decorated function can request access to additional parameters that will be injected automatically at run time. These parameters include:

Parameter | Description  
---|---  
**`store`**|  An instance of [BaseStore](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore). Useful for long-term memory.  
**`writer`**|  A [StreamWriter](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.StreamWriter) instance for writing custom data to a stream.  
**`config`**|  A configuration object (aka RunnableConfig) that holds run-time configuration values.  
**`previous`**|  The previous return value for the given thread (available only when a checkpointer is provided).  
  
The entrypoint decorator can be applied to sync functions or async functions.

##### State management[¶](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint--state-management "Permanent link")

The **`previous`**parameter can be used to access the return value of the previous invocation of the entrypoint on the same thread id. This value is only available when a checkpointer is provided.

If you want **`previous`**to be different from the return value, you can use the`entrypoint.final` object to return a value while saving a different value to the checkpoint.

Parameters:

  * **`checkpointer`**(`Optional[BaseCheckpointSaver]` , default: `None` ) – 

Specify a checkpointer to create a workflow that can persist its state across runs.

  * **`store`**(`Optional[BaseStore]` , default: `None` ) – 

A generalized key-value store. Some implementations may support semantic search capabilities through an optional `index` configuration.

  * **`config_schema`**(`Optional[type[Any]]` , default: `None` ) – 

Specifies the schema for the configuration object that will be passed to the workflow.


Using entrypoint and tasks

```
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-1)importtime
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-2)
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-3)fromlanggraph.funcimport entrypoint, task
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-4)fromlanggraph.typesimport interrupt, Command
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-5)fromlanggraph.checkpoint.memoryimport MemorySaver
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-6)
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-7)@task
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-8)defcompose_essay(topic: str) -> str:
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-9)  time.sleep(1.0) # Simulate slow operation
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-10)  return f"An essay about {topic}"
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-11)
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-12)@entrypoint(checkpointer=MemorySaver())
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-13)defreview_workflow(topic: str) -> dict:
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-14)"""Manages the workflow for generating and reviewing an essay.
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-15)
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-16)  The workflow includes:
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-17)  1. Generating an essay about the given topic.
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-18)  2. Interrupting the workflow for human review of the generated essay.
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-19)
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-20)  Upon resuming the workflow, compose_essay task will not be re-executed
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-21)  as its result is cached by the checkpointer.
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-22)
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-23)  Args:
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-24)    topic (str): The subject of the essay.
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-25)
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-26)  Returns:
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-27)    dict: A dictionary containing the generated essay and the human review.
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-28)  """
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-29)  essay_future = compose_essay(topic)
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-30)  essay = essay_future.result()
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-31)  human_review = interrupt({
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-32)    "question": "Please provide a review",
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-33)    "essay": essay
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-34)  })
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-35)  return {
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-36)    "essay": essay,
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-37)    "review": human_review,
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-38)  }
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-39)
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-40)# Example configuration for the workflow
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-41)config = {
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-42)  "configurable": {
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-43)    "thread_id": "some_thread"
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-44)  }
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-45)}
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-46)
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-47)# Topic for the essay
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-48)topic = "cats"
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-49)
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-50)# Stream the workflow to generate the essay and await human review
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-51)for result in review_workflow.stream(topic, config):
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-52)  print(result)
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-53)
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-54)# Example human review provided after the interrupt
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-55)human_review = "This essay is great."
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-56)
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-57)# Resume the workflow with the provided human review
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-58)for result in review_workflow.stream(Command(resume=human_review), config):
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-59)  print(result)

```


Accessing the previous return value

When a checkpointer is enabled the function can access the previous return value of the previous invocation on the same thread id.

```
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-1)fromlanggraph.checkpoint.memoryimport MemorySaver
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-2)fromlanggraph.funcimport entrypoint
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-3)
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-4)@entrypoint(checkpointer=MemorySaver())
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-5)defmy_workflow(input_data: str, previous: Optional[str] = None) -> str:
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-6)  return "world"
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-7)
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-8)config = {
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-9)  "configurable": {
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-10)    "thread_id": "some_thread"
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-11)  }
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-12)}
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-13)my_workflow.invoke("hello")

```


Using entrypoint.final to save a value

The `entrypoint.final` object allows you to return a value while saving a different value to the checkpoint. This value will be accessible in the next invocation of the entrypoint via the `previous` parameter, as long as the same thread id is used.

```
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-1)fromlanggraph.checkpoint.memoryimport MemorySaver
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-2)fromlanggraph.funcimport entrypoint
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-3)
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-4)@entrypoint(checkpointer=MemorySaver())
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-5)defmy_workflow(number: int, *, previous: Any = None) -> entrypoint.final[int, int]:
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-6)  previous = previous or 0
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-7)  # This will return the previous value to the caller, saving
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-8)  # 2 * number to the checkpoint, which will be used in the next invocation
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-9)  # for the `previous` parameter.
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-10)  return entrypoint.final(value=previous, save=2 * number)
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-11)
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-12)config = {
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-13)  "configurable": {
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-14)    "thread_id": "some_thread"
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-15)  }
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-16)}
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-17)
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-18)my_workflow.invoke(3, config) # 0 (previous was None)
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-19)my_workflow.invoke(1, config) # 6 (previous was 3 * 2 from the previous invocation)

```


###  `final` `dataclass` [¶](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint.final "Permanent link")

Bases: `Generic[R, S]`

A primitive that can be returned from an entrypoint.

This primitive allows to save a value to the checkpointer distinct from the return value from the entrypoint.

Decoupling the return value and the save value

```
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-1)fromlanggraph.checkpoint.memoryimport MemorySaver
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-2)fromlanggraph.funcimport entrypoint
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-3)
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-4)@entrypoint(checkpointer=MemorySaver())
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-5)defmy_workflow(number: int, *, previous: Any = None) -> entrypoint.final[int, int]:
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-6)  previous = previous or 0
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-7)  # This will return the previous value to the caller, saving
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-8)  # 2 * number to the checkpoint, which will be used in the next invocation
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-9)  # for the `previous` parameter.
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-10)  return entrypoint.final(value=previous, save=2 * number)
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-11)
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-12)config = {
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-13)  "configurable": {
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-14)    "thread_id": "1"
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-15)  }
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-16)}
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-17)
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-18)my_workflow.invoke(3, config) # 0 (previous was None)
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-19)my_workflow.invoke(1, config) # 6 (previous was 3 * 2 from the previous invocation)

```


####  `value: R` `instance-attribute` [¶](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint.final.value "Permanent link")

Value to return. A value will always be returned even if it is None.

####  `save: S` `instance-attribute` [¶](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint.final.save "Permanent link")

The value for the state for the next checkpoint. 

A value will always be saved even if it is None.

###  `__init__(checkpointer: Optional[BaseCheckpointSaver] = None, store: Optional[BaseStore] = None, config_schema: Optional[type[Any]] = None) -> None` [¶](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint.__init__ "Permanent link")

Initialize the entrypoint decorator.

###  `__call__(func: Callable[..., Any]) -> Pregel` [¶](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint.__call__ "Permanent link")

Convert a function into a Pregel graph.

Parameters:

  * **`func`**(`Callable[..., Any]`) – 

The function to convert. Support both sync and async functions.




Returns:

  * `Pregel` – 

A Pregel graph.




##  `task(__func_or_none__: Optional[Union[Callable[P, T], Callable[P, Awaitable[T]]]] = None, *, name: Optional[str] = None, retry: Optional[RetryPolicy] = None) -> Union[Callable[[Callable[P, T]], Callable[P, SyncAsyncFuture[T]]], Callable[P, SyncAsyncFuture[T]]]` [¶](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.task "Permanent link")

Define a LangGraph task using the `task` decorator.

Beta

The Functional API is currently in beta and is subject to change.

Requires python 3.11 or higher for async functions

The `task` decorator supports both sync and async functions. To use async functions, ensure that you are using Python 3.11 or higher.

Tasks can only be called from within an [entrypoint](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint) or from within a StateGraph. A task can be called like a regular function with the following differences:

  * When a checkpointer is enabled, the function inputs and outputs must be serializable.
  * The decorated function can only be called from within an entrypoint or StateGraph.
  * Calling the function produces a future. This makes it easy to parallelize tasks.



Parameters:

  * **`retry`**(`Optional[RetryPolicy]` , default: `None` ) – 

An optional retry policy to use for the task in case of a failure.




Returns:

  * `Union[Callable[[Callable[P, T]], Callable[P, SyncAsyncFuture[T]]], Callable[P, SyncAsyncFuture[T]]]` – 

A callable function when used as a decorator.


Sync Task

```
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-1)fromlanggraph.funcimport entrypoint, task
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-2)
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-3)@task
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-4)defadd_one(a: int) -> int:
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-5)  return a + 1
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-6)
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-7)@entrypoint()
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-8)defadd_one(numbers: list[int]) -> list[int]:
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-9)  futures = [add_one(n) for n in numbers]
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-10)  results = [f.result() for f in futures]
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-11)  return results
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-12)
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-13)# Call the entrypoint
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-14)add_one.invoke([1, 2, 3]) # Returns [2, 3, 4]

```


Async Task

```
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-1)importasyncio
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-2)fromlanggraph.funcimport entrypoint, task
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-3)
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-4)@task
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-5)async defadd_one(a: int) -> int:
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-6)  return a + 1
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-7)
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-8)@entrypoint()
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-9)async defadd_one(numbers: list[int]) -> list[int]:
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-10)  futures = [add_one(n) for n in numbers]
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-11)  return asyncio.gather(*futures)
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-12)
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-13)# Call the entrypoint
[](https://langchain-ai.github.io/langgraph/reference/func/#__codelineno-0-14)await add_one.ainvoke([1, 2, 3]) # Returns [2, 3, 4]

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Config  ](https://langchain-ai.github.io/langgraph/reference/config/) [ Next  Server API  ](https://langchain-ai.github.io/langgraph/cloud/reference/api/api_ref/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/reference/func/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
