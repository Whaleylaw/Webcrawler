---
url: https://langchain-ai.github.io/langgraph/how-tos/map-reduce/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#how-to-create-map-reduce-branches-for-parallel-execution)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to create map-reduce branches for parallel execution 

[ ](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/?q= "Share")

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

How-to Guides 
        * LangGraph  LangGraph 
          * [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
          * [ Graph API Basics  ](https://langchain-ai.github.io/langgraph/how-tos#graph-api-basics)
          * Controllability  Controllability 
            * [ Controllability  ](https://langchain-ai.github.io/langgraph/how-tos#controllability)
            * How to create map-reduce branches for parallel execution  [ How to create map-reduce branches for parallel execution  ](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#setup)
              * [ Define the graph  ](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#define-the-graph)
              * [ Use the graph  ](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#use-the-graph)
            * [ How to combine control flow and state updates with Command  ](https://langchain-ai.github.io/langgraph/how-tos/command/)
            * [ How to add runtime configuration to your graph  ](https://langchain-ai.github.io/langgraph/how-tos/configuration/)
            * [ How to add node retry policies  ](https://langchain-ai.github.io/langgraph/how-tos/node-retries/)
            * [ How to return state before hitting recursion limit  ](https://langchain-ai.github.io/langgraph/how-tos/return-when-recursion-limit-hits/)
          * [ Persistence  ](https://langchain-ai.github.io/langgraph/how-tos#persistence)
          * [ Memory  ](https://langchain-ai.github.io/langgraph/how-tos#memory)
          * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraph/how-tos#human-in-the-loop)
          * [ Streaming  ](https://langchain-ai.github.io/langgraph/how-tos#streaming)
          * [ Tool calling  ](https://langchain-ai.github.io/langgraph/how-tos#tool-calling)
          * [ Subgraphs  ](https://langchain-ai.github.io/langgraph/how-tos#subgraphs)
          * [ Multi-agent  ](https://langchain-ai.github.io/langgraph/how-tos#multi-agent)
          * [ State Management  ](https://langchain-ai.github.io/langgraph/how-tos#state-management)
          * [ Other  ](https://langchain-ai.github.io/langgraph/how-tos#other)
          * [ Prebuilt ReAct Agent  ](https://langchain-ai.github.io/langgraph/how-tos#prebuilt-react-agent)
        * [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph-platform)
      * [ Concepts  ](https://langchain-ai.github.io/langgraph/concepts/)
      * [ Tutorials  ](https://langchain-ai.github.io/langgraph/tutorials/)
    * Resources  Resources 
      * [ Prebuilt Agents  ](https://langchain-ai.github.io/langgraph/prebuilt/)
      * [ Adopters  ](https://langchain-ai.github.io/langgraph/adopters/)
      * [ FAQ  ](https://langchain-ai.github.io/langgraph/concepts/faq/)
      * [ Troubleshooting  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraph/reference/graphs/)



Table of contents 

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#setup)
  * [ Define the graph  ](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#define-the-graph)
  * [ Use the graph  ](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#use-the-graph)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Controllability  ](https://langchain-ai.github.io/langgraph/how-tos#controllability)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/map-reduce.ipynb "Edit this page")

# How to create map-reduce branches for parallel execution[¶](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#how-to-create-map-reduce-branches-for-parallel-execution "Permanent link")

Prerequisites

This guide assumes familiarity with the following: 

  * [ LangGraph Glossary ](https://langchain-ai.github.io/langgraph/concepts/low_level/)
  * [ Send API ](https://langchain-ai.github.io/langgraph/concepts/low_level/#send)
  * [ Chat Models ](https://python.langchain.com/docs/concepts/#chat-models/)
  * [ Structured Output ](https://python.langchain.com/docs/concepts/#structured-output)



[Map-reduce](https://en.wikipedia.org/wiki/MapReduce) operations are essential for efficient task decomposition and parallel processing. This approach involves breaking a task into smaller sub-tasks, processing each sub-task in parallel, and aggregating the results across all of the completed sub-tasks. 

Consider this example: given a general topic from the user, generate a list of related subjects, generate a joke for each subject, and select the best joke from the resulting list. In this design pattern, a first node may generate a list of objects (e.g., related subjects) and we want to apply some other node (e.g., generate a joke) to all those objects (e.g., subjects). However, two main challenges arise.

(1) the number of objects (e.g., subjects) may be unknown ahead of time (meaning the number of edges may not be known) when we lay out the graph and (2) the input State to the downstream Node should be different (one for each generated object).

LangGraph addresses these challenges [through its `Send` API](https://langchain-ai.github.io/langgraph/concepts/low_level/#send). By utilizing conditional edges, `Send` can distribute different states (e.g., subjects) to multiple instances of a node (e.g., joke generation). Importantly, the sent state can differ from the core graph's state, allowing for flexible and dynamic workflow management. 

![Screenshot 2024-07-12 at 9.45.40 AM.png]()

## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#setup "Permanent link")

First, let's install the required packages and set our API keys

```
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-0-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-0-2)%pip install -U langchain-anthropic langgraph

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-1-1)importos
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-1-2)importgetpass
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-1-5)def_set_env(name: str):
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-1-6)  if not os.getenv(name):
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-1-7)    os.environ[name] = getpass.getpass(f"{name}: ")
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-1-8)
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-1-10)_set_env("ANTHROPIC_API_KEY")

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Define the graph[¶](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#define-the-graph "Permanent link")

Using Pydantic with LangChain

This notebook uses Pydantic v2 `BaseModel`, which requires `langchain-core >= 0.3`. Using `langchain-core < 0.3` will result in errors due to mixing of Pydantic v1 and v2 `BaseModels`. 

```
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-1)importoperator
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-2)fromtypingimport Annotated
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-3)fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-4)
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-5)fromlangchain_anthropicimport ChatAnthropic
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-6)
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-7)fromlanggraph.typesimport Send
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-8)fromlanggraph.graphimport END, StateGraph, START
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-9)
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-10)frompydanticimport BaseModel, Field
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-11)
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-12)# Model and prompts
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-13)# Define model and prompts we will use
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-14)subjects_prompt = """Generate a comma separated list of between 2 and 5 examples related to: {topic}."""
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-15)joke_prompt = """Generate a joke about {subject}"""
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-16)best_joke_prompt = """Below are a bunch of jokes about {topic}. Select the best one! Return the ID of the best one.
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-17)
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-18){jokes}"""
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-19)
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-20)
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-21)classSubjects(BaseModel):
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-22)  subjects: list[str]
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-23)
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-24)
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-25)classJoke(BaseModel):
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-26)  joke: str
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-27)
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-28)
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-29)classBestJoke(BaseModel):
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-30)  id: int = Field(description="Index of the best joke, starting with 0", ge=0)
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-31)
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-32)
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-33)model = ChatAnthropic(model="claude-3-5-sonnet-20240620")
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-34)
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-35)# Graph components: define the components that will make up the graph
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-36)
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-37)
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-38)# This will be the overall state of the main graph.
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-39)# It will contain a topic (which we expect the user to provide)
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-40)# and then will generate a list of subjects, and then a joke for
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-41)# each subject
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-42)classOverallState(TypedDict):
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-43)  topic: str
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-44)  subjects: list
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-45)  # Notice here we use the operator.add
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-46)  # This is because we want combine all the jokes we generate
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-47)  # from individual nodes back into one list - this is essentially
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-48)  # the "reduce" part
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-49)  jokes: Annotated[list, operator.add]
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-50)  best_selected_joke: str
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-51)
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-52)
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-53)# This will be the state of the node that we will "map" all
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-54)# subjects to in order to generate a joke
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-55)classJokeState(TypedDict):
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-56)  subject: str
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-57)
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-58)
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-59)# This is the function we will use to generate the subjects of the jokes
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-60)defgenerate_topics(state: OverallState):
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-61)  prompt = subjects_prompt.format(topic=state["topic"])
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-62)  response = model.with_structured_output(Subjects).invoke(prompt)
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-63)  return {"subjects": response.subjects}
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-64)
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-65)
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-66)# Here we generate a joke, given a subject
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-67)defgenerate_joke(state: JokeState):
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-68)  prompt = joke_prompt.format(subject=state["subject"])
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-69)  response = model.with_structured_output(Joke).invoke(prompt)
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-70)  return {"jokes": [response.joke]}
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-71)
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-72)
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-73)# Here we define the logic to map out over the generated subjects
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-74)# We will use this an edge in the graph
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-75)defcontinue_to_jokes(state: OverallState):
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-76)  # We will return a list of `Send` objects
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-77)  # Each `Send` object consists of the name of a node in the graph
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-78)  # as well as the state to send to that node
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-79)  return [Send("generate_joke", {"subject": s}) for s in state["subjects"]]
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-80)
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-81)
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-82)# Here we will judge the best joke
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-83)defbest_joke(state: OverallState):
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-84)  jokes = "\n\n".join(state["jokes"])
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-85)  prompt = best_joke_prompt.format(topic=state["topic"], jokes=jokes)
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-86)  response = model.with_structured_output(BestJoke).invoke(prompt)
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-87)  return {"best_selected_joke": state["jokes"][response.id]}
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-88)
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-89)
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-90)# Construct the graph: here we put everything together to construct our graph
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-91)graph = StateGraph(OverallState)
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-92)graph.add_node("generate_topics", generate_topics)
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-93)graph.add_node("generate_joke", generate_joke)
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-94)graph.add_node("best_joke", best_joke)
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-95)graph.add_edge(START, "generate_topics")
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-96)graph.add_conditional_edges("generate_topics", continue_to_jokes, ["generate_joke"])
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-97)graph.add_edge("generate_joke", "best_joke")
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-98)graph.add_edge("best_joke", END)
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-2-99)app = graph.compile()

