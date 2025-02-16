---
url: https://ai.pydantic.dev/api/pydantic_graph/mermaid/
title: Untitled
date_crawled: 
---

[ Skip to content ](#pydantic_graphmermaid)

[ ![logo](../../../img/logo-white.svg) ](../../.. "PydanticAI")

PydanticAI 

pydantic_graph.mermaid 

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
    * [ pydantic_graph.state  ](../state/)
    * pydantic_graph.mermaid  [ pydantic_graph.mermaid  ](./) Table of contents 
      * [ mermaid  ](#pydantic_graph.mermaid)
      * [ DEFAULT_HIGHLIGHT_CSS  ](#pydantic_graph.mermaid.DEFAULT_HIGHLIGHT_CSS)
      * [ StateDiagramDirection  ](#pydantic_graph.mermaid.StateDiagramDirection)
      * [ generate_code  ](#pydantic_graph.mermaid.generate_code)
      * [ request_image  ](#pydantic_graph.mermaid.request_image)
      * [ save_image  ](#pydantic_graph.mermaid.save_image)
      * [ MermaidConfig  ](#pydantic_graph.mermaid.MermaidConfig)
        * [ start_node  ](#pydantic_graph.mermaid.MermaidConfig.start_node)
        * [ highlighted_nodes  ](#pydantic_graph.mermaid.MermaidConfig.highlighted_nodes)
        * [ highlight_css  ](#pydantic_graph.mermaid.MermaidConfig.highlight_css)
        * [ title  ](#pydantic_graph.mermaid.MermaidConfig.title)
        * [ edge_labels  ](#pydantic_graph.mermaid.MermaidConfig.edge_labels)
        * [ notes  ](#pydantic_graph.mermaid.MermaidConfig.notes)
        * [ image_type  ](#pydantic_graph.mermaid.MermaidConfig.image_type)
        * [ pdf_fit  ](#pydantic_graph.mermaid.MermaidConfig.pdf_fit)
        * [ pdf_landscape  ](#pydantic_graph.mermaid.MermaidConfig.pdf_landscape)
        * [ pdf_paper  ](#pydantic_graph.mermaid.MermaidConfig.pdf_paper)
        * [ background_color  ](#pydantic_graph.mermaid.MermaidConfig.background_color)
        * [ theme  ](#pydantic_graph.mermaid.MermaidConfig.theme)
        * [ width  ](#pydantic_graph.mermaid.MermaidConfig.width)
        * [ height  ](#pydantic_graph.mermaid.MermaidConfig.height)
        * [ scale  ](#pydantic_graph.mermaid.MermaidConfig.scale)
        * [ httpx_client  ](#pydantic_graph.mermaid.MermaidConfig.httpx_client)
        * [ direction  ](#pydantic_graph.mermaid.MermaidConfig.direction)
      * [ NodeIdent  ](#pydantic_graph.mermaid.NodeIdent)
    * [ pydantic_graph.exceptions  ](../exceptions/)



Table of contents 

  * [ mermaid  ](#pydantic_graph.mermaid)
  * [ DEFAULT_HIGHLIGHT_CSS  ](#pydantic_graph.mermaid.DEFAULT_HIGHLIGHT_CSS)
  * [ StateDiagramDirection  ](#pydantic_graph.mermaid.StateDiagramDirection)
  * [ generate_code  ](#pydantic_graph.mermaid.generate_code)
  * [ request_image  ](#pydantic_graph.mermaid.request_image)
  * [ save_image  ](#pydantic_graph.mermaid.save_image)
  * [ MermaidConfig  ](#pydantic_graph.mermaid.MermaidConfig)
    * [ start_node  ](#pydantic_graph.mermaid.MermaidConfig.start_node)
    * [ highlighted_nodes  ](#pydantic_graph.mermaid.MermaidConfig.highlighted_nodes)
    * [ highlight_css  ](#pydantic_graph.mermaid.MermaidConfig.highlight_css)
    * [ title  ](#pydantic_graph.mermaid.MermaidConfig.title)
    * [ edge_labels  ](#pydantic_graph.mermaid.MermaidConfig.edge_labels)
    * [ notes  ](#pydantic_graph.mermaid.MermaidConfig.notes)
    * [ image_type  ](#pydantic_graph.mermaid.MermaidConfig.image_type)
    * [ pdf_fit  ](#pydantic_graph.mermaid.MermaidConfig.pdf_fit)
    * [ pdf_landscape  ](#pydantic_graph.mermaid.MermaidConfig.pdf_landscape)
    * [ pdf_paper  ](#pydantic_graph.mermaid.MermaidConfig.pdf_paper)
    * [ background_color  ](#pydantic_graph.mermaid.MermaidConfig.background_color)
    * [ theme  ](#pydantic_graph.mermaid.MermaidConfig.theme)
    * [ width  ](#pydantic_graph.mermaid.MermaidConfig.width)
    * [ height  ](#pydantic_graph.mermaid.MermaidConfig.height)
    * [ scale  ](#pydantic_graph.mermaid.MermaidConfig.scale)
    * [ httpx_client  ](#pydantic_graph.mermaid.MermaidConfig.httpx_client)
    * [ direction  ](#pydantic_graph.mermaid.MermaidConfig.direction)
  * [ NodeIdent  ](#pydantic_graph.mermaid.NodeIdent)



  1. [ Introduction  ](../../..)
  2. [ API Reference  ](../../agent/)



Version Notice

This documentation is ahead of the last release by [6 commits](https://github.com/pydantic/pydantic-ai/compare/v0.0.24...main). You may see documentation for features not yet supported in the latest release [v0.0.24 2025-02-12](https://github.com/pydantic/pydantic-ai/releases/tag/v0.0.24). 

# `pydantic_graph.mermaid`

###  DEFAULT_HIGHLIGHT_CSS `module-attribute`

```
DEFAULT_HIGHLIGHT_CSS = 'fill:#fdff32'

```


The default CSS to use for highlighting nodes.

###  StateDiagramDirection `module-attribute`

```
StateDiagramDirection = Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['TB', 'LR', 'RL', 'BT']

```


Used to specify the direction of the state diagram generated by mermaid.

  * `'TB'`: Top to bottom, this is the default for mermaid charts.
  * `'LR'`: Left to right
  * `'RL'`: Right to left
  * `'BT'`: Bottom to top



###  generate_code

```
generate_code(
  graph: Graph[](../graph/#pydantic_graph.graph.Graph "pydantic_graph.graph.Graph")[Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any"), Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any"), Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")],
  /,
  *,
  start_node: (
    Sequence[](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "collections.abc.Sequence")[NodeIdent[](#pydantic_graph.mermaid.NodeIdent "pydantic_graph.mermaid.NodeIdent")] | NodeIdent[](#pydantic_graph.mermaid.NodeIdent "pydantic_graph.mermaid.NodeIdent") | None
  ) = None,
  highlighted_nodes: (
    Sequence[](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "collections.abc.Sequence")[NodeIdent[](#pydantic_graph.mermaid.NodeIdent "pydantic_graph.mermaid.NodeIdent")] | NodeIdent[](#pydantic_graph.mermaid.NodeIdent "pydantic_graph.mermaid.NodeIdent") | None
  ) = None,
  highlight_css: str[](https://docs.python.org/3/library/stdtypes.html#str) = DEFAULT_HIGHLIGHT_CSS[](#pydantic_graph.mermaid.DEFAULT_HIGHLIGHT_CSS "pydantic_graph.mermaid.DEFAULT_HIGHLIGHT_CSS"),
  title: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None,
  edge_labels: bool[](https://docs.python.org/3/library/functions.html#bool) = True,
  notes: bool[](https://docs.python.org/3/library/functions.html#bool) = True,
  direction: StateDiagramDirection[](#pydantic_graph.mermaid.StateDiagramDirection "pydantic_graph.mermaid.StateDiagramDirection") | None,
) -> str[](https://docs.python.org/3/library/stdtypes.html#str)

```


Generate [Mermaid state diagram](https://mermaid.js.org/syntax/stateDiagram.html) code for a graph.

Parameters:

Name | Type | Description | Default  
---|---|---|---  
`graph` |  `Graph[](../graph/#pydantic_graph.graph.Graph "pydantic_graph.graph.Graph")[Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any"), Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any"), Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")]` |  The graph to generate the image for. |  _required_  
`start_node` |  `Sequence[](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "collections.abc.Sequence")[NodeIdent[](#pydantic_graph.mermaid.NodeIdent "pydantic_graph.mermaid.NodeIdent")] | NodeIdent[](#pydantic_graph.mermaid.NodeIdent "pydantic_graph.mermaid.NodeIdent") | None` |  Identifiers of nodes that start the graph. |  `None`  
`highlighted_nodes` |  `Sequence[](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "collections.abc.Sequence")[NodeIdent[](#pydantic_graph.mermaid.NodeIdent "pydantic_graph.mermaid.NodeIdent")] | NodeIdent[](#pydantic_graph.mermaid.NodeIdent "pydantic_graph.mermaid.NodeIdent") | None` |  Identifiers of nodes to highlight. |  `None`  
`highlight_css` |  `str[](https://docs.python.org/3/library/stdtypes.html#str)` |  CSS to use for highlighting nodes. |  `DEFAULT_HIGHLIGHT_CSS[](#pydantic_graph.mermaid.DEFAULT_HIGHLIGHT_CSS "pydantic_graph.mermaid.DEFAULT_HIGHLIGHT_CSS")`  
`title` |  `str[](https://docs.python.org/3/library/stdtypes.html#str) | None` |  The title of the diagram. |  `None`  
`edge_labels` |  `bool[](https://docs.python.org/3/library/functions.html#bool)` |  Whether to include edge labels in the diagram. |  `True`  
`notes` |  `bool[](https://docs.python.org/3/library/functions.html#bool)` |  Whether to include notes in the diagram. |  `True`  
`direction` |  `StateDiagramDirection[](#pydantic_graph.mermaid.StateDiagramDirection "pydantic_graph.mermaid.StateDiagramDirection") | None` |  The direction of flow. |  _required_  
  
Returns:

Type | Description  
---|---  
`str[](https://docs.python.org/3/library/stdtypes.html#str)` |  The Mermaid code for the graph.  
  
Source code in `pydantic_graph/pydantic_graph/mermaid.py`

```
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
```
| ```
def generate_code( # noqa: C901
  graph: Graph[Any, Any, Any],
  /,
  *,
  start_node: Sequence[NodeIdent] | NodeIdent | None = None,
  highlighted_nodes: Sequence[NodeIdent] | NodeIdent | None = None,
  highlight_css: str = DEFAULT_HIGHLIGHT_CSS,
  title: str | None = None,
  edge_labels: bool = True,
  notes: bool = True,
  direction: StateDiagramDirection | None,
) -> str:
"""Generate [Mermaid state diagram](https://mermaid.js.org/syntax/stateDiagram.html) code for a graph.
  Args:
    graph: The graph to generate the image for.
    start_node: Identifiers of nodes that start the graph.
    highlighted_nodes: Identifiers of nodes to highlight.
    highlight_css: CSS to use for highlighting nodes.
    title: The title of the diagram.
    edge_labels: Whether to include edge labels in the diagram.
    notes: Whether to include notes in the diagram.
    direction: The direction of flow.

  Returns:
    The Mermaid code for the graph.
  """
  start_node_ids = set(_node_ids(start_node or ()))
  for node_id in start_node_ids:
    if node_id not in graph.node_defs:
      raise LookupError(f'Start node "{node_id}" is not in the graph.')
  lines: list[str] = []
  if title:
    lines = ['---', f'title: {title}', '---']
  lines.append('stateDiagram-v2')
  if direction is not None:
    lines.append(f' direction {direction}')
  for node_id, node_def in graph.node_defs.items():
    # we use round brackets (rounded box) for nodes other than the start and end
    if node_id in start_node_ids:
      lines.append(f' [*] --> {node_id}')
    if node_def.returns_base_node:
      for next_node_id in graph.node_defs:
        lines.append(f' {node_id} --> {next_node_id}')
    else:
      for next_node_id, edge in node_def.next_node_edges.items():
        line = f' {node_id} --> {next_node_id}'
        if edge_labels and edge.label:
          line += f': {edge.label}'
        lines.append(line)
    if end_edge := node_def.end_edge:
      line = f' {node_id} --> [*]'
      if edge_labels and end_edge.label:
        line += f': {end_edge.label}'
      lines.append(line)
    if notes and node_def.note:
      lines.append(f' note right of {node_id}')
      # mermaid doesn't like multiple paragraphs in a note, and shows if so
      clean_docs = re.sub('\n{2,}', '\n', node_def.note)
      lines.append(indent(clean_docs, '  '))
      lines.append(' end note')
  if highlighted_nodes:
    lines.append('')
    lines.append(f'classDef highlighted {highlight_css}')
    for node_id in _node_ids(highlighted_nodes):
      if node_id not in graph.node_defs:
        raise LookupError(f'Highlighted node "{node_id}" is not in the graph.')
      lines.append(f'class {node_id} highlighted')
  return '\n'.join(lines)

```
  
---|---  
  
###  request_image

```
request_image(
  graph: Graph[](../graph/#pydantic_graph.graph.Graph "pydantic_graph.graph.Graph")[Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any"), Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any"), Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")],
  /,
  **kwargs: Unpack[](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Unpack "typing_extensions.Unpack")[MermaidConfig[](#pydantic_graph.mermaid.MermaidConfig "pydantic_graph.mermaid.MermaidConfig")],
) -> bytes[](https://docs.python.org/3/library/stdtypes.html#bytes)

```


Generate an image of a Mermaid diagram using [mermaid.ink](https://mermaid.ink).

Parameters:

Name | Type | Description | Default  
---|---|---|---  
`graph` |  `Graph[](../graph/#pydantic_graph.graph.Graph "pydantic_graph.graph.Graph")[Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any"), Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any"), Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")]` |  The graph to generate the image for. |  _required_  
`**kwargs` |  `Unpack[](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Unpack "typing_extensions.Unpack")[MermaidConfig[](#pydantic_graph.mermaid.MermaidConfig "pydantic_graph.mermaid.MermaidConfig")]` |  Additional parameters to configure mermaid chart generation. |  `{}`  
  
Returns:

Type | Description  
---|---  
`bytes[](https://docs.python.org/3/library/stdtypes.html#bytes)` |  The image data.  
  
Source code in `pydantic_graph/pydantic_graph/mermaid.py`

```
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
```
| ```
def request_image(
  graph: Graph[Any, Any, Any],
  /,
  **kwargs: Unpack[MermaidConfig],
) -> bytes:
"""Generate an image of a Mermaid diagram using [mermaid.ink](https://mermaid.ink).
  Args:
    graph: The graph to generate the image for.
    **kwargs: Additional parameters to configure mermaid chart generation.
  Returns:
    The image data.
  """
  code = generate_code(
    graph,
    start_node=kwargs.get('start_node'),
    highlighted_nodes=kwargs.get('highlighted_nodes'),
    highlight_css=kwargs.get('highlight_css', DEFAULT_HIGHLIGHT_CSS),
    title=kwargs.get('title'),
    edge_labels=kwargs.get('edge_labels', True),
    notes=kwargs.get('notes', True),
    direction=kwargs.get('direction'),
  )
  code_base64 = base64.b64encode(code.encode()).decode()
  params: dict[str, str | float] = {}
  if kwargs.get('image_type') == 'pdf':
    url = f'https://mermaid.ink/pdf/{code_base64}'
    if kwargs.get('pdf_fit'):
      params['fit'] = ''
    if kwargs.get('pdf_landscape'):
      params['landscape'] = ''
    if pdf_paper := kwargs.get('pdf_paper'):
      params['paper'] = pdf_paper
  elif kwargs.get('image_type') == 'svg':
    url = f'https://mermaid.ink/svg/{code_base64}'
  else:
    url = f'https://mermaid.ink/img/{code_base64}'
    if image_type := kwargs.get('image_type'):
      params['type'] = image_type
  if background_color := kwargs.get('background_color'):
    params['bgColor'] = background_color
  if theme := kwargs.get('theme'):
    params['theme'] = theme
  if width := kwargs.get('width'):
    params['width'] = width
  if height := kwargs.get('height'):
    params['height'] = height
  if scale := kwargs.get('scale'):
    params['scale'] = scale
  httpx_client = kwargs.get('httpx_client') or httpx.Client()
  response = httpx_client.get(url, params=params)
  if not response.is_success:
    raise httpx.HTTPStatusError(
      f'{response.status_code} error generating image:\n{response.text}',
      request=response.request,
      response=response,
    )
  return response.content

```
  
---|---  
  
###  save_image

```
save_image(
  path: Path[](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path") | str[](https://docs.python.org/3/library/stdtypes.html#str),
  graph: Graph[](../graph/#pydantic_graph.graph.Graph "pydantic_graph.graph.Graph")[Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any"), Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any"), Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")],
  /,
  **kwargs: Unpack[](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Unpack "typing_extensions.Unpack")[MermaidConfig[](#pydantic_graph.mermaid.MermaidConfig "pydantic_graph.mermaid.MermaidConfig")],
) -> None

```


Generate an image of a Mermaid diagram using [mermaid.ink](https://mermaid.ink) and save it to a local file.

Parameters:

Name | Type | Description | Default  
---|---|---|---  
`path` |  `Path[](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path") | str[](https://docs.python.org/3/library/stdtypes.html#str)` |  The path to save the image to. |  _required_  
`graph` |  `Graph[](../graph/#pydantic_graph.graph.Graph "pydantic_graph.graph.Graph")[Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any"), Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any"), Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")]` |  The graph to generate the image for. |  _required_  
`**kwargs` |  `Unpack[](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Unpack "typing_extensions.Unpack")[MermaidConfig[](#pydantic_graph.mermaid.MermaidConfig "pydantic_graph.mermaid.MermaidConfig")]` |  Additional parameters to configure mermaid chart generation. |  `{}`  
  
Source code in `pydantic_graph/pydantic_graph/mermaid.py`

```
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
```
| ```
def save_image(
  path: Path | str,
  graph: Graph[Any, Any, Any],
  /,
  **kwargs: Unpack[MermaidConfig],
) -> None:
"""Generate an image of a Mermaid diagram using [mermaid.ink](https://mermaid.ink) and save it to a local file.
  Args:
    path: The path to save the image to.
    graph: The graph to generate the image for.
    **kwargs: Additional parameters to configure mermaid chart generation.
  """
  if isinstance(path, str):
    path = Path(path)
  if 'image_type' not in kwargs:
    ext = path.suffix.lower()[1:]
    # no need to check for .jpeg/.jpg, as it is the default
    if ext in ('png', 'webp', 'svg', 'pdf'):
      kwargs['image_type'] = ext
  image_data = request_image(graph, **kwargs)
  path.write_bytes(image_data)

```
  
---|---  
  
###  MermaidConfig

Bases: `TypedDict[](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypedDict "typing_extensions.TypedDict")`

Parameters to configure mermaid chart generation.

Source code in `pydantic_graph/pydantic_graph/mermaid.py`

```
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
```
| ```
class MermaidConfig(TypedDict, total=False):
"""Parameters to configure mermaid chart generation."""
  start_node: Sequence[NodeIdent] | NodeIdent
"""Identifiers of nodes that start the graph."""
  highlighted_nodes: Sequence[NodeIdent] | NodeIdent
"""Identifiers of nodes to highlight."""
  highlight_css: str
"""CSS to use for highlighting nodes."""
  title: str | None
"""The title of the diagram."""
  edge_labels: bool
"""Whether to include edge labels in the diagram."""
  notes: bool
"""Whether to include notes on nodes in the diagram, defaults to true."""
  image_type: Literal['jpeg', 'png', 'webp', 'svg', 'pdf']
"""The image type to generate. If unspecified, the default behavior is `'jpeg'`."""
  pdf_fit: bool
"""When using image_type='pdf', whether to fit the diagram to the PDF page."""
  pdf_landscape: bool
"""When using image_type='pdf', whether to use landscape orientation for the PDF.
  This has no effect if using `pdf_fit`.
  """
  pdf_paper: Literal['letter', 'legal', 'tabloid', 'ledger', 'a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6']
"""When using image_type='pdf', the paper size of the PDF."""
  background_color: str
"""The background color of the diagram.
  If None, the default transparent background is used. The color value is interpreted as a hexadecimal color
  code by default (and should not have a leading '#'), but you can also use named colors by prefixing the
  value with `'!'`. For example, valid choices include `background_color='!white'` or `background_color='FF0000'`.
  """
  theme: Literal['default', 'neutral', 'dark', 'forest']
"""The theme of the diagram. Defaults to 'default'."""
  width: int
"""The width of the diagram."""
  height: int
"""The height of the diagram."""
  scale: Annotated[float, Ge(1), Le(3)]
"""The scale of the diagram.
  The scale must be a number between 1 and 3, and you can only set a scale if one or both of width and height are set.
  """
  httpx_client: httpx.Client
"""An HTTPX client to use for requests, mostly for testing purposes."""
  direction: StateDiagramDirection
"""The direction of the state diagram."""

```
  
---|---  
  
####  start_node `instance-attribute`

```
start_node: Sequence[](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "collections.abc.Sequence")[NodeIdent[](#pydantic_graph.mermaid.NodeIdent "pydantic_graph.mermaid.NodeIdent")] | NodeIdent[](#pydantic_graph.mermaid.NodeIdent "pydantic_graph.mermaid.NodeIdent")

```


Identifiers of nodes that start the graph.

####  highlighted_nodes `instance-attribute`

```
highlighted_nodes: Sequence[](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "collections.abc.Sequence")[NodeIdent[](#pydantic_graph.mermaid.NodeIdent "pydantic_graph.mermaid.NodeIdent")] | NodeIdent[](#pydantic_graph.mermaid.NodeIdent "pydantic_graph.mermaid.NodeIdent")

```


Identifiers of nodes to highlight.

####  highlight_css `instance-attribute`

```
highlight_css: str[](https://docs.python.org/3/library/stdtypes.html#str)

```


CSS to use for highlighting nodes.

####  title `instance-attribute`

```
title: str[](https://docs.python.org/3/library/stdtypes.html#str) | None

```


The title of the diagram.

####  edge_labels `instance-attribute`

```
edge_labels: bool[](https://docs.python.org/3/library/functions.html#bool)

```


Whether to include edge labels in the diagram.

####  notes `instance-attribute`

```
notes: bool[](https://docs.python.org/3/library/functions.html#bool)

```


Whether to include notes on nodes in the diagram, defaults to true.

####  image_type `instance-attribute`

```
image_type: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['jpeg', 'png', 'webp', 'svg', 'pdf']

```


The image type to generate. If unspecified, the default behavior is `'jpeg'`.

####  pdf_fit `instance-attribute`

```
pdf_fit: bool[](https://docs.python.org/3/library/functions.html#bool)

```


When using image_type='pdf', whether to fit the diagram to the PDF page.

####  pdf_landscape `instance-attribute`

```
pdf_landscape: bool[](https://docs.python.org/3/library/functions.html#bool)

```


When using image_type='pdf', whether to use landscape orientation for the PDF.

This has no effect if using `pdf_fit`.

####  pdf_paper `instance-attribute`

```
pdf_paper: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")[
  "letter",
  "legal",
  "tabloid",
  "ledger",
  "a0",
  "a1",
  "a2",
  "a3",
  "a4",
  "a5",
  "a6",
]

```


When using image_type='pdf', the paper size of the PDF.

####  background_color `instance-attribute`

```
background_color: str[](https://docs.python.org/3/library/stdtypes.html#str)

```


The background color of the diagram.

If None, the default transparent background is used. The color value is interpreted as a hexadecimal color code by default (and should not have a leading '#'), but you can also use named colors by prefixing the value with `'!'`. For example, valid choices include `background_color='!white'` or `background_color='FF0000'`.

####  theme `instance-attribute`

```
theme: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['default', 'neutral', 'dark', 'forest']

```


The theme of the diagram. Defaults to 'default'.

####  width `instance-attribute`

```
width: int[](https://docs.python.org/3/library/functions.html#int)

```


The width of the diagram.

####  height `instance-attribute`

```
height: int[](https://docs.python.org/3/library/functions.html#int)

```


The height of the diagram.

####  scale `instance-attribute`

```
scale: Annotated[](https://docs.python.org/3/library/typing.html#typing.Annotated "typing.Annotated")[float[](https://docs.python.org/3/library/functions.html#float), Ge(1), Le(3)]

```


The scale of the diagram.

The scale must be a number between 1 and 3, and you can only set a scale if one or both of width and height are set.

####  httpx_client `instance-attribute`

```
httpx_client: Client

```


An HTTPX client to use for requests, mostly for testing purposes.

####  direction `instance-attribute`

```
direction: StateDiagramDirection[](#pydantic_graph.mermaid.StateDiagramDirection "pydantic_graph.mermaid.StateDiagramDirection")

```


The direction of the state diagram.

###  NodeIdent `module-attribute`

```
NodeIdent: TypeAlias[](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypeAlias "typing_extensions.TypeAlias") = (
  "type[BaseNode[Any, Any, Any]] | BaseNode[Any, Any, Any] | str"
)

```


A type alias for a node identifier.

This can be:

  * A node instance (instance of a subclass of `BaseNode`[](../nodes/#pydantic_graph.nodes.BaseNode)).
  * A node class (subclass of `BaseNode`[](../nodes/#pydantic_graph.nodes.BaseNode)).
  * A string representing the node ID.



© Pydantic Services Inc. 2024 to present 
