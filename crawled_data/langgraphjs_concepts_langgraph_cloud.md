---
url: https://langchain-ai.github.io/langgraphjs/concepts/langgraph_cloud/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_cloud/#cloud-saas)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

Cloud SaaS 

[ ](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_cloud/?q= "Share")

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
            * [ Self-Hosted  ](https://langchain-ai.github.io/langgraphjs/concepts/self_hosted/)
            * Cloud SaaS  [ Cloud SaaS  ](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_cloud/) Table of contents 
              * [ Overview  ](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_cloud/#overview)
              * [ Deployment  ](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_cloud/#deployment)
              * [ Revision  ](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_cloud/#revision)
              * [ Asynchronous Deployment  ](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_cloud/#asynchronous-deployment)
              * [ Architecture  ](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_cloud/#architecture)
              * [ Related  ](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_cloud/#related)
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

  * [ Overview  ](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_cloud/#overview)
  * [ Deployment  ](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_cloud/#deployment)
  * [ Revision  ](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_cloud/#revision)
  * [ Asynchronous Deployment  ](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_cloud/#asynchronous-deployment)
  * [ Architecture  ](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_cloud/#architecture)
  * [ Related  ](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_cloud/#related)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ Concepts  ](https://langchain-ai.github.io/langgraphjs/concepts/)
  4. [ LangGraph Platform  ](https://langchain-ai.github.io/langgraphjs/concepts#langgraph-platform)
  5. [ Deployment Options  ](https://langchain-ai.github.io/langgraphjs/concepts#deployment-options)



# Cloud SaaS[¶](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_cloud/#cloud-saas "Permanent link")

Prerequisites

  * [LangGraph Platform](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_platform/)
  * [LangGraph Server](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_server/)



## Overview[¶](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_cloud/#overview "Permanent link")

LangGraph's Cloud SaaS is a managed service that provides a scalable and secure environment for deploying LangGraph APIs. It is designed to work seamlessly with your LangGraph API regardless of how it is defined, what tools it uses, or any dependencies. Cloud SaaS provides a simple way to deploy and manage your LangGraph API in the cloud.

## Deployment[¶](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_cloud/#deployment "Permanent link")

A **deployment** is an instance of a LangGraph API. A single deployment can have many [revisions](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_cloud/#revision). When a deployment is created, all the necessary infrastructure (e.g. database, containers, secrets store) are automatically provisioned. See the [architecture diagram](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_cloud/#architecture) below for more details.

See the [how-to guide](https://langchain-ai.github.io/langgraphjs/cloud/deployment/cloud.md#create-new-deployment) for creating a new deployment.

## Revision[¶](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_cloud/#revision "Permanent link")

A revision is an iteration of a [deployment](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_cloud/#deployment). When a new deployment is created, an initial revision is automatically created. To deploy new code changes or update environment variable configurations for a deployment, a new revision must be created. When a revision is created, a new container image is built automatically.

See the [how-to guide](https://langchain-ai.github.io/langgraphjs/cloud/deployment/cloud.md#create-new-revision) for creating a new revision.

## Asynchronous Deployment[¶](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_cloud/#asynchronous-deployment "Permanent link")

Infrastructure for [deployments](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_cloud/#deployment) and [revisions](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_cloud/#revision) are provisioned and deployed asynchronously. They are not deployed immediately after submission. Currently, deployment can take up to several minutes.

## Architecture[¶](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_cloud/#architecture "Permanent link")

Subject to Change

The Cloud SaaS deployment architecture may change in the future.

A high-level diagram of a Cloud SaaS deployment.

![diagram](https://langchain-ai.github.io/langgraphjs/concepts/img/langgraph_cloud_architecture.png)

## Related[¶](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_cloud/#related "Permanent link")

  * [Deployment Options](https://langchain-ai.github.io/langgraphjs/concepts/deployment_options/)

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  Self-Hosted  ](https://langchain-ai.github.io/langgraphjs/concepts/self_hosted/) [ Next  Bring Your Own Cloud (BYOC)  ](https://langchain-ai.github.io/langgraphjs/concepts/bring_your_own_cloud/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_cloud/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
