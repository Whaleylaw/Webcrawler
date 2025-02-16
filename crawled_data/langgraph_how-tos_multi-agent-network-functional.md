---
url: https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#how-to-build-a-multi-agent-network-functional-api)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to build a multi-agent network (functional API) 

[ ](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/?q= "Share")

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
          * Multi-agent  Multi-agent 
            * [ Multi-agent  ](https://langchain-ai.github.io/langgraph/how-tos#multi-agent)
            * [ How to implement handoffs between agents  ](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/)
            * [ How to build a multi-agent network  ](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/)
            * [ How to add multi-turn conversation in a multi-agent application  ](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/)
            * How to build a multi-agent network (functional API)  [ How to build a multi-agent network (functional API)  ](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#setup)
              * [ Travel agent example  ](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#travel-agent-example)
            * [ How to add multi-turn conversation in a multi-agent application (functional API)  ](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#setup)
  * [ Travel agent example  ](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#travel-agent-example)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Multi-agent  ](https://langchain-ai.github.io/langgraph/how-tos#multi-agent)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/multi-agent-network-functional.ipynb "Edit this page")

# How to build a multi-agent network (functional API)[¶](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#how-to-build-a-multi-agent-network-functional-api "Permanent link")

Prerequisites

This guide assumes familiarity with the following:

  * [Multi-agent systems](https://langchain-ai.github.io/langgraph/concepts/multi_agent)
  * [Functional API](https://langchain-ai.github.io/langgraph/concepts/functional_api)
  * [Command](https://langchain-ai.github.io/langgraph/concepts/low_level/#command)
  * [LangGraph Glossary](https://langchain-ai.github.io/langgraph/concepts/low_level/)



In this how-to guide we will demonstrate how to implement a [multi-agent network](https://langchain-ai.github.io/langgraph/concepts/multi_agent#network) architecture where each agent can communicate with every other agent (many-to-many connections) and can decide which agent to call next. We will be using [functional API](https://langchain-ai.github.io/langgraph/concepts/functional_api) — individual agents will be defined as tasks and the agent handoffs will be defined in the main [entrypoint()](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint):

```
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-0-1)fromlanggraph.funcimport entrypoint
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-0-2)fromlanggraph.prebuiltimport create_react_agent
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-0-3)fromlangchain_core.toolsimport tool
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-0-4)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-0-5)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-0-6)# Define a tool to signal intent to hand off to a different agent
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-0-7)@tool(return_direct=True)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-0-8)deftransfer_to_hotel_advisor():
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-0-9)"""Ask hotel advisor agent for help."""
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-0-10)  return "Successfully transferred to hotel advisor"
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-0-11)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-0-12)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-0-13)# define an agent
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-0-14)travel_advisor_tools = [transfer_to_hotel_advisor, ...]
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-0-15)travel_advisor = create_react_agent(model, travel_advisor_tools)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-0-16)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-0-17)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-0-18)# define a task that calls an agent
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-0-19)@task
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-0-20)defcall_travel_advisor(messages):
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-0-21)  response = travel_advisor.invoke({"messages": messages})
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-0-22)  return response["messages"]
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-0-23)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-0-24)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-0-25)# define the multi-agent network workflow
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-0-26)@entrypoint()
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-0-27)defworkflow(messages):
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-0-28)  call_active_agent = call_travel_advisor
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-0-29)  while True:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-0-30)    agent_messages = call_active_agent(messages).result()
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-0-31)    messages = messages + agent_messages
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-0-32)    call_active_agent = get_next_agent(messages)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-0-33)  return messages

```


API Reference: [tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html) | [entrypoint](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint) | [create_react_agent](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent)

## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#setup "Permanent link")

First, let's install the required packages

```
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-1-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-1-2)%pip install -U langgraph langchain-anthropic

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-2-1)importgetpass
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-2-2)importos
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-2-3)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-2-4)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-2-5)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-2-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-2-7)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-2-8)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-2-9)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-2-10)_set_env("ANTHROPIC_API_KEY")

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-3-1)ANTHROPIC_API_KEY: ········

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Travel agent example[¶](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#travel-agent-example "Permanent link")

In this example we will build a team of travel assistant agents that can communicate with each other.

We will create 2 agents:

  * `travel_advisor`: can help with travel destination recommendations. Can ask `hotel_advisor` for help.
  * `hotel_advisor`: can help with hotel recommendations. Can ask `travel_advisor` for help.



This is a fully-connected network - every agent can talk to any other agent. 

First, let's create some of the tools that the agents will be using:

```
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-4-1)importrandom
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-4-2)fromtyping_extensionsimport Literal
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-4-3)fromlangchain_core.toolsimport tool
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-4-4)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-4-5)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-4-6)@tool
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-4-7)defget_travel_recommendations():
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-4-8)"""Get recommendation for travel destinations"""
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-4-9)  return random.choice(["aruba", "turks and caicos"])
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-4-10)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-4-11)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-4-12)@tool
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-4-13)defget_hotel_recommendations(location: Literal["aruba", "turks and caicos"]):
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-4-14)"""Get hotel recommendations for a given destination."""
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-4-15)  return {
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-4-16)    "aruba": [
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-4-17)      "The Ritz-Carlton, Aruba (Palm Beach)"
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-4-18)      "Bucuti & Tara Beach Resort (Eagle Beach)"
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-4-19)    ],
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-4-20)    "turks and caicos": ["Grace Bay Club", "COMO Parrot Cay"],
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-4-21)  }[location]
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-4-22)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-4-23)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-4-24)@tool(return_direct=True)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-4-25)deftransfer_to_hotel_advisor():
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-4-26)"""Ask hotel advisor agent for help."""
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-4-27)  return "Successfully transferred to hotel advisor"
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-4-28)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-4-29)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-4-30)@tool(return_direct=True)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-4-31)deftransfer_to_travel_advisor():
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-4-32)"""Ask travel advisor agent for help."""
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-4-33)  return "Successfully transferred to travel advisor"

