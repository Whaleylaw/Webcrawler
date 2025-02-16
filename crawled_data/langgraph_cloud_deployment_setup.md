---
url: https://langchain-ai.github.io/langgraph/cloud/deployment/setup/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#how-to-set-up-a-langgraph-application-for-deployment)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to Set Up a LangGraph Application for Deployment 

[ ](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/?q= "Share")

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
            * How to Set Up a LangGraph Application for Deployment  [ How to Set Up a LangGraph Application for Deployment  ](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/) Table of contents 
              * [ Specify Dependencies  ](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#specify-dependencies)
              * [ Specify Environment Variables  ](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#specify-environment-variables)
              * [ Define Graphs  ](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#define-graphs)
              * [ Create LangGraph API Config  ](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#create-langgraph-api-config)
              * [ Next  ](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#next)
            * [ How to Set Up a LangGraph Application for Deployment  ](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_pyproject/)
            * [ How to Set Up a LangGraph.js Application for Deployment  ](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/)
            * [ How to add semantic search to your LangGraph deployment  ](https://langchain-ai.github.io/langgraph/cloud/deployment/semantic_search/)
            * [ How to customize Dockerfile  ](https://langchain-ai.github.io/langgraph/cloud/deployment/custom_docker/)
            * [ How to test a LangGraph app locally  ](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/)
            * [ Rebuild Graph at Runtime  ](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/)
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

  * [ Specify Dependencies  ](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#specify-dependencies)
  * [ Specify Environment Variables  ](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#specify-environment-variables)
  * [ Define Graphs  ](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#define-graphs)
  * [ Create LangGraph API Config  ](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#create-langgraph-api-config)
  * [ Next  ](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#next)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph-platform)
  5. [ Application Structure  ](https://langchain-ai.github.io/langgraph/how-tos#application-structure)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/cloud/deployment/setup.md "Edit this page")

# How to Set Up a LangGraph Application for Deployment[¶](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#how-to-set-up-a-langgraph-application-for-deployment "Permanent link")

A LangGraph application must be configured with a [LangGraph API configuration file](https://langchain-ai.github.io/langgraph/cloud/reference/cli/#configuration-file) in order to be deployed to LangGraph Cloud (or to be self-hosted). This how-to guide discusses the basic steps to setup a LangGraph application for deployment using `requirements.txt` to specify project dependencies.

This walkthrough is based on [this repository](https://github.com/langchain-ai/langgraph-example), which you can play around with to learn more about how to setup your LangGraph application for deployment.

Setup with pyproject.toml

If you prefer using poetry for dependency management, check out [this how-to guide](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_pyproject/) on using `pyproject.toml` for LangGraph Cloud.

Setup with a Monorepo

If you are interested in deploying a graph located inside a monorepo, take a look at [this](https://github.com/langchain-ai/langgraph-example-monorepo) repository for an example of how to do so.

The final repo structure will look something like this:

```
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-0-1)my-app/
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-0-2)├──my_agent# all project code lies within here
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-0-3)│├──utils# utilities for your graph
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-0-4)││├──__init__.py
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-0-5)││├──tools.py# tools for your graph
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-0-6)││├──nodes.py# node functions for you graph
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-0-7)││└──state.py# state definition of your graph
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-0-8)│├──requirements.txt# package dependencies
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-0-9)│├──__init__.py
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-0-10)│└──agent.py# code for constructing your graph
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-0-11)├──.env# environment variables
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-0-12)└──langgraph.json# configuration file for LangGraph

```


After each step, an example file directory is provided to demonstrate how code can be organized.

## Specify Dependencies[¶](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#specify-dependencies "Permanent link")

Dependencies can optionally be specified in one of the following files: `pyproject.toml`, `setup.py`, or `requirements.txt`. If none of these files is created, then dependencies can be specified later in the [LangGraph API configuration file](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#create-langgraph-api-config).

The dependencies below will be included in the image, you can also use them in your code, as long as with a compatible version range:

```
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-1-1)langgraph>=0.2.56,<0.3.0
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-1-2)langgraph-checkpoint>=2.0.5,<3.0
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-1-3)langchain-core>=0.2.38,<0.4.0
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-1-4)langsmith>=0.1.63
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-1-5)orjson>=3.9.7
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-1-6)httpx>=0.25.0
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-1-7)tenacity>=8.0.0
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-1-8)uvicorn>=0.26.0
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-1-9)sse-starlette>=2.1.0
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-1-10)uvloop>=0.18.0
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-1-11)httptools>=0.5.0
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-1-12)jsonschema-rs>=0.16.3
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-1-13)croniter>=1.0.1
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-1-14)structlog>=23.1.0
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-1-15)redis>=5.0.0,<6.0.0

```


Example `requirements.txt` file:

```
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-2-1)langgraph
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-2-2)langchain_anthropic
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-2-3)tavily-python
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-2-4)langchain_community
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-2-5)langchain_openai

```


Example file directory:

```
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-3-1)my-app/
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-3-2)├──my_agent# all project code lies within here
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-3-3)│└──requirements.txt# package dependencies

```


## Specify Environment Variables[¶](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#specify-environment-variables "Permanent link")

Environment variables can optionally be specified in a file (e.g. `.env`). See the [Environment Variables reference](https://langchain-ai.github.io/langgraph/cloud/reference/env_var/) to configure additional variables for a deployment.

Example `.env` file:

```
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-4-1)MY_ENV_VAR_1=foo
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-4-2)MY_ENV_VAR_2=bar
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-4-3)OPENAI_API_KEY=key

```


Example file directory:

```
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-5-1)my-app/
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-5-2)├──my_agent# all project code lies within here
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-5-3)│└──requirements.txt# package dependencies
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-5-4)└──.env# environment variables

```


## Define Graphs[¶](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#define-graphs "Permanent link")

Implement your graphs! Graphs can be defined in a single file or multiple files. Make note of the variable names of each [CompiledGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.graph.CompiledGraph) to be included in the LangGraph application. The variable names will be used later when creating the [LangGraph API configuration file](https://langchain-ai.github.io/langgraph/cloud/reference/cli/#configuration-file).

Example `agent.py` file, which shows how to import from other modules you define (code for the modules is not shown here, please see [this repo](https://github.com/langchain-ai/langgraph-example) to see their implementation):

```
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-6-1)# my_agent/agent.py
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-6-2)fromtypingimport Literal
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-6-3)fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-6-4)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-6-5)fromlanggraph.graphimport StateGraph, END, START
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-6-6)frommy_agent.utils.nodesimport call_model, should_continue, tool_node # import nodes
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-6-7)frommy_agent.utils.stateimport AgentState # import state
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-6-8)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-6-9)# Define the config
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-6-10)classGraphConfig(TypedDict):
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-6-11)  model_name: Literal["anthropic", "openai"]
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-6-12)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-6-13)workflow = StateGraph(AgentState, config_schema=GraphConfig)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-6-14)workflow.add_node("agent", call_model)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-6-15)workflow.add_node("action", tool_node)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-6-16)workflow.add_edge(START, "agent")
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-6-17)workflow.add_conditional_edges(
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-6-18)  "agent",
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-6-19)  should_continue,
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-6-20)  {
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-6-21)    "continue": "action",
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-6-22)    "end": END,
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-6-23)  },
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-6-24))
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-6-25)workflow.add_edge("action", "agent")
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-6-26)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-6-27)graph = workflow.compile()

```


API Reference: [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START)

Assign `CompiledGraph` to Variable

The build process for LangGraph Cloud requires that the `CompiledGraph` object be assigned to a variable at the top-level of a Python module (alternatively, you can provide [a function that creates a graph](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/)).

Example file directory:

```
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-7-1)my-app/
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-7-2)├──my_agent# all project code lies within here
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-7-3)│├──utils# utilities for your graph
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-7-4)││├──__init__.py
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-7-5)││├──tools.py# tools for your graph
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-7-6)││├──nodes.py# node functions for you graph
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-7-7)││└──state.py# state definition of your graph
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-7-8)│├──requirements.txt# package dependencies
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-7-9)│├──__init__.py
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-7-10)│└──agent.py# code for constructing your graph
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-7-11)└──.env# environment variables

```


## Create LangGraph API Config[¶](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#create-langgraph-api-config "Permanent link")

Create a [LangGraph API configuration file](https://langchain-ai.github.io/langgraph/cloud/reference/cli/#configuration-file) called `langgraph.json`. See the [LangGraph CLI reference](https://langchain-ai.github.io/langgraph/cloud/reference/cli/#configuration-file) for detailed explanations of each key in the JSON object of the configuration file.

Example `langgraph.json` file:

```
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-8-1){
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-8-2)"dependencies":["./my_agent"],
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-8-3)"graphs":{
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-8-4)"agent":"./my_agent/agent.py:graph"
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-8-5)},
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-8-6)"env":".env"
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-8-7)}

```


Note that the variable name of the `CompiledGraph` appears at the end of the value of each subkey in the top-level `graphs` key (i.e. `:<variable_name>`).

Configuration Location

The LangGraph API configuration file must be placed in a directory that is at the same level or higher than the Python files that contain compiled graphs and associated dependencies.

Example file directory:

```
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-9-1)my-app/
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-9-2)├──my_agent# all project code lies within here
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-9-3)│├──utils# utilities for your graph
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-9-4)││├──__init__.py
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-9-5)││├──tools.py# tools for your graph
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-9-6)││├──nodes.py# node functions for you graph
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-9-7)││└──state.py# state definition of your graph
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-9-8)│├──requirements.txt# package dependencies
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-9-9)│├──__init__.py
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-9-10)│└──agent.py# code for constructing your graph
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-9-11)├──.env# environment variables
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__codelineno-9-12)└──langgraph.json# configuration file for LangGraph

```


## Next[¶](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#next "Permanent link")

After you setup your project and place it in a github repo, it's time to [deploy your app](https://langchain-ai.github.io/langgraph/cloud/deployment/cloud/).

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to create a ReAct agent from scratch (Functional API)  ](https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch-functional/) [ Next  How to Set Up a LangGraph Application for Deployment  ](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_pyproject/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
