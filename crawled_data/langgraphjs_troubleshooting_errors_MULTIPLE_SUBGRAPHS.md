---
url: https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/MULTIPLE_SUBGRAPHS/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/MULTIPLE_SUBGRAPHS/#multiple_subgraphs)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

MULTIPLE_SUBGRAPHS 

[ ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/MULTIPLE_SUBGRAPHS/?q= "Share")

Initializing search 

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
      * [ Tutorials  ](https://langchain-ai.github.io/langgraphjs/tutorials/)
    * Resources  Resources 
      * [ Adopters  ](https://langchain-ai.github.io/langgraphjs/adopters/)
      * [ FAQ  ](https://langchain-ai.github.io/langgraphjs/concepts/faq/)
      * [ Troubleshooting  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/)

Troubleshooting 
        * [ Troubleshooting  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/)
        * [ GRAPH_RECURSION_LIMIT  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/GRAPH_RECURSION_LIMIT/)
        * [ INVALID_CONCURRENT_GRAPH_UPDATE  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/)
        * [ INVALID_GRAPH_NODE_RETURN_VALUE  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_GRAPH_NODE_RETURN_VALUE/)
        * MULTIPLE_SUBGRAPHS  [ MULTIPLE_SUBGRAPHS  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/MULTIPLE_SUBGRAPHS/) Table of contents 
          * [ Troubleshooting  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/MULTIPLE_SUBGRAPHS/#troubleshooting)
        * [ UNREACHABLE_NODE  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/UNREACHABLE_NODE/)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraphjs/reference/)
  * [ Versions  ](https://langchain-ai.github.io/langgraphjs/versions/)



Table of contents 

  * [ Troubleshooting  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/MULTIPLE_SUBGRAPHS/#troubleshooting)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Resources  ](https://langchain-ai.github.io/langgraphjs/adopters/)
  3. [ Troubleshooting  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/)



# MULTIPLE_SUBGRAPHS[¶](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/MULTIPLE_SUBGRAPHS/#multiple_subgraphs "Permanent link")

You are calling subgraphs multiple times within a single LangGraph node with checkpointing enabled for each subgraph.

This is currently not allowed due to internal restrictions on how checkpoint namespacing for subgraphs works.

## Troubleshooting[¶](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/MULTIPLE_SUBGRAPHS/#troubleshooting "Permanent link")

The following may help resolve this error:

  * If you don't need to interrupt/resume from a subgraph, pass `checkpointer=false` when compiling it like this: `.compile({ checkpointer: false })`
  * Don't imperatively call graphs multiple times in the same node, and instead use the `Send`[](https://langchain-ai.github.io/langgraphjs/reference/classes/langgraph.Send.html) API.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  INVALID_GRAPH_NODE_RETURN_VALUE  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_GRAPH_NODE_RETURN_VALUE/) [ Next  UNREACHABLE_NODE  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/UNREACHABLE_NODE/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/MULTIPLE_SUBGRAPHS/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
