---
url: https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#how-to-add-thread-level-persistence-to-a-subgraph)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to add thread-level persistence to a subgraph 

[ ](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/?q= "Share")

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
          * Persistence  Persistence 
            * [ Persistence  ](https://langchain-ai.github.io/langgraph/how-tos#persistence)
            * [ How to add thread-level persistence to your graph  ](https://langchain-ai.github.io/langgraph/how-tos/persistence/)
            * How to add thread-level persistence to a subgraph  [ How to add thread-level persistence to a subgraph  ](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#setup)
              * [ Define the graph with persistence  ](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#define-the-graph-with-persistence)
              * [ Verify persistence works  ](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#verify-persistence-works)
            * [ How to add cross-thread persistence to your graph  ](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/)
            * [ How to use Postgres checkpointer for persistence  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/)
            * [ How to use MongoDB checkpointer for persistence  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_mongodb/)
            * [ How to create a custom checkpointer using Redis  ](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/)
            * [ How to add thread-level persistence (functional API)  ](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/)
            * [ How to add cross-thread persistence (functional API)  ](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#setup)
  * [ Define the graph with persistence  ](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#define-the-graph-with-persistence)
  * [ Verify persistence works  ](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#verify-persistence-works)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Persistence  ](https://langchain-ai.github.io/langgraph/how-tos#persistence)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/subgraph-persistence.ipynb "Edit this page")

# How to add thread-level persistence to a subgraph[¶](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#how-to-add-thread-level-persistence-to-a-subgraph "Permanent link")

Prerequisites

This guide assumes familiarity with the following: 

  * [ Subgraphs ](https://langchain-ai.github.io/langgraph/concepts/low_level/#subgraphs)
  * [ Persistence ](https://langchain-ai.github.io/langgraph/concepts/persistence/)



This guide shows how you can add [thread-level](https://langchain-ai.github.io/langgraph/how-tos/persistence/) persistence to graphs that use [subgraphs](https://langchain-ai.github.io/langgraph/how-tos/subgraph/).

## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#setup "Permanent link")

First, let's install the required packages

```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-0-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-0-2)%pip install -U langgraph

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Define the graph with persistence[¶](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#define-the-graph-with-persistence "Permanent link")

To add persistence to a graph with subgraphs, all you need to do is pass a [checkpointer](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver) when **compiling the parent graph**. LangGraph will automatically propagate the checkpointer to the child subgraphs.

Note

You **shouldn't provide** a checkpointer when compiling a subgraph. Instead, you must define a **single** checkpointer that you pass to `parent_graph.compile()`, and LangGraph will automatically propagate the checkpointer to the child subgraphs. If you pass the checkpointer to the `subgraph.compile()`, it will simply be ignored. This also applies when you [add a node function that invokes the subgraph](https://langchain-ai.github.io/langgraph/how-tos/subgraph#add-a-node-function-that-invokes-the-subgraph).

Let's define a simple graph with a single subgraph node to show how to do this.

```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-1-1)fromlanggraph.graphimport START, StateGraph
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-1-2)fromlanggraph.checkpoint.memoryimport MemorySaver
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-1-3)fromtypingimport TypedDict
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-1-5)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-1-6)# subgraph
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-1-7)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-1-8)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-1-9)classSubgraphState(TypedDict):
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-1-10)  foo: str # note that this key is shared with the parent graph state
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-1-11)  bar: str
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-1-12)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-1-13)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-1-14)defsubgraph_node_1(state: SubgraphState):
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-1-15)  return {"bar": "bar"}
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-1-16)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-1-17)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-1-18)defsubgraph_node_2(state: SubgraphState):
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-1-19)  # note that this node is using a state key ('bar') that is only available in the subgraph
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-1-20)  # and is sending update on the shared state key ('foo')
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-1-21)  return {"foo": state["foo"] + state["bar"]}
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-1-22)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-1-23)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-1-24)subgraph_builder = StateGraph(SubgraphState)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-1-25)subgraph_builder.add_node(subgraph_node_1)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-1-26)subgraph_builder.add_node(subgraph_node_2)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-1-27)subgraph_builder.add_edge(START, "subgraph_node_1")
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-1-28)subgraph_builder.add_edge("subgraph_node_1", "subgraph_node_2")
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-1-29)subgraph = subgraph_builder.compile()
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-1-30)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-1-31)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-1-32)# parent graph
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-1-33)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-1-34)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-1-35)classState(TypedDict):
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-1-36)  foo: str
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-1-37)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-1-38)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-1-39)defnode_1(state: State):
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-1-40)  return {"foo": "hi! " + state["foo"]}
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-1-41)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-1-42)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-1-43)builder = StateGraph(State)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-1-44)builder.add_node("node_1", node_1)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-1-45)# note that we're adding the compiled subgraph as a node to the parent graph
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-1-46)builder.add_node("node_2", subgraph)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-1-47)builder.add_edge(START, "node_1")
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-1-48)builder.add_edge("node_1", "node_2")

