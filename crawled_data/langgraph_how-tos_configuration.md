---
url: https://langchain-ai.github.io/langgraph/how-tos/configuration/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/configuration/#how-to-add-runtime-configuration-to-your-graph)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to add runtime configuration to your graph 

[ ](https://langchain-ai.github.io/langgraph/how-tos/configuration/?q= "Share")

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
          * Controllability  Controllability 
            * [ Controllability  ](https://langchain-ai.github.io/langgraph/how-tos#controllability)
            * [ How to create map-reduce branches for parallel execution  ](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/)
            * [ How to combine control flow and state updates with Command  ](https://langchain-ai.github.io/langgraph/how-tos/command/)
            * How to add runtime configuration to your graph  [ How to add runtime configuration to your graph  ](https://langchain-ai.github.io/langgraph/how-tos/configuration/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/configuration/#setup)
              * [ Define graph  ](https://langchain-ai.github.io/langgraph/how-tos/configuration/#define-graph)
              * [ Configure the graph  ](https://langchain-ai.github.io/langgraph/how-tos/configuration/#configure-the-graph)
            * [ How to add node retry policies  ](https://langchain-ai.github.io/langgraph/how-tos/node-retries/)
            * [ How to return state before hitting recursion limit  ](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/)
          * [ Persistence  ](https://langchain-ai.github.io/langgraph/how-tos#persistence)
          * [ Memory  ](https://langchain-ai.github.io/langgraph/how-tos#memory)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/configuration/#setup)
  * [ Define graph  ](https://langchain-ai.github.io/langgraph/how-tos/configuration/#define-graph)
  * [ Configure the graph  ](https://langchain-ai.github.io/langgraph/how-tos/configuration/#configure-the-graph)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Controllability  ](https://langchain-ai.github.io/langgraph/how-tos#controllability)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/configuration.ipynb "Edit this page")

# How to add runtime configuration to your graph[¶](https://langchain-ai.github.io/langgraph/how-tos/configuration/#how-to-add-runtime-configuration-to-your-graph "Permanent link")

Sometimes you want to be able to configure your agent when calling it. Examples of this include configuring which LLM to use. Below we walk through an example of doing so.

Prerequisites

This guide assumes familiarity with the following: 

  * [ LangGraph State ](https://langchain-ai.github.io/langgraph/concepts/low_level/#state)
  * [ Chat Models ](https://python.langchain.com/docs/concepts/#chat-models/)



## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/configuration/#setup "Permanent link")

First, let's install the required packages and set our API keys

```
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-0-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-0-2)%pip install -U langgraph langchain_anthropic

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-1-1)importgetpass
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-1-2)importos
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-1-5)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-1-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-1-7)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-1-8)
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-1-10)_set_env("ANTHROPIC_API_KEY")

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Define graph[¶](https://langchain-ai.github.io/langgraph/how-tos/configuration/#define-graph "Permanent link")

First, let's create a very simple graph

```
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-2-1)importoperator
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-2-2)fromtypingimport Annotated, Sequence
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-2-3)fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-2-4)
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-2-5)fromlangchain_anthropicimport ChatAnthropic
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-2-6)fromlangchain_core.messagesimport BaseMessage, HumanMessage
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-2-7)
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-2-8)fromlanggraph.graphimport END, StateGraph, START
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-2-9)
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-2-10)model = ChatAnthropic(model_name="claude-2.1")
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-2-11)
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-2-12)
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-2-13)classAgentState(TypedDict):
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-2-14)  messages: Annotated[Sequence[BaseMessage], operator.add]
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-2-15)
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-2-16)
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-2-17)def_call_model(state):
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-2-18)  state["messages"]
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-2-19)  response = model.invoke(state["messages"])
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-2-20)  return {"messages": [response]}
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-2-21)
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-2-22)
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-2-23)# Define a new graph
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-2-24)builder = StateGraph(AgentState)
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-2-25)builder.add_node("model", _call_model)
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-2-26)builder.add_edge(START, "model")
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-2-27)builder.add_edge("model", END)
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-2-28)
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-2-29)graph = builder.compile()

```


API Reference: [ChatAnthropic](https://python.langchain.com/api_reference/anthropic/chat_models/langchain_anthropic.chat_models.ChatAnthropic.html) | [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html) | [HumanMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.human.HumanMessage.html) | [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START)

## Configure the graph[¶](https://langchain-ai.github.io/langgraph/how-tos/configuration/#configure-the-graph "Permanent link")

Great! Now let's suppose that we want to extend this example so the user is able to choose from multiple llms. We can easily do that by passing in a config. Any configuration information needs to be passed inside `configurable` key as shown below. This config is meant to contain things are not part of the input (and therefore that we don't want to track as part of the state).

```
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-3-1)fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-3-2)fromtypingimport Optional
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-3-3)fromlangchain_core.runnables.configimport RunnableConfig
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-3-4)
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-3-5)openai_model = ChatOpenAI()
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-3-6)
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-3-7)models = {
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-3-8)  "anthropic": model,
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-3-9)  "openai": openai_model,
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-3-10)}
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-3-11)
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-3-12)
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-3-13)def_call_model(state: AgentState, config: RunnableConfig):
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-3-14)  # Access the config through the configurable key
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-3-15)  model_name = config["configurable"].get("model", "anthropic")
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-3-16)  model = models[model_name]
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-3-17)  response = model.invoke(state["messages"])
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-3-18)  return {"messages": [response]}
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-3-19)
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-3-20)
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-3-21)# Define a new graph
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-3-22)builder = StateGraph(AgentState)
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-3-23)builder.add_node("model", _call_model)
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-3-24)builder.add_edge(START, "model")
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-3-25)builder.add_edge("model", END)
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-3-26)
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-3-27)graph = builder.compile()

