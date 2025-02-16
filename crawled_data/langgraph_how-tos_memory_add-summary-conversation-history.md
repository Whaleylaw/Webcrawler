---
url: https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#how-to-add-summary-of-the-conversation-history)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to add summary of the conversation history 

[ ](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/?q= "Share")

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
            * [ How to delete messages  ](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/)
            * How to add summary of the conversation history  [ How to add summary of the conversation history  ](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#setup)
              * [ Build the chatbot  ](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#build-the-chatbot)
              * [ Using the graph  ](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#using-the-graph)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#setup)
  * [ Build the chatbot  ](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#build-the-chatbot)
  * [ Using the graph  ](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#using-the-graph)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Memory  ](https://langchain-ai.github.io/langgraph/how-tos#memory)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/memory/add-summary-conversation-history.ipynb "Edit this page")

# How to add summary of the conversation history[¶](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#how-to-add-summary-of-the-conversation-history "Permanent link")

One of the most common use cases for persistence is to use it to keep track of conversation history. This is great - it makes it easy to continue conversations. As conversations get longer and longer, however, this conversation history can build up and take up more and more of the context window. This can often be undesirable as it leads to more expensive and longer calls to the LLM, and potentially ones that error. One way to work around that is to create a summary of the conversation to date, and use that with the past N messages. This guide will go through an example of how to do that.

This will involve a few steps: - Check if the conversation is too long (can be done by checking number of messages or length of messages) - If yes, the create summary (will need a prompt for this) - Then remove all except the last N messages

A big part of this is deleting old messages. For an in depth guide on how to do that, see [this guide](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages)

## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#setup "Permanent link")

First, let's set up the packages we're going to want to use

```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-0-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-0-2)%pip install --quiet -U langgraph langchain_anthropic

```


Next, we need to set API keys for Anthropic (the LLM we will use)

```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-1-1)importgetpass
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-1-2)importos
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-1-5)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-1-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-1-7)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-1-8)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-1-10)_set_env("ANTHROPIC_API_KEY")

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Build the chatbot[¶](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#build-the-chatbot "Permanent link")

Let's now build the chatbot.

```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-1)fromtypingimport Literal
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-2)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-3)fromlangchain_anthropicimport ChatAnthropic
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-4)fromlangchain_core.messagesimport SystemMessage, RemoveMessage
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-5)fromlanggraph.checkpoint.memoryimport MemorySaver
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-6)fromlanggraph.graphimport MessagesState, StateGraph, START, END
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-7)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-8)memory = MemorySaver()
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-9)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-10)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-11)# We will add a `summary` attribute (in addition to `messages` key,
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-12)# which MessagesState already has)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-13)classState(MessagesState):
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-14)  summary: str
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-15)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-16)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-17)# We will use this model for both the conversation and the summarization
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-18)model = ChatAnthropic(model_name="claude-3-haiku-20240307")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-19)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-20)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-21)# Define the logic to call the model
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-22)defcall_model(state: State):
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-23)  # If a summary exists, we add this in as a system message
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-24)  summary = state.get("summary", "")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-25)  if summary:
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-26)    system_message = f"Summary of conversation earlier: {summary}"
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-27)    messages = [SystemMessage(content=system_message)] + state["messages"]
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-28)  else:
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-29)    messages = state["messages"]
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-30)  response = model.invoke(messages)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-31)  # We return a list, because this will get added to the existing list
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-32)  return {"messages": [response]}
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-33)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-34)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-35)# We now define the logic for determining whether to end or summarize the conversation
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-36)defshould_continue(state: State) -> Literal["summarize_conversation", END]:
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-37)"""Return the next node to execute."""
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-38)  messages = state["messages"]
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-39)  # If there are more than six messages, then we summarize the conversation
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-40)  if len(messages) > 6:
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-41)    return "summarize_conversation"
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-42)  # Otherwise we can just end
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-43)  return END
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-44)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-45)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-46)defsummarize_conversation(state: State):
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-47)  # First, we summarize the conversation
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-48)  summary = state.get("summary", "")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-49)  if summary:
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-50)    # If a summary already exists, we use a different system prompt
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-51)    # to summarize it than if one didn't
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-52)    summary_message = (
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-53)      f"This is summary of the conversation to date: {summary}\n\n"
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-54)      "Extend the summary by taking into account the new messages above:"
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-55)    )
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-56)  else:
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-57)    summary_message = "Create a summary of the conversation above:"
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-58)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-59)  messages = state["messages"] + [HumanMessage(content=summary_message)]
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-60)  response = model.invoke(messages)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-61)  # We now need to delete messages that we no longer want to show up
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-62)  # I will delete all but the last two messages, but you can change this
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-63)  delete_messages = [RemoveMessage(id=m.id) for m in state["messages"][:-2]]
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-64)  return {"summary": response.content, "messages": delete_messages}
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-65)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-66)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-67)# Define a new graph
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-68)workflow = StateGraph(State)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-69)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-70)# Define the conversation node and the summarize node
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-71)workflow.add_node("conversation", call_model)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-72)workflow.add_node(summarize_conversation)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-73)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-74)# Set the entrypoint as conversation
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-75)workflow.add_edge(START, "conversation")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-76)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-77)# We now add a conditional edge
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-78)workflow.add_conditional_edges(
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-79)  # First, we define the start node. We use `conversation`.
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-80)  # This means these are the edges taken after the `conversation` node is called.
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-81)  "conversation",
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-82)  # Next, we pass in the function that will determine which node is called next.
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-83)  should_continue,
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-84))
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-85)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-86)# We now add a normal edge from `summarize_conversation` to END.
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-87)# This means that after `summarize_conversation` is called, we end.
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-88)workflow.add_edge("summarize_conversation", END)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-89)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-90)# Finally, we compile it!
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-2-91)app = workflow.compile(checkpointer=memory)

