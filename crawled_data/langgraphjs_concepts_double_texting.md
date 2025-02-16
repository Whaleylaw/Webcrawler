---
url: https://langchain-ai.github.io/langgraphjs/concepts/double_texting
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/concepts/double_texting/#double-texting)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

Double Texting 

[ ](https://langchain-ai.github.io/langgraphjs/concepts/double_texting/?q= "Share")

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
          * LangGraph Server  LangGraph Server 
            * [ LangGraph Server  ](https://langchain-ai.github.io/langgraphjs/concepts#langgraph-server)
            * [ Application Structure  ](https://langchain-ai.github.io/langgraphjs/concepts/application_structure/)
            * [ Assistants  ](https://langchain-ai.github.io/langgraphjs/concepts/assistants/)
            * Double Texting  [ Double Texting  ](https://langchain-ai.github.io/langgraphjs/concepts/double_texting/) Table of contents 
              * [ Reject  ](https://langchain-ai.github.io/langgraphjs/concepts/double_texting/#reject)
              * [ Enqueue  ](https://langchain-ai.github.io/langgraphjs/concepts/double_texting/#enqueue)
              * [ Interrupt  ](https://langchain-ai.github.io/langgraphjs/concepts/double_texting/#interrupt)
              * [ Rollback  ](https://langchain-ai.github.io/langgraphjs/concepts/double_texting/#rollback)
          * [ Deployment Options  ](https://langchain-ai.github.io/langgraphjs/concepts#deployment-options)
      * [ Tutorials  ](https://langchain-ai.github.io/langgraphjs/tutorials/)
    * Resources  Resources 
      * [ Adopters  ](https://langchain-ai.github.io/langgraphjs/adopters/)
      * [ FAQ  ](https://langchain-ai.github.io/langgraphjs/concepts/faq/)
      * [ Troubleshooting  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraphjs/reference/)
  * [ Versions  ](https://langchain-ai.github.io/langgraphjs/versions/)



Table of contents 

  * [ Reject  ](https://langchain-ai.github.io/langgraphjs/concepts/double_texting/#reject)
  * [ Enqueue  ](https://langchain-ai.github.io/langgraphjs/concepts/double_texting/#enqueue)
  * [ Interrupt  ](https://langchain-ai.github.io/langgraphjs/concepts/double_texting/#interrupt)
  * [ Rollback  ](https://langchain-ai.github.io/langgraphjs/concepts/double_texting/#rollback)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ Concepts  ](https://langchain-ai.github.io/langgraphjs/concepts/)
  4. [ LangGraph Platform  ](https://langchain-ai.github.io/langgraphjs/concepts#langgraph-platform)
  5. [ LangGraph Server  ](https://langchain-ai.github.io/langgraphjs/concepts#langgraph-server)



# Double Texting[¶](https://langchain-ai.github.io/langgraphjs/concepts/double_texting/#double-texting "Permanent link")

Prerequisites

  * [LangGraph Server](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_server/)



Many times users might interact with your graph in unintended ways. For instance, a user may send one message and before the graph has finished running send a second message. More generally, users may invoke the graph a second time before the first run has finished. We call this "double texting".

Currently, LangGraph only addresses this as part of [LangGraph Platform](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_platform/), not in the open source. The reason for this is that in order to handle this we need to know how the graph is deployed, and since LangGraph Platform deals with deployment the logic needs to live there. If you do not want to use LangGraph Platform, we describe the options we have implemented in detail below.

![](https://langchain-ai.github.io/langgraphjs/concepts/img/double_texting.png)

## Reject[¶](https://langchain-ai.github.io/langgraphjs/concepts/double_texting/#reject "Permanent link")

This is the simplest option, this just rejects any follow up runs and does not allow double texting. See the [how-to guide](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/reject_concurrent) for configuring the reject double text option.

## Enqueue[¶](https://langchain-ai.github.io/langgraphjs/concepts/double_texting/#enqueue "Permanent link")

This is a relatively simple option which continues the first run until it completes the whole run, then sends the new input as a separate run. See the [how-to guide](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/enqueue_concurrent) for configuring the enqueue double text option.

## Interrupt[¶](https://langchain-ai.github.io/langgraphjs/concepts/double_texting/#interrupt "Permanent link")

This option interrupts the current execution but saves all the work done up until that point. It then inserts the user input and continues from there.

If you enable this option, your graph should be able to handle weird edge cases that may arise. For example, you could have called a tool but not yet gotten back a result from running that tool. You may need to remove that tool call in order to not have a dangling tool call.

See the [how-to guide](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/interrupt_concurrent) for configuring the interrupt double text option.

## Rollback[¶](https://langchain-ai.github.io/langgraphjs/concepts/double_texting/#rollback "Permanent link")

This option rolls back all work done up until that point. It then sends the user input in, basically as if it just followed the original run input.

This may create some weird states - for example, you may have two `User` messages in a row, with no `Assistant` message in between them.

You will need to make sure the LLM you are calling can handle that, or combine those into a single `User` message.

See the [how-to guide](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/rollback_concurrent) for configuring the rollback double text option.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  Assistants  ](https://langchain-ai.github.io/langgraphjs/concepts/assistants/) [ Next  Self-Hosted  ](https://langchain-ai.github.io/langgraphjs/concepts/self_hosted/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/concepts/double_texting/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
