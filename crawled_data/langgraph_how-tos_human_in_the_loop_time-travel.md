---
url: https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#how-to-view-and-update-past-graph-state)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to view and update past graph state 

[ ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/?q= "Share")

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
            * How to view and update past graph state  [ How to view and update past graph state  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#setup)
              * [ Build the agent  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#build-the-agent)
              * [ Interacting with the Agent  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#interacting-with-the-agent)
              * [ Checking history  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#checking-history)
              * [ Replay a state  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#replay-a-state)
              * [ Branch off a past state  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#branch-off-a-past-state)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#setup)
  * [ Build the agent  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#build-the-agent)
  * [ Interacting with the Agent  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#interacting-with-the-agent)
  * [ Checking history  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#checking-history)
  * [ Replay a state  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#replay-a-state)
  * [ Branch off a past state  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#branch-off-a-past-state)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraph/how-tos#human-in-the-loop)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/human_in_the_loop/time-travel.ipynb "Edit this page")

# How to view and update past graph state[¶](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#how-to-view-and-update-past-graph-state "Permanent link")

Prerequisites

This guide assumes familiarity with the following concepts:

  * [Time Travel](https://langchain-ai.github.io/langgraph/concepts/time-travel)
  * [Breakpoints](https://langchain-ai.github.io/langgraph/concepts/breakpoints)
  * [LangGraph Glossary](https://langchain-ai.github.io/langgraph/concepts/low_level)



Once you start [checkpointing](https://langchain-ai.github.io/langgraph/how-tos/persistence) your graphs, you can easily **get** or **update** the state of the agent at any point in time. This permits a few things:

  1. You can surface a state during an interrupt to a user to let them accept an action.
  2. You can **rewind** the graph to reproduce or avoid issues.
  3. You can **modify** the state to embed your agent into a larger system, or to let the user better control its actions.



The key methods used for this functionality are:

  * [get_state](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.graph.CompiledGraph.get_state): fetch the values from the target config
  * [update_state](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.graph.CompiledGraph.update_state): apply the given values to the target state



**Note:** this requires passing in a checkpointer.

Below is a quick example.

## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#setup "Permanent link")

First we need to install the packages required

```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-0-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-0-2)%pip install --quiet -U langgraph langchain_openai

```


Next, we need to set API keys for OpenAI (the LLM we will use)

```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-1-1)importgetpass
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-1-2)importos
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-1-5)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-1-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-1-7)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-1-8)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-1-10)_set_env("OPENAI_API_KEY")

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-2-1)ANTHROPIC_API_KEY: ········

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Build the agent[¶](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#build-the-agent "Permanent link")

We can now build the agent. We will build a relatively simple ReAct-style agent that does tool calling. We will use Anthropic's models and fake tools (just for demo purposes).

```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-1)# Set up the tool
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-2)fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-3)fromlangchain_core.toolsimport tool
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-4)fromlanggraph.graphimport MessagesState, START
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-5)fromlanggraph.prebuiltimport ToolNode
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-6)fromlanggraph.graphimport END, StateGraph
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-7)fromlanggraph.checkpoint.memoryimport MemorySaver
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-8)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-9)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-10)@tool
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-11)defplay_song_on_spotify(song: str):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-12)"""Play a song on Spotify"""
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-13)  # Call the spotify API ...
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-14)  return f"Successfully played {song} on Spotify!"
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-15)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-16)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-17)@tool
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-18)defplay_song_on_apple(song: str):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-19)"""Play a song on Apple Music"""
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-20)  # Call the apple music API ...
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-21)  return f"Successfully played {song} on Apple Music!"
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-22)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-23)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-24)tools = [play_song_on_apple, play_song_on_spotify]
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-25)tool_node = ToolNode(tools)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-26)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-27)# Set up the model
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-28)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-29)model = ChatOpenAI(model="gpt-4o-mini")
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-30)model = model.bind_tools(tools, parallel_tool_calls=False)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-31)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-32)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-33)# Define nodes and conditional edges
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-34)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-35)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-36)# Define the function that determines whether to continue or not
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-37)defshould_continue(state):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-38)  messages = state["messages"]
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-39)  last_message = messages[-1]
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-40)  # If there is no function call, then we finish
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-41)  if not last_message.tool_calls:
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-42)    return "end"
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-43)  # Otherwise if there is, we continue
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-44)  else:
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-45)    return "continue"
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-46)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-47)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-48)# Define the function that calls the model
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-49)defcall_model(state):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-50)  messages = state["messages"]
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-51)  response = model.invoke(messages)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-52)  # We return a list, because this will get added to the existing list
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-53)  return {"messages": [response]}
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-54)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-55)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-56)# Define a new graph
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-57)workflow = StateGraph(MessagesState)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-58)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-59)# Define the two nodes we will cycle between
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-60)workflow.add_node("agent", call_model)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-61)workflow.add_node("action", tool_node)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-62)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-63)# Set the entrypoint as `agent`
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-64)# This means that this node is the first one called
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-65)workflow.add_edge(START, "agent")
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-66)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-67)# We now add a conditional edge
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-68)workflow.add_conditional_edges(
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-69)  # First, we define the start node. We use `agent`.
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-70)  # This means these are the edges taken after the `agent` node is called.
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-71)  "agent",
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-72)  # Next, we pass in the function that will determine which node is called next.
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-73)  should_continue,
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-74)  # Finally we pass in a mapping.
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-75)  # The keys are strings, and the values are other nodes.
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-76)  # END is a special node marking that the graph should finish.
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-77)  # What will happen is we will call `should_continue`, and then the output of that
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-78)  # will be matched against the keys in this mapping.
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-79)  # Based on which one it matches, that node will then be called.
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-80)  {
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-81)    # If `tools`, then we call the tool node.
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-82)    "continue": "action",
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-83)    # Otherwise we finish.
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-84)    "end": END,
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-85)  },
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-86))
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-87)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-88)# We now add a normal edge from `tools` to `agent`.
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-89)# This means that after `tools` is called, `agent` node is called next.
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-90)workflow.add_edge("action", "agent")
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-91)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-92)# Set up memory
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-93)memory = MemorySaver()
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-94)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-95)# Finally, we compile it!
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-96)# This compiles it into a LangChain Runnable,
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-97)# meaning you can use it as you would any other runnable
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-98)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-99)# We add in `interrupt_before=["action"]`
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-100)# This will add a breakpoint before the `action` node is called
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-3-101)app = workflow.compile(checkpointer=memory)

