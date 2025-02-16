---
url: https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#how-to-handle-tool-calling-errors)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to handle tool calling errors 

[ ](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/?q= "Share")

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
          * Tool calling  Tool calling 
            * [ Tool calling  ](https://langchain-ai.github.io/langgraph/how-tos#tool-calling)
            * [ How to call tools using ToolNode  ](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/)
            * How to handle tool calling errors  [ How to handle tool calling errors  ](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#setup)
              * [ Using the prebuilt ToolNode  ](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#using-the-prebuilt-toolnode)
              * [ Custom strategies  ](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#custom-strategies)
              * [ Next steps  ](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#next-steps)
            * [ How to pass runtime values to tools  ](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/)
            * [ How to update graph state from tools  ](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#setup)
  * [ Using the prebuilt ToolNode  ](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#using-the-prebuilt-toolnode)
  * [ Custom strategies  ](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#custom-strategies)
  * [ Next steps  ](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#next-steps)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Tool calling  ](https://langchain-ai.github.io/langgraph/how-tos#tool-calling)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/tool-calling-errors.ipynb "Edit this page")

# How to handle tool calling errors[¶](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#how-to-handle-tool-calling-errors "Permanent link")

Prerequisites

This guide assumes familiarity with the following: 

  * [ Tool calling ](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#tool-calling)
  * [ Deleting messages ](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/)



LLMs aren't perfect at calling tools. The model may try to call a tool that doesn't exist or fail to return arguments that match the requested schema. Strategies like keeping schemas simple, reducing the number of tools you pass at once, and having good names and descriptions can help mitigate this risk, but aren't foolproof.

This guide covers some ways to build error handling into your graphs to mitigate these failure modes.

## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#setup "Permanent link")

First, let's install the required packages and set our API keys

```
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-0-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-0-2)%pip install --quiet -U langgraph langchain_anthropic

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-1-1)importgetpass
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-1-2)importos
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-1-5)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-1-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-1-7)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-1-8)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-1-10)_set_env("ANTHROPIC_API_KEY")

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Using the prebuilt `ToolNode`[¶](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#using-the-prebuilt-toolnode "Permanent link")

To start, define a mock weather tool that has some hidden restrictions on input queries. The intent here is to simulate a real-world case where a model fails to call a tool correctly:

```
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-2-1)fromlangchain_core.toolsimport tool
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-2-2)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-2-3)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-2-4)@tool
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-2-5)defget_weather(location: str):
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-2-6)"""Call to get the current weather."""
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-2-7)  if location == "san francisco":
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-2-8)    raise ValueError("Input queries must be proper nouns")
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-2-9)  elif location == "San Francisco":
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-2-10)    return "It's 60 degrees and foggy."
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-2-11)  else:
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-2-12)    raise ValueError("Invalid input.")

```


API Reference: [tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html)

Next, set up a graph implementation of the [ReAct agent](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#react-agent). This agent takes some query as input, then repeatedly call tools until it has enough information to resolve the query. We'll use the prebuilt `ToolNode`[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#toolnode) to execute called tools, and a small, fast model powered by Anthropic:

```
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-3-1)fromtypingimport Literal
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-3-2)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-3-3)fromlangchain_anthropicimport ChatAnthropic
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-3-4)fromlanggraph.graphimport StateGraph, MessagesState, START, END
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-3-5)fromlanggraph.prebuiltimport ToolNode
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-3-6)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-3-7)tool_node = ToolNode([get_weather])
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-3-8)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-3-9)model_with_tools = ChatAnthropic(
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-3-10)  model="claude-3-haiku-20240307", temperature=0
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-3-11)).bind_tools([get_weather])
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-3-12)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-3-13)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-3-14)defshould_continue(state: MessagesState):
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-3-15)  messages = state["messages"]
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-3-16)  last_message = messages[-1]
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-3-17)  if last_message.tool_calls:
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-3-18)    return "tools"
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-3-19)  return END
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-3-20)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-3-21)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-3-22)defcall_model(state: MessagesState):
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-3-23)  messages = state["messages"]
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-3-24)  response = model_with_tools.invoke(messages)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-3-25)  return {"messages": [response]}
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-3-26)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-3-27)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-3-28)workflow = StateGraph(MessagesState)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-3-29)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-3-30)# Define the two nodes we will cycle between
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-3-31)workflow.add_node("agent", call_model)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-3-32)workflow.add_node("tools", tool_node)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-3-33)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-3-34)workflow.add_edge(START, "agent")
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-3-35)workflow.add_conditional_edges("agent", should_continue, ["tools", END])
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-3-36)workflow.add_edge("tools", "agent")
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-3-37)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-3-38)app = workflow.compile()

