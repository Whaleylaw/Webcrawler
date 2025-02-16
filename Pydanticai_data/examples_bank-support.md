---
url: https://ai.pydantic.dev/examples/bank-support/
title: Untitled
date_crawled: 
---

[ Skip to content ](#running-the-example)

[ ![logo](../../img/logo-white.svg) ](../.. "PydanticAI")

PydanticAI 

Bank support 

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
    * Bank support  [ Bank support  ](./) Table of contents 
      * [ Running the Example  ](#running-the-example)
      * [ Example Code  ](#example-code)
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

# Bank support

Small but complete example of using PydanticAI to build a support agent for a bank.

Demonstrates:

  * [dynamic system prompt](../../agents/#system-prompts)
  * [structured `result_type`](../../results/#structured-result-validation)
  * [tools](../../tools/)



## Running the Example

With [dependencies installed and environment variables set](../#usage), run:

[pip](#__tabbed_1_1)[uv](#__tabbed_1_2)

```
python-mpydantic_ai_examples.bank_support

```


```
uvrun-mpydantic_ai_examples.bank_support

```


(or `PYDANTIC_AI_MODEL=gemini-1.5-flash ...`)

## Example Code

bank_support.py```
from dataclasses import dataclass
from pydantic import BaseModel, Field
from pydantic_ai import Agent, RunContext

class DatabaseConn:
"""This is a fake database for example purposes.
  In reality, you'd be connecting to an external database
  (e.g. PostgreSQL) to get information about customers.
  """
  @classmethod
  async def customer_name(cls, *, id: int) -> str | None:
    if id == 123:
      return 'John'
  @classmethod
  async def customer_balance(cls, *, id: int, include_pending: bool) -> float:
    if id == 123 and include_pending:
      return 123.45
    else:
      raise ValueError('Customer not found')

@dataclass
class SupportDependencies:
  customer_id: int
  db: DatabaseConn

class SupportResult(BaseModel):
  support_advice: str = Field(description='Advice returned to the customer')
  block_card: bool = Field(description='Whether to block their card or not')
  risk: int = Field(description='Risk level of query', ge=0, le=10)

support_agent = Agent(
  'openai:gpt-4o',
  deps_type=SupportDependencies,
  result_type=SupportResult,
  system_prompt=(
    'You are a support agent in our bank, give the '
    'customer support and judge the risk level of their query. '
    "Reply using the customer's name."
  ),
)

@support_agent.system_prompt
async def add_customer_name(ctx: RunContext[SupportDependencies]) -> str:
  customer_name = await ctx.deps.db.customer_name(id=ctx.deps.customer_id)
  return f"The customer's name is {customer_name!r}"

@support_agent.tool
async def customer_balance(
  ctx: RunContext[SupportDependencies], include_pending: bool
) -> str:
"""Returns the customer's current account balance."""
  balance = await ctx.deps.db.customer_balance(
    id=ctx.deps.customer_id,
    include_pending=include_pending,
  )
  return f'${balance:.2f}'

if __name__ == '__main__':
  deps = SupportDependencies(customer_id=123, db=DatabaseConn())
  result = support_agent.run_sync('What is my balance?', deps=deps)
  print(result.data)
"""
  support_advice='Hello John, your current account balance, including pending transactions, is $123.45.' block_card=False risk=1
  """
  result = support_agent.run_sync('I just lost my card!', deps=deps)
  print(result.data)
"""
  support_advice="I'm sorry to hear that, John. We are temporarily blocking your card to prevent unauthorized transactions." block_card=True risk=8
  """

```


© Pydantic Services Inc. 2024 to present 
