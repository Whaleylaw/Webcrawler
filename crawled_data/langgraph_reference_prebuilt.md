---
url: https://langchain-ai.github.io/langgraph/reference/prebuilt/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/reference/prebuilt/#prebuilt)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Prebuilt components 

[ ](https://langchain-ai.github.io/langgraph/reference/prebuilt/?q= "Share")

Type to start searching

[ GitHub  ](https://github.com/langchain-ai/langgraph "Go to repository")

  * [ Home ](https://langchain-ai.github.io/langgraph/)
  * [ API reference ](https://langchain-ai.github.io/langgraph/reference/graphs/)



[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

[ GitHub  ](https://github.com/langchain-ai/langgraph "Go to repository")

  * [ Home  ](https://langchain-ai.github.io/langgraph/)
  * API reference  API reference 
    * Library  Library 
      * [ Graphs  ](https://langchain-ai.github.io/langgraph/reference/graphs/)
      * [ Checkpointing  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/)
      * [ Storage  ](https://langchain-ai.github.io/langgraph/reference/store/)
      * Prebuilt components  [ Prebuilt components  ](https://langchain-ai.github.io/langgraph/reference/prebuilt/) Table of contents 
        * [ create_react_agent  ](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent)
        * [ ToolNode  ](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.ToolNode)
          * [ inject_tool_args  ](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.ToolNode.inject_tool_args)
        * [ InjectedState  ](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.InjectedState)
        * [ InjectedStore  ](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.InjectedStore)
        * [ tools_condition  ](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.tools_condition)
        * [ ValidationNode  ](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_validator.ValidationNode)
      * [ Channels  ](https://langchain-ai.github.io/langgraph/reference/channels/)
      * [ Errors  ](https://langchain-ai.github.io/langgraph/reference/errors/)
      * [ Types  ](https://langchain-ai.github.io/langgraph/reference/types/)
      * [ Constants  ](https://langchain-ai.github.io/langgraph/reference/constants/)
      * [ Pregel  ](https://langchain-ai.github.io/langgraph/reference/pregel/)
      * [ Config  ](https://langchain-ai.github.io/langgraph/reference/config/)
      * [ Functional API  ](https://langchain-ai.github.io/langgraph/reference/func/)
    * LangGraph Platform  LangGraph Platform 
      * [ Server API  ](https://langchain-ai.github.io/langgraph/cloud/reference/api/api_ref/)
      * [ CLI  ](https://langchain-ai.github.io/langgraph/cloud/reference/cli/)
      * [ SDK (Python)  ](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/)
      * [ SDK (JS/TS)  ](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/)
      * [ RemoteGraph  ](https://langchain-ai.github.io/langgraph/reference/remote_graph/)
      * [ Environment variables  ](https://langchain-ai.github.io/langgraph/cloud/reference/env_var/)



Table of contents 

  * [ create_react_agent  ](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent)
  * [ ToolNode  ](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.ToolNode)
    * [ inject_tool_args  ](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.ToolNode.inject_tool_args)
  * [ InjectedState  ](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.InjectedState)
  * [ InjectedStore  ](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.InjectedStore)
  * [ tools_condition  ](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.tools_condition)
  * [ ValidationNode  ](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_validator.ValidationNode)



  1. [ API reference  ](https://langchain-ai.github.io/langgraph/reference/graphs/)
  2. [ Library  ](https://langchain-ai.github.io/langgraph/reference/graphs/)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/reference/prebuilt.md "Edit this page")

# Prebuilt[¶](https://langchain-ai.github.io/langgraph/reference/prebuilt/#prebuilt "Permanent link")

##  `create_react_agent(model: Union[str, LanguageModelLike], tools: Union[ToolExecutor, Sequence[BaseTool], ToolNode], *, state_schema: Optional[StateSchemaType] = None, prompt: Optional[Prompt] = None, response_format: Optional[Union[StructuredResponseSchema, tuple[str, StructuredResponseSchema]]] = None, checkpointer: Optional[Checkpointer] = None, store: Optional[BaseStore] = None, interrupt_before: Optional[list[str]] = None, interrupt_after: Optional[list[str]] = None, debug: bool = False, version: Literal['v1', 'v2'] = 'v1', name: Optional[str] = None) -> CompiledGraph` [¶](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent "Permanent link")

Creates a graph that works with a chat model that utilizes tool calling.

Parameters:

  * **`model`**(`Union[str, LanguageModelLike]`) – 

The `LangChain` chat model that supports tool calling.

  * **`tools`**(`Union[ToolExecutor, Sequence[BaseTool], ToolNode]`) – 

A list of tools, a ToolExecutor, or a ToolNode instance. If an empty list is provided, the agent will consist of a single LLM node without tool calling.

  * **`state_schema`**(`Optional[StateSchemaType]` , default: `None` ) – 

An optional state schema that defines graph state. Must have `messages` and `is_last_step` keys. Defaults to `AgentState` that defines those two keys.

  * **`prompt`**(`Optional[Prompt]` , default: `None` ) – 

An optional prompt for the LLM. Can take a few different forms:

    * str: This is converted to a SystemMessage and added to the beginning of the list of messages in state["messages"].
    * SystemMessage: this is added to the beginning of the list of messages in state["messages"].
    * Callable: This function should take in full graph state and the output is then passed to the language model.
    * Runnable: This runnable should take in full graph state and the output is then passed to the language model.

Note

Prior to `v0.2.68`, the prompt was set using `state_modifier` / `messages_modifier` parameters.

  * **`response_format`**(`Optional[Union[StructuredResponseSchema, tuple[str, StructuredResponseSchema]]]` , default: `None` ) – 

An optional schema for the final agent output.

If provided, output will be formatted to match the given schema and returned in the 'structured_response' state key. If not provided, `structured_response` will not be present in the output state. Can be passed in as:

```
- an OpenAI function/tool schema,
- a JSON Schema,
- a TypedDict class,
- or a Pydantic class.
- a tuple (prompt, schema), where schema is one of the above.
  The prompt will be used together with the model that is being used to generate the structured response.

```


Important

`response_format` requires the model to support `.with_structured_output`

Note

The graph will make a separate call to the LLM to generate the structured response after the agent loop is finished. This is not the only strategy to get structured responses, see more options in [this guide](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/).

  * **`checkpointer`**(`Optional[Checkpointer]` , default: `None` ) – 

An optional checkpoint saver object. This is used for persisting the state of the graph (e.g., as chat memory) for a single thread (e.g., a single conversation).

  * **`store`**(`Optional[BaseStore]` , default: `None` ) – 

An optional store object. This is used for persisting data across multiple threads (e.g., multiple conversations / users).

  * **`interrupt_before`**(`Optional[list[str]]` , default: `None` ) – 

An optional list of node names to interrupt before. Should be one of the following: "agent", "tools". This is useful if you want to add a user confirmation or other interrupt before taking an action.

  * **`interrupt_after`**(`Optional[list[str]]` , default: `None` ) – 

An optional list of node names to interrupt after. Should be one of the following: "agent", "tools". This is useful if you want to return directly or run additional processing on an output.

  * **`debug`**(`bool` , default: `False` ) – 

A flag indicating whether to enable debug mode.

  * **`version`**(`Literal['v1', 'v2']` , default: `'v1'` ) – 

Determines the version of the graph to create. Can be one of:

    * `"v1"`: The tool node processes a single message. All tool calls in the message are executed in parallel within the tool node.
    * `"v2"`: The tool node processes a tool call. Tool calls are distributed across multiple instances of the tool node using the [Send](https://langchain-ai.github.io/langgraph/concepts/low_level/#send) API.

  * **`name`**(`Optional[str]` , default: `None` ) – 

An optional name for the CompiledStateGraph. This name will be automatically used when adding ReAct agent graph to another graph as a subgraph node - particularly useful for building multi-agent systems.




Returns:

  * `CompiledGraph` – 

A compiled LangChain runnable that can be used for chat interactions.




The resulting graph looks like this:

The "agent" node calls the language model with the messages list (after applying the messages modifier). If the resulting AIMessage contains `tool_calls`, the graph will then call the ["tools"](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.ToolNode). The "tools" node executes the tools (1 tool per `tool_call`) and adds the responses to the messages list as `ToolMessage` objects. The agent node then calls the language model again. The process repeats until no more `tool_calls` are present in the response. The agent then returns the full list of messages as a dictionary containing the key "messages".

Examples:

Use with a simple tool:

```
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-1)>>> fromdatetimeimport datetime
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-2)>>> fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-3)>>> fromlanggraph.prebuiltimport create_react_agent
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-4)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-5)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-6)... def check_weather(location: str, at_time: datetime | None = None) -> str:
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-7)...   '''Return the weather forecast for the specified location.'''
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-8)...   return f"It's always sunny in {location}"
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-9)>>>
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-10)>>> tools = [check_weather]
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-11)>>> model = ChatOpenAI(model="gpt-4o")
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-12)>>> graph = create_react_agent(model, tools=tools)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-13)>>> inputs = {"messages": [("user", "what is the weather in sf")]}
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-14)>>> for s in graph.stream(inputs, stream_mode="values"):
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-15)...   message = s["messages"][-1]
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-16)...   if isinstance(message, tuple):
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-17)...     print(message)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-18)...   else:
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-19)...     message.pretty_print()
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-20)('user', 'what is the weather in sf')
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-21)================================== Ai Message ==================================
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-22)Tool Calls:
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-23)check_weather (call_LUzFvKJRuaWQPeXvBOzwhQOu)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-24)Call ID: call_LUzFvKJRuaWQPeXvBOzwhQOu
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-25)Args:
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-26)  location: San Francisco
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-27)================================= Tool Message =================================
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-28)Name: check_weather
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-29)It's always sunny in San Francisco
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-30)================================== Ai Message ==================================
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-31)The weather in San Francisco is sunny.

```


Add a system prompt for the LLM: 

```
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-1-1)>>> system_prompt = "You are a helpful bot named Fred."
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-1-2)>>> graph = create_react_agent(model, tools, prompt=system_prompt)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-1-3)>>> inputs = {"messages": [("user", "What's your name? And what's the weather in SF?")]}
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-1-4)>>> for s in graph.stream(inputs, stream_mode="values"):
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-1-5)...   message = s["messages"][-1]
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-1-6)...   if isinstance(message, tuple):
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-1-7)...     print(message)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-1-8)...   else:
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-1-9)...     message.pretty_print()
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-1-10)('user', "What's your name? And what's the weather in SF?")
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-1-11)================================== Ai Message ==================================
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-1-12)Hi, my name is Fred. Let me check the weather in San Francisco for you.
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-1-13)Tool Calls:
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-1-14)check_weather (call_lqhj4O0hXYkW9eknB4S41EXk)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-1-15)Call ID: call_lqhj4O0hXYkW9eknB4S41EXk
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-1-16)Args:
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-1-17)  location: San Francisco
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-1-18)================================= Tool Message =================================
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-1-19)Name: check_weather
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-1-20)It's always sunny in San Francisco
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-1-21)================================== Ai Message ==================================
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-1-22)The weather in San Francisco is currently sunny. If you need any more details or have other questions, feel free to ask!

```


Add a more complex prompt for the LLM:

```
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-2-1)>>> fromlangchain_core.promptsimport ChatPromptTemplate
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-2-2)>>> prompt = ChatPromptTemplate.from_messages([
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-2-3)...   ("system", "You are a helpful bot named Fred."),
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-2-4)...   ("placeholder", "{messages}"),
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-2-5)...   ("user", "Remember, always be polite!"),
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-2-6)... ])
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-2-7)>>>
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-2-8)>>> graph = create_react_agent(model, tools, prompt=prompt)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-2-9)>>> inputs = {"messages": [("user", "What's your name? And what's the weather in SF?")]}
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-2-10)>>> for s in graph.stream(inputs, stream_mode="values"):
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-2-11)...   message = s["messages"][-1]
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-2-12)...   if isinstance(message, tuple):
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-2-13)...     print(message)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-2-14)...   else:
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-2-15)...     message.pretty_print()

```


Add complex prompt with custom graph state:

```
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-3-1)>>> fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-3-2)>>>
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-3-3)>>> fromlanggraph.managedimport IsLastStep
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-3-4)>>> prompt = ChatPromptTemplate.from_messages(
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-3-5)...   [
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-3-6)...     ("system", "Today is {today}"),
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-3-7)...     ("placeholder", "{messages}"),
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-3-8)...   ]
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-3-9)... )
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-3-10)>>>
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-3-11)>>> classCustomState(TypedDict):
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-3-12)...   today: str
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-3-13)...   messages: Annotated[list[BaseMessage], add_messages]
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-3-14)...   is_last_step: IsLastStep
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-3-15)>>>
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-3-16)>>> graph = create_react_agent(model, tools, state_schema=CustomState, prompt=prompt)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-3-17)>>> inputs = {"messages": [("user", "What's today's date? And what's the weather in SF?")], "today": "July 16, 2004"}
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-3-18)>>> for s in graph.stream(inputs, stream_mode="values"):
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-3-19)...   message = s["messages"][-1]
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-3-20)...   if isinstance(message, tuple):
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-3-21)...     print(message)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-3-22)...   else:
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-3-23)...     message.pretty_print()

```


Add thread-level "chat memory" to the graph:

```
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-4-1)>>> fromlanggraph.checkpoint.memoryimport MemorySaver
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-4-2)>>> graph = create_react_agent(model, tools, checkpointer=MemorySaver())
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-4-3)>>> config = {"configurable": {"thread_id": "thread-1"}}
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-4-4)>>> defprint_stream(graph, inputs, config):
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-4-5)...   for s in graph.stream(inputs, config, stream_mode="values"):
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-4-6)...     message = s["messages"][-1]
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-4-7)...     if isinstance(message, tuple):
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-4-8)...       print(message)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-4-9)...     else:
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-4-10)...       message.pretty_print()
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-4-11)>>> inputs = {"messages": [("user", "What's the weather in SF?")]}
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-4-12)>>> print_stream(graph, inputs, config)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-4-13)>>> inputs2 = {"messages": [("user", "Cool, so then should i go biking today?")]}
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-4-14)>>> print_stream(graph, inputs2, config)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-4-15)('user', "What's the weather in SF?")
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-4-16)================================== Ai Message ==================================
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-4-17)Tool Calls:
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-4-18)check_weather (call_ChndaktJxpr6EMPEB5JfOFYc)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-4-19)Call ID: call_ChndaktJxpr6EMPEB5JfOFYc
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-4-20)Args:
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-4-21)  location: San Francisco
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-4-22)================================= Tool Message =================================
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-4-23)Name: check_weather
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-4-24)It's always sunny in San Francisco
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-4-25)================================== Ai Message ==================================
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-4-26)The weather in San Francisco is sunny. Enjoy your day!
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-4-27)================================ Human Message =================================
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-4-28)Cool, so then should i go biking today?
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-4-29)================================== Ai Message ==================================
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-4-30)Since the weather in San Francisco is sunny, it sounds like a great day for biking! Enjoy your ride!

```


Add an interrupt to let the user confirm before taking an action:

```
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-5-1)>>> graph = create_react_agent(
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-5-2)...   model, tools, interrupt_before=["tools"], checkpointer=MemorySaver()
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-5-3)>>> )
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-5-4)>>> config = {"configurable": {"thread_id": "thread-1"}}
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-5-5)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-5-6)>>> inputs = {"messages": [("user", "What's the weather in SF?")]}
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-5-7)>>> print_stream(graph, inputs, config)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-5-8)>>> snapshot = graph.get_state(config)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-5-9)>>> print("Next step: ", snapshot.next)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-5-10)>>> print_stream(graph, None, config)

```


Add cross-thread memory to the graph:

```
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-6-1)>>> fromlanggraph.prebuiltimport InjectedStore
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-6-2)>>> fromlanggraph.store.baseimport BaseStore
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-6-3)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-6-4)>>> defsave_memory(memory: str, *, config: RunnableConfig, store: Annotated[BaseStore, InjectedStore()]) -> str:
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-6-5)... '''Save the given memory for the current user.'''
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-6-6)...   # This is a **tool** the model can use to save memories to storage
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-6-7)...   user_id = config.get("configurable", {}).get("user_id")
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-6-8)...   namespace = ("memories", user_id)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-6-9)...   store.put(namespace, f"memory_{len(store.search(namespace))}", {"data": memory})
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-6-10)...   return f"Saved memory: {memory}"
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-6-11)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-6-12)>>> defprepare_model_inputs(state: AgentState, config: RunnableConfig, store: BaseStore):
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-6-13)...   # Retrieve user memories and add them to the system message
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-6-14)...   # This function is called **every time** the model is prompted. It converts the state to a prompt
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-6-15)...   user_id = config.get("configurable", {}).get("user_id")
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-6-16)...   namespace = ("memories", user_id)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-6-17)...   memories = [m.value["data"] for m in store.search(namespace)]
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-6-18)...   system_msg = f"User memories: {', '.join(memories)}"
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-6-19)...   return [{"role": "system", "content": system_msg)] + state["messages"]
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-6-20)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-6-21)>>> fromlanggraph.checkpoint.memoryimport MemorySaver
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-6-22)>>> fromlanggraph.store.memoryimport InMemoryStore
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-6-23)>>> store = InMemoryStore()
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-6-24)>>> graph = create_react_agent(model, [save_memory], prompt=prepare_model_inputs, store=store, checkpointer=MemorySaver())
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-6-25)>>> config = {"configurable": {"thread_id": "thread-1", "user_id": "1"}}
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-6-26)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-6-27)>>> inputs = {"messages": [("user", "Hey I'm Will, how's it going?")]}
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-6-28)>>> print_stream(graph, inputs, config)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-6-29)('user', "Hey I'm Will, how's it going?")
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-6-30)================================== Ai Message ==================================
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-6-31)Hello Will! It's nice to meet you. I'm doing well, thank you for asking. How are you doing today?
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-6-32)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-6-33)>>> inputs2 = {"messages": [("user", "I like to bike")]}
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-6-34)>>> print_stream(graph, inputs2, config)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-6-35)================================ Human Message =================================
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-6-36)I like to bike
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-6-37)================================== Ai Message ==================================
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-6-38)That's great to hear, Will! Biking is an excellent hobby and form of exercise. It's a fun way to stay active and explore your surroundings. Do you have any favorite biking routes or trails you enjoy? Or perhaps you're into a specific type of biking, like mountain biking or road cycling?
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-6-39)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-6-40)>>> config = {"configurable": {"thread_id": "thread-2", "user_id": "1"}}
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-6-41)>>> inputs3 = {"messages": [("user", "Hi there! Remember me?")]}
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-6-42)>>> print_stream(graph, inputs3, config)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-6-43)================================ Human Message =================================
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-6-44)Hi there! Remember me?
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-6-45)================================== Ai Message ==================================
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-6-46)User memories:
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-6-47)Hello! Of course, I remember you, Will! You mentioned earlier that you like to bike. It's great to hear from you again. How have you been? Have you been on any interesting bike rides lately?

```


Add a timeout for a given step:

```
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-7-1)>>> importtime
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-7-2)... defcheck_weather(location: str, at_time: datetime | None = None) -> float:
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-7-3)... '''Return the weather forecast for the specified location.'''
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-7-4)...   time.sleep(2)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-7-5)...   return f"It's always sunny in {location}"
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-7-6)>>>
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-7-7)>>> tools = [check_weather]
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-7-8)>>> graph = create_react_agent(model, tools)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-7-9)>>> graph.step_timeout = 1 # Seconds
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-7-10)>>> for s in graph.stream({"messages": [("user", "what is the weather in sf")]}):
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-7-11)...   print(s)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-7-12)TimeoutError: Timed out at step 2

```


##  `ToolNode` [¶](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.ToolNode "Permanent link")

Bases: `RunnableCallable`

A node that runs the tools called in the last AIMessage.

It can be used either in StateGraph with a "messages" state key (or a custom key passed via ToolNode's 'messages_key'). If multiple tool calls are requested, they will be run in parallel. The output will be a list of ToolMessages, one for each tool call.

Tool calls can also be passed directly as a list of `ToolCall` dicts.

Parameters:

  * **`tools`**(`Sequence[Union[BaseTool, Callable]]`) – 

A sequence of tools that can be invoked by the ToolNode.

  * **`name`**(`str` , default: `'tools'` ) – 

The name of the ToolNode in the graph. Defaults to "tools".

  * **`tags`**(`Optional[list[str]]` , default: `None` ) – 

Optional tags to associate with the node. Defaults to None.

  * **`handle_tool_errors`**(`Union[bool, str, Callable[..., str], tuple[type[Exception], ...]]` , default: `True` ) – 

How to handle tool errors raised by tools inside the node. Defaults to True. Must be one of the following:

    * True: all errors will be caught and a ToolMessage with a default error message (TOOL_CALL_ERROR_TEMPLATE) will be returned.
    * str: all errors will be caught and a ToolMessage with the string value of 'handle_tool_errors' will be returned.
    * tuple[type[Exception], ...]: exceptions in the tuple will be caught and a ToolMessage with a default error message (TOOL_CALL_ERROR_TEMPLATE) will be returned.
    * Callable[..., str]: exceptions from the signature of the callable will be caught and a ToolMessage with the string value of the result of the 'handle_tool_errors' callable will be returned.
    * False: none of the errors raised by the tools will be caught

  * **`messages_key`**(`str` , default: `'messages'` ) – 

The state key in the input that contains the list of messages. The same key will be used for the output from the ToolNode. Defaults to "messages".




The `ToolNode` is roughly analogous to:

```
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-1)tools_by_name = {tool.name: tool for tool in tools}
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-2)deftool_node(state: dict):
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-3)  result = []
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-4)  for tool_call in state["messages"][-1].tool_calls:
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-5)    tool = tools_by_name[tool_call["name"]]
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-6)    observation = tool.invoke(tool_call["args"])
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-7)    result.append(ToolMessage(content=observation, tool_call_id=tool_call["id"]))
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-8)  return {"messages": result}

```


Tool calls can also be passed directly to a ToolNode. This can be useful when using the Send API, e.g., in a conditional edge:

```
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-1-1)defexample_conditional_edge(state: dict) -> List[Send]:
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-1-2)  tool_calls = state["messages"][-1].tool_calls
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-1-3)  # If tools rely on state or store variables (whose values are not generated
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-1-4)  # directly by a model), you can inject them into the tool calls.
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-1-5)  tool_calls = [
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-1-6)    tool_node.inject_tool_args(call, state, store)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-1-7)    for call in last_message.tool_calls
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-1-8)  ]
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-1-9)  return [Send("tools", [tool_call]) for tool_call in tool_calls]

```


Important

  * The input state can be one of the following:
    * A dict with a messages key containing a list of messages.
    * A list of messages.
    * A list of tool calls.
  * If operating on a message list, the last message must be an `AIMessage` with `tool_calls` populated.



###  `inject_tool_args(tool_call: ToolCall, input: Union[list[AnyMessage], dict[str, Any], BaseModel], store: Optional[BaseStore]) -> ToolCall` [¶](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.ToolNode.inject_tool_args "Permanent link")

Injects the state and store into the tool call.

Tool arguments with types annotated as `InjectedState` and `InjectedStore` are ignored in tool schemas for generation purposes. This method injects them into tool calls for tool invocation.

Parameters:

  * **`tool_call`**(`ToolCall`) – 

The tool call to inject state and store into.

  * **`input`**(`Union[list[AnyMessage], dict[str, Any], BaseModel]`) – 

The input state to inject.

  * **`store`**(`Optional[BaseStore]`) – 

The store to inject.




Returns:

  * **`ToolCall`**(`ToolCall` ) – 

The tool call with injected state and store.




##  `InjectedState` [¶](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.InjectedState "Permanent link")

Bases: `InjectedToolArg`

Annotation for a Tool arg that is meant to be populated with the graph state.

Any Tool argument annotated with InjectedState will be hidden from a tool-calling model, so that the model doesn't attempt to generate the argument. If using ToolNode, the appropriate graph state field will be automatically injected into the model-generated tool args.

Parameters:

  * **`field`**(`Optional[str]` , default: `None` ) – 

The key from state to insert. If None, the entire state is expected to be passed in.


Example

```
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-1)fromtypingimport List
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-2)fromtyping_extensionsimport Annotated, TypedDict
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-3)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-4)fromlangchain_core.messagesimport BaseMessage, AIMessage
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-5)fromlangchain_core.toolsimport tool
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-6)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-7)fromlanggraph.prebuiltimport InjectedState, ToolNode
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-8)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-9)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-10)classAgentState(TypedDict):
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-11)  messages: List[BaseMessage]
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-12)  foo: str
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-13)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-14)@tool
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-15)defstate_tool(x: int, state: Annotated[dict, InjectedState]) -> str:
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-16)'''Do something with state.'''
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-17)  if len(state["messages"]) > 2:
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-18)    return state["foo"] + str(x)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-19)  else:
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-20)    return "not enough messages"
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-21)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-22)@tool
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-23)deffoo_tool(x: int, foo: Annotated[str, InjectedState("foo")]) -> str:
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-24)'''Do something else with state.'''
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-25)  return foo + str(x + 1)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-26)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-27)node = ToolNode([state_tool, foo_tool])
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-28)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-29)tool_call1 = {"name": "state_tool", "args": {"x": 1}, "id": "1", "type": "tool_call"}
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-30)tool_call2 = {"name": "foo_tool", "args": {"x": 1}, "id": "2", "type": "tool_call"}
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-31)state = {
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-32)  "messages": [AIMessage("", tool_calls=[tool_call1, tool_call2])],
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-33)  "foo": "bar",
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-34)}
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-35)node.invoke(state)

```


```
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-1-1)[
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-1-2)  ToolMessage(content='not enough messages', name='state_tool', tool_call_id='1'),
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-1-3)  ToolMessage(content='bar2', name='foo_tool', tool_call_id='2')
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-1-4)]

```


##  `InjectedStore` [¶](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.InjectedStore "Permanent link")

Bases: `InjectedToolArg`

Annotation for a Tool arg that is meant to be populated with LangGraph store.

Any Tool argument annotated with InjectedStore will be hidden from a tool-calling model, so that the model doesn't attempt to generate the argument. If using ToolNode, the appropriate store field will be automatically injected into the model-generated tool args. Note: if a graph is compiled with a store object, the store will be automatically propagated to the tools with InjectedStore args when using ToolNode.

Warning

`InjectedStore` annotation requires `langchain-core >= 0.3.8`

Example

```
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-1)fromtypingimport Any
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-2)fromtyping_extensionsimport Annotated
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-3)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-4)fromlangchain_core.messagesimport AIMessage
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-5)fromlangchain_core.toolsimport tool
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-6)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-7)fromlanggraph.store.memoryimport InMemoryStore
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-8)fromlanggraph.prebuiltimport InjectedStore, ToolNode
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-9)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-10)store = InMemoryStore()
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-11)store.put(("values",), "foo", {"bar": 2})
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-12)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-13)@tool
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-14)defstore_tool(x: int, my_store: Annotated[Any, InjectedStore()]) -> str:
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-15)'''Do something with store.'''
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-16)  stored_value = my_store.get(("values",), "foo").value["bar"]
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-17)  return stored_value + x
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-18)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-19)node = ToolNode([store_tool])
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-20)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-21)tool_call = {"name": "store_tool", "args": {"x": 1}, "id": "1", "type": "tool_call"}
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-22)state = {
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-23)  "messages": [AIMessage("", tool_calls=[tool_call])],
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-24)}
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-25)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-26)node.invoke(state, store=store)

```


```
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-1-1){
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-1-2)  "messages": [
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-1-3)    ToolMessage(content='3', name='store_tool', tool_call_id='1'),
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-1-4)  ]
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-1-5)}

```


##  `tools_condition(state: Union[list[AnyMessage], dict[str, Any], BaseModel], messages_key: str = 'messages') -> Literal['tools', '__end__']` [¶](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.tools_condition "Permanent link")

Use in the conditional_edge to route to the ToolNode if the last message

has tool calls. Otherwise, route to the end.

Parameters:

  * **`state`**(`Union[list[AnyMessage], dict[str, Any], BaseModel]`) – 

The state to check for tool calls. Must have a list of messages (MessageGraph) or have the "messages" key (StateGraph).




Returns:

  * `Literal['tools', '__end__']` – 

The next node to route to.




Examples:

Create a custom ReAct-style agent with tools.

```
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-1)>>> fromlangchain_anthropicimport ChatAnthropic
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-2)>>> fromlangchain_core.toolsimport tool
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-3)...
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-4)>>> fromlanggraph.graphimport StateGraph
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-5)>>> fromlanggraph.prebuiltimport ToolNode, tools_condition
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-6)>>> fromlanggraph.graph.messageimport add_messages
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-7)...
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-8)>>> fromtypingimport Annotated
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-9)>>> fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-10)...
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-11)>>> @tool
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-12)>>> defdivide(a: float, b: float) -> int:
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-13)... """Return a / b."""
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-14)...   return a / b
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-15)...
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-16)>>> llm = ChatAnthropic(model="claude-3-haiku-20240307")
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-17)>>> tools = [divide]
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-18)...
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-19)>>> classState(TypedDict):
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-20)...   messages: Annotated[list, add_messages]
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-21)>>>
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-22)>>> graph_builder = StateGraph(State)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-23)>>> graph_builder.add_node("tools", ToolNode(tools))
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-24)>>> graph_builder.add_node("chatbot", lambda state: {"messages":llm.bind_tools(tools).invoke(state['messages'])})
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-25)>>> graph_builder.add_edge("tools", "chatbot")
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-26)>>> graph_builder.add_conditional_edges(
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-27)...   "chatbot", tools_condition
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-28)... )
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-29)>>> graph_builder.set_entry_point("chatbot")
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-30)>>> graph = graph_builder.compile()
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-31)>>> graph.invoke({"messages": {"role": "user", "content": "What's 329993 divided by 13662?"}})

```


This module provides a ValidationNode class that can be used to validate tool calls in a langchain graph. It applies a pydantic schema to tool_calls in the models' outputs, and returns a ToolMessage with the validated content. If the schema is not valid, it returns a ToolMessage with the error message. The ValidationNode can be used in a StateGraph with a "messages" key or in a MessageGraph. If multiple tool calls are requested, they will be run in parallel.

##  `ValidationNode` [¶](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_validator.ValidationNode "Permanent link")

Bases: `RunnableCallable`

A node that validates all tools requests from the last AIMessage.

It can be used either in StateGraph with a "messages" key or in MessageGraph.

Note

This node does not actually **run** the tools, it only validates the tool calls, which is useful for extraction and other use cases where you need to generate structured output that conforms to a complex schema without losing the original messages and tool IDs (for use in multi-turn conversations).

Parameters:

  * **`schemas`**(`Sequence[Union[BaseTool, Type[BaseModel], Callable]]`) – 

A list of schemas to validate the tool calls with. These can be any of the following: - A pydantic BaseModel class - A BaseTool instance (the args_schema will be used) - A function (a schema will be created from the function signature)

  * **`format_error`**(`Optional[Callable[[BaseException, ToolCall, Type[BaseModel]], str]]` , default: `None` ) – 

A function that takes an exception, a ToolCall, and a schema and returns a formatted error string. By default, it returns the exception repr and a message to respond after fixing validation errors.

  * **`name`**(`str` , default: `'validation'` ) – 

The name of the node.

  * **`tags`**(`Optional[list[str]]` , default: `None` ) – 

A list of tags to add to the node.




Returns:

  * `Union[Dict[str, List[ToolMessage]], Sequence[ToolMessage]]` – 

A list of ToolMessages with the validated content or error messages.




Examples:

Example usage for re-prompting the model to generate a valid response:

```
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-1)>>> fromtypingimport Literal, Annotated
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-2)>>> fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-3)...
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-4)>>> fromlangchain_anthropicimport ChatAnthropic
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-5)>>> frompydanticimport BaseModel, validator
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-6)...
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-7)>>> fromlanggraph.graphimport END, START, StateGraph
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-8)>>> fromlanggraph.prebuiltimport ValidationNode
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-9)>>> fromlanggraph.graph.messageimport add_messages
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-10)...
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-11)...
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-12)>>> classSelectNumber(BaseModel):
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-13)...   a: int
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-14)...
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-15)...   @validator("a")
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-16)...   defa_must_be_meaningful(cls, v):
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-17)...     if v != 37:
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-18)...       raise ValueError("Only 37 is allowed")
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-19)...     return v
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-20)...
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-21)...
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-22)>>> classState(TypedDict):
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-23)...   messages: Annotated[list, add_messages]
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-24)...
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-25)>>> builder = StateGraph(State)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-26)>>> llm = ChatAnthropic(model="claude-3-haiku-20240307").bind_tools([SelectNumber])
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-27)>>> builder.add_node("model", llm)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-28)>>> builder.add_node("validation", ValidationNode([SelectNumber]))
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-29)>>> builder.add_edge(START, "model")
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-30)...
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-31)...
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-32)>>> defshould_validate(state: list) -> Literal["validation", "__end__"]:
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-33)...   if state[-1].tool_calls:
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-34)...     return "validation"
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-35)...   return END
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-36)...
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-37)...
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-38)>>> builder.add_conditional_edges("model", should_validate)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-39)...
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-40)...
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-41)>>> defshould_reprompt(state: list) -> Literal["model", "__end__"]:
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-42)...   for msg in state[::-1]:
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-43)...     # None of the tool calls were errors
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-44)...     if msg.type == "ai":
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-45)...       return END
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-46)...     if msg.additional_kwargs.get("is_error"):
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-47)...       return "model"
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-48)...   return END
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-49)...
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-50)...
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-51)>>> builder.add_conditional_edges("validation", should_reprompt)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-52)...
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-53)...
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-54)>>> graph = builder.compile()
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-55)>>> res = graph.invoke(("user", "Select a number, any number"))
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-56)>>> # Show the retry logic
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-57)>>> for msg in res:
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-58)...   msg.pretty_print()
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-59)================================ Human Message =================================
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-60)Select a number, any number
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-61)================================== Ai Message ==================================
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-62)[{'id': 'toolu_01JSjT9Pq8hGmTgmMPc6KnvM', 'input': {'a': 42}, 'name': 'SelectNumber', 'type': 'tool_use'}]
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-63)Tool Calls:
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-64)SelectNumber (toolu_01JSjT9Pq8hGmTgmMPc6KnvM)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-65)Call ID: toolu_01JSjT9Pq8hGmTgmMPc6KnvM
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-66)Args:
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-67)  a: 42
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-68)================================= Tool Message =================================
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-69)Name: SelectNumber
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-70)ValidationError(model='SelectNumber', errors=[{'loc': ('a',), 'msg': 'Only 37 is allowed', 'type': 'value_error'}])
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-71)Respond after fixing all validation errors.
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-72)================================== Ai Message ==================================
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-73)[{'id': 'toolu_01PkxSVxNxc5wqwCPW1FiSmV', 'input': {'a': 37}, 'name': 'SelectNumber', 'type': 'tool_use'}]
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-74)Tool Calls:
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-75)SelectNumber (toolu_01PkxSVxNxc5wqwCPW1FiSmV)
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-76)Call ID: toolu_01PkxSVxNxc5wqwCPW1FiSmV
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-77)Args:
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-78)  a: 37
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-79)================================= Tool Message =================================
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-80)Name: SelectNumber
[](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__codelineno-0-81){"a": 37}

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Storage  ](https://langchain-ai.github.io/langgraph/reference/store/) [ Next  Channels  ](https://langchain-ai.github.io/langgraph/reference/channels/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/reference/prebuilt/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
