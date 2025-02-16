---
url: https://langchain-ai.github.io/langgraph/concepts/assistants/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/concepts/assistants/#assistants)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Assistants 

[ ](https://langchain-ai.github.io/langgraph/concepts/assistants/?q= "Share")

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
          * LangGraph Server  LangGraph Server 
            * [ LangGraph Server  ](https://langchain-ai.github.io/langgraph/concepts#langgraph-server)
            * [ Application Structure  ](https://langchain-ai.github.io/langgraph/concepts/application_structure/)
            * Assistants  [ Assistants  ](https://langchain-ai.github.io/langgraph/concepts/assistants/) Table of contents 
              * [ Configuring Assistants  ](https://langchain-ai.github.io/langgraph/concepts/assistants/#configuring-assistants)
              * [ Versioning Assistants  ](https://langchain-ai.github.io/langgraph/concepts/assistants/#versioning-assistants)
              * [ Resources  ](https://langchain-ai.github.io/langgraph/concepts/assistants/#resources)
            * [ Double Texting  ](https://langchain-ai.github.io/langgraph/concepts/double_texting/)
            * [ Authentication & Access Control  ](https://langchain-ai.github.io/langgraph/concepts/auth/)
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

  * [ Configuring Assistants  ](https://langchain-ai.github.io/langgraph/concepts/assistants/#configuring-assistants)
  * [ Versioning Assistants  ](https://langchain-ai.github.io/langgraph/concepts/assistants/#versioning-assistants)
  * [ Resources  ](https://langchain-ai.github.io/langgraph/concepts/assistants/#resources)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ Concepts  ](https://langchain-ai.github.io/langgraph/concepts/)
  4. [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/concepts#langgraph-platform)
  5. [ LangGraph Server  ](https://langchain-ai.github.io/langgraph/concepts#langgraph-server)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/concepts/assistants.md "Edit this page")

# Assistants[¶](https://langchain-ai.github.io/langgraph/concepts/assistants/#assistants "Permanent link")

Prerequisites

  * [LangGraph Server](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/)



When building agents, it is fairly common to make rapid changes that _do not_ alter the graph logic. For example, simply changing prompts or the LLM selection can have significant impacts on the behavior of the agents. Assistants offer an easy way to make and save these types of changes to agent configuration. This can have at least two use-cases:

  * Assistants give developers a quick and easy way to modify and version agents for experimentation.
  * Assistants can be modified via LangGraph Studio, offering a no-code way to configure agents (e.g., for business users). 



Assistants build off the concept of ["configuration"](https://langchain-ai.github.io/langgraph/concepts/low_level/#configuration). While ["configuration"](https://langchain-ai.github.io/langgraph/concepts/low_level/#configuration) is available in the open source LangGraph library as well, assistants are only present in [LangGraph Platform](https://langchain-ai.github.io/langgraph/concepts/langgraph_platform/). This is because Assistants are tightly coupled to your deployed graph, and so we can only make them available when we are also deploying the graphs.

## Configuring Assistants[¶](https://langchain-ai.github.io/langgraph/concepts/assistants/#configuring-assistants "Permanent link")

In practice, an assistant is just an _instance_ of a graph with a specific configuration. Because of this, multiple assistants can reference the same graph but can contain different configurations, such as prompts, models, and other graph configuration options. The LangGraph Cloud API provides several endpoints for creating and managing assistants. See the [API reference](https://langchain-ai.github.io/langgraph/cloud/reference/api/api_ref.html) and [this how-to](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/) for more details on how to create assistants.

## Versioning Assistants[¶](https://langchain-ai.github.io/langgraph/concepts/assistants/#versioning-assistants "Permanent link")

Once you've created an assistant, you can save and version it to track changes to the configuration over time. You can think about this at three levels:

1) The graph lays out the general agent application logic 2) The agent configuration options represent parameters that can be changed 3) Assistant versions save and track specific settings of the agent configuration options 

For example, let's imagine you have a general writing agent. You have created a general graph architecture that works well for writing. However, there are different types of writing, e.g. blogs vs tweets. In order to get the best performance on each use case, you need to make some minor changes to the models and prompts used. In this setup, you could create an assistant for each use case - one for blog writing and one for tweeting. These would share the same graph structure, but they may use different models and different prompts. Read [this how-to](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/) to learn how you can use assistant versioning through both the [Studio](https://langchain-ai.github.io/langgraph/concepts/langgraph_studio/) and the SDK.

![assistant versions](https://langchain-ai.github.io/langgraph/concepts/img/assistants.png)

## Resources[¶](https://langchain-ai.github.io/langgraph/concepts/assistants/#resources "Permanent link")

For more information on assistants, see the following resources:

  * [Assistants how-to guides](https://langchain-ai.github.io/langgraph/how-tos/#assistants)

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Application Structure  ](https://langchain-ai.github.io/langgraph/concepts/application_structure/) [ Next  Double Texting  ](https://langchain-ai.github.io/langgraph/concepts/double_texting/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/concepts/assistants/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
