---
url: https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#how-to-review-tool-calls)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to Review Tool Calls 

[ ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/?q= "Share")

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
          * Human-in-the-loop  Human-in-the-loop 
            * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraph/how-tos#human-in-the-loop)
            * [ How to add breakpoints  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/)
            * [ How to add dynamic breakpoints with NodeInterrupt  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/dynamic_breakpoints/)
            * [ How to edit graph state  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/)
            * [ How to wait for user input using interrupt  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/)
            * [ How to view and update past graph state  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/)
            * How to Review Tool Calls  [ How to Review Tool Calls  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#setup)
              * [ Simple Usage  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#simple-usage)
              * [ Example with no review  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#example-with-no-review)
              * [ Example of approving tool  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#example-of-approving-tool)
              * [ Edit Tool Call  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#edit-tool-call)
              * [ Give feedback to a tool call  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#give-feedback-to-a-tool-call)
            * [ How to wait for user input (Functional API)  ](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/)
            * [ How to review tool calls (Functional API)  ](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#setup)
  * [ Simple Usage  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#simple-usage)
  * [ Example with no review  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#example-with-no-review)
  * [ Example of approving tool  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#example-of-approving-tool)
  * [ Edit Tool Call  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#edit-tool-call)
  * [ Give feedback to a tool call  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#give-feedback-to-a-tool-call)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraph/how-tos#human-in-the-loop)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/human_in_the_loop/review-tool-calls.ipynb "Edit this page")

# How to Review Tool Calls[¶](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#how-to-review-tool-calls "Permanent link")

Prerequisites

This guide assumes familiarity with the following concepts:

  * [Tool calling](https://python.langchain.com/docs/concepts/tool_calling/)
  * [Human-in-the-loop](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop)
  * [LangGraph Glossary](https://langchain-ai.github.io/langgraph/concepts/low_level)



Human-in-the-loop (HIL) interactions are crucial for [agentic systems](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts). A common pattern is to add some human in the loop step after certain tool calls. These tool calls often lead to either a function call or saving of some information. Examples include:

  * A tool call to execute SQL, which will then be run by the tool
  * A tool call to generate a summary, which will then be saved to the State of the graph



Note that using tool calls is common **whether actually calling tools or not**.

There are typically a few different interactions you may want to do here:

  1. Approve the tool call and continue
  2. Modify the tool call manually and then continue
  3. Give natural language feedback, and then pass that back to the agent



We can implement these in LangGraph using the `interrupt()`[](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.interrupt) function. `interrupt` allows us to stop graph execution to collect input from a user and continue execution with collected input:

```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-0-1)defhuman_review_node(state) -> Command[Literal["call_llm", "run_tool"]]:
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-0-2)  # this is the value we'll be providing via Command(resume=<human_review>)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-0-3)  human_review = interrupt(
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-0-4)    {
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-0-5)      "question": "Is this correct?",
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-0-6)      # Surface tool calls for review
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-0-7)      "tool_call": tool_call
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-0-8)    }
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-0-9)  )
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-0-10)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-0-11)  review_action, review_data = human_review
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-0-12)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-0-13)  # Approve the tool call and continue
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-0-14)  if review_action == "continue":
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-0-15)    return Command(goto="run_tool")
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-0-16)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-0-17)  # Modify the tool call manually and then continue
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-0-18)  elif review_action == "update":
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-0-19)    ...
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-0-20)    updated_msg = get_updated_msg(review_data)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-0-21)    return Command(goto="run_tool", update={"messages": [updated_message]})
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-0-22)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-0-23)  # Give natural language feedback, and then pass that back to the agent
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-0-24)  elif review_action == "feedback":
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-0-25)    ...
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-0-26)    feedback_msg = get_feedback_msg(review_data)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-0-27)    return Command(goto="call_llm", update={"messages": [feedback_msg]})

```


## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#setup "Permanent link")

First we need to install the packages required

```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-1-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-1-2)%pip install --quiet -U langgraph langchain_anthropic

```


Next, we need to set API keys for Anthropic (the LLM we will use)

```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-2-1)importgetpass
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-2-2)importos
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-2-3)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-2-4)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-2-5)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-2-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-2-7)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-2-8)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-2-9)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-2-10)_set_env("ANTHROPIC_API_KEY")

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-3-1)ANTHROPIC_API_KEY: ········

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Simple Usage[¶](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#simple-usage "Permanent link")

Let's set up a very simple graph that facilitates this. First, we will have an LLM call that decides what action to take. Then we go to a human node. This node actually doesn't do anything - the idea is that we interrupt before this node and then apply any updates to the state. After that, we check the state and either route back to the LLM or to the correct tool.

Let's see this in action!

```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-1)fromtyping_extensionsimport TypedDict, Literal
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-2)fromlanggraph.graphimport StateGraph, START, END, MessagesState
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-3)fromlanggraph.checkpoint.memoryimport MemorySaver
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-4)fromlanggraph.typesimport Command, interrupt
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-5)fromlangchain_anthropicimport ChatAnthropic
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-6)fromlangchain_core.toolsimport tool
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-7)fromlangchain_core.messagesimport AIMessage
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-8)fromIPython.displayimport Image, display
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-9)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-10)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-11)@tool
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-12)defweather_search(city: str):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-13)"""Search for the weather"""
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-14)  print("----")
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-15)  print(f"Searching for: {city}")
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-16)  print("----")
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-17)  return "Sunny!"
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-18)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-19)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-20)model = ChatAnthropic(model_name="claude-3-5-sonnet-latest").bind_tools(
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-21)  [weather_search]
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-22))
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-23)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-24)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-25)classState(MessagesState):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-26)"""Simple state."""
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-27)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-28)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-29)defcall_llm(state):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-30)  return {"messages": [model.invoke(state["messages"])]}
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-31)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-32)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-33)defhuman_review_node(state) -> Command[Literal["call_llm", "run_tool"]]:
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-34)  last_message = state["messages"][-1]
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-35)  tool_call = last_message.tool_calls[-1]
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-36)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-37)  # this is the value we'll be providing via Command(resume=<human_review>)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-38)  human_review = interrupt(
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-39)    {
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-40)      "question": "Is this correct?",
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-41)      # Surface tool calls for review
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-42)      "tool_call": tool_call,
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-43)    }
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-44)  )
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-45)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-46)  review_action = human_review["action"]
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-47)  review_data = human_review.get("data")
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-48)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-49)  # if approved, call the tool
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-50)  if review_action == "continue":
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-51)    return Command(goto="run_tool")
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-52)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-53)  # update the AI message AND call tools
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-54)  elif review_action == "update":
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-55)    updated_message = {
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-56)      "role": "ai",
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-57)      "content": last_message.content,
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-58)      "tool_calls": [
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-59)        {
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-60)          "id": tool_call["id"],
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-61)          "name": tool_call["name"],
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-62)          # This the update provided by the human
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-63)          "args": review_data,
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-64)        }
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-65)      ],
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-66)      # This is important - this needs to be the same as the message you replacing!
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-67)      # Otherwise, it will show up as a separate message
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-68)      "id": last_message.id,
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-69)    }
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-70)    return Command(goto="run_tool", update={"messages": [updated_message]})
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-71)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-72)  # provide feedback to LLM
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-73)  elif review_action == "feedback":
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-74)    # NOTE: we're adding feedback message as a ToolMessage
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-75)    # to preserve the correct order in the message history
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-76)    # (AI messages with tool calls need to be followed by tool call messages)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-77)    tool_message = {
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-78)      "role": "tool",
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-79)      # This is our natural language feedback
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-80)      "content": review_data,
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-81)      "name": tool_call["name"],
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-82)      "tool_call_id": tool_call["id"],
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-83)    }
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-84)    return Command(goto="call_llm", update={"messages": [tool_message]})
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-85)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-86)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-87)defrun_tool(state):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-88)  new_messages = []
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-89)  tools = {"weather_search": weather_search}
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-90)  tool_calls = state["messages"][-1].tool_calls
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-91)  for tool_call in tool_calls:
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-92)    tool = tools[tool_call["name"]]
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-93)    result = tool.invoke(tool_call["args"])
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-94)    new_messages.append(
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-95)      {
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-96)        "role": "tool",
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-97)        "name": tool_call["name"],
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-98)        "content": result,
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-99)        "tool_call_id": tool_call["id"],
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-100)      }
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-101)    )
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-102)  return {"messages": new_messages}
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-103)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-104)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-105)defroute_after_llm(state) -> Literal[END, "human_review_node"]:
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-106)  if len(state["messages"][-1].tool_calls) == 0:
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-107)    return END
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-108)  else:
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-109)    return "human_review_node"
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-110)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-111)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-112)builder = StateGraph(State)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-113)builder.add_node(call_llm)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-114)builder.add_node(run_tool)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-115)builder.add_node(human_review_node)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-116)builder.add_edge(START, "call_llm")
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-117)builder.add_conditional_edges("call_llm", route_after_llm)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-118)builder.add_edge("run_tool", "call_llm")
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-119)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-120)# Set up memory
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-121)memory = MemorySaver()
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-122)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-123)# Add
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-124)graph = builder.compile(checkpointer=memory)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-125)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-126)# View
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-4-127)display(Image(graph.get_graph().draw_mermaid_png()))

