---
url: https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#how-to-build-a-multi-agent-network)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to build a multi-agent network 

[ ](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/?q= "Share")

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
            * How to build a multi-agent network  [ How to build a multi-agent network  ](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#setup)
              * [ Using a custom agent implementation  ](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#using-a-custom-agent-implementation)
              * [ Using with a prebuilt ReAct agent  ](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#using-with-a-prebuilt-react-agent)
            * [ How to add multi-turn conversation in a multi-agent application  ](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#setup)
  * [ Using a custom agent implementation  ](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#using-a-custom-agent-implementation)
  * [ Using with a prebuilt ReAct agent  ](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#using-with-a-prebuilt-react-agent)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Multi-agent  ](https://langchain-ai.github.io/langgraph/how-tos#multi-agent)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/multi-agent-network.ipynb "Edit this page")

# How to build a multi-agent network[¶](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#how-to-build-a-multi-agent-network "Permanent link")

Prerequisites

This guide assumes familiarity with the following:

  * [How to implement handoffs between agents](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs)
  * [Multi-agent systems](https://langchain-ai.github.io/langgraph/concepts/multi_agent)
  * [Command](https://langchain-ai.github.io/langgraph/concepts/low_level/#command)
  * [LangGraph Glossary](https://langchain-ai.github.io/langgraph/concepts/low_level/)



In this how-to guide we will demonstrate how to implement a [multi-agent network](https://langchain-ai.github.io/langgraph/concepts/multi_agent#network) architecture where each agent can communicate with every other agent (many-to-many connections) and can decide which agent to call next. Individual agents will be defined as graph nodes.

To implement communication between the agents, we will be using [handoffs](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs):

```
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-0-1)defagent(state) -> Command[Literal["agent", "another_agent"]]:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-0-2)  # the condition for routing/halting can be anything, e.g. LLM tool call / structured output, etc.
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-0-3)  goto = get_next_agent(...) # 'agent' / 'another_agent'
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-0-4)  return Command(
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-0-5)    # Specify which agent to call next
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-0-6)    goto=goto,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-0-7)    # Update the graph state
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-0-8)    update={"my_state_key": "my_state_value"}
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-0-9)  )

```


## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#setup "Permanent link")

First, let's install the required packages

```
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-1-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-1-2)%pip install -U langgraph langchain-anthropic

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-2-1)importgetpass
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-2-2)importos
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-2-3)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-2-4)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-2-5)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-2-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-2-7)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-2-8)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-2-9)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-2-10)_set_env("ANTHROPIC_API_KEY")

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-3-1)ANTHROPIC_API_KEY: ········

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Using a custom agent implementation[¶](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#using-a-custom-agent-implementation "Permanent link")

In this example we will build a team of travel assistant agents that can communicate with each other via handoffs.

We will create 2 agents:

  * `travel_advisor`: can help with travel destination recommendations. Can ask `hotel_advisor` for help.
  * `hotel_advisor`: can help with hotel recommendations. Can ask `travel_advisor` for help.



This is a fully-connected network - every agent can talk to any other agent. 

Each agent will have a corresponding node function that can conditionally return a `Command` object (the handoff). The node function will use an LLM with a system prompt and a tool that lets it signal when it needs to hand off to another agent. If the LLM responds with the tool calls, we will return a `Command(goto=<other_agent>)`.

> **Note** : while we're using tools for the LLM to signal that it needs a handoff, the condition for the handoff can be anything: a specific response text from the LLM, structured output from the LLM, any other custom logic, etc.

Now, let's define our agent nodes and graph!

```
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-1)fromtyping_extensionsimport Literal
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-2)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-3)fromlangchain_core.messagesimport ToolMessage
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-4)fromlangchain_core.toolsimport tool
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-5)fromlangchain_anthropicimport ChatAnthropic
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-6)fromlanggraph.graphimport MessagesState, StateGraph, START
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-7)fromlanggraph.typesimport Command
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-8)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-9)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-10)model = ChatAnthropic(model="claude-3-5-sonnet-latest")
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-11)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-12)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-13)# Define a helper for each of the agent nodes to call
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-14)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-15)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-16)@tool
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-17)deftransfer_to_travel_advisor():
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-18)"""Ask travel advisor for help."""
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-19)  # This tool is not returning anything: we're just using it
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-20)  # as a way for LLM to signal that it needs to hand off to another agent
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-21)  # (See the paragraph above)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-22)  return
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-23)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-24)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-25)@tool
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-26)deftransfer_to_hotel_advisor():
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-27)"""Ask hotel advisor for help."""
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-28)  return
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-29)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-30)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-31)deftravel_advisor(
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-32)  state: MessagesState,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-33)) -> Command[Literal["hotel_advisor", "__end__"]]:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-34)  system_prompt = (
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-35)    "You are a general travel expert that can recommend travel destinations (e.g. countries, cities, etc). "
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-36)    "If you need hotel recommendations, ask 'hotel_advisor' for help."
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-37)  )
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-38)  messages = [{"role": "system", "content": system_prompt}] + state["messages"]
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-39)  ai_msg = model.bind_tools([transfer_to_hotel_advisor]).invoke(messages)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-40)  # If there are tool calls, the LLM needs to hand off to another agent
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-41)  if len(ai_msg.tool_calls) > 0:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-42)    tool_call_id = ai_msg.tool_calls[-1]["id"]
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-43)    # NOTE: it's important to insert a tool message here because LLM providers are expecting
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-44)    # all AI messages to be followed by a corresponding tool result message
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-45)    tool_msg = {
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-46)      "role": "tool",
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-47)      "content": "Successfully transferred",
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-48)      "tool_call_id": tool_call_id,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-49)    }
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-50)    return Command(goto="hotel_advisor", update={"messages": [ai_msg, tool_msg]})
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-51)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-52)  # If the expert has an answer, return it directly to the user
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-53)  return {"messages": [ai_msg]}
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-54)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-55)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-56)defhotel_advisor(
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-57)  state: MessagesState,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-58)) -> Command[Literal["travel_advisor", "__end__"]]:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-59)  system_prompt = (
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-60)    "You are a hotel expert that can provide hotel recommendations for a given destination. "
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-61)    "If you need help picking travel destinations, ask 'travel_advisor' for help."
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-62)  )
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-63)  messages = [{"role": "system", "content": system_prompt}] + state["messages"]
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-64)  ai_msg = model.bind_tools([transfer_to_travel_advisor]).invoke(messages)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-65)  # If there are tool calls, the LLM needs to hand off to another agent
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-66)  if len(ai_msg.tool_calls) > 0:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-67)    tool_call_id = ai_msg.tool_calls[-1]["id"]
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-68)    # NOTE: it's important to insert a tool message here because LLM providers are expecting
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-69)    # all AI messages to be followed by a corresponding tool result message
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-70)    tool_msg = {
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-71)      "role": "tool",
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-72)      "content": "Successfully transferred",
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-73)      "tool_call_id": tool_call_id,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-74)    }
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-75)    return Command(goto="travel_advisor", update={"messages": [ai_msg, tool_msg]})
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-76)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-77)  # If the expert has an answer, return it directly to the user
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-78)  return {"messages": [ai_msg]}
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-79)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-80)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-81)builder = StateGraph(MessagesState)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-82)builder.add_node("travel_advisor", travel_advisor)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-83)builder.add_node("hotel_advisor", hotel_advisor)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-84)# we'll always start with a general travel advisor
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-85)builder.add_edge(START, "travel_advisor")
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-86)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-87)graph = builder.compile()
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-88)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-89)fromIPython.displayimport display, Image
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-90)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-4-91)display(Image(graph.get_graph().draw_mermaid_png()))

