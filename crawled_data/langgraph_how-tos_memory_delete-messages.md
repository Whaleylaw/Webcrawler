---
url: https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#how-to-delete-messages)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to delete messages 

[ ](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/?q= "Share")

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
          * Memory  Memory 
            * [ Memory  ](https://langchain-ai.github.io/langgraph/how-tos#memory)
            * [ How to manage conversation history  ](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/)
            * How to delete messages  [ How to delete messages  ](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#setup)
              * [ Build the agent  ](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#build-the-agent)
              * [ Manually deleting messages  ](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#manually-deleting-messages)
              * [ Programmatically deleting messages  ](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#programmatically-deleting-messages)
            * [ How to add summary of the conversation history  ](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/)
            * [ How to add semantic search to your agent's memory  ](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/)
          * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraph/how-tos#human-in-the-loop)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#setup)
  * [ Build the agent  ](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#build-the-agent)
  * [ Manually deleting messages  ](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#manually-deleting-messages)
  * [ Programmatically deleting messages  ](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#programmatically-deleting-messages)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Memory  ](https://langchain-ai.github.io/langgraph/how-tos#memory)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/memory/delete-messages.ipynb "Edit this page")

# How to delete messages[¶](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#how-to-delete-messages "Permanent link")

One of the common states for a graph is a list of messages. Usually you only add messages to that state. However, sometimes you may want to remove messages (either by directly modifying the state or as part of the graph). To do that, you can use the `RemoveMessage` modifier. In this guide, we will cover how to do that.

The key idea is that each state key has a `reducer` key. This key specifies how to combine updates to the state. The default `MessagesState` has a messages key, and the reducer for that key accepts these `RemoveMessage` modifiers. That reducer then uses these `RemoveMessage` to delete messages from the key.

So note that just because your graph state has a key that is a list of messages, it doesn't mean that that this `RemoveMessage` modifier will work. You also have to have a `reducer` defined that knows how to work with this.

**NOTE** : Many models expect certain rules around lists of messages. For example, some expect them to start with a `user` message, others expect all messages with tool calls to be followed by a tool message. **When deleting messages, you will want to make sure you don't violate these rules.**

## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#setup "Permanent link")

First, let's build a simple graph that uses messages. Note that it's using the `MessagesState` which has the required `reducer`.

```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-0-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-0-2)%pip install --quiet -U langgraph langchain_anthropic

```


Next, we need to set API keys for Anthropic (the LLM we will use)

```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-1-1)importgetpass
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-1-2)importos
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-1-5)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-1-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-1-7)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-1-8)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-1-10)_set_env("ANTHROPIC_API_KEY")

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-2-1)ANTHROPIC_API_KEY: ········

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Build the agent[¶](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#build-the-agent "Permanent link")

Let's now build a simple ReAct style agent.

```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-1)fromtypingimport Literal
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-2)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-3)fromlangchain_anthropicimport ChatAnthropic
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-4)fromlangchain_core.toolsimport tool
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-5)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-6)fromlanggraph.checkpoint.memoryimport MemorySaver
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-7)fromlanggraph.graphimport MessagesState, StateGraph, START, END
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-8)fromlanggraph.prebuiltimport ToolNode
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-9)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-10)memory = MemorySaver()
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-11)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-12)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-13)@tool
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-14)defsearch(query: str):
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-15)"""Call to surf the web."""
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-16)  # This is a placeholder for the actual implementation
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-17)  # Don't let the LLM know this though 😊
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-18)  return "It's sunny in San Francisco, but you better look out if you're a Gemini 😈."
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-19)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-20)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-21)tools = [search]
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-22)tool_node = ToolNode(tools)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-23)model = ChatAnthropic(model_name="claude-3-haiku-20240307")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-24)bound_model = model.bind_tools(tools)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-25)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-26)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-27)defshould_continue(state: MessagesState):
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-28)"""Return the next node to execute."""
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-29)  last_message = state["messages"][-1]
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-30)  # If there is no function call, then we finish
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-31)  if not last_message.tool_calls:
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-32)    return END
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-33)  # Otherwise if there is, we continue
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-34)  return "action"
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-35)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-36)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-37)# Define the function that calls the model
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-38)defcall_model(state: MessagesState):
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-39)  response = model.invoke(state["messages"])
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-40)  # We return a list, because this will get added to the existing list
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-41)  return {"messages": response}
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-42)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-43)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-44)# Define a new graph
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-45)workflow = StateGraph(MessagesState)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-46)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-47)# Define the two nodes we will cycle between
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-48)workflow.add_node("agent", call_model)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-49)workflow.add_node("action", tool_node)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-50)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-51)# Set the entrypoint as `agent`
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-52)# This means that this node is the first one called
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-53)workflow.add_edge(START, "agent")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-54)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-55)# We now add a conditional edge
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-56)workflow.add_conditional_edges(
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-57)  # First, we define the start node. We use `agent`.
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-58)  # This means these are the edges taken after the `agent` node is called.
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-59)  "agent",
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-60)  # Next, we pass in the function that will determine which node is called next.
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-61)  should_continue,
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-62)  # Next, we pass in the path map - all the possible nodes this edge could go to
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-63)  ["action", END],
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-64))
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-65)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-66)# We now add a normal edge from `tools` to `agent`.
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-67)# This means that after `tools` is called, `agent` node is called next.
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-68)workflow.add_edge("action", "agent")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-69)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-70)# Finally, we compile it!
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-71)# This compiles it into a LangChain Runnable,
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-72)# meaning you can use it as you would any other runnable
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-3-73)app = workflow.compile(checkpointer=memory)

