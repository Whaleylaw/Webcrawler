---
url: https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#how-to-add-thread-level-persistence-to-subgraphs)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to add thread-level persistence to subgraphs 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/?q= "Share")

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
            * [ How to add thread-level persistence (functional API)  ](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/)
            * How to add thread-level persistence to subgraphs  [ How to add thread-level persistence to subgraphs  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#setup)
              * [ Define the graph with persistence  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#define-the-graph-with-persistence)
              * [ Verify persistence works  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#verify-persistence-works)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#setup)
  * [ Define the graph with persistence  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#define-the-graph-with-persistence)
  * [ Verify persistence works  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#verify-persistence-works)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
  5. [ Persistence  ](https://langchain-ai.github.io/langgraphjs/how-tos#persistence)



# How to add thread-level persistence to subgraphs[¶](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#how-to-add-thread-level-persistence-to-subgraphs "Permanent link")

Prerequisites

This guide assumes familiarity with the following: 

  * [ Subgraphs ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#subgraphs)
  * [ Persistence ](https://langchain-ai.github.io/langgraphjs/concepts/persistence/)



This guide shows how you can add [thread-level](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/) persistence to graphs that use [subgraphs](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/).

## Setup[¶](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#setup "Permanent link")

First, let's install required packages:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-0-1)$npminstall@langchain/langgraph@langchain/core

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Define the graph with persistence[¶](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#define-the-graph-with-persistence "Permanent link")

To add persistence to a graph with subgraphs, all you need to do is pass a [checkpointer](https://langchain-ai.github.io/langgraphjs/reference/classes/checkpoint.BaseCheckpointSaver.html) when **compiling the parent graph**. LangGraph will automatically propagate the checkpointer to the child subgraphs.

Note

You **shouldn't provide** a checkpointer when compiling a subgraph. Instead, you must define a **single** checkpointer that you pass to `parentGraph.compile()`, and LangGraph will automatically propagate the checkpointer to the child subgraphs. If you pass the checkpointer to the `subgraph.compile()`, it will simply be ignored. This also applies when you [add a node that invokes the subgraph explicitly](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph#add-a-node-function-that-invokes-the-subgraph). 

Let's define a simple graph with a single subgraph node to show how to do this.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-1-1)import{StateGraph,Annotation}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-1-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-1-3)// subgraph
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-1-5)constSubgraphStateAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-1-6)foo:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-1-7)bar:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-1-8)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-1-10)constsubgraphNode1=async(state:typeofSubgraphStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-1-11)return{bar:"bar"};
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-1-12)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-1-13)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-1-14)constsubgraphNode2=async(state:typeofSubgraphStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-1-15)// note that this node is using a state key ('bar') that is only available in the subgraph
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-1-16)// and is sending update on the shared state key ('foo')
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-1-17)return{foo:state.foo+state.bar};
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-1-18)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-1-19)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-1-20)constsubgraph=newStateGraph(SubgraphStateAnnotation)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-1-21).addNode("subgraphNode1",subgraphNode1)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-1-22).addNode("subgraphNode2",subgraphNode2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-1-23).addEdge("__start__","subgraphNode1")
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-1-24).addEdge("subgraphNode1","subgraphNode2")
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-1-25).compile();
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-1-26)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-1-27)// parent graph
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-1-28)constStateAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-1-29)foo:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-1-30)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-1-31)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-1-32)constnode1=async(state:typeofStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-1-33)return{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-1-34)foo:"hi! "+state.foo,
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-1-35)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-1-36)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-1-37)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-1-38)constbuilder=newStateGraph(StateAnnotation)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-1-39).addNode("node1",node1)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-1-40)// note that we're adding the compiled subgraph as a node to the parent graph
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-1-41).addNode("node2",subgraph)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-1-42).addEdge("__start__","node1")
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-1-43).addEdge("node1","node2");

```


We can now compile the graph with an in-memory checkpointer (`MemorySaver`).

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-2-1)import{MemorySaver}from"@langchain/langgraph-checkpoint";
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-2-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-2-3)constcheckpointer=newMemorySaver();
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-2-4)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-2-5)// You must only pass checkpointer when compiling the parent graph.
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-2-6)// LangGraph will automatically propagate the checkpointer to the child subgraphs.
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-2-7)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-2-8)constgraph=builder.compile({
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-2-9)checkpointer:checkpointer
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-2-10)});

```


## Verify persistence works[¶](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#verify-persistence-works "Permanent link")

Let's now run the graph and inspect the persisted state for both the parent graph and the subgraph to verify that persistence works. We should expect to see the final execution results for both the parent and subgraph in `state.values`.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-3-1)constconfig={configurable:{thread_id:"1"}};

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-4-1)conststream=awaitgraph.stream({
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-4-2)foo:"foo"
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-4-3)},{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-4-4)...config,
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-4-5)subgraphs:true,
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-4-6)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-4-7)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-4-8)forawait(const[_source,chunk]ofstream){
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-4-9)console.log(chunk);
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-4-10)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-5-1){ node1: { foo: 'hi! foo' } }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-5-2){ subgraphNode1: { bar: 'bar' } }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-5-3){ subgraphNode2: { foo: 'hi! foobar' } }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-5-4){ node2: { foo: 'hi! foobar' } }

```


We can now view the parent graph state by calling `graph.get_state()` with the same config that we used to invoke the graph. 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-6-1)(awaitgraph.getState(config)).values;

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-7-1){ foo: 'hi! foobar' }

```


To view the subgraph state, we need to do two things: 

  1. Find the most recent config value for the subgraph
  2. Use `graph.getState()` to retrieve that value for the most recent subgraph config.



To find the correct config, we can examine the state history from the parent graph and find the state snapshot before we return results from `node2` (the node with subgraph):

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-8-1)letstateWithSubgraph;
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-8-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-8-3)constgraphHistories=awaitgraph.getStateHistory(config);
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-8-4)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-8-5)forawait(conststateofgraphHistories){
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-8-6)if(state.next[0]==="node2"){
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-8-7)stateWithSubgraph=state;
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-8-8)break;
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-8-9)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-8-10)}

```


The state snapshot will include the list of `tasks` to be executed next. When using subgraphs, the `tasks` will contain the config that we can use to retrieve the subgraph state:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-9-1)constsubgraphConfig=stateWithSubgraph.tasks[0].state;
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-9-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-9-3)console.log(subgraphConfig);

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-10-1){
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-10-2) configurable: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-10-3)  thread_id: '1',
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-10-4)  checkpoint_ns: 'node2:25814e09-45f0-5b70-a5b4-23b869d582c2'
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-10-5) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-10-6)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-11-1)(awaitgraph.getState(subgraphConfig)).values

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__codelineno-12-1){ foo: 'hi! foobar', bar: 'bar' }

```


If you want to learn more about how to modify the subgraph state for human-in-the-loop workflows, check out this [how-to guide](https://langchain-ai.github.io/langgraph/how-tos/subgraphs-manage-state/).  Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to add thread-level persistence (functional API)  ](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/) [ Next  How to add cross-thread persistence to your graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
