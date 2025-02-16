---
url: https://langchain-ai.github.io/langgraph/concepts/sdk
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/concepts/sdk/#langgraph-sdk)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

LangGraph SDK 

[ ](https://langchain-ai.github.io/langgraph/concepts/sdk/?q= "Share")

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
      * [ Concepts  ](https://langchain-ai.github.io/langgraph/concepts/)

Concepts 
        * [ LangGraph  ](https://langchain-ai.github.io/langgraph/concepts#langgraph)
        * LangGraph Platform  LangGraph Platform 
          * [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/concepts#langgraph-platform)
          * [ High Level  ](https://langchain-ai.github.io/langgraph/concepts#high-level)
          * Components  Components 
            * [ Components  ](https://langchain-ai.github.io/langgraph/concepts#components)
            * [ LangGraph Server  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/)
            * [ LangGraph Studio  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_studio/)
            * [ LangGraph CLI  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_cli/)
            * LangGraph SDK  [ LangGraph SDK  ](https://langchain-ai.github.io/langgraph/concepts/sdk/) Table of contents 
              * [ Installation  ](https://langchain-ai.github.io/langgraph/concepts/sdk/#installation)
              * [ API Reference  ](https://langchain-ai.github.io/langgraph/concepts/sdk/#api-reference)
              * [ Python Sync vs. Async  ](https://langchain-ai.github.io/langgraph/concepts/sdk/#python-sync-vs-async)
              * [ Related  ](https://langchain-ai.github.io/langgraph/concepts/sdk/#related)
            * [ How to interact with the deployment using RemoteGraph  ](https://langchain-ai.github.io/langgraph/how-tos/use-remote-graph/)
          * [ LangGraph Server  ](https://langchain-ai.github.io/langgraph/concepts#langgraph-server)
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

  * [ Installation  ](https://langchain-ai.github.io/langgraph/concepts/sdk/#installation)
  * [ API Reference  ](https://langchain-ai.github.io/langgraph/concepts/sdk/#api-reference)
  * [ Python Sync vs. Async  ](https://langchain-ai.github.io/langgraph/concepts/sdk/#python-sync-vs-async)
  * [ Related  ](https://langchain-ai.github.io/langgraph/concepts/sdk/#related)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ Concepts  ](https://langchain-ai.github.io/langgraph/concepts/)
  4. [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/concepts#langgraph-platform)
  5. [ Components  ](https://langchain-ai.github.io/langgraph/concepts#components)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/concepts/sdk.md "Edit this page")

# LangGraph SDK[¶](https://langchain-ai.github.io/langgraph/concepts/sdk/#langgraph-sdk "Permanent link")

Prerequisites

  * [LangGraph Platform](https://langchain-ai.github.io/langgraph/concepts/langgraph_platform/)
  * [LangGraph Server](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/)



The LangGraph Platform provides both a Python and JS SDK for interacting with the [LangGraph Server API](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/). 

## Installation[¶](https://langchain-ai.github.io/langgraph/concepts/sdk/#installation "Permanent link")

You can install the packages using the appropriate package manager for your language.

[Python](#__tabbed_1_1)[JS](#__tabbed_1_2)

```
[](https://langchain-ai.github.io/langgraph/concepts/sdk/#__codelineno-0-1)pipinstalllanggraph-sdk

```


```
[](https://langchain-ai.github.io/langgraph/concepts/sdk/#__codelineno-1-1)yarnadd@langchain/langgraph-sdk

```


## API Reference[¶](https://langchain-ai.github.io/langgraph/concepts/sdk/#api-reference "Permanent link")

You can find the API reference for the SDKs here:

  * [Python SDK Reference](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/)
  * [JS/TS SDK Reference](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/)



## Python Sync vs. Async[¶](https://langchain-ai.github.io/langgraph/concepts/sdk/#python-sync-vs-async "Permanent link")

The Python SDK provides both synchronous (`get_sync_client`) and asynchronous (`get_client`) clients for interacting with the LangGraph Server API.

[Async](#__tabbed_2_1)[Sync](#__tabbed_2_2)

```
[](https://langchain-ai.github.io/langgraph/concepts/sdk/#__codelineno-2-1)fromlanggraph_sdkimport get_client
[](https://langchain-ai.github.io/langgraph/concepts/sdk/#__codelineno-2-2)
[](https://langchain-ai.github.io/langgraph/concepts/sdk/#__codelineno-2-3)client = get_client(url=..., api_key=...)
[](https://langchain-ai.github.io/langgraph/concepts/sdk/#__codelineno-2-4)await client.assistants.search()

```


```
[](https://langchain-ai.github.io/langgraph/concepts/sdk/#__codelineno-3-1)fromlanggraph_sdkimport get_sync_client
[](https://langchain-ai.github.io/langgraph/concepts/sdk/#__codelineno-3-2)
[](https://langchain-ai.github.io/langgraph/concepts/sdk/#__codelineno-3-3)client = get_sync_client(url=..., api_key=...)
[](https://langchain-ai.github.io/langgraph/concepts/sdk/#__codelineno-3-4)client.assistants.search()

```


## Related[¶](https://langchain-ai.github.io/langgraph/concepts/sdk/#related "Permanent link")

  * [LangGraph CLI API Reference](https://langchain-ai.github.io/langgraph/cloud/reference/cli/)
  * [Python SDK Reference](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/)
  * [JS/TS SDK Reference](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/)

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  LangGraph CLI  ](https://langchain-ai.github.io/langgraph/concepts/langgraph_cli/) [ Next  How to interact with the deployment using RemoteGraph  ](https://langchain-ai.github.io/langgraph/how-tos/use-remote-graph/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/concepts/sdk/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
