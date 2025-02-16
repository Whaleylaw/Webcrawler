---
url: https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#how-to-pass-private-state-between-nodes)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to pass private state between nodes 

[ ](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/?q= "Share")

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
            * [ How to define input/output schema for your graph  ](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/)
            * How to pass private state between nodes  [ How to pass private state between nodes  ](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#setup)
              * [ Define and use the graph  ](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#define-and-use-the-graph)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#setup)
  * [ Define and use the graph  ](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#define-and-use-the-graph)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ State Management  ](https://langchain-ai.github.io/langgraph/how-tos#state-management)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/pass_private_state.ipynb "Edit this page")

# How to pass private state between nodes[¶](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#how-to-pass-private-state-between-nodes "Permanent link")

Prerequisites

This guide assumes familiarity with the following: 

  * [ Multiple Schemas ](https://langchain-ai.github.io/langgraph/concepts/low_level/#multiple-schemas)



In some cases, you may want nodes to exchange information that is crucial for intermediate logic but doesn’t need to be part of the main schema of the graph. This private data is not relevant to the overall input/output of the graph and should only be shared between certain nodes.

In this how-to guide, we'll create an example sequential graph consisting of three nodes (node_1, node_2 and node_3), where private data is passed between the first two steps (node_1 and node_2), while the third step (node_3) only has access to the public overall state.

## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#setup "Permanent link")

First, let's install the required packages

```
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-0-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-0-2)%pip install -U langgraph

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Define and use the graph[¶](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#define-and-use-the-graph "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-1)fromlanggraph.graphimport StateGraph, START, END
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-2)fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-5)# The overall state of the graph (this is the public state shared across nodes)
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-6)classOverallState(TypedDict):
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-7)  a: str
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-8)
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-10)# Output from node_1 contains private data that is not part of the overall state
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-11)classNode1Output(TypedDict):
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-12)  private_data: str
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-13)
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-14)
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-15)# The private data is only shared between node_1 and node_2
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-16)defnode_1(state: OverallState) -> Node1Output:
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-17)  output = {"private_data": "set by node_1"}
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-18)  print(f"Entered node `node_1`:\n\tInput: {state}.\n\tReturned: {output}")
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-19)  return output
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-20)
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-21)
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-22)# Node 2 input only requests the private data available after node_1
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-23)classNode2Input(TypedDict):
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-24)  private_data: str
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-25)
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-26)
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-27)defnode_2(state: Node2Input) -> OverallState:
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-28)  output = {"a": "set by node_2"}
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-29)  print(f"Entered node `node_2`:\n\tInput: {state}.\n\tReturned: {output}")
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-30)  return output
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-31)
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-32)
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-33)# Node 3 only has access to the overall state (no access to private data from node_1)
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-34)defnode_3(state: OverallState) -> OverallState:
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-35)  output = {"a": "set by node_3"}
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-36)  print(f"Entered node `node_3`:\n\tInput: {state}.\n\tReturned: {output}")
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-37)  return output
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-38)
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-39)
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-40)# Build the state graph
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-41)builder = StateGraph(OverallState)
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-42)builder.add_node(node_1) # node_1 is the first node
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-43)builder.add_node(
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-44)  node_2
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-45)) # node_2 is the second node and accepts private data from node_1
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-46)builder.add_node(node_3) # node_3 is the third node and does not see the private data
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-47)builder.add_edge(START, "node_1") # Start the graph with node_1
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-48)builder.add_edge("node_1", "node_2") # Pass from node_1 to node_2
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-49)builder.add_edge(
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-50)  "node_2", "node_3"
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-51)) # Pass from node_2 to node_3 (only overall state is shared)
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-52)builder.add_edge("node_3", END) # End the graph after node_3
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-53)graph = builder.compile()
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-54)
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-55)# Invoke the graph with the initial state
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-56)response = graph.invoke(
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-57)  {
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-58)    "a": "set at start",
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-59)  }
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-60))
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-61)
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-62)print()
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-1-63)print(f"Output of graph invocation: {response}")

```


API Reference: [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END)

```
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-2-1)Entered node `node_1`:
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-2-2)  Input: {'a': 'set at start'}.
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-2-3)  Returned: {'private_data': 'set by node_1'}
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-2-4)Entered node `node_2`:
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-2-5)  Input: {'private_data': 'set by node_1'}.
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-2-6)  Returned: {'a': 'set by node_2'}
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-2-7)Entered node `node_3`:
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-2-8)  Input: {'a': 'set by node_2'}.
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-2-9)  Returned: {'a': 'set by node_3'}
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-2-10)
[](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__codelineno-2-11)Output of graph invocation: {'a': 'set by node_3'}

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to define input/output schema for your graph  ](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/) [ Next  How to run a graph asynchronously  ](https://langchain-ai.github.io/langgraph/how-tos/async/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/pass_private_state/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