```


API Reference: [ChatAnthropic](https://python.langchain.com/api_reference/anthropic/chat_models/langchain_anthropic.chat_models.ChatAnthropic.html) | [tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html) | [MemorySaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.MemorySaver) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END) | [ToolNode](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.ToolNode)

```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-4-1)fromlangchain_core.messagesimport HumanMessage
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-4-2)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-4-3)config = {"configurable": {"thread_id": "2"}}
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-4-4)input_message = HumanMessage(content="hi! I'm bob")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-4-5)for event in app.stream({"messages": [input_message]}, config, stream_mode="values"):
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-4-6)  event["messages"][-1].pretty_print()
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-4-7)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-4-8)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-4-9)input_message = HumanMessage(content="what's my name?")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-4-10)for event in app.stream({"messages": [input_message]}, config, stream_mode="values"):
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-4-11)  event["messages"][-1].pretty_print()

```


API Reference: [HumanMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.human.HumanMessage.html)

```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-5-1)================================[1m Human Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-5-2)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-5-3)hi! I'm bob
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-5-4)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-5-5)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-5-6)It's nice to meet you, Bob! I'm an AI assistant created by Anthropic. I'm here to help out with any questions or tasks you might have. Please let me know if there's anything I can assist you with.
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-5-7)================================[1m Human Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-5-8)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-5-9)what's my name?
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-5-10)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-5-11)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-5-12)You said your name is Bob.

```


## Manually deleting messages[¶](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#manually-deleting-messages "Permanent link")

First, we will cover how to manually delete messages. Let's take a look at the current state of the thread:

```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-6-1)messages = app.get_state(config).values["messages"]
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-6-2)messages

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-7-1)[HumanMessage(content="hi! I'm bob", additional_kwargs={}, response_metadata={}, id='db576005-3a60-4b3b-8925-dc602ac1c571'),
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-7-2) AIMessage(content="It's nice to meet you, Bob! I'm an AI assistant created by Anthropic. I'm here to help out with any questions or tasks you might have. Please let me know if there's anything I can assist you with.", additional_kwargs={}, response_metadata={'id': 'msg_01BKAnYxmoC6bQ9PpCuHk8ZT', 'model': 'claude-3-haiku-20240307', 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 12, 'output_tokens': 52}}, id='run-3a60c536-b207-4c56-98f3-03f94d49a9e4-0', usage_metadata={'input_tokens': 12, 'output_tokens': 52, 'total_tokens': 64}),
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-7-3) HumanMessage(content="what's my name?", additional_kwargs={}, response_metadata={}, id='2088c465-400b-430b-ad80-fad47dc1f2d6'),
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-7-4) AIMessage(content='You said your name is Bob.', additional_kwargs={}, response_metadata={'id': 'msg_013UWTLTzwZi81vke8mMQ2KP', 'model': 'claude-3-haiku-20240307', 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 72, 'output_tokens': 10}}, id='run-3a6883be-0c52-4938-af98-e9e7476659eb-0', usage_metadata={'input_tokens': 72, 'output_tokens': 10, 'total_tokens': 82})]