```


API Reference: [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html) | [tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [ToolNode](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.ToolNode) | [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [MemorySaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.MemorySaver)

## Interacting with the Agent[¶](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#interacting-with-the-agent "Permanent link")

We can now interact with the agent. Let's ask it to play Taylor Swift's most popular song:

```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-4-1)fromlangchain_core.messagesimport HumanMessage
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-4-2)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-4-3)config = {"configurable": {"thread_id": "1"}}
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-4-4)input_message = HumanMessage(content="Can you play Taylor Swift's most popular song?")
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-4-5)for event in app.stream({"messages": [input_message]}, config, stream_mode="values"):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-4-6)  event["messages"][-1].pretty_print()

```


API Reference: [HumanMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.human.HumanMessage.html)

```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-5-1)================================[1m Human Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-5-2)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-5-3)Can you play Taylor Swift's most popular song?
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-5-4)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-5-5)Tool Calls:
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-5-6) play_song_on_apple (call_uhGY6Fv6Mr4ZOhSokintuoD7)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-5-7) Call ID: call_uhGY6Fv6Mr4ZOhSokintuoD7
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-5-8) Args:
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-5-9)  song: Anti-Hero by Taylor Swift
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-5-10)=================================[1m Tool Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-5-11)Name: play_song_on_apple
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-5-12)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-5-13)Succesfully played Anti-Hero by Taylor Swift on Apple Music!
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-5-14)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-5-15)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-5-16)I've successfully played "Anti-Hero" by Taylor Swift on Apple Music! Enjoy the music!

