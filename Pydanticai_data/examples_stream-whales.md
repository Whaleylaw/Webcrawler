---
url: https://ai.pydantic.dev/examples/stream-whales/
title: Untitled
date_crawled: 
---

[ Skip to content ](#running-the-example)

[ ![logo](../../img/logo-white.svg) ](../.. "PydanticAI")

PydanticAI 

Stream whales 

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
    * [ Pydantic Model  ](../pydantic-model/)
    * [ Weather agent  ](../weather-agent/)
    * [ Bank support  ](../bank-support/)
    * [ SQL Generation  ](../sql-gen/)
    * [ Flight booking  ](../flight-booking/)
    * [ RAG  ](../rag/)
    * [ Stream markdown  ](../stream-markdown/)
    * Stream whales  [ Stream whales  ](./) Table of contents 
      * [ Running the Example  ](#running-the-example)
      * [ Example Code  ](#example-code)
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

# Stream whales

Information about whales — an example of streamed structured response validation.

Demonstrates:

  * [streaming structured responses](../../results/#streaming-structured-responses)



This script streams structured responses from GPT-4 about whales, validates the data and displays it as a dynamic table using `rich`[](https://github.com/Textualize/rich) as the data is received.

## Running the Example

With [dependencies installed and environment variables set](../#usage), run:

[pip](#__tabbed_1_1)[uv](#__tabbed_1_2)

```
python-mpydantic_ai_examples.stream_whales

```


```
uvrun-mpydantic_ai_examples.stream_whales

```


Should give an output like this:

## Example Code

stream_whales.py```
from typing import Annotated
import logfire
from pydantic import Field, ValidationError
from rich.console import Console
from rich.live import Live
from rich.table import Table
from typing_extensions import NotRequired, TypedDict
from pydantic_ai import Agent
# 'if-token-present' means nothing will be sent (and the example will work) if you don't have logfire configured
logfire.configure(send_to_logfire='if-token-present')

class Whale(TypedDict):
  name: str
  length: Annotated[
    float, Field(description='Average length of an adult whale in meters.')
  ]
  weight: NotRequired[
    Annotated[
      float,
      Field(description='Average weight of an adult whale in kilograms.', ge=50),
    ]
  ]
  ocean: NotRequired[str]
  description: NotRequired[Annotated[str, Field(description='Short Description')]]

agent = Agent('openai:gpt-4', result_type=list[Whale])

async def main():
  console = Console()
  with Live('\n' * 36, console=console) as live:
    console.print('Requesting data...', style='cyan')
    async with agent.run_stream(
      'Generate me details of 5 species of Whale.'
    ) as result:
      console.print('Response:', style='green')
      async for message, last in result.stream_structured(debounce_by=0.01):
        try:
          whales = await result.validate_structured_result(
            message, allow_partial=not last
          )
        except ValidationError as exc:
          if all(
            e['type'] == 'missing' and e['loc'] == ('response',)
            for e in exc.errors()
          ):
            continue
          else:
            raise
        table = Table(
          title='Species of Whale',
          caption='Streaming Structured responses from GPT-4',
          width=120,
        )
        table.add_column('ID', justify='right')
        table.add_column('Name')
        table.add_column('Avg. Length (m)', justify='right')
        table.add_column('Avg. Weight (kg)', justify='right')
        table.add_column('Ocean')
        table.add_column('Description', justify='right')
        for wid, whale in enumerate(whales, start=1):
          table.add_row(
            str(wid),
            whale['name'],
            f'{whale["length"]:0.0f}',
            f'{w:0.0f}' if (w := whale.get('weight')) else '…',
            whale.get('ocean') or '…',
            whale.get('description') or '…',
          )
        live.update(table)

if __name__ == '__main__':
  import asyncio
  asyncio.run(main())

```


© Pydantic Services Inc. 2024 to present 
