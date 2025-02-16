---
url: https://ai.pydantic.dev/api/format_as_xml/
title: Untitled
date_crawled: 
---

[ Skip to content ](#pydantic_aiformat_as_xml)

[ ![logo](../../img/logo-white.svg) ](../.. "PydanticAI")

PydanticAI 

pydantic_ai.format_as_xml 

Type to start searching

[ pydantic/pydantic-ai  ](https://github.com/pydantic/pydantic-ai "Go to repository")

[ ![logo](../../img/logo-white.svg) ](../.. "PydanticAI") PydanticAI 

[ pydantic/pydantic-ai  ](https://github.com/pydantic/pydantic-ai "Go to repository")

  * [ Introduction  ](../..)
  * [ Installation  ](../../install/)
  * [ Getting Help  ](../../help/)
  * [ Contributing  ](../../contributing/)
  * [ Troubleshooting  ](../../troubleshooting/)
  * Documentation  Documentation 
    * [ Agents  ](../../agents/)
    * [ Models  ](../../models/)
    * [ Dependencies  ](../../dependencies/)
    * [ Function Tools  ](../../tools/)
    * [ Results  ](../../results/)
    * [ Messages and chat history  ](../../message-history/)
    * [ Testing and Evals  ](../../testing-evals/)
    * [ Debugging and Monitoring  ](../../logfire/)
    * [ Multi-agent Applications  ](../../multi-agent-applications/)
    * [ Graphs  ](../../graph/)
  * [ Examples  ](../../examples/)

Examples 
    * [ Pydantic Model  ](../../examples/pydantic-model/)
    * [ Weather agent  ](../../examples/weather-agent/)
    * [ Bank support  ](../../examples/bank-support/)
    * [ SQL Generation  ](../../examples/sql-gen/)
    * [ Flight booking  ](../../examples/flight-booking/)
    * [ RAG  ](../../examples/rag/)
    * [ Stream markdown  ](../../examples/stream-markdown/)
    * [ Stream whales  ](../../examples/stream-whales/)
    * [ Chat App with FastAPI  ](../../examples/chat-app/)
    * [ Question Graph  ](../../examples/question-graph/)
  * API Reference  API Reference 
    * [ pydantic_ai.agent  ](../agent/)
    * [ pydantic_ai.tools  ](../tools/)
    * [ pydantic_ai.result  ](../result/)
    * [ pydantic_ai.messages  ](../messages/)
    * [ pydantic_ai.exceptions  ](../exceptions/)
    * [ pydantic_ai.settings  ](../settings/)
    * [ pydantic_ai.usage  ](../usage/)
    * pydantic_ai.format_as_xml  [ pydantic_ai.format_as_xml  ](./) Table of contents 
      * [ format_as_xml  ](#pydantic_ai.format_as_xml)
      * [ format_as_xml  ](#pydantic_ai.format_as_xml.format_as_xml)
    * [ pydantic_ai.models  ](../models/base/)
    * [ pydantic_ai.models.openai  ](../models/openai/)
    * [ pydantic_ai.models.anthropic  ](../models/anthropic/)
    * [ pydantic_ai.models.cohere  ](../models/cohere/)
    * [ pydantic_ai.models.gemini  ](../models/gemini/)
    * [ pydantic_ai.models.vertexai  ](../models/vertexai/)
    * [ pydantic_ai.models.groq  ](../models/groq/)
    * [ pydantic_ai.models.mistral  ](../models/mistral/)
    * [ pydantic_ai.models.test  ](../models/test/)
    * [ pydantic_ai.models.function  ](../models/function/)
    * [ pydantic_graph  ](../pydantic_graph/graph/)
    * [ pydantic_graph.nodes  ](../pydantic_graph/nodes/)
    * [ pydantic_graph.state  ](../pydantic_graph/state/)
    * [ pydantic_graph.mermaid  ](../pydantic_graph/mermaid/)
    * [ pydantic_graph.exceptions  ](../pydantic_graph/exceptions/)



Table of contents 

  * [ format_as_xml  ](#pydantic_ai.format_as_xml)
  * [ format_as_xml  ](#pydantic_ai.format_as_xml.format_as_xml)



  1. [ Introduction  ](../..)
  2. [ API Reference  ](../agent/)



Version Notice

This documentation is ahead of the last release by [6 commits](https://github.com/pydantic/pydantic-ai/compare/v0.0.24...main). You may see documentation for features not yet supported in the latest release [v0.0.24 2025-02-12](https://github.com/pydantic/pydantic-ai/releases/tag/v0.0.24). 

# `pydantic_ai.format_as_xml`

###  format_as_xml

```
format_as_xml(
  obj: Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any"),
  root_tag: str[](https://docs.python.org/3/library/stdtypes.html#str) = "examples",
  item_tag: str[](https://docs.python.org/3/library/stdtypes.html#str) = "example",
  include_root_tag: bool[](https://docs.python.org/3/library/functions.html#bool) = True,
  none_str: str[](https://docs.python.org/3/library/stdtypes.html#str) = "null",
  indent: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = " ",
) -> str[](https://docs.python.org/3/library/stdtypes.html#str)

```


Format a Python object as XML.

This is useful since LLMs often find it easier to read semi-structured data (e.g. examples) as XML, rather than JSON etc.

Supports: `str`, `bytes`, `bytearray`, `bool`, `int`, `float`, `date`, `datetime`, `Mapping`, `Iterable`, `dataclass`, and `BaseModel`.

Parameters:

Name | Type | Description | Default  
---|---|---|---  
`obj` |  `Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")` |  Python Object to serialize to XML. |  _required_  
`root_tag` |  `str[](https://docs.python.org/3/library/stdtypes.html#str)` |  Outer tag to wrap the XML in, use `None` to omit the outer tag. |  `'examples'`  
`item_tag` |  `str[](https://docs.python.org/3/library/stdtypes.html#str)` |  Tag to use for each item in an iterable (e.g. list), this is overridden by the class name for dataclasses and Pydantic models. |  `'example'`  
`include_root_tag` |  `bool[](https://docs.python.org/3/library/functions.html#bool)` |  Whether to include the root tag in the output (The root tag is always included if it includes a body - e.g. when the input is a simple value). |  `True`  
`none_str` |  `str[](https://docs.python.org/3/library/stdtypes.html#str)` |  String to use for `None` values. |  `'null'`  
`indent` |  `str[](https://docs.python.org/3/library/stdtypes.html#str) | None` |  Indentation string to use for pretty printing. |  `' '`  
  
Returns:

Type | Description  
---|---  
`str[](https://docs.python.org/3/library/stdtypes.html#str)` |  XML representation of the object.  
  
Example: 

format_as_xml_example.py```
from pydantic_ai.format_as_xml import format_as_xml
print(format_as_xml({'name': 'John', 'height': 6, 'weight': 200}, root_tag='user'))
'''
<user>
 <name>John</name>
 <height>6</height>
 <weight>200</weight>
</user>
'''

```


Source code in `pydantic_ai_slim/pydantic_ai/format_as_xml.py`

```
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
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
62
63
64
```
| ```
def format_as_xml(
  obj: Any,
  root_tag: str = 'examples',
  item_tag: str = 'example',
  include_root_tag: bool = True,
  none_str: str = 'null',
  indent: str | None = ' ',
) -> str:
"""Format a Python object as XML.
  This is useful since LLMs often find it easier to read semi-structured data (e.g. examples) as XML,
  rather than JSON etc.
  Supports: `str`, `bytes`, `bytearray`, `bool`, `int`, `float`, `date`, `datetime`, `Mapping`,
  `Iterable`, `dataclass`, and `BaseModel`.
  Args:
    obj: Python Object to serialize to XML.
    root_tag: Outer tag to wrap the XML in, use `None` to omit the outer tag.
    item_tag: Tag to use for each item in an iterable (e.g. list), this is overridden by the class name
      for dataclasses and Pydantic models.
    include_root_tag: Whether to include the root tag in the output
      (The root tag is always included if it includes a body - e.g. when the input is a simple value).
    none_str: String to use for `None` values.
    indent: Indentation string to use for pretty printing.
  Returns:
    XML representation of the object.
  Example:
  ```python {title="format_as_xml_example.py" lint="skip"}
  from pydantic_ai.format_as_xml import format_as_xml
  print(format_as_xml({'name': 'John', 'height': 6, 'weight': 200}, root_tag='user'))
  '''
  <user>
   <name>John</name>
   <height>6</height>
   <weight>200</weight>
  </user>
  '''
  ```
  """
  el = _ToXml(item_tag=item_tag, none_str=none_str).to_xml(obj, root_tag)
  if not include_root_tag and el.text is None:
    join = '' if indent is None else '\n'
    return join.join(_rootless_xml_elements(el, indent))
  else:
    if indent is not None:
      ElementTree.indent(el, space=indent)
    return ElementTree.tostring(el, encoding='unicode')

```
  
---|---  
  
© Pydantic Services Inc. 2024 to present 
