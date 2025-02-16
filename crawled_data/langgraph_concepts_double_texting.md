---
url: https://langchain-ai.github.io/langgraph/concepts/double_texting/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/concepts/double_texting/#double-texting)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Double Texting 

[ ](https://langchain-ai.github.io/langgraph/concepts/double_texting/?q= "Share")

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
            * [ Assistants  ](https://langchain-ai.github.io/langgraph/concepts/assistants/)
            * Double Texting  [ Double Texting  ](https://langchain-ai.github.io/langgraph/concepts/double_texting/) Table of contents 
              * [ Reject  ](https://langchain-ai.github.io/langgraph/concepts/double_texting/#reject)
              * [ Enqueue  ](https://langchain-ai.github.io/langgraph/concepts/double_texting/#enqueue)
              * [ Interrupt  ](https://langchain-ai.github.io/langgraph/concepts/double_texting/#interrupt)
              * [ Rollback  ](https://langchain-ai.github.io/langgraph/concepts/double_texting/#rollback)
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

  * [ Reject  ](https://langchain-ai.github.io/langgraph/concepts/double_texting/#reject)
  * [ Enqueue  ](https://langchain-ai.github.io/langgraph/concepts/double_texting/#enqueue)
  * [ Interrupt  ](https://langchain-ai.github.io/langgraph/concepts/double_texting/#interrupt)
  * [ Rollback  ](https://langchain-ai.github.io/langgraph/concepts/double_texting/#rollback)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ Concepts  ](https://langchain-ai.github.io/langgraph/concepts/)
  4. [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/concepts#langgraph-platform)
  5. [ LangGraph Server  ](https://langchain-ai.github.io/langgraph/concepts#langgraph-server)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/concepts/double_texting.md "Edit this page")

# Double Texting[¶](https://langchain-ai.github.io/langgraph/concepts/double_texting/#double-texting "Permanent link")

Prerequisites

  * [LangGraph Server](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/)



Many times users might interact with your graph in unintended ways. For instance, a user may send one message and before the graph has finished running send a second message. More generally, users may invoke the graph a second time before the first run has finished. We call this "double texting".

Currently, LangGraph only addresses this as part of [LangGraph Platform](https://langchain-ai.github.io/langgraph/concepts/langgraph_platform/), not in the open source. The reason for this is that in order to handle this we need to know how the graph is deployed, and since LangGraph Platform deals with deployment the logic needs to live there. If you do not want to use LangGraph Platform, we describe the options we have implemented in detail below.

![](https://langchain-ai.github.io/langgraph/concepts/img/double_texting.png)

## Reject[¶](https://langchain-ai.github.io/langgraph/concepts/double_texting/#reject "Permanent link")

This is the simplest option, this just rejects any follow-up runs and does not allow double texting. See the [how-to guide](https://langchain-ai.github.io/langgraph/cloud/how-tos/reject_concurrent/) for configuring the reject double text option.

## Enqueue[¶](https://langchain-ai.github.io/langgraph/concepts/double_texting/#enqueue "Permanent link")

This is a relatively simple option which continues the first run until it completes the whole run, then sends the new input as a separate run. See the [how-to guide](https://langchain-ai.github.io/langgraph/cloud/how-tos/enqueue_concurrent/) for configuring the enqueue double text option.

## Interrupt[¶](https://langchain-ai.github.io/langgraph/concepts/double_texting/#interrupt "Permanent link")

This option interrupts the current execution but saves all the work done up until that point. It then inserts the user input and continues from there. 

If you enable this option, your graph should be able to handle weird edge cases that may arise. For example, you could have called a tool but not yet gotten back a result from running that tool. You may need to remove that tool call in order to not have a dangling tool call.

See the [how-to guide](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/) for configuring the interrupt double text option.

## Rollback[¶](https://langchain-ai.github.io/langgraph/concepts/double_texting/#rollback "Permanent link")

This option interrupts the current execution AND rolls back all work done up until that point, including the original run input. It then sends the new user input in, basically as if it was the original input.

See the [how-to guide](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/) for configuring the rollback double text option.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Assistants  ](https://langchain-ai.github.io/langgraph/concepts/assistants/) [ Next  Authentication & Access Control  ](https://langchain-ai.github.io/langgraph/concepts/auth/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/concepts/double_texting/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
