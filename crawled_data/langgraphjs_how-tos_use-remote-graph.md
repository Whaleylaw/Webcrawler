---
url: https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#how-to-interact-with-the-deployment-using-remotegraph)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to interact with the deployment using RemoteGraph 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/?q= "Share")

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
        * [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/concepts#langgraph)
        * LangGraph Platform  LangGraph Platform 
          * [ LangGraph Platform  ](https://langchain-ai.github.io/langgraphjs/concepts#langgraph-platform)
          * [ High Level  ](https://langchain-ai.github.io/langgraphjs/concepts#high-level)
          * Components  Components 
            * [ Components  ](https://langchain-ai.github.io/langgraphjs/concepts#components)
            * [ LangGraph Server  ](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_server/)
            * [ LangGraph Studio  ](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_studio/)
            * [ LangGraph.js CLI  ](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_cli/)
            * [ LangGraph SDK  ](https://langchain-ai.github.io/langgraphjs/concepts/sdk/)
            * How to interact with the deployment using RemoteGraph  [ How to interact with the deployment using RemoteGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/) Table of contents 
              * [ Initializing the graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#initializing-the-graph)
                * [ Using URL  ](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#using-url)
                * [ Using clients  ](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#using-clients)
              * [ Invoking the graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#invoking-the-graph)
                * [ Asynchronously  ](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#asynchronously)
                * [ Synchronously  ](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#synchronously)
              * [ Thread-level persistence  ](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#thread-level-persistence)
              * [ Using as a subgraph  ](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#using-as-a-subgraph)
          * [ LangGraph Server  ](https://langchain-ai.github.io/langgraphjs/concepts#langgraph-server)
          * [ Deployment Options  ](https://langchain-ai.github.io/langgraphjs/concepts#deployment-options)
      * [ Tutorials  ](https://langchain-ai.github.io/langgraphjs/tutorials/)
    * Resources  Resources 
      * [ Adopters  ](https://langchain-ai.github.io/langgraphjs/adopters/)
      * [ FAQ  ](https://langchain-ai.github.io/langgraphjs/concepts/faq/)
      * [ Troubleshooting  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraphjs/reference/)
  * [ Versions  ](https://langchain-ai.github.io/langgraphjs/versions/)



Table of contents 

  * [ Initializing the graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#initializing-the-graph)
    * [ Using URL  ](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#using-url)
    * [ Using clients  ](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#using-clients)
  * [ Invoking the graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#invoking-the-graph)
    * [ Asynchronously  ](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#asynchronously)
    * [ Synchronously  ](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#synchronously)
  * [ Thread-level persistence  ](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#thread-level-persistence)
  * [ Using as a subgraph  ](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#using-as-a-subgraph)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ Concepts  ](https://langchain-ai.github.io/langgraphjs/concepts/)
  4. [ LangGraph Platform  ](https://langchain-ai.github.io/langgraphjs/concepts#langgraph-platform)
  5. [ Components  ](https://langchain-ai.github.io/langgraphjs/concepts#components)



# How to interact with the deployment using RemoteGraph[¶](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#how-to-interact-with-the-deployment-using-remotegraph "Permanent link")

Prerequisites

  * [LangGraph Platform](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_platform/)
  * [LangGraph Server](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_server/)



`RemoteGraph` is an interface that allows you to interact with your LangGraph Platform deployment as if it were a regular, locally-defined LangGraph graph (e.g. a `CompiledGraph`). This guide shows you how you can initialize a `RemoteGraph` and interact with it.

## Initializing the graph[¶](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#initializing-the-graph "Permanent link")

When initializing a `RemoteGraph`, you must always specify:

  * `name`: the name of the graph you want to interact with. This is the same graph name you use in `langgraph.json` configuration file for your deployment. 
  * `api_key`: a valid LangSmith API key. Can be set as an environment variable (`LANGSMITH_API_KEY`) or passed directly via the `api_key` argument. The API key could also be provided via the `client` / `sync_client` arguments, if `LangGraphClient` / `SyncLangGraphClient` were initialized with `api_key` argument.



Additionally, you have to provide one of the following:

  * `url`: URL of the deployment you want to interact with. If you pass `url` argument, both sync and async clients will be created using the provided URL, headers (if provided) and default configuration values (e.g. timeout, etc).
  * `client`: a `LangGraphClient` instance for interacting with the deployment asynchronously (e.g. using `.astream()`, `.ainvoke()`, `.aget_state()`, `.aupdate_state()`, etc.)
  * `sync_client`: a `SyncLangGraphClient` instance for interacting with the deployment synchronously (e.g. using `.stream()`, `.invoke()`, `.get_state()`, `.update_state()`, etc.)



Note

If you pass both `client` or `sync_client` as well as `url` argument, they will take precedence over the `url` argument. If none of the `client` / `sync_client` / `url` arguments are provided, `RemoteGraph` will raise a `ValueError` at runtime.

### Using URL[¶](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#using-url "Permanent link")

[Python](#__tabbed_1_1)[JavaScript](#__tabbed_1_2)

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-0-1)fromlanggraph.pregel.remoteimport RemoteGraph
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-0-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-0-3)url = <DEPLOYMENT_URL>
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-0-4)graph_name = "agent"
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-0-5)remote_graph = RemoteGraph(graph_name, url=url)

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-1-1)import{RemoteGraph}from"@langchain/langgraph/remote";
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-1-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-1-3)consturl=`<DEPLOYMENT_URL>`;
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-1-4)constgraphName="agent";
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-1-5)constremoteGraph=newRemoteGraph({graphId:graphName,url});

```


### Using clients[¶](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#using-clients "Permanent link")

[Python](#__tabbed_2_1)[JavaScript](#__tabbed_2_2)

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-2-1)fromlanggraph_sdkimport get_client, get_sync_client
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-2-2)fromlanggraph.pregel.remoteimport RemoteGraph
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-2-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-2-4)url = <DEPLOYMENT_URL>
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-2-5)graph_name = "agent"
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-2-6)client = get_client(url=url)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-2-7)sync_client = get_sync_client(url=url)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-2-8)remote_graph = RemoteGraph(graph_name, client=client, sync_client=sync_client)

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-3-1)import{Client}from"@langchain/langgraph-sdk";
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-3-2)import{RemoteGraph}from"@langchain/langgraph/remote";
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-3-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-3-4)constclient=newClient({apiUrl:`<DEPLOYMENT_URL>`});
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-3-5)constgraphName="agent";
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-3-6)constremoteGraph=newRemoteGraph({graphId:graphName,client});

```


## Invoking the graph[¶](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#invoking-the-graph "Permanent link")

Since `RemoteGraph` is a `Runnable` that implements the same methods as `CompiledGraph`, you can interact with it the same way you normally would with a compiled graph, i.e. by calling `.invoke()`, `.stream()`, `.get_state()`, `.update_state()`, etc (as well as their async counterparts).

### Asynchronously[¶](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#asynchronously "Permanent link")

Note

To use the graph asynchronously, you must provide either the `url` or `client` when initializing the `RemoteGraph`.

[Python](#__tabbed_3_1)[JavaScript](#__tabbed_3_2)

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-4-1)# invoke the graph
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-4-2)result = await remote_graph.ainvoke({
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-4-3)  "messages": [{"role": "user", "content": "what's the weather in sf"}]
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-4-4)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-4-5)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-4-6)# stream outputs from the graph
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-4-7)async for chunk in remote_graph.astream({
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-4-8)  "messages": [("user", "what's the weather in la?")]
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-4-9)}):
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-4-10)  print(chunk)

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-5-1)// invoke the graph
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-5-2)constresult=awaitremoteGraph.invoke({
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-5-3)messages:[{role:"user",content:"what's the weather in sf"}]
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-5-4)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-5-5)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-5-6)// stream outputs from the graph
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-5-7)forawait(constchunkofawaitremoteGraph.stream({
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-5-8)messages:[{role:"user",content:"what's the weather in la"}]
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-5-9)})):
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-5-10)console.log(chunk)

```


### Synchronously[¶](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#synchronously "Permanent link")

Note

To use the graph synchronously, you must provide either the `url` or `sync_client` when initializing the `RemoteGraph`.

[Python](#__tabbed_4_1)

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-6-1)# invoke the graph
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-6-2)result = remote_graph.invoke({
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-6-3)  "messages": [{"role": "user", "content": "what's the weather in sf"}]
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-6-4)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-6-5)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-6-6)# stream outputs from the graph
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-6-7)for chunk in remote_graph.stream({
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-6-8)  "messages": [("user", "what's the weather in la?")]
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-6-9)}):
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-6-10)  print(chunk)

```


## Thread-level persistence[¶](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#thread-level-persistence "Permanent link")

By default, the graph runs (i.e. `.invoke()` or `.stream()` invocations) are stateless - the checkpoints and the final state of the graph are not persisted. If you would like to persist the outputs of the graph run (for example, to enable human-in-the-loop features), you can create a thread and provide the thread ID via the `config` argument, same as you would with a regular compiled graph:

[Python](#__tabbed_5_1)[JavaScript](#__tabbed_5_2)

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-7-1)fromlanggraph_sdkimport get_sync_client
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-7-2)url = <DEPLOYMENT_URL>
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-7-3)graph_name = "agent"
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-7-4)sync_client = get_sync_client(url=url)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-7-5)remote_graph = RemoteGraph(graph_name, url=url)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-7-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-7-7)# create a thread (or use an existing thread instead)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-7-8)thread = sync_client.threads.create()
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-7-9)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-7-10)# invoke the graph with the thread config
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-7-11)config = {"configurable": {"thread_id": thread["thread_id"]}}
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-7-12)result = remote_graph.invoke({
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-7-13)  "messages": [{"role": "user", "content": "what's the weather in sf"}], config=config
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-7-14)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-7-15)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-7-16)# verify that the state was persisted to the thread
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-7-17)thread_state = remote_graph.get_state(config)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-7-18)print(thread_state)

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-8-1)import{Client}from"@langchain/langgraph-sdk";
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-8-2)import{RemoteGraph}from"@langchain/langgraph/remote";
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-8-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-8-4)consturl=`<DEPLOYMENT_URL>`;
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-8-5)constgraphName="agent";
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-8-6)constclient=newClient({apiUrl:url});
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-8-7)constremoteGraph=newRemoteGraph({graphId:graphName,url});
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-8-8)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-8-9)// create a thread (or use an existing thread instead)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-8-10)constthread=awaitclient.threads.create();
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-8-11)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-8-12)// invoke the graph with the thread config
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-8-13)constconfig={configurable:{thread_id:thread.thread_id}};
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-8-14)constresult=awaitremoteGraph.invoke({
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-8-15)messages:[{role:"user",content:"what's the weather in sf"}],
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-8-16)config
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-8-17)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-8-18)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-8-19)// verify that the state was persisted to the thread
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-8-20)constthreadState=awaitremoteGraph.getState(config);
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-8-21)console.log(threadState);

