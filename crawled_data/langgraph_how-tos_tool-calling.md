---
url: https://langchain-ai.github.io/langgraph/how-tos/tool-calling/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#how-to-call-tools-using-toolnode)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to call tools using ToolNode 

[ ](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/?q= "Share")

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
            * How to call tools using ToolNode  [ How to call tools using ToolNode  ](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#setup)
              * [ Define tools  ](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#define-tools)
              * [ Manually call ToolNode  ](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#manually-call-toolnode)
              * [ Using with chat models  ](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#using-with-chat-models)
              * [ ReAct Agent  ](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#react-agent)
            * [ How to handle tool calling errors  ](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/)
            * [ How to pass runtime values to tools  ](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/)
            * [ How to update graph state from tools  ](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/)
            * [ How to pass config to tools  ](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#setup)
  * [ Define tools  ](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#define-tools)
  * [ Manually call ToolNode  ](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#manually-call-toolnode)
  * [ Using with chat models  ](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#using-with-chat-models)
  * [ ReAct Agent  ](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#react-agent)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Tool calling  ](https://langchain-ai.github.io/langgraph/how-tos#tool-calling)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/tool-calling.ipynb "Edit this page")

# How to call tools using ToolNode[¶](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#how-to-call-tools-using-toolnode "Permanent link")

This guide covers how to use LangGraph's prebuilt `ToolNode`[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.ToolNode) for tool calling.

`ToolNode` is a LangChain Runnable that takes graph state (with a list of messages) as input and outputs state update with the result of tool calls. It is designed to work well out-of-box with LangGraph's prebuilt [ReAct agent](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/), but can also work with any `StateGraph` as long as its state has a `messages` key with an appropriate reducer (see `MessagesState`[](https://github.com/langchain-ai/langgraph/blob/e3ef9adac7395e5c0943c22bbc8a4a856b103aa3/libs/langgraph/langgraph/graph/message.py#L150)).

## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#setup "Permanent link")

First, let's install the required packages and set our API keys

```
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-0-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-0-2)%pip install --quiet -U langgraph langchain_anthropic

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-1-1)importgetpass
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-1-2)importos
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-1-5)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-1-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-1-7)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-1-8)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-1-10)_set_env("ANTHROPIC_API_KEY")

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Define tools[¶](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#define-tools "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-2-1)fromlangchain_core.messagesimport AIMessage
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-2-2)fromlangchain_core.toolsimport tool
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-2-3)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-2-4)fromlanggraph.prebuiltimport ToolNode

```


API Reference: [AIMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.AIMessage.html) | [tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html) | [ToolNode](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.ToolNode)

```
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-3-1)@tool
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-3-2)defget_weather(location: str):
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-3-3)"""Call to get the current weather."""
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-3-4)  if location.lower() in ["sf", "san francisco"]:
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-3-5)    return "It's 60 degrees and foggy."
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-3-6)  else:
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-3-7)    return "It's 90 degrees and sunny."
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-3-8)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-3-9)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-3-10)@tool
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-3-11)defget_coolest_cities():
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-3-12)"""Get a list of coolest cities"""
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-3-13)  return "nyc, sf"

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-4-1)tools = [get_weather, get_coolest_cities]
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-4-2)tool_node = ToolNode(tools)

```


## Manually call `ToolNode`[¶](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#manually-call-toolnode "Permanent link")

`ToolNode` operates on graph state with a list of messages. It expects the last message in the list to be an `AIMessage` with `tool_calls` parameter. 

Let's first see how to invoke the tool node manually:

```
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-5-1)message_with_single_tool_call = AIMessage(
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-5-2)  content="",
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-5-3)  tool_calls=[
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-5-4)    {
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-5-5)      "name": "get_weather",
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-5-6)      "args": {"location": "sf"},
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-5-7)      "id": "tool_call_id",
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-5-8)      "type": "tool_call",
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-5-9)    }
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-5-10)  ],
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-5-11))
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-5-12)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-5-13)tool_node.invoke({"messages": [message_with_single_tool_call]})

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-6-1){'messages': [ToolMessage(content="It's 60 degrees and foggy.", name='get_weather', tool_call_id='tool_call_id')]}

```


Note that typically you don't need to create `AIMessage` manually, and it will be automatically generated by any LangChain chat model that supports tool calling.

You can also do parallel tool calling using `ToolNode` if you pass multiple tool calls to `AIMessage`'s `tool_calls` parameter:

```
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-7-1)message_with_multiple_tool_calls = AIMessage(
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-7-2)  content="",
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-7-3)  tool_calls=[
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-7-4)    {
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-7-5)      "name": "get_coolest_cities",
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-7-6)      "args": {},
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-7-7)      "id": "tool_call_id_1",
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-7-8)      "type": "tool_call",
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-7-9)    },
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-7-10)    {
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-7-11)      "name": "get_weather",
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-7-12)      "args": {"location": "sf"},
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-7-13)      "id": "tool_call_id_2",
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-7-14)      "type": "tool_call",
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-7-15)    },
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-7-16)  ],
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-7-17))
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-7-18)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-7-19)tool_node.invoke({"messages": [message_with_multiple_tool_calls]})

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-8-1){'messages': [ToolMessage(content='nyc, sf', name='get_coolest_cities', tool_call_id='tool_call_id_1'),
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-8-2) ToolMessage(content="It's 60 degrees and foggy.", name='get_weather', tool_call_id='tool_call_id_2')]}

```


## Using with chat models[¶](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#using-with-chat-models "Permanent link")

We'll be using a small chat model from Anthropic in our example. To use chat models with tool calling, we need to first ensure that the model is aware of the available tools. We do this by calling `.bind_tools` method on `ChatAnthropic` model

```
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-9-1)fromtypingimport Literal
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-9-2)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-9-3)fromlangchain_anthropicimport ChatAnthropic
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-9-4)fromlanggraph.graphimport StateGraph, MessagesState
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-9-5)fromlanggraph.prebuiltimport ToolNode
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-9-6)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-9-7)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-9-8)model_with_tools = ChatAnthropic(
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-9-9)  model="claude-3-haiku-20240307", temperature=0
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-9-10)).bind_tools(tools)

```


API Reference: [ChatAnthropic](https://python.langchain.com/api_reference/anthropic/chat_models/langchain_anthropic.chat_models.ChatAnthropic.html) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [ToolNode](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.ToolNode)

```
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-10-1)model_with_tools.invoke("what's the weather in sf?").tool_calls

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-11-1)[{'name': 'get_weather',
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-11-2) 'args': {'location': 'San Francisco'},
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-11-3) 'id': 'toolu_01Fwm7dg1mcJU43Fkx2pqgm8',
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-11-4) 'type': 'tool_call'}]

```


As you can see, the AI message generated by the chat model already has `tool_calls` populated, so we can just pass it directly to `ToolNode`

```
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-12-1)tool_node.invoke({"messages": [model_with_tools.invoke("what's the weather in sf?")]})

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-13-1){'messages': [ToolMessage(content="It's 60 degrees and foggy.", name='get_weather', tool_call_id='toolu_01LFvAVT3xJMeZS6kbWwBGZK')]}

```


## ReAct Agent[¶](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#react-agent "Permanent link")

Next, let's see how to use `ToolNode` inside a LangGraph graph. Let's set up a graph implementation of the [ReAct agent](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#react-agent). This agent takes some query as input, then repeatedly call tools until it has enough information to resolve the query. We'll be using `ToolNode` and the Anthropic model with tools we just defined

```
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-14-1)fromtypingimport Literal
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-14-2)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-14-3)fromlanggraph.graphimport StateGraph, MessagesState, START, END
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-14-4)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-14-5)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-14-6)defshould_continue(state: MessagesState):
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-14-7)  messages = state["messages"]
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-14-8)  last_message = messages[-1]
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-14-9)  if last_message.tool_calls:
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-14-10)    return "tools"
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-14-11)  return END
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-14-12)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-14-13)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-14-14)defcall_model(state: MessagesState):
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-14-15)  messages = state["messages"]
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-14-16)  response = model_with_tools.invoke(messages)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-14-17)  return {"messages": [response]}
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-14-18)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-14-19)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-14-20)workflow = StateGraph(MessagesState)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-14-21)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-14-22)# Define the two nodes we will cycle between
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-14-23)workflow.add_node("agent", call_model)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-14-24)workflow.add_node("tools", tool_node)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-14-25)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-14-26)workflow.add_edge(START, "agent")
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-14-27)workflow.add_conditional_edges("agent", should_continue, ["tools", END])
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-14-28)workflow.add_edge("tools", "agent")
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-14-29)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-14-30)app = workflow.compile()

```


API Reference: [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END)

```
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-15-1)fromIPython.displayimport Image, display
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-15-2)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-15-3)try:
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-15-4)  display(Image(app.get_graph().draw_mermaid_png()))
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-15-5)except Exception:
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-15-6)  # This requires some extra dependencies and is optional
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-15-7)  pass

```


![]()

Let's try it out!

```
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-16-1)# example with a single tool call
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-16-2)for chunk in app.stream(
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-16-3)  {"messages": [("human", "what's the weather in sf?")]}, stream_mode="values"
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-16-4)):
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-16-5)  chunk["messages"][-1].pretty_print()

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-17-1)================================[1m Human Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-17-2)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-17-3)what's the weather in sf?
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-17-4)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-17-5)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-17-6)[{'text': "Okay, let's check the weather in San Francisco:", 'type': 'text'}, {'id': 'toolu_01LdmBXYeccWKdPrhZSwFCDX', 'input': {'location': 'San Francisco'}, 'name': 'get_weather', 'type': 'tool_use'}]
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-17-7)Tool Calls:
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-17-8) get_weather (toolu_01LdmBXYeccWKdPrhZSwFCDX)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-17-9) Call ID: toolu_01LdmBXYeccWKdPrhZSwFCDX
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-17-10) Args:
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-17-11)  location: San Francisco
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-17-12)=================================[1m Tool Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-17-13)Name: get_weather
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-17-14)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-17-15)It's 60 degrees and foggy.
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-17-16)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-17-17)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-17-18)The weather in San Francisco is currently 60 degrees with foggy conditions.

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-18-1)# example with a multiple tool calls in succession
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-18-2)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-18-3)for chunk in app.stream(
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-18-4)  {"messages": [("human", "what's the weather in the coolest cities?")]},
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-18-5)  stream_mode="values",
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-18-6)):
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-18-7)  chunk["messages"][-1].pretty_print()

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-19-1)================================[1m Human Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-19-2)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-19-3)what's the weather in the coolest cities?
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-19-4)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-19-5)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-19-6)[{'text': "Okay, let's find out the weather in the coolest cities:", 'type': 'text'}, {'id': 'toolu_01LFZUWTccyveBdaSAisMi95', 'input': {}, 'name': 'get_coolest_cities', 'type': 'tool_use'}]
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-19-7)Tool Calls:
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-19-8) get_coolest_cities (toolu_01LFZUWTccyveBdaSAisMi95)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-19-9) Call ID: toolu_01LFZUWTccyveBdaSAisMi95
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-19-10) Args:
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-19-11)=================================[1m Tool Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-19-12)Name: get_coolest_cities
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-19-13)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-19-14)nyc, sf
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-19-15)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-19-16)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-19-17)[{'text': "Now let's get the weather for those cities:", 'type': 'text'}, {'id': 'toolu_01RHPQBhT1u6eDnPqqkGUpsV', 'input': {'location': 'nyc'}, 'name': 'get_weather', 'type': 'tool_use'}]
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-19-18)Tool Calls:
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-19-19) get_weather (toolu_01RHPQBhT1u6eDnPqqkGUpsV)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-19-20) Call ID: toolu_01RHPQBhT1u6eDnPqqkGUpsV
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-19-21) Args:
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-19-22)  location: nyc
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-19-23)=================================[1m Tool Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-19-24)Name: get_weather
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-19-25)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-19-26)It's 90 degrees and sunny.
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-19-27)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-19-28)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-19-29)[{'id': 'toolu_01W5sFGF8PfgYzdY4CqT5c6e', 'input': {'location': 'sf'}, 'name': 'get_weather', 'type': 'tool_use'}]
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-19-30)Tool Calls:
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-19-31) get_weather (toolu_01W5sFGF8PfgYzdY4CqT5c6e)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-19-32) Call ID: toolu_01W5sFGF8PfgYzdY4CqT5c6e
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-19-33) Args:
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-19-34)  location: sf
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-19-35)=================================[1m Tool Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-19-36)Name: get_weather
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-19-37)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-19-38)It's 60 degrees and foggy.
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-19-39)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-19-40)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-19-41)Based on the results, it looks like the weather in the coolest cities is:
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-19-42)- New York City: 90 degrees and sunny
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-19-43)- San Francisco: 60 degrees and foggy
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-19-44)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__codelineno-19-45)So the weather in the coolest cities is a mix of warm and cool temperatures, with some sunny and some foggy conditions.

```


`ToolNode` can also handle errors during tool execution. You can enable / disable this by setting `handle_tool_errors=True` (enabled by default). See our guide on handling errors in `ToolNode` [here](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/) Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to disable streaming for models that don't support it  ](https://langchain-ai.github.io/langgraph/how-tos/disable-streaming/) [ Next  How to handle tool calling errors  ](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