```


API Reference: [ChatAnthropic](https://python.langchain.com/api_reference/anthropic/chat_models/langchain_anthropic.chat_models.ChatAnthropic.html) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END) | [ToolNode](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.ToolNode)

```
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-4-1)fromIPython.displayimport Image, display
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-4-2)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-4-3)try:
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-4-4)  display(Image(app.get_graph().draw_mermaid_png()))
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-4-5)except Exception:
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-4-6)  # This requires some extra dependencies and is optional
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-4-7)  pass

```


![]()

When you try to call the tool, you can see that the model calls the tool with a bad input, causing the tool to throw an error. The prebuilt `ToolNode` that executes the tool has some built-in error handling that captures the error and passes it back to the model so that it can try again:

```
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-5-1)response = app.invoke(
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-5-2)  {"messages": [("human", "what is the weather in san francisco?")]},
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-5-3))
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-5-4)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-5-5)for message in response["messages"]:
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-5-6)  string_representation = f"{message.type.upper()}: {message.content}\n"
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-5-7)  print(string_representation)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-6-1)HUMAN: what is the weather in san francisco?
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-6-2)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-6-3)AI: [{'id': 'toolu_01K5tXKVRbETcs7Q8U9PHy96', 'input': {'location': 'san francisco'}, 'name': 'get_weather', 'type': 'tool_use'}]
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-6-4)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-6-5)TOOL: Error: ValueError('Input queries must be proper nouns')
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-6-6) Please fix your mistakes.
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-6-7)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-6-8)AI: [{'text': 'Apologies, it looks like there was an issue with the weather lookup. Let me try that again with the proper format:', 'type': 'text'}, {'id': 'toolu_01KSCsme3Du2NBazSJQ1af4b', 'input': {'location': 'San Francisco'}, 'name': 'get_weather', 'type': 'tool_use'}]
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-6-9)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-6-10)TOOL: It's 60 degrees and foggy.
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-6-11)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-6-12)AI: The current weather in San Francisco is 60 degrees and foggy.

```


## Custom strategies[¶](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#custom-strategies "Permanent link")

This is a fine default in many cases, but there are cases where custom fallbacks may be better.

For example, the below tool requires as input a list of elements of a specific length - tricky for a small model! We'll also intentionally avoid pluralizing `topic` to trick the model into thinking it should pass a string:

```
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-1)fromlangchain_core.output_parsersimport StrOutputParser
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-2)frompydanticimport BaseModel, Field
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-3)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-4)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-5)classHaikuRequest(BaseModel):
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-6)  topic: list[str] = Field(
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-7)    max_length=3,
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-8)    min_length=3,
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-9)  )
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-10)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-11)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-12)@tool
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-13)defmaster_haiku_generator(request: HaikuRequest):
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-14)"""Generates a haiku based on the provided topics."""
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-15)  model = ChatAnthropic(model="claude-3-haiku-20240307", temperature=0)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-16)  chain = model | StrOutputParser()
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-17)  topics = ", ".join(request.topic)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-18)  haiku = chain.invoke(f"Write a haiku about {topics}")
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-19)  return haiku
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-20)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-21)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-22)tool_node = ToolNode([master_haiku_generator])
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-23)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-24)model = ChatAnthropic(model="claude-3-haiku-20240307", temperature=0)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-25)model_with_tools = model.bind_tools([master_haiku_generator])
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-26)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-27)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-28)defshould_continue(state: MessagesState):
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-29)  messages = state["messages"]
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-30)  last_message = messages[-1]
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-31)  if last_message.tool_calls:
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-32)    return "tools"
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-33)  return END
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-34)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-35)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-36)defcall_model(state: MessagesState):
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-37)  messages = state["messages"]
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-38)  response = model_with_tools.invoke(messages)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-39)  return {"messages": [response]}
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-40)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-41)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-42)workflow = StateGraph(MessagesState)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-43)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-44)# Define the two nodes we will cycle between
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-45)workflow.add_node("agent", call_model)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-46)workflow.add_node("tools", tool_node)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-47)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-48)workflow.add_edge(START, "agent")
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-49)workflow.add_conditional_edges("agent", should_continue, ["tools", END])
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-50)workflow.add_edge("tools", "agent")
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-51)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-52)app = workflow.compile()
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-53)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-54)response = app.invoke(
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-55)  {"messages": [("human", "Write me an incredible haiku about water.")]},
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-56)  {"recursion_limit": 10},
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-57))
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-58)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-59)for message in response["messages"]:
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-60)  string_representation = f"{message.type.upper()}: {message.content}\n"
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-7-61)  print(string_representation)

