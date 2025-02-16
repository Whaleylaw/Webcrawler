---
url: https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#how-to-integrate-langgraph-with-autogen-crewai-and-other-frameworks)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to integrate LangGraph with AutoGen, CrewAI, and other frameworks 

[ ](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/?q= "Share")

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
          * [ Multi-agent  ](https://langchain-ai.github.io/langgraph/how-tos#multi-agent)
          * [ State Management  ](https://langchain-ai.github.io/langgraph/how-tos#state-management)
          * Other  Other 
            * [ Other  ](https://langchain-ai.github.io/langgraph/how-tos#other)
            * [ How to run a graph asynchronously  ](https://langchain-ai.github.io/langgraph/how-tos/async/)
            * [ How to force tool-calling agent to structure output  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/)
            * [ How to pass custom run ID or set tags and metadata for graph runs in LangSmith  ](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/)
            * How to integrate LangGraph with AutoGen, CrewAI, and other frameworks  [ How to integrate LangGraph with AutoGen, CrewAI, and other frameworks  ](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#setup)
              * [ Define AutoGen agent  ](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#define-autogen-agent)
              * [ Create the graph  ](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#create-the-graph)
              * [ Run the graph  ](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#run-the-graph)
            * [ How to integrate LangGraph (functional API) with AutoGen, CrewAI, and other frameworks  ](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration-functional/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#setup)
  * [ Define AutoGen agent  ](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#define-autogen-agent)
  * [ Create the graph  ](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#create-the-graph)
  * [ Run the graph  ](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#run-the-graph)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Other  ](https://langchain-ai.github.io/langgraph/how-tos#other)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/autogen-integration.ipynb "Edit this page")

# How to integrate LangGraph with AutoGen, CrewAI, and other frameworks[¶](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#how-to-integrate-langgraph-with-autogen-crewai-and-other-frameworks "Permanent link")

LangGraph is a framework for building agentic and multi-agent applications. LangGraph can be easily integrated with other agent frameworks. 

The primary reasons you might want to integrate LangGraph with other agent frameworks:

  * create [multi-agent systems](https://langchain-ai.github.io/langgraph/concepts/multi_agent) where individual agents are built with different frameworks
  * leverage LangGraph to add features like [persistence](https://langchain-ai.github.io/langgraph/concepts/persistence), [streaming](https://langchain-ai.github.io/langgraph/concepts/streaming), [short and long-term memory](https://langchain-ai.github.io/langgraph/concepts/memory) and more



The simplest way to integrate agents from other frameworks is by calling those agents inside a LangGraph [node](https://langchain-ai.github.io/langgraph/concepts/low_level/#nodes):

```
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-0-1)fromlanggraph.graphimport StateGraph, MessagesState, START
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-0-2)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-0-3)autogen_agent = autogen.AssistantAgent(name="assistant", ...)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-0-4)user_proxy = autogen.UserProxyAgent(name="user_proxy", ...)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-0-5)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-0-6)defcall_autogen_agent(state: MessagesState):
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-0-7)  response = user_proxy.initiate_chat(
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-0-8)    autogen_agent,
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-0-9)    message=state["messages"][-1],
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-0-10)    ...
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-0-11)  )
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-0-12)  ...
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-0-13)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-0-14)graph = (
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-0-15)  StateGraph(MessagesState)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-0-16)  .add_node(call_autogen_agent)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-0-17)  .add_edge(START, "call_autogen_agent")
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-0-18)  .compile()
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-0-19))
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-0-20)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-0-21)graph.invoke({
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-0-22)  "messages": [
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-0-23)    {
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-0-24)      "role": "user",
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-0-25)      "content": "Find numbers between 10 and 30 in fibonacci sequence",
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-0-26)    }
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-0-27)  ]
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-0-28)})

```


API Reference: [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START)

In this guide we show how to build a LangGraph chatbot that integrates with AutoGen, but you can follow the same approach with other frameworks.

## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#setup "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-1-1)%pip install autogen langgraph

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-2-1)importgetpass
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-2-2)importos
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-2-3)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-2-4)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-2-5)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-2-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-2-7)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-2-8)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-2-9)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-2-10)_set_env("OPENAI_API_KEY")

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-3-1)OPENAI_API_KEY: ········

```


## Define AutoGen agent[¶](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#define-autogen-agent "Permanent link")

Here we define our AutoGen agent. Adapted from official tutorial [here](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_web_info.ipynb).

```
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-4-1)importautogen
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-4-2)importos
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-4-3)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-4-4)config_list = [{"model": "gpt-4o", "api_key": os.environ["OPENAI_API_KEY"]}]
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-4-5)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-4-6)llm_config = {
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-4-7)  "timeout": 600,
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-4-8)  "cache_seed": 42,
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-4-9)  "config_list": config_list,
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-4-10)  "temperature": 0,
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-4-11)}
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-4-12)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-4-13)autogen_agent = autogen.AssistantAgent(
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-4-14)  name="assistant",
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-4-15)  llm_config=llm_config,
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-4-16))
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-4-17)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-4-18)user_proxy = autogen.UserProxyAgent(
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-4-19)  name="user_proxy",
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-4-20)  human_input_mode="NEVER",
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-4-21)  max_consecutive_auto_reply=10,
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-4-22)  is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-4-23)  code_execution_config={
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-4-24)    "work_dir": "web",
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-4-25)    "use_docker": False,
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-4-26)  }, # Please set use_docker=True if docker is available to run the generated code. Using docker is safer than running the generated code directly.
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-4-27)  llm_config=llm_config,
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-4-28)  system_message="Reply TERMINATE if the task has been solved at full satisfaction. Otherwise, reply CONTINUE, or the reason why the task is not solved yet.",
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-4-29))