```


API Reference: [ChatAnthropic](https://python.langchain.com/api_reference/anthropic/chat_models/langchain_anthropic.chat_models.ChatAnthropic.html) | [Send](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Send) | [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START)

```
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-3-1)fromIPython.displayimport Image
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-3-2)
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-3-3)Image(app.get_graph().draw_mermaid_png())

```


![]()

## Use the graph[¶](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#use-the-graph "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-4-1)# Call the graph: here we call it to generate a list of jokes
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-4-2)for s in app.stream({"topic": "animals"}):
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-4-3)  print(s)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-5-1){'generate_topics': {'subjects': ['Lions', 'Elephants', 'Penguins', 'Dolphins']}}
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-5-2){'generate_joke': {'jokes': ["Why don't elephants use computers? They're afraid of the mouse!"]}}
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-5-3){'generate_joke': {'jokes': ["Why don't dolphins use smartphones? Because they're afraid of phishing!"]}}
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-5-4){'generate_joke': {'jokes': ["Why don't you see penguins in Britain? Because they're afraid of Wales!"]}}
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-5-5){'generate_joke': {'jokes': ["Why don't lions like fast food? Because they can't catch it!"]}}
[](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__codelineno-5-6){'best_joke': {'best_selected_joke': "Why don't dolphins use smartphones? Because they're afraid of phishing!"}}

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to visualize your graph  ](https://langchain-ai.github.io/langgraph/how-tos/visualization/) [ Next  How to combine control flow and state updates with Command  ](https://langchain-ai.github.io/langgraph/how-tos/command/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/map-reduce/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
