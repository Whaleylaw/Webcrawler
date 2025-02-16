---
url: https://langchain-ai.github.io/langgraph/cloud/deployment/custom_docker/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/cloud/deployment/custom_docker/#how-to-customize-dockerfile)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to customize Dockerfile 

[ ](https://langchain-ai.github.io/langgraph/cloud/deployment/custom_docker/?q= "Share")

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
          * Application Structure  Application Structure 
            * [ Application Structure  ](https://langchain-ai.github.io/langgraph/how-tos#application-structure)
            * [ How to Set Up a LangGraph Application for Deployment  ](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/)
            * [ How to Set Up a LangGraph Application for Deployment  ](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_pyproject/)
            * [ How to Set Up a LangGraph.js Application for Deployment  ](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/)
            * [ How to add semantic search to your LangGraph deployment  ](https://langchain-ai.github.io/langgraph/cloud/deployment/semantic_search/)
            * [ How to customize Dockerfile  ](https://langchain-ai.github.io/langgraph/cloud/deployment/custom_docker/)
            * [ How to test a LangGraph app locally  ](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/)
            * [ Rebuild Graph at Runtime  ](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/)
            * [ How to use LangGraph Platform to deploy CrewAI, AutoGen, and other frameworks  ](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/)
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
          * [ LangGraph Studio  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph-studio)
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
  5. [ Application Structure  ](https://langchain-ai.github.io/langgraph/how-tos#application-structure)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/cloud/deployment/custom_docker.md "Edit this page")

# How to customize Dockerfile[¶](https://langchain-ai.github.io/langgraph/cloud/deployment/custom_docker/#how-to-customize-dockerfile "Permanent link")

Users can add an array of additional lines to add to the Dockerfile following the import from the parent LangGraph image. In order to do this, you simply need to modify your `langgraph.json` file by passing in the commands you want run to the `dockerfile_lines` key. For example, if we wanted to use `Pillow` in our graph you would need to add the following dependencies:

```
[](https://langchain-ai.github.io/langgraph/cloud/deployment/custom_docker/#__codelineno-0-1){
[](https://langchain-ai.github.io/langgraph/cloud/deployment/custom_docker/#__codelineno-0-2)  "dependencies": ["."],
[](https://langchain-ai.github.io/langgraph/cloud/deployment/custom_docker/#__codelineno-0-3)  "graphs": {
[](https://langchain-ai.github.io/langgraph/cloud/deployment/custom_docker/#__codelineno-0-4)    "openai_agent": "./openai_agent.py:agent",
[](https://langchain-ai.github.io/langgraph/cloud/deployment/custom_docker/#__codelineno-0-5)  },
[](https://langchain-ai.github.io/langgraph/cloud/deployment/custom_docker/#__codelineno-0-6)  "env": "./.env",
[](https://langchain-ai.github.io/langgraph/cloud/deployment/custom_docker/#__codelineno-0-7)  "dockerfile_lines": [
[](https://langchain-ai.github.io/langgraph/cloud/deployment/custom_docker/#__codelineno-0-8)    "RUN apt-get update && apt-get install -y libjpeg-dev zlib1g-dev libpng-dev",
[](https://langchain-ai.github.io/langgraph/cloud/deployment/custom_docker/#__codelineno-0-9)    "RUN pip install Pillow"
[](https://langchain-ai.github.io/langgraph/cloud/deployment/custom_docker/#__codelineno-0-10)  ]
[](https://langchain-ai.github.io/langgraph/cloud/deployment/custom_docker/#__codelineno-0-11)}

```


This would install the system packages required to use Pillow if we were working with `jpeq` or `png` image formats. 

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to add semantic search to your LangGraph deployment  ](https://langchain-ai.github.io/langgraph/cloud/deployment/semantic_search/) [ Next  How to test a LangGraph app locally  ](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/cloud/deployment/custom_docker/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
