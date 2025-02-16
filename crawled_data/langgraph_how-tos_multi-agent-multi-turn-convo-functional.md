---
url: https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#how-to-add-multi-turn-conversation-in-a-multi-agent-application-functional-api)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to add multi-turn conversation in a multi-agent application (functional API) 

[ ](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/?q= "Share")

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
            * [ How to build a multi-agent network (functional API)  ](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/)
            * How to add multi-turn conversation in a multi-agent application (functional API)  [ How to add multi-turn conversation in a multi-agent application (functional API)  ](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#setup)
              * [ Test multi-turn conversation  ](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#test-multi-turn-conversation)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#setup)
  * [ Test multi-turn conversation  ](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#test-multi-turn-conversation)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Multi-agent  ](https://langchain-ai.github.io/langgraph/how-tos#multi-agent)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/multi-agent-multi-turn-convo-functional.ipynb "Edit this page")

# How to add multi-turn conversation in a multi-agent application (functional API)[¶](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#how-to-add-multi-turn-conversation-in-a-multi-agent-application-functional-api "Permanent link")

Prerequisites

This guide assumes familiarity with the following:

  * [Multi-agent systems](https://langchain-ai.github.io/langgraph/concepts/multi_agent)
  * [Human-in-the-loop](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop)
  * [Functional API](https://langchain-ai.github.io/langgraph/concepts/functional_api)
  * [Command](https://langchain-ai.github.io/langgraph/concepts/low_level/#command)
  * [LangGraph Glossary](https://langchain-ai.github.io/langgraph/concepts/low_level/)



In this how-to guide, we’ll build an application that allows an end-user to engage in a _multi-turn conversation_ with one or more agents. We'll create a node that uses an `interrupt`[](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.interrupt) to collect user input and routes back to the **active** agent.

The agents will be implemented as tasks in a workflow that executes agent steps and determines the next action:

  1. **Wait for user input** to continue the conversation, or
  2. **Route to another agent** (or back to itself, such as in a loop) via a [**handoff**](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#handoffs).



```
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-0-1)fromlanggraph.funcimport entrypoint, task
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-0-2)fromlanggraph.prebuiltimport create_react_agent
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-0-3)fromlangchain_core.toolsimport tool
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-0-4)fromlanggraph.typesimport interrupt
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-0-5)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-0-6)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-0-7)# Define a tool to signal intent to hand off to a different agent
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-0-8)# Note: this is not using Command(goto) syntax for navigating to different agents:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-0-9)# `workflow()` below handles the handoffs explicitly
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-0-10)@tool(return_direct=True)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-0-11)deftransfer_to_hotel_advisor():
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-0-12)"""Ask hotel advisor agent for help."""
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-0-13)  return "Successfully transferred to hotel advisor"
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-0-14)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-0-15)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-0-16)# define an agent
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-0-17)travel_advisor_tools = [transfer_to_hotel_advisor, ...]
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-0-18)travel_advisor = create_react_agent(model, travel_advisor_tools)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-0-19)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-0-20)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-0-21)# define a task that calls an agent
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-0-22)@task
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-0-23)defcall_travel_advisor(messages):
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-0-24)  response = travel_advisor.invoke({"messages": messages})
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-0-25)  return response["messages"]
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-0-26)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-0-27)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-0-28)# define the multi-agent network workflow
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-0-29)@entrypoint(checkpointer)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-0-30)defworkflow(messages):
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-0-31)  call_active_agent = call_travel_advisor
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-0-32)  while True:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-0-33)    agent_messages = call_active_agent(messages).result()
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-0-34)    ai_msg = get_last_ai_msg(agent_messages)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-0-35)    if not ai_msg.tool_calls:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-0-36)      user_input = interrupt(value="Ready for user input.")
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-0-37)      messages = messages + [{"role": "user", "content": user_input}]
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-0-38)      continue
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-0-39)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-0-40)    messages = messages + agent_messages
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-0-41)    call_active_agent = get_next_agent(messages)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-0-42)  return entrypoint.final(value=agent_messages[-1], save=messages)

```


API Reference: [tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html) | [entrypoint](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint) | [task](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.task) | [create_react_agent](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent) | [interrupt](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.interrupt)

## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#setup "Permanent link")

First, let's install the required packages

```
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-1-1)# %%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-1-2)# %pip install -U langgraph langchain-anthropic

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-1)importgetpass
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-2)importos
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-3)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-4)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-5)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-7)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-8)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-9)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-2-10)_set_env("ANTHROPIC_API_KEY")

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-3-1)ANTHROPIC_API_KEY: ········

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

In this example we will build a team of travel assistant agents that can communicate with each other.

We will create 2 agents:

  * `travel_advisor`: can help with travel destination recommendations. Can ask `hotel_advisor` for help.
  * `hotel_advisor`: can help with hotel recommendations. Can ask `travel_advisor` for help.



This is a fully-connected network - every agent can talk to any other agent. 

```
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-1)importrandom
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-2)fromtyping_extensionsimport Literal
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-3)fromlangchain_core.toolsimport tool
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-4)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-5)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-6)@tool
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-7)defget_travel_recommendations():
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-8)"""Get recommendation for travel destinations"""
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-9)  return random.choice(["aruba", "turks and caicos"])
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-10)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-11)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-12)@tool
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-13)defget_hotel_recommendations(location: Literal["aruba", "turks and caicos"]):
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-14)"""Get hotel recommendations for a given destination."""
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-15)  return {
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-16)    "aruba": [
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-17)      "The Ritz-Carlton, Aruba (Palm Beach)"
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-18)      "Bucuti & Tara Beach Resort (Eagle Beach)"
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-19)    ],
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-20)    "turks and caicos": ["Grace Bay Club", "COMO Parrot Cay"],
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-21)  }[location]
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-22)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-23)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-24)@tool(return_direct=True)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-25)deftransfer_to_hotel_advisor():
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-26)"""Ask hotel advisor agent for help."""
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-27)  return "Successfully transferred to hotel advisor"
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-28)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-29)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-30)@tool(return_direct=True)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-31)deftransfer_to_travel_advisor():
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-32)"""Ask travel advisor agent for help."""
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-4-33)  return "Successfully transferred to travel advisor"

