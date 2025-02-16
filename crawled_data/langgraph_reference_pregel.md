---
url: https://langchain-ai.github.io/langgraph/reference/pregel/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/reference/pregel/#langgraph.pregel.Pregel--channels)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Pregel 

[ ](https://langchain-ai.github.io/langgraph/reference/pregel/?q= "Share")

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
      * Pregel  [ Pregel  ](https://langchain-ai.github.io/langgraph/reference/pregel/) Table of contents 
        * [ Channels  ](https://langchain-ai.github.io/langgraph/reference/pregel/#langgraph.pregel.Pregel--channels)
          * [ Basic channels: LastValue and Topic  ](https://langchain-ai.github.io/langgraph/reference/pregel/#langgraph.pregel.Pregel--basic-channels-lastvalue-and-topic)
          * [ Advanced channels: Context and BinaryOperatorAggregate  ](https://langchain-ai.github.io/langgraph/reference/pregel/#langgraph.pregel.Pregel--advanced-channels-context-and-binaryoperatoraggregate)
        * [ Chains  ](https://langchain-ai.github.io/langgraph/reference/pregel/#langgraph.pregel.Pregel--chains)
        * [ Pregel  ](https://langchain-ai.github.io/langgraph/reference/pregel/#langgraph.pregel.Pregel--pregel)
        * [ stream  ](https://langchain-ai.github.io/langgraph/reference/pregel/#langgraph.pregel.Pregel.stream)
        * [ astream  ](https://langchain-ai.github.io/langgraph/reference/pregel/#langgraph.pregel.Pregel.astream)
        * [ invoke  ](https://langchain-ai.github.io/langgraph/reference/pregel/#langgraph.pregel.Pregel.invoke)
        * [ ainvoke  ](https://langchain-ai.github.io/langgraph/reference/pregel/#langgraph.pregel.Pregel.ainvoke)
        * [ update_state  ](https://langchain-ai.github.io/langgraph/reference/pregel/#langgraph.pregel.Pregel.update_state)
        * [ aupdate_state  ](https://langchain-ai.github.io/langgraph/reference/pregel/#langgraph.pregel.Pregel.aupdate_state)
      * [ Config  ](https://langchain-ai.github.io/langgraph/reference/config/)
      * [ Functional API  ](https://langchain-ai.github.io/langgraph/reference/func/)
    * LangGraph Platform  LangGraph Platform 
      * [ Server API  ](https://langchain-ai.github.io/langgraph/cloud/reference/api/api_ref/)
      * [ CLI  ](https://langchain-ai.github.io/langgraph/cloud/reference/cli/)
      * [ SDK (Python)  ](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/)
      * [ SDK (JS/TS)  ](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/)
      * [ RemoteGraph  ](https://langchain-ai.github.io/langgraph/reference/remote_graph/)
      * [ Environment variables  ](https://langchain-ai.github.io/langgraph/cloud/reference/env_var/)



Table of contents 

  * [ Channels  ](https://langchain-ai.github.io/langgraph/reference/pregel/#langgraph.pregel.Pregel--channels)
    * [ Basic channels: LastValue and Topic  ](https://langchain-ai.github.io/langgraph/reference/pregel/#langgraph.pregel.Pregel--basic-channels-lastvalue-and-topic)
    * [ Advanced channels: Context and BinaryOperatorAggregate  ](https://langchain-ai.github.io/langgraph/reference/pregel/#langgraph.pregel.Pregel--advanced-channels-context-and-binaryoperatoraggregate)
  * [ Chains  ](https://langchain-ai.github.io/langgraph/reference/pregel/#langgraph.pregel.Pregel--chains)
  * [ Pregel  ](https://langchain-ai.github.io/langgraph/reference/pregel/#langgraph.pregel.Pregel--pregel)
  * [ stream  ](https://langchain-ai.github.io/langgraph/reference/pregel/#langgraph.pregel.Pregel.stream)
  * [ astream  ](https://langchain-ai.github.io/langgraph/reference/pregel/#langgraph.pregel.Pregel.astream)
  * [ invoke  ](https://langchain-ai.github.io/langgraph/reference/pregel/#langgraph.pregel.Pregel.invoke)
  * [ ainvoke  ](https://langchain-ai.github.io/langgraph/reference/pregel/#langgraph.pregel.Pregel.ainvoke)
  * [ update_state  ](https://langchain-ai.github.io/langgraph/reference/pregel/#langgraph.pregel.Pregel.update_state)
  * [ aupdate_state  ](https://langchain-ai.github.io/langgraph/reference/pregel/#langgraph.pregel.Pregel.aupdate_state)



  1. [ API reference  ](https://langchain-ai.github.io/langgraph/reference/graphs/)
  2. [ Library  ](https://langchain-ai.github.io/langgraph/reference/graphs/)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/reference/pregel.md "Edit this page")

# Pregel

Bases: `PregelProtocol`

Pregel manages the runtime behavior for LangGraph applications.

### Channels[¶](https://langchain-ai.github.io/langgraph/reference/pregel/#langgraph.pregel.Pregel--channels "Permanent link")

Channels are used to communicate between chains. Each channel has a value type, an update type, and an update function – which takes a sequence of updates and modifies the stored value. Channels can be used to send data from one chain to another, or to send data from a chain to itself in a future step. LangGraph provides a number of built-in channels:

#### Basic channels: LastValue and Topic[¶](https://langchain-ai.github.io/langgraph/reference/pregel/#langgraph.pregel.Pregel--basic-channels-lastvalue-and-topic "Permanent link")

  * `LastValue`: The default channel, stores the last value sent to the channel, useful for input and output values, or for sending data from one step to the next
  * `Topic`: A configurable PubSub Topic, useful for sending multiple values between chains, or for accumulating output. Can be configured to deduplicate values, and/or to accumulate values over the course of multiple steps.



#### Advanced channels: Context and BinaryOperatorAggregate[¶](https://langchain-ai.github.io/langgraph/reference/pregel/#langgraph.pregel.Pregel--advanced-channels-context-and-binaryoperatoraggregate "Permanent link")

  * `Context`: exposes the value of a context manager, managing its lifecycle. Useful for accessing external resources that require setup and/or teardown. eg. `client = Context(httpx.Client)`
  * `BinaryOperatorAggregate`: stores a persistent value, updated by applying a binary operator to the current value and each update sent to the channel, useful for computing aggregates over multiple steps. eg. `total = BinaryOperatorAggregate(int, operator.add)`



### Chains[¶](https://langchain-ai.github.io/langgraph/reference/pregel/#langgraph.pregel.Pregel--chains "Permanent link")

Chains are LCEL Runnables which subscribe to one or more channels, and write to one or more channels. Any valid LCEL expression can be used as a chain. Chains can be combined into a Pregel application, which coordinates the execution of the chains across multiple steps.

### Pregel[¶](https://langchain-ai.github.io/langgraph/reference/pregel/#langgraph.pregel.Pregel--pregel "Permanent link")

Pregel combines multiple chains (or actors) into a single application. It coordinates the execution of the chains across multiple steps, following the Pregel/Bulk Synchronous Parallel model. Each step consists of three phases:

  * **Plan** : Determine which chains to execute in this step, ie. the chains that subscribe to channels updated in the previous step (or, in the first step, chains that subscribe to input channels)
  * **Execution** : Execute those chains in parallel, until all complete, or one fails, or a timeout is reached. Any channel updates are invisible to other chains until the next step.
  * **Update** : Update the channels with the values written by the chains in this step.



Repeat until no chains are planned for execution, or a maximum number of steps is reached.

Example

```
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-0-1)fromlanggraphimport Channel, Pregel
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-0-2)
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-0-3)grow_value = (
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-0-4)  Channel.subscribe_to("value")
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-0-5)  | (lambda x: x + x)
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-0-6)  | Channel.write_to(value=lambda x: x if len(x) < 10 else None)
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-0-7))
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-0-8)
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-0-9)app = Pregel(
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-0-10)  chains={"grow_value": grow_value},
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-0-11)  input="value",
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-0-12)  output="value",
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-0-13))
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-0-14)
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-0-15)assert app.invoke("a") == "aaaaaaaa"

```


##  `stream(input: Union[dict[str, Any], Any], config: Optional[RunnableConfig] = None, *, stream_mode: Optional[Union[StreamMode, list[StreamMode]]] = None, output_keys: Optional[Union[str, Sequence[str]]] = None, interrupt_before: Optional[Union[All, Sequence[str]]] = None, interrupt_after: Optional[Union[All, Sequence[str]]] = None, debug: Optional[bool] = None, subgraphs: bool = False) -> Iterator[Union[dict[str, Any], Any]]` [¶](https://langchain-ai.github.io/langgraph/reference/pregel/#langgraph.pregel.Pregel.stream "Permanent link")

Stream graph steps for a single input.

Parameters:

  * **`input`**(`Union[dict[str, Any], Any]`) – 

The input to the graph.

  * **`config`**(`Optional[RunnableConfig]` , default: `None` ) – 

The configuration to use for the run.

  * **`stream_mode`**(`Optional[Union[StreamMode, list[StreamMode]]]` , default: `None` ) – 

The mode to stream output, defaults to self.stream_mode. Options are:

    * `"values"`: Emit all values in the state after each step. When used with functional API, values are emitted once at the end of the workflow.
    * `"updates"`: Emit only the node or task names and updates returned by the nodes or tasks after each step. If multiple updates are made in the same step (e.g. multiple nodes are run) then those updates are emitted separately.
    * `"custom"`: Emit custom data from inside nodes or tasks using `StreamWriter`.
    * `"messages"`: Emit LLM messages token-by-token together with metadata for any LLM invocations inside nodes or tasks.
    * `"debug"`: Emit debug events with as much information as possible for each step.

  * **`output_keys`**(`Optional[Union[str, Sequence[str]]]` , default: `None` ) – 

The keys to stream, defaults to all non-context channels.

  * **`interrupt_before`**(`Optional[Union[All, Sequence[str]]]` , default: `None` ) – 

Nodes to interrupt before, defaults to all nodes in the graph.

  * **`interrupt_after`**(`Optional[Union[All, Sequence[str]]]` , default: `None` ) – 

Nodes to interrupt after, defaults to all nodes in the graph.

  * **`debug`**(`Optional[bool]` , default: `None` ) – 

Whether to print debug information during execution, defaults to False.

  * **`subgraphs`**(`bool` , default: `False` ) – 

Whether to stream subgraphs, defaults to False.




Yields:

  * `Union[dict[str, Any], Any]` – 

The output of each step in the graph. The output shape depends on the stream_mode.




Examples:

Using different stream modes with a graph: 

```
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-0-1)>>> importoperator
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-0-2)>>> fromtyping_extensionsimport Annotated, TypedDict
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-0-3)>>> fromlanggraph.graphimport StateGraph, START
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-0-4)...
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-0-5)>>> classState(TypedDict):
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-0-6)...   alist: Annotated[list, operator.add]
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-0-7)...   another_list: Annotated[list, operator.add]
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-0-8)...
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-0-9)>>> builder = StateGraph(State)
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-0-10)>>> builder.add_node("a", lambda _state: {"another_list": ["hi"]})
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-0-11)>>> builder.add_node("b", lambda _state: {"alist": ["there"]})
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-0-12)>>> builder.add_edge("a", "b")
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-0-13)>>> builder.add_edge(START, "a")
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-0-14)>>> graph = builder.compile()

```


With stream_mode="values": 

```
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-1-1)>>> for event in graph.stream({"alist": ['Ex for stream_mode="values"']}, stream_mode="values"):
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-1-2)...   print(event)
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-1-3){'alist': ['Ex for stream_mode="values"'], 'another_list': []}
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-1-4){'alist': ['Ex for stream_mode="values"'], 'another_list': ['hi']}
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-1-5){'alist': ['Ex for stream_mode="values"', 'there'], 'another_list': ['hi']}

```


With stream_mode="updates": 

```
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-2-1)>>> for event in graph.stream({"alist": ['Ex for stream_mode="updates"']}, stream_mode="updates"):
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-2-2)...   print(event)
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-2-3){'a': {'another_list': ['hi']}}
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-2-4){'b': {'alist': ['there']}}

```


With stream_mode="debug": 

```
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-3-1)>>> for event in graph.stream({"alist": ['Ex for stream_mode="debug"']}, stream_mode="debug"):
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-3-2)...   print(event)
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-3-3){'type': 'task', 'timestamp': '2024-06-23T...+00:00', 'step': 1, 'payload': {'id': '...', 'name': 'a', 'input': {'alist': ['Ex for stream_mode="debug"'], 'another_list': []}, 'triggers': ['start:a']}}
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-3-4){'type': 'task_result', 'timestamp': '2024-06-23T...+00:00', 'step': 1, 'payload': {'id': '...', 'name': 'a', 'result': [('another_list', ['hi'])]}}
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-3-5){'type': 'task', 'timestamp': '2024-06-23T...+00:00', 'step': 2, 'payload': {'id': '...', 'name': 'b', 'input': {'alist': ['Ex for stream_mode="debug"'], 'another_list': ['hi']}, 'triggers': ['a']}}
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-3-6){'type': 'task_result', 'timestamp': '2024-06-23T...+00:00', 'step': 2, 'payload': {'id': '...', 'name': 'b', 'result': [('alist', ['there'])]}}

```


With stream_mode="custom":

```
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-4-1)>>> fromlanggraph.typesimport StreamWriter
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-4-2)...
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-4-3)>>> defnode_a(state: State, writer: StreamWriter):
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-4-4)...   writer({"custom_data": "foo"})
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-4-5)...   return {"alist": ["hi"]}
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-4-6)...
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-4-7)>>> builder = StateGraph(State)
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-4-8)>>> builder.add_node("a", node_a)
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-4-9)>>> builder.add_edge(START, "a")
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-4-10)>>> graph = builder.compile()
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-4-11)...
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-4-12)>>> for event in graph.stream({"alist": ['Ex for stream_mode="custom"']}, stream_mode="custom"):
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-4-13)...   print(event)
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-4-14){'custom_data': 'foo'}

```


With stream_mode="messages":

```
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-5-1)>>> fromtyping_extensionsimport Annotated, TypedDict
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-5-2)>>> fromlanggraph.graphimport StateGraph, START
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-5-3)>>> fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-5-4)...
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-5-5)>>> llm = ChatOpenAI(model="gpt-4o-mini")
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-5-6)...
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-5-7)>>> classState(TypedDict):
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-5-8)...   question: str
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-5-9)...   answer: str
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-5-10)...
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-5-11)>>> defnode_a(state: State):
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-5-12)...   response = llm.invoke(state["question"])
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-5-13)...   return {"answer": response.content}
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-5-14)...
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-5-15)>>> builder = StateGraph(State)
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-5-16)>>> builder.add_node("a", node_a)
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-5-17)>>> builder.add_edge(START, "a")
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-5-18)>>> graph = builder.compile()
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-5-19)
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-5-20)>>> for event in graph.stream({"question": "What is the capital of France?"}, stream_mode="messages"):
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-5-21)...   print(event)
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-5-22)(AIMessageChunk(content='The', additional_kwargs={}, response_metadata={}, id='...'), {'langgraph_step': 1, 'langgraph_node': 'a', 'langgraph_triggers': ['start:a'], 'langgraph_path': ('__pregel_pull', 'a'), 'langgraph_checkpoint_ns': '...', 'checkpoint_ns': '...', 'ls_provider': 'openai', 'ls_model_name': 'gpt-4o-mini', 'ls_model_type': 'chat', 'ls_temperature': 0.7})
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-5-23)(AIMessageChunk(content=' capital', additional_kwargs={}, response_metadata={}, id='...'), {'langgraph_step': 1, 'langgraph_node': 'a', 'langgraph_triggers': ['start:a'], ...})
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-5-24)(AIMessageChunk(content=' of', additional_kwargs={}, response_metadata={}, id='...'), {...})
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-5-25)(AIMessageChunk(content=' France', additional_kwargs={}, response_metadata={}, id='...'), {...})
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-5-26)(AIMessageChunk(content=' is', additional_kwargs={}, response_metadata={}, id='...'), {...})
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-5-27)(AIMessageChunk(content=' Paris', additional_kwargs={}, response_metadata={}, id='...'), {...})

```


##  `astream(input: Union[dict[str, Any], Any], config: Optional[RunnableConfig] = None, *, stream_mode: Optional[Union[StreamMode, list[StreamMode]]] = None, output_keys: Optional[Union[str, Sequence[str]]] = None, interrupt_before: Optional[Union[All, Sequence[str]]] = None, interrupt_after: Optional[Union[All, Sequence[str]]] = None, debug: Optional[bool] = None, subgraphs: bool = False) -> AsyncIterator[Union[dict[str, Any], Any]]` `async` [¶](https://langchain-ai.github.io/langgraph/reference/pregel/#langgraph.pregel.Pregel.astream "Permanent link")

Stream graph steps for a single input.

Parameters:

  * **`input`**(`Union[dict[str, Any], Any]`) – 

The input to the graph.

  * **`config`**(`Optional[RunnableConfig]` , default: `None` ) – 

The configuration to use for the run.

  * **`stream_mode`**(`Optional[Union[StreamMode, list[StreamMode]]]` , default: `None` ) – 

The mode to stream output, defaults to self.stream_mode. Options are:

    * `"values"`: Emit all values in the state after each step. When used with functional API, values are emitted once at the end of the workflow.
    * `"updates"`: Emit only the node or task names and updates returned by the nodes or tasks after each step. If multiple updates are made in the same step (e.g. multiple nodes are run) then those updates are emitted separately.
    * `"custom"`: Emit custom data from inside nodes or tasks using `StreamWriter`.
    * `"messages"`: Emit LLM messages token-by-token together with metadata for any LLM invocations inside nodes or tasks.
    * `"debug"`: Emit debug events with as much information as possible for each step.

  * **`output_keys`**(`Optional[Union[str, Sequence[str]]]` , default: `None` ) – 

The keys to stream, defaults to all non-context channels.

  * **`interrupt_before`**(`Optional[Union[All, Sequence[str]]]` , default: `None` ) – 

Nodes to interrupt before, defaults to all nodes in the graph.

  * **`interrupt_after`**(`Optional[Union[All, Sequence[str]]]` , default: `None` ) – 

Nodes to interrupt after, defaults to all nodes in the graph.

  * **`debug`**(`Optional[bool]` , default: `None` ) – 

Whether to print debug information during execution, defaults to False.

  * **`subgraphs`**(`bool` , default: `False` ) – 

Whether to stream subgraphs, defaults to False.




Yields:

  * `AsyncIterator[Union[dict[str, Any], Any]]` – 

The output of each step in the graph. The output shape depends on the stream_mode.




Examples:

Using different stream modes with a graph: 

```
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-0-1)>>> importoperator
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-0-2)>>> fromtyping_extensionsimport Annotated, TypedDict
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-0-3)>>> fromlanggraph.graphimport StateGraph, START
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-0-4)...
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-0-5)>>> classState(TypedDict):
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-0-6)...   alist: Annotated[list, operator.add]
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-0-7)...   another_list: Annotated[list, operator.add]
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-0-8)...
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-0-9)>>> builder = StateGraph(State)
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-0-10)>>> builder.add_node("a", lambda _state: {"another_list": ["hi"]})
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-0-11)>>> builder.add_node("b", lambda _state: {"alist": ["there"]})
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-0-12)>>> builder.add_edge("a", "b")
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-0-13)>>> builder.add_edge(START, "a")
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-0-14)>>> graph = builder.compile()

```


With stream_mode="values": 

```
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-1-1)>>> async for event in graph.astream({"alist": ['Ex for stream_mode="values"']}, stream_mode="values"):
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-1-2)...   print(event)
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-1-3){'alist': ['Ex for stream_mode="values"'], 'another_list': []}
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-1-4){'alist': ['Ex for stream_mode="values"'], 'another_list': ['hi']}
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-1-5){'alist': ['Ex for stream_mode="values"', 'there'], 'another_list': ['hi']}

```


With stream_mode="updates": 

```
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-2-1)>>> async for event in graph.astream({"alist": ['Ex for stream_mode="updates"']}, stream_mode="updates"):
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-2-2)...   print(event)
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-2-3){'a': {'another_list': ['hi']}}
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-2-4){'b': {'alist': ['there']}}

```


With stream_mode="debug": 

```
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-3-1)>>> async for event in graph.astream({"alist": ['Ex for stream_mode="debug"']}, stream_mode="debug"):
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-3-2)...   print(event)
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-3-3){'type': 'task', 'timestamp': '2024-06-23T...+00:00', 'step': 1, 'payload': {'id': '...', 'name': 'a', 'input': {'alist': ['Ex for stream_mode="debug"'], 'another_list': []}, 'triggers': ['start:a']}}
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-3-4){'type': 'task_result', 'timestamp': '2024-06-23T...+00:00', 'step': 1, 'payload': {'id': '...', 'name': 'a', 'result': [('another_list', ['hi'])]}}
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-3-5){'type': 'task', 'timestamp': '2024-06-23T...+00:00', 'step': 2, 'payload': {'id': '...', 'name': 'b', 'input': {'alist': ['Ex for stream_mode="debug"'], 'another_list': ['hi']}, 'triggers': ['a']}}
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-3-6){'type': 'task_result', 'timestamp': '2024-06-23T...+00:00', 'step': 2, 'payload': {'id': '...', 'name': 'b', 'result': [('alist', ['there'])]}}

```


With stream_mode="custom":

```
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-4-1)>>> fromlanggraph.typesimport StreamWriter
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-4-2)...
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-4-3)>>> async defnode_a(state: State, writer: StreamWriter):
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-4-4)...   writer({"custom_data": "foo"})
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-4-5)...   return {"alist": ["hi"]}
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-4-6)...
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-4-7)>>> builder = StateGraph(State)
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-4-8)>>> builder.add_node("a", node_a)
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-4-9)>>> builder.add_edge(START, "a")
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-4-10)>>> graph = builder.compile()
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-4-11)...
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-4-12)>>> async for event in graph.astream({"alist": ['Ex for stream_mode="custom"']}, stream_mode="custom"):
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-4-13)...   print(event)
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-4-14){'custom_data': 'foo'}

```


With stream_mode="messages":

```
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-5-1)>>> fromtyping_extensionsimport Annotated, TypedDict
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-5-2)>>> fromlanggraph.graphimport StateGraph, START
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-5-3)>>> fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-5-4)...
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-5-5)>>> llm = ChatOpenAI(model="gpt-4o-mini")
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-5-6)...
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-5-7)>>> classState(TypedDict):
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-5-8)...   question: str
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-5-9)...   answer: str
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-5-10)...
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-5-11)>>> async defnode_a(state: State):
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-5-12)...   response = await llm.ainvoke(state["question"])
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-5-13)...   return {"answer": response.content}
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-5-14)...
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-5-15)>>> builder = StateGraph(State)
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-5-16)>>> builder.add_node("a", node_a)
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-5-17)>>> builder.add_edge(START, "a")
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-5-18)>>> graph = builder.compile()
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-5-19)
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-5-20)>>> for event in graph.stream({"question": "What is the capital of France?"}, stream_mode="messages"):
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-5-21)...   print(event)
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-5-22)(AIMessageChunk(content='The', additional_kwargs={}, response_metadata={}, id='...'), {'langgraph_step': 1, 'langgraph_node': 'a', 'langgraph_triggers': ['start:a'], 'langgraph_path': ('__pregel_pull', 'a'), 'langgraph_checkpoint_ns': '...', 'checkpoint_ns': '...', 'ls_provider': 'openai', 'ls_model_name': 'gpt-4o-mini', 'ls_model_type': 'chat', 'ls_temperature': 0.7})
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-5-23)(AIMessageChunk(content=' capital', additional_kwargs={}, response_metadata={}, id='...'), {'langgraph_step': 1, 'langgraph_node': 'a', 'langgraph_triggers': ['start:a'], ...})
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-5-24)(AIMessageChunk(content=' of', additional_kwargs={}, response_metadata={}, id='...'), {...})
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-5-25)(AIMessageChunk(content=' France', additional_kwargs={}, response_metadata={}, id='...'), {...})
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-5-26)(AIMessageChunk(content=' is', additional_kwargs={}, response_metadata={}, id='...'), {...})
[](https://langchain-ai.github.io/langgraph/reference/pregel/#__codelineno-5-27)(AIMessageChunk(content=' Paris', additional_kwargs={}, response_metadata={}, id='...'), {...})

```


##  `invoke(input: Union[dict[str, Any], Any], config: Optional[RunnableConfig] = None, *, stream_mode: StreamMode = 'values', output_keys: Optional[Union[str, Sequence[str]]] = None, interrupt_before: Optional[Union[All, Sequence[str]]] = None, interrupt_after: Optional[Union[All, Sequence[str]]] = None, debug: Optional[bool] = None, **kwargs: Any) -> Union[dict[str, Any], Any]` [¶](https://langchain-ai.github.io/langgraph/reference/pregel/#langgraph.pregel.Pregel.invoke "Permanent link")

Run the graph with a single input and config.

Parameters:

  * **`input`**(`Union[dict[str, Any], Any]`) – 

The input data for the graph. It can be a dictionary or any other type.

  * **`config`**(`Optional[RunnableConfig]` , default: `None` ) – 

Optional. The configuration for the graph run.

  * **`stream_mode`**(`StreamMode` , default: `'values'` ) – 

Optional[str]. The stream mode for the graph run. Default is "values".

  * **`output_keys`**(`Optional[Union[str, Sequence[str]]]` , default: `None` ) – 

Optional. The output keys to retrieve from the graph run.

  * **`interrupt_before`**(`Optional[Union[All, Sequence[str]]]` , default: `None` ) – 

Optional. The nodes to interrupt the graph run before.

  * **`interrupt_after`**(`Optional[Union[All, Sequence[str]]]` , default: `None` ) – 

Optional. The nodes to interrupt the graph run after.

  * **`debug`**(`Optional[bool]` , default: `None` ) – 

Optional. Enable debug mode for the graph run.

  * **`**kwargs`**(`Any` , default: `{}` ) – 

Additional keyword arguments to pass to the graph run.




Returns:

  * `Union[dict[str, Any], Any]` – 

The output of the graph run. If stream_mode is "values", it returns the latest output.

  * `Union[dict[str, Any], Any]` – 

If stream_mode is not "values", it returns a list of output chunks.




##  `ainvoke(input: Union[dict[str, Any], Any], config: Optional[RunnableConfig] = None, *, stream_mode: StreamMode = 'values', output_keys: Optional[Union[str, Sequence[str]]] = None, interrupt_before: Optional[Union[All, Sequence[str]]] = None, interrupt_after: Optional[Union[All, Sequence[str]]] = None, debug: Optional[bool] = None, **kwargs: Any) -> Union[dict[str, Any], Any]` `async` [¶](https://langchain-ai.github.io/langgraph/reference/pregel/#langgraph.pregel.Pregel.ainvoke "Permanent link")

Asynchronously invoke the graph on a single input.

Parameters:

  * **`input`**(`Union[dict[str, Any], Any]`) – 

The input data for the computation. It can be a dictionary or any other type.

  * **`config`**(`Optional[RunnableConfig]` , default: `None` ) – 

Optional. The configuration for the computation.

  * **`stream_mode`**(`StreamMode` , default: `'values'` ) – 

Optional. The stream mode for the computation. Default is "values".

  * **`output_keys`**(`Optional[Union[str, Sequence[str]]]` , default: `None` ) – 

Optional. The output keys to include in the result. Default is None.

  * **`interrupt_before`**(`Optional[Union[All, Sequence[str]]]` , default: `None` ) – 

Optional. The nodes to interrupt before. Default is None.

  * **`interrupt_after`**(`Optional[Union[All, Sequence[str]]]` , default: `None` ) – 

Optional. The nodes to interrupt after. Default is None.

  * **`debug`**(`Optional[bool]` , default: `None` ) – 

Optional. Whether to enable debug mode. Default is None.

  * **`**kwargs`**(`Any` , default: `{}` ) – 

Additional keyword arguments.




Returns:

  * `Union[dict[str, Any], Any]` – 

The result of the computation. If stream_mode is "values", it returns the latest value.

  * `Union[dict[str, Any], Any]` – 

If stream_mode is "chunks", it returns a list of chunks.




##  `update_state(config: RunnableConfig, values: Optional[Union[dict[str, Any], Any]], as_node: Optional[str] = None) -> RunnableConfig` [¶](https://langchain-ai.github.io/langgraph/reference/pregel/#langgraph.pregel.Pregel.update_state "Permanent link")

Update the state of the graph with the given values, as if they came from node `as_node`. If `as_node` is not provided, it will be set to the last node that updated the state, if not ambiguous.

##  `aupdate_state(config: RunnableConfig, values: dict[str, Any] | Any, as_node: Optional[str] = None) -> RunnableConfig` `async` [¶](https://langchain-ai.github.io/langgraph/reference/pregel/#langgraph.pregel.Pregel.aupdate_state "Permanent link")

Update the state of the graph asynchronously with the given values, as if they came from node `as_node`. If `as_node` is not provided, it will be set to the last node that updated the state, if not ambiguous.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Constants  ](https://langchain-ai.github.io/langgraph/reference/constants/) [ Next  Config  ](https://langchain-ai.github.io/langgraph/reference/config/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/reference/pregel/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
