---
url: https://langchain-ai.github.io/langgraphjs/concepts/high_level/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/concepts/high_level/#why-langgraph)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

Why LangGraph? 

[ ](https://langchain-ai.github.io/langgraphjs/concepts/high_level/?q= "Share")

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

Concepts 
        * LangGraph  LangGraph 
          * [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/concepts#langgraph)
          * Why LangGraph?  [ Why LangGraph?  ](https://langchain-ai.github.io/langgraphjs/concepts/high_level/) Table of contents 
            * [ Challenges  ](https://langchain-ai.github.io/langgraphjs/concepts/high_level/#challenges)
            * [ Core Principles  ](https://langchain-ai.github.io/langgraphjs/concepts/high_level/#core-principles)
            * [ Debugging  ](https://langchain-ai.github.io/langgraphjs/concepts/high_level/#debugging)
            * [ Deployment  ](https://langchain-ai.github.io/langgraphjs/concepts/high_level/#deployment)
          * [ LangGraph Glossary  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/)
          * [ Agent architectures  ](https://langchain-ai.github.io/langgraphjs/concepts/agentic_concepts/)
          * [ Multi-agent Systems  ](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/)
          * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/)
          * [ Persistence  ](https://langchain-ai.github.io/langgraphjs/concepts/persistence/)
          * [ Memory  ](https://langchain-ai.github.io/langgraphjs/concepts/memory/)
          * [ Streaming  ](https://langchain-ai.github.io/langgraphjs/concepts/streaming/)
          * [ Functional API  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/)
        * [ LangGraph Platform  ](https://langchain-ai.github.io/langgraphjs/concepts#langgraph-platform)
      * [ Tutorials  ](https://langchain-ai.github.io/langgraphjs/tutorials/)
    * Resources  Resources 
      * [ Adopters  ](https://langchain-ai.github.io/langgraphjs/adopters/)
      * [ FAQ  ](https://langchain-ai.github.io/langgraphjs/concepts/faq/)
      * [ Troubleshooting  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraphjs/reference/)
  * [ Versions  ](https://langchain-ai.github.io/langgraphjs/versions/)



Table of contents 

  * [ Challenges  ](https://langchain-ai.github.io/langgraphjs/concepts/high_level/#challenges)
  * [ Core Principles  ](https://langchain-ai.github.io/langgraphjs/concepts/high_level/#core-principles)
  * [ Debugging  ](https://langchain-ai.github.io/langgraphjs/concepts/high_level/#debugging)
  * [ Deployment  ](https://langchain-ai.github.io/langgraphjs/concepts/high_level/#deployment)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ Concepts  ](https://langchain-ai.github.io/langgraphjs/concepts/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/concepts#langgraph)



# Why LangGraph?[¶](https://langchain-ai.github.io/langgraphjs/concepts/high_level/#why-langgraph "Permanent link")

LLMs are extremely powerful, particularly when connected to other systems such as a retriever or APIs. This is why many LLM applications use a control flow of steps before and / or after LLM calls. As an example [RAG](https://github.com/langchain-ai/rag-from-scratch) performs retrieval of relevant documents to a question, and passes those documents to an LLM in order to ground the response. Often a control flow of steps before and / or after an LLM is called a "chain." Chains are a popular paradigm for programming with LLMs and offer a high degree of reliability; the same set of steps runs with each chain invocation.

However, we often want LLM systems that can pick their own control flow! This is one definition of an [agent](https://blog.langchain.dev/what-is-an-agent/): an agent is a system that uses an LLM to decide the control flow of an application. Unlike a chain, an agent given an LLM some degree of control over the sequence of steps in the application. Examples of using an LLM to decide the control of an application:

  * Using an LLM to route between two potential paths
  * Using an LLM to decide which of many tools to call
  * Using an LLM to decide whether the generated answer is sufficient or more work is need



There are many different types of [agent architectures](https://blog.langchain.dev/what-is-a-cognitive-architecture/) to consider, which given an LLM varying levels of control. On one extreme, a router allows an LLM to select a single step from a specified set of options and, on the other extreme, a fully autonomous long-running agent may have complete freedom to select any sequence of steps that it wants for a given problem. 

![Agent Types](https://langchain-ai.github.io/langgraphjs/concepts/img/agent_types.png)

Several concepts are utilized in many agent architectures:

  * [Tool calling](https://langchain-ai.github.io/langgraphjs/concepts/agentic_concepts/#tool-calling): this is often how LLMs make decisions
  * Action taking: often times, the LLMs' outputs are used as the input to an action
  * [Memory](https://langchain-ai.github.io/langgraphjs/concepts/agentic_concepts/#memory): reliable systems need to have knowledge of things that occurred
  * [Planning](https://langchain-ai.github.io/langgraphjs/concepts/agentic_concepts/#planning): planning steps (either explicit or implicit) are useful for ensuring that the LLM, when making decisions, makes them in the highest fidelity way.



## Challenges[¶](https://langchain-ai.github.io/langgraphjs/concepts/high_level/#challenges "Permanent link")

In practice, there is often a trade-off between control and reliability. As we give LLMs more control, the application often become less reliable. This can be due to factors such as LLM non-determinism and / or errors in selecting tools (or steps) that the agent uses (takes).

![Agent Challenge](https://langchain-ai.github.io/langgraphjs/concepts/img/challenge.png)

## Core Principles[¶](https://langchain-ai.github.io/langgraphjs/concepts/high_level/#core-principles "Permanent link")

The motivation of LangGraph is to help bend the curve, preserving higher reliability as we give the agent more control over the application. We'll outline a few specific pillars of LangGraph that make it well suited for building reliable agents. 

![Langgraph](https://langchain-ai.github.io/langgraphjs/concepts/img/langgraph.png)

**Controllability**

LangGraph gives the developer a high degree of [control](https://langchain-ai.github.io/langgraphjs/how-tos#controllability) by expressing the flow of the application as a set of nodes and edges. All nodes can access and modify a common state (memory). The control flow of the application can set using edges that connect nodes, either deterministically or via conditional logic. 

**Persistence**

LangGraph gives the developer many options for [persisting](https://langchain-ai.github.io/langgraphjs/how-tos#persistence) graph state using short-term or long-term (e.g., via a database) memory. 

**Human-in-the-Loop**

The persistence layer enables several different [human-in-the-loop](https://langchain-ai.github.io/langgraphjs/how-tos#human-in-the-loop) interaction patterns with agents; for example, it's possible to pause an agent, review its state, edit it state, and approve a follow-up step. 

**Streaming**

LangGraph comes with first class support for [streaming](https://langchain-ai.github.io/langgraphjs/how-tos#streaming), which can expose state to the user (or developer) over the course of agent execution. LangGraph supports streaming of both events ([like a tool call being taken](https://langchain-ai.github.io/langgraphjs/how-tos/stream-updates.ipynb)) as well as of [tokens that an LLM may emit](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens).

## Debugging[¶](https://langchain-ai.github.io/langgraphjs/concepts/high_level/#debugging "Permanent link")

Once you've built a graph, you often want to test and debug it. [LangGraph Studio](https://github.com/langchain-ai/langgraph-studio?tab=readme-ov-file) is a specialized IDE for visualization and debugging of LangGraph applications.

![Langgraph Studio](https://langchain-ai.github.io/langgraphjs/concepts/img/lg_studio.png)

## Deployment[¶](https://langchain-ai.github.io/langgraphjs/concepts/high_level/#deployment "Permanent link")

Once you have confidence in your LangGraph application, many developers want an easy path to deployment. [LangGraph Cloud](https://langchain-ai.github.io/langgraphjs/cloud) is an opinionated, simple way to deploy LangGraph objects from the LangChain team. Of course, you can also use services like [Express.js](https://expressjs.com/) and call your graph from inside the Express.js server as you see fit.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  Concepts  ](https://langchain-ai.github.io/langgraphjs/concepts/) [ Next  LangGraph Glossary  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/concepts/high_level/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
