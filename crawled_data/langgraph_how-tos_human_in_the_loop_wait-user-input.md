---
url: https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#how-to-wait-for-user-input-using-interrupt)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to wait for user input using interrupt 

[ ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/?q= "Share")

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
            * How to wait for user input using interrupt  [ How to wait for user input using interrupt  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#setup)
              * [ Simple Usage  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#simple-usage)
              * [ Agent  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#agent)
              * [ Interacting with the Agent  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#interacting-with-the-agent)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#setup)
  * [ Simple Usage  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#simple-usage)
  * [ Agent  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#agent)
  * [ Interacting with the Agent  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#interacting-with-the-agent)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraph/how-tos#human-in-the-loop)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/human_in_the_loop/wait-user-input.ipynb "Edit this page")

# How to wait for user input using `interrupt`[¶](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#how-to-wait-for-user-input-using-interrupt "Permanent link")

Prerequisites

This guide assumes familiarity with the following concepts:

  * [Human-in-the-loop](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop)
  * [Breakpoints](https://langchain-ai.github.io/langgraph/concepts/breakpoints)
  * [LangGraph Glossary](https://langchain-ai.github.io/langgraph/concepts/low_level)



**Human-in-the-loop (HIL)** interactions are crucial for [agentic systems](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#human-in-the-loop). Waiting for human input is a common HIL interaction pattern, allowing the agent to ask the user clarifying questions and await input before proceeding. 

We can implement this in LangGraph using the `interrupt()`[](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.interrupt) function. `interrupt` allows us to stop graph execution to collect input from a user and continue execution with collected input.

## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#setup "Permanent link")

First we need to install the packages required

```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-0-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-0-2)%pip install --quiet -U langgraph langchain_anthropic

```


Next, we need to set API keys for Anthropic and / or OpenAI (the LLM(s) we will use)

```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-1-1)importgetpass
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-1-2)importos
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-1-5)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-1-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-1-7)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-1-8)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-1-10)_set_env("ANTHROPIC_API_KEY")

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-2-1)ANTHROPIC_API_KEY: ········

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Simple Usage[¶](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#simple-usage "Permanent link")

Let's explore a basic example of using human feedback. A straightforward approach is to create a node, **`human_feedback`**, designed specifically to collect user input. This allows us to gather feedback at a specific, chosen point in our graph.

Steps:

  1. **Call`interrupt()`** inside the **`human_feedback`**node.
  2. **Set up a[checkpointer](https://langchain-ai.github.io/langgraph/concepts/low_level/#checkpointer)** to save the graph's state up to this node. 
  3. **Use`Command(resume=...)`** to provide the requested value to the **`human_feedback`**node and resume execution.



```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-3-1)fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-3-2)fromlanggraph.graphimport StateGraph, START, END
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-3-3)fromlanggraph.typesimport Command, interrupt
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-3-4)fromlanggraph.checkpoint.memoryimport MemorySaver
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-3-5)fromIPython.displayimport Image, display
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-3-6)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-3-7)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-3-8)classState(TypedDict):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-3-9)  input: str
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-3-10)  user_feedback: str
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-3-11)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-3-12)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-3-13)defstep_1(state):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-3-14)  print("---Step 1---")
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-3-15)  pass
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-3-16)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-3-17)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-3-18)defhuman_feedback(state):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-3-19)  print("---human_feedback---")
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-3-20)  feedback = interrupt("Please provide feedback:")
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-3-21)  return {"user_feedback": feedback}
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-3-22)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-3-23)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-3-24)defstep_3(state):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-3-25)  print("---Step 3---")
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-3-26)  pass
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-3-27)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-3-28)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-3-29)builder = StateGraph(State)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-3-30)builder.add_node("step_1", step_1)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-3-31)builder.add_node("human_feedback", human_feedback)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-3-32)builder.add_node("step_3", step_3)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-3-33)builder.add_edge(START, "step_1")
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-3-34)builder.add_edge("step_1", "human_feedback")
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-3-35)builder.add_edge("human_feedback", "step_3")
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-3-36)builder.add_edge("step_3", END)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-3-37)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-3-38)# Set up memory
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-3-39)memory = MemorySaver()
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-3-40)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-3-41)# Add
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-3-42)graph = builder.compile(checkpointer=memory)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-3-43)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-3-44)# View
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-3-45)display(Image(graph.get_graph().draw_mermaid_png()))

```


API Reference: [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END) | [Command](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Command) | [interrupt](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.interrupt) | [MemorySaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.MemorySaver)

![]()

Run until our breakpoint at `human_feedback`:

```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-4-1)# Input
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-4-2)initial_input = {"input": "hello world"}
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-4-3)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-4-4)# Thread
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-4-5)thread = {"configurable": {"thread_id": "1"}}
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-4-6)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-4-7)# Run the graph until the first interruption
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-4-8)for event in graph.stream(initial_input, thread, stream_mode="updates"):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-4-9)  print(event)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-4-10)  print("\n")

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-5-1)---Step 1---
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-5-2){'step_1': None}
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-5-3)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-5-4)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-5-5)---human_feedback---
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-5-6){'__interrupt__': (Interrupt(value='Please provide feedback:', resumable=True, ns=['human_feedback:e9a51d27-22ed-8c01-3f17-0ed33209b554'], when='during'),)}

