---
url: https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#how-to-create-a-react-agent-from-scratch)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to create a ReAct agent from scratch 

[ ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/?q= "Share")

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
          * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraph/how-tos#human-in-the-loop)
          * [ Streaming  ](https://langchain-ai.github.io/langgraph/how-tos#streaming)
          * [ Tool calling  ](https://langchain-ai.github.io/langgraph/how-tos#tool-calling)
          * [ Subgraphs  ](https://langchain-ai.github.io/langgraph/how-tos#subgraphs)
          * [ Multi-agent  ](https://langchain-ai.github.io/langgraph/how-tos#multi-agent)
          * [ State Management  ](https://langchain-ai.github.io/langgraph/how-tos#state-management)
          * [ Other  ](https://langchain-ai.github.io/langgraph/how-tos#other)
          * Prebuilt ReAct Agent  Prebuilt ReAct Agent 
            * [ Prebuilt ReAct Agent  ](https://langchain-ai.github.io/langgraph/how-tos#prebuilt-react-agent)
            * [ How to use the pre-built ReAct agent  ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/)
            * [ How to add thread-level memory to a ReAct Agent  ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/)
            * [ How to add a custom system prompt to the prebuilt ReAct agent  ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-system-prompt/)
            * [ How to add human-in-the-loop processes to the prebuilt ReAct agent  ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/)
            * [ How to return structured output from the prebuilt ReAct agent  ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/)
            * How to create a ReAct agent from scratch  [ How to create a ReAct agent from scratch  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#setup)
              * [ Create ReAct agent  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#create-react-agent)
                * [ Define graph state  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#define-graph-state)
                * [ Define model and tools  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#define-model-and-tools)
                * [ Define nodes and edges  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#define-nodes-and-edges)
                * [ Define the graph  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#define-the-graph)
              * [ Use ReAct agent  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#use-react-agent)
            * [ How to create a ReAct agent from scratch (Functional API)  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#setup)
  * [ Create ReAct agent  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#create-react-agent)
    * [ Define graph state  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#define-graph-state)
    * [ Define model and tools  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#define-model-and-tools)
    * [ Define nodes and edges  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#define-nodes-and-edges)
    * [ Define the graph  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#define-the-graph)
  * [ Use ReAct agent  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#use-react-agent)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Prebuilt ReAct Agent  ](https://langchain-ai.github.io/langgraph/how-tos#prebuilt-react-agent)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/react-agent-from-scratch.ipynb "Edit this page")

# How to create a ReAct agent from scratch[¶](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#how-to-create-a-react-agent-from-scratch "Permanent link")

Prerequisites

This guide assumes familiarity with the following:

  * [Tool calling agent](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#tool-calling-agent)
  * [Chat Models](https://python.langchain.com/docs/concepts/chat_models/)
  * [Messages](https://python.langchain.com/docs/concepts/messages/)
  * [LangGraph Glossary](https://langchain-ai.github.io/langgraph/concepts/low_level/)



Using the prebuilt ReAct agent [create_react_agent](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent) is a great way to get started, but sometimes you might want more control and customization. In those cases, you can create a custom ReAct agent. This guide shows how to implement ReAct agent from scratch using LangGraph.

## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#setup "Permanent link")

First, let's install the required packages and set our API keys:

```
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-0-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-0-2)%pip install -U langgraph langchain-openai

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-1-1)importgetpass
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-1-2)importos
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-1-5)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-1-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-1-7)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-1-8)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-1-10)_set_env("OPENAI_API_KEY")

```


Set up [LangSmith](https://smith.langchain.com) for better debugging

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM aps built with LangGraph — read more about how to get started in the [docs](https://docs.smith.langchain.com). 

## Create ReAct agent[¶](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#create-react-agent "Permanent link")

Now that you have installed the required packages and set your environment variables, we can code our ReAct agent!

### Define graph state[¶](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#define-graph-state "Permanent link")

We are going to define the most basic ReAct state in this example, which will just contain a list of messages.

For your specific use case, feel free to add any other state keys that you need.

```
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-2-1)fromtypingimport (
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-2-2)  Annotated,
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-2-3)  Sequence,
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-2-4)  TypedDict,
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-2-5))
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-2-6)fromlangchain_core.messagesimport BaseMessage
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-2-7)fromlanggraph.graph.messageimport add_messages
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-2-8)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-2-9)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-2-10)classAgentState(TypedDict):
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-2-11)"""The state of the agent."""
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-2-12)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-2-13)  # add_messages is a reducer
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-2-14)  # See https://langchain-ai.github.io/langgraph/concepts/low_level/#reducers
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-2-15)  messages: Annotated[Sequence[BaseMessage], add_messages]

```


API Reference: [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html) | [add_messages](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.message.add_messages)

### Define model and tools[¶](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#define-model-and-tools "Permanent link")

Next, let's define the tools and model we will use for our example.

```
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-3-1)fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-3-2)fromlangchain_core.toolsimport tool
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-3-3)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-3-4)model = ChatOpenAI(model="gpt-4o-mini")
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-3-5)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-3-6)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-3-7)@tool
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-3-8)defget_weather(location: str):
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-3-9)"""Call to get the weather from a specific location."""
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-3-10)  # This is a placeholder for the actual implementation
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-3-11)  # Don't let the LLM know this though 😊
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-3-12)  if any([city in location.lower() for city in ["sf", "san francisco"]]):
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-3-13)    return "It's sunny in San Francisco, but you better look out if you're a Gemini 😈."
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-3-14)  else:
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-3-15)    return f"I am not sure what the weather is in {location}"
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-3-16)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-3-17)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-3-18)tools = [get_weather]
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-3-19)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-3-20)model = model.bind_tools(tools)

```


API Reference: [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html) | [tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html)

### Define nodes and edges[¶](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#define-nodes-and-edges "Permanent link")

Next let's define our nodes and edges. In our basic ReAct agent there are only two nodes, one for calling the model and one for using tools, however you can modify this basic structure to work better for your use case. The tool node we define here is a simplified version of the prebuilt `ToolNode`[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/), which has some additional features.

Perhaps you want to add a node for [adding structured output](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/) or a node for executing some external action (sending an email, adding a calendar event, etc.). Maybe you just want to change the way the `call_model` node works and how `should_continue` decides whether to call tools - the possibilities are endless and LangGraph makes it easy to customize this basic structure for your specific use case.

```
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-4-1)importjson
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-4-2)fromlangchain_core.messagesimport ToolMessage, SystemMessage
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-4-3)fromlangchain_core.runnablesimport RunnableConfig
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-4-4)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-4-5)tools_by_name = {tool.name: tool for tool in tools}
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-4-6)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-4-7)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-4-8)# Define our tool node
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-4-9)deftool_node(state: AgentState):
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-4-10)  outputs = []
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-4-11)  for tool_call in state["messages"][-1].tool_calls:
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-4-12)    tool_result = tools_by_name[tool_call["name"]].invoke(tool_call["args"])
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-4-13)    outputs.append(
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-4-14)      ToolMessage(
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-4-15)        content=json.dumps(tool_result),
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-4-16)        name=tool_call["name"],
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-4-17)        tool_call_id=tool_call["id"],
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-4-18)      )
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-4-19)    )
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-4-20)  return {"messages": outputs}
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-4-21)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-4-22)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-4-23)# Define the node that calls the model
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-4-24)defcall_model(
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-4-25)  state: AgentState,
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-4-26)  config: RunnableConfig,
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-4-27)):
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-4-28)  # this is similar to customizing the create_react_agent with 'prompt' parameter, but is more flexible
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-4-29)  system_prompt = SystemMessage(
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-4-30)    "You are a helpful AI assistant, please respond to the users query to the best of your ability!"
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-4-31)  )
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-4-32)  response = model.invoke([system_prompt] + state["messages"], config)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-4-33)  # We return a list, because this will get added to the existing list
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-4-34)  return {"messages": [response]}
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-4-35)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-4-36)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-4-37)# Define the conditional edge that determines whether to continue or not
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-4-38)defshould_continue(state: AgentState):
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-4-39)  messages = state["messages"]
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-4-40)  last_message = messages[-1]
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-4-41)  # If there is no function call, then we finish
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-4-42)  if not last_message.tool_calls:
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-4-43)    return "end"
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-4-44)  # Otherwise if there is, we continue
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-4-45)  else:
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-4-46)    return "continue"

```


API Reference: [ToolMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.tool.ToolMessage.html) | [SystemMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.system.SystemMessage.html) | [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html)

### Define the graph[¶](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#define-the-graph "Permanent link")

Now that we have defined all of our nodes and edges, we can define and compile our graph. Depending on if you have added more nodes or different edges, you will need to edit this to fit your specific use case.

```
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-5-1)fromlanggraph.graphimport StateGraph, END
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-5-2)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-5-3)# Define a new graph
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-5-4)workflow = StateGraph(AgentState)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-5-5)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-5-6)# Define the two nodes we will cycle between
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-5-7)workflow.add_node("agent", call_model)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-5-8)workflow.add_node("tools", tool_node)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-5-9)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-5-10)# Set the entrypoint as `agent`
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-5-11)# This means that this node is the first one called
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-5-12)workflow.set_entry_point("agent")
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-5-13)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-5-14)# We now add a conditional edge
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-5-15)workflow.add_conditional_edges(
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-5-16)  # First, we define the start node. We use `agent`.
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-5-17)  # This means these are the edges taken after the `agent` node is called.
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-5-18)  "agent",
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-5-19)  # Next, we pass in the function that will determine which node is called next.
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-5-20)  should_continue,
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-5-21)  # Finally we pass in a mapping.
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-5-22)  # The keys are strings, and the values are other nodes.
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-5-23)  # END is a special node marking that the graph should finish.
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-5-24)  # What will happen is we will call `should_continue`, and then the output of that
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-5-25)  # will be matched against the keys in this mapping.
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-5-26)  # Based on which one it matches, that node will then be called.
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-5-27)  {
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-5-28)    # If `tools`, then we call the tool node.
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-5-29)    "continue": "tools",
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-5-30)    # Otherwise we finish.
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-5-31)    "end": END,
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-5-32)  },
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-5-33))
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-5-34)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-5-35)# We now add a normal edge from `tools` to `agent`.
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-5-36)# This means that after `tools` is called, `agent` node is called next.
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-5-37)workflow.add_edge("tools", "agent")
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-5-38)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-5-39)# Now we can compile and visualize our graph
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-5-40)graph = workflow.compile()
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-5-41)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-5-42)fromIPython.displayimport Image, display
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-5-43)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-5-44)try:
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-5-45)  display(Image(graph.get_graph().draw_mermaid_png()))
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-5-46)except Exception:
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-5-47)  # This requires some extra dependencies and is optional
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-5-48)  pass

```


API Reference: [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END)

![]()

## Use ReAct agent[¶](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#use-react-agent "Permanent link")

Now that we have created our react agent, let's actually put it to the test!

```
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-6-1)# Helper function for formatting the stream nicely
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-6-2)defprint_stream(stream):
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-6-3)  for s in stream:
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-6-4)    message = s["messages"][-1]
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-6-5)    if isinstance(message, tuple):
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-6-6)      print(message)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-6-7)    else:
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-6-8)      message.pretty_print()
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-6-9)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-6-10)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-6-11)inputs = {"messages": [("user", "what is the weather in sf")]}
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-6-12)print_stream(graph.stream(inputs, stream_mode="values"))

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-7-1)================================[1m Human Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-7-2)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-7-3)what is the weather in sf
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-7-4)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-7-5)Tool Calls:
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-7-6) get_weather (call_azW0cQ4XjWWj0IAkWAxq9nLB)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-7-7) Call ID: call_azW0cQ4XjWWj0IAkWAxq9nLB
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-7-8) Args:
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-7-9)  location: San Francisco
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-7-10)=================================[1m Tool Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-7-11)Name: get_weather
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-7-12)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-7-13)"It's sunny in San Francisco, but you better look out if you're a Gemini \ud83d\ude08."
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-7-14)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-7-15)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__codelineno-7-16)The weather in San Francisco is sunny! However, it seems there's a playful warning for Geminis. Enjoy the sunshine!

```


Perfect! The graph correctly calls the `get_weather` tool and responds to the user after receiving the information from the tool.  Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to return structured output from the prebuilt ReAct agent  ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/) [ Next  How to create a ReAct agent from scratch (Functional API)  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