```


API Reference: [ToolMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.tool.ToolMessage.html) | [tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html) | [ChatAnthropic](https://python.langchain.com/api_reference/anthropic/chat_models/langchain_anthropic.chat_models.ChatAnthropic.html) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [Command](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Command)

![]()

First, let's invoke it with a generic input:

```
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-5-1)fromlangchain_core.messagesimport convert_to_messages
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-5-2)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-5-3)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-5-4)defpretty_print_messages(update):
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-5-5)  if isinstance(update, tuple):
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-5-6)    ns, update = update
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-5-7)    # skip parent graph updates in the printouts
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-5-8)    if len(ns) == 0:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-5-9)      return
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-5-10)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-5-11)    graph_id = ns[-1].split(":")[0]
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-5-12)    print(f"Update from subgraph {graph_id}:")
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-5-13)    print("\n")
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-5-14)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-5-15)  for node_name, node_update in update.items():
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-5-16)    print(f"Update from node {node_name}:")
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-5-17)    print("\n")
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-5-18)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-5-19)    for m in convert_to_messages(node_update["messages"]):
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-5-20)      m.pretty_print()
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-5-21)    print("\n")

```


API Reference: [convert_to_messages](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.utils.convert_to_messages.html)

```
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-6-1)for chunk in graph.stream(
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-6-2)  {"messages": [("user", "i wanna go somewhere warm in the caribbean")]}
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-6-3)):
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-6-4)  pretty_print_messages(chunk)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-7-1)Update from node travel_advisor:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-7-2)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-7-3)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-7-4)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-7-5)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-7-6)I'd be happy to help you plan a Caribbean vacation! The Caribbean is perfect for warm weather getaways. Let me suggest some fantastic destinations:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-7-7)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-7-8)1. Dominican Republic
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-7-9)- Known for beautiful beaches, all-inclusive resorts, and tropical climate
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-7-10)- Popular areas include Punta Cana and Puerto Plata
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-7-11)- Great mix of beaches, culture, and activities
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-7-12)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-7-13)2. Jamaica
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-7-14)- Famous for its laid-back atmosphere and beautiful beaches
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-7-15)- Popular spots include Montego Bay, Negril, and Ocho Rios
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-7-16)- Known for reggae music, delicious cuisine, and water sports
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-7-17)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-7-18)3. Bahamas
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-7-19)- Crystal clear waters and stunning beaches
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-7-20)- Perfect for island hopping
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-7-21)- Great for water activities and swimming with pigs at Pig Beach
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-7-22)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-7-23)4. Turks and Caicos
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-7-24)- Pristine beaches and luxury resorts
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-7-25)- Excellent for snorkeling and diving
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-7-26)- More peaceful and less crowded than some other Caribbean destinations
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-7-27)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-7-28)5. Aruba
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-7-29)- Known for constant sunny weather and minimal rainfall
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-7-30)- Beautiful white sand beaches
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-7-31)- Great shopping and dining options
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-7-32)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-7-33)Would you like me to provide more specific information about any of these destinations? Also, if you'd like hotel recommendations for any of these locations, I can transfer you to our hotel advisor for specific accommodation suggestions. Just let me know which destination interests you most!

