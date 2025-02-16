---
url: https://langchain-ai.github.io/langgraphjs/cloud/how-tos/datasets_studio/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/datasets_studio/#adding-nodes-as-dataset-examples-in-studio)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

Adding nodes as dataset examples in Studio 

[ ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/datasets_studio/?q= "Share")

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
            * [ Interacting with Threads in Studio  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/threads_studio/)
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



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph Platform  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph-platform)
  5. [ LangGraph Studio  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph-studio)



# Adding nodes as dataset examples in Studio[¶](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/datasets_studio/#adding-nodes-as-dataset-examples-in-studio "Permanent link")

In LangGraph Studio you can create dataset examples from the thread history in the right-hand pane. This can be especially useful when you want to evaluate intermediate steps of the agent.

  1. Click on the `Add to Dataset` button to enter the dataset mode.
  2. Select nodes which you want to add to dataset.
  3. Select the target dataset to create the example in.



You can edit the example payload before sending it to the dataset, which is useful if you need to make changes to conform the example to the dataset schema.

Finally, you can customise the target dataset by clicking on the `Settings` button.

See [Evaluating intermediate steps](https://docs.smith.langchain.com/evaluation/how_to_guides/langgraph#evaluating-intermediate-steps) for more details on how to evaluate intermediate steps.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  Interacting with Threads in Studio  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/threads_studio/) [ Next  Concepts  ](https://langchain-ai.github.io/langgraphjs/concepts/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/datasets_studio/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
