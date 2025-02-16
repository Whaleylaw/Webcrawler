---
url: https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#how-to-stream-from-subgraphs)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to stream from subgraphs 

[ ](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/?q= "Share")

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
          * [ Controllability  ](https://langchain-ai.github.io/langgraph/how-tos#controllability)
          * [ Persistence  ](https://langchain-ai.github.io/langgraph/how-tos#persistence)
          * [ Memory  ](https://langchain-ai.github.io/langgraph/how-tos#memory)
          * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraph/how-tos#human-in-the-loop)
          * Streaming  Streaming 
            * [ Streaming  ](https://langchain-ai.github.io/langgraph/how-tos#streaming)
            * [ How to stream  ](https://langchain-ai.github.io/langgraph/how-tos/streaming/)
            * [ How to stream LLM tokens from your graph  ](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/)
            * [ How to stream LLM tokens from specific nodes  ](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/)
            * [ How to stream data from within a tool  ](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/)
            * How to stream from subgraphs  [ How to stream from subgraphs  ](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#setup)
              * [ Example  ](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#example)
            * [ How to disable streaming for models that don't support it  ](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#setup)
  * [ Example  ](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#example)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Streaming  ](https://langchain-ai.github.io/langgraph/how-tos#streaming)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/streaming-subgraphs.ipynb "Edit this page")

# How to stream from subgraphs[¶](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#how-to-stream-from-subgraphs "Permanent link")

Prerequisites

This guide assumes familiarity with the following:

  * [Subgraphs](https://langchain-ai.github.io/langgraph/concepts/low_level/#subgraphs)
  * [Chat Models](https://python.langchain.com/docs/concepts/chat_models/)



If you have created a graph with [subgraphs](https://langchain-ai.github.io/langgraph/how-tos/subgraph), you may wish to stream outputs from those subgraphs. To do so, you can specify `subgraphs=True` in parent graph's `.stream()` method:

```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-0-1)for chunk in parent_graph.stream(
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-0-2)  {"foo": "foo"},
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-0-3)  subgraphs=True
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-0-4)):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-0-5)  print(chunk)

```


## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#setup "Permanent link")

First let's install the required packages

```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-1-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-1-2)%pip install -U langgraph

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Example[¶](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#example "Permanent link")

Let's define a simple example:

```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-2-1)fromlanggraph.graphimport START, StateGraph
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-2-2)fromtypingimport TypedDict
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-2-3)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-2-4)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-2-5)# Define subgraph
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-2-6)classSubgraphState(TypedDict):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-2-7)  foo: str # note that this key is shared with the parent graph state
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-2-8)  bar: str
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-2-9)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-2-10)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-2-11)defsubgraph_node_1(state: SubgraphState):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-2-12)  return {"bar": "bar"}
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-2-13)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-2-14)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-2-15)defsubgraph_node_2(state: SubgraphState):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-2-16)  return {"foo": state["foo"] + state["bar"]}
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-2-17)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-2-18)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-2-19)subgraph_builder = StateGraph(SubgraphState)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-2-20)subgraph_builder.add_node(subgraph_node_1)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-2-21)subgraph_builder.add_node(subgraph_node_2)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-2-22)subgraph_builder.add_edge(START, "subgraph_node_1")
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-2-23)subgraph_builder.add_edge("subgraph_node_1", "subgraph_node_2")
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-2-24)subgraph = subgraph_builder.compile()
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-2-25)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-2-26)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-2-27)# Define parent graph
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-2-28)classParentState(TypedDict):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-2-29)  foo: str
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-2-30)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-2-31)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-2-32)defnode_1(state: ParentState):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-2-33)  return {"foo": "hi! " + state["foo"]}
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-2-34)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-2-35)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-2-36)builder = StateGraph(ParentState)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-2-37)builder.add_node("node_1", node_1)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-2-38)builder.add_node("node_2", subgraph)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-2-39)builder.add_edge(START, "node_1")
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-2-40)builder.add_edge("node_1", "node_2")
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-2-41)graph = builder.compile()

```


API Reference: [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph)

Let's now stream the outputs from the graph:

```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-3-1)for chunk in graph.stream({"foo": "foo"}, stream_mode="updates"):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-3-2)  print(chunk)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-4-1){'node_1': {'foo': 'hi! foo'}}
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-4-2){'node_2': {'foo': 'hi! foobar'}}

```


You can see that we're only emitting the updates from the parent graph nodes (`node_1` and `node_2`). To emit the updates from the _subgraph_ nodes you can specify `subgraphs=True`: 

```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-5-1)for chunk in graph.stream(
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-5-2)  {"foo": "foo"},
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-5-3)  stream_mode="updates",
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-5-4)  subgraphs=True,
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-5-5)):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-5-6)  print(chunk)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-6-1)((), {'node_1': {'foo': 'hi! foo'}})
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-6-2)(('node_2:b692b345-cfb3-b709-628c-f0ba9608f72e',), {'subgraph_node_1': {'bar': 'bar'}})
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-6-3)(('node_2:b692b345-cfb3-b709-628c-f0ba9608f72e',), {'subgraph_node_2': {'foo': 'hi! foobar'}})
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__codelineno-6-4)((), {'node_2': {'foo': 'hi! foobar'}})

```


Voila! The streamed outputs now contain updates from both the parent graph and the subgraph. **Note** that we are receiving not just the node updates, but we also the namespaces which tell us what graph (or subgraph) we are streaming from.  Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to stream data from within a tool  ](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/) [ Next  How to disable streaming for models that don't support it  ](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
