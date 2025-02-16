---
url: https://langchain-ai.github.io/langgraphjs/concepts/persistence/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#persistence)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

Persistence 

[ ](https://langchain-ai.github.io/langgraphjs/concepts/persistence/?q= "Share")

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
          * [ LangGraph Glossary  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/)
          * [ Agent architectures  ](https://langchain-ai.github.io/langgraphjs/concepts/agentic_concepts/)
          * [ Multi-agent Systems  ](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/)
          * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/)
          * Persistence  [ Persistence  ](https://langchain-ai.github.io/langgraphjs/concepts/persistence/) Table of contents 
            * [ Threads  ](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#threads)
            * [ Checkpoints  ](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#checkpoints)
              * [ Get state  ](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#get-state)
              * [ Get state history  ](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#get-state-history)
              * [ Replay  ](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#replay)
              * [ Update state  ](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#update-state)
                * [ config  ](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#config)
                * [ values  ](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#values)
                * [ As Node  ](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#as-node)
            * [ Memory Store  ](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#memory-store)
            * [ Checkpointer libraries  ](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#checkpointer-libraries)
              * [ Checkpointer interface  ](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#checkpointer-interface)
              * [ Serializer  ](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#serializer)
            * [ Capabilities  ](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#capabilities)
              * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#human-in-the-loop)
              * [ Memory  ](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#memory)
              * [ Time Travel  ](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#time-travel)
              * [ Fault-tolerance  ](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#fault-tolerance)
                * [ Pending writes  ](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#pending-writes)
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

  * [ Threads  ](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#threads)
  * [ Checkpoints  ](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#checkpoints)
    * [ Get state  ](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#get-state)
    * [ Get state history  ](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#get-state-history)
    * [ Replay  ](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#replay)
    * [ Update state  ](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#update-state)
      * [ config  ](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#config)
      * [ values  ](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#values)
      * [ As Node  ](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#as-node)
  * [ Memory Store  ](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#memory-store)
  * [ Checkpointer libraries  ](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#checkpointer-libraries)
    * [ Checkpointer interface  ](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#checkpointer-interface)
    * [ Serializer  ](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#serializer)
  * [ Capabilities  ](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#capabilities)
    * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#human-in-the-loop)
    * [ Memory  ](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#memory)
    * [ Time Travel  ](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#time-travel)
    * [ Fault-tolerance  ](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#fault-tolerance)
      * [ Pending writes  ](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#pending-writes)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ Concepts  ](https://langchain-ai.github.io/langgraphjs/concepts/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/concepts#langgraph)



# Persistence[¶](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#persistence "Permanent link")

LangGraph has a built-in persistence layer, implemented through checkpointers. When you compile graph with a checkpointer, the checkpointer saves a `checkpoint` of the graph state at every super-step. Those checkpoints are saved to a `thread`, which can be accessed after graph execution. Because `threads` allow access to graph's state after execution, several powerful capabilities including human-in-the-loop, memory, time travel, and fault-tolerance are all possible. See [this how-to guide](https://langchain-ai.github.io/langgraphjs/how-tos/persistence) for an end-to-end example on how to add and use checkpointers with your graph. Below, we'll discuss each of these concepts in more detail. 

![Checkpoints](https://langchain-ai.github.io/langgraphjs/concepts/img/persistence/checkpoints.jpg)

## Threads[¶](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#threads "Permanent link")

A thread is a unique ID or [thread identifier](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#threads) assigned to each checkpoint saved by a checkpointer. When invoking graph with a checkpointer, you **must** specify a `thread_id` as part of the `configurable` portion of the config:

```
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-0-1){"configurable":{"thread_id":"1"}}

```


## Checkpoints[¶](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#checkpoints "Permanent link")

Checkpoint is a snapshot of the graph state saved at each super-step and is represented by `StateSnapshot` object with the following key properties:

  * `config`: Config associated with this checkpoint. 
  * `metadata`: Metadata associated with this checkpoint.
  * `values`: Values of the state channels at this point in time.
  * `next` A tuple of the node names to execute next in the graph.
  * `tasks`: A tuple of `PregelTask` objects that contain information about next tasks to be executed. If the step was previously attempted, it will include error information. If a graph was interrupted [dynamically](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints) from within a node, tasks will contain additional data associated with interrupts.



Let's see what checkpoints are saved when a simple graph is invoked as follows:

```
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-1-1)import{StateGraph,START,END,MemorySaver,Annotation}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-1-2)
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-1-3)constGraphAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-1-4)foo:Annotation<string>
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-1-5)bar:Annotation<string[]>({
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-1-6)reducer:(a,b)=>[...a,...b],
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-1-7)default:()=>[],
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-1-8)})
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-1-9)});
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-1-10)
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-1-11)functionnodeA(state:typeofGraphAnnotation.State){
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-1-12)return{foo:"a",bar:["a"]};
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-1-13)}
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-1-14)
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-1-15)functionnodeB(state:typeofGraphAnnotation.State){
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-1-16)return{foo:"b",bar:["b"]};
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-1-17)}
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-1-18)
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-1-19)constworkflow=newStateGraph(GraphAnnotation);
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-1-20).addNode("nodeA",nodeA)
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-1-21).addNode("nodeB",nodeB)
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-1-22).addEdge(START,"nodeA")
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-1-23).addEdge("nodeA","nodeB")
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-1-24).addEdge("nodeB",END);
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-1-25)
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-1-26)constcheckpointer=newMemorySaver();
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-1-27)constgraph=workflow.compile({checkpointer});
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-1-28)
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-1-29)constconfig={configurable:{thread_id:"1"}};
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-1-30)awaitgraph.invoke({foo:""},config);

```


After we run the graph, we expect to see exactly 4 checkpoints:

  * empty checkpoint with `START` as the next node to be executed
  * checkpoint with the user input `{foo: '', bar: []}` and `nodeA` as the next node to be executed
  * checkpoint with the outputs of `nodeA` `{foo: 'a', bar: ['a']}` and `nodeB` as the next node to be executed
  * checkpoint with the outputs of `nodeB` `{foo: 'b', bar: ['a', 'b']}` and no next nodes to be executed



Note that we `bar` channel values contain outputs from both nodes as we have a reducer for `bar` channel.

### Get state[¶](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#get-state "Permanent link")

When interacting with the saved graph state, you **must** specify a [thread identifier](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#threads). You can view the _latest_ state of the graph by calling `await graph.getState(config)`. This will return a `StateSnapshot` object that corresponds to the latest checkpoint associated with the thread ID provided in the config or a checkpoint associated with a checkpoint ID for the thread, if provided.

```
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-2-1)// Get the latest state snapshot
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-2-2)constconfig={configurable:{thread_id:"1"}};
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-2-3)conststate=awaitgraph.getState(config);
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-2-4)
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-2-5)// Get a state snapshot for a specific checkpoint_id
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-2-6)constconfigWithCheckpoint={configurable:{thread_id:"1",checkpoint_id:"1ef663ba-28fe-6528-8002-5a559208592c"}};
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-2-7)conststateWithCheckpoint=awaitgraph.getState(configWithCheckpoint);

```


In our example, the output of `getState` will look like this:

```
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-3-1){
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-3-2) values: { foo: 'b', bar: ['a', 'b'] },
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-3-3) next: [],
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-3-4) config: { configurable: { thread_id: '1', checkpoint_ns: '', checkpoint_id: '1ef663ba-28fe-6528-8002-5a559208592c' } },
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-3-5) metadata: { source: 'loop', writes: { nodeB: { foo: 'b', bar: ['b'] } }, step: 2 },
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-3-6) created_at: '2024-08-29T19:19:38.821749+00:00',
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-3-7) parent_config: { configurable: { thread_id: '1', checkpoint_ns: '', checkpoint_id: '1ef663ba-28f9-6ec4-8001-31981c2c39f8' } },
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-3-8) tasks: []
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-3-9)}

```


### Get state history[¶](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#get-state-history "Permanent link")

You can get the full history of the graph execution for a given thread by calling `await graph.getStateHistory(config)`. This will return a list of `StateSnapshot` objects associated with the thread ID provided in the config. Importantly, the checkpoints will be ordered chronologically with the most recent checkpoint / `StateSnapshot` being the first in the list.

```
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-4-1)constconfig={configurable:{thread_id:"1"}};
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-4-2)consthistory=awaitgraph.getStateHistory(config);

```


In our example, the output of `getStateHistory` will look like this:

```
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-5-1)[
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-5-2) {
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-5-3)  values: { foo: 'b', bar: ['a', 'b'] },
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-5-4)  next: [],
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-5-5)  config: { configurable: { thread_id: '1', checkpoint_ns: '', checkpoint_id: '1ef663ba-28fe-6528-8002-5a559208592c' } },
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-5-6)  metadata: { source: 'loop', writes: { nodeB: { foo: 'b', bar: ['b'] } }, step: 2 },
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-5-7)  created_at: '2024-08-29T19:19:38.821749+00:00',
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-5-8)  parent_config: { configurable: { thread_id: '1', checkpoint_ns: '', checkpoint_id: '1ef663ba-28f9-6ec4-8001-31981c2c39f8' } },
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-5-9)  tasks: [],
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-5-10) },
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-5-11) {
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-5-12)  values: { foo: 'a', bar: ['a'] },
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-5-13)  next: ['nodeB'],
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-5-14)  config: { configurable: { thread_id: '1', checkpoint_ns: '', checkpoint_id: '1ef663ba-28f9-6ec4-8001-31981c2c39f8' } },
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-5-15)  metadata: { source: 'loop', writes: { nodeA: { foo: 'a', bar: ['a'] } }, step: 1 },
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-5-16)  created_at: '2024-08-29T19:19:38.819946+00:00',
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-5-17)  parent_config: { configurable: { thread_id: '1', checkpoint_ns: '', checkpoint_id: '1ef663ba-28f4-6b4a-8000-ca575a13d36a' } },
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-5-18)  tasks: [{ id: '6fb7314f-f114-5413-a1f3-d37dfe98ff44', name: 'nodeB', error: null, interrupts: [] }],
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-5-19) },
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-5-20) // ... (other checkpoints)
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-5-21)]

```


![State](https://langchain-ai.github.io/langgraphjs/concepts/img/persistence/get_state.jpg)

### Replay[¶](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#replay "Permanent link")

It's also possible to play-back a prior graph execution. If we `invoking` a graph with a `thread_id` and a `checkpoint_id`, then we will _re-play_ the graph from a checkpoint that corresponds to the `checkpoint_id`.

  * `thread_id` is simply the ID of a thread. This is always required.
  * `checkpoint_id` This identifier refers to a specific checkpoint within a thread. 



You must pass these when invoking the graph as part of the `configurable` portion of the config:

```
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-6-1)// { configurable: { thread_id: "1" } } // valid config
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-6-2)// { configurable: { thread_id: "1", checkpoint_id: "0c62ca34-ac19-445d-bbb0-5b4984975b2a" } } // also valid config
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-6-3)
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-6-4)constconfig={configurable:{thread_id:"1"}};
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-6-5)awaitgraph.invoke(inputs,config);

```


Importantly, LangGraph knows whether a particular checkpoint has been executed previously. If it has, LangGraph simply _re-plays_ that particular step in the graph and does not re-execute the step. See this [how to guide on time-travel to learn more about replaying](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel).

![Replay](https://langchain-ai.github.io/langgraphjs/concepts/img/persistence/re_play.jpg)

### Update state[¶](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#update-state "Permanent link")

In addition to re-playing the graph from specific `checkpoints`, we can also _edit_ the graph state. We do this using `graph.updateState()`. This method three different arguments:

#### `config`[¶](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#config "Permanent link")

The config should contain `thread_id` specifying which thread to update. When only the `thread_id` is passed, we update (or fork) the current state. Optionally, if we include `checkpoint_id` field, then we fork that selected checkpoint.

#### `values`[¶](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#values "Permanent link")

These are the values that will be used to update the state. Note that this update is treated exactly as any update from a node is treated. This means that these values will be passed to the [reducer](https://langchain-ai.github.io/langgraphjs/concepts/low_level#reducers) functions, if they are defined for some of the channels in the graph state. This means that `updateState` does NOT automatically overwrite the channel values for every channel, but only for the channels without reducers. Let's walk through an example.

Let's assume you have defined the state of your graph with the following schema (see full example above):

```
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-7-1)import{Annotation}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-7-2)
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-7-3)constGraphAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-7-4)foo:Annotation<string>
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-7-5)bar:Annotation<string[]>({
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-7-6)reducer:(a,b)=>[...a,...b],
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-7-7)default:()=>[],
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-7-8)})
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-7-9)});

```


Let's now assume the current state of the graph is

```
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-8-1){ foo: "1", bar: ["a"] }

```


If you update the state as below:

```
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-9-1)awaitgraph.updateState(config,{foo:"2",bar:["b"]});

```


Then the new state of the graph will be:

```
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-10-1){ foo: "2", bar: ["a", "b"] }

```


The `foo` key (channel) is completely changed (because there is no reducer specified for that channel, so `updateState` overwrites it). However, there is a reducer specified for the `bar` key, and so it appends `"b"` to the state of `bar`.

#### As Node[¶](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#as-node "Permanent link")

The final argument you can optionally specify when calling `updateState` is the third positional `asNode` argument. If you provided it, the update will be applied as if it came from node `asNode`. If `asNode` is not provided, it will be set to the last node that updated the state, if not ambiguous. The reason this matters is that the next steps to execute depend on the last node to have given an update, so this can be used to control which node executes next. See this [how to guide on time-travel to learn more about forking state](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel).

![Update](https://langchain-ai.github.io/langgraphjs/concepts/img/persistence/checkpoints_full_story.jpg)

## Memory Store[¶](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#memory-store "Permanent link")

![Update](https://langchain-ai.github.io/langgraphjs/concepts/img/persistence/shared_state.png)

A [state schema](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#state) specifies a set of keys that are populated as a graph is executed. As discussed above, state can be written by a checkpointer to a thread at each graph step, enabling state persistence.

But, what if we want to retrain some information _across threads_? Consider the case of a chatbot where we want to retain specific information about the user across _all_ chat conversations (e.g., threads) with that user!

With checkpointers alone, we cannot share information across threads. This motivates the need for the `Store` interface. As an illustration, we can define an `InMemoryStore` to store information about a user across threads. First, let's showcase this in isolation without using LangGraph.

```
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-11-1)import{InMemoryStore}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-11-2)
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-11-3)constinMemoryStore=newInMemoryStore();

```


Memories are namespaced by a `tuple`, which in this specific example will be `[<user_id>, "memories"]`. The namespace can be any length and represent anything, does not have be user specific.

```
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-12-1)constuserId="1";
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-12-2)constnamespaceForMemory=[userId,"memories"];

```


We use the `store.put` method to save memories to our namespace in the store. When we do this, we specify the namespace, as defined above, and a key-value pair for the memory: the key is simply a unique identifier for the memory (`memoryId`) and the value (an object) is the memory itself.

```
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-13-1)import{v4asuuid4}from'uuid';
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-13-2)
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-13-3)constmemoryId=uuid4();
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-13-4)constmemory={food_preference:"I like pizza"};
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-13-5)awaitinMemoryStore.put(namespaceForMemory,memoryId,memory);

```


We can read out memories in our namespace using `store.search`, which will return all memories for a given user as a list. The most recent memory is the last in the list.

```
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-14-1)constmemories=awaitinMemoryStore.search(namespaceForMemory);
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-14-2)console.log(memories.at(-1));
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-14-3)
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-14-4)/*
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-14-5) {
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-14-6)  'value': {'food_preference': 'I like pizza'},
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-14-7)  'key': '07e0caf4-1631-47b7-b15f-65515d4c1843',
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-14-8)  'namespace': ['1', 'memories'],
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-14-9)  'created_at': '2024-10-02T17:22:31.590602+00:00',
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-14-10)  'updated_at': '2024-10-02T17:22:31.590605+00:00'
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-14-11) }
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-14-12)*/

```


The attributes a retrieved memory has are:

  * `value`: The value (itself a dictionary) of this memory
  * `key`: The UUID for this memory in this namespace
  * `namespace`: A list of strings, the namespace of this memory type
  * `created_at`: Timestamp for when this memory was created
  * `updated_at`: Timestamp for when this memory was updated



With this all in place, we use the `inMemoryStore` in LangGraph. The `inMemoryStore` works hand-in-hand with the checkpointer: the checkpointer saves state to threads, as discussed above, and the the `inMemoryStore` allows us to store arbitrary information for access _across_ threads. We compile the graph with both the checkpointer and the `inMemoryStore` as follows. 

```
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-15-1)import{MemorySaver}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-15-2)
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-15-3)// We need this because we want to enable threads (conversations)
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-15-4)constcheckpointer=newMemorySaver();
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-15-5)
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-15-6)// ... Define the graph ...
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-15-7)
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-15-8)// Compile the graph with the checkpointer and store
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-15-9)constgraph=builder.compile({
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-15-10)checkpointer,
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-15-11)store:inMemoryStore
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-15-12)});

```


We invoke the graph with a `thread_id`, as before, and also with a `user_id`, which we'll use to namespace our memories to this particular user as we showed above.

```
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-16-1)// Invoke the graph
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-16-2)constuser_id="1";
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-16-3)constconfig={configurable:{thread_id:"1",user_id}};
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-16-4)
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-16-5)// First let's just say hi to the AI
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-16-6)conststream=awaitgraph.stream(
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-16-7){messages:[{role:"user",content:"hi"}]},
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-16-8){...config,streamMode:"updates"},
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-16-9));
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-16-10)
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-16-11)forawait(constupdateofstream){
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-16-12)console.log(update);
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-16-13)}

```


We can access the `inMemoryStore` and the `user_id` in _any node_ by passing `config: LangGraphRunnableConfig` as a node argument. Then, just as we saw above, simply use the `put` method to save memories to the store.

```
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-17-1)import{
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-17-2)typeLangGraphRunnableConfig,
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-17-3)MessagesAnnotation,
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-17-4)}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-17-5)
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-17-6)constupdateMemory=async(
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-17-7)state:typeofMessagesAnnotation.State,
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-17-8)config:LangGraphRunnableConfig
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-17-9))=>{
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-17-10)// Get the store instance from the config
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-17-11)conststore=config.store;
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-17-12)
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-17-13)// Get the user id from the config
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-17-14)constuserId=config.configurable.user_id;
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-17-15)
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-17-16)// Namespace the memory
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-17-17)constnamespace=[userId,"memories"];
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-17-18)
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-17-19)// ... Analyze conversation and create a new memory
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-17-20)
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-17-21)// Create a new memory ID
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-17-22)constmemoryId=uuid4();
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-17-23)
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-17-24)// We create a new memory
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-17-25)awaitstore.put(namespace,memoryId,{memory});
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-17-26)};

```


As we showed above, we can also access the store in any node and use `search` to get memories. Recall the the memories are returned as a list of objects that can be converted to a dictionary.

```
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-18-1)constmemories=inMemoryStore.search(namespaceForMemory);
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-18-2)console.log(memories.at(-1));
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-18-3)
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-18-4)/*
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-18-5) {
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-18-6)  'value': {'food_preference': 'I like pizza'},
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-18-7)  'key': '07e0caf4-1631-47b7-b15f-65515d4c1843',
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-18-8)  'namespace': ['1', 'memories'],
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-18-9)  'created_at': '2024-10-02T17:22:31.590602+00:00',
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-18-10)  'updated_at': '2024-10-02T17:22:31.590605+00:00'
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-18-11) }
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-18-12)*/

```


We can access the memories and use them in our model call.

```
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-19-1)constcallModel=async(
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-19-2)state:typeofStateAnnotation.State,
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-19-3)config:LangGraphRunnableConfig
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-19-4))=>{
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-19-5)conststore=config.store;
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-19-6)
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-19-7)// Get the user id from the config
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-19-8)constuserId=config.configurable.user_id;
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-19-9)
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-19-10)// Get the memories for the user from the store
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-19-11)constmemories=awaitstore.search([userId,"memories"]);
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-19-12)constinfo=memories.map((memory)=>{
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-19-13)returnJSON.stringify(memory.value);
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-19-14)}).join("\n");
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-19-15)
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-19-16)// ... Use memories in the model call
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-19-17)}

```


If we create a new thread, we can still access the same memories so long as the `user_id` is the same. 

```
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-20-1)// Invoke the graph
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-20-2)constconfig={configurable:{thread_id:"2",user_id:"1"}};
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-20-3)
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-20-4)// Let's say hi again
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-20-5)conststream=awaitgraph.stream(
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-20-6){messages:[{role:"user",content:"hi, tell me about my memories"}]},
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-20-7){...config,streamMode:"updates"},
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-20-8));
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-20-9)
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-20-10)forawait(constupdateofstream){
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-20-11)console.log(update);
[](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__codelineno-20-12)}

```


When we use the LangGraph API, either locally (e.g., in LangGraph Studio) or with LangGraph Cloud, the memory store is available to use by default and does not need to be specified during graph compilation.

## Checkpointer libraries[¶](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#checkpointer-libraries "Permanent link")

Under the hood, checkpointing is powered by checkpointer objects that conform to [BaseCheckpointSaver](https://langchain-ai.github.io/langgraphjs/reference/classes/checkpoint.BaseCheckpointSaver.html) interface. LangGraph provides several checkpointer implementations, all implemented via standalone, installable libraries:

  * `@langchain/langgraph-checkpoint`: The base interface for checkpointer savers ([BaseCheckpointSaver](https://langchain-ai.github.io/langgraphjs/reference/classes/checkpoint.BaseCheckpointSaver.html)) and serialization/deserialization interface ([SerializerProtocol](https://langchain-ai.github.io/langgraphjs/reference/interfaces/checkpoint.SerializerProtocol.html)). Includes in-memory checkpointer implementation ([MemorySaver](https://langchain-ai.github.io/langgraphjs/reference/classes/checkpoint.MemorySaver.html)) for experimentation. LangGraph comes with `@langchain/langgraph-checkpoint` included.
  * `@langchain/langgraph-checkpoint-sqlite`: An implementation of LangGraph checkpointer that uses SQLite database ([SqliteSaver](https://langchain-ai.github.io/langgraphjs/reference/classes/checkpoint_sqlite.SqliteSaver.html)). Ideal for experimentation and local workflows. Needs to be installed separately.
  * `@langchain/langgraph-checkpoint-postgres`: An advanced checkpointer that uses a Postgres database ([PostgresSaver](https://langchain-ai.github.io/langgraphjs/reference/classes/checkpoint_postgres.PostgresSaver.html)), used in LangGraph Cloud. Ideal for using in production. Needs to be installed separately.



### Checkpointer interface[¶](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#checkpointer-interface "Permanent link")

Each checkpointer conforms to [BaseCheckpointSaver](https://langchain-ai.github.io/langgraphjs/reference/classes/checkpoint.BaseCheckpointSaver.html) interface and implements the following methods:

  * `.put` - Store a checkpoint with its configuration and metadata. 
  * `.putWrites` - Store intermediate writes linked to a checkpoint (i.e. [pending writes](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#pending-writes)). 
  * `.getTuple` - Fetch a checkpoint tuple using for a given configuration (`thread_id` and `checkpoint_id`). This is used to populate `StateSnapshot` in `graph.getState()`. 
  * `.list` - List checkpoints that match a given configuration and filter criteria. This is used to populate state history in `graph.getStateHistory()`



### Serializer[¶](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#serializer "Permanent link")

When checkpointers save the graph state, they need to serialize the channel values in the state. This is done using serializer objects. `@langchain/langgraph-checkpoint` defines a [protocol](https://langchain-ai.github.io/langgraphjs/reference/interfaces/checkpoint.SerializerProtocol.html) for implementing serializers and a default implementation that handles a wide variety of types, including LangChain and LangGraph primitives, datetimes, enums and more.

## Capabilities[¶](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#capabilities "Permanent link")

### Human-in-the-loop[¶](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#human-in-the-loop "Permanent link")

First, checkpointers facilitate [human-in-the-loop workflows](https://langchain-ai.github.io/langgraphjs/concepts/agentic_concepts#human-in-the-loop) workflows by allowing humans to inspect, interrupt, and approve graph steps. Checkpointers are needed for these workflows as the human has to be able to view the state of a graph at any point in time, and the graph has to be to resume execution after the human has made any updates to the state. See [these how-to guides](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints) for concrete examples.

### Memory[¶](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#memory "Permanent link")

Second, checkpointers allow for ["memory"](https://langchain-ai.github.io/langgraphjs/concepts/agentic_concepts#memory) between interactions. In the case of repeated human interactions (like conversations) any follow up messages can be sent to that thread, which will retain its memory of previous ones. See [this how-to guide](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history) for an end-to-end example on how to add and manage conversation memory using checkpointers.

### Time Travel[¶](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#time-travel "Permanent link")

Third, checkpointers allow for ["time travel"](https://langchain-ai.github.io/langgraphjs/how-tos/time-travel), allowing users to replay prior graph executions to review and / or debug specific graph steps. In addition, checkpointers make it possible to fork the graph state at arbitrary checkpoints to explore alternative trajectories.

### Fault-tolerance[¶](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#fault-tolerance "Permanent link")

Lastly, checkpointing also provides fault-tolerance and error recovery: if one or more nodes fail at a given superstep, you can restart your graph from the last successful step. Additionally, when a graph node fails mid-execution at a given superstep, LangGraph stores pending checkpoint writes from any other nodes that completed successfully at that superstep, so that whenever we resume graph execution from that superstep we don't re-run the successful nodes.

#### Pending writes[¶](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#pending-writes "Permanent link")

Additionally, when a graph node fails mid-execution at a given superstep, LangGraph stores pending checkpoint writes from any other nodes that completed successfully at that superstep, so that whenever we resume graph execution from that superstep we don't re-run the successful nodes.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  Human-in-the-loop  ](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/) [ Next  Memory  ](https://langchain-ai.github.io/langgraphjs/concepts/memory/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
