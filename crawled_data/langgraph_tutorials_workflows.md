---
url: https://langchain-ai.github.io/langgraph/tutorials/workflows/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/tutorials/workflows/#workflows-and-agents)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Workflows and Agents 

[ ](https://langchain-ai.github.io/langgraph/tutorials/workflows/?q= "Share")

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
      * [ Tutorials  ](https://langchain-ai.github.io/langgraph/tutorials/)

Tutorials 
        * [ Quick Start  ](https://langchain-ai.github.io/langgraph/tutorials/workflows/)

Quick Start 
          * [ Quick Start  ](https://langchain-ai.github.io/langgraph/tutorials#quick-start)
          * [ Learn the basics  ](https://langchain-ai.github.io/langgraph/tutorials/introduction/)
          * [ Local Deploy  ](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/)
          * [ Cloud Deploy  ](https://langchain-ai.github.io/langgraph/cloud/quick_start/)
        * [ Chatbots  ](https://langchain-ai.github.io/langgraph/tutorials#chatbots)
        * [ RAG  ](https://langchain-ai.github.io/langgraph/tutorials#rag)
        * [ Agent Architectures  ](https://langchain-ai.github.io/langgraph/tutorials#agent-architectures)
        * [ Evaluation & Analysis  ](https://langchain-ai.github.io/langgraph/tutorials#evaluation)
        * [ Experimental  ](https://langchain-ai.github.io/langgraph/tutorials#experimental)
        * [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/concepts#langgraph-platform)
    * Resources  Resources 
      * [ Prebuilt Agents  ](https://langchain-ai.github.io/langgraph/prebuilt/)
      * [ Adopters  ](https://langchain-ai.github.io/langgraph/adopters/)
      * [ FAQ  ](https://langchain-ai.github.io/langgraph/concepts/faq/)
      * [ Troubleshooting  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraph/reference/graphs/)



Table of contents 

  * [ Set up  ](https://langchain-ai.github.io/langgraph/tutorials/workflows/#set-up)
  * [ Building Blocks: The Augmented LLM  ](https://langchain-ai.github.io/langgraph/tutorials/workflows/#building-blocks-the-augmented-llm)
  * [ Prompt chaining  ](https://langchain-ai.github.io/langgraph/tutorials/workflows/#prompt-chaining)
  * [ Parallelization  ](https://langchain-ai.github.io/langgraph/tutorials/workflows/#parallelization)
  * [ Routing  ](https://langchain-ai.github.io/langgraph/tutorials/workflows/#routing)
  * [ Orchestrator-Worker  ](https://langchain-ai.github.io/langgraph/tutorials/workflows/#orchestrator-worker)
  * [ Evaluator-optimizer  ](https://langchain-ai.github.io/langgraph/tutorials/workflows/#evaluator-optimizer)
  * [ Agent  ](https://langchain-ai.github.io/langgraph/tutorials/workflows/#agent)
    * [ Pre-built  ](https://langchain-ai.github.io/langgraph/tutorials/workflows/#pre-built)
  * [ What LangGraph provides  ](https://langchain-ai.github.io/langgraph/tutorials/workflows/#what-langgraph-provides)
    * [ Persistence: Human-in-the-Loop  ](https://langchain-ai.github.io/langgraph/tutorials/workflows/#persistence-human-in-the-loop)
    * [ Persistence: Memory  ](https://langchain-ai.github.io/langgraph/tutorials/workflows/#persistence-memory)
    * [ Streaming  ](https://langchain-ai.github.io/langgraph/tutorials/workflows/#streaming)
    * [ Deployment  ](https://langchain-ai.github.io/langgraph/tutorials/workflows/#deployment)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ Tutorials  ](https://langchain-ai.github.io/langgraph/tutorials/)
  4. [ Quick Start  ](https://langchain-ai.github.io/langgraph/tutorials#quick-start)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/tutorials/workflows/index.md "Edit this page")

# Workflows and Agents[¶](https://langchain-ai.github.io/langgraph/tutorials/workflows/#workflows-and-agents "Permanent link")

This guide reviews common patterns for agentic systems. In describing these systems, it can be useful to make a distinction between "workflows" and "agents". One way to think about this difference is nicely explained [here](https://www.anthropic.com/research/building-effective-agents) by Anthropic:

> Workflows are systems where LLMs and tools are orchestrated through predefined code paths. Agents, on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks.

Here is a simple way to visualize these differences:

![Agent Workflow](https://langchain-ai.github.io/langgraph/concepts/img/agent_workflow.png)

When building agents and workflows, LangGraph [offers a number of benefits](https://langchain-ai.github.io/langgraph/concepts/high_level/) including persistence, streaming, and support for debugging as well as deployment.

## Set up[¶](https://langchain-ai.github.io/langgraph/tutorials/workflows/#set-up "Permanent link")

You can use [any chat model](https://python.langchain.com/docs/integrations/chat/) that supports structured outputs and tool calling. Below, we show the process of installing the packages, setting API keys, and testing structured outputs / tool calling for Anthropic.

Install dependencies

```
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-0-1)pipinstalllangchain_corelangchain-anthropiclanggraph

```


Initialize an LLM

```
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-1-1)importos
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-1-2)importgetpass
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-1-4)fromlangchain_anthropicimport ChatAnthropic
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-1-5)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-1-6)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-1-7)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-1-8)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-1-10)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-1-11)_set_env("ANTHROPIC_API_KEY")
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-1-12)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-1-13)llm = ChatAnthropic(model="claude-3-5-sonnet-latest")

```


API Reference: [ChatAnthropic](https://python.langchain.com/api_reference/anthropic/chat_models/langchain_anthropic.chat_models.ChatAnthropic.html)

## Building Blocks: The Augmented LLM[¶](https://langchain-ai.github.io/langgraph/tutorials/workflows/#building-blocks-the-augmented-llm "Permanent link")

LLM have [augmentations](https://www.anthropic.com/research/building-effective-agents) that support building workflows and agents. These include [structured outputs](https://python.langchain.com/docs/concepts/structured_outputs/) and [tool calling](https://python.langchain.com/docs/concepts/tool_calling/), as shown in this image from the Anthropic [blog](https://www.anthropic.com/research/building-effective-agents):

![augmented_llm.png](https://langchain-ai.github.io/langgraph/tutorials/workflows/img/augmented_llm.png)

```
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-2-1)# Schema for structured output
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-2-2)frompydanticimport BaseModel, Field
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-2-3)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-2-4)classSearchQuery(BaseModel):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-2-5)  search_query: str = Field(None, description="Query that is optimized web search.")
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-2-6)  justification: str = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-2-7)    None, description="Why this query is relevant to the user's request."
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-2-8)  )
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-2-9)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-2-10)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-2-11)# Augment the LLM with schema for structured output
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-2-12)structured_llm = llm.with_structured_output(SearchQuery)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-2-13)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-2-14)# Invoke the augmented LLM
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-2-15)output = structured_llm.invoke("How does Calcium CT score relate to high cholesterol?")
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-2-16)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-2-17)# Define a tool
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-2-18)defmultiply(a: int, b: int) -> int:
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-2-19)  return a * b
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-2-20)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-2-21)# Augment the LLM with tools
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-2-22)llm_with_tools = llm.bind_tools([multiply])
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-2-23)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-2-24)# Invoke the LLM with input that triggers the tool call
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-2-25)msg = llm_with_tools.invoke("What is 2 times 3?")
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-2-26)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-2-27)# Get the tool call
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-2-28)msg.tool_calls

```


## Prompt chaining[¶](https://langchain-ai.github.io/langgraph/tutorials/workflows/#prompt-chaining "Permanent link")

In prompt chaining, each LLM call processes the output of the previous one. 

As noted in the [Anthropic blog](https://www.anthropic.com/research/building-effective-agents): 

> Prompt chaining decomposes a task into a sequence of steps, where each LLM call processes the output of the previous one. You can add programmatic checks (see "gate” in the diagram below) on any intermediate steps to ensure that the process is still on track.
> 
> When to use this workflow: This workflow is ideal for situations where the task can be easily and cleanly decomposed into fixed subtasks. The main goal is to trade off latency for higher accuracy, by making each LLM call an easier task.

![prompt_chain.png](https://langchain-ai.github.io/langgraph/tutorials/workflows/img/prompt_chain.png)

[Graph API](#__tabbed_1_1)[Functional API (beta)](#__tabbed_1_2)

```
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-1)fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-2)fromlanggraph.graphimport StateGraph, START, END
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-3)fromIPython.displayimport Image, display
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-4)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-5)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-6)# Graph state
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-7)classState(TypedDict):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-8)  topic: str
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-9)  joke: str
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-10)  improved_joke: str
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-11)  final_joke: str
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-12)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-13)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-14)# Nodes
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-15)defgenerate_joke(state: State):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-16)"""First LLM call to generate initial joke"""
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-17)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-18)  msg = llm.invoke(f"Write a short joke about {state['topic']}")
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-19)  return {"joke": msg.content}
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-20)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-21)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-22)defcheck_punchline(state: State):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-23)"""Gate function to check if the joke has a punchline"""
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-24)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-25)  # Simple check - does the joke contain "?" or "!"
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-26)  if "?" in state["joke"] or "!" in state["joke"]:
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-27)    return "Fail"
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-28)  return "Pass"
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-29)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-30)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-31)defimprove_joke(state: State):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-32)"""Second LLM call to improve the joke"""
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-33)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-34)  msg = llm.invoke(f"Make this joke funnier by adding wordplay: {state['joke']}")
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-35)  return {"improved_joke": msg.content}
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-36)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-37)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-38)defpolish_joke(state: State):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-39)"""Third LLM call for final polish"""
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-40)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-41)  msg = llm.invoke(f"Add a surprising twist to this joke: {state['improved_joke']}")
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-42)  return {"final_joke": msg.content}
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-43)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-44)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-45)# Build workflow
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-46)workflow = StateGraph(State)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-47)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-48)# Add nodes
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-49)workflow.add_node("generate_joke", generate_joke)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-50)workflow.add_node("improve_joke", improve_joke)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-51)workflow.add_node("polish_joke", polish_joke)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-52)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-53)# Add edges to connect nodes
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-54)workflow.add_edge(START, "generate_joke")
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-55)workflow.add_conditional_edges(
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-56)  "generate_joke", check_punchline, {"Fail": "improve_joke", "Pass": END}
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-57))
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-58)workflow.add_edge("improve_joke", "polish_joke")
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-59)workflow.add_edge("polish_joke", END)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-60)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-61)# Compile
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-62)chain = workflow.compile()
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-63)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-64)# Show workflow
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-65)display(Image(chain.get_graph().draw_mermaid_png()))
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-66)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-67)# Invoke
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-68)state = chain.invoke({"topic": "cats"})
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-69)print("Initial joke:")
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-70)print(state["joke"])
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-71)print("\n--- --- ---\n")
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-72)if "improved_joke" in state:
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-73)  print("Improved joke:")
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-74)  print(state["improved_joke"])
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-75)  print("\n--- --- ---\n")
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-76)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-77)  print("Final joke:")
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-78)  print(state["final_joke"])
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-79)else:
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-3-80)  print("Joke failed quality gate - no punchline detected!")

```


API Reference: [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END)

**LangSmith Trace**

<https://smith.langchain.com/public/a0281fca-3a71-46de-beee-791468607b75/r>

**Resources:**

**LangChain Academy**

See our lesson on Prompt Chaining [here](https://github.com/langchain-ai/langchain-academy/blob/main/module-1/chain.ipynb).

```
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-4-1)fromlanggraph.funcimport entrypoint, task
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-4-2)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-4-3)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-4-4)# Tasks
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-4-5)@task
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-4-6)defgenerate_joke(topic: str):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-4-7)"""First LLM call to generate initial joke"""
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-4-8)  msg = llm.invoke(f"Write a short joke about {topic}")
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-4-9)  return msg.content
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-4-10)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-4-11)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-4-12)defcheck_punchline(joke: str):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-4-13)"""Gate function to check if the joke has a punchline"""
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-4-14)  # Simple check - does the joke contain "?" or "!"
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-4-15)  if "?" in joke or "!" in joke:
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-4-16)    return "Fail"
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-4-17)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-4-18)  return "Pass"
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-4-19)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-4-20)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-4-21)@task
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-4-22)defimprove_joke(joke: str):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-4-23)"""Second LLM call to improve the joke"""
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-4-24)  msg = llm.invoke(f"Make this joke funnier by adding wordplay: {joke}")
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-4-25)  return msg.content
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-4-26)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-4-27)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-4-28)@task
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-4-29)defpolish_joke(joke: str):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-4-30)"""Third LLM call for final polish"""
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-4-31)  msg = llm.invoke(f"Add a surprising twist to this joke: {joke}")
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-4-32)  return msg.content
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-4-33)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-4-34)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-4-35)@entrypoint()
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-4-36)defparallel_workflow(topic: str):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-4-37)  original_joke = generate_joke(topic).result()
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-4-38)  if check_punchline(original_joke) == "Pass":
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-4-39)    return original_joke
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-4-40)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-4-41)  improved_joke = improve_joke(original_joke).result()
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-4-42)  return polish_joke(improved_joke).result()
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-4-43)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-4-44)# Invoke
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-4-45)for step in parallel_workflow.stream("cats", stream_mode="updates"):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-4-46)  print(step)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-4-47)  print("\n")

```


API Reference: [entrypoint](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint) | [task](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.task)

**LangSmith Trace**

<https://smith.langchain.com/public/332fa4fc-b6ca-416e-baa3-161625e69163/r>

## Parallelization[¶](https://langchain-ai.github.io/langgraph/tutorials/workflows/#parallelization "Permanent link")

With parallelization, LLMs work simultaneously on a task:

> LLMs can sometimes work simultaneously on a task and have their outputs aggregated programmatically. This workflow, parallelization, manifests in two key variations: Sectioning: Breaking a task into independent subtasks run in parallel. Voting: Running the same task multiple times to get diverse outputs.
> 
> When to use this workflow: Parallelization is effective when the divided subtasks can be parallelized for speed, or when multiple perspectives or attempts are needed for higher confidence results. For complex tasks with multiple considerations, LLMs generally perform better when each consideration is handled by a separate LLM call, allowing focused attention on each specific aspect.

![parallelization.png](https://langchain-ai.github.io/langgraph/tutorials/workflows/img/parallelization.png)

[Graph API](#__tabbed_2_1)[Functional API (beta)](#__tabbed_2_2)

```
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-1)# Graph state
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-2)classState(TypedDict):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-3)  topic: str
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-4)  joke: str
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-5)  story: str
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-6)  poem: str
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-7)  combined_output: str
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-8)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-9)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-10)# Nodes
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-11)defcall_llm_1(state: State):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-12)"""First LLM call to generate initial joke"""
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-13)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-14)  msg = llm.invoke(f"Write a joke about {state['topic']}")
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-15)  return {"joke": msg.content}
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-16)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-17)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-18)defcall_llm_2(state: State):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-19)"""Second LLM call to generate story"""
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-20)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-21)  msg = llm.invoke(f"Write a story about {state['topic']}")
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-22)  return {"story": msg.content}
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-23)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-24)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-25)defcall_llm_3(state: State):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-26)"""Third LLM call to generate poem"""
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-27)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-28)  msg = llm.invoke(f"Write a poem about {state['topic']}")
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-29)  return {"poem": msg.content}
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-30)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-31)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-32)defaggregator(state: State):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-33)"""Combine the joke and story into a single output"""
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-34)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-35)  combined = f"Here's a story, joke, and poem about {state['topic']}!\n\n"
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-36)  combined += f"STORY:\n{state['story']}\n\n"
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-37)  combined += f"JOKE:\n{state['joke']}\n\n"
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-38)  combined += f"POEM:\n{state['poem']}"
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-39)  return {"combined_output": combined}
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-40)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-41)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-42)# Build workflow
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-43)parallel_builder = StateGraph(State)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-44)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-45)# Add nodes
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-46)parallel_builder.add_node("call_llm_1", call_llm_1)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-47)parallel_builder.add_node("call_llm_2", call_llm_2)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-48)parallel_builder.add_node("call_llm_3", call_llm_3)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-49)parallel_builder.add_node("aggregator", aggregator)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-50)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-51)# Add edges to connect nodes
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-52)parallel_builder.add_edge(START, "call_llm_1")
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-53)parallel_builder.add_edge(START, "call_llm_2")
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-54)parallel_builder.add_edge(START, "call_llm_3")
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-55)parallel_builder.add_edge("call_llm_1", "aggregator")
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-56)parallel_builder.add_edge("call_llm_2", "aggregator")
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-57)parallel_builder.add_edge("call_llm_3", "aggregator")
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-58)parallel_builder.add_edge("aggregator", END)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-59)parallel_workflow = parallel_builder.compile()
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-60)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-61)# Show workflow
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-62)display(Image(parallel_workflow.get_graph().draw_mermaid_png()))
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-63)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-64)# Invoke
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-65)state = parallel_workflow.invoke({"topic": "cats"})
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-5-66)print(state["combined_output"])

```


**LangSmith Trace**

<https://smith.langchain.com/public/3be2e53c-ca94-40dd-934f-82ff87fac277/r>

**Resources:**

**Documentation**

See our documentation on parallelization [here](https://langchain-ai.github.io/langgraph/how-tos/branching/).

**LangChain Academy**

See our lesson on parallelization [here](https://github.com/langchain-ai/langchain-academy/blob/main/module-1/simple-graph.ipynb).

```
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-6-1)@task
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-6-2)defcall_llm_1(topic: str):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-6-3)"""First LLM call to generate initial joke"""
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-6-4)  msg = llm.invoke(f"Write a joke about {topic}")
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-6-5)  return msg.content
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-6-6)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-6-7)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-6-8)@task
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-6-9)defcall_llm_2(topic: str):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-6-10)"""Second LLM call to generate story"""
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-6-11)  msg = llm.invoke(f"Write a story about {topic}")
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-6-12)  return msg.content
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-6-13)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-6-14)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-6-15)@task
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-6-16)defcall_llm_3(topic):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-6-17)"""Third LLM call to generate poem"""
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-6-18)  msg = llm.invoke(f"Write a poem about {topic}")
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-6-19)  return msg.content
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-6-20)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-6-21)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-6-22)@task
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-6-23)defaggregator(topic, joke, story, poem):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-6-24)"""Combine the joke and story into a single output"""
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-6-25)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-6-26)  combined = f"Here's a story, joke, and poem about {topic}!\n\n"
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-6-27)  combined += f"STORY:\n{story}\n\n"
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-6-28)  combined += f"JOKE:\n{joke}\n\n"
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-6-29)  combined += f"POEM:\n{poem}"
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-6-30)  return combined
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-6-31)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-6-32)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-6-33)# Build workflow
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-6-34)@entrypoint()
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-6-35)defparallel_workflow(topic: str):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-6-36)  joke_fut = call_llm_1(topic)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-6-37)  story_fut = call_llm_2(topic)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-6-38)  poem_fut = call_llm_3(topic)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-6-39)  return aggregator(
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-6-40)    topic, joke_fut.result(), story_fut.result(), poem_fut.result()
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-6-41)  ).result()
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-6-42)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-6-43)# Invoke
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-6-44)for step in parallel_workflow.stream("cats", stream_mode="updates"):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-6-45)  print(step)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-6-46)  print("\n")

```


**LangSmith Trace**

<https://smith.langchain.com/public/623d033f-e814-41e9-80b1-75e6abb67801/r>

## Routing[¶](https://langchain-ai.github.io/langgraph/tutorials/workflows/#routing "Permanent link")

Routing classifies an input and directs it to a followup task. As noted in the [Anthropic blog](https://www.anthropic.com/research/building-effective-agents): 

> Routing classifies an input and directs it to a specialized followup task. This workflow allows for separation of concerns, and building more specialized prompts. Without this workflow, optimizing for one kind of input can hurt performance on other inputs.
> 
> When to use this workflow: Routing works well for complex tasks where there are distinct categories that are better handled separately, and where classification can be handled accurately, either by an LLM or a more traditional classification model/algorithm.

![routing.png](https://langchain-ai.github.io/langgraph/tutorials/workflows/img/routing.png)

[Graph API](#__tabbed_3_1)[Functional API (beta)](#__tabbed_3_2)

```
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-1)fromtyping_extensionsimport Literal
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-2)fromlangchain_core.messagesimport HumanMessage, SystemMessage
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-3)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-4)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-5)# Schema for structured output to use as routing logic
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-6)classRoute(BaseModel):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-7)  step: Literal["poem", "story", "joke"] = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-8)    None, description="The next step in the routing process"
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-9)  )
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-10)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-11)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-12)# Augment the LLM with schema for structured output
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-13)router = llm.with_structured_output(Route)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-14)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-15)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-16)# State
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-17)classState(TypedDict):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-18)  input: str
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-19)  decision: str
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-20)  output: str
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-21)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-22)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-23)# Nodes
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-24)defllm_call_1(state: State):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-25)"""Write a story"""
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-26)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-27)  result = llm.invoke(state["input"])
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-28)  return {"output": result.content}
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-29)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-30)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-31)defllm_call_2(state: State):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-32)"""Write a joke"""
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-33)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-34)  result = llm.invoke(state["input"])
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-35)  return {"output": result.content}
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-36)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-37)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-38)defllm_call_3(state: State):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-39)"""Write a poem"""
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-40)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-41)  result = llm.invoke(state["input"])
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-42)  return {"output": result.content}
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-43)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-44)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-45)defllm_call_router(state: State):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-46)"""Route the input to the appropriate node"""
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-47)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-48)  # Run the augmented LLM with structured output to serve as routing logic
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-49)  decision = router.invoke(
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-50)    [
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-51)      SystemMessage(
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-52)        content="Route the input to story, joke, or poem based on the user's request."
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-53)      ),
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-54)      HumanMessage(content=state["input"]),
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-55)    ]
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-56)  )
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-57)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-58)  return {"decision": decision.step}
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-59)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-60)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-61)# Conditional edge function to route to the appropriate node
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-62)defroute_decision(state: State):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-63)  # Return the node name you want to visit next
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-64)  if state["decision"] == "story":
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-65)    return "llm_call_1"
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-66)  elif state["decision"] == "joke":
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-67)    return "llm_call_2"
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-68)  elif state["decision"] == "poem":
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-69)    return "llm_call_3"
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-70)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-71)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-72)# Build workflow
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-73)router_builder = StateGraph(State)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-74)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-75)# Add nodes
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-76)router_builder.add_node("llm_call_1", llm_call_1)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-77)router_builder.add_node("llm_call_2", llm_call_2)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-78)router_builder.add_node("llm_call_3", llm_call_3)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-79)router_builder.add_node("llm_call_router", llm_call_router)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-80)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-81)# Add edges to connect nodes
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-82)router_builder.add_edge(START, "llm_call_router")
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-83)router_builder.add_conditional_edges(
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-84)  "llm_call_router",
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-85)  route_decision,
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-86)  { # Name returned by route_decision : Name of next node to visit
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-87)    "llm_call_1": "llm_call_1",
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-88)    "llm_call_2": "llm_call_2",
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-89)    "llm_call_3": "llm_call_3",
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-90)  },
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-91))
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-92)router_builder.add_edge("llm_call_1", END)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-93)router_builder.add_edge("llm_call_2", END)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-94)router_builder.add_edge("llm_call_3", END)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-95)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-96)# Compile workflow
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-97)router_workflow = router_builder.compile()
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-98)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-99)# Show the workflow
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-100)display(Image(router_workflow.get_graph().draw_mermaid_png()))
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-101)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-102)# Invoke
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-103)state = router_workflow.invoke({"input": "Write me a joke about cats"})
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-7-104)print(state["output"])

```


API Reference: [HumanMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.human.HumanMessage.html) | [SystemMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.system.SystemMessage.html)

**LangSmith Trace**

<https://smith.langchain.com/public/c4580b74-fe91-47e4-96fe-7fac598d509c/r>

**Resources:**

**LangChain Academy**

See our lesson on routing [here](https://github.com/langchain-ai/langchain-academy/blob/main/module-1/router.ipynb).

**Examples**

[Here](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/) is RAG workflow that routes questions. See our video [here](https://www.youtube.com/watch?v=bq1Plo2RhYI).

```
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-1)fromtyping_extensionsimport Literal
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-2)frompydanticimport BaseModel
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-3)fromlangchain_core.messagesimport HumanMessage, SystemMessage
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-4)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-5)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-6)# Schema for structured output to use as routing logic
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-7)classRoute(BaseModel):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-8)  step: Literal["poem", "story", "joke"] = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-9)    None, description="The next step in the routing process"
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-10)  )
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-11)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-12)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-13)# Augment the LLM with schema for structured output
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-14)router = llm.with_structured_output(Route)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-15)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-16)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-17)@task
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-18)defllm_call_1(input_: str):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-19)"""Write a story"""
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-20)  result = llm.invoke(input_)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-21)  return result.content
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-22)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-23)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-24)@task
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-25)defllm_call_2(input_: str):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-26)"""Write a joke"""
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-27)  result = llm.invoke(input_)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-28)  return result.content
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-29)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-30)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-31)@task
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-32)defllm_call_3(input_: str):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-33)"""Write a poem"""
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-34)  result = llm.invoke(input_)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-35)  return result.content
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-36)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-37)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-38)defllm_call_router(input_: str):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-39)"""Route the input to the appropriate node"""
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-40)  # Run the augmented LLM with structured output to serve as routing logic
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-41)  decision = router.invoke(
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-42)    [
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-43)      SystemMessage(
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-44)        content="Route the input to story, joke, or poem based on the user's request."
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-45)      ),
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-46)      HumanMessage(content=input_),
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-47)    ]
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-48)  )
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-49)  return decision.step
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-50)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-51)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-52)# Create workflow
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-53)@entrypoint()
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-54)defrouter_workflow(input_: str):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-55)  next_step = llm_call_router(input_)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-56)  if next_step == "story":
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-57)    llm_call = llm_call_1
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-58)  elif next_step == "joke":
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-59)    llm_call = llm_call_2
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-60)  elif next_step == "poem":
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-61)    llm_call = llm_call_3
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-62)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-63)  return llm_call(input_).result()
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-64)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-65)# Invoke
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-66)for step in router_workflow.stream("Write me a joke about cats", stream_mode="updates"):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-67)  print(step)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-8-68)  print("\n")

```


API Reference: [HumanMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.human.HumanMessage.html) | [SystemMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.system.SystemMessage.html)

**LangSmith Trace**

<https://smith.langchain.com/public/5e2eb979-82dd-402c-b1a0-a8cceaf2a28a/r>

## Orchestrator-Worker[¶](https://langchain-ai.github.io/langgraph/tutorials/workflows/#orchestrator-worker "Permanent link")

With orchestrator-worker, an orchestrator breaks down a task and delegates each sub-task to workers. As noted in the [Anthropic blog](https://www.anthropic.com/research/building-effective-agents): 

> In the orchestrator-workers workflow, a central LLM dynamically breaks down tasks, delegates them to worker LLMs, and synthesizes their results.
> 
> When to use this workflow: This workflow is well-suited for complex tasks where you can’t predict the subtasks needed (in coding, for example, the number of files that need to be changed and the nature of the change in each file likely depend on the task). Whereas it’s topographically similar, the key difference from parallelization is its flexibility—subtasks aren't pre-defined, but determined by the orchestrator based on the specific input.

![worker.png](https://langchain-ai.github.io/langgraph/tutorials/workflows/img/worker.png)

[Graph API](#__tabbed_4_1)[Functional API (beta)](#__tabbed_4_2)

```
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-9-1)fromtypingimport Annotated, List
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-9-2)importoperator
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-9-3)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-9-4)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-9-5)# Schema for structured output to use in planning
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-9-6)classSection(BaseModel):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-9-7)  name: str = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-9-8)    description="Name for this section of the report.",
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-9-9)  )
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-9-10)  description: str = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-9-11)    description="Brief overview of the main topics and concepts to be covered in this section.",
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-9-12)  )
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-9-13)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-9-14)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-9-15)classSections(BaseModel):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-9-16)  sections: List[Section] = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-9-17)    description="Sections of the report.",
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-9-18)  )
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-9-19)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-9-20)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-9-21)# Augment the LLM with schema for structured output
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-9-22)planner = llm.with_structured_output(Sections)

```


**Creating Workers in LangGraph**

Because orchestrator-worker workflows are common, LangGraph **has the`Send` API to support this**. It lets you dynamically create worker nodes and send each one a specific input. Each worker has its own state, and all worker outputs are written to a _shared state key_ that is accessible to the orchestrator graph. This gives the orchestrator access to all worker output and allows it to synthesize them into a final output. As you can see below, we iterate over a list of sections and `Send` each to a worker node. See further documentation [here](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/) and [here](https://langchain-ai.github.io/langgraph/concepts/low_level/#send).

```
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-1)fromlanggraph.constantsimport Send
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-2)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-3)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-4)# Graph state
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-5)classState(TypedDict):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-6)  topic: str # Report topic
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-7)  sections: list[Section] # List of report sections
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-8)  completed_sections: Annotated[
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-9)    list, operator.add
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-10)  ] # All workers write to this key in parallel
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-11)  final_report: str # Final report
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-12)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-13)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-14)# Worker state
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-15)classWorkerState(TypedDict):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-16)  section: Section
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-17)  completed_sections: Annotated[list, operator.add]
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-18)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-19)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-20)# Nodes
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-21)deforchestrator(state: State):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-22)"""Orchestrator that generates a plan for the report"""
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-23)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-24)  # Generate queries
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-25)  report_sections = planner.invoke(
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-26)    [
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-27)      SystemMessage(content="Generate a plan for the report."),
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-28)      HumanMessage(content=f"Here is the report topic: {state['topic']}"),
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-29)    ]
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-30)  )
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-31)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-32)  return {"sections": report_sections.sections}
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-33)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-34)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-35)defllm_call(state: WorkerState):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-36)"""Worker writes a section of the report"""
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-37)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-38)  # Generate section
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-39)  section = llm.invoke(
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-40)    [
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-41)      SystemMessage(
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-42)        content="Write a report section following the provided name and description. Include no preamble for each section. Use markdown formatting."
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-43)      ),
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-44)      HumanMessage(
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-45)        content=f"Here is the section name: {state['section'].name} and description: {state['section'].description}"
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-46)      ),
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-47)    ]
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-48)  )
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-49)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-50)  # Write the updated section to completed sections
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-51)  return {"completed_sections": [section.content]}
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-52)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-53)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-54)defsynthesizer(state: State):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-55)"""Synthesize full report from sections"""
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-56)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-57)  # List of completed sections
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-58)  completed_sections = state["completed_sections"]
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-59)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-60)  # Format completed section to str to use as context for final sections
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-61)  completed_report_sections = "\n\n---\n\n".join(completed_sections)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-62)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-63)  return {"final_report": completed_report_sections}
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-64)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-65)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-66)# Conditional edge function to create llm_call workers that each write a section of the report
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-67)defassign_workers(state: State):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-68)"""Assign a worker to each section in the plan"""
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-69)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-70)  # Kick off section writing in parallel via Send() API
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-71)  return [Send("llm_call", {"section": s}) for s in state["sections"]]
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-72)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-73)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-74)# Build workflow
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-75)orchestrator_worker_builder = StateGraph(State)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-76)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-77)# Add the nodes
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-78)orchestrator_worker_builder.add_node("orchestrator", orchestrator)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-79)orchestrator_worker_builder.add_node("llm_call", llm_call)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-80)orchestrator_worker_builder.add_node("synthesizer", synthesizer)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-81)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-82)# Add edges to connect nodes
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-83)orchestrator_worker_builder.add_edge(START, "orchestrator")
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-84)orchestrator_worker_builder.add_conditional_edges(
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-85)  "orchestrator", assign_workers, ["llm_call"]
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-86))
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-87)orchestrator_worker_builder.add_edge("llm_call", "synthesizer")
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-88)orchestrator_worker_builder.add_edge("synthesizer", END)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-89)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-90)# Compile the workflow
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-91)orchestrator_worker = orchestrator_worker_builder.compile()
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-92)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-93)# Show the workflow
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-94)display(Image(orchestrator_worker.get_graph().draw_mermaid_png()))
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-95)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-96)# Invoke
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-97)state = orchestrator_worker.invoke({"topic": "Create a report on LLM scaling laws"})
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-98)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-99)fromIPython.displayimport Markdown
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-10-100)Markdown(state["final_report"])

```


API Reference: [Send](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Send)

**LangSmith Trace**

<https://smith.langchain.com/public/78cbcfc3-38bf-471d-b62a-b299b144237d/r>

**Resources:**

**LangChain Academy**

See our lesson on orchestrator-worker [here](https://github.com/langchain-ai/langchain-academy/blob/main/module-4/map-reduce.ipynb).

**Examples**

[Here](https://github.com/langchain-ai/report-mAIstro) is a project that uses orchestrator-worker for report planning and writing. See our video [here](https://www.youtube.com/watch?v=wSxZ7yFbbas).

```
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-1)fromtypingimport List
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-2)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-3)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-4)# Schema for structured output to use in planning
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-5)classSection(BaseModel):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-6)  name: str = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-7)    description="Name for this section of the report.",
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-8)  )
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-9)  description: str = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-10)    description="Brief overview of the main topics and concepts to be covered in this section.",
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-11)  )
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-12)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-13)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-14)classSections(BaseModel):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-15)  sections: List[Section] = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-16)    description="Sections of the report.",
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-17)  )
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-18)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-19)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-20)# Augment the LLM with schema for structured output
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-21)planner = llm.with_structured_output(Sections)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-22)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-23)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-24)@task
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-25)deforchestrator(topic: str):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-26)"""Orchestrator that generates a plan for the report"""
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-27)  # Generate queries
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-28)  report_sections = planner.invoke(
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-29)    [
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-30)      SystemMessage(content="Generate a plan for the report."),
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-31)      HumanMessage(content=f"Here is the report topic: {topic}"),
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-32)    ]
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-33)  )
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-34)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-35)  return report_sections.sections
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-36)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-37)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-38)@task
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-39)defllm_call(section: Section):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-40)"""Worker writes a section of the report"""
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-41)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-42)  # Generate section
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-43)  result = llm.invoke(
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-44)    [
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-45)      SystemMessage(content="Write a report section."),
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-46)      HumanMessage(
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-47)        content=f"Here is the section name: {section.name} and description: {section.description}"
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-48)      ),
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-49)    ]
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-50)  )
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-51)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-52)  # Write the updated section to completed sections
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-53)  return result.content
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-54)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-55)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-56)@task
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-57)defsynthesizer(completed_sections: list[str]):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-58)"""Synthesize full report from sections"""
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-59)  final_report = "\n\n---\n\n".join(completed_sections)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-60)  return final_report
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-61)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-62)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-63)@entrypoint()
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-64)deforchestrator_worker(topic: str):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-65)  sections = orchestrator(topic).result()
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-66)  section_futures = [llm_call(section) for section in sections]
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-67)  final_report = synthesizer(
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-68)    [section_fut.result() for section_fut in section_futures]
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-69)  ).result()
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-70)  return final_report
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-71)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-72)# Invoke
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-73)report = orchestrator_worker.invoke("Create a report on LLM scaling laws")
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-74)fromIPython.displayimport Markdown
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-11-75)Markdown(report)

```


**LangSmith Trace**

<https://smith.langchain.com/public/75a636d0-6179-4a12-9836-e0aa571e87c5/r>

## Evaluator-optimizer[¶](https://langchain-ai.github.io/langgraph/tutorials/workflows/#evaluator-optimizer "Permanent link")

In the evaluator-optimizer workflow, one LLM call generates a response while another provides evaluation and feedback in a loop:

> In the evaluator-optimizer workflow, one LLM call generates a response while another provides evaluation and feedback in a loop.
> 
> When to use this workflow: This workflow is particularly effective when we have clear evaluation criteria, and when iterative refinement provides measurable value. The two signs of good fit are, first, that LLM responses can be demonstrably improved when a human articulates their feedback; and second, that the LLM can provide such feedback. This is analogous to the iterative writing process a human writer might go through when producing a polished document.

![evaluator_optimizer.png](https://langchain-ai.github.io/langgraph/tutorials/workflows/img/evaluator_optimizer.png)

[Graph API](#__tabbed_5_1)[Functional API (beta)](#__tabbed_5_2)

```
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-1)# Graph state
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-2)classState(TypedDict):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-3)  joke: str
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-4)  topic: str
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-5)  feedback: str
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-6)  funny_or_not: str
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-7)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-8)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-9)# Schema for structured output to use in evaluation
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-10)classFeedback(BaseModel):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-11)  grade: Literal["funny", "not funny"] = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-12)    description="Decide if the joke is funny or not.",
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-13)  )
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-14)  feedback: str = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-15)    description="If the joke is not funny, provide feedback on how to improve it.",
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-16)  )
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-17)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-18)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-19)# Augment the LLM with schema for structured output
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-20)evaluator = llm.with_structured_output(Feedback)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-21)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-22)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-23)# Nodes
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-24)defllm_call_generator(state: State):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-25)"""LLM generates a joke"""
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-26)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-27)  if state.get("feedback"):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-28)    msg = llm.invoke(
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-29)      f"Write a joke about {state['topic']} but take into account the feedback: {state['feedback']}"
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-30)    )
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-31)  else:
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-32)    msg = llm.invoke(f"Write a joke about {state['topic']}")
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-33)  return {"joke": msg.content}
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-34)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-35)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-36)defllm_call_evaluator(state: State):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-37)"""LLM evaluates the joke"""
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-38)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-39)  grade = evaluator.invoke(f"Grade the joke {state['joke']}")
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-40)  return {"funny_or_not": grade.grade, "feedback": grade.feedback}
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-41)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-42)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-43)# Conditional edge function to route back to joke generator or end based upon feedback from the evaluator
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-44)defroute_joke(state: State):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-45)"""Route back to joke generator or end based upon feedback from the evaluator"""
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-46)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-47)  if state["funny_or_not"] == "funny":
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-48)    return "Accepted"
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-49)  elif state["funny_or_not"] == "not funny":
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-50)    return "Rejected + Feedback"
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-51)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-52)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-53)# Build workflow
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-54)optimizer_builder = StateGraph(State)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-55)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-56)# Add the nodes
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-57)optimizer_builder.add_node("llm_call_generator", llm_call_generator)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-58)optimizer_builder.add_node("llm_call_evaluator", llm_call_evaluator)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-59)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-60)# Add edges to connect nodes
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-61)optimizer_builder.add_edge(START, "llm_call_generator")
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-62)optimizer_builder.add_edge("llm_call_generator", "llm_call_evaluator")
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-63)optimizer_builder.add_conditional_edges(
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-64)  "llm_call_evaluator",
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-65)  route_joke,
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-66)  { # Name returned by route_joke : Name of next node to visit
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-67)    "Accepted": END,
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-68)    "Rejected + Feedback": "llm_call_generator",
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-69)  },
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-70))
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-71)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-72)# Compile the workflow
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-73)optimizer_workflow = optimizer_builder.compile()
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-74)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-75)# Show the workflow
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-76)display(Image(optimizer_workflow.get_graph().draw_mermaid_png()))
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-77)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-78)# Invoke
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-79)state = optimizer_workflow.invoke({"topic": "Cats"})
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-12-80)print(state["joke"])

```


**LangSmith Trace**

<https://smith.langchain.com/public/86ab3e60-2000-4bff-b988-9b89a3269789/r>

**Resources:**

**Examples**

[Here](https://github.com/langchain-ai/research-rabbit) is an assistant that uses evaluator-optimizer to improve a report. See our video [here](https://www.youtube.com/watch?v=XGuTzHoqlj8).

[Here](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/) is a RAG workflow that grades answers for hallucinations or errors. See our video [here](https://www.youtube.com/watch?v=bq1Plo2RhYI).

```
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-13-1)# Schema for structured output to use in evaluation
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-13-2)classFeedback(BaseModel):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-13-3)  grade: Literal["funny", "not funny"] = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-13-4)    description="Decide if the joke is funny or not.",
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-13-5)  )
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-13-6)  feedback: str = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-13-7)    description="If the joke is not funny, provide feedback on how to improve it.",
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-13-8)  )
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-13-9)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-13-10)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-13-11)# Augment the LLM with schema for structured output
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-13-12)evaluator = llm.with_structured_output(Feedback)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-13-13)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-13-14)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-13-15)# Nodes
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-13-16)@task
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-13-17)defllm_call_generator(topic: str, feedback: Feedback):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-13-18)"""LLM generates a joke"""
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-13-19)  if feedback:
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-13-20)    msg = llm.invoke(
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-13-21)      f"Write a joke about {topic} but take into account the feedback: {feedback}"
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-13-22)    )
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-13-23)  else:
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-13-24)    msg = llm.invoke(f"Write a joke about {topic}")
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-13-25)  return msg.content
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-13-26)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-13-27)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-13-28)@task
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-13-29)defllm_call_evaluator(joke: str):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-13-30)"""LLM evaluates the joke"""
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-13-31)  feedback = evaluator.invoke(f"Grade the joke {joke}")
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-13-32)  return feedback
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-13-33)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-13-34)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-13-35)@entrypoint()
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-13-36)defoptimizer_workflow(topic: str):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-13-37)  feedback = None
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-13-38)  while True:
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-13-39)    joke = llm_call_generator(topic, feedback).result()
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-13-40)    feedback = llm_call_evaluator(joke).result()
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-13-41)    if feedback.grade == "funny":
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-13-42)      break
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-13-43)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-13-44)  return joke
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-13-45)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-13-46)# Invoke
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-13-47)for step in optimizer_workflow.stream("Cats", stream_mode="updates"):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-13-48)  print(step)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-13-49)  print("\n")

```


**LangSmith Trace**

<https://smith.langchain.com/public/f66830be-4339-4a6b-8a93-389ce5ae27b4/r>

## Agent[¶](https://langchain-ai.github.io/langgraph/tutorials/workflows/#agent "Permanent link")

Agents are typically implemented as an LLM performing actions (via tool-calling) based on environmental feedback in a loop. As noted in the [Anthropic blog](https://www.anthropic.com/research/building-effective-agents):

> Agents can handle sophisticated tasks, but their implementation is often straightforward. They are typically just LLMs using tools based on environmental feedback in a loop. It is therefore crucial to design toolsets and their documentation clearly and thoughtfully.
> 
> When to use agents: Agents can be used for open-ended problems where it’s difficult or impossible to predict the required number of steps, and where you can’t hardcode a fixed path. The LLM will potentially operate for many turns, and you must have some level of trust in its decision-making. Agents' autonomy makes them ideal for scaling tasks in trusted environments.

![agent.png](https://langchain-ai.github.io/langgraph/tutorials/workflows/img/agent.png)

```
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-14-1)fromlangchain_core.toolsimport tool
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-14-2)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-14-3)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-14-4)# Define tools
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-14-5)@tool
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-14-6)defmultiply(a: int, b: int) -> int:
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-14-7)"""Multiply a and b.
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-14-8)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-14-9)  Args:
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-14-10)    a: first int
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-14-11)    b: second int
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-14-12)  """
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-14-13)  return a * b
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-14-14)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-14-15)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-14-16)@tool
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-14-17)defadd(a: int, b: int) -> int:
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-14-18)"""Adds a and b.
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-14-19)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-14-20)  Args:
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-14-21)    a: first int
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-14-22)    b: second int
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-14-23)  """
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-14-24)  return a + b
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-14-25)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-14-26)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-14-27)@tool
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-14-28)defdivide(a: int, b: int) -> float:
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-14-29)"""Divide a and b.
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-14-30)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-14-31)  Args:
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-14-32)    a: first int
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-14-33)    b: second int
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-14-34)  """
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-14-35)  return a / b
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-14-36)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-14-37)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-14-38)# Augment the LLM with tools
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-14-39)tools = [add, multiply, divide]
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-14-40)tools_by_name = {tool.name: tool for tool in tools}
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-14-41)llm_with_tools = llm.bind_tools(tools)

```


API Reference: [tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html)

[Graph API](#__tabbed_6_1)[Functional API (beta)](#__tabbed_6_2)

```
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-1)fromlanggraph.graphimport MessagesState
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-2)fromlangchain_core.messagesimport SystemMessage, HumanMessage, ToolMessage
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-3)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-4)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-5)# Nodes
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-6)defllm_call(state: MessagesState):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-7)"""LLM decides whether to call a tool or not"""
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-8)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-9)  return {
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-10)    "messages": [
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-11)      llm_with_tools.invoke(
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-12)        [
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-13)          SystemMessage(
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-14)            content="You are a helpful assistant tasked with performing arithmetic on a set of inputs."
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-15)          )
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-16)        ]
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-17)        + state["messages"]
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-18)      )
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-19)    ]
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-20)  }
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-21)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-22)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-23)deftool_node(state: dict):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-24)"""Performs the tool call"""
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-25)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-26)  result = []
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-27)  for tool_call in state["messages"][-1].tool_calls:
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-28)    tool = tools_by_name[tool_call["name"]]
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-29)    observation = tool.invoke(tool_call["args"])
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-30)    result.append(ToolMessage(content=observation, tool_call_id=tool_call["id"]))
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-31)  return {"messages": result}
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-32)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-33)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-34)# Conditional edge function to route to the tool node or end based upon whether the LLM made a tool call
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-35)defshould_continue(state: MessagesState) -> Literal["environment", END]:
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-36)"""Decide if we should continue the loop or stop based upon whether the LLM made a tool call"""
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-37)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-38)  messages = state["messages"]
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-39)  last_message = messages[-1]
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-40)  # If the LLM makes a tool call, then perform an action
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-41)  if last_message.tool_calls:
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-42)    return "Action"
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-43)  # Otherwise, we stop (reply to the user)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-44)  return END
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-45)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-46)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-47)# Build workflow
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-48)agent_builder = StateGraph(MessagesState)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-49)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-50)# Add nodes
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-51)agent_builder.add_node("llm_call", llm_call)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-52)agent_builder.add_node("environment", tool_node)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-53)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-54)# Add edges to connect nodes
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-55)agent_builder.add_edge(START, "llm_call")
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-56)agent_builder.add_conditional_edges(
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-57)  "llm_call",
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-58)  should_continue,
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-59)  {
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-60)    # Name returned by should_continue : Name of next node to visit
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-61)    "Action": "environment",
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-62)    END: END,
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-63)  },
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-64))
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-65)agent_builder.add_edge("environment", "llm_call")
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-66)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-67)# Compile the agent
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-68)agent = agent_builder.compile()
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-69)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-70)# Show the agent
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-71)display(Image(agent.get_graph(xray=True).draw_mermaid_png()))
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-72)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-73)# Invoke
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-74)messages = [HumanMessage(content="Add 3 and 4.")]
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-75)messages = agent.invoke({"messages": messages})
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-76)for m in messages["messages"]:
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-15-77)  m.pretty_print()

```


API Reference: [SystemMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.system.SystemMessage.html) | [HumanMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.human.HumanMessage.html) | [ToolMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.tool.ToolMessage.html)

**LangSmith Trace**

<https://smith.langchain.com/public/051f0391-6761-4f8c-a53b-22231b016690/r>

**Resources:**

**LangChain Academy**

See our lesson on agents [here](https://github.com/langchain-ai/langchain-academy/blob/main/module-1/agent.ipynb).

**Examples**

[Here](https://github.com/langchain-ai/memory-agent) is a project that uses a tool calling agent to create / store long-term memories.

```
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-16-1)fromlanggraph.graphimport add_messages
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-16-2)fromlangchain_core.messagesimport (
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-16-3)  SystemMessage,
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-16-4)  HumanMessage,
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-16-5)  BaseMessage,
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-16-6)  ToolCall,
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-16-7))
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-16-8)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-16-9)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-16-10)@task
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-16-11)defcall_llm(messages: list[BaseMessage]):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-16-12)"""LLM decides whether to call a tool or not"""
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-16-13)  return llm_with_tools.invoke(
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-16-14)    [
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-16-15)      SystemMessage(
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-16-16)        content="You are a helpful assistant tasked with performing arithmetic on a set of inputs."
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-16-17)      )
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-16-18)    ]
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-16-19)    + messages
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-16-20)  )
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-16-21)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-16-22)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-16-23)@task
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-16-24)defcall_tool(tool_call: ToolCall):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-16-25)"""Performs the tool call"""
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-16-26)  tool = tools_by_name[tool_call["name"]]
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-16-27)  return tool.invoke(tool_call)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-16-28)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-16-29)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-16-30)@entrypoint()
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-16-31)defagent(messages: list[BaseMessage]):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-16-32)  llm_response = call_llm(messages).result()
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-16-33)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-16-34)  while True:
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-16-35)    if not llm_response.tool_calls:
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-16-36)      break
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-16-37)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-16-38)    # Execute tools
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-16-39)    tool_result_futures = [
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-16-40)      call_tool(tool_call) for tool_call in llm_response.tool_calls
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-16-41)    ]
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-16-42)    tool_results = [fut.result() for fut in tool_result_futures]
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-16-43)    messages = add_messages(messages, [llm_response, *tool_results])
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-16-44)    llm_response = call_llm(messages).result()
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-16-45)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-16-46)  messages = add_messages(messages, llm_response)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-16-47)  return messages
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-16-48)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-16-49)# Invoke
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-16-50)messages = [HumanMessage(content="Add 3 and 4.")]
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-16-51)for chunk in agent.stream(messages, stream_mode="updates"):
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-16-52)  print(chunk)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-16-53)  print("\n")

```


API Reference: [add_messages](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.message.add_messages)

**LangSmith Trace**

<https://smith.langchain.com/public/42ae8bf9-3935-4504-a081-8ddbcbfc8b2e/r>

#### Pre-built[¶](https://langchain-ai.github.io/langgraph/tutorials/workflows/#pre-built "Permanent link")

LangGraph also provides a **pre-built method** for creating an agent as defined above (using the `create_react_agent`[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent) function):

<https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/>

```
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-17-1)fromlanggraph.prebuiltimport create_react_agent
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-17-2)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-17-3)# Pass in:
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-17-4)# (1) the augmented LLM with tools
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-17-5)# (2) the tools list (which is used to create the tool node)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-17-6)pre_built_agent = create_react_agent(llm, tools=tools)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-17-7)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-17-8)# Show the agent
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-17-9)display(Image(pre_built_agent.get_graph().draw_mermaid_png()))
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-17-10)
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-17-11)# Invoke
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-17-12)messages = [HumanMessage(content="Add 3 and 4.")]
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-17-13)messages = pre_built_agent.invoke({"messages": messages})
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-17-14)for m in messages["messages"]:
[](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__codelineno-17-15)  m.pretty_print()

```


API Reference: [create_react_agent](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent)

**LangSmith Trace**

<https://smith.langchain.com/public/abab6a44-29f6-4b97-8164-af77413e494d/r>

## What LangGraph provides[¶](https://langchain-ai.github.io/langgraph/tutorials/workflows/#what-langgraph-provides "Permanent link")

By constructing each of the above in LangGraph, we get a few things:

### Persistence: Human-in-the-Loop[¶](https://langchain-ai.github.io/langgraph/tutorials/workflows/#persistence-human-in-the-loop "Permanent link")

LangGraph persistence layer supports interruption and approval of actions (e.g., Human In The Loop). See [Module 3 of LangChain Academy](https://github.com/langchain-ai/langchain-academy/tree/main/module-3).

### Persistence: Memory[¶](https://langchain-ai.github.io/langgraph/tutorials/workflows/#persistence-memory "Permanent link")

LangGraph persistence layer supports conversational (short-term) memory and long-term memory. See [Modules 2](https://github.com/langchain-ai/langchain-academy/tree/main/module-2) [and 5](https://github.com/langchain-ai/langchain-academy/tree/main/module-5) of LangChain Academy:

### Streaming[¶](https://langchain-ai.github.io/langgraph/tutorials/workflows/#streaming "Permanent link")

LangGraph provides several ways to stream workflow / agent outputs or intermediate state. See [Module 3 of LangChain Academy](https://github.com/langchain-ai/langchain-academy/blob/main/module-3/streaming-interruption.ipynb).

### Deployment[¶](https://langchain-ai.github.io/langgraph/tutorials/workflows/#deployment "Permanent link")

LangGraph provides an easy on-ramp for deployment, observability, and evaluation. See [module 6](https://github.com/langchain-ai/langchain-academy/tree/main/module-6) of LangChain Academy.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Learn the basics  ](https://langchain-ai.github.io/langgraph/tutorials/introduction/) [ Next  Local Deploy  ](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/tutorials/workflows/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