```


API Reference: [tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html)

Transfer tools

You might have noticed that we're using `@tool(return_direct=True)` in the transfer tools. This is done so that individual agents (e.g., `travel_advisor`) can exit the ReAct loop early once these tools are called. This is the desired behavior, as we want to detect when the agent calls this tool and hand control off _immediately_ to a different agent. 

**NOTE** : This is meant to work with the prebuilt `create_react_agent`[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent) -- if you are building a custom agent, make sure to manually add logic for handling early exit for tools that are marked with `return_direct`.

Let's now create our agents using the the prebuilt `create_react_agent`[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent) and our multi-agent workflow. Note that will be calling `interrupt`[](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.interrupt) every time after we get the final response from each of the agents.

```
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-1)importuuid
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-2)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-3)fromlangchain_core.messagesimport AIMessage
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-4)fromlangchain_anthropicimport ChatAnthropic
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-5)fromlanggraph.prebuiltimport create_react_agent
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-6)fromlanggraph.graphimport add_messages
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-7)fromlanggraph.funcimport entrypoint, task
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-8)fromlanggraph.checkpoint.memoryimport MemorySaver
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-9)fromlanggraph.typesimport interrupt, Command
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-10)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-11)model = ChatAnthropic(model="claude-3-5-sonnet-latest")
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-12)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-13)# Define travel advisor ReAct agent
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-14)travel_advisor_tools = [
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-15)  get_travel_recommendations,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-16)  transfer_to_hotel_advisor,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-17)]
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-18)travel_advisor = create_react_agent(
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-19)  model,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-20)  travel_advisor_tools,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-21)  state_modifier=(
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-22)    "You are a general travel expert that can recommend travel destinations (e.g. countries, cities, etc). "
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-23)    "If you need hotel recommendations, ask 'hotel_advisor' for help. "
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-24)    "You MUST include human-readable response before transferring to another agent."
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-25)  ),
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-26))
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-27)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-28)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-29)@task
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-30)defcall_travel_advisor(messages):
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-31)  # You can also add additional logic like changing the input to the agent / output from the agent, etc.
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-32)  # NOTE: we're invoking the ReAct agent with the full history of messages in the state
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-33)  response = travel_advisor.invoke({"messages": messages})
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-34)  return response["messages"]
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-35)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-36)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-37)# Define hotel advisor ReAct agent
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-38)hotel_advisor_tools = [get_hotel_recommendations, transfer_to_travel_advisor]
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-39)hotel_advisor = create_react_agent(
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-40)  model,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-41)  hotel_advisor_tools,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-42)  state_modifier=(
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-43)    "You are a hotel expert that can provide hotel recommendations for a given destination. "
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-44)    "If you need help picking travel destinations, ask 'travel_advisor' for help."
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-45)    "You MUST include human-readable response before transferring to another agent."
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-46)  ),
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-47))
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-48)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-49)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-50)@task
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-51)defcall_hotel_advisor(messages):
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-52)  response = hotel_advisor.invoke({"messages": messages})
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-53)  return response["messages"]
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-54)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-55)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-56)checkpointer = MemorySaver()
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-57)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-58)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-59)defstring_to_uuid(input_string):
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-60)  return str(uuid.uuid5(uuid.NAMESPACE_URL, input_string))
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-61)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-62)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-63)@entrypoint(checkpointer=checkpointer)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-64)defmulti_turn_graph(messages, previous):
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-65)  previous = previous or []
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-66)  messages = add_messages(previous, messages)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-67)  call_active_agent = call_travel_advisor
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-68)  while True:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-69)    agent_messages = call_active_agent(messages).result()
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-70)    messages = add_messages(messages, agent_messages)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-71)    # Find the last AI message
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-72)    # If one of the handoff tools is called, the last message returned
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-73)    # by the agent will be a ToolMessage because we set them to have
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-74)    # "return_direct=True". This means that the last AIMessage will
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-75)    # have tool calls.
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-76)    # Otherwise, the last returned message will be an AIMessage with
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-77)    # no tool calls, which means we are ready for new input.
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-78)    ai_msg = next(m for m in reversed(agent_messages) if isinstance(m, AIMessage))
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-79)    if not ai_msg.tool_calls:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-80)      user_input = interrupt(value="Ready for user input.")
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-81)      # Add user input as a human message
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-82)      # NOTE: we generate unique ID for the human message based on its content
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-83)      # it's important, since on subsequent invocations previous user input (interrupt) values
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-84)      # will be looked up again and we will attempt to add them again here
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-85)      # `add_messages` deduplicates messages based on the ID, ensuring correct message history
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-86)      human_message = {
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-87)        "role": "user",
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-88)        "content": user_input,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-89)        "id": string_to_uuid(user_input),
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-90)      }
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-91)      messages = add_messages(messages, [human_message])
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-92)      continue
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-93)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-94)    tool_call = ai_msg.tool_calls[-1]
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-95)    if tool_call["name"] == "transfer_to_hotel_advisor":
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-96)      call_active_agent = call_hotel_advisor
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-97)    elif tool_call["name"] == "transfer_to_travel_advisor":
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-98)      call_active_agent = call_travel_advisor
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-99)    else:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-100)      raise ValueError(f"Expected transfer tool, got '{tool_call['name']}'")
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-101)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-5-102)  return entrypoint.final(value=agent_messages[-1], save=messages)

