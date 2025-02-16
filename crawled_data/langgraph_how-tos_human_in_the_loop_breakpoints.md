---
url: https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#how-to-add-breakpoints)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to add breakpoints 

[ ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/?q= "Share")

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
          * Human-in-the-loop  Human-in-the-loop 
            * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraph/how-tos#human-in-the-loop)
            * How to add breakpoints  [ How to add breakpoints  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#setup)
              * [ Simple Usage  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#simple-usage)
              * [ Agent  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#agent)
              * [ Interacting with the Agent  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#interacting-with-the-agent)
            * [ How to add dynamic breakpoints with NodeInterrupt  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/dynamic_breakpoints/)
            * [ How to edit graph state  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/)
            * [ How to wait for user input using interrupt  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/)
            * [ How to view and update past graph state  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/)
            * [ How to Review Tool Calls  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#setup)
  * [ Simple Usage  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#simple-usage)
  * [ Agent  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#agent)
  * [ Interacting with the Agent  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#interacting-with-the-agent)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraph/how-tos#human-in-the-loop)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/human_in_the_loop/breakpoints.ipynb "Edit this page")

# How to add breakpoints[¶](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#how-to-add-breakpoints "Permanent link")

Prerequisites

This guide assumes familiarity with the following concepts:

  * [Breakpoints](https://langchain-ai.github.io/langgraph/concepts/breakpoints)
  * [LangGraph Glossary](https://langchain-ai.github.io/langgraph/concepts/low_level)



Human-in-the-loop (HIL) interactions are crucial for [agentic systems](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#human-in-the-loop). [Breakpoints](https://langchain-ai.github.io/langgraph/concepts/low_level/#breakpoints) are a common HIL interaction pattern, allowing the graph to stop at specific steps and seek human approval before proceeding (e.g., for sensitive actions). 

Breakpoints are built on top of LangGraph [checkpoints](https://langchain-ai.github.io/langgraph/concepts/low_level/#checkpointer), which save the graph's state after each node execution. Checkpoints are saved in [threads](https://langchain-ai.github.io/langgraph/concepts/low_level/#threads) that preserve graph state and can be accessed after a graph has finished execution. This allows for graph execution to pause at specific points, await human approval, and then resume execution from the last checkpoint.

![approval.png]()

## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#setup "Permanent link")

First we need to install the packages required

```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-0-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-0-2)%pip install --quiet -U langgraph langchain_anthropic

```


Next, we need to set API keys for Anthropic (the LLM we will use)

```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-1-1)importgetpass
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-1-2)importos
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-1-5)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-1-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-1-7)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-1-8)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-1-10)_set_env("ANTHROPIC_API_KEY")

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-2-1)ANTHROPIC_API_KEY: ········

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Simple Usage[¶](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#simple-usage "Permanent link")

Let's look at very basic usage of this.

Below, we do two things:

1) We specify the [breakpoint](https://langchain-ai.github.io/langgraph/concepts/low_level/#breakpoints) using `interrupt_before` the specified step.

2) We set up a [checkpointer](https://langchain-ai.github.io/langgraph/concepts/low_level/#checkpointer) to save the state of the graph.

```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-3-1)fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-3-2)fromlanggraph.graphimport StateGraph, START, END
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-3-3)fromlanggraph.checkpoint.memoryimport MemorySaver
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-3-4)fromIPython.displayimport Image, display
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-3-5)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-3-6)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-3-7)classState(TypedDict):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-3-8)  input: str
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-3-9)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-3-10)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-3-11)defstep_1(state):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-3-12)  print("---Step 1---")
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-3-13)  pass
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-3-14)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-3-15)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-3-16)defstep_2(state):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-3-17)  print("---Step 2---")
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-3-18)  pass
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-3-19)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-3-20)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-3-21)defstep_3(state):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-3-22)  print("---Step 3---")
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-3-23)  pass
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-3-24)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-3-25)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-3-26)builder = StateGraph(State)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-3-27)builder.add_node("step_1", step_1)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-3-28)builder.add_node("step_2", step_2)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-3-29)builder.add_node("step_3", step_3)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-3-30)builder.add_edge(START, "step_1")
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-3-31)builder.add_edge("step_1", "step_2")
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-3-32)builder.add_edge("step_2", "step_3")
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-3-33)builder.add_edge("step_3", END)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-3-34)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-3-35)# Set up memory
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-3-36)memory = MemorySaver()
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-3-37)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-3-38)# Add
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-3-39)graph = builder.compile(checkpointer=memory, interrupt_before=["step_3"])
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-3-40)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-3-41)# View
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-3-42)display(Image(graph.get_graph().draw_mermaid_png()))

