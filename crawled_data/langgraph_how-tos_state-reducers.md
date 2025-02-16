---
url: https://langchain-ai.github.io/langgraph/how-tos/state-reducers/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#how-to-update-graph-state-from-nodes)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to update graph state from nodes 

[ ](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/?q= "Share")

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
          * Graph API Basics  Graph API Basics 
            * [ Graph API Basics  ](https://langchain-ai.github.io/langgraph/how-tos#graph-api-basics)
            * How to update graph state from nodes  [ How to update graph state from nodes  ](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#setup)
              * [ Example graph  ](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#example-graph)
                * [ Define state  ](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#define-state)
                * [ Define graph structure  ](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#define-graph-structure)
                * [ Use graph  ](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#use-graph)
              * [ Process state updates with reducers  ](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#process-state-updates-with-reducers)
                * [ MessagesState  ](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#messagesstate)
              * [ Next steps  ](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#next-steps)
            * [ How to create a sequence of steps  ](https://langchain-ai.github.io/langgraph/how-tos/sequence/)
            * [ How to create branches for parallel node execution  ](https://langchain-ai.github.io/langgraph/how-tos/branching/)
            * [ How to create and control loops  ](https://langchain-ai.github.io/langgraph/how-tos/recursion-limit/)
            * [ How to visualize your graph  ](https://langchain-ai.github.io/langgraph/how-tos/visualization/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#setup)
  * [ Example graph  ](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#example-graph)
    * [ Define state  ](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#define-state)
    * [ Define graph structure  ](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#define-graph-structure)
    * [ Use graph  ](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#use-graph)
  * [ Process state updates with reducers  ](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#process-state-updates-with-reducers)
    * [ MessagesState  ](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#messagesstate)
  * [ Next steps  ](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#next-steps)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Graph API Basics  ](https://langchain-ai.github.io/langgraph/how-tos#graph-api-basics)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/state-reducers.md "Edit this page")

# How to update graph state from nodes[¶](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#how-to-update-graph-state-from-nodes "Permanent link")

This guide demonstrates how to define and update [state](https://langchain-ai.github.io/langgraph/concepts/low_level/#state) in LangGraph. We will demonstrate:

  1. How to use state to define a graph's [schema](https://langchain-ai.github.io/langgraph/concepts/low_level/#schema)
  2. How to use [reducers](https://langchain-ai.github.io/langgraph/concepts/low_level/#reducers) to control how state updates are processed.



We will use [messages](https://langchain-ai.github.io/langgraph/concepts/low_level/#messagesstate) in our examples. This represents a versatile formulation of state for many LLM applications. See our [concepts page](https://langchain-ai.github.io/langgraph/concepts/low_level/#working-with-messages-in-graph-state) for more detail.

## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#setup "Permanent link")

First, let's install langgraph:

```
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-2)%pip install -U langgraph

```


Set up [LangSmith](https://smith.langchain.com) for better debugging

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM aps built with LangGraph — read more about how to get started in the [docs](https://docs.smith.langchain.com). 

## Example graph[¶](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#example-graph "Permanent link")

### Define state[¶](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#define-state "Permanent link")

[State](https://langchain-ai.github.io/langgraph/concepts/low_level/#state) in LangGraph can be a `TypedDict`, `Pydantic` model, or dataclass. Below we will use `TypedDict`. See [this guide](https://langchain-ai.github.io/langgraph/how-tos/state-model/) for detail on using Pydantic.

By default, graphs will have the same input and output schema, and the state determines that schema. See [this guide](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/) for how to define distinct input and output schemas.

Let's consider a simple example:

```
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-1)fromlangchain_core.messagesimport AnyMessage
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-2)fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-3)
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-4)
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-5)classState(TypedDict):
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-6)  messages: list[AnyMessage]
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-7)  extra_field: int

```


This state tracks a list of [message](https://python.langchain.com/docs/concepts/messages/) objects, as well as an extra integer field.

### Define graph structure[¶](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#define-graph-structure "Permanent link")

Let's build an example graph with a single node. Our [node](https://langchain-ai.github.io/langgraph/concepts/low_level/#nodes) is just a Python function that reads our graph's state and makes updates to it. The first argument to this function will always be the state:

```
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-1)fromlangchain_core.messagesimport AIMessage
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-2)
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-3)
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-4)defnode(state: State):
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-5)  messages = state["messages"]
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-6)  new_message = AIMessage("Hello!")
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-7)
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-8)  return {"messages": messages + [new_message], "extra_field": 10}

```


This node simply appends a message to our message list, and populates an extra field.

Important

Nodes should return updates to the state directly, instead of mutating the state.

Let's next define a simple graph containing this node. We use [StateGraph](https://langchain-ai.github.io/langgraph/concepts/low_level/#stategraph) to define a graph that operates on this state. We then use [add_node](https://langchain-ai.github.io/langgraph/concepts/low_level/#messagesstate) populate our graph.

```
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-1)fromlanggraph.graphimport StateGraph
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-2)
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-3)graph_builder = StateGraph(State)
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-4)graph_builder.add_node(node)
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-5)graph_builder.set_entry_point("node")
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-6)graph = graph_builder.compile()

```


LangGraph provides built-in utilities for visualizing your graph. Let's inspect our graph. See [this guide](https://langchain-ai.github.io/langgraph/how-tos/visualization/) for detail on visualization.

```
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-1-1)fromIPython.displayimport Image, display
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-1-2)
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-1-3)display(Image(graph.get_graph().draw_mermaid_png()))

```


![]()

In this case, our graph just executes a single node.

### Use graph[¶](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#use-graph "Permanent link")

Let's proceed with a simple invocation:

```
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-1)fromlangchain_core.messagesimport HumanMessage
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-2)
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-3)result = graph.invoke({"messages": [HumanMessage("Hi")]})
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-4)result

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-1-1){'messages': [HumanMessage(content='Hi', additional_kwargs={}, response_metadata={}),
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-1-2) AIMessage(content='Hello!', additional_kwargs={}, response_metadata={})],
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-1-3) 'extra_field': 10}

```


Note that:

  * We kicked off invocation by updating a single key of the state.
  * We receive the entire state in the invocation result.



For convenience, we frequently inspect the content of [message objects](https://python.langchain.com/docs/concepts/messages/) via pretty-print:

```
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-1)for message in result["messages"]:
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-2)  message.pretty_print()

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-1-1)================================ Human Message =================================
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-1-2)
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-1-3)Hi
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-1-4)================================== Ai Message ==================================
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-1-5)
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-1-6)Hello!

```


## Process state updates with reducers[¶](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#process-state-updates-with-reducers "Permanent link")

Each key in the state can have its own independent [reducer](https://langchain-ai.github.io/langgraph/concepts/low_level/#reducers) function, which controls how updates from nodes are applied. If no reducer function is explicitly specified then it is assumed that all updates to the key should override it.

For `TypedDict` state schemas, we can define reducers by annotating the corresponding field of the state with a reducer function.

In the earlier example, our node updated the `"messages"` key in the state by appending a message to it. Below, we add a reducer to this key, such that updates are automatically appended:

```
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-1)fromtyping_extensionsimport Annotated
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-2)
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-3)
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-4)defadd(left, right):
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-5)"""Can also import `add` from the `operator` built-in."""
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-6)  return left + right
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-7)
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-8)
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-9)classState(TypedDict):
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-10)  messages: Annotated[list[AnyMessage], add]
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-11)  extra_field: int

```


Now our node can be simplified:

```
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-1)defnode(state: State):
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-2)  new_message = AIMessage("Hello!")
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-3)  return {"messages": [new_message], "extra_field": 10}

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-1)fromlanggraph.graphimport START
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-2)
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-3)
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-4)graph = StateGraph(State).add_node(node).add_edge(START, "node").compile()
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-5)
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-6)result = graph.invoke({"messages": [HumanMessage("Hi")]})
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-7)
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-8)for message in result["messages"]:
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-9)  message.pretty_print()

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-1-1)================================ Human Message =================================
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-1-2)
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-1-3)Hi
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-1-4)================================== Ai Message ==================================
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-1-5)
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-1-6)Hello!

```


### MessagesState[¶](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#messagesstate "Permanent link")

In practice, there are additional considerations for updating lists of messages:

  * We may wish to update an existing message in the state.
  * We may want to accept short-hands for [message formats](https://langchain-ai.github.io/langgraph/concepts/low_level/#using-messages-in-your-graph), such as [OpenAI format](https://python.langchain.com/docs/concepts/messages/#openai-format).



LangGraph includes a built-in reducer `add_messages` that handles these considerations:

```
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-1)fromlanggraph.graph.messageimport add_messages
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-2)
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-3)
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-4)classState(TypedDict):
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-5)  messages: Annotated[list[AnyMessage], add_messages]
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-6)  extra_field: int
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-7)
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-8)
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-9)defnode(state: State):
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-10)  new_message = AIMessage("Hello!")
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-11)  return {"messages": [new_message], "extra_field": 10}
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-12)
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-13)
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-14)graph = StateGraph(State).add_node(node).set_entry_point("node").compile()

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-1)input_message = {"role": "user", "content": "Hi"}
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-2)
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-3)result = graph.invoke({"messages": [input_message]})
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-4)
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-5)for message in result["messages"]:
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-6)  message.pretty_print()

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-1-1)================================ Human Message =================================
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-1-2)
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-1-3)Hi
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-1-4)================================== Ai Message ==================================
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-1-5)
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-1-6)Hello!

```


This is a versatile representation of state for applications involving [chat models](https://python.langchain.com/docs/concepts/chat_models/). LangGraph includes a pre-built `MessagesState` for convenience, so that we can have:

```
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-1)fromlanggraph.graphimport MessagesState
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-2)
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-3)
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-4)classState(MessagesState):
[](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__codelineno-0-5)  extra_field: int

```


## Next steps[¶](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#next-steps "Permanent link")

  * Continue with the [Graph API Basics](https://langchain-ai.github.io/langgraph/how-tos/#graph-api-basics) guides.
  * See more detail on [state management](https://langchain-ai.github.io/langgraph/how-tos/#state-management).

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/) [ Next  How to create a sequence of steps  ](https://langchain-ai.github.io/langgraph/how-tos/sequence/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/state-reducers/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
