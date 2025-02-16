---
url: https://ai.pydantic.dev/logfire/
title: Untitled
date_crawled: 
---

[ Skip to content ](#debugging-and-monitoring)

[ ![logo](../img/logo-white.svg) ](.. "PydanticAI")

PydanticAI 

Debugging and Monitoring 

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
    * Debugging and Monitoring  [ Debugging and Monitoring  ](./) Table of contents 
      * [ Pydantic Logfire  ](#pydantic-logfire)
      * [ Using Logfire  ](#using-logfire)
        * [ Debugging  ](#debugging)
        * [ Monitoring Performance  ](#monitoring-performance)
        * [ Monitoring HTTPX Requests  ](#monitoring-httpx-requests)
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

  * [ Pydantic Logfire  ](#pydantic-logfire)
  * [ Using Logfire  ](#using-logfire)
    * [ Debugging  ](#debugging)
    * [ Monitoring Performance  ](#monitoring-performance)
    * [ Monitoring HTTPX Requests  ](#monitoring-httpx-requests)



  1. [ Introduction  ](..)
  2. [ Documentation  ](../agents/)



Version Notice

This documentation is ahead of the last release by [6 commits](https://github.com/pydantic/pydantic-ai/compare/v0.0.24...main). You may see documentation for features not yet supported in the latest release [v0.0.24 2025-02-12](https://github.com/pydantic/pydantic-ai/releases/tag/v0.0.24). 

# Debugging and Monitoring

Applications that use LLMs have some challenges that are well known and understood: LLMs are **slow** , **unreliable** and **expensive**.

These applications also have some challenges that most developers have encountered much less often: LLMs are **fickle** and **non-deterministic**. Subtle changes in a prompt can completely change a model's performance, and there's no `EXPLAIN` query you can run to understand why.

Warning

From a software engineers point of view, you can think of LLMs as the worst database you've ever heard of, but worse.

If LLMs weren't so bloody useful, we'd never touch them.

To build successful applications with LLMs, we need new tools to understand both model performance, and the behavior of applications that rely on them.

LLM Observability tools that just let you understand how your model is performing are useless: making API calls to an LLM is easy, it's building that into an application that's hard.

## Pydantic Logfire

[Pydantic Logfire](https://pydantic.dev/logfire) is an observability platform developed by the team who created and maintain Pydantic and PydanticAI. Logfire aims to let you understand your entire application: Gen AI, classic predictive AI, HTTP traffic, database queries and everything else a modern application needs.

Pydantic Logfire is a commercial product

Logfire is a commercially supported, hosted platform with an extremely generous and perpetual [free tier](https://pydantic.dev/pricing/). You can sign up and start using Logfire in a couple of minutes.

PydanticAI has built-in (but optional) support for Logfire via the `logfire-api`[](https://github.com/pydantic/logfire/tree/main/logfire-api) no-op package.

That means if the `logfire` package is installed and configured, detailed information about agent runs is sent to Logfire. But if the `logfire` package is not installed, there's virtually no overhead and nothing is sent.

Here's an example showing details of running the [Weather Agent](../examples/weather-agent/) in Logfire:

[![Weather Agent Logfire](../img/logfire-weather-agent.png)](../img/logfire-weather-agent.png)

## Using Logfire

To use logfire, you'll need a logfire [account](https://logfire.pydantic.dev), and logfire installed:

[pip](#__tabbed_1_1)[uv](#__tabbed_1_2)

```
pipinstall'pydantic-ai[logfire]'

```


```
uvadd'pydantic-ai[logfire]'

```


Then authenticate your local environment with logfire:

[pip](#__tabbed_2_1)[uv](#__tabbed_2_2)

```
logfireauth

```


```
uvrunlogfireauth

```


And configure a project to send data to:

[pip](#__tabbed_3_1)[uv](#__tabbed_3_2)

```
logfireprojectsnew

```


```
uvrunlogfireprojectsnew

```


(Or use an existing project with `logfire projects use`)

The last step is to add logfire to your code:

adding_logfire.py```
import logfire
logfire.configure()

```


The [logfire documentation](https://logfire.pydantic.dev/docs/) has more details on how to use logfire, including how to instrument other libraries like [Pydantic](https://logfire.pydantic.dev/docs/integrations/pydantic/), [HTTPX](https://logfire.pydantic.dev/docs/integrations/http-clients/httpx/) and [FastAPI](https://logfire.pydantic.dev/docs/integrations/web-frameworks/fastapi/).

Since Logfire is build on [OpenTelemetry](https://opentelemetry.io/), you can use the Logfire Python SDK to send data to any OpenTelemetry collector.

Once you have logfire set up, there are two primary ways it can help you understand your application:

  * **Debugging** — Using the live view to see what's happening in your application in real-time.
  * **Monitoring** — Using SQL and dashboards to observe the behavior of your application, Logfire is effectively a SQL database that stores information about how your application is running.



### Debugging

To demonstrate how Logfire can let you visualise the flow of a PydanticAI run, here's the view you get from Logfire while running the [chat app examples](../examples/chat-app/):

### Monitoring Performance

We can also query data with SQL in Logfire to monitor the performance of an application. Here's a real world example of using Logfire to monitor PydanticAI runs inside Logfire itself:

[![Logfire monitoring PydanticAI](../img/logfire-monitoring-pydanticai.png)](../img/logfire-monitoring-pydanticai.png)

### Monitoring HTTPX Requests

In order to monitor HTTPX requests made by models, you can use `logfire`'s [HTTPX](https://logfire.pydantic.dev/docs/integrations/http-clients/httpx/) integration.

Instrumentation is as easy as adding the following three lines to your application:

instrument_httpx.py```
import logfire
logfire.configure()
logfire.instrument_httpx(capture_all=True) [](#__code_7_annotation_1)

```


In particular, this can help you to trace specific requests, responses, and headers:

instrument_httpx_example.py```
import logfire
from pydantic_ai import Agent
logfire.configure()
logfire.instrument_httpx(capture_all=True) [](#__code_8_annotation_1)
agent = Agent('openai:gpt-4o')
result = agent.run_sync('What is the capital of France?')
print(result.data)
#> The capital of France is Paris.

```


[With `httpx` instrumentation](#__tabbed_4_1)[Without `httpx` instrumentation](#__tabbed_4_2)

[![Logfire with HTTPX instrumentation](../img/logfire-with-httpx.png)](../img/logfire-with-httpx.png)

[![Logfire without HTTPX instrumentation](../img/logfire-without-httpx.png)](../img/logfire-without-httpx.png)

Tip

`httpx` instrumentation might be of particular utility if you're using a custom `httpx` client in your model in order to get insights into your custom requests.

© Pydantic Services Inc. 2024 to present 
