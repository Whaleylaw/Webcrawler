---
url: https://langchain-ai.github.io/langgraph/how-tos/state-model/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/state-model/#how-to-use-pydantic-model-as-graph-state)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to use Pydantic model as graph state 

[ ](https://langchain-ai.github.io/langgraph/how-tos/state-model/?q= "Share")

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
          * State Management  State Management 
            * [ State Management  ](https://langchain-ai.github.io/langgraph/how-tos#state-management)
            * How to use Pydantic model as graph state  [ How to use Pydantic model as graph state  ](https://langchain-ai.github.io/langgraph/how-tos/state-model/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/state-model/#setup)
              * [ Input Validation  ](https://langchain-ai.github.io/langgraph/how-tos/state-model/#input-validation)
              * [ Multiple Nodes  ](https://langchain-ai.github.io/langgraph/how-tos/state-model/#multiple-nodes)
            * [ How to define input/output schema for your graph  ](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/)
            * [ How to pass private state between nodes  ](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/state-model/#setup)
  * [ Input Validation  ](https://langchain-ai.github.io/langgraph/how-tos/state-model/#input-validation)
  * [ Multiple Nodes  ](https://langchain-ai.github.io/langgraph/how-tos/state-model/#multiple-nodes)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ State Management  ](https://langchain-ai.github.io/langgraph/how-tos#state-management)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/state-model.ipynb "Edit this page")

# How to use Pydantic model as graph state[¶](https://langchain-ai.github.io/langgraph/how-tos/state-model/#how-to-use-pydantic-model-as-graph-state "Permanent link")

Prerequisites

This guide assumes familiarity with the following: 

  * [ State ](https://langchain-ai.github.io/langgraph/concepts/low_level/#state)
  * [ Nodes ](https://langchain-ai.github.io/langgraph/concepts/low_level/#nodes)
  * [ Pydantic ](https://github.com/pydantic/pydantic): this is a popular Python library for run time validation. 



A [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.StateGraph) accepts a `state_schema` argument on initialization that specifies the "shape" of the state that the nodes in the graph can access and update.

In our examples, we typically use a python-native `TypedDict` for `state_schema` (or in the case of [MessageGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#messagegraph), a [list](https://docs.python.org/3/library/stdtypes.html#list)), but `state_schema` can be any [type](https://docs.python.org/3/library/stdtypes.html#type-objects).

In this how-to guide, we'll see how a [Pydantic BaseModel](https://docs.pydantic.dev/latest/api/base_model/). can be used for `state_schema` to add run time validation on **inputs**.

Known Limitations

  * This notebook uses Pydantic v2 `BaseModel`, which requires `langchain-core >= 0.3`. Using `langchain-core < 0.3` will result in errors due to mixing of Pydantic v1 and v2 `BaseModels`. 
  * Currently, the `output` of the graph will **NOT** be an instance of a pydantic model. 
  * Run-time validation only occurs on **inputs** into nodes, not on the outputs. 
  * The validation error trace from pydantic does not show which node the error arises in. 



## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/state-model/#setup "Permanent link")

First we need to install the packages required

```
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-0-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-0-2)%pip install --quiet -U langgraph

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-1-1)importgetpass
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-1-2)importos
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-1-5)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-1-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-1-7)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-1-8)
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-1-10)_set_env("OPENAI_API_KEY")

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Input Validation[¶](https://langchain-ai.github.io/langgraph/how-tos/state-model/#input-validation "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-2-1)fromlanggraph.graphimport StateGraph, START, END
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-2-2)fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-2-3)
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-2-4)frompydanticimport BaseModel
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-2-5)
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-2-6)
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-2-7)# The overall state of the graph (this is the public state shared across nodes)
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-2-8)classOverallState(BaseModel):
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-2-9)  a: str
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-2-10)
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-2-11)
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-2-12)defnode(state: OverallState):
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-2-13)  return {"a": "goodbye"}
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-2-14)
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-2-15)
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-2-16)# Build the state graph
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-2-17)builder = StateGraph(OverallState)
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-2-18)builder.add_node(node) # node_1 is the first node
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-2-19)builder.add_edge(START, "node") # Start the graph with node_1
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-2-20)builder.add_edge("node", END) # End the graph after node_1
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-2-21)graph = builder.compile()
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-2-22)
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-2-23)# Test the graph with a valid input
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-2-24)graph.invoke({"a": "hello"})

```


API Reference: [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END)

```
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-3-1){'a': 'goodbye'}

```


Invoke the graph with an **invalid** input

```
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-4-1)try:
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-4-2)  graph.invoke({"a": 123}) # Should be a string
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-4-3)except Exception as e:
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-4-4)  print("An exception was raised because `a` is an integer rather than a string.")
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-4-5)  print(e)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-5-1)An exception was raised because `a` is an integer rather than a string.
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-5-2)1 validation error for OverallState
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-5-3)a
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-5-4) Input should be a valid string [type=string_type, input_value=123, input_type=int]
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-5-5)  For further information visit https://errors.pydantic.dev/2.9/v/string_type

```


## Multiple Nodes[¶](https://langchain-ai.github.io/langgraph/how-tos/state-model/#multiple-nodes "Permanent link")

Run-time validation will also work in a multi-node graph. In the example below `bad_node` updates `a` to an integer. 

Because run-time validation occurs on **inputs** , the validation error will occur when `ok_node` is called (not when `bad_node` returns an update to the state which is inconsistent with the schema).

```
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-6-1)fromlanggraph.graphimport StateGraph, START, END
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-6-2)fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-6-3)
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-6-4)frompydanticimport BaseModel
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-6-5)
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-6-6)
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-6-7)# The overall state of the graph (this is the public state shared across nodes)
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-6-8)classOverallState(BaseModel):
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-6-9)  a: str
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-6-10)
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-6-11)
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-6-12)defbad_node(state: OverallState):
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-6-13)  return {
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-6-14)    "a": 123 # Invalid
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-6-15)  }
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-6-16)
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-6-17)
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-6-18)defok_node(state: OverallState):
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-6-19)  return {"a": "goodbye"}
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-6-20)
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-6-21)
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-6-22)# Build the state graph
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-6-23)builder = StateGraph(OverallState)
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-6-24)builder.add_node(bad_node)
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-6-25)builder.add_node(ok_node)
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-6-26)builder.add_edge(START, "bad_node")
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-6-27)builder.add_edge("bad_node", "ok_node")
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-6-28)builder.add_edge("ok_node", END)
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-6-29)graph = builder.compile()
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-6-30)
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-6-31)# Test the graph with a valid input
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-6-32)try:
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-6-33)  graph.invoke({"a": "hello"})
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-6-34)except Exception as e:
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-6-35)  print("An exception was raised because bad_node sets `a` to an integer.")
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-6-36)  print(e)

```


API Reference: [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END)

```
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-7-1)An exception was raised because bad_node sets `a` to an integer.
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-7-2)1 validation error for OverallState
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-7-3)a
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-7-4) Input should be a valid string [type=string_type, input_value=123, input_type=int]
[](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__codelineno-7-5)  For further information visit https://errors.pydantic.dev/2.9/v/string_type

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to add multi-turn conversation in a multi-agent application (functional API)  ](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo-functional/) [ Next  How to define input/output schema for your graph  ](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/state-model/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
