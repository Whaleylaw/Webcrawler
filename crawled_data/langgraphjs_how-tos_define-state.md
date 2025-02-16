---
url: https://langchain-ai.github.io/langgraphjs/how-tos/define-state/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#how-to-define-graph-state)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to define graph state 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/?q= "Share")

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
          * [ Subgraphs  ](https://langchain-ai.github.io/langgraphjs/how-tos#subgraphs)
          * [ Multi-agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/)
          * State Management  State Management 
            * [ State Management  ](https://langchain-ai.github.io/langgraphjs/how-tos#state-management)
            * How to define graph state  [ How to define graph state  ](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/) Table of contents 
              * [ Prerequisites  ](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#prerequisites)
              * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#setup)
              * [ Getting started  ](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#getting-started)
              * [ Merging states  ](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#merging-states)
              * [ State channels  ](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#state-channels)
            * [ How to define input/output schema for your graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/input_output_schema/)
            * [ How to pass private state  ](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/)
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

  * [ Prerequisites  ](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#prerequisites)
  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#setup)
  * [ Getting started  ](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#getting-started)
  * [ Merging states  ](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#merging-states)
  * [ State channels  ](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#state-channels)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
  5. [ State Management  ](https://langchain-ai.github.io/langgraphjs/how-tos#state-management)



# How to define graph state[¶](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#how-to-define-graph-state "Permanent link")

This how to guide will cover different ways to define the state of your graph.

## Prerequisites[¶](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#prerequisites "Permanent link")

  * [State conceptual guide](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#state) - Conceptual guide on defining the state of your graph.
  * [Building graphs](https://langchain-ai.github.io/langgraphjs/tutorials/quickstart/) - This how-to assumes you have a basic understanding of how to build graphs.



## Setup[¶](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#setup "Permanent link")

This guide requires installing the `@langchain/langgraph`, and `@langchain/core` packages:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#__codelineno-0-1)npminstall@langchain/langgraph@langchain/core

```


## Getting started[¶](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#getting-started "Permanent link")

The `Annotation` function is the recommended way to define your graph state for new `StateGraph` graphs. The `Annotation.Root` function is used to create the top-level state object, where each field represents a channel in the graph.

Here's an example of how to define a simple graph state with one channel called `messages`:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#__codelineno-1-1)import{BaseMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#__codelineno-1-2)import{Annotation}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#__codelineno-1-4)constGraphAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#__codelineno-1-5)// Define a 'messages' channel to store an array of BaseMessage objects
[](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#__codelineno-1-6)messages:Annotation<BaseMessage[]>({
[](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#__codelineno-1-7)// Reducer function: Combines the current state with new messages
[](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#__codelineno-1-8)reducer:(currentState,updateValue)=>currentState.concat(updateValue),
[](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#__codelineno-1-9)// Default function: Initialize the channel with an empty array
[](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#__codelineno-1-10)default:()=>[],
[](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#__codelineno-1-11)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#__codelineno-1-12)});

```


Each channel can optionally have `reducer` and `default` functions: - The `reducer` function defines how new values are combined with the existing state. - The `default` function provides an initial value for the channel.

For more information on reducers, see the [reducers conceptual guide](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#reducers)

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#__codelineno-2-1)constQuestionAnswerAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#__codelineno-2-2)question:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#__codelineno-2-3)answer:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#__codelineno-2-4)});

```


Above, all we're doing is defining the channels, and then passing the un-instantiated `Annotation` function as the value. It is important to note we always pass in the TypeScript type of each channel as the first generics argument to `Annotation`. Doing this ensures our graph state is type safe, and we can get the proper types when defining our nodes. Below shows how you can extract the typings from the `Annotation` function:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#__codelineno-3-1)typeQuestionAnswerAnnotationType=typeofQuestionAnswerAnnotation.State;

```


This is equivalent to the following type:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#__codelineno-4-1)typeQuestionAnswerAnnotationType={
[](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#__codelineno-4-2)question:string;
[](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#__codelineno-4-3)answer:string;
[](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#__codelineno-4-4)}

```


## Merging states[¶](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#merging-states "Permanent link")

If you have two graph state annotations, you can merge the two into a single annotation by using the `spec` value:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#__codelineno-5-1)constMergedAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#__codelineno-5-2)...QuestionAnswerAnnotation.spec,
[](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#__codelineno-5-3)...GraphAnnotation.spec,
[](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#__codelineno-5-4)})

```


The type of the merged annotation is the intersection of the two annotations:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#__codelineno-6-1)typeMergedAnnotation={
[](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#__codelineno-6-2)messages:BaseMessage[];
[](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#__codelineno-6-3)question:string;
[](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#__codelineno-6-4)answer:string;
[](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#__codelineno-6-5)}

```


Finally, instantiating your graph using the annotations is as simple as passing the annotation to the `StateGraph` constructor:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#__codelineno-7-1)import{StateGraph}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#__codelineno-7-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#__codelineno-7-3)constworkflow=newStateGraph(MergedAnnotation);

```


## State channels[¶](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#state-channels "Permanent link")

The `Annotation` function is a convince wrapper around the low level implementation of how states are defined in LangGraph. Defining state using the `channels` object (which is what `Annotation` is a wrapper of) is still possible, although not recommended for most cases. The below example shows how to implement a graph using this pattern:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#__codelineno-8-1)import{StateGraph}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#__codelineno-8-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#__codelineno-8-3)interfaceWorkflowChannelsState{
[](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#__codelineno-8-4)messages:BaseMessage[];
[](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#__codelineno-8-5)question:string;
[](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#__codelineno-8-6)answer:string;
[](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#__codelineno-8-7)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#__codelineno-8-8)
[](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#__codelineno-8-9)constworkflowWithChannels=newStateGraph<WorkflowChannelsState>({
[](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#__codelineno-8-10)channels:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#__codelineno-8-11)messages:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#__codelineno-8-12)reducer:(currentState,updateValue)=>currentState.concat(updateValue),
[](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#__codelineno-8-13)default:()=>[],
[](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#__codelineno-8-14)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#__codelineno-8-15)question:null,
[](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#__codelineno-8-16)answer:null,
[](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#__codelineno-8-17)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#__codelineno-8-18)});

```


Above, we set the value of `question` and `answer` to `null`, as it does not contain a default value. To set a default value, the channel should be implemented how the `messages` key is, with the `default` factory returing the default value. The `reducer` function is optional, and can be added to the channel object if needed.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to add multi-turn conversation in a multi-agent application (functional API)  ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/) [ Next  How to define input/output schema for your graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/input_output_schema/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
