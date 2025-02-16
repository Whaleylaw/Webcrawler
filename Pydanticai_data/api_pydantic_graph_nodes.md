---
url: https://ai.pydantic.dev/api/pydantic_graph/nodes/
title: Untitled
date_crawled: 
---

[ Skip to content ](#pydantic_graphnodes)

[ ![logo](../../../img/logo-white.svg) ](../../.. "PydanticAI")

PydanticAI 

pydantic_graph.nodes 

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
    * pydantic_graph.nodes  [ pydantic_graph.nodes  ](./) Table of contents 
      * [ nodes  ](#pydantic_graph.nodes)
      * [ GraphRunContext  ](#pydantic_graph.nodes.GraphRunContext)
        * [ state  ](#pydantic_graph.nodes.GraphRunContext.state)
        * [ deps  ](#pydantic_graph.nodes.GraphRunContext.deps)
      * [ BaseNode  ](#pydantic_graph.nodes.BaseNode)
        * [ docstring_notes  ](#pydantic_graph.nodes.BaseNode.docstring_notes)
        * [ run  ](#pydantic_graph.nodes.BaseNode.run)
        * [ get_id  ](#pydantic_graph.nodes.BaseNode.get_id)
        * [ get_note  ](#pydantic_graph.nodes.BaseNode.get_note)
        * [ get_node_def  ](#pydantic_graph.nodes.BaseNode.get_node_def)
      * [ End  ](#pydantic_graph.nodes.End)
        * [ data  ](#pydantic_graph.nodes.End.data)
      * [ Edge  ](#pydantic_graph.nodes.Edge)
        * [ label  ](#pydantic_graph.nodes.Edge.label)
      * [ DepsT  ](#pydantic_graph.nodes.DepsT)
      * [ RunEndT  ](#pydantic_graph.nodes.RunEndT)
      * [ NodeRunEndT  ](#pydantic_graph.nodes.NodeRunEndT)
    * [ pydantic_graph.state  ](../state/)
    * [ pydantic_graph.mermaid  ](../mermaid/)
    * [ pydantic_graph.exceptions  ](../exceptions/)



Table of contents 

  * [ nodes  ](#pydantic_graph.nodes)
  * [ GraphRunContext  ](#pydantic_graph.nodes.GraphRunContext)
    * [ state  ](#pydantic_graph.nodes.GraphRunContext.state)
    * [ deps  ](#pydantic_graph.nodes.GraphRunContext.deps)
  * [ BaseNode  ](#pydantic_graph.nodes.BaseNode)
    * [ docstring_notes  ](#pydantic_graph.nodes.BaseNode.docstring_notes)
    * [ run  ](#pydantic_graph.nodes.BaseNode.run)
    * [ get_id  ](#pydantic_graph.nodes.BaseNode.get_id)
    * [ get_note  ](#pydantic_graph.nodes.BaseNode.get_note)
    * [ get_node_def  ](#pydantic_graph.nodes.BaseNode.get_node_def)
  * [ End  ](#pydantic_graph.nodes.End)
    * [ data  ](#pydantic_graph.nodes.End.data)
  * [ Edge  ](#pydantic_graph.nodes.Edge)
    * [ label  ](#pydantic_graph.nodes.Edge.label)
  * [ DepsT  ](#pydantic_graph.nodes.DepsT)
  * [ RunEndT  ](#pydantic_graph.nodes.RunEndT)
  * [ NodeRunEndT  ](#pydantic_graph.nodes.NodeRunEndT)



  1. [ Introduction  ](../../..)
  2. [ API Reference  ](../../agent/)



Version Notice

This documentation is ahead of the last release by [6 commits](https://github.com/pydantic/pydantic-ai/compare/v0.0.24...main). You may see documentation for features not yet supported in the latest release [v0.0.24 2025-02-12](https://github.com/pydantic/pydantic-ai/releases/tag/v0.0.24). 

# `pydantic_graph.nodes`

###  GraphRunContext `dataclass`

Bases: `Generic[](https://docs.python.org/3/library/typing.html#typing.Generic "typing.Generic")[StateT[](../state/#pydantic_graph.state.StateT "pydantic_graph.state.StateT"), DepsT[](#pydantic_graph.nodes.DepsT "pydantic_graph.nodes.DepsT")]`

Context for a graph.

Source code in `pydantic_graph/pydantic_graph/nodes.py`

```
27
28
29
30
31
32
33
34
```
| ```
@dataclass
class GraphRunContext(Generic[StateT, DepsT]):
"""Context for a graph."""
  state: StateT
"""The state of the graph."""
  deps: DepsT
"""Dependencies for the graph."""

```
  
---|---  
  
####  state `instance-attribute`

```
state: StateT[](../state/#pydantic_graph.state.StateT "pydantic_graph.state.StateT")

```


The state of the graph.

####  deps `instance-attribute`

```
deps: DepsT[](#pydantic_graph.nodes.DepsT "pydantic_graph.nodes.DepsT")

```


Dependencies for the graph.

###  BaseNode

Bases: `ABC[](https://docs.python.org/3/library/abc.html#abc.ABC "abc.ABC")`, `Generic[](https://docs.python.org/3/library/typing.html#typing.Generic "typing.Generic")[StateT[](../state/#pydantic_graph.state.StateT "pydantic_graph.state.StateT"), DepsT[](#pydantic_graph.nodes.DepsT "pydantic_graph.nodes.DepsT"), NodeRunEndT[](#pydantic_graph.nodes.NodeRunEndT "pydantic_graph.nodes.NodeRunEndT")]`

Base class for a node.

Source code in `pydantic_graph/pydantic_graph/nodes.py`

```
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
 62
 63
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
 81
 82
 83
 84
 85
 86
 87
 88
 89
 90
 91
 92
 93
 94
 95
 96
 97
 98
 99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
```
| ```
class BaseNode(ABC, Generic[StateT, DepsT, NodeRunEndT]):
"""Base class for a node."""
  docstring_notes: ClassVar[bool] = False
"""Set to `True` to generate mermaid diagram notes from the class's docstring.
  While this can add valuable information to the diagram, it can make diagrams harder to view, hence
  it is disabled by default. You can also customise notes overriding the
  [`get_note`][pydantic_graph.nodes.BaseNode.get_note] method.
  """
  @abstractmethod
  async def run(self, ctx: GraphRunContext[StateT, DepsT]) -> BaseNode[StateT, DepsT, Any] | End[NodeRunEndT]:
"""Run the node.
    This is an abstract method that must be implemented by subclasses.
    !!! note "Return types used at runtime"
      The return type of this method are read by `pydantic_graph` at runtime and used to define which
      nodes can be called next in the graph. This is displayed in [mermaid diagrams](mermaid.md)
      and enforced when running the graph.
    Args:
      ctx: The graph context.
    Returns:
      The next node to run or [`End`][pydantic_graph.nodes.End] to signal the end of the graph.
    """
    ...
  @classmethod
  @cache
  def get_id(cls) -> str:
"""Get the ID of the node."""
    return cls.__name__
  @classmethod
  def get_note(cls) -> str | None:
"""Get a note about the node to render on mermaid charts.
    By default, this returns a note only if [`docstring_notes`][pydantic_graph.nodes.BaseNode.docstring_notes]
    is `True`. You can override this method to customise the node notes.
    """
    if not cls.docstring_notes:
      return None
    docstring = cls.__doc__
    # dataclasses get an automatic docstring which is just their signature, we don't want that
    if docstring and is_dataclass(cls) and docstring.startswith(f'{cls.__name__}('):
      docstring = None
    if docstring:
      # remove indentation from docstring
      import inspect
      docstring = inspect.cleandoc(docstring)
    return docstring
  @classmethod
  def get_node_def(cls, local_ns: dict[str, Any] | None) -> NodeDef[StateT, DepsT, NodeRunEndT]:
"""Get the node definition."""
    type_hints = get_type_hints(cls.run, localns=local_ns, include_extras=True)
    try:
      return_hint = type_hints['return']
    except KeyError as e:
      raise exceptions.GraphSetupError(f'Node {cls} is missing a return type hint on its `run` method') from e
    next_node_edges: dict[str, Edge] = {}
    end_edge: Edge | None = None
    returns_base_node: bool = False
    for return_type in _utils.get_union_args(return_hint):
      return_type, annotations = _utils.unpack_annotated(return_type)
      edge = next((a for a in annotations if isinstance(a, Edge)), Edge(None))
      return_type_origin = get_origin(return_type) or return_type
      if return_type_origin is End:
        end_edge = edge
      elif return_type_origin is BaseNode:
        # TODO: Should we disallow this?
        returns_base_node = True
      elif issubclass(return_type_origin, BaseNode):
        next_node_edges[return_type.get_id()] = edge
      else:
        raise exceptions.GraphSetupError(f'Invalid return type: {return_type}')
    return NodeDef(
      cls,
      cls.get_id(),
      cls.get_note(),
      next_node_edges,
      end_edge,
      returns_base_node,
    )

```
  
---|---  
  
####  docstring_notes `class-attribute`

```
docstring_notes: bool[](https://docs.python.org/3/library/functions.html#bool) = False

```


Set to `True` to generate mermaid diagram notes from the class's docstring.

While this can add valuable information to the diagram, it can make diagrams harder to view, hence it is disabled by default. You can also customise notes overriding the `get_note`[](#pydantic_graph.nodes.BaseNode.get_note) method.

####  run `abstractmethod` `async`

```
run(
  ctx: GraphRunContext[](#pydantic_graph.nodes.GraphRunContext "pydantic_graph.nodes.GraphRunContext")[StateT[](../state/#pydantic_graph.state.StateT "pydantic_graph.state.StateT"), DepsT[](#pydantic_graph.nodes.DepsT "pydantic_graph.nodes.DepsT")]
) -> BaseNode[](#pydantic_graph.nodes.BaseNode "pydantic_graph.nodes.BaseNode")[StateT[](../state/#pydantic_graph.state.StateT "pydantic_graph.state.StateT"), DepsT[](#pydantic_graph.nodes.DepsT "pydantic_graph.nodes.DepsT"), Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")] | End[](#pydantic_graph.nodes.End "pydantic_graph.nodes.End")[NodeRunEndT[](#pydantic_graph.nodes.NodeRunEndT "pydantic_graph.nodes.NodeRunEndT")]

```


Run the node.

This is an abstract method that must be implemented by subclasses.

Return types used at runtime

The return type of this method are read by `pydantic_graph` at runtime and used to define which nodes can be called next in the graph. This is displayed in [mermaid diagrams](../mermaid/) and enforced when running the graph.

Parameters:

Name | Type | Description | Default  
---|---|---|---  
`ctx` |  `GraphRunContext[](#pydantic_graph.nodes.GraphRunContext "pydantic_graph.nodes.GraphRunContext")[StateT[](../state/#pydantic_graph.state.StateT "pydantic_graph.state.StateT"), DepsT[](#pydantic_graph.nodes.DepsT "pydantic_graph.nodes.DepsT")]` |  The graph context. |  _required_  
  
Returns:

Type | Description  
---|---  
`BaseNode[](#pydantic_graph.nodes.BaseNode "pydantic_graph.nodes.BaseNode")[StateT[](../state/#pydantic_graph.state.StateT "pydantic_graph.state.StateT"), DepsT[](#pydantic_graph.nodes.DepsT "pydantic_graph.nodes.DepsT"), Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")] | End[](#pydantic_graph.nodes.End "pydantic_graph.nodes.End")[NodeRunEndT[](#pydantic_graph.nodes.NodeRunEndT "pydantic_graph.nodes.NodeRunEndT")]` |  The next node to run or `End`[](#pydantic_graph.nodes.End) to signal the end of the graph.  
  
Source code in `pydantic_graph/pydantic_graph/nodes.py`

```
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
62
63
64
65
```
| ```
@abstractmethod
async def run(self, ctx: GraphRunContext[StateT, DepsT]) -> BaseNode[StateT, DepsT, Any] | End[NodeRunEndT]:
"""Run the node.
  This is an abstract method that must be implemented by subclasses.
  !!! note "Return types used at runtime"
    The return type of this method are read by `pydantic_graph` at runtime and used to define which
    nodes can be called next in the graph. This is displayed in [mermaid diagrams](mermaid.md)
    and enforced when running the graph.
  Args:
    ctx: The graph context.
  Returns:
    The next node to run or [`End`][pydantic_graph.nodes.End] to signal the end of the graph.
  """
  ...

```
  
---|---  
  
####  get_id `cached` `classmethod`

```
get_id() -> str[](https://docs.python.org/3/library/stdtypes.html#str)

```


Get the ID of the node.

Source code in `pydantic_graph/pydantic_graph/nodes.py`

```
67
68
69
70
71
```
| ```
@classmethod
@cache
def get_id(cls) -> str:
"""Get the ID of the node."""
  return cls.__name__

```
  
---|---  
  
####  get_note `classmethod`

```
get_note() -> str[](https://docs.python.org/3/library/stdtypes.html#str) | None

```


Get a note about the node to render on mermaid charts.

By default, this returns a note only if `docstring_notes`[](#pydantic_graph.nodes.BaseNode.docstring_notes) is `True`. You can override this method to customise the node notes.

Source code in `pydantic_graph/pydantic_graph/nodes.py`

```
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
```
| ```
@classmethod
def get_note(cls) -> str | None:
"""Get a note about the node to render on mermaid charts.
  By default, this returns a note only if [`docstring_notes`][pydantic_graph.nodes.BaseNode.docstring_notes]
  is `True`. You can override this method to customise the node notes.
  """
  if not cls.docstring_notes:
    return None
  docstring = cls.__doc__
  # dataclasses get an automatic docstring which is just their signature, we don't want that
  if docstring and is_dataclass(cls) and docstring.startswith(f'{cls.__name__}('):
    docstring = None
  if docstring:
    # remove indentation from docstring
    import inspect
    docstring = inspect.cleandoc(docstring)
  return docstring

```
  
---|---  
  
####  get_node_def `classmethod`

```
get_node_def(
  local_ns: dict[](https://docs.python.org/3/library/stdtypes.html#dict)[str[](https://docs.python.org/3/library/stdtypes.html#str), Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")] | None
) -> NodeDef[StateT[](../state/#pydantic_graph.state.StateT "pydantic_graph.state.StateT"), DepsT[](#pydantic_graph.nodes.DepsT "pydantic_graph.nodes.DepsT"), NodeRunEndT[](#pydantic_graph.nodes.NodeRunEndT "pydantic_graph.nodes.NodeRunEndT")]

```


Get the node definition.

Source code in `pydantic_graph/pydantic_graph/nodes.py`

```
 93
 94
 95
 96
 97
 98
 99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
```
| ```
@classmethod
def get_node_def(cls, local_ns: dict[str, Any] | None) -> NodeDef[StateT, DepsT, NodeRunEndT]:
"""Get the node definition."""
  type_hints = get_type_hints(cls.run, localns=local_ns, include_extras=True)
  try:
    return_hint = type_hints['return']
  except KeyError as e:
    raise exceptions.GraphSetupError(f'Node {cls} is missing a return type hint on its `run` method') from e
  next_node_edges: dict[str, Edge] = {}
  end_edge: Edge | None = None
  returns_base_node: bool = False
  for return_type in _utils.get_union_args(return_hint):
    return_type, annotations = _utils.unpack_annotated(return_type)
    edge = next((a for a in annotations if isinstance(a, Edge)), Edge(None))
    return_type_origin = get_origin(return_type) or return_type
    if return_type_origin is End:
      end_edge = edge
    elif return_type_origin is BaseNode:
      # TODO: Should we disallow this?
      returns_base_node = True
    elif issubclass(return_type_origin, BaseNode):
      next_node_edges[return_type.get_id()] = edge
    else:
      raise exceptions.GraphSetupError(f'Invalid return type: {return_type}')
  return NodeDef(
    cls,
    cls.get_id(),
    cls.get_note(),
    next_node_edges,
    end_edge,
    returns_base_node,
  )

```
  
---|---  
  
###  End `dataclass`

Bases: `Generic[](https://docs.python.org/3/library/typing.html#typing.Generic "typing.Generic")[RunEndT[](#pydantic_graph.nodes.RunEndT "pydantic_graph.nodes.RunEndT")]`

Type to return from a node to signal the end of the graph.

Source code in `pydantic_graph/pydantic_graph/nodes.py`

```
129
130
131
132
133
134
```
| ```
@dataclass
class End(Generic[RunEndT]):
"""Type to return from a node to signal the end of the graph."""
  data: RunEndT
"""Data to return from the graph."""

```
  
---|---  
  
####  data `instance-attribute`

```
data: RunEndT[](#pydantic_graph.nodes.RunEndT "pydantic_graph.nodes.RunEndT")

```


Data to return from the graph.

###  Edge `dataclass`

Annotation to apply a label to an edge in a graph.

Source code in `pydantic_graph/pydantic_graph/nodes.py`

```
137
138
139
140
141
142
```
| ```
@dataclass
class Edge:
"""Annotation to apply a label to an edge in a graph."""
  label: str | None
"""Label for the edge."""

```
  
---|---  
  
####  label `instance-attribute`

```
label: str[](https://docs.python.org/3/library/stdtypes.html#str) | None

```


Label for the edge.

###  DepsT `module-attribute`

```
DepsT = TypeVar('DepsT', default=None, contravariant=True)

```


Type variable for the dependencies of a graph and node.

###  RunEndT `module-attribute`

```
RunEndT = TypeVar('RunEndT', covariant=True, default=None)

```


Covariant type variable for the return type of a graph `run`[](../graph/#pydantic_graph.graph.Graph.run).

###  NodeRunEndT `module-attribute`

```
NodeRunEndT = TypeVar(
  "NodeRunEndT", covariant=True, default=Never[](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Never "typing_extensions.Never")
)

```


Covariant type variable for the return type of a node `run`[](#pydantic_graph.nodes.BaseNode.run).

© Pydantic Services Inc. 2024 to present 
