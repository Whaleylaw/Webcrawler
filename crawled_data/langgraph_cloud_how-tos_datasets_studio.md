---
url: https://langchain-ai.github.io/langgraph/cloud/how-tos/datasets_studio/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/cloud/how-tos/datasets_studio/#adding-nodes-as-dataset-examples-in-studio)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Adding nodes as dataset examples in Studio 

[ ](https://langchain-ai.github.io/langgraph/cloud/how-tos/datasets_studio/?q= "Share")

Initializing search 

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
            * [ Interacting with Threads in Studio  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/threads_studio/)
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



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph-platform)
  5. [ LangGraph Studio  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph-studio)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/cloud/how-tos/datasets_studio.md "Edit this page")

# Adding nodes as dataset examples in Studio[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/datasets_studio/#adding-nodes-as-dataset-examples-in-studio "Permanent link")

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

## Comments

Back to top  [ Previous  Interacting with Threads in Studio  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/threads_studio/) [ Next  Concepts  ](https://langchain-ai.github.io/langgraph/concepts/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/cloud/how-tos/datasets_studio/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
