---
url: https://langchain-ai.github.io/langgraph/concepts/langgraph_server
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#langgraph-server)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

LangGraph Server 

[ ](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/?q= "Share")

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
        * [ LangGraph  ](https://langchain-ai.github.io/langgraph/concepts#langgraph)
        * LangGraph Platform  LangGraph Platform 
          * [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/concepts#langgraph-platform)
          * [ High Level  ](https://langchain-ai.github.io/langgraph/concepts#high-level)
          * Components  Components 
            * [ Components  ](https://langchain-ai.github.io/langgraph/concepts#components)
            * LangGraph Server  [ LangGraph Server  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/) Table of contents 
              * [ Overview  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#overview)
              * [ Key Features  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#key-features)
              * [ What are you deploying?  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#what-are-you-deploying)
                * [ Graphs  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#graphs)
                * [ Persistence and Task Queue  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#persistence-and-task-queue)
              * [ Application Structure  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#application-structure)
              * [ LangGraph Server API  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#langgraph-server-api)
                * [ Assistants  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#assistants)
                * [ Threads  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#threads)
                * [ Runs  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#runs)
                * [ Store  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#store)
                * [ Cron Jobs  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#cron-jobs)
                * [ Webhooks  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#webhooks)
              * [ Related  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#related)
            * [ LangGraph Studio  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_studio/)
            * [ LangGraph CLI  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_cli/)
            * [ LangGraph SDK  ](https://langchain-ai.github.io/langgraph/concepts/sdk/)
            * [ How to interact with the deployment using RemoteGraph  ](https://langchain-ai.github.io/langgraph/how-tos/use-remote-graph/)
          * [ LangGraph Server  ](https://langchain-ai.github.io/langgraph/concepts#langgraph-server)
          * [ Deployment Options  ](https://langchain-ai.github.io/langgraph/concepts#deployment-options)
      * [ Tutorials  ](https://langchain-ai.github.io/langgraph/tutorials/)
    * Resources  Resources 
      * [ Prebuilt Agents  ](https://langchain-ai.github.io/langgraph/prebuilt/)
      * [ Adopters  ](https://langchain-ai.github.io/langgraph/adopters/)
      * [ FAQ  ](https://langchain-ai.github.io/langgraph/concepts/faq/)
      * [ Troubleshooting  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraph/reference/graphs/)



Table of contents 

  * [ Overview  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#overview)
  * [ Key Features  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#key-features)
  * [ What are you deploying?  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#what-are-you-deploying)
    * [ Graphs  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#graphs)
    * [ Persistence and Task Queue  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#persistence-and-task-queue)
  * [ Application Structure  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#application-structure)
  * [ LangGraph Server API  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#langgraph-server-api)
    * [ Assistants  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#assistants)
    * [ Threads  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#threads)
    * [ Runs  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#runs)
    * [ Store  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#store)
    * [ Cron Jobs  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#cron-jobs)
    * [ Webhooks  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#webhooks)
  * [ Related  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#related)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ Concepts  ](https://langchain-ai.github.io/langgraph/concepts/)
  4. [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/concepts#langgraph-platform)
  5. [ Components  ](https://langchain-ai.github.io/langgraph/concepts#components)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/concepts/langgraph_server.md "Edit this page")

# LangGraph Server[¶](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#langgraph-server "Permanent link")

Prerequisites

  * [LangGraph Platform](https://langchain-ai.github.io/langgraph/concepts/langgraph_platform/)
  * [LangGraph Glossary](https://langchain-ai.github.io/langgraph/concepts/low_level/)



## Overview[¶](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#overview "Permanent link")

LangGraph Server offers an API for creating and managing agent-based applications. It is built on the concept of [assistants](https://langchain-ai.github.io/langgraph/concepts/assistants/), which are agents configured for specific tasks, and includes built-in [persistence](https://langchain-ai.github.io/langgraph/concepts/persistence/#memory-store) and a **task queue**. This versatile API supports a wide range of agentic application use cases, from background processing to real-time interactions.

## Key Features[¶](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#key-features "Permanent link")

The LangGraph Platform incorporates best practices for agent deployment, so you can focus on building your agent logic.

  * **Streaming endpoints** : Endpoints that expose [multiple different streaming modes](https://langchain-ai.github.io/langgraph/concepts/streaming/). We've made these work even for long-running agents that may go minutes between consecutive stream events.
  * **Background runs** : The LangGraph Server supports launching assistants in the background with endpoints for polling the status of the assistant's run and webhooks to monitor run status effectively.
  * **Support for long runs** : Our blocking endpoints for running assistants send regular heartbeat signals, preventing unexpected connection closures when handling requests that take a long time to complete.
  * **Task queue** : We've added a task queue to make sure we don't drop any requests if they arrive in a bursty nature.
  * **Horizontally scalable infrastructure** : LangGraph Server is designed to be horizontally scalable, allowing you to scale up and down your usage as needed.
  * **Double texting support** : Many times users might interact with your graph in unintended ways. For instance, a user may send one message and before the graph has finished running send a second message. We call this ["double texting"](https://langchain-ai.github.io/langgraph/concepts/double_texting/) and have added four different ways to handle this.
  * **Optimized checkpointer** : LangGraph Platform comes with a built-in [checkpointer](https://langchain-ai.github.io/langgraph/concepts/persistence/#checkpoints) optimized for LangGraph applications.
  * **Human-in-the-loop endpoints** : We've exposed all endpoints needed to support [human-in-the-loop](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/) features.
  * **Memory** : In addition to thread-level persistence (covered above by [checkpointers]l(./persistence.md#checkpoints)), LangGraph Platform also comes with a built-in [memory store](https://langchain-ai.github.io/langgraph/concepts/persistence/#memory-store).
  * **Cron jobs** : Built-in support for scheduling tasks, enabling you to automate regular actions like data clean-up or batch processing within your applications.
  * **Webhooks** : Allows your application to send real-time notifications and data updates to external systems, making it easy to integrate with third-party services and trigger actions based on specific events.
  * **Monitoring** : LangGraph Server integrates seamlessly with the [LangSmith](https://docs.smith.langchain.com/) monitoring platform, providing real-time insights into your application's performance and health.



## What are you deploying?[¶](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#what-are-you-deploying "Permanent link")

When you deploy a LangGraph Server, you are deploying one or more [graphs](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#graphs), a database for [persistence](https://langchain-ai.github.io/langgraph/concepts/persistence/), and a task queue.

### Graphs[¶](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#graphs "Permanent link")

When you deploy a graph with LangGraph Server, you are deploying a "blueprint" for an [Assistant](https://langchain-ai.github.io/langgraph/concepts/assistants/). 

An [Assistant](https://langchain-ai.github.io/langgraph/concepts/assistants/) is a graph paired with specific configuration settings. You can create multiple assistants per graph, each with unique settings to accommodate different use cases that can be served by the same graph.

Upon deployment, LangGraph Server will automatically create a default assistant for each graph using the graph's default configuration settings.

You can interact with assistants through the [LangGraph Server API](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#langgraph-server-api).

Note

We often think of a graph as implementing an [agent](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/), but a graph does not necessarily need to implement an agent. For example, a graph could implement a simple chatbot that only supports back-and-forth conversation, without the ability to influence any application control flow. In reality, as applications get more complex, a graph will often implement a more complex flow that may use [multiple agents](https://langchain-ai.github.io/langgraph/concepts/multi_agent/) working in tandem.

### Persistence and Task Queue[¶](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#persistence-and-task-queue "Permanent link")

The LangGraph Server leverages a database for [persistence](https://langchain-ai.github.io/langgraph/concepts/persistence/) and a task queue.

Currently, only [Postgres](https://www.postgresql.org/) is supported as a database for LangGraph Server and [Redis](https://redis.io/) as the task queue.

If you're deploying using [LangGraph Cloud](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/), these components are managed for you. If you're deploying LangGraph Server on your own infrastructure, you'll need to set up and manage these components yourself.

Please review the [deployment options](https://langchain-ai.github.io/langgraph/concepts/deployment_options/) guide for more information on how these components are set up and managed.

## Application Structure[¶](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#application-structure "Permanent link")

To deploy a LangGraph Server application, you need to specify the graph(s) you want to deploy, as well as any relevant configuration settings, such as dependencies and environment variables.

Read the [application structure](https://langchain-ai.github.io/langgraph/concepts/application_structure/) guide to learn how to structure your LangGraph application for deployment.

## LangGraph Server API[¶](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#langgraph-server-api "Permanent link")

The LangGraph Server API allows you to create and manage [assistants](https://langchain-ai.github.io/langgraph/concepts/assistants/), [threads](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#threads), [runs](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#runs), [cron jobs](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#cron-jobs), and more.

The [LangGraph Cloud API Reference](https://langchain-ai.github.io/langgraph/cloud/reference/api/api_ref.html) provides detailed information on the API endpoints and data models.

### Assistants[¶](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#assistants "Permanent link")

An [Assistant](https://langchain-ai.github.io/langgraph/concepts/assistants/) refers to a [graph](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#graphs) plus specific [configuration](https://langchain-ai.github.io/langgraph/concepts/low_level/#configuration) settings for that graph.

You can think of an assistant as a saved configuration of an [agent](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/).

When building agents, it is fairly common to make rapid changes that _do not_ alter the graph logic. For example, simply changing prompts or the LLM selection can have significant impacts on the behavior of the agents. Assistants offer an easy way to make and save these types of changes to agent configuration.

### Threads[¶](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#threads "Permanent link")

A thread contains the accumulated state of a sequence of [runs](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#runs). If a run is executed on a thread, then the [state](https://langchain-ai.github.io/langgraph/concepts/low_level/#state) of the underlying graph of the assistant will be persisted to the thread.

A thread's current and historical state can be retrieved. To persist state, a thread must be created prior to executing a run.

The state of a thread at a particular point in time is called a [checkpoint](https://langchain-ai.github.io/langgraph/concepts/persistence/#checkpoints). Checkpoints can be used to restore the state of a thread at a later time.

For more on threads and checkpoints, see this section of the [LangGraph conceptual guide](https://langchain-ai.github.io/langgraph/concepts/low_level/#persistence).

The LangGraph Cloud API provides several endpoints for creating and managing threads and thread state. See the [API reference](https://langchain-ai.github.io/langgraph/cloud/reference/api/api_ref.html#tag/threads) for more details.

### Runs[¶](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#runs "Permanent link")

A run is an invocation of an [assistant](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#assistants). Each run may have its own input, configuration, and metadata, which may affect execution and output of the underlying graph. A run can optionally be executed on a [thread](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#threads).

The LangGraph Cloud API provides several endpoints for creating and managing runs. See the [API reference](https://langchain-ai.github.io/langgraph/cloud/reference/api/api_ref.html#tag/thread-runs/) for more details.

### Store[¶](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#store "Permanent link")

Store is an API for managing persistent [key-value store](https://langchain-ai.github.io/langgraph/concepts/persistence/#memory-store) that is available from any [thread](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#threads).

Stores are useful for implementing [memory](https://langchain-ai.github.io/langgraph/concepts/memory/) in your LangGraph application.

### Cron Jobs[¶](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#cron-jobs "Permanent link")

There are many situations in which it is useful to run an assistant on a schedule. 

For example, say that you're building an assistant that runs daily and sends an email summary of the day's news. You could use a cron job to run the assistant every day at 8:00 PM.

LangGraph Cloud supports cron jobs, which run on a user-defined schedule. The user specifies a schedule, an assistant, and some input. After that, on the specified schedule, the server will:

  * Create a new thread with the specified assistant
  * Send the specified input to that thread



Note that this sends the same input to the thread every time. See the [how-to guide](https://langchain-ai.github.io/langgraph/cloud/how-tos/cron_jobs/) for creating cron jobs.

The LangGraph Cloud API provides several endpoints for creating and managing cron jobs. See the [API reference](https://langchain-ai.github.io/langgraph/cloud/reference/api/api_ref.html#tag/runscreate/POST/threads/{thread_id}/runs/crons) for more details.

### Webhooks[¶](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#webhooks "Permanent link")

Webhooks enable event-driven communication from your LangGraph Cloud application to external services. For example, you may want to issue an update to a separate service once an API call to LangGraph Cloud has finished running.

Many LangGraph Cloud endpoints accept a `webhook` parameter. If this parameter is specified by a an endpoint that can accept POST requests, LangGraph Cloud will send a request at the completion of a run.

See the corresponding [how-to guide](https://langchain-ai.github.io/langgraph/cloud/how-tos/webhooks/) for more detail.

## Related[¶](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#related "Permanent link")

  * LangGraph [Application Structure](https://langchain-ai.github.io/langgraph/concepts/application_structure/) guide explains how to structure your LangGraph application for deployment.
  * [How-to guides for the LangGraph Platform](https://langchain-ai.github.io/langgraph/how-tos/).
  * The [LangGraph Cloud API Reference](https://langchain-ai.github.io/langgraph/cloud/reference/api/api_ref.html) provides detailed information on the API endpoints and data models.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Template Applications  ](https://langchain-ai.github.io/langgraph/concepts/template_applications/) [ Next  LangGraph Studio  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_studio/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