```


API Reference: [ChatAnthropic](https://python.langchain.com/api_reference/anthropic/chat_models/langchain_anthropic.chat_models.ChatAnthropic.html) | [tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html) | [AIMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.AIMessage.html) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END) | [MemorySaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.MemorySaver) | [Command](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Command) | [interrupt](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.interrupt)

![]()

## Example with no review[¶](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#example-with-no-review "Permanent link")

Let's look at an example when no review is required (because no tools are called)

```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-5-1)# Input
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-5-2)initial_input = {"messages": [{"role": "user", "content": "hi!"}]}
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-5-3)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-5-4)# Thread
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-5-5)thread = {"configurable": {"thread_id": "1"}}
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-5-6)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-5-7)# Run the graph until the first interruption
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-5-8)for event in graph.stream(initial_input, thread, stream_mode="updates"):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-5-9)  print(event)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-5-10)  print("\n")

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-6-1){'call_llm': {'messages': [AIMessage(content="Hello! I'm here to help you. I can assist you with checking the weather in different cities using the weather search tool. Would you like to know the weather for a specific city? Just let me know which city you're interested in!", additional_kwargs={}, response_metadata={'id': 'msg_01XHvA3ZWpsq4PdyiruWFLBs', 'model': 'claude-3-5-sonnet-20241022', 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 374, 'output_tokens': 52}}, id='run-c3ff5fea-0135-4d66-8ec1-f8ed6a88356b-0', usage_metadata={'input_tokens': 374, 'output_tokens': 52, 'total_tokens': 426, 'input_token_details': {}})]}}