```


## Using as a subgraph[¶](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#using-as-a-subgraph "Permanent link")

Note

If you need to use a `checkpointer` with a graph that has a `RemoteGraph` subgraph node, make sure to use UUIDs as thread IDs.

Since the `RemoteGraph` behaves the same way as a regular `CompiledGraph`, it can be also used as a subgraph in another graph. For example:

[Python](#__tabbed_6_1)[JavaScript](#__tabbed_6_2)

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-9-1)fromlanggraph_sdkimport get_sync_client
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-9-2)fromlanggraph.graphimport StateGraph, MessagesState, START
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-9-3)fromtypingimport TypedDict
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-9-4)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-9-5)url = <DEPLOYMENT_URL>
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-9-6)graph_name = "agent"
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-9-7)remote_graph = RemoteGraph(graph_name, url=url)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-9-8)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-9-9)# define parent graph
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-9-10)builder = StateGraph(MessagesState)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-9-11)# add remote graph directly as a node
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-9-12)builder.add_node("child", remote_graph)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-9-13)builder.add_edge(START, "child")
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-9-14)graph = builder.compile()
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-9-15)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-9-16)# invoke the parent graph
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-9-17)result = graph.invoke({
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-9-18)  "messages": [{"role": "user", "content": "what's the weather in sf"}]
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-9-19)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-9-20)print(result)

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-10-1)import{MessagesAnnotation,StateGraph,START}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-10-2)import{RemoteGraph}from"@langchain/langgraph/remote";
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-10-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-10-4)consturl=`<DEPLOYMENT_URL>`;
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-10-5)constgraphName="agent";
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-10-6)constremoteGraph=newRemoteGraph({graphId:graphName,url});
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-10-7)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-10-8)// define parent graph and add remote graph directly as a node
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-10-9)constgraph=newStateGraph(MessagesAnnotation)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-10-10).addNode("child",remoteGraph)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-10-11).addEdge("START","child")
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-10-12).compile()
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-10-13)
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-10-14)// invoke the parent graph
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-10-15)constresult=awaitgraph.invoke({
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-10-16)messages:[{role:"user",content:"what's the weather in sf"}]
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-10-17)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__codelineno-10-18)console.log(result);

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  LangGraph SDK  ](https://langchain-ai.github.io/langgraphjs/concepts/sdk/) [ Next  Application Structure  ](https://langchain-ai.github.io/langgraphjs/concepts/application_structure/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/use-remote-graph/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