```


API Reference: [StrOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.string.StrOutputParser.html)

```
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-8-1)HUMAN: Write me an incredible haiku about water.
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-8-2)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-8-3)AI: [{'text': 'Here is a haiku about water:', 'type': 'text'}, {'id': 'toolu_01L13Z3Gtaym5KKgPXVyZhYn', 'input': {'topic': ['water']}, 'name': 'master_haiku_generator', 'type': 'tool_use'}]
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-8-4)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-8-5)TOOL: Error: 1 validation error for master_haiku_generator
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-8-6)request
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-8-7) Field required [type=missing, input_value={'topic': ['water']}, input_type=dict]
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-8-8)  For further information visit https://errors.pydantic.dev/2.7/v/missing
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-8-9) Please fix your mistakes.
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-8-10)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-8-11)AI: [{'text': 'Oops, my apologies. Let me try that again with the correct format:', 'type': 'text'}, {'id': 'toolu_01HCQ5uXr5kXQHBQ3FyQ1Ysk', 'input': {'topic': ['water']}, 'name': 'master_haiku_generator', 'type': 'tool_use'}]
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-8-12)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-8-13)TOOL: Error: 1 validation error for master_haiku_generator
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-8-14)request
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-8-15) Field required [type=missing, input_value={'topic': ['water']}, input_type=dict]
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-8-16)  For further information visit https://errors.pydantic.dev/2.7/v/missing
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-8-17) Please fix your mistakes.
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-8-18)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-8-19)AI: [{'text': 'Hmm, it seems there was an issue with the input format. Let me try a different approach:', 'type': 'text'}, {'id': 'toolu_01RF96nruwr4nMqhLBRsbfE5', 'input': {'request': {'topic': ['water']}}, 'name': 'master_haiku_generator', 'type': 'tool_use'}]
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-8-20)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-8-21)TOOL: Error: 1 validation error for master_haiku_generator
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-8-22)request.topic
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-8-23) List should have at least 3 items after validation, not 1 [type=too_short, input_value=['water'], input_type=list]
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-8-24)  For further information visit https://errors.pydantic.dev/2.7/v/too_short
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-8-25) Please fix your mistakes.
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-8-26)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-8-27)AI: [{'text': 'Ah I see, the haiku generator requires at least 3 topics. Let me provide 3 topics related to water:', 'type': 'text'}, {'id': 'toolu_011jcgHuG2Kyr87By459huqQ', 'input': {'request': {'topic': ['ocean', 'rain', 'river']}}, 'name': 'master_haiku_generator', 'type': 'tool_use'}]
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-8-28)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-8-29)TOOL: Here is a haiku about ocean, rain, and river:
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-8-30)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-8-31)Vast ocean's embrace,
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-8-32)Raindrops caress the river,
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-8-33)Nature's symphony.
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-8-34)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-8-35)AI: I hope this haiku about water captures the essence you were looking for! Let me know if you would like me to generate another one.

