---
url: https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#how-to-add-human-in-the-loop-processes-to-the-prebuilt-react-agent)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to add human-in-the-loop processes to the prebuilt ReAct agent 

[ ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/?q= "Share")

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
          * [ Tool calling  ](https://langchain-ai.github.io/langgraph/how-tos#tool-calling)
          * [ Subgraphs  ](https://langchain-ai.github.io/langgraph/how-tos#subgraphs)
          * [ Multi-agent  ](https://langchain-ai.github.io/langgraph/how-tos#multi-agent)
          * [ State Management  ](https://langchain-ai.github.io/langgraph/how-tos#state-management)
          * [ Other  ](https://langchain-ai.github.io/langgraph/how-tos#other)
          * Prebuilt ReAct Agent  Prebuilt ReAct Agent 
            * [ Prebuilt ReAct Agent  ](https://langchain-ai.github.io/langgraph/how-tos#prebuilt-react-agent)
            * [ How to use the pre-built ReAct agent  ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/)
            * [ How to add thread-level memory to a ReAct Agent  ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/)
            * [ How to add a custom system prompt to the prebuilt ReAct agent  ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-system-prompt/)
            * How to add human-in-the-loop processes to the prebuilt ReAct agent  [ How to add human-in-the-loop processes to the prebuilt ReAct agent  ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#setup)
              * [ Code  ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#code)
              * [ Usage  ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#usage)
            * [ How to return structured output from the prebuilt ReAct agent  ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/)
            * [ How to create a ReAct agent from scratch  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/)
            * [ How to create a ReAct agent from scratch (Functional API)  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#setup)
  * [ Code  ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#code)
  * [ Usage  ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#usage)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Prebuilt ReAct Agent  ](https://langchain-ai.github.io/langgraph/how-tos#prebuilt-react-agent)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/create-react-agent-hitl.ipynb "Edit this page")

# How to add human-in-the-loop processes to the prebuilt ReAct agent[¶](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#how-to-add-human-in-the-loop-processes-to-the-prebuilt-react-agent "Permanent link")

Prerequisites

This guide assumes familiarity with the following: 

  * [ Human-in-the-loop ](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/)
  * [ Agent Architectures ](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/)
  * [ Chat Models ](https://python.langchain.com/docs/concepts/chat_models/)
  * [ Tools ](https://python.langchain.com/docs/concepts/tools/)



This guide will show how to add human-in-the-loop processes to the prebuilt ReAct agent. Please see [this tutorial](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent) for how to get started with the prebuilt ReAct agent

You can add a a breakpoint before tools are called by passing `interrupt_before=["tools"]` to `create_react_agent`. Note that you need to be using a checkpointer for this to work.

## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#setup "Permanent link")

First, let's install the required packages and set our API keys

```
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-0-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-0-2)%pip install -U langgraph langchain-openai

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-1-1)importgetpass
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-1-2)importos
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-1-5)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-1-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-1-7)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-1-8)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-1-10)_set_env("OPENAI_API_KEY")

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Code[¶](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#code "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-2-1)# First we initialize the model we want to use.
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-2-2)fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-2-3)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-2-4)model = ChatOpenAI(model="gpt-4o", temperature=0)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-2-5)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-2-6)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-2-7)# For this tutorial we will use custom tool that returns pre-defined values for weather in two cities (NYC & SF)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-2-8)fromtypingimport Literal
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-2-9)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-2-10)fromlangchain_core.toolsimport tool
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-2-11)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-2-12)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-2-13)@tool
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-2-14)defget_weather(location: str):
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-2-15)"""Use this to get weather information from a given location."""
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-2-16)  if location.lower() in ["nyc", "new york"]:
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-2-17)    return "It might be cloudy in nyc"
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-2-18)  elif location.lower() in ["sf", "san francisco"]:
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-2-19)    return "It's always sunny in sf"
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-2-20)  else:
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-2-21)    raise AssertionError("Unknown Location")
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-2-22)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-2-23)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-2-24)tools = [get_weather]
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-2-25)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-2-26)# We need a checkpointer to enable human-in-the-loop patterns
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-2-27)fromlanggraph.checkpoint.memoryimport MemorySaver
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-2-28)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-2-29)memory = MemorySaver()
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-2-30)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-2-31)# Define the graph
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-2-32)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-2-33)fromlanggraph.prebuiltimport create_react_agent
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-2-34)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-2-35)graph = create_react_agent(
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-2-36)  model, tools=tools, interrupt_before=["tools"], checkpointer=memory
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-2-37))

```


API Reference: [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html) | [tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html) | [MemorySaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.MemorySaver) | [create_react_agent](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent)

## Usage[¶](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#usage "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-3-1)defprint_stream(stream):
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-3-2)"""A utility to pretty print the stream."""
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-3-3)  for s in stream:
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-3-4)    message = s["messages"][-1]
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-3-5)    if isinstance(message, tuple):
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-3-6)      print(message)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-3-7)    else:
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-3-8)      message.pretty_print()

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-4-1)fromlangchain_core.messagesimport HumanMessage
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-4-2)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-4-3)config = {"configurable": {"thread_id": "42"}}
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-4-4)inputs = {"messages": [("user", "what is the weather in SF, CA?")]}
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-4-5)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-4-6)print_stream(graph.stream(inputs, config, stream_mode="values"))

```


API Reference: [HumanMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.human.HumanMessage.html)

```
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-5-1)================================[1m Human Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-5-2)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-5-3)what is the weather in SF, CA?
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-5-4)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-5-5)Tool Calls:
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-5-6) get_weather (call_YjOKDkgMGgUZUpKIasYk1AdK)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-5-7) Call ID: call_YjOKDkgMGgUZUpKIasYk1AdK
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-5-8) Args:
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-5-9)  location: SF, CA

