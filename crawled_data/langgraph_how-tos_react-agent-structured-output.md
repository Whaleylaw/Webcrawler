---
url: https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#how-to-force-tool-calling-agent-to-structure-output)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to force tool-calling agent to structure output 

[ ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/?q= "Share")

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
            * How to force tool-calling agent to structure output  [ How to force tool-calling agent to structure output  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#setup)
              * [ Define model, tools, and graph state  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#define-model-tools-and-graph-state)
              * [ Option 1: Bind output as tool  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#option-1-bind-output-as-tool)
                * [ Define Graph  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#define-graph)
                * [ Usage  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#usage)
              * [ Option 2: 2 LLMs  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#option-2-2-llms)
                * [ Define Graph  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#define-graph_1)
                * [ Usage  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#usage_1)
            * [ How to pass custom run ID or set tags and metadata for graph runs in LangSmith  ](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/)
            * [ How to integrate LangGraph with AutoGen, CrewAI, and other frameworks  ](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#setup)
  * [ Define model, tools, and graph state  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#define-model-tools-and-graph-state)
  * [ Option 1: Bind output as tool  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#option-1-bind-output-as-tool)
    * [ Define Graph  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#define-graph)
    * [ Usage  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#usage)
  * [ Option 2: 2 LLMs  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#option-2-2-llms)
    * [ Define Graph  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#define-graph_1)
    * [ Usage  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#usage_1)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Other  ](https://langchain-ai.github.io/langgraph/how-tos#other)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/react-agent-structured-output.ipynb "Edit this page")

# How to force tool-calling agent to structure output[¶](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#how-to-force-tool-calling-agent-to-structure-output "Permanent link")

Prerequisites

This guide assumes familiarity with the following: 

  * [ Structured Output ](https://python.langchain.com/docs/concepts/#structured-output)
  * [ Tool calling agent ](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#tool-calling-agent)
  * [ Chat Models ](https://python.langchain.com/docs/concepts/#chat-models)
  * [ Messages ](https://python.langchain.com/docs/concepts/#messages)
  * [ LangGraph Glossary ](https://langchain-ai.github.io/langgraph/concepts/low_level/)



You might want your agent to return its output in a structured format. For example, if the output of the agent is used by some other downstream software, you may want the output to be in the same structured format every time the agent is invoked to ensure consistency.

This notebook will walk through two different options for forcing a tool calling agent to structure its output. We will be using a basic [ReAct agent](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/) (a model node and a tool-calling node) together with a third node at the end that will format response for the user. Both of the options will use the same graph structure as shown in the diagram below, but will have different mechanisms under the hood.

![react_diagrams.png]()

**Option 1**

![option1.png]()

The first way you can force your tool calling agent to have structured output is to bind the output you would like as an additional tool for the `agent` node to use. In contrast to the basic ReAct agent, the `agent` node in this case is not selecting between `tools` and `END` but rather selecting between the specific tools it calls. The expected flow in this case is that the LLM in the `agent` node will first select the action tool, and after receiving the action tool output it will call the response tool, which will then route to the `respond` node which simply structures the arguments from the `agent` node tool call.

**Pros and Cons**

The benefit to this format is that you only need one LLM, and can save money and latency because of this. The downside to this option is that it isn't guaranteed that the single LLM will call the correct tool when you want it to. We can help the LLM by setting `tool_choice` to `any` when we use `bind_tools` which forces the LLM to select at least one tool at every turn, but this is far from a fool proof strategy. In addition, another downside is that the agent might call _multiple_ tools, so we need to check for this explicitly in our routing function (or if we are using OpenAI we an set `parallell_tool_calling=False` to ensure only one tool is called at a time).

**Option 2**

![option2.png]()

The second way you can force your tool calling agent to have structured output is to use a second LLM (in this case `model_with_structured_output`) to respond to the user. 

In this case, you will define a basic ReAct agent normally, but instead of having the `agent` node choose between the `tools` node and ending the conversation, the `agent` node will choose between the `tools` node and the `respond` node. The `respond` node will contain a second LLM that uses structured output, and once called will return directly to the user. You can think of this method as basic ReAct with one extra step before responding to the user. 

**Pros and Cons**

The benefit of this method is that it guarantees structured output (as long as `.with_structured_output` works as expected with the LLM). The downside to using this approach is that it requires making an additional LLM call before responding to the user, which can increase costs as well as latency. In addition, by not providing the `agent` node LLM with information about the desired output schema there is a risk that the `agent` LLM will fail to call the correct tools required to answer in the correct output schema.

Note that both of these options will follow the exact same graph structure (see the diagram above), in that they are both exact replicas of the basic ReAct architecture but with a `respond` node before the end.

## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#setup "Permanent link")

First, let's install the required packages and set our API keys

```
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-0-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-0-2)%pip install -U langgraph langchain_anthropic

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-1-1)importgetpass
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-1-2)importos
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-1-5)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-1-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-1-7)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-1-8)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-1-10)_set_env("ANTHROPIC_API_KEY")

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Define model, tools, and graph state[¶](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#define-model-tools-and-graph-state "Permanent link")

Now we can define how we want to structure our output, define our graph state, and also our tools and the models we are going to use.

To use structured output, we will use the `with_structured_output` method from LangChain, which you can read more about [here](https://python.langchain.com/docs/how_to/structured_output/).

We are going to use a single tool in this example for finding the weather, and will return a structured weather response to the user.

```
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-2-1)frompydanticimport BaseModel, Field
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-2-2)fromtypingimport Literal
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-2-3)fromlangchain_core.toolsimport tool
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-2-4)fromlangchain_anthropicimport ChatAnthropic
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-2-5)fromlanggraph.graphimport MessagesState
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-2-6)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-2-7)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-2-8)classWeatherResponse(BaseModel):
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-2-9)"""Respond to the user with this"""
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-2-10)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-2-11)  temperature: float = Field(description="The temperature in fahrenheit")
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-2-12)  wind_directon: str = Field(
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-2-13)    description="The direction of the wind in abbreviated form"
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-2-14)  )
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-2-15)  wind_speed: float = Field(description="The speed of the wind in km/h")
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-2-16)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-2-17)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-2-18)# Inherit 'messages' key from MessagesState, which is a list of chat messages
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-2-19)classAgentState(MessagesState):
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-2-20)  # Final structured response from the agent
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-2-21)  final_response: WeatherResponse
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-2-22)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-2-23)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-2-24)@tool
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-2-25)defget_weather(city: Literal["nyc", "sf"]):
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-2-26)"""Use this to get weather information."""
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-2-27)  if city == "nyc":
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-2-28)    return "It is cloudy in NYC, with 5 mph winds in the North-East direction and a temperature of 70 degrees"
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-2-29)  elif city == "sf":
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-2-30)    return "It is 75 degrees and sunny in SF, with 3 mph winds in the South-East direction"
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-2-31)  else:
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-2-32)    raise AssertionError("Unknown city")
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-2-33)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-2-34)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-2-35)tools = [get_weather]
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-2-36)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-2-37)model = ChatAnthropic(model="claude-3-opus-20240229")
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-2-38)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-2-39)model_with_tools = model.bind_tools(tools)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-2-40)model_with_structured_output = model.with_structured_output(WeatherResponse)

