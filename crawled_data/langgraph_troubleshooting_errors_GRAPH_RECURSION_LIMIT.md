---
url: https://langchain-ai.github.io/langgraph/troubleshooting/errors/GRAPH_RECURSION_LIMIT/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/GRAPH_RECURSION_LIMIT/#graph_recursion_limit)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

GRAPH_RECURSION_LIMIT 

[ ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/GRAPH_RECURSION_LIMIT/?q= "Share")

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
        * GRAPH_RECURSION_LIMIT  [ GRAPH_RECURSION_LIMIT  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/GRAPH_RECURSION_LIMIT/) Table of contents 
          * [ Troubleshooting  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/GRAPH_RECURSION_LIMIT/#troubleshooting)
        * [ INVALID_CONCURRENT_GRAPH_UPDATE  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/)
        * [ INVALID_GRAPH_NODE_RETURN_VALUE  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_GRAPH_NODE_RETURN_VALUE/)
        * [ MULTIPLE_SUBGRAPHS  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/MULTIPLE_SUBGRAPHS/)
        * [ INVALID_CHAT_HISTORY  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_CHAT_HISTORY/)
        * [ INVALID_LICENSE  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_LICENSE/)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraph/reference/graphs/)



Table of contents 

  * [ Troubleshooting  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/GRAPH_RECURSION_LIMIT/#troubleshooting)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Resources  ](https://langchain-ai.github.io/langgraph/prebuilt/)
  3. [ Troubleshooting  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/troubleshooting/errors/GRAPH_RECURSION_LIMIT.md "Edit this page")

# GRAPH_RECURSION_LIMIT[¶](https://langchain-ai.github.io/langgraph/troubleshooting/errors/GRAPH_RECURSION_LIMIT/#graph_recursion_limit "Permanent link")

Your LangGraph `StateGraph`[](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) reached the maximum number of steps before hitting a stop condition. This is often due to an infinite loop caused by code like the example below:

```
[](https://langchain-ai.github.io/langgraph/troubleshooting/errors/GRAPH_RECURSION_LIMIT/#__codelineno-0-1)classState(TypedDict):
[](https://langchain-ai.github.io/langgraph/troubleshooting/errors/GRAPH_RECURSION_LIMIT/#__codelineno-0-2)  some_key: str
[](https://langchain-ai.github.io/langgraph/troubleshooting/errors/GRAPH_RECURSION_LIMIT/#__codelineno-0-3)
[](https://langchain-ai.github.io/langgraph/troubleshooting/errors/GRAPH_RECURSION_LIMIT/#__codelineno-0-4)builder = StateGraph(State)
[](https://langchain-ai.github.io/langgraph/troubleshooting/errors/GRAPH_RECURSION_LIMIT/#__codelineno-0-5)builder.add_node("a", ...)
[](https://langchain-ai.github.io/langgraph/troubleshooting/errors/GRAPH_RECURSION_LIMIT/#__codelineno-0-6)builder.add_node("b", ...)
[](https://langchain-ai.github.io/langgraph/troubleshooting/errors/GRAPH_RECURSION_LIMIT/#__codelineno-0-7)builder.add_edge("a", "b")
[](https://langchain-ai.github.io/langgraph/troubleshooting/errors/GRAPH_RECURSION_LIMIT/#__codelineno-0-8)builder.add_edge("b", "a")
[](https://langchain-ai.github.io/langgraph/troubleshooting/errors/GRAPH_RECURSION_LIMIT/#__codelineno-0-9)...
[](https://langchain-ai.github.io/langgraph/troubleshooting/errors/GRAPH_RECURSION_LIMIT/#__codelineno-0-10)
[](https://langchain-ai.github.io/langgraph/troubleshooting/errors/GRAPH_RECURSION_LIMIT/#__codelineno-0-11)graph = builder.compile()

```


However, complex graphs may hit the default limit naturally.

## Troubleshooting[¶](https://langchain-ai.github.io/langgraph/troubleshooting/errors/GRAPH_RECURSION_LIMIT/#troubleshooting "Permanent link")

  * If you are not expecting your graph to go through many iterations, you likely have a cycle. Check your logic for infinite loops.
  * If you have a complex graph, you can pass in a higher `recursion_limit` value into your `config` object when invoking your graph like this:



```
[](https://langchain-ai.github.io/langgraph/troubleshooting/errors/GRAPH_RECURSION_LIMIT/#__codelineno-1-1)graph.invoke({...}, {"recursion_limit": 100})

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Troubleshooting  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/) [ Next  INVALID_CONCURRENT_GRAPH_UPDATE  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/troubleshooting/errors/GRAPH_RECURSION_LIMIT/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
