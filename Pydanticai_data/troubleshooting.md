---
url: https://ai.pydantic.dev/troubleshooting/
title: Untitled
date_crawled: 
---

[ Skip to content ](#troubleshooting)

[ ![logo](../img/logo-white.svg) ](.. "PydanticAI")

PydanticAI 

Troubleshooting 

Type to start searching

[ pydantic/pydantic-ai  ](https://github.com/pydantic/pydantic-ai "Go to repository")

[ ![logo](../img/logo-white.svg) ](.. "PydanticAI") PydanticAI 

[ pydantic/pydantic-ai  ](https://github.com/pydantic/pydantic-ai "Go to repository")

  * [ Introduction  ](..)
  * [ Installation  ](../install/)
  * [ Getting Help  ](../help/)
  * [ Contributing  ](../contributing/)
  * Troubleshooting  [ Troubleshooting  ](./) Table of contents 
    * [ Jupyter Notebook Errors  ](#jupyter-notebook-errors)
      * [ RuntimeError: This event loop is already running  ](#runtimeerror-this-event-loop-is-already-running)
    * [ API Key Configuration  ](#api-key-configuration)
      * [ UserError: API key must be provided or set in the [MODEL]_API_KEY environment variable  ](#usererror-api-key-must-be-provided-or-set-in-the-model_api_key-environment-variable)
    * [ Monitoring HTTPX Requests  ](#monitoring-httpx-requests)
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

  * [ Jupyter Notebook Errors  ](#jupyter-notebook-errors)
    * [ RuntimeError: This event loop is already running  ](#runtimeerror-this-event-loop-is-already-running)
  * [ API Key Configuration  ](#api-key-configuration)
    * [ UserError: API key must be provided or set in the [MODEL]_API_KEY environment variable  ](#usererror-api-key-must-be-provided-or-set-in-the-model_api_key-environment-variable)
  * [ Monitoring HTTPX Requests  ](#monitoring-httpx-requests)



Version Notice

This documentation is ahead of the last release by [6 commits](https://github.com/pydantic/pydantic-ai/compare/v0.0.24...main). You may see documentation for features not yet supported in the latest release [v0.0.24 2025-02-12](https://github.com/pydantic/pydantic-ai/releases/tag/v0.0.24). 

# Troubleshooting

Below are suggestions on how to fix some common errors you might encounter while using PydanticAI. If the issue you're experiencing is not listed below or addressed in the documentation, please feel free to ask in the [Pydantic Slack](../help/) or create an issue on [GitHub](https://github.com/pydantic/pydantic-ai/issues).

## Jupyter Notebook Errors

### `RuntimeError: This event loop is already running`

This error is caused by conflicts between the event loops in Jupyter notebook and PydanticAI's. One way to manage these conflicts is by using `nest-asyncio`[](https://pypi.org/project/nest-asyncio/). Namely, before you execute any agent runs, do the following: 

```
import nest_asyncio
nest_asyncio.apply()

```


Note: This fix also applies to Google Colab. 

## API Key Configuration

### `UserError: API key must be provided or set in the [MODEL]_API_KEY environment variable`

If you're running into issues with setting the API key for your model, visit the [Models](../models/) page to learn more about how to set an environment variable and/or pass in an `api_key` argument.

## Monitoring HTTPX Requests

You can use custom `httpx` clients in your models in order to access specific requests, responses, and headers at runtime.

It's particularly helpful to use `logfire`'s [HTTPX integration](../logfire/#monitoring-httpx-requests) to monitor the above.

© Pydantic Services Inc. 2024 to present 
