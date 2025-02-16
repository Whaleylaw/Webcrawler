---
url: https://langchain-ai.github.io/langgraph/concepts/high_level/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/concepts/high_level/#why-langgraph)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Why LangGraph? 

[ ](https://langchain-ai.github.io/langgraph/concepts/high_level/?q= "Share")

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
      * [ Concepts  ](https://langchain-ai.github.io/langgraph/concepts/)

Concepts 
        * LangGraph  LangGraph 
          * [ LangGraph  ](https://langchain-ai.github.io/langgraph/concepts#langgraph)
          * Why LangGraph?  [ Why LangGraph?  ](https://langchain-ai.github.io/langgraph/concepts/high_level/) Table of contents 
            * [ LLM applications  ](https://langchain-ai.github.io/langgraph/concepts/high_level/#llm-applications)
            * [ What LangGraph provides  ](https://langchain-ai.github.io/langgraph/concepts/high_level/#what-langgraph-provides)
              * [ Persistence  ](https://langchain-ai.github.io/langgraph/concepts/high_level/#persistence)
              * [ Streaming  ](https://langchain-ai.github.io/langgraph/concepts/high_level/#streaming)
              * [ Debugging and Deployment  ](https://langchain-ai.github.io/langgraph/concepts/high_level/#debugging-and-deployment)
          * [ LangGraph Glossary  ](https://langchain-ai.github.io/langgraph/concepts/low_level/)
          * [ Agent architectures  ](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/)
          * [ Multi-agent Systems  ](https://langchain-ai.github.io/langgraph/concepts/multi_agent/)
          * [ None  ](https://langchain-ai.github.io/langgraph/concepts/breakpoints)
          * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/)
          * [ Time Travel ⏱️  ](https://langchain-ai.github.io/langgraph/concepts/time-travel/)
          * [ Persistence  ](https://langchain-ai.github.io/langgraph/concepts/persistence/)
          * [ Memory  ](https://langchain-ai.github.io/langgraph/concepts/memory/)
          * [ Streaming  ](https://langchain-ai.github.io/langgraph/concepts/streaming/)
          * [ Functional API  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/)
        * [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/concepts#langgraph-platform)
      * [ Tutorials  ](https://langchain-ai.github.io/langgraph/tutorials/)
    * Resources  Resources 
      * [ Prebuilt Agents  ](https://langchain-ai.github.io/langgraph/prebuilt/)
      * [ Adopters  ](https://langchain-ai.github.io/langgraph/adopters/)
      * [ FAQ  ](https://langchain-ai.github.io/langgraph/concepts/faq/)
      * [ Troubleshooting  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraph/reference/graphs/)



Table of contents 

  * [ LLM applications  ](https://langchain-ai.github.io/langgraph/concepts/high_level/#llm-applications)
  * [ What LangGraph provides  ](https://langchain-ai.github.io/langgraph/concepts/high_level/#what-langgraph-provides)
    * [ Persistence  ](https://langchain-ai.github.io/langgraph/concepts/high_level/#persistence)
    * [ Streaming  ](https://langchain-ai.github.io/langgraph/concepts/high_level/#streaming)
    * [ Debugging and Deployment  ](https://langchain-ai.github.io/langgraph/concepts/high_level/#debugging-and-deployment)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ Concepts  ](https://langchain-ai.github.io/langgraph/concepts/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/concepts#langgraph)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/concepts/high_level.md "Edit this page")

# Why LangGraph?[¶](https://langchain-ai.github.io/langgraph/concepts/high_level/#why-langgraph "Permanent link")

## LLM applications[¶](https://langchain-ai.github.io/langgraph/concepts/high_level/#llm-applications "Permanent link")

LLMs make it possible to embed intelligence into a new class of applications. There are many patterns for building applications that use LLMs. [Workflows](https://www.anthropic.com/research/building-effective-agents) have scaffolding of predefined code paths around LLM calls. LLMs can direct the control flow through these predefined code paths, which some consider to be an "[agentic system](https://www.anthropic.com/research/building-effective-agents)". In other cases, it's possible to remove this scaffolding, creating autonomous agents that can [plan](https://huyenchip.com/2025/01/07/agents.html), take actions via [tool calls](https://python.langchain.com/docs/concepts/tool_calling/), and directly respond [to the feedback from their own actions](https://research.google/blog/react-synergizing-reasoning-and-acting-in-language-models/) with further actions.

![Agent Workflow](https://langchain-ai.github.io/langgraph/concepts/img/agent_workflow.png)

## What LangGraph provides[¶](https://langchain-ai.github.io/langgraph/concepts/high_level/#what-langgraph-provides "Permanent link")

LangGraph provides low-level supporting infrastructure that sits underneath _any_ workflow or agent. It does not abstract prompts or architecture, and provides three central benefits:

### Persistence[¶](https://langchain-ai.github.io/langgraph/concepts/high_level/#persistence "Permanent link")

LangGraph has a [persistence layer](https://langchain-ai.github.io/langgraph/concepts/persistence/), which offers a number of benefits:

  * [Memory](https://langchain-ai.github.io/langgraph/concepts/memory/): LangGraph persists arbitrary aspects of your application's state, supporting memory of conversations and other updates within and across user interactions;
  * [Human-in-the-loop](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/): Because state is checkpointed, execution can be interrupted and resumed, allowing for decisions, validation, and corrections via human input.



### Streaming[¶](https://langchain-ai.github.io/langgraph/concepts/high_level/#streaming "Permanent link")

LangGraph also provides support for [streaming](https://langchain-ai.github.io/langgraph/how-tos/#streaming) workflow / agent state to the user (or developer) over the course of execution. LangGraph supports streaming of both events ([such as feedback from a tool call](https://langchain-ai.github.io/langgraph/how-tos/streaming/#updates)) and [tokens from LLM calls](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/) embedded in an application.

### Debugging and Deployment[¶](https://langchain-ai.github.io/langgraph/concepts/high_level/#debugging-and-deployment "Permanent link")

LangGraph provides an easy onramp for testing, debugging, and deploying applications via [LangGraph Platform](https://langchain-ai.github.io/langgraph/concepts/langgraph_platform/). This includes [Studio](https://langchain-ai.github.io/langgraph/concepts/langgraph_studio/), an IDE that enables visualization, interaction, and debugging of workflows or agents. This also includes numerous [options](https://langchain-ai.github.io/langgraph/tutorials/deployment/) for deployment. 

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Concepts  ](https://langchain-ai.github.io/langgraph/concepts/) [ Next  LangGraph Glossary  ](https://langchain-ai.github.io/langgraph/concepts/low_level/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/concepts/high_level/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
