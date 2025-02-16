---
url: https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#how-to-update-graph-state-from-tools)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to update graph state from tools 

[ ](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/?q= "Share")

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
          * Tool calling  Tool calling 
            * [ Tool calling  ](https://langchain-ai.github.io/langgraph/how-tos#tool-calling)
            * [ How to call tools using ToolNode  ](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/)
            * [ How to handle tool calling errors  ](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/)
            * [ How to pass runtime values to tools  ](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/)
            * How to update graph state from tools  [ How to update graph state from tools  ](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#setup)
              * [ Define tool  ](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#define-tool)
              * [ Define prompt  ](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#define-prompt)
              * [ Define graph  ](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#define-graph)
              * [ Use it!  ](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#use-it)
            * [ How to pass config to tools  ](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/)
            * [ How to handle large numbers of tools  ](https://langchain-ai.github.io/langgraph/how-tos/many-tools/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#setup)
  * [ Define tool  ](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#define-tool)
  * [ Define prompt  ](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#define-prompt)
  * [ Define graph  ](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#define-graph)
  * [ Use it!  ](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#use-it)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Tool calling  ](https://langchain-ai.github.io/langgraph/how-tos#tool-calling)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/update-state-from-tools.ipynb "Edit this page")

# How to update graph state from tools[¶](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#how-to-update-graph-state-from-tools "Permanent link")

Prerequisites

This guide assumes familiarity with the following:

  * [Command](https://langchain-ai.github.io/langgraph/concepts/low_level/#command)



A common use case is updating graph state from inside a tool. For example, in a customer support application you might want to look up customer account number or ID in the beginning of the conversation. To update the graph state from the tool, you can return `Command(update={"my_custom_key": "foo", "messages": [...]})` from the tool:

```
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-0-1)@tool
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-0-2)deflookup_user_info(tool_call_id: Annotated[str, InjectedToolCallId], config: RunnableConfig):
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-0-3)"""Use this to look up user information to better assist them with their questions."""
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-0-4)  user_info = get_user_info(config)
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-0-5)  return Command(
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-0-6)    update={
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-0-7)      # update the state keys
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-0-8)      "user_info": user_info,
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-0-9)      # update the message history
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-0-10)      "messages": [ToolMessage("Successfully looked up user information", tool_call_id=tool_call_id)]
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-0-11)    }
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-0-12)  )

```


Important

If you want to use tools that return `Command` and update graph state, you can either use prebuilt `create_react_agent`[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent) / `ToolNode`[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.ToolNode) components, or implement your own tool-executing node that collects `Command` objects returned by the tools and returns a list of them, e.g.:

```
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-1-1)defcall_tools(state):
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-1-2)  ...
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-1-3)  commands = [tools_by_name[tool_call["name"]].invoke(tool_call) for tool_call in tool_calls]
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-1-4)  return commands

```


This guide shows how you can do this using LangGraph's prebuilt components (`create_react_agent`[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent) / `ToolNode`[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.ToolNode)).

Note

Support for tools that return `Command`[](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Command) was added in LangGraph `v0.2.59`.

## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#setup "Permanent link")

First, let's install the required packages and set our API keys:

```
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-2-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-2-2)%pip install -U langgraph langchain-openai

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-3-1)importos
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-3-2)importgetpass
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-3-3)
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-3-4)
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-3-5)def_set_if_undefined(var: str):
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-3-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-3-7)    os.environ[var] = getpass.getpass(f"Please provide your {var}")
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-3-8)
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-3-9)
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-3-10)_set_if_undefined("OPENAI_API_KEY")

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-4-1)Please provide your OPENAI_API_KEY ········

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

Let's create a simple ReAct style agent that can look up user information and personalize the response based on the user info.

## Define tool[¶](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#define-tool "Permanent link")

First, let's define the tool that we'll be using to look up user information. We'll use a naive implementation that simply looks user information up using a dictionary:

```
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-5-1)USER_INFO = [
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-5-2)  {"user_id": "1", "name": "Bob Dylan", "location": "New York, NY"},
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-5-3)  {"user_id": "2", "name": "Taylor Swift", "location": "Beverly Hills, CA"},
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-5-4)]
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-5-5)
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-5-6)USER_ID_TO_USER_INFO = {info["user_id"]: info for info in USER_INFO}

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-6-1)fromlanggraph.prebuilt.chat_agent_executorimport AgentState
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-6-2)fromlanggraph.typesimport Command
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-6-3)fromlangchain_core.toolsimport tool
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-6-4)fromlangchain_core.tools.baseimport InjectedToolCallId
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-6-5)fromlangchain_core.messagesimport ToolMessage
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-6-6)fromlangchain_core.runnablesimport RunnableConfig
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-6-7)
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-6-8)fromtyping_extensionsimport Any, Annotated
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-6-9)
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-6-10)
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-6-11)classState(AgentState):
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-6-12)  # updated by the tool
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-6-13)  user_info: dict[str, Any]
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-6-14)
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-6-15)
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-6-16)@tool
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-6-17)deflookup_user_info(
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-6-18)  tool_call_id: Annotated[str, InjectedToolCallId], config: RunnableConfig
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-6-19)):
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-6-20)"""Use this to look up user information to better assist them with their questions."""
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-6-21)  user_id = config.get("configurable", {}).get("user_id")
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-6-22)  if user_id is None:
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-6-23)    raise ValueError("Please provide user ID")
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-6-24)
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-6-25)  if user_id not in USER_ID_TO_USER_INFO:
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-6-26)    raise ValueError(f"User '{user_id}' not found")
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-6-27)
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-6-28)  user_info = USER_ID_TO_USER_INFO[user_id]
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-6-29)  return Command(
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-6-30)    update={
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-6-31)      # update the state keys
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-6-32)      "user_info": user_info,
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-6-33)      # update the message history
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-6-34)      "messages": [
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-6-35)        ToolMessage(
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-6-36)          "Successfully looked up user information", tool_call_id=tool_call_id
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-6-37)        )
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-6-38)      ],
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-6-39)    }
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-6-40)  )