```


API Reference: [tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html) | [ChatAnthropic](https://python.langchain.com/api_reference/anthropic/chat_models/langchain_anthropic.chat_models.ChatAnthropic.html)

## Option 1: Bind output as tool[¶](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#option-1-bind-output-as-tool "Permanent link")

Let's now examine how we would use the single LLM option.

### Define Graph[¶](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#define-graph "Permanent link")

The graph definition is very similar to the one above, the only difference is we no longer call an LLM in the `response` node, and instead bind the `WeatherResponse` tool to our LLM that already contains the `get_weather` tool.

```
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-1)fromlanggraph.graphimport StateGraph, END
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-2)fromlanggraph.prebuiltimport ToolNode
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-3)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-4)tools = [get_weather, WeatherResponse]
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-5)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-6)# Force the model to use tools by passing tool_choice="any"
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-7)model_with_response_tool = model.bind_tools(tools, tool_choice="any")
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-8)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-9)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-10)# Define the function that calls the model
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-11)defcall_model(state: AgentState):
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-12)  response = model_with_response_tool.invoke(state["messages"])
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-13)  # We return a list, because this will get added to the existing list
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-14)  return {"messages": [response]}
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-15)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-16)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-17)# Define the function that responds to the user
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-18)defrespond(state: AgentState):
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-19)  # Construct the final answer from the arguments of the last tool call
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-20)  weather_tool_call = state["messages"][-1].tool_calls[0]
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-21)  response = WeatherResponse(**weather_tool_call["args"])
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-22)  # Since we're using tool calling to return structured output,
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-23)  # we need to add a tool message corresponding to the WeatherResponse tool call,
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-24)  # This is due to LLM providers' requirement that AI messages with tool calls
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-25)  # need to be followed by a tool message for each tool call
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-26)  tool_message = {
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-27)    "type": "tool",
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-28)    "content": "Here is your structured response",
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-29)    "tool_call_id": weather_tool_call["id"],
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-30)  }
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-31)  # We return the final answer
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-32)  return {"final_response": response, "messages": [tool_message]}
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-33)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-34)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-35)# Define the function that determines whether to continue or not
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-36)defshould_continue(state: AgentState):
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-37)  messages = state["messages"]
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-38)  last_message = messages[-1]
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-39)  # If there is only one tool call and it is the response tool call we respond to the user
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-40)  if (
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-41)    len(last_message.tool_calls) == 1
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-42)    and last_message.tool_calls[0]["name"] == "WeatherResponse"
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-43)  ):
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-44)    return "respond"
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-45)  # Otherwise we will use the tool node again
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-46)  else:
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-47)    return "continue"
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-48)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-49)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-50)# Define a new graph
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-51)workflow = StateGraph(AgentState)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-52)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-53)# Define the two nodes we will cycle between
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-54)workflow.add_node("agent", call_model)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-55)workflow.add_node("respond", respond)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-56)workflow.add_node("tools", ToolNode(tools))
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-57)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-58)# Set the entrypoint as `agent`
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-59)# This means that this node is the first one called
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-60)workflow.set_entry_point("agent")
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-61)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-62)# We now add a conditional edge
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-63)workflow.add_conditional_edges(
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-64)  "agent",
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-65)  should_continue,
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-66)  {
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-67)    "continue": "tools",
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-68)    "respond": "respond",
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-69)  },
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-70))
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-71)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-72)workflow.add_edge("tools", "agent")
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-73)workflow.add_edge("respond", END)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-3-74)graph = workflow.compile()

