---
url: https://langchain-ai.github.io/langgraphjs/concepts/self_hosted/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/concepts/self_hosted/#self-hosted)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

Self-Hosted 

[ ](https://langchain-ai.github.io/langgraphjs/concepts/self_hosted/?q= "Share")

Type to start searching

[ GitHub  ](https://github.com/langchain-ai/langgraphjs "Go to repository")

  * [ Home ](https://langchain-ai.github.io/langgraphjs/)
  * [ API reference ](https://langchain-ai.github.io/langgraphjs/reference/)
  * [ Versions ](https://langchain-ai.github.io/langgraphjs/versions/)



[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

[ GitHub  ](https://github.com/langchain-ai/langgraphjs "Go to repository")

  * [ Home  ](https://langchain-ai.github.io/langgraphjs/)

Home 
    * Get started  Get started 
      * [ Learn the basics  ](https://langchain-ai.github.io/langgraphjs/tutorials/quickstart/)
      * [ Deployment  ](https://langchain-ai.github.io/langgraphjs/tutorials/deployment/)
    * Guides  Guides 
      * [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
      * [ Concepts  ](https://langchain-ai.github.io/langgraphjs/concepts/)

Concepts 
        * [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/concepts#langgraph)
        * LangGraph Platform  LangGraph Platform 
          * [ LangGraph Platform  ](https://langchain-ai.github.io/langgraphjs/concepts#langgraph-platform)
          * [ High Level  ](https://langchain-ai.github.io/langgraphjs/concepts#high-level)
          * [ Components  ](https://langchain-ai.github.io/langgraphjs/concepts#components)
          * [ LangGraph Server  ](https://langchain-ai.github.io/langgraphjs/concepts#langgraph-server)
          * Deployment Options  Deployment Options 
            * [ Deployment Options  ](https://langchain-ai.github.io/langgraphjs/concepts#deployment-options)
            * Self-Hosted  [ Self-Hosted  ](https://langchain-ai.github.io/langgraphjs/concepts/self_hosted/) Table of contents 
              * [ Versions  ](https://langchain-ai.github.io/langgraphjs/concepts/self_hosted/#versions)
                * [ Self-Hosted Lite  ](https://langchain-ai.github.io/langgraphjs/concepts/self_hosted/#self-hosted-lite)
                * [ Self-Hosted Enterprise  ](https://langchain-ai.github.io/langgraphjs/concepts/self_hosted/#self-hosted-enterprise)
              * [ Requirements  ](https://langchain-ai.github.io/langgraphjs/concepts/self_hosted/#requirements)
              * [ How it works  ](https://langchain-ai.github.io/langgraphjs/concepts/self_hosted/#how-it-works)
            * [ Cloud SaaS  ](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_cloud/)
            * [ Bring Your Own Cloud (BYOC)  ](https://langchain-ai.github.io/langgraphjs/concepts/bring_your_own_cloud/)
      * [ Tutorials  ](https://langchain-ai.github.io/langgraphjs/tutorials/)
    * Resources  Resources 
      * [ Adopters  ](https://langchain-ai.github.io/langgraphjs/adopters/)
      * [ FAQ  ](https://langchain-ai.github.io/langgraphjs/concepts/faq/)
      * [ Troubleshooting  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraphjs/reference/)
  * [ Versions  ](https://langchain-ai.github.io/langgraphjs/versions/)



Table of contents 

  * [ Versions  ](https://langchain-ai.github.io/langgraphjs/concepts/self_hosted/#versions)
    * [ Self-Hosted Lite  ](https://langchain-ai.github.io/langgraphjs/concepts/self_hosted/#self-hosted-lite)
    * [ Self-Hosted Enterprise  ](https://langchain-ai.github.io/langgraphjs/concepts/self_hosted/#self-hosted-enterprise)
  * [ Requirements  ](https://langchain-ai.github.io/langgraphjs/concepts/self_hosted/#requirements)
  * [ How it works  ](https://langchain-ai.github.io/langgraphjs/concepts/self_hosted/#how-it-works)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ Concepts  ](https://langchain-ai.github.io/langgraphjs/concepts/)
  4. [ LangGraph Platform  ](https://langchain-ai.github.io/langgraphjs/concepts#langgraph-platform)
  5. [ Deployment Options  ](https://langchain-ai.github.io/langgraphjs/concepts#deployment-options)



# Self-Hosted[¶](https://langchain-ai.github.io/langgraphjs/concepts/self_hosted/#self-hosted "Permanent link")

Note

  * [LangGraph Platform](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_platform/)
  * [Deployment Options](https://langchain-ai.github.io/langgraphjs/concepts/deployment_options/)



## Versions[¶](https://langchain-ai.github.io/langgraphjs/concepts/self_hosted/#versions "Permanent link")

There are two versions of the self hosted deployment: [Self-Hosted Enterprise](https://langchain-ai.github.io/langgraphjs/concepts/deployment_options/#self-hosted-enterprise) and [Self-Hosted Lite](https://langchain-ai.github.io/langgraphjs/concepts/deployment_options/#self-hosted-lite).

### Self-Hosted Lite[¶](https://langchain-ai.github.io/langgraphjs/concepts/self_hosted/#self-hosted-lite "Permanent link")

The Self-Hosted Lite version is a limited version of LangGraph Platform that you can run locally or in a self-hosted manner (up to 1 million nodes executed).

When using the Self-Hosted Lite version, you authenticate with a [LangSmith](https://smith.langchain.com/) API key.

### Self-Hosted Enterprise[¶](https://langchain-ai.github.io/langgraphjs/concepts/self_hosted/#self-hosted-enterprise "Permanent link")

The Self-Hosted Enterprise version is the full version of LangGraph Platform.

To use the Self-Hosted Enterprise version, you must acquire a license key that you will need to pass in when running the Docker image. To acquire a license key, please email sales@langchain.dev.

## Requirements[¶](https://langchain-ai.github.io/langgraphjs/concepts/self_hosted/#requirements "Permanent link")

  * You use `langgraph-cli` and/or [LangGraph Studio](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_studio/) app to test graph locally.
  * You use `langgraph build` command to build image.



## How it works[¶](https://langchain-ai.github.io/langgraphjs/concepts/self_hosted/#how-it-works "Permanent link")

  * Deploy Redis and Postgres instances on your own infrastructure.
  * Build the docker image for [LangGraph Server](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_server/) using the [LangGraph CLI](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_cli/)
  * Deploy a web server that will run the docker image and pass in the necessary environment variables.



See the [how-to guide](https://langchain-ai.github.io/langgraphjs/how-tos/deploy-self-hosted/)

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  Double Texting  ](https://langchain-ai.github.io/langgraphjs/concepts/double_texting/) [ Next  Cloud SaaS  ](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_cloud/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/concepts/self_hosted/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
