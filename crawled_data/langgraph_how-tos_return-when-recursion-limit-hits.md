---
url: https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#how-to-return-state-before-hitting-recursion-limit)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to return state before hitting recursion limit 

[ ](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/?q= "Share")

Initializing search 

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

How-to Guides 
        * LangGraph  LangGraph 
          * [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
          * [ Graph API Basics  ](https://langchain-ai.github.io/langgraph/how-tos#graph-api-basics)
          * Controllability  Controllability 
            * [ Controllability  ](https://langchain-ai.github.io/langgraph/how-tos#controllability)
            * [ How to create map-reduce branches for parallel execution  ](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/)
            * [ How to combine control flow and state updates with Command  ](https://langchain-ai.github.io/langgraph/how-tos/command/)
            * [ How to add runtime configuration to your graph  ](https://langchain-ai.github.io/langgraph/how-tos/configuration/)
            * [ How to add node retry policies  ](https://langchain-ai.github.io/langgraph/how-tos/node-retries/)
            * How to return state before hitting recursion limit  [ How to return state before hitting recursion limit  ](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#setup)
              * [ Without returning state  ](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#without-returning-state)
              * [ With returning state  ](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#with-returning-state)
          * [ Persistence  ](https://langchain-ai.github.io/langgraph/how-tos#persistence)
          * [ Memory  ](https://langchain-ai.github.io/langgraph/how-tos#memory)
          * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraph/how-tos#human-in-the-loop)
          * [ Streaming  ](https://langchain-ai.github.io/langgraph/how-tos#streaming)
          * [ Tool calling  ](https://langchain-ai.github.io/langgraph/how-tos#tool-calling)
          * [ Subgraphs  ](https://langchain-ai.github.io/langgraph/how-tos#subgraphs)
          * [ Multi-agent  ](https://langchain-ai.github.io/langgraph/how-tos#multi-agent)
          * [ State Management  ](https://langchain-ai.github.io/langgraph/how-tos#state-management)
          * [ Other  ](https://langchain-ai.github.io/langgraph/how-tos#other)
          * [ Prebuilt ReAct Agent  ](https://langchain-ai.github.io/langgraph/how-tos#prebuilt-react-agent)
        * [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph-platform)
      * [ Concepts  ](https://langchain-ai.github.io/langgraph/concepts/)
      * [ Tutorials  ](https://langchain-ai.github.io/langgraph/tutorials/)
    * Resources  Resources 
      * [ Prebuilt Agents  ](https://langchain-ai.github.io/langgraph/prebuilt/)
      * [ Adopters  ](https://langchain-ai.github.io/langgraph/adopters/)
      * [ FAQ  ](https://langchain-ai.github.io/langgraph/concepts/faq/)
      * [ Troubleshooting  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraph/reference/graphs/)



Table of contents 

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#setup)
  * [ Without returning state  ](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#without-returning-state)
  * [ With returning state  ](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#with-returning-state)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Controllability  ](https://langchain-ai.github.io/langgraph/how-tos#controllability)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/return-when-recursion-limit-hits.ipynb "Edit this page")

# How to return state before hitting recursion limit[¶](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#how-to-return-state-before-hitting-recursion-limit "Permanent link")

Prerequisites

This guide assumes familiarity with the following: 

  * [ Graphs ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#graphs)
  * [ Recursion Limit ](https://langchain-ai.github.io/langgraph/concepts/low_level/#recursion-limit)
  * [ Nodes ](https://langchain-ai.github.io/langgraph/concepts/low_level/#nodes)



[Setting the graph recursion limit](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/) can help you control how long your graph will stay running, but if the recursion limit is hit your graph returns an error - which may not be ideal for all use cases. Instead you may wish to return the value of the state _just before_ the recursion limit is hit. This how-to will show you how to do this.

## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#setup "Permanent link")

First, let's installed the required packages:

```
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-0-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-0-2)%pip install -U langgraph

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Without returning state[¶](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#without-returning-state "Permanent link")

We are going to define a dummy graph in this example that will always hit the recursion limit. First, we will implement it without returning the state and show that it hits the recursion limit. This graph is based on the ReAct architecture, but instead of actually making decisions and taking actions it just loops forever.

```
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-1-1)fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-1-2)fromlanggraph.graphimport StateGraph
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-1-3)fromlanggraph.graphimport START, END
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-1-5)
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-1-6)classState(TypedDict):
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-1-7)  value: str
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-1-8)  action_result: str
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-1-10)
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-1-11)defrouter(state: State):
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-1-12)  if state["value"] == "end":
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-1-13)    return END
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-1-14)  else:
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-1-15)    return "action"
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-1-16)
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-1-17)
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-1-18)defdecision_node(state):
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-1-19)  return {"value": "keep going!"}
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-1-20)
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-1-21)
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-1-22)defaction_node(state: State):
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-1-23)  # Do your action here ...
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-1-24)  return {"action_result": "what a great result!"}
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-1-25)
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-1-26)
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-1-27)workflow = StateGraph(State)
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-1-28)workflow.add_node("decision", decision_node)
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-1-29)workflow.add_node("action", action_node)
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-1-30)workflow.add_edge(START, "decision")
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-1-31)workflow.add_conditional_edges("decision", router, ["action", END])
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-1-32)workflow.add_edge("action", "decision")
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-1-33)app = workflow.compile()