```


API Reference: [ChatAnthropic](https://python.langchain.com/api_reference/anthropic/chat_models/langchain_anthropic.chat_models.ChatAnthropic.html) | [SystemMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.system.SystemMessage.html) | [RemoveMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.modifier.RemoveMessage.html) | [MemorySaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.MemorySaver) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END)

## Using the graph[¶](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#using-the-graph "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-3-1)defprint_update(update):
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-3-2)  for k, v in update.items():
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-3-3)    for m in v["messages"]:
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-3-4)      m.pretty_print()
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-3-5)    if "summary" in v:
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-3-6)      print(v["summary"])

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-4-1)fromlangchain_core.messagesimport HumanMessage
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-4-2)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-4-3)config = {"configurable": {"thread_id": "4"}}
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-4-4)input_message = HumanMessage(content="hi! I'm bob")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-4-5)input_message.pretty_print()
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-4-6)for event in app.stream({"messages": [input_message]}, config, stream_mode="updates"):
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-4-7)  print_update(event)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-4-8)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-4-9)input_message = HumanMessage(content="what's my name?")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-4-10)input_message.pretty_print()
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-4-11)for event in app.stream({"messages": [input_message]}, config, stream_mode="updates"):
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-4-12)  print_update(event)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-4-13)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-4-14)input_message = HumanMessage(content="i like the celtics!")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-4-15)input_message.pretty_print()
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-4-16)for event in app.stream({"messages": [input_message]}, config, stream_mode="updates"):
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-4-17)  print_update(event)

```


API Reference: [HumanMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.human.HumanMessage.html)

```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-5-1)================================[1m Human Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-5-2)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-5-3)hi! I'm bob
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-5-4)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-5-5)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-5-6)It's nice to meet you, Bob! I'm an AI assistant created by Anthropic. How can I help you today?
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-5-7)================================[1m Human Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-5-8)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-5-9)what's my name?
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-5-10)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-5-11)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-5-12)Your name is Bob, as you told me at the beginning of our conversation.
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-5-13)================================[1m Human Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-5-14)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-5-15)i like the celtics!
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-5-16)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-5-17)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-5-18)That's great, the Celtics are a fun team to follow! Basketball is an exciting sport. Do you have a favorite Celtics player or a favorite moment from a Celtics game you've watched? I'd be happy to discuss the team and the sport with you.

```


We can see that so far no summarization has happened - this is because there are only six messages in the list. 

