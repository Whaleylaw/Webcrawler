---
url: https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#self-discover-agent)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Self-Discover Agent 

[ ](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/?q= "Share")

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
      * [ Tutorials  ](https://langchain-ai.github.io/langgraph/tutorials/)

Tutorials 
        * [ Quick Start  ](https://langchain-ai.github.io/langgraph/tutorials#quick-start)
        * [ Chatbots  ](https://langchain-ai.github.io/langgraph/tutorials#chatbots)
        * [ RAG  ](https://langchain-ai.github.io/langgraph/tutorials#rag)
        * Agent Architectures  Agent Architectures 
          * [ Agent Architectures  ](https://langchain-ai.github.io/langgraph/tutorials#agent-architectures)
          * [ Multi-Agent Systems  ](https://langchain-ai.github.io/langgraph/tutorials#multi-agent-systems)
          * [ Planning Agents  ](https://langchain-ai.github.io/langgraph/tutorials#planning-agents)
          * Reflection & Critique  Reflection & Critique 
            * [ Reflection & Critique  ](https://langchain-ai.github.io/langgraph/tutorials#reflection-critique)
            * [ Reflection  ](https://langchain-ai.github.io/langgraph/tutorials/reflection/reflection/)
            * [ Reflexion  ](https://langchain-ai.github.io/langgraph/tutorials/reflexion/reflexion/)
            * [ Tree of Thoughts  ](https://langchain-ai.github.io/langgraph/tutorials/tot/tot/)
            * [ Language Agent Tree Search  ](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/)
            * Self-Discover Agent  [ Self-Discover Agent  ](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#setup)
              * [ Define the prompts  ](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#define-the-prompts)
              * [ Define the graph  ](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#define-the-graph)
              * [ Invoke the graph  ](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#invoke-the-graph)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#setup)
  * [ Define the prompts  ](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#define-the-prompts)
  * [ Define the graph  ](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#define-the-graph)
  * [ Invoke the graph  ](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#invoke-the-graph)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ Tutorials  ](https://langchain-ai.github.io/langgraph/tutorials/)
  4. [ Agent Architectures  ](https://langchain-ai.github.io/langgraph/tutorials#agent-architectures)
  5. [ Reflection & Critique  ](https://langchain-ai.github.io/langgraph/tutorials#reflection-critique)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/tutorials/self-discover/self-discover.ipynb "Edit this page")

# Self-Discover Agent[¶](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#self-discover-agent "Permanent link")

An implementation of the [Self-Discover paper](https://arxiv.org/pdf/2402.03620.pdf).

Based on [this implementation from @catid](https://github.com/catid/self-discover/tree/main?tab=readme-ov-file)

## Setup[¶](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#setup "Permanent link")

First, let's install our required packages and set our API keys

```
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-0-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-0-2)%pip install -U --quiet langchain langgraph langchain_openai

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-1-1)importgetpass
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-1-2)importos
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-1-5)def_set_if_undefined(var: str) -> None:
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-1-6)  if os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-1-7)    return
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-1-8)  os.environ[var] = getpass.getpass(var)
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-1-10)
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-1-11)_set_if_undefined("OPENAI_API_KEY")

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Define the prompts[¶](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#define-the-prompts "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-2-1)fromlangchainimport hub
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-2-2)
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-2-3)select_prompt = hub.pull("hwchase17/self-discovery-select")
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-2-4)print("Self-Discovery Select Prompt:")
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-2-5)select_prompt.pretty_print()
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-2-6)print("Self-Discovery Select Response:")
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-2-7)adapt_prompt = hub.pull("hwchase17/self-discovery-adapt")
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-2-8)adapt_prompt.pretty_print()
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-2-9)structured_prompt = hub.pull("hwchase17/self-discovery-structure")
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-2-10)print("Self-Discovery Structured Prompt:")
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-2-11)structured_prompt.pretty_print()
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-2-12)reasoning_prompt = hub.pull("hwchase17/self-discovery-reasoning")
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-2-13)print("Self-Discovery Structured Response:")
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-2-14)reasoning_prompt.pretty_print()

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-3-1)Self-Discovery Select Prompt:
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-3-2)Select several reasoning modules that are crucial to utilize in order to solve the given task:
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-3-3)
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-3-4)All reasoning module descriptions:
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-3-5)[33;1m[1;3m{reasoning_modules}[0m
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-3-6)
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-3-7)Task: [33;1m[1;3m{task_description}[0m
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-3-8)
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-3-9)Select several modules are crucial for solving the task above:
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-3-10)
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-3-11)Self-Discovery Select Response:
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-3-12)Rephrase and specify each reasoning module so that it better helps solving the task:
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-3-13)
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-3-14)SELECTED module descriptions:
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-3-15)[33;1m[1;3m{selected_modules}[0m
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-3-16)
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-3-17)Task: [33;1m[1;3m{task_description}[0m
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-3-18)
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-3-19)Adapt each reasoning module description to better solve the task:
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-3-20)
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-3-21)Self-Discovery Structured Prompt:
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-3-22)Operationalize the reasoning modules into a step-by-step reasoning plan in JSON format:
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-3-23)
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-3-24)Here's an example:
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-3-25)
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-3-26)Example task:
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-3-27)
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-3-28)If you follow these instructions, do you return to the starting point? Always face forward. Take 1 step backward. Take 9 steps left. Take 2 steps backward. Take 6 steps forward. Take 4 steps forward. Take 4 steps backward. Take 3 steps right.
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-3-29)
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-3-30)Example reasoning structure:
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-3-31)
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-3-32){
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-3-33)  "Position after instruction 1":
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-3-34)  "Position after instruction 2":
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-3-35)  "Position after instruction n":
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-3-36)  "Is final position the same as starting position":
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-3-37)}
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-3-38)
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-3-39)Adapted module description:
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-3-40)[33;1m[1;3m{adapted_modules}[0m
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-3-41)
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-3-42)Task: [33;1m[1;3m{task_description}[0m
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-3-43)
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-3-44)Implement a reasoning structure for solvers to follow step-by-step and arrive at correct answer.
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-3-45)
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-3-46)Note: do NOT actually arrive at a conclusion in this pass. Your job is to generate a PLAN so that in the future you can fill it out and arrive at the correct conclusion for tasks like this
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-3-47)Self-Discovery Structured Response:
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-3-48)Follow the step-by-step reasoning plan in JSON to correctly solve the task. Fill in the values following the keys by reasoning specifically about the task given. Do not simply rephrase the keys.
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-3-49)
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-3-50)Reasoning Structure:
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-3-51)[33;1m[1;3m{reasoning_structure}[0m
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-3-52)
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-3-53)Task: [33;1m[1;3m{task_description}[0m

```


## Define the graph[¶](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#define-the-graph "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-4-1)fromtypingimport Optional
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-4-2)fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-4-3)
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-4-4)fromlangchain_core.output_parsersimport StrOutputParser
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-4-5)fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-4-6)
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-4-7)fromlanggraph.graphimport END, START, StateGraph
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-4-8)
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-4-9)
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-4-10)classSelfDiscoverState(TypedDict):
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-4-11)  reasoning_modules: str
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-4-12)  task_description: str
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-4-13)  selected_modules: Optional[str]
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-4-14)  adapted_modules: Optional[str]
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-4-15)  reasoning_structure: Optional[str]
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-4-16)  answer: Optional[str]
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-4-17)
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-4-18)
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-4-19)model = ChatOpenAI(temperature=0, model="gpt-4-turbo-preview")
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-4-20)
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-4-21)
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-4-22)defselect(inputs):
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-4-23)  select_chain = select_prompt | model | StrOutputParser()
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-4-24)  return {"selected_modules": select_chain.invoke(inputs)}
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-4-25)
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-4-26)
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-4-27)defadapt(inputs):
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-4-28)  adapt_chain = adapt_prompt | model | StrOutputParser()
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-4-29)  return {"adapted_modules": adapt_chain.invoke(inputs)}
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-4-30)
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-4-31)
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-4-32)defstructure(inputs):
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-4-33)  structure_chain = structured_prompt | model | StrOutputParser()
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-4-34)  return {"reasoning_structure": structure_chain.invoke(inputs)}
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-4-35)
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-4-36)
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-4-37)defreason(inputs):
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-4-38)  reasoning_chain = reasoning_prompt | model | StrOutputParser()
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-4-39)  return {"answer": reasoning_chain.invoke(inputs)}
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-4-40)
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-4-41)
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-4-42)graph = StateGraph(SelfDiscoverState)
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-4-43)graph.add_node(select)
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-4-44)graph.add_node(adapt)
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-4-45)graph.add_node(structure)
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-4-46)graph.add_node(reason)
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-4-47)graph.add_edge(START, "select")
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-4-48)graph.add_edge("select", "adapt")
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-4-49)graph.add_edge("adapt", "structure")
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-4-50)graph.add_edge("structure", "reason")
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-4-51)graph.add_edge("reason", END)
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-4-52)app = graph.compile()