```


## Checking history[¶](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#checking-history "Permanent link")

Let's browse the history of this thread, from start to finish.

```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-6-1)app.get_state(config).values["messages"]

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-7-1)[HumanMessage(content="Can you play Taylor Swift's most popular song?", id='7e32f0f3-75f5-48e1-a4ae-d38ccc15973b'),
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-7-2) AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_uhGY6Fv6Mr4ZOhSokintuoD7', 'function': {'arguments': '{"song":"Anti-Hero by Taylor Swift"}', 'name': 'play_song_on_apple'}, 'type': 'function'}], 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 22, 'prompt_tokens': 80, 'total_tokens': 102}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_483d39d857', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-af077bc4-f03c-4afe-8d92-78bdae394412-0', tool_calls=[{'name': 'play_song_on_apple', 'args': {'song': 'Anti-Hero by Taylor Swift'}, 'id': 'call_uhGY6Fv6Mr4ZOhSokintuoD7', 'type': 'tool_call'}], usage_metadata={'input_tokens': 80, 'output_tokens': 22, 'total_tokens': 102}),
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-7-3) ToolMessage(content='Succesfully played Anti-Hero by Taylor Swift on Apple Music!', name='play_song_on_apple', id='43a39ca7-326a-4033-8607-bf061615ed6b', tool_call_id='call_uhGY6Fv6Mr4ZOhSokintuoD7'),
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-7-4) AIMessage(content='I\'ve successfully played "Anti-Hero" by Taylor Swift on Apple Music! Enjoy the music!', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 20, 'prompt_tokens': 126, 'total_tokens': 146}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_483d39d857', 'finish_reason': 'stop', 'logprobs': None}, id='run-bfee6b28-9f16-49cc-8d28-bfb5a5b9aea1-0', usage_metadata={'input_tokens': 126, 'output_tokens': 20, 'total_tokens': 146})]

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-8-1)all_states = []
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-8-2)for state in app.get_state_history(config):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-8-3)  print(state)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-8-4)  all_states.append(state)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-8-5)  print("--")

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-9-1)StateSnapshot(values={'messages': [HumanMessage(content="Can you play Taylor Swift's most popular song?", id='7e32f0f3-75f5-48e1-a4ae-d38ccc15973b'), AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_uhGY6Fv6Mr4ZOhSokintuoD7', 'function': {'arguments': '{"song":"Anti-Hero by Taylor Swift"}', 'name': 'play_song_on_apple'}, 'type': 'function'}], 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 22, 'prompt_tokens': 80, 'total_tokens': 102}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_483d39d857', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-af077bc4-f03c-4afe-8d92-78bdae394412-0', tool_calls=[{'name': 'play_song_on_apple', 'args': {'song': 'Anti-Hero by Taylor Swift'}, 'id': 'call_uhGY6Fv6Mr4ZOhSokintuoD7', 'type': 'tool_call'}], usage_metadata={'input_tokens': 80, 'output_tokens': 22, 'total_tokens': 102}), ToolMessage(content='Succesfully played Anti-Hero by Taylor Swift on Apple Music!', name='play_song_on_apple', id='43a39ca7-326a-4033-8607-bf061615ed6b', tool_call_id='call_uhGY6Fv6Mr4ZOhSokintuoD7'), AIMessage(content='I\'ve successfully played "Anti-Hero" by Taylor Swift on Apple Music! Enjoy the music!', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 20, 'prompt_tokens': 126, 'total_tokens': 146}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_483d39d857', 'finish_reason': 'stop', 'logprobs': None}, id='run-bfee6b28-9f16-49cc-8d28-bfb5a5b9aea1-0', usage_metadata={'input_tokens': 126, 'output_tokens': 20, 'total_tokens': 146})]}, next=(), config={'configurable': {'thread_id': '1', 'checkpoint_ns': '', 'checkpoint_id': '1ef6bcf1-364f-6228-8003-dd67a426334e'}}, metadata={'source': 'loop', 'writes': {'agent': {'messages': [AIMessage(content='I\'ve successfully played "Anti-Hero" by Taylor Swift on Apple Music! Enjoy the music!', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 20, 'prompt_tokens': 126, 'total_tokens': 146}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_483d39d857', 'finish_reason': 'stop', 'logprobs': None}, id='run-bfee6b28-9f16-49cc-8d28-bfb5a5b9aea1-0', usage_metadata={'input_tokens': 126, 'output_tokens': 20, 'total_tokens': 146})]}}, 'step': 3, 'parents': {}}, created_at='2024-09-05T21:37:39.955948+00:00', parent_config={'configurable': {'thread_id': '1', 'checkpoint_ns': '', 'checkpoint_id': '1ef6bcf1-318f-6dc8-8002-dbdf9aaeac83'}}, tasks=())
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-9-2)--
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-9-3)StateSnapshot(values={'messages': [HumanMessage(content="Can you play Taylor Swift's most popular song?", id='7e32f0f3-75f5-48e1-a4ae-d38ccc15973b'), AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_uhGY6Fv6Mr4ZOhSokintuoD7', 'function': {'arguments': '{"song":"Anti-Hero by Taylor Swift"}', 'name': 'play_song_on_apple'}, 'type': 'function'}], 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 22, 'prompt_tokens': 80, 'total_tokens': 102}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_483d39d857', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-af077bc4-f03c-4afe-8d92-78bdae394412-0', tool_calls=[{'name': 'play_song_on_apple', 'args': {'song': 'Anti-Hero by Taylor Swift'}, 'id': 'call_uhGY6Fv6Mr4ZOhSokintuoD7', 'type': 'tool_call'}], usage_metadata={'input_tokens': 80, 'output_tokens': 22, 'total_tokens': 102}), ToolMessage(content='Succesfully played Anti-Hero by Taylor Swift on Apple Music!', name='play_song_on_apple', id='43a39ca7-326a-4033-8607-bf061615ed6b', tool_call_id='call_uhGY6Fv6Mr4ZOhSokintuoD7')]}, next=('agent',), config={'configurable': {'thread_id': '1', 'checkpoint_ns': '', 'checkpoint_id': '1ef6bcf1-318f-6dc8-8002-dbdf9aaeac83'}}, metadata={'source': 'loop', 'writes': {'action': {'messages': [ToolMessage(content='Succesfully played Anti-Hero by Taylor Swift on Apple Music!', name='play_song_on_apple', id='43a39ca7-326a-4033-8607-bf061615ed6b', tool_call_id='call_uhGY6Fv6Mr4ZOhSokintuoD7')]}}, 'step': 2, 'parents': {}}, created_at='2024-09-05T21:37:39.458185+00:00', parent_config={'configurable': {'thread_id': '1', 'checkpoint_ns': '', 'checkpoint_id': '1ef6bcf1-3185-663e-8001-12b1ec3114b8'}}, tasks=(PregelTask(id='3a4c5ddb-14b2-5def-a766-02ddc32948ba', name='agent', error=None, interrupts=(), state=None),))
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-9-4)--
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-9-5)StateSnapshot(values={'messages': [HumanMessage(content="Can you play Taylor Swift's most popular song?", id='7e32f0f3-75f5-48e1-a4ae-d38ccc15973b'), AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_uhGY6Fv6Mr4ZOhSokintuoD7', 'function': {'arguments': '{"song":"Anti-Hero by Taylor Swift"}', 'name': 'play_song_on_apple'}, 'type': 'function'}], 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 22, 'prompt_tokens': 80, 'total_tokens': 102}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_483d39d857', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-af077bc4-f03c-4afe-8d92-78bdae394412-0', tool_calls=[{'name': 'play_song_on_apple', 'args': {'song': 'Anti-Hero by Taylor Swift'}, 'id': 'call_uhGY6Fv6Mr4ZOhSokintuoD7', 'type': 'tool_call'}], usage_metadata={'input_tokens': 80, 'output_tokens': 22, 'total_tokens': 102})]}, next=('action',), config={'configurable': {'thread_id': '1', 'checkpoint_ns': '', 'checkpoint_id': '1ef6bcf1-3185-663e-8001-12b1ec3114b8'}}, metadata={'source': 'loop', 'writes': {'agent': {'messages': [AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_uhGY6Fv6Mr4ZOhSokintuoD7', 'function': {'arguments': '{"song":"Anti-Hero by Taylor Swift"}', 'name': 'play_song_on_apple'}, 'type': 'function'}], 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 22, 'prompt_tokens': 80, 'total_tokens': 102}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_483d39d857', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-af077bc4-f03c-4afe-8d92-78bdae394412-0', tool_calls=[{'name': 'play_song_on_apple', 'args': {'song': 'Anti-Hero by Taylor Swift'}, 'id': 'call_uhGY6Fv6Mr4ZOhSokintuoD7', 'type': 'tool_call'}], usage_metadata={'input_tokens': 80, 'output_tokens': 22, 'total_tokens': 102})]}}, 'step': 1, 'parents': {}}, created_at='2024-09-05T21:37:39.453898+00:00', parent_config={'configurable': {'thread_id': '1', 'checkpoint_ns': '', 'checkpoint_id': '1ef6bcf1-29b8-6370-8000-f9f6e7ca1b06'}}, tasks=(PregelTask(id='01f1dc72-5a39-5876-97a6-abdc12f70c2a', name='action', error=None, interrupts=(), state=None),))
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-9-6)--
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-9-7)StateSnapshot(values={'messages': [HumanMessage(content="Can you play Taylor Swift's most popular song?", id='7e32f0f3-75f5-48e1-a4ae-d38ccc15973b')]}, next=('agent',), config={'configurable': {'thread_id': '1', 'checkpoint_ns': '', 'checkpoint_id': '1ef6bcf1-29b8-6370-8000-f9f6e7ca1b06'}}, metadata={'source': 'loop', 'writes': None, 'step': 0, 'parents': {}}, created_at='2024-09-05T21:37:38.635849+00:00', parent_config={'configurable': {'thread_id': '1', 'checkpoint_ns': '', 'checkpoint_id': '1ef6bcf1-29b3-6514-bfff-fe07fb36f14f'}}, tasks=(PregelTask(id='348e1ba7-95c6-5b89-80c9-1fc4720e35ef', name='agent', error=None, interrupts=(), state=None),))
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-9-8)--
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-9-9)StateSnapshot(values={'messages': []}, next=('__start__',), config={'configurable': {'thread_id': '1', 'checkpoint_ns': '', 'checkpoint_id': '1ef6bcf1-29b3-6514-bfff-fe07fb36f14f'}}, metadata={'source': 'input', 'writes': {'__start__': {'messages': [HumanMessage(content="Can you play Taylor Swift's most popular song?")]}}, 'step': -1, 'parents': {}}, created_at='2024-09-05T21:37:38.633849+00:00', parent_config=None, tasks=(PregelTask(id='f1cfbb8c-7792-5cf9-9d28-ae3ac7724cf3', name='__start__', error=None, interrupts=(), state=None),))
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-9-10)--