```


If we check the state, we can see that it is finished 

## Example of approving tool[¶](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#example-of-approving-tool "Permanent link")

Let's now look at what it looks like to approve a tool call

```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-7-1)# Input
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-7-2)initial_input = {"messages": [{"role": "user", "content": "what's the weather in sf?"}]}
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-7-3)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-7-4)# Thread
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-7-5)thread = {"configurable": {"thread_id": "2"}}
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-7-6)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-7-7)# Run the graph until the first interruption
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-7-8)for event in graph.stream(initial_input, thread, stream_mode="updates"):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-7-9)  print(event)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-7-10)  print("\n")

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-8-1){'call_llm': {'messages': [AIMessage(content=[{'text': "I'll help you check the weather in San Francisco.", 'type': 'text'}, {'id': 'toolu_01Kn67GmQAA3BEF1cfYdNW3c', 'input': {'city': 'sf'}, 'name': 'weather_search', 'type': 'tool_use'}], additional_kwargs={}, response_metadata={'id': 'msg_013eJXUAEA2ANvYLkDUQFRPo', 'model': 'claude-3-5-sonnet-20241022', 'stop_reason': 'tool_use', 'stop_sequence': None, 'usage': {'input_tokens': 379, 'output_tokens': 65}}, id='run-e8174b94-f681-4688-967f-a32295412f91-0', tool_calls=[{'name': 'weather_search', 'args': {'city': 'sf'}, 'id': 'toolu_01Kn67GmQAA3BEF1cfYdNW3c', 'type': 'tool_call'}], usage_metadata={'input_tokens': 379, 'output_tokens': 65, 'total_tokens': 444, 'input_token_details': {}})]}}
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-8-2)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-8-3)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-8-4){'__interrupt__': (Interrupt(value={'question': 'Is this correct?', 'tool_call': {'name': 'weather_search', 'args': {'city': 'sf'}, 'id': 'toolu_01Kn67GmQAA3BEF1cfYdNW3c', 'type': 'tool_call'}}, resumable=True, ns=['human_review_node:be252162-5b29-0a98-1ed2-c807c1fc64c6'], when='during'),)}

```


If we now check, we can see that it is waiting on human review 

```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-9-1)print("Pending Executions!")
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-9-2)print(graph.get_state(thread).next)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-10-1)Pending Executions!
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-10-2)('human_review_node',)

