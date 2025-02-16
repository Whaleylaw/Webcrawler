---
url: https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#how-to-review-tool-calls-functional-api)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to review tool calls (Functional API) 

[ ](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/?q= "Share")

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
            * [ How to view and update past graph state  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/)
            * [ How to Review Tool Calls  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/)
            * [ How to wait for user input (Functional API)  ](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/)
            * How to review tool calls (Functional API)  [ How to review tool calls (Functional API)  ](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#setup)
              * [ Define model and tools  ](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#define-model-and-tools)
              * [ Define tasks  ](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#define-tasks)
              * [ Define entrypoint  ](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#define-entrypoint)
                * [ Usage  ](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#usage)
                * [ Accept a tool call  ](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#accept-a-tool-call)
                * [ Revise a tool call  ](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#revise-a-tool-call)
                * [ Generate a custom ToolMessage  ](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#generate-a-custom-toolmessage)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#setup)
  * [ Define model and tools  ](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#define-model-and-tools)
  * [ Define tasks  ](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#define-tasks)
  * [ Define entrypoint  ](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#define-entrypoint)
    * [ Usage  ](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#usage)
    * [ Accept a tool call  ](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#accept-a-tool-call)
    * [ Revise a tool call  ](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#revise-a-tool-call)
    * [ Generate a custom ToolMessage  ](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#generate-a-custom-toolmessage)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraph/how-tos#human-in-the-loop)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/review-tool-calls-functional.ipynb "Edit this page")

# How to review tool calls (Functional API)[¶](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#how-to-review-tool-calls-functional-api "Permanent link")

Prerequisites

This guide assumes familiarity with the following:

  * Implementing [human-in-the-loop](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop) workflows with [interrupt](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#interrupt)
  * [How to create a ReAct agent using the Functional API](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional)



This guide demonstrates how to implement human-in-the-loop workflows in a ReAct agent using the LangGraph [Functional API](https://langchain-ai.github.io/langgraph/concepts/functional_api).

We will build off of the agent created in the [How to create a ReAct agent using the Functional API](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional) guide.

Specifically, we will demonstrate how to review [tool calls](https://python.langchain.com/docs/concepts/tool_calling/) generated by a [chat model](https://python.langchain.com/docs/concepts/chat_models/) prior to their execution. This can be accomplished through use of the [interrupt](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#interrupt) function at key points in our application.

**Preview** :

We will implement a simple function that reviews tool calls generated from our chat model and call it from inside our application's [entrypoint](https://langchain-ai.github.io/langgraph/concepts/functional_api/#entrypoint):

```
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-0-1)defreview_tool_call(tool_call: ToolCall) -> Union[ToolCall, ToolMessage]:
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-0-2)"""Review a tool call, returning a validated version."""
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-0-3)  human_review = interrupt(
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-0-4)    {
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-0-5)      "question": "Is this correct?",
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-0-6)      "tool_call": tool_call,
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-0-7)    }
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-0-8)  )
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-0-9)  review_action = human_review["action"]
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-0-10)  review_data = human_review.get("data")
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-0-11)  if review_action == "continue":
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-0-12)    return tool_call
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-0-13)  elif review_action == "update":
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-0-14)    updated_tool_call = {**tool_call, **{"args": review_data}}
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-0-15)    return updated_tool_call
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-0-16)  elif review_action == "feedback":
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-0-17)    return ToolMessage(
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-0-18)      content=review_data, name=tool_call["name"], tool_call_id=tool_call["id"]
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-0-19)    )

```


## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#setup "Permanent link")

First, let's install the required packages and set our API keys:

```
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-1-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-1-2)%pip install -U langgraph langchain-openai

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-2-1)importgetpass
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-2-2)importos
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-2-3)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-2-4)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-2-5)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-2-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-2-7)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-2-8)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-2-9)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-2-10)_set_env("OPENAI_API_KEY")

```


Set up [LangSmith](https://smith.langchain.com) for better debugging

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM aps built with LangGraph — read more about how to get started in the [docs](https://docs.smith.langchain.com). 

## Define model and tools[¶](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#define-model-and-tools "Permanent link")

Let's first define the tools and model we will use for our example. As in the [ReAct agent guide](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional), we will use a single place-holder tool that gets a description of the weather for a location.

We will use an [OpenAI](https://python.langchain.com/docs/integrations/providers/openai/) chat model for this example, but any model [supporting tool-calling](https://python.langchain.com/docs/integrations/chat/) will suffice.

```
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-3-1)fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-3-2)fromlangchain_core.toolsimport tool
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-3-3)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-3-4)model = ChatOpenAI(model="gpt-4o-mini")
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-3-5)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-3-6)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-3-7)@tool
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-3-8)defget_weather(location: str):
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-3-9)"""Call to get the weather from a specific location."""
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-3-10)  # This is a placeholder for the actual implementation
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-3-11)  if any([city in location.lower() for city in ["sf", "san francisco"]]):
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-3-12)    return "It's sunny!"
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-3-13)  elif "boston" in location.lower():
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-3-14)    return "It's rainy!"
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-3-15)  else:
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-3-16)    return f"I am not sure what the weather is in {location}"
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-3-17)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-3-18)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-3-19)tools = [get_weather]

```


API Reference: [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html) | [tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html)

## Define tasks[¶](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#define-tasks "Permanent link")

Our [tasks](https://langchain-ai.github.io/langgraph/concepts/functional_api/#task) are unchanged from the [ReAct agent guide](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional):

  1. **Call model** : We want to query our chat model with a list of messages.
  2. **Call tool** : If our model generates tool calls, we want to execute them.



```
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-4-1)fromlangchain_core.messagesimport ToolCall, ToolMessage
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-4-2)fromlanggraph.funcimport entrypoint, task
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-4-3)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-4-4)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-4-5)tools_by_name = {tool.name: tool for tool in tools}
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-4-6)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-4-7)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-4-8)@task
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-4-9)defcall_model(messages):
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-4-10)"""Call model with a sequence of messages."""
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-4-11)  response = model.bind_tools(tools).invoke(messages)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-4-12)  return response
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-4-13)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-4-14)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-4-15)@task
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-4-16)defcall_tool(tool_call):
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-4-17)  tool = tools_by_name[tool_call["name"]]
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-4-18)  observation = tool.invoke(tool_call["args"])
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-4-19)  return ToolMessage(content=observation, tool_call_id=tool_call["id"])

```


API Reference: [ToolCall](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.tool.ToolCall.html) | [ToolMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.tool.ToolMessage.html) | [entrypoint](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint) | [task](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.task)

## Define entrypoint[¶](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#define-entrypoint "Permanent link")

To review tool calls before execution, we add a `review_tool_call` function that calls [interrupt](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#interrupt). When this function is called, execution will be paused until we issue a command to resume it.

Given a tool call, our function will `interrupt` for human review. At that point we can either:

  * Accept the tool call;
  * Revise the tool call and continue;
  * Generate a custom tool message (e.g., instructing the model to re-format its tool call).



We will demonstrate these three cases in the [usage examples](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#usage) below.

```
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-5-1)fromtypingimport Union
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-5-2)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-5-3)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-5-4)defreview_tool_call(tool_call: ToolCall) -> Union[ToolCall, ToolMessage]:
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-5-5)"""Review a tool call, returning a validated version."""
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-5-6)  human_review = interrupt(
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-5-7)    {
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-5-8)      "question": "Is this correct?",
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-5-9)      "tool_call": tool_call,
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-5-10)    }
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-5-11)  )
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-5-12)  review_action = human_review["action"]
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-5-13)  review_data = human_review.get("data")
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-5-14)  if review_action == "continue":
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-5-15)    return tool_call
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-5-16)  elif review_action == "update":
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-5-17)    updated_tool_call = {**tool_call, **{"args": review_data}}
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-5-18)    return updated_tool_call
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-5-19)  elif review_action == "feedback":
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-5-20)    return ToolMessage(
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-5-21)      content=review_data, name=tool_call["name"], tool_call_id=tool_call["id"]
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-5-22)    )

```


We can now update our [entrypoint](https://langchain-ai.github.io/langgraph/concepts/functional_api/#entrypoint) to review the generated tool calls. If a tool call is accepted or revised, we execute in the same way as before. Otherwise, we just append the `ToolMessage` supplied by the human.

Tip

The results of prior tasks — in this case the initial model call — are persisted, so that they are not run again following the `interrupt`.

```
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-6-1)fromlanggraph.checkpoint.memoryimport MemorySaver
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-6-2)fromlanggraph.graph.messageimport add_messages
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-6-3)fromlanggraph.typesimport Command, interrupt
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-6-4)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-6-5)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-6-6)checkpointer = MemorySaver()
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-6-7)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-6-8)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-6-9)@entrypoint(checkpointer=checkpointer)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-6-10)defagent(messages, previous):
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-6-11)  if previous is not None:
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-6-12)    messages = add_messages(previous, messages)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-6-13)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-6-14)  llm_response = call_model(messages).result()
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-6-15)  while True:
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-6-16)    if not llm_response.tool_calls:
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-6-17)      break
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-6-18)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-6-19)    # Review tool calls
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-6-20)    tool_results = []
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-6-21)    tool_calls = []
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-6-22)    for i, tool_call in enumerate(llm_response.tool_calls):
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-6-23)      review = review_tool_call(tool_call)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-6-24)      if isinstance(review, ToolMessage):
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-6-25)        tool_results.append(review)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-6-26)      else: # is a validated tool call
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-6-27)        tool_calls.append(review)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-6-28)        if review != tool_call:
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-6-29)          llm_response.tool_calls[i] = review # update message
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-6-30)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-6-31)    # Execute remaining tool calls
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-6-32)    tool_result_futures = [call_tool(tool_call) for tool_call in tool_calls]
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-6-33)    remaining_tool_results = [fut.result() for fut in tool_result_futures]
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-6-34)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-6-35)    # Append to message list
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-6-36)    messages = add_messages(
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-6-37)      messages,
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-6-38)      [llm_response, *tool_results, *remaining_tool_results],
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-6-39)    )
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-6-40)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-6-41)    # Call model again
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-6-42)    llm_response = call_model(messages).result()
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-6-43)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-6-44)  # Generate final response
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-6-45)  messages = add_messages(messages, llm_response)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-6-46)  return entrypoint.final(value=llm_response, save=messages)

```


API Reference: [MemorySaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.MemorySaver) | [add_messages](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.message.add_messages) | [Command](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Command) | [interrupt](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.interrupt)

### Usage[¶](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#usage "Permanent link")

Let's demonstrate some scenarios.

```
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-7-1)def_print_step(step: dict) -> None:
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-7-2)  for task_name, result in step.items():
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-7-3)    if task_name == "agent":
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-7-4)      continue # just stream from tasks
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-7-5)    print(f"\n{task_name}:")
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-7-6)    if task_name in ("__interrupt__", "review_tool_call"):
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-7-7)      print(result)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-7-8)    else:
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-7-9)      result.pretty_print()

```


### Accept a tool call[¶](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#accept-a-tool-call "Permanent link")

To accept a tool call, we just indicate in the data we provide in the `Command` that the tool call should pass through.

```
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-8-1)config = {"configurable": {"thread_id": "1"}}

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-9-1)user_message = {"role": "user", "content": "What's the weather in san francisco?"}
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-9-2)print(user_message)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-9-3)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-9-4)for step in agent.stream([user_message], config):
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-9-5)  _print_step(step)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-10-1){'role': 'user', 'content': "What's the weather in san francisco?"}
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-10-2)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-10-3)call_model:
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-10-4)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-10-5)Tool Calls:
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-10-6) get_weather (call_Bh5cSwMqCpCxTjx7AjdrQTPd)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-10-7) Call ID: call_Bh5cSwMqCpCxTjx7AjdrQTPd
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-10-8) Args:
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-10-9)  location: San Francisco
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-10-10)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-10-11)__interrupt__:
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-10-12)(Interrupt(value={'question': 'Is this correct?', 'tool_call': {'name': 'get_weather', 'args': {'location': 'San Francisco'}, 'id': 'call_Bh5cSwMqCpCxTjx7AjdrQTPd', 'type': 'tool_call'}}, resumable=True, ns=['agent:22fcc9cd-3573-b39b-eea7-272a025903e2'], when='during'),)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-11-1)human_input = Command(resume={"action": "continue"})
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-11-2)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-11-3)for step in agent.stream(human_input, config):
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-11-4)  _print_step(step)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-12-1)call_tool:
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-12-2)=================================[1m Tool Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-12-3)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-12-4)It's sunny!
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-12-5)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-12-6)call_model:
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-12-7)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-12-8)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-12-9)The weather in San Francisco is sunny!

```


### Revise a tool call[¶](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#revise-a-tool-call "Permanent link")

To revise a tool call, we can supply updated arguments.

```
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-13-1)config = {"configurable": {"thread_id": "2"}}

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-14-1)user_message = {"role": "user", "content": "What's the weather in san francisco?"}
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-14-2)print(user_message)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-14-3)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-14-4)for step in agent.stream([user_message], config):
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-14-5)  _print_step(step)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-15-1){'role': 'user', 'content': "What's the weather in san francisco?"}
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-15-2)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-15-3)call_model:
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-15-4)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-15-5)Tool Calls:
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-15-6) get_weather (call_b9h8e18FqH0IQm3NMoeYKz6N)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-15-7) Call ID: call_b9h8e18FqH0IQm3NMoeYKz6N
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-15-8) Args:
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-15-9)  location: san francisco
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-15-10)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-15-11)__interrupt__:
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-15-12)(Interrupt(value={'question': 'Is this correct?', 'tool_call': {'name': 'get_weather', 'args': {'location': 'san francisco'}, 'id': 'call_b9h8e18FqH0IQm3NMoeYKz6N', 'type': 'tool_call'}}, resumable=True, ns=['agent:9559a81d-5720-dc19-a457-457bac7bdd83'], when='during'),)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-16-1)human_input = Command(resume={"action": "update", "data": {"location": "SF, CA"}})
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-16-2)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-16-3)for step in agent.stream(human_input, config):
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-16-4)  _print_step(step)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-17-1)call_tool:
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-17-2)=================================[1m Tool Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-17-3)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-17-4)It's sunny!
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-17-5)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-17-6)call_model:
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-17-7)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-17-8)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-17-9)The weather in San Francisco is sunny!

```


The LangSmith traces for this run are particularly informative: 

  * In the trace [before the interrupt](https://smith.langchain.com/public/c8b07579-5cf4-4adb-a849-282163bc9d99/r/b5b128d6-e715-480b-b58d-59e64f724275), we generate a tool call for location `"San Francisco"`.
  * In the trace [after resuming](https://smith.langchain.com/public/b28b92e5-a555-482d-aa4d-c675a19f0eb5/r), we see that the tool call in the message has been updated to `"SF, CA"`.



### Generate a custom ToolMessage[¶](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#generate-a-custom-toolmessage "Permanent link")

To Generate a custom `ToolMessage`, we supply the content of the message. In this case we will ask the model to reformat its tool call.

```
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-18-1)config = {"configurable": {"thread_id": "3"}}

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-19-1)user_message = {"role": "user", "content": "What's the weather in san francisco?"}
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-19-2)print(user_message)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-19-3)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-19-4)for step in agent.stream([user_message], config):
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-19-5)  _print_step(step)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-20-1){'role': 'user', 'content': "What's the weather in san francisco?"}
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-20-2)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-20-3)call_model:
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-20-4)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-20-5)Tool Calls:
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-20-6) get_weather (call_VqGjKE7uu8HdWs9XuY1kMV18)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-20-7) Call ID: call_VqGjKE7uu8HdWs9XuY1kMV18
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-20-8) Args:
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-20-9)  location: San Francisco
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-20-10)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-20-11)__interrupt__:
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-20-12)(Interrupt(value={'question': 'Is this correct?', 'tool_call': {'name': 'get_weather', 'args': {'location': 'San Francisco'}, 'id': 'call_VqGjKE7uu8HdWs9XuY1kMV18', 'type': 'tool_call'}}, resumable=True, ns=['agent:4b3b372b-9da3-70be-5c68-3d9317346070'], when='during'),)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-21-1)human_input = Command(
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-21-2)  resume={
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-21-3)    "action": "feedback",
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-21-4)    "data": "Please format as <City>, <State>.",
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-21-5)  },
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-21-6))
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-21-7)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-21-8)for step in agent.stream(human_input, config):
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-21-9)  _print_step(step)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-22-1)call_model:
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-22-2)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-22-3)Tool Calls:
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-22-4) get_weather (call_xoXkK8Cz0zIpvWs78qnXpvYp)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-22-5) Call ID: call_xoXkK8Cz0zIpvWs78qnXpvYp
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-22-6) Args:
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-22-7)  location: San Francisco, CA
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-22-8)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-22-9)__interrupt__:
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-22-10)(Interrupt(value={'question': 'Is this correct?', 'tool_call': {'name': 'get_weather', 'args': {'location': 'San Francisco, CA'}, 'id': 'call_xoXkK8Cz0zIpvWs78qnXpvYp', 'type': 'tool_call'}}, resumable=True, ns=['agent:4b3b372b-9da3-70be-5c68-3d9317346070'], when='during'),)

```


Once it is re-formatted, we can accept it: 

```
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-23-1)human_input = Command(resume={"action": "continue"})
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-23-2)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-23-3)for step in agent.stream(human_input, config):
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-23-4)  _print_step(step)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-24-1)call_tool:
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-24-2)=================================[1m Tool Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-24-3)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-24-4)It's sunny!
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-24-5)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-24-6)call_model:
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-24-7)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-24-8)
[](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__codelineno-24-9)The weather in San Francisco, CA is sunny!

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to wait for user input (Functional API)  ](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/) [ Next  How to stream  ](https://langchain-ai.github.io/langgraph/how-tos/streaming/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
