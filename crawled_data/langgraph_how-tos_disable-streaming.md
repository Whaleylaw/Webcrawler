---
url: https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/#how-to-disable-streaming-for-models-that-dont-support-it)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to disable streaming for models that don't support it 

[ ](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/?q= "Share")

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

How-to Guides 
        * LangGraph  LangGraph 
          * [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
          * [ Graph API Basics  ](https://langchain-ai.github.io/langgraph/how-tos#graph-api-basics)
          * [ Controllability  ](https://langchain-ai.github.io/langgraph/how-tos#controllability)
          * [ Persistence  ](https://langchain-ai.github.io/langgraph/how-tos#persistence)
          * [ Memory  ](https://langchain-ai.github.io/langgraph/how-tos#memory)
          * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraph/how-tos#human-in-the-loop)
          * Streaming  Streaming 
            * [ Streaming  ](https://langchain-ai.github.io/langgraph/how-tos#streaming)
            * [ How to stream  ](https://langchain-ai.github.io/langgraph/how-tos/streaming/)
            * [ How to stream LLM tokens from your graph  ](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/)
            * [ How to stream LLM tokens from specific nodes  ](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/)
            * [ How to stream data from within a tool  ](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/)
            * [ How to stream from subgraphs  ](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/)
            * How to disable streaming for models that don't support it  [ How to disable streaming for models that don't support it  ](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/) Table of contents 
              * [ Without disabling streaming  ](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/#without-disabling-streaming)
              * [ Disabling streaming  ](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/#disabling-streaming)
          * [ Tool calling  ](https://langchain-ai.github.io/langgraph/how-tos#tool-calling)
          * [ Subgraphs  ](https://langchain-ai.github.io/langgraph/how-tos#subgraphs)
          * [ Multi-agent  ](https://langchain-ai.github.io/langgraph/how-tos#multi-agent)
          * [ State Management  ](https://langchain-ai.github.io/langgraph/how-tos#state-management)
          * [ Other  ](https://langchain-ai.github.io/langgraph/how-tos#other)
          * [ Prebuilt ReAct Agent  ](https://langchain-ai.github.io/langgraph/how-tos#prebuilt-react-agent)
        * [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph-platform)
      * [ Concepts  ](https://langchain-ai.github.io/langgraph/concepts/)
      * [ Tutorials  ](https://langchain-ai.github.io/langgraph/tutorials/)
    * Resources  Resources 
      * [ Prebuilt Agents  ](https://langchain-ai.github.io/langgraph/prebuilt/)
      * [ Adopters  ](https://langchain-ai.github.io/langgraph/adopters/)
      * [ FAQ  ](https://langchain-ai.github.io/langgraph/concepts/faq/)
      * [ Troubleshooting  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraph/reference/graphs/)



Table of contents 

  * [ Without disabling streaming  ](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/#without-disabling-streaming)
  * [ Disabling streaming  ](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/#disabling-streaming)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Streaming  ](https://langchain-ai.github.io/langgraph/how-tos#streaming)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/disable-streaming.ipynb "Edit this page")

# How to disable streaming for models that don't support it[¶](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/#how-to-disable-streaming-for-models-that-dont-support-it "Permanent link")

Prerequisites

This guide assumes familiarity with the following: 

  * [ streaming ](https://python.langchain.com/docs/concepts/#streaming)
  * [ Chat Models ](https://python.langchain.com/docs/concepts/#chat-models/)



Some chat models, including the new O1 models from OpenAI (depending on when you're reading this), do not support streaming. This can lead to issues when using the [astream_events API](https://python.langchain.com/docs/concepts/#astream_events), as it calls models in streaming mode, expecting streaming to function properly.

In this guide, we’ll show you how to disable streaming for models that don’t support it, ensuring they they're never called in streaming mode, even when invoked through the astream_events API.

```
[](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/#__codelineno-0-1)fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/#__codelineno-0-2)fromlanggraph.graphimport MessagesState
[](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/#__codelineno-0-3)fromlanggraph.graphimport StateGraph, START, END
[](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/#__codelineno-0-4)
[](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/#__codelineno-0-5)llm = ChatOpenAI(model="o1-preview", temperature=1)
[](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/#__codelineno-0-6)
[](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/#__codelineno-0-7)graph_builder = StateGraph(MessagesState)
[](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/#__codelineno-0-8)
[](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/#__codelineno-0-9)
[](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/#__codelineno-0-10)defchatbot(state: MessagesState):
[](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/#__codelineno-0-11)  return {"messages": [llm.invoke(state["messages"])]}
[](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/#__codelineno-0-12)
[](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/#__codelineno-0-13)
[](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/#__codelineno-0-14)graph_builder.add_node("chatbot", chatbot)
[](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/#__codelineno-0-15)graph_builder.add_edge(START, "chatbot")
[](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/#__codelineno-0-16)graph_builder.add_edge("chatbot", END)
[](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/#__codelineno-0-17)graph = graph_builder.compile()

```


API Reference: [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END)

```
[](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/#__codelineno-1-1)fromIPython.displayimport Image, display
[](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/#__codelineno-1-2)
[](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/#__codelineno-1-3)display(Image(graph.get_graph().draw_mermaid_png()))

```


![]()

## Without disabling streaming[¶](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/#without-disabling-streaming "Permanent link")

Now that we've defined our graph, let's try to call `astream_events` without disabling streaming. This should throw an error because the `o1` model does not support streaming natively:

```
[](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/#__codelineno-2-1)input = {"messages": {"role": "user", "content": "how many r's are in strawberry?"}}
[](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/#__codelineno-2-2)try:
[](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/#__codelineno-2-3)  async for event in graph.astream_events(input, version="v2"):
[](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/#__codelineno-2-4)    if event["event"] == "on_chat_model_end":
[](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/#__codelineno-2-5)      print(event["data"]["output"].content, end="", flush=True)
[](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/#__codelineno-2-6)except:
[](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/#__codelineno-2-7)  print("Streaming not supported!")

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/#__codelineno-3-1)Streaming not supported!

```


An error occurred as we expected, luckily there is an easy fix! 

## Disabling streaming[¶](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/#disabling-streaming "Permanent link")

Now without making any changes to our graph, let's set the [disable_streaming](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel.disable_streaming) parameter on our model to be `True` which will solve the problem:

```
[](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/#__codelineno-4-1)llm = ChatOpenAI(model="o1-preview", temperature=1, disable_streaming=True)
[](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/#__codelineno-4-2)
[](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/#__codelineno-4-3)graph_builder = StateGraph(MessagesState)
[](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/#__codelineno-4-4)
[](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/#__codelineno-4-5)
[](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/#__codelineno-4-6)defchatbot(state: MessagesState):
[](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/#__codelineno-4-7)  return {"messages": [llm.invoke(state["messages"])]}
[](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/#__codelineno-4-8)
[](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/#__codelineno-4-9)
[](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/#__codelineno-4-10)graph_builder.add_node("chatbot", chatbot)
[](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/#__codelineno-4-11)graph_builder.add_edge(START, "chatbot")
[](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/#__codelineno-4-12)graph_builder.add_edge("chatbot", END)
[](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/#__codelineno-4-13)graph = graph_builder.compile()

```


And now, rerunning with the same input, we should see no errors:

```
[](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/#__codelineno-5-1)input = {"messages": {"role": "user", "content": "how many r's are in strawberry?"}}
[](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/#__codelineno-5-2)async for event in graph.astream_events(input, version="v2"):
[](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/#__codelineno-5-3)  if event["event"] == "on_chat_model_end":
[](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/#__codelineno-5-4)    print(event["data"]["output"].content, end="", flush=True)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/#__codelineno-6-1)There are three "r"s in the word "strawberry".

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to stream from subgraphs  ](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/) [ Next  How to call tools using ToolNode  ](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