```


API Reference: [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END) | [MemorySaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.MemorySaver)

![]()

We create a [thread ID](https://langchain-ai.github.io/langgraph/concepts/low_level/#threads) for the checkpointer.

We run until step 3, as defined with `interrupt_before`. 

After the user input / approval, [we resume execution](https://langchain-ai.github.io/langgraph/concepts/low_level/#breakpoints) by invoking the graph with `None`. 

```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-4-1)# Input
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-4-2)initial_input = {"input": "hello world"}
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-4-3)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-4-4)# Thread
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-4-5)thread = {"configurable": {"thread_id": "1"}}
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-4-6)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-4-7)# Run the graph until the first interruption
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-4-8)for event in graph.stream(initial_input, thread, stream_mode="values"):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-4-9)  print(event)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-4-10)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-4-11)try:
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-4-12)  user_approval = input("Do you want to go to Step 3? (yes/no): ")
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-4-13)except:
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-4-14)  user_approval = "yes"
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-4-15)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-4-16)if user_approval.lower() == "yes":
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-4-17)  # If approved, continue the graph execution
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-4-18)  for event in graph.stream(None, thread, stream_mode="values"):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-4-19)    print(event)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-4-20)else:
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-4-21)  print("Operation cancelled by user.")

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-5-1){'input': 'hello world'}
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-5-2)---Step 1---
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-5-3)---Step 2---
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-5-4)``````output
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-5-5)Do you want to go to Step 3? (yes/no): yes
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-5-6)``````output
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-5-7)---Step 3---

```


## Agent[¶](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#agent "Permanent link")

In the context of agents, breakpoints are useful to manually approve certain agent actions.

To show this, we will build a relatively simple ReAct-style agent that does tool calling. 

We'll add a breakpoint before the `action` node is called. 

```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-1)# Set up the tool
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-2)fromlangchain_anthropicimport ChatAnthropic
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-3)fromlangchain_core.toolsimport tool
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-4)fromlanggraph.graphimport MessagesState, START
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-5)fromlanggraph.prebuiltimport ToolNode
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-6)fromlanggraph.graphimport END, StateGraph
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-7)fromlanggraph.checkpoint.memoryimport MemorySaver
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-8)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-9)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-10)@tool
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-11)defsearch(query: str):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-12)"""Call to surf the web."""
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-13)  # This is a placeholder for the actual implementation
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-14)  # Don't let the LLM know this though 😊
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-15)  return [
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-16)    "It's sunny in San Francisco, but you better look out if you're a Gemini 😈."
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-17)  ]
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-18)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-19)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-20)tools = [search]
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-21)tool_node = ToolNode(tools)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-22)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-23)# Set up the model
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-24)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-25)model = ChatAnthropic(model="claude-3-5-sonnet-20240620")
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-26)model = model.bind_tools(tools)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-27)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-28)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-29)# Define nodes and conditional edges
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-30)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-31)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-32)# Define the function that determines whether to continue or not
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-33)defshould_continue(state):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-34)  messages = state["messages"]
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-35)  last_message = messages[-1]
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-36)  # If there is no function call, then we finish
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-37)  if not last_message.tool_calls:
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-38)    return "end"
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-39)  # Otherwise if there is, we continue
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-40)  else:
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-41)    return "continue"
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-42)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-43)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-44)# Define the function that calls the model
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-45)defcall_model(state):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-46)  messages = state["messages"]
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-47)  response = model.invoke(messages)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-48)  # We return a list, because this will get added to the existing list
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-49)  return {"messages": [response]}
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-50)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-51)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-52)# Define a new graph
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-53)workflow = StateGraph(MessagesState)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-54)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-55)# Define the two nodes we will cycle between
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-56)workflow.add_node("agent", call_model)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-57)workflow.add_node("action", tool_node)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-58)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-59)# Set the entrypoint as `agent`
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-60)# This means that this node is the first one called
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-61)workflow.add_edge(START, "agent")
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-62)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-63)# We now add a conditional edge
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-64)workflow.add_conditional_edges(
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-65)  # First, we define the start node. We use `agent`.
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-66)  # This means these are the edges taken after the `agent` node is called.
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-67)  "agent",
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-68)  # Next, we pass in the function that will determine which node is called next.
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-69)  should_continue,
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-70)  # Finally we pass in a mapping.
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-71)  # The keys are strings, and the values are other nodes.
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-72)  # END is a special node marking that the graph should finish.
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-73)  # What will happen is we will call `should_continue`, and then the output of that
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-74)  # will be matched against the keys in this mapping.
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-75)  # Based on which one it matches, that node will then be called.
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-76)  {
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-77)    # If `tools`, then we call the tool node.
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-78)    "continue": "action",
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-79)    # Otherwise we finish.
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-80)    "end": END,
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-81)  },
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-82))
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-83)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-84)# We now add a normal edge from `tools` to `agent`.
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-85)# This means that after `tools` is called, `agent` node is called next.
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-86)workflow.add_edge("action", "agent")
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-87)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-88)# Set up memory
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-89)memory = MemorySaver()
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-90)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-91)# Finally, we compile it!
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-92)# This compiles it into a LangChain Runnable,
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-93)# meaning you can use it as you would any other runnable
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-94)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-95)# We add in `interrupt_before=["action"]`
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-96)# This will add a breakpoint before the `action` node is called
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-97)app = workflow.compile(checkpointer=memory, interrupt_before=["action"])
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-98)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-6-99)display(Image(app.get_graph().draw_mermaid_png()))

