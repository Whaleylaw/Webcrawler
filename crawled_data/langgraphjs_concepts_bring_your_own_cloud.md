---
url: https://langchain-ai.github.io/langgraphjs/concepts/bring_your_own_cloud/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/concepts/bring_your_own_cloud/#bring-your-own-cloud-byoc)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

Bring Your Own Cloud (BYOC) 

[ ](https://langchain-ai.github.io/langgraphjs/concepts/bring_your_own_cloud/?q= "Share")

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
            * [ Cloud SaaS  ](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_cloud/)
            * Bring Your Own Cloud (BYOC)  [ Bring Your Own Cloud (BYOC)  ](https://langchain-ai.github.io/langgraphjs/concepts/bring_your_own_cloud/) Table of contents 
              * [ Architecture  ](https://langchain-ai.github.io/langgraphjs/concepts/bring_your_own_cloud/#architecture)
              * [ Requirements  ](https://langchain-ai.github.io/langgraphjs/concepts/bring_your_own_cloud/#requirements)
              * [ How it works  ](https://langchain-ai.github.io/langgraphjs/concepts/bring_your_own_cloud/#how-it-works)
      * [ Tutorials  ](https://langchain-ai.github.io/langgraphjs/tutorials/)
    * Resources  Resources 
      * [ Adopters  ](https://langchain-ai.github.io/langgraphjs/adopters/)
      * [ FAQ  ](https://langchain-ai.github.io/langgraphjs/concepts/faq/)
      * [ Troubleshooting  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraphjs/reference/)
  * [ Versions  ](https://langchain-ai.github.io/langgraphjs/versions/)



Table of contents 

  * [ Architecture  ](https://langchain-ai.github.io/langgraphjs/concepts/bring_your_own_cloud/#architecture)
  * [ Requirements  ](https://langchain-ai.github.io/langgraphjs/concepts/bring_your_own_cloud/#requirements)
  * [ How it works  ](https://langchain-ai.github.io/langgraphjs/concepts/bring_your_own_cloud/#how-it-works)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ Concepts  ](https://langchain-ai.github.io/langgraphjs/concepts/)
  4. [ LangGraph Platform  ](https://langchain-ai.github.io/langgraphjs/concepts#langgraph-platform)
  5. [ Deployment Options  ](https://langchain-ai.github.io/langgraphjs/concepts#deployment-options)



# Bring Your Own Cloud (BYOC)[¶](https://langchain-ai.github.io/langgraphjs/concepts/bring_your_own_cloud/#bring-your-own-cloud-byoc "Permanent link")

Note

  * [LangGraph Platform](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_platform/)
  * [Deployment Options](https://langchain-ai.github.io/langgraphjs/concepts/deployment_options/)



## Architecture[¶](https://langchain-ai.github.io/langgraphjs/concepts/bring_your_own_cloud/#architecture "Permanent link")

Split control plane (hosted by us) and data plane (hosted by you, managed by us).

Control Plane | Data Plane  
---|---  
What it does | Manages deployments, revisions. | Runs your LangGraph graphs, stores your data.  
Where it is hosted | LangChain Cloud account | Your cloud account  
Who provisions and monitors | LangChain | LangChain  
  
LangChain has no direct access to the resources created in your cloud account, and can only interact with them via AWS APIs. Your data never leaves your cloud account / VPC at rest or in transit.

![Architecture](https://langchain-ai.github.io/langgraphjs/concepts/img/byoc_architecture.png)

## Requirements[¶](https://langchain-ai.github.io/langgraphjs/concepts/bring_your_own_cloud/#requirements "Permanent link")

  * You’re using AWS already.
  * You use `langgraph-cli` and/or [LangGraph Studio](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_studio/) app to test graph locally.
  * You use `langgraph build` command to build image and then push it to your AWS ECR repository (`docker push`).



## How it works[¶](https://langchain-ai.github.io/langgraphjs/concepts/bring_your_own_cloud/#how-it-works "Permanent link")

  * We provide you a [Terraform module](https://github.com/langchain-ai/terraform/tree/main/modules/langgraph_cloud_setup) which you run to set up our requirements
    1. Creates an AWS role (which our control plane will later assume to provision and monitor resources)
       * <https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonVPCReadOnlyAccess.html>
         * Read VPCS to find subnets
       * <https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonECS_FullAccess.html>
         * Used to create/delete ECS resources for your LangGraph Cloud instances
       * <https://docs.aws.amazon.com/aws-managed-policy/latest/reference/SecretsManagerReadWrite.html>
         * Create secrets for your ECS resources
       * <https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudWatchReadOnlyAccess.html>
         * Read CloudWatch metrics/logs to monitor your instances/push deployment logs
       * <https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonRDSFullAccess.html>
         * Provision `RDS` instances for your LangGraph Cloud instances
    2. Either
       * Tags an existing vpc / subnets as `langgraph-cloud-enabled`
       * Creates a new vpc and subnets and tags them as `langgraph-cloud-enabled`
  * You create a LangGraph Cloud Project in `smith.langchain.com` providing
    * the ID of the AWS role created in the step above
    * the AWS ECR repo to pull the service image from
  * We provision the resources in your cloud account using the role above
  * We monitor those resources to ensure uptime and recovery from errors



Notes for customers using [self-hosted LangSmith](https://docs.smith.langchain.com/self_hosting):

  * Creation of new LangGraph Cloud projects and revisions currently needs to be done on smith.langchain.com.
  * You can however set up the project to trace to your self-hosted LangSmith instance if desired

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  Cloud SaaS  ](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_cloud/) [ Next  Tutorials  ](https://langchain-ai.github.io/langgraphjs/tutorials/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/concepts/bring_your_own_cloud/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
