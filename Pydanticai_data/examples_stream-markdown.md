---
url: https://ai.pydantic.dev/examples/stream-markdown/
title: Untitled
date_crawled: 
---

[ Skip to content ](#running-the-example)

[ ![logo](../../img/logo-white.svg) ](../.. "PydanticAI")

PydanticAI 

Stream markdown 

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
    * Stream markdown  [ Stream markdown  ](./) Table of contents 
      * [ Running the Example  ](#running-the-example)
      * [ Example Code  ](#example-code)
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

# Stream markdown

This example shows how to stream markdown from an agent, using the `rich`[](https://github.com/Textualize/rich) library to highlight the output in the terminal.

It'll run the example with both OpenAI and Google Gemini models if the required environment variables are set.

Demonstrates:

  * [streaming text responses](../../results/#streaming-text)



## Running the Example

With [dependencies installed and environment variables set](../#usage), run:

[pip](#__tabbed_1_1)[uv](#__tabbed_1_2)

```
python-mpydantic_ai_examples.stream_markdown

```


```
uvrun-mpydantic_ai_examples.stream_markdown

```


## Example Code

```
import asyncio
import os
import logfire
from rich.console import Console, ConsoleOptions, RenderResult
from rich.live import Live
from rich.markdown import CodeBlock, Markdown
from rich.syntax import Syntax
from rich.text import Text
from pydantic_ai import Agent
from pydantic_ai.models import KnownModelName
# 'if-token-present' means nothing will be sent (and the example will work) if you don't have logfire configured
logfire.configure(send_to_logfire='if-token-present')
agent = Agent()
# models to try, and the appropriate env var
models: list[tuple[KnownModelName, str]] = [
  ('google-gla:gemini-1.5-flash', 'GEMINI_API_KEY'),
  ('openai:gpt-4o-mini', 'OPENAI_API_KEY'),
  ('groq:llama-3.3-70b-versatile', 'GROQ_API_KEY'),
]

async def main():
  prettier_code_blocks()
  console = Console()
  prompt = 'Show me a short example of using Pydantic.'
  console.log(f'Asking: {prompt}...', style='cyan')
  for model, env_var in models:
    if env_var in os.environ:
      console.log(f'Using model: {model}')
      with Live('', console=console, vertical_overflow='visible') as live:
        async with agent.run_stream(prompt, model=model) as result:
          async for message in result.stream():
            live.update(Markdown(message))
      console.log(result.usage())
    else:
      console.log(f'{model} requires {env_var} to be set.')

def prettier_code_blocks():
"""Make rich code blocks prettier and easier to copy.
  From https://github.com/samuelcolvin/aicli/blob/v0.8.0/samuelcolvin_aicli.py#L22
  """
  class SimpleCodeBlock(CodeBlock):
    def __rich_console__(
      self, console: Console, options: ConsoleOptions
    ) -> RenderResult:
      code = str(self.text).rstrip()
      yield Text(self.lexer_name, style='dim')
      yield Syntax(
        code,
        self.lexer_name,
        theme=self.theme,
        background_color='default',
        word_wrap=True,
      )
      yield Text(f'/{self.lexer_name}', style='dim')
  Markdown.elements['fence'] = SimpleCodeBlock

if __name__ == '__main__':
  asyncio.run(main())

```


© Pydantic Services Inc. 2024 to present 
