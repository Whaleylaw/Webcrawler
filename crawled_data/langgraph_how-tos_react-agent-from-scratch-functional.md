---
url: https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#how-to-create-a-react-agent-from-scratch-functional-api)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to create a ReAct agent from scratch (Functional API) 

[ ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/?q= "Share")

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
          * [ Other  ](https://langchain-ai.github.io/langgraph/how-tos#other)
          * Prebuilt ReAct Agent  Prebuilt ReAct Agent 
            * [ Prebuilt ReAct Agent  ](https://langchain-ai.github.io/langgraph/how-tos#prebuilt-react-agent)
            * [ How to use the pre-built ReAct agent  ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/)
            * [ How to add thread-level memory to a ReAct Agent  ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/)
            * [ How to add a custom system prompt to the prebuilt ReAct agent  ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-system-prompt/)
            * [ How to add human-in-the-loop processes to the prebuilt ReAct agent  ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/)
            * [ How to return structured output from the prebuilt ReAct agent  ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/)
            * [ How to create a ReAct agent from scratch  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/)
            * How to create a ReAct agent from scratch (Functional API)  [ How to create a ReAct agent from scratch (Functional API)  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#setup)
              * [ Create ReAct agent  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#create-react-agent)
                * [ Define model and tools  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#define-model-and-tools)
                * [ Define tasks  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#define-tasks)
                * [ Define entrypoint  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#define-entrypoint)
              * [ Usage  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#usage)
              * [ Add thread-level persistence  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#add-thread-level-persistence)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#setup)
  * [ Create ReAct agent  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#create-react-agent)
    * [ Define model and tools  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#define-model-and-tools)
    * [ Define tasks  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#define-tasks)
    * [ Define entrypoint  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#define-entrypoint)
  * [ Usage  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#usage)
  * [ Add thread-level persistence  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#add-thread-level-persistence)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Prebuilt ReAct Agent  ](https://langchain-ai.github.io/langgraph/how-tos#prebuilt-react-agent)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/react-agent-from-scratch-functional.ipynb "Edit this page")

# How to create a ReAct agent from scratch (Functional API)[¶](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#how-to-create-a-react-agent-from-scratch-functional-api "Permanent link")

Prerequisites

This guide assumes familiarity with the following:

  * [Chat Models](https://python.langchain.com/docs/concepts/chat_models)
  * [Messages](https://python.langchain.com/docs/concepts/messages)
  * [Tool Calling](https://python.langchain.com/docs/concepts/tool_calling/)
  * [Entrypoints](https://langchain-ai.github.io/langgraph/concepts/functional_api/#entrypoint) and [Tasks](https://langchain-ai.github.io/langgraph/concepts/functional_api/#task)



This guide demonstrates how to implement a ReAct agent using the LangGraph [Functional API](https://langchain-ai.github.io/langgraph/concepts/functional_api).

The ReAct agent is a [tool-calling agent](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#tool-calling-agent) that operates as follows:

  1. Queries are issued to a chat model;
  2. If the model generates no [tool calls](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#tool-calling), we return the model response.
  3. If the model generates tool calls, we execute the tool calls with available tools, append them as [tool messages](https://python.langchain.com/docs/concepts/messages/) to our message list, and repeat the process.



This is a simple and versatile set-up that can be extended with memory, human-in-the-loop capabilities, and other features. See the dedicated [how-to guides](https://langchain-ai.github.io/langgraph/how-tos/#prebuilt-react-agent) for examples.

## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#setup "Permanent link")

First, let's install the required packages and set our API keys:

```
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-0-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-0-2)%pip install -U langgraph langchain-openai

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-1-1)importgetpass
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-1-2)importos
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-1-5)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-1-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-1-7)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-1-8)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-1-10)_set_env("OPENAI_API_KEY")

```


Set up [LangSmith](https://smith.langchain.com) for better debugging

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM aps built with LangGraph — read more about how to get started in the [docs](https://docs.smith.langchain.com). 

## Create ReAct agent[¶](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#create-react-agent "Permanent link")

Now that you have installed the required packages and set your environment variables, we can create our agent.

### Define model and tools[¶](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#define-model-and-tools "Permanent link")

Let's first define the tools and model we will use for our example. Here we will use a single place-holder tool that gets a description of the weather for a location.

We will use an [OpenAI](https://python.langchain.com/docs/integrations/providers/openai/) chat model for this example, but any model [supporting tool-calling](https://python.langchain.com/docs/integrations/chat/) will suffice.

```
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-2-1)fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-2-2)fromlangchain_core.toolsimport tool
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-2-3)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-2-4)model = ChatOpenAI(model="gpt-4o-mini")
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-2-5)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-2-6)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-2-7)@tool
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-2-8)defget_weather(location: str):
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-2-9)"""Call to get the weather from a specific location."""
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-2-10)  # This is a placeholder for the actual implementation
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-2-11)  if any([city in location.lower() for city in ["sf", "san francisco"]]):
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-2-12)    return "It's sunny!"
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-2-13)  elif "boston" in location.lower():
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-2-14)    return "It's rainy!"
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-2-15)  else:
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-2-16)    return f"I am not sure what the weather is in {location}"
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-2-17)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-2-18)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-2-19)tools = [get_weather]

```


API Reference: [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html) | [tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html)

### Define tasks[¶](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#define-tasks "Permanent link")

We next define the [tasks](https://langchain-ai.github.io/langgraph/concepts/functional_api/#task) we will execute. Here there are two different tasks:

  1. **Call model** : We want to query our chat model with a list of messages.
  2. **Call tool** : If our model generates tool calls, we want to execute them.



```
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-3-1)fromlangchain_core.messagesimport ToolMessage
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-3-2)fromlanggraph.funcimport entrypoint, task
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-3-3)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-3-4)tools_by_name = {tool.name: tool for tool in tools}
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-3-5)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-3-6)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-3-7)@task
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-3-8)defcall_model(messages):
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-3-9)"""Call model with a sequence of messages."""
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-3-10)  response = model.bind_tools(tools).invoke(messages)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-3-11)  return response
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-3-12)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-3-13)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-3-14)@task
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-3-15)defcall_tool(tool_call):
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-3-16)  tool = tools_by_name[tool_call["name"]]
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-3-17)  observation = tool.invoke(tool_call["args"])
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-3-18)  return ToolMessage(content=observation, tool_call_id=tool_call["id"])

```


API Reference: [ToolMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.tool.ToolMessage.html) | [entrypoint](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint) | [task](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.task)

### Define entrypoint[¶](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#define-entrypoint "Permanent link")

Our [entrypoint](https://langchain-ai.github.io/langgraph/concepts/functional_api/#entrypoint) will handle the orchestration of these two tasks. As described above, when our `call_model` task generates tool calls, the `call_tool` task will generate responses for each. We append all messages to a single messages list.

Tip

Note that because tasks return future-like objects, the below implementation executes tools in parallel.

```
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-4-1)fromlanggraph.graph.messageimport add_messages
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-4-2)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-4-3)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-4-4)@entrypoint()
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-4-5)defagent(messages):
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-4-6)  llm_response = call_model(messages).result()
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-4-7)  while True:
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-4-8)    if not llm_response.tool_calls:
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-4-9)      break
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-4-10)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-4-11)    # Execute tools
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-4-12)    tool_result_futures = [
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-4-13)      call_tool(tool_call) for tool_call in llm_response.tool_calls
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-4-14)    ]
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-4-15)    tool_results = [fut.result() for fut in tool_result_futures]
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-4-16)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-4-17)    # Append to message list
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-4-18)    messages = add_messages(messages, [llm_response, *tool_results])
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-4-19)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-4-20)    # Call model again
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-4-21)    llm_response = call_model(messages).result()
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-4-22)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-4-23)  return llm_response

```


API Reference: [add_messages](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.message.add_messages)

## Usage[¶](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#usage "Permanent link")

To use our agent, we invoke it with a messages list. Based on our implementation, these can be LangChain [message](https://python.langchain.com/docs/concepts/messages/) objects or OpenAI-style dicts:

```
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-5-1)user_message = {"role": "user", "content": "What's the weather in san francisco?"}
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-5-2)print(user_message)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-5-3)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-5-4)for step in agent.stream([user_message]):
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-5-5)  for task_name, message in step.items():
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-5-6)    if task_name == "agent":
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-5-7)      continue # Just print task updates
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-5-8)    print(f"\n{task_name}:")
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-5-9)    message.pretty_print()

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-6-1){'role': 'user', 'content': "What's the weather in san francisco?"}
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-6-2)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-6-3)call_model:
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-6-4)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-6-5)Tool Calls:
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-6-6) get_weather (call_tNnkrjnoz6MNfCHJpwfuEQ0v)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-6-7) Call ID: call_tNnkrjnoz6MNfCHJpwfuEQ0v
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-6-8) Args:
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-6-9)  location: san francisco
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-6-10)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-6-11)call_tool:
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-6-12)=================================[1m Tool Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-6-13)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-6-14)It's sunny!
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-6-15)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-6-16)call_model:
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-6-17)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-6-18)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-6-19)The weather in San Francisco is sunny!

```


Perfect! The graph correctly calls the `get_weather` tool and responds to the user after receiving the information from the tool. Check out the LangSmith trace [here](https://smith.langchain.com/public/d5a0d5ea-bdaa-4032-911e-7db177c8141b/r). 

## Add thread-level persistence[¶](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#add-thread-level-persistence "Permanent link")

Adding [thread-level persistence](https://langchain-ai.github.io/langgraph/concepts/persistence#threads) lets us support conversational experiences with our agent: subsequent invocations will append to the prior messages list, retaining the full conversational context.

To add thread-level persistence to our agent:

  1. Select a [checkpointer](https://langchain-ai.github.io/langgraph/concepts/persistence#checkpointer-libraries): here we will use [MemorySaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.MemorySaver), a simple in-memory checkpointer.
  2. Update our entrypoint to accept the previous messages state as a second argument. Here, we simply append the message updates to the previous sequence of messages.
  3. Choose which values will be returned from the workflow and which will be saved by the checkpointer as `previous` using `entrypoint.final` (optional)



```
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-7-1)fromlanggraph.checkpoint.memoryimport MemorySaver
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-7-2)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-7-3)checkpointer = MemorySaver()
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-7-4)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-7-5)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-7-6)@entrypoint(checkpointer=checkpointer)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-7-7)defagent(messages, previous):
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-7-8)  if previous is not None:
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-7-9)    messages = add_messages(previous, messages)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-7-10)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-7-11)  llm_response = call_model(messages).result()
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-7-12)  while True:
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-7-13)    if not llm_response.tool_calls:
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-7-14)      break
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-7-15)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-7-16)    # Execute tools
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-7-17)    tool_result_futures = [
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-7-18)      call_tool(tool_call) for tool_call in llm_response.tool_calls
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-7-19)    ]
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-7-20)    tool_results = [fut.result() for fut in tool_result_futures]
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-7-21)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-7-22)    # Append to message list
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-7-23)    messages = add_messages(messages, [llm_response, *tool_results])
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-7-24)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-7-25)    # Call model again
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-7-26)    llm_response = call_model(messages).result()
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-7-27)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-7-28)  # Generate final response
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-7-29)  messages = add_messages(messages, llm_response)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-7-30)  return entrypoint.final(value=llm_response, save=messages)

```


API Reference: [MemorySaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.MemorySaver)

We will now need to pass in a config when running our application. The config will specify an identifier for the conversational thread.

Tip

Read more about thread-level persistence in our [concepts page](https://langchain-ai.github.io/langgraph/concepts/persistence/) and [how-to guides](https://langchain-ai.github.io/langgraph/how-tos/#persistence).

```
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-8-1)config = {"configurable": {"thread_id": "1"}}

```


We start a thread the same way as before, this time passing in the config:

```
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-9-1)user_message = {"role": "user", "content": "What's the weather in san francisco?"}
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-9-2)print(user_message)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-9-3)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-9-4)for step in agent.stream([user_message], config):
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-9-5)  for task_name, message in step.items():
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-9-6)    if task_name == "agent":
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-9-7)      continue # Just print task updates
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-9-8)    print(f"\n{task_name}:")
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-9-9)    message.pretty_print()

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-10-1){'role': 'user', 'content': "What's the weather in san francisco?"}
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-10-2)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-10-3)call_model:
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-10-4)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-10-5)Tool Calls:
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-10-6) get_weather (call_lubbUSdDofmOhFunPEZLBz3g)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-10-7) Call ID: call_lubbUSdDofmOhFunPEZLBz3g
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-10-8) Args:
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-10-9)  location: San Francisco
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-10-10)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-10-11)call_tool:
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-10-12)=================================[1m Tool Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-10-13)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-10-14)It's sunny!
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-10-15)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-10-16)call_model:
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-10-17)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-10-18)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-10-19)The weather in San Francisco is sunny!

```


When we ask a follow-up conversation, the model uses the prior context to infer that we are asking about the weather: 

```
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-11-1)user_message = {"role": "user", "content": "How does it compare to Boston, MA?"}
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-11-2)print(user_message)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-11-3)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-11-4)for step in agent.stream([user_message], config):
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-11-5)  for task_name, message in step.items():
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-11-6)    if task_name == "agent":
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-11-7)      continue # Just print task updates
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-11-8)    print(f"\n{task_name}:")
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-11-9)    message.pretty_print()

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-12-1){'role': 'user', 'content': 'How does it compare to Boston, MA?'}
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-12-2)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-12-3)call_model:
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-12-4)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-12-5)Tool Calls:
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-12-6) get_weather (call_8sTKYAhSIHOdjLD5d6gaswuV)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-12-7) Call ID: call_8sTKYAhSIHOdjLD5d6gaswuV
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-12-8) Args:
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-12-9)  location: Boston, MA
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-12-10)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-12-11)call_tool:
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-12-12)=================================[1m Tool Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-12-13)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-12-14)It's rainy!
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-12-15)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-12-16)call_model:
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-12-17)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-12-18)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__codelineno-12-19)Compared to San Francisco, which is sunny, Boston, MA is experiencing rainy weather.

```


In the [LangSmith trace](https://smith.langchain.com/public/20a1116b-bb3b-44c1-8765-7a28663439d9/r), we can see that the full conversational context is retained in each model call.  Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to create a ReAct agent from scratch  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/) [ Next  How to Set Up a LangGraph Application for Deployment  ](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