```


Now, we can manually update our graph state with the user input: 

```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-6-1)# Continue the graph execution
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-6-2)for event in graph.stream(
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-6-3)  Command(resume="go to step 3!"), thread, stream_mode="updates"
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-6-4)):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-6-5)  print(event)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-6-6)  print("\n")

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-7-1)---human_feedback---
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-7-2){'human_feedback': {'user_feedback': 'go to step 3!'}}
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-7-3)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-7-4)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-7-5)---Step 3---
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-7-6){'step_3': None}

```


We can see our feedback was added to state - 

```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-8-1)graph.get_state(thread).values

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-9-1){'input': 'hello world', 'user_feedback': 'go to step 3!'}

```


## Agent[¶](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#agent "Permanent link")

In the context of [agents](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts), waiting for user feedback is especially useful for asking clarifying questions. To illustrate this, we’ll create a simple [ReAct-style agent](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts#react-implementation) capable of [tool calling](https://python.langchain.com/docs/concepts/tool_calling/). 

For this example, we’ll use Anthropic's chat model along with a **mock tool** (purely for demonstration purposes).

Using Pydantic with LangChain

This notebook uses Pydantic v2 `BaseModel`, which requires `langchain-core >= 0.3`. Using `langchain-core < 0.3` will result in errors due to mixing of Pydantic v1 and v2 `BaseModels`. 

```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-1)# Set up the state
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-2)fromlanggraph.graphimport MessagesState, START
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-3)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-4)# Set up the tool
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-5)# We will have one real tool - a search tool
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-6)# We'll also have one "fake" tool - a "ask_human" tool
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-7)# Here we define any ACTUAL tools
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-8)fromlangchain_core.toolsimport tool
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-9)fromlanggraph.prebuiltimport ToolNode
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-10)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-11)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-12)@tool
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-13)defsearch(query: str):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-14)"""Call to surf the web."""
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-15)  # This is a placeholder for the actual implementation
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-16)  # Don't let the LLM know this though 😊
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-17)  return f"I looked up: {query}. Result: It's sunny in San Francisco, but you better look out if you're a Gemini 😈."
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-18)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-19)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-20)tools = [search]
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-21)tool_node = ToolNode(tools)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-22)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-23)# Set up the model
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-24)fromlangchain_anthropicimport ChatAnthropic
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-25)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-26)model = ChatAnthropic(model="claude-3-5-sonnet-latest")
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-27)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-28)frompydanticimport BaseModel
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-29)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-30)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-31)# We are going "bind" all tools to the model
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-32)# We have the ACTUAL tools from above, but we also need a mock tool to ask a human
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-33)# Since `bind_tools` takes in tools but also just tool definitions,
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-34)# We can define a tool definition for `ask_human`
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-35)classAskHuman(BaseModel):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-36)"""Ask the human a question"""
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-37)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-38)  question: str
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-39)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-40)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-41)model = model.bind_tools(tools + [AskHuman])
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-42)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-43)# Define nodes and conditional edges
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-44)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-45)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-46)# Define the function that determines whether to continue or not
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-47)defshould_continue(state):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-48)  messages = state["messages"]
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-49)  last_message = messages[-1]
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-50)  # If there is no function call, then we finish
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-51)  if not last_message.tool_calls:
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-52)    return END
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-53)  # If tool call is asking Human, we return that node
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-54)  # You could also add logic here to let some system know that there's something that requires Human input
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-55)  # For example, send a slack message, etc
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-56)  elif last_message.tool_calls[0]["name"] == "AskHuman":
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-57)    return "ask_human"
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-58)  # Otherwise if there is, we continue
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-59)  else:
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-60)    return "action"
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-61)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-62)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-63)# Define the function that calls the model
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-64)defcall_model(state):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-65)  messages = state["messages"]
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-66)  response = model.invoke(messages)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-67)  # We return a list, because this will get added to the existing list
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-68)  return {"messages": [response]}
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-69)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-70)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-71)# We define a fake node to ask the human
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-72)defask_human(state):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-73)  tool_call_id = state["messages"][-1].tool_calls[0]["id"]
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-74)  location = interrupt("Please provide your location:")
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-75)  tool_message = [{"tool_call_id": tool_call_id, "type": "tool", "content": location}]
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-76)  return {"messages": tool_message}
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-77)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-78)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-79)# Build the graph
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-80)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-81)fromlanggraph.graphimport END, StateGraph
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-82)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-83)# Define a new graph
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-84)workflow = StateGraph(MessagesState)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-85)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-86)# Define the three nodes we will cycle between
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-87)workflow.add_node("agent", call_model)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-88)workflow.add_node("action", tool_node)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-89)workflow.add_node("ask_human", ask_human)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-90)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-91)# Set the entrypoint as `agent`
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-92)# This means that this node is the first one called
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-93)workflow.add_edge(START, "agent")
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-94)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-95)# We now add a conditional edge
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-96)workflow.add_conditional_edges(
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-97)  # First, we define the start node. We use `agent`.
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-98)  # This means these are the edges taken after the `agent` node is called.
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-99)  "agent",
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-100)  # Next, we pass in the function that will determine which node is called next.
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-101)  should_continue,
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-102))
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-103)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-104)# We now add a normal edge from `tools` to `agent`.
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-105)# This means that after `tools` is called, `agent` node is called next.
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-106)workflow.add_edge("action", "agent")
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-107)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-108)# After we get back the human response, we go back to the agent
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-109)workflow.add_edge("ask_human", "agent")
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-110)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-111)# Set up memory
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-112)fromlanggraph.checkpoint.memoryimport MemorySaver
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-113)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-114)memory = MemorySaver()
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-115)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-116)# Finally, we compile it!
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-117)# This compiles it into a LangChain Runnable,
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-118)# meaning you can use it as you would any other runnable
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-119)# We add a breakpoint BEFORE the `ask_human` node so it never executes
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-120)app = workflow.compile(checkpointer=memory)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-121)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-10-122)display(Image(app.get_graph().draw_mermaid_png()))

