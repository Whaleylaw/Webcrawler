---
url: https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#how-to-stream-custom-data)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to stream custom data 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/?q= "Share")

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
          * Streaming  Streaming 
            * [ Streaming  ](https://langchain-ai.github.io/langgraphjs/how-tos#streaming)
            * [ How to stream full state of your graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/)
            * [ How to stream state updates of your graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-updates/)
            * [ How to stream LLM tokens from your graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/)
            * [ How to stream LLM tokens (without LangChain models)  ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/)
            * How to stream custom data  [ How to stream custom data  ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#setup)
              * [ Stream custom data using .stream  ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#stream-custom-data-using-stream)
                * [ Define the graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#define-the-graph)
                * [ Stream content  ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#stream-content)
              * [ Stream custom data using .streamEvents  ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#stream-custom-data-using-streamevents)
                * [ Define the graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#define-the-graph_1)
                * [ Stream content  ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#stream-content_1)
            * [ How to configure multiple streaming modes at the same time  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/)
            * [ How to stream events from within a tool  ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/)
            * [ How to stream from the final node  ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-from-final-node/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#setup)
  * [ Stream custom data using .stream  ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#stream-custom-data-using-stream)
    * [ Define the graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#define-the-graph)
    * [ Stream content  ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#stream-content)
  * [ Stream custom data using .streamEvents  ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#stream-custom-data-using-streamevents)
    * [ Define the graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#define-the-graph_1)
    * [ Stream content  ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#stream-content_1)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
  5. [ Streaming  ](https://langchain-ai.github.io/langgraphjs/how-tos#streaming)



# How to stream custom data[¶](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#how-to-stream-custom-data "Permanent link")

Prerequisites

This guide assumes familiarity with the following: 

  * [ Streaming ](https://langchain-ai.github.io/langgraphjs/concepts/streaming/)
  * [ streamEvents API ](https://js.langchain.com/docs/how_to/streaming#using-stream-events)
  * [ Chat Models ](https://js.langchain.com/docs/concepts/chat_models)
  * [ Tools ](https://js.langchain.com/docs/concepts/tools)



The most common use case for streaming from inside a node is to stream LLM tokens, but you may also want to stream custom data.

For example, if you have a long-running tool call, you can dispatch custom events between the steps and use these custom events to monitor progress. You could also surface these custom events to an end user of your application to show them how the current task is progressing.

You can do so in two ways:

  * using your graph's `.stream` method with `streamMode: "custom"`
  * emitting custom events using `dispatchCustomEvents`[](https://js.langchain.com/docs/how_to/callbacks_custom_events/) with `streamEvents`.



Below we'll see how to use both APIs.

## Setup[¶](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#setup "Permanent link")

First, let's install our required packages:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-0-1)npminstall@langchain/langgraph@langchain/core

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Stream custom data using .stream[¶](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#stream-custom-data-using-stream "Permanent link")

Compatibility

This section requires `@langchain/langgraph>=0.2.20`. For help upgrading, see [this guide](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/). 

### Define the graph[¶](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#define-the-graph "Permanent link")

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-1-1)import{
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-1-2)StateGraph,
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-1-3)MessagesAnnotation,
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-1-4)LangGraphRunnableConfig,
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-1-5)}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-1-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-1-7)constmyNode=async(
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-1-8)_state:typeofMessagesAnnotation.State,
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-1-9)config:LangGraphRunnableConfig
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-1-10))=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-1-11)constchunks=[
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-1-12)"Four",
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-1-13)"score",
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-1-14)"and",
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-1-15)"seven",
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-1-16)"years",
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-1-17)"ago",
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-1-18)"our",
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-1-19)"fathers",
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-1-20)"...",
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-1-21)];
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-1-22)for(constchunkofchunks){
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-1-23)// write the chunk to be streamed using streamMode=custom
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-1-24)// Only populated if one of the passed stream modes is "custom".
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-1-25)config.writer?.(chunk);
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-1-26)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-1-27)return{
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-1-28)messages:[{
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-1-29)role:"assistant",
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-1-30)content:chunks.join(" "),
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-1-31)}],
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-1-32)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-1-33)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-1-34)
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-1-35)constgraph=newStateGraph(MessagesAnnotation)
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-1-36).addNode("model",myNode)
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-1-37).addEdge("__start__","model")
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-1-38).compile();

