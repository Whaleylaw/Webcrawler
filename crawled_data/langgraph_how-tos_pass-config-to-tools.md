---
url: https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#how-to-pass-config-to-tools)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to pass config to tools 

[ ](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/?q= "Share")

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
          * [ Streaming  ](https://langchain-ai.github.io/langgraph/how-tos#streaming)
          * Tool calling  Tool calling 
            * [ Tool calling  ](https://langchain-ai.github.io/langgraph/how-tos#tool-calling)
            * [ How to call tools using ToolNode  ](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/)
            * [ How to handle tool calling errors  ](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/)
            * [ How to pass runtime values to tools  ](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/)
            * [ How to update graph state from tools  ](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/)
            * How to pass config to tools  [ How to pass config to tools  ](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#setup)
              * [ Define tools and model  ](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#define-tools-and-model)
              * [ ReAct Agent  ](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#react-agent)
              * [ Use it!  ](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#use-it)
            * [ How to handle large numbers of tools  ](https://langchain-ai.github.io/langgraph/how-tos/many-tools/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#setup)
  * [ Define tools and model  ](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#define-tools-and-model)
  * [ ReAct Agent  ](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#react-agent)
  * [ Use it!  ](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#use-it)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Tool calling  ](https://langchain-ai.github.io/langgraph/how-tos#tool-calling)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/pass-config-to-tools.ipynb "Edit this page")

# How to pass config to tools[¶](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#how-to-pass-config-to-tools "Permanent link")

Prerequisites

This guide assumes familiarity with the following: 

  * [ Runnable Interface ](https://python.langchain.com/docs/concepts/#runnable-interface)
  * [ Tool calling agent ](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#tool-calling-agent)
  * [ Tools ](https://python.langchain.com/docs/concepts/#tools)
  * [ Streaming ](https://langchain-ai.github.io/langgraph/concepts/streaming/)
  * [ Chat Models ](https://python.langchain.com/docs/concepts/#chat-models/)



At runtime, you may need to pass values to a tool, like a user ID, which should be set by the application logic, not controlled by the LLM, for security reasons. The LLM should only manage its intended parameters.

LangChain tools use the `Runnable` interface, where methods like `invoke` accept runtime information through the config argument with a `RunnableConfig` type annotation.

In the following example, we’ll set up an agent with tools to manage a user's favorite pets—adding, reading, and deleting entries—while fixing the user ID through application logic and letting the chat model control other parameters

## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#setup "Permanent link")

First, let's install the required packages and set our API keys

```
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-0-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-0-2)%pip install --quiet -U langgraph langchain_anthropic

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-1-1)importgetpass
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-1-2)importos
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-1-5)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-1-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-1-7)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-1-8)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-1-10)_set_env("ANTHROPIC_API_KEY")

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Define tools and model[¶](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#define-tools-and-model "Permanent link")

Config type annotations

Each tool function can take a `config` argument. In order for the config to be correctly propagated to the function, you MUST always add a `RunnableConfig` type annotation for your `config` argument. For example:

```
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-2-1)defmy_tool(tool_arg: str, config: RunnableConfig):
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-2-2)  ...

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-3-1)fromtypingimport List
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-3-2)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-3-3)fromlangchain_core.toolsimport tool
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-3-4)fromlangchain_core.runnables.configimport RunnableConfig
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-3-5)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-3-6)fromlanggraph.prebuiltimport ToolNode
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-3-7)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-3-8)user_to_pets = {}
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-3-9)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-3-10)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-3-11)@tool(parse_docstring=True)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-3-12)defupdate_favorite_pets(
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-3-13)  # NOTE: config arg does not need to be added to docstring, as we don't want it to be included in the function signature attached to the LLM
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-3-14)  pets: List[str],
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-3-15)  config: RunnableConfig,
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-3-16)) -> None:
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-3-17)"""Add the list of favorite pets.
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-3-18)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-3-19)  Args:
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-3-20)    pets: List of favorite pets to set.
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-3-21)  """
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-3-22)  user_id = config.get("configurable", {}).get("user_id")
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-3-23)  user_to_pets[user_id] = pets
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-3-24)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-3-25)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-3-26)@tool
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-3-27)defdelete_favorite_pets(config: RunnableConfig) -> None:
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-3-28)"""Delete the list of favorite pets."""
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-3-29)  user_id = config.get("configurable", {}).get("user_id")
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-3-30)  if user_id in user_to_pets:
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-3-31)    del user_to_pets[user_id]
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-3-32)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-3-33)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-3-34)@tool
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-3-35)deflist_favorite_pets(config: RunnableConfig) -> None:
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-3-36)"""List favorite pets if asked to."""
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-3-37)  user_id = config.get("configurable", {}).get("user_id")
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-3-38)  return ", ".join(user_to_pets.get(user_id, []))
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-3-39)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-3-40)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-3-41)tools = [update_favorite_pets, delete_favorite_pets, list_favorite_pets]