```


## Replay a state[¶](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#replay-a-state "Permanent link")

We can go back to any of these states and restart the agent from there! Let's go back to right before the tool call gets executed.

```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-10-1)to_replay = all_states[2]

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-11-1)to_replay.values

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-12-1){'messages': [HumanMessage(content="Can you play Taylor Swift's most popular song?", id='7e32f0f3-75f5-48e1-a4ae-d38ccc15973b'),
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-12-2) AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_uhGY6Fv6Mr4ZOhSokintuoD7', 'function': {'arguments': '{"song":"Anti-Hero by Taylor Swift"}', 'name': 'play_song_on_apple'}, 'type': 'function'}], 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 22, 'prompt_tokens': 80, 'total_tokens': 102}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_483d39d857', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-af077bc4-f03c-4afe-8d92-78bdae394412-0', tool_calls=[{'name': 'play_song_on_apple', 'args': {'song': 'Anti-Hero by Taylor Swift'}, 'id': 'call_uhGY6Fv6Mr4ZOhSokintuoD7', 'type': 'tool_call'}], usage_metadata={'input_tokens': 80, 'output_tokens': 22, 'total_tokens': 102})]}

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-13-1)to_replay.next

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-14-1)('action',)

```


To replay from this place we just need to pass its config back to the agent. Notice that it just resumes from right where it left all - making a tool call.

```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-15-1)for event in app.stream(None, to_replay.config):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-15-2)  for v in event.values():
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-15-3)    print(v)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-16-1){'messages': [ToolMessage(content='Succesfully played Anti-Hero by Taylor Swift on Apple Music!', name='play_song_on_apple', tool_call_id='call_uhGY6Fv6Mr4ZOhSokintuoD7')]}
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-16-2){'messages': [AIMessage(content='I\'ve started playing "Anti-Hero" by Taylor Swift on Apple Music! Enjoy the music!', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 20, 'prompt_tokens': 126, 'total_tokens': 146}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_483d39d857', 'finish_reason': 'stop', 'logprobs': None}, id='run-dc338bbd-d623-40bb-b824-5d2307954b57-0', usage_metadata={'input_tokens': 126, 'output_tokens': 20, 'total_tokens': 146})]}

```


## Branch off a past state[¶](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#branch-off-a-past-state "Permanent link")

Using LangGraph's checkpointing, you can do more than just replay past states. You can branch off previous locations to let the agent explore alternate trajectories or to let a user "version control" changes in a workflow.

Let's show how to do this to edit the state at a particular point in time. Let's update the state to instead of playing the song on Apple to play it on Spotify:

```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-17-1)# Let's now get the last message in the state
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-17-2)# This is the one with the tool calls that we want to update
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-17-3)last_message = to_replay.values["messages"][-1]
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-17-4)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-17-5)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-17-6)# Let's now update the tool we are calling
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-17-7)last_message.tool_calls[0]["name"] = "play_song_on_spotify"
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-17-8)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-17-9)branch_config = app.update_state(
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-17-10)  to_replay.config,
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-17-11)  {"messages": [last_message]},
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-17-12))