```


To approve the tool call, we can just continue the thread with no edits. To do so, we need to let `human_review_node` know what value to use for the `human_review` variable we defined inside the node. We can provide this value by invoking the graph with a `Command(resume=<human_review>)` input. Since we're approving the tool call, we'll provide `resume` value of `{"action": "continue"}` to navigate to `run_tool` node: 

```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-11-1)for event in graph.stream(
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-11-2)  # provide value
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-11-3)  Command(resume={"action": "continue"}),
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-11-4)  thread,
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-11-5)  stream_mode="updates",
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-11-6)):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-11-7)  print(event)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-11-8)  print("\n")

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-12-1){'human_review_node': None}
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-12-2)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-12-3)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-12-4)----
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-12-5)Searching for: sf
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-12-6)----
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-12-7){'run_tool': {'messages': [{'role': 'tool', 'name': 'weather_search', 'content': 'Sunny!', 'tool_call_id': 'toolu_01Kn67GmQAA3BEF1cfYdNW3c'}]}}
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-12-8)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-12-9)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-12-10){'call_llm': {'messages': [AIMessage(content="According to the search, it's sunny in San Francisco today!", additional_kwargs={}, response_metadata={'id': 'msg_01FJTbC8oK5fkD73rUBmAtUx', 'model': 'claude-3-5-sonnet-20241022', 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 457, 'output_tokens': 17}}, id='run-c21af72d-3cc5-4b74-bb7c-fbeb8f88bd6d-0', usage_metadata={'input_tokens': 457, 'output_tokens': 17, 'total_tokens': 474, 'input_token_details': {}})]}}

```


## Edit Tool Call[¶](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#edit-tool-call "Permanent link")

Let's now say we want to edit the tool call. E.g. change some of the parameters (or even the tool called!) but then execute that tool.

```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-13-1)# Input
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-13-2)initial_input = {"messages": [{"role": "user", "content": "what's the weather in sf?"}]}
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-13-3)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-13-4)# Thread
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-13-5)thread = {"configurable": {"thread_id": "3"}}
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-13-6)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-13-7)# Run the graph until the first interruption
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-13-8)for event in graph.stream(initial_input, thread, stream_mode="updates"):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-13-9)  print(event)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-13-10)  print("\n")

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-14-1){'call_llm': {'messages': [AIMessage(content=[{'text': "I'll help you check the weather in San Francisco.", 'type': 'text'}, {'id': 'toolu_013eUXow3jwM6eekcDJdrjDa', 'input': {'city': 'sf'}, 'name': 'weather_search', 'type': 'tool_use'}], additional_kwargs={}, response_metadata={'id': 'msg_013ruFpCRNZKX3cDeBAH8rEb', 'model': 'claude-3-5-sonnet-20241022', 'stop_reason': 'tool_use', 'stop_sequence': None, 'usage': {'input_tokens': 379, 'output_tokens': 65}}, id='run-13df3982-ce6d-4fe2-9e5c-ea6ce30a63e4-0', tool_calls=[{'name': 'weather_search', 'args': {'city': 'sf'}, 'id': 'toolu_013eUXow3jwM6eekcDJdrjDa', 'type': 'tool_call'}], usage_metadata={'input_tokens': 379, 'output_tokens': 65, 'total_tokens': 444, 'input_token_details': {}})]}}
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-14-2)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-14-3)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-14-4){'__interrupt__': (Interrupt(value={'question': 'Is this correct?', 'tool_call': {'name': 'weather_search', 'args': {'city': 'sf'}, 'id': 'toolu_013eUXow3jwM6eekcDJdrjDa', 'type': 'tool_call'}}, resumable=True, ns=['human_review_node:da717c23-60a0-2a1a-45de-cac5cff308bb'], when='during'),)}

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-15-1)print("Pending Executions!")
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-15-2)print(graph.get_state(thread).next)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-16-1)Pending Executions!
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-16-2)('human_review_node',)

