---
url: https://langchain-ai.github.io/langgraph/concepts/langgraph_platform
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/concepts/langgraph_platform/#langgraph-platform)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

LangGraph Platform 

[ ](https://langchain-ai.github.io/langgraph/concepts/langgraph_platform/?q= "Share")

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
          * High Level  High Level 
            * [ High Level  ](https://langchain-ai.github.io/langgraph/concepts#high-level)
            * LangGraph Platform  [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_platform/) Table of contents 
              * [ Overview  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_platform/#overview)
              * [ Why Use LangGraph Platform?  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_platform/#why-use-langgraph-platform)
            * [ Deployment Options  ](https://langchain-ai.github.io/langgraph/concepts/deployment_options/)
            * [ LangGraph Platform Plans  ](https://langchain-ai.github.io/langgraph/concepts/plans/)
            * [ Template Applications  ](https://langchain-ai.github.io/langgraph/concepts/template_applications/)
          * [ Components  ](https://langchain-ai.github.io/langgraph/concepts#components)
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

  * [ Overview  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_platform/#overview)
  * [ Why Use LangGraph Platform?  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_platform/#why-use-langgraph-platform)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ Concepts  ](https://langchain-ai.github.io/langgraph/concepts/)
  4. [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/concepts#langgraph-platform)
  5. [ High Level  ](https://langchain-ai.github.io/langgraph/concepts#high-level)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/concepts/langgraph_platform.md "Edit this page")

# LangGraph Platform[¶](https://langchain-ai.github.io/langgraph/concepts/langgraph_platform/#langgraph-platform "Permanent link")

## Overview[¶](https://langchain-ai.github.io/langgraph/concepts/langgraph_platform/#overview "Permanent link")

LangGraph Platform is a commercial solution for deploying agentic applications to production, built on the open-source [LangGraph framework](https://langchain-ai.github.io/langgraph/concepts/high_level/).

The LangGraph Platform consists of several components that work together to support the development, deployment, debugging, and monitoring of LangGraph applications:

  * [LangGraph Server](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/): The server defines an opinionated API and architecture that incorporates best practices for deploying agentic applications, allowing you to focus on building your agent logic rather than developing server infrastructure.
  * [LangGraph Studio](https://langchain-ai.github.io/langgraph/concepts/langgraph_studio/): LangGraph Studio is a specialized IDE that can connect to a LangGraph Server to enable visualization, interaction, and debugging of the application locally.
  * [LangGraph CLI](https://langchain-ai.github.io/langgraph/concepts/langgraph_cli/): LangGraph CLI is a command-line interface that helps to interact with a local LangGraph
  * [Python/JS SDK](https://langchain-ai.github.io/langgraph/concepts/sdk/): The Python/JS SDK provides a programmatic way to interact with deployed LangGraph Applications.
  * [Remote Graph](https://langchain-ai.github.io/langgraph/how-tos/use-remote-graph/): A RemoteGraph allows you to interact with any deployed LangGraph application as though it were running locally.



![](https://langchain-ai.github.io/langgraph/concepts/img/lg_platform.png)

The LangGraph Platform offers a few different deployment options described in the [deployment options guide](https://langchain-ai.github.io/langgraph/concepts/deployment_options/).

## Why Use LangGraph Platform?[¶](https://langchain-ai.github.io/langgraph/concepts/langgraph_platform/#why-use-langgraph-platform "Permanent link")

**LangGraph Platform** handles common issues that arise when deploying LLM applications to production, allowing you to focus on agent logic instead of managing server infrastructure.

  * **[Streaming Support](https://langchain-ai.github.io/langgraph/concepts/streaming/)** : As agents grow more sophisticated, they often benefit from streaming both token outputs and intermediate states back to the user. Without this, users are left waiting for potentially long operations with no feedback. LangGraph Server provides [multiple streaming modes](https://langchain-ai.github.io/langgraph/concepts/streaming/) optimized for various application needs.

  * **Background Runs** : For agents that take longer to process (e.g., hours), maintaining an open connection can be impractical. The LangGraph Server supports launching agent runs in the background and provides both polling endpoints and webhooks to monitor run status effectively.

  * **Support for long runs** : Vanilla server setups often encounter timeouts or disruptions when handling requests that take a long time to complete. LangGraph Server’s API provides robust support for these tasks by sending regular heartbeat signals, preventing unexpected connection closures during prolonged processes.

  * **Handling Burstiness** : Certain applications, especially those with real-time user interaction, may experience "bursty" request loads where numerous requests hit the server simultaneously. LangGraph Server includes a task queue, ensuring requests are handled consistently without loss, even under heavy loads.

  * **[Double Texting](https://langchain-ai.github.io/langgraph/concepts/double_texting/)** : In user-driven applications, it’s common for users to send multiple messages rapidly. This “double texting” can disrupt agent flows if not handled properly. LangGraph Server offers built-in strategies to address and manage such interactions.

  * **[Checkpointers and Memory Management](https://langchain-ai.github.io/langgraph/concepts/persistence/#checkpoints)** : For agents needing persistence (e.g., conversation memory), deploying a robust storage solution can be complex. LangGraph Platform includes optimized [checkpointers](https://langchain-ai.github.io/langgraph/concepts/persistence/#checkpoints) and a [memory store](https://langchain-ai.github.io/langgraph/concepts/persistence/#memory-store), managing state across sessions without the need for custom solutions.

  * **[Human-in-the-loop Support](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/)** : In many applications, users require a way to intervene in agent processes. LangGraph Server provides specialized endpoints for human-in-the-loop scenarios, simplifying the integration of manual oversight into agent workflows.




By using LangGraph Platform, you gain access to a robust, scalable deployment solution that mitigates these challenges, saving you the effort of implementing and maintaining them manually. This allows you to focus more on building effective agent behavior and less on solving deployment infrastructure issues.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Functional API  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/) [ Next  Deployment Options  ](https://langchain-ai.github.io/langgraph/concepts/deployment_options/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/concepts/langgraph_platform/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
