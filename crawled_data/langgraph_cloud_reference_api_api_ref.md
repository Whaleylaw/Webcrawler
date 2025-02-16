---
url: https://langchain-ai.github.io/langgraph/cloud/reference/api/api_ref/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/cloud/reference/api/api_ref/#api-reference)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Server API 

[ ](https://langchain-ai.github.io/langgraph/cloud/reference/api/api_ref/?q= "Share")

Type to start searching

[ GitHub  ](https://github.com/langchain-ai/langgraph "Go to repository")

  * [ Home ](https://langchain-ai.github.io/langgraph/)
  * [ API reference ](https://langchain-ai.github.io/langgraph/reference/graphs/)



[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

[ GitHub  ](https://github.com/langchain-ai/langgraph "Go to repository")

  * [ Home  ](https://langchain-ai.github.io/langgraph/)
  * API reference  API reference 
    * Library  Library 
      * [ Graphs  ](https://langchain-ai.github.io/langgraph/reference/graphs/)
      * [ Checkpointing  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/)
      * [ Storage  ](https://langchain-ai.github.io/langgraph/reference/store/)
      * [ Prebuilt components  ](https://langchain-ai.github.io/langgraph/reference/prebuilt/)
      * [ Channels  ](https://langchain-ai.github.io/langgraph/reference/channels/)
      * [ Errors  ](https://langchain-ai.github.io/langgraph/reference/errors/)
      * [ Types  ](https://langchain-ai.github.io/langgraph/reference/types/)
      * [ Constants  ](https://langchain-ai.github.io/langgraph/reference/constants/)
      * [ Pregel  ](https://langchain-ai.github.io/langgraph/reference/pregel/)
      * [ Config  ](https://langchain-ai.github.io/langgraph/reference/config/)
      * [ Functional API  ](https://langchain-ai.github.io/langgraph/reference/func/)
    * LangGraph Platform  LangGraph Platform 
      * Server API  [ Server API  ](https://langchain-ai.github.io/langgraph/cloud/reference/api/api_ref/) Table of contents 
        * [ Authentication  ](https://langchain-ai.github.io/langgraph/cloud/reference/api/api_ref/#authentication)
      * [ CLI  ](https://langchain-ai.github.io/langgraph/cloud/reference/cli/)
      * [ SDK (Python)  ](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/)
      * [ SDK (JS/TS)  ](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/)
      * [ RemoteGraph  ](https://langchain-ai.github.io/langgraph/reference/remote_graph/)
      * [ Environment variables  ](https://langchain-ai.github.io/langgraph/cloud/reference/env_var/)



Table of contents 

  * [ Authentication  ](https://langchain-ai.github.io/langgraph/cloud/reference/api/api_ref/#authentication)



  1. [ API reference  ](https://langchain-ai.github.io/langgraph/reference/graphs/)
  2. [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/cloud/reference/api/api_ref/)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/cloud/reference/api/api_ref.md "Edit this page")

# API Reference[¶](https://langchain-ai.github.io/langgraph/cloud/reference/api/api_ref/#api-reference "Permanent link")

The LangGraph Cloud API reference is available with each deployment at the `/docs` URL path (e.g. `http://localhost:8124/docs`).

Click [here](https://langchain-ai.github.io/langgraph/cloud/reference/api/api_ref.html) to view the API reference.

## Authentication[¶](https://langchain-ai.github.io/langgraph/cloud/reference/api/api_ref/#authentication "Permanent link")

For deployments to LangGraph Cloud, authentication is required. Pass the `X-Api-Key` header with each request to the LangGraph Cloud API. The value of the header should be set to a valid LangSmith API key for the organization where the API is deployed.

Example `curl` command: 

```
[](https://langchain-ai.github.io/langgraph/cloud/reference/api/api_ref/#__codelineno-0-1)curl--requestPOST\
[](https://langchain-ai.github.io/langgraph/cloud/reference/api/api_ref/#__codelineno-0-2)--urlhttp://localhost:8124/assistants/search\
[](https://langchain-ai.github.io/langgraph/cloud/reference/api/api_ref/#__codelineno-0-3)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraph/cloud/reference/api/api_ref/#__codelineno-0-4)--header'X-Api-Key: LANGSMITH_API_KEY'\
[](https://langchain-ai.github.io/langgraph/cloud/reference/api/api_ref/#__codelineno-0-5)--data'{
[](https://langchain-ai.github.io/langgraph/cloud/reference/api/api_ref/#__codelineno-0-6) "metadata": {},
[](https://langchain-ai.github.io/langgraph/cloud/reference/api/api_ref/#__codelineno-0-7) "limit": 10,
[](https://langchain-ai.github.io/langgraph/cloud/reference/api/api_ref/#__codelineno-0-8) "offset": 0
[](https://langchain-ai.github.io/langgraph/cloud/reference/api/api_ref/#__codelineno-0-9)}'

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Functional API  ](https://langchain-ai.github.io/langgraph/reference/func/) [ Next  CLI  ](https://langchain-ai.github.io/langgraph/cloud/reference/cli/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/cloud/reference/api/api_ref/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