```


API Reference: [ChatAnthropic](https://python.langchain.com/api_reference/anthropic/chat_models/langchain_anthropic.chat_models.ChatAnthropic.html) | [tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [ToolNode](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.ToolNode) | [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [MemorySaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.MemorySaver)

![]()

## Interacting with the Agent[¶](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#interacting-with-the-agent "Permanent link")

We can now interact with the agent.

We see that it stops before calling a tool, because `interrupt_before` is set before the `action` node.

```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-7-1)fromlangchain_core.messagesimport HumanMessage
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-7-2)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-7-3)thread = {"configurable": {"thread_id": "3"}}
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-7-4)inputs = [HumanMessage(content="search for the weather in sf now")]
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-7-5)for event in app.stream({"messages": inputs}, thread, stream_mode="values"):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-7-6)  event["messages"][-1].pretty_print()

```


API Reference: [HumanMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.human.HumanMessage.html)

```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-8-1)================================[1m Human Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-8-2)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-8-3)search for the weather in sf now
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-8-4)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-8-5)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-8-6)[{'text': "Certainly! I'll search for the current weather in San Francisco for you. Let me use the search function to find this information.", 'type': 'text'}, {'text': None, 'type': 'tool_use', 'id': 'toolu_011ezBx5hKKjVJwqnECNPyyC', 'name': 'search', 'input': {'query': 'current weather in San Francisco'}}]

```


**Resume**

We can now call the agent again with no inputs to continue.

This will run the tool as requested.

Running an interrupted graph with `None` in the inputs means to `proceed as if the interruption didn't occur.`

```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-9-1)for event in app.stream(None, thread, stream_mode="values"):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-9-2)  event["messages"][-1].pretty_print()

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-10-1)=================================[1m Tool Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-10-2)Name: search
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-10-3)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-10-4)["It's sunny in San Francisco, but you better look out if you're a Gemini \ud83d\ude08."]
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-10-5)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-10-6)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-10-7)Based on the search results, I can provide you with information about the current weather in San Francisco:
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-10-8)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-10-9)The weather in San Francisco right now is sunny. 
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-10-10)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-10-11)It's worth noting that the search result includes a playful reference to astrology, suggesting that Geminis should "look out." However, this is likely just a humorous addition and not related to the actual weather conditions.
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-10-12)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__codelineno-10-13)Is there anything else you'd like to know about the weather in San Francisco or any other location?

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to add semantic search to your agent's memory  ](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/) [ Next  How to add dynamic breakpoints with NodeInterrupt  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/dynamic_breakpoints/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