```


We can see that the model takes two tries to get the input correct. 

A better strategy might be to trim the failed attempt to reduce distraction, then fall back to a more advanced model. Here's an example. We also use a custom-built node to call our tools instead of the prebuilt `ToolNode`:

```
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-1)importjson
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-2)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-3)fromlangchain_core.messagesimport AIMessage, ToolMessage
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-4)fromlangchain_core.messages.modifierimport RemoveMessage
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-5)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-6)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-7)@tool
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-8)defmaster_haiku_generator(request: HaikuRequest):
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-9)"""Generates a haiku based on the provided topics."""
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-10)  model = ChatAnthropic(model="claude-3-haiku-20240307", temperature=0)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-11)  chain = model | StrOutputParser()
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-12)  topics = ", ".join(request.topic)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-13)  haiku = chain.invoke(f"Write a haiku about {topics}")
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-14)  return haiku
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-15)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-16)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-17)defcall_tool(state: MessagesState):
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-18)  tools_by_name = {master_haiku_generator.name: master_haiku_generator}
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-19)  messages = state["messages"]
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-20)  last_message = messages[-1]
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-21)  output_messages = []
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-22)  for tool_call in last_message.tool_calls:
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-23)    try:
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-24)      tool_result = tools_by_name[tool_call["name"]].invoke(tool_call["args"])
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-25)      output_messages.append(
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-26)        ToolMessage(
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-27)          content=json.dumps(tool_result),
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-28)          name=tool_call["name"],
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-29)          tool_call_id=tool_call["id"],
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-30)        )
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-31)      )
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-32)    except Exception as e:
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-33)      # Return the error if the tool call fails
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-34)      output_messages.append(
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-35)        ToolMessage(
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-36)          content="",
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-37)          name=tool_call["name"],
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-38)          tool_call_id=tool_call["id"],
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-39)          additional_kwargs={"error": e},
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-40)        )
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-41)      )
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-42)  return {"messages": output_messages}
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-43)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-44)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-45)model = ChatAnthropic(model="claude-3-haiku-20240307", temperature=0)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-46)model_with_tools = model.bind_tools([master_haiku_generator])
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-47)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-48)better_model = ChatAnthropic(model="claude-3-5-sonnet-20240620", temperature=0)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-49)better_model_with_tools = better_model.bind_tools([master_haiku_generator])
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-50)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-51)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-52)defshould_continue(state: MessagesState):
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-53)  messages = state["messages"]
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-54)  last_message = messages[-1]
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-55)  if last_message.tool_calls:
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-56)    return "tools"
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-57)  return END
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-58)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-59)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-60)defshould_fallback(
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-61)  state: MessagesState,
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-62)) -> Literal["agent", "remove_failed_tool_call_attempt"]:
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-63)  messages = state["messages"]
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-64)  failed_tool_messages = [
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-65)    msg
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-66)    for msg in messages
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-67)    if isinstance(msg, ToolMessage)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-68)    and msg.additional_kwargs.get("error") is not None
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-69)  ]
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-70)  if failed_tool_messages:
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-71)    return "remove_failed_tool_call_attempt"
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-72)  return "agent"
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-73)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-74)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-75)defcall_model(state: MessagesState):
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-76)  messages = state["messages"]
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-77)  response = model_with_tools.invoke(messages)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-78)  return {"messages": [response]}
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-79)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-80)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-81)defremove_failed_tool_call_attempt(state: MessagesState):
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-82)  messages = state["messages"]
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-83)  # Remove all messages from the most recent
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-84)  # instance of AIMessage onwards.
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-85)  last_ai_message_index = next(
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-86)    i
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-87)    for i, msg in reversed(list(enumerate(messages)))
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-88)    if isinstance(msg, AIMessage)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-89)  )
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-90)  messages_to_remove = messages[last_ai_message_index:]
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-91)  return {"messages": [RemoveMessage(id=m.id) for m in messages_to_remove]}
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-92)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-93)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-94)# Fallback to a better model if a tool call fails
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-95)defcall_fallback_model(state: MessagesState):
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-96)  messages = state["messages"]
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-97)  response = better_model_with_tools.invoke(messages)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-98)  return {"messages": [response]}
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-99)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-100)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-101)workflow = StateGraph(MessagesState)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-102)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-103)workflow.add_node("agent", call_model)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-104)workflow.add_node("tools", call_tool)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-105)workflow.add_node("remove_failed_tool_call_attempt", remove_failed_tool_call_attempt)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-106)workflow.add_node("fallback_agent", call_fallback_model)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-107)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-108)workflow.add_edge(START, "agent")
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-109)workflow.add_conditional_edges("agent", should_continue, ["tools", END])
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-110)workflow.add_conditional_edges("tools", should_fallback)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-111)workflow.add_edge("remove_failed_tool_call_attempt", "fallback_agent")
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-112)workflow.add_edge("fallback_agent", "tools")
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-113)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-9-114)app = workflow.compile()

```


API Reference: [AIMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.AIMessage.html) | [ToolMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.tool.ToolMessage.html) | [RemoveMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.modifier.RemoveMessage.html)

The `tools` node will now return `ToolMessage`s with an `error` field in `additional_kwargs` if a tool call fails. If that happens, it will go to another node that removes the failed tool messages, and has a better model retry the tool call generation.

The diagram below shows this visually:

```
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-10-1)try:
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-10-2)  display(Image(app.get_graph().draw_mermaid_png()))
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-10-3)except Exception:
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-10-4)  # This requires some extra dependencies and is optional
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-10-5)  pass

