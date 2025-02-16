---
url: https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/GRAPH_RECURSION_LIMIT/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/GRAPH_RECURSION_LIMIT/#graph_recursion_limit)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

GRAPH_RECURSION_LIMIT 

[ ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/GRAPH_RECURSION_LIMIT/?q= "Share")

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
      * [ Tutorials  ](https://langchain-ai.github.io/langgraphjs/tutorials/)
    * Resources  Resources 
      * [ Adopters  ](https://langchain-ai.github.io/langgraphjs/adopters/)
      * [ FAQ  ](https://langchain-ai.github.io/langgraphjs/concepts/faq/)
      * [ Troubleshooting  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/)

Troubleshooting 
        * [ Troubleshooting  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/)
        * GRAPH_RECURSION_LIMIT  [ GRAPH_RECURSION_LIMIT  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/GRAPH_RECURSION_LIMIT/) Table of contents 
          * [ Troubleshooting  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/GRAPH_RECURSION_LIMIT/#troubleshooting)
        * [ INVALID_CONCURRENT_GRAPH_UPDATE  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/)
        * [ INVALID_GRAPH_NODE_RETURN_VALUE  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_GRAPH_NODE_RETURN_VALUE/)
        * [ MULTIPLE_SUBGRAPHS  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/MULTIPLE_SUBGRAPHS/)
        * [ UNREACHABLE_NODE  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/UNREACHABLE_NODE/)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraphjs/reference/)
  * [ Versions  ](https://langchain-ai.github.io/langgraphjs/versions/)



Table of contents 

  * [ Troubleshooting  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/GRAPH_RECURSION_LIMIT/#troubleshooting)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Resources  ](https://langchain-ai.github.io/langgraphjs/adopters/)
  3. [ Troubleshooting  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/)



# GRAPH_RECURSION_LIMIT[¶](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/GRAPH_RECURSION_LIMIT/#graph_recursion_limit "Permanent link")

Your LangGraph `StateGraph`[](https://langchain-ai.github.io/langgraphjs/reference/classes/langgraph.StateGraph.html) reached the maximum number of steps before hitting a stop condition. This is often due to an infinite loop caused by code like the example below:

```
[](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/GRAPH_RECURSION_LIMIT/#__codelineno-0-1)constgraph=newStateGraph(...)
[](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/GRAPH_RECURSION_LIMIT/#__codelineno-0-2).addNode("a",...)
[](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/GRAPH_RECURSION_LIMIT/#__codelineno-0-3).addNode("b",...)
[](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/GRAPH_RECURSION_LIMIT/#__codelineno-0-4).addEdge("a","b")
[](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/GRAPH_RECURSION_LIMIT/#__codelineno-0-5).addEdge("b","a")
[](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/GRAPH_RECURSION_LIMIT/#__codelineno-0-6)...
[](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/GRAPH_RECURSION_LIMIT/#__codelineno-0-7).compile();

```


However, complex graphs may hit the default limit naturally.

## Troubleshooting[¶](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/GRAPH_RECURSION_LIMIT/#troubleshooting "Permanent link")

  * If you are not expecting your graph to go through many iterations, you likely have a cycle. Check your logic for infinite loops.
  * If you have a complex graph, you can pass in a higher `recursionLimit` value into your `config` object when invoking your graph like this:



```
[](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/GRAPH_RECURSION_LIMIT/#__codelineno-1-1)awaitgraph.invoke({...},{recursionLimit:100});

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  Error reference  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/) [ Next  INVALID_CONCURRENT_GRAPH_UPDATE  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/GRAPH_RECURSION_LIMIT/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
