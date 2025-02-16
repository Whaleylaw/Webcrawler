---
url: https://ai.pydantic.dev/api/pydantic_graph/state/
title: Untitled
date_crawled: 
---

[ Skip to content ](#pydantic_graphstate)

[ ![logo](../../../img/logo-white.svg) ](../../.. "PydanticAI")

PydanticAI 

pydantic_graph.state 

Type to start searching

[ pydantic/pydantic-ai  ](https://github.com/pydantic/pydantic-ai "Go to repository")

[ ![logo](../../../img/logo-white.svg) ](../../.. "PydanticAI") PydanticAI 

[ pydantic/pydantic-ai  ](https://github.com/pydantic/pydantic-ai "Go to repository")

  * [ Introduction  ](../../..)
  * [ Installation  ](../../../install/)
  * [ Getting Help  ](../../../help/)
  * [ Contributing  ](../../../contributing/)
  * [ Troubleshooting  ](../../../troubleshooting/)
  * Documentation  Documentation 
    * [ Agents  ](../../../agents/)
    * [ Models  ](../../../models/)
    * [ Dependencies  ](../../../dependencies/)
    * [ Function Tools  ](../../../tools/)
    * [ Results  ](../../../results/)
    * [ Messages and chat history  ](../../../message-history/)
    * [ Testing and Evals  ](../../../testing-evals/)
    * [ Debugging and Monitoring  ](../../../logfire/)
    * [ Multi-agent Applications  ](../../../multi-agent-applications/)
    * [ Graphs  ](../../../graph/)
  * [ Examples  ](../../../examples/)

Examples 
    * [ Pydantic Model  ](../../../examples/pydantic-model/)
    * [ Weather agent  ](../../../examples/weather-agent/)
    * [ Bank support  ](../../../examples/bank-support/)
    * [ SQL Generation  ](../../../examples/sql-gen/)
    * [ Flight booking  ](../../../examples/flight-booking/)
    * [ RAG  ](../../../examples/rag/)
    * [ Stream markdown  ](../../../examples/stream-markdown/)
    * [ Stream whales  ](../../../examples/stream-whales/)
    * [ Chat App with FastAPI  ](../../../examples/chat-app/)
    * [ Question Graph  ](../../../examples/question-graph/)
  * API Reference  API Reference 
    * [ pydantic_ai.agent  ](../../agent/)
    * [ pydantic_ai.tools  ](../../tools/)
    * [ pydantic_ai.result  ](../../result/)
    * [ pydantic_ai.messages  ](../../messages/)
    * [ pydantic_ai.exceptions  ](../../exceptions/)
    * [ pydantic_ai.settings  ](../../settings/)
    * [ pydantic_ai.usage  ](../../usage/)
    * [ pydantic_ai.format_as_xml  ](../../format_as_xml/)
    * [ pydantic_ai.models  ](../../models/base/)
    * [ pydantic_ai.models.openai  ](../../models/openai/)
    * [ pydantic_ai.models.anthropic  ](../../models/anthropic/)
    * [ pydantic_ai.models.cohere  ](../../models/cohere/)
    * [ pydantic_ai.models.gemini  ](../../models/gemini/)
    * [ pydantic_ai.models.vertexai  ](../../models/vertexai/)
    * [ pydantic_ai.models.groq  ](../../models/groq/)
    * [ pydantic_ai.models.mistral  ](../../models/mistral/)
    * [ pydantic_ai.models.test  ](../../models/test/)
    * [ pydantic_ai.models.function  ](../../models/function/)
    * [ pydantic_graph  ](../graph/)
    * [ pydantic_graph.nodes  ](../nodes/)
    * pydantic_graph.state  [ pydantic_graph.state  ](./) Table of contents 
      * [ state  ](#pydantic_graph.state)
      * [ StateT  ](#pydantic_graph.state.StateT)
      * [ deep_copy_state  ](#pydantic_graph.state.deep_copy_state)
      * [ NodeStep  ](#pydantic_graph.state.NodeStep)
        * [ state  ](#pydantic_graph.state.NodeStep.state)
        * [ node  ](#pydantic_graph.state.NodeStep.node)
        * [ start_ts  ](#pydantic_graph.state.NodeStep.start_ts)
        * [ duration  ](#pydantic_graph.state.NodeStep.duration)
        * [ kind  ](#pydantic_graph.state.NodeStep.kind)
        * [ snapshot_state  ](#pydantic_graph.state.NodeStep.snapshot_state)
        * [ data_snapshot  ](#pydantic_graph.state.NodeStep.data_snapshot)
      * [ EndStep  ](#pydantic_graph.state.EndStep)
        * [ result  ](#pydantic_graph.state.EndStep.result)
        * [ ts  ](#pydantic_graph.state.EndStep.ts)
        * [ kind  ](#pydantic_graph.state.EndStep.kind)
        * [ data_snapshot  ](#pydantic_graph.state.EndStep.data_snapshot)
      * [ HistoryStep  ](#pydantic_graph.state.HistoryStep)
    * [ pydantic_graph.mermaid  ](../mermaid/)
    * [ pydantic_graph.exceptions  ](../exceptions/)



Table of contents 

  * [ state  ](#pydantic_graph.state)
  * [ StateT  ](#pydantic_graph.state.StateT)
  * [ deep_copy_state  ](#pydantic_graph.state.deep_copy_state)
  * [ NodeStep  ](#pydantic_graph.state.NodeStep)
    * [ state  ](#pydantic_graph.state.NodeStep.state)
    * [ node  ](#pydantic_graph.state.NodeStep.node)
    * [ start_ts  ](#pydantic_graph.state.NodeStep.start_ts)
    * [ duration  ](#pydantic_graph.state.NodeStep.duration)
    * [ kind  ](#pydantic_graph.state.NodeStep.kind)
    * [ snapshot_state  ](#pydantic_graph.state.NodeStep.snapshot_state)
    * [ data_snapshot  ](#pydantic_graph.state.NodeStep.data_snapshot)
  * [ EndStep  ](#pydantic_graph.state.EndStep)
    * [ result  ](#pydantic_graph.state.EndStep.result)
    * [ ts  ](#pydantic_graph.state.EndStep.ts)
    * [ kind  ](#pydantic_graph.state.EndStep.kind)
    * [ data_snapshot  ](#pydantic_graph.state.EndStep.data_snapshot)
  * [ HistoryStep  ](#pydantic_graph.state.HistoryStep)



  1. [ Introduction  ](../../..)
  2. [ API Reference  ](../../agent/)



Version Notice

This documentation is ahead of the last release by [6 commits](https://github.com/pydantic/pydantic-ai/compare/v0.0.24...main). You may see documentation for features not yet supported in the latest release [v0.0.24 2025-02-12](https://github.com/pydantic/pydantic-ai/releases/tag/v0.0.24). 

# `pydantic_graph.state`

###  StateT `module-attribute`

```
StateT = TypeVar('StateT', default=None)

```


Type variable for the state in a graph.

###  deep_copy_state

```
deep_copy_state(state: StateT[](#pydantic_graph.state.StateT "pydantic_graph.state.StateT")) -> StateT[](#pydantic_graph.state.StateT "pydantic_graph.state.StateT")

```


Default method for snapshotting the state in a graph run, uses `copy.deepcopy`[](https://docs.python.org/3/library/copy.html#copy.deepcopy).

Source code in `pydantic_graph/pydantic_graph/state.py`

```
24
25
26
27
28
29
```
| ```
def deep_copy_state(state: StateT) -> StateT:
"""Default method for snapshotting the state in a graph run, uses [`copy.deepcopy`][copy.deepcopy]."""
  if state is None:
    return state
  else:
    return copy.deepcopy(state)

```
  
---|---  
  
###  NodeStep `dataclass`

Bases: `Generic[](https://docs.python.org/3/library/typing.html#typing.Generic "typing.Generic")[StateT[](#pydantic_graph.state.StateT "pydantic_graph.state.StateT"), RunEndT[](../nodes/#pydantic_graph.nodes.RunEndT "pydantic_graph.nodes.RunEndT")]`

History step describing the execution of a node in a graph.

Source code in `pydantic_graph/pydantic_graph/state.py`

```
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
```
| ```
@dataclass
class NodeStep(Generic[StateT, RunEndT]):
"""History step describing the execution of a node in a graph."""
  state: StateT
"""The state of the graph after the node has been run."""
  node: Annotated[BaseNode[StateT, Any, RunEndT], CustomNodeSchema()]
"""The node that was run."""
  start_ts: datetime = field(default_factory=_utils.now_utc)
"""The timestamp when the node started running."""
  duration: float | None = None
"""The duration of the node run in seconds."""
  kind: Literal['node'] = 'node'
"""The kind of history step, can be used as a discriminator when deserializing history."""
  # TODO waiting for https://github.com/pydantic/pydantic/issues/11264, should be an InitVar
  snapshot_state: Annotated[Callable[[StateT], StateT], pydantic.Field(exclude=True, repr=False)] = field(
    default=deep_copy_state, repr=False
  )
"""Function to snapshot the state of the graph."""
  def __post_init__(self):
    # Copy the state to prevent it from being modified by other code
    self.state = self.snapshot_state(self.state)
  def data_snapshot(self) -> BaseNode[StateT, Any, RunEndT]:
"""Returns a deep copy of [`self.node`][pydantic_graph.state.NodeStep.node].
    Useful for summarizing history.
    """
    return copy.deepcopy(self.node)

```
  
---|---  
  
####  state `instance-attribute`

```
state: StateT[](#pydantic_graph.state.StateT "pydantic_graph.state.StateT")

```


The state of the graph after the node has been run.

####  node `instance-attribute`

```
node: Annotated[](https://docs.python.org/3/library/typing.html#typing.Annotated "typing.Annotated")[
  BaseNode[](../nodes/#pydantic_graph.nodes.BaseNode "pydantic_graph.nodes.BaseNode")[StateT[](#pydantic_graph.state.StateT "pydantic_graph.state.StateT"), Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any"), RunEndT[](../nodes/#pydantic_graph.nodes.RunEndT "pydantic_graph.nodes.RunEndT")], CustomNodeSchema()
]

```


The node that was run.

####  start_ts `class-attribute` `instance-attribute`

```
start_ts: datetime[](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") = field[](https://docs.python.org/3/library/dataclasses.html#dataclasses.field "dataclasses.field")(default_factory=now_utc)

```


The timestamp when the node started running.

####  duration `class-attribute` `instance-attribute`

```
duration: float[](https://docs.python.org/3/library/functions.html#float) | None = None

```


The duration of the node run in seconds.

####  kind `class-attribute` `instance-attribute`

```
kind: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['node'] = 'node'

```


The kind of history step, can be used as a discriminator when deserializing history.

####  snapshot_state `class-attribute` `instance-attribute`

```
snapshot_state: Annotated[](https://docs.python.org/3/library/typing.html#typing.Annotated "typing.Annotated")[
  Callable[](https://docs.python.org/3/library/typing.html#typing.Callable "typing.Callable")[[StateT[](#pydantic_graph.state.StateT "pydantic_graph.state.StateT")], StateT[](#pydantic_graph.state.StateT "pydantic_graph.state.StateT")],
  Field[](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field "pydantic.Field")(exclude=True, repr=False),
] = field[](https://docs.python.org/3/library/dataclasses.html#dataclasses.field "dataclasses.field")(default=deep_copy_state[](#pydantic_graph.state.deep_copy_state "pydantic_graph.state.deep_copy_state"), repr=False)

```


Function to snapshot the state of the graph.

####  data_snapshot

```
data_snapshot() -> BaseNode[](../nodes/#pydantic_graph.nodes.BaseNode "pydantic_graph.nodes.BaseNode")[StateT[](#pydantic_graph.state.StateT "pydantic_graph.state.StateT"), Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any"), RunEndT[](../nodes/#pydantic_graph.nodes.RunEndT "pydantic_graph.nodes.RunEndT")]

```


Returns a deep copy of `self.node`[](#pydantic_graph.state.NodeStep.node).

Useful for summarizing history.

Source code in `pydantic_graph/pydantic_graph/state.py`

```
56
57
58
59
60
61
```
| ```
def data_snapshot(self) -> BaseNode[StateT, Any, RunEndT]:
"""Returns a deep copy of [`self.node`][pydantic_graph.state.NodeStep.node].
  Useful for summarizing history.
  """
  return copy.deepcopy(self.node)

```
  
---|---  
  
###  EndStep `dataclass`

Bases: `Generic[](https://docs.python.org/3/library/typing.html#typing.Generic "typing.Generic")[RunEndT[](../nodes/#pydantic_graph.nodes.RunEndT "pydantic_graph.nodes.RunEndT")]`

History step describing the end of a graph run.

Source code in `pydantic_graph/pydantic_graph/state.py`

```
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
```
| ```
@dataclass
class EndStep(Generic[RunEndT]):
"""History step describing the end of a graph run."""
  result: End[RunEndT]
"""The result of the graph run."""
  ts: datetime = field(default_factory=_utils.now_utc)
"""The timestamp when the graph run ended."""
  kind: Literal['end'] = 'end'
"""The kind of history step, can be used as a discriminator when deserializing history."""
  def data_snapshot(self) -> End[RunEndT]:
"""Returns a deep copy of [`self.result`][pydantic_graph.state.EndStep.result].
    Useful for summarizing history.
    """
    return copy.deepcopy(self.result)

```
  
---|---  
  
####  result `instance-attribute`

```
result: End[](../nodes/#pydantic_graph.nodes.End "pydantic_graph.nodes.End")[RunEndT[](../nodes/#pydantic_graph.nodes.RunEndT "pydantic_graph.nodes.RunEndT")]

```


The result of the graph run.

####  ts `class-attribute` `instance-attribute`

```
ts: datetime[](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") = field[](https://docs.python.org/3/library/dataclasses.html#dataclasses.field "dataclasses.field")(default_factory=now_utc)

```


The timestamp when the graph run ended.

####  kind `class-attribute` `instance-attribute`

```
kind: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['end'] = 'end'

```


The kind of history step, can be used as a discriminator when deserializing history.

####  data_snapshot

```
data_snapshot() -> End[](../nodes/#pydantic_graph.nodes.End "pydantic_graph.nodes.End")[RunEndT[](../nodes/#pydantic_graph.nodes.RunEndT "pydantic_graph.nodes.RunEndT")]

```


Returns a deep copy of `self.result`[](#pydantic_graph.state.EndStep.result).

Useful for summarizing history.

Source code in `pydantic_graph/pydantic_graph/state.py`

```
75
76
77
78
79
80
```
| ```
def data_snapshot(self) -> End[RunEndT]:
"""Returns a deep copy of [`self.result`][pydantic_graph.state.EndStep.result].
  Useful for summarizing history.
  """
  return copy.deepcopy(self.result)

```
  
---|---  
  
###  HistoryStep `module-attribute`

```
HistoryStep = Union[](https://docs.python.org/3/library/typing.html#typing.Union "typing.Union")[
  NodeStep[](#pydantic_graph.state.NodeStep "pydantic_graph.state.NodeStep")[StateT[](#pydantic_graph.state.StateT "pydantic_graph.state.StateT"), RunEndT[](../nodes/#pydantic_graph.nodes.RunEndT "pydantic_graph.nodes.RunEndT")], EndStep[](#pydantic_graph.state.EndStep "pydantic_graph.state.EndStep")[RunEndT[](../nodes/#pydantic_graph.nodes.RunEndT "pydantic_graph.nodes.RunEndT")]
]

```


A step in the history of a graph run.

`Graph.run`[](../graph/#pydantic_graph.graph.Graph.run) returns a list of these steps describing the execution of the graph, together with the run return value.

© Pydantic Services Inc. 2024 to present 