```


To do this, we will use `Command` with a different resume value of `{"action": "update", "data": <tool call args>}`. This will do the following: 

  * combine existing tool call with user-provided tool call arguments and update the existing AI message with the new tool call
  * navigate to `run_tool` node with the updated AI message and continue execution



```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-17-1)# Let's now continue executing from here
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-17-2)for event in graph.stream(
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-17-3)  Command(resume={"action": "update", "data": {"city": "San Francisco, USA"}}),
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-17-4)  thread,
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-17-5)  stream_mode="updates",
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-17-6)):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-17-7)  print(event)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-17-8)  print("\n")

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-18-1){'human_review_node': {'messages': [{'role': 'ai', 'content': [{'text': "I'll help you check the weather in San Francisco.", 'type': 'text'}, {'id': 'toolu_013eUXow3jwM6eekcDJdrjDa', 'input': {'city': 'sf'}, 'name': 'weather_search', 'type': 'tool_use'}], 'tool_calls': [{'id': 'toolu_013eUXow3jwM6eekcDJdrjDa', 'name': 'weather_search', 'args': {'city': 'San Francisco, USA'}}], 'id': 'run-13df3982-ce6d-4fe2-9e5c-ea6ce30a63e4-0'}]}}
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-18-2)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-18-3)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-18-4)----
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-18-5)Searching for: San Francisco, USA
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-18-6)----
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-18-7){'run_tool': {'messages': [{'role': 'tool', 'name': 'weather_search', 'content': 'Sunny!', 'tool_call_id': 'toolu_013eUXow3jwM6eekcDJdrjDa'}]}}
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-18-8)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-18-9)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-18-10){'call_llm': {'messages': [AIMessage(content="According to the search, it's sunny in San Francisco right now!", additional_kwargs={}, response_metadata={'id': 'msg_01QssVtxXPqr8NWjYjTaiHqN', 'model': 'claude-3-5-sonnet-20241022', 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 460, 'output_tokens': 18}}, id='run-8ab865c8-cc9e-4300-8e1d-9eb673e8445c-0', usage_metadata={'input_tokens': 460, 'output_tokens': 18, 'total_tokens': 478, 'input_token_details': {}})]}}

```


## Give feedback to a tool call[¶](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#give-feedback-to-a-tool-call "Permanent link")

Sometimes, you may not want to execute a tool call, but you also may not want to ask the user to manually modify the tool call. In that case it may be better to get natural language feedback from the user. You can then insert this feedback as a mock **RESULT** of the tool call.

There are multiple ways to do this:

  1. You could add a new message to the state (representing the "result" of a tool call)
  2. You could add TWO new messages to the state - one representing an "error" from the tool call, other HumanMessage representing the feedback



Both are similar in that they involve adding messages to the state. The main difference lies in the logic AFTER the `human_review_node` and how it handles different types of messages.

For this example we will just add a single tool call representing the feedback (see `human_review_node` implementation). Let's see this in action!

```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-19-1)# Input
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-19-2)initial_input = {"messages": [{"role": "user", "content": "what's the weather in sf?"}]}
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-19-3)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-19-4)# Thread
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-19-5)thread = {"configurable": {"thread_id": "4"}}
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-19-6)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-19-7)# Run the graph until the first interruption
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-19-8)for event in graph.stream(initial_input, thread, stream_mode="updates"):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-19-9)  print(event)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-19-10)  print("\n")

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-20-1){'call_llm': {'messages': [AIMessage(content=[{'text': "I'll help you check the weather in San Francisco.", 'type': 'text'}, {'id': 'toolu_01QxXNTCasnNLQCGAiVoNUBe', 'input': {'city': 'sf'}, 'name': 'weather_search', 'type': 'tool_use'}], additional_kwargs={}, response_metadata={'id': 'msg_01DjwkVxgfqT2K329rGkycx6', 'model': 'claude-3-5-sonnet-20241022', 'stop_reason': 'tool_use', 'stop_sequence': None, 'usage': {'input_tokens': 379, 'output_tokens': 65}}, id='run-c57bee36-9f5f-4d2e-85df-758b56d3cc05-0', tool_calls=[{'name': 'weather_search', 'args': {'city': 'sf'}, 'id': 'toolu_01QxXNTCasnNLQCGAiVoNUBe', 'type': 'tool_call'}], usage_metadata={'input_tokens': 379, 'output_tokens': 65, 'total_tokens': 444, 'input_token_details': {}})]}}
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-20-2)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-20-3)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-20-4){'__interrupt__': (Interrupt(value={'question': 'Is this correct?', 'tool_call': {'name': 'weather_search', 'args': {'city': 'sf'}, 'id': 'toolu_01QxXNTCasnNLQCGAiVoNUBe', 'type': 'tool_call'}}, resumable=True, ns=['human_review_node:47a3f541-b630-5f8a-32d7-5a44826d99da'], when='during'),)}

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-21-1)print("Pending Executions!")
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-21-2)print(graph.get_state(thread).next)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-22-1)Pending Executions!
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-22-2)('human_review_node',)