```


API Reference: [tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html) | [ChatAnthropic](https://python.langchain.com/api_reference/anthropic/chat_models/langchain_anthropic.chat_models.ChatAnthropic.html) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [ToolNode](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.ToolNode) | [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [MemorySaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.MemorySaver)

![]()

## Interacting with the Agent[¶](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#interacting-with-the-agent "Permanent link")

We can now interact with the agent. Let's ask it to ask the user where they are, then tell them the weather. 

This should make it use the `ask_human` tool first, then use the normal tool.

```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-11-1)config = {"configurable": {"thread_id": "2"}}
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-11-2)for event in app.stream(
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-11-3)  {
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-11-4)    "messages": [
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-11-5)      (
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-11-6)        "user",
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-11-7)        "Use the search tool to ask the user where they are, then look up the weather there",
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-11-8)      )
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-11-9)    ]
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-11-10)  },
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-11-11)  config,
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-11-12)  stream_mode="values",
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-11-13)):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-11-14)  event["messages"][-1].pretty_print()

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-12-1)================================[1m Human Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-12-2)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-12-3)Use the search tool to ask the user where they are, then look up the weather there
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-12-4)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-12-5)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-12-6)[{'text': "I'll help you with that. Let me first ask the user about their location.", 'type': 'text'}, {'id': 'toolu_01KNvb7RCVu8yKYUuQQSKN1x', 'input': {'question': 'Where are you located?'}, 'name': 'AskHuman', 'type': 'tool_use'}]
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-12-7)Tool Calls:
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-12-8) AskHuman (toolu_01KNvb7RCVu8yKYUuQQSKN1x)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-12-9) Call ID: toolu_01KNvb7RCVu8yKYUuQQSKN1x
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-12-10) Args:
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-12-11)  question: Where are you located?

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-13-1)app.get_state(config).next

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-14-1)('ask_human',)

```


You can see that our graph got interrupted inside the `ask_human` node, which is now waiting for a `location` to be provided. We can provide this value by invoking the graph with a `Command(resume="<location>")` input:

```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-15-1)for event in app.stream(Command(resume="san francisco"), config, stream_mode="values"):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-15-2)  event["messages"][-1].pretty_print()

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-16-1)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-16-2)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-16-3)[{'text': "I'll help you with that. Let me first ask the user about their location.", 'type': 'text'}, {'id': 'toolu_01KNvb7RCVu8yKYUuQQSKN1x', 'input': {'question': 'Where are you located?'}, 'name': 'AskHuman', 'type': 'tool_use'}]
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-16-4)Tool Calls:
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-16-5) AskHuman (toolu_01KNvb7RCVu8yKYUuQQSKN1x)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-16-6) Call ID: toolu_01KNvb7RCVu8yKYUuQQSKN1x
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-16-7) Args:
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-16-8)  question: Where are you located?
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-16-9)=================================[1m Tool Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-16-10)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-16-11)san francisco
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-16-12)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-16-13)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-16-14)[{'text': "Now I'll search for the weather in San Francisco.", 'type': 'text'}, {'id': 'toolu_01Y5C4rU9WcxBqFLYSMGjV1F', 'input': {'query': 'current weather in san francisco'}, 'name': 'search', 'type': 'tool_use'}]
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-16-15)Tool Calls:
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-16-16) search (toolu_01Y5C4rU9WcxBqFLYSMGjV1F)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-16-17) Call ID: toolu_01Y5C4rU9WcxBqFLYSMGjV1F
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-16-18) Args:
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-16-19)  query: current weather in san francisco
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-16-20)=================================[1m Tool Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-16-21)Name: search
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-16-22)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-16-23)I looked up: current weather in san francisco. Result: It's sunny in San Francisco, but you better look out if you're a Gemini 😈.
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-16-24)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-16-25)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__codelineno-16-26)Based on the search results, it's currently sunny in San Francisco. Note that this is the current weather at the time of our conversation, and conditions can change throughout the day.

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to edit graph state  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/edit-graph-state/) [ Next  How to view and update past graph state  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
