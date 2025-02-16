---
url: https://ai.pydantic.dev/examples/weather-agent/
title: Untitled
date_crawled: 
---

[ Skip to content ](#running-the-example)

[ ![logo](../../img/logo-white.svg) ](../.. "PydanticAI")

PydanticAI 

Weather agent 

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
    * Weather agent  [ Weather agent  ](./) Table of contents 
      * [ Running the Example  ](#running-the-example)
      * [ Example Code  ](#example-code)
      * [ Running the UI  ](#running-the-ui)
      * [ UI Code  ](#ui-code)
    * [ Bank support  ](../bank-support/)
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
  * [ Running the UI  ](#running-the-ui)
  * [ UI Code  ](#ui-code)



  1. [ Introduction  ](../..)
  2. [ Examples  ](../)



Version Notice

This documentation is ahead of the last release by [6 commits](https://github.com/pydantic/pydantic-ai/compare/v0.0.24...main). You may see documentation for features not yet supported in the latest release [v0.0.24 2025-02-12](https://github.com/pydantic/pydantic-ai/releases/tag/v0.0.24). 

# Weather agent

Example of PydanticAI with multiple tools which the LLM needs to call in turn to answer a question.

Demonstrates:

  * [tools](../../tools/)
  * [agent dependencies](../../dependencies/)
  * [streaming text responses](../../results/#streaming-text)
  * Building a [Gradio](https://www.gradio.app/) UI for the agent



In this case the idea is a "weather" agent — the user can ask for the weather in multiple locations, the agent will use the `get_lat_lng` tool to get the latitude and longitude of the locations, then use the `get_weather` tool to get the weather for those locations.

## Running the Example

To run this example properly, you might want to add two extra API keys **(Note if either key is missing, the code will fall back to dummy data, so they're not required)** :

  * A weather API key from [tomorrow.io](https://www.tomorrow.io/weather-api/) set via `WEATHER_API_KEY`
  * A geocoding API key from [geocode.maps.co](https://geocode.maps.co/) set via `GEO_API_KEY`



With [dependencies installed and environment variables set](../#usage), run:

[pip](#__tabbed_1_1)[uv](#__tabbed_1_2)

```
python-mpydantic_ai_examples.weather_agent

```


```
uvrun-mpydantic_ai_examples.weather_agent

```


## Example Code

pydantic_ai_examples/weather_agent.py```
from __future__ import annotations as _annotations
import asyncio
import os
from dataclasses import dataclass
from typing import Any
import logfire
from devtools import debug
from httpx import AsyncClient
from pydantic_ai import Agent, ModelRetry, RunContext
# 'if-token-present' means nothing will be sent (and the example will work) if you don't have logfire configured
logfire.configure(send_to_logfire='if-token-present')

@dataclass
class Deps:
  client: AsyncClient
  weather_api_key: str | None
  geo_api_key: str | None

weather_agent = Agent(
  'openai:gpt-4o',
  # 'Be concise, reply with one sentence.' is enough for some models (like openai) to use
  # the below tools appropriately, but others like anthropic and gemini require a bit more direction.
  system_prompt=(
    'Be concise, reply with one sentence.'
    'Use the `get_lat_lng` tool to get the latitude and longitude of the locations, '
    'then use the `get_weather` tool to get the weather.'
  ),
  deps_type=Deps,
  retries=2,
)

@weather_agent.tool
async def get_lat_lng(
  ctx: RunContext[Deps], location_description: str
) -> dict[str, float]:
"""Get the latitude and longitude of a location.
  Args:
    ctx: The context.
    location_description: A description of a location.
  """
  if ctx.deps.geo_api_key is None:
    # if no API key is provided, return a dummy response (London)
    return {'lat': 51.1, 'lng': -0.1}
  params = {
    'q': location_description,
    'api_key': ctx.deps.geo_api_key,
  }
  with logfire.span('calling geocode API', params=params) as span:
    r = await ctx.deps.client.get('https://geocode.maps.co/search', params=params)
    r.raise_for_status()
    data = r.json()
    span.set_attribute('response', data)
  if data:
    return {'lat': data[0]['lat'], 'lng': data[0]['lon']}
  else:
    raise ModelRetry('Could not find the location')

@weather_agent.tool
async def get_weather(ctx: RunContext[Deps], lat: float, lng: float) -> dict[str, Any]:
"""Get the weather at a location.
  Args:
    ctx: The context.
    lat: Latitude of the location.
    lng: Longitude of the location.
  """
  if ctx.deps.weather_api_key is None:
    # if no API key is provided, return a dummy response
    return {'temperature': '21 °C', 'description': 'Sunny'}
  params = {
    'apikey': ctx.deps.weather_api_key,
    'location': f'{lat},{lng}',
    'units': 'metric',
  }
  with logfire.span('calling weather API', params=params) as span:
    r = await ctx.deps.client.get(
      'https://api.tomorrow.io/v4/weather/realtime', params=params
    )
    r.raise_for_status()
    data = r.json()
    span.set_attribute('response', data)
  values = data['data']['values']
  # https://docs.tomorrow.io/reference/data-layers-weather-codes
  code_lookup = {
    1000: 'Clear, Sunny',
    1100: 'Mostly Clear',
    1101: 'Partly Cloudy',
    1102: 'Mostly Cloudy',
    1001: 'Cloudy',
    2000: 'Fog',
    2100: 'Light Fog',
    4000: 'Drizzle',
    4001: 'Rain',
    4200: 'Light Rain',
    4201: 'Heavy Rain',
    5000: 'Snow',
    5001: 'Flurries',
    5100: 'Light Snow',
    5101: 'Heavy Snow',
    6000: 'Freezing Drizzle',
    6001: 'Freezing Rain',
    6200: 'Light Freezing Rain',
    6201: 'Heavy Freezing Rain',
    7000: 'Ice Pellets',
    7101: 'Heavy Ice Pellets',
    7102: 'Light Ice Pellets',
    8000: 'Thunderstorm',
  }
  return {
    'temperature': f'{values["temperatureApparent"]:0.0f}°C',
    'description': code_lookup.get(values['weatherCode'], 'Unknown'),
  }

async def main():
  async with AsyncClient() as client:
    # create a free API key at https://www.tomorrow.io/weather-api/
    weather_api_key = os.getenv('WEATHER_API_KEY')
    # create a free API key at https://geocode.maps.co/
    geo_api_key = os.getenv('GEO_API_KEY')
    deps = Deps(
      client=client, weather_api_key=weather_api_key, geo_api_key=geo_api_key
    )
    result = await weather_agent.run(
      'What is the weather like in London and in Wiltshire?', deps=deps
    )
    debug(result)
    print('Response:', result.data)

if __name__ == '__main__':
  asyncio.run(main())

```


## Running the UI

You can build multi-turn chat applications for your agent with [Gradio](https://www.gradio.app/), a framework for building AI web applications entirely in python. Gradio comes with built-in chat components and agent support so the entire UI will be implemented in a single python file!

Here's what the UI looks like for the weather agent:

Note, to run the UI, you'll need Python 3.10+.

```
pipinstallgradio>=5.9.0
python/uv-run-mpydantic_ai_examples.weather_agent_gradio

```


## UI Code

pydantic_ai_examples/weather_agent_gradio.py```
#! pydantic_ai_examples/weather_agent_gradio.py

```


© Pydantic Services Inc. 2024 to present 
