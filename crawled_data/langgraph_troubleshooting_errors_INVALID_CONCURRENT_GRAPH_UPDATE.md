---
url: https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/#invalid_concurrent_graph_update)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

INVALID_CONCURRENT_GRAPH_UPDATE 

[ ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/?q= "Share")

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
        * INVALID_CONCURRENT_GRAPH_UPDATE  [ INVALID_CONCURRENT_GRAPH_UPDATE  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/) Table of contents 
          * [ Troubleshooting  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/#troubleshooting)
        * [ INVALID_GRAPH_NODE_RETURN_VALUE  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_GRAPH_NODE_RETURN_VALUE/)
        * [ MULTIPLE_SUBGRAPHS  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/MULTIPLE_SUBGRAPHS/)
        * [ INVALID_CHAT_HISTORY  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_CHAT_HISTORY/)
        * [ INVALID_LICENSE  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_LICENSE/)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraph/reference/graphs/)



Table of contents 

  * [ Troubleshooting  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/#troubleshooting)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Resources  ](https://langchain-ai.github.io/langgraph/prebuilt/)
  3. [ Troubleshooting  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE.md "Edit this page")

# INVALID_CONCURRENT_GRAPH_UPDATE[¶](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/#invalid_concurrent_graph_update "Permanent link")

A LangGraph `StateGraph`[](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) received concurrent updates to its state from multiple nodes to a state property that doesn't support it.

One way this can occur is if you are using a [fanout](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/) or other parallel execution in your graph and you have defined a graph like this:

```
[](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/#__codelineno-0-1)classState(TypedDict):
[](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/#__codelineno-0-2)  some_key: str
[](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/#__codelineno-0-3)
[](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/#__codelineno-0-4)defnode(state: State):
[](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/#__codelineno-0-5)  return {"some_key": "some_string_value"}
[](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/#__codelineno-0-6)
[](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/#__codelineno-0-7)defother_node(state: State):
[](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/#__codelineno-0-8)  return {"some_key": "some_string_value"}
[](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/#__codelineno-0-9)
[](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/#__codelineno-0-10)
[](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/#__codelineno-0-11)builder = StateGraph(State)
[](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/#__codelineno-0-12)builder.add_node(node)
[](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/#__codelineno-0-13)builder.add_node(other_node)
[](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/#__codelineno-0-14)builder.add_edge(START, "node")
[](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/#__codelineno-0-15)builder.add_edge(START, "other_node")
[](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/#__codelineno-0-16)graph = builder.compile()

```


If a node in the above graph returns `{ "some_key": "some_string_value" }`, this will overwrite the state value for `"some_key"` with `"some_string_value"`. However, if multiple nodes in e.g. a fanout within a single step return values for `"some_key"`, the graph will throw this error because there is uncertainty around how to update the internal state.

To get around this, you can define a reducer that combines multiple values:

```
[](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/#__codelineno-1-1)importoperator
[](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/#__codelineno-1-2)fromtypingimport Annotated
[](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/#__codelineno-1-4)classState(TypedDict):
[](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/#__codelineno-1-5)  # The operator.add reducer fn makes this append-only
[](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/#__codelineno-1-6)  some_key: Annotated[list, operator.add]

```


This will allow you to define logic that handles the same key returned from multiple nodes executed in parallel.

## Troubleshooting[¶](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/#troubleshooting "Permanent link")

The following may help resolve this error:

  * If your graph executes nodes in parallel, make sure you have defined relevant state keys with a reducer.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  GRAPH_RECURSION_LIMIT  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/GRAPH_RECURSION_LIMIT/) [ Next  INVALID_GRAPH_NODE_RETURN_VALUE  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_GRAPH_NODE_RETURN_VALUE/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
