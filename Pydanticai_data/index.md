---
url: https://ai.pydantic.dev/
title: Untitled
date_crawled: 
---

[ Skip to content ](#introduction)

[ ![logo](img/logo-white.svg) ](. "PydanticAI")

PydanticAI 

Introduction 

Type to start searching

[ pydantic/pydantic-ai  ](https://github.com/pydantic/pydantic-ai "Go to repository")

[ ![logo](img/logo-white.svg) ](. "PydanticAI") PydanticAI 

[ pydantic/pydantic-ai  ](https://github.com/pydantic/pydantic-ai "Go to repository")

  * Introduction  [ Introduction  ](.) Table of contents 
    * [ Why use PydanticAI  ](#why-use-pydanticai)
    * [ Hello World Example  ](#hello-world-example)
    * [ Tools & Dependency Injection Example  ](#tools-dependency-injection-example)
    * [ Instrumentation with Pydantic Logfire  ](#instrumentation-with-pydantic-logfire)
    * [ Next Steps  ](#next-steps)
  * [ Installation  ](install/)
  * [ Getting Help  ](help/)
  * [ Contributing  ](contributing/)
  * [ Troubleshooting  ](troubleshooting/)
  * Documentation  Documentation 
    * [ Agents  ](agents/)
    * [ Models  ](models/)
    * [ Dependencies  ](dependencies/)
    * [ Function Tools  ](tools/)
    * [ Results  ](results/)
    * [ Messages and chat history  ](message-history/)
    * [ Testing and Evals  ](testing-evals/)
    * [ Debugging and Monitoring  ](logfire/)
    * [ Multi-agent Applications  ](multi-agent-applications/)
    * [ Graphs  ](graph/)
  * [ Examples  ](examples/)

Examples 
    * [ Pydantic Model  ](examples/pydantic-model/)
    * [ Weather agent  ](examples/weather-agent/)
    * [ Bank support  ](examples/bank-support/)
    * [ SQL Generation  ](examples/sql-gen/)
    * [ Flight booking  ](examples/flight-booking/)
    * [ RAG  ](examples/rag/)
    * [ Stream markdown  ](examples/stream-markdown/)
    * [ Stream whales  ](examples/stream-whales/)
    * [ Chat App with FastAPI  ](examples/chat-app/)
    * [ Question Graph  ](examples/question-graph/)
  * API Reference  API Reference 
    * [ pydantic_ai.agent  ](api/agent/)
    * [ pydantic_ai.tools  ](api/tools/)
    * [ pydantic_ai.result  ](api/result/)
    * [ pydantic_ai.messages  ](api/messages/)
    * [ pydantic_ai.exceptions  ](api/exceptions/)
    * [ pydantic_ai.settings  ](api/settings/)
    * [ pydantic_ai.usage  ](api/usage/)
    * [ pydantic_ai.format_as_xml  ](api/format_as_xml/)
    * [ pydantic_ai.models  ](api/models/base/)
    * [ pydantic_ai.models.openai  ](api/models/openai/)
    * [ pydantic_ai.models.anthropic  ](api/models/anthropic/)
    * [ pydantic_ai.models.cohere  ](api/models/cohere/)
    * [ pydantic_ai.models.gemini  ](api/models/gemini/)
    * [ pydantic_ai.models.vertexai  ](api/models/vertexai/)
    * [ pydantic_ai.models.groq  ](api/models/groq/)
    * [ pydantic_ai.models.mistral  ](api/models/mistral/)
    * [ pydantic_ai.models.test  ](api/models/test/)
    * [ pydantic_ai.models.function  ](api/models/function/)
    * [ pydantic_graph  ](api/pydantic_graph/graph/)
    * [ pydantic_graph.nodes  ](api/pydantic_graph/nodes/)
    * [ pydantic_graph.state  ](api/pydantic_graph/state/)
    * [ pydantic_graph.mermaid  ](api/pydantic_graph/mermaid/)
    * [ pydantic_graph.exceptions  ](api/pydantic_graph/exceptions/)



Table of contents 

  * [ Why use PydanticAI  ](#why-use-pydanticai)
  * [ Hello World Example  ](#hello-world-example)
  * [ Tools & Dependency Injection Example  ](#tools-dependency-injection-example)
  * [ Instrumentation with Pydantic Logfire  ](#instrumentation-with-pydantic-logfire)
  * [ Next Steps  ](#next-steps)



Version Notice

This documentation is ahead of the last release by [6 commits](https://github.com/pydantic/pydantic-ai/compare/v0.0.24...main). You may see documentation for features not yet supported in the latest release [v0.0.24 2025-02-12](https://github.com/pydantic/pydantic-ai/releases/tag/v0.0.24). 

# Introduction

![PydanticAI](./img/pydantic-ai-dark.svg#only-dark)

![PydanticAI](./img/pydantic-ai-light.svg#only-light)

_Agent Framework / shim to use Pydantic with LLMs_

[ ![CI](https://github.com/pydantic/pydantic-ai/actions/workflows/ci.yml/badge.svg?event=push) ](https://github.com/pydantic/pydantic-ai/actions/workflows/ci.yml?query=branch%3Amain) [ ![Coverage](https://coverage-badge.samuelcolvin.workers.dev/pydantic/pydantic-ai.svg) ](https://coverage-badge.samuelcolvin.workers.dev/redirect/pydantic/pydantic-ai) [ ![PyPI](https://img.shields.io/pypi/v/pydantic-ai.svg) ](https://pypi.python.org/pypi/pydantic-ai) [ ![versions](https://img.shields.io/pypi/pyversions/pydantic-ai.svg) ](https://github.com/pydantic/pydantic-ai) [ ![license](https://img.shields.io/github/license/pydantic/pydantic-ai.svg) ](https://github.com/pydantic/pydantic-ai/blob/main/LICENSE)

PydanticAI is a Python agent framework designed to make it less painful to build production grade applications with Generative AI. 

PydanticAI is a Python Agent Framework designed to make it less painful to build production grade applications with Generative AI.

FastAPI revolutionized web development by offering an innovative and ergonomic design, built on the foundation of [Pydantic](https://docs.pydantic.dev).

Similarly, virtually every agent framework and LLM library in Python uses Pydantic, yet when we began to use LLMs in [Pydantic Logfire](https://pydantic.dev/logfire), we couldn't find anything that gave us the same feeling.

We built PydanticAI with one simple aim: to bring that FastAPI feeling to GenAI app development.

## Why use PydanticAI

  * **Built by the Pydantic Team** : Built by the team behind [Pydantic](https://docs.pydantic.dev/latest/) (the validation layer of the OpenAI SDK, the Anthropic SDK, LangChain, LlamaIndex, AutoGPT, Transformers, CrewAI, Instructor and many more).

  * **Model-agnostic** : Supports OpenAI, Anthropic, Gemini, Deepseek, Ollama, Groq, Cohere, and Mistral, and there is a simple interface to implement support for [other models](models/).

  * **Pydantic Logfire Integration** : Seamlessly [integrates](logfire/) with [Pydantic Logfire](https://pydantic.dev/logfire) for real-time debugging, performance monitoring, and behavior tracking of your LLM-powered applications.

  * **Type-safe** : Designed to make [type checking](agents/#static-type-checking) as powerful and informative as possible for you.

  * **Python-centric Design** : Leverages Python's familiar control flow and agent composition to build your AI-driven projects, making it easy to apply standard Python best practices you'd use in any other (non-AI) project.

  * **Structured Responses** : Harnesses the power of [Pydantic](https://docs.pydantic.dev/latest/) to [validate and structure](results/#structured-result-validation) model outputs, ensuring responses are consistent across runs.

  * **Dependency Injection System** : Offers an optional [dependency injection](dependencies/) system to provide data and services to your agent's [system prompts](agents/#system-prompts), [tools](tools/) and [result validators](results/#result-validators-functions). This is useful for testing and eval-driven iterative development.

  * **Streamed Responses** : Provides the ability to [stream](results/#streamed-results) LLM outputs continuously, with immediate validation, ensuring rapid and accurate results.

  * **Graph Support** : [Pydantic Graph](graph/) provides a powerful way to define graphs using typing hints, this is useful in complex applications where standard control flow can degrade to spaghetti code.




In Beta

PydanticAI is in early beta, the API is still subject to change and there's a lot more to do. [Feedback](https://github.com/pydantic/pydantic-ai/issues) is very welcome!

## Hello World Example

Here's a minimal example of PydanticAI:

hello_world.py```
from pydantic_ai import Agent
agent = Agent( [](#__code_0_annotation_1)
  'google-gla:gemini-1.5-flash',
  system_prompt='Be concise, reply with one sentence.', [](#__code_0_annotation_2)
)
result = agent.run_sync('Where does "hello world" come from?') [](#__code_0_annotation_3)
print(result.data)
"""
The first known use of "hello, world" was in a 1974 textbook about the C programming language.
"""

```


_(This example is complete, it can be run "as is")_

The exchange should be very short: PydanticAI will send the system prompt and the user query to the LLM, the model will return a text response.

Not very interesting yet, but we can easily add "tools", dynamic system prompts, and structured responses to build more powerful agents.

## Tools & Dependency Injection Example

Here is a concise example using PydanticAI to build a support agent for a bank:

bank_support.py```
from dataclasses import dataclass
from pydantic import BaseModel, Field
from pydantic_ai import Agent, RunContext
from bank_database import DatabaseConn

@dataclass
class SupportDependencies: [](#__code_1_annotation_3)
  customer_id: int
  db: DatabaseConn [](#__code_1_annotation_12)

class SupportResult(BaseModel): [](#__code_1_annotation_13)
  support_advice: str = Field(description='Advice returned to the customer')
  block_card: bool = Field(description="Whether to block the customer's card")
  risk: int = Field(description='Risk level of query', ge=0, le=10)

support_agent = Agent( [](#__code_1_annotation_1)
  'openai:gpt-4o', [](#__code_1_annotation_2)
  deps_type=SupportDependencies,
  result_type=SupportResult, [](#__code_1_annotation_9)
  system_prompt=( [](#__code_1_annotation_4)
    'You are a support agent in our bank, give the '
    'customer support and judge the risk level of their query.'
  ),
)

@support_agent.system_prompt [](#__code_1_annotation_5)
async def add_customer_name(ctx: RunContext[SupportDependencies]) -> str:
  customer_name = await ctx.deps.db.customer_name(id=ctx.deps.customer_id)
  return f"The customer's name is {customer_name!r}"

@support_agent.tool [](#__code_1_annotation_6)
async def customer_balance(
  ctx: RunContext[SupportDependencies], include_pending: bool
) -> float:
"""Returns the customer's current account balance.""" [](#__code_1_annotation_7)
  return await ctx.deps.db.customer_balance(
    id=ctx.deps.customer_id,
    include_pending=include_pending,
  )

... [](#__code_1_annotation_11)

async def main():
  deps = SupportDependencies(customer_id=123, db=DatabaseConn())
  result = await support_agent.run('What is my balance?', deps=deps) [](#__code_1_annotation_8)
  print(result.data) [](#__code_1_annotation_10)
"""
  support_advice='Hello John, your current account balance, including pending transactions, is $123.45.' block_card=False risk=1
  """
  result = await support_agent.run('I just lost my card!', deps=deps)
  print(result.data)
"""
  support_advice="I'm sorry to hear that, John. We are temporarily blocking your card to prevent unauthorized transactions." block_card=True risk=8
  """

```


Complete `bank_support.py` example

The code included here is incomplete for the sake of brevity (the definition of `DatabaseConn` is missing); you can find the complete `bank_support.py` example [here](examples/bank-support/).

## Instrumentation with Pydantic Logfire

To understand the flow of the above runs, we can watch the agent in action using Pydantic Logfire.

To do this, we need to set up logfire, and add the following to our code:

bank_support_with_logfire.py```
...
from bank_database import DatabaseConn
import logfire
logfire.configure() [](#__code_2_annotation_1)
logfire.instrument_asyncpg() [](#__code_2_annotation_2)
...

```


That's enough to get the following view of your agent in action:

See [Monitoring and Performance](logfire/) to learn more.

## Next Steps

To try PydanticAI yourself, follow the instructions [in the examples](examples/).

Read the [docs](agents/) to learn more about building applications with PydanticAI.

Read the [API Reference](api/agent/) to understand PydanticAI's interface.

© Pydantic Services Inc. 2024 to present 
