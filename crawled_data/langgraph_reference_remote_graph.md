---
url: https://langchain-ai.github.io/langgraph/reference/remote_graph/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/reference/remote_graph/#remotegraph)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

RemoteGraph 

[ ](https://langchain-ai.github.io/langgraph/reference/remote_graph/?q= "Share")

Type to start searching

[ GitHub  ](https://github.com/langchain-ai/langgraph "Go to repository")

  * [ Home ](https://langchain-ai.github.io/langgraph/)
  * [ API reference ](https://langchain-ai.github.io/langgraph/reference/graphs/)



[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

[ GitHub  ](https://github.com/langchain-ai/langgraph "Go to repository")

  * [ Home  ](https://langchain-ai.github.io/langgraph/)
  * API reference  API reference 
    * Library  Library 
      * [ Graphs  ](https://langchain-ai.github.io/langgraph/reference/graphs/)
      * [ Checkpointing  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/)
      * [ Storage  ](https://langchain-ai.github.io/langgraph/reference/store/)
      * [ Prebuilt components  ](https://langchain-ai.github.io/langgraph/reference/prebuilt/)
      * [ Channels  ](https://langchain-ai.github.io/langgraph/reference/channels/)
      * [ Errors  ](https://langchain-ai.github.io/langgraph/reference/errors/)
      * [ Types  ](https://langchain-ai.github.io/langgraph/reference/types/)
      * [ Constants  ](https://langchain-ai.github.io/langgraph/reference/constants/)
      * [ Pregel  ](https://langchain-ai.github.io/langgraph/reference/pregel/)
      * [ Config  ](https://langchain-ai.github.io/langgraph/reference/config/)
      * [ Functional API  ](https://langchain-ai.github.io/langgraph/reference/func/)
    * LangGraph Platform  LangGraph Platform 
      * [ Server API  ](https://langchain-ai.github.io/langgraph/cloud/reference/api/api_ref/)
      * [ CLI  ](https://langchain-ai.github.io/langgraph/cloud/reference/cli/)
      * [ SDK (Python)  ](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/)
      * [ SDK (JS/TS)  ](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/)
      * RemoteGraph  [ RemoteGraph  ](https://langchain-ai.github.io/langgraph/reference/remote_graph/) Table of contents 
        * [ RemoteGraph  ](https://langchain-ai.github.io/langgraph/reference/remote_graph/#langgraph.pregel.remote.RemoteGraph)
          * [ __init__  ](https://langchain-ai.github.io/langgraph/reference/remote_graph/#langgraph.pregel.remote.RemoteGraph.__init__)
          * [ get_graph  ](https://langchain-ai.github.io/langgraph/reference/remote_graph/#langgraph.pregel.remote.RemoteGraph.get_graph)
          * [ aget_graph  ](https://langchain-ai.github.io/langgraph/reference/remote_graph/#langgraph.pregel.remote.RemoteGraph.aget_graph)
          * [ get_state  ](https://langchain-ai.github.io/langgraph/reference/remote_graph/#langgraph.pregel.remote.RemoteGraph.get_state)
          * [ aget_state  ](https://langchain-ai.github.io/langgraph/reference/remote_graph/#langgraph.pregel.remote.RemoteGraph.aget_state)
          * [ get_state_history  ](https://langchain-ai.github.io/langgraph/reference/remote_graph/#langgraph.pregel.remote.RemoteGraph.get_state_history)
          * [ aget_state_history  ](https://langchain-ai.github.io/langgraph/reference/remote_graph/#langgraph.pregel.remote.RemoteGraph.aget_state_history)
          * [ update_state  ](https://langchain-ai.github.io/langgraph/reference/remote_graph/#langgraph.pregel.remote.RemoteGraph.update_state)
          * [ aupdate_state  ](https://langchain-ai.github.io/langgraph/reference/remote_graph/#langgraph.pregel.remote.RemoteGraph.aupdate_state)
          * [ stream  ](https://langchain-ai.github.io/langgraph/reference/remote_graph/#langgraph.pregel.remote.RemoteGraph.stream)
          * [ astream  ](https://langchain-ai.github.io/langgraph/reference/remote_graph/#langgraph.pregel.remote.RemoteGraph.astream)
          * [ invoke  ](https://langchain-ai.github.io/langgraph/reference/remote_graph/#langgraph.pregel.remote.RemoteGraph.invoke)
          * [ ainvoke  ](https://langchain-ai.github.io/langgraph/reference/remote_graph/#langgraph.pregel.remote.RemoteGraph.ainvoke)
      * [ Environment variables  ](https://langchain-ai.github.io/langgraph/cloud/reference/env_var/)



Table of contents 

  * [ RemoteGraph  ](https://langchain-ai.github.io/langgraph/reference/remote_graph/#langgraph.pregel.remote.RemoteGraph)
    * [ __init__  ](https://langchain-ai.github.io/langgraph/reference/remote_graph/#langgraph.pregel.remote.RemoteGraph.__init__)
    * [ get_graph  ](https://langchain-ai.github.io/langgraph/reference/remote_graph/#langgraph.pregel.remote.RemoteGraph.get_graph)
    * [ aget_graph  ](https://langchain-ai.github.io/langgraph/reference/remote_graph/#langgraph.pregel.remote.RemoteGraph.aget_graph)
    * [ get_state  ](https://langchain-ai.github.io/langgraph/reference/remote_graph/#langgraph.pregel.remote.RemoteGraph.get_state)
    * [ aget_state  ](https://langchain-ai.github.io/langgraph/reference/remote_graph/#langgraph.pregel.remote.RemoteGraph.aget_state)
    * [ get_state_history  ](https://langchain-ai.github.io/langgraph/reference/remote_graph/#langgraph.pregel.remote.RemoteGraph.get_state_history)
    * [ aget_state_history  ](https://langchain-ai.github.io/langgraph/reference/remote_graph/#langgraph.pregel.remote.RemoteGraph.aget_state_history)
    * [ update_state  ](https://langchain-ai.github.io/langgraph/reference/remote_graph/#langgraph.pregel.remote.RemoteGraph.update_state)
    * [ aupdate_state  ](https://langchain-ai.github.io/langgraph/reference/remote_graph/#langgraph.pregel.remote.RemoteGraph.aupdate_state)
    * [ stream  ](https://langchain-ai.github.io/langgraph/reference/remote_graph/#langgraph.pregel.remote.RemoteGraph.stream)
    * [ astream  ](https://langchain-ai.github.io/langgraph/reference/remote_graph/#langgraph.pregel.remote.RemoteGraph.astream)
    * [ invoke  ](https://langchain-ai.github.io/langgraph/reference/remote_graph/#langgraph.pregel.remote.RemoteGraph.invoke)
    * [ ainvoke  ](https://langchain-ai.github.io/langgraph/reference/remote_graph/#langgraph.pregel.remote.RemoteGraph.ainvoke)



  1. [ API reference  ](https://langchain-ai.github.io/langgraph/reference/graphs/)
  2. [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/cloud/reference/api/api_ref/)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/reference/remote_graph.md "Edit this page")

# RemoteGraph[¶](https://langchain-ai.github.io/langgraph/reference/remote_graph/#remotegraph "Permanent link")

##  `RemoteGraph` [¶](https://langchain-ai.github.io/langgraph/reference/remote_graph/#langgraph.pregel.remote.RemoteGraph "Permanent link")

Bases: `PregelProtocol`

The `RemoteGraph` class is a client implementation for calling remote APIs that implement the LangGraph Server API specification.

For example, the `RemoteGraph` class can be used to call APIs from deployments on LangGraph Cloud.

`RemoteGraph` behaves the same way as a `Graph` and can be used directly as a node in another `Graph`.

###  `__init__(name: str, /, *, url: Optional[str] = None, api_key: Optional[str] = None, headers: Optional[dict[str, str]] = None, client: Optional[LangGraphClient] = None, sync_client: Optional[SyncLangGraphClient] = None, config: Optional[RunnableConfig] = None)` [¶](https://langchain-ai.github.io/langgraph/reference/remote_graph/#langgraph.pregel.remote.RemoteGraph.__init__ "Permanent link")

Specify `url`, `api_key`, and/or `headers` to create default sync and async clients.

If `client` or `sync_client` are provided, they will be used instead of the default clients. See `LangGraphClient` and `SyncLangGraphClient` for details on the default clients. At least one of `url`, `client`, or `sync_client` must be provided.

Parameters:

  * **`name`**(`str`) – 

The name of the graph.

  * **`url`**(`Optional[str]` , default: `None` ) – 

The URL of the remote API.

  * **`api_key`**(`Optional[str]` , default: `None` ) – 

The API key to use for authentication. If not provided, it will be read from the environment (`LANGGRAPH_API_KEY`, `LANGSMITH_API_KEY`, or `LANGCHAIN_API_KEY`).

  * **`headers`**(`Optional[dict[str, str]]` , default: `None` ) – 

Additional headers to include in the requests.

  * **`client`**(`Optional[LangGraphClient]` , default: `None` ) – 

A `LangGraphClient` instance to use instead of creating a default client.

  * **`sync_client`**(`Optional[SyncLangGraphClient]` , default: `None` ) – 

A `SyncLangGraphClient` instance to use instead of creating a default client.

  * **`config`**(`Optional[RunnableConfig]` , default: `None` ) – 

An optional `RunnableConfig` instance with additional configuration.




###  `get_graph(config: Optional[RunnableConfig] = None, *, xray: Union[int, bool] = False) -> DrawableGraph` [¶](https://langchain-ai.github.io/langgraph/reference/remote_graph/#langgraph.pregel.remote.RemoteGraph.get_graph "Permanent link")

Get graph by graph name.

This method calls `GET /assistants/{assistant_id}/graph`.

Parameters:

  * **`config`**(`Optional[RunnableConfig]` , default: `None` ) – 

This parameter is not used.

  * **`xray`**(`Union[int, bool]` , default: `False` ) – 

Include graph representation of subgraphs. If an integer value is provided, only subgraphs with a depth less than or equal to the value will be included.




Returns:

  * `Graph` – 

The graph information for the assistant in JSON format.




###  `aget_graph(config: Optional[RunnableConfig] = None, *, xray: Union[int, bool] = False) -> DrawableGraph` `async` [¶](https://langchain-ai.github.io/langgraph/reference/remote_graph/#langgraph.pregel.remote.RemoteGraph.aget_graph "Permanent link")

Get graph by graph name.

This method calls `GET /assistants/{assistant_id}/graph`.

Parameters:

  * **`config`**(`Optional[RunnableConfig]` , default: `None` ) – 

This parameter is not used.

  * **`xray`**(`Union[int, bool]` , default: `False` ) – 

Include graph representation of subgraphs. If an integer value is provided, only subgraphs with a depth less than or equal to the value will be included.




Returns:

  * `Graph` – 

The graph information for the assistant in JSON format.




###  `get_state(config: RunnableConfig, *, subgraphs: bool = False) -> StateSnapshot` [¶](https://langchain-ai.github.io/langgraph/reference/remote_graph/#langgraph.pregel.remote.RemoteGraph.get_state "Permanent link")

Get the state of a thread.

This method calls `POST /threads/{thread_id}/state/checkpoint` if a checkpoint is specified in the config or `GET /threads/{thread_id}/state` if no checkpoint is specified.

Parameters:

  * **`config`**(`RunnableConfig`) – 

A `RunnableConfig` that includes `thread_id` in the `configurable` field.

  * **`subgraphs`**(`bool` , default: `False` ) – 

Include subgraphs in the state.




Returns:

  * `StateSnapshot` – 

The latest state of the thread.




###  `aget_state(config: RunnableConfig, *, subgraphs: bool = False) -> StateSnapshot` `async` [¶](https://langchain-ai.github.io/langgraph/reference/remote_graph/#langgraph.pregel.remote.RemoteGraph.aget_state "Permanent link")

Get the state of a thread.

This method calls `POST /threads/{thread_id}/state/checkpoint` if a checkpoint is specified in the config or `GET /threads/{thread_id}/state` if no checkpoint is specified.

Parameters:

  * **`config`**(`RunnableConfig`) – 

A `RunnableConfig` that includes `thread_id` in the `configurable` field.

  * **`subgraphs`**(`bool` , default: `False` ) – 

Include subgraphs in the state.




Returns:

  * `StateSnapshot` – 

The latest state of the thread.




###  `get_state_history(config: RunnableConfig, *, filter: Optional[dict[str, Any]] = None, before: Optional[RunnableConfig] = None, limit: Optional[int] = None) -> Iterator[StateSnapshot]` [¶](https://langchain-ai.github.io/langgraph/reference/remote_graph/#langgraph.pregel.remote.RemoteGraph.get_state_history "Permanent link")

Get the state history of a thread.

This method calls `POST /threads/{thread_id}/history`.

Parameters:

  * **`config`**(`RunnableConfig`) – 

A `RunnableConfig` that includes `thread_id` in the `configurable` field.

  * **`filter`**(`Optional[dict[str, Any]]` , default: `None` ) – 

Metadata to filter on.

  * **`before`**(`Optional[RunnableConfig]` , default: `None` ) – 

A `RunnableConfig` that includes checkpoint metadata.

  * **`limit`**(`Optional[int]` , default: `None` ) – 

Max number of states to return.




Returns:

  * `Iterator[StateSnapshot]` – 

States of the thread.




###  `aget_state_history(config: RunnableConfig, *, filter: Optional[dict[str, Any]] = None, before: Optional[RunnableConfig] = None, limit: Optional[int] = None) -> AsyncIterator[StateSnapshot]` `async` [¶](https://langchain-ai.github.io/langgraph/reference/remote_graph/#langgraph.pregel.remote.RemoteGraph.aget_state_history "Permanent link")

Get the state history of a thread.

This method calls `POST /threads/{thread_id}/history`.

Parameters:

  * **`config`**(`RunnableConfig`) – 

A `RunnableConfig` that includes `thread_id` in the `configurable` field.

  * **`filter`**(`Optional[dict[str, Any]]` , default: `None` ) – 

Metadata to filter on.

  * **`before`**(`Optional[RunnableConfig]` , default: `None` ) – 

A `RunnableConfig` that includes checkpoint metadata.

  * **`limit`**(`Optional[int]` , default: `None` ) – 

Max number of states to return.




Returns:

  * `AsyncIterator[StateSnapshot]` – 

States of the thread.




###  `update_state(config: RunnableConfig, values: Optional[Union[dict[str, Any], Any]], as_node: Optional[str] = None) -> RunnableConfig` [¶](https://langchain-ai.github.io/langgraph/reference/remote_graph/#langgraph.pregel.remote.RemoteGraph.update_state "Permanent link")

Update the state of a thread.

This method calls `POST /threads/{thread_id}/state`.

Parameters:

  * **`config`**(`RunnableConfig`) – 

A `RunnableConfig` that includes `thread_id` in the `configurable` field.

  * **`values`**(`Optional[Union[dict[str, Any], Any]]`) – 

Values to update to the state.

  * **`as_node`**(`Optional[str]` , default: `None` ) – 

Update the state as if this node had just executed.




Returns:

  * `RunnableConfig` – 

`RunnableConfig` for the updated thread.




###  `aupdate_state(config: RunnableConfig, values: Optional[Union[dict[str, Any], Any]], as_node: Optional[str] = None) -> RunnableConfig` `async` [¶](https://langchain-ai.github.io/langgraph/reference/remote_graph/#langgraph.pregel.remote.RemoteGraph.aupdate_state "Permanent link")

Update the state of a thread.

This method calls `POST /threads/{thread_id}/state`.

Parameters:

  * **`config`**(`RunnableConfig`) – 

A `RunnableConfig` that includes `thread_id` in the `configurable` field.

  * **`values`**(`Optional[Union[dict[str, Any], Any]]`) – 

Values to update to the state.

  * **`as_node`**(`Optional[str]` , default: `None` ) – 

Update the state as if this node had just executed.




Returns:

  * `RunnableConfig` – 

`RunnableConfig` for the updated thread.




###  `stream(input: Union[dict[str, Any], Any], config: Optional[RunnableConfig] = None, *, stream_mode: Optional[Union[StreamMode, list[StreamMode]]] = None, interrupt_before: Optional[Union[All, Sequence[str]]] = None, interrupt_after: Optional[Union[All, Sequence[str]]] = None, subgraphs: bool = False, **kwargs: Any) -> Iterator[Union[dict[str, Any], Any]]` [¶](https://langchain-ai.github.io/langgraph/reference/remote_graph/#langgraph.pregel.remote.RemoteGraph.stream "Permanent link")

Create a run and stream the results.

This method calls `POST /threads/{thread_id}/runs/stream` if a `thread_id` is speciffed in the `configurable` field of the config or `POST /runs/stream` otherwise.

Parameters:

  * **`input`**(`Union[dict[str, Any], Any]`) – 

Input to the graph.

  * **`config`**(`Optional[RunnableConfig]` , default: `None` ) – 

A `RunnableConfig` for graph invocation.

  * **`stream_mode`**(`Optional[Union[StreamMode, list[StreamMode]]]` , default: `None` ) – 

Stream mode(s) to use.

  * **`interrupt_before`**(`Optional[Union[All, Sequence[str]]]` , default: `None` ) – 

Interrupt the graph before these nodes.

  * **`interrupt_after`**(`Optional[Union[All, Sequence[str]]]` , default: `None` ) – 

Interrupt the graph after these nodes.

  * **`subgraphs`**(`bool` , default: `False` ) – 

Stream from subgraphs.

  * **`**kwargs`**(`Any` , default: `{}` ) – 

Additional params to pass to client.runs.stream.




Yields:

  * `Union[dict[str, Any], Any]` – 

The output of the graph.




###  `astream(input: Union[dict[str, Any], Any], config: Optional[RunnableConfig] = None, *, stream_mode: Optional[Union[StreamMode, list[StreamMode]]] = None, interrupt_before: Optional[Union[All, Sequence[str]]] = None, interrupt_after: Optional[Union[All, Sequence[str]]] = None, subgraphs: bool = False, **kwargs: Any) -> AsyncIterator[Union[dict[str, Any], Any]]` `async` [¶](https://langchain-ai.github.io/langgraph/reference/remote_graph/#langgraph.pregel.remote.RemoteGraph.astream "Permanent link")

Create a run and stream the results.

This method calls `POST /threads/{thread_id}/runs/stream` if a `thread_id` is speciffed in the `configurable` field of the config or `POST /runs/stream` otherwise.

Parameters:

  * **`input`**(`Union[dict[str, Any], Any]`) – 

Input to the graph.

  * **`config`**(`Optional[RunnableConfig]` , default: `None` ) – 

A `RunnableConfig` for graph invocation.

  * **`stream_mode`**(`Optional[Union[StreamMode, list[StreamMode]]]` , default: `None` ) – 

Stream mode(s) to use.

  * **`interrupt_before`**(`Optional[Union[All, Sequence[str]]]` , default: `None` ) – 

Interrupt the graph before these nodes.

  * **`interrupt_after`**(`Optional[Union[All, Sequence[str]]]` , default: `None` ) – 

Interrupt the graph after these nodes.

  * **`subgraphs`**(`bool` , default: `False` ) – 

Stream from subgraphs.

  * **`**kwargs`**(`Any` , default: `{}` ) – 

Additional params to pass to client.runs.stream.




Yields:

  * `AsyncIterator[Union[dict[str, Any], Any]]` – 

The output of the graph.




###  `invoke(input: Union[dict[str, Any], Any], config: Optional[RunnableConfig] = None, *, interrupt_before: Optional[Union[All, Sequence[str]]] = None, interrupt_after: Optional[Union[All, Sequence[str]]] = None, **kwargs: Any) -> Union[dict[str, Any], Any]` [¶](https://langchain-ai.github.io/langgraph/reference/remote_graph/#langgraph.pregel.remote.RemoteGraph.invoke "Permanent link")

Create a run, wait until it finishes and return the final state.

Parameters:

  * **`input`**(`Union[dict[str, Any], Any]`) – 

Input to the graph.

  * **`config`**(`Optional[RunnableConfig]` , default: `None` ) – 

A `RunnableConfig` for graph invocation.

  * **`interrupt_before`**(`Optional[Union[All, Sequence[str]]]` , default: `None` ) – 

Interrupt the graph before these nodes.

  * **`interrupt_after`**(`Optional[Union[All, Sequence[str]]]` , default: `None` ) – 

Interrupt the graph after these nodes.

  * **`**kwargs`**(`Any` , default: `{}` ) – 

Additional params to pass to RemoteGraph.stream.




Returns:

  * `Union[dict[str, Any], Any]` – 

The output of the graph.




###  `ainvoke(input: Union[dict[str, Any], Any], config: Optional[RunnableConfig] = None, *, interrupt_before: Optional[Union[All, Sequence[str]]] = None, interrupt_after: Optional[Union[All, Sequence[str]]] = None, **kwargs: Any) -> Union[dict[str, Any], Any]` `async` [¶](https://langchain-ai.github.io/langgraph/reference/remote_graph/#langgraph.pregel.remote.RemoteGraph.ainvoke "Permanent link")

Create a run, wait until it finishes and return the final state.

Parameters:

  * **`input`**(`Union[dict[str, Any], Any]`) – 

Input to the graph.

  * **`config`**(`Optional[RunnableConfig]` , default: `None` ) – 

A `RunnableConfig` for graph invocation.

  * **`interrupt_before`**(`Optional[Union[All, Sequence[str]]]` , default: `None` ) – 

Interrupt the graph before these nodes.

  * **`interrupt_after`**(`Optional[Union[All, Sequence[str]]]` , default: `None` ) – 

Interrupt the graph after these nodes.

  * **`**kwargs`**(`Any` , default: `{}` ) – 

Additional params to pass to RemoteGraph.astream.




Returns:

  * `Union[dict[str, Any], Any]` – 

The output of the graph.




Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  SDK (JS/TS)  ](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/) [ Next  Environment variables  ](https://langchain-ai.github.io/langgraph/cloud/reference/env_var/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/reference/remote_graph/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