```


### Stream content[¶](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#stream-content "Permanent link")

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-2-1)constinputs=[{
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-2-2)role:"user",
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-2-3)content:"What are you thinking about?",
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-2-4)}];
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-2-5)
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-2-6)conststream=awaitgraph.stream(
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-2-7){messages:inputs},
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-2-8){streamMode:"custom"}
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-2-9));
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-2-10)
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-2-11)forawait(constchunkofstream){
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-2-12)console.log(chunk);
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-2-13)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-3-1)Four
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-3-2)score
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-3-3)and
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-3-4)seven
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-3-5)years
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-3-6)ago
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-3-7)our
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-3-8)fathers
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-3-9)...

```


You will likely need to use [multiple streaming modes](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/) as you will want access to both the custom data and the state updates. 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-4-1)conststreamMultiple=awaitgraph.stream(
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-4-2){messages:inputs},
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-4-3){streamMode:["custom","updates"]}
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-4-4));
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-4-5)
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-4-6)forawait(constchunkofstreamMultiple){
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-4-7)console.log(chunk);
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-4-8)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-5-1)[ 'custom', 'Four' ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-5-2)[ 'custom', 'score' ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-5-3)[ 'custom', 'and' ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-5-4)[ 'custom', 'seven' ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-5-5)[ 'custom', 'years' ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-5-6)[ 'custom', 'ago' ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-5-7)[ 'custom', 'our' ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-5-8)[ 'custom', 'fathers' ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-5-9)[ 'custom', '...' ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-5-10)[ 'updates', { model: { messages: [Array] } } ]

```


## Stream custom data using .streamEvents[¶](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#stream-custom-data-using-streamevents "Permanent link")

If you are already using graph's `.streamEvents` method in your workflow, you can also stream custom data by emitting custom events using `dispatchCustomEvents`

### Define the graph[¶](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#define-the-graph_1 "Permanent link")

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-6-1)import{dispatchCustomEvent}from"@langchain/core/callbacks/dispatch";
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-6-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-6-3)constgraphNode=async(_state:typeofMessagesAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-6-4)constchunks=[
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-6-5)"Four",
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-6-6)"score",
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-6-7)"and",
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-6-8)"seven",
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-6-9)"years",
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-6-10)"ago",
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-6-11)"our",
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-6-12)"fathers",
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-6-13)"...",
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-6-14)];
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-6-15)for(constchunkofchunks){
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-6-16)awaitdispatchCustomEvent("my_custom_event",{chunk});
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-6-17)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-6-18)return{
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-6-19)messages:[{
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-6-20)role:"assistant",
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-6-21)content:chunks.join(" "),
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-6-22)}],
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-6-23)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-6-24)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-6-25)
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-6-26)constgraphWithDispatch=newStateGraph(MessagesAnnotation)
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-6-27).addNode("model",graphNode)
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-6-28).addEdge("__start__","model")
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-6-29).compile();

```


### Stream content[¶](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#stream-content_1 "Permanent link")

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-7-1)consteventStream=awaitgraphWithDispatch.streamEvents(
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-7-2){
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-7-3)messages:[{
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-7-4)role:"user",
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-7-5)content:"What are you thinking about?",
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-7-6)}]
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-7-7)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-7-8){
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-7-9)version:"v2",
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-7-10)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-7-11));
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-7-12)
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-7-13)forawait(const{event,name,data}ofeventStream){
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-7-14)if(event==="on_custom_event"&&name==="my_custom_event"){
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-7-15)console.log(`${data.chunk}|`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-7-16)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-7-17)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-8-1)Four|
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-8-2)score|
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-8-3)and|
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-8-4)seven|
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-8-5)years|
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-8-6)ago|
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-8-7)our|
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-8-8)fathers|
[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__codelineno-8-9)...|

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to stream LLM tokens (without LangChain models)  ](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/) [ Next  How to configure multiple streaming modes at the same time  ](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