```


You can see that in this case only the first agent (`travel_advisor`) ran. Let's now ask for more recommendations: 

```
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-8-1)for chunk in graph.stream(
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-8-2)  {
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-8-3)    "messages": [
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-8-4)      (
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-8-5)        "user",
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-8-6)        "i wanna go somewhere warm in the caribbean. pick one destination and give me hotel recommendations",
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-8-7)      )
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-8-8)    ]
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-8-9)  }
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-8-10)):
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-8-11)  pretty_print_messages(chunk)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-9-1)Update from node travel_advisor:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-9-2)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-9-3)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-9-4)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-9-5)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-9-6)[{'text': "I'll help you with a Caribbean destination recommendation! Given the vast number of beautiful Caribbean islands, I'll recommend one popular destination: the Dominican Republic, specifically Punta Cana. It offers pristine beaches, warm weather year-round, crystal-clear waters, and excellent resorts.\n\nLet me get some hotel recommendations for Punta Cana by consulting our hotel advisor.", 'type': 'text'}, {'id': 'toolu_01B9djUstpDKHVSy3o3rfzsG', 'input': {}, 'name': 'transfer_to_hotel_advisor', 'type': 'tool_use'}]
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-9-7)Tool Calls:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-9-8) transfer_to_hotel_advisor (toolu_01B9djUstpDKHVSy3o3rfzsG)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-9-9) Call ID: toolu_01B9djUstpDKHVSy3o3rfzsG
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-9-10) Args:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-9-11)=================================[1m Tool Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-9-12)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-9-13)Successfully transferred
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-9-14)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-9-15)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-9-16)Update from node hotel_advisor:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-9-17)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-9-18)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-9-19)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-9-20)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-9-21)For Punta Cana, here are some top hotel recommendations:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-9-22)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-9-23)1. Hyatt Zilara Cap Cana - Adults-only, all-inclusive luxury resort with pristine beachfront location, multiple pools, and upscale dining options.
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-9-24)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-9-25)2. Hard Rock Hotel & Casino Punta Cana - Perfect for entertainment lovers, featuring 13 pools, 9 restaurants, a casino, and extensive amenities.
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-9-26)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-9-27)3. Excellence Punta Cana - Adults-only, all-inclusive resort known for its romantic atmosphere and excellent service.
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-9-28)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-9-29)4. Secrets Cap Cana Resort & Spa - Sophisticated adults-only resort with beautiful swim-out suites and gourmet dining options.
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-9-30)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-9-31)5. The Reserve at Paradisus Palma Real - Family-friendly luxury resort with dedicated family concierge, kids' activities, and beautiful pools.
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-9-32)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-9-33)These resorts all offer:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-9-34)- Direct beach access
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-9-35)- Multiple restaurants
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-9-36)- Swimming pools
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-9-37)- Spa facilities
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-9-38)- High-quality accommodations
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-9-39)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-9-40)Would you like more specific information about any of these hotels or would you prefer to explore hotels in a different Caribbean destination?

