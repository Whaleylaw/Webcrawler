---
url: https://langchain-ai.github.io/langgraph/cloud/how-tos/threads_studio/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/cloud/how-tos/threads_studio/#interacting-with-threads-in-studio)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Interacting with Threads in Studio 

[ ](https://langchain-ai.github.io/langgraph/cloud/how-tos/threads_studio/?q= "Share")

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

How-to Guides 
        * [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
        * LangGraph Platform  LangGraph Platform 
          * [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph-platform)
          * [ Application Structure  ](https://langchain-ai.github.io/langgraph/how-tos#application-structure)
          * [ Deployment  ](https://langchain-ai.github.io/langgraph/how-tos#deployment)
          * [ Authentication & Access Control  ](https://langchain-ai.github.io/langgraph/how-tos#authentication-access-control)
          * [ Assistants  ](https://langchain-ai.github.io/langgraph/how-tos#assistants)
          * [ Threads  ](https://langchain-ai.github.io/langgraph/how-tos#threads)
          * [ Runs  ](https://langchain-ai.github.io/langgraph/how-tos#runs)
          * [ Streaming  ](https://langchain-ai.github.io/langgraph/how-tos#streaming_1)
          * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraph/how-tos#human-in-the-loop_1)
          * [ Double-texting  ](https://langchain-ai.github.io/langgraph/how-tos#double-texting)
          * [ Webhooks  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/webhooks/)
          * [ Cron Jobs  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/cron_jobs/)
          * LangGraph Studio  LangGraph Studio 
            * [ LangGraph Studio  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph-studio)
            * [ Test Cloud Deployment  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/test_deployment/)
            * [ LangGraph Studio With Local Deployment  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/test_local_deployment/)
            * [ Invoke Assistant  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/invoke_studio/)
            * Interacting with Threads in Studio  [ Interacting with Threads in Studio  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/threads_studio/) Table of contents 
              * [ View Thread  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/threads_studio/#view-thread)
              * [ Edit Thread State  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/threads_studio/#edit-thread-state)
            * [ Adding nodes as dataset examples in Studio  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/datasets_studio/)
      * [ Concepts  ](https://langchain-ai.github.io/langgraph/concepts/)
      * [ Tutorials  ](https://langchain-ai.github.io/langgraph/tutorials/)
    * Resources  Resources 
      * [ Prebuilt Agents  ](https://langchain-ai.github.io/langgraph/prebuilt/)
      * [ Adopters  ](https://langchain-ai.github.io/langgraph/adopters/)
      * [ FAQ  ](https://langchain-ai.github.io/langgraph/concepts/faq/)
      * [ Troubleshooting  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraph/reference/graphs/)



Table of contents 

  * [ View Thread  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/threads_studio/#view-thread)
  * [ Edit Thread State  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/threads_studio/#edit-thread-state)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph-platform)
  5. [ LangGraph Studio  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph-studio)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/cloud/how-tos/threads_studio.md "Edit this page")

# Interacting with Threads in Studio[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/threads_studio/#interacting-with-threads-in-studio "Permanent link")

## View Thread[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/threads_studio/#view-thread "Permanent link")

  1. In the top of the right-hand pane, select the `New Thread` dropdown menu to view existing threads.
  2. View the state of the thread (i.e. the output) in the right-hand pane.
  3. To create a new thread, select `+ New Thread`.



The following video shows these exact steps being carried out:

## Edit Thread State[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/threads_studio/#edit-thread-state "Permanent link")

The LangGraph Studio UI contains features for editing thread state. Explore these features in the right-hand pane. Select the `Edit` icon, modify the desired state, and then select `Fork` to invoke the assistant with the updated state.

The following video shows how to edit a thread in the studio:

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Invoke Assistant  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/invoke_studio/) [ Next  Adding nodes as dataset examples in Studio  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/datasets_studio/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/cloud/how-tos/threads_studio/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
