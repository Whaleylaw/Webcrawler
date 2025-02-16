---
url: https://langchain-ai.github.io/langgraphjs/concepts/faq/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/concepts/faq/#faq)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

FAQ 

[ ](https://langchain-ai.github.io/langgraphjs/concepts/faq/?q= "Share")

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
      * [ Tutorials  ](https://langchain-ai.github.io/langgraphjs/tutorials/)
    * Resources  Resources 
      * [ Adopters  ](https://langchain-ai.github.io/langgraphjs/adopters/)
      * FAQ  [ FAQ  ](https://langchain-ai.github.io/langgraphjs/concepts/faq/) Table of contents 
        * [ Do I need to use LangChain in order to use LangGraph?  ](https://langchain-ai.github.io/langgraphjs/concepts/faq/#do-i-need-to-use-langchain-in-order-to-use-langgraph)
        * [ Does LangGraph work with LLMs that don't support tool calling?  ](https://langchain-ai.github.io/langgraphjs/concepts/faq/#does-langgraph-work-with-llms-that-dont-support-tool-calling)
        * [ Does LangGraph work with OSS LLMs?  ](https://langchain-ai.github.io/langgraphjs/concepts/faq/#does-langgraph-work-with-oss-llms)
      * [ Troubleshooting  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraphjs/reference/)
  * [ Versions  ](https://langchain-ai.github.io/langgraphjs/versions/)



Table of contents 

  * [ Do I need to use LangChain in order to use LangGraph?  ](https://langchain-ai.github.io/langgraphjs/concepts/faq/#do-i-need-to-use-langchain-in-order-to-use-langgraph)
  * [ Does LangGraph work with LLMs that don't support tool calling?  ](https://langchain-ai.github.io/langgraphjs/concepts/faq/#does-langgraph-work-with-llms-that-dont-support-tool-calling)
  * [ Does LangGraph work with OSS LLMs?  ](https://langchain-ai.github.io/langgraphjs/concepts/faq/#does-langgraph-work-with-oss-llms)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Resources  ](https://langchain-ai.github.io/langgraphjs/adopters/)



# FAQ[¶](https://langchain-ai.github.io/langgraphjs/concepts/faq/#faq "Permanent link")

Common questions and their answers!

## Do I need to use LangChain in order to use LangGraph?[¶](https://langchain-ai.github.io/langgraphjs/concepts/faq/#do-i-need-to-use-langchain-in-order-to-use-langgraph "Permanent link")

No! LangGraph is a general-purpose framework - the nodes and edges are nothing more than JavaScript/TypeScript functions. You can use LangChain, raw HTTP requests, or even other frameworks inside these nodes and edges.

## Does LangGraph work with LLMs that don't support tool calling?[¶](https://langchain-ai.github.io/langgraphjs/concepts/faq/#does-langgraph-work-with-llms-that-dont-support-tool-calling "Permanent link")

Yes! You can use LangGraph with any LLMs. The main reason we use LLMs that support tool calling is that this is often the most convenient way to have the LLM make its decision about what to do. If your LLM does not support tool calling, you can still use it - you just need to write a bit of logic to convert the raw LLM string response to a decision about what to do.

## Does LangGraph work with OSS LLMs?[¶](https://langchain-ai.github.io/langgraphjs/concepts/faq/#does-langgraph-work-with-oss-llms "Permanent link")

Yes! LangGraph is totally ambivalent to what LLMs are used under the hood. The main reason we use closed LLMs in most of the tutorials is that they seamlessly support tool calling, while OSS LLMs often don't. But tool calling is not necessary (see [this section](https://langchain-ai.github.io/langgraphjs/concepts/faq/#does-langgraph-work-with-llms-that-dont-support-tool-calling)) so you can totally use LangGraph with OSS LLMs.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  Adopters  ](https://langchain-ai.github.io/langgraphjs/adopters/) [ Next  Error reference  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/concepts/faq/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