```


We can then invoke with this new `branch_config` to resume running from here with changed state. We can see from the log that the tool was called with different input.

```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-18-1)for event in app.stream(None, branch_config):
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-18-2)  for v in event.values():
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-18-3)    print(v)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-19-1){'messages': [ToolMessage(content='Succesfully played Anti-Hero by Taylor Swift on Spotify!', name='play_song_on_spotify', tool_call_id='call_uhGY6Fv6Mr4ZOhSokintuoD7')]}
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-19-2){'messages': [AIMessage(content='I\'ve started playing "Anti-Hero" by Taylor Swift on Spotify. Enjoy the music!', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 19, 'prompt_tokens': 125, 'total_tokens': 144}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_483d39d857', 'finish_reason': 'stop', 'logprobs': None}, id='run-7d8d5094-7029-4da3-9e0e-ef9d18b63615-0', usage_metadata={'input_tokens': 125, 'output_tokens': 19, 'total_tokens': 144})]}

```


Alternatively, we could update the state to not even call a tool! 

```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-20-1)fromlangchain_core.messagesimport AIMessage
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-20-2)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-20-3)# Let's now get the last message in the state
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-20-4)# This is the one with the tool calls that we want to update
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-20-5)last_message = to_replay.values["messages"][-1]
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-20-6)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-20-7)# Let's now get the ID for the last message, and create a new message with that ID.
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-20-8)new_message = AIMessage(
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-20-9)  content="It's quiet hours so I can't play any music right now!", id=last_message.id
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-20-10))
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-20-11)
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-20-12)branch_config = app.update_state(
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-20-13)  to_replay.config,
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-20-14)  {"messages": [new_message]},
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-20-15))

```


API Reference: [AIMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.AIMessage.html)

```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-21-1)branch_state = app.get_state(branch_config)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-22-1)branch_state.values

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-23-1){'messages': [HumanMessage(content="Can you play Taylor Swift's most popular song?", id='7e32f0f3-75f5-48e1-a4ae-d38ccc15973b'),
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-23-2) AIMessage(content="It's quiet hours so I can't play any music right now!", id='run-af077bc4-f03c-4afe-8d92-78bdae394412-0')]}

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-24-1)branch_state.next

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__codelineno-25-1)()

```


You can see the snapshot was updated and now correctly reflects that there is no next step.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to wait for user input using interrupt  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/) [ Next  How to Review Tool Calls  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