```


To do this, we will use `Command` with a different resume value of `{"action": "feedback", "data": <feedback string>}`. This will do the following: 

  * create a new tool message that combines existing tool call from LLM with the with user-provided feedback as content
  * navigate to `call_llm` node with the updated tool message and continue execution



```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-23-1)# Let's now continue executing from here
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-23-2)for event in graph.stream(
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-23-3)  # provide our natural language feedback!
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-23-4)  Command(
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-23-5)    resume={
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-23-6)      "action": "feedback",
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-23-7)      "data": "User requested changes: use <city, country> format for location",
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-23-8)    }
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-23-9)  ),
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-23-10)  thread,
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-23-11)  stream_mode="updates",
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-23-12)):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-23-13)  print(event)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-23-14)  print("\n")

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-24-1){'human_review_node': {'messages': [{'role': 'tool', 'content': 'User requested changes: use <city, country> format for location', 'name': 'weather_search', 'tool_call_id': 'toolu_01QxXNTCasnNLQCGAiVoNUBe'}]}}
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-24-2)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-24-3)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-24-4){'call_llm': {'messages': [AIMessage(content=[{'text': 'Let me try again with the full city name.', 'type': 'text'}, {'id': 'toolu_01WBGTKBWusaPNZYJi5LKmeQ', 'input': {'city': 'San Francisco, USA'}, 'name': 'weather_search', 'type': 'tool_use'}], additional_kwargs={}, response_metadata={'id': 'msg_0141KCdx6KhJmWXyYwAYGvmj', 'model': 'claude-3-5-sonnet-20241022', 'stop_reason': 'tool_use', 'stop_sequence': None, 'usage': {'input_tokens': 468, 'output_tokens': 68}}, id='run-60c8267a-52c7-4b6e-87ca-16aa3bd6266b-0', tool_calls=[{'name': 'weather_search', 'args': {'city': 'San Francisco, USA'}, 'id': 'toolu_01WBGTKBWusaPNZYJi5LKmeQ', 'type': 'tool_call'}], usage_metadata={'input_tokens': 468, 'output_tokens': 68, 'total_tokens': 536, 'input_token_details': {}})]}}
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-24-5)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-24-6)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-24-7){'__interrupt__': (Interrupt(value={'question': 'Is this correct?', 'tool_call': {'name': 'weather_search', 'args': {'city': 'San Francisco, USA'}, 'id': 'toolu_01WBGTKBWusaPNZYJi5LKmeQ', 'type': 'tool_call'}}, resumable=True, ns=['human_review_node:621fc4a9-bbf1-9a99-f50b-3bf91675234e'], when='during'),)}

```


We can see that we now get to another interrupt - because it went back to the model and got an entirely new prediction of what to call. Let's now approve this one and continue. 

```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-25-1)print("Pending Executions!")
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-25-2)print(graph.get_state(thread).next)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-26-1)Pending Executions!
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-26-2)('human_review_node',)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-27-1)for event in graph.stream(
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-27-2)  Command(resume={"action": "continue"}), thread, stream_mode="updates"
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-27-3)):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-27-4)  print(event)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-27-5)  print("\n")

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-28-1){'human_review_node': None}
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-28-2)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-28-3)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-28-4)----
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-28-5)Searching for: San Francisco, USA
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-28-6)----
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-28-7){'run_tool': {'messages': [{'role': 'tool', 'name': 'weather_search', 'content': 'Sunny!', 'tool_call_id': 'toolu_01WBGTKBWusaPNZYJi5LKmeQ'}]}}
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-28-8)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-28-9)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__codelineno-28-10){'call_llm': {'messages': [AIMessage(content='The weather in San Francisco is sunny!', additional_kwargs={}, response_metadata={'id': 'msg_01JrfZd8SYyH51Q8rhZuaC3W', 'model': 'claude-3-5-sonnet-20241022', 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 549, 'output_tokens': 12}}, id='run-09a198b2-79fa-484d-9d9d-f12432978488-0', usage_metadata={'input_tokens': 549, 'output_tokens': 12, 'total_tokens': 561, 'input_token_details': {}})]}}

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to view and update past graph state  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/) [ Next  How to wait for user input (Functional API)  ](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
