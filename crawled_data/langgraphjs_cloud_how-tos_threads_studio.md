---
url: https://langchain-ai.github.io/langgraphjs/cloud/how-tos/threads_studio/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/threads_studio/#interacting-with-threads-in-studio)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

Interacting with Threads in Studio 

[ ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/threads_studio/?q= "Share")

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

How-to Guides 
        * [ Installation  ](https://langchain-ai.github.io/langgraphjs/how-tos#installation)
        * [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
        * LangGraph Platform  LangGraph Platform 
          * [ LangGraph Platform  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph-platform)
          * [ Application Structure  ](https://langchain-ai.github.io/langgraphjs/how-tos#application-structure)
          * [ Deployment  ](https://langchain-ai.github.io/langgraphjs/how-tos#deployment)
          * [ Authentication & Access Control  ](https://langchain-ai.github.io/langgraphjs/how-tos#authentication-access-control)
          * [ Assistants  ](https://langchain-ai.github.io/langgraphjs/how-tos#assistants)
          * [ Threads  ](https://langchain-ai.github.io/langgraphjs/how-tos#threads)
          * [ Runs  ](https://langchain-ai.github.io/langgraphjs/how-tos#runs)
          * [ Streaming  ](https://langchain-ai.github.io/langgraphjs/how-tos#streaming_1)
          * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraphjs/how-tos#human-in-the-loop_1)
          * [ Double-texting  ](https://langchain-ai.github.io/langgraphjs/how-tos#double-texting)
          * [ Webhooks  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/webhooks/)
          * [ Cron Jobs  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/cron_jobs/)
          * LangGraph Studio  LangGraph Studio 
            * [ LangGraph Studio  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph-studio)
            * [ Test Cloud Deployment  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/test_deployment/)
            * [ LangGraph Studio With Local Deployment  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/test_local_deployment/)
            * [ Invoke Assistant  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/invoke_studio/)
            * Interacting with Threads in Studio  [ Interacting with Threads in Studio  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/threads_studio/) Table of contents 
              * [ View Thread  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/threads_studio/#view-thread)
              * [ Edit Thread State  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/threads_studio/#edit-thread-state)
            * [ Adding nodes as dataset examples in Studio  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/datasets_studio/)
      * [ Concepts  ](https://langchain-ai.github.io/langgraphjs/concepts/)
      * [ Tutorials  ](https://langchain-ai.github.io/langgraphjs/tutorials/)
    * Resources  Resources 
      * [ Adopters  ](https://langchain-ai.github.io/langgraphjs/adopters/)
      * [ FAQ  ](https://langchain-ai.github.io/langgraphjs/concepts/faq/)
      * [ Troubleshooting  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraphjs/reference/)
  * [ Versions  ](https://langchain-ai.github.io/langgraphjs/versions/)



Table of contents 

  * [ View Thread  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/threads_studio/#view-thread)
  * [ Edit Thread State  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/threads_studio/#edit-thread-state)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph Platform  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph-platform)
  5. [ LangGraph Studio  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph-studio)



# Interacting with Threads in Studio[¶](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/threads_studio/#interacting-with-threads-in-studio "Permanent link")

## View Thread[¶](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/threads_studio/#view-thread "Permanent link")

  1. In the top of the right-hand pane, select the `New Thread` dropdown menu to view existing threads.
  2. View the state of the thread (i.e. the output) in the right-hand pane.
  3. To create a new thread, select `+ New Thread`.



The following video shows these exact steps being carried out:

## Edit Thread State[¶](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/threads_studio/#edit-thread-state "Permanent link")

The LangGraph Studio UI contains features for editing thread state. Explore these features in the right-hand pane. Select the `Edit` icon, modify the desired state, and then select `Fork` to invoke the assistant with the updated state.

The following video shows how to edit a thread in the studio:

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  Invoke Assistant  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/invoke_studio/) [ Next  Adding nodes as dataset examples in Studio  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/datasets_studio/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/threads_studio/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