```


We can call `update_state` and pass in the id of the first message. This will delete that message.

```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-8-1)fromlangchain_core.messagesimport RemoveMessage
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-8-2)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-8-3)app.update_state(config, {"messages": RemoveMessage(id=messages[0].id)})

```


API Reference: [RemoveMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.modifier.RemoveMessage.html)

```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-9-1){'configurable': {'thread_id': '2',
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-9-2) 'checkpoint_ns': '',
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-9-3) 'checkpoint_id': '1ef75157-f251-6a2a-8005-82a86a6593a0'}}

```


If we now look at the messages, we can verify that the first one was deleted.

```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-10-1)messages = app.get_state(config).values["messages"]
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-10-2)messages

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-11-1)[AIMessage(content="It's nice to meet you, Bob! I'm Claude, an AI assistant created by Anthropic. How can I assist you today?", response_metadata={'id': 'msg_01XPSAenmSqK8rX2WgPZHfz7', 'model': 'claude-3-haiku-20240307', 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 12, 'output_tokens': 32}}, id='run-1c69af09-adb1-412d-9010-2456e5a555fb-0', usage_metadata={'input_tokens': 12, 'output_tokens': 32, 'total_tokens': 44}),
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-11-2) HumanMessage(content="what's my name?", id='f3c71afe-8ce2-4ed0-991e-65021f03b0a5'),
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-11-3) AIMessage(content='Your name is Bob, as you introduced yourself at the beginning of our conversation.', response_metadata={'id': 'msg_01BPZdwsjuMAbC1YAkqawXaF', 'model': 'claude-3-haiku-20240307', 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 52, 'output_tokens': 19}}, id='run-b2eb9137-2f4e-446f-95f5-3d5f621a2cf8-0', usage_metadata={'input_tokens': 52, 'output_tokens': 19, 'total_tokens': 71})]

```


## Programmatically deleting messages[¶](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#programmatically-deleting-messages "Permanent link")

We can also delete messages programmatically from inside the graph. Here we'll modify the graph to delete any old messages (longer than 3 messages ago) at the end of a graph run.

```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-12-1)fromlangchain_core.messagesimport RemoveMessage
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-12-2)fromlanggraph.graphimport END
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-12-3)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-12-4)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-12-5)defdelete_messages(state):
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-12-6)  messages = state["messages"]
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-12-7)  if len(messages) > 3:
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-12-8)    return {"messages": [RemoveMessage(id=m.id) for m in messages[:-3]]}
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-12-9)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-12-10)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-12-11)# We need to modify the logic to call delete_messages rather than end right away
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-12-12)defshould_continue(state: MessagesState) -> Literal["action", "delete_messages"]:
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-12-13)"""Return the next node to execute."""
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-12-14)  last_message = state["messages"][-1]
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-12-15)  # If there is no function call, then we call our delete_messages function
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-12-16)  if not last_message.tool_calls:
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-12-17)    return "delete_messages"
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-12-18)  # Otherwise if there is, we continue
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-12-19)  return "action"
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-12-20)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-12-21)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-12-22)# Define a new graph
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-12-23)workflow = StateGraph(MessagesState)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-12-24)workflow.add_node("agent", call_model)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-12-25)workflow.add_node("action", tool_node)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-12-26)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-12-27)# This is our new node we're defining
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-12-28)workflow.add_node(delete_messages)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-12-29)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-12-30)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-12-31)workflow.add_edge(START, "agent")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-12-32)workflow.add_conditional_edges(
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-12-33)  "agent",
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-12-34)  should_continue,
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-12-35))
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-12-36)workflow.add_edge("action", "agent")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-12-37)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-12-38)# This is the new edge we're adding: after we delete messages, we finish
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-12-39)workflow.add_edge("delete_messages", END)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-12-40)app = workflow.compile(checkpointer=memory)

