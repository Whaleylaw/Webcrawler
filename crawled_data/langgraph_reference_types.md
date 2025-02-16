---
url: https://langchain-ai.github.io/langgraph/reference/types/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/reference/types/#types)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Types 

[ ](https://langchain-ai.github.io/langgraph/reference/types/?q= "Share")

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
      * Types  [ Types  ](https://langchain-ai.github.io/langgraph/reference/types/) Table of contents 
        * [ All  ](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.All)
        * [ StreamMode  ](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.StreamMode)
        * [ StreamWriter  ](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.StreamWriter)
        * [ RetryPolicy  ](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.RetryPolicy)
          * [ initial_interval  ](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.RetryPolicy.initial_interval)
          * [ backoff_factor  ](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.RetryPolicy.backoff_factor)
          * [ max_interval  ](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.RetryPolicy.max_interval)
          * [ max_attempts  ](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.RetryPolicy.max_attempts)
          * [ jitter  ](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.RetryPolicy.jitter)
          * [ retry_on  ](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.RetryPolicy.retry_on)
        * [ CachePolicy  ](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.CachePolicy)
        * [ Interrupt  ](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Interrupt)
        * [ PregelTask  ](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.PregelTask)
        * [ PregelExecutableTask  ](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.PregelExecutableTask)
        * [ StateSnapshot  ](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.StateSnapshot)
          * [ values  ](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.StateSnapshot.values)
          * [ next  ](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.StateSnapshot.next)
          * [ config  ](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.StateSnapshot.config)
          * [ metadata  ](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.StateSnapshot.metadata)
          * [ created_at  ](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.StateSnapshot.created_at)
          * [ parent_config  ](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.StateSnapshot.parent_config)
          * [ tasks  ](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.StateSnapshot.tasks)
        * [ Send  ](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Send)
          * [ __init__  ](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Send.__init__)
        * [ Command  ](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Command)
        * [ interrupt  ](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.interrupt)
      * [ Constants  ](https://langchain-ai.github.io/langgraph/reference/constants/)
      * [ Pregel  ](https://langchain-ai.github.io/langgraph/reference/pregel/)
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

  * [ All  ](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.All)
  * [ StreamMode  ](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.StreamMode)
  * [ StreamWriter  ](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.StreamWriter)
  * [ RetryPolicy  ](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.RetryPolicy)
    * [ initial_interval  ](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.RetryPolicy.initial_interval)
    * [ backoff_factor  ](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.RetryPolicy.backoff_factor)
    * [ max_interval  ](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.RetryPolicy.max_interval)
    * [ max_attempts  ](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.RetryPolicy.max_attempts)
    * [ jitter  ](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.RetryPolicy.jitter)
    * [ retry_on  ](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.RetryPolicy.retry_on)
  * [ CachePolicy  ](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.CachePolicy)
  * [ Interrupt  ](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Interrupt)
  * [ PregelTask  ](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.PregelTask)
  * [ PregelExecutableTask  ](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.PregelExecutableTask)
  * [ StateSnapshot  ](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.StateSnapshot)
    * [ values  ](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.StateSnapshot.values)
    * [ next  ](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.StateSnapshot.next)
    * [ config  ](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.StateSnapshot.config)
    * [ metadata  ](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.StateSnapshot.metadata)
    * [ created_at  ](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.StateSnapshot.created_at)
    * [ parent_config  ](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.StateSnapshot.parent_config)
    * [ tasks  ](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.StateSnapshot.tasks)
  * [ Send  ](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Send)
    * [ __init__  ](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Send.__init__)
  * [ Command  ](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Command)
  * [ interrupt  ](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.interrupt)



  1. [ API reference  ](https://langchain-ai.github.io/langgraph/reference/graphs/)
  2. [ Library  ](https://langchain-ai.github.io/langgraph/reference/graphs/)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/reference/types.md "Edit this page")

# Types[¶](https://langchain-ai.github.io/langgraph/reference/types/#types "Permanent link")

##  `All = Literal['*']` `module-attribute` [¶](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.All "Permanent link")

Special value to indicate that graph should interrupt on all nodes.

##  `StreamMode = Literal['values', 'updates', 'debug', 'messages', 'custom']` `module-attribute` [¶](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.StreamMode "Permanent link")

How the stream method should emit outputs.

  * `"values"`: Emit all values in the state after each step. When used with functional API, values are emitted once at the end of the workflow.
  * `"updates"`: Emit only the node or task names and updates returned by the nodes or tasks after each step. If multiple updates are made in the same step (e.g. multiple nodes are run) then those updates are emitted separately.
  * `"custom"`: Emit custom data using from inside nodes or tasks using `StreamWriter`.
  * `"messages"`: Emit LLM messages token-by-token together with metadata for any LLM invocations inside nodes or tasks.
  * `"debug"`: Emit debug events with as much information as possible for each step.



##  `StreamWriter = Callable[[Any], None]` `module-attribute` [¶](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.StreamWriter "Permanent link")

Callable that accepts a single argument and writes it to the output stream. Always injected into nodes if requested as a keyword argument, but it's a no-op when not using stream_mode="custom".

##  `RetryPolicy` [¶](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.RetryPolicy "Permanent link")

Bases: `NamedTuple`

Configuration for retrying nodes.

###  `initial_interval: float = 0.5` `class-attribute` `instance-attribute` [¶](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.RetryPolicy.initial_interval "Permanent link")

Amount of time that must elapse before the first retry occurs. In seconds.

###  `backoff_factor: float = 2.0` `class-attribute` `instance-attribute` [¶](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.RetryPolicy.backoff_factor "Permanent link")

Multiplier by which the interval increases after each retry.

###  `max_interval: float = 128.0` `class-attribute` `instance-attribute` [¶](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.RetryPolicy.max_interval "Permanent link")

Maximum amount of time that may elapse between retries. In seconds.

###  `max_attempts: int = 3` `class-attribute` `instance-attribute` [¶](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.RetryPolicy.max_attempts "Permanent link")

Maximum number of attempts to make before giving up, including the first.

###  `jitter: bool = True` `class-attribute` `instance-attribute` [¶](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.RetryPolicy.jitter "Permanent link")

Whether to add random jitter to the interval between retries.

###  `retry_on: Union[Type[Exception], Sequence[Type[Exception]], Callable[[Exception], bool]] = default_retry_on` `class-attribute` `instance-attribute` [¶](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.RetryPolicy.retry_on "Permanent link")

List of exception classes that should trigger a retry, or a callable that returns True for exceptions that should trigger a retry.

##  `CachePolicy` [¶](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.CachePolicy "Permanent link")

Bases: `NamedTuple`

Configuration for caching nodes.

##  `Interrupt` `dataclass` [¶](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Interrupt "Permanent link")

##  `PregelTask` [¶](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.PregelTask "Permanent link")

Bases: `NamedTuple`

##  `PregelExecutableTask` [¶](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.PregelExecutableTask "Permanent link")

Bases: `NamedTuple`

##  `StateSnapshot` [¶](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.StateSnapshot "Permanent link")

Bases: `NamedTuple`

Snapshot of the state of the graph at the beginning of a step.

###  `values: Union[dict[str, Any], Any]` `instance-attribute` [¶](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.StateSnapshot.values "Permanent link")

Current values of channels

###  `next: tuple[str, ...]` `instance-attribute` [¶](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.StateSnapshot.next "Permanent link")

The name of the node to execute in each task for this step.

###  `config: RunnableConfig` `instance-attribute` [¶](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.StateSnapshot.config "Permanent link")

Config used to fetch this snapshot

###  `metadata: Optional[CheckpointMetadata]` `instance-attribute` [¶](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.StateSnapshot.metadata "Permanent link")

Metadata associated with this snapshot

###  `created_at: Optional[str]` `instance-attribute` [¶](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.StateSnapshot.created_at "Permanent link")

Timestamp of snapshot creation

###  `parent_config: Optional[RunnableConfig]` `instance-attribute` [¶](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.StateSnapshot.parent_config "Permanent link")

Config used to fetch the parent snapshot, if any

###  `tasks: tuple[PregelTask, ...]` `instance-attribute` [¶](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.StateSnapshot.tasks "Permanent link")

Tasks to execute in this step. If already attempted, may contain an error.

##  `Send` [¶](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Send "Permanent link")

A message or packet to send to a specific node in the graph.

The `Send` class is used within a `StateGraph`'s conditional edges to dynamically invoke a node with a custom state at the next step.

Importantly, the sent state can differ from the core graph's state, allowing for flexible and dynamic workflow management.

One such example is a "map-reduce" workflow where your graph invokes the same node multiple times in parallel with different states, before aggregating the results back into the main graph's state.

Attributes:

  * **`node`**(`str`) – 

The name of the target node to send the message to.

  * **`arg`**(`Any`) – 

The state or message to send to the target node.




Examples:

```
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-1)>>> fromtypingimport Annotated
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-2)>>> importoperator
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-3)>>> classOverallState(TypedDict):
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-4)...   subjects: list[str]
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-5)...   jokes: Annotated[list[str], operator.add]
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-6)...
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-7)>>> fromlanggraph.typesimport Send
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-8)>>> fromlanggraph.graphimport END, START
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-9)>>> defcontinue_to_jokes(state: OverallState):
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-10)...   return [Send("generate_joke", {"subject": s}) for s in state['subjects']]
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-11)...
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-12)>>> fromlanggraph.graphimport StateGraph
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-13)>>> builder = StateGraph(OverallState)
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-14)>>> builder.add_node("generate_joke", lambda state: {"jokes": [f"Joke about {state['subject']}"]})
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-15)>>> builder.add_conditional_edges(START, continue_to_jokes)
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-16)>>> builder.add_edge("generate_joke", END)
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-17)>>> graph = builder.compile()
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-18)>>>
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-19)>>> # Invoking with two subjects results in a generated joke for each
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-20)>>> graph.invoke({"subjects": ["cats", "dogs"]})
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-21){'subjects': ['cats', 'dogs'], 'jokes': ['Joke about cats', 'Joke about dogs']}

```


###  `__init__(node: str, arg: Any) -> None` [¶](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Send.__init__ "Permanent link")

Initialize a new instance of the Send class.

Parameters:

  * **`node`**(`str`) – 

The name of the target node to send the message to.

  * **`arg`**(`Any`) – 

The state or message to send to the target node.




##  `Command` `dataclass` [¶](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Command "Permanent link")

Bases: `Generic[N]`, `ToolOutputMixin`

One or more commands to update the graph's state and send messages to nodes.

Parameters:

  * **`graph`**(`Optional[str]` , default: `None` ) – 

graph to send the command to. Supported values are:

    * None: the current graph (default)
    * Command.PARENT: closest parent graph

  * **`update`**(`Optional[Any]` , default: `None` ) – 

update to apply to the graph's state.

  * **`resume`**(`Optional[Union[Any, dict[str, Any]]]` , default: `None` ) – 

value to resume execution with. To be used together with `interrupt()`[](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.interrupt).

  * **`goto`**(`Union[Send, Sequence[Union[Send, str]], str]` , default: `()` ) – 

can be one of the following:

    * name of the node to navigate to next (any node that belongs to the specified `graph`)
    * sequence of node names to navigate to next
    * `Send` object (to execute a node with the input provided)
    * sequence of `Send` objects




##  `interrupt(value: Any) -> Any` [¶](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.interrupt "Permanent link")

Interrupt the graph with a resumable exception from within a node.

The `interrupt` function enables human-in-the-loop workflows by pausing graph execution and surfacing a value to the client. This value can communicate context or request input required to resume execution.

In a given node, the first invocation of this function raises a `GraphInterrupt` exception, halting execution. The provided `value` is included with the exception and sent to the client executing the graph.

A client resuming the graph must use the `Command`[](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Command) primitive to specify a value for the interrupt and continue execution. The graph resumes from the start of the node, **re-executing** all logic.

If a node contains multiple `interrupt` calls, LangGraph matches resume values to interrupts based on their order in the node. This list of resume values is scoped to the specific task executing the node and is not shared across tasks.

To use an `interrupt`, you must enable a checkpointer, as the feature relies on persisting the graph state.

Example

```
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-1)importuuid
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-2)fromtypingimport Optional
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-3)fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-4)
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-5)fromlanggraph.checkpoint.memoryimport MemorySaver
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-6)fromlanggraph.constantsimport START
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-7)fromlanggraph.graphimport StateGraph
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-8)fromlanggraph.typesimport interrupt
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-9)
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-10)
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-11)classState(TypedDict):
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-12)"""The graph state."""
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-13)
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-14)  foo: str
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-15)  human_value: Optional[str]
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-16)"""Human value will be updated using an interrupt."""
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-17)
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-18)
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-19)defnode(state: State):
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-20)  answer = interrupt(
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-21)    # This value will be sent to the client
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-22)    # as part of the interrupt information.
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-23)    "what is your age?"
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-24)  )
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-25)  print(f"> Received an input from the interrupt: {answer}")
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-26)  return {"human_value": answer}
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-27)
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-28)
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-29)builder = StateGraph(State)
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-30)builder.add_node("node", node)
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-31)builder.add_edge(START, "node")
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-32)
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-33)# A checkpointer must be enabled for interrupts to work!
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-34)checkpointer = MemorySaver()
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-35)graph = builder.compile(checkpointer=checkpointer)
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-36)
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-37)config = {
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-38)  "configurable": {
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-39)    "thread_id": uuid.uuid4(),
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-40)  }
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-41)}
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-42)
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-43)for chunk in graph.stream({"foo": "abc"}, config):
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-0-44)  print(chunk)

```


```
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-1-1){'__interrupt__': (Interrupt(value='what is your age?', resumable=True, ns=['node:62e598fa-8653-9d6d-2046-a70203020e37'], when='during'),)}

```


```
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-2-1)command = Command(resume="some input from a human!!!")
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-2-2)
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-2-3)for chunk in graph.stream(Command(resume="some input from a human!!!"), config):
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-2-4)  print(chunk)

```


```
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-3-1)Received an input from the interrupt: some input from a human!!!
[](https://langchain-ai.github.io/langgraph/reference/types/#__codelineno-3-2){'node': {'human_value': 'some input from a human!!!'}}

```


Parameters:

  * **`value`**(`Any`) – 

The value to surface to the client when the graph is interrupted.




Returns:

  * **`Any`**(`Any` ) – 

On subsequent invocations within the same node (same task to be precise), returns the value provided during the first invocation




Raises:

  * `GraphInterrupt` – 

On the first invocation within the node, halts execution and surfaces the provided value to the client.




Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Errors  ](https://langchain-ai.github.io/langgraph/reference/errors/) [ Next  Constants  ](https://langchain-ai.github.io/langgraph/reference/constants/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/reference/types/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
