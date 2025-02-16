---
url: https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#how-to-add-multi-turn-conversation-in-a-multi-agent-application)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to add multi-turn conversation in a multi-agent application 

[ ](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/?q= "Share")

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
            * How to add multi-turn conversation in a multi-agent application  [ How to add multi-turn conversation in a multi-agent application  ](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#setup)
              * [ Define agents  ](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#define-agents)
              * [ Test multi-turn conversation  ](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#test-multi-turn-conversation)
            * [ How to build a multi-agent network (functional API)  ](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#setup)
  * [ Define agents  ](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#define-agents)
  * [ Test multi-turn conversation  ](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#test-multi-turn-conversation)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Multi-agent  ](https://langchain-ai.github.io/langgraph/how-tos#multi-agent)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/multi-agent-multi-turn-convo.ipynb "Edit this page")

# How to add multi-turn conversation in a multi-agent application[¶](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#how-to-add-multi-turn-conversation-in-a-multi-agent-application "Permanent link")

Prerequisites

This guide assumes familiarity with the following:

  * [How to implement handoffs between agents](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs)
  * [Multi-agent systems](https://langchain-ai.github.io/langgraph/concepts/multi_agent)
  * [Human-in-the-loop](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop)
  * [Command](https://langchain-ai.github.io/langgraph/concepts/low_level/#command)
  * [LangGraph Glossary](https://langchain-ai.github.io/langgraph/concepts/low_level/)



In this how-to guide, we’ll build an application that allows an end-user to engage in a _multi-turn conversation_ with one or more agents. We'll create a node that uses an `interrupt`[](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.interrupt) to collect user input and routes back to the **active** agent.

The agents will be implemented as nodes in a graph that executes agent steps and determines the next action: 

  1. **Wait for user input** to continue the conversation, or 
  2. **Route to another agent** (or back to itself, such as in a loop) via a [**handoff**](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#handoffs).



```
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-1)defhuman(state: MessagesState) -> Command[Literal["agent", "another_agent"]]:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-2)"""A node for collecting user input."""
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-3)  user_input = interrupt(value="Ready for user input.")
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-4)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-5)  # Determine the active agent.
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-6)  active_agent = ...
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-7)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-8)  ...
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-9)  return Command(
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-10)    update={
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-11)      "messages": [{
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-12)        "role": "human",
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-13)        "content": user_input,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-14)      }]
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-15)    },
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-16)    goto=active_agent
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-17)  )
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-18)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-19)defagent(state) -> Command[Literal["agent", "another_agent", "human"]]:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-20)  # The condition for routing/halting can be anything, e.g. LLM tool call / structured output, etc.
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-21)  goto = get_next_agent(...) # 'agent' / 'another_agent'
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-22)  if goto:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-23)    return Command(goto=goto, update={"my_state_key": "my_state_value"})
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-24)  else:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-0-25)    return Command(goto="human") # Go to human node

```


## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#setup "Permanent link")

First, let's install the required packages

```
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-1-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-1-2)%pip install -U langgraph langchain-anthropic

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-2-1)importgetpass
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-2-2)importos
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-2-3)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-2-4)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-2-5)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-2-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-2-7)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-2-8)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-2-9)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-2-10)_set_env("ANTHROPIC_API_KEY")

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-3-1)ANTHROPIC_API_KEY: ········

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Define agents[¶](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#define-agents "Permanent link")

In this example, we will build a team of travel assistant agents that can communicate with each other via handoffs.

We will create 2 agents:

  * `travel_advisor`: can help with travel destination recommendations. Can ask `hotel_advisor` for help.
  * `hotel_advisor`: can help with hotel recommendations. Can ask `travel_advisor` for help.



We will be using prebuilt `create_react_agent`[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent) for the agents - each agent will have tools specific to its area of expertise as well as a special [tool for handoffs](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs#implementing-handoffs-using-tools) to another agent.

First, let's define the tools we'll be using:

```
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-1)importrandom
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-2)fromtypingimport Annotated, Literal
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-3)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-4)fromlangchain_core.toolsimport tool
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-5)fromlangchain_core.tools.baseimport InjectedToolCallId
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-6)fromlanggraph.prebuiltimport InjectedState
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-7)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-8)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-9)@tool
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-10)defget_travel_recommendations():
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-11)"""Get recommendation for travel destinations"""
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-12)  return random.choice(["aruba", "turks and caicos"])
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-13)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-14)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-15)@tool
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-16)defget_hotel_recommendations(location: Literal["aruba", "turks and caicos"]):
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-17)"""Get hotel recommendations for a given destination."""
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-18)  return {
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-19)    "aruba": [
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-20)      "The Ritz-Carlton, Aruba (Palm Beach)"
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-21)      "Bucuti & Tara Beach Resort (Eagle Beach)"
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-22)    ],
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-23)    "turks and caicos": ["Grace Bay Club", "COMO Parrot Cay"],
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-24)  }[location]
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-25)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-26)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-27)defmake_handoff_tool(*, agent_name: str):
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-28)"""Create a tool that can return handoff via a Command"""
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-29)  tool_name = f"transfer_to_{agent_name}"
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-30)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-31)  @tool(tool_name)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-32)  defhandoff_to_agent(
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-33)    state: Annotated[dict, InjectedState],
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-34)    tool_call_id: Annotated[str, InjectedToolCallId],
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-35)  ):
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-36)"""Ask another agent for help."""
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-37)    tool_message = {
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-38)      "role": "tool",
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-39)      "content": f"Successfully transferred to {agent_name}",
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-40)      "name": tool_name,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-41)      "tool_call_id": tool_call_id,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-42)    }
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-43)    return Command(
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-44)      # navigate to another agent node in the PARENT graph
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-45)      goto=agent_name,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-46)      graph=Command.PARENT,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-47)      # This is the state update that the agent `agent_name` will see when it is invoked.
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-48)      # We're passing agent's FULL internal message history AND adding a tool message to make sure
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-49)      # the resulting chat history is valid.
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-50)      update={"messages": state["messages"] + [tool_message]},
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-51)    )
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-52)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-4-53)  return handoff_to_agent

