---
url: https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#how-to-manage-conversation-history)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to manage conversation history 

[ ](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/?q= "Share")

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
            * How to manage conversation history  [ How to manage conversation history  ](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#setup)
              * [ Build the agent  ](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#build-the-agent)
              * [ Filtering messages  ](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#filtering-messages)
            * [ How to delete messages  ](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#setup)
  * [ Build the agent  ](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#build-the-agent)
  * [ Filtering messages  ](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#filtering-messages)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Memory  ](https://langchain-ai.github.io/langgraph/how-tos#memory)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/memory/manage-conversation-history.ipynb "Edit this page")

# How to manage conversation history[¶](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#how-to-manage-conversation-history "Permanent link")

One of the most common use cases for persistence is to use it to keep track of conversation history. This is great - it makes it easy to continue conversations. As conversations get longer and longer, however, this conversation history can build up and take up more and more of the context window. This can often be undesirable as it leads to more expensive and longer calls to the LLM, and potentially ones that error. In order to prevent this from happening, you need to probably manage the conversation history.

Note: this guide focuses on how to do this in LangGraph, where you can fully customize how this is done. If you want a more off-the-shelf solution, you can look into functionality provided in LangChain:

  * [How to filter messages](https://python.langchain.com/docs/how_to/filter_messages/)
  * [How to trim messages](https://python.langchain.com/docs/how_to/trim_messages/)



## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#setup "Permanent link")

First, let's set up the packages we're going to want to use

```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-0-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-0-2)%pip install --quiet -U langgraph langchain_anthropic

```


Next, we need to set API keys for Anthropic (the LLM we will use)

```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-1-1)importgetpass
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-1-2)importos
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-1-5)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-1-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-1-7)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-1-8)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-1-10)_set_env("ANTHROPIC_API_KEY")

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Build the agent[¶](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#build-the-agent "Permanent link")

Let's now build a simple ReAct style agent.

```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-1)fromtypingimport Literal
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-2)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-3)fromlangchain_anthropicimport ChatAnthropic
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-4)fromlangchain_core.toolsimport tool
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-5)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-6)fromlanggraph.checkpoint.memoryimport MemorySaver
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-7)fromlanggraph.graphimport MessagesState, StateGraph, START, END
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-8)fromlanggraph.prebuiltimport ToolNode
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-9)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-10)memory = MemorySaver()
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-11)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-12)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-13)@tool
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-14)defsearch(query: str):
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-15)"""Call to surf the web."""
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-16)  # This is a placeholder for the actual implementation
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-17)  # Don't let the LLM know this though 😊
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-18)  return "It's sunny in San Francisco, but you better look out if you're a Gemini 😈."
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-19)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-20)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-21)tools = [search]
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-22)tool_node = ToolNode(tools)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-23)model = ChatAnthropic(model_name="claude-3-haiku-20240307")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-24)bound_model = model.bind_tools(tools)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-25)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-26)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-27)defshould_continue(state: MessagesState):
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-28)"""Return the next node to execute."""
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-29)  last_message = state["messages"][-1]
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-30)  # If there is no function call, then we finish
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-31)  if not last_message.tool_calls:
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-32)    return END
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-33)  # Otherwise if there is, we continue
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-34)  return "action"
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-35)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-36)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-37)# Define the function that calls the model
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-38)defcall_model(state: MessagesState):
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-39)  response = bound_model.invoke(state["messages"])
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-40)  # We return a list, because this will get added to the existing list
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-41)  return {"messages": response}
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-42)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-43)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-44)# Define a new graph
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-45)workflow = StateGraph(MessagesState)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-46)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-47)# Define the two nodes we will cycle between
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-48)workflow.add_node("agent", call_model)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-49)workflow.add_node("action", tool_node)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-50)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-51)# Set the entrypoint as `agent`
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-52)# This means that this node is the first one called
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-53)workflow.add_edge(START, "agent")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-54)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-55)# We now add a conditional edge
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-56)workflow.add_conditional_edges(
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-57)  # First, we define the start node. We use `agent`.
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-58)  # This means these are the edges taken after the `agent` node is called.
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-59)  "agent",
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-60)  # Next, we pass in the function that will determine which node is called next.
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-61)  should_continue,
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-62)  # Next, we pass in the path map - all the possible nodes this edge could go to
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-63)  ["action", END],
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-64))
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-65)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-66)# We now add a normal edge from `tools` to `agent`.
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-67)# This means that after `tools` is called, `agent` node is called next.
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-68)workflow.add_edge("action", "agent")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-69)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-70)# Finally, we compile it!
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-71)# This compiles it into a LangChain Runnable,
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-72)# meaning you can use it as you would any other runnable
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-2-73)app = workflow.compile(checkpointer=memory)

