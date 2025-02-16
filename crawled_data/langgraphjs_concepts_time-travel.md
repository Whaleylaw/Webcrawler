---
url: https://langchain-ai.github.io/langgraphjs/concepts/time-travel/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/concepts/time-travel/#time-travel)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

Time Travel ⏱️ 

[ ](https://langchain-ai.github.io/langgraphjs/concepts/time-travel/?q= "Share")

Type to start searching

[ GitHub  ](https://github.com/langchain-ai/langgraphjs "Go to repository")

  * [ Home ](https://langchain-ai.github.io/langgraphjs/)
  * [ API reference ](https://langchain-ai.github.io/langgraphjs/reference/)
  * [ Versions ](https://langchain-ai.github.io/langgraphjs/versions/)



[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

[ GitHub  ](https://github.com/langchain-ai/langgraphjs "Go to repository")

  * [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  * [ API reference  ](https://langchain-ai.github.io/langgraphjs/reference/)
  * [ Versions  ](https://langchain-ai.github.io/langgraphjs/versions/)



Table of contents 

  * [ Replaying  ](https://langchain-ai.github.io/langgraphjs/concepts/time-travel/#replaying)
  * [ Forking  ](https://langchain-ai.github.io/langgraphjs/concepts/time-travel/#forking)
  * [ Additional Resources 📚  ](https://langchain-ai.github.io/langgraphjs/concepts/time-travel/#additional-resources)



# Time Travel ⏱️[¶](https://langchain-ai.github.io/langgraphjs/concepts/time-travel/#time-travel "Permanent link")

Prerequisites

This guide assumes that you are familiar with LangGraph's checkpoints and states. If not, please review the [persistence](https://langchain-ai.github.io/langgraphjs/concepts/persistence/) concept first.

When working with non-deterministic systems that make model-based decisions (e.g., agents powered by LLMs), it can be useful to examine their decision-making process in detail:

  1. 🤔 **Understand Reasoning** : Analyze the steps that led to a successful result.

  2. 🐞 **Debug Mistakes** : Identify where and why errors occurred.

  3. 🔍 **Explore Alternatives** : Test different paths to uncover better solutions.




We call these debugging techniques **Time Travel** , composed of two key actions: [**Replaying**](https://langchain-ai.github.io/langgraphjs/concepts/time-travel/#replaying) 🔁 and [**Forking**](https://langchain-ai.github.io/langgraphjs/concepts/time-travel/#forking) 🔀.

## Replaying[¶](https://langchain-ai.github.io/langgraphjs/concepts/time-travel/#replaying "Permanent link")

![](https://langchain-ai.github.io/langgraphjs/concepts/img/human_in_the_loop/replay.png)

Replaying allows us to revisit and reproduce an agent's past actions. This can be done either from the current state (or checkpoint) of the graph or from a specific checkpoint.

To replay from the current state, simply pass `null` as the input along with a `threadConfig`:

```
[](https://langchain-ai.github.io/langgraphjs/concepts/time-travel/#__codelineno-0-1)constthreadConfig={configurable:{thread_id:"1"},streamMode:"values"};
[](https://langchain-ai.github.io/langgraphjs/concepts/time-travel/#__codelineno-0-2)
[](https://langchain-ai.github.io/langgraphjs/concepts/time-travel/#__codelineno-0-3)forawait(consteventofawaitgraph.stream(null,threadConfig)){
[](https://langchain-ai.github.io/langgraphjs/concepts/time-travel/#__codelineno-0-4)console.log(event);
[](https://langchain-ai.github.io/langgraphjs/concepts/time-travel/#__codelineno-0-5)}

```


To replay actions from a specific checkpoint, start by retrieving all checkpoints for the thread:

```
[](https://langchain-ai.github.io/langgraphjs/concepts/time-travel/#__codelineno-1-1)constallCheckpoints=[];
[](https://langchain-ai.github.io/langgraphjs/concepts/time-travel/#__codelineno-1-2)
[](https://langchain-ai.github.io/langgraphjs/concepts/time-travel/#__codelineno-1-3)forawait(conststateofgraph.getStateHistory(threadConfig)){
[](https://langchain-ai.github.io/langgraphjs/concepts/time-travel/#__codelineno-1-4)allCheckpoints.push(state);
[](https://langchain-ai.github.io/langgraphjs/concepts/time-travel/#__codelineno-1-5)}

```


Each checkpoint has a unique ID. After identifying the desired checkpoint, for instance, `xyz`, include its ID in the configuration:

```
[](https://langchain-ai.github.io/langgraphjs/concepts/time-travel/#__codelineno-2-1)constthreadConfig={configurable:{thread_id:'1',checkpoint_id:'xyz'},streamMode:"values"};
[](https://langchain-ai.github.io/langgraphjs/concepts/time-travel/#__codelineno-2-2)
[](https://langchain-ai.github.io/langgraphjs/concepts/time-travel/#__codelineno-2-3)forawait(consteventofawaitgraph.stream(null,threadConfig)){
[](https://langchain-ai.github.io/langgraphjs/concepts/time-travel/#__codelineno-2-4)console.log(event);
[](https://langchain-ai.github.io/langgraphjs/concepts/time-travel/#__codelineno-2-5)}

```


The graph efficiently replays previously executed nodes instead of re-executing them, leveraging its awareness of prior checkpoint executions.

## Forking[¶](https://langchain-ai.github.io/langgraphjs/concepts/time-travel/#forking "Permanent link")

![](https://langchain-ai.github.io/langgraphjs/concepts/img/human_in_the_loop/forking.png)

Forking allows you to revisit an agent's past actions and explore alternative paths within the graph.

To edit a specific checkpoint, such as `xyz`, provide its `checkpoint_id` when updating the graph's state:

```
[](https://langchain-ai.github.io/langgraphjs/concepts/time-travel/#__codelineno-3-1)constthreadConfig={configurable:{thread_id:"1",checkpoint_id:"xyz"}};
[](https://langchain-ai.github.io/langgraphjs/concepts/time-travel/#__codelineno-3-2)
[](https://langchain-ai.github.io/langgraphjs/concepts/time-travel/#__codelineno-3-3)graph.updateState(threadConfig,{state:"updated state"});

```


This creates a new forked checkpoint, xyz-fork, from which you can continue running the graph:

```
[](https://langchain-ai.github.io/langgraphjs/concepts/time-travel/#__codelineno-4-1)constthreadConfig={configurable:{thread_id:'1',checkpoint_id:'xyz-fork'},streamMode:"values"};
[](https://langchain-ai.github.io/langgraphjs/concepts/time-travel/#__codelineno-4-2)
[](https://langchain-ai.github.io/langgraphjs/concepts/time-travel/#__codelineno-4-3)forawait(consteventofawaitgraph.stream(null,threadConfig)){
[](https://langchain-ai.github.io/langgraphjs/concepts/time-travel/#__codelineno-4-4)console.log(event);
[](https://langchain-ai.github.io/langgraphjs/concepts/time-travel/#__codelineno-4-5)}

```


## Additional Resources 📚[¶](https://langchain-ai.github.io/langgraphjs/concepts/time-travel/#additional-resources "Permanent link")

  * [**Conceptual Guide: Persistence**](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#replay): Read the persistence guide for more context on replaying.

  * [**How to View and Update Past Graph State**](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel): Step-by-step instructions for working with graph state that demonstrate the **replay** and **fork** actions.


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top 

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/concepts/time-travel/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