```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-6-1)values = app.get_state(config).values
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-6-2)values

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-7-1){'messages': [HumanMessage(content="hi! I'm bob", id='6534853d-b8a7-44b9-837b-eb7abaf7ebf7'),
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-7-2) AIMessage(content="It's nice to meet you, Bob! I'm an AI assistant created by Anthropic. How can I help you today?", response_metadata={'id': 'msg_015wCFew2vwMQJcpUh2VZ5ah', 'model': 'claude-3-haiku-20240307', 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 12, 'output_tokens': 30}}, id='run-0d33008b-1094-4f5e-94ce-293283fc3024-0'),
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-7-3) HumanMessage(content="what's my name?", id='0a4f203a-b95a-42a9-b1c5-bb20f68b3251'),
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-7-4) AIMessage(content='Your name is Bob, as you told me at the beginning of our conversation.', response_metadata={'id': 'msg_01PLp8wg2xDsJbNR9uCtxcGz', 'model': 'claude-3-haiku-20240307', 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 50, 'output_tokens': 19}}, id='run-3815dd4d-ee0c-4fc2-9889-f6dd40325961-0'),
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-7-5) HumanMessage(content='i like the celtics!', id='ac128172-42d1-4390-b7cc-7bcb2d22ee48'),
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-7-6) AIMessage(content="That's great, the Celtics are a fun team to follow! Basketball is an exciting sport. Do you have a favorite Celtics player or a favorite moment from a Celtics game you've watched? I'd be happy to discuss the team and the sport with you.", response_metadata={'id': 'msg_01CSg5avZEx6CKcZsSvSVXpr', 'model': 'claude-3-haiku-20240307', 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 78, 'output_tokens': 61}}, id='run-698faa28-0f72-495f-8ebe-e948664d2200-0')]}

```


Now let's send another message in

```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-8-1)input_message = HumanMessage(content="i like how much they win")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-8-2)input_message.pretty_print()
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-8-3)for event in app.stream({"messages": [input_message]}, config, stream_mode="updates"):
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-8-4)  print_update(event)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-9-1)================================[1m Human Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-9-2)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-9-3)i like how much they win
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-9-4)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-9-5)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-9-6)That's understandable, the Celtics have been one of the more successful NBA franchises over the years. Their history of winning championships is very impressive. It's always fun to follow a team that regularly competes for titles. What do you think has been the key to the Celtics' sustained success? Is there a particular era or team that stands out as your favorite?
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-9-7)================================[1m Remove Message [0m================================
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-9-8)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-9-9)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-9-10)================================[1m Remove Message [0m================================
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-9-11)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-9-12)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-9-13)================================[1m Remove Message [0m================================
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-9-14)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-9-15)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-9-16)================================[1m Remove Message [0m================================
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-9-17)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-9-18)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-9-19)================================[1m Remove Message [0m================================
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-9-20)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-9-21)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-9-22)================================[1m Remove Message [0m================================
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-9-23)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-9-24)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-9-25)Here is a summary of our conversation so far:
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-9-26)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-9-27)- You introduced yourself as Bob and said you like the Boston Celtics basketball team.
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-9-28)- I acknowledged that it's nice to meet you, Bob, and noted that you had shared your name earlier in the conversation.
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-9-29)- You expressed that you like how much the Celtics win, and I agreed that their history of sustained success and championship pedigree is impressive.
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-9-30)- I asked if you have a favorite Celtics player or moment that stands out to you, and invited further discussion about the team and the sport of basketball.
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-9-31)- The overall tone has been friendly and conversational, with me trying to engage with your interest in the Celtics by asking follow-up questions.

```


If we check the state now, we can see that we have a summary of the conversation, as well as the last two messages 

```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-10-1)values = app.get_state(config).values
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-10-2)values

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-11-1){'messages': [HumanMessage(content='i like how much they win', id='bb916ce7-534c-4d48-9f92-e269f9dc4859'),
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-11-2) AIMessage(content="That's understandable, the Celtics have been one of the more successful NBA franchises over the years. Their history of winning championships is very impressive. It's always fun to follow a team that regularly competes for titles. What do you think has been the key to the Celtics' sustained success? Is there a particular era or team that stands out as your favorite?", response_metadata={'id': 'msg_01B7TMagaM8xBnYXLSMwUDAG', 'model': 'claude-3-haiku-20240307', 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 148, 'output_tokens': 82}}, id='run-c5aa9a8f-7983-4a7f-9c1e-0c0055334ac1-0')],
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-11-3) 'summary': "Here is a summary of our conversation so far:\n\n- You introduced yourself as Bob and said you like the Boston Celtics basketball team.\n- I acknowledged that it's nice to meet you, Bob, and noted that you had shared your name earlier in the conversation.\n- You expressed that you like how much the Celtics win, and I agreed that their history of sustained success and championship pedigree is impressive.\n- I asked if you have a favorite Celtics player or moment that stands out to you, and invited further discussion about the team and the sport of basketball.\n- The overall tone has been friendly and conversational, with me trying to engage with your interest in the Celtics by asking follow-up questions."}

```