```


We can verify that our graph stopped at the right place: 

```
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-6-1)snapshot = graph.get_state(config)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-6-2)print("Next step: ", snapshot.next)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-7-1)Next step: ('tools',)

```


Now we can either approve or edit the tool call before proceeding to the next node. If we wanted to approve the tool call, we would simply continue streaming the graph with `None` input. If we wanted to edit the tool call we need to update the state to have the correct tool call, and then after the update has been applied we can continue. 

We can try resuming and we will see an error arise:

```
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-8-1)print_stream(graph.stream(None, config, stream_mode="values"))

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-9-1)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-9-2)Tool Calls:
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-9-3) get_weather (call_YjOKDkgMGgUZUpKIasYk1AdK)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-9-4) Call ID: call_YjOKDkgMGgUZUpKIasYk1AdK
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-9-5) Args:
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-9-6)  location: SF, CA
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-9-7)=================================[1m Tool Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-9-8)Name: get_weather
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-9-9)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-9-10)Error: AssertionError('Unknown Location')
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-9-11) Please fix your mistakes.
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-9-12)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-9-13)Tool Calls:
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-9-14) get_weather (call_CLu9ofeBhtWF2oheBspxXkfE)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-9-15) Call ID: call_CLu9ofeBhtWF2oheBspxXkfE
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-9-16) Args:
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-9-17)  location: San Francisco, CA

```


This error arose because our tool argument of "San Francisco, CA" is not a location our tool recognizes. 

Let's show how we would edit the tool call to search for "San Francisco" instead of "San Francisco, CA" - since our tool as written treats "San Francisco, CA" as an unknown location. We will update the state and then resume streaming the graph and should see no errors arise:

```
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-10-1)state = graph.get_state(config)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-10-2)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-10-3)last_message = state.values["messages"][-1]
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-10-4)last_message.tool_calls[0]["args"] = {"location": "San Francisco"}
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-10-5)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-10-6)graph.update_state(config, {"messages": [last_message]})

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-11-1){'configurable': {'thread_id': '42',
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-11-2) 'checkpoint_ns': '',
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-11-3) 'checkpoint_id': '1ef801d1-5b93-6bb9-8004-a088af1f9cec'}}

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-12-1)print_stream(graph.stream(None, config, stream_mode="values"))

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-13-1)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-13-2)Tool Calls:
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-13-3) get_weather (call_CLu9ofeBhtWF2oheBspxXkfE)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-13-4) Call ID: call_CLu9ofeBhtWF2oheBspxXkfE
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-13-5) Args:
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-13-6)  location: San Francisco
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-13-7)=================================[1m Tool Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-13-8)Name: get_weather
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-13-9)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-13-10)It's always sunny in sf
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-13-11)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-13-12)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__codelineno-13-13)The weather in San Francisco is currently sunny.

```


Fantastic! Our graph updated properly to query the weather in San Francisco and got the correct "It's always sunny in sf" response from the tool, and then responded to the user accordingly.  Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to add a custom system prompt to the prebuilt ReAct agent  ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-system-prompt/) [ Next  How to return structured output from the prebuilt ReAct agent  ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
