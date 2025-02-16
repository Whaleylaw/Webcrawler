---
url: https://langchain-ai.github.io/langgraphjs/concepts/low_level/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#langgraph-glossary)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

LangGraph Glossary 

[ ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/?q= "Share")

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
          * [ Why LangGraph?  ](https://langchain-ai.github.io/langgraphjs/concepts/high_level/)
          * LangGraph Glossary  [ LangGraph Glossary  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/) Table of contents 
            * [ Graphs  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#graphs)
              * [ StateGraph  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#stategraph)
              * [ MessageGraph (legacy)  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#messagegraph)
              * [ Compiling your graph  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#compiling-your-graph)
            * [ State  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#state)
              * [ Annotation  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#annotation)
                * [ Multiple schemas  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#multiple-schemas)
              * [ Reducers  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#reducers)
              * [ Working with Messages in Graph State  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#working-with-messages-in-graph-state)
                * [ Why use messages?  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#why-use-messages)
                * [ Using Messages in your Graph  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#using-messages-in-your-graph)
                * [ Serialization  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#serialization)
                * [ MessagesAnnotation  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#messagesannotation)
            * [ Nodes  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#nodes)
              * [ START Node  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#start-node)
              * [ END Node  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#end-node)
            * [ Edges  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#edges)
              * [ Normal Edges  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#normal-edges)
              * [ Conditional Edges  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#conditional-edges)
              * [ Entry Point  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#entry-point)
              * [ Conditional Entry Point  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#conditional-entry-point)
            * [ Send  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#send)
            * [ Command  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#command)
              * [ When should I use Command instead of conditional edges?  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#when-should-i-use-command-instead-of-conditional-edges)
              * [ Navigating to a node in a parent graph  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#navigating-to-a-node-in-a-parent-graph)
              * [ Using inside tools  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#using-inside-tools)
              * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#human-in-the-loop)
            * [ Persistence  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#persistence)
            * [ Threads  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#threads)
            * [ Storage  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#storage)
            * [ Graph Migrations  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#graph-migrations)
            * [ Configuration  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#configuration)
            * [ Breakpoints  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#breakpoints)
              * [ Dynamic Breakpoints  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#dynamic-breakpoints)
            * [ Subgraphs  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#subgraphs)
              * [ As a compiled graph  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#as-a-compiled-graph)
              * [ As a function  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#as-a-function)
            * [ Visualization  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#visualization)
            * [ Streaming  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#streaming)
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

  * [ Graphs  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#graphs)
    * [ StateGraph  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#stategraph)
    * [ MessageGraph (legacy)  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#messagegraph)
    * [ Compiling your graph  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#compiling-your-graph)
  * [ State  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#state)
    * [ Annotation  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#annotation)
      * [ Multiple schemas  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#multiple-schemas)
    * [ Reducers  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#reducers)
    * [ Working with Messages in Graph State  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#working-with-messages-in-graph-state)
      * [ Why use messages?  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#why-use-messages)
      * [ Using Messages in your Graph  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#using-messages-in-your-graph)
      * [ Serialization  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#serialization)
      * [ MessagesAnnotation  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#messagesannotation)
  * [ Nodes  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#nodes)
    * [ START Node  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#start-node)
    * [ END Node  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#end-node)
  * [ Edges  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#edges)
    * [ Normal Edges  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#normal-edges)
    * [ Conditional Edges  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#conditional-edges)
    * [ Entry Point  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#entry-point)
    * [ Conditional Entry Point  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#conditional-entry-point)
  * [ Send  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#send)
  * [ Command  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#command)
    * [ When should I use Command instead of conditional edges?  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#when-should-i-use-command-instead-of-conditional-edges)
    * [ Navigating to a node in a parent graph  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#navigating-to-a-node-in-a-parent-graph)
    * [ Using inside tools  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#using-inside-tools)
    * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#human-in-the-loop)
  * [ Persistence  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#persistence)
  * [ Threads  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#threads)
  * [ Storage  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#storage)
  * [ Graph Migrations  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#graph-migrations)
  * [ Configuration  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#configuration)
  * [ Breakpoints  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#breakpoints)
    * [ Dynamic Breakpoints  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#dynamic-breakpoints)
  * [ Subgraphs  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#subgraphs)
    * [ As a compiled graph  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#as-a-compiled-graph)
    * [ As a function  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#as-a-function)
  * [ Visualization  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#visualization)
  * [ Streaming  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#streaming)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ Concepts  ](https://langchain-ai.github.io/langgraphjs/concepts/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/concepts#langgraph)



# LangGraph Glossary[¶](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#langgraph-glossary "Permanent link")

## Graphs[¶](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#graphs "Permanent link")

At its core, LangGraph models agent workflows as graphs. You define the behavior of your agents using three key components:

  1. `State`[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#state): A shared data structure that represents the current snapshot of your application. It is represented by an `Annotation`[](https://langchain-ai.github.io/langgraphjs/reference/modules/langgraph.Annotation.html) object.

  2. `Nodes`[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#nodes): JavaScript/TypeScript functions that encode the logic of your agents. They receive the current `State` as input, perform some computation or side-effect, and return an updated `State`.

  3. `Edges`[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#edges): JavaScript/TypeScript functions that determine which `Node` to execute next based on the current `State`. They can be conditional branches or fixed transitions.




By composing `Nodes` and `Edges`, you can create complex, looping workflows that evolve the `State` over time. The real power, though, comes from how LangGraph manages that `State`. To emphasize: `Nodes` and `Edges` are nothing more than JavaScript/TypeScript functions - they can contain an LLM or just good ol' JavaScript/TypeScript code.

In short: _nodes do the work. edges tell what to do next_.

LangGraph's underlying graph algorithm uses [message passing](https://en.wikipedia.org/wiki/Message_passing) to define a general program. When a Node completes its operation, it sends messages along one or more edges to other node(s). These recipient nodes then execute their functions, pass the resulting messages to the next set of nodes, and the process continues. Inspired by Google's [Pregel](https://research.google/pubs/pregel-a-system-for-large-scale-graph-processing/) system, the program proceeds in discrete "super-steps."

A super-step can be considered a single iteration over the graph nodes. Nodes that run in parallel are part of the same super-step, while nodes that run sequentially belong to separate super-steps. At the start of graph execution, all nodes begin in an `inactive` state. A node becomes `active` when it receives a new message (state) on any of its incoming edges (or "channels"). The active node then runs its function and responds with updates. At the end of each super-step, nodes with no incoming messages vote to `halt` by marking themselves as `inactive`. The graph execution terminates when all nodes are `inactive` and no messages are in transit.

### StateGraph[¶](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#stategraph "Permanent link")

The `StateGraph` class is the main graph class to use. This is parameterized by a user defined `State` object. (defined using the `Annotation` object and passed as the first argument)

### MessageGraph (legacy)[¶](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#messagegraph "Permanent link")

The `MessageGraph` class is a special type of graph. The `State` of a `MessageGraph` is ONLY an array of messages. This class is rarely used except for chatbots, as most applications require the `State` to be more complex than an array of messages.

### Compiling your graph[¶](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#compiling-your-graph "Permanent link")

To build your graph, you first define the [state](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#state), you then add [nodes](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#nodes) and [edges](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#edges), and then you compile it. What exactly is compiling your graph and why is it needed?

Compiling is a pretty simple step. It provides a few basic checks on the structure of your graph (no orphaned nodes, etc). It is also where you can specify runtime args like checkpointers and [breakpoints](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#breakpoints). You compile your graph by just calling the `.compile` method:

```
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-0-1)constgraph=graphBuilder.compile(...);

```


You **MUST** compile your graph before you can use it.

## State[¶](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#state "Permanent link")

The first thing you do when you define a graph is define the `State` of the graph. The `State` includes information on the structure of the graph, as well as `reducer`[ functions](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#reducers) which specify how to apply updates to the state. The schema of the `State` will be the input schema to all `Nodes` and `Edges` in the graph, and should be defined using an `Annotation`[](https://langchain-ai.github.io/langgraphjs/reference/modules/langgraph.Annotation.html) object. All `Nodes` will emit updates to the `State` which are then applied using the specified `reducer` function.

### Annotation[¶](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#annotation "Permanent link")

The way to specify the schema of a graph is by defining a root `Annotation`[](https://langchain-ai.github.io/langgraphjs/reference/modules/langgraph.Annotation.html) object, where each key is an item in the state.

#### Multiple schemas[¶](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#multiple-schemas "Permanent link")

Typically, all graph nodes communicate with a single state annotation. This means that they will read and write to the same state channels. But, there are cases where we want more control over this:

  * Internal nodes can pass information that is not required in the graph's input / output.
  * We may also want to use different input / output schemas for the graph. The output might, for example, only contain a single relevant output key.



It is possible to have nodes write to private state channels inside the graph for internal node communication. We can simply define a private annotation, `PrivateState`. See [this notebook](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/) for more detail.

It is also possible to define explicit input and output schemas for a graph. In these cases, we define an "internal" schema that contains _all_ keys relevant to graph operations. But, we also define `input` and `output` schemas that are sub-sets of the "internal" schema to constrain the input and output of the graph. See [this guide](https://langchain-ai.github.io/langgraphjs/how-tos/input_output_schema/) for more detail.

Let's look at an example:

```
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-1-1)import{Annotation,StateGraph}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-1-2)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-1-3)constInputStateAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-1-4)user_input:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-1-5)});
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-1-6)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-1-7)constOutputStateAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-1-8)graph_output:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-1-9)});
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-1-10)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-1-11)constOverallStateAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-1-12)foo:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-1-13)bar:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-1-14)user_input:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-1-15)graph_output:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-1-16)});
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-1-17)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-1-18)constnode1=async(state:typeofInputStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-1-19)// Write to OverallStateAnnotation
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-1-20)return{foo:state.user_input+" name"};
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-1-21)};
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-1-22)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-1-23)constnode2=async(state:typeofOverallStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-1-24)// Read from OverallStateAnnotation, write to OverallStateAnnotation
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-1-25)return{bar:state.foo+" is"};
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-1-26)};
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-1-27)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-1-28)constnode3=async(state:typeofOverallStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-1-29)// Read from OverallStateAnnotation, write to OutputStateAnnotation
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-1-30)return{graph_output:state.bar+" Lance"};
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-1-31)};
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-1-32)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-1-33)constgraph=newStateGraph({
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-1-34)input:InputStateAnnotation,
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-1-35)output:OutputStateAnnotation,
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-1-36)stateSchema:OverallStateAnnotation,
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-1-37)})
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-1-38).addNode("node1",node1)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-1-39).addNode("node2",node2)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-1-40).addNode("node3",node3)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-1-41).addEdge("__start__","node1")
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-1-42).addEdge("node1","node2")
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-1-43).addEdge("node2","node3")
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-1-44).compile();
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-1-45)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-1-46)awaitgraph.invoke({user_input:"My"});

```


```
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-2-1){ graph_output: "My name is Lance" }

```


Note that we pass `state: typeof InputStateAnnotation.State` as the input schema to `node1`. But, we write out to `foo`, a channel in `OverallStateAnnotation`. How can we write out to a state channel that is not included in the input schema? This is because a node _can write to any state channel in the graph state._ The graph state is the union of of the state channels defined at initialization, which includes `OverallStateAnnotation` and the filters `InputStateAnnotation` and `OutputStateAnnotation`.

### Reducers[¶](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#reducers "Permanent link")

Reducers are key to understanding how updates from nodes are applied to the `State`. Each key in the `State` has its own independent reducer function. If no reducer function is explicitly specified then it is assumed that all updates to that key should override it. Let's take a look at a few examples to understand them better.

**Example A:**

```
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-3-1)import{StateGraph,Annotation}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-3-2)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-3-3)constState=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-3-4)foo:Annotation<number>,
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-3-5)bar:Annotation<string[]>,
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-3-6)});
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-3-7)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-3-8)constgraphBuilder=newStateGraph(State);

```


In this example, no reducer functions are specified for any key. Let's assume the input to the graph is `{ foo: 1, bar: ["hi"] }`. Let's then assume the first `Node` returns `{ foo: 2 }`. This is treated as an update to the state. Notice that the `Node` does not need to return the whole `State` schema - just an update. After applying this update, the `State` would then be `{ foo: 2, bar: ["hi"] }`. If the second node returns `{ bar: ["bye"] }` then the `State` would then be `{ foo: 2, bar: ["bye"] }`

**Example B:**

```
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-4-1)import{StateGraph,Annotation}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-4-2)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-4-3)constState=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-4-4)foo:Annotation<number>,
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-4-5)bar:Annotation<string[]>({
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-4-6)reducer:(state:string[],update:string[])=>state.concat(update),
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-4-7)default:()=>[],
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-4-8)}),
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-4-9)});
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-4-10)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-4-11)constgraphBuilder=newStateGraph(State);

```


In this example, we've updated our `bar` field to be an object containing a `reducer` function. This function will always accept two positional arguments: `state` and `update`, with `state` representing the current state value, and `update` representing the update returned from a `Node`. Note that the first key remains unchanged. Let's assume the input to the graph is `{ foo: 1, bar: ["hi"] }`. Let's then assume the first `Node` returns `{ foo: 2 }`. This is treated as an update to the state. Notice that the `Node` does not need to return the whole `State` schema - just an update. After applying this update, the `State` would then be `{ foo: 2, bar: ["hi"] }`. If the second node returns`{ bar: ["bye"] }` then the `State` would then be `{ foo: 2, bar: ["hi", "bye"] }`. Notice here that the `bar` key is updated by concatenating the two arrays together.

### Working with Messages in Graph State[¶](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#working-with-messages-in-graph-state "Permanent link")

#### Why use messages?[¶](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#why-use-messages "Permanent link")

Most modern LLM providers have a chat model interface that accepts a list of messages as input. LangChain's `ChatModel`[](https://js.langchain.com/docs/concepts/#chat-models) in particular accepts a list of `Message` objects as inputs. These messages come in a variety of forms such as `HumanMessage` (user input) or `AIMessage` (LLM response). To read more about what message objects are, please refer to [this](https://js.langchain.com/docs/concepts/#message-types) conceptual guide.

#### Using Messages in your Graph[¶](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#using-messages-in-your-graph "Permanent link")

In many cases, it is helpful to store prior conversation history as a list of messages in your graph state. To do so, we can add a key (channel) to the graph state that stores a list of `Message` objects and annotate it with a reducer function (see `messages` key in the example below). The reducer function is vital to telling the graph how to update the list of `Message` objects in the state with each state update (for example, when a node sends an update). If you don't specify a reducer, every state update will overwrite the list of messages with the most recently provided value.

However, you might also want to manually update messages in your graph state (e.g. human-in-the-loop). If you were to use something like `(a, b) => a.concat(b)` as a reducer, the manual state updates you send to the graph would be appended to the existing list of messages, instead of updating existing messages. To avoid that, you need a reducer that can keep track of message IDs and overwrite existing messages, if updated. To achieve this, you can use the prebuilt `messagesStateReducer` function. For brand new messages, it will simply append to existing list, but it will also handle the updates for existing messages correctly.

#### Serialization[¶](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#serialization "Permanent link")

In addition to keeping track of message IDs, the `messagesStateReducer` function will also try to deserialize messages into LangChain `Message` objects whenever a state update is received on the `messages` channel. This allows sending graph inputs / state updates in the following format:

```
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-5-1)// this is supported
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-5-2){
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-5-3)messages:[newHumanMessage({content:"message"})];
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-5-4)}
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-5-5)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-5-6)// and this is also supported
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-5-7){
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-5-8)messages:[{role:"user",content:"message"}];
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-5-9)}

```


Below is an example of a graph state annotation that uses `messagesStateReducer` as it's reducer function.

```
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-6-1)importtype{BaseMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-6-2)import{Annotation,typeMessages}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-6-3)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-6-4)constStateAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-6-5)messages:Annotation<BaseMessage[],Messages>({
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-6-6)reducer:messagesStateReducer,
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-6-7)}),
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-6-8)});

```


#### MessagesAnnotation[¶](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#messagesannotation "Permanent link")

Since having a list of messages in your state is so common, there exists a prebuilt annotation called `MessagesAnnotation` which makes it easy to use messages as graph state. `MessagesAnnotation` is defined with a single `messages` key which is a list of `BaseMessage` objects and uses the `messagesStateReducer` reducer.

```
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-7-1)import{MessagesAnnotation,StateGraph}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-7-2)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-7-3)constgraph=newStateGraph(MessagesAnnotation)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-7-4).addNode(...)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-7-5)...

```


Is equivalent to initializing your state manually like this:

```
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-8-1)import{BaseMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-8-2)import{Annotation,StateGraph,messagesStateReducer}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-8-3)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-8-4)exportconstStateAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-8-5)messages:Annotation<BaseMessage[]>({
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-8-6)reducer:messagesStateReducer,
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-8-7)default:()=>[],
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-8-8)}),
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-8-9)});
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-8-10)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-8-11)constgraph=newStateGraph(StateAnnotation)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-8-12).addNode(...)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-8-13)...

```


The state of a `MessagesAnnotation` has a single key called `messages`. This is an array of `BaseMessage`s, with `messagesStateReducer`[](https://langchain-ai.github.io/langgraphjs/reference/functions/langgraph.messagesStateReducer.html) as a reducer. `messagesStateReducer` basically adds messages to the existing list (it also does some nice extra things, like convert from OpenAI message format to the standard LangChain message format, handle updates based on message IDs, etc).

We often see an array of messages being a key component of state, so this prebuilt state is intended to make it easy to use messages. Typically, there is more state to track than just messages, so we see people extend this state and add more fields, like:

```
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-9-1)import{Annotation,MessagesAnnotation}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-9-2)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-9-3)constStateWithDocuments=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-9-4)...MessagesAnnotation.spec,// Spread in the messages state
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-9-5)documents:Annotation<string[]>,
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-9-6)});

```


## Nodes[¶](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#nodes "Permanent link")

In LangGraph, nodes are typically JavaScript/TypeScript functions (sync or `async`) where the **first** positional argument is the [state](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#state), and (optionally), the **second** positional argument is a "config", containing optional [configurable parameters](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#configuration) (such as a `thread_id`).

Similar to `NetworkX`, you add these nodes to a graph using the [addNode](https://langchain-ai.github.io/langgraphjs/reference/classes/langgraph.StateGraph.html#addNode) method:

```
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-10-1)import{RunnableConfig}from"@langchain/core/runnables";
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-10-2)import{StateGraph,Annotation}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-10-3)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-10-4)constGraphAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-10-5)input:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-10-6)results:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-10-7)});
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-10-8)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-10-9)// The state type can be extracted using `typeof <annotation variable name>.State`
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-10-10)constmyNode=(state:typeofGraphAnnotation.State,config?:RunnableConfig)=>{
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-10-11)console.log("In node: ",config.configurable?.user_id);
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-10-12)return{
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-10-13)results:`Hello, ${state.input}!`
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-10-14)};
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-10-15)};
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-10-16)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-10-17)// The second argument is optional
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-10-18)constmyOtherNode=(state:typeofGraphAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-10-19)returnstate;
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-10-20)};
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-10-21)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-10-22)constbuilder=newStateGraph(GraphAnnotation)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-10-23).addNode("myNode",myNode)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-10-24).addNode("myOtherNode",myOtherNode)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-10-25)...

```


Behind the scenes, functions are converted to [RunnableLambda's](https://v02.api.js.langchain.com/classes/langchain_core_runnables.RunnableLambda.html), which adds batch and streaming support to your function, along with native tracing and debugging.

### `START` Node[¶](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#start-node "Permanent link")

The `START` Node is a special node that represents the node sends user input to the graph. The main purpose for referencing this node is to determine which nodes should be called first.

```
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-11-1)import{START}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-11-2)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-11-3)graph.addEdge(START,"nodeA");

```


### `END` Node[¶](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#end-node "Permanent link")

The `END` Node is a special node that represents a terminal node. This node is referenced when you want to denote which edges have no actions after they are done.

```
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-12-1)import{END}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-12-2)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-12-3)graph.addEdge("nodeA",END);

```


## Edges[¶](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#edges "Permanent link")

Edges define how the logic is routed and how the graph decides to stop. This is a big part of how your agents work and how different nodes communicate with each other. There are a few key types of edges:

  * Normal Edges: Go directly from one node to the next.
  * Conditional Edges: Call a function to determine which node(s) to go to next.
  * Entry Point: Which node to call first when user input arrives.
  * Conditional Entry Point: Call a function to determine which node(s) to call first when user input arrives.



A node can have MULTIPLE outgoing edges. If a node has multiple out-going edges, **all** of those destination nodes will be executed in parallel as a part of the next superstep.

### Normal Edges[¶](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#normal-edges "Permanent link")

If you **always** want to go from node A to node B, you can use the [addEdge](https://langchain-ai.github.io/langgraphjs/reference/classes/langgraph.StateGraph.html#addEdge) method directly.

```
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-13-1)graph.addEdge("nodeA","nodeB");

```


### Conditional Edges[¶](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#conditional-edges "Permanent link")

If you want to **optionally** route to 1 or more edges (or optionally terminate), you can use the [addConditionalEdges](https://langchain-ai.github.io/langgraphjs/reference/classes/langgraph.StateGraph.html#addConditionalEdges) method. This method accepts the name of a node and a "routing function" to call after that node is executed:

```
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-14-1)graph.addConditionalEdges("nodeA",routingFunction);

```


Similar to nodes, the `routingFunction` accept the current `state` of the graph and return a value.

By default, the return value `routingFunction` is used as the name of the node (or an array of nodes) to send the state to next. All those nodes will be run in parallel as a part of the next superstep.

You can optionally provide an object that maps the `routingFunction`'s output to the name of the next node.

```
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-15-1)graph.addConditionalEdges("nodeA",routingFunction,{
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-15-2)true:"nodeB",
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-15-3)false:"nodeC",
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-15-4)});

```


Tip

Use `Command`[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#command) instead of conditional edges if you want to combine state updates and routing in a single function.

### Entry Point[¶](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#entry-point "Permanent link")

The entry point is the first node(s) that are run when the graph starts. You can use the `addEdge`[](https://langchain-ai.github.io/langgraphjs/reference/classes/langgraph.StateGraph.html#addEdge) method from the virtual `START`[](https://langchain-ai.github.io/langgraphjs/reference/variables/langgraph.START.html) node to the first node to execute to specify where to enter the graph.

```
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-16-1)import{START}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-16-2)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-16-3)graph.addEdge(START,"nodeA");

```


### Conditional Entry Point[¶](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#conditional-entry-point "Permanent link")

A conditional entry point lets you start at different nodes depending on custom logic. You can use `addConditionalEdges`[](https://langchain-ai.github.io/langgraphjs/reference/classes/langgraph.StateGraph.html#addConditionalEdges) from the virtual `START`[](https://langchain-ai.github.io/langgraphjs/reference/variables/langgraph.START.html) node to accomplish this.

```
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-17-1)import{START}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-17-2)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-17-3)graph.addConditionalEdges(START,routingFunction);

```


You can optionally provide an object that maps the `routingFunction`'s output to the name of the next node.

```
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-18-1)graph.addConditionalEdges(START,routingFunction,{
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-18-2)true:"nodeB",
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-18-3)false:"nodeC",
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-18-4)});

```


## `Send`[¶](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#send "Permanent link")

By default, `Nodes` and `Edges` are defined ahead of time and operate on the same shared state. However, there can be cases where the exact edges are not known ahead of time and/or you may want different versions of `State` to exist at the same time. A common of example of this is with `map-reduce` design patterns. In this design pattern, a first node may generate an array of objects, and you may want to apply some other node to all those objects. The number of objects may be unknown ahead of time (meaning the number of edges may not be known) and the input `State` to the downstream `Node` should be different (one for each generated object).

To support this design pattern, LangGraph supports returning `Send`[](https://langchain-ai.github.io/langgraphjs/reference/classes/langgraph.Send.html) objects from conditional edges. `Send` takes two arguments: first is the name of the node, and second is the state to pass to that node.

```
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-19-1)constcontinueToJokes=(state:{subjects:string[]})=>{
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-19-2)returnstate.subjects.map(
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-19-3)(subject)=>newSend("generate_joke",{subject})
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-19-4));
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-19-5)};
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-19-6)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-19-7)graph.addConditionalEdges("nodeA",continueToJokes);

```


## `Command`[¶](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#command "Permanent link")

Tip

This functionality requires `@langchain/langgraph>=0.2.31`.

It can be convenient to combine control flow (edges) and state updates (nodes). For example, you might want to BOTH perform state updates AND decide which node to go to next in the SAME node rather than use a conditional edge. LangGraph provides a way to do so by returning a `Command`[](https://langchain-ai.github.io/langgraphjs/reference/classes/langgraph.Command.html) object from node functions:

```
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-20-1)import{StateGraph,Annotation,Command}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-20-2)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-20-3)constStateAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-20-4)foo:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-20-5)});
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-20-6)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-20-7)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-20-8)constmyNode=(state:typeofStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-20-9)returnnewCommand({
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-20-10)// state update
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-20-11)update:{
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-20-12)foo:"bar",
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-20-13)},
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-20-14)// control flow
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-20-15)goto:"myOtherNode",
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-20-16)});
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-20-17)};

```


With `Command` you can also achieve dynamic control flow behavior (identical to [conditional edges](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#conditional-edges)):

```
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-21-1)constmyNode=async(state:typeofStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-21-2)if(state.foo==="bar"){
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-21-3)returnnewCommand({
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-21-4)update:{
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-21-5)foo:"baz",
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-21-6)},
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-21-7)goto:"myOtherNode",
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-21-8)});
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-21-9)}
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-21-10)// ...
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-21-11)};

```


Important

When returning `Command` in your node functions, you must also add an `ends` parameter with the list of node names the node is routing to, e.g. `.addNode("myNode", myNode, { ends: ["myOtherNode"] })`. This is necessary for graph compilation and validation, and indicates that `myNode` can navigate to `myOtherNode`.

Check out this [how-to guide](https://langchain-ai.github.io/langgraphjs/how-tos/command/) for an end-to-end example of how to use `Command`.

### When should I use Command instead of conditional edges?[¶](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#when-should-i-use-command-instead-of-conditional-edges "Permanent link")

Use `Command` when you need to **both** update the graph state **and** route to a different node. For example, when implementing [multi-agent handoffs](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#handoffs) where it's important to route to a different agent and pass some information to that agent.

Use [conditional edges](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#conditional-edges) to route between nodes conditionally without updating the state.

### Navigating to a node in a parent graph[¶](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#navigating-to-a-node-in-a-parent-graph "Permanent link")

If you are using [subgraphs](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#subgraphs), you might want to navigate from a node a subgraph to a different subgraph (i.e. a different node in the parent graph). To do so, you can specify `graph: Command.PARENT` in `Command`:

```
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-22-1)constmyNode=(state:typeofStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-22-2)returnnewCommand({
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-22-3)update:{foo:"bar"},
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-22-4)goto:"other_subgraph",// where `other_subgraph` is a node in the parent graph
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-22-5)graph:Command.PARENT,
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-22-6)});
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-22-7)};

```


Note

Setting `graph` to `Command.PARENT` will navigate to the closest parent graph.

This is particularly useful when implementing [multi-agent handoffs](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#handoffs).

### Using inside tools[¶](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#using-inside-tools "Permanent link")

A common use case is updating graph state from inside a tool. For example, in a customer support application you might want to look up customer information based on their account number or ID in the beginning of the conversation. To update the graph state from the tool, you can return `Command({ update: { my_custom_key: "foo", messages: [...] } })` from the tool:

```
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-23-1)import{tool}from"@langchain/core/tools";
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-23-2)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-23-3)constlookupUserInfo=tool(async(input,config)=>{
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-23-4)constuserInfo=getUserInfo(config);
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-23-5)returnnewCommand({
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-23-6)// update state keys
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-23-7)update:{
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-23-8)user_info:userInfo,
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-23-9)messages:[
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-23-10)newToolMessage({
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-23-11)content:"Successfully looked up user information",
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-23-12)tool_call_id:config.toolCall.id,
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-23-13)}),
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-23-14)],
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-23-15)},
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-23-16)});
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-23-17)},{
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-23-18)name:"lookup_user_info",
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-23-19)description:"Use this to look up user information to better assist them with their questions.",
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-23-20)schema:z.object(...)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-23-21)});

```


Important

You MUST include `messages` (or any state key used for the message history) in `Command.update` when returning `Command` from a tool and the list of messages in `messages` MUST contain a `ToolMessage`. This is necessary for the resulting message history to be valid (LLM providers require AI messages with tool calls to be followed by the tool result messages).

If you are using tools that update state via `Command`, we recommend using prebuilt `ToolNode`[](https://langchain-ai.github.io/langgraphjs/reference/classes/langgraph_prebuilt.ToolNode.html) which automatically handles tools returning `Command` objects and propagates them to the graph state. If you're writing a custom node that calls tools, you would need to manually propagate `Command` objects returned by the tools as the update from node.

### Human-in-the-loop[¶](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#human-in-the-loop "Permanent link")

`Command` is an important part of human-in-the-loop workflows: when using `interrupt()` to collect user input, `Command` is then used to supply the input and resume execution via `new Command({ resume: "User input" })`. Check out [this conceptual guide](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop) for more information.

## Persistence[¶](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#persistence "Permanent link")

LangGraph provides built-in persistence for your agent's state using [checkpointers](https://langchain-ai.github.io/langgraphjs/reference/classes/checkpoint.BaseCheckpointSaver.html). Checkpointers save snapshots of the graph state at every superstep, allowing resumption at any time. This enables features like human-in-the-loop interactions, memory management, and fault-tolerance. You can even directly manipulate a graph's state after its execution using the appropriate `get` and `update` methods. For more details, see the [conceptual guide](https://langchain-ai.github.io/langgraphjs/concepts/persistence) for more information.

## Threads[¶](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#threads "Permanent link")

Threads in LangGraph represent individual sessions or conversations between your graph and a user. When using checkpointing, turns in a single conversation (and even steps within a single graph execution) are organized by a unique thread ID.

## Storage[¶](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#storage "Permanent link")

LangGraph provides built-in document storage through the [BaseStore](https://langchain-ai.github.io/langgraphjs/reference/classes/store.BaseStore.html) interface. Unlike checkpointers, which save state by thread ID, stores use custom namespaces for organizing data. This enables cross-thread persistence, allowing agents to maintain long-term memories, learn from past interactions, and accumulate knowledge over time. Common use cases include storing user profiles, building knowledge bases, and managing global preferences across all threads.

## Graph Migrations[¶](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#graph-migrations "Permanent link")

LangGraph can easily handle migrations of graph definitions (nodes, edges, and state) even when using a checkpointer to track state.

  * For threads at the end of the graph (i.e. not interrupted) you can change the entire topology of the graph (i.e. all nodes and edges, remove, add, rename, etc)
  * For threads currently interrupted, we support all topology changes other than renaming / removing nodes (as that thread could now be about to enter a node that no longer exists) -- if this is a blocker please reach out and we can prioritize a solution.
  * For modifying state, we have full backwards and forwards compatibility for adding and removing keys
  * State keys that are renamed lose their saved state in existing threads
  * State keys whose types change in incompatible ways could currently cause issues in threads with state from before the change -- if this is a blocker please reach out and we can prioritize a solution.



## Configuration[¶](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#configuration "Permanent link")

When creating a graph, you can also mark that certain parts of the graph are configurable. This is commonly done to enable easily switching between models or system prompts. This allows you to create a single "cognitive architecture" (the graph) but have multiple different instance of it.

You can then pass this configuration into the graph using the `configurable` config field.

```
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-24-1)constconfig={configurable:{llm:"anthropic"}};
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-24-2)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-24-3)awaitgraph.invoke(inputs,config);

```


You can then access and use this configuration inside a node:

```
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-25-1)constnodeA=(state,config)=>{
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-25-2)constllmType=config?.configurable?.llm;
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-25-3)letllm:BaseChatModel;
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-25-4)if(llmType){
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-25-5)constllm=getLlm(llmType);
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-25-6)}
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-25-7)...
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-25-8)};

```


See [this guide](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/) for a full breakdown on configuration

## Breakpoints[¶](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#breakpoints "Permanent link")

It can often be useful to set breakpoints before or after certain nodes execute. This can be used to wait for human approval before continuing. These can be set when you ["compile" a graph](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#compiling-your-graph), or thrown dynamically using a special error called a `NodeInterrupt`[](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/). You can set breakpoints either _before_ a node executes (using `interruptBefore`) or after a node executes (using `interruptAfter`).

You **MUST** use a checkpointer when using breakpoints. This is because your graph needs to be able to resume execution after interrupting.

In order to resume execution, you can just invoke your graph with `null` as the input and the same `thread_id`.

```
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-26-1)constconfig={configurable:{thread_id:"foo"}};
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-26-2)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-26-3)// Initial run of graph
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-26-4)awaitgraph.invoke(inputs,config);
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-26-5)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-26-6)// Let's assume it hit a breakpoint somewhere, you can then resume by passing in None
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-26-7)awaitgraph.invoke(null,config);

```


See [this guide](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/) for a full walkthrough of how to add breakpoints.

### Dynamic Breakpoints[¶](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#dynamic-breakpoints "Permanent link")

It may be helpful to **dynamically** interrupt the graph from inside a given node based on some condition. In `LangGraph` you can do so by using `NodeInterrupt` -- a special error that can be raised from inside a node.

```
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-27-1)functionmyNode(
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-27-2)state:typeofGraphAnnotation.State
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-27-3)):typeofGraphAnnotation.State{
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-27-4)if(state.input.length>5){
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-27-5)thrownewNodeInterrupt(
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-27-6)`Received input that is longer than 5 characters: ${state.input}`
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-27-7));
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-27-8)}
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-27-9)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-27-10)returnstate;
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-27-11)}

```


## Subgraphs[¶](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#subgraphs "Permanent link")

A subgraph is a [graph](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#graphs) that is used as a [node](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#nodes) in another graph. This is nothing more than the age-old concept of encapsulation, applied to LangGraph. Some reasons for using subgraphs are:

  * building [multi-agent systems](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/)
  * when you want to reuse a set of nodes in multiple graphs, which maybe share some state, you can define them once in a subgraph and then use them in multiple parent graphs
  * when you want different teams to work on different parts of the graph independently, you can define each part as a subgraph, and as long as the subgraph interface (the input and output schemas) is respected, the parent graph can be built without knowing any details of the subgraph



There are two ways to add subgraphs to a parent graph:

  * add a node with the compiled subgraph: this is useful when the parent graph and the subgraph share state keys and you don't need to transform state on the way in or out



```
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-28-1).addNode("subgraph",subgraphBuilder.compile());

```


  * add a node with a function that invokes the subgraph: this is useful when the parent graph and the subgraph have different state schemas and you need to transform state before or after calling the subgraph



```
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-29-1)constsubgraph=subgraphBuilder.compile();
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-29-2)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-29-3)constcallSubgraph=async(state:typeofStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-29-4)returnsubgraph.invoke({subgraph_key:state.parent_key});
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-29-5)};
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-29-6)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-29-7)builder.addNode("subgraph",callSubgraph);

```


Let's take a look at examples for each.

### As a compiled graph[¶](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#as-a-compiled-graph "Permanent link")

The simplest way to create subgraph nodes is by using a [compiled subgraph](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#compiling-your-graph) directly. When doing so, it is **important** that the parent graph and the subgraph [state schemas](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#state) share at least one key which they can use to communicate. If your graph and subgraph do not share any keys, you should use write a function [invoking the subgraph](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#as-a-function) instead.

Note

If you pass extra keys to the subgraph node (i.e., in addition to the shared keys), they will be ignored by the subgraph node. Similarly, if you return extra keys from the subgraph, they will be ignored by the parent graph. 

```
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-30-1)import{StateGraph,Annotation}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-30-2)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-30-3)constStateAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-30-4)foo:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-30-5)});
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-30-6)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-30-7)constSubgraphStateAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-30-8)foo:Annotation<string>,// note that this key is shared with the parent graph state
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-30-9)bar:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-30-10)});
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-30-11)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-30-12)// Define subgraph
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-30-13)constsubgraphNode=async(state:typeofSubgraphStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-30-14)// note that this subgraph node can communicate with
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-30-15)// the parent graph via the shared "foo" key
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-30-16)return{foo:state.foo+"bar"};
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-30-17)};
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-30-18)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-30-19)constsubgraph=newStateGraph(SubgraphStateAnnotation)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-30-20).addNode("subgraph",subgraphNode);
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-30-21)...
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-30-22).compile();
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-30-23)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-30-24)// Define parent graph
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-30-25)constparentGraph=newStateGraph(StateAnnotation)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-30-26).addNode("subgraph",subgraph)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-30-27)...
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-30-28).compile();

```


### As a function[¶](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#as-a-function "Permanent link")

You might want to define a subgraph with a completely different schema. In this case, you can create a node function that invokes the subgraph. This function will need to [transform](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/) the input (parent) state to the subgraph state before invoking the subgraph, and transform the results back to the parent state before returning the state update from the node.

```
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-31-1)import{StateGraph,Annotation}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-31-2)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-31-3)constStateAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-31-4)foo:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-31-5)});
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-31-6)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-31-7)constSubgraphStateAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-31-8)// note that none of these keys are shared with the parent graph state
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-31-9)bar:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-31-10)baz:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-31-11)});
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-31-12)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-31-13)// Define subgraph
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-31-14)constsubgraphNode=async(state:typeofSubgraphStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-31-15)return{bar:state.bar+"baz"};
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-31-16)};
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-31-17)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-31-18)constsubgraph=newStateGraph(SubgraphStateAnnotation)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-31-19).addNode("subgraph",subgraphNode);
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-31-20)...
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-31-21).compile();
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-31-22)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-31-23)// Define parent graph
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-31-24)constsubgraphWrapperNode=async(state:typeofStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-31-25)// transform the state to the subgraph state
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-31-26)constresponse=awaitsubgraph.invoke({
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-31-27)bar:state.foo,
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-31-28)});
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-31-29)// transform response back to the parent state
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-31-30)return{
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-31-31)foo:response.bar,
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-31-32)};
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-31-33)}
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-31-34)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-31-35)constparentGraph=newStateGraph(StateAnnotation)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-31-36).addNode("subgraph",subgraphWrapperNode)
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-31-37)...
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-31-38).compile();

```


## Visualization[¶](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#visualization "Permanent link")

It's often nice to be able to visualize graphs, especially as they get more complex. LangGraph comes with a nice built-in way to render a graph as a Mermaid diagram. You can use the `getGraph()` method like this:

```
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-32-1)constrepresentation=graph.getGraph();
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-32-2)constimage=awaitrepresentation.drawMermaidPng();
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-32-3)constarrayBuffer=awaitimage.arrayBuffer();
[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__codelineno-32-4)constbuffer=newUint8Array(arrayBuffer);

```


You can also check out [LangGraph Studio](https://github.com/langchain-ai/langgraph-studio) for a bespoke IDE that includes powerful visualization and debugging features.

## Streaming[¶](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#streaming "Permanent link")

LangGraph is built with first class support for streaming. There are several different streaming modes that LangGraph supports:

  * `"values"`[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/): This streams the full value of the state after each step of the graph.
  * `"updates`[](https://langchain-ai.github.io/langgraphjs/how-tos/stream-updates/): This streams the updates to the state after each step of the graph. If multiple updates are made in the same step (e.g. multiple nodes are run) then those updates are streamed separately.



In addition, you can use the `streamEvents`[](https://api.js.langchain.com/classes/langchain_core_runnables.Runnable.html#streamEvents) method to stream back events that happen _inside_ nodes. This is useful for [streaming tokens of LLM calls](https://langchain-ai.github.io/langgraphjs/how-tos/streaming-tokens-without-langchain/).

LangGraph is built with first class support for streaming, including streaming updates from graph nodes during execution, streaming tokens from LLM calls and more. See this [conceptual guide](https://langchain-ai.github.io/langgraphjs/concepts/streaming/) for more information.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  Why LangGraph?  ](https://langchain-ai.github.io/langgraphjs/concepts/high_level/) [ Next  Agent architectures  ](https://langchain-ai.github.io/langgraphjs/concepts/agentic_concepts/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