```


![]()

Let's try it out. To emphasize the removal steps, let's `stream` the responses from the model so that we can see each executed node:

```
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-11-1)stream = app.stream(
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-11-2)  {"messages": [("human", "Write me an incredible haiku about water.")]},
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-11-3)  {"recursion_limit": 10},
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-11-4))
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-11-5)
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-11-6)for chunk in stream:
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-11-7)  print(chunk)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-12-1){'agent': {'messages': [AIMessage(content=[{'text': 'Here is a haiku about water:', 'type': 'text'}, {'id': 'toolu_019mY8NX4t7YkJBWeHG6jE4T', 'input': {'topic': ['water']}, 'name': 'master_haiku_generator', 'type': 'tool_use'}], additional_kwargs={}, response_metadata={'id': 'msg_01RmoaLh38DnRX2fv7E8vCFh', 'model': 'claude-3-haiku-20240307', 'stop_reason': 'tool_use', 'stop_sequence': None, 'usage': {'input_tokens': 384, 'output_tokens': 67}}, id='run-a1511215-1a62-49b5-b5b3-b2c8f8c7920e-0', tool_calls=[{'name': 'master_haiku_generator', 'args': {'topic': ['water']}, 'id': 'toolu_019mY8NX4t7YkJBWeHG6jE4T', 'type': 'tool_call'}], usage_metadata={'input_tokens': 384, 'output_tokens': 67, 'total_tokens': 451})]}}
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-12-2){'tools': {'messages': [ToolMessage(content='', name='master_haiku_generator', id='69f85339-dbc2-4341-8c4d-26300dfe31a5', tool_call_id='toolu_019mY8NX4t7YkJBWeHG6jE4T')]}}
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-12-3){'remove_failed_tool_call_attempt': {'messages': [RemoveMessage(content='', additional_kwargs={}, response_metadata={}, id='run-a1511215-1a62-49b5-b5b3-b2c8f8c7920e-0'), RemoveMessage(content='', additional_kwargs={}, response_metadata={}, id='69f85339-dbc2-4341-8c4d-26300dfe31a5')]}}
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-12-4){'fallback_agent': {'messages': [AIMessage(content=[{'text': 'Certainly! I\'d be happy to help you create an incredible haiku about water. To do this, I\'ll use the master_haiku_generator function, which requires three topics. Since you\'ve specified water as the main theme, I\'ll add two related concepts to create a more vivid and interesting haiku. Let\'s use "water," "flow," and "reflection" as our three topics.', 'type': 'text'}, {'id': 'toolu_01FxSxy8LeQ5PjdNYq8vLFTd', 'input': {'request': {'topic': ['water', 'flow', 'reflection']}}, 'name': 'master_haiku_generator', 'type': 'tool_use'}], additional_kwargs={}, response_metadata={'id': 'msg_01U5HV3pt1NVm6syGbxx29no', 'model': 'claude-3-5-sonnet-20240620', 'stop_reason': 'tool_use', 'stop_sequence': None, 'usage': {'input_tokens': 414, 'output_tokens': 158}}, id='run-3eb746c7-b607-4ad3-881a-1c11a7638af7-0', tool_calls=[{'name': 'master_haiku_generator', 'args': {'request': {'topic': ['water', 'flow', 'reflection']}}, 'id': 'toolu_01FxSxy8LeQ5PjdNYq8vLFTd', 'type': 'tool_call'}], usage_metadata={'input_tokens': 414, 'output_tokens': 158, 'total_tokens': 572})]}}
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-12-5){'tools': {'messages': [ToolMessage(content='"Here is a haiku about water, flow, and reflection:\\n\\nRippling waters flow,\\nMirroring the sky above,\\nTranquil reflection."', name='master_haiku_generator', id='fdfc497d-939a-42c0-8748-31371b98a3a7', tool_call_id='toolu_01FxSxy8LeQ5PjdNYq8vLFTd')]}}
[](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__codelineno-12-6){'agent': {'messages': [AIMessage(content='I hope you enjoy this haiku about the beauty and serenity of water. Please let me know if you would like me to generate another one.', additional_kwargs={}, response_metadata={'id': 'msg_012rXWHapc8tPfBPEonpAT6W', 'model': 'claude-3-haiku-20240307', 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 587, 'output_tokens': 35}}, id='run-ab6d412d-9374-4a4b-950d-6dcc43d87cf5-0', usage_metadata={'input_tokens': 587, 'output_tokens': 35, 'total_tokens': 622})]}}

```


You can see that you get a cleaner response - the more powerful model gets it right on the first try, and the smaller model's failure gets wiped from the graph state. This shorter message history also avoid overpopulating the graph state with attempts. 

You can also inspect this [LangSmith trace](https://smith.langchain.com/public/7ce6f1fe-48c4-400e-9cbe-1de2da6d2800/r), which shows the failed initial call to the smaller model.

## Next steps[¶](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#next-steps "Permanent link")

You've now seen how to implement some strategies to handle tool calling errors.

Next, check out some of the [other LangGraph how-to guides here](https://langchain-ai.github.io/langgraph/how-tos/).

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to call tools using ToolNode  ](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/) [ Next  How to pass runtime values to tools  ](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
