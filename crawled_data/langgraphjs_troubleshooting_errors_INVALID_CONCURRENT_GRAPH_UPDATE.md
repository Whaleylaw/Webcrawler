---
url: https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/#invalid_concurrent_graph_update)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

INVALID_CONCURRENT_GRAPH_UPDATE 

[ ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/?q= "Share")

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
        * [ GRAPH_RECURSION_LIMIT  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/GRAPH_RECURSION_LIMIT/)
        * INVALID_CONCURRENT_GRAPH_UPDATE  [ INVALID_CONCURRENT_GRAPH_UPDATE  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/) Table of contents 
          * [ Troubleshooting  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/#troubleshooting)
        * [ INVALID_GRAPH_NODE_RETURN_VALUE  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_GRAPH_NODE_RETURN_VALUE/)
        * [ MULTIPLE_SUBGRAPHS  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/MULTIPLE_SUBGRAPHS/)
        * [ UNREACHABLE_NODE  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/UNREACHABLE_NODE/)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraphjs/reference/)
  * [ Versions  ](https://langchain-ai.github.io/langgraphjs/versions/)



Table of contents 

  * [ Troubleshooting  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/#troubleshooting)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Resources  ](https://langchain-ai.github.io/langgraphjs/adopters/)
  3. [ Troubleshooting  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/)



# INVALID_CONCURRENT_GRAPH_UPDATE[¶](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/#invalid_concurrent_graph_update "Permanent link")

A LangGraph `StateGraph`[](https://langchain-ai.github.io/langgraphjs/reference/classes/langgraph.StateGraph.html) received concurrent updates to its state from multiple nodes to a state property that doesn't support it.

One way this can occur is if you are using a [fanout](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/) or other parallel execution in your graph and you have defined a state with a value like this:

```
[](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/#__codelineno-0-1)constStateAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/#__codelineno-0-2)someKey:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/#__codelineno-0-3)});
[](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/#__codelineno-0-4)
[](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/#__codelineno-0-5)constgraph=newStateGraph(StateAnnotation)
[](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/#__codelineno-0-6).addNode(...)
[](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/#__codelineno-0-7)...
[](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/#__codelineno-0-8).compile();

```


If a node in the above graph returns `{ someKey: "someStringValue" }`, this will overwrite the state value for `someKey` with `"someStringValue"`. However, if multiple nodes in e.g. a fanout within a single step return values for `"someKey"`, the graph will throw this error because there is uncertainty around how to update the internal state.

To get around this, you can define a reducer that combines multiple values:

```
[](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/#__codelineno-1-1)constStateAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/#__codelineno-1-2)someKey:Annotation<string[]>({
[](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/#__codelineno-1-3)default:()=>[],
[](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/#__codelineno-1-4)reducer:(a,b)=>a.concat(b),
[](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/#__codelineno-1-5)}),
[](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/#__codelineno-1-6)});

```


This will allow you to define logic that handles the same key returned from multiple nodes executed in parallel.

## Troubleshooting[¶](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/#troubleshooting "Permanent link")

The following may help resolve this error:

  * If your graph executes nodes in parallel, make sure you have defined relevant state keys with a reducer.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  GRAPH_RECURSION_LIMIT  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/GRAPH_RECURSION_LIMIT/) [ Next  INVALID_GRAPH_NODE_RETURN_VALUE  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_GRAPH_NODE_RETURN_VALUE/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
