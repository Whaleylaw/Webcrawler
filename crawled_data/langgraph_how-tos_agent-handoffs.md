---
url: https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#how-to-implement-handoffs-between-agents)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to implement handoffs between agents 

[ ](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/?q= "Share")

Initializing search 

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
            * How to implement handoffs between agents  [ How to implement handoffs between agents  ](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#setup)
              * [ Implement handoffs using Command  ](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#implement-handoffs-using-command)
              * [ Implement handoffs using tools  ](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#implement-handoffs-using-tools)
                * [ Implement a handoff tool  ](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#implement-a-handoff-tool)
                * [ Using with a custom agent  ](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#using-with-a-custom-agent)
              * [ Using with a prebuilt ReAct agent  ](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#using-with-a-prebuilt-react-agent)
            * [ How to build a multi-agent network  ](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#setup)
  * [ Implement handoffs using Command  ](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#implement-handoffs-using-command)
  * [ Implement handoffs using tools  ](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#implement-handoffs-using-tools)
    * [ Implement a handoff tool  ](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#implement-a-handoff-tool)
    * [ Using with a custom agent  ](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#using-with-a-custom-agent)
  * [ Using with a prebuilt ReAct agent  ](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#using-with-a-prebuilt-react-agent)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Multi-agent  ](https://langchain-ai.github.io/langgraph/how-tos#multi-agent)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/agent-handoffs.ipynb "Edit this page")

# How to implement handoffs between agents[¶](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#how-to-implement-handoffs-between-agents "Permanent link")

Prerequisites

This guide assumes familiarity with the following:

  * [Multi-agent systems](https://langchain-ai.github.io/langgraph/concepts/multi_agent)
  * [Command](https://langchain-ai.github.io/langgraph/concepts/low_level/#command)
  * [LangGraph Glossary](https://langchain-ai.github.io/langgraph/concepts/low_level/)



In multi-agent architectures, agents can be represented as graph nodes. Each agent node executes its step(s) and decides whether to finish execution or route to another agent, including potentially routing to itself (e.g., running in a loop). A natural pattern in multi-agent interactions is [handoffs](https://langchain-ai.github.io/langgraph/concepts/multi_agent#handoffs), where one agent hands off control to another. Handoffs allow you to specify:

  * **destination** : target agent to navigate to - node name in LangGraph
  * **payload** : information to pass to that agent - state update in LangGraph



To implement handoffs in LangGraph, agent nodes can return `Command` object that allows you to [combine both control flow and state updates](https://langchain-ai.github.io/langgraph/how-tos/command):

```
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-0-1)defagent(state) -> Command[Literal["agent", "another_agent"]]:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-0-2)  # the condition for routing/halting can be anything, e.g. LLM tool call / structured output, etc.
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-0-3)  goto = get_next_agent(...) # 'agent' / 'another_agent'
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-0-4)  return Command(
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-0-5)    # Specify which agent to call next
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-0-6)    goto=goto,
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-0-7)    # Update the graph state
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-0-8)    update={"my_state_key": "my_state_value"}
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-0-9)  )

```


One of the most common agent types is a tool-calling agent. For those types of agents, one pattern is wrapping a handoff in a tool call, e.g.:

```
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-1-1)@tool
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-1-2)deftransfer_to_bob(state):
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-1-3)"""Transfer to bob."""
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-1-4)  return Command(
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-1-5)    goto="bob",
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-1-6)    update={"my_state_key": "my_state_value"},
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-1-7)    # Each tool-calling agent is implemented as a subgraph.
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-1-8)    # As a result, to navigate to another agent (a sibling sub-graph), 
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-1-9)    # we need to specify that navigation is w/ respect to the parent graph.
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-1-10)    graph=Command.PARENT,
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-1-11)  )

```


This guide shows how you can:

  * implement handoffs using `Command`: agent node makes a decision on who to hand off to (usually LLM-based), and explicitly returns a handoff via `Command`. These are useful when you need fine-grained control over how an agent routes to another agent. It could be well suited for implementing a supervisor agent in a supervisor architecture.
  * implement handoffs using tools: a tool-calling agent has access to tools that can return a handoff via `Command`. The tool-executing node in the agent recognizes `Command` objects returned by the tools and routes accordingly. Handoff tool a general-purpose primitive that is useful in any multi-agent systems that contain tool-calling agents.



## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#setup "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-2-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-2-2)%pip install -U langgraph langchain-anthropic

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-3-1)importgetpass
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-3-2)importos
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-3-3)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-3-4)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-3-5)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-3-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-3-7)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-3-8)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-3-9)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-3-10)_set_env("ANTHROPIC_API_KEY")

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Implement handoffs using `Command`[¶](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#implement-handoffs-using-command "Permanent link")

Let's implement a system with two agents:

  * an addition expert (can only add numbers)
  * a multiplication expert (can only multiply numbers).



In this example the agents will be relying on the LLM for doing math. In a more realistic [follow-up example](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#using-with-a-custom-agent), we will give the agents tools for doing math.

When the addition expert needs help with multiplication, it hands off to the multiplication expert and vice-versa. This is an example of a simple multi-agent network.

Each agent will have a corresponding node function that can conditionally return a `Command` object (e.g. our handoff). The node function will use an LLM with a system prompt and a tool that lets it signal when it needs to hand off to another agent. If the LLM responds with the tool calls, we will return a `Command(goto=<other_agent>)`.

> **Note** : while we're using tools for the LLM to signal that it needs a handoff, the condition for the handoff can be anything: a specific response text from the LLM, structured output from the LLM, any other custom logic, etc.

```
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-1)fromtyping_extensionsimport Literal
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-2)fromlangchain_core.messagesimport ToolMessage
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-3)fromlangchain_core.toolsimport tool
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-4)fromlangchain_anthropicimport ChatAnthropic
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-5)fromlanggraph.graphimport MessagesState, StateGraph, START
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-6)fromlanggraph.typesimport Command
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-7)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-8)model = ChatAnthropic(model="claude-3-5-sonnet-latest")
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-9)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-10)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-11)@tool
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-12)deftransfer_to_multiplication_expert():
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-13)"""Ask multiplication agent for help."""
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-14)  # This tool is not returning anything: we're just using it
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-15)  # as a way for LLM to signal that it needs to hand off to another agent
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-16)  # (See the paragraph above)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-17)  return
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-18)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-19)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-20)@tool
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-21)deftransfer_to_addition_expert():
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-22)"""Ask addition agent for help."""
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-23)  return
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-24)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-25)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-26)defaddition_expert(
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-27)  state: MessagesState,
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-28)) -> Command[Literal["multiplication_expert", "__end__"]]:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-29)  system_prompt = (
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-30)    "You are an addition expert, you can ask the multiplication expert for help with multiplication. "
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-31)    "Always do your portion of calculation before the handoff."
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-32)  )
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-33)  messages = [{"role": "system", "content": system_prompt}] + state["messages"]
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-34)  ai_msg = model.bind_tools([transfer_to_multiplication_expert]).invoke(messages)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-35)  # If there are tool calls, the LLM needs to hand off to another agent
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-36)  if len(ai_msg.tool_calls) > 0:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-37)    tool_call_id = ai_msg.tool_calls[-1]["id"]
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-38)    # NOTE: it's important to insert a tool message here because LLM providers are expecting
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-39)    # all AI messages to be followed by a corresponding tool result message
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-40)    tool_msg = {
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-41)      "role": "tool",
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-42)      "content": "Successfully transferred",
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-43)      "tool_call_id": tool_call_id,
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-44)    }
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-45)    return Command(
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-46)      goto="multiplication_expert", update={"messages": [ai_msg, tool_msg]}
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-47)    )
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-48)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-49)  # If the expert has an answer, return it directly to the user
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-50)  return {"messages": [ai_msg]}
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-51)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-52)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-53)defmultiplication_expert(
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-54)  state: MessagesState,
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-55)) -> Command[Literal["addition_expert", "__end__"]]:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-56)  system_prompt = (
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-57)    "You are a multiplication expert, you can ask an addition expert for help with addition. "
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-58)    "Always do your portion of calculation before the handoff."
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-59)  )
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-60)  messages = [{"role": "system", "content": system_prompt}] + state["messages"]
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-61)  ai_msg = model.bind_tools([transfer_to_addition_expert]).invoke(messages)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-62)  if len(ai_msg.tool_calls) > 0:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-63)    tool_call_id = ai_msg.tool_calls[-1]["id"]
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-64)    tool_msg = {
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-65)      "role": "tool",
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-66)      "content": "Successfully transferred",
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-67)      "tool_call_id": tool_call_id,
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-68)    }
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-69)    return Command(goto="addition_expert", update={"messages": [ai_msg, tool_msg]})
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-70)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-4-71)  return {"messages": [ai_msg]}

```


API Reference: [ToolMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.tool.ToolMessage.html) | [tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html) | [ChatAnthropic](https://python.langchain.com/api_reference/anthropic/chat_models/langchain_anthropic.chat_models.ChatAnthropic.html) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [Command](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Command)

Let's now combine both of these nodes into a single graph. Note that there are no edges between the agents! If the expert has an answer, it will return it directly to the user, otherwise it will route to the other expert for help.

```
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-5-1)builder = StateGraph(MessagesState)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-5-2)builder.add_node("addition_expert", addition_expert)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-5-3)builder.add_node("multiplication_expert", multiplication_expert)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-5-4)# we'll always start with the addition expert
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-5-5)builder.add_edge(START, "addition_expert")
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-5-6)graph = builder.compile()

```


Finally, let's define a helper function to render the streamed outputs nicely:

```
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-6-1)fromlangchain_core.messagesimport convert_to_messages
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-6-2)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-6-3)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-6-4)defpretty_print_messages(update):
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-6-5)  if isinstance(update, tuple):
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-6-6)    ns, update = update
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-6-7)    # skip parent graph updates in the printouts
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-6-8)    if len(ns) == 0:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-6-9)      return
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-6-10)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-6-11)    graph_id = ns[-1].split(":")[0]
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-6-12)    print(f"Update from subgraph {graph_id}:")
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-6-13)    print("\n")
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-6-14)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-6-15)  for node_name, node_update in update.items():
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-6-16)    print(f"Update from node {node_name}:")
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-6-17)    print("\n")
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-6-18)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-6-19)    for m in convert_to_messages(node_update["messages"]):
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-6-20)      m.pretty_print()
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-6-21)    print("\n")

```


API Reference: [convert_to_messages](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.utils.convert_to_messages.html)

Let's run the graph with an expression that requires both addition and multiplication:

```
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-7-1)for chunk in graph.stream(
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-7-2)  {"messages": [("user", "what's (3 + 5) * 12")]},
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-7-3)):
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-7-4)  pretty_print_messages(chunk)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-8-1)Update from node addition_expert:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-8-2)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-8-3)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-8-4)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-8-5)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-8-6)[{'text': "Let me help break this down:\n\nFirst, I'll handle the addition part since I'm the addition expert:\n3 + 5 = 8\n\nNow, for the multiplication of 8 * 12, I'll need to ask the multiplication expert for help.", 'type': 'text'}, {'id': 'toolu_015LCrsomHbeoQPtCzuff78Y', 'input': {}, 'name': 'transfer_to_multiplication_expert', 'type': 'tool_use'}]
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-8-7)Tool Calls:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-8-8) transfer_to_multiplication_expert (toolu_015LCrsomHbeoQPtCzuff78Y)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-8-9) Call ID: toolu_015LCrsomHbeoQPtCzuff78Y
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-8-10) Args:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-8-11)=================================[1m Tool Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-8-12)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-8-13)Successfully transferred
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-8-14)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-8-15)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-8-16)Update from node multiplication_expert:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-8-17)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-8-18)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-8-19)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-8-20)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-8-21)[{'text': 'I see there was an error in my approach. I am actually the multiplication expert, and I need to ask the addition expert for help with (3 + 5) first.', 'type': 'text'}, {'id': 'toolu_01HFcB8WesPfDyrdgxoXApZk', 'input': {}, 'name': 'transfer_to_addition_expert', 'type': 'tool_use'}]
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-8-22)Tool Calls:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-8-23) transfer_to_addition_expert (toolu_01HFcB8WesPfDyrdgxoXApZk)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-8-24) Call ID: toolu_01HFcB8WesPfDyrdgxoXApZk
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-8-25) Args:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-8-26)=================================[1m Tool Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-8-27)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-8-28)Successfully transferred
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-8-29)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-8-30)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-8-31)Update from node addition_expert:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-8-32)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-8-33)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-8-34)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-8-35)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-8-36)Now that I have the result of 3 + 5 = 8 from the addition expert, I can multiply 8 * 12:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-8-37)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-8-38)8 * 12 = 96
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-8-39)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-8-40)So, (3 + 5) * 12 = 96

```


You can see that the addition expert first handled the expression in the parentheses, and then handed off to the multiplication expert to finish the calculation. 

Now let's see how we can implement this same system using special handoff tools and give our agents actual math tools.

## Implement handoffs using tools[¶](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#implement-handoffs-using-tools "Permanent link")

### Implement a handoff tool[¶](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#implement-a-handoff-tool "Permanent link")

In the previous example we explicitly defined custom handoffs in each of the agent nodes. Another pattern is to create special **handoff tools** that directly return `Command` objects. When an agent calls a tool like this, it hands the control off to a different agent. Specifically, the tool-executing node in the agent recognizes the `Command` objects returned by the tools and routes control flow accordingly. **Note** : unlike the previous example, a tool-calling agent is not a single node but another graph that can be added to the multi-agent graph as a subgraph node.

There are a few important considerations when implementing handoff tools:

  * since each agent is a **subgraph** node in another graph, and the tools will be called in one of the agent subgraph nodes (e.g. tool executor), we need to specify `graph=Command.PARENT` in the `Command`, so that LangGraph knows to navigate outside of the agent subgraph
  * we can optionally specify a state update that will be applied to the parent graph state before the next agent is called

    * these state updates can be used to control [how much of the chat message history](https://langchain-ai.github.io/langgraph/concepts/multi_agent#shared-message-list) the target agent sees. For example, you might choose to just share the last AI messages from the current agent, or its full internal chat history, etc. In the examples below we'll be sharing the full internal chat history.
  * we can optionally provide the following to the tool (in the tool function signature):

    * graph state (using `InjectedState`[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.InjectedState))
    * graph long-term memory (using `InjectedStore`[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.InjectedStore))
    * the current tool call ID (using `InjectedToolCallId`[](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.InjectedToolCallId.html))

These are not necessary but are useful for creating the state update passed to the next agent.




```
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-9-1)fromtypingimport Annotated
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-9-2)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-9-3)fromlangchain_core.toolsimport tool
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-9-4)fromlangchain_core.tools.baseimport InjectedToolCallId
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-9-5)fromlanggraph.prebuiltimport InjectedState
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-9-6)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-9-7)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-9-8)defmake_handoff_tool(*, agent_name: str):
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-9-9)"""Create a tool that can return handoff via a Command"""
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-9-10)  tool_name = f"transfer_to_{agent_name}"
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-9-11)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-9-12)  @tool(tool_name)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-9-13)  defhandoff_to_agent(
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-9-14)    # # optionally pass current graph state to the tool (will be ignored by the LLM)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-9-15)    state: Annotated[dict, InjectedState],
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-9-16)    # optionally pass the current tool call ID (will be ignored by the LLM)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-9-17)    tool_call_id: Annotated[str, InjectedToolCallId],
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-9-18)  ):
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-9-19)"""Ask another agent for help."""
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-9-20)    tool_message = {
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-9-21)      "role": "tool",
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-9-22)      "content": f"Successfully transferred to {agent_name}",
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-9-23)      "name": tool_name,
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-9-24)      "tool_call_id": tool_call_id,
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-9-25)    }
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-9-26)    return Command(
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-9-27)      # navigate to another agent node in the PARENT graph
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-9-28)      goto=agent_name,
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-9-29)      graph=Command.PARENT,
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-9-30)      # This is the state update that the agent `agent_name` will see when it is invoked.
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-9-31)      # We're passing agent's FULL internal message history AND adding a tool message to make sure
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-9-32)      # the resulting chat history is valid. See the paragraph above for more information.
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-9-33)      update={"messages": state["messages"] + [tool_message]},
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-9-34)    )
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-9-35)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-9-36)  return handoff_to_agent

```


API Reference: [tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html) | [InjectedToolCallId](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.InjectedToolCallId.html) | [InjectedState](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.InjectedState)

### Using with a custom agent[¶](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#using-with-a-custom-agent "Permanent link")

To demonstrate how to use handoff tools, let's first implement a simple version of the prebuilt [create_react_agent](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent). This is useful in case you want to have a custom tool-calling agent implementation and want to leverage handoff tools.

```
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-1)fromtyping_extensionsimport Literal
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-2)fromlangchain_core.messagesimport ToolMessage
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-3)fromlangchain_core.toolsimport tool
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-4)fromlanggraph.graphimport MessagesState, StateGraph, START
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-5)fromlanggraph.typesimport Command
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-6)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-7)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-8)defmake_agent(model, tools, system_prompt=None):
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-9)  model_with_tools = model.bind_tools(tools)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-10)  tools_by_name = {tool.name: tool for tool in tools}
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-11)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-12)  defcall_model(state: MessagesState) -> Command[Literal["call_tools", "__end__"]]:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-13)    messages = state["messages"]
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-14)    if system_prompt:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-15)      messages = [{"role": "system", "content": system_prompt}] + messages
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-16)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-17)    response = model_with_tools.invoke(messages)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-18)    if len(response.tool_calls) > 0:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-19)      return Command(goto="call_tools", update={"messages": [response]})
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-20)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-21)    return {"messages": [response]}
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-22)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-23)  # NOTE: this is a simplified version of the prebuilt ToolNode
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-24)  # If you want to have a tool node that has full feature parity, please refer to the source code
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-25)  defcall_tools(state: MessagesState) -> Command[Literal["call_model"]]:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-26)    tool_calls = state["messages"][-1].tool_calls
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-27)    results = []
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-28)    for tool_call in tool_calls:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-29)      tool_ = tools_by_name[tool_call["name"]]
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-30)      tool_input_fields = tool_.get_input_schema().model_json_schema()[
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-31)        "properties"
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-32)      ]
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-33)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-34)      # this is simplified for demonstration purposes and
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-35)      # is different from the ToolNode implementation
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-36)      if "state" in tool_input_fields:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-37)        # inject state
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-38)        tool_call = {**tool_call, "args": {**tool_call["args"], "state": state}}
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-39)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-40)      tool_response = tool_.invoke(tool_call)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-41)      if isinstance(tool_response, ToolMessage):
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-42)        results.append(Command(update={"messages": [tool_response]}))
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-43)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-44)      # handle tools that return Command directly
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-45)      elif isinstance(tool_response, Command):
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-46)        results.append(tool_response)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-47)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-48)    # NOTE: nodes in LangGraph allow you to return list of updates, including Command objects
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-49)    return results
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-50)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-51)  graph = StateGraph(MessagesState)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-52)  graph.add_node(call_model)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-53)  graph.add_node(call_tools)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-54)  graph.add_edge(START, "call_model")
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-55)  graph.add_edge("call_tools", "call_model")
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-56)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-10-57)  return graph.compile()

```


API Reference: [ToolMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.tool.ToolMessage.html) | [tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [Command](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Command)

Let's also define math tools that we'll give our agents:

```
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-11-1)@tool
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-11-2)defadd(a: int, b: int) -> int:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-11-3)"""Adds two numbers."""
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-11-4)  return a + b
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-11-5)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-11-6)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-11-7)@tool
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-11-8)defmultiply(a: int, b: int) -> int:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-11-9)"""Multiplies two numbers."""
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-11-10)  return a * b

```


Let's test the agent implementation out to make sure it's working as expected:

```
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-12-1)agent = make_agent(model, [add, multiply])
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-12-2)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-12-3)for chunk in agent.stream({"messages": [("user", "what's (3 + 5) * 12")]}):
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-12-4)  pretty_print_messages(chunk)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-13-1)Update from node call_model:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-13-2)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-13-3)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-13-4)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-13-5)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-13-6)[{'text': "I'll help break this down into two steps:\n1. First calculate 3 + 5\n2. Then multiply that result by 12\n\nLet me make these calculations:\n\n1. Adding 3 and 5:", 'type': 'text'}, {'id': 'toolu_01DUAzgWFqq6XZtj1hzHTka9', 'input': {'a': 3, 'b': 5}, 'name': 'add', 'type': 'tool_use'}]
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-13-7)Tool Calls:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-13-8) add (toolu_01DUAzgWFqq6XZtj1hzHTka9)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-13-9) Call ID: toolu_01DUAzgWFqq6XZtj1hzHTka9
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-13-10) Args:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-13-11)  a: 3
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-13-12)  b: 5
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-13-13)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-13-14)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-13-15)Update from node call_tools:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-13-16)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-13-17)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-13-18)=================================[1m Tool Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-13-19)Name: add
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-13-20)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-13-21)8
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-13-22)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-13-23)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-13-24)Update from node call_model:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-13-25)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-13-26)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-13-27)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-13-28)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-13-29)[{'text': '2. Multiplying the result (8) by 12:', 'type': 'text'}, {'id': 'toolu_01QXi1prSN4etgJ1QCuFJsgN', 'input': {'a': 8, 'b': 12}, 'name': 'multiply', 'type': 'tool_use'}]
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-13-30)Tool Calls:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-13-31) multiply (toolu_01QXi1prSN4etgJ1QCuFJsgN)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-13-32) Call ID: toolu_01QXi1prSN4etgJ1QCuFJsgN
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-13-33) Args:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-13-34)  a: 8
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-13-35)  b: 12
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-13-36)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-13-37)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-13-38)Update from node call_tools:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-13-39)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-13-40)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-13-41)=================================[1m Tool Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-13-42)Name: multiply
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-13-43)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-13-44)96
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-13-45)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-13-46)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-13-47)Update from node call_model:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-13-48)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-13-49)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-13-50)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-13-51)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-13-52)The result of (3 + 5) * 12 = 96

```


Now, we can implement our multi-agent system with the multiplication and addition expert agents. This time we'll give them the tools for doing math, as well as our special handoff tools: 

```
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-14-1)addition_expert = make_agent(
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-14-2)  model,
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-14-3)  [add, make_handoff_tool(agent_name="multiplication_expert")],
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-14-4)  system_prompt="You are an addition expert, you can ask the multiplication expert for help with multiplication.",
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-14-5))
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-14-6)multiplication_expert = make_agent(
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-14-7)  model,
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-14-8)  [multiply, make_handoff_tool(agent_name="addition_expert")],
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-14-9)  system_prompt="You are a multiplication expert, you can ask an addition expert for help with addition.",
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-14-10))
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-14-11)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-14-12)builder = StateGraph(MessagesState)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-14-13)builder.add_node("addition_expert", addition_expert)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-14-14)builder.add_node("multiplication_expert", multiplication_expert)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-14-15)builder.add_edge(START, "addition_expert")
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-14-16)graph = builder.compile()

```


Let's run the graph with the same multi-step calculation input as before:

```
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-15-1)for chunk in graph.stream(
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-15-2)  {"messages": [("user", "what's (3 + 5) * 12")]}, subgraphs=True
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-15-3)):
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-15-4)  pretty_print_messages(chunk)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-1)Update from subgraph addition_expert:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-2)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-3)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-4)Update from node call_model:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-5)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-6)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-7)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-8)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-9)[{'text': "I can help with the addition part (3 + 5), but I'll need to ask the multiplication expert for help with multiplying the result by 12. Let me break this down:\n\n1. First, let me calculate 3 + 5:", 'type': 'text'}, {'id': 'toolu_01McaW4XWczLGKaetg88fxQ5', 'input': {'a': 3, 'b': 5}, 'name': 'add', 'type': 'tool_use'}]
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-10)Tool Calls:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-11) add (toolu_01McaW4XWczLGKaetg88fxQ5)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-12) Call ID: toolu_01McaW4XWczLGKaetg88fxQ5
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-13) Args:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-14)  a: 3
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-15)  b: 5
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-16)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-17)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-18)Update from subgraph addition_expert:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-19)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-20)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-21)Update from node call_tools:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-22)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-23)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-24)=================================[1m Tool Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-25)Name: add
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-26)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-27)8
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-28)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-29)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-30)Update from subgraph addition_expert:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-31)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-32)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-33)Update from node call_model:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-34)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-35)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-36)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-37)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-38)[{'text': "Now that we have 8, we need to multiply it by 12. I'll ask the multiplication expert for help with this:", 'type': 'text'}, {'id': 'toolu_01KpdUhHuyrmha62z5SduKRc', 'input': {}, 'name': 'transfer_to_multiplication_expert', 'type': 'tool_use'}]
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-39)Tool Calls:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-40) transfer_to_multiplication_expert (toolu_01KpdUhHuyrmha62z5SduKRc)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-41) Call ID: toolu_01KpdUhHuyrmha62z5SduKRc
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-42) Args:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-43)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-44)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-45)Update from subgraph multiplication_expert:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-46)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-47)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-48)Update from node call_model:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-49)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-50)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-51)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-52)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-53)[{'text': 'Now that we have 8 as the result of the addition, I can help with the multiplication by 12:', 'type': 'text'}, {'id': 'toolu_01Vnp4k3TE87siad3BNJgRKb', 'input': {'a': 8, 'b': 12}, 'name': 'multiply', 'type': 'tool_use'}]
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-54)Tool Calls:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-55) multiply (toolu_01Vnp4k3TE87siad3BNJgRKb)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-56) Call ID: toolu_01Vnp4k3TE87siad3BNJgRKb
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-57) Args:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-58)  a: 8
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-59)  b: 12
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-60)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-61)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-62)Update from subgraph multiplication_expert:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-63)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-64)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-65)Update from node call_tools:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-66)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-67)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-68)=================================[1m Tool Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-69)Name: multiply
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-70)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-71)96
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-72)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-73)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-74)Update from subgraph multiplication_expert:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-75)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-76)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-77)Update from node call_model:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-78)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-79)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-80)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-81)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-82)The final result is 96.
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-83)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-84)To break down the steps:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-85)1. 3 + 5 = 8
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-16-86)2. 8 * 12 = 96

```


We can see that after the addition expert is done with the first part of the calculation (after calling the `add` tool), it decides to hand off to the multiplication expert, which computes the final result. 

## Using with a prebuilt ReAct agent[¶](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#using-with-a-prebuilt-react-agent "Permanent link")

If you don't need extra customization, you can use the prebuilt `create_react_agent`[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent), which includes built-in support for handoff tools through `ToolNode`[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.ToolNode).

```
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-17-1)fromlanggraph.prebuiltimport create_react_agent
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-17-2)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-17-3)addition_expert = create_react_agent(
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-17-4)  model,
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-17-5)  [add, make_handoff_tool(agent_name="multiplication_expert")],
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-17-6)  prompt="You are an addition expert, you can ask the multiplication expert for help with multiplication.",
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-17-7))
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-17-8)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-17-9)multiplication_expert = create_react_agent(
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-17-10)  model,
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-17-11)  [multiply, make_handoff_tool(agent_name="addition_expert")],
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-17-12)  prompt="You are a multiplication expert, you can ask an addition expert for help with addition.",
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-17-13))
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-17-14)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-17-15)builder = StateGraph(MessagesState)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-17-16)builder.add_node("addition_expert", addition_expert)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-17-17)builder.add_node("multiplication_expert", multiplication_expert)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-17-18)builder.add_edge(START, "addition_expert")
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-17-19)graph = builder.compile()

```


API Reference: [create_react_agent](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent)

We can now verify that the prebuilt ReAct agent works exactly the same as the custom agent above:

```
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-18-1)for chunk in graph.stream(
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-18-2)  {"messages": [("user", "what's (3 + 5) * 12")]}, subgraphs=True
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-18-3)):
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-18-4)  pretty_print_messages(chunk)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-1)Update from subgraph addition_expert:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-2)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-3)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-4)Update from node agent:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-5)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-6)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-7)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-8)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-9)[{'text': "I can help with the addition part of this calculation (3 + 5), and then I'll need to ask the multiplication expert for help with multiplying the result by 12.\n\nLet me first calculate 3 + 5:", 'type': 'text'}, {'id': 'toolu_01GUasumGGJVXDV7TJEqEfmY', 'input': {'a': 3, 'b': 5}, 'name': 'add', 'type': 'tool_use'}]
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-10)Tool Calls:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-11) add (toolu_01GUasumGGJVXDV7TJEqEfmY)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-12) Call ID: toolu_01GUasumGGJVXDV7TJEqEfmY
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-13) Args:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-14)  a: 3
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-15)  b: 5
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-16)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-17)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-18)Update from subgraph addition_expert:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-19)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-20)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-21)Update from node tools:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-22)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-23)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-24)=================================[1m Tool Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-25)Name: add
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-26)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-27)8
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-28)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-29)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-30)Update from subgraph addition_expert:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-31)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-32)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-33)Update from node agent:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-34)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-35)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-36)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-37)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-38)[{'text': "Now that we have 8, we need to multiply it by 12. Since I'm an addition expert, I'll transfer this to the multiplication expert to complete the calculation:", 'type': 'text'}, {'id': 'toolu_014HEbwiH2jVno8r1Pc6t9Qh', 'input': {}, 'name': 'transfer_to_multiplication_expert', 'type': 'tool_use'}]
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-39)Tool Calls:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-40) transfer_to_multiplication_expert (toolu_014HEbwiH2jVno8r1Pc6t9Qh)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-41) Call ID: toolu_014HEbwiH2jVno8r1Pc6t9Qh
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-42) Args:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-43)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-44)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-45)Update from subgraph multiplication_expert:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-46)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-47)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-48)Update from node agent:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-49)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-50)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-51)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-52)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-53)[{'text': 'I notice I made a mistake - I actually don\'t have access to the "add" function or "transfer_to_multiplication_expert". Instead, I am the multiplication expert and I should ask the addition expert for help with the first part. Let me correct this:', 'type': 'text'}, {'id': 'toolu_01VAGpmr4ysHjvvuZp3q5Dzj', 'input': {}, 'name': 'transfer_to_addition_expert', 'type': 'tool_use'}]
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-54)Tool Calls:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-55) transfer_to_addition_expert (toolu_01VAGpmr4ysHjvvuZp3q5Dzj)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-56) Call ID: toolu_01VAGpmr4ysHjvvuZp3q5Dzj
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-57) Args:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-58)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-59)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-60)Update from subgraph addition_expert:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-61)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-62)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-63)Update from node agent:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-64)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-65)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-66)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-67)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-68)[{'text': "I'll help you with the addition part of (3 + 5) * 12. First, let me calculate 3 + 5:", 'type': 'text'}, {'id': 'toolu_01RE16cRGVo4CC4wwHFB6gaE', 'input': {'a': 3, 'b': 5}, 'name': 'add', 'type': 'tool_use'}]
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-69)Tool Calls:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-70) add (toolu_01RE16cRGVo4CC4wwHFB6gaE)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-71) Call ID: toolu_01RE16cRGVo4CC4wwHFB6gaE
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-72) Args:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-73)  a: 3
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-74)  b: 5
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-75)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-76)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-77)Update from subgraph addition_expert:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-78)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-79)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-80)Update from node tools:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-81)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-82)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-83)=================================[1m Tool Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-84)Name: add
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-85)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-86)8
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-87)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-88)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-89)Update from subgraph addition_expert:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-90)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-91)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-92)Update from node agent:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-93)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-94)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-95)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-96)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-97)[{'text': "Now that we have 8, we need to multiply it by 12. Since I'm an addition expert, I'll need to transfer this to the multiplication expert to complete the calculation:", 'type': 'text'}, {'id': 'toolu_01HBDRh64SzGcCp7EX1u3MFa', 'input': {}, 'name': 'transfer_to_multiplication_expert', 'type': 'tool_use'}]
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-98)Tool Calls:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-99) transfer_to_multiplication_expert (toolu_01HBDRh64SzGcCp7EX1u3MFa)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-100) Call ID: toolu_01HBDRh64SzGcCp7EX1u3MFa
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-101) Args:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-102)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-103)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-104)Update from subgraph multiplication_expert:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-105)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-106)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-107)Update from node agent:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-108)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-109)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-110)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-111)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-112)[{'text': 'Now that I have the result of 3 + 5 = 8, I can help with multiplying by 12:', 'type': 'text'}, {'id': 'toolu_014Ay95rsKvvbWWJV4CcZSPY', 'input': {'a': 8, 'b': 12}, 'name': 'multiply', 'type': 'tool_use'}]
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-113)Tool Calls:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-114) multiply (toolu_014Ay95rsKvvbWWJV4CcZSPY)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-115) Call ID: toolu_014Ay95rsKvvbWWJV4CcZSPY
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-116) Args:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-117)  a: 8
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-118)  b: 12
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-119)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-120)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-121)Update from subgraph multiplication_expert:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-122)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-123)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-124)Update from node tools:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-125)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-126)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-127)=================================[1m Tool Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-128)Name: multiply
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-129)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-130)96
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-131)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-132)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-133)Update from subgraph multiplication_expert:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-134)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-135)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-136)Update from node agent:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-137)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-138)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-139)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-140)
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-141)The final result is 96. Here's the complete calculation:
[](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__codelineno-19-142)(3 + 5) * 12 = 8 * 12 = 96

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to transform inputs and outputs of a subgraph  ](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/) [ Next  How to build a multi-agent network  ](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/agent-handoffs/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