```


## Create the graph[¶](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#create-the-graph "Permanent link")

We will now create a LangGraph chatbot graph that calls AutoGen agent.

```
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-5-1)fromtypingimport Literal, TypedDict
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-5-2)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-5-3)fromlangchain_core.messagesimport convert_to_openai_messages
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-5-4)fromlanggraph.graphimport StateGraph, MessagesState, START
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-5-5)fromlanggraph.checkpoint.memoryimport MemorySaver
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-5-6)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-5-7)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-5-8)defcall_autogen_agent(state: MessagesState):
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-5-9)  # convert to openai-style messages
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-5-10)  messages = convert_to_openai_messages(state["messages"])
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-5-11)  response = user_proxy.initiate_chat(
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-5-12)    autogen_agent,
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-5-13)    message=messages[-1],
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-5-14)    # pass previous message history as context
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-5-15)    carryover=messages[:-1],
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-5-16)  )
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-5-17)  # get the final response from the agent
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-5-18)  content = response.chat_history[-1]["content"]
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-5-19)  return {"messages": {"role": "assistant", "content": content}}
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-5-20)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-5-21)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-5-22)# add short-term memory for storing conversation history
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-5-23)checkpointer = MemorySaver()
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-5-24)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-5-25)builder = StateGraph(MessagesState)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-5-26)builder.add_node(call_autogen_agent)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-5-27)builder.add_edge(START, "call_autogen_agent")
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-5-28)graph = builder.compile(checkpointer=checkpointer)

```


API Reference: [convert_to_openai_messages](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.utils.convert_to_openai_messages.html) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [MemorySaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.MemorySaver)

```
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-6-1)fromIPython.displayimport display, Image
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-6-2)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-6-3)display(Image(graph.get_graph().draw_mermaid_png()))

