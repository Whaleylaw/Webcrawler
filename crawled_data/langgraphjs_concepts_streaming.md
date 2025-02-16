---
url: https://langchain-ai.github.io/langgraphjs/concepts/streaming
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#streaming)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

Streaming 

[ ](https://langchain-ai.github.io/langgraphjs/concepts/streaming/?q= "Share")

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
      * [ Concepts  ](https://langchain-ai.github.io/langgraphjs/concepts/)

Concepts 
        * LangGraph  LangGraph 
          * [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/concepts#langgraph)
          * [ Why LangGraph?  ](https://langchain-ai.github.io/langgraphjs/concepts/high_level/)
          * [ LangGraph Glossary  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/)
          * [ Agent architectures  ](https://langchain-ai.github.io/langgraphjs/concepts/agentic_concepts/)
          * [ Multi-agent Systems  ](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/)
          * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/)
          * [ Persistence  ](https://langchain-ai.github.io/langgraphjs/concepts/persistence/)
          * [ Memory  ](https://langchain-ai.github.io/langgraphjs/concepts/memory/)
          * Streaming  [ Streaming  ](https://langchain-ai.github.io/langgraphjs/concepts/streaming/) Table of contents 
            * [ Streaming graph outputs (.stream)  ](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#streaming-graph-outputs-stream)
            * [ Streaming LLM tokens and events (.streamEvents)  ](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#streaming-llm-tokens-and-events-streamevents)
          * [ Functional API  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/)
        * [ LangGraph Platform  ](https://langchain-ai.github.io/langgraphjs/concepts#langgraph-platform)
      * [ Tutorials  ](https://langchain-ai.github.io/langgraphjs/tutorials/)
    * Resources  Resources 
      * [ Adopters  ](https://langchain-ai.github.io/langgraphjs/adopters/)
      * [ FAQ  ](https://langchain-ai.github.io/langgraphjs/concepts/faq/)
      * [ Troubleshooting  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraphjs/reference/)
  * [ Versions  ](https://langchain-ai.github.io/langgraphjs/versions/)



Table of contents 

  * [ Streaming graph outputs (.stream)  ](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#streaming-graph-outputs-stream)
  * [ Streaming LLM tokens and events (.streamEvents)  ](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#streaming-llm-tokens-and-events-streamevents)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ Concepts  ](https://langchain-ai.github.io/langgraphjs/concepts/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/concepts#langgraph)



# Streaming[¶](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#streaming "Permanent link")

LangGraph is built with first class support for streaming. There are several different ways to stream back outputs from a graph run

## Streaming graph outputs (`.stream`)[¶](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#streaming-graph-outputs-stream "Permanent link")

`.stream` is an async method for streaming back outputs from a graph run. There are several different modes you can specify when calling these methods (e.g. `await graph.stream(..., { ...config, streamMode: "values" })):

  * `"values"`[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values): This streams the full value of the state after each step of the graph.
  * `"updates"`[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-updates): This streams the updates to the state after each step of the graph. If multiple updates are made in the same step (e.g. multiple nodes are run) then those updates are streamed separately.
  * `"custom"`[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content.ipynb): This streams custom data from inside your graph nodes.
  * `"messages"`[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens.ipynb): This streams LLM tokens and metadata for the graph node where LLM is invoked.
  * `"debug"`: This streams as much information as possible throughout the execution of the graph.



The below visualization shows the difference between the `values` and `updates` modes:

![values vs updates](https://langchain-ai.github.io/langgraphjs/concepts/img/streaming/values_vs_updates.png)

## Streaming LLM tokens and events (`.streamEvents`)[¶](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#streaming-llm-tokens-and-events-streamevents "Permanent link")

In addition, you can use the `streamEvents`[](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools) method to stream back events that happen _inside_ nodes. This is useful for streaming tokens of LLM calls.

This is a standard method on all [LangChain objects](https://js.langchain.com/docs/concepts/#runnable-interface). This means that as the graph is executed, certain events are emitted along the way and can be seen if you run the graph using `.streamEvents`.

All events have (among other things) `event`, `name`, and `data` fields. What do these mean?

  * `event`: This is the type of event that is being emitted. You can find a detailed table of all callback events and triggers [here](https://js.langchain.com/docs/concepts/#callback-events).
  * `name`: This is the name of event.
  * `data`: This is the data associated with the event.



What types of things cause events to be emitted?

  * each node (runnable) emits `on_chain_start` when it starts execution, `on_chain_stream` during the node execution and `on_chain_end` when the node finishes. Node events will have the node name in the event's `name` field
  * the graph will emit `on_chain_start` in the beginning of the graph execution, `on_chain_stream` after each node execution and `on_chain_end` when the graph finishes. Graph events will have the `LangGraph` in the event's `name` field
  * Any writes to state channels (i.e. anytime you update the value of one of your state keys) will emit `on_chain_start` and `on_chain_end` events



Additionally, any events that are created inside your nodes (LLM events, tool events, manually emitted events, etc.) will also be visible in the output of `.streamEvents`.

To make this more concrete and to see what this looks like, let's see what events are returned when we run a simple graph:

```
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-0-1)import{ChatOpenAI}from"@langchain/openai";
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-0-2)import{StateGraph,MessagesAnnotation}from"langgraph";
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-0-3)
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-0-4)constmodel=newChatOpenAI({model:"gpt-4-turbo-preview"});
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-0-5)
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-0-6)functioncallModel(state:typeofMessagesAnnotation.State){
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-0-7)constresponse=model.invoke(state.messages);
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-0-8)return{messages:response};
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-0-9)}
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-0-10)
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-0-11)constworkflow=newStateGraph(MessagesAnnotation)
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-0-12).addNode("callModel",callModel)
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-0-13).addEdge("start","callModel")
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-0-14).addEdge("callModel","end");
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-0-15)constapp=workflow.compile();
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-0-16)
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-0-17)constinputs=[{role:"user",content:"hi!"}];
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-0-18)
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-0-19)forawait(consteventofapp.streamEvents({messages:inputs})){
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-0-20)constkind=event.event;
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-0-21)console.log(`${kind}: ${event.name}`);
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-0-22)}

