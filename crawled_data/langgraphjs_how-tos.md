---
url: https://langchain-ai.github.io/langgraphjs/how-tos
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/#how-to-guides)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How-to Guides 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/?q= "Share")

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

How-to Guides 
        * [ Installation  ](https://langchain-ai.github.io/langgraphjs/how-tos#installation)
        * [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
        * [ LangGraph Platform  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph-platform)
      * [ Concepts  ](https://langchain-ai.github.io/langgraphjs/concepts/)
      * [ Tutorials  ](https://langchain-ai.github.io/langgraphjs/tutorials/)
    * Resources  Resources 
      * [ Adopters  ](https://langchain-ai.github.io/langgraphjs/adopters/)
      * [ FAQ  ](https://langchain-ai.github.io/langgraphjs/concepts/faq/)
      * [ Troubleshooting  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraphjs/reference/)
  * [ Versions  ](https://langchain-ai.github.io/langgraphjs/versions/)



Table of contents 

  * [ Installation  ](https://langchain-ai.github.io/langgraphjs/how-tos/#installation)
  * [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos/#langgraph)
    * [ Controllability  ](https://langchain-ai.github.io/langgraphjs/how-tos/#controllability)
    * [ Persistence  ](https://langchain-ai.github.io/langgraphjs/how-tos/#persistence)
    * [ Memory  ](https://langchain-ai.github.io/langgraphjs/how-tos/#memory)
    * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraphjs/how-tos/#human-in-the-loop)
    * [ Time Travel  ](https://langchain-ai.github.io/langgraphjs/how-tos/#time-travel)
    * [ Streaming  ](https://langchain-ai.github.io/langgraphjs/how-tos/#streaming)
    * [ Tool calling  ](https://langchain-ai.github.io/langgraphjs/how-tos/#tool-calling)
    * [ Subgraphs  ](https://langchain-ai.github.io/langgraphjs/how-tos/#subgraphs)
    * [ Multi-agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/#multi-agent)
    * [ State management  ](https://langchain-ai.github.io/langgraphjs/how-tos/#state-management)
    * [ Other  ](https://langchain-ai.github.io/langgraphjs/how-tos/#other)
    * [ Prebuilt ReAct Agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/#prebuilt-react-agent)
  * [ LangGraph Platform  ](https://langchain-ai.github.io/langgraphjs/how-tos/#langgraph-platform)
    * [ Application Structure  ](https://langchain-ai.github.io/langgraphjs/how-tos/#application-structure)
    * [ Deployment  ](https://langchain-ai.github.io/langgraphjs/how-tos/#deployment)
    * [ Assistants  ](https://langchain-ai.github.io/langgraphjs/how-tos/#assistants)
    * [ Threads  ](https://langchain-ai.github.io/langgraphjs/how-tos/#threads)
    * [ Runs  ](https://langchain-ai.github.io/langgraphjs/how-tos/#runs)
    * [ Streaming  ](https://langchain-ai.github.io/langgraphjs/how-tos/#streaming_1)
    * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraphjs/how-tos/#human-in-the-loop_1)
    * [ Double-texting  ](https://langchain-ai.github.io/langgraphjs/how-tos/#double-texting)
    * [ Webhooks  ](https://langchain-ai.github.io/langgraphjs/how-tos/#webhooks)
    * [ Cron Jobs  ](https://langchain-ai.github.io/langgraphjs/how-tos/#cron-jobs)
    * [ LangGraph Studio  ](https://langchain-ai.github.io/langgraphjs/how-tos/#langgraph-studio)
  * [ Troubleshooting  ](https://langchain-ai.github.io/langgraphjs/how-tos/#troubleshooting)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)



# How-to guides[¶](https://langchain-ai.github.io/langgraphjs/how-tos/#how-to-guides "Permanent link")

Here you’ll find answers to “How do I...?” types of questions. These guides are **goal-oriented** and concrete; they're meant to help you complete a specific task. For conceptual explanations see the [Conceptual guide](https://langchain-ai.github.io/langgraphjs/concepts/). For end-to-end walk-throughs see [Tutorials](https://langchain-ai.github.io/langgraphjs/tutorials/). For comprehensive descriptions of every class and function see the [API Reference](https://langchain-ai.github.io/langgraphjs/reference/).

## Installation[¶](https://langchain-ai.github.io/langgraphjs/how-tos/#installation "Permanent link")

  * [How to install and manage dependencies](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/)
  * [How to use LangGraph.js in web environments](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/)



## LangGraph[¶](https://langchain-ai.github.io/langgraphjs/how-tos/#langgraph "Permanent link")

### Controllability[¶](https://langchain-ai.github.io/langgraphjs/how-tos/#controllability "Permanent link")

LangGraph.js is known for being a highly controllable agent framework. These how-to guides show how to achieve that controllability.

  * [How to create branches for parallel execution](https://langchain-ai.github.io/langgraphjs/how-tos/branching/)
  * [How to create map-reduce branches for parallel execution](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/)
  * [How to combine control flow and state updates with Command](https://langchain-ai.github.io/langgraphjs/how-tos/command/)



### Persistence[¶](https://langchain-ai.github.io/langgraphjs/how-tos/#persistence "Permanent link")

LangGraph.js makes it easy to persist state across graph runs. The guides below shows how to add persistence to your graph.

  * [How to add thread-level persistence to your graph](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/)
  * [How to add thread-level persistence to subgraphs](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-persistence/)
  * [How to add cross-thread persistence](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/)
  * [How to use a Postgres checkpointer for persistence](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/)



See the below guides for how-to add persistence to your workflow using the (beta) [Functional API](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/):

  * [How to add thread-level persistence (functional API)](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/)
  * [How to add cross-thread persistence (functional API)](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/)



### Memory[¶](https://langchain-ai.github.io/langgraphjs/how-tos/#memory "Permanent link")

LangGraph makes it easy to manage conversation [memory](https://langchain-ai.github.io/langgraphjs/concepts/memory/) in your graph. These how-to guides show how to implement different strategies for that.

  * [How to manage conversation history](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/)
  * [How to delete messages](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/)
  * [How to add summary of the conversation history](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/)
  * [How to add long-term memory (cross-thread)](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/)
  * [How to use semantic search for long-term memory](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/)



### Human-in-the-loop[¶](https://langchain-ai.github.io/langgraphjs/how-tos/#human-in-the-loop "Permanent link")

[Human-in-the-loop](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop) functionality allows you to involve humans in the decision-making process of your graph. These how-to guides show how to implement human-in-the-loop workflows in your graph.

Key workflows:

  * [How to wait for user input](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input/): A basic example that shows how to implement a human-in-the-loop workflow in your graph using the `interrupt` function.
  * [How to review tool calls](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/): Incorporate human-in-the-loop for reviewing/editing/accepting tool call requests before they executed using the `interrupt` function.



Other methods:

  * [How to add static breakpoints](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/): Use for debugging purposes. For [**human-in-the-loop**](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop) workflows, we recommend the `interrupt`[ function](https://langchain-ai.github.io/langgraphjs/reference/functions/langgraph.interrupt-1.html) instead.
  * [How to edit graph state](https://langchain-ai.github.io/langgraphjs/how-tos/edit-graph-state/): Edit graph state using `graph.update_state` method. Use this if implementing a **human-in-the-loop** workflow via **static breakpoints**.
  * [How to add dynamic breakpoints with `NodeInterrupt`](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/): **Not recommended** : Use the `interrupt`[ function](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop) instead.



See the below guides for how-to implement human-in-the-loop workflows with the (beta) [Functional API](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/):

  * [How to wait for user input (Functional API)](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input-functional/)
  * [How to review tool calls (Functional API)](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls-functional/)



### Time Travel[¶](https://langchain-ai.github.io/langgraphjs/how-tos/#time-travel "Permanent link")

[Time travel](https://langchain-ai.github.io/langgraphjs/concepts/time-travel/) allows you to replay past actions in your LangGraph application to explore alternative paths and debug issues. These how-to guides show how to use time travel in your graph.

  * [How to view and update past graph state](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel/)



### Streaming[¶](https://langchain-ai.github.io/langgraphjs/how-tos/#streaming "Permanent link")

LangGraph is built to be streaming first. These guides show how to use different streaming modes.

  * [How to stream the full state of your graph](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/)
  * [How to stream state updates of your graph](https://langchain-ai.github.io/langgraphjs/how-tos/stream-updates/)
  * [How to stream LLM tokens](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/)
  * [How to stream LLM tokens without LangChain models](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/)
  * [How to stream custom data](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-content/)
  * [How to configure multiple streaming modes](https://langchain-ai.github.io/langgraphjs/how-tos/stream-multiple/)
  * [How to stream events from within a tool](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-events-from-within-tools/)
  * [How to stream from the final node](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-from-final-node/)



### Tool calling[¶](https://langchain-ai.github.io/langgraphjs/how-tos/#tool-calling "Permanent link")

  * [How to call tools using ToolNode](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/)
  * [How to force an agent to call a tool](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/)
  * [How to handle tool calling errors](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/)
  * [How to pass runtime values to tools](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/)
  * [How to update graph state from tools](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/)



### Subgraphs[¶](https://langchain-ai.github.io/langgraphjs/how-tos/#subgraphs "Permanent link")

[Subgraphs](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#subgraphs) allow you to reuse an existing graph from another graph. These how-to guides show how to use subgraphs:

  * [How to add and use subgraphs](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph/)
  * [How to view and update state in subgraphs](https://langchain-ai.github.io/langgraphjs/how-tos/subgraphs-manage-state/)
  * [How to transform inputs and outputs of a subgraph](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/)



### Multi-agent[¶](https://langchain-ai.github.io/langgraphjs/how-tos/#multi-agent "Permanent link")

  * [How to build a multi-agent network](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/)
  * [How to add multi-turn conversation in a multi-agent application](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo/)



See the [multi-agent tutorials](https://langchain-ai.github.io/langgraphjs/tutorials/#multi-agent-systems) for implementations of other multi-agent architectures.

See the below guides for how-to implement multi-agent workflows with the (beta) [Functional API](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/):

  * [How to build a multi-agent network (functional API)](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network-functional/)
  * [How to add multi-turn conversation in a multi-agent application (functional API)](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo-functional/)



### State management[¶](https://langchain-ai.github.io/langgraphjs/how-tos/#state-management "Permanent link")

  * [How to define graph state](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/)
  * [Have a separate input and output schema](https://langchain-ai.github.io/langgraphjs/how-tos/input_output_schema/)
  * [Pass private state between nodes inside the graph](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/)



### Other[¶](https://langchain-ai.github.io/langgraphjs/how-tos/#other "Permanent link")

  * [How to add runtime configuration to your graph](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/)
  * [How to add node retries](https://langchain-ai.github.io/langgraphjs/how-tos/node-retry-policies/)
  * [How to let agent return tool results directly](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/)
  * [How to have agent respond in structured format](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/)
  * [How to manage agent steps](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/)



### Prebuilt ReAct Agent[¶](https://langchain-ai.github.io/langgraphjs/how-tos/#prebuilt-react-agent "Permanent link")

  * [How to create a ReAct agent](https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/)
  * [How to add memory to a ReAct agent](https://langchain-ai.github.io/langgraphjs/how-tos/react-memory/)
  * [How to add a system prompt to a ReAct agent](https://langchain-ai.github.io/langgraphjs/how-tos/react-system-prompt/)
  * [How to add Human-in-the-loop to a ReAct agent](https://langchain-ai.github.io/langgraphjs/how-tos/react-human-in-the-loop/)
  * [How to return structured output from a ReAct agent](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/)



See the below guide for how-to build ReAct agents with the (beta) [Functional API](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/):

  * [How to create a ReAct agent from scratch (Functional API)](https://langchain-ai.github.io/langgraphjs/how-tos/react-agent-from-scratch-functional/)



## LangGraph Platform[¶](https://langchain-ai.github.io/langgraphjs/how-tos/#langgraph-platform "Permanent link")

This section includes how-to guides for LangGraph Platform.

LangGraph Platform is a commercial solution for deploying agentic applications in production, built on the open-source LangGraph framework. It provides four deployment options to fit a range of needs: a free tier, a self-hosted version, a cloud SaaS, and a Bring Your Own Cloud (BYOC) option. You can explore these options in detail in the [deployment options guide](https://langchain-ai.github.io/langgraphjs/concepts/deployment_options/).

Tip

  * LangGraph is an MIT-licensed open-source library, which we are committed to maintaining and growing for the community.
  * You can always deploy LangGraph applications on your own infrastructure using the open-source LangGraph project without using LangGraph Platform.



### Application Structure[¶](https://langchain-ai.github.io/langgraphjs/how-tos/#application-structure "Permanent link")

Learn how to set up your app for deployment to LangGraph Platform:

  * [How to set up app for deployment (requirements.txt)](https://langchain-ai.github.io/langgraphjs/cloud/deployment/setup)
  * [How to set up app for deployment (pyproject.toml)](https://langchain-ai.github.io/langgraphjs/cloud/deployment/setup_pyproject)
  * [How to set up app for deployment (JavaScript)](https://langchain-ai.github.io/langgraphjs/cloud/deployment/setup_javascript)
  * [How to customize Dockerfile](https://langchain-ai.github.io/langgraphjs/cloud/deployment/custom_docker)
  * [How to test locally](https://langchain-ai.github.io/langgraphjs/cloud/deployment/test_locally)



### Deployment[¶](https://langchain-ai.github.io/langgraphjs/how-tos/#deployment "Permanent link")

LangGraph applications can be deployed using LangGraph Cloud, which provides a range of services to help you deploy, manage, and scale your applications.

  * [How to deploy to LangGraph cloud](https://langchain-ai.github.io/langgraphjs/cloud/deployment/cloud)
  * [How to deploy to a self-hosted environment](https://langchain-ai.github.io/langgraphjs/how-tos/deploy-self-hosted/)
  * [How to interact with the deployment using RemoteGraph](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/)



### Assistants[¶](https://langchain-ai.github.io/langgraphjs/how-tos/#assistants "Permanent link")

[Assistants](https://langchain-ai.github.io/langgraphjs/concepts/assistants/) are a configured instance of a template.

  * [How to configure agents](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/configuration_cloud)
  * [How to version assistants](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/assistant_versioning)



### Threads[¶](https://langchain-ai.github.io/langgraphjs/how-tos/#threads "Permanent link")

  * [How to copy threads](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads)
  * [How to check status of your threads](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/check_thread_status)



### Runs[¶](https://langchain-ai.github.io/langgraphjs/how-tos/#runs "Permanent link")

LangGraph Cloud supports multiple types of runs besides streaming runs.

  * [How to run an agent in the background](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run)
  * [How to run multiple agents in the same thread](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread)
  * [How to create cron jobs](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/cron_jobs)
  * [How to create stateless runs](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs)



### Streaming[¶](https://langchain-ai.github.io/langgraphjs/how-tos/#streaming_1 "Permanent link")

Streaming the results of your LLM application is vital for ensuring a good user experience, especially when your graph may call multiple models and take a long time to fully complete a run. Read about how to stream values from your graph in these how to guides:

  * [How to stream values](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_values)
  * [How to stream updates](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_updates)
  * [How to stream messages](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_messages)
  * [How to stream events](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_events)
  * [How to stream in debug mode](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug)
  * [How to stream multiple modes](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple)



### Human-in-the-loop[¶](https://langchain-ai.github.io/langgraphjs/how-tos/#human-in-the-loop_1 "Permanent link")

When creating complex graphs, leaving every decision up to the LLM can be dangerous, especially when the decisions involve invoking certain tools or accessing specific documents. To remedy this, LangGraph allows you to insert human-in-the-loop behavior to ensure your graph does not have undesired outcomes. Read more about the different ways you can add human-in-the-loop capabilities to your LangGraph Cloud projects in these how-to guides:

  * [How to add a breakpoint](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_breakpoint)
  * [How to wait for user input](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input)
  * [How to edit graph state](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state)
  * [How to replay and branch from prior states](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_time_travel)
  * [How to review tool calls](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls)



### Double-texting[¶](https://langchain-ai.github.io/langgraphjs/how-tos/#double-texting "Permanent link")

Graph execution can take a while, and sometimes users may change their mind about the input they wanted to send before their original input has finished running. For example, a user might notice a typo in their original request and will edit the prompt and resend it. Deciding what to do in these cases is important for ensuring a smooth user experience and preventing your graphs from behaving in unexpected ways. The following how-to guides provide information on the various options LangGraph Cloud gives you for dealing with double-texting:

  * [How to use the interrupt option](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/interrupt_concurrent)
  * [How to use the rollback option](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/rollback_concurrent)
  * [How to use the reject option](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/reject_concurrent)
  * [How to use the enqueue option](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/enqueue_concurrent)



### Webhooks[¶](https://langchain-ai.github.io/langgraphjs/how-tos/#webhooks "Permanent link")

  * [How to integrate webhooks](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/webhooks)



### Cron Jobs[¶](https://langchain-ai.github.io/langgraphjs/how-tos/#cron-jobs "Permanent link")

  * [How to create cron jobs](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/cron_jobs)



### LangGraph Studio[¶](https://langchain-ai.github.io/langgraphjs/how-tos/#langgraph-studio "Permanent link")

LangGraph Studio is a built-in UI for visualizing, testing, and debugging your agents.

  * [How to connect to a LangGraph Cloud deployment](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/test_deployment)
  * [How to connect to a local deployment](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/test_local_deployment)
  * [How to test your graph in LangGraph Studio](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/invoke_studio)
  * [How to interact with threads in LangGraph Studio](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/threads_studio)



## Troubleshooting[¶](https://langchain-ai.github.io/langgraphjs/how-tos/#troubleshooting "Permanent link")

These are the guides for resolving common errors you may find while building with LangGraph. Errors referenced below will have an `lc_error_code` property corresponding to one of the below codes when they are thrown in code.

  * [GRAPH_RECURSION_LIMIT](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/GRAPH_RECURSION_LIMIT/)
  * [INVALID_CONCURRENT_GRAPH_UPDATE](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE/)
  * [INVALID_GRAPH_NODE_RETURN_VALUE](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/INVALID_GRAPH_NODE_RETURN_VALUE/)
  * [MULTIPLE_SUBGRAPHS](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/MULTIPLE_SUBGRAPHS/)
  * [UNREACHABLE_NODE](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/UNREACHABLE_NODE/)

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  Cloud Deploy  ](https://langchain-ai.github.io/langgraphjs/cloud/quick_start/) [ Next  How to install and manage dependencies  ](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