```


API Reference: [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [MemorySaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.MemorySaver)

```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-2-1)<langgraph.graph.state.StateGraph at 0x106d2fa10>

```


We can now compile the graph with an in-memory checkpointer (`MemorySaver`).

```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-3-1)checkpointer = MemorySaver()
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-3-2)# You must only pass checkpointer when compiling the parent graph.
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-3-3)# LangGraph will automatically propagate the checkpointer to the child subgraphs.
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-3-4)graph = builder.compile(checkpointer=checkpointer)

```


## Verify persistence works[¶](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#verify-persistence-works "Permanent link")

Let's now run the graph and inspect the persisted state for both the parent graph and the subgraph to verify that persistence works. We should expect to see the final execution results for both the parent and subgraph in `state.values`.

```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-4-1)config = {"configurable": {"thread_id": "1"}}

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-5-1)for _, chunk in graph.stream({"foo": "foo"}, config, subgraphs=True):
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-5-2)  print(chunk)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-6-1){'node_1': {'foo': 'hi! foo'}}
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-6-2){'subgraph_node_1': {'bar': 'bar'}}
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-6-3){'subgraph_node_2': {'foo': 'hi! foobar'}}
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-6-4){'node_2': {'foo': 'hi! foobar'}}

```


We can now view the parent graph state by calling `graph.get_state()` with the same config that we used to invoke the graph. 

```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-7-1)graph.get_state(config).values

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-8-1){'foo': 'hi! foobar'}

```


To view the subgraph state, we need to do two things:

  1. Find the most recent config value for the subgraph
  2. Use `graph.get_state()` to retrieve that value for the most recent subgraph config.



To find the correct config, we can examine the state history from the parent graph and find the state snapshot before we return results from `node_2` (the node with subgraph):

```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-9-1)state_with_subgraph = [
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-9-2)  s for s in graph.get_state_history(config) if s.next == ("node_2",)
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-9-3)][0]

```


The state snapshot will include the list of `tasks` to be executed next. When using subgraphs, the `tasks` will contain the config that we can use to retrieve the subgraph state:

```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-10-1)subgraph_config = state_with_subgraph.tasks[0].state
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-10-2)subgraph_config

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-11-1){'configurable': {'thread_id': '1',
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-11-2) 'checkpoint_ns': 'node_2:6ef111a6-f290-7376-0dfc-a4152307bc5b'}}

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-12-1)graph.get_state(subgraph_config).values

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__codelineno-13-1){'foo': 'hi! foobar', 'bar': 'bar'}

```


If you want to learn more about how to modify the subgraph state for human-in-the-loop workflows, check out this [how-to guide](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/).

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to add thread-level persistence to your graph  ](https://langchain-ai.github.io/langgraph/how-tos/persistence/) [ Next  How to add cross-thread persistence to your graph  ](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/subgraph-persistence/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
