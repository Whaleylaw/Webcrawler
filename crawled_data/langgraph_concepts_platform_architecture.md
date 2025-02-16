---
url: https://langchain-ai.github.io/langgraph/concepts/platform_architecture/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/concepts/platform_architecture/#langgraph-platform-architecture)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

LangGraph Platform Architecture 

[ ](https://langchain-ai.github.io/langgraph/concepts/platform_architecture/?q= "Share")

Type to start searching

[ GitHub  ](https://github.com/langchain-ai/langgraph "Go to repository")

  * [ Home ](https://langchain-ai.github.io/langgraph/)
  * [ API reference ](https://langchain-ai.github.io/langgraph/reference/graphs/)



[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

[ GitHub  ](https://github.com/langchain-ai/langgraph "Go to repository")

  * [ Home  ](https://langchain-ai.github.io/langgraph/)
  * [ API reference  ](https://langchain-ai.github.io/langgraph/reference/graphs/)



Table of contents 

  * [ How we use Postgres  ](https://langchain-ai.github.io/langgraph/concepts/platform_architecture/#how-we-use-postgres)
  * [ How we use Redis  ](https://langchain-ai.github.io/langgraph/concepts/platform_architecture/#how-we-use-redis)
    * [ Communication  ](https://langchain-ai.github.io/langgraph/concepts/platform_architecture/#communication)
    * [ Ephemeral metadata  ](https://langchain-ai.github.io/langgraph/concepts/platform_architecture/#ephemeral-metadata)



[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/concepts/platform_architecture.md "Edit this page")

# LangGraph Platform Architecture[¶](https://langchain-ai.github.io/langgraph/concepts/platform_architecture/#langgraph-platform-architecture "Permanent link")

![](https://langchain-ai.github.io/langgraph/concepts/img/langgraph_platform_deployment_architecture.png)

## How we use Postgres[¶](https://langchain-ai.github.io/langgraph/concepts/platform_architecture/#how-we-use-postgres "Permanent link")

Postgres is the persistence layer for all user and run data in LGP. This stores both checkpoints (see more info [here](https://langchain-ai.github.io/langgraph/concepts/persistence/)) as well as the server resources (threads, runs, assistants and crons).

## How we use Redis[¶](https://langchain-ai.github.io/langgraph/concepts/platform_architecture/#how-we-use-redis "Permanent link")

Redis is used in each LGP deployment as a way for server and queue workers to communicate, and to store ephemeral metadata, more details on both below. No user/run data is stored in Redis.

### Communication[¶](https://langchain-ai.github.io/langgraph/concepts/platform_architecture/#communication "Permanent link")

All runs in LGP are executed by the pool of background workers that are part of each deployment. In order to enable some features for those runs (such as cancellation and output streaming) we need a channel for two-way communication between the server and the worker handling a particular run. We use Redis to organize that communication.

  1. A Redis list is used as a mechanism to wake up a worker as soon as a new run is created. Only a sentinel value is stored in this list, no actual run info. The run information is then retrieved from Postgres by the worker.
  2. A combination of a Redis string and Redis PubSub channel is used for the server to communicate a run cancellation request to the appropriate worker.
  3. A Redis PubSub channel is used by the worker to broadcast streaming output from an agent while the run is being handled. Any open `/stream` request in the server will subscribe to that channel and forward any events to the response as they arrive. No events are stored in Redis at any time.



### Ephemeral metadata[¶](https://langchain-ai.github.io/langgraph/concepts/platform_architecture/#ephemeral-metadata "Permanent link")

Runs in an LGP deployment may be retried for specific failures (currently only for transient Postgres errors encountered during the run). In order to limit the number of retries (currently limited to 3 attempts per run) we record the attempt number in a Redis string when is picked up. This contains no run-specific info other than its ID, and expires after a short delay.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top 

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/concepts/platform_architecture/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