```


Voila - `travel_advisor` picks a destination and then makes a decision to call `hotel_advisor` for more info! 

## Using with a prebuilt ReAct agent[¶](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#using-with-a-prebuilt-react-agent "Permanent link")

Let's now see how we can implement the same team of travel agents, but give each of the agents some tools to call. We'll be using prebuilt `create_react_agent`[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent) to implement the agents. First, let's create some of the tools that the agents will be using:

```
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-10-1)importrandom
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-10-2)fromtyping_extensionsimport Literal
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-10-3)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-10-4)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-10-5)@tool
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-10-6)defget_travel_recommendations():
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-10-7)"""Get recommendation for travel destinations"""
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-10-8)  return random.choice(["aruba", "turks and caicos"])
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-10-9)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-10-10)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-10-11)@tool
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-10-12)defget_hotel_recommendations(location: Literal["aruba", "turks and caicos"]):
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-10-13)"""Get hotel recommendations for a given destination."""
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-10-14)  return {
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-10-15)    "aruba": [
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-10-16)      "The Ritz-Carlton, Aruba (Palm Beach)"
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-10-17)      "Bucuti & Tara Beach Resort (Eagle Beach)"
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-10-18)    ],
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-10-19)    "turks and caicos": ["Grace Bay Club", "COMO Parrot Cay"],
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-10-20)  }[location]

```


Let's also write a helper to create a handoff tool. See [this how-to guide](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs#implementing-handoffs-using-tools) for a more in-depth walkthrough of how to make a handoff tool.

```
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-11-1)fromtypingimport Annotated
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-11-2)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-11-3)fromlangchain_core.toolsimport tool
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-11-4)fromlangchain_core.tools.baseimport InjectedToolCallId
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-11-5)fromlanggraph.prebuiltimport InjectedState
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-11-6)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-11-7)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-11-8)defmake_handoff_tool(*, agent_name: str):
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-11-9)"""Create a tool that can return handoff via a Command"""
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-11-10)  tool_name = f"transfer_to_{agent_name}"
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-11-11)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-11-12)  @tool(tool_name)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-11-13)  defhandoff_to_agent(
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-11-14)    state: Annotated[dict, InjectedState],
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-11-15)    tool_call_id: Annotated[str, InjectedToolCallId],
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-11-16)  ):
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-11-17)"""Ask another agent for help."""
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-11-18)    tool_message = {
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-11-19)      "role": "tool",
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-11-20)      "content": f"Successfully transferred to {agent_name}",
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-11-21)      "name": tool_name,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-11-22)      "tool_call_id": tool_call_id,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-11-23)    }
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-11-24)    return Command(
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-11-25)      # navigate to another agent node in the PARENT graph
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-11-26)      goto=agent_name,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-11-27)      graph=Command.PARENT,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-11-28)      # This is the state update that the agent `agent_name` will see when it is invoked.
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-11-29)      # We're passing agent's FULL internal message history AND adding a tool message to make sure
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-11-30)      # the resulting chat history is valid.
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-11-31)      update={"messages": state["messages"] + [tool_message]},
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-11-32)    )
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-11-33)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-11-34)  return handoff_to_agent