```


API Reference: [RemoveMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.modifier.RemoveMessage.html) | [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END)

We can now try this out. We can call the graph twice and then check the state

```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-13-1)fromlangchain_core.messagesimport HumanMessage
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-13-2)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-13-3)config = {"configurable": {"thread_id": "3"}}
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-13-4)input_message = HumanMessage(content="hi! I'm bob")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-13-5)for event in app.stream({"messages": [input_message]}, config, stream_mode="values"):
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-13-6)  print([(message.type, message.content) for message in event["messages"]])
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-13-7)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-13-8)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-13-9)input_message = HumanMessage(content="what's my name?")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-13-10)for event in app.stream({"messages": [input_message]}, config, stream_mode="values"):
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-13-11)  print([(message.type, message.content) for message in event["messages"]])

```


API Reference: [HumanMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.human.HumanMessage.html)

```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-14-1)[('human', "hi! I'm bob")]
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-14-2)[('human', "hi! I'm bob"), ('ai', "Hello Bob! It's nice to meet you. I'm an AI assistant created by Anthropic. I'm here to help with any questions or tasks you might have. Please let me know how I can assist you.")]
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-14-3)[('human', "hi! I'm bob"), ('ai', "Hello Bob! It's nice to meet you. I'm an AI assistant created by Anthropic. I'm here to help with any questions or tasks you might have. Please let me know how I can assist you."), ('human', "what's my name?")]
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-14-4)[('human', "hi! I'm bob"), ('ai', "Hello Bob! It's nice to meet you. I'm an AI assistant created by Anthropic. I'm here to help with any questions or tasks you might have. Please let me know how I can assist you."), ('human', "what's my name?"), ('ai', 'You said your name is Bob, so that is the name I have for you.')]
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-14-5)[('ai', "Hello Bob! It's nice to meet you. I'm an AI assistant created by Anthropic. I'm here to help with any questions or tasks you might have. Please let me know how I can assist you."), ('human', "what's my name?"), ('ai', 'You said your name is Bob, so that is the name I have for you.')]

```


If we now check the state, we should see that it is only three messages long. This is because we just deleted the earlier messages - otherwise it would be four! 

```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-15-1)messages = app.get_state(config).values["messages"]
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-15-2)messages

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-16-1)[AIMessage(content="Hello Bob! It's nice to meet you. I'm an AI assistant created by Anthropic. I'm here to help with any questions or tasks you might have. Please let me know how I can assist you.", response_metadata={'id': 'msg_01XPEgPPbcnz5BbGWUDWTmzG', 'model': 'claude-3-haiku-20240307', 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 12, 'output_tokens': 48}}, id='run-eded3820-b6a9-4d66-9210-03ca41787ce6-0', usage_metadata={'input_tokens': 12, 'output_tokens': 48, 'total_tokens': 60}),
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-16-2) HumanMessage(content="what's my name?", id='a0ea2097-3280-402b-92e1-67177b807ae8'),
[](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__codelineno-16-3) AIMessage(content='You said your name is Bob, so that is the name I have for you.', response_metadata={'id': 'msg_01JGT62pxhrhN4SykZ57CSjW', 'model': 'claude-3-haiku-20240307', 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 68, 'output_tokens': 20}}, id='run-ace3519c-81f8-45fe-a777-91f42d48b3a3-0', usage_metadata={'input_tokens': 68, 'output_tokens': 20, 'total_tokens': 88})]

```


Remember, when deleting messages you will want to make sure that the remaining message list is still valid. This message list **may actually not be** - this is because it currently starts with an AI message, which some models do not allow.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to manage conversation history  ](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/) [ Next  How to add summary of the conversation history  ](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