```


```
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-1-1)on_chain_start:LangGraph
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-1-2)on_chain_start:__start__
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-1-3)on_chain_end:__start__
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-1-4)on_chain_start:callModel
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-1-5)on_chat_model_start:ChatOpenAI
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-1-6)on_chat_model_stream:ChatOpenAI
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-1-7)on_chat_model_stream:ChatOpenAI
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-1-8)on_chat_model_stream:ChatOpenAI
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-1-9)on_chat_model_stream:ChatOpenAI
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-1-10)on_chat_model_stream:ChatOpenAI
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-1-11)on_chat_model_stream:ChatOpenAI
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-1-12)on_chat_model_stream:ChatOpenAI
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-1-13)on_chat_model_stream:ChatOpenAI
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-1-14)on_chat_model_stream:ChatOpenAI
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-1-15)on_chat_model_stream:ChatOpenAI
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-1-16)on_chat_model_stream:ChatOpenAI
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-1-17)on_chat_model_end:ChatOpenAI
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-1-18)on_chain_start:ChannelWrite<callModel,messages>
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-1-19)on_chain_end:ChannelWrite<callModel,messages>
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-1-20)on_chain_stream:callModel
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-1-21)on_chain_end:callModel
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-1-22)on_chain_stream:LangGraph
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-1-23)on_chain_end:LangGraph

```


We start with the overall graph start (`on_chain_start: LangGraph`). We then write to the `__start__` node (this is special node to handle input). We then start the `callModel` node (`on_chain_start: callModel`). We then start the chat model invocation (`on_chat_model_start: ChatOpenAI`), stream back token by token (`on_chat_model_stream: ChatOpenAI`) and then finish the chat model (`on_chat_model_end: ChatOpenAI`). From there, we write the results back to the channel (`ChannelWrite<callModel,messages>`) and then finish the `callModel` node and then the graph as a whole.

This should hopefully give you a good sense of what events are emitted in a simple graph. But what data do these events contain? Each type of event contains data in a different format. Let's look at what `on_chat_model_stream` events look like. This is an important type of event since it is needed for streaming tokens from an LLM response.

These events look like:

```
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-2-1){'event':'on_chat_model_stream',
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-2-2)'name':'ChatOpenAI',
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-2-3)'run_id':'3fdbf494-acce-402e-9b50-4eab46403859',
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-2-4)'tags':['seq:step:1'],
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-2-5)'metadata':{'langgraph_step':1,
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-2-6)'langgraph_node':'callModel',
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-2-7)'langgraph_triggers':['start:callModel'],
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-2-8)'langgraph_task_idx':0,
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-2-9)'checkpoint_id':'1ef657a0-0f9d-61b8-bffe-0c39e4f9ad6c',
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-2-10)'checkpoint_ns':'callModel',
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-2-11)'ls_provider':'openai',
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-2-12)'ls_model_name':'gpt-4o-mini',
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-2-13)'ls_model_type':'chat',
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-2-14)'ls_temperature':0.7},
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-2-15)'data':{'chunk':AIMessageChunk({content:'Hello',id:'run-3fdbf494-acce-402e-9b50-4eab46403859'})},
[](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__codelineno-2-16)'parent_ids':[]}

```


We can see that we have the event type and name (which we knew from before).

We also have a bunch of stuff in metadata. Noticeably, `'langgraph_node': 'callModel',` is some really helpful information which tells us which node this model was invoked inside of.

Finally, `data` is a really important field. This contains the actual data for this event! Which in this case is an AIMessageChunk. This contains the `content` for the message, as well as an `id`. This is the ID of the overall AIMessage (not just this chunk) and is super helpful - it helps us track which chunks are part of the same message (so we can show them together in the UI).

This information contains all that is needed for creating a UI for streaming LLM tokens.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  Memory  ](https://langchain-ai.github.io/langgraphjs/concepts/memory/) [ Next  Functional API  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/concepts/streaming/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
