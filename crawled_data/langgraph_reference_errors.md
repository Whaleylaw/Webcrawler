---
url: https://langchain-ai.github.io/langgraph/reference/errors/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/reference/errors/#errors)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Errors 

[ ](https://langchain-ai.github.io/langgraph/reference/errors/?q= "Share")

Type to start searching

[ GitHub  ](https://github.com/langchain-ai/langgraph "Go to repository")

  * [ Home ](https://langchain-ai.github.io/langgraph/)
  * [ API reference ](https://langchain-ai.github.io/langgraph/reference/graphs/)



[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

[ GitHub  ](https://github.com/langchain-ai/langgraph "Go to repository")

  * [ Home  ](https://langchain-ai.github.io/langgraph/)
  * API reference  API reference 
    * Library  Library 
      * [ Graphs  ](https://langchain-ai.github.io/langgraph/reference/graphs/)
      * [ Checkpointing  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/)
      * [ Storage  ](https://langchain-ai.github.io/langgraph/reference/store/)
      * [ Prebuilt components  ](https://langchain-ai.github.io/langgraph/reference/prebuilt/)
      * [ Channels  ](https://langchain-ai.github.io/langgraph/reference/channels/)
      * Errors  [ Errors  ](https://langchain-ai.github.io/langgraph/reference/errors/) Table of contents 
        * [ GraphRecursionError  ](https://langchain-ai.github.io/langgraph/reference/errors/#langgraph.errors.GraphRecursionError)
        * [ InvalidUpdateError  ](https://langchain-ai.github.io/langgraph/reference/errors/#langgraph.errors.InvalidUpdateError)
        * [ GraphInterrupt  ](https://langchain-ai.github.io/langgraph/reference/errors/#langgraph.errors.GraphInterrupt)
        * [ NodeInterrupt  ](https://langchain-ai.github.io/langgraph/reference/errors/#langgraph.errors.NodeInterrupt)
        * [ GraphDelegate  ](https://langchain-ai.github.io/langgraph/reference/errors/#langgraph.errors.GraphDelegate)
        * [ EmptyInputError  ](https://langchain-ai.github.io/langgraph/reference/errors/#langgraph.errors.EmptyInputError)
        * [ TaskNotFound  ](https://langchain-ai.github.io/langgraph/reference/errors/#langgraph.errors.TaskNotFound)
        * [ CheckpointNotLatest  ](https://langchain-ai.github.io/langgraph/reference/errors/#langgraph.errors.CheckpointNotLatest)
      * [ Types  ](https://langchain-ai.github.io/langgraph/reference/types/)
      * [ Constants  ](https://langchain-ai.github.io/langgraph/reference/constants/)
      * [ Pregel  ](https://langchain-ai.github.io/langgraph/reference/pregel/)
      * [ Config  ](https://langchain-ai.github.io/langgraph/reference/config/)
      * [ Functional API  ](https://langchain-ai.github.io/langgraph/reference/func/)
    * LangGraph Platform  LangGraph Platform 
      * [ Server API  ](https://langchain-ai.github.io/langgraph/cloud/reference/api/api_ref/)
      * [ CLI  ](https://langchain-ai.github.io/langgraph/cloud/reference/cli/)
      * [ SDK (Python)  ](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/)
      * [ SDK (JS/TS)  ](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/)
      * [ RemoteGraph  ](https://langchain-ai.github.io/langgraph/reference/remote_graph/)
      * [ Environment variables  ](https://langchain-ai.github.io/langgraph/cloud/reference/env_var/)



Table of contents 

  * [ GraphRecursionError  ](https://langchain-ai.github.io/langgraph/reference/errors/#langgraph.errors.GraphRecursionError)
  * [ InvalidUpdateError  ](https://langchain-ai.github.io/langgraph/reference/errors/#langgraph.errors.InvalidUpdateError)
  * [ GraphInterrupt  ](https://langchain-ai.github.io/langgraph/reference/errors/#langgraph.errors.GraphInterrupt)
  * [ NodeInterrupt  ](https://langchain-ai.github.io/langgraph/reference/errors/#langgraph.errors.NodeInterrupt)
  * [ GraphDelegate  ](https://langchain-ai.github.io/langgraph/reference/errors/#langgraph.errors.GraphDelegate)
  * [ EmptyInputError  ](https://langchain-ai.github.io/langgraph/reference/errors/#langgraph.errors.EmptyInputError)
  * [ TaskNotFound  ](https://langchain-ai.github.io/langgraph/reference/errors/#langgraph.errors.TaskNotFound)
  * [ CheckpointNotLatest  ](https://langchain-ai.github.io/langgraph/reference/errors/#langgraph.errors.CheckpointNotLatest)



  1. [ API reference  ](https://langchain-ai.github.io/langgraph/reference/graphs/)
  2. [ Library  ](https://langchain-ai.github.io/langgraph/reference/graphs/)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/reference/errors.md "Edit this page")

# Errors[¶](https://langchain-ai.github.io/langgraph/reference/errors/#errors "Permanent link")

##  `GraphRecursionError` [¶](https://langchain-ai.github.io/langgraph/reference/errors/#langgraph.errors.GraphRecursionError "Permanent link")

Bases: `RecursionError`

Raised when the graph has exhausted the maximum number of steps.

This prevents infinite loops. To increase the maximum number of steps, run your graph with a config specifying a higher `recursion_limit`.

Troubleshooting Guides:

  * [GRAPH_RECURSION_LIMIT](https://python.langchain.com/docs/troubleshooting/errors/GRAPH_RECURSION_LIMIT)



Examples:

```
graph = builder.compile()
graph.invoke(
  {"messages": [("user", "Hello, world!")]},
  # The config is the second positional argument
  {"recursion_limit": 1000},
)

```


##  `InvalidUpdateError` [¶](https://langchain-ai.github.io/langgraph/reference/errors/#langgraph.errors.InvalidUpdateError "Permanent link")

Bases: `Exception`

Raised when attempting to update a channel with an invalid set of updates.

Troubleshooting Guides:

  * [INVALID_CONCURRENT_GRAPH_UPDATE](https://python.langchain.com/docs/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE)
  * [INVALID_GRAPH_NODE_RETURN_VALUE](https://python.langchain.com/docs/troubleshooting/errors/INVALID_GRAPH_NODE_RETURN_VALUE)



##  `GraphInterrupt` [¶](https://langchain-ai.github.io/langgraph/reference/errors/#langgraph.errors.GraphInterrupt "Permanent link")

Bases: `GraphBubbleUp`

Raised when a subgraph is interrupted, suppressed by the root graph. Never raised directly, or surfaced to the user.

##  `NodeInterrupt` [¶](https://langchain-ai.github.io/langgraph/reference/errors/#langgraph.errors.NodeInterrupt "Permanent link")

Bases: `GraphInterrupt`

Raised by a node to interrupt execution.

##  `GraphDelegate` [¶](https://langchain-ai.github.io/langgraph/reference/errors/#langgraph.errors.GraphDelegate "Permanent link")

Bases: `GraphBubbleUp`

Raised when a graph is delegated (for distributed mode).

##  `EmptyInputError` [¶](https://langchain-ai.github.io/langgraph/reference/errors/#langgraph.errors.EmptyInputError "Permanent link")

Bases: `Exception`

Raised when graph receives an empty input.

##  `TaskNotFound` [¶](https://langchain-ai.github.io/langgraph/reference/errors/#langgraph.errors.TaskNotFound "Permanent link")

Bases: `Exception`

Raised when the executor is unable to find a task (for distributed mode).

##  `CheckpointNotLatest` [¶](https://langchain-ai.github.io/langgraph/reference/errors/#langgraph.errors.CheckpointNotLatest "Permanent link")

Bases: `Exception`

Raised when the checkpoint is not the latest version (for distributed mode).

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Channels  ](https://langchain-ai.github.io/langgraph/reference/channels/) [ Next  Types  ](https://langchain-ai.github.io/langgraph/reference/types/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/reference/errors/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