```


API Reference: [AIMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.AIMessage.html) | [ChatAnthropic](https://python.langchain.com/api_reference/anthropic/chat_models/langchain_anthropic.chat_models.ChatAnthropic.html) | [create_react_agent](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent) | [add_messages](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.message.add_messages) | [entrypoint](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint) | [task](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.task) | [MemorySaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.MemorySaver) | [interrupt](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.interrupt) | [Command](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Command)

## Test multi-turn conversation[¶](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#test-multi-turn-conversation "Permanent link")

Let's test a multi turn conversation with this application.

```
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-6-1)thread_config = {"configurable": {"thread_id": uuid.uuid4()}}
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-6-2)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-6-3)inputs = [
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-6-4)  # 1st round of conversation,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-6-5)  {
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-6-6)    "role": "user",
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-6-7)    "content": "i wanna go somewhere warm in the caribbean",
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-6-8)    "id": str(uuid.uuid4()),
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-6-9)  },
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-6-10)  # Since we're using `interrupt`, we'll need to resume using the Command primitive.
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-6-11)  # 2nd round of conversation,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-6-12)  Command(
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-6-13)    resume="could you recommend a nice hotel in one of the areas and tell me which area it is."
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-6-14)  ),
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-6-15)  # 3rd round of conversation,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-6-16)  Command(
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-6-17)    resume="i like the first one. could you recommend something to do near the hotel?"
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-6-18)  ),
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-6-19)]
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-6-20)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-6-21)for idx, user_input in enumerate(inputs):
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-6-22)  print()
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-6-23)  print(f"--- Conversation Turn {idx+1} ---")
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-6-24)  print()
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-6-25)  print(f"User: {user_input}")
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-6-26)  print()
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-6-27)  for update in multi_turn_graph.stream(
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-6-28)    user_input,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-6-29)    config=thread_config,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-6-30)    stream_mode="updates",
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-6-31)  ):
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-6-32)    for node_id, value in update.items():
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-6-33)      if isinstance(value, list) and value:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-6-34)        last_message = value[-1]
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-6-35)        if isinstance(last_message, dict) or last_message.type != "ai":
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-6-36)          continue
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-6-37)        print(f"{node_id}: {last_message.content}")

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-7-1)--- Conversation Turn 1 ---
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-7-2)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-7-3)User: {'role': 'user', 'content': 'i wanna go somewhere warm in the caribbean', 'id': 'f48d82a7-7efa-43f5-ad4c-541758c95f61'}
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-7-4)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-7-5)call_travel_advisor: Based on the recommendations, Aruba would be an excellent choice for your Caribbean getaway! Known as "One Happy Island," Aruba offers:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-7-6)- Year-round warm weather with consistent temperatures around 82°F (28°C)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-7-7)- Beautiful white sand beaches like Eagle Beach and Palm Beach
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-7-8)- Crystal clear waters perfect for swimming and snorkeling
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-7-9)- Minimal rainfall and location outside the hurricane belt
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-7-10)- Rich culture blending Dutch and Caribbean influences
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-7-11)- Various activities from water sports to desert-like landscape exploration
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-7-12)- Excellent dining and shopping options
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-7-13)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-7-14)Would you like me to help you find suitable accommodations in Aruba? I can transfer you to our hotel advisor who can recommend specific hotels based on your preferences.
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-7-15)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-7-16)--- Conversation Turn 2 ---
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-7-17)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-7-18)User: Command(resume='could you recommend a nice hotel in one of the areas and tell me which area it is.')
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-7-19)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-7-20)call_hotel_advisor: I can recommend two excellent options in different areas:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-7-21)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-7-22)1. The Ritz-Carlton, Aruba - Located in Palm Beach
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-7-23)- Luxury beachfront resort
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-7-24)- Located in the vibrant Palm Beach area, known for its lively atmosphere
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-7-25)- Close to restaurants, shopping, and nightlife
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-7-26)- Perfect for those who want a more active vacation with plenty of amenities nearby
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-7-27)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-7-28)2. Bucuti & Tara Beach Resort - Located in Eagle Beach
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-7-29)- Adults-only boutique resort
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-7-30)- Situated on the quieter Eagle Beach
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-7-31)- Known for its romantic atmosphere and excellent service
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-7-32)- Ideal for couples seeking a more peaceful, intimate setting
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-7-33)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-7-34)Would you like more specific information about either of these properties or their locations?
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-7-35)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-7-36)--- Conversation Turn 3 ---
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-7-37)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-7-38)User: Command(resume='i like the first one. could you recommend something to do near the hotel?')
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-7-39)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-7-40)call_travel_advisor: Near The Ritz-Carlton in Palm Beach, here are some popular activities you can enjoy:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-7-41)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-7-42)1. Palm Beach Strip - Take a walk along this bustling strip filled with restaurants, shops, and bars
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-7-43)2. Visit the Bubali Bird Sanctuary - Just a short distance away
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-7-44)3. Try your luck at the Stellaris Casino - Located right in The Ritz-Carlton
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-7-45)4. Water Sports at Palm Beach - Right in front of the hotel you can:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-7-46)  - Go parasailing
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-7-47)  - Try jet skiing
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-7-48)  - Take a sunset sailing cruise
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-7-49)5. Visit the Palm Beach Plaza Mall - High-end shopping just a short walk away
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-7-50)6. Enjoy dinner at Madame Janette's - One of Aruba's most famous restaurants nearby
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-7-51)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__codelineno-7-52)Would you like more specific information about any of these activities or other suggestions in the area?

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to build a multi-agent network (functional API)  ](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/) [ Next  How to use Pydantic model as graph state  ](https://langchain-ai.github.io/langgraph/how-tos/state-model/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
