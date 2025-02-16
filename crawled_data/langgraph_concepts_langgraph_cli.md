---
url: https://langchain-ai.github.io/langgraph/concepts/langgraph_cli
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/concepts/langgraph_cli/#langgraph-cli)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

LangGraph CLI 

[ ](https://langchain-ai.github.io/langgraph/concepts/langgraph_cli/?q= "Share")

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
      * [ Concepts  ](https://langchain-ai.github.io/langgraph/concepts/)

Concepts 
        * [ LangGraph  ](https://langchain-ai.github.io/langgraph/concepts#langgraph)
        * LangGraph Platform  LangGraph Platform 
          * [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/concepts#langgraph-platform)
          * [ High Level  ](https://langchain-ai.github.io/langgraph/concepts#high-level)
          * Components  Components 
            * [ Components  ](https://langchain-ai.github.io/langgraph/concepts#components)
            * [ LangGraph Server  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/)
            * [ LangGraph Studio  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_studio/)
            * LangGraph CLI  [ LangGraph CLI  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_cli/) Table of contents 
              * [ Installation  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_cli/#installation)
              * [ Commands  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_cli/#commands)
                * [ build  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_cli/#build)
                * [ dev  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_cli/#dev)
                * [ up  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_cli/#up)
                * [ dockerfile  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_cli/#dockerfile)
              * [ Related  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_cli/#related)
            * [ LangGraph SDK  ](https://langchain-ai.github.io/langgraph/concepts/sdk/)
            * [ How to interact with the deployment using RemoteGraph  ](https://langchain-ai.github.io/langgraph/how-tos/use-remote-graph/)
          * [ LangGraph Server  ](https://langchain-ai.github.io/langgraph/concepts#langgraph-server)
          * [ Deployment Options  ](https://langchain-ai.github.io/langgraph/concepts#deployment-options)
      * [ Tutorials  ](https://langchain-ai.github.io/langgraph/tutorials/)
    * Resources  Resources 
      * [ Prebuilt Agents  ](https://langchain-ai.github.io/langgraph/prebuilt/)
      * [ Adopters  ](https://langchain-ai.github.io/langgraph/adopters/)
      * [ FAQ  ](https://langchain-ai.github.io/langgraph/concepts/faq/)
      * [ Troubleshooting  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraph/reference/graphs/)



Table of contents 

  * [ Installation  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_cli/#installation)
  * [ Commands  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_cli/#commands)
    * [ build  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_cli/#build)
    * [ dev  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_cli/#dev)
    * [ up  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_cli/#up)
    * [ dockerfile  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_cli/#dockerfile)
  * [ Related  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_cli/#related)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ Concepts  ](https://langchain-ai.github.io/langgraph/concepts/)
  4. [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/concepts#langgraph-platform)
  5. [ Components  ](https://langchain-ai.github.io/langgraph/concepts#components)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/concepts/langgraph_cli.md "Edit this page")

# LangGraph CLI[¶](https://langchain-ai.github.io/langgraph/concepts/langgraph_cli/#langgraph-cli "Permanent link")

Prerequisites

  * [LangGraph Platform](https://langchain-ai.github.io/langgraph/concepts/langgraph_platform/)
  * [LangGraph Server](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/)



The LangGraph CLI is a multi-platform command-line tool for building and running the [LangGraph API server](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/) locally. This offers an alternative to the [LangGraph Studio desktop app](https://langchain-ai.github.io/langgraph/concepts/langgraph_studio/) for developing and testing agents across all major operating systems (Linux, Windows, MacOS). The resulting server includes all API endpoints for your graph's runs, threads, assistants, etc. as well as the other services required to run your agent, including a managed database for checkpointing and storage.

## Installation[¶](https://langchain-ai.github.io/langgraph/concepts/langgraph_cli/#installation "Permanent link")

The LangGraph CLI can be installed via Homebrew (on macOS) or pip:

[Homebrew](#__tabbed_1_1)[pip](#__tabbed_1_2)

```
[](https://langchain-ai.github.io/langgraph/concepts/langgraph_cli/#__codelineno-0-1)brewinstalllanggraph-cli

```


```
[](https://langchain-ai.github.io/langgraph/concepts/langgraph_cli/#__codelineno-1-1)pipinstalllanggraph-cli

```


## Commands[¶](https://langchain-ai.github.io/langgraph/concepts/langgraph_cli/#commands "Permanent link")

The CLI provides the following core functionality:

### `build`[¶](https://langchain-ai.github.io/langgraph/concepts/langgraph_cli/#build "Permanent link")

The `langgraph build` command builds a Docker image for the [LangGraph API server](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/) that can be directly deployed.

### `dev`[¶](https://langchain-ai.github.io/langgraph/concepts/langgraph_cli/#dev "Permanent link")

New in version 0.1.55

The `langgraph dev` command was introduced in langgraph-cli version 0.1.55.

Python only

Currently, the CLI only supports Python >= 3.11. JS support is coming soon.

The `langgraph dev` command starts a lightweight development server that requires no Docker installation. This server is ideal for rapid development and testing, with features like:

  * Hot reloading: Changes to your code are automatically detected and reloaded
  * Debugger support: Attach your IDE's debugger for line-by-line debugging
  * In-memory state with local persistence: Server state is stored in memory for speed but persisted locally between restarts



To use this command, you need to install the CLI with the "inmem" extra:

```
[](https://langchain-ai.github.io/langgraph/concepts/langgraph_cli/#__codelineno-2-1)pipinstall-U"langgraph-cli[inmem]"

```


**Note** : This command is intended for local development and testing only. It is not recommended for production use. Since it does not use Docker, we recommend using virtual environments to manage your project's dependencies.

### `up`[¶](https://langchain-ai.github.io/langgraph/concepts/langgraph_cli/#up "Permanent link")

The `langgraph up` command starts an instance of the [LangGraph API server](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/) locally in a docker container. This requires thedocker server to be running locally. It also requires a LangSmith API key for local development or a license key for production use.

The server includes all API endpoints for your graph's runs, threads, assistants, etc. as well as the other services required to run your agent, including a managed database for checkpointing and storage.

### `dockerfile`[¶](https://langchain-ai.github.io/langgraph/concepts/langgraph_cli/#dockerfile "Permanent link")

The `langgraph dockerfile` command generates a [Dockerfile](https://docs.docker.com/reference/dockerfile/) that can be used to build images for and deploy instances of the [LangGraph API server](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/). This is useful if you want to further customize the dockerfile or deploy in a more custom way.

Updating your langgraph.json file

The `langgraph dockerfile` command translates all the configuration in your `langgraph.json` file into Dockerfile commands. When using this command, you will have to re-run it whenever you update your `langgraph.json` file. Otherwise, your changes will not be reflected when you build or run the dockerfile.

## Related[¶](https://langchain-ai.github.io/langgraph/concepts/langgraph_cli/#related "Permanent link")

  * [LangGraph CLI API Reference](https://langchain-ai.github.io/langgraph/cloud/reference/cli/)

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  LangGraph Studio  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_studio/) [ Next  LangGraph SDK  ](https://langchain-ai.github.io/langgraph/concepts/sdk/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/concepts/langgraph_cli/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
