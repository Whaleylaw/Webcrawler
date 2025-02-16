---
url: https://langchain-ai.github.io/langgraphjs/versions/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/versions/#langgraph-over-time)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

LangGraph Over Time 

[ ](https://langchain-ai.github.io/langgraphjs/versions/?q= "Share")

Type to start searching

[ GitHub  ](https://github.com/langchain-ai/langgraphjs "Go to repository")

  * [ Home ](https://langchain-ai.github.io/langgraphjs/)
  * [ API reference ](https://langchain-ai.github.io/langgraphjs/reference/)
  * [ Versions ](https://langchain-ai.github.io/langgraphjs/versions/)



[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

[ GitHub  ](https://github.com/langchain-ai/langgraphjs "Go to repository")

  * [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  * [ API reference  ](https://langchain-ai.github.io/langgraphjs/reference/)
  * [ Versions  ](https://langchain-ai.github.io/langgraphjs/versions/)

Versions 



Table of contents 

  * [ Version History  ](https://langchain-ai.github.io/langgraphjs/versions/#version-history)
    * [ v0.2.0 (Latest)  ](https://langchain-ai.github.io/langgraphjs/versions/#v020-latest)
    * [ v0.1.0  ](https://langchain-ai.github.io/langgraphjs/versions/#v010)
  * [ Upgrading  ](https://langchain-ai.github.io/langgraphjs/versions/#upgrading)
    * [ Upgrading to v0.2.0  ](https://langchain-ai.github.io/langgraphjs/versions/#upgrading-to-v020)
    * [ Upgrading to v0.1.0  ](https://langchain-ai.github.io/langgraphjs/versions/#upgrading-to-v010)
  * [ Deprecation Notices  ](https://langchain-ai.github.io/langgraphjs/versions/#deprecation-notices)
    * [ MessageGraph  ](https://langchain-ai.github.io/langgraphjs/versions/#messagegraph)
    * [ createFunctionCallingExecutor  ](https://langchain-ai.github.io/langgraphjs/versions/#createfunctioncallingexecutor)
    * [ ToolExecutor  ](https://langchain-ai.github.io/langgraphjs/versions/#toolexecutor)
  * [ Full changelog  ](https://langchain-ai.github.io/langgraphjs/versions/#full-changelog)



# LangGraph Over Time[¶](https://langchain-ai.github.io/langgraphjs/versions/#langgraph-over-time "Permanent link")

As LangGraph.js continues to evolve and improve, breaking changes are sometimes necessary to enhance functionality, performance, or developer experience. This page serves as a guide to the version history of LangGraph.js, documenting significant changes and providing assistance for upgrading between versions.

## Version History[¶](https://langchain-ai.github.io/langgraphjs/versions/#version-history "Permanent link")

### v0.2.0 (Latest)[¶](https://langchain-ai.github.io/langgraphjs/versions/#v020-latest "Permanent link")

  * (Breaking) `@langchain/core`[](https://www.npmjs.com/package/@langchain/core) is now a peer dependency and requires explicit installation.
  * Added support for [dynamic breakpoints](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/).
  * Added support for [separate input and output schema](https://langchain-ai.github.io/langgraphjs/how-tos/input_output_schema/).
  * Allow using an array to specify destination nodes from a conditional edge as shorthand for object.
  * Numerous bugfixes.



### v0.1.0[¶](https://langchain-ai.github.io/langgraphjs/versions/#v010 "Permanent link")

  * (Breaking) Changed checkpoint representations to support namespacing for subgraphs and pending writes.
  * (Breaking) `MessagesState` was changed to `MessagesAnnotation`[](https://langchain-ai.github.io/langgraphjs/reference/variables/langgraph.MessagesAnnotation.html).
  * Added `Annotation`[](https://langchain-ai.github.io/langgraphjs/reference/modules/langgraph.Annotation.html), a more streamlined way to declare state. Removes the need for separate type and channel declarations.
  * Split checkpointer implementations into different libraries for easier inheritance.
  * Major internal architecture refactor to use more robust patterns.
  * Deprecated `MessageGraph` in favor of `StateGraph`[](https://langchain-ai.github.io/langgraphjs/reference/classes/langgraph.StateGraph.html) + `MessagesAnnotation`[](https://langchain-ai.github.io/langgraphjs/reference/variables/langgraph.MessagesAnnotation.html).
  * Numerous bugfixes.



## Upgrading[¶](https://langchain-ai.github.io/langgraphjs/versions/#upgrading "Permanent link")

When upgrading LangGraph.js, please refer to the specific version sections below for detailed instructions on how to adapt your code to the latest changes.

### Upgrading to v0.2.0[¶](https://langchain-ai.github.io/langgraphjs/versions/#upgrading-to-v020 "Permanent link")

  * You will now need to install `@langchain/core` explicitly. See [this page](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/) for more information.



### Upgrading to v0.1.0[¶](https://langchain-ai.github.io/langgraphjs/versions/#upgrading-to-v010 "Permanent link")

  * Old saved checkpoints will no longer be valid, and you will need to update to use a new prebuilt checkpointer.
  * We recommend switching to the new `Annotation` syntax when declaring graph state.



## Deprecation Notices[¶](https://langchain-ai.github.io/langgraphjs/versions/#deprecation-notices "Permanent link")

This section will list any deprecated features or APIs, along with their planned removal dates and recommended alternatives.

#### `MessageGraph`[¶](https://langchain-ai.github.io/langgraphjs/versions/#messagegraph "Permanent link")

Use `MessagesAnnotation`[](https://langchain-ai.github.io/langgraphjs/reference/variables/langgraph.MessagesAnnotation.html) with `StateGraph`[](https://langchain-ai.github.io/langgraphjs/reference/classes/langgraph.StateGraph.html).

#### `createFunctionCallingExecutor`[¶](https://langchain-ai.github.io/langgraphjs/versions/#createfunctioncallingexecutor "Permanent link")

Use `createReactAgent`[](https://langchain-ai.github.io/langgraphjs/reference/functions/langgraph_prebuilt.createReactAgent.html) with a model that supports tool calling.

#### `ToolExecutor`[¶](https://langchain-ai.github.io/langgraphjs/versions/#toolexecutor "Permanent link")

Use `ToolNode`[](https://langchain-ai.github.io/langgraphjs/reference/classes/langgraph_prebuilt.ToolNode.html) instead.

## Full changelog[¶](https://langchain-ai.github.io/langgraphjs/versions/#full-changelog "Permanent link")

For the most up-to-date information on LangGraph.js versions and changes, please refer to our [GitHub repository](https://github.com/langchain-ai/langgraphjs) and [release notes](https://github.com/langchain-ai/langgraphjs/releases).

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  Environment variables  ](https://langchain-ai.github.io/langgraphjs/cloud/reference/env_var/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/versions/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
