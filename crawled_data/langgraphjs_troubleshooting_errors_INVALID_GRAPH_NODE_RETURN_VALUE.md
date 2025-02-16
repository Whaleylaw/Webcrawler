---
url: https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_GRAPH_NODE_RETURN_VALUE
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_GRAPH_NODE_RETURN_VALUE/#invalid_graph_node_return_value)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

INVALID_GRAPH_NODE_RETURN_VALUE 

[ ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_GRAPH_NODE_RETURN_VALUE/?q= "Share")

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
        * [ INVALID_CONCURRENT_GRAPH_UPDATE  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/)
        * INVALID_GRAPH_NODE_RETURN_VALUE  [ INVALID_GRAPH_NODE_RETURN_VALUE  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_GRAPH_NODE_RETURN_VALUE/) Table of contents 
          * [ Troubleshooting  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_GRAPH_NODE_RETURN_VALUE/#troubleshooting)
        * [ MULTIPLE_SUBGRAPHS  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/MULTIPLE_SUBGRAPHS/)
        * [ UNREACHABLE_NODE  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/UNREACHABLE_NODE/)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraphjs/reference/)
  * [ Versions  ](https://langchain-ai.github.io/langgraphjs/versions/)



Table of contents 

  * [ Troubleshooting  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_GRAPH_NODE_RETURN_VALUE/#troubleshooting)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Resources  ](https://langchain-ai.github.io/langgraphjs/adopters/)
  3. [ Troubleshooting  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/)



# INVALID_GRAPH_NODE_RETURN_VALUE[¶](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_GRAPH_NODE_RETURN_VALUE/#invalid_graph_node_return_value "Permanent link")

A LangGraph `StateGraph`[](https://langchain-ai.github.io/langgraphjs/reference/classes/langgraph.StateGraph.html) received a non-object return type from a node. Here's an example:

```
[](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_GRAPH_NODE_RETURN_VALUE/#__codelineno-0-1)constStateAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_GRAPH_NODE_RETURN_VALUE/#__codelineno-0-2)someKey:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_GRAPH_NODE_RETURN_VALUE/#__codelineno-0-3)});
[](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_GRAPH_NODE_RETURN_VALUE/#__codelineno-0-4)
[](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_GRAPH_NODE_RETURN_VALUE/#__codelineno-0-5)constgraph=newStateGraph(StateAnnotation)
[](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_GRAPH_NODE_RETURN_VALUE/#__codelineno-0-6).addNode("badNode",async(state)=>{
[](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_GRAPH_NODE_RETURN_VALUE/#__codelineno-0-7)// Should return an empty object, one with a value for "someKey", or undefined
[](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_GRAPH_NODE_RETURN_VALUE/#__codelineno-0-8)return["whoops!"];
[](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_GRAPH_NODE_RETURN_VALUE/#__codelineno-0-9)})
[](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_GRAPH_NODE_RETURN_VALUE/#__codelineno-0-10)...
[](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_GRAPH_NODE_RETURN_VALUE/#__codelineno-0-11).compile();

```


Invoking the above graph will result in an error like this:

```
[](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_GRAPH_NODE_RETURN_VALUE/#__codelineno-1-1)awaitgraph.invoke({someKey:"someval"});

```


```
[](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_GRAPH_NODE_RETURN_VALUE/#__codelineno-2-1)InvalidUpdateError: Expected node "badNode" to return an object, received number
[](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_GRAPH_NODE_RETURN_VALUE/#__codelineno-2-2)
[](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_GRAPH_NODE_RETURN_VALUE/#__codelineno-2-3)Troubleshooting URL: https://js.langchain.com/troubleshooting/errors/INVALID_GRAPH_NODE_RETURN_VALUE

```


Nodes in your graph must return an object containing one or more keys defined in your state.

## Troubleshooting[¶](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_GRAPH_NODE_RETURN_VALUE/#troubleshooting "Permanent link")

The following may help resolve this error:

  * If you have complex logic in your node, make sure all code paths return an appropriate object for your defined state.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  INVALID_CONCURRENT_GRAPH_UPDATE  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/) [ Next  MULTIPLE_SUBGRAPHS  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/MULTIPLE_SUBGRAPHS/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_GRAPH_NODE_RETURN_VALUE/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