```


API Reference: [tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html) | [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html) | [ToolNode](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.ToolNode)

We'll be using a small chat model from Anthropic in our example.

```
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-4-1)fromlangchain_anthropicimport ChatAnthropic
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-4-2)fromlanggraph.graphimport StateGraph, MessagesState
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-4-3)fromlanggraph.prebuiltimport ToolNode
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-4-4)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-4-5)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-4-6)model = ChatAnthropic(model="claude-3-5-haiku-latest")

```


API Reference: [ChatAnthropic](https://python.langchain.com/api_reference/anthropic/chat_models/langchain_anthropic.chat_models.ChatAnthropic.html) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [ToolNode](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.ToolNode)

## ReAct Agent[¶](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#react-agent "Permanent link")

Let's set up a graph implementation of the [ReAct agent](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#react-agent). This agent takes some query as input, then repeatedly call tools until it has enough information to resolve the query. We'll be using prebuilt `create_react_agent`[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent) and the Anthropic model with tools we just defined. Note: the tools are automatically added to the model via `model.bind_tools` inside the `create_react_agent` implementation.

```
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-5-1)fromlanggraph.prebuiltimport create_react_agent
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-5-2)fromIPython.displayimport Image, display
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-5-3)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-5-4)graph = create_react_agent(model, tools)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-5-5)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-5-6)try:
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-5-7)  display(Image(graph.get_graph().draw_mermaid_png()))
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-5-8)except Exception:
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-5-9)  # This requires some extra dependencies and is optional
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-5-10)  pass

```


API Reference: [create_react_agent](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent)

![]()

## Use it![¶](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#use-it "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-6-1)fromlangchain_core.messagesimport HumanMessage
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-6-2)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-6-3)user_to_pets.clear() # Clear the state
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-6-4)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-6-5)print(f"User information prior to run: {user_to_pets}")
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-6-6)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-6-7)inputs = {"messages": [HumanMessage(content="my favorite pets are cats and dogs")]}
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-6-8)for chunk in graph.stream(
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-6-9)  inputs, {"configurable": {"user_id": "123"}}, stream_mode="values"
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-6-10)):
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-6-11)  chunk["messages"][-1].pretty_print()
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-6-12)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-6-13)print(f"User information after the run: {user_to_pets}")

```


API Reference: [HumanMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.human.HumanMessage.html)