We can now resume having a conversation! Note that even though we only have the last two messages, we can still ask it questions about things mentioned earlier in the conversation (because we summarized those)

```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-12-1)input_message = HumanMessage(content="what's my name?")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-12-2)input_message.pretty_print()
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-12-3)for event in app.stream({"messages": [input_message]}, config, stream_mode="updates"):
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-12-4)  print_update(event)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-13-1)================================[1m Human Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-13-2)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-13-3)what's my name?
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-13-4)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-13-5)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-13-6)In our conversation so far, you introduced yourself as Bob. I acknowledged that earlier when you had shared your name.

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-14-1)input_message = HumanMessage(content="what NFL team do you think I like?")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-14-2)input_message.pretty_print()
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-14-3)for event in app.stream({"messages": [input_message]}, config, stream_mode="updates"):
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-14-4)  print_update(event)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-15-1)================================[1m Human Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-15-2)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-15-3)what NFL team do you think I like?
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-15-4)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-15-5)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-15-6)I don't actually have any information about what NFL team you might like. In our conversation so far, you've only mentioned that you're a fan of the Boston Celtics basketball team. I don't have any prior knowledge about your preferences for NFL teams. Unless you provide me with that information, I don't have a basis to guess which NFL team you might be a fan of.

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-16-1)input_message = HumanMessage(content="i like the patriots!")
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-16-2)input_message.pretty_print()
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-16-3)for event in app.stream({"messages": [input_message]}, config, stream_mode="updates"):
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-16-4)  print_update(event)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-17-1)================================[1m Human Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-17-2)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-17-3)i like the patriots!
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-17-4)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-17-5)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-17-6)Okay, got it! Thanks for sharing that you're also a fan of the New England Patriots in the NFL. That makes sense, given your interest in other Boston sports teams like the Celtics. The Patriots have also had a very successful run over the past couple of decades, winning multiple Super Bowls. It's fun to follow winning franchises like the Celtics and Patriots. Do you have a favorite Patriots player or moment that stands out to you?
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-17-7)================================[1m Remove Message [0m================================
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-17-8)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-17-9)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-17-10)================================[1m Remove Message [0m================================
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-17-11)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-17-12)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-17-13)================================[1m Remove Message [0m================================
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-17-14)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-17-15)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-17-16)================================[1m Remove Message [0m================================
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-17-17)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-17-18)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-17-19)================================[1m Remove Message [0m================================
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-17-20)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-17-21)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-17-22)================================[1m Remove Message [0m================================
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-17-23)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-17-24)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-17-25)Okay, extending the summary with the new information:
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-17-26)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-17-27)- You initially introduced yourself as Bob and said you like the Boston Celtics basketball team. 
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-17-28)- I acknowledged that and we discussed your appreciation for the Celtics' history of winning.
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-17-29)- You then asked what your name was, and I reminded you that you had introduced yourself as Bob earlier in the conversation.
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-17-30)- You followed up by asking what NFL team I thought you might like, and I explained that I didn't have any prior information about your NFL team preferences.
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-17-31)- You then revealed that you are also a fan of the New England Patriots, which made sense given your Celtics fandom.
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-17-32)- I responded positively to this new information, noting the Patriots' own impressive success and dynasty over the past couple of decades.
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-17-33)- I then asked if you have a particular favorite Patriots player or moment that stands out to you, continuing the friendly, conversational tone.
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-17-34)
[](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__codelineno-17-35)Overall, the discussion has focused on your sports team preferences, with you sharing that you are a fan of both the Celtics and the Patriots. I've tried to engage with your interests and ask follow-up questions to keep the dialogue flowing.

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to delete messages  ](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/) [ Next  How to add semantic search to your agent's memory  ](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
