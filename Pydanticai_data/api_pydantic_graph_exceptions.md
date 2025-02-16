---
url: https://ai.pydantic.dev/api/pydantic_graph/exceptions/
title: Untitled
date_crawled: 
---

[ Skip to content ](#pydantic_graphexceptions)

[ ![logo](../../../img/logo-white.svg) ](../../.. "PydanticAI")

PydanticAI 

pydantic_graph.exceptions 

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
    * [ pydantic_graph.mermaid  ](../mermaid/)
    * pydantic_graph.exceptions  [ pydantic_graph.exceptions  ](./) Table of contents 
      * [ exceptions  ](#pydantic_graph.exceptions)
      * [ GraphSetupError  ](#pydantic_graph.exceptions.GraphSetupError)
        * [ message  ](#pydantic_graph.exceptions.GraphSetupError.message)
      * [ GraphRuntimeError  ](#pydantic_graph.exceptions.GraphRuntimeError)
        * [ message  ](#pydantic_graph.exceptions.GraphRuntimeError.message)



Table of contents 

  * [ exceptions  ](#pydantic_graph.exceptions)
  * [ GraphSetupError  ](#pydantic_graph.exceptions.GraphSetupError)
    * [ message  ](#pydantic_graph.exceptions.GraphSetupError.message)
  * [ GraphRuntimeError  ](#pydantic_graph.exceptions.GraphRuntimeError)
    * [ message  ](#pydantic_graph.exceptions.GraphRuntimeError.message)



  1. [ Introduction  ](../../..)
  2. [ API Reference  ](../../agent/)



Version Notice

This documentation is ahead of the last release by [6 commits](https://github.com/pydantic/pydantic-ai/compare/v0.0.24...main). You may see documentation for features not yet supported in the latest release [v0.0.24 2025-02-12](https://github.com/pydantic/pydantic-ai/releases/tag/v0.0.24). 

# `pydantic_graph.exceptions`

###  GraphSetupError

Bases: `TypeError[](https://docs.python.org/3/library/exceptions.html#TypeError)`

Error caused by an incorrectly configured graph.

Source code in `pydantic_graph/pydantic_graph/exceptions.py`

```
1
2
3
4
5
6
7
8
9
```
| ```
class GraphSetupError(TypeError):
"""Error caused by an incorrectly configured graph."""
  message: str
"""Description of the mistake."""
  def __init__(self, message: str):
    self.message = message
    super().__init__(message)

```
  
---|---  
  
####  message `instance-attribute`

```
message: str[](https://docs.python.org/3/library/stdtypes.html#str) = message[](#pydantic_graph.exceptions.GraphSetupError.message "pydantic_graph.exceptions.GraphSetupError.message")

```


Description of the mistake.

###  GraphRuntimeError

Bases: `RuntimeError[](https://docs.python.org/3/library/exceptions.html#RuntimeError)`

Error caused by an issue during graph execution.

Source code in `pydantic_graph/pydantic_graph/exceptions.py`

```
12
13
14
15
16
17
18
19
20
```
| ```
class GraphRuntimeError(RuntimeError):
"""Error caused by an issue during graph execution."""
  message: str
"""The error message."""
  def __init__(self, message: str):
    self.message = message
    super().__init__(message)

```
  
---|---  
  
####  message `instance-attribute`

```
message: str[](https://docs.python.org/3/library/stdtypes.html#str) = message[](#pydantic_graph.exceptions.GraphRuntimeError.message "pydantic_graph.exceptions.GraphRuntimeError.message")

```


The error message.

© Pydantic Services Inc. 2024 to present 
