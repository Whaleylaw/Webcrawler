---
url: https://langchain-ai.github.io/langgraph/cloud/how-tos/test_local_deployment/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/cloud/how-tos/test_local_deployment/#langgraph-studio-with-local-deployment)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

LangGraph Studio With Local Deployment 

[ ](https://langchain-ai.github.io/langgraph/cloud/how-tos/test_local_deployment/?q= "Share")

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
            * LangGraph Studio With Local Deployment  [ LangGraph Studio With Local Deployment  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/test_local_deployment/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/test_local_deployment/#setup)
              * [ Access Studio  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/test_local_deployment/#access-studio)
              * [ Use the Studio for Testing  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/test_local_deployment/#use-the-studio-for-testing)
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



Table of contents 

  * [ Setup  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/test_local_deployment/#setup)
  * [ Access Studio  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/test_local_deployment/#access-studio)
  * [ Use the Studio for Testing  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/test_local_deployment/#use-the-studio-for-testing)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph-platform)
  5. [ LangGraph Studio  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph-studio)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/cloud/how-tos/test_local_deployment.md "Edit this page")

# LangGraph Studio With Local Deployment[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/test_local_deployment/#langgraph-studio-with-local-deployment "Permanent link")

Browser Compatibility

Viewing the studio page of a local LangGraph deployment does not work in Safari. Use Chrome instead.

## Setup[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/test_local_deployment/#setup "Permanent link")

Make sure you have setup your app correctly, by creating a compiled graph, a `.env` file with any environment variables, and a `langgraph.json` config file that points to your environment file and compiled graph. See [here](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/) for more detailed instructions.

After you have your app setup, head into the directory with your `langgraph.json` file and call `langgraph dev` to start the API server in watch mode which means it will restart on code changes, which is ideal for local testing. If the API server start correctly you should see logs that look something like this:

> Ready!
> 
>   * API: [http://localhost:2024](http://localhost:2024/)
> 
>   * Docs: <http://localhost:2024/docs>
> 
>   * LangGraph Studio Web UI: <https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024>
> 
> 


Read this [reference](https://langchain-ai.github.io/langgraph/cloud/reference/cli/#up) to learn about all the options for starting the API server.

## Access Studio[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/test_local_deployment/#access-studio "Permanent link")

Once you have successfully started the API server, you can access the studio by going to the following URL: `https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024` (see warning above if using Safari).

If everything is working correctly you should see the studio show up looking something like this (with your graph diagram on the left hand side):

![LangGraph Studio](https://langchain-ai.github.io/langgraph/cloud/how-tos/img/studio_screenshot.png)

## Use the Studio for Testing[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/test_local_deployment/#use-the-studio-for-testing "Permanent link")

To learn about how to use the studio for testing, read the [LangGraph Studio how-tos](https://langchain-ai.github.io/langgraph/cloud/how-tos/#langgraph-studio).

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Test Cloud Deployment  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/test_deployment/) [ Next  Invoke Assistant  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/invoke_studio/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/cloud/how-tos/test_local_deployment/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
