---
url: https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#how-to-transform-inputs-and-outputs-of-a-subgraph)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to transform inputs and outputs of a subgraph 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/?q= "Share")

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
          * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraphjs/how-tos#human-in-the-loop)
          * [ Streaming  ](https://langchain-ai.github.io/langgraphjs/how-tos#streaming)
          * [ Tool calling  ](https://langchain-ai.github.io/langgraphjs/how-tos#tool-calling)
          * Subgraphs  Subgraphs 
            * [ Subgraphs  ](https://langchain-ai.github.io/langgraphjs/how-tos#subgraphs)
            * [ How to add and use subgraphs  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/)
            * [ How to view and update state in subgraphs  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/)
            * How to transform inputs and outputs of a subgraph  [ How to transform inputs and outputs of a subgraph  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#setup)
              * [ Define graph and subgraphs  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#define-graph-and-subgraphs)
                * [ Define grandchild  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#define-grandchild)
                * [ Define child  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#define-child)
                * [ Define parent  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#define-parent)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#setup)
  * [ Define graph and subgraphs  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#define-graph-and-subgraphs)
    * [ Define grandchild  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#define-grandchild)
    * [ Define child  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#define-child)
    * [ Define parent  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#define-parent)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
  5. [ Subgraphs  ](https://langchain-ai.github.io/langgraphjs/how-tos#subgraphs)



# How to transform inputs and outputs of a subgraph[¶](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#how-to-transform-inputs-and-outputs-of-a-subgraph "Permanent link")

It's possible that your subgraph state is completely independent from the parent graph state, i.e. there are no overlapping channels (keys) between the two. For example, you might have a supervisor agent that needs to produce a report with a help of multiple ReAct agents. ReAct agent subgraphs might keep track of a list of messages whereas the supervisor only needs user input and final report in its state, and doesn't need to keep track of messages.

In such cases you need to transform the inputs to the subgraph before calling it and then transform its outputs before returning. This guide shows how to do that.

## Setup[¶](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#setup "Permanent link")

First, let's install the required packages

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-0-1)npminstall@langchain/langgraph@langchain/core

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Define graph and subgraphs[¶](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#define-graph-and-subgraphs "Permanent link")

Let's define 3 graphs: - a parent graph - a child subgraph that will be called by the parent graph - a grandchild subgraph that will be called by the child graph

### Define grandchild[¶](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#define-grandchild "Permanent link")

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-1-1)import{StateGraph,START,Annotation}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-1-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-1-3)constGrandChildAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-1-4)myGrandchildKey:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-1-5)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-1-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-1-7)constgrandchild1=(state:typeofGrandChildAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-1-8)// NOTE: child or parent keys will not be accessible here
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-1-9)return{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-1-10)myGrandchildKey:state.myGrandchildKey+", how are you"
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-1-11)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-1-12)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-1-13)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-1-14)constgrandchild=newStateGraph(GrandChildAnnotation)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-1-15).addNode("grandchild1",grandchild1)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-1-16).addEdge(START,"grandchild1")
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-1-17)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-1-18)constgrandchildGraph=grandchild.compile();

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-2-1)awaitgrandchildGraph.invoke({myGrandchildKey:"hi Bob"})

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-3-1){ myGrandchildKey: 'hi Bob, how are you' }

```


### Define child[¶](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#define-child "Permanent link")

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-4-1)import{StateGraph,START,Annotation}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-4-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-4-3)constChildAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-4-4)myChildKey:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-4-5)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-4-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-4-7)constcallGrandchildGraph=async(state:typeofChildAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-4-8)// NOTE: parent or grandchild keys won't be accessible here
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-4-9)// we're transforming the state from the child state channels (`myChildKey`)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-4-10)// to the grandchild state channels (`myGrandchildKey`)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-4-11)constgrandchildGraphInput={myGrandchildKey:state.myChildKey};
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-4-12)// we're transforming the state from the grandchild state channels (`myGrandchildKey`)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-4-13)// back to the child state channels (`myChildKey`)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-4-14)constgrandchildGraphOutput=awaitgrandchildGraph.invoke(grandchildGraphInput);
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-4-15)return{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-4-16)myChildKey:grandchildGraphOutput.myGrandchildKey+" today?"
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-4-17)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-4-18)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-4-19)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-4-20)constchild=newStateGraph(ChildAnnotation)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-4-21)// NOTE: we're passing a function here instead of just compiled graph (`childGraph`)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-4-22).addNode("child1",callGrandchildGraph)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-4-23).addEdge(START,"child1");
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-4-24)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-4-25)constchildGraph=child.compile();

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-5-1)awaitchildGraph.invoke({myChildKey:"hi Bob"})

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-6-1){ myChildKey: 'hi Bob, how are you today?' }

```


Note

We're wrapping the `grandchildGraph` invocation in a separate function (`callGrandchildGraph`) that transforms the input state before calling the grandchild graph and then transforms the output of grandchild graph back to child graph state. If you just pass `grandchildGraph` directly to `.addNode` without the transformations, LangGraph will raise an error as there are no shared state channels (keys) between child and grandchild states. 

Note that child and grandchild subgraphs have their own, **independent** state that is not shared with the parent graph.

### Define parent[¶](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#define-parent "Permanent link")

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-7-1)import{StateGraph,START,END,Annotation}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-7-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-7-3)constParentAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-7-4)myKey:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-7-5)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-7-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-7-7)constparent1=(state:typeofParentAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-7-8)// NOTE: child or grandchild keys won't be accessible here
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-7-9)return{myKey:"hi "+state.myKey};
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-7-10)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-7-11)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-7-12)constparent2=(state:typeofParentAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-7-13)return{myKey:state.myKey+" bye!"};
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-7-14)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-7-15)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-7-16)constcallChildGraph=async(state:typeofParentAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-7-17)// we're transforming the state from the parent state channels (`myKey`)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-7-18)// to the child state channels (`myChildKey`)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-7-19)constchildGraphInput={myChildKey:state.myKey};
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-7-20)// we're transforming the state from the child state channels (`myChildKey`)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-7-21)// back to the parent state channels (`myKey`)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-7-22)constchildGraphOutput=awaitchildGraph.invoke(childGraphInput);
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-7-23)return{myKey:childGraphOutput.myChildKey};
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-7-24)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-7-25)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-7-26)constparent=newStateGraph(ParentAnnotation)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-7-27).addNode("parent1",parent1)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-7-28)// NOTE: we're passing a function here instead of just a compiled graph (`childGraph`)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-7-29).addNode("child",callChildGraph)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-7-30).addNode("parent2",parent2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-7-31).addEdge(START,"parent1")
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-7-32).addEdge("parent1","child")
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-7-33).addEdge("child","parent2")
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-7-34).addEdge("parent2",END);
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-7-35)
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-7-36)constparentGraph=parent.compile();

```


Note

We're wrapping the `childGraph` invocation in a separate function (`callChildGraph`) that transforms the input state before calling the child graph and then transforms the output of the child graph back to parent graph state. If you just pass `childGraph` directly to `.addNode` without the transformations, LangGraph will raise an error as there are no shared state channels (keys) between parent and child states. 

Let's run the parent graph and make sure it correctly calls both the child and grandchild subgraphs:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-8-1)awaitparentGraph.invoke({myKey:"Bob"})

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__codelineno-9-1){ myKey: 'hi Bob, how are you today? bye!' }

```


Perfect! The parent graph correctly calls both the child and grandchild subgraphs (which we know since the ", how are you" and "today?" are added to our original "myKey" state value).  Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to view and update state in subgraphs  ](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/) [ Next  How to build a multi-agent network  ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
