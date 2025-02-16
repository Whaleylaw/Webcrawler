---
url: https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/#how-to-define-inputoutput-schema-for-your-graph)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to define input/output schema for your graph 

[ ](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/?q= "Share")

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
            * [ How to use Pydantic model as graph state  ](https://langchain-ai.github.io/langgraph/how-tos/state-model/)
            * How to define input/output schema for your graph  [ How to define input/output schema for your graph  ](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/#setup)
              * [ Define and use the graph  ](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/#define-and-use-the-graph)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/#setup)
  * [ Define and use the graph  ](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/#define-and-use-the-graph)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ State Management  ](https://langchain-ai.github.io/langgraph/how-tos#state-management)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/input_output_schema.ipynb "Edit this page")

# How to define input/output schema for your graph[¶](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/#how-to-define-inputoutput-schema-for-your-graph "Permanent link")

Prerequisites

This guide assumes familiarity with the following: 

  * [ Multiple Schemas ](https://langchain-ai.github.io/langgraph/concepts/low_level/#multiple-schemas)
  * [ State Graph ](https://langchain-ai.github.io/langgraph/concepts/low_level/#stategraph)



By default, `StateGraph` operates with a single schema, and all nodes are expected to communicate using that schema. However, it's also possible to define distinct input and output schemas for a graph.

When distinct schemas are specified, an internal schema will still be used for communication between nodes. The input schema ensures that the provided input matches the expected structure, while the output schema filters the internal data to return only the relevant information according to the defined output schema.

In this example, we'll see how to define distinct input and output schema.

## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/#setup "Permanent link")

First, let's install the required packages

```
[](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/#__codelineno-0-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/#__codelineno-0-2)%pip install -U langgraph

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Define and use the graph[¶](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/#define-and-use-the-graph "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/#__codelineno-1-1)fromlanggraph.graphimport StateGraph, START, END
[](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/#__codelineno-1-2)fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/#__codelineno-1-5)# Define the schema for the input
[](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/#__codelineno-1-6)classInputState(TypedDict):
[](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/#__codelineno-1-7)  question: str
[](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/#__codelineno-1-8)
[](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/#__codelineno-1-10)# Define the schema for the output
[](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/#__codelineno-1-11)classOutputState(TypedDict):
[](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/#__codelineno-1-12)  answer: str
[](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/#__codelineno-1-13)
[](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/#__codelineno-1-14)
[](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/#__codelineno-1-15)# Define the overall schema, combining both input and output
[](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/#__codelineno-1-16)classOverallState(InputState, OutputState):
[](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/#__codelineno-1-17)  pass
[](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/#__codelineno-1-18)
[](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/#__codelineno-1-19)
[](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/#__codelineno-1-20)# Define the node that processes the input and generates an answer
[](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/#__codelineno-1-21)defanswer_node(state: InputState):
[](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/#__codelineno-1-22)  # Example answer and an extra key
[](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/#__codelineno-1-23)  return {"answer": "bye", "question": state["question"]}
[](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/#__codelineno-1-24)
[](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/#__codelineno-1-25)
[](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/#__codelineno-1-26)# Build the graph with input and output schemas specified
[](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/#__codelineno-1-27)builder = StateGraph(OverallState, input=InputState, output=OutputState)
[](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/#__codelineno-1-28)builder.add_node(answer_node) # Add the answer node
[](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/#__codelineno-1-29)builder.add_edge(START, "answer_node") # Define the starting edge
[](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/#__codelineno-1-30)builder.add_edge("answer_node", END) # Define the ending edge
[](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/#__codelineno-1-31)graph = builder.compile() # Compile the graph
[](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/#__codelineno-1-32)
[](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/#__codelineno-1-33)# Invoke the graph with an input and print the result
[](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/#__codelineno-1-34)print(graph.invoke({"question": "hi"}))

```


API Reference: [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END)

```
[](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/#__codelineno-2-1){'answer': 'bye'}

```


Notice that the output of invoke only includes the output schema.  Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to use Pydantic model as graph state  ](https://langchain-ai.github.io/langgraph/how-tos/state-model/) [ Next  How to pass private state between nodes  ](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
