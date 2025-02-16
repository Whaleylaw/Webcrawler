---
url: https://ai.pydantic.dev/api/models/test/
title: Untitled
date_crawled: 
---

[ Skip to content ](#pydantic_aimodelstest)

[ ![logo](../../../img/logo-white.svg) ](../../.. "PydanticAI")

PydanticAI 

pydantic_ai.models.test 

Type to start searching

[ pydantic/pydantic-ai  ](https://github.com/pydantic/pydantic-ai "Go to repository")

[ ![logo](../../../img/logo-white.svg) ](../../.. "PydanticAI") PydanticAI 

[ pydantic/pydantic-ai  ](https://github.com/pydantic/pydantic-ai "Go to repository")

  * [ Introduction  ](../../..)
  * [ Installation  ](../../../install/)
  * [ Getting Help  ](../../../help/)
  * [ Contributing  ](../../../contributing/)
  * [ Troubleshooting  ](../../../troubleshooting/)
  * Documentation  Documentation 
    * [ Agents  ](../../../agents/)
    * [ Models  ](../../../models/)
    * [ Dependencies  ](../../../dependencies/)
    * [ Function Tools  ](../../../tools/)
    * [ Results  ](../../../results/)
    * [ Messages and chat history  ](../../../message-history/)
    * [ Testing and Evals  ](../../../testing-evals/)
    * [ Debugging and Monitoring  ](../../../logfire/)
    * [ Multi-agent Applications  ](../../../multi-agent-applications/)
    * [ Graphs  ](../../../graph/)
  * [ Examples  ](../../../examples/)

Examples 
    * [ Pydantic Model  ](../../../examples/pydantic-model/)
    * [ Weather agent  ](../../../examples/weather-agent/)
    * [ Bank support  ](../../../examples/bank-support/)
    * [ SQL Generation  ](../../../examples/sql-gen/)
    * [ Flight booking  ](../../../examples/flight-booking/)
    * [ RAG  ](../../../examples/rag/)
    * [ Stream markdown  ](../../../examples/stream-markdown/)
    * [ Stream whales  ](../../../examples/stream-whales/)
    * [ Chat App with FastAPI  ](../../../examples/chat-app/)
    * [ Question Graph  ](../../../examples/question-graph/)
  * API Reference  API Reference 
    * [ pydantic_ai.agent  ](../../agent/)
    * [ pydantic_ai.tools  ](../../tools/)
    * [ pydantic_ai.result  ](../../result/)
    * [ pydantic_ai.messages  ](../../messages/)
    * [ pydantic_ai.exceptions  ](../../exceptions/)
    * [ pydantic_ai.settings  ](../../settings/)
    * [ pydantic_ai.usage  ](../../usage/)
    * [ pydantic_ai.format_as_xml  ](../../format_as_xml/)
    * [ pydantic_ai.models  ](../base/)
    * [ pydantic_ai.models.openai  ](../openai/)
    * [ pydantic_ai.models.anthropic  ](../anthropic/)
    * [ pydantic_ai.models.cohere  ](../cohere/)
    * [ pydantic_ai.models.gemini  ](../gemini/)
    * [ pydantic_ai.models.vertexai  ](../vertexai/)
    * [ pydantic_ai.models.groq  ](../groq/)
    * [ pydantic_ai.models.mistral  ](../mistral/)
    * pydantic_ai.models.test  [ pydantic_ai.models.test  ](./) Table of contents 
      * [ test  ](#pydantic_ai.models.test)
      * [ TestModel  ](#pydantic_ai.models.test.TestModel)
        * [ call_tools  ](#pydantic_ai.models.test.TestModel.call_tools)
        * [ custom_result_text  ](#pydantic_ai.models.test.TestModel.custom_result_text)
        * [ custom_result_args  ](#pydantic_ai.models.test.TestModel.custom_result_args)
        * [ seed  ](#pydantic_ai.models.test.TestModel.seed)
        * [ last_model_request_parameters  ](#pydantic_ai.models.test.TestModel.last_model_request_parameters)
        * [ model_name  ](#pydantic_ai.models.test.TestModel.model_name)
        * [ system  ](#pydantic_ai.models.test.TestModel.system)
      * [ TestStreamedResponse  ](#pydantic_ai.models.test.TestStreamedResponse)
        * [ model_name  ](#pydantic_ai.models.test.TestStreamedResponse.model_name)
        * [ timestamp  ](#pydantic_ai.models.test.TestStreamedResponse.timestamp)
    * [ pydantic_ai.models.function  ](../function/)
    * [ pydantic_graph  ](../../pydantic_graph/graph/)
    * [ pydantic_graph.nodes  ](../../pydantic_graph/nodes/)
    * [ pydantic_graph.state  ](../../pydantic_graph/state/)
    * [ pydantic_graph.mermaid  ](../../pydantic_graph/mermaid/)
    * [ pydantic_graph.exceptions  ](../../pydantic_graph/exceptions/)



Table of contents 

  * [ test  ](#pydantic_ai.models.test)
  * [ TestModel  ](#pydantic_ai.models.test.TestModel)
    * [ call_tools  ](#pydantic_ai.models.test.TestModel.call_tools)
    * [ custom_result_text  ](#pydantic_ai.models.test.TestModel.custom_result_text)
    * [ custom_result_args  ](#pydantic_ai.models.test.TestModel.custom_result_args)
    * [ seed  ](#pydantic_ai.models.test.TestModel.seed)
    * [ last_model_request_parameters  ](#pydantic_ai.models.test.TestModel.last_model_request_parameters "last_model_request_parameters")
    * [ model_name  ](#pydantic_ai.models.test.TestModel.model_name)
    * [ system  ](#pydantic_ai.models.test.TestModel.system)
  * [ TestStreamedResponse  ](#pydantic_ai.models.test.TestStreamedResponse)
    * [ model_name  ](#pydantic_ai.models.test.TestStreamedResponse.model_name)
    * [ timestamp  ](#pydantic_ai.models.test.TestStreamedResponse.timestamp)



  1. [ Introduction  ](../../..)
  2. [ API Reference  ](../../agent/)



Version Notice

This documentation is ahead of the last release by [6 commits](https://github.com/pydantic/pydantic-ai/compare/v0.0.24...main). You may see documentation for features not yet supported in the latest release [v0.0.24 2025-02-12](https://github.com/pydantic/pydantic-ai/releases/tag/v0.0.24). 

# `pydantic_ai.models.test`

Utility model for quickly testing apps built with PydanticAI.

Here's a minimal example:

test_model_usage.py```
from pydantic_ai import Agent
from pydantic_ai.models.test import TestModel
my_agent = Agent('openai:gpt-4o', system_prompt='...')

async def test_my_agent():
"""Unit test for my_agent, to be run by pytest."""
  m = TestModel()
  with my_agent.override(model=m):
    result = await my_agent.run('Testing my agent...')
    assert result.data == 'success (no tool calls)'
  assert m.last_model_request_parameters.function_tools == []

```


See [Unit testing with `TestModel`](../../../testing-evals/#unit-testing-with-testmodel) for detailed documentation.

###  TestModel `dataclass`

Bases: `Model[](../base/#pydantic_ai.models.Model "pydantic_ai.models.Model")`

A model specifically for testing purposes.

This will (by default) call all tools in the agent, then return a tool response if possible, otherwise a plain response.

How useful this model is will vary significantly.

Apart from `__init__` derived by the `dataclass` decorator, all methods are private or match those of the base class.

Source code in `pydantic_ai_slim/pydantic_ai/models/test.py`

```
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
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
```
| ```
@dataclass
class TestModel(Model):
"""A model specifically for testing purposes.
  This will (by default) call all tools in the agent, then return a tool response if possible,
  otherwise a plain response.
  How useful this model is will vary significantly.
  Apart from `__init__` derived by the `dataclass` decorator, all methods are private or match those
  of the base class.
  """
  # NOTE: Avoid test discovery by pytest.
  __test__ = False
  call_tools: list[str] | Literal['all'] = 'all'
"""List of tools to call. If `'all'`, all tools will be called."""
  custom_result_text: str | None = None
"""If set, this text is returned as the final result."""
  custom_result_args: Any | None = None
"""If set, these args will be passed to the result tool."""
  seed: int = 0
"""Seed for generating random data."""
  last_model_request_parameters: ModelRequestParameters | None = field(default=None, init=False)
"""The last ModelRequestParameters passed to the model in a request.
  The ModelRequestParameters contains information about the function and result tools available during request handling.
  This is set when a request is made, so will reflect the function tools from the last step of the last run.
  """
  _model_name: str = field(default='test', repr=False)
  _system: str | None = field(default=None, repr=False)
  async def request(
    self,
    messages: list[ModelMessage],
    model_settings: ModelSettings | None,
    model_request_parameters: ModelRequestParameters,
  ) -> tuple[ModelResponse, Usage]:
    self.last_model_request_parameters = model_request_parameters
    model_response = self._request(messages, model_settings, model_request_parameters)
    usage = _estimate_usage([*messages, model_response])
    return model_response, usage
  @asynccontextmanager
  async def request_stream(
    self,
    messages: list[ModelMessage],
    model_settings: ModelSettings | None,
    model_request_parameters: ModelRequestParameters,
  ) -> AsyncIterator[StreamedResponse]:
    self.last_model_request_parameters = model_request_parameters
    model_response = self._request(messages, model_settings, model_request_parameters)
    yield TestStreamedResponse(
      _model_name=self._model_name, _structured_response=model_response, _messages=messages
    )
  @property
  def model_name(self) -> str:
"""The model name."""
    return self._model_name
  @property
  def system(self) -> str | None:
"""The system / model provider."""
    return self._system
  def gen_tool_args(self, tool_def: ToolDefinition) -> Any:
    return _JsonSchemaTestData(tool_def.parameters_json_schema, self.seed).generate()
  def _get_tool_calls(self, model_request_parameters: ModelRequestParameters) -> list[tuple[str, ToolDefinition]]:
    if self.call_tools == 'all':
      return [(r.name, r) for r in model_request_parameters.function_tools]
    else:
      function_tools_lookup = {t.name: t for t in model_request_parameters.function_tools}
      tools_to_call = (function_tools_lookup[name] for name in self.call_tools)
      return [(r.name, r) for r in tools_to_call]
  def _get_result(self, model_request_parameters: ModelRequestParameters) -> _TextResult | _FunctionToolResult:
    if self.custom_result_text is not None:
      assert (
        model_request_parameters.allow_text_result
      ), 'Plain response not allowed, but `custom_result_text` is set.'
      assert self.custom_result_args is None, 'Cannot set both `custom_result_text` and `custom_result_args`.'
      return _TextResult(self.custom_result_text)
    elif self.custom_result_args is not None:
      assert (
        model_request_parameters.result_tools is not None
      ), 'No result tools provided, but `custom_result_args` is set.'
      result_tool = model_request_parameters.result_tools[0]
      if k := result_tool.outer_typed_dict_key:
        return _FunctionToolResult({k: self.custom_result_args})
      else:
        return _FunctionToolResult(self.custom_result_args)
    elif model_request_parameters.allow_text_result:
      return _TextResult(None)
    elif model_request_parameters.result_tools:
      return _FunctionToolResult(None)
    else:
      return _TextResult(None)
  def _request(
    self,
    messages: list[ModelMessage],
    model_settings: ModelSettings | None,
    model_request_parameters: ModelRequestParameters,
  ) -> ModelResponse:
    tool_calls = self._get_tool_calls(model_request_parameters)
    result = self._get_result(model_request_parameters)
    result_tools = model_request_parameters.result_tools
    # if there are tools, the first thing we want to do is call all of them
    if tool_calls and not any(isinstance(m, ModelResponse) for m in messages):
      return ModelResponse(
        parts=[ToolCallPart(name, self.gen_tool_args(args)) for name, args in tool_calls],
        model_name=self._model_name,
      )
    if messages:
      last_message = messages[-1]
      assert isinstance(last_message, ModelRequest), 'Expected last message to be a `ModelRequest`.'
      # check if there are any retry prompts, if so retry them
      new_retry_names = {p.tool_name for p in last_message.parts if isinstance(p, RetryPromptPart)}
      if new_retry_names:
        # Handle retries for both function tools and result tools
        # Check function tools first
        retry_parts: list[ModelResponsePart] = [
          ToolCallPart(name, self.gen_tool_args(args)) for name, args in tool_calls if name in new_retry_names
        ]
        # Check result tools
        if result_tools:
          retry_parts.extend(
            [
              ToolCallPart(
                tool.name,
                result.value
                if isinstance(result, _FunctionToolResult) and result.value is not None
                else self.gen_tool_args(tool),
              )
              for tool in result_tools
              if tool.name in new_retry_names
            ]
          )
        return ModelResponse(parts=retry_parts, model_name=self._model_name)
    if isinstance(result, _TextResult):
      if (response_text := result.value) is None:
        # build up details of tool responses
        output: dict[str, Any] = {}
        for message in messages:
          if isinstance(message, ModelRequest):
            for part in message.parts:
              if isinstance(part, ToolReturnPart):
                output[part.tool_name] = part.content
        if output:
          return ModelResponse(
            parts=[TextPart(pydantic_core.to_json(output).decode())], model_name=self._model_name
          )
        else:
          return ModelResponse(parts=[TextPart('success (no tool calls)')], model_name=self._model_name)
      else:
        return ModelResponse(parts=[TextPart(response_text)], model_name=self._model_name)
    else:
      assert result_tools, 'No result tools provided'
      custom_result_args = result.value
      result_tool = result_tools[self.seed % len(result_tools)]
      if custom_result_args is not None:
        return ModelResponse(
          parts=[ToolCallPart(result_tool.name, custom_result_args)], model_name=self._model_name
        )
      else:
        response_args = self.gen_tool_args(result_tool)
        return ModelResponse(parts=[ToolCallPart(result_tool.name, response_args)], model_name=self._model_name)

```
  
---|---  
  
####  call_tools `class-attribute` `instance-attribute`

```
call_tools: list[](https://docs.python.org/3/library/stdtypes.html#list)[str[](https://docs.python.org/3/library/stdtypes.html#str)] | Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['all'] = 'all'

```


List of tools to call. If `'all'`, all tools will be called.

####  custom_result_text `class-attribute` `instance-attribute`

```
custom_result_text: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None

```


If set, this text is returned as the final result.

####  custom_result_args `class-attribute` `instance-attribute`

```
custom_result_args: Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any") | None = None

```


If set, these args will be passed to the result tool.

####  seed `class-attribute` `instance-attribute`

```
seed: int[](https://docs.python.org/3/library/functions.html#int) = 0

```


Seed for generating random data.

####  last_model_request_parameters `class-attribute` `instance-attribute`

```
last_model_request_parameters: (
  ModelRequestParameters[](../base/#pydantic_ai.models.ModelRequestParameters "pydantic_ai.models.ModelRequestParameters") | None
) = field[](https://docs.python.org/3/library/dataclasses.html#dataclasses.field "dataclasses.field")(default=None, init=False)

```


The last ModelRequestParameters passed to the model in a request.

The ModelRequestParameters contains information about the function and result tools available during request handling.

This is set when a request is made, so will reflect the function tools from the last step of the last run.

####  model_name `property`

```
model_name: str[](https://docs.python.org/3/library/stdtypes.html#str)

```


The model name.

####  system `property`

```
system: str[](https://docs.python.org/3/library/stdtypes.html#str) | None

```


The system / model provider.

###  TestStreamedResponse `dataclass`

Bases: `StreamedResponse[](../base/#pydantic_ai.models.StreamedResponse "pydantic_ai.models.StreamedResponse")`

A structured response that streams test data.

Source code in `pydantic_ai_slim/pydantic_ai/models/test.py`

```
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
```
| ```
@dataclass
class TestStreamedResponse(StreamedResponse):
"""A structured response that streams test data."""
  _model_name: str
  _structured_response: ModelResponse
  _messages: InitVar[Iterable[ModelMessage]]
  _timestamp: datetime = field(default_factory=_utils.now_utc, init=False)
  def __post_init__(self, _messages: Iterable[ModelMessage]):
    self._usage = _estimate_usage(_messages)
  async def _get_event_iterator(self) -> AsyncIterator[ModelResponseStreamEvent]:
    for i, part in enumerate(self._structured_response.parts):
      if isinstance(part, TextPart):
        text = part.content
        *words, last_word = text.split(' ')
        words = [f'{word} ' for word in words]
        words.append(last_word)
        if len(words) == 1 and len(text) > 2:
          mid = len(text) // 2
          words = [text[:mid], text[mid:]]
        self._usage += _get_string_usage('')
        yield self._parts_manager.handle_text_delta(vendor_part_id=i, content='')
        for word in words:
          self._usage += _get_string_usage(word)
          yield self._parts_manager.handle_text_delta(vendor_part_id=i, content=word)
      else:
        yield self._parts_manager.handle_tool_call_part(
          vendor_part_id=i, tool_name=part.tool_name, args=part.args, tool_call_id=part.tool_call_id
        )
  @property
  def model_name(self) -> str:
"""Get the model name of the response."""
    return self._model_name
  @property
  def timestamp(self) -> datetime:
"""Get the timestamp of the response."""
    return self._timestamp

```
  
---|---  
  
####  model_name `property`

```
model_name: str[](https://docs.python.org/3/library/stdtypes.html#str)

```


Get the model name of the response.

####  timestamp `property`

```
timestamp: datetime[](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime")

```


Get the timestamp of the response.

© Pydantic Services Inc. 2024 to present 
