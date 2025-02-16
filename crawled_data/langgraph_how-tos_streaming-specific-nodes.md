---
url: https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#how-to-stream-llm-tokens-from-specific-nodes)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to stream LLM tokens from specific nodes 

[ ](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/?q= "Share")

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
            * How to stream LLM tokens from specific nodes  [ How to stream LLM tokens from specific nodes  ](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#setup)
              * [ Example  ](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#example)
            * [ How to stream data from within a tool  ](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/)
            * [ How to stream from subgraphs  ](https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/)
            * [ How to disable streaming for models that don't support it  ](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#setup)
  * [ Example  ](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#example)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Streaming  ](https://langchain-ai.github.io/langgraph/how-tos#streaming)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/streaming-specific-nodes.ipynb "Edit this page")

# How to stream LLM tokens from specific nodes[¶](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#how-to-stream-llm-tokens-from-specific-nodes "Permanent link")

Prerequisites

This guide assumes familiarity with the following:

  * [Streaming](https://langchain-ai.github.io/langgraph/concepts/streaming/)
  * [Chat Models](https://python.langchain.com/docs/concepts/chat_models/)



A common use case when [streaming LLM tokens](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens) is to only stream them from specific nodes. To do so, you can use `stream_mode="messages"` and filter the outputs by the `langgraph_node` field in the streamed metadata:

```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-0-1)fromlanggraph.graphimport StateGraph
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-0-2)fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-0-3)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-0-4)model = ChatOpenAI()
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-0-5)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-0-6)defnode_a(state: State):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-0-7)  model.invoke(...)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-0-8)  ...
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-0-9)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-0-10)defnode_b(state: State):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-0-11)  model.invoke(...)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-0-12)  ...
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-0-13)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-0-14)graph = (
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-0-15)  StateGraph(State)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-0-16)  .add_node(node_a)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-0-17)  .add_node(node_b)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-0-18)  ...
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-0-19)  .compile()
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-0-20)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-0-21)for msg, metadata in graph.stream(
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-0-22)  inputs,
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-0-23)  stream_mode="messages"
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-0-24)):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-0-25)  # stream from 'node_a'
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-0-26)  if metadata["langgraph_node"] == "node_a":
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-0-27)    print(msg)

```


API Reference: [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph)

Streaming from a specific LLM invocation

If you need to instead filter streamed LLM tokens to a specific LLM invocation, check out [this guide](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens#filter-to-specific-llm-invocation)

## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#setup "Permanent link")

First we need to install the packages required

```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-1-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-1-2)%pip install --quiet -U langgraph langchain_openai

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-2-1)importgetpass
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-2-2)importos
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-2-3)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-2-4)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-2-5)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-2-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-2-7)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-2-8)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-2-9)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-2-10)_set_env("OPENAI_API_KEY")

```


## Example[¶](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#example "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-3-1)fromtypingimport TypedDict
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-3-2)fromlanggraph.graphimport START, StateGraph, MessagesState
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-3-3)fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-3-4)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-3-5)model = ChatOpenAI(model="gpt-4o-mini")
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-3-6)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-3-7)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-3-8)classState(TypedDict):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-3-9)  topic: str
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-3-10)  joke: str
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-3-11)  poem: str
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-3-12)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-3-13)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-3-14)defwrite_joke(state: State):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-3-15)  topic = state["topic"]
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-3-16)  joke_response = model.invoke(
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-3-17)    [{"role": "user", "content": f"Write a joke about {topic}"}]
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-3-18)  )
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-3-19)  return {"joke": joke_response.content}
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-3-20)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-3-21)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-3-22)defwrite_poem(state: State):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-3-23)  topic = state["topic"]
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-3-24)  poem_response = model.invoke(
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-3-25)    [{"role": "user", "content": f"Write a short poem about {topic}"}]
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-3-26)  )
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-3-27)  return {"poem": poem_response.content}
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-3-28)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-3-29)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-3-30)graph = (
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-3-31)  StateGraph(State)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-3-32)  .add_node(write_joke)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-3-33)  .add_node(write_poem)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-3-34)  # write both the joke and the poem concurrently
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-3-35)  .add_edge(START, "write_joke")
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-3-36)  .add_edge(START, "write_poem")
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-3-37)  .compile()
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-3-38))

```


API Reference: [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph)

```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-4-1)for msg, metadata in graph.stream(
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-4-2)  {"topic": "cats"},
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-4-3)  stream_mode="messages",
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-4-4)):
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-4-5)  if msg.content and metadata["langgraph_node"] == "write_poem":
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-4-6)    print(msg.content, end="|", flush=True)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-5-1)In| shadows| soft|,| they| quietly| creep|,| 
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-5-2)|Wh|isk|ered| wonders|,| in| dreams| they| leap|.| 
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-5-3)|With| eyes| like| lantern|s|,| bright| and| wide|,| 
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-5-4)|Myst|eries| linger| where| they| reside|.| 
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-5-5)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-5-6)|P|aws| that| pat|ter| on| silent| floors|,| 
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-5-7)|Cur|led| in| sun|be|ams|,| they| seek| out| more|.| 
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-5-8)|A| flick| of| a| tail|,| a| leap|,| a| p|ounce|,| 
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-5-9)|In| their| playful| world|,| we| can't| help| but| bounce|.| 
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-5-10)
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-5-11)|Guard|ians| of| secrets|,| with| gentle| grace|,| 
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-5-12)|Each| little| me|ow|,| a| warm| embrace|.| 
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-5-13)|Oh|,| the| joy| that| they| bring|,| so| pure| and| true|,| 
[](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__codelineno-5-14)|In| the| heart| of| a| cat|,| there's| magic| anew|.| |

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to stream LLM tokens from your graph  ](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/) [ Next  How to stream data from within a tool  ](https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/streaming-specific-nodes/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
