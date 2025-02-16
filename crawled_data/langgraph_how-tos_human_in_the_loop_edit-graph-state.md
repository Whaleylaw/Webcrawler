---
url: https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#how-to-edit-graph-state)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to edit graph state 

[ ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/?q= "Share")

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
            * How to edit graph state  [ How to edit graph state  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#setup)
              * [ Simple Usage  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#simple-usage)
              * [ Agent  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#agent)
              * [ Interacting with the Agent  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#interacting-with-the-agent)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#setup)
  * [ Simple Usage  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#simple-usage)
  * [ Agent  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#agent)
  * [ Interacting with the Agent  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#interacting-with-the-agent)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraph/how-tos#human-in-the-loop)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/human_in_the_loop/edit-graph-state.ipynb "Edit this page")

# How to edit graph state[¶](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#how-to-edit-graph-state "Permanent link")

Prerequisites

  * [Human-in-the-loop](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop)
  * [Breakpoints](https://langchain-ai.github.io/langgraph/concepts/breakpoints)
  * [LangGraph Glossary](https://langchain-ai.github.io/langgraph/concepts/low_level)



Human-in-the-loop (HIL) interactions are crucial for [agentic systems](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#human-in-the-loop). Manually updating the graph state a common HIL interaction pattern, allowing the human to edit actions (e.g., what tool is being called or how it is being called).

We can implement this in LangGraph using a [breakpoint](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/): breakpoints allow us to interrupt graph execution before a specific step. At this breakpoint, we can manually update the graph state and then resume from that spot to continue. 

![edit_graph_state.png]()

## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#setup "Permanent link")

First we need to install the packages required

```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-0-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-0-2)%pip install --quiet -U langgraph langchain_anthropic

```


Next, we need to set API keys for Anthropic (the LLM we will use)

```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-1-1)importgetpass
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-1-2)importos
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-1-5)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-1-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-1-7)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-1-8)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-1-10)_set_env("ANTHROPIC_API_KEY")

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-2-1)ANTHROPIC_API_KEY: ········

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Simple Usage[¶](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#simple-usage "Permanent link")

Let's look at very basic usage of this.

Below, we do three things:

1) We specify the [breakpoint](https://langchain-ai.github.io/langgraph/concepts/low_level/#breakpoints) using `interrupt_before` a specified step (node).

2) We set up a [checkpointer](https://langchain-ai.github.io/langgraph/concepts/low_level/#checkpointer) to save the state of the graph up until this node.

3) We use `.update_state` to update the state of the graph.

```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-3-1)fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-3-2)fromlanggraph.graphimport StateGraph, START, END
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-3-3)fromlanggraph.checkpoint.memoryimport MemorySaver
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-3-4)fromIPython.displayimport Image, display
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-3-5)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-3-6)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-3-7)classState(TypedDict):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-3-8)  input: str
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-3-9)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-3-10)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-3-11)defstep_1(state):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-3-12)  print("---Step 1---")
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-3-13)  pass
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-3-14)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-3-15)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-3-16)defstep_2(state):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-3-17)  print("---Step 2---")
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-3-18)  pass
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-3-19)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-3-20)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-3-21)defstep_3(state):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-3-22)  print("---Step 3---")
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-3-23)  pass
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-3-24)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-3-25)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-3-26)builder = StateGraph(State)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-3-27)builder.add_node("step_1", step_1)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-3-28)builder.add_node("step_2", step_2)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-3-29)builder.add_node("step_3", step_3)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-3-30)builder.add_edge(START, "step_1")
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-3-31)builder.add_edge("step_1", "step_2")
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-3-32)builder.add_edge("step_2", "step_3")
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-3-33)builder.add_edge("step_3", END)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-3-34)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-3-35)# Set up memory
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-3-36)memory = MemorySaver()
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-3-37)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-3-38)# Add
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-3-39)graph = builder.compile(checkpointer=memory, interrupt_before=["step_2"])
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-3-40)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-3-41)# View
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-3-42)display(Image(graph.get_graph().draw_mermaid_png()))

```


API Reference: [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END) | [MemorySaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.MemorySaver)

![]()

```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-4-1)# Input
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-4-2)initial_input = {"input": "hello world"}
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-4-3)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-4-4)# Thread
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-4-5)thread = {"configurable": {"thread_id": "1"}}
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-4-6)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-4-7)# Run the graph until the first interruption
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-4-8)for event in graph.stream(initial_input, thread, stream_mode="values"):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-4-9)  print(event)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-5-1){'input': 'hello world'}
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-5-2)---Step 1---