```


API Reference: [tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html) | [InjectedToolCallId](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.InjectedToolCallId.html) | [InjectedState](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.InjectedState)

Now let's define our agent nodes and combine them into a graph:

```
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-1)fromlanggraph.graphimport MessagesState, StateGraph, START, END
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-2)fromlanggraph.prebuiltimport create_react_agent
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-3)fromlanggraph.typesimport Command
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-4)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-5)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-6)model = ChatAnthropic(model="claude-3-5-sonnet-latest")
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-7)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-8)# Define travel advisor ReAct agent
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-9)travel_advisor_tools = [
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-10)  get_travel_recommendations,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-11)  make_handoff_tool(agent_name="hotel_advisor"),
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-12)]
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-13)travel_advisor = create_react_agent(
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-14)  model,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-15)  travel_advisor_tools,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-16)  prompt=(
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-17)    "You are a general travel expert that can recommend travel destinations (e.g. countries, cities, etc). "
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-18)    "If you need hotel recommendations, ask 'hotel_advisor' for help. "
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-19)    "You MUST include human-readable response before transferring to another agent."
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-20)  ),
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-21))
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-22)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-23)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-24)defcall_travel_advisor(
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-25)  state: MessagesState,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-26)) -> Command[Literal["hotel_advisor", "__end__"]]:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-27)  # You can also add additional logic like changing the input to the agent / output from the agent, etc.
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-28)  # NOTE: we're invoking the ReAct agent with the full history of messages in the state
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-29)  return travel_advisor.invoke(state)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-30)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-31)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-32)# Define hotel advisor ReAct agent
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-33)hotel_advisor_tools = [
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-34)  get_hotel_recommendations,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-35)  make_handoff_tool(agent_name="travel_advisor"),
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-36)]
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-37)hotel_advisor = create_react_agent(
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-38)  model,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-39)  hotel_advisor_tools,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-40)  prompt=(
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-41)    "You are a hotel expert that can provide hotel recommendations for a given destination. "
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-42)    "If you need help picking travel destinations, ask 'travel_advisor' for help."
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-43)    "You MUST include human-readable response before transferring to another agent."
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-44)  ),
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-45))
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-46)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-47)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-48)defcall_hotel_advisor(
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-49)  state: MessagesState,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-50)) -> Command[Literal["travel_advisor", "__end__"]]:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-51)  return hotel_advisor.invoke(state)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-52)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-53)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-54)builder = StateGraph(MessagesState)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-55)builder.add_node("travel_advisor", call_travel_advisor)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-56)builder.add_node("hotel_advisor", call_hotel_advisor)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-57)# we'll always start with a general travel advisor
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-58)builder.add_edge(START, "travel_advisor")
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-59)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-60)graph = builder.compile()
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-12-61)display(Image(graph.get_graph().draw_mermaid_png()))

