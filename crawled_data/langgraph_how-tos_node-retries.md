---
url: https://langchain-ai.github.io/langgraph/how-tos/node-retries/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#how-to-add-node-retry-policies)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to add node retry policies 

[ ](https://langchain-ai.github.io/langgraph/how-tos/node-retries/?q= "Share")

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
          * Controllability  Controllability 
            * [ Controllability  ](https://langchain-ai.github.io/langgraph/how-tos#controllability)
            * [ How to create map-reduce branches for parallel execution  ](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/)
            * [ How to combine control flow and state updates with Command  ](https://langchain-ai.github.io/langgraph/how-tos/command/)
            * [ How to add runtime configuration to your graph  ](https://langchain-ai.github.io/langgraph/how-tos/configuration/)
            * How to add node retry policies  [ How to add node retry policies  ](https://langchain-ai.github.io/langgraph/how-tos/node-retries/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#setup)
              * [ Passing a retry policy to a node  ](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#passing-a-retry-policy-to-a-node)
            * [ How to return state before hitting recursion limit  ](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/)
          * [ Persistence  ](https://langchain-ai.github.io/langgraph/how-tos#persistence)
          * [ Memory  ](https://langchain-ai.github.io/langgraph/how-tos#memory)
          * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraph/how-tos#human-in-the-loop)
          * [ Streaming  ](https://langchain-ai.github.io/langgraph/how-tos#streaming)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#setup)
  * [ Passing a retry policy to a node  ](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#passing-a-retry-policy-to-a-node)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Controllability  ](https://langchain-ai.github.io/langgraph/how-tos#controllability)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/node-retries.ipynb "Edit this page")

# How to add node retry policies[¶](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#how-to-add-node-retry-policies "Permanent link")

Prerequisites

This guide assumes familiarity with the following: 

  * [ LangGraph Glossary ](https://langchain-ai.github.io/langgraph/concepts/low_level/)



There are many use cases where you may wish for your node to have a custom retry policy, for example if you are calling an API, querying a database, or calling an LLM, etc. 

## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#setup "Permanent link")

First, let's install the required packages and set our API keys

```
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-0-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-0-2)%pip install -U langgraph langchain_anthropic langchain_community

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-1-1)importgetpass
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-1-2)importos
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-1-5)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-1-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-1-7)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-1-8)
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-1-10)_set_env("ANTHROPIC_API_KEY")

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

In order to configure the retry policy, you have to pass the `retry` parameter to the [add_node](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph.add_node). The `retry` parameter takes in a `RetryPolicy` named tuple object. Below we instantiate a `RetryPolicy` object with the default parameters:

```
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-2-1)fromlanggraph.pregelimport RetryPolicy
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-2-2)
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-2-3)RetryPolicy()

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-3-1)RetryPolicy(initial_interval=0.5, backoff_factor=2.0, max_interval=128.0, max_attempts=3, jitter=True, retry_on=<function default_retry_on at 0x78b964b89940>)

```


By default, the `retry_on` parameter uses the `default_retry_on` function, which retries on any exception except for the following:

  * `ValueError`
  * `TypeError`
  * `ArithmeticError`
  * `ImportError`
  * `LookupError`
  * `NameError`
  * `SyntaxError`
  * `RuntimeError`
  * `ReferenceError`
  * `StopIteration`
  * `StopAsyncIteration`
  * `OSError`



In addition, for exceptions from popular http request libraries such as `requests` and `httpx` it only retries on 5xx status codes.

## Passing a retry policy to a node[¶](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#passing-a-retry-policy-to-a-node "Permanent link")

Lastly, we can pass `RetryPolicy` objects when we call the [add_node](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph.add_node) function. In the example below we pass two different retry policies to each of our nodes:

```
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-4-1)importoperator
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-4-2)importsqlite3
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-4-3)fromtypingimport Annotated, Sequence
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-4-4)fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-4-5)
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-4-6)fromlangchain_anthropicimport ChatAnthropic
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-4-7)fromlangchain_core.messagesimport BaseMessage
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-4-8)
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-4-9)fromlanggraph.graphimport END, StateGraph, START
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-4-10)fromlangchain_community.utilitiesimport SQLDatabase
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-4-11)fromlangchain_core.messagesimport AIMessage
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-4-12)
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-4-13)db = SQLDatabase.from_uri("sqlite:///:memory:")
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-4-14)
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-4-15)model = ChatAnthropic(model_name="claude-2.1")
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-4-16)
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-4-17)
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-4-18)classAgentState(TypedDict):
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-4-19)  messages: Annotated[Sequence[BaseMessage], operator.add]
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-4-20)
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-4-21)
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-4-22)defquery_database(state):
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-4-23)  query_result = db.run("SELECT * FROM Artist LIMIT 10;")
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-4-24)  return {"messages": [AIMessage(content=query_result)]}
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-4-25)
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-4-26)
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-4-27)defcall_model(state):
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-4-28)  response = model.invoke(state["messages"])
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-4-29)  return {"messages": [response]}
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-4-30)
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-4-31)
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-4-32)# Define a new graph
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-4-33)builder = StateGraph(AgentState)
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-4-34)builder.add_node(
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-4-35)  "query_database",
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-4-36)  query_database,
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-4-37)  retry=RetryPolicy(retry_on=sqlite3.OperationalError),
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-4-38))
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-4-39)builder.add_node("model", call_model, retry=RetryPolicy(max_attempts=5))
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-4-40)builder.add_edge(START, "model")
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-4-41)builder.add_edge("model", "query_database")
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-4-42)builder.add_edge("query_database", END)
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-4-43)
[](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__codelineno-4-44)graph = builder.compile()

```


API Reference: [ChatAnthropic](https://python.langchain.com/api_reference/anthropic/chat_models/langchain_anthropic.chat_models.ChatAnthropic.html) | [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html) | [SQLDatabase](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html) | [AIMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.AIMessage.html) | [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START)

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to add runtime configuration to your graph  ](https://langchain-ai.github.io/langgraph/how-tos/configuration/) [ Next  How to return state before hitting recursion limit  ](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/node-retries/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