```


Now, we can just manually update our graph state - 

```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-6-1)print("Current state!")
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-6-2)print(graph.get_state(thread).values)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-6-3)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-6-4)graph.update_state(thread, {"input": "hello universe!"})
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-6-5)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-6-6)print("---\n---\nUpdated state!")
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-6-7)print(graph.get_state(thread).values)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-7-1)Current state!
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-7-2){'input': 'hello world'}
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-7-3)---
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-7-4)---
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-7-5)Updated state!
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-7-6){'input': 'hello universe!'}

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-8-1)# Continue the graph execution
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-8-2)for event in graph.stream(None, thread, stream_mode="values"):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-8-3)  print(event)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-9-1)---Step 2---
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-9-2)---Step 3---

```


## Agent[¶](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#agent "Permanent link")

In the context of agents, updating state is useful for things like editing tool calls.

To show this, we will build a relatively simple ReAct-style agent that does tool calling. 

We will use Anthropic's models and a fake tool (just for demo purposes).

```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-1)# Set up the tool
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-2)fromlangchain_anthropicimport ChatAnthropic
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-3)fromlangchain_core.toolsimport tool
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-4)fromlanggraph.graphimport MessagesState, START, END, StateGraph
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-5)fromlanggraph.prebuiltimport ToolNode
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-6)fromlanggraph.checkpoint.memoryimport MemorySaver
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-7)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-8)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-9)@tool
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-10)defsearch(query: str):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-11)"""Call to surf the web."""
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-12)  # This is a placeholder for the actual implementation
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-13)  # Don't let the LLM know this though 😊
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-14)  return [
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-15)    "It's sunny in San Francisco, but you better look out if you're a Gemini 😈."
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-16)  ]
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-17)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-18)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-19)tools = [search]
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-20)tool_node = ToolNode(tools)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-21)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-22)# Set up the model
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-23)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-24)model = ChatAnthropic(model="claude-3-5-sonnet-20240620")
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-25)model = model.bind_tools(tools)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-26)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-27)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-28)# Define nodes and conditional edges
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-29)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-30)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-31)# Define the function that determines whether to continue or not
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-32)defshould_continue(state):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-33)  messages = state["messages"]
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-34)  last_message = messages[-1]
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-35)  # If there is no function call, then we finish
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-36)  if not last_message.tool_calls:
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-37)    return "end"
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-38)  # Otherwise if there is, we continue
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-39)  else:
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-40)    return "continue"
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-41)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-42)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-43)# Define the function that calls the model
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-44)defcall_model(state):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-45)  messages = state["messages"]
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-46)  response = model.invoke(messages)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-47)  # We return a list, because this will get added to the existing list
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-48)  return {"messages": [response]}
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-49)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-50)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-51)# Define a new graph
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-52)workflow = StateGraph(MessagesState)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-53)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-54)# Define the two nodes we will cycle between
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-55)workflow.add_node("agent", call_model)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-56)workflow.add_node("action", tool_node)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-57)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-58)# Set the entrypoint as `agent`
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-59)# This means that this node is the first one called
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-60)workflow.add_edge(START, "agent")
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-61)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-62)# We now add a conditional edge
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-63)workflow.add_conditional_edges(
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-64)  # First, we define the start node. We use `agent`.
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-65)  # This means these are the edges taken after the `agent` node is called.
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-66)  "agent",
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-67)  # Next, we pass in the function that will determine which node is called next.
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-68)  should_continue,
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-69)  # Finally we pass in a mapping.
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-70)  # The keys are strings, and the values are other nodes.
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-71)  # END is a special node marking that the graph should finish.
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-72)  # What will happen is we will call `should_continue`, and then the output of that
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-73)  # will be matched against the keys in this mapping.
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-74)  # Based on which one it matches, that node will then be called.
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-75)  {
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-76)    # If `tools`, then we call the tool node.
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-77)    "continue": "action",
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-78)    # Otherwise we finish.
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-79)    "end": END,
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-80)  },
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-81))
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-82)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-83)# We now add a normal edge from `tools` to `agent`.
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-84)# This means that after `tools` is called, `agent` node is called next.
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-85)workflow.add_edge("action", "agent")
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-86)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-87)# Set up memory
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-88)memory = MemorySaver()
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-89)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-90)# Finally, we compile it!
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-91)# This compiles it into a LangChain Runnable,
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-92)# meaning you can use it as you would any other runnable
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-93)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-94)# We add in `interrupt_before=["action"]`
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-95)# This will add a breakpoint before the `action` node is called
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-10-96)app = workflow.compile(checkpointer=memory, interrupt_before=["action"])

