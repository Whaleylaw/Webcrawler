---
url: https://langchain-ai.github.io/langgraph/concepts/streaming
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/concepts/streaming/#streaming)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Streaming 

[ ](https://langchain-ai.github.io/langgraph/concepts/streaming/?q= "Share")

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
      * [ Concepts  ](https://langchain-ai.github.io/langgraph/concepts/)

Concepts 
        * LangGraph  LangGraph 
          * [ LangGraph  ](https://langchain-ai.github.io/langgraph/concepts#langgraph)
          * [ Why LangGraph?  ](https://langchain-ai.github.io/langgraph/concepts/high_level/)
          * [ LangGraph Glossary  ](https://langchain-ai.github.io/langgraph/concepts/low_level/)
          * [ Agent architectures  ](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/)
          * [ Multi-agent Systems  ](https://langchain-ai.github.io/langgraph/concepts/multi_agent/)
          * [ None  ](https://langchain-ai.github.io/langgraph/concepts/breakpoints)
          * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/)
          * [ Time Travel ⏱️  ](https://langchain-ai.github.io/langgraph/concepts/time-travel/)
          * [ Persistence  ](https://langchain-ai.github.io/langgraph/concepts/persistence/)
          * [ Memory  ](https://langchain-ai.github.io/langgraph/concepts/memory/)
          * Streaming  [ Streaming  ](https://langchain-ai.github.io/langgraph/concepts/streaming/) Table of contents 
            * [ Streaming graph outputs (.stream and .astream)  ](https://langchain-ai.github.io/langgraph/concepts/streaming/#streaming-graph-outputs-stream-and-astream)
            * [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/concepts/streaming/#langgraph-platform)
          * [ Functional API  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/)
        * [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/concepts#langgraph-platform)
      * [ Tutorials  ](https://langchain-ai.github.io/langgraph/tutorials/)
    * Resources  Resources 
      * [ Prebuilt Agents  ](https://langchain-ai.github.io/langgraph/prebuilt/)
      * [ Adopters  ](https://langchain-ai.github.io/langgraph/adopters/)
      * [ FAQ  ](https://langchain-ai.github.io/langgraph/concepts/faq/)
      * [ Troubleshooting  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraph/reference/graphs/)



Table of contents 

  * [ Streaming graph outputs (.stream and .astream)  ](https://langchain-ai.github.io/langgraph/concepts/streaming/#streaming-graph-outputs-stream-and-astream)
  * [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/concepts/streaming/#langgraph-platform)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ Concepts  ](https://langchain-ai.github.io/langgraph/concepts/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/concepts#langgraph)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/concepts/streaming.md "Edit this page")

# Streaming[¶](https://langchain-ai.github.io/langgraph/concepts/streaming/#streaming "Permanent link")

Building a responsive app for end-users? Real-time updates are key to keeping users engaged as your app progresses.

There are three main types of data you’ll want to stream:

  1. Workflow progress (e.g., get state updates after each graph node is executed).
  2. LLM tokens as they’re generated.
  3. Custom updates (e.g., "Fetched 10/100 records").



## Streaming graph outputs (`.stream` and `.astream`)[¶](https://langchain-ai.github.io/langgraph/concepts/streaming/#streaming-graph-outputs-stream-and-astream "Permanent link")

`.stream` and `.astream` are sync and async methods for streaming back outputs from a graph run. There are several different modes you can specify when calling these methods (e.g. `graph.stream(..., mode="...")):

  * `"values"`[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#values): This streams the full value of the state after each step of the graph.
  * `"updates"`[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#updates): This streams the updates to the state after each step of the graph. If multiple updates are made in the same step (e.g. multiple nodes are run) then those updates are streamed separately.
  * `"custom"`[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#custom): This streams custom data from inside your graph nodes.
  * `"messages"`[](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/): This streams LLM tokens and metadata for the graph node where LLM is invoked.
  * `"debug"`[](https://langchain-ai.github.io/langgraph/how-tos/streaming/#debug): This streams as much information as possible throughout the execution of the graph.



You can also specify multiple streaming modes at the same time by passing them as a list. When you do this, the streamed outputs will be tuples `(stream_mode, data)`. For example:

```
[](https://langchain-ai.github.io/langgraph/concepts/streaming/#__codelineno-0-1)graph.stream(..., stream_mode=["updates", "messages"])

```


```
[](https://langchain-ai.github.io/langgraph/concepts/streaming/#__codelineno-1-1)...
[](https://langchain-ai.github.io/langgraph/concepts/streaming/#__codelineno-1-2)('messages', (AIMessageChunk(content='Hi'), {'langgraph_step': 3, 'langgraph_node': 'agent', ...}))
[](https://langchain-ai.github.io/langgraph/concepts/streaming/#__codelineno-1-3)...
[](https://langchain-ai.github.io/langgraph/concepts/streaming/#__codelineno-1-4)('updates', {'agent': {'messages': [AIMessage(content="Hi, how can I help you?")]}})

```


The below visualization shows the difference between the `values` and `updates` modes:

![values vs updates](https://langchain-ai.github.io/langgraph/static/values_vs_updates.png)

## LangGraph Platform[¶](https://langchain-ai.github.io/langgraph/concepts/streaming/#langgraph-platform "Permanent link")

Streaming is critical for making LLM applications feel responsive to end users. When creating a streaming run, the streaming mode determines what data is streamed back to the API client. LangGraph Platform supports five streaming modes:

  * `values`: Stream the full state of the graph after each [super-step](https://langchain-ai.github.io/langgraph/concepts/low_level/#graphs) is executed. See the [how-to guide](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/) for streaming values.
  * `messages-tuple`: Stream LLM tokens for any messages generated inside a node. This mode is primarily meant for powering chat applications. See the [how-to guide](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_messages/) for streaming messages.
  * `updates`: Streams updates to the state of the graph after each node is executed. See the [how-to guide](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_updates/) for streaming updates.
  * `debug`: Stream debug events throughout graph execution. See the [how-to guide](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_debug/) for streaming debug events.
  * `events`: Stream all events (including the state of the graph) that occur during graph execution. See the [how-to guide](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_events/) for streaming events. This mode is only useful for users migrating large LCEL applications to LangGraph. Generally, this mode is not necessary for most applications.



You can also specify multiple streaming modes at the same time. See the [how-to guide](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_multiple/) for configuring multiple streaming modes at the same time.

See the [API reference](https://langchain-ai.github.io/langgraph/cloud/reference/api/api_ref.html#tag/threads-runs/POST/threads/{thread_id}/runs/stream) for how to create streaming runs.

Streaming modes `values`, `updates`, `messages-tuple` and `debug` are very similar to modes available in the LangGraph library - for a deeper conceptual explanation of those, you can see the [previous section](https://langchain-ai.github.io/langgraph/concepts/streaming/#streaming-graph-outputs-stream-and-astream).

Streaming mode `events` is the same as using `.astream_events` in the LangGraph library - for a deeper conceptual explanation of this, you can see the [previous section](https://langchain-ai.github.io/langgraph/concepts/streaming/#streaming-graph-outputs-stream-and-astream).

All events emitted have two attributes:

  * `event`: This is the name of the event
  * `data`: This is data associated with the event

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Memory  ](https://langchain-ai.github.io/langgraph/concepts/memory/) [ Next  Functional API  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/concepts/streaming/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