```


API Reference: [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html) | [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html)

If we call it with no configuration, it will use the default as we defined it (Anthropic).

```
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-4-1)graph.invoke({"messages": [HumanMessage(content="hi")]})

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-5-1){'messages': [HumanMessage(content='hi', additional_kwargs={}, response_metadata={}),
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-5-2) AIMessage(content='Hello!', additional_kwargs={}, response_metadata={'id': 'msg_01WFXkfgK8AvSckLvYYrHshi', 'model': 'claude-2.1', 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 10, 'output_tokens': 6}}, id='run-ece54b16-f8fc-4201-8405-b97122edf8d8-0', usage_metadata={'input_tokens': 10, 'output_tokens': 6, 'total_tokens': 16})]}

```


We can also call it with a config to get it to use a different model.

```
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-6-1)config = {"configurable": {"model": "openai"}}
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-6-2)graph.invoke({"messages": [HumanMessage(content="hi")]}, config=config)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-7-1){'messages': [HumanMessage(content='hi', additional_kwargs={}, response_metadata={}),
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-7-2) AIMessage(content='Hello! How can I assist you today?', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 9, 'prompt_tokens': 8, 'total_tokens': 17, 'completion_tokens_details': {'reasoning_tokens': 0}}, 'model_name': 'gpt-3.5-turbo-0125', 'system_fingerprint': None, 'finish_reason': 'stop', 'logprobs': None}, id='run-f8331964-d811-4b44-afb8-56c30ade7c15-0', usage_metadata={'input_tokens': 8, 'output_tokens': 9, 'total_tokens': 17})]}

```


We can also adapt our graph to take in more configuration! Like a system message for example.

```
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-8-1)fromlangchain_core.messagesimport SystemMessage
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-8-2)
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-8-3)
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-8-4)# We can define a config schema to specify the configuration options for the graph
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-8-5)# A config schema is useful for indicating which fields are available in the configurable dict inside the config
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-8-6)classConfigSchema(TypedDict):
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-8-7)  model: Optional[str]
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-8-8)  system_message: Optional[str]
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-8-9)
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-8-10)
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-8-11)def_call_model(state: AgentState, config: RunnableConfig):
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-8-12)  # Access the config through the configurable key
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-8-13)  model_name = config["configurable"].get("model", "anthropic")
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-8-14)  model = models[model_name]
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-8-15)  messages = state["messages"]
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-8-16)  if "system_message" in config["configurable"]:
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-8-17)    messages = [
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-8-18)      SystemMessage(content=config["configurable"]["system_message"])
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-8-19)    ] + messages
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-8-20)  response = model.invoke(messages)
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-8-21)  return {"messages": [response]}
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-8-22)
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-8-23)
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-8-24)# Define a new graph - note that we pass in the configuration schema here, but it is not necessary
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-8-25)workflow = StateGraph(AgentState, ConfigSchema)
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-8-26)workflow.add_node("model", _call_model)
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-8-27)workflow.add_edge(START, "model")
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-8-28)workflow.add_edge("model", END)
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-8-29)
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-8-30)graph = workflow.compile()

```


API Reference: [SystemMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.system.SystemMessage.html)

```
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-9-1)graph.invoke({"messages": [HumanMessage(content="hi")]})

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-10-1){'messages': [HumanMessage(content='hi', additional_kwargs={}, response_metadata={}),
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-10-2) AIMessage(content='Hello!', additional_kwargs={}, response_metadata={'id': 'msg_01VgCANVHr14PsHJSXyKkLVh', 'model': 'claude-2.1', 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 10, 'output_tokens': 6}}, id='run-f8c5f18c-be58-4e44-9a4e-d43692d7eed1-0', usage_metadata={'input_tokens': 10, 'output_tokens': 6, 'total_tokens': 16})]}

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-11-1)config = {"configurable": {"system_message": "respond in italian"}}
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-11-2)graph.invoke({"messages": [HumanMessage(content="hi")]}, config=config)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-12-1){'messages': [HumanMessage(content='hi', additional_kwargs={}, response_metadata={}),
[](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__codelineno-12-2) AIMessage(content='Ciao!', additional_kwargs={}, response_metadata={'id': 'msg_011YuCYQk1Rzc8PEhVCpQGr6', 'model': 'claude-2.1', 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 14, 'output_tokens': 7}}, id='run-a583341e-5868-4e8c-a536-881338f21252-0', usage_metadata={'input_tokens': 14, 'output_tokens': 7, 'total_tokens': 21})]}

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to combine control flow and state updates with Command  ](https://langchain-ai.github.io/langgraph/how-tos/command/) [ Next  How to add node retry policies  ](https://langchain-ai.github.io/langgraph/how-tos/node-retries/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/configuration/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