```


API Reference: [tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html) | [InjectedToolCallId](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.InjectedToolCallId.html) | [ToolMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.tool.ToolMessage.html) | [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html) | [Command](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Command)

## Define prompt[¶](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#define-prompt "Permanent link")

Let's now add personalization: we'll respond differently to the user based on the state values AFTER the state has been updated from the tool. To achieve this, let's define a function that will dynamically construct the system prompt based on the graph state. It will be called ever time the LLM is called and the function output will be passed to the LLM:

```
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-7-1)defprompt(state: State):
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-7-2)  user_info = state.get("user_info")
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-7-3)  if user_info is None:
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-7-4)    return state["messages"]
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-7-5)
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-7-6)  system_msg = (
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-7-7)    f"User name is {user_info['name']}. User lives in {user_info['location']}"
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-7-8)  )
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-7-9)  return [{"role": "system", "content": system_msg}] + state["messages"]

```


## Define graph[¶](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#define-graph "Permanent link")

Finally, let's combine this into a single graph using the prebuilt `create_react_agent`:

```
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-8-1)fromlanggraph.prebuiltimport create_react_agent
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-8-2)fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-8-3)
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-8-4)model = ChatOpenAI(model="gpt-4o")
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-8-5)
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-8-6)agent = create_react_agent(
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-8-7)  model,
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-8-8)  # pass the tool that can update state
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-8-9)  [lookup_user_info],
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-8-10)  state_schema=State,
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-8-11)  # pass dynamic prompt function
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-8-12)  prompt=prompt,
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-8-13))

