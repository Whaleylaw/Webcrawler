---
url: https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#how-to-add-thread-level-memory-to-a-react-agent)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to add thread-level memory to a ReAct Agent 

[ ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/?q= "Share")

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
            * How to add thread-level memory to a ReAct Agent  [ How to add thread-level memory to a ReAct Agent  ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#setup)
              * [ Code  ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#code)
              * [ Usage  ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#usage)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#setup)
  * [ Code  ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#code)
  * [ Usage  ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#usage)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Prebuilt ReAct Agent  ](https://langchain-ai.github.io/langgraph/how-tos#prebuilt-react-agent)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/create-react-agent-memory.ipynb "Edit this page")

# How to add thread-level memory to a ReAct Agent[¶](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#how-to-add-thread-level-memory-to-a-react-agent "Permanent link")

Prerequisites

This guide assumes familiarity with the following: 

  * [ LangGraph Persistence ](https://langchain-ai.github.io/langgraph/concepts/persistence/)
  * [ Checkpointer interface ](https://langchain-ai.github.io/langgraph/concepts/persistence/#checkpointer-interface)
  * [ Agent Architectures ](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/)
  * [ Chat Models ](https://python.langchain.com/docs/concepts/chat_models/)
  * [ Tools ](https://python.langchain.com/docs/concepts/tools/)



This guide will show how to add memory to the prebuilt ReAct agent. Please see [this tutorial](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent) for how to get started with the prebuilt ReAct agent

We can add memory to the agent, by passing a [checkpointer](https://langchain-ai.github.io/langgraph/reference/checkpoints/) to the [create_react_agent](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent) function.

## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#setup "Permanent link")

First, let's install the required packages and set our API keys

```
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-0-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-0-2)%pip install -U langgraph langchain-openai

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-1-1)importgetpass
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-1-2)importos
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-1-5)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-1-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-1-7)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-1-8)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-1-10)_set_env("OPENAI_API_KEY")

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Code[¶](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#code "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-2-1)# First we initialize the model we want to use.
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-2-2)fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-2-3)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-2-4)model = ChatOpenAI(model="gpt-4o", temperature=0)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-2-5)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-2-6)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-2-7)# For this tutorial we will use custom tool that returns pre-defined values for weather in two cities (NYC & SF)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-2-8)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-2-9)fromtypingimport Literal
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-2-10)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-2-11)fromlangchain_core.toolsimport tool
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-2-12)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-2-13)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-2-14)@tool
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-2-15)defget_weather(city: Literal["nyc", "sf"]):
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-2-16)"""Use this to get weather information."""
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-2-17)  if city == "nyc":
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-2-18)    return "It might be cloudy in nyc"
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-2-19)  elif city == "sf":
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-2-20)    return "It's always sunny in sf"
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-2-21)  else:
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-2-22)    raise AssertionError("Unknown city")
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-2-23)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-2-24)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-2-25)tools = [get_weather]
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-2-26)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-2-27)# We can add "chat memory" to the graph with LangGraph's checkpointer
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-2-28)# to retain the chat context between interactions
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-2-29)fromlanggraph.checkpoint.memoryimport MemorySaver
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-2-30)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-2-31)memory = MemorySaver()
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-2-32)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-2-33)# Define the graph
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-2-34)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-2-35)fromlanggraph.prebuiltimport create_react_agent
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-2-36)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-2-37)graph = create_react_agent(model, tools=tools, checkpointer=memory)

```


API Reference: [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html) | [tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html) | [MemorySaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.MemorySaver) | [create_react_agent](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent)

## Usage[¶](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#usage "Permanent link")

Let's interact with it multiple times to show that it can remember

```
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-3-1)defprint_stream(stream):
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-3-2)  for s in stream:
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-3-3)    message = s["messages"][-1]
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-3-4)    if isinstance(message, tuple):
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-3-5)      print(message)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-3-6)    else:
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-3-7)      message.pretty_print()

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-4-1)config = {"configurable": {"thread_id": "1"}}
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-4-2)inputs = {"messages": [("user", "What's the weather in NYC?")]}
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-4-3)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-4-4)print_stream(graph.stream(inputs, config=config, stream_mode="values"))

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-5-1)================================[1m Human Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-5-2)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-5-3)What's the weather in NYC?
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-5-4)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-5-5)Tool Calls:
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-5-6) get_weather (call_xM1suIq26KXvRFqJIvLVGfqG)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-5-7) Call ID: call_xM1suIq26KXvRFqJIvLVGfqG
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-5-8) Args:
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-5-9)  city: nyc
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-5-10)=================================[1m Tool Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-5-11)Name: get_weather
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-5-12)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-5-13)It might be cloudy in nyc
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-5-14)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-5-15)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-5-16)The weather in NYC might be cloudy.

```


Notice that when we pass the same the same thread ID, the chat history is preserved 

```
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-6-1)inputs = {"messages": [("user", "What's it known for?")]}
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-6-2)print_stream(graph.stream(inputs, config=config, stream_mode="values"))

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-7-1)================================[1m Human Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-7-2)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-7-3)What's it known for?
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-7-4)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-7-5)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-7-6)New York City (NYC) is known for a variety of iconic landmarks, cultural institutions, and vibrant neighborhoods. Some of the most notable aspects include:
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-7-7)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-7-8)1. **Statue of Liberty**: A symbol of freedom and democracy.
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-7-9)2. **Times Square**: Known for its bright lights, Broadway theaters, and bustling atmosphere.
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-7-10)3. **Central Park**: A large urban park offering a green oasis in the middle of the city.
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-7-11)4. **Empire State Building**: An iconic skyscraper with an observation deck offering panoramic views of the city.
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-7-12)5. **Broadway**: Famous for its world-class theater productions.
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-7-13)6. **Wall Street**: The financial hub of the United States.
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-7-14)7. **Museums**: Including the Metropolitan Museum of Art, the Museum of Modern Art (MoMA), and the American Museum of Natural History.
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-7-15)8. **Diverse Cuisine**: A melting pot of culinary experiences from around the world.
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-7-16)9. **Cultural Diversity**: A rich tapestry of cultures, languages, and traditions.
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-7-17)10. **Fashion**: A global fashion capital, home to New York Fashion Week.
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-7-18)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-7-19)These are just a few highlights of what makes NYC a unique and vibrant city.

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__codelineno-8-1)

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to use the pre-built ReAct agent  ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/) [ Next  How to add a custom system prompt to the prebuilt ReAct agent  ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-system-prompt/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-memory/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
