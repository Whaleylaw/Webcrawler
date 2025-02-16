---
url: https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#how-to-use-the-pre-built-react-agent)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to use the pre-built ReAct agent 

[ ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/?q= "Share")

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
            * How to use the pre-built ReAct agent  [ How to use the pre-built ReAct agent  ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#setup)
              * [ Code  ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#code)
              * [ Usage  ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#usage)
            * [ How to add thread-level memory to a ReAct Agent  ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/)
            * [ How to add a custom system prompt to the prebuilt ReAct agent  ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-system-prompt/)
            * [ How to add human-in-the-loop processes to the prebuilt ReAct agent  ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/)
            * [ How to return structured output from the prebuilt ReAct agent  ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/)
            * [ How to create a ReAct agent from scratch  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#setup)
  * [ Code  ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#code)
  * [ Usage  ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#usage)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Prebuilt ReAct Agent  ](https://langchain-ai.github.io/langgraph/how-tos#prebuilt-react-agent)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/create-react-agent.md "Edit this page")

# How to use the pre-built ReAct agent[¶](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#how-to-use-the-pre-built-react-agent "Permanent link")

Prerequisites

This guide assumes familiarity with the following: 

  * [ Agent Architectures ](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/)
  * [ Chat Models ](https://python.langchain.com/docs/concepts/chat_models/)
  * [ Tools ](https://python.langchain.com/docs/concepts/tools/)



In this how-to we'll create a simple [ReAct](https://arxiv.org/abs/2210.03629) agent app that can check the weather. The app consists of an agent (LLM) and tools. As we interact with the app, we will first call the agent (LLM) to decide if we should use tools. Then we will run a loop: 

  1. If the agent said to take an action (i.e. call tool), we'll run the tools and pass the results back to the agent
  2. If the agent did not ask to run tools, we will finish (respond to the user)



Prebuilt Agent

Please note that here will we use [a prebuilt agent](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent). One of the big benefits of LangGraph is that you can easily create your own agent architectures. So while it's fine to start here to build an agent quickly, we would strongly recommend learning how to build your own agent so that you can take full advantage of LangGraph. 

## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#setup "Permanent link")

First let's install the required packages and set our API keys

```
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-0-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-0-2)%pip install -U langgraph langchain-openai

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-1-1)importgetpass
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-1-2)importos
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-1-5)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-1-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-1-7)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-1-8)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-1-10)_set_env("OPENAI_API_KEY")

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Code[¶](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#code "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-0-1)# First we initialize the model we want to use.
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-0-2)fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-0-3)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-0-4)model = ChatOpenAI(model="gpt-4o", temperature=0)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-0-5)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-0-6)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-0-7)# For this tutorial we will use custom tool that returns pre-defined values for weather in two cities (NYC & SF)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-0-8)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-0-9)fromtypingimport Literal
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-0-10)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-0-11)fromlangchain_core.toolsimport tool
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-0-12)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-0-13)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-0-14)@tool
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-0-15)defget_weather(city: Literal["nyc", "sf"]):
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-0-16)"""Use this to get weather information."""
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-0-17)  if city == "nyc":
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-0-18)    return "It might be cloudy in nyc"
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-0-19)  elif city == "sf":
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-0-20)    return "It's always sunny in sf"
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-0-21)  else:
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-0-22)    raise AssertionError("Unknown city")
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-0-23)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-0-24)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-0-25)tools = [get_weather]
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-0-26)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-0-27)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-0-28)# Define the graph
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-0-29)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-0-30)fromlanggraph.prebuiltimport create_react_agent
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-0-31)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-0-32)graph = create_react_agent(model, tools=tools)

```


## Usage[¶](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#usage "Permanent link")

First, let's visualize the graph we just created

```
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-0-1)fromIPython.displayimport Image, display
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-0-2)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-0-3)display(Image(graph.get_graph().draw_mermaid_png()))

```


![]()

```
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-0-1)defprint_stream(stream):
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-0-2)  for s in stream:
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-0-3)    message = s["messages"][-1]
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-0-4)    if isinstance(message, tuple):
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-0-5)      print(message)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-0-6)    else:
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-0-7)      message.pretty_print()

```


Let's run the app with an input that needs a tool call

```
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-0-1)inputs = {"messages": [("user", "what is the weather in sf")]}
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-0-2)print_stream(graph.stream(inputs, stream_mode="values"))

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-1-1)================================ Human Message =================================
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-1-2)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-1-3)what is the weather in sf

```


Now let's try a question that doesn't need tools

```
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-0-1)inputs = {"messages": [("user", "who built you?")]}
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-0-2)print_stream(graph.stream(inputs, stream_mode="values"))

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-1-1)================================ Human Message =================================
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-1-2)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__codelineno-1-3)who built you?

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to integrate LangGraph (functional API) with AutoGen, CrewAI, and other frameworks  ](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration-functional/) [ Next  How to add thread-level memory to a ReAct Agent  ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
