---
url: https://ai.pydantic.dev/api/settings/
title: Untitled
date_crawled: 
---

[ Skip to content ](#pydantic_aisettings)

[ ![logo](../../img/logo-white.svg) ](../.. "PydanticAI")

PydanticAI 

pydantic_ai.settings 

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
  * [ Examples  ](../../examples/)

Examples 
    * [ Pydantic Model  ](../../examples/pydantic-model/)
    * [ Weather agent  ](../../examples/weather-agent/)
    * [ Bank support  ](../../examples/bank-support/)
    * [ SQL Generation  ](../../examples/sql-gen/)
    * [ Flight booking  ](../../examples/flight-booking/)
    * [ RAG  ](../../examples/rag/)
    * [ Stream markdown  ](../../examples/stream-markdown/)
    * [ Stream whales  ](../../examples/stream-whales/)
    * [ Chat App with FastAPI  ](../../examples/chat-app/)
    * [ Question Graph  ](../../examples/question-graph/)
  * API Reference  API Reference 
    * [ pydantic_ai.agent  ](../agent/)
    * [ pydantic_ai.tools  ](../tools/)
    * [ pydantic_ai.result  ](../result/)
    * [ pydantic_ai.messages  ](../messages/)
    * [ pydantic_ai.exceptions  ](../exceptions/)
    * pydantic_ai.settings  [ pydantic_ai.settings  ](./) Table of contents 
      * [ settings  ](#pydantic_ai.settings)
      * [ ModelSettings  ](#pydantic_ai.settings.ModelSettings)
        * [ max_tokens  ](#pydantic_ai.settings.ModelSettings.max_tokens)
        * [ temperature  ](#pydantic_ai.settings.ModelSettings.temperature)
        * [ top_p  ](#pydantic_ai.settings.ModelSettings.top_p)
        * [ timeout  ](#pydantic_ai.settings.ModelSettings.timeout)
        * [ parallel_tool_calls  ](#pydantic_ai.settings.ModelSettings.parallel_tool_calls)
        * [ seed  ](#pydantic_ai.settings.ModelSettings.seed)
        * [ presence_penalty  ](#pydantic_ai.settings.ModelSettings.presence_penalty)
        * [ frequency_penalty  ](#pydantic_ai.settings.ModelSettings.frequency_penalty)
        * [ logit_bias  ](#pydantic_ai.settings.ModelSettings.logit_bias)
    * [ pydantic_ai.usage  ](../usage/)
    * [ pydantic_ai.format_as_xml  ](../format_as_xml/)
    * [ pydantic_ai.models  ](../models/base/)
    * [ pydantic_ai.models.openai  ](../models/openai/)
    * [ pydantic_ai.models.anthropic  ](../models/anthropic/)
    * [ pydantic_ai.models.cohere  ](../models/cohere/)
    * [ pydantic_ai.models.gemini  ](../models/gemini/)
    * [ pydantic_ai.models.vertexai  ](../models/vertexai/)
    * [ pydantic_ai.models.groq  ](../models/groq/)
    * [ pydantic_ai.models.mistral  ](../models/mistral/)
    * [ pydantic_ai.models.test  ](../models/test/)
    * [ pydantic_ai.models.function  ](../models/function/)
    * [ pydantic_graph  ](../pydantic_graph/graph/)
    * [ pydantic_graph.nodes  ](../pydantic_graph/nodes/)
    * [ pydantic_graph.state  ](../pydantic_graph/state/)
    * [ pydantic_graph.mermaid  ](../pydantic_graph/mermaid/)
    * [ pydantic_graph.exceptions  ](../pydantic_graph/exceptions/)



Table of contents 

  * [ settings  ](#pydantic_ai.settings)
  * [ ModelSettings  ](#pydantic_ai.settings.ModelSettings)
    * [ max_tokens  ](#pydantic_ai.settings.ModelSettings.max_tokens)
    * [ temperature  ](#pydantic_ai.settings.ModelSettings.temperature)
    * [ top_p  ](#pydantic_ai.settings.ModelSettings.top_p)
    * [ timeout  ](#pydantic_ai.settings.ModelSettings.timeout)
    * [ parallel_tool_calls  ](#pydantic_ai.settings.ModelSettings.parallel_tool_calls)
    * [ seed  ](#pydantic_ai.settings.ModelSettings.seed)
    * [ presence_penalty  ](#pydantic_ai.settings.ModelSettings.presence_penalty)
    * [ frequency_penalty  ](#pydantic_ai.settings.ModelSettings.frequency_penalty)
    * [ logit_bias  ](#pydantic_ai.settings.ModelSettings.logit_bias)



  1. [ Introduction  ](../..)
  2. [ API Reference  ](../agent/)



Version Notice

This documentation is ahead of the last release by [6 commits](https://github.com/pydantic/pydantic-ai/compare/v0.0.24...main). You may see documentation for features not yet supported in the latest release [v0.0.24 2025-02-12](https://github.com/pydantic/pydantic-ai/releases/tag/v0.0.24). 

# `pydantic_ai.settings`

###  ModelSettings

Bases: `TypedDict[](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypedDict "typing_extensions.TypedDict")`

Settings to configure an LLM.

Here we include only settings which apply to multiple models / model providers, though not all of these settings are supported by all models.

Source code in `pydantic_ai_slim/pydantic_ai/settings.py`

```
 12
 13
 14
 15
 16
 17
 18
 19
 20
 21
 22
 23
 24
 25
 26
 27
 28
 29
 30
 31
 32
 33
 34
 35
 36
 37
 38
 39
 40
 41
 42
 43
 44
 45
 46
 47
 48
 49
 50
 51
 52
 53
 54
 55
 56
 57
 58
 59
 60
 61
 62
 63
 64
 65
 66
 67
 68
 69
 70
 71
 72
 73
 74
 75
 76
 77
 78
 79
 80
 81
 82
 83
 84
 85
 86
 87
 88
 89
 90
 91
 92
 93
 94
 95
 96
 97
 98
 99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
```
| ```
class ModelSettings(TypedDict, total=False):
"""Settings to configure an LLM.
  Here we include only settings which apply to multiple models / model providers,
  though not all of these settings are supported by all models.
  """
  max_tokens: int
"""The maximum number of tokens to generate before stopping.
  Supported by:
  * Gemini
  * Anthropic
  * OpenAI
  * Groq
  * Cohere
  * Mistral
  """
  temperature: float
"""Amount of randomness injected into the response.
  Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to a model's
  maximum `temperature` for creative and generative tasks.
  Note that even with `temperature` of `0.0`, the results will not be fully deterministic.
  Supported by:
  * Gemini
  * Anthropic
  * OpenAI
  * Groq
  * Cohere
  * Mistral
  """
  top_p: float
"""An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass.
  So 0.1 means only the tokens comprising the top 10% probability mass are considered.
  You should either alter `temperature` or `top_p`, but not both.
  Supported by:
  * Gemini
  * Anthropic
  * OpenAI
  * Groq
  * Cohere
  * Mistral
  """
  timeout: float | Timeout
"""Override the client-level default timeout for a request, in seconds.
  Supported by:
  * Gemini
  * Anthropic
  * OpenAI
  * Groq
  * Mistral
  """
  parallel_tool_calls: bool
"""Whether to allow parallel tool calls.
  Supported by:
  * OpenAI (some models, not o1)
  * Groq
  * Anthropic
  """
  seed: int
"""The random seed to use for the model, theoretically allowing for deterministic results.
  Supported by:
  * OpenAI
  * Groq
  * Cohere
  * Mistral
  """
  presence_penalty: float
"""Penalize new tokens based on whether they have appeared in the text so far.
  Supported by:
  * OpenAI
  * Groq
  * Cohere
  * Gemini
  * Mistral
  """
  frequency_penalty: float
"""Penalize new tokens based on their existing frequency in the text so far.
  Supported by:
  * OpenAI
  * Groq
  * Cohere
  * Gemini
  * Mistral
  """
  logit_bias: dict[str, int]
"""Modify the likelihood of specified tokens appearing in the completion.
  Supported by:
  * OpenAI
  * Groq
  """

```
  
---|---  
  
####  max_tokens `instance-attribute`

```
max_tokens: int[](https://docs.python.org/3/library/functions.html#int)

```


The maximum number of tokens to generate before stopping.

Supported by:

  * Gemini
  * Anthropic
  * OpenAI
  * Groq
  * Cohere
  * Mistral



####  temperature `instance-attribute`

```
temperature: float[](https://docs.python.org/3/library/functions.html#float)

```


Amount of randomness injected into the response.

Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to a model's maximum `temperature` for creative and generative tasks.

Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

Supported by:

  * Gemini
  * Anthropic
  * OpenAI
  * Groq
  * Cohere
  * Mistral



####  top_p `instance-attribute`

```
top_p: float[](https://docs.python.org/3/library/functions.html#float)

```


An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass.

So 0.1 means only the tokens comprising the top 10% probability mass are considered.

You should either alter `temperature` or `top_p`, but not both.

Supported by:

  * Gemini
  * Anthropic
  * OpenAI
  * Groq
  * Cohere
  * Mistral



####  timeout `instance-attribute`

```
timeout: float[](https://docs.python.org/3/library/functions.html#float) | Timeout

```


Override the client-level default timeout for a request, in seconds.

Supported by:

  * Gemini
  * Anthropic
  * OpenAI
  * Groq
  * Mistral



####  parallel_tool_calls `instance-attribute`

```
parallel_tool_calls: bool[](https://docs.python.org/3/library/functions.html#bool)

```


Whether to allow parallel tool calls.

Supported by:

  * OpenAI (some models, not o1)
  * Groq
  * Anthropic



####  seed `instance-attribute`

```
seed: int[](https://docs.python.org/3/library/functions.html#int)

```


The random seed to use for the model, theoretically allowing for deterministic results.

Supported by:

  * OpenAI
  * Groq
  * Cohere
  * Mistral



####  presence_penalty `instance-attribute`

```
presence_penalty: float[](https://docs.python.org/3/library/functions.html#float)

```


Penalize new tokens based on whether they have appeared in the text so far.

Supported by:

  * OpenAI
  * Groq
  * Cohere
  * Gemini
  * Mistral



####  frequency_penalty `instance-attribute`

```
frequency_penalty: float[](https://docs.python.org/3/library/functions.html#float)

```


Penalize new tokens based on their existing frequency in the text so far.

Supported by:

  * OpenAI
  * Groq
  * Cohere
  * Gemini
  * Mistral



####  logit_bias `instance-attribute`

```
logit_bias: dict[](https://docs.python.org/3/library/stdtypes.html#dict)[str[](https://docs.python.org/3/library/stdtypes.html#str), int[](https://docs.python.org/3/library/functions.html#int)]

```


Modify the likelihood of specified tokens appearing in the completion.

Supported by:

  * OpenAI
  * Groq



© Pydantic Services Inc. 2024 to present 
