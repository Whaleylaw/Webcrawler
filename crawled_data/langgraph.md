---
url: https://langchain-ai.github.io/langgraph/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/#langgraph)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Home 

[ ](https://langchain-ai.github.io/langgraph/?q= "Share")

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

  * [ Overview  ](https://langchain-ai.github.io/langgraph/#overview)
    * [ Why use LangGraph?  ](https://langchain-ai.github.io/langgraph/#why-use-langgraph)
    * [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/#langgraph-platform)
  * [ Installation  ](https://langchain-ai.github.io/langgraph/#installation)
  * [ Example  ](https://langchain-ai.github.io/langgraph/#example)
  * [ Documentation  ](https://langchain-ai.github.io/langgraph/#documentation)
  * [ Resources  ](https://langchain-ai.github.io/langgraph/#resources)
  * [ Contributing  ](https://langchain-ai.github.io/langgraph/#contributing)



[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/index.md "Edit this page")

# 🦜🕸️LangGraph[¶](https://langchain-ai.github.io/langgraph/#langgraph "Permanent link")

![Version](https://img.shields.io/pypi/v/langgraph) [![Downloads](https://static.pepy.tech/badge/langgraph/month)](https://pepy.tech/project/langgraph) [![Open Issues](https://img.shields.io/github/issues-raw/langchain-ai/langgraph)](https://github.com/langchain-ai/langgraph/issues) [![Docs](https://img.shields.io/badge/docs-latest-blue)](https://langchain-ai.github.io/langgraph/)

⚡ Building language agents as graphs ⚡

Note

Looking for the JS version? See the [JS repo](https://github.com/langchain-ai/langgraphjs) and the [JS docs](https://langchain-ai.github.io/langgraphjs/).

## Overview[¶](https://langchain-ai.github.io/langgraph/#overview "Permanent link")

[LangGraph](https://langchain-ai.github.io/langgraph/) is a library for building stateful, multi-actor applications with LLMs, used to create agent and multi-agent workflows. Check out an introductory tutorial [here](https://langchain-ai.github.io/langgraph/tutorials/introduction/).

LangGraph is inspired by [Pregel](https://research.google/pubs/pub37252/) and [Apache Beam](https://beam.apache.org/). The public interface draws inspiration from [NetworkX](https://networkx.org/documentation/latest/). LangGraph is built by LangChain Inc, the creators of LangChain, but can be used without LangChain.

### Why use LangGraph?[¶](https://langchain-ai.github.io/langgraph/#why-use-langgraph "Permanent link")

LangGraph powers [production-grade agents](https://www.langchain.com/built-with-langgraph), trusted by Linkedin, Uber, Klarna, GitLab, and many more. LangGraph provides fine-grained control over both the flow and state of your agent applications. It implements a central [persistence layer](https://langchain-ai.github.io/langgraph/concepts/persistence/), enabling features that are common to most agent architectures:

  * **Memory** : LangGraph persists arbitrary aspects of your application's state, supporting memory of conversations and other updates within and across user interactions;
  * **Human-in-the-loop** : Because state is checkpointed, execution can be interrupted and resumed, allowing for decisions, validation, and corrections at key stages via human input.



Standardizing these components allows individuals and teams to focus on the behavior of their agent, instead of its supporting infrastructure.

Through [LangGraph Platform](https://langchain-ai.github.io/langgraph/#langgraph-platform), LangGraph also provides tooling for the development, deployment, debugging, and monitoring of your applications.

LangGraph integrates seamlessly with [LangChain](https://python.langchain.com/docs/introduction/) and [LangSmith](https://docs.smith.langchain.com/) (but does not require them).

To learn more about LangGraph, check out our first LangChain Academy course, _Introduction to LangGraph_ , available for free [here](https://academy.langchain.com/courses/intro-to-langgraph).

### LangGraph Platform[¶](https://langchain-ai.github.io/langgraph/#langgraph-platform "Permanent link")

[LangGraph Platform](https://langchain-ai.github.io/langgraph/concepts/langgraph_platform) is infrastructure for deploying LangGraph agents. It is a commercial solution for deploying agentic applications to production, built on the open-source LangGraph framework. The LangGraph Platform consists of several components that work together to support the development, deployment, debugging, and monitoring of LangGraph applications: [LangGraph Server](https://langchain-ai.github.io/langgraph/concepts/langgraph_server) (APIs), [LangGraph SDKs](https://langchain-ai.github.io/langgraph/concepts/sdk) (clients for the APIs), [LangGraph CLI](https://langchain-ai.github.io/langgraph/concepts/langgraph_cli) (command line tool for building the server), and [LangGraph Studio](https://langchain-ai.github.io/langgraph/concepts/langgraph_studio) (UI/debugger).

See deployment options [here](https://langchain-ai.github.io/langgraph/concepts/deployment_options/) (includes a free tier).

Here are some common issues that arise in complex deployments, which LangGraph Platform addresses:

  * **Streaming support** : LangGraph Server provides [multiple streaming modes](https://langchain-ai.github.io/langgraph/concepts/streaming) optimized for various application needs
  * **Background runs** : Runs agents asynchronously in the background
  * **Support for long running agents** : Infrastructure that can handle long running processes
  * **[Double texting](https://langchain-ai.github.io/langgraph/concepts/double_texting)** : Handle the case where you get two messages from the user before the agent can respond
  * **Handle burstiness** : Task queue for ensuring requests are handled consistently without loss, even under heavy loads



## Installation[¶](https://langchain-ai.github.io/langgraph/#installation "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/#__codelineno-0-1)pipinstall-Ulanggraph

```


## Example[¶](https://langchain-ai.github.io/langgraph/#example "Permanent link")

Let's build a tool-calling [ReAct-style](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#react-implementation) agent that uses a search tool!

```
[](https://langchain-ai.github.io/langgraph/#__codelineno-1-1)pipinstalllangchain-anthropic

```


```
[](https://langchain-ai.github.io/langgraph/#__codelineno-2-1)exportANTHROPIC_API_KEY=sk-...

```


Optionally, we can set up [LangSmith](https://docs.smith.langchain.com/) for best-in-class observability.

```
[](https://langchain-ai.github.io/langgraph/#__codelineno-3-1)exportLANGSMITH_TRACING=true
[](https://langchain-ai.github.io/langgraph/#__codelineno-3-2)exportLANGSMITH_API_KEY=lsv2_sk_...

```


The simplest way to create a tool-calling agent in LangGraph is to use `create_react_agent`:

High-level implementation

```
[](https://langchain-ai.github.io/langgraph/#__codelineno-4-1)fromlanggraph.prebuiltimport create_react_agent
[](https://langchain-ai.github.io/langgraph/#__codelineno-4-2)fromlanggraph.checkpoint.memoryimport MemorySaver
[](https://langchain-ai.github.io/langgraph/#__codelineno-4-3)fromlangchain_anthropicimport ChatAnthropic
[](https://langchain-ai.github.io/langgraph/#__codelineno-4-4)fromlangchain_core.toolsimport tool
[](https://langchain-ai.github.io/langgraph/#__codelineno-4-5)
[](https://langchain-ai.github.io/langgraph/#__codelineno-4-6)# Define the tools for the agent to use
[](https://langchain-ai.github.io/langgraph/#__codelineno-4-7)@tool
[](https://langchain-ai.github.io/langgraph/#__codelineno-4-8)defsearch(query: str):
[](https://langchain-ai.github.io/langgraph/#__codelineno-4-9)"""Call to surf the web."""
[](https://langchain-ai.github.io/langgraph/#__codelineno-4-10)  # This is a placeholder, but don't tell the LLM that...
[](https://langchain-ai.github.io/langgraph/#__codelineno-4-11)  if "sf" in query.lower() or "san francisco" in query.lower():
[](https://langchain-ai.github.io/langgraph/#__codelineno-4-12)    return "It's 60 degrees and foggy."
[](https://langchain-ai.github.io/langgraph/#__codelineno-4-13)  return "It's 90 degrees and sunny."
[](https://langchain-ai.github.io/langgraph/#__codelineno-4-14)
[](https://langchain-ai.github.io/langgraph/#__codelineno-4-15)
[](https://langchain-ai.github.io/langgraph/#__codelineno-4-16)tools = [search]
[](https://langchain-ai.github.io/langgraph/#__codelineno-4-17)model = ChatAnthropic(model="claude-3-5-sonnet-latest", temperature=0)
[](https://langchain-ai.github.io/langgraph/#__codelineno-4-18)
[](https://langchain-ai.github.io/langgraph/#__codelineno-4-19)# Initialize memory to persist state between graph runs
[](https://langchain-ai.github.io/langgraph/#__codelineno-4-20)checkpointer = MemorySaver()
[](https://langchain-ai.github.io/langgraph/#__codelineno-4-21)
[](https://langchain-ai.github.io/langgraph/#__codelineno-4-22)app = create_react_agent(model, tools, checkpointer=checkpointer)
[](https://langchain-ai.github.io/langgraph/#__codelineno-4-23)
[](https://langchain-ai.github.io/langgraph/#__codelineno-4-24)# Use the agent
[](https://langchain-ai.github.io/langgraph/#__codelineno-4-25)final_state = app.invoke(
[](https://langchain-ai.github.io/langgraph/#__codelineno-4-26)  {"messages": [{"role": "user", "content": "what is the weather in sf"}]},
[](https://langchain-ai.github.io/langgraph/#__codelineno-4-27)  config={"configurable": {"thread_id": 42}}
[](https://langchain-ai.github.io/langgraph/#__codelineno-4-28))
[](https://langchain-ai.github.io/langgraph/#__codelineno-4-29)final_state["messages"][-1].content

```


```
[](https://langchain-ai.github.io/langgraph/#__codelineno-5-1)"Based on the search results, I can tell you that the current weather in San Francisco is:\n\nTemperature: 60 degrees Fahrenheit\nConditions: Foggy\n\nSan Francisco is known for its microclimates and frequent fog, especially during the summer months. The temperature of 60°F (about 15.5°C) is quite typical for the city, which tends to have mild temperatures year-round. The fog, often referred to as "Karl the Fog" by locals, is a characteristic feature of San Francisco\'s weather, particularly in the mornings and evenings.\n\nIs there anything else you\'d like to know about the weather in San Francisco or any other location?"

```


Now when we pass the same `"thread_id"`, the conversation context is retained via the saved state (i.e. stored list of messages) 

```
[](https://langchain-ai.github.io/langgraph/#__codelineno-6-1)final_state = app.invoke(
[](https://langchain-ai.github.io/langgraph/#__codelineno-6-2)  {"messages": [{"role": "user", "content": "what about ny"}]},
[](https://langchain-ai.github.io/langgraph/#__codelineno-6-3)  config={"configurable": {"thread_id": 42}}
[](https://langchain-ai.github.io/langgraph/#__codelineno-6-4))
[](https://langchain-ai.github.io/langgraph/#__codelineno-6-5)final_state["messages"][-1].content

```


```
[](https://langchain-ai.github.io/langgraph/#__codelineno-7-1)"Based on the search results, I can tell you that the current weather in New York City is:\n\nTemperature: 90 degrees Fahrenheit (approximately 32.2 degrees Celsius)\nConditions: Sunny\n\nThis weather is quite different from what we just saw in San Francisco. New York is experiencing much warmer temperatures right now. Here are a few points to note:\n\n1. The temperature of 90°F is quite hot, typical of summer weather in New York City.\n2. The sunny conditions suggest clear skies, which is great for outdoor activities but also means it might feel even hotter due to direct sunlight.\n3. This kind of weather in New York often comes with high humidity, which can make it feel even warmer than the actual temperature suggests.\n\nIt's interesting to see the stark contrast between San Francisco's mild, foggy weather and New York's hot, sunny conditions. This difference illustrates how varied weather can be across different parts of the United States, even on the same day.\n\nIs there anything else you'd like to know about the weather in New York or any other location?"

```


Tip

LangGraph is a **low-level** framework that allows you to implement any custom agent architectures. Click on the low-level implementation below to see how to implement a tool-calling agent from scratch.

Low-level implementation

```
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-1)fromtypingimport Literal
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-2)
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-3)fromlangchain_anthropicimport ChatAnthropic
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-4)fromlangchain_core.toolsimport tool
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-5)fromlanggraph.checkpoint.memoryimport MemorySaver
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-6)fromlanggraph.graphimport END, START, StateGraph, MessagesState
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-7)fromlanggraph.prebuiltimport ToolNode
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-8)
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-9)
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-10)# Define the tools for the agent to use
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-11)@tool
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-12)defsearch(query: str):
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-13)"""Call to surf the web."""
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-14)  # This is a placeholder, but don't tell the LLM that...
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-15)  if "sf" in query.lower() or "san francisco" in query.lower():
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-16)    return "It's 60 degrees and foggy."
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-17)  return "It's 90 degrees and sunny."
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-18)
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-19)
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-20)tools = [search]
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-21)
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-22)tool_node = ToolNode(tools)
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-23)
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-24)model = ChatAnthropic(model="claude-3-5-sonnet-latest", temperature=0).bind_tools(tools)
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-25)
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-26)# Define the function that determines whether to continue or not
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-27)defshould_continue(state: MessagesState) -> Literal["tools", END]:
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-28)  messages = state['messages']
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-29)  last_message = messages[-1]
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-30)  # If the LLM makes a tool call, then we route to the "tools" node
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-31)  if last_message.tool_calls:
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-32)    return "tools"
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-33)  # Otherwise, we stop (reply to the user)
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-34)  return END
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-35)
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-36)
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-37)# Define the function that calls the model
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-38)defcall_model(state: MessagesState):
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-39)  messages = state['messages']
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-40)  response = model.invoke(messages)
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-41)  # We return a list, because this will get added to the existing list
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-42)  return {"messages": [response]}
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-43)
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-44)
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-45)# Define a new graph
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-46)workflow = StateGraph(MessagesState)
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-47)
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-48)# Define the two nodes we will cycle between
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-49)workflow.add_node("agent", call_model)
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-50)workflow.add_node("tools", tool_node)
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-51)
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-52)# Set the entrypoint as `agent`
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-53)# This means that this node is the first one called
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-54)workflow.add_edge(START, "agent")
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-55)
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-56)# We now add a conditional edge
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-57)workflow.add_conditional_edges(
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-58)  # First, we define the start node. We use `agent`.
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-59)  # This means these are the edges taken after the `agent` node is called.
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-60)  "agent",
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-61)  # Next, we pass in the function that will determine which node is called next.
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-62)  should_continue,
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-63))
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-64)
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-65)# We now add a normal edge from `tools` to `agent`.
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-66)# This means that after `tools` is called, `agent` node is called next.
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-67)workflow.add_edge("tools", 'agent')
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-68)
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-69)# Initialize memory to persist state between graph runs
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-70)checkpointer = MemorySaver()
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-71)
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-72)# Finally, we compile it!
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-73)# This compiles it into a LangChain Runnable,
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-74)# meaning you can use it as you would any other runnable.
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-75)# Note that we're (optionally) passing the memory when compiling the graph
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-76)app = workflow.compile(checkpointer=checkpointer)
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-77)
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-78)# Use the agent
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-79)final_state = app.invoke(
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-80)  {"messages": [{"role": "user", "content": "what is the weather in sf"}]},
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-81)  config={"configurable": {"thread_id": 42}}
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-82))
[](https://langchain-ai.github.io/langgraph/#__codelineno-8-83)final_state["messages"][-1].content

```


**Step-by-step Breakdown** :  Initialize the model and tools.

  * We use `ChatAnthropic` as our LLM. **NOTE:** we need to make sure the model knows that it has these tools available to call. We can do this by converting the LangChain tools into the format for OpenAI tool calling using the `.bind_tools()` method. 
  * We define the tools we want to use - a search tool in our case. It is really easy to create your own tools - see documentation here on how to do that [here](https://python.langchain.com/docs/how_to/custom_tools/). 

Initialize graph with state.

  * We initialize graph (`StateGraph`) by passing state schema (in our case `MessagesState`)
  * `MessagesState` is a prebuilt state schema that has one attribute -- a list of LangChain `Message` objects, as well as logic for merging the updates from each node into the state.

Define graph nodes. There are two main nodes we need: 

  * The `agent` node: responsible for deciding what (if any) actions to take.
  * The `tools` node that invokes tools: if the agent decides to take an action, this node will then execute that action.

Define entry point and graph edges. First, we need to set the entry point for graph execution - `agent` node. Then we define one normal and one conditional edge. Conditional edge means that the destination depends on the contents of the graph's state (`MessagesState`). In our case, the destination is not known until the agent (LLM) decides. 

  * Conditional edge: after the agent is called, we should either: 
    * a. Run tools if the agent said to take an action, OR
    * b. Finish (respond to the user) if the agent did not ask to run tools
  * Normal edge: after the tools are invoked, the graph should always return to the agent to decide what to do next

Compile the graph.

  * When we compile the graph, we turn it into a LangChain [Runnable](https://python.langchain.com/docs/concepts/runnables/), which automatically enables calling `.invoke()`, `.stream()` and `.batch()` with your inputs 
  * We can also optionally pass checkpointer object for persisting state between graph runs, and enabling memory, human-in-the-loop workflows, time travel and more. In our case we use `MemorySaver` - a simple in-memory checkpointer 

Execute the graph.

  1. LangGraph adds the input message to the internal state, then passes the state to the entrypoint node, `"agent"`.
  2. The `"agent"` node executes, invoking the chat model.
  3. The chat model returns an `AIMessage`. LangGraph adds this to the state.
  4. Graph cycles the following steps until there are no more `tool_calls` on `AIMessage`: 
     * If `AIMessage` has `tool_calls`, `"tools"` node executes
     * The `"agent"` node executes again and returns `AIMessage`
  5. Execution progresses to the special `END` value and outputs the final state. And as a result, we get a list of all our chat messages as output.



## Documentation[¶](https://langchain-ai.github.io/langgraph/#documentation "Permanent link")

  * [Tutorials](https://langchain-ai.github.io/langgraph/tutorials/): Learn to build with LangGraph through guided examples.
  * [How-to Guides](https://langchain-ai.github.io/langgraph/how-tos/): Accomplish specific things within LangGraph, from streaming, to adding memory & persistence, to common design patterns (branching, subgraphs, etc.), these are the place to go if you want to copy and run a specific code snippet.
  * [Conceptual Guides](https://langchain-ai.github.io/langgraph/concepts/high_level/): In-depth explanations of the key concepts and principles behind LangGraph, such as nodes, edges, state and more.
  * [API Reference](https://langchain-ai.github.io/langgraph/reference/graphs/): Review important classes and methods, simple examples of how to use the graph and checkpointing APIs, higher-level prebuilt components and more.
  * [LangGraph Platform](https://langchain-ai.github.io/langgraph/concepts/#langgraph-platform): LangGraph Platform is a commercial solution for deploying agentic applications in production, built on the open-source LangGraph framework.



## Resources[¶](https://langchain-ai.github.io/langgraph/#resources "Permanent link")

  * [Built with LangGraph](https://www.langchain.com/built-with-langgraph): Hear how industry leaders use LangGraph to ship powerful, production-ready AI applications.



## Contributing[¶](https://langchain-ai.github.io/langgraph/#contributing "Permanent link")

For more information on how to contribute, see [here](https://github.com/langchain-ai/langgraph/blob/main/CONTRIBUTING.md).

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Next  Learn the basics  ](https://langchain-ai.github.io/langgraph/tutorials/introduction/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
