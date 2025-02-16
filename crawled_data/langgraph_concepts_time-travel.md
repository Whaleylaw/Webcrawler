---
url: https://langchain-ai.github.io/langgraph/concepts/time-travel/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/concepts/time-travel/#time-travel)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Time Travel ⏱️ 

[ ](https://langchain-ai.github.io/langgraph/concepts/time-travel/?q= "Share")

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
          * [ Why LangGraph?  ](https://langchain-ai.github.io/langgraph/concepts/high_level/)
          * [ LangGraph Glossary  ](https://langchain-ai.github.io/langgraph/concepts/low_level/)
          * [ Agent architectures  ](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/)
          * [ Multi-agent Systems  ](https://langchain-ai.github.io/langgraph/concepts/multi_agent/)
          * [ None  ](https://langchain-ai.github.io/langgraph/concepts/breakpoints)
          * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/)
          * Time Travel ⏱️  [ Time Travel ⏱️  ](https://langchain-ai.github.io/langgraph/concepts/time-travel/) Table of contents 
            * [ Replaying  ](https://langchain-ai.github.io/langgraph/concepts/time-travel/#replaying)
            * [ Forking  ](https://langchain-ai.github.io/langgraph/concepts/time-travel/#forking)
            * [ Additional Resources 📚  ](https://langchain-ai.github.io/langgraph/concepts/time-travel/#additional-resources)
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

  * [ Replaying  ](https://langchain-ai.github.io/langgraph/concepts/time-travel/#replaying)
  * [ Forking  ](https://langchain-ai.github.io/langgraph/concepts/time-travel/#forking)
  * [ Additional Resources 📚  ](https://langchain-ai.github.io/langgraph/concepts/time-travel/#additional-resources)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ Concepts  ](https://langchain-ai.github.io/langgraph/concepts/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/concepts#langgraph)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/concepts/time-travel.md "Edit this page")

# Time Travel ⏱️[¶](https://langchain-ai.github.io/langgraph/concepts/time-travel/#time-travel "Permanent link")

Prerequisites

This guide assumes that you are familiar with LangGraph's checkpoints and states. If not, please review the [persistence](https://langchain-ai.github.io/langgraph/concepts/persistence/) concept first.

When working with non-deterministic systems that make model-based decisions (e.g., agents powered by LLMs), it can be useful to examine their decision-making process in detail:

  1. 🤔 **Understand Reasoning** : Analyze the steps that led to a successful result.
  2. 🐞 **Debug Mistakes** : Identify where and why errors occurred.
  3. 🔍 **Explore Alternatives** : Test different paths to uncover better solutions.



We call these debugging techniques **Time Travel** , composed of two key actions: [**Replaying**](https://langchain-ai.github.io/langgraph/concepts/time-travel/#replaying) 🔁 and [**Forking**](https://langchain-ai.github.io/langgraph/concepts/time-travel/#forking) 🔀 .

## Replaying[¶](https://langchain-ai.github.io/langgraph/concepts/time-travel/#replaying "Permanent link")

![](https://langchain-ai.github.io/langgraph/concepts/img/human_in_the_loop/replay.png)

Replaying allows us to revisit and reproduce an agent's past actions, up to and including a specific step (checkpoint).

To replay actions before a specific checkpoint, start by retrieving all checkpoints for the thread:

```
[](https://langchain-ai.github.io/langgraph/concepts/time-travel/#__codelineno-0-1)all_checkpoints = []
[](https://langchain-ai.github.io/langgraph/concepts/time-travel/#__codelineno-0-2)for state in graph.get_state_history(thread):
[](https://langchain-ai.github.io/langgraph/concepts/time-travel/#__codelineno-0-3)  all_checkpoints.append(state)

```


Each checkpoint has a unique ID. After identifying the desired checkpoint, for instance, `xyz`, include its ID in the configuration:

```
[](https://langchain-ai.github.io/langgraph/concepts/time-travel/#__codelineno-1-1)config = {'configurable': {'thread_id': '1', 'checkpoint_id': 'xyz'}}
[](https://langchain-ai.github.io/langgraph/concepts/time-travel/#__codelineno-1-2)for event in graph.stream(None, config, stream_mode="values"):
[](https://langchain-ai.github.io/langgraph/concepts/time-travel/#__codelineno-1-3)  print(event)

```


The graph replays previously executed steps _before_ the provided `checkpoint_id` and executes the steps _after_ `checkpoint_id` (i.e., a new fork), even if they have been executed previously.

## Forking[¶](https://langchain-ai.github.io/langgraph/concepts/time-travel/#forking "Permanent link")

![](https://langchain-ai.github.io/langgraph/concepts/img/human_in_the_loop/forking.png)

Forking allows you to revisit an agent's past actions and explore alternative paths within the graph.

To edit a specific checkpoint, such as `xyz`, provide its `checkpoint_id` when updating the graph's state:

```
[](https://langchain-ai.github.io/langgraph/concepts/time-travel/#__codelineno-2-1)config = {"configurable": {"thread_id": "1", "checkpoint_id": "xyz"}}
[](https://langchain-ai.github.io/langgraph/concepts/time-travel/#__codelineno-2-2)graph.update_state(config, {"state": "updated state"})

```


This creates a new forked checkpoint, xyz-fork, from which you can continue running the graph:

```
[](https://langchain-ai.github.io/langgraph/concepts/time-travel/#__codelineno-3-1)config = {'configurable': {'thread_id': '1', 'checkpoint_id': 'xyz-fork'}}
[](https://langchain-ai.github.io/langgraph/concepts/time-travel/#__codelineno-3-2)for event in graph.stream(None, config, stream_mode="values"):
[](https://langchain-ai.github.io/langgraph/concepts/time-travel/#__codelineno-3-3)  print(event)

```


## Additional Resources 📚[¶](https://langchain-ai.github.io/langgraph/concepts/time-travel/#additional-resources "Permanent link")

  * [**Conceptual Guide: Persistence**](https://langchain-ai.github.io/langgraph/concepts/persistence/#replay): Read the persistence guide for more context on replaying.
  * [**How to View and Update Past Graph State**](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/): Step-by-step instructions for working with graph state that demonstrate the **replay** and **fork** actions.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Human-in-the-loop  ](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/) [ Next  Persistence  ](https://langchain-ai.github.io/langgraph/concepts/persistence/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/concepts/time-travel/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
