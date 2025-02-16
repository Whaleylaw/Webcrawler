---
url: https://langchain-ai.github.io/langgraph/concepts/deployment_options/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/concepts/deployment_options/#deployment-options)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Deployment Options 

[ ](https://langchain-ai.github.io/langgraph/concepts/deployment_options/?q= "Share")

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
          * High Level  High Level 
            * [ High Level  ](https://langchain-ai.github.io/langgraph/concepts#high-level)
            * [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_platform/)
            * Deployment Options  [ Deployment Options  ](https://langchain-ai.github.io/langgraph/concepts/deployment_options/) Table of contents 
              * [ Overview  ](https://langchain-ai.github.io/langgraph/concepts/deployment_options/#overview)
              * [ Self-Hosted Enterprise  ](https://langchain-ai.github.io/langgraph/concepts/deployment_options/#self-hosted-enterprise)
              * [ Self-Hosted Lite  ](https://langchain-ai.github.io/langgraph/concepts/deployment_options/#self-hosted-lite)
              * [ Cloud SaaS  ](https://langchain-ai.github.io/langgraph/concepts/deployment_options/#cloud-saas)
              * [ Bring Your Own Cloud  ](https://langchain-ai.github.io/langgraph/concepts/deployment_options/#bring-your-own-cloud)
              * [ Related  ](https://langchain-ai.github.io/langgraph/concepts/deployment_options/#related)
            * [ LangGraph Platform Plans  ](https://langchain-ai.github.io/langgraph/concepts/plans/)
            * [ Template Applications  ](https://langchain-ai.github.io/langgraph/concepts/template_applications/)
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

  * [ Overview  ](https://langchain-ai.github.io/langgraph/concepts/deployment_options/#overview)
  * [ Self-Hosted Enterprise  ](https://langchain-ai.github.io/langgraph/concepts/deployment_options/#self-hosted-enterprise)
  * [ Self-Hosted Lite  ](https://langchain-ai.github.io/langgraph/concepts/deployment_options/#self-hosted-lite)
  * [ Cloud SaaS  ](https://langchain-ai.github.io/langgraph/concepts/deployment_options/#cloud-saas)
  * [ Bring Your Own Cloud  ](https://langchain-ai.github.io/langgraph/concepts/deployment_options/#bring-your-own-cloud)
  * [ Related  ](https://langchain-ai.github.io/langgraph/concepts/deployment_options/#related)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ Concepts  ](https://langchain-ai.github.io/langgraph/concepts/)
  4. [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/concepts#langgraph-platform)
  5. [ High Level  ](https://langchain-ai.github.io/langgraph/concepts#high-level)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/concepts/deployment_options.md "Edit this page")

# Deployment Options[¶](https://langchain-ai.github.io/langgraph/concepts/deployment_options/#deployment-options "Permanent link")

Prerequisites

  * [LangGraph Platform](https://langchain-ai.github.io/langgraph/concepts/langgraph_platform/)
  * [LangGraph Server](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/)
  * [LangGraph Platform Plans](https://langchain-ai.github.io/langgraph/concepts/plans/)



## Overview[¶](https://langchain-ai.github.io/langgraph/concepts/deployment_options/#overview "Permanent link")

There are 4 main options for deploying with the LangGraph Platform:

  1. **[Self-Hosted Lite](https://langchain-ai.github.io/langgraph/concepts/deployment_options/#self-hosted-lite)** : Available for all plans.

  2. **[Self-Hosted Enterprise](https://langchain-ai.github.io/langgraph/concepts/deployment_options/#self-hosted-enterprise)** : Available for the **Enterprise** plan.

  3. **[Cloud SaaS](https://langchain-ai.github.io/langgraph/concepts/deployment_options/#cloud-saas)** : Available for **Plus** and **Enterprise** plans.

  4. **[Bring Your Own Cloud](https://langchain-ai.github.io/langgraph/concepts/deployment_options/#bring-your-own-cloud)** : Available only for **Enterprise** plans and **only on AWS**.




Please see the [LangGraph Platform Plans](https://langchain-ai.github.io/langgraph/concepts/plans/) for more information on the different plans.

The guide below will explain the differences between the deployment options.

## Self-Hosted Enterprise[¶](https://langchain-ai.github.io/langgraph/concepts/deployment_options/#self-hosted-enterprise "Permanent link")

Important

The Self-Hosted Enterprise version is only available for the **Enterprise** plan.

Note

The LangGraph Platform Deployments view (within LangSmith SaaS and self-hosted LangSmith) is not available for Self-Hosted Enterprise LangGraph deployments. Self-hosted LangGraph deployments are managed externally from LangSmith (e.g. there is no UI to manage these deployments).

With a Self-Hosted Enterprise deployment, you are responsible for managing the infrastructure, including setting up and maintaining required databases and Redis instances.

You’ll build a Docker image using the [LangGraph CLI](https://langchain-ai.github.io/langgraph/concepts/langgraph_cli/), which can then be deployed on your own infrastructure.

For more information, please see:

  * [Self-Hosted conceptual guide](https://langchain-ai.github.io/langgraph/concepts/self_hosted/)
  * [Self-Hosted Deployment how-to guide](https://langchain-ai.github.io/langgraph/how-tos/deploy-self-hosted/)



## Self-Hosted Lite[¶](https://langchain-ai.github.io/langgraph/concepts/deployment_options/#self-hosted-lite "Permanent link")

Important

The Self-Hosted Lite version is available for all plans.

Note

The LangGraph Platform Deployments view (within LangSmith SaaS and self-hosted LangSmith) is not available for Self-Hosted Lite LangGraph deployments. Self-hosted LangGraph deployments are managed externally from LangSmith (e.g. there is no UI to manage these deployments).

The Self-Hosted Lite deployment option is a free (up to 1 million nodes executed per year), limited version of LangGraph Platform that you can run locally or in a self-hosted manner.

With a Self-Hosted Lite deployment, you are responsible for managing the infrastructure, including setting up and maintaining required databases and Redis instances.

You’ll build a Docker image using the [LangGraph CLI](https://langchain-ai.github.io/langgraph/concepts/langgraph_cli/), which can then be deployed on your own infrastructure.

[Cron jobs](https://langchain-ai.github.io/langgraph/cloud/how-tos/cron_jobs/) are not available for Self-Hosted Lite deployments.

For more information, please see:

  * [Self-Hosted conceptual guide](https://langchain-ai.github.io/langgraph/concepts/self_hosted/)
  * [Self-Hosted deployment how-to guide](https://langchain-ai.github.io/langgraph/how-tos/deploy-self-hosted/)



## Cloud SaaS[¶](https://langchain-ai.github.io/langgraph/concepts/deployment_options/#cloud-saas "Permanent link")

Important

The Cloud SaaS version of LangGraph Platform is only available for **Plus** and **Enterprise** plans.

The [Cloud SaaS](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/) version of LangGraph Platform is hosted as part of [LangSmith](https://smith.langchain.com/).

The Cloud SaaS version of LangGraph Platform provides a simple way to deploy and manage your LangGraph applications.

This deployment option provides access to the LangGraph Platform UI (within LangSmith) and an integration with GitHub, allowing you to deploy code from any of your repositories on GitHub.

For more information, please see:

  * [Cloud SaaS Conceptual Guide](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/)
  * [How to deploy to Cloud SaaS](https://langchain-ai.github.io/langgraph/cloud/deployment/cloud/)



## Bring Your Own Cloud[¶](https://langchain-ai.github.io/langgraph/concepts/deployment_options/#bring-your-own-cloud "Permanent link")

Important

The Bring Your Own Cloud version of LangGraph Platform is only available for **Enterprise** plans.

This combines the best of both worlds for Cloud and Self-Hosted. Create your deployments through the LangGraph Platform UI (within LangSmith) and we manage the infrastructure so you don't have to. The infrastructure all runs within your cloud. This is currently only available on AWS.

For more information please see:

  * [Bring Your Own Cloud Conceptual Guide](https://langchain-ai.github.io/langgraph/concepts/bring_your_own_cloud/)



## Related[¶](https://langchain-ai.github.io/langgraph/concepts/deployment_options/#related "Permanent link")

For more information, please see:

  * [LangGraph Platform plans](https://langchain-ai.github.io/langgraph/concepts/plans/)
  * [LangGraph Platform pricing](https://www.langchain.com/langgraph-platform-pricing)
  * [Deployment how-to guides](https://langchain-ai.github.io/langgraph/how-tos/#deployment)

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  LangGraph Platform  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_platform/) [ Next  LangGraph Platform Plans  ](https://langchain-ai.github.io/langgraph/concepts/plans/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/concepts/deployment_options/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
