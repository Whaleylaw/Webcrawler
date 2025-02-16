---
url: https://langchain-ai.github.io/langgraph/concepts/self_hosted/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/concepts/self_hosted/#self-hosted)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Self-Hosted 

[ ](https://langchain-ai.github.io/langgraph/concepts/self_hosted/?q= "Share")

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
          * [ Components  ](https://langchain-ai.github.io/langgraph/concepts#components)
          * [ LangGraph Server  ](https://langchain-ai.github.io/langgraph/concepts#langgraph-server)
          * Deployment Options  Deployment Options 
            * [ Deployment Options  ](https://langchain-ai.github.io/langgraph/concepts#deployment-options)
            * Self-Hosted  [ Self-Hosted  ](https://langchain-ai.github.io/langgraph/concepts/self_hosted/) Table of contents 
              * [ Versions  ](https://langchain-ai.github.io/langgraph/concepts/self_hosted/#versions)
                * [ Self-Hosted Lite  ](https://langchain-ai.github.io/langgraph/concepts/self_hosted/#self-hosted-lite)
                * [ Self-Hosted Enterprise  ](https://langchain-ai.github.io/langgraph/concepts/self_hosted/#self-hosted-enterprise)
              * [ Requirements  ](https://langchain-ai.github.io/langgraph/concepts/self_hosted/#requirements)
              * [ How it works  ](https://langchain-ai.github.io/langgraph/concepts/self_hosted/#how-it-works)
              * [ Helm Chart  ](https://langchain-ai.github.io/langgraph/concepts/self_hosted/#helm-chart)
              * [ Related  ](https://langchain-ai.github.io/langgraph/concepts/self_hosted/#related)
            * [ Cloud SaaS  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/)
            * [ Bring Your Own Cloud (BYOC)  ](https://langchain-ai.github.io/langgraph/concepts/bring_your_own_cloud/)
      * [ Tutorials  ](https://langchain-ai.github.io/langgraph/tutorials/)
    * Resources  Resources 
      * [ Prebuilt Agents  ](https://langchain-ai.github.io/langgraph/prebuilt/)
      * [ Adopters  ](https://langchain-ai.github.io/langgraph/adopters/)
      * [ FAQ  ](https://langchain-ai.github.io/langgraph/concepts/faq/)
      * [ Troubleshooting  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraph/reference/graphs/)



Table of contents 

  * [ Versions  ](https://langchain-ai.github.io/langgraph/concepts/self_hosted/#versions)
    * [ Self-Hosted Lite  ](https://langchain-ai.github.io/langgraph/concepts/self_hosted/#self-hosted-lite)
    * [ Self-Hosted Enterprise  ](https://langchain-ai.github.io/langgraph/concepts/self_hosted/#self-hosted-enterprise)
  * [ Requirements  ](https://langchain-ai.github.io/langgraph/concepts/self_hosted/#requirements)
  * [ How it works  ](https://langchain-ai.github.io/langgraph/concepts/self_hosted/#how-it-works)
  * [ Helm Chart  ](https://langchain-ai.github.io/langgraph/concepts/self_hosted/#helm-chart)
  * [ Related  ](https://langchain-ai.github.io/langgraph/concepts/self_hosted/#related)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ Concepts  ](https://langchain-ai.github.io/langgraph/concepts/)
  4. [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/concepts#langgraph-platform)
  5. [ Deployment Options  ](https://langchain-ai.github.io/langgraph/concepts#deployment-options)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/concepts/self_hosted.md "Edit this page")

# Self-Hosted[¶](https://langchain-ai.github.io/langgraph/concepts/self_hosted/#self-hosted "Permanent link")

Note

  * [LangGraph Platform](https://langchain-ai.github.io/langgraph/concepts/langgraph_platform/)
  * [Deployment Options](https://langchain-ai.github.io/langgraph/concepts/deployment_options/)



## Versions[¶](https://langchain-ai.github.io/langgraph/concepts/self_hosted/#versions "Permanent link")

There are two versions of the self-hosted deployment: [Self-Hosted Enterprise](https://langchain-ai.github.io/langgraph/concepts/deployment_options/#self-hosted-enterprise) and [Self-Hosted Lite](https://langchain-ai.github.io/langgraph/concepts/deployment_options/#self-hosted-lite).

### Self-Hosted Lite[¶](https://langchain-ai.github.io/langgraph/concepts/self_hosted/#self-hosted-lite "Permanent link")

The Self-Hosted Lite version is a limited version of LangGraph Platform that you can run locally or in a self-hosted manner (up to 1 million nodes executed per year).

When using the Self-Hosted Lite version, you authenticate with a [LangSmith](https://smith.langchain.com/) API key.

### Self-Hosted Enterprise[¶](https://langchain-ai.github.io/langgraph/concepts/self_hosted/#self-hosted-enterprise "Permanent link")

The Self-Hosted Enterprise version is the full version of LangGraph Platform.

To use the Self-Hosted Enterprise version, you must acquire a license key that you will need to pass in when running the Docker image. To acquire a license key, please email sales@langchain.dev.

## Requirements[¶](https://langchain-ai.github.io/langgraph/concepts/self_hosted/#requirements "Permanent link")

  * You use `langgraph-cli` and/or [LangGraph Studio](https://langchain-ai.github.io/langgraph/concepts/langgraph_studio/) app to test graph locally.
  * You use `langgraph build` command to build image.



## How it works[¶](https://langchain-ai.github.io/langgraph/concepts/self_hosted/#how-it-works "Permanent link")

  * Deploy Redis and Postgres instances on your own infrastructure.
  * Build the docker image for [LangGraph Server](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/) using the [LangGraph CLI](https://langchain-ai.github.io/langgraph/concepts/langgraph_cli/).
  * Deploy a web server that will run the docker image and pass in the necessary environment variables.



Note

The LangGraph Platform Deployments view (within LangSmith SaaS and self-hosted LangSmith) is not available for Self-Hosted Lite or Self-Hosted Enterprise LangGraph deployments. Self-hosted LangGraph deployments are managed externally from LangSmith (e.g. there is no UI to manage these deployments).

For step-by-step instructions, see [How to set up a self-hosted deployment of LangGraph](https://langchain-ai.github.io/langgraph/how-tos/deploy-self-hosted/).

## Helm Chart[¶](https://langchain-ai.github.io/langgraph/concepts/self_hosted/#helm-chart "Permanent link")

If you would like to deploy LangGraph Cloud on Kubernetes, you can use this [Helm chart](https://github.com/langchain-ai/helm/blob/main/charts/langgraph-cloud/README.md).

## Related[¶](https://langchain-ai.github.io/langgraph/concepts/self_hosted/#related "Permanent link")

  * [How to set up a self-hosted deployment of LangGraph](https://langchain-ai.github.io/langgraph/how-tos/deploy-self-hosted/).

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Authentication & Access Control  ](https://langchain-ai.github.io/langgraph/concepts/auth/) [ Next  Cloud SaaS  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/concepts/self_hosted/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