```


API Reference: [StrOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.string.StrOutputParser.html) | [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html) | [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph)

## Invoke the graph[¶](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#invoke-the-graph "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-5-1)reasoning_modules = [
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-5-2)  "1. How could I devise an experiment to help solve that problem?",
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-5-3)  "2. Make a list of ideas for solving this problem, and apply them one by one to the problem to see if any progress can be made.",
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-5-4)  # "3. How could I measure progress on this problem?",
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-5-5)  "4. How can I simplify the problem so that it is easier to solve?",
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-5-6)  "5. What are the key assumptions underlying this problem?",
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-5-7)  "6. What are the potential risks and drawbacks of each solution?",
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-5-8)  "7. What are the alternative perspectives or viewpoints on this problem?",
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-5-9)  "8. What are the long-term implications of this problem and its solutions?",
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-5-10)  "9. How can I break down this problem into smaller, more manageable parts?",
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-5-11)  "10. Critical Thinking: This style involves analyzing the problem from different perspectives, questioning assumptions, and evaluating the evidence or information available. It focuses on logical reasoning, evidence-based decision-making, and identifying potential biases or flaws in thinking.",
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-5-12)  "11. Try creative thinking, generate innovative and out-of-the-box ideas to solve the problem. Explore unconventional solutions, thinking beyond traditional boundaries, and encouraging imagination and originality.",
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-5-13)  # "12. Seek input and collaboration from others to solve the problem. Emphasize teamwork, open communication, and leveraging the diverse perspectives and expertise of a group to come up with effective solutions.",
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-5-14)  "13. Use systems thinking: Consider the problem as part of a larger system and understanding the interconnectedness of various elements. Focuses on identifying the underlying causes, feedback loops, and interdependencies that influence the problem, and developing holistic solutions that address the system as a whole.",
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-5-15)  "14. Use Risk Analysis: Evaluate potential risks, uncertainties, and tradeoffs associated with different solutions or approaches to a problem. Emphasize assessing the potential consequences and likelihood of success or failure, and making informed decisions based on a balanced analysis of risks and benefits.",
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-5-16)  # "15. Use Reflective Thinking: Step back from the problem, take the time for introspection and self-reflection. Examine personal biases, assumptions, and mental models that may influence problem-solving, and being open to learning from past experiences to improve future approaches.",
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-5-17)  "16. What is the core issue or problem that needs to be addressed?",
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-5-18)  "17. What are the underlying causes or factors contributing to the problem?",
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-5-19)  "18. Are there any potential solutions or strategies that have been tried before? If yes, what were the outcomes and lessons learned?",
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-5-20)  "19. What are the potential obstacles or challenges that might arise in solving this problem?",
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-5-21)  "20. Are there any relevant data or information that can provide insights into the problem? If yes, what data sources are available, and how can they be analyzed?",
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-5-22)  "21. Are there any stakeholders or individuals who are directly affected by the problem? What are their perspectives and needs?",
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-5-23)  "22. What resources (financial, human, technological, etc.) are needed to tackle the problem effectively?",
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-5-24)  "23. How can progress or success in solving the problem be measured or evaluated?",
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-5-25)  "24. What indicators or metrics can be used?",
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-5-26)  "25. Is the problem a technical or practical one that requires a specific expertise or skill set? Or is it more of a conceptual or theoretical problem?",
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-5-27)  "26. Does the problem involve a physical constraint, such as limited resources, infrastructure, or space?",
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-5-28)  "27. Is the problem related to human behavior, such as a social, cultural, or psychological issue?",
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-5-29)  "28. Does the problem involve decision-making or planning, where choices need to be made under uncertainty or with competing objectives?",
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-5-30)  "29. Is the problem an analytical one that requires data analysis, modeling, or optimization techniques?",
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-5-31)  "30. Is the problem a design challenge that requires creative solutions and innovation?",
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-5-32)  "31. Does the problem require addressing systemic or structural issues rather than just individual instances?",
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-5-33)  "32. Is the problem time-sensitive or urgent, requiring immediate attention and action?",
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-5-34)  "33. What kinds of solution typically are produced for this kind of problem specification?",
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-5-35)  "34. Given the problem specification and the current best solution, have a guess about other possible solutions."
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-5-36)  "35. Let’s imagine the current best solution is totally wrong, what other ways are there to think about the problem specification?"
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-5-37)  "36. What is the best way to modify this current best solution, given what you know about these kinds of problem specification?"
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-5-38)  "37. Ignoring the current best solution, create an entirely new solution to the problem."
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-5-39)  # "38. Let’s think step by step."
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-5-40)  "39. Let’s make a step by step plan and implement it with good notation and explanation.",
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-5-41)]
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-5-42)
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-5-43)
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-5-44)task_example = "Lisa has 10 apples. She gives 3 apples to her friend and then buys 5 more apples from the store. How many apples does Lisa have now?"
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-5-45)
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-5-46)task_example = """This SVG path element <path d="M 55.57,80.69 L 57.38,65.80 M 57.38,65.80 L 48.90,57.46 M 48.90,57.46 L
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-5-47)45.58,47.78 M 45.58,47.78 L 53.25,36.07 L 66.29,48.90 L 78.69,61.09 L 55.57,80.69"/> draws a:
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-5-48)(A) circle (B) heptagon (C) hexagon (D) kite (E) line (F) octagon (G) pentagon(H) rectangle (I) sector (J) triangle"""
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-5-49)
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-5-50)reasoning_modules_str = "\n".join(reasoning_modules)
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-5-51)
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-5-52)for s in app.stream(
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-5-53)  {"task_description": task_example, "reasoning_modules": reasoning_modules_str}
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-5-54)):
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-5-55)  print(s)

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-6-1){'select': {'selected_modules': 'To solve the task of identifying the shape drawn by the SVG path element, the following reasoning modules are crucial:\n\n1. **Critical Thinking (10):** This involves analyzing the provided SVG path commands to understand how they contribute to forming a shape. It requires questioning assumptions (e.g., not assuming the shape is simple or common) and evaluating the information given in the path data.\n\n2. **Creative Thinking (11):** While the task seems straightforward, creative thinking can help in visualizing the shape described by the path commands without immediately drawing it. This involves imagining the transitions and connections between the points defined in the path.\n\n3. **Systems Thinking (13):** Understanding the SVG path as a system of coordinates and lines that connect to form a shape. This includes recognizing the interconnectedness of the start and end points of each line segment and how they contribute to the overall shape.\n\n4. **Analytical Problem Solving (29):** This task requires data analysis skills to interpret the SVG path commands and deduce the shape they form. Analyzing the coordinates and the movements (lines and moves) can reveal the structure of the shape.\n\n5. **Design Challenge (30):** Interpreting and visualizing SVG paths can be seen as a design challenge, requiring an understanding of how individual parts (line segments) come together to create a whole (shape).\n\n6. **Step-by-Step Planning and Implementation (39):** Formulating a plan to sequentially interpret each segment of the SVG path and understanding how each segment contributes to the overall shape. This could involve sketching the path based on the commands to better visualize the shape.\n\nThese modules collectively enable a comprehensive approach to solving the task, from understanding and analyzing the SVG path data to creatively and systematically deducing the shape it represents.'}}
[](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__codelineno-6-2){'adapt': {'adapted_modules': "To enhance the process of identifying the shape drawn by the SVG path element, the reasoning modules can be adapted and specified as follows:\n\n1. **Enhanced Critical Analysis (10):** This module focuses on a detailed examination of the SVG path commands, challenging initial perceptions and critically assessing each command's role in shaping the figure. It involves a deep dive into the syntax and semantics of the path data, ensuring no detail is overlooked, especially in recognizing less obvious or complex shapes.\n\n2. **Visual Creative Thinking (11):** Leveraging imagination to mentally construct the shape from the path commands, this module emphasizes the ability to visualize the sequential flow and connection of points without physical drawing. It encourages innovative approaches to mentally piecing together the described shape, enhancing the ability to predict the outcome based on abstract data.\n\n3. **Integrated Systems Analysis (13):** This module treats the SVG path as a complex system where each command and coordinate plays a critical role in the final shape. It focuses on understanding the relationship between individual path segments and their collective contribution to forming a coherent structure, emphasizing the holistic view of the path's construction.\n\n4. **Targeted Analytical Problem Solving (29):** Specializing in dissecting the SVG path's commands to systematically uncover the represented shape, this module applies precise analytical techniques to decode the sequence of movements and coordinates. It involves a methodical breakdown of the path data to reveal the underlying geometric figure.\n\n5. **Design Synthesis Challenge (30):** Approaching the task as a problem of synthesizing a coherent design from segmented inputs, this module requires an adept understanding of how discrete line segments interconnect to form a unified shape. It challenges one to think like a designer, piecing together the puzzle of path commands into a complete and recognizable form.\n\n6. **Sequential Interpretation and Visualization (39):** This module involves developing a step-by-step strategy for interpreting and visualizing the SVG path, focusing on the incremental construction of the shape from the path commands. It advocates for a systematic approach to translating the abstract commands into a tangible visual representation, potentially through sketching or mentally mapping the path's progression.\n\nBy refining these modules, the approach to solving the task becomes more targeted, enhancing the ability to accurately identify the shape described by the SVG path element."}}

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Language Agent Tree Search  ](https://langchain-ai.github.io/langgraph/tutorials/lats/lats/) [ Next  Chat Bot Evaluation as Multi-agent Simulation  ](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
