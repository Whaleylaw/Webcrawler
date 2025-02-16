---
url: https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_LICENSE/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_LICENSE/#invalid_license)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

INVALID_LICENSE 

[ ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_LICENSE/?q= "Share")

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
      * [ Tutorials  ](https://langchain-ai.github.io/langgraph/tutorials/)
    * Resources  Resources 
      * [ Prebuilt Agents  ](https://langchain-ai.github.io/langgraph/prebuilt/)
      * [ Adopters  ](https://langchain-ai.github.io/langgraph/adopters/)
      * [ FAQ  ](https://langchain-ai.github.io/langgraph/concepts/faq/)
      * [ Troubleshooting  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/)

Troubleshooting 
        * [ GRAPH_RECURSION_LIMIT  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/GRAPH_RECURSION_LIMIT/)
        * [ INVALID_CONCURRENT_GRAPH_UPDATE  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/)
        * [ INVALID_GRAPH_NODE_RETURN_VALUE  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_GRAPH_NODE_RETURN_VALUE/)
        * [ MULTIPLE_SUBGRAPHS  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/MULTIPLE_SUBGRAPHS/)
        * [ INVALID_CHAT_HISTORY  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_CHAT_HISTORY/)
        * INVALID_LICENSE  [ INVALID_LICENSE  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_LICENSE/) Table of contents 
          * [ When This Occurs  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_LICENSE/#when-this-occurs)
          * [ Troubleshooting  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_LICENSE/#troubleshooting)
            * [ Confirm deployment type  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_LICENSE/#confirm-deployment-type)
              * [ For Local Development  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_LICENSE/#for-local-development)
              * [ For Managed LangGraph Platform  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_LICENSE/#for-managed-langgraph-platform)
              * [ For Self-Hosted Lite (Limited Features)  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_LICENSE/#for-self-hosted-lite-limited-features)
              * [ For Self-Hosted Enterprise (Full Features)  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_LICENSE/#for-self-hosted-enterprise-full-features)
            * [ Confirm credentials  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_LICENSE/#confirm-credentials)
              * [ For Self-Hosted Lite  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_LICENSE/#for-self-hosted-lite)
              * [ For Self-Hosted Enterprise  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_LICENSE/#for-self-hosted-enterprise)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraph/reference/graphs/)



Table of contents 

  * [ When This Occurs  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_LICENSE/#when-this-occurs)
  * [ Troubleshooting  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_LICENSE/#troubleshooting)
    * [ Confirm deployment type  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_LICENSE/#confirm-deployment-type)
      * [ For Local Development  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_LICENSE/#for-local-development)
      * [ For Managed LangGraph Platform  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_LICENSE/#for-managed-langgraph-platform)
      * [ For Self-Hosted Lite (Limited Features)  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_LICENSE/#for-self-hosted-lite-limited-features)
      * [ For Self-Hosted Enterprise (Full Features)  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_LICENSE/#for-self-hosted-enterprise-full-features)
    * [ Confirm credentials  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_LICENSE/#confirm-credentials)
      * [ For Self-Hosted Lite  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_LICENSE/#for-self-hosted-lite)
      * [ For Self-Hosted Enterprise  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_LICENSE/#for-self-hosted-enterprise)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Resources  ](https://langchain-ai.github.io/langgraph/prebuilt/)
  3. [ Troubleshooting  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/troubleshooting/errors/INVALID_LICENSE.md "Edit this page")

# INVALID_LICENSE[¶](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_LICENSE/#invalid_license "Permanent link")

This error is raised when license verification fails while attempting to start a self-hosted LangGraph Platform server. This error is specific to the LangGraph Platform and is not related to the open source libraries.

## When This Occurs[¶](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_LICENSE/#when-this-occurs "Permanent link")

This error occurs when running a self-hosted deployment of LangGraph Platform without a valid enterprise license or API key.

## Troubleshooting[¶](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_LICENSE/#troubleshooting "Permanent link")

### Confirm deployment type[¶](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_LICENSE/#confirm-deployment-type "Permanent link")

First, confirm the desired mode of deployment.

#### For Local Development[¶](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_LICENSE/#for-local-development "Permanent link")

If you're just developing locally, you can use the lightweight in-memory server by running `langgraph dev`. See the [local server](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/) docs for more information.

#### For Managed LangGraph Platform[¶](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_LICENSE/#for-managed-langgraph-platform "Permanent link")

If you would like a fast managed environment, consider the [Cloud SaaS](https://langchain-ai.github.io/langgraph/concepts/langgraph_cloud/) deployment option. This requires no additional license key.

#### For Self-Hosted Lite (Limited Features)[¶](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_LICENSE/#for-self-hosted-lite-limited-features "Permanent link")

If your deployment is unlikely to see more than 1 million node executions per year and don't need Crons and other enterprise features, consider the [Self-Hosted Lite](https://langchain-ai.github.io/langgraph/concepts/deployment_options/#self-hosted-lite) deployment option.

You can deploy with Self-Hosted Lite by setting a valid `LANGSMITH_API_KEY` in your environment (e.g., in the `.env` file referenced by `langgraph.json`) and building a Docker image. The API key must be associated with an account on a **Plus** plan or greater.

#### For Self-Hosted Enterprise (Full Features)[¶](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_LICENSE/#for-self-hosted-enterprise-full-features "Permanent link")

For full self-hosting, set the `LANGGRAPH_CLOUD_LICENSE_KEY` environment variable. If you are interested in an enterprise license key, please contact the LangChain support team.

For more information on deployment options and their features, see the [Deployment Options](https://langchain-ai.github.io/langgraph/concepts/deployment_options/) documentation.

### Confirm credentials[¶](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_LICENSE/#confirm-credentials "Permanent link")

If you have confirmed that you would like to self-host LangGraph Platform, please verify your credentials.

#### For Self-Hosted Lite[¶](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_LICENSE/#for-self-hosted-lite "Permanent link")

  1. Confirm that you have provided a working `LANGSMITH_API_KEY` environment variable in your deployment environment or `.env` file
  2. Confirm the provided API key is associated with an account on a **Plus** or **Enterprise** plan (or equivalent)



#### For Self-Hosted Enterprise[¶](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_LICENSE/#for-self-hosted-enterprise "Permanent link")

  1. Confirm that you have provided a working `LANGGRAPH_CLOUD_LICENSE_KEY` environment variable in your deployment environment or `.env` file
  2. Confirm the key is still valid and has not surpassed its expiration date

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  INVALID_CHAT_HISTORY  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_CHAT_HISTORY/) [ Next  Graphs  ](https://langchain-ai.github.io/langgraph/reference/graphs/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/troubleshooting/errors/INVALID_LICENSE/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