```


API Reference: [tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html)

Transfer tools

You might have noticed that we're using `@tool(return_direct=True)` in the transfer tools. This is done so that individual agents (e.g., `travel_advisor`) can exit the ReAct loop early once these tools are called. This is the desired behavior, as we want to detect when the agent calls this tool and hand control off _immediately_ to a different agent. 

**NOTE** : This is meant to work with the prebuilt `create_react_agent`[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent) -- if you are building a custom agent, make sure to manually add logic for handling early exit for tools that are marked with `return_direct`.

Now let's define our agent tasks and combine them into a single multi-agent network workflow:

```
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-1)fromlangchain_core.messagesimport AIMessage
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-2)fromlangchain_anthropicimport ChatAnthropic
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-3)fromlanggraph.prebuiltimport create_react_agent
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-4)fromlanggraph.graphimport add_messages
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-5)fromlanggraph.funcimport entrypoint, task
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-6)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-7)model = ChatAnthropic(model="claude-3-5-sonnet-latest")
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-8)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-9)# Define travel advisor ReAct agent
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-10)travel_advisor_tools = [
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-11)  get_travel_recommendations,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-12)  transfer_to_hotel_advisor,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-13)]
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-14)travel_advisor = create_react_agent(
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-15)  model,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-16)  travel_advisor_tools,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-17)  state_modifier=(
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-18)    "You are a general travel expert that can recommend travel destinations (e.g. countries, cities, etc). "
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-19)    "If you need hotel recommendations, ask 'hotel_advisor' for help. "
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-20)    "You MUST include human-readable response before transferring to another agent."
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-21)  ),
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-22))
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-23)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-24)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-25)@task
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-26)defcall_travel_advisor(messages):
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-27)  # You can also add additional logic like changing the input to the agent / output from the agent, etc.
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-28)  # NOTE: we're invoking the ReAct agent with the full history of messages in the state
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-29)  response = travel_advisor.invoke({"messages": messages})
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-30)  return response["messages"]
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-31)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-32)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-33)# Define hotel advisor ReAct agent
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-34)hotel_advisor_tools = [get_hotel_recommendations, transfer_to_travel_advisor]
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-35)hotel_advisor = create_react_agent(
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-36)  model,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-37)  hotel_advisor_tools,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-38)  state_modifier=(
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-39)    "You are a hotel expert that can provide hotel recommendations for a given destination. "
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-40)    "If you need help picking travel destinations, ask 'travel_advisor' for help."
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-41)    "You MUST include human-readable response before transferring to another agent."
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-42)  ),
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-43))
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-44)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-45)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-46)@task
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-47)defcall_hotel_advisor(messages):
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-48)  response = hotel_advisor.invoke({"messages": messages})
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-49)  return response["messages"]
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-50)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-51)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-52)@entrypoint()
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-53)defworkflow(messages):
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-54)  messages = add_messages([], messages)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-55)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-56)  call_active_agent = call_travel_advisor
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-57)  while True:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-58)    agent_messages = call_active_agent(messages).result()
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-59)    messages = add_messages(messages, agent_messages)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-60)    ai_msg = next(m for m in reversed(agent_messages) if isinstance(m, AIMessage))
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-61)    if not ai_msg.tool_calls:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-62)      break
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-63)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-64)    tool_call = ai_msg.tool_calls[-1]
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-65)    if tool_call["name"] == "transfer_to_travel_advisor":
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-66)      call_active_agent = call_travel_advisor
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-67)    elif tool_call["name"] == "transfer_to_hotel_advisor":
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-68)      call_active_agent = call_hotel_advisor
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-69)    else:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-70)      raise ValueError(f"Expected transfer tool, got '{tool_call['name']}'")
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-71)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-5-72)  return messages