```


API Reference: [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html) | [create_react_agent](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent)

## Use it![¶](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#use-it "Permanent link")

Let's now try running our agent. We'll need to provide user ID in the config so that our tool knows what information to look up:

```
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-9-1)for chunk in agent.stream(
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-9-2)  {"messages": [("user", "hi, what should i do this weekend?")]},
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-9-3)  # provide user ID in the config
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-9-4)  {"configurable": {"user_id": "1"}},
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-9-5)):
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-9-6)  print(chunk)
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-9-7)  print("\n")

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-10-1){'agent': {'messages': [AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_7LSUh6ZDvGJAUvlWvXiCK4Gf', 'function': {'arguments': '{}', 'name': 'lookup_user_info'}, 'type': 'function'}], 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 11, 'prompt_tokens': 56, 'total_tokens': 67, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-4o-2024-08-06', 'system_fingerprint': 'fp_9d50cd990b', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-57eeb216-e35d-4501-aaac-b5c6b26fb17c-0', tool_calls=[{'name': 'lookup_user_info', 'args': {}, 'id': 'call_7LSUh6ZDvGJAUvlWvXiCK4Gf', 'type': 'tool_call'}], usage_metadata={'input_tokens': 56, 'output_tokens': 11, 'total_tokens': 67, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}})]}}
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-10-2)
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-10-3)
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-10-4){'tools': {'user_info': {'user_id': '1', 'name': 'Bob Dylan', 'location': 'New York, NY'}, 'messages': [ToolMessage(content='Successfully looked up user information', name='lookup_user_info', id='168d8ff8-b021-4c8b-a11a-3b50c30a072c', tool_call_id='call_7LSUh6ZDvGJAUvlWvXiCK4Gf')]}}
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-10-5)
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-10-6)
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-10-7){'agent': {'messages': [AIMessage(content="Hi Bob! Since you're in New York, NY, there are plenty of exciting things to do over the weekend. Here are some suggestions:\n\n1. **Explore Central Park**: Take a leisurely walk, rent a bike, or have a picnic in this iconic park.\n\n2. **Visit a Museum**: Check out The Metropolitan Museum of Art or the Museum of Modern Art (MoMA) for an enriching cultural experience.\n\n3. **Broadway Show**: Catch a Broadway show or an off-Broadway performance for some world-class entertainment.\n\n4. **Food Tour**: Explore different neighborhoods like Greenwich Village or Williamsburg for diverse culinary experiences.\n\n5. **Brooklyn Bridge Walk**: Take a walk across the Brooklyn Bridge for stunning views of the city skyline.\n\n6. **Visit a Rooftop Bar**: Enjoy a drink with a view at one of New York’s many rooftop bars.\n\n7. **Explore a New Neighborhood**: Discover the unique charm of areas like SoHo, Chelsea, or Astoria.\n\n8. **Live Music**: Check out live music venues for a night of great performances.\n\n9. **Art Galleries**: Visit some of the smaller art galleries around Chelsea or the Lower East Side.\n\n10. **Attend a Local Event**: Look up any local events or festivals happening this weekend.\n\nFeel free to let me know if you want more details on any of these activities!", additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 285, 'prompt_tokens': 95, 'total_tokens': 380, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-4o-2024-08-06', 'system_fingerprint': 'fp_9d50cd990b', 'finish_reason': 'stop', 'logprobs': None}, id='run-f13ce15b-02b6-40e6-8264-c4d9edd0d03a-0', usage_metadata={'input_tokens': 95, 'output_tokens': 285, 'total_tokens': 380, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}})]}}

```


We can see that the model correctly recommended some New York activities for Bob Dylan! Let's try getting recommendations for Taylor Swift: 

```
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-11-1)for chunk in agent.stream(
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-11-2)  {"messages": [("user", "hi, what should i do this weekend?")]},
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-11-3)  {"configurable": {"user_id": "2"}},
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-11-4)):
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-11-5)  print(chunk)
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-11-6)  print("\n")

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-12-1){'agent': {'messages': [AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_5HLtJtzcgmKbtmK6By21wW5Y', 'function': {'arguments': '{}', 'name': 'lookup_user_info'}, 'type': 'function'}], 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 11, 'prompt_tokens': 56, 'total_tokens': 67, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-4o-2024-08-06', 'system_fingerprint': 'fp_c7ca0ebaca', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-bacacd7d-76cc-4f6b-9e9b-d9e6f00b9391-0', tool_calls=[{'name': 'lookup_user_info', 'args': {}, 'id': 'call_5HLtJtzcgmKbtmK6By21wW5Y', 'type': 'tool_call'}], usage_metadata={'input_tokens': 56, 'output_tokens': 11, 'total_tokens': 67, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}})]}}
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-12-2)
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-12-3)
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-12-4){'tools': {'user_info': {'user_id': '2', 'name': 'Taylor Swift', 'location': 'Beverly Hills, CA'}, 'messages': [ToolMessage(content='Successfully looked up user information', name='lookup_user_info', id='d81ef31e-6d77-4f13-ae86-e2e6ba567e3d', tool_call_id='call_5HLtJtzcgmKbtmK6By21wW5Y')]}}
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-12-5)
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-12-6)
[](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__codelineno-12-7){'agent': {'messages': [AIMessage(content="Hi Taylor! Since you're in Beverly Hills, here are a few suggestions for a fun weekend:\n\n1. **Hiking at Runyon Canyon**: Enjoy a scenic hike with beautiful views of Los Angeles. It's a great way to get some exercise and enjoy the outdoors.\n\n2. **Visit Rodeo Drive**: Spend some time shopping or window shopping at the famous Rodeo Drive. You might even spot some celebrities!\n\n3. **Explore the Getty Center**: Check out the art collections and beautiful gardens at the Getty Center. The architecture and views are stunning.\n\n4. **Relax at a Spa**: Treat yourself to a relaxing day at one of Beverly Hills' luxurious spas.\n\n5. **Dining Out**: Try a new restaurant or visit your favorite spot for a delicious meal. Beverly Hills has a fantastic dining scene.\n\n6. **Attend a Local Event**: Check out any local events or concerts happening this weekend. Beverly Hills often hosts exciting events.\n\nEnjoy your weekend!", additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 198, 'prompt_tokens': 95, 'total_tokens': 293, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-4o-2024-08-06', 'system_fingerprint': 'fp_c7ca0ebaca', 'finish_reason': 'stop', 'logprobs': None}, id='run-2057df76-f192-4c69-a66a-1f0a86bf5d66-0', usage_metadata={'input_tokens': 95, 'output_tokens': 198, 'total_tokens': 293, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}})]}}

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to pass runtime values to tools  ](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/) [ Next  How to pass config to tools  ](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
