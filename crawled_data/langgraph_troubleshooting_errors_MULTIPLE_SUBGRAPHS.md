---
url: https://langchain-ai.github.io/langgraph/troubleshooting/errors/MULTIPLE_SUBGRAPHS/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/MULTIPLE_SUBGRAPHS/#multiple_subgraphs)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

MULTIPLE_SUBGRAPHS 

[ ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/MULTIPLE_SUBGRAPHS/?q= "Share")

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
      * [ Tutorials  ](https://langchain-ai.github.io/langgraph/tutorials/)
    * Resources  Resources 
      * [ Prebuilt Agents  ](https://langchain-ai.github.io/langgraph/prebuilt/)
      * [ Adopters  ](https://langchain-ai.github.io/langgraph/adopters/)
      * [ FAQ  ](https://langchain-ai.github.io/langgraph/concepts/faq/)
      * [ Troubleshooting  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/)

Troubleshooting 
        * [ GRAPH_RECURSION_LIMIT  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/GRAPH_RECURSION_LIMIT/)
        * [ INVALID_CONCURRENT_GRAPH_UPDATE  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/)
        * [ INVALID_GRAPH_NODE_RETURN_VALUE  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_GRAPH_NODE_RETURN_VALUE/)
        * MULTIPLE_SUBGRAPHS  [ MULTIPLE_SUBGRAPHS  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/MULTIPLE_SUBGRAPHS/) Table of contents 
          * [ Troubleshooting  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/MULTIPLE_SUBGRAPHS/#troubleshooting)
        * [ INVALID_CHAT_HISTORY  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_CHAT_HISTORY/)
        * [ INVALID_LICENSE  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_LICENSE/)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraph/reference/graphs/)



Table of contents 

  * [ Troubleshooting  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/MULTIPLE_SUBGRAPHS/#troubleshooting)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Resources  ](https://langchain-ai.github.io/langgraph/prebuilt/)
  3. [ Troubleshooting  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/troubleshooting/errors/MULTIPLE_SUBGRAPHS.md "Edit this page")

# MULTIPLE_SUBGRAPHS[¶](https://langchain-ai.github.io/langgraph/troubleshooting/errors/MULTIPLE_SUBGRAPHS/#multiple_subgraphs "Permanent link")

You are calling subgraphs multiple times within a single LangGraph node with checkpointing enabled for each subgraph.

This is currently not allowed due to internal restrictions on how checkpoint namespacing for subgraphs works.

## Troubleshooting[¶](https://langchain-ai.github.io/langgraph/troubleshooting/errors/MULTIPLE_SUBGRAPHS/#troubleshooting "Permanent link")

The following may help resolve this error:

  * If you don't need to interrupt/resume from a subgraph, pass `checkpointer=False` when compiling it like this: `.compile(checkpointer=False)`
  * Don't imperatively call graphs multiple times in the same node, and instead use the `Send`[](https://langchain-ai.github.io/langgraph/concepts/low_level/#send) API.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  INVALID_GRAPH_NODE_RETURN_VALUE  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_GRAPH_NODE_RETURN_VALUE/) [ Next  INVALID_CHAT_HISTORY  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_CHAT_HISTORY/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/troubleshooting/errors/MULTIPLE_SUBGRAPHS/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
