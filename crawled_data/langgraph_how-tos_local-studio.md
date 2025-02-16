---
url: https://langchain-ai.github.io/langgraph/how-tos/local-studio/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/local-studio/#how-to-connect-a-local-agent-to-langgraph-studio)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to connect a local agent to LangGraph Studio 

[ ](https://langchain-ai.github.io/langgraph/how-tos/local-studio/?q= "Share")

Initializing search 

[ GitHub  ](https://github.com/langchain-ai/langgraph "Go to repository")

  * [ Home ](https://langchain-ai.github.io/langgraph/)
  * [ API reference ](https://langchain-ai.github.io/langgraph/reference/graphs/)



[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

[ GitHub  ](https://github.com/langchain-ai/langgraph "Go to repository")

  * [ Home  ](https://langchain-ai.github.io/langgraph/)
  * [ API reference  ](https://langchain-ai.github.io/langgraph/reference/graphs/)



Table of contents 

  * [ Connection Options  ](https://langchain-ai.github.io/langgraph/how-tos/local-studio/#connection-options)
  * [ Setup your application  ](https://langchain-ai.github.io/langgraph/how-tos/local-studio/#setup-your-application)
  * [ Install langgraph-cli  ](https://langchain-ai.github.io/langgraph/how-tos/local-studio/#install-langgraph-cli)
  * [ Run the development server  ](https://langchain-ai.github.io/langgraph/how-tos/local-studio/#run-the-development-server)
  * [ Use the studio  ](https://langchain-ai.github.io/langgraph/how-tos/local-studio/#use-the-studio)



[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/local-studio.md "Edit this page")

# How to connect a local agent to LangGraph Studio[¶](https://langchain-ai.github.io/langgraph/how-tos/local-studio/#how-to-connect-a-local-agent-to-langgraph-studio "Permanent link")

This guide shows you how to connect your local agent to [LangGraph Studio](https://langchain-ai.github.io/langgraph/concepts/langgraph_studio/) for visualization, interaction, and debugging.

## Connection Options[¶](https://langchain-ai.github.io/langgraph/how-tos/local-studio/#connection-options "Permanent link")

There are two ways to connect your local agent to LangGraph Studio:

  * [Development Server](https://langchain-ai.github.io/langgraph/concepts/langgraph_studio/#development-server-with-web-ui): Python package, all platforms, no Docker
  * [LangGraph Desktop](https://langchain-ai.github.io/langgraph/concepts/langgraph_studio/#desktop-app): Application, Mac only, requires Docker



In this guide we will cover how to use the development server as that is generally an easier and better experience.

## Setup your application[¶](https://langchain-ai.github.io/langgraph/how-tos/local-studio/#setup-your-application "Permanent link")

First, you will need to setup your application in the proper format. This means defining a `langgraph.json` file which contains paths to your agent(s). See [this guide](https://langchain-ai.github.io/langgraph/concepts/application_structure/) for information on how to do so.

## Install langgraph-cli[¶](https://langchain-ai.github.io/langgraph/how-tos/local-studio/#install-langgraph-cli "Permanent link")

You will need to install `langgraph-cli`[](https://langchain-ai.github.io/langgraph/cloud/reference/cli/#langgraph-cli) (version `0.1.55` or higher). You will need to make sure to install the `inmem` extras.

Minimum version

The minimum version to use the `inmem` extra with `langgraph-cli` is `0.1.55`. Python 3.11 or higher is required.

```
[](https://langchain-ai.github.io/langgraph/how-tos/local-studio/#__codelineno-0-1)pipinstall-U"langgraph-cli[inmem]"

```


## Run the development server[¶](https://langchain-ai.github.io/langgraph/how-tos/local-studio/#run-the-development-server "Permanent link")

  1. Navigate to your project directory (where `langgraph.json` is located)

  2. Start the server: 

```
[](https://langchain-ai.github.io/langgraph/how-tos/local-studio/#__codelineno-1-1)langgraphdev

```





This will look for the `langgraph.json` file in your current directory. In there, it will find the paths to the graph(s), and start those up. It will then automatically connect to the cloud-hosted studio.

## Use the studio[¶](https://langchain-ai.github.io/langgraph/how-tos/local-studio/#use-the-studio "Permanent link")

After connecting to the studio, a browser window should automatically pop up. This will use the cloud hosted studio UI to connect to your local development server. Your graph is still running locally, the UI is connecting to visualizing the agent and threads that are defined locally.

The graph will always use the most up-to-date code, so you will be able to change the underlying code and have it automatically reflected in the studio. This is useful for debugging workflows. You can run your graph in the UI until it messes up, go in and change your code, and then rerun from the node that failed.

# (Optional) Attach a debugger[¶](https://langchain-ai.github.io/langgraph/how-tos/local-studio/#optional-attach-a-debugger "Permanent link")

For step-by-step debugging with breakpoints and variable inspection:

```
[](https://langchain-ai.github.io/langgraph/how-tos/local-studio/#__codelineno-2-1)# Install debugpy package
[](https://langchain-ai.github.io/langgraph/how-tos/local-studio/#__codelineno-2-2)pipinstalldebugpy
[](https://langchain-ai.github.io/langgraph/how-tos/local-studio/#__codelineno-2-3)
[](https://langchain-ai.github.io/langgraph/how-tos/local-studio/#__codelineno-2-4)# Start server with debugging enabled
[](https://langchain-ai.github.io/langgraph/how-tos/local-studio/#__codelineno-2-5)langgraphdev--debug-port5678

```


Then attach your preferred debugger:

[VS Code](#__tabbed_1_1)[PyCharm](#__tabbed_1_2)

Add this configuration to `launch.json`: 

```
[](https://langchain-ai.github.io/langgraph/how-tos/local-studio/#__codelineno-3-1){
[](https://langchain-ai.github.io/langgraph/how-tos/local-studio/#__codelineno-3-2)"name":"Attach to LangGraph",
[](https://langchain-ai.github.io/langgraph/how-tos/local-studio/#__codelineno-3-3)"type":"debugpy",
[](https://langchain-ai.github.io/langgraph/how-tos/local-studio/#__codelineno-3-4)"request":"attach",
[](https://langchain-ai.github.io/langgraph/how-tos/local-studio/#__codelineno-3-5)"connect":{
[](https://langchain-ai.github.io/langgraph/how-tos/local-studio/#__codelineno-3-6)"host":"0.0.0.0",
[](https://langchain-ai.github.io/langgraph/how-tos/local-studio/#__codelineno-3-7)"port":5678
[](https://langchain-ai.github.io/langgraph/how-tos/local-studio/#__codelineno-3-8)}
[](https://langchain-ai.github.io/langgraph/how-tos/local-studio/#__codelineno-3-9)}

```


Specify the port number you chose in the previous step. 

  1. Go to Run → Edit Configurations
  2. Click + and select "Python Debug Server"
  3. Set IDE host name: `localhost`
  4. Set port: `5678` (or the port number you chose in the previous step)
  5. Click "OK" and start debugging



Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top 

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/local-studio/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