```


API Reference: [ChatAnthropic](https://python.langchain.com/api_reference/anthropic/chat_models/langchain_anthropic.chat_models.ChatAnthropic.html) | [tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [ToolNode](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.ToolNode) | [MemorySaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.MemorySaver)

## Interacting with the Agent[¶](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#interacting-with-the-agent "Permanent link")

We can now interact with the agent and see that it stops before calling a tool.

```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-11-1)fromlangchain_core.messagesimport HumanMessage
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-11-2)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-11-3)thread = {"configurable": {"thread_id": "3"}}
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-11-4)inputs = [HumanMessage(content="search for the weather in sf now")]
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-11-5)for event in app.stream({"messages": inputs}, thread, stream_mode="values"):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-11-6)  event["messages"][-1].pretty_print()

```


API Reference: [HumanMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.human.HumanMessage.html)

```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-12-1)================================[1m Human Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-12-2)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-12-3)search for the weather in sf now
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-12-4)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-12-5)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-12-6)[{'text': "Certainly! I'll search for the current weather in San Francisco for you. Let me use the search function to find this information.", 'type': 'text'}, {'id': 'toolu_01DxRhkj4fAvaGWoBhVuvfeL', 'input': {'query': 'current weather in San Francisco'}, 'name': 'search', 'type': 'tool_use'}]
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-12-7)Tool Calls:
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-12-8) search (toolu_01DxRhkj4fAvaGWoBhVuvfeL)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-12-9) Call ID: toolu_01DxRhkj4fAvaGWoBhVuvfeL
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-12-10) Args:
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-12-11)  query: current weather in San Francisco

```


**Edit**

We can now update the state accordingly. Let's modify the tool call to have the query `"current weather in SF"`.

```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-13-1)# First, lets get the current state
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-13-2)current_state = app.get_state(thread)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-13-3)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-13-4)# Let's now get the last message in the state
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-13-5)# This is the one with the tool calls that we want to update
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-13-6)last_message = current_state.values["messages"][-1]
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-13-7)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-13-8)# Let's now update the args for that tool call
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-13-9)last_message.tool_calls[0]["args"] = {"query": "current weather in SF"}
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-13-10)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-13-11)# Let's now call `update_state` to pass in this message in the `messages` key
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-13-12)# This will get treated as any other update to the state
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-13-13)# It will get passed to the reducer function for the `messages` key
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-13-14)# That reducer function will use the ID of the message to update it
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-13-15)# It's important that it has the right ID! Otherwise it would get appended
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-13-16)# as a new message
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-13-17)app.update_state(thread, {"messages": last_message})

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-14-1){'configurable': {'thread_id': '3',
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-14-2) 'checkpoint_ns': '',
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-14-3) 'checkpoint_id': '1ef7830a-c688-6fc6-8002-824126081ba0'}}

```


Let's now check the current state of the app to make sure it got updated accordingly

```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-15-1)current_state = app.get_state(thread).values["messages"][-1].tool_calls
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-15-2)current_state

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-16-1)[{'name': 'search',
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-16-2) 'args': {'query': 'current weather in SF'},
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-16-3) 'id': 'toolu_01FSkinAVXR1C4D5kecrzAnj'}]

```


**Resume**

We can now call the agent again with no inputs to continue, ie. run the tool as requested. We can see from the logs that it passes in the update args to the tool.

```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-17-1)for event in app.stream(None, thread, stream_mode="values"):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-17-2)  event["messages"][-1].pretty_print()

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-18-1)=================================[1m Tool Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-18-2)Name: search
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-18-3)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-18-4)["It's sunny in San Francisco, but you better look out if you're a Gemini \ud83d\ude08."]
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-18-5)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-18-6)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-18-7)Based on the search results, I can provide you with the current weather information for San Francisco:
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-18-8)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-18-9)The weather in San Francisco is currently sunny. 
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-18-10)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-18-11)It's important to note that the search result also included a playful astrological reference, which isn't directly related to the weather. If you need more specific weather details like temperature, humidity, or forecast, please let me know, and I can perform another search to find that information for you.
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-18-12)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__codelineno-18-13)Is there anything else you'd like to know about the weather in San Francisco or any other location?

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to add dynamic breakpoints with NodeInterrupt  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/dynamic_breakpoints/) [ Next  How to wait for user input using interrupt  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