```
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-7-1)User information prior to run: {}
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-7-2)================================[1m Human Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-7-3)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-7-4)my favorite pets are cats and dogs
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-7-5)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-7-6)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-7-7)[{'text': "I'll help you update your favorite pets using the `update_favorite_pets` function.", 'type': 'text'}, {'id': 'toolu_015jtecJ4jnosAfXEC3KADS2', 'input': {'pets': ['cats', 'dogs']}, 'name': 'update_favorite_pets', 'type': 'tool_use'}]
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-7-8)Tool Calls:
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-7-9) update_favorite_pets (toolu_015jtecJ4jnosAfXEC3KADS2)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-7-10) Call ID: toolu_015jtecJ4jnosAfXEC3KADS2
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-7-11) Args:
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-7-12)  pets: ['cats', 'dogs']
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-7-13)=================================[1m Tool Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-7-14)Name: update_favorite_pets
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-7-15)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-7-16)null
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-7-17)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-7-18)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-7-19)Great! I've added cats and dogs to your list of favorite pets. Would you like to confirm the list or do anything else with it?
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-7-20)User information after the run: {'123': ['cats', 'dogs']}

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-8-1)fromlangchain_core.messagesimport HumanMessage
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-8-2)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-8-3)print(f"User information prior to run: {user_to_pets}")
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-8-4)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-8-5)inputs = {"messages": [HumanMessage(content="what are my favorite pets")]}
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-8-6)for chunk in graph.stream(
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-8-7)  inputs, {"configurable": {"user_id": "123"}}, stream_mode="values"
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-8-8)):
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-8-9)  chunk["messages"][-1].pretty_print()
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-8-10)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-8-11)print(f"User information prior to run: {user_to_pets}")

```


API Reference: [HumanMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.human.HumanMessage.html)

```
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-9-1)User information prior to run: {'123': ['cats', 'dogs']}
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-9-2)================================[1m Human Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-9-3)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-9-4)what are my favorite pets
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-9-5)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-9-6)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-9-7)[{'text': "I'll help you check your favorite pets by using the list_favorite_pets function.", 'type': 'text'}, {'id': 'toolu_01EMTtX5WtKJXMJ4WqXpxPUw', 'input': {}, 'name': 'list_favorite_pets', 'type': 'tool_use'}]
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-9-8)Tool Calls:
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-9-9) list_favorite_pets (toolu_01EMTtX5WtKJXMJ4WqXpxPUw)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-9-10) Call ID: toolu_01EMTtX5WtKJXMJ4WqXpxPUw
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-9-11) Args:
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-9-12)=================================[1m Tool Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-9-13)Name: list_favorite_pets
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-9-14)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-9-15)cats, dogs
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-9-16)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-9-17)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-9-18)Based on the results, your favorite pets are cats and dogs.
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-9-19)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-9-20)Is there anything else you'd like to know about your favorite pets, or would you like to update the list?
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-9-21)User information prior to run: {'123': ['cats', 'dogs']}

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-10-1)print(f"User information prior to run: {user_to_pets}")
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-10-2)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-10-3)inputs = {
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-10-4)  "messages": [
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-10-5)    HumanMessage(content="please forget what i told you about my favorite animals")
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-10-6)  ]
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-10-7)}
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-10-8)for chunk in graph.stream(
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-10-9)  inputs, {"configurable": {"user_id": "123"}}, stream_mode="values"
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-10-10)):
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-10-11)  chunk["messages"][-1].pretty_print()
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-10-12)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-10-13)print(f"User information prior to run: {user_to_pets}")

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-11-1)User information prior to run: {'123': ['cats', 'dogs']}
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-11-2)================================[1m Human Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-11-3)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-11-4)please forget what i told you about my favorite animals
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-11-5)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-11-6)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-11-7)[{'text': "I'll help you delete the list of favorite pets. I'll use the delete_favorite_pets function to remove any previously saved list.", 'type': 'text'}, {'id': 'toolu_01JqpxgxdsDJFMzSLeogoRtG', 'input': {}, 'name': 'delete_favorite_pets', 'type': 'tool_use'}]
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-11-8)Tool Calls:
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-11-9) delete_favorite_pets (toolu_01JqpxgxdsDJFMzSLeogoRtG)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-11-10) Call ID: toolu_01JqpxgxdsDJFMzSLeogoRtG
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-11-11) Args:
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-11-12)=================================[1m Tool Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-11-13)Name: delete_favorite_pets
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-11-14)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-11-15)null
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-11-16)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-11-17)
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-11-18)The list of favorite pets has been deleted. If you'd like to create a new list of favorite pets in the future, just let me know.
[](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__codelineno-11-19)User information prior to run: {}

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to update graph state from tools  ](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/) [ Next  How to handle large numbers of tools  ](https://langchain-ai.github.io/langgraph/how-tos/many-tools/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