```


API Reference: [tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html) | [InjectedToolCallId](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.InjectedToolCallId.html) | [InjectedState](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.InjectedState)

Let's now create our agents using the the prebuilt `create_react_agent`[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent). We'll also define a dedicated `human` node with an `interrupt`[](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.interrupt) -- we will route to this node after the final response from the agents. Note that to do so we're wrapping each agent invocation in a separate node function that returns `Command(goto="human", ...)`.

```
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-1)fromlangchain_anthropicimport ChatAnthropic
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-2)fromlanggraph.graphimport MessagesState, StateGraph, START
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-3)fromlanggraph.prebuiltimport create_react_agent, InjectedState
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-4)fromlanggraph.typesimport Command, interrupt
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-5)fromlanggraph.checkpoint.memoryimport MemorySaver
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-6)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-7)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-8)model = ChatAnthropic(model="claude-3-5-sonnet-latest")
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-9)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-10)# Define travel advisor tools and ReAct agent
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-11)travel_advisor_tools = [
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-12)  get_travel_recommendations,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-13)  make_handoff_tool(agent_name="hotel_advisor"),
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-14)]
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-15)travel_advisor = create_react_agent(
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-16)  model,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-17)  travel_advisor_tools,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-18)  prompt=(
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-19)    "You are a general travel expert that can recommend travel destinations (e.g. countries, cities, etc). "
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-20)    "If you need hotel recommendations, ask 'hotel_advisor' for help. "
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-21)    "You MUST include human-readable response before transferring to another agent."
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-22)  ),
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-23))
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-24)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-25)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-26)defcall_travel_advisor(
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-27)  state: MessagesState,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-28)) -> Command[Literal["hotel_advisor", "human"]]:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-29)  # You can also add additional logic like changing the input to the agent / output from the agent, etc.
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-30)  # NOTE: we're invoking the ReAct agent with the full history of messages in the state
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-31)  response = travel_advisor.invoke(state)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-32)  return Command(update=response, goto="human")
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-33)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-34)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-35)# Define hotel advisor tools and ReAct agent
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-36)hotel_advisor_tools = [
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-37)  get_hotel_recommendations,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-38)  make_handoff_tool(agent_name="travel_advisor"),
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-39)]
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-40)hotel_advisor = create_react_agent(
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-41)  model,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-42)  hotel_advisor_tools,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-43)  prompt=(
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-44)    "You are a hotel expert that can provide hotel recommendations for a given destination. "
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-45)    "If you need help picking travel destinations, ask 'travel_advisor' for help."
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-46)    "You MUST include human-readable response before transferring to another agent."
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-47)  ),
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-48))
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-49)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-50)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-51)defcall_hotel_advisor(
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-52)  state: MessagesState,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-53)) -> Command[Literal["travel_advisor", "human"]]:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-54)  response = hotel_advisor.invoke(state)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-55)  return Command(update=response, goto="human")
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-56)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-57)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-58)defhuman_node(
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-59)  state: MessagesState, config
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-60)) -> Command[Literal["hotel_advisor", "travel_advisor", "human"]]:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-61)"""A node for collecting user input."""
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-62)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-63)  user_input = interrupt(value="Ready for user input.")
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-64)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-65)  # identify the last active agent
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-66)  # (the last active node before returning to human)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-67)  langgraph_triggers = config["metadata"]["langgraph_triggers"]
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-68)  if len(langgraph_triggers) != 1:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-69)    raise AssertionError("Expected exactly 1 trigger in human node")
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-70)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-71)  active_agent = langgraph_triggers[0].split(":")[1]
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-72)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-73)  return Command(
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-74)    update={
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-75)      "messages": [
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-76)        {
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-77)          "role": "human",
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-78)          "content": user_input,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-79)        }
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-80)      ]
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-81)    },
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-82)    goto=active_agent,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-83)  )
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-84)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-85)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-86)builder = StateGraph(MessagesState)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-87)builder.add_node("travel_advisor", call_travel_advisor)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-88)builder.add_node("hotel_advisor", call_hotel_advisor)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-89)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-90)# This adds a node to collect human input, which will route
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-91)# back to the active agent.
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-92)builder.add_node("human", human_node)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-93)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-94)# We'll always start with a general travel advisor.
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-95)builder.add_edge(START, "travel_advisor")
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-96)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-97)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-98)checkpointer = MemorySaver()
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-5-99)graph = builder.compile(checkpointer=checkpointer)

