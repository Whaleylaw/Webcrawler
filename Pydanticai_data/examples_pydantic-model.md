---
url: https://ai.pydantic.dev/examples/pydantic-model/
title: Untitled
date_crawled: 
---

[ Skip to content ](#pydantic-model)

[ ![logo](../../img/logo-white.svg) ](../.. "PydanticAI")

PydanticAI 

Pydantic Model 

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
  * [ Examples  ](../)

Examples 
    * Pydantic Model  [ Pydantic Model  ](./) Table of contents 
      * [ Running the Example  ](#running-the-example)
      * [ Example Code  ](#example-code)
    * [ Weather agent  ](../weather-agent/)
    * [ Bank support  ](../bank-support/)
    * [ SQL Generation  ](../sql-gen/)
    * [ Flight booking  ](../flight-booking/)
    * [ RAG  ](../rag/)
    * [ Stream markdown  ](../stream-markdown/)
    * [ Stream whales  ](../stream-whales/)
    * [ Chat App with FastAPI  ](../chat-app/)
    * [ Question Graph  ](../question-graph/)
  * API Reference  API Reference 
    * [ pydantic_ai.agent  ](../../api/agent/)
    * [ pydantic_ai.tools  ](../../api/tools/)
    * [ pydantic_ai.result  ](../../api/result/)
    * [ pydantic_ai.messages  ](../../api/messages/)
    * [ pydantic_ai.exceptions  ](../../api/exceptions/)
    * [ pydantic_ai.settings  ](../../api/settings/)
    * [ pydantic_ai.usage  ](../../api/usage/)
    * [ pydantic_ai.format_as_xml  ](../../api/format_as_xml/)
    * [ pydantic_ai.models  ](../../api/models/base/)
    * [ pydantic_ai.models.openai  ](../../api/models/openai/)
    * [ pydantic_ai.models.anthropic  ](../../api/models/anthropic/)
    * [ pydantic_ai.models.cohere  ](../../api/models/cohere/)
    * [ pydantic_ai.models.gemini  ](../../api/models/gemini/)
    * [ pydantic_ai.models.vertexai  ](../../api/models/vertexai/)
    * [ pydantic_ai.models.groq  ](../../api/models/groq/)
    * [ pydantic_ai.models.mistral  ](../../api/models/mistral/)
    * [ pydantic_ai.models.test  ](../../api/models/test/)
    * [ pydantic_ai.models.function  ](../../api/models/function/)
    * [ pydantic_graph  ](../../api/pydantic_graph/graph/)
    * [ pydantic_graph.nodes  ](../../api/pydantic_graph/nodes/)
    * [ pydantic_graph.state  ](../../api/pydantic_graph/state/)
    * [ pydantic_graph.mermaid  ](../../api/pydantic_graph/mermaid/)
    * [ pydantic_graph.exceptions  ](../../api/pydantic_graph/exceptions/)



Table of contents 

  * [ Running the Example  ](#running-the-example)
  * [ Example Code  ](#example-code)



  1. [ Introduction  ](../..)
  2. [ Examples  ](../)



Version Notice

This documentation is ahead of the last release by [6 commits](https://github.com/pydantic/pydantic-ai/compare/v0.0.24...main). You may see documentation for features not yet supported in the latest release [v0.0.24 2025-02-12](https://github.com/pydantic/pydantic-ai/releases/tag/v0.0.24). 

# Pydantic Model

Simple example of using PydanticAI to construct a Pydantic model from a text input.

Demonstrates:

  * [structured `result_type`](../../results/#structured-result-validation)



## Running the Example

With [dependencies installed and environment variables set](../#usage), run:

[pip](#__tabbed_1_1)[uv](#__tabbed_1_2)

```
python-mpydantic_ai_examples.pydantic_model

```


```
uvrun-mpydantic_ai_examples.pydantic_model

```


This examples uses `openai:gpt-4o` by default, but it works well with other models, e.g. you can run it with Gemini using:

[pip](#__tabbed_2_1)[uv](#__tabbed_2_2)

```
PYDANTIC_AI_MODEL=gemini-1.5-propython-mpydantic_ai_examples.pydantic_model

```


```
PYDANTIC_AI_MODEL=gemini-1.5-prouvrun-mpydantic_ai_examples.pydantic_model

```


(or `PYDANTIC_AI_MODEL=gemini-1.5-flash ...`)

## Example Code

pydantic_model.py```
import os
from typing import cast
import logfire
from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai.models import KnownModelName
# 'if-token-present' means nothing will be sent (and the example will work) if you don't have logfire configured
logfire.configure(send_to_logfire='if-token-present')

class MyModel(BaseModel):
  city: str
  country: str

model = cast(KnownModelName, os.getenv('PYDANTIC_AI_MODEL', 'openai:gpt-4o'))
print(f'Using model: {model}')
agent = Agent(model, result_type=MyModel)
if __name__ == '__main__':
  result = agent.run_sync('The windy city in the US of A.')
  print(result.data)
  print(result.usage())

```


© Pydantic Services Inc. 2024 to present 