```


API Reference: [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END) | [ToolNode](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.ToolNode)

### Usage[¶](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#usage "Permanent link")

Now we can run our graph to check that it worked as intended:

```
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-4-1)answer = graph.invoke(input={"messages": [("human", "what's the weather in SF?")]})[
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-4-2)  "final_response"
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-4-3)]

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-5-1)answer

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-6-1)WeatherResponse(temperature=75.0, wind_directon='SE', wind_speed=3.0)

```


Again, the agent returned a `WeatherResponse` object as we expected.

## Option 2: 2 LLMs[¶](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#option-2-2-llms "Permanent link")

Let's now dive into how we would use a second LLM to force structured output.

### Define Graph[¶](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#define-graph_1 "Permanent link")

We can now define our graph:

```
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-1)fromlanggraph.graphimport StateGraph, END
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-2)fromlanggraph.prebuiltimport ToolNode
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-3)fromlangchain_core.messagesimport HumanMessage
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-4)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-5)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-6)# Define the function that calls the model
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-7)defcall_model(state: AgentState):
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-8)  response = model_with_tools.invoke(state["messages"])
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-9)  # We return a list, because this will get added to the existing list
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-10)  return {"messages": [response]}
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-11)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-12)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-13)# Define the function that responds to the user
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-14)defrespond(state: AgentState):
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-15)  # We call the model with structured output in order to return the same format to the user every time
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-16)  # state['messages'][-2] is the last ToolMessage in the convo, which we convert to a HumanMessage for the model to use
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-17)  # We could also pass the entire chat history, but this saves tokens since all we care to structure is the output of the tool
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-18)  response = model_with_structured_output.invoke(
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-19)    [HumanMessage(content=state["messages"][-2].content)]
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-20)  )
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-21)  # We return the final answer
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-22)  return {"final_response": response}
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-23)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-24)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-25)# Define the function that determines whether to continue or not
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-26)defshould_continue(state: AgentState):
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-27)  messages = state["messages"]
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-28)  last_message = messages[-1]
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-29)  # If there is no function call, then we respond to the user
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-30)  if not last_message.tool_calls:
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-31)    return "respond"
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-32)  # Otherwise if there is, we continue
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-33)  else:
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-34)    return "continue"
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-35)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-36)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-37)# Define a new graph
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-38)workflow = StateGraph(AgentState)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-39)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-40)# Define the two nodes we will cycle between
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-41)workflow.add_node("agent", call_model)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-42)workflow.add_node("respond", respond)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-43)workflow.add_node("tools", ToolNode(tools))
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-44)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-45)# Set the entrypoint as `agent`
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-46)# This means that this node is the first one called
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-47)workflow.set_entry_point("agent")
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-48)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-49)# We now add a conditional edge
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-50)workflow.add_conditional_edges(
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-51)  "agent",
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-52)  should_continue,
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-53)  {
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-54)    "continue": "tools",
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-55)    "respond": "respond",
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-56)  },
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-57))
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-58)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-59)workflow.add_edge("tools", "agent")
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-60)workflow.add_edge("respond", END)
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-7-61)graph = workflow.compile()

```


API Reference: [HumanMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.human.HumanMessage.html) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END) | [ToolNode](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.ToolNode)

### Usage[¶](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#usage_1 "Permanent link")

We can now invoke our graph to verify that the output is being structured as desired:

```
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-8-1)answer = graph.invoke(input={"messages": [("human", "what's the weather in SF?")]})[
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-8-2)  "final_response"
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-8-3)]

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-9-1)answer

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__codelineno-10-1)WeatherResponse(temperature=75.0, wind_directon='SE', wind_speed=4.83)

```


As we can see, the agent returned a `WeatherResponse` object as we expected. If would now be easy to use this agent in a more complex software stack without having to worry about the output of the agent not matching the format expected from the next step in the stack.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to run a graph asynchronously  ](https://langchain-ai.github.io/langgraph/how-tos/async/) [ Next  How to pass custom run ID or set tags and metadata for graph runs in LangSmith  ](https://langchain-ai.github.io/langgraph/how-tos/run-id-langsmith/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
