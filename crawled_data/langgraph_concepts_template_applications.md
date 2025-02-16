---
url: https://langchain-ai.github.io/langgraph/concepts/template_applications/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/concepts/template_applications/#template-applications)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Template Applications 

[ ](https://langchain-ai.github.io/langgraph/concepts/template_applications/?q= "Share")

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
      * [ Concepts  ](https://langchain-ai.github.io/langgraph/concepts/)

Concepts 
        * [ LangGraph  ](https://langchain-ai.github.io/langgraph/concepts#langgraph)
        * LangGraph Platform  LangGraph Platform 
          * [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/concepts#langgraph-platform)
          * High Level  High Level 
            * [ High Level  ](https://langchain-ai.github.io/langgraph/concepts#high-level)
            * [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_platform/)
            * [ Deployment Options  ](https://langchain-ai.github.io/langgraph/concepts/deployment_options/)
            * [ LangGraph Platform Plans  ](https://langchain-ai.github.io/langgraph/concepts/plans/)
            * Template Applications  [ Template Applications  ](https://langchain-ai.github.io/langgraph/concepts/template_applications/) Table of contents 
              * [ Install the LangGraph CLI  ](https://langchain-ai.github.io/langgraph/concepts/template_applications/#install-the-langgraph-cli)
              * [ Available Templates  ](https://langchain-ai.github.io/langgraph/concepts/template_applications/#available-templates)
              * [ 🌱 Create a LangGraph App  ](https://langchain-ai.github.io/langgraph/concepts/template_applications/#create-a-langgraph-app)
              * [ Next Steps  ](https://langchain-ai.github.io/langgraph/concepts/template_applications/#next-steps)
                * [ LangGraph Framework  ](https://langchain-ai.github.io/langgraph/concepts/template_applications/#langgraph-framework)
                * [ 📚 Learn More about LangGraph Platform  ](https://langchain-ai.github.io/langgraph/concepts/template_applications/#learn-more-about-langgraph-platform)
          * [ Components  ](https://langchain-ai.github.io/langgraph/concepts#components)
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

  * [ Install the LangGraph CLI  ](https://langchain-ai.github.io/langgraph/concepts/template_applications/#install-the-langgraph-cli)
  * [ Available Templates  ](https://langchain-ai.github.io/langgraph/concepts/template_applications/#available-templates)
  * [ 🌱 Create a LangGraph App  ](https://langchain-ai.github.io/langgraph/concepts/template_applications/#create-a-langgraph-app)
  * [ Next Steps  ](https://langchain-ai.github.io/langgraph/concepts/template_applications/#next-steps)
    * [ LangGraph Framework  ](https://langchain-ai.github.io/langgraph/concepts/template_applications/#langgraph-framework)
    * [ 📚 Learn More about LangGraph Platform  ](https://langchain-ai.github.io/langgraph/concepts/template_applications/#learn-more-about-langgraph-platform)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ Concepts  ](https://langchain-ai.github.io/langgraph/concepts/)
  4. [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/concepts#langgraph-platform)
  5. [ High Level  ](https://langchain-ai.github.io/langgraph/concepts#high-level)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/concepts/template_applications.md "Edit this page")

# Template Applications[¶](https://langchain-ai.github.io/langgraph/concepts/template_applications/#template-applications "Permanent link")

Templates are open source reference applications designed to help you get started quickly when building with LangGraph. They provide working examples of common agentic workflows that can be customized to your needs.

You can create an application from a template using the LangGraph CLI.

Requirements

  * Python >= 3.11
  * [LangGraph CLI](https://langchain-ai.github.io/langgraph/cloud/reference/cli/): Requires langchain-cli[inmem] >= 0.1.58



## Install the LangGraph CLI[¶](https://langchain-ai.github.io/langgraph/concepts/template_applications/#install-the-langgraph-cli "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/concepts/template_applications/#__codelineno-0-1)pipinstall"langgraph-cli[inmem]"--upgrade

```


## Available Templates[¶](https://langchain-ai.github.io/langgraph/concepts/template_applications/#available-templates "Permanent link")

Template | Description | Python | JS/TS  
---|---|---|---  
**New LangGraph Project** | A simple, minimal chatbot with memory. | [Repo](https://github.com/langchain-ai/new-langgraph-project) | [Repo](https://github.com/langchain-ai/new-langgraphjs-project)  
**ReAct Agent** | A simple agent that can be flexibly extended to many tools. | [Repo](https://github.com/langchain-ai/react-agent) | [Repo](https://github.com/langchain-ai/react-agent-js)  
**Memory Agent** | A ReAct-style agent with an additional tool to store memories for use across threads. | [Repo](https://github.com/langchain-ai/memory-agent) | [Repo](https://github.com/langchain-ai/memory-agent-js)  
**Retrieval Agent** | An agent that includes a retrieval-based question-answering system. | [Repo](https://github.com/langchain-ai/retrieval-agent-template) | [Repo](https://github.com/langchain-ai/retrieval-agent-template-js)  
**Data-Enrichment Agent** | An agent that performs web searches and organizes its findings into a structured format. | [Repo](https://github.com/langchain-ai/data-enrichment) | [Repo](https://github.com/langchain-ai/data-enrichment-js)  
  
## 🌱 Create a LangGraph App[¶](https://langchain-ai.github.io/langgraph/concepts/template_applications/#create-a-langgraph-app "Permanent link")

To create a new app from a template, use the `langgraph new` command.

```
[](https://langchain-ai.github.io/langgraph/concepts/template_applications/#__codelineno-1-1)langgraphnew

```


## Next Steps[¶](https://langchain-ai.github.io/langgraph/concepts/template_applications/#next-steps "Permanent link")

Review the `README.md` file in the root of your new LangGraph app for more information about the template and how to customize it.

After configuring the app properly and adding your API keys, you can start the app using the LangGraph CLI:

```
[](https://langchain-ai.github.io/langgraph/concepts/template_applications/#__codelineno-2-1)langgraphdev

```


See the following guides for more information on how to deploy your app:

  * **[Launch Local LangGraph Server](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/)** : This quick start guide shows how to start a LangGraph Server locally for the **ReAct Agent** template. The steps are similar for other templates.
  * **[Deploy to LangGraph Cloud](https://langchain-ai.github.io/langgraph/cloud/quick_start/)** : Deploy your LangGraph app using LangGraph Cloud.



### LangGraph Framework[¶](https://langchain-ai.github.io/langgraph/concepts/template_applications/#langgraph-framework "Permanent link")

  * **[LangGraph Concepts](https://langchain-ai.github.io/langgraph/concepts/)** : Learn the foundational concepts of LangGraph.
  * **[LangGraph How-to Guides](https://langchain-ai.github.io/langgraph/how-tos/)** : Guides for common tasks with LangGraph.



### 📚 Learn More about LangGraph Platform[¶](https://langchain-ai.github.io/langgraph/concepts/template_applications/#learn-more-about-langgraph-platform "Permanent link")

Expand your knowledge with these resources:

  * **[LangGraph Platform Concepts](https://langchain-ai.github.io/langgraph/concepts/#langgraph-platform)** : Understand the foundational concepts of the LangGraph Platform.
  * **[LangGraph Platform How-to Guides](https://langchain-ai.github.io/langgraph/how-tos/#langgraph-platform)** : Discover step-by-step guides to build and deploy applications.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  LangGraph Platform Plans  ](https://langchain-ai.github.io/langgraph/concepts/plans/) [ Next  LangGraph Server  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/concepts/template_applications/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
