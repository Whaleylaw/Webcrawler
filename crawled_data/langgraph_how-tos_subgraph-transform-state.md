---
url: https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#how-to-transform-inputs-and-outputs-of-a-subgraph)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to transform inputs and outputs of a subgraph 

[ ](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/?q= "Share")

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

How-to Guides 
        * LangGraph  LangGraph 
          * [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
          * [ Graph API Basics  ](https://langchain-ai.github.io/langgraph/how-tos#graph-api-basics)
          * [ Controllability  ](https://langchain-ai.github.io/langgraph/how-tos#controllability)
          * [ Persistence  ](https://langchain-ai.github.io/langgraph/how-tos#persistence)
          * [ Memory  ](https://langchain-ai.github.io/langgraph/how-tos#memory)
          * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraph/how-tos#human-in-the-loop)
          * [ Streaming  ](https://langchain-ai.github.io/langgraph/how-tos#streaming)
          * [ Tool calling  ](https://langchain-ai.github.io/langgraph/how-tos#tool-calling)
          * Subgraphs  Subgraphs 
            * [ Subgraphs  ](https://langchain-ai.github.io/langgraph/how-tos#subgraphs)
            * [ How to use subgraphs  ](https://langchain-ai.github.io/langgraph/how-tos/subgraph/)
            * [ How to view and update state in subgraphs  ](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/)
            * How to transform inputs and outputs of a subgraph  [ How to transform inputs and outputs of a subgraph  ](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#setup)
              * [ Define graph and subgraphs  ](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#define-graph-and-subgraphs)
                * [ Define grandchild  ](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#define-grandchild)
                * [ Define child  ](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#define-child)
                * [ Define parent  ](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#define-parent)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#setup)
  * [ Define graph and subgraphs  ](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#define-graph-and-subgraphs)
    * [ Define grandchild  ](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#define-grandchild)
    * [ Define child  ](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#define-child)
    * [ Define parent  ](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#define-parent)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Subgraphs  ](https://langchain-ai.github.io/langgraph/how-tos#subgraphs)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/subgraph-transform-state.ipynb "Edit this page")

# How to transform inputs and outputs of a subgraph[¶](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#how-to-transform-inputs-and-outputs-of-a-subgraph "Permanent link")

It's possible that your subgraph state is completely independent from the parent graph state, i.e. there are no overlapping channels (keys) between the two. For example, you might have a supervisor agent that needs to produce a report with a help of multiple ReAct agents. ReAct agent subgraphs might keep track of a list of messages whereas the supervisor only needs user input and final report in its state, and doesn't need to keep track of messages.

In such cases you need to transform the inputs to the subgraph before calling it and then transform its outputs before returning. This guide shows how to do that.

## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#setup "Permanent link")

First, let's install the required packages

```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-0-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-0-2)%pip install -U langgraph

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Define graph and subgraphs[¶](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#define-graph-and-subgraphs "Permanent link")

Let's define 3 graphs: - a parent graph - a child subgraph that will be called by the parent graph - a grandchild subgraph that will be called by the child graph

### Define grandchild[¶](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#define-grandchild "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-1-1)fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-1-2)fromlanggraph.graph.stateimport StateGraph, START, END
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-1-5)classGrandChildState(TypedDict):
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-1-6)  my_grandchild_key: str
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-1-7)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-1-8)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-1-9)defgrandchild_1(state: GrandChildState) -> GrandChildState:
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-1-10)  # NOTE: child or parent keys will not be accessible here
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-1-11)  return {"my_grandchild_key": state["my_grandchild_key"] + ", how are you"}
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-1-12)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-1-13)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-1-14)grandchild = StateGraph(GrandChildState)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-1-15)grandchild.add_node("grandchild_1", grandchild_1)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-1-16)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-1-17)grandchild.add_edge(START, "grandchild_1")
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-1-18)grandchild.add_edge("grandchild_1", END)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-1-19)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-1-20)grandchild_graph = grandchild.compile()

```


API Reference: [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph)

```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-2-1)grandchild_graph.invoke({"my_grandchild_key": "hi Bob"})

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-3-1){'my_grandchild_key': 'hi Bob, how are you'}

```


### Define child[¶](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#define-child "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-4-1)classChildState(TypedDict):
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-4-2)  my_child_key: str
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-4-3)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-4-4)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-4-5)defcall_grandchild_graph(state: ChildState) -> ChildState:
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-4-6)  # NOTE: parent or grandchild keys won't be accessible here
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-4-7)  # we're transforming the state from the child state channels (`my_child_key`)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-4-8)  # to the child state channels (`my_grandchild_key`)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-4-9)  grandchild_graph_input = {"my_grandchild_key": state["my_child_key"]}
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-4-10)  # we're transforming the state from the grandchild state channels (`my_grandchild_key`)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-4-11)  # back to the child state channels (`my_child_key`)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-4-12)  grandchild_graph_output = grandchild_graph.invoke(grandchild_graph_input)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-4-13)  return {"my_child_key": grandchild_graph_output["my_grandchild_key"] + " today?"}
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-4-14)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-4-15)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-4-16)child = StateGraph(ChildState)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-4-17)# NOTE: we're passing a function here instead of just compiled graph (`child_graph`)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-4-18)child.add_node("child_1", call_grandchild_graph)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-4-19)child.add_edge(START, "child_1")
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-4-20)child.add_edge("child_1", END)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-4-21)child_graph = child.compile()

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-5-1)child_graph.invoke({"my_child_key": "hi Bob"})

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-6-1){'my_child_key': 'hi Bob, how are you today?'}

```


Note

We're wrapping the `grandchild_graph` invocation in a separate function (`call_grandchild_graph`) that transforms the input state before calling the grandchild graph and then transforms the output of grandchild graph back to child graph state. If you just pass `grandchild_graph` directly to `.add_node` without the transformations, LangGraph will raise an error as there are no shared state channels (keys) between child and grandchild states. 

Note that child and grandchild subgraphs have their own, **independent** state that is not shared with the parent graph.

### Define parent[¶](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#define-parent "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-7-1)classParentState(TypedDict):
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-7-2)  my_key: str
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-7-3)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-7-4)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-7-5)defparent_1(state: ParentState) -> ParentState:
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-7-6)  # NOTE: child or grandchild keys won't be accessible here
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-7-7)  return {"my_key": "hi " + state["my_key"]}
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-7-8)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-7-9)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-7-10)defparent_2(state: ParentState) -> ParentState:
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-7-11)  return {"my_key": state["my_key"] + " bye!"}
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-7-12)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-7-13)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-7-14)defcall_child_graph(state: ParentState) -> ParentState:
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-7-15)  # we're transforming the state from the parent state channels (`my_key`)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-7-16)  # to the child state channels (`my_child_key`)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-7-17)  child_graph_input = {"my_child_key": state["my_key"]}
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-7-18)  # we're transforming the state from the child state channels (`my_child_key`)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-7-19)  # back to the parent state channels (`my_key`)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-7-20)  child_graph_output = child_graph.invoke(child_graph_input)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-7-21)  return {"my_key": child_graph_output["my_child_key"]}
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-7-22)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-7-23)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-7-24)parent = StateGraph(ParentState)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-7-25)parent.add_node("parent_1", parent_1)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-7-26)# NOTE: we're passing a function here instead of just a compiled graph (`<code>child_graph</code>`)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-7-27)parent.add_node("child", call_child_graph)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-7-28)parent.add_node("parent_2", parent_2)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-7-29)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-7-30)parent.add_edge(START, "parent_1")
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-7-31)parent.add_edge("parent_1", "child")
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-7-32)parent.add_edge("child", "parent_2")
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-7-33)parent.add_edge("parent_2", END)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-7-34)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-7-35)parent_graph = parent.compile()

```


Note

We're wrapping the `child_graph` invocation in a separate function (`call_child_graph`) that transforms the input state before calling the child graph and then transforms the output of the child graph back to parent graph state. If you just pass `child_graph` directly to `.add_node` without the transformations, LangGraph will raise an error as there are no shared state channels (keys) between parent and child states. 

Let's run the parent graph and make sure it correctly calls both the child and grandchild subgraphs:

```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-8-1)parent_graph.invoke({"my_key": "Bob"})

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__codelineno-9-1){'my_key': 'hi Bob, how are you today? bye!'}

```


Perfect! The parent graph correctly calls both the child and grandchild subgraphs (which we know since the ", how are you" and "today?" are added to our original "my_key" state value).

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to view and update state in subgraphs  ](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/) [ Next  How to implement handoffs between agents  ](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
