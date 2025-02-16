---
url: https://ai.pydantic.dev/contributing/
title: Untitled
date_crawled: 
---

[ Skip to content ](#installation-and-setup)

[ ![logo](../img/logo-white.svg) ](.. "PydanticAI")

PydanticAI 

Contributing 

Type to start searching

[ pydantic/pydantic-ai  ](https://github.com/pydantic/pydantic-ai "Go to repository")

[ ![logo](../img/logo-white.svg) ](.. "PydanticAI") PydanticAI 

[ pydantic/pydantic-ai  ](https://github.com/pydantic/pydantic-ai "Go to repository")

  * [ Introduction  ](..)
  * [ Installation  ](../install/)
  * [ Getting Help  ](../help/)
  * Contributing  [ Contributing  ](./) Table of contents 
    * [ Installation and Setup  ](#installation-and-setup)
    * [ Running Tests etc.  ](#running-tests-etc)
    * [ Documentation Changes  ](#documentation-changes)
    * [ Rules for adding new models to PydanticAI  ](#new-model-rules)
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

  * [ Installation and Setup  ](#installation-and-setup)
  * [ Running Tests etc.  ](#running-tests-etc)
  * [ Documentation Changes  ](#documentation-changes)
  * [ Rules for adding new models to PydanticAI  ](#new-model-rules)



Version Notice

This documentation is ahead of the last release by [6 commits](https://github.com/pydantic/pydantic-ai/compare/v0.0.24...main). You may see documentation for features not yet supported in the latest release [v0.0.24 2025-02-12](https://github.com/pydantic/pydantic-ai/releases/tag/v0.0.24). 

# Contributing

We'd love you to contribute to PydanticAI!

## Installation and Setup

Clone your fork and cd into the repo directory

```
gitclonegit@github.com:<yourusername>/pydantic-ai.git
cdpydantic-ai

```


Install `uv` (version 0.4.30 or later) and `pre-commit`

We use pipx here, for other options see:

  * `uv`[ install docs](https://docs.astral.sh/uv/getting-started/installation/)
  * `pre-commit`[ install docs](https://pre-commit.com/#install)



To get `pipx` itself, see [these docs](https://pypa.github.io/pipx/)

```
pipxinstalluvpre-commit

```


Install `pydantic-ai`, all dependencies and pre-commit hooks

```
makeinstall

```


## Running Tests etc.

We use `make` to manage most commands you'll need to run.

For details on available commands, run:

```
makehelp

```


To run code formatting, linting, static type checks, and tests with coverage report generation, run:

```
make

```


## Documentation Changes

To run the documentation page locally, run:

```
uvrunmkdocsserve

```


## Rules for adding new models to PydanticAI

To avoid an excessive workload for the maintainers of PydanticAI, we can't accept all model contributions, so we're setting the following rules for when we'll accept new models and when we won't. This should hopefully reduce the chances of disappointment and wasted work.

  * To add a new model with an extra dependency, that dependency needs > 500k monthly downloads from PyPI consistently over 3 months or more
  * To add a new model which uses another models logic internally and has no extra dependencies, that model's GitHub org needs > 20k stars in total
  * For any other model that's just a custom URL and API key, we're happy to add a one-paragraph description with a link and instructions on the URL to use
  * For any other model that requires more logic, we recommend you release your own Python package `pydantic-ai-xxx`, which depends on `pydantic-ai-slim`[](../install/#slim-install) and implements a model that inherits from our `Model`[](../api/models/base/#pydantic_ai.models.Model) ABC



If you're unsure about adding a model, please [create an issue](https://github.com/pydantic/pydantic-ai/issues).

© Pydantic Services Inc. 2024 to present 
