---
url: https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#how-to-wait-for-user-input-functional-api)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to wait for user input (Functional API) 

[ ](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/?q= "Share")

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
            * How to wait for user input (Functional API)  [ How to wait for user input (Functional API)  ](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#setup)
              * [ Simple usage  ](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#simple-usage)
              * [ Agent  ](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#agent)
                * [ Define model and tools  ](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#define-model-and-tools)
                * [ Define tasks  ](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#define-tasks)
                * [ Define entrypoint  ](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#define-entrypoint)
                * [ Usage  ](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#usage)
            * [ How to review tool calls (Functional API)  ](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#setup)
  * [ Simple usage  ](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#simple-usage)
  * [ Agent  ](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#agent)
    * [ Define model and tools  ](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#define-model-and-tools)
    * [ Define tasks  ](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#define-tasks)
    * [ Define entrypoint  ](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#define-entrypoint)
    * [ Usage  ](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#usage)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraph/how-tos#human-in-the-loop)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/wait-user-input-functional.ipynb "Edit this page")

# How to wait for user input (Functional API)[¶](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#how-to-wait-for-user-input-functional-api "Permanent link")

Prerequisites

This guide assumes familiarity with the following:

  * Implementing [human-in-the-loop](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop) workflows with [interrupt](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#interrupt)
  * [How to create a ReAct agent using the Functional API](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional)



**Human-in-the-loop (HIL)** interactions are crucial for [agentic systems](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#human-in-the-loop). Waiting for human input is a common HIL interaction pattern, allowing the agent to ask the user clarifying questions and await input before proceeding. 

We can implement this in LangGraph using the [interrupt()](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.interrupt) function. `interrupt` allows us to stop graph execution to collect input from a user and continue execution with collected input.

This guide demonstrates how to implement human-in-the-loop workflows using LangGraph's [Functional API](https://langchain-ai.github.io/langgraph/concepts/functional_api). Specifically, we will demonstrate:

  1. [A simple usage example](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#simple-usage)
  2. [How to use with a ReAct agent](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#agent)



## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#setup "Permanent link")

First, let's install the required packages and set our API keys:

```
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-0-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-0-2)%pip install -U langgraph langchain-openai

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-1-1)importgetpass
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-1-2)importos
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-1-5)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-1-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-1-7)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-1-8)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-1-10)_set_env("OPENAI_API_KEY")

```


Set up [LangSmith](https://smith.langchain.com) for better debugging

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM aps built with LangGraph — read more about how to get started in the [docs](https://docs.smith.langchain.com). 

## Simple usage[¶](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#simple-usage "Permanent link")

Let's demonstrate a simple usage example. We will create three [tasks](https://langchain-ai.github.io/langgraph/concepts/functional_api/#task):

  1. Append `"bar"`.
  2. Pause for human input. When resuming, append human input.
  3. Append `"qux"`.



```
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-2-1)fromlanggraph.funcimport entrypoint, task
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-2-2)fromlanggraph.typesimport Command, interrupt
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-2-3)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-2-4)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-2-5)@task
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-2-6)defstep_1(input_query):
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-2-7)"""Append bar."""
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-2-8)  return f"{input_query} bar"
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-2-9)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-2-10)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-2-11)@task
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-2-12)defhuman_feedback(input_query):
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-2-13)"""Append user input."""
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-2-14)  feedback = interrupt(f"Please provide feedback: {input_query}")
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-2-15)  return f"{input_query}{feedback}"
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-2-16)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-2-17)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-2-18)@task
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-2-19)defstep_3(input_query):
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-2-20)"""Append qux."""
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-2-21)  return f"{input_query} qux"

```


API Reference: [entrypoint](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint) | [task](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.task) | [Command](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Command) | [interrupt](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.interrupt)

We can now compose these tasks in a simple [entrypoint](https://langchain-ai.github.io/langgraph/concepts/functional_api/#entrypoint):

```
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-3-1)fromlanggraph.checkpoint.memoryimport MemorySaver
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-3-2)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-3-3)checkpointer = MemorySaver()
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-3-4)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-3-5)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-3-6)@entrypoint(checkpointer=checkpointer)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-3-7)defgraph(input_query):
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-3-8)  result_1 = step_1(input_query).result()
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-3-9)  result_2 = human_feedback(result_1).result()
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-3-10)  result_3 = step_3(result_2).result()
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-3-11)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-3-12)  return result_3

```


API Reference: [MemorySaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.MemorySaver)

All we have done to enable human-in-the-loop workflows is called [interrupt()](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#interrupt) inside a task.

Tip

The results of prior tasks-- in this case `step_1`-- are persisted, so that they are not run again following the `interrupt`.

Let's send in a query string:

```
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-4-1)config = {"configurable": {"thread_id": "1"}}

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-5-1)for event in graph.stream("foo", config):
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-5-2)  print(event)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-5-3)  print("\n")

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-6-1){'step_1': 'foo bar'}
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-6-2)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-6-3)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-6-4){'__interrupt__': (Interrupt(value='Please provide feedback: foo bar', resumable=True, ns=['graph:d66b2e35-0ee3-d8d6-1a22-aec9d58f13b9', 'human_feedback:e0cd4ee2-b874-e1d2-8bc4-3f7ddc06bcc2'], when='during'),)}

```


Note that we've paused with an `interrupt` after `step_1`. The interrupt provides instructions to resume the run. To resume, we issue a [Command](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#the-command-primitive) containing the data expected by the `human_feedback` task. 

```
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-7-1)# Continue execution
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-7-2)for event in graph.stream(Command(resume="baz"), config):
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-7-3)  print(event)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-7-4)  print("\n")

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-8-1){'human_feedback': 'foo bar baz'}
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-8-2)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-8-3)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-8-4){'step_3': 'foo bar baz qux'}
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-8-5)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-8-6)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-8-7){'graph': 'foo bar baz qux'}

```


After resuming, the run proceeds through the remaining step and terminates as expected. 

## Agent[¶](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#agent "Permanent link")

We will build off of the agent created in the [How to create a ReAct agent using the Functional API](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional) guide.

Here we will extend the agent by allowing it to reach out to a human for assistance when needed.

### Define model and tools[¶](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#define-model-and-tools "Permanent link")

Let's first define the tools and model we will use for our example. As in the [ReAct agent guide](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional), we will use a single place-holder tool that gets a description of the weather for a location.

We will use an [OpenAI](https://python.langchain.com/docs/integrations/providers/openai/) chat model for this example, but any model [supporting tool-calling](https://python.langchain.com/docs/integrations/chat/) will suffice.

```
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-9-1)fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-9-2)fromlangchain_core.toolsimport tool
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-9-3)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-9-4)model = ChatOpenAI(model="gpt-4o-mini")
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-9-5)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-9-6)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-9-7)@tool
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-9-8)defget_weather(location: str):
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-9-9)"""Call to get the weather from a specific location."""
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-9-10)  # This is a placeholder for the actual implementation
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-9-11)  if any([city in location.lower() for city in ["sf", "san francisco"]]):
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-9-12)    return "It's sunny!"
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-9-13)  elif "boston" in location.lower():
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-9-14)    return "It's rainy!"
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-9-15)  else:
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-9-16)    return f"I am not sure what the weather is in {location}"

```


API Reference: [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html) | [tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html)

To reach out to a human for assistance, we can simply add a tool that calls [interrupt](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#interrupt):

```
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-10-1)fromlanggraph.typesimport Command, interrupt
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-10-2)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-10-3)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-10-4)@tool
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-10-5)defhuman_assistance(query: str) -> str:
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-10-6)"""Request assistance from a human."""
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-10-7)  human_response = interrupt({"query": query})
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-10-8)  return human_response["data"]
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-10-9)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-10-10)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-10-11)tools = [get_weather, human_assistance]

```


API Reference: [Command](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Command) | [interrupt](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.interrupt)

### Define tasks[¶](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#define-tasks "Permanent link")

Our tasks are otherwise unchanged from the [ReAct agent guide](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional):

  1. **Call model** : We want to query our chat model with a list of messages.
  2. **Call tool** : If our model generates tool calls, we want to execute them.



We just have one more tool accessible to the model.

```
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-11-1)fromlangchain_core.messagesimport ToolMessage
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-11-2)fromlanggraph.funcimport entrypoint, task
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-11-3)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-11-4)tools_by_name = {tool.name: tool for tool in tools}
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-11-5)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-11-6)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-11-7)@task
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-11-8)defcall_model(messages):
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-11-9)"""Call model with a sequence of messages."""
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-11-10)  response = model.bind_tools(tools).invoke(messages)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-11-11)  return response
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-11-12)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-11-13)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-11-14)@task
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-11-15)defcall_tool(tool_call):
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-11-16)  tool = tools_by_name[tool_call["name"]]
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-11-17)  observation = tool.invoke(tool_call)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-11-18)  return ToolMessage(content=observation, tool_call_id=tool_call["id"])

```


API Reference: [ToolMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.tool.ToolMessage.html) | [entrypoint](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint) | [task](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.task)

### Define entrypoint[¶](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#define-entrypoint "Permanent link")

Our [entrypoint](https://langchain-ai.github.io/langgraph/concepts/functional_api/#entrypoint) is also unchanged from the [ReAct agent guide](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional):

```
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-12-1)fromlanggraph.checkpoint.memoryimport MemorySaver
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-12-2)fromlanggraph.graph.messageimport add_messages
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-12-3)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-12-4)checkpointer = MemorySaver()
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-12-5)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-12-6)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-12-7)@entrypoint(checkpointer=checkpointer)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-12-8)defagent(messages, previous):
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-12-9)  if previous is not None:
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-12-10)    messages = add_messages(previous, messages)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-12-11)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-12-12)  llm_response = call_model(messages).result()
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-12-13)  while True:
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-12-14)    if not llm_response.tool_calls:
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-12-15)      break
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-12-16)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-12-17)    # Execute tools
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-12-18)    tool_result_futures = [
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-12-19)      call_tool(tool_call) for tool_call in llm_response.tool_calls
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-12-20)    ]
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-12-21)    tool_results = [fut.result() for fut in tool_result_futures]
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-12-22)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-12-23)    # Append to message list
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-12-24)    messages = add_messages(messages, [llm_response, *tool_results])
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-12-25)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-12-26)    # Call model again
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-12-27)    llm_response = call_model(messages).result()
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-12-28)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-12-29)  # Generate final response
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-12-30)  messages = add_messages(messages, llm_response)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-12-31)  return entrypoint.final(value=llm_response, save=messages)

```


API Reference: [MemorySaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.MemorySaver) | [add_messages](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.message.add_messages)

### Usage[¶](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#usage "Permanent link")

Let's invoke our model with a question that requires human assistance. Our question will also require an invocation of the `get_weather` tool:

```
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-13-1)def_print_step(step: dict) -> None:
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-13-2)  for task_name, result in step.items():
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-13-3)    if task_name == "agent":
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-13-4)      continue # just stream from tasks
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-13-5)    print(f"\n{task_name}:")
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-13-6)    if task_name == "__interrupt__":
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-13-7)      print(result)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-13-8)    else:
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-13-9)      result.pretty_print()

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-14-1)config = {"configurable": {"thread_id": "1"}}

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-15-1)user_message = {
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-15-2)  "role": "user",
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-15-3)  "content": (
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-15-4)    "Can you reach out for human assistance: what should I feed my cat? "
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-15-5)    "Separately, can you check the weather in San Francisco?"
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-15-6)  ),
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-15-7)}
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-15-8)print(user_message)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-15-9)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-15-10)for step in agent.stream([user_message], config):
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-15-11)  _print_step(step)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-16-1){'role': 'user', 'content': 'Can you reach out for human assistance: what should I feed my cat? Separately, can you check the weather in San Francisco?'}
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-16-2)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-16-3)call_model:
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-16-4)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-16-5)Tool Calls:
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-16-6) human_assistance (call_joAEBVX7Abfm7TsZ0k95ZkVx)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-16-7) Call ID: call_joAEBVX7Abfm7TsZ0k95ZkVx
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-16-8) Args:
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-16-9)  query: What should I feed my cat?
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-16-10) get_weather (call_ut7zfHFCcms63BOZLrRHszGH)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-16-11) Call ID: call_ut7zfHFCcms63BOZLrRHszGH
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-16-12) Args:
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-16-13)  location: San Francisco
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-16-14)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-16-15)call_tool:
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-16-16)=================================[1m Tool Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-16-17)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-16-18)content="It's sunny!" name='get_weather' tool_call_id='call_ut7zfHFCcms63BOZLrRHszGH'
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-16-19)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-16-20)__interrupt__:
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-16-21)(Interrupt(value={'query': 'What should I feed my cat?'}, resumable=True, ns=['agent:aa676ccc-b038-25e3-9c8a-18e81d4e1372', 'call_tool:059d53d2-3344-13bc-e170-48b632c2dd97'], when='during'),)

```


Note that we generate two tool calls, and although our run is interrupted, we did not block the execution of the `get_weather` tool. 

Let's inspect where we're interrupted:

```
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-17-1)print(step)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-18-1){'__interrupt__': (Interrupt(value={'query': 'What should I feed my cat?'}, resumable=True, ns=['agent:aa676ccc-b038-25e3-9c8a-18e81d4e1372', 'call_tool:059d53d2-3344-13bc-e170-48b632c2dd97'], when='during'),)}

```


We can resume execution by issuing a [Command](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#the-command-primitive). Note that the data we supply in the `Command` can be customized to your needs based on the implementation of `human_assistance`. 

```
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-19-1)human_response = "You should feed your cat a fish."
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-19-2)human_command = Command(resume={"data": human_response})
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-19-3)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-19-4)for step in agent.stream(human_command, config):
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-19-5)  _print_step(step)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-20-1)call_tool:
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-20-2)=================================[1m Tool Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-20-3)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-20-4)content='You should feed your cat a fish.' name='human_assistance' tool_call_id='call_joAEBVX7Abfm7TsZ0k95ZkVx'
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-20-5)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-20-6)call_model:
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-20-7)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-20-8)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-20-9)For human assistance, you should feed your cat fish. 
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-20-10)
[](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__codelineno-20-11)Regarding the weather in San Francisco, it's sunny!

```


Above, when we resume we provide the final tool message, allowing the model to generate its response. Check out the LangSmith traces to see a full breakdown of the runs: 

  1. [Trace from initial query](https://smith.langchain.com/public/c3d8879d-4d01-41be-807e-6d9eed15df99/r)
  2. [Trace after resuming](https://smith.langchain.com/public/97c05ef9-8b4c-428e-8826-3fd417c8c75f/r)

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to Review Tool Calls  ](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/) [ Next  How to review tool calls (Functional API)  ](https://langchain-ai.github.io/langgraph/how-tos/review-tool-calls-functional/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/wait-user-input-functional/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
