---
url: https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_CHAT_HISTORY/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_CHAT_HISTORY/#invalid_chat_history)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

INVALID_CHAT_HISTORY 

[ ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_CHAT_HISTORY/?q= "Share")

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
        * [ MULTIPLE_SUBGRAPHS  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/MULTIPLE_SUBGRAPHS/)
        * INVALID_CHAT_HISTORY  [ INVALID_CHAT_HISTORY  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_CHAT_HISTORY/) Table of contents 
          * [ Troubleshooting  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_CHAT_HISTORY/#troubleshooting)
        * [ INVALID_LICENSE  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_LICENSE/)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraph/reference/graphs/)



Table of contents 

  * [ Troubleshooting  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_CHAT_HISTORY/#troubleshooting)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Resources  ](https://langchain-ai.github.io/langgraph/prebuilt/)
  3. [ Troubleshooting  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/troubleshooting/errors/INVALID_CHAT_HISTORY.md "Edit this page")

# INVALID_CHAT_HISTORY[¶](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_CHAT_HISTORY/#invalid_chat_history "Permanent link")

This error is raised in the prebuilt [create_react_agent](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent) when the `call_model` graph node receives a malformed list of messages. Specifically, it is malformed when there are `AIMessages` with `tool_calls` (LLM requesting to call a tool) that do not have a corresponding `ToolMessage` (result of a tool invocation to return to the LLM).

There could be a few reasons you're seeing this error:

  1. You manually passed a malformed list of messages when invoking the graph, e.g. `graph.invoke({'messages': [AIMessage(..., tool_calls=[...])]})`
  2. The graph was interrupted before receiving updates from the `tools` node (i.e. a list of ToolMessages) and you invoked it with a an input that is not None or a ToolMessage, e.g. `graph.invoke({'messages': [HumanMessage(...)]}, config)`. This interrupt could have been triggered in one of the following ways:
     * You manually set `interrupt_before = ['tools']` in `create_react_agent`
     * One of the tools raised an error that wasn't handled by the [ToolNode](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.ToolNode) (`"tools"`)



## Troubleshooting[¶](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_CHAT_HISTORY/#troubleshooting "Permanent link")

To resolve this, you can do one of the following:

  1. Don't invoke the graph with a malformed list of messages
  2. In case of an interrupt (manual or due to an error) you can:

     * provide ToolMessages that match existing tool calls and call `graph.invoke({'messages': [ToolMessage(...)]})`. **NOTE** : this will append the messages to the history and run the graph from the START node.
     * manually update the state and resume the graph from the interrupt:

       1. get the list of most recent messages from the graph state with `graph.get_state(config)`
       2. modify the list of messages to either remove unanswered tool calls from AIMessages or add ToolMessages with tool_call_ids that match unanswered tool calls
       3. call `graph.update_state(config, {'messages': ...})` with the modified list of messages
       4. resume the graph, e.g. call `graph.invoke(None, config)`

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  MULTIPLE_SUBGRAPHS  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/MULTIPLE_SUBGRAPHS/) [ Next  INVALID_LICENSE  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_LICENSE/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_CHAT_HISTORY/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
