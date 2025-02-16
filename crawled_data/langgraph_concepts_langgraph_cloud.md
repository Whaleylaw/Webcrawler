---
url: https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/#cloud-saas)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Cloud SaaS 

[ ](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/?q= "Share")

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
            * [ Self-Hosted  ](https://langchain-ai.github.io/langgraph/concepts/self_hosted/)
            * Cloud SaaS  [ Cloud SaaS  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/) Table of contents 
              * [ Overview  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/#overview)
              * [ Deployment  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/#deployment)
              * [ Revision  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/#revision)
              * [ Persistence  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/#persistence)
              * [ Autoscaling  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/#autoscaling)
              * [ Asynchronous Deployment  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/#asynchronous-deployment)
              * [ LangSmith Integration  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/#langsmith-integration)
              * [ Automatic Deletion  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/#automatic-deletion)
              * [ Architecture  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/#architecture)
              * [ Related  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/#related)
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

  * [ Overview  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/#overview)
  * [ Deployment  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/#deployment)
  * [ Revision  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/#revision)
  * [ Persistence  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/#persistence)
  * [ Autoscaling  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/#autoscaling)
  * [ Asynchronous Deployment  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/#asynchronous-deployment)
  * [ LangSmith Integration  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/#langsmith-integration)
  * [ Automatic Deletion  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/#automatic-deletion)
  * [ Architecture  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/#architecture)
  * [ Related  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/#related)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ Concepts  ](https://langchain-ai.github.io/langgraph/concepts/)
  4. [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/concepts#langgraph-platform)
  5. [ Deployment Options  ](https://langchain-ai.github.io/langgraph/concepts#deployment-options)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/concepts/langgraph_cloud.md "Edit this page")

# Cloud SaaS[¶](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/#cloud-saas "Permanent link")

Prerequisites

  * [LangGraph Platform](https://langchain-ai.github.io/langgraph/concepts/langgraph_platform/)
  * [LangGraph Server](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/)



## Overview[¶](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/#overview "Permanent link")

LangGraph's Cloud SaaS is a managed service for deploying LangGraph Servers, regardless of its definition or dependencies. The service offers managed implementations of checkpointers and stores, allowing you to focus on building the right cognitive architecture for your use case. By handling scalable & secure infrastructure, LangGraph Cloud SaaS offers the fastest path to getting your LangGraph Server deployed to production.

## Deployment[¶](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/#deployment "Permanent link")

A **deployment** is an instance of a LangGraph Server. A single deployment can have many [revisions](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/#revision). When a deployment is created, all the necessary infrastructure (e.g. database, containers, secrets store) are automatically provisioned. See the [architecture diagram](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/#architecture) below for more details.

Resource Allocation:

**Deployment Type** | **CPU** | **Memory** | **Scaling**  
---|---|---|---  
Development | 1 CPU | 1 GB | Up to 1 container  
Production | 2 CPU | 2 GB | Up to 10 containers  
  
See the [how-to guide](https://langchain-ai.github.io/langgraph/cloud/deployment/cloud/#create-new-deployment) for creating a new deployment.

## Revision[¶](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/#revision "Permanent link")

A revision is an iteration of a [deployment](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/#deployment). When a new deployment is created, an initial revision is automatically created. To deploy new code changes or update environment variable configurations for a deployment, a new revision must be created. When a revision is created, a new container image is built automatically.

See the [how-to guide](https://langchain-ai.github.io/langgraph/cloud/deployment/cloud/#create-new-revision) for creating a new revision.

## Persistence[¶](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/#persistence "Permanent link")

A dedicated database is automatically created for each deployment. The database serves as the [persistence layer](https://langchain-ai.github.io/langgraph/concepts/persistence/) for the deployment.

When defining a graph to be deployed to LangGraph Cloud SaaS, a [checkpointer](https://langchain-ai.github.io/langgraph/concepts/persistence/#checkpointer-libraries) should not be configured by the user. Instead, a checkpointer is automatically configured for the graph.

There is no direct access to the database. All access to the database occurs through the LangGraph Server APIs.

## Autoscaling[¶](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/#autoscaling "Permanent link")

`Production` type deployments automatically scale up to 10 containers. Scaling is based on the current request load for a single container. Specifically, the autoscaling implementation scales the deployment so that each container is processing about 10 concurrent requests. For example... 

  * If the deployment is processing 20 concurrent requests, the deployment will scale up from 1 container to 2 containers (20 requests / 2 containers = 10 requests per container).
  * If a deployment of 2 containers is processing 10 requests, the deployment will scale down from 2 containers to 1 container (10 requests / 1 container = 10 requests per container).



10 concurrent requests per container is the target threshold. However, 10 concurrent requests per container is not a hard limit. The number of concurrent requests can exceed 10 if there is a sudden burst of requests.

Scale down actions are delayed for 30 minutes before any action is taken. In other words, if the autoscaling implementation decides to scale down a deployment, it will first wait for 30 minutes before scaling down. After 30 minutes, the concurrency metric is recomputed and the deployment will scale down if the concurrency metric has met the target threshold. Otherwise, the deployment remains scaled up. This "cool down" period ensures that deployments do not scale up and down too frequently.

In the future, the autoscaling implementation may evolve to accommodate other metrics such as background run queue size.

## Asynchronous Deployment[¶](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/#asynchronous-deployment "Permanent link")

Infrastructure for [deployments](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/#deployment) and [revisions](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/#revision) are provisioned and deployed asynchronously. They are not deployed immediately after submission. Currently, deployment can take up to several minutes.

  * When a new deployment is created, a new database is created for the deployment. Database creation is a one-time step. This step contributes to a longer deployment time for the initial revision of the deployment.
  * When a subsequent revision is created for a deployment, there is no database creation step. The deployment time for a subsequent revision is significantly faster compared to the deployment time of the initial revision.
  * The deployment process for each revision contains a build step, which can take up to a few minutes.



## LangSmith Integration[¶](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/#langsmith-integration "Permanent link")

A [LangSmith](https://docs.smith.langchain.com/) tracing project is automatically created for each deployemnt. The tracing project has the same name as the deployment. When creating a deployment, the `LANGCHAIN_TRACING_V2` and `LANGCHAIN_API_KEY` environment variables do not need to be specified; they are set internally, automatically. Traces are created for each run and are emitted to the tracing project automatically.

When a deployment is deleted, the traces and the tracing project are not deleted.

## Automatic Deletion[¶](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/#automatic-deletion "Permanent link")

Deployments are automatically deleted after 28 consecutive days of non-use (it is in an unused state). A deployment is in an unused state if there are no traces emitted to LangSmith from the deployment after 28 consecutive days. On any given day, if a deployment emits a trace to LangSmith, the counter for consecutive days of non-use is reset.

  * An email notification is sent after 7 consecutive days of non-use.
  * A deployment is deleted after 28 consecutive days of non-use.



Data Cannot Be Recovered

After a deployment is deleted, the data (i.e. [persistence](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/#persistence)) from the deployment cannot be recovered.

## Architecture[¶](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/#architecture "Permanent link")

Subject to Change

The Cloud SaaS deployment architecture may change in the future.

A high-level diagram of a Cloud SaaS deployment.

![diagram](https://langchain-ai.github.io/langgraph/concepts/img/langgraph_cloud_architecture.png)

## Related[¶](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/#related "Permanent link")

  * [Deployment Options](https://langchain-ai.github.io/langgraph/concepts/deployment_options/)

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Self-Hosted  ](https://langchain-ai.github.io/langgraph/concepts/self_hosted/) [ Next  Bring Your Own Cloud (BYOC)  ](https://langchain-ai.github.io/langgraph/concepts/bring_your_own_cloud/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
