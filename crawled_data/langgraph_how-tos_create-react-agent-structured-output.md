---
url: https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#how-to-return-structured-output-from-the-prebuilt-react-agent)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to return structured output from the prebuilt ReAct agent 

[ ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/?q= "Share")

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
            * How to return structured output from the prebuilt ReAct agent  [ How to return structured output from the prebuilt ReAct agent  ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#setup)
              * [ Code  ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#code)
              * [ Usage  ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#usage)
                * [ Customizing prompt  ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#customizing-prompt)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#setup)
  * [ Code  ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#code)
  * [ Usage  ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#usage)
    * [ Customizing prompt  ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#customizing-prompt)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Prebuilt ReAct Agent  ](https://langchain-ai.github.io/langgraph/how-tos#prebuilt-react-agent)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/create-react-agent-structured-output.ipynb "Edit this page")

# How to return structured output from the prebuilt ReAct agent[¶](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#how-to-return-structured-output-from-the-prebuilt-react-agent "Permanent link")

Prerequisites

This guide assumes familiarity with the following:

  * [Agent Architectures](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/)
  * [Chat Models](https://python.langchain.com/docs/concepts/chat_models/)
  * [Tools](https://python.langchain.com/docs/concepts/tools/)
  * [Structured Output](https://python.langchain.com/docs/concepts/structured_outputs/)



To return structured output from the prebuilt ReAct agent you can provide a `response_format` parameter with the desired output schema to [create_react_agent](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent):

```
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-0-1)classResponseFormat(BaseModel):
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-0-2)"""Respond to the user in this format."""
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-0-3)  my_special_output: str
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-0-4)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-0-5)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-0-6)graph = create_react_agent(
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-0-7)  model,
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-0-8)  tools=tools,
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-0-9)  # specify the schema for the structured output using `response_format` parameter
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-0-10)  response_format=ResponseFormat
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-0-11))

```


Prebuilt ReAct makes an additional LLM call at the end of the ReAct loop to produce a structured output response. Please see [this guide](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output) to learn about other strategies for returning structured outputs from a tool-calling agent.

## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#setup "Permanent link")

First, let's install the required packages and set our API keys

```
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-1-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-1-2)%pip install -U langgraph langchain-openai

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-2-1)importgetpass
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-2-2)importos
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-2-3)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-2-4)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-2-5)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-2-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-2-7)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-2-8)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-2-9)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-2-10)_set_env("OPENAI_API_KEY")

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Code[¶](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#code "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-3-1)# First we initialize the model we want to use.
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-3-2)fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-3-3)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-3-4)model = ChatOpenAI(model="gpt-4o", temperature=0)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-3-5)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-3-6)# For this tutorial we will use custom tool that returns pre-defined values for weather in two cities (NYC & SF)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-3-7)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-3-8)fromtypingimport Literal
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-3-9)fromlangchain_core.toolsimport tool
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-3-10)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-3-11)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-3-12)@tool
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-3-13)defget_weather(city: Literal["nyc", "sf"]):
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-3-14)"""Use this to get weather information."""
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-3-15)  if city == "nyc":
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-3-16)    return "It might be cloudy in nyc"
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-3-17)  elif city == "sf":
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-3-18)    return "It's always sunny in sf"
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-3-19)  else:
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-3-20)    raise AssertionError("Unknown city")
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-3-21)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-3-22)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-3-23)tools = [get_weather]
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-3-24)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-3-25)# Define the structured output schema
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-3-26)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-3-27)frompydanticimport BaseModel, Field
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-3-28)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-3-29)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-3-30)classWeatherResponse(BaseModel):
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-3-31)"""Respond to the user in this format."""
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-3-32)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-3-33)  conditions: str = Field(description="Weather conditions")
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-3-34)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-3-35)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-3-36)# Define the graph
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-3-37)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-3-38)fromlanggraph.prebuiltimport create_react_agent
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-3-39)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-3-40)graph = create_react_agent(
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-3-41)  model,
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-3-42)  tools=tools,
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-3-43)  # specify the schema for the structured output using `response_format` parameter
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-3-44)  response_format=WeatherResponse,
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-3-45))

```


API Reference: [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html) | [tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html) | [create_react_agent](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent)

## Usage[¶](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#usage "Permanent link")

Let's now test our agent:

```
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-4-1)inputs = {"messages": [("user", "What's the weather in NYC?")]}
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-4-2)response = graph.invoke(inputs)

```


You can see that the agent output contains a `structured_response` key with the structured output conforming to the specified `WeatherResponse` schema, in addition to the message history under `messages` key.

```
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-5-1)response["structured_response"]

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-6-1)WeatherResponse(conditions='cloudy')

```


### Customizing prompt[¶](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#customizing-prompt "Permanent link")

You might need to further customize the second LLM call for the structured output generation and provide a system prompt. To do so, you can pass a tuple (prompt, schema):

```
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-7-1)graph = create_react_agent(
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-7-2)  model,
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-7-3)  tools=tools,
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-7-4)  # specify both the system prompt and the schema for the structured output
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-7-5)  response_format=("Always return capitalized weather conditions", WeatherResponse),
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-7-6))
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-7-7)
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-7-8)inputs = {"messages": [("user", "What's the weather in NYC?")]}
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-7-9)response = graph.invoke(inputs)

```


You can verify that the structured response now contains a capitalized value:

```
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-8-1)response["structured_response"]

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__codelineno-9-1)WeatherResponse(conditions='Cloudy')

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to add human-in-the-loop processes to the prebuilt ReAct agent  ](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-hitl/) [ Next  How to create a ReAct agent from scratch  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-structured-output/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