```


![]()

## Run the graph[¶](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#run-the-graph "Permanent link")

We can now run the graph.

```
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-7-1)# pass the thread ID to persist agent outputs for future interactions
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-7-2)config = {"configurable": {"thread_id": "1"}}
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-7-3)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-7-4)for chunk in graph.stream(
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-7-5)  {
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-7-6)    "messages": [
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-7-7)      {
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-7-8)        "role": "user",
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-7-9)        "content": "Find numbers between 10 and 30 in fibonacci sequence",
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-7-10)      }
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-7-11)    ]
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-7-12)  },
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-7-13)  config,
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-7-14)):
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-7-15)  print(chunk)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-1)[33muser_proxy[0m (to assistant):
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-2)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-3)Find numbers between 10 and 30 in fibonacci sequence
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-4)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-5)--------------------------------------------------------------------------------
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-6)[33massistant[0m (to user_proxy):
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-7)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-8)To find numbers between 10 and 30 in the Fibonacci sequence, we can generate the Fibonacci sequence and check which numbers fall within this range. Here's a plan:
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-9)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-10)1. Generate Fibonacci numbers starting from 0.
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-11)2. Continue generating until the numbers exceed 30.
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-12)3. Collect and print the numbers that are between 10 and 30.
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-13)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-14)Let's implement this in Python:
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-15)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-16)\`\`\`python
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-17)# filename: fibonacci_range.py
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-18)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-19)def fibonacci_sequence():
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-20)  a, b = 0, 1
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-21)  while a <= 30:
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-22)    if 10 <= a <= 30:
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-23)      print(a)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-24)    a, b = b, a + b
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-25)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-26)fibonacci_sequence()
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-27)\`\`\`
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-28)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-29)This script will print the Fibonacci numbers between 10 and 30. Please execute the code to see the result.
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-30)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-31)--------------------------------------------------------------------------------
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-32)[31m
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-33)>>>>>>>> EXECUTING CODE BLOCK 0 (inferred language is python)...[0m
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-34)[33muser_proxy[0m (to assistant):
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-35)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-36)exitcode: 0 (execution succeeded)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-37)Code output: 
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-38)13
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-39)21
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-40)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-41)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-42)--------------------------------------------------------------------------------
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-43)[33massistant[0m (to user_proxy):
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-44)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-45)The Fibonacci numbers between 10 and 30 are 13 and 21. 
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-46)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-47)These numbers are part of the Fibonacci sequence, which is generated by adding the two preceding numbers to get the next number, starting from 0 and 1. 
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-48)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-49)The sequence goes: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-50)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-51)As you can see, 13 and 21 are the only numbers in this sequence that fall between 10 and 30.
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-52)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-53)TERMINATE
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-54)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-55)--------------------------------------------------------------------------------
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-8-56){'call_autogen_agent': {'messages': {'role': 'assistant', 'content': 'The Fibonacci numbers between 10 and 30 are 13 and 21. \n\nThese numbers are part of the Fibonacci sequence, which is generated by adding the two preceding numbers to get the next number, starting from 0 and 1. \n\nThe sequence goes: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...\n\nAs you can see, 13 and 21 are the only numbers in this sequence that fall between 10 and 30.\n\nTERMINATE'}}}

```


Since we're leveraging LangGraph's [persistence](https://langchain-ai.github.io/langgraph/concepts/persistence/) features we can now continue the conversation using the same thread ID -- LangGraph will automatically pass previous history to the AutoGen agent: 

```
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-9-1)for chunk in graph.stream(
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-9-2)  {
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-9-3)    "messages": [
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-9-4)      {
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-9-5)        "role": "user",
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-9-6)        "content": "Multiply the last number by 3",
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-9-7)      }
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-9-8)    ]
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-9-9)  },
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-9-10)  config,
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-9-11)):
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-9-12)  print(chunk)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-10-1)[33muser_proxy[0m (to assistant):
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-10-2)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-10-3)Multiply the last number by 3
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-10-4)Context: 
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-10-5)Find numbers between 10 and 30 in fibonacci sequence
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-10-6)The Fibonacci numbers between 10 and 30 are 13 and 21. 
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-10-7)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-10-8)These numbers are part of the Fibonacci sequence, which is generated by adding the two preceding numbers to get the next number, starting from 0 and 1. 
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-10-9)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-10-10)The sequence goes: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-10-11)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-10-12)As you can see, 13 and 21 are the only numbers in this sequence that fall between 10 and 30.
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-10-13)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-10-14)TERMINATE
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-10-15)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-10-16)--------------------------------------------------------------------------------
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-10-17)[33massistant[0m (to user_proxy):
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-10-18)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-10-19)The last number in the Fibonacci sequence between 10 and 30 is 21. Multiplying 21 by 3 gives:
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-10-20)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-10-21)21 * 3 = 63
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-10-22)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-10-23)TERMINATE
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-10-24)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-10-25)--------------------------------------------------------------------------------
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__codelineno-10-26){'call_autogen_agent': {'messages': {'role': 'assistant', 'content': 'The last number in the Fibonacci sequence between 10 and 30 is 21. Multiplying 21 by 3 gives:\n\n21 * 3 = 63\n\nTERMINATE'}}}

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to pass custom run ID or set tags and metadata for graph runs in LangSmith  ](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/) [ Next  How to integrate LangGraph (functional API) with AutoGen, CrewAI, and other frameworks  ](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration-functional/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