```


API Reference: [ChatAnthropic](https://python.langchain.com/api_reference/anthropic/chat_models/langchain_anthropic.chat_models.ChatAnthropic.html) | [tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html) | [MemorySaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.MemorySaver) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END) | [ToolNode](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.ToolNode)

```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-3-1)fromlangchain_core.messagesimport HumanMessage
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-3-2)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-3-3)config = {"configurable": {"thread_id": "2"}}
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-3-4)input_message = HumanMessage(content="hi! I'm bob")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-3-5)for event in app.stream({"messages": [input_message]}, config, stream_mode="values"):
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-3-6)  event["messages"][-1].pretty_print()
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-3-7)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-3-8)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-3-9)input_message = HumanMessage(content="what's my name?")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-3-10)for event in app.stream({"messages": [input_message]}, config, stream_mode="values"):
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-3-11)  event["messages"][-1].pretty_print()

```


API Reference: [HumanMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.human.HumanMessage.html)

```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-4-1)================================[1m Human Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-4-2)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-4-3)hi! I'm bob
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-4-4)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-4-5)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-4-6)Nice to meet you, Bob! As an AI assistant, I don't have a physical form, but I'm happy to chat with you and try my best to help out however I can. Please feel free to ask me anything, and I'll do my best to provide useful information or assistance.
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-4-7)================================[1m Human Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-4-8)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-4-9)what's my name?
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-4-10)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-4-11)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-4-12)You said your name is Bob, so that is the name I have for you.

