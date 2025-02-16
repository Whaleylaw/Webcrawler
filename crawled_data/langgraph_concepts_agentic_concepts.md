---
url: https://langchain-ai.github.io/langgraph/concepts/agentic_concepts
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#agent-architectures)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Agent architectures 

[ ](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/?q= "Share")

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
          * Agent architectures  [ Agent architectures  ](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/) Table of contents 
            * [ Router  ](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#router)
              * [ Structured Output  ](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#structured-output)
            * [ Tool calling agent  ](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#tool-calling-agent)
              * [ Tool calling  ](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#tool-calling)
              * [ Memory  ](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#memory)
              * [ Planning  ](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#planning)
              * [ ReAct implementation  ](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#react-implementation)
            * [ Custom agent architectures  ](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#custom-agent-architectures)
              * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#human-in-the-loop)
              * [ Parallelization  ](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#parallelization)
              * [ Subgraphs  ](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#subgraphs)
              * [ Reflection  ](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#reflection)
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

  * [ Router  ](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#router)
    * [ Structured Output  ](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#structured-output)
  * [ Tool calling agent  ](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#tool-calling-agent)
    * [ Tool calling  ](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#tool-calling)
    * [ Memory  ](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#memory)
    * [ Planning  ](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#planning)
    * [ ReAct implementation  ](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#react-implementation)
  * [ Custom agent architectures  ](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#custom-agent-architectures)
    * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#human-in-the-loop)
    * [ Parallelization  ](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#parallelization)
    * [ Subgraphs  ](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#subgraphs)
    * [ Reflection  ](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#reflection)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ Concepts  ](https://langchain-ai.github.io/langgraph/concepts/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/concepts#langgraph)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/concepts/agentic_concepts.md "Edit this page")

# Agent architectures[¶](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#agent-architectures "Permanent link")

Many LLM applications implement a particular control flow of steps before and / or after LLM calls. As an example, [RAG](https://github.com/langchain-ai/rag-from-scratch) performs retrieval of documents relevant to a user question, and passes those documents to an LLM in order to ground the model's response in the provided document context. 

Instead of hard-coding a fixed control flow, we sometimes want LLM systems that can pick their own control flow to solve more complex problems! This is one definition of an [agent](https://blog.langchain.dev/what-is-an-agent/): _an agent is a system that uses an LLM to decide the control flow of an application._ There are many ways that an LLM can control application:

  * An LLM can route between two potential paths
  * An LLM can decide which of many tools to call
  * An LLM can decide whether the generated answer is sufficient or more work is needed



As a result, there are many different types of [agent architectures](https://blog.langchain.dev/what-is-a-cognitive-architecture/), which give an LLM varying levels of control. 

![Agent Types](https://langchain-ai.github.io/langgraph/concepts/img/agent_types.png)

## Router[¶](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#router "Permanent link")

A router allows an LLM to select a single step from a specified set of options. This is an agent architecture that exhibits a relatively limited level of control because the LLM usually focuses on making a single decision and produces a specific output from limited set of pre-defined options. Routers typically employ a few different concepts to achieve this.

### Structured Output[¶](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#structured-output "Permanent link")

Structured outputs with LLMs work by providing a specific format or schema that the LLM should follow in its response. This is similar to tool calling, but more general. While tool calling typically involves selecting and using predefined functions, structured outputs can be used for any type of formatted response. Common methods to achieve structured outputs include:

  1. Prompt engineering: Instructing the LLM to respond in a specific format via the system prompt.
  2. Output parsers: Using post-processing to extract structured data from LLM responses.
  3. Tool calling: Leveraging built-in tool calling capabilities of some LLMs to generate structured outputs.



Structured outputs are crucial for routing as they ensure the LLM's decision can be reliably interpreted and acted upon by the system. Learn more about [structured outputs in this how-to guide](https://python.langchain.com/docs/how_to/structured_output/).

## Tool calling agent[¶](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#tool-calling-agent "Permanent link")

While a router allows an LLM to make a single decision, more complex agent architectures expand the LLM's control in two key ways:

  1. Multi-step decision making: The LLM can make a series of decisions, one after another, instead of just one.
  2. Tool access: The LLM can choose from and use a variety of tools to accomplish tasks.



[ReAct](https://arxiv.org/abs/2210.03629) is a popular general purpose agent architecture that combines these expansions, integrating three core concepts. 

  1. `Tool calling`: Allowing the LLM to select and use various tools as needed.
  2. `Memory`: Enabling the agent to retain and use information from previous steps.
  3. `Planning`: Empowering the LLM to create and follow multi-step plans to achieve goals.



This architecture allows for more complex and flexible agent behaviors, going beyond simple routing to enable dynamic problem-solving with multiple steps. You can use it with `create_react_agent`[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent).

### Tool calling[¶](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#tool-calling "Permanent link")

Tools are useful whenever you want an agent to interact with external systems. External systems (e.g., APIs) often require a particular input schema or payload, rather than natural language. When we bind an API, for example, as a tool, we give the model awareness of the required input schema. The model will choose to call a tool based upon the natural language input from the user and it will return an output that adheres to the tool's required schema. 

[Many LLM providers support tool calling](https://python.langchain.com/docs/integrations/chat/) and [tool calling interface](https://blog.langchain.dev/improving-core-tool-interfaces-and-docs-in-langchain/) in LangChain is simple: you can simply pass any Python `function` into `ChatModel.bind_tools(function)`.

![Tools](https://langchain-ai.github.io/langgraph/concepts/img/tool_call.png)

### Memory[¶](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#memory "Permanent link")

Memory is crucial for agents, enabling them to retain and utilize information across multiple steps of problem-solving. It operates on different scales:

  1. Short-term memory: Allows the agent to access information acquired during earlier steps in a sequence.
  2. Long-term memory: Enables the agent to recall information from previous interactions, such as past messages in a conversation.



LangGraph provides full control over memory implementation:

  * `State`[](https://langchain-ai.github.io/langgraph/concepts/low_level/#state): User-defined schema specifying the exact structure of memory to retain.
  * `Checkpointers`[](https://langchain-ai.github.io/langgraph/concepts/persistence/): Mechanism to store state at every step across different interactions.



This flexible approach allows you to tailor the memory system to your specific agent architecture needs. For a practical guide on adding memory to your graph, see [this tutorial](https://langchain-ai.github.io/langgraph/how-tos/persistence/).

Effective memory management enhances an agent's ability to maintain context, learn from past experiences, and make more informed decisions over time.

### Planning[¶](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#planning "Permanent link")

In the ReAct architecture, an LLM is called repeatedly in a while-loop. At each step the agent decides which tools to call, and what the inputs to those tools should be. Those tools are then executed, and the outputs are fed back into the LLM as observations. The while-loop terminates when the agent decides it has enough information to solve the user request and it is not worth calling any more tools.

### ReAct implementation[¶](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#react-implementation "Permanent link")

There are several differences between [this](https://arxiv.org/abs/2210.03629) paper and the pre-built `create_react_agent`[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent) implementation:

  * First, we use [tool-calling](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#tool-calling) to have LLMs call tools, whereas the paper used prompting + parsing of raw output. This is because tool calling did not exist when the paper was written, but is generally better and more reliable.
  * Second, we use messages to prompt the LLM, whereas the paper used string formatting. This is because at the time of writing, LLMs didn't even expose a message-based interface, whereas now that's the only interface they expose.
  * Third, the paper required all inputs to the tools to be a single string. This was largely due to LLMs not being super capable at the time, and only really being able to generate a single input. Our implementation allows for using tools that require multiple inputs.
  * Fourth, the paper only looks at calling a single tool at the time, largely due to limitations in LLMs performance at the time. Our implementation allows for calling multiple tools at a time.
  * Finally, the paper asked the LLM to explicitly generate a "Thought" step before deciding which tools to call. This is the "Reasoning" part of "ReAct". Our implementation does not do this by default, largely because LLMs have gotten much better and that is not as necessary. Of course, if you wish to prompt it do so, you certainly can.



## Custom agent architectures[¶](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#custom-agent-architectures "Permanent link")

While routers and tool-calling agents (like ReAct) are common, [customizing agent architectures](https://blog.langchain.dev/why-you-should-outsource-your-agentic-infrastructure-but-own-your-cognitive-architecture/) often leads to better performance for specific tasks. LangGraph offers several powerful features for building tailored agent systems:

### Human-in-the-loop[¶](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#human-in-the-loop "Permanent link")

Human involvement can significantly enhance agent reliability, especially for sensitive tasks. This can involve:

  * Approving specific actions
  * Providing feedback to update the agent's state
  * Offering guidance in complex decision-making processes



Human-in-the-loop patterns are crucial when full automation isn't feasible or desirable. Learn more in our [human-in-the-loop guide](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/).

### Parallelization[¶](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#parallelization "Permanent link")

Parallel processing is vital for efficient multi-agent systems and complex tasks. LangGraph supports parallelization through its [Send](https://langchain-ai.github.io/langgraph/concepts/low_level/#send) API, enabling:

  * Concurrent processing of multiple states
  * Implementation of map-reduce-like operations
  * Efficient handling of independent subtasks



For practical implementation, see our [map-reduce tutorial](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/).

### Subgraphs[¶](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#subgraphs "Permanent link")

[Subgraphs](https://langchain-ai.github.io/langgraph/concepts/low_level/#subgraphs) are essential for managing complex agent architectures, particularly in [multi-agent systems](https://langchain-ai.github.io/langgraph/concepts/multi_agent/). They allow:

  * Isolated state management for individual agents
  * Hierarchical organization of agent teams
  * Controlled communication between agents and the main system



Subgraphs communicate with the parent graph through overlapping keys in the state schema. This enables flexible, modular agent design. For implementation details, refer to our [subgraph how-to guide](https://langchain-ai.github.io/langgraph/how-tos/subgraph/).

### Reflection[¶](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#reflection "Permanent link")

Reflection mechanisms can significantly improve agent reliability by:

  1. Evaluating task completion and correctness
  2. Providing feedback for iterative improvement
  3. Enabling self-correction and learning



While often LLM-based, reflection can also use deterministic methods. For instance, in coding tasks, compilation errors can serve as feedback. This approach is demonstrated in [this video using LangGraph for self-corrective code generation](https://www.youtube.com/watch?v=MvNdgmM7uyc).

By leveraging these features, LangGraph enables the creation of sophisticated, task-specific agent architectures that can handle complex workflows, collaborate effectively, and continuously improve their performance.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  LangGraph Glossary  ](https://langchain-ai.github.io/langgraph/concepts/low_level/) [ Next  Multi-agent Systems  ](https://langchain-ai.github.io/langgraph/concepts/multi_agent/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