```


API Reference: [ChatAnthropic](https://python.langchain.com/api_reference/anthropic/chat_models/langchain_anthropic.chat_models.ChatAnthropic.html) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [create_react_agent](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent) | [InjectedState](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.InjectedState) | [Command](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Command) | [interrupt](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.interrupt) | [MemorySaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.MemorySaver)

```
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-6-1)fromIPython.displayimport display, Image
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-6-2)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-6-3)display(Image(graph.get_graph().draw_mermaid_png()))

```


![]()

## Test multi-turn conversation[¶](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#test-multi-turn-conversation "Permanent link")

Let's test a multi turn conversation with this application.

```
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-7-1)importuuid
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-7-2)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-7-3)thread_config = {"configurable": {"thread_id": uuid.uuid4()}}
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-7-4)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-7-5)inputs = [
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-7-6)  # 1st round of conversation,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-7-7)  {
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-7-8)    "messages": [
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-7-9)      {"role": "user", "content": "i wanna go somewhere warm in the caribbean"}
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-7-10)    ]
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-7-11)  },
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-7-12)  # Since we're using `interrupt`, we'll need to resume using the Command primitive.
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-7-13)  # 2nd round of conversation,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-7-14)  Command(
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-7-15)    resume="could you recommend a nice hotel in one of the areas and tell me which area it is."
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-7-16)  ),
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-7-17)  # 3rd round of conversation,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-7-18)  Command(
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-7-19)    resume="i like the first one. could you recommend something to do near the hotel?"
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-7-20)  ),
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-7-21)]
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-7-22)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-7-23)for idx, user_input in enumerate(inputs):
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-7-24)  print()
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-7-25)  print(f"--- Conversation Turn {idx+1} ---")
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-7-26)  print()
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-7-27)  print(f"User: {user_input}")
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-7-28)  print()
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-7-29)  for update in graph.stream(
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-7-30)    user_input,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-7-31)    config=thread_config,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-7-32)    stream_mode="updates",
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-7-33)  ):
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-7-34)    for node_id, value in update.items():
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-7-35)      if isinstance(value, dict) and value.get("messages", []):
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-7-36)        last_message = value["messages"][-1]
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-7-37)        if isinstance(last_message, dict) or last_message.type != "ai":
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-7-38)          continue
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-7-39)        print(f"{node_id}: {last_message.content}")

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-1)--- Conversation Turn 1 ---
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-2)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-3)User: {'messages': [{'role': 'user', 'content': 'i wanna go somewhere warm in the caribbean'}]}
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-4)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-5)travel_advisor: Based on the recommendations, I suggest considering Aruba! It's a fantastic Caribbean destination known for its perfect warm weather year-round, with average temperatures around 82°F (28°C). Aruba is famous for its pristine white-sand beaches, crystal-clear waters, and constant cooling trade winds.
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-6)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-7)Some highlights of Aruba include:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-8)1. Beautiful Eagle Beach and Palm Beach
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-9)2. Excellent snorkeling and diving opportunities
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-10)3. Vibrant culture and dining scene
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-11)4. Consistent sunny weather (it's outside the hurricane belt!)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-12)5. Great shopping and nightlife in Oranjestad
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-13)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-14)Would you like me to help you explore more specific aspects of visiting Aruba? Or if you're interested in finding a hotel there, I can connect you with our hotel advisor who can provide detailed accommodation recommendations.
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-15)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-16)--- Conversation Turn 2 ---
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-17)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-18)User: Command(resume='could you recommend a nice hotel in one of the areas and tell me which area it is.')
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-19)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-20)hotel_advisor: Based on the recommendations, I can suggest two excellent options in different areas:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-21)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-22)1. The Ritz-Carlton, Aruba - Located in Palm Beach
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-23)This luxury resort is situated in the bustling Palm Beach area, known for its high-rise hotels and vibrant atmosphere. The Ritz offers world-class amenities, including a luxurious spa, multiple restaurants, and a casino. The location is perfect if you want to be close to shopping, dining, and nightlife.
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-24)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-25)2. Bucuti & Tara Beach Resort - Located in Eagle Beach
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-26)This adults-only boutique resort is situated on the stunning Eagle Beach, which is wider and generally quieter than Palm Beach. It's perfect for those seeking a more peaceful, romantic atmosphere. The resort is known for its exceptional service and sustainability practices.
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-27)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-28)Would you like more specific information about either of these hotels or their locations?
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-29)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-30)--- Conversation Turn 3 ---
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-31)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-32)User: Command(resume='i like the first one. could you recommend something to do near the hotel?')
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-33)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-34)travel_advisor: Near The Ritz-Carlton in Palm Beach, there are several excellent activities you can enjoy:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-35)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-36)1. Palm Beach Strip - Right outside the hotel, you can walk along this vibrant strip featuring:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-37)  - High-end shopping at luxury boutiques
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-38)  - Various restaurants and bars
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-39)  - The Paseo Herencia Shopping & Entertainment Center
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-40)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-41)2. Water Activities (within walking distance):
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-42)  - Snorkeling at the artificial reef
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-43)  - Parasailing
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-44)  - Jet ski rentals
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-45)  - Catamaran sailing trips
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-46)  - Paddleboarding
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-47)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-48)3. Nearby Attractions:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-49)  - Bubali Bird Sanctuary (5-minute drive)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-50)  - Butterfly Farm (10-minute walk)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-51)  - California Lighthouse (short drive)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-52)  - Visit the famous Stellaris Casino (located within the Ritz-Carlton)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-53)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-54)4. Local Culture:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-55)  - Visit the nearby fishing pier
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-56)  - Take a short trip to local craft markets
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-57)  - Evening sunset watching on the beach
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-58)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__codelineno-8-59)Would you like more specific information about any of these activities? I can also recommend some specific restaurants or shopping venues in the area!

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to build a multi-agent network  ](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/) [ Next  How to build a multi-agent network (functional API)  ](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network-functional/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