```


API Reference: [AIMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.AIMessage.html) | [ChatAnthropic](https://python.langchain.com/api_reference/anthropic/chat_models/langchain_anthropic.chat_models.ChatAnthropic.html) | [create_react_agent](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent) | [add_messages](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.message.add_messages) | [entrypoint](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint) | [task](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.task)

Lastly, let's define a helper to render the agent outputs:

```
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-6-1)fromlangchain_core.messagesimport convert_to_messages
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-6-2)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-6-3)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-6-4)defpretty_print_messages(update):
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-6-5)  if isinstance(update, tuple):
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-6-6)    ns, update = update
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-6-7)    # skip parent graph updates in the printouts
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-6-8)    if len(ns) == 0:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-6-9)      return
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-6-10)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-6-11)    graph_id = ns[-1].split(":")[0]
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-6-12)    print(f"Update from subgraph {graph_id}:")
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-6-13)    print("\n")
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-6-14)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-6-15)  for node_name, node_update in update.items():
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-6-16)    print(f"Update from node {node_name}:")
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-6-17)    print("\n")
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-6-18)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-6-19)    for m in convert_to_messages(node_update["messages"]):
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-6-20)      m.pretty_print()
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-6-21)    print("\n")

```


API Reference: [convert_to_messages](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.utils.convert_to_messages.html)

Let's test it out using the same input as our original multi-agent system:

```
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-7-1)for chunk in workflow.stream(
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-7-2)  [
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-7-3)    {
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-7-4)      "role": "user",
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-7-5)      "content": "i wanna go somewhere warm in the caribbean. pick one destination and give me hotel recommendations",
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-7-6)    }
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-7-7)  ],
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-7-8)  subgraphs=True,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-7-9)):
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-7-10)  pretty_print_messages(chunk)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-1)Update from subgraph call_travel_advisor:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-2)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-3)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-4)Update from node agent:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-5)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-6)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-7)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-8)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-9)[{'text': "I'll help you find a warm Caribbean destination and then get some hotel recommendations for you.\n\nLet me first get some destination recommendations for the Caribbean region.", 'type': 'text'}, {'id': 'toolu_015vT8PkPq1VXvjrDvSpWUwJ', 'input': {}, 'name': 'get_travel_recommendations', 'type': 'tool_use'}]
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-10)Tool Calls:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-11) get_travel_recommendations (toolu_015vT8PkPq1VXvjrDvSpWUwJ)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-12) Call ID: toolu_015vT8PkPq1VXvjrDvSpWUwJ
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-13) Args:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-14)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-15)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-16)Update from subgraph call_travel_advisor:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-17)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-18)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-19)Update from node tools:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-20)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-21)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-22)=================================[1m Tool Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-23)Name: get_travel_recommendations
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-24)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-25)turks and caicos
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-26)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-27)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-28)Update from subgraph call_travel_advisor:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-29)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-30)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-31)Update from node agent:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-32)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-33)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-34)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-35)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-36)[{'text': "Based on the recommendation, I suggest Turks and Caicos! This beautiful British Overseas Territory is known for its stunning white-sand beaches, crystal-clear turquoise waters, and year-round warm weather. Grace Bay Beach in Providenciales is consistently ranked among the world's best beaches. The islands offer excellent snorkeling, diving, and water sports opportunities, plus a relaxed Caribbean atmosphere.\n\nNow, let me connect you with our hotel advisor to get some specific hotel recommendations for Turks and Caicos.", 'type': 'text'}, {'id': 'toolu_01JY7pNNWFuaWoe9ymxFYiPV', 'input': {}, 'name': 'transfer_to_hotel_advisor', 'type': 'tool_use'}]
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-37)Tool Calls:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-38) transfer_to_hotel_advisor (toolu_01JY7pNNWFuaWoe9ymxFYiPV)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-39) Call ID: toolu_01JY7pNNWFuaWoe9ymxFYiPV
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-40) Args:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-41)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-42)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-43)Update from subgraph call_travel_advisor:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-44)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-45)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-46)Update from node tools:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-47)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-48)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-49)=================================[1m Tool Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-50)Name: transfer_to_hotel_advisor
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-51)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-52)Successfully transferred to hotel advisor
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-53)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-54)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-55)Update from subgraph call_hotel_advisor:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-56)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-57)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-58)Update from node agent:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-59)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-60)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-61)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-62)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-63)[{'text': 'Let me get some hotel recommendations for Turks and Caicos:', 'type': 'text'}, {'id': 'toolu_0129ELa7jFocn16bowaGNapg', 'input': {'location': 'turks and caicos'}, 'name': 'get_hotel_recommendations', 'type': 'tool_use'}]
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-64)Tool Calls:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-65) get_hotel_recommendations (toolu_0129ELa7jFocn16bowaGNapg)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-66) Call ID: toolu_0129ELa7jFocn16bowaGNapg
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-67) Args:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-68)  location: turks and caicos
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-69)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-70)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-71)Update from subgraph call_hotel_advisor:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-72)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-73)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-74)Update from node tools:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-75)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-76)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-77)=================================[1m Tool Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-78)Name: get_hotel_recommendations
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-79)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-80)["Grace Bay Club", "COMO Parrot Cay"]
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-81)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-82)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-83)Update from subgraph call_hotel_advisor:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-84)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-85)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-86)Update from node agent:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-87)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-88)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-89)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-90)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-91)Here are two excellent hotel options in Turks and Caicos:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-92)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-93)1. Grace Bay Club: This luxury resort is located on the world-famous Grace Bay Beach. It offers all-oceanfront suites, exceptional dining options, and personalized service. The resort features adult-only and family-friendly sections, making it perfect for any type of traveler.
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-94)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-95)2. COMO Parrot Cay: This exclusive private island resort offers the ultimate luxury escape. It's known for its pristine beach, world-class spa, and holistic wellness programs. The resort provides an intimate, secluded experience with top-notch amenities and service.
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-96)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__codelineno-8-97)Would you like more specific information about either of these properties or would you like to explore hotels in another destination?

```


Voila - `travel_advisor` picks a destination and then makes a decision to call `hotel_advisor` for more info!  Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to add multi-turn conversation in a multi-agent application  ](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/) [ Next  How to add multi-turn conversation in a multi-agent application (functional API)  ](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