```


API Reference: [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END) | [create_react_agent](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent) | [Command](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Command)

![]()

Let's test it out using the same input as our original multi-agent system:

```
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-13-1)for chunk in graph.stream(
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-13-2)  {
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-13-3)    "messages": [
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-13-4)      (
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-13-5)        "user",
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-13-6)        "i wanna go somewhere warm in the caribbean. pick one destination and give me hotel recommendations",
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-13-7)      )
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-13-8)    ]
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-13-9)  },
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-13-10)  subgraphs=True,
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-13-11)):
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-13-12)  pretty_print_messages(chunk)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-1)Update from subgraph travel_advisor:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-2)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-3)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-4)Update from node agent:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-5)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-6)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-7)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-8)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-9)[{'text': "I'll help you find a warm Caribbean destination and get some hotel recommendations for you.\n\nLet me first get some travel recommendations for Caribbean destinations.", 'type': 'text'}, {'id': 'toolu_01GGDP6XSoJZFCYVA9Emhg89', 'input': {}, 'name': 'get_travel_recommendations', 'type': 'tool_use'}]
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-10)Tool Calls:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-11) get_travel_recommendations (toolu_01GGDP6XSoJZFCYVA9Emhg89)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-12) Call ID: toolu_01GGDP6XSoJZFCYVA9Emhg89
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-13) Args:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-14)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-15)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-16)Update from subgraph travel_advisor:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-17)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-18)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-19)Update from node tools:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-20)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-21)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-22)=================================[1m Tool Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-23)Name: get_travel_recommendations
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-24)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-25)turks and caicos
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-26)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-27)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-28)Update from subgraph travel_advisor:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-29)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-30)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-31)Update from node agent:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-32)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-33)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-34)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-35)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-36)[{'text': 'Based on the recommendations, I suggest Turks and Caicos! This beautiful British Overseas Territory is known for its stunning white-sand beaches, crystal-clear turquoise waters, and perfect warm weather year-round. The main island, Providenciales (often called "Provo"), is home to the famous Grace Bay Beach, consistently rated one of the world\'s best beaches.\n\nNow, let me connect you with our hotel advisor to get some specific hotel recommendations for Turks and Caicos.', 'type': 'text'}, {'id': 'toolu_01JbPSSbTdbWSPNPwsKxifKR', 'input': {}, 'name': 'transfer_to_hotel_advisor', 'type': 'tool_use'}]
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-37)Tool Calls:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-38) transfer_to_hotel_advisor (toolu_01JbPSSbTdbWSPNPwsKxifKR)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-39) Call ID: toolu_01JbPSSbTdbWSPNPwsKxifKR
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-40) Args:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-41)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-42)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-43)Update from subgraph hotel_advisor:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-44)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-45)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-46)Update from node agent:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-47)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-48)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-49)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-50)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-51)[{'text': 'Let me get some hotel recommendations for Turks and Caicos:', 'type': 'text'}, {'id': 'toolu_01JfcmUUmpdiYEFXaDFEkh1G', 'input': {'location': 'turks and caicos'}, 'name': 'get_hotel_recommendations', 'type': 'tool_use'}]
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-52)Tool Calls:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-53) get_hotel_recommendations (toolu_01JfcmUUmpdiYEFXaDFEkh1G)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-54) Call ID: toolu_01JfcmUUmpdiYEFXaDFEkh1G
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-55) Args:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-56)  location: turks and caicos
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-57)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-58)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-59)Update from subgraph hotel_advisor:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-60)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-61)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-62)Update from node tools:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-63)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-64)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-65)=================================[1m Tool Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-66)Name: get_hotel_recommendations
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-67)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-68)["Grace Bay Club", "COMO Parrot Cay"]
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-69)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-70)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-71)Update from subgraph hotel_advisor:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-72)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-73)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-74)Update from node agent:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-75)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-76)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-77)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-78)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-79)Here are two excellent hotel options in Turks and Caicos:
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-80)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-81)1. Grace Bay Club: This luxury resort is located on the world-famous Grace Bay Beach. It offers elegant accommodations, multiple swimming pools, a spa, and several dining options. The resort is divided into different sections including adults-only and family-friendly areas.
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-82)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-83)2. COMO Parrot Cay: This exclusive private island resort offers the ultimate luxury escape. It features pristine beaches, world-class spa facilities, and exceptional dining experiences. The resort is known for its serene atmosphere and excellent service.
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-84)
[](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__codelineno-14-85)Would you like more specific information about either of these properties?

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to implement handoffs between agents  ](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/) [ Next  How to add multi-turn conversation in a multi-agent application  ](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
