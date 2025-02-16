---
url: https://langchain-ai.github.io/langgraph/concepts/breakpoints
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#breakpoints)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Breakpoints 

[ ](https://langchain-ai.github.io/langgraph/concepts/breakpoints/?q= "Share")

Type to start searching

[ GitHub  ](https://github.com/langchain-ai/langgraph "Go to repository")

  * [ Home ](https://langchain-ai.github.io/langgraph/)
  * [ API reference ](https://langchain-ai.github.io/langgraph/reference/graphs/)



[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

[ GitHub  ](https://github.com/langchain-ai/langgraph "Go to repository")

  * [ Home  ](https://langchain-ai.github.io/langgraph/)
  * [ API reference  ](https://langchain-ai.github.io/langgraph/reference/graphs/)



Table of contents 

  * [ Requirements  ](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#requirements)
  * [ Setting breakpoints  ](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#setting-breakpoints)
    * [ Static breakpoints  ](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#static-breakpoints)
    * [ NodeInterrupt exception  ](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#nodeinterrupt-exception)
  * [ Additional Resources 📚  ](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#additional-resources)



[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/concepts/breakpoints.md "Edit this page")

# Breakpoints[¶](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#breakpoints "Permanent link")

Breakpoints pause graph execution at specific points and enable stepping through execution step by step. Breakpoints are powered by LangGraph's [**persistence layer**](https://langchain-ai.github.io/langgraph/concepts/persistence/), which saves the state after each graph step. Breakpoints can also be used to enable [**human-in-the-loop**](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/) workflows, though we recommend using the `interrupt`[ function](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#interrupt) for this purpose.

## Requirements[¶](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#requirements "Permanent link")

To use breakpoints, you will need to:

  1. [**Specify a checkpointer**](https://langchain-ai.github.io/langgraph/concepts/persistence/#checkpoints) to save the graph state after each step.
  2. [**Set breakpoints**](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#setting-breakpoints) to specify where execution should pause.
  3. **Run the graph** with a [**thread ID**](https://langchain-ai.github.io/langgraph/concepts/persistence/#threads) to pause execution at the breakpoint.
  4. **Resume execution** using `invoke`/`ainvoke`/`stream`/`astream` (see [**The`Command` primitive**](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#the-command-primitive)).



## Setting breakpoints[¶](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#setting-breakpoints "Permanent link")

There are two places where you can set breakpoints:

  1. **Before** or **after** a node executes by setting breakpoints at **compile time** or **run time**. We call these [**static breakpoints**](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#static-breakpoints).
  2. **Inside** a node using the `NodeInterrupt`[ exception](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#nodeinterrupt-exception).



### Static breakpoints[¶](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#static-breakpoints "Permanent link")

Static breakpoints are triggered either **before** or **after** a node executes. You can set static breakpoints by specifying `interrupt_before` and `interrupt_after` at **"compile" time** or **run time**.

[Compile time](#__tabbed_1_1)[Run time](#__tabbed_1_2)

```
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-0-1)graph = graph_builder.compile(
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-0-2)  interrupt_before=["node_a"], 
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-0-3)  interrupt_after=["node_b", "node_c"],
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-0-4)  checkpointer=..., # Specify a checkpointer
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-0-5))
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-0-6)
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-0-7)thread_config = {
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-0-8)  "configurable": {
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-0-9)    "thread_id": "some_thread"
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-0-10)  }
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-0-11)}
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-0-12)
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-0-13)# Run the graph until the breakpoint
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-0-14)graph.invoke(inputs, config=thread_config)
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-0-15)
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-0-16)# Optionally update the graph state based on user input
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-0-17)graph.update_state(update, config=thread_config)
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-0-18)
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-0-19)# Resume the graph
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-0-20)graph.invoke(None, config=thread_config)

```


```
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-1-1)graph.invoke(
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-1-2)  inputs, 
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-1-3)  config={"configurable": {"thread_id": "some_thread"}}, 
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-1-4)  interrupt_before=["node_a"], 
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-1-5)  interrupt_after=["node_b", "node_c"]
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-1-6))
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-1-7)
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-1-8)thread_config = {
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-1-9)  "configurable": {
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-1-10)    "thread_id": "some_thread"
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-1-11)  }
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-1-12)}
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-1-13)
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-1-14)# Run the graph until the breakpoint
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-1-15)graph.invoke(inputs, config=thread_config)
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-1-16)
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-1-17)# Optionally update the graph state based on user input
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-1-18)graph.update_state(update, config=thread_config)
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-1-19)
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-1-20)# Resume the graph
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-1-21)graph.invoke(None, config=thread_config)

```


Note

You cannot set static breakpoints at runtime for **sub-graphs**. If you have a sub-graph, you must set the breakpoints at compilation time.

Static breakpoints can be especially useful for debugging if you want to step through the graph execution one node at a time or if you want to pause the graph execution at specific nodes.

### `NodeInterrupt` exception[¶](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#nodeinterrupt-exception "Permanent link")

We recommend that you [**use the`interrupt` function instead**](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#the-interrupt-function) of the `NodeInterrupt` exception if you're trying to implement [human-in-the-loop](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/) workflows. The `interrupt` function is easier to use and more flexible.

`NodeInterrupt` exception

The developer can define some _condition_ that must be met for a breakpoint to be triggered. This concept of _dynamic breakpoints_ is useful when the developer wants to halt the graph under _a particular condition_. This uses a `NodeInterrupt`, which is a special type of exception that can be raised from within a node based upon some condition. As an example, we can define a dynamic breakpoint that triggers when the `input` is longer than 5 characters.

```
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-2-1)defmy_node(state: State) -> State:
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-2-2)  if len(state['input']) > 5:
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-2-3)    raise NodeInterrupt(f"Received input that is longer than 5 characters: {state['input']}")
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-2-4)
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-2-5)  return state

```


Let's assume we run the graph with an input that triggers the dynamic breakpoint and then attempt to resume the graph execution simply by passing in `None` for the input.

```
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-3-1)# Attempt to continue the graph execution with no change to state after we hit the dynamic breakpoint 
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-3-2)for event in graph.stream(None, thread_config, stream_mode="values"):
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-3-3)  print(event)

```


The graph will _interrupt_ again because this node will be _re-run_ with the same graph state. We need to change the graph state such that the condition that triggers the dynamic breakpoint is no longer met. So, we can simply edit the graph state to an input that meets the condition of our dynamic breakpoint (< 5 characters) and re-run the node.

```
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-4-1)# Update the state to pass the dynamic breakpoint
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-4-2)graph.update_state(config=thread_config, values={"input": "foo"})
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-4-3)for event in graph.stream(None, thread_config, stream_mode="values"):
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-4-4)  print(event)

```


Alternatively, what if we want to keep our current input and skip the node (`my_node`) that performs the check? To do this, we can simply perform the graph update with `as_node="my_node"` and pass in `None` for the values. This will make no update the graph state, but run the update as `my_node`, effectively skipping the node and bypassing the dynamic breakpoint.

```
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-5-1)# This update will skip the node `my_node` altogether
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-5-2)graph.update_state(config=thread_config, values=None, as_node="my_node")
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-5-3)for event in graph.stream(None, thread_config, stream_mode="values"):
[](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__codelineno-5-4)  print(event)

```


## Additional Resources 📚[¶](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#additional-resources "Permanent link")

  * [**Conceptual Guide: Persistence**](https://langchain-ai.github.io/langgraph/concepts/persistence/): Read the persistence guide for more context about persistence.
  * [**Conceptual Guide: Human-in-the-loop**](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/): Read the human-in-the-loop guide for more context on integrating human feedback into LangGraph applications using breakpoints.
  * [**How to View and Update Past Graph State**](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/): Step-by-step instructions for working with graph state that demonstrate the **replay** and **fork** actions.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top 

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/concepts/breakpoints/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
