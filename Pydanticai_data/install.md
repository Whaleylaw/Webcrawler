---
url: https://ai.pydantic.dev/install/
title: Untitled
date_crawled: 
---

[ Skip to content ](#installation)

[ ![logo](../img/logo-white.svg) ](.. "PydanticAI")

PydanticAI 

Installation 

Type to start searching

[ pydantic/pydantic-ai  ](https://github.com/pydantic/pydantic-ai "Go to repository")

[ ![logo](../img/logo-white.svg) ](.. "PydanticAI") PydanticAI 

[ pydantic/pydantic-ai  ](https://github.com/pydantic/pydantic-ai "Go to repository")

  * [ Introduction  ](..)
  * Installation  [ Installation  ](./) Table of contents 
    * [ Use with Pydantic Logfire  ](#use-with-pydantic-logfire)
    * [ Running Examples  ](#running-examples)
    * [ Slim Install  ](#slim-install)
  * [ Getting Help  ](../help/)
  * [ Contributing  ](../contributing/)
  * [ Troubleshooting  ](../troubleshooting/)
  * Documentation  Documentation 
    * [ Agents  ](../agents/)
    * [ Models  ](../models/)
    * [ Dependencies  ](../dependencies/)
    * [ Function Tools  ](../tools/)
    * [ Results  ](../results/)
    * [ Messages and chat history  ](../message-history/)
    * [ Testing and Evals  ](../testing-evals/)
    * [ Debugging and Monitoring  ](../logfire/)
    * [ Multi-agent Applications  ](../multi-agent-applications/)
    * [ Graphs  ](../graph/)
  * [ Examples  ](../examples/)

Examples 
    * [ Pydantic Model  ](../examples/pydantic-model/)
    * [ Weather agent  ](../examples/weather-agent/)
    * [ Bank support  ](../examples/bank-support/)
    * [ SQL Generation  ](../examples/sql-gen/)
    * [ Flight booking  ](../examples/flight-booking/)
    * [ RAG  ](../examples/rag/)
    * [ Stream markdown  ](../examples/stream-markdown/)
    * [ Stream whales  ](../examples/stream-whales/)
    * [ Chat App with FastAPI  ](../examples/chat-app/)
    * [ Question Graph  ](../examples/question-graph/)
  * API Reference  API Reference 
    * [ pydantic_ai.agent  ](../api/agent/)
    * [ pydantic_ai.tools  ](../api/tools/)
    * [ pydantic_ai.result  ](../api/result/)
    * [ pydantic_ai.messages  ](../api/messages/)
    * [ pydantic_ai.exceptions  ](../api/exceptions/)
    * [ pydantic_ai.settings  ](../api/settings/)
    * [ pydantic_ai.usage  ](../api/usage/)
    * [ pydantic_ai.format_as_xml  ](../api/format_as_xml/)
    * [ pydantic_ai.models  ](../api/models/base/)
    * [ pydantic_ai.models.openai  ](../api/models/openai/)
    * [ pydantic_ai.models.anthropic  ](../api/models/anthropic/)
    * [ pydantic_ai.models.cohere  ](../api/models/cohere/)
    * [ pydantic_ai.models.gemini  ](../api/models/gemini/)
    * [ pydantic_ai.models.vertexai  ](../api/models/vertexai/)
    * [ pydantic_ai.models.groq  ](../api/models/groq/)
    * [ pydantic_ai.models.mistral  ](../api/models/mistral/)
    * [ pydantic_ai.models.test  ](../api/models/test/)
    * [ pydantic_ai.models.function  ](../api/models/function/)
    * [ pydantic_graph  ](../api/pydantic_graph/graph/)
    * [ pydantic_graph.nodes  ](../api/pydantic_graph/nodes/)
    * [ pydantic_graph.state  ](../api/pydantic_graph/state/)
    * [ pydantic_graph.mermaid  ](../api/pydantic_graph/mermaid/)
    * [ pydantic_graph.exceptions  ](../api/pydantic_graph/exceptions/)



Table of contents 

  * [ Use with Pydantic Logfire  ](#use-with-pydantic-logfire)
  * [ Running Examples  ](#running-examples)
  * [ Slim Install  ](#slim-install)



Version Notice

This documentation is ahead of the last release by [6 commits](https://github.com/pydantic/pydantic-ai/compare/v0.0.24...main). You may see documentation for features not yet supported in the latest release [v0.0.24 2025-02-12](https://github.com/pydantic/pydantic-ai/releases/tag/v0.0.24). 

# Installation

PydanticAI is available on PyPI as `pydantic-ai`[](https://pypi.org/project/pydantic-ai/) so installation is as simple as:

[pip](#__tabbed_1_1)[uv](#__tabbed_1_2)

```
pipinstallpydantic-ai

```


```
uvaddpydantic-ai

```


(Requires Python 3.9+)

This installs the `pydantic_ai` package, core dependencies, and libraries required to use all the models included in PydanticAI. If you want to use a specific model, you can install the ["slim"](#slim-install) version of PydanticAI.

## Use with Pydantic Logfire

PydanticAI has an excellent (but completely optional) integration with [Pydantic Logfire](https://pydantic.dev/logfire) to help you view and understand agent runs.

To use Logfire with PydanticAI, install `pydantic-ai` or `pydantic-ai-slim` with the `logfire` optional group:

[pip](#__tabbed_2_1)[uv](#__tabbed_2_2)

```
pipinstall'pydantic-ai[logfire]'

```


```
uvadd'pydantic-ai[logfire]'

```


From there, follow the [Logfire setup docs](../logfire/#using-logfire) to configure Logfire.

## Running Examples

We distribute the `pydantic_ai_examples`[](https://github.com/pydantic/pydantic-ai/tree/main/examples/pydantic_ai_examples) directory as a separate PyPI package (`pydantic-ai-examples`[](https://pypi.org/project/pydantic-ai-examples/)) to make examples extremely easy to customize and run.

To install examples, use the `examples` optional group:

[pip](#__tabbed_3_1)[uv](#__tabbed_3_2)

```
pipinstall'pydantic-ai[examples]'

```


```
uvadd'pydantic-ai[examples]'

```


To run the examples, follow instructions in the [examples docs](../examples/).

## Slim Install

If you know which model you're going to use and want to avoid installing superfluous packages, you can use the `pydantic-ai-slim`[](https://pypi.org/project/pydantic-ai-slim/) package. For example, if you're using just `OpenAIModel`[](../api/models/openai/#pydantic_ai.models.openai.OpenAIModel), you would run:

[pip](#__tabbed_4_1)[uv](#__tabbed_4_2)

```
pipinstall'pydantic-ai-slim[openai]'

```


```
uvadd'pydantic-ai-slim[openai]'

```


`pydantic-ai-slim` has the following optional groups:

  * `logfire` — installs `logfire`[](../logfire/) [PyPI ↗](https://pypi.org/project/logfire)
  * `openai` — installs `openai` [PyPI ↗](https://pypi.org/project/openai)
  * `vertexai` — installs `google-auth` [PyPI ↗](https://pypi.org/project/google-auth) and `requests` [PyPI ↗](https://pypi.org/project/requests)
  * `anthropic` — installs `anthropic` [PyPI ↗](https://pypi.org/project/anthropic)
  * `groq` — installs `groq` [PyPI ↗](https://pypi.org/project/groq)
  * `mistral` — installs `mistralai` [PyPI ↗](https://pypi.org/project/mistralai)
  * `cohere` - installs `cohere` [PyPI ↗](https://pypi.org/project/cohere)



See the [models](../models/) documentation for information on which optional dependencies are required for each model.

You can also install dependencies for multiple models and use cases, for example:

[pip](#__tabbed_5_1)[uv](#__tabbed_5_2)

```
pipinstall'pydantic-ai-slim[openai,vertexai,logfire]'

```


```
uvadd'pydantic-ai-slim[openai,vertexai,logfire]'

```


© Pydantic Services Inc. 2024 to present 