```


API Reference: [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END)

```
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-2-1)fromIPython.displayimport Image, display
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-2-2)
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-2-3)display(Image(app.get_graph().draw_mermaid_png()))

```


![]()

Let's verify that our graph will always hit the recursion limit:

```
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-3-1)fromlanggraph.errorsimport GraphRecursionError
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-3-2)
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-3-3)try:
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-3-4)  app.invoke({"value": "hi!"})
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-3-5)except GraphRecursionError:
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-3-6)  print("Recursion Error")

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-4-1)Recursion Error

```


## With returning state[¶](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#with-returning-state "Permanent link")

To avoid hitting the recursion limit, we can introduce a new key to our state called `remaining_steps`. It will keep track of number of steps until reaching the recursion limit. We can then check the value of `remaining_steps` to determine whether we should terminate the graph execution and return the state to the user without causing the `RecursionError`.

To do so, we will use a special `RemainingSteps` annotation. Under the hood, it creates a special `ManagedValue` channel -- a state channel that will exist for the duration of our graph run and no longer.

Since our `action` node is going to always induce at least 2 extra steps to our graph (since the `action` node ALWAYS calls the `decision` node afterwards), we will use this channel to check if we are within 2 steps of the limit.

Now, when we run our graph we should receive no errors and instead get the last value of the state before the recursion limit was hit.

```
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-5-1)fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-5-2)fromlanggraph.graphimport StateGraph
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-5-3)fromtypingimport Annotated
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-5-4)
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-5-5)fromlanggraph.managed.is_last_stepimport RemainingSteps
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-5-6)
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-5-7)
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-5-8)classState(TypedDict):
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-5-9)  value: str
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-5-10)  action_result: str
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-5-11)  remaining_steps: RemainingSteps
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-5-12)
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-5-13)
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-5-14)defrouter(state: State):
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-5-15)  # Force the agent to end
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-5-16)  if state["remaining_steps"] <= 2:
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-5-17)    return END
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-5-18)  if state["value"] == "end":
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-5-19)    return END
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-5-20)  else:
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-5-21)    return "action"
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-5-22)
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-5-23)
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-5-24)defdecision_node(state):
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-5-25)  return {"value": "keep going!"}
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-5-26)
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-5-27)
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-5-28)defaction_node(state: State):
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-5-29)  # Do your action here ...
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-5-30)  return {"action_result": "what a great result!"}
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-5-31)
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-5-32)
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-5-33)workflow = StateGraph(State)
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-5-34)workflow.add_node("decision", decision_node)
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-5-35)workflow.add_node("action", action_node)
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-5-36)workflow.add_edge(START, "decision")
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-5-37)workflow.add_conditional_edges("decision", router, ["action", END])
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-5-38)workflow.add_edge("action", "decision")
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-5-39)app = workflow.compile()

```


API Reference: [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph)

```
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-6-1)app.invoke({"value": "hi!"})

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__codelineno-7-1){'value': 'keep going!', 'action_result': 'what a great result!'}

```


Perfect! Our code ran with no error, just as we expected!

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to add node retry policies  ](https://langchain-ai.github.io/langgraph/how-tos/node-retries/) [ Next  How to add thread-level persistence to your graph  ](https://langchain-ai.github.io/langgraph/how-tos/persistence/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
