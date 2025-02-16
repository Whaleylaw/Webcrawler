---
url: https://ai.pydantic.dev/examples/question-graph/
title: Untitled
date_crawled: 
---

[ Skip to content ](#question-graph)

[ ![logo](../../img/logo-white.svg) ](../.. "PydanticAI")

PydanticAI 

Question Graph 

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
    * [ Stream whales  ](../stream-whales/)
    * [ Chat App with FastAPI  ](../chat-app/)
    * Question Graph  [ Question Graph  ](./) Table of contents 
      * [ Running the Example  ](#running-the-example)
      * [ Example Code  ](#example-code)
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

# Question Graph

Example of a graph for asking and evaluating questions.

Demonstrates:

  * `pydantic_graph`[](../../graph/)



## Running the Example

With [dependencies installed and environment variables set](../#usage), run:

[pip](#__tabbed_1_1)[uv](#__tabbed_1_2)

```
python-mpydantic_ai_examples.question_graph

```


```
uvrun-mpydantic_ai_examples.question_graph

```


## Example Code

question_graph.py```
from __future__ import annotations as _annotations
from dataclasses import dataclass, field
from pathlib import Path
from typing import Annotated
import logfire
from devtools import debug
from pydantic_graph import BaseNode, Edge, End, Graph, GraphRunContext, HistoryStep
from pydantic_ai import Agent
from pydantic_ai.format_as_xml import format_as_xml
from pydantic_ai.messages import ModelMessage
# 'if-token-present' means nothing will be sent (and the example will work) if you don't have logfire configured
logfire.configure(send_to_logfire='if-token-present')
ask_agent = Agent('openai:gpt-4o', result_type=str)

@dataclass
class QuestionState:
  question: str | None = None
  ask_agent_messages: list[ModelMessage] = field(default_factory=list)
  evaluate_agent_messages: list[ModelMessage] = field(default_factory=list)

@dataclass
class Ask(BaseNode[QuestionState]):
  async def run(self, ctx: GraphRunContext[QuestionState]) -> Answer:
    result = await ask_agent.run(
      'Ask a simple question with a single correct answer.',
      message_history=ctx.state.ask_agent_messages,
    )
    ctx.state.ask_agent_messages += result.all_messages()
    ctx.state.question = result.data
    return Answer()

@dataclass
class Answer(BaseNode[QuestionState]):
  answer: str | None = None
  async def run(self, ctx: GraphRunContext[QuestionState]) -> Evaluate:
    assert self.answer is not None
    return Evaluate(self.answer)

@dataclass
class EvaluationResult:
  correct: bool
  comment: str

evaluate_agent = Agent(
  'openai:gpt-4o',
  result_type=EvaluationResult,
  system_prompt='Given a question and answer, evaluate if the answer is correct.',
)

@dataclass
class Evaluate(BaseNode[QuestionState]):
  answer: str
  async def run(
    self,
    ctx: GraphRunContext[QuestionState],
  ) -> Congratulate | Reprimand:
    assert ctx.state.question is not None
    result = await evaluate_agent.run(
      format_as_xml({'question': ctx.state.question, 'answer': self.answer}),
      message_history=ctx.state.evaluate_agent_messages,
    )
    ctx.state.evaluate_agent_messages += result.all_messages()
    if result.data.correct:
      return Congratulate(result.data.comment)
    else:
      return Reprimand(result.data.comment)

@dataclass
class Congratulate(BaseNode[QuestionState, None, None]):
  comment: str
  async def run(
    self, ctx: GraphRunContext[QuestionState]
  ) -> Annotated[End, Edge(label='success')]:
    print(f'Correct answer! {self.comment}')
    return End(None)

@dataclass
class Reprimand(BaseNode[QuestionState]):
  comment: str
  async def run(self, ctx: GraphRunContext[QuestionState]) -> Ask:
    print(f'Comment: {self.comment}')
    # > Comment: Vichy is no longer the capital of France.
    ctx.state.question = None
    return Ask()

question_graph = Graph(
  nodes=(Ask, Answer, Evaluate, Congratulate, Reprimand), state_type=QuestionState
)

async def run_as_continuous():
  state = QuestionState()
  node = Ask()
  history: list[HistoryStep[QuestionState, None]] = []
  with logfire.span('run questions graph'):
    while True:
      node = await question_graph.next(node, history, state=state)
      if isinstance(node, End):
        debug([e.data_snapshot() for e in history])
        break
      elif isinstance(node, Answer):
        assert state.question
        node.answer = input(f'{state.question} ')
      # otherwise just continue

async def run_as_cli(answer: str | None):
  history_file = Path('question_graph_history.json')
  history = (
    question_graph.load_history(history_file.read_bytes())
    if history_file.exists()
    else []
  )
  if history:
    last = history[-1]
    assert last.kind == 'node', 'expected last step to be a node'
    state = last.state
    assert answer is not None, 'answer is required to continue from history'
    node = Answer(answer)
  else:
    state = QuestionState()
    node = Ask()
  debug(state, node)
  with logfire.span('run questions graph'):
    while True:
      node = await question_graph.next(node, history, state=state)
      if isinstance(node, End):
        debug([e.data_snapshot() for e in history])
        print('Finished!')
        break
      elif isinstance(node, Answer):
        print(state.question)
        break
      # otherwise just continue
  history_file.write_bytes(question_graph.dump_history(history, indent=2))

if __name__ == '__main__':
  import asyncio
  import sys
  try:
    sub_command = sys.argv[1]
    assert sub_command in ('continuous', 'cli', 'mermaid')
  except (IndexError, AssertionError):
    print(
      'Usage:\n'
      ' uv run -m pydantic_ai_examples.question_graph mermaid\n'
      'or:\n'
      ' uv run -m pydantic_ai_examples.question_graph continuous\n'
      'or:\n'
      ' uv run -m pydantic_ai_examples.question_graph cli [answer]',
      file=sys.stderr,
    )
    sys.exit(1)
  if sub_command == 'mermaid':
    print(question_graph.mermaid_code(start_node=Ask))
  elif sub_command == 'continuous':
    asyncio.run(run_as_continuous())
  else:
    a = sys.argv[2] if len(sys.argv) > 2 else None
    asyncio.run(run_as_cli(a))

```


The mermaid diagram generated in this example looks like this:

```
---
title: question_graph
---
stateDiagram-v2
 [*] --> Ask
 Ask --> Answer: ask the question
 Answer --> Evaluate: answer the question
 Evaluate --> Congratulate
 Evaluate --> Castigate
 Congratulate --> [*]: success
 Castigate --> Ask: try again
```


© Pydantic Services Inc. 2024 to present 
