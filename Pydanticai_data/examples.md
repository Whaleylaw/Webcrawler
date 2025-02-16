---
url: https://ai.pydantic.dev/examples/
title: Untitled
date_crawled: 
---

[ Skip to content ](#examples)

[ ![logo](../img/logo-white.svg) ](.. "PydanticAI")

PydanticAI 

Examples 

Type to start searching

[ pydantic/pydantic-ai  ](https://github.com/pydantic/pydantic-ai "Go to repository")

[ ![logo](../img/logo-white.svg) ](.. "PydanticAI") PydanticAI 

[ pydantic/pydantic-ai  ](https://github.com/pydantic/pydantic-ai "Go to repository")

  * [ Introduction  ](..)
  * [ Installation  ](../install/)
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
  * [ Examples  ](./)

Examples 
    * [ Pydantic Model  ](pydantic-model/)
    * [ Weather agent  ](weather-agent/)
    * [ Bank support  ](bank-support/)
    * [ SQL Generation  ](sql-gen/)
    * [ Flight booking  ](flight-booking/)
    * [ RAG  ](rag/)
    * [ Stream markdown  ](stream-markdown/)
    * [ Stream whales  ](stream-whales/)
    * [ Chat App with FastAPI  ](chat-app/)
    * [ Question Graph  ](question-graph/)
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

  * [ Usage  ](#usage)
    * [ Installing required dependencies  ](#installing-required-dependencies)
    * [ Setting model environment variables  ](#setting-model-environment-variables)
    * [ Running Examples  ](#running-examples)



  1. [ Introduction  ](..)
  2. [ Examples  ](./)



Version Notice

This documentation is ahead of the last release by [6 commits](https://github.com/pydantic/pydantic-ai/compare/v0.0.24...main). You may see documentation for features not yet supported in the latest release [v0.0.24 2025-02-12](https://github.com/pydantic/pydantic-ai/releases/tag/v0.0.24). 

# Examples

Examples of how to use PydanticAI and what it can do.

## Usage

These examples are distributed with `pydantic-ai` so you can run them either by cloning the [pydantic-ai repo](https://github.com/pydantic/pydantic-ai) or by simply installing `pydantic-ai` from PyPI with `pip` or `uv`.

### Installing required dependencies

Either way you'll need to install extra dependencies to run some examples, you just need to install the `examples` optional dependency group.

If you've installed `pydantic-ai` via pip/uv, you can install the extra dependencies with:

[pip](#__tabbed_1_1)[uv](#__tabbed_1_2)

```
pipinstall'pydantic-ai[examples]'

```


```
uvadd'pydantic-ai[examples]'

```


If you clone the repo, you should instead use `uv sync --extra examples` to install extra dependencies.

### Setting model environment variables

These examples will need you to set up authentication with one or more of the LLMs, see the [model configuration](../models/) docs for details on how to do this.

TL;DR: in most cases you'll need to set one of the following environment variables:

[OpenAI](#__tabbed_2_1)[Google Gemini](#__tabbed_2_2)

```
exportOPENAI_API_KEY=your-api-key

```


```
exportGEMINI_API_KEY=your-api-key

```


### Running Examples

To run the examples (this will work whether you installed `pydantic_ai`, or cloned the repo), run:

[pip](#__tabbed_3_1)[uv](#__tabbed_3_2)

```
python-mpydantic_ai_examples.<example_module_name>

```


```
uvrun-mpydantic_ai_examples.<example_module_name>

```


For examples, to run the very simple `pydantic_model`[](pydantic-model/) example:

[pip](#__tabbed_4_1)[uv](#__tabbed_4_2)

```
python-mpydantic_ai_examples.pydantic_model

```


```
uvrun-mpydantic_ai_examples.pydantic_model

```


If you like one-liners and you're using uv, you can run a pydantic-ai example with zero setup:

```
OPENAI_API_KEY='your-api-key'\
uvrun--with'pydantic-ai[examples]'\
-mpydantic_ai_examples.pydantic_model

```


You'll probably want to edit examples in addition to just running them. You can copy the examples to a new directory with:

[pip](#__tabbed_5_1)[uv](#__tabbed_5_2)

```
python-mpydantic_ai_examples--copy-toexamples/

```


```
uvrun-mpydantic_ai_examples--copy-toexamples/

```


© Pydantic Services Inc. 2024 to present 