```


## Filtering messages[¶](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#filtering-messages "Permanent link")

The most straight-forward thing to do to prevent conversation history from blowing up is to filter the list of messages before they get passed to the LLM. This involves two parts: defining a function to filter messages, and then adding it to the graph. See the example below which defines a really simple `filter_messages` function and then uses it.

```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-1)fromtypingimport Literal
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-2)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-3)fromlangchain_anthropicimport ChatAnthropic
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-4)fromlangchain_core.toolsimport tool
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-5)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-6)fromlanggraph.checkpoint.memoryimport MemorySaver
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-7)fromlanggraph.graphimport MessagesState, StateGraph, START
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-8)fromlanggraph.prebuiltimport ToolNode
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-9)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-10)memory = MemorySaver()
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-11)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-12)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-13)@tool
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-14)defsearch(query: str):
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-15)"""Call to surf the web."""
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-16)  # This is a placeholder for the actual implementation
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-17)  # Don't let the LLM know this though 😊
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-18)  return "It's sunny in San Francisco, but you better look out if you're a Gemini 😈."
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-19)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-20)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-21)tools = [search]
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-22)tool_node = ToolNode(tools)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-23)model = ChatAnthropic(model_name="claude-3-haiku-20240307")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-24)bound_model = model.bind_tools(tools)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-25)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-26)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-27)defshould_continue(state: MessagesState):
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-28)"""Return the next node to execute."""
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-29)  last_message = state["messages"][-1]
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-30)  # If there is no function call, then we finish
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-31)  if not last_message.tool_calls:
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-32)    return END
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-33)  # Otherwise if there is, we continue
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-34)  return "action"
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-35)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-36)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-37)deffilter_messages(messages: list):
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-38)  # This is very simple helper function which only ever uses the last message
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-39)  return messages[-1:]
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-40)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-41)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-42)# Define the function that calls the model
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-43)defcall_model(state: MessagesState):
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-44)  messages = filter_messages(state["messages"])
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-45)  response = bound_model.invoke(messages)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-46)  # We return a list, because this will get added to the existing list
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-47)  return {"messages": response}
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-48)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-49)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-50)# Define a new graph
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-51)workflow = StateGraph(MessagesState)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-52)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-53)# Define the two nodes we will cycle between
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-54)workflow.add_node("agent", call_model)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-55)workflow.add_node("action", tool_node)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-56)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-57)# Set the entrypoint as `agent`
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-58)# This means that this node is the first one called
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-59)workflow.add_edge(START, "agent")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-60)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-61)# We now add a conditional edge
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-62)workflow.add_conditional_edges(
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-63)  # First, we define the start node. We use `agent`.
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-64)  # This means these are the edges taken after the `agent` node is called.
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-65)  "agent",
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-66)  # Next, we pass in the function that will determine which node is called next.
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-67)  should_continue,
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-68)  # Next, we pass in the pathmap - all the possible nodes this edge could go to
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-69)  ["action", END],
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-70))
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-71)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-72)# We now add a normal edge from `tools` to `agent`.
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-73)# This means that after `tools` is called, `agent` node is called next.
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-74)workflow.add_edge("action", "agent")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-75)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-76)# Finally, we compile it!
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-77)# This compiles it into a LangChain Runnable,
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-78)# meaning you can use it as you would any other runnable
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-5-79)app = workflow.compile(checkpointer=memory)

```


API Reference: [ChatAnthropic](https://python.langchain.com/api_reference/anthropic/chat_models/langchain_anthropic.chat_models.ChatAnthropic.html) | [tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html) | [MemorySaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.MemorySaver) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [ToolNode](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.ToolNode)

```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-6-1)fromlangchain_core.messagesimport HumanMessage
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-6-2)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-6-3)config = {"configurable": {"thread_id": "2"}}
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-6-4)input_message = HumanMessage(content="hi! I'm bob")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-6-5)for event in app.stream({"messages": [input_message]}, config, stream_mode="values"):
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-6-6)  event["messages"][-1].pretty_print()
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-6-7)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-6-8)# This will now not remember the previous messages
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-6-9)# (because we set `messages[-1:]` in the filter messages argument)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-6-10)input_message = HumanMessage(content="what's my name?")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-6-11)for event in app.stream({"messages": [input_message]}, config, stream_mode="values"):
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-6-12)  event["messages"][-1].pretty_print()

```


API Reference: [HumanMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.human.HumanMessage.html)

```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-7-1)================================[1m Human Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-7-2)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-7-3)hi! I'm bob
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-7-4)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-7-5)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-7-6)Nice to meet you, Bob! I'm Claude, an AI assistant created by Anthropic. It's a pleasure to chat with you. Feel free to ask me anything, I'm here to help!
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-7-7)================================[1m Human Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-7-8)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-7-9)what's my name?
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-7-10)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-7-11)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__codelineno-7-12)I'm afraid I don't actually know your name. As an AI assistant, I don't have information about the specific identities of the people I talk to. I only know what is provided to me during our conversation.

```


In the above example we defined the `filter_messages` function ourselves. We also provide off-the-shelf ways to trim and filter messages in LangChain. 

  * [How to filter messages](https://python.langchain.com/docs/how_to/filter_messages/)
  * [How to trim messages](https://python.langchain.com/docs/how_to/trim_messages/)

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to add cross-thread persistence (functional API)  ](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/) [ Next  How to delete messages  ](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/memory/manage-conversation-history/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
