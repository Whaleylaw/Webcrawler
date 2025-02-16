---
url: https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#rebuild-graph-at-runtime)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Rebuild Graph at Runtime 

[ ](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/?q= "Share")

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
        * [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
        * LangGraph Platform  LangGraph Platform 
          * [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph-platform)
          * Application Structure  Application Structure 
            * [ Application Structure  ](https://langchain-ai.github.io/langgraph/how-tos#application-structure)
            * [ How to Set Up a LangGraph Application for Deployment  ](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/)
            * [ How to Set Up a LangGraph Application for Deployment  ](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_pyproject/)
            * [ How to Set Up a LangGraph.js Application for Deployment  ](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/)
            * [ How to add semantic search to your LangGraph deployment  ](https://langchain-ai.github.io/langgraph/cloud/deployment/semantic_search/)
            * [ How to customize Dockerfile  ](https://langchain-ai.github.io/langgraph/cloud/deployment/custom_docker/)
            * [ How to test a LangGraph app locally  ](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/)
            * Rebuild Graph at Runtime  [ Rebuild Graph at Runtime  ](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/) Table of contents 
              * [ Prerequisites  ](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#prerequisites)
              * [ Define graphs  ](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#define-graphs)
                * [ No rebuild  ](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#no-rebuild)
                * [ Rebuild  ](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#rebuild)
            * [ How to use LangGraph Platform to deploy CrewAI, AutoGen, and other frameworks  ](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/)
          * [ Deployment  ](https://langchain-ai.github.io/langgraph/how-tos#deployment)
          * [ Authentication & Access Control  ](https://langchain-ai.github.io/langgraph/how-tos#authentication-access-control)
          * [ Assistants  ](https://langchain-ai.github.io/langgraph/how-tos#assistants)
          * [ Threads  ](https://langchain-ai.github.io/langgraph/how-tos#threads)
          * [ Runs  ](https://langchain-ai.github.io/langgraph/how-tos#runs)
          * [ Streaming  ](https://langchain-ai.github.io/langgraph/how-tos#streaming_1)
          * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraph/how-tos#human-in-the-loop_1)
          * [ Double-texting  ](https://langchain-ai.github.io/langgraph/how-tos#double-texting)
          * [ Webhooks  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/webhooks/)
          * [ Cron Jobs  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/cron_jobs/)
          * [ LangGraph Studio  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph-studio)
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

  * [ Prerequisites  ](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#prerequisites)
  * [ Define graphs  ](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#define-graphs)
    * [ No rebuild  ](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#no-rebuild)
    * [ Rebuild  ](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#rebuild)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph-platform)
  5. [ Application Structure  ](https://langchain-ai.github.io/langgraph/how-tos#application-structure)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/cloud/deployment/graph_rebuild.md "Edit this page")

# Rebuild Graph at Runtime[¶](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#rebuild-graph-at-runtime "Permanent link")

You might need to rebuild your graph with a different configuration for a new run. For example, you might need to use a different graph state or graph structure depending on the config. This guide shows how you can do this.

Note

In most cases, customizing behavior based on the config should be handled by a single graph where each node can read a config and change its behavior based on it

## Prerequisites[¶](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#prerequisites "Permanent link")

Make sure to check out [this how-to guide](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/) on setting up your app for deployment first.

## Define graphs[¶](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#define-graphs "Permanent link")

Let's say you have an app with a simple graph that calls an LLM and returns the response to the user. The app file directory looks like the following:

```
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-0-1)my-app/
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-0-2)|-- requirements.txt
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-0-3)|-- .env
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-0-4)|-- openai_agent.py   # code for your graph

```


where the graph is defined in `openai_agent.py`. 

### No rebuild[¶](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#no-rebuild "Permanent link")

In the standard LangGraph API configuration, the server uses the compiled graph instance that's defined at the top level of `openai_agent.py`, which looks like the following:

```
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-1-1)fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-1-2)fromlanggraph.graphimport END, START, MessageGraph
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-1-4)model = ChatOpenAI(temperature=0)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-1-5)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-1-6)graph_workflow = MessageGraph()
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-1-7)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-1-8)graph_workflow.add_node("agent", model)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-1-9)graph_workflow.add_edge("agent", END)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-1-10)graph_workflow.add_edge(START, "agent")
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-1-11)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-1-12)agent = graph_workflow.compile()

```


API Reference: [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html) | [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START)

To make the server aware of your graph, you need to specify a path to the variable that contains the `CompiledStateGraph` instance in your LangGraph API configuration (`langgraph.json`), e.g.:

```
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-2-1){
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-2-2)  "dependencies": ["."],
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-2-3)  "graphs": {
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-2-4)    "openai_agent": "./openai_agent.py:agent",
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-2-5)  },
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-2-6)  "env": "./.env"
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-2-7)}

```


### Rebuild[¶](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#rebuild "Permanent link")

To make your graph rebuild on each new run with custom configuration, you need to rewrite `openai_agent.py` to instead provide a _function_ that takes a config and returns a graph (or compiled graph) instance. Let's say we want to return our existing graph for user ID '1', and a tool-calling agent for other users. We can modify `openai_agent.py` as follows:

```
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-1)fromtypingimport Annotated
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-2)fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-3)fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-4)fromlanggraph.graphimport END, START, MessageGraph
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-5)fromlanggraph.graph.stateimport StateGraph
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-6)fromlanggraph.graph.messageimport add_messages
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-7)fromlanggraph.prebuiltimport ToolNode
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-8)fromlangchain_core.toolsimport tool
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-9)fromlangchain_core.messagesimport BaseMessage
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-10)fromlangchain_core.runnablesimport RunnableConfig
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-11)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-12)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-13)classState(TypedDict):
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-14)  messages: Annotated[list[BaseMessage], add_messages]
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-15)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-16)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-17)model = ChatOpenAI(temperature=0)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-18)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-19)defmake_default_graph():
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-20)"""Make a simple LLM agent"""
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-21)  graph_workflow = StateGraph(State)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-22)  defcall_model(state):
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-23)    return {"messages": [model.invoke(state["messages"])]}
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-24)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-25)  graph_workflow.add_node("agent", call_model)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-26)  graph_workflow.add_edge("agent", END)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-27)  graph_workflow.add_edge(START, "agent")
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-28)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-29)  agent = graph_workflow.compile()
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-30)  return agent
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-31)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-32)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-33)defmake_alternative_graph():
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-34)"""Make a tool-calling agent"""
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-35)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-36)  @tool
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-37)  defadd(a: float, b: float):
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-38)"""Adds two numbers."""
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-39)    return a + b
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-40)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-41)  tool_node = ToolNode([add])
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-42)  model_with_tools = model.bind_tools([add])
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-43)  defcall_model(state):
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-44)    return {"messages": [model_with_tools.invoke(state["messages"])]}
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-45)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-46)  defshould_continue(state: State):
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-47)    if state["messages"][-1].tool_calls:
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-48)      return "tools"
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-49)    else:
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-50)      return END
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-51)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-52)  graph_workflow = StateGraph(State)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-53)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-54)  graph_workflow.add_node("agent", call_model)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-55)  graph_workflow.add_node("tools", tool_node)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-56)  graph_workflow.add_edge("tools", "agent")
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-57)  graph_workflow.add_edge(START, "agent")
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-58)  graph_workflow.add_conditional_edges("agent", should_continue)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-59)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-60)  agent = graph_workflow.compile()
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-61)  return agent
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-62)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-63)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-64)# this is the graph making function that will decide which graph to
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-65)# build based on the provided config
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-66)defmake_graph(config: RunnableConfig):
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-67)  user_id = config.get("configurable", {}).get("user_id")
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-68)  # route to different graph state / structure based on the user ID
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-69)  if user_id == "1":
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-70)    return make_default_graph()
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-71)  else:
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-3-72)    return make_alternative_graph()

```


API Reference: [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html) | [tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html) | [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html) | [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html) | [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [add_messages](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.message.add_messages) | [ToolNode](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.ToolNode)

Finally, you need to specify the path to your graph-making function (`make_graph`) in `langgraph.json`:

```
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-4-1){
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-4-2)  "dependencies": ["."],
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-4-3)  "graphs": {
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-4-4)    "openai_agent": "./openai_agent.py:make_graph",
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-4-5)  },
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-4-6)  "env": "./.env"
[](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__codelineno-4-7)}

```


See more info on LangGraph API configuration file [here](https://langchain-ai.github.io/langgraph/cloud/reference/cli/#configuration-file)

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to test a LangGraph app locally  ](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/) [ Next  How to use LangGraph Platform to deploy CrewAI, AutoGen, and other frameworks  ](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
