---
url: https://langchain-ai.github.io/langgraphjs/reference/classes/langgraph_prebuilt.ToolNode.html
title: Untitled
date_crawled: 
---

[Back to documentation](/langgraphjs/)

  * Preparing search index...
  * The search index is not available

[API Reference](/)

[](#)

  * [API Reference](../index.html)
  * [langgraph/prebuilt](../modules/langgraph_prebuilt.html)
  * [ToolNode](langgraph_prebuilt.ToolNode.html)



# Class ToolNode<T>

A node that runs the tools requested in the last AIMessage. It can be used either in StateGraph with a "messages" key or in MessageGraph. If multiple tool calls are requested, they will be run in parallel. The output will be a list of ToolMessages, one for each tool call.

#### Example

```
import { ToolNode } from"@langchain/langgraph/prebuilt";import { tool } from"@langchain/core/tools";import { z } from"zod";import { AIMessage } from"@langchain/core/messages";constgetWeather = tool((input) => {if (["sf", "san francisco"].includes(input.location.toLowerCase())) {return"It's 60 degrees and foggy."; } else {return"It's 90 degrees and sunny."; }}, {name:"get_weather",description:"Call to get the current weather.",schema:z.object({location:z.string().describe("Location to get the weather for."), }),});consttools = [getWeather];consttoolNode = newToolNode(tools);constmessageWithSingleToolCall = newAIMessage({content:"",tool_calls: [  {name:"get_weather",args: { location:"sf" },id:"tool_call_id",type:"tool_call",  } ]})awaittoolNode.invoke({ messages: [messageWithSingleToolCall] });// Returns tool invocation responses as:// { messages: ToolMessage[] }
Copy
```


#### Example

```
import {StateGraph,MessagesAnnotation,} from"@langchain/langgraph";import { ToolNode } from"@langchain/langgraph/prebuilt";import { tool } from"@langchain/core/tools";import { z } from"zod";import { ChatAnthropic } from"@langchain/anthropic";constgetWeather = tool((input) => {if (["sf", "san francisco"].includes(input.location.toLowerCase())) {return"It's 60 degrees and foggy."; } else {return"It's 90 degrees and sunny."; }}, {name:"get_weather",description:"Call to get the current weather.",schema:z.object({location:z.string().describe("Location to get the weather for."), }),});consttools = [getWeather];constmodelWithTools = newChatAnthropic({model:"claude-3-haiku-20240307",temperature:0}).bindTools(tools);consttoolNodeForGraph = newToolNode(tools)constshouldContinue = (state: typeofMessagesAnnotation.State) => {const { messages } = state;constlastMessage = messages[messages.length - 1];if ("tool_calls"inlastMessage && Array.isArray(lastMessage.tool_calls) && lastMessage.tool_calls?.length) {return"tools"; }return"__end__";}constcallModel = async (state: typeofMessagesAnnotation.State) => {const { messages } = state;constresponse = awaitmodelWithTools.invoke(messages);return { messages:response };}constgraph = newStateGraph(MessagesAnnotation) .addNode("agent", callModel) .addNode("tools", toolNodeForGraph) .addEdge("__start__", "agent") .addConditionalEdges("agent", shouldContinue) .addEdge("tools", "agent") .compile();constinputs = {messages: [{ role:"user", content:"what is the weather in SF?" }],};conststream = awaitgraph.stream(inputs, {streamMode:"values",});forawait (const { messages } ofstream) {console.log(messages);}// Returns the messages in the state at each step of execution
Copy
```


#### Type Parameters

  * T = any



#### Hierarchy

  * RunnableCallable<[T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1), [T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1)>
    * ToolNode



  * Defined in libs/langgraph/dist/prebuilt/tool_node.d.ts:129



#####  Index

### Constructors

[constructor](langgraph_prebuilt.ToolNode.html#constructor)

### Properties

[config?](langgraph_prebuilt.ToolNode.html#config) [func](langgraph_prebuilt.ToolNode.html#func) [handleToolErrors](langgraph_prebuilt.ToolNode.html#handleToolErrors) [lc_kwargs](langgraph_prebuilt.ToolNode.html#lc_kwargs) [lc_namespace](langgraph_prebuilt.ToolNode.html#lc_namespace) [lc_runnable](langgraph_prebuilt.ToolNode.html#lc_runnable) [lc_serializable](langgraph_prebuilt.ToolNode.html#lc_serializable) [name?](langgraph_prebuilt.ToolNode.html#name) [recurse](langgraph_prebuilt.ToolNode.html#recurse) [tags?](langgraph_prebuilt.ToolNode.html#tags) [tools](langgraph_prebuilt.ToolNode.html#tools) [trace](langgraph_prebuilt.ToolNode.html#trace)

### Accessors

[lc_aliases](langgraph_prebuilt.ToolNode.html#lc_aliases) [lc_attributes](langgraph_prebuilt.ToolNode.html#lc_attributes) [lc_id](langgraph_prebuilt.ToolNode.html#lc_id) [lc_secrets](langgraph_prebuilt.ToolNode.html#lc_secrets)

### Methods

[_batchWithConfig](langgraph_prebuilt.ToolNode.html#_batchWithConfig) [_callWithConfig](langgraph_prebuilt.ToolNode.html#_callWithConfig) [_getOptionsList](langgraph_prebuilt.ToolNode.html#_getOptionsList) [_separateRunnableConfigFromCallOptions](langgraph_prebuilt.ToolNode.html#_separateRunnableConfigFromCallOptions) [_streamIterator](langgraph_prebuilt.ToolNode.html#_streamIterator) [_streamLog](langgraph_prebuilt.ToolNode.html#_streamLog) [_tracedInvoke](langgraph_prebuilt.ToolNode.html#_tracedInvoke) [_transformStreamWithConfig](langgraph_prebuilt.ToolNode.html#_transformStreamWithConfig) [asTool](langgraph_prebuilt.ToolNode.html#asTool) [assign](langgraph_prebuilt.ToolNode.html#assign) [batch](langgraph_prebuilt.ToolNode.html#batch) [bind](langgraph_prebuilt.ToolNode.html#bind) [getGraph](langgraph_prebuilt.ToolNode.html#getGraph) [getName](langgraph_prebuilt.ToolNode.html#getName) [invoke](langgraph_prebuilt.ToolNode.html#invoke) [map](langgraph_prebuilt.ToolNode.html#map) [pick](langgraph_prebuilt.ToolNode.html#pick) [pipe](langgraph_prebuilt.ToolNode.html#pipe) [run](langgraph_prebuilt.ToolNode.html#run) [stream](langgraph_prebuilt.ToolNode.html#stream) [streamEvents](langgraph_prebuilt.ToolNode.html#streamEvents) [streamLog](langgraph_prebuilt.ToolNode.html#streamLog) [toJSON](langgraph_prebuilt.ToolNode.html#toJSON) [toJSONNotImplemented](langgraph_prebuilt.ToolNode.html#toJSONNotImplemented) [transform](langgraph_prebuilt.ToolNode.html#transform) [withConfig](langgraph_prebuilt.ToolNode.html#withConfig) [withFallbacks](langgraph_prebuilt.ToolNode.html#withFallbacks) [withListeners](langgraph_prebuilt.ToolNode.html#withListeners) [withRetry](langgraph_prebuilt.ToolNode.html#withRetry) [isRunnable](langgraph_prebuilt.ToolNode.html#isRunnable) [lc_name](langgraph_prebuilt.ToolNode.html#lc_name)

## Constructors

### constructor[](#constructor)

  * new ToolNode<[T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1)>(tools, options?): [ToolNode](langgraph_prebuilt.ToolNode.html)<[T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1)>[](#constructor.new_ToolNode)
  * #### Type Parameters

    * T = any

#### Parameters

    * tools: (RunnableToolLike<ZodType<any, ZodTypeDef, any>, unknown> | StructuredToolInterface<ZodObjectAny>)[]
    * `Optional` options: [ToolNodeOptions](../types/langgraph_prebuilt.ToolNodeOptions.html)

#### Returns [ToolNode](langgraph_prebuilt.ToolNode.html)<[T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1)>

Overrides RunnableCallable<T, T>.constructor

    * Defined in libs/langgraph/dist/prebuilt/tool_node.d.ts:133



## Properties

### `Optional` config[](#config)

config?: RunnableConfig<Record<string, any>>

Inherited from RunnableCallable.config

  * Defined in libs/langgraph/dist/utils.d.ts:14



### func[](#func)

func: ((...args) => any)

#### Type declaration

  *     * (...args): any
    * #### Parameters

      * `Rest` ...args: any[]

#### Returns any




Inherited from RunnableCallable.func

  * Defined in libs/langgraph/dist/utils.d.ts:12



### handleToolErrors[](#handleToolErrors)

handleToolErrors: boolean

  * Defined in libs/langgraph/dist/prebuilt/tool_node.d.ts:131



### lc_kwargs[](#lc_kwargs)

lc_kwargs: SerializedFields

Inherited from RunnableCallable.lc_kwargs

  * Defined in node_modules/@langchain/core/dist/load/serializable.d.ts:27



### lc_namespace[](#lc_namespace)

lc_namespace: string[]

Inherited from RunnableCallable.lc_namespace

  * Defined in libs/langgraph/dist/utils.d.ts:11



### `Protected` lc_runnable[](#lc_runnable)

lc_runnable: boolean

Inherited from RunnableCallable.lc_runnable

  * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:25



### lc_serializable[](#lc_serializable)

lc_serializable: boolean

Inherited from RunnableCallable.lc_serializable

  * Defined in node_modules/@langchain/core/dist/load/serializable.d.ts:26



### `Optional` name[](#name)

name?: string

Inherited from RunnableCallable.name

  * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:26



### recurse[](#recurse)

recurse: boolean

Inherited from RunnableCallable.recurse

  * Defined in libs/langgraph/dist/utils.d.ts:16



### `Optional` tags[](#tags)

tags?: string[]

Inherited from RunnableCallable.tags

  * Defined in libs/langgraph/dist/utils.d.ts:13



### tools[](#tools)

tools: (RunnableToolLike<ZodType<any, ZodTypeDef, any>, unknown> | StructuredToolInterface<ZodObjectAny>)[]

  * Defined in libs/langgraph/dist/prebuilt/tool_node.d.ts:130



### trace[](#trace)

trace: boolean

Overrides RunnableCallable.trace

  * Defined in libs/langgraph/dist/prebuilt/tool_node.d.ts:132



## Accessors

### lc_aliases[](#lc_aliases)

  * get lc_aliases(): undefined | { [key: string]: string; }
  * A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

#### Returns undefined | { [key: string]: string; }

Inherited from RunnableCallable.lc_aliases

    * Defined in node_modules/@langchain/core/dist/load/serializable.d.ts:65



### lc_attributes[](#lc_attributes)

  * get lc_attributes(): undefined | SerializedFields
  * A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

#### Returns undefined | SerializedFields

Inherited from RunnableCallable.lc_attributes

    * Defined in node_modules/@langchain/core/dist/load/serializable.d.ts:58



### lc_id[](#lc_id)

  * get lc_id(): string[]
  * The final serialized identifier for the module.

#### Returns string[]

Inherited from RunnableCallable.lc_id

    * Defined in node_modules/@langchain/core/dist/load/serializable.d.ts:43



### lc_secrets[](#lc_secrets)

  * get lc_secrets(): undefined | { [key: string]: string; }
  * A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

#### Returns undefined | { [key: string]: string; }

Inherited from RunnableCallable.lc_secrets

    * Defined in node_modules/@langchain/core/dist/load/serializable.d.ts:49



## Methods

### _batchWithConfig[](#_batchWithConfig)

  * _batchWithConfig<[T](langgraph_prebuilt.ToolNode.html#_batchWithConfig._batchWithConfig-1.T-2)>(func, inputs, options?, batchOptions?): Promise<(Error | [T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1))[]>[](#_batchWithConfig._batchWithConfig-1)
  * Internal method that handles batching and configuration for a runnable It takes a function, input values, and optional configuration, and returns a promise that resolves to the output values.

#### Type Parameters

    * T

#### Parameters

    * func: ((inputs, options?, runManagers?, batchOptions?) => Promise<(Error | [T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1))[]>)

The function to be executed for each input value.

      *         * (inputs, options?, runManagers?, batchOptions?): Promise<(Error | [T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1))[]>
        * #### Parameters

          * inputs: [T](langgraph.CompiledStateGraph.html#_batchWithConfig._batchWithConfig-1.T)[]
          * `Optional` options: Partial<RunnableConfig<Record<string, any>>>[]
          * `Optional` runManagers: (undefined | CallbackManagerForChainRun)[]
          * `Optional` batchOptions: RunnableBatchOptions

#### Returns Promise<(Error | [T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1))[]>

    * inputs: [T](langgraph.CompiledStateGraph.html#_batchWithConfig._batchWithConfig-1.T)[]
    * `Optional` options: Partial<RunnableConfig<Record<string, any>> & { runType?: string; }> | Partial<RunnableConfig<Record<string, any>> & { runType?: string; }>[]
    * `Optional` batchOptions: RunnableBatchOptions

#### Returns Promise<(Error | [T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1))[]>

A promise that resolves to the output values.

Inherited from RunnableCallable._batchWithConfig

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:109



### `Protected` _callWithConfig[](#_callWithConfig)

  * _callWithConfig<[T](langgraph_prebuilt.ToolNode.html#_callWithConfig._callWithConfig-1.T-3)>(func, input, options?): Promise<[T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1)>[](#_callWithConfig._callWithConfig-1)
  * #### Type Parameters

    * T

#### Parameters

    * func: ((input) => Promise<[T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1)>) | ((input, config?, runManager?) => Promise<[T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1)>)
    * input: [T](langgraph.CompiledStateGraph.html#_callWithConfig._callWithConfig-1.T-1)
    * `Optional` options: Partial<RunnableConfig<Record<string, any>>> & { runType?: string; }

#### Returns Promise<[T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1)>

Inherited from RunnableCallable._callWithConfig

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:97



### `Protected` _getOptionsList[](#_getOptionsList)

  * _getOptionsList<[O](langgraph_prebuilt.ToolNode.html#_getOptionsList._getOptionsList-1.O)>(options, length?): Partial<[O](langgraph.CompiledStateGraph.html#_getOptionsList._getOptionsList-1.O-2)>[][](#_getOptionsList._getOptionsList-1)
  * #### Type Parameters

    * O extends RunnableConfig<Record<string, any>, [O](langgraph.CompiledStateGraph.html#_getOptionsList._getOptionsList-1.O-2)> & { runType?: string; }

#### Parameters

    * options: Partial<[O](langgraph.CompiledStateGraph.html#_getOptionsList._getOptionsList-1.O-2)> | Partial<[O](langgraph.CompiledStateGraph.html#_getOptionsList._getOptionsList-1.O-2)>[]
    * `Optional` length: number

#### Returns Partial<[O](langgraph.CompiledStateGraph.html#_getOptionsList._getOptionsList-1.O-2)>[]

Inherited from RunnableCallable._getOptionsList

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:64



### `Protected` _separateRunnableConfigFromCallOptions[](#_separateRunnableConfigFromCallOptions)

  * _separateRunnableConfigFromCallOptions(options?): [RunnableConfig<Record<string, any>>, Omit<Partial<RunnableConfig<Record<string, any>>>, keyof RunnableConfig<Record<string, any>>>][](#_separateRunnableConfigFromCallOptions._separateRunnableConfigFromCallOptions-1)
  * #### Parameters

    * `Optional` options: Partial<RunnableConfig<Record<string, any>>>

#### Returns [RunnableConfig<Record<string, any>>, Omit<Partial<RunnableConfig<Record<string, any>>>, keyof RunnableConfig<Record<string, any>>>]

Inherited from RunnableCallable._separateRunnableConfigFromCallOptions

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:96



### _streamIterator[](#_streamIterator)

  * _streamIterator(input, options?): AsyncGenerator<[T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1), any, unknown>[](#_streamIterator._streamIterator-1)
  * Default streaming implementation. Subclasses should override this method if they support streaming output.

#### Parameters

    * input: [T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1)
    * `Optional` options: Partial<RunnableConfig<Record<string, any>>>

#### Returns AsyncGenerator<[T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1), any, unknown>

Inherited from RunnableCallable._streamIterator

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:88



### `Protected` _streamLog[](#_streamLog)

  * _streamLog(input, logStreamCallbackHandler, config): AsyncGenerator<RunLogPatch, any, unknown>[](#_streamLog._streamLog-1)
  * #### Parameters

    * input: [T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1)
    * logStreamCallbackHandler: LogStreamCallbackHandler
    * config: Partial<RunnableConfig<Record<string, any>>>

#### Returns AsyncGenerator<RunLogPatch, any, unknown>

Inherited from RunnableCallable._streamLog

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:158



### `Protected` _tracedInvoke[](#_tracedInvoke)

  * _tracedInvoke(input, config?, runManager?): Promise<[T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1)>[](#_tracedInvoke._tracedInvoke-1)
  * #### Parameters

    * input: [T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1)
    * `Optional` config: Partial<RunnableConfig<Record<string, any>>>
    * `Optional` runManager: CallbackManagerForChainRun

#### Returns Promise<[T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1)>

Inherited from RunnableCallable._tracedInvoke

    * Defined in libs/langgraph/dist/utils.d.ts:18



### `Protected` _transformStreamWithConfig[](#_transformStreamWithConfig)

  * _transformStreamWithConfig<[I](langgraph_prebuilt.ToolNode.html#_transformStreamWithConfig._transformStreamWithConfig-1.I), [O](langgraph_prebuilt.ToolNode.html#_transformStreamWithConfig._transformStreamWithConfig-1.O-1)>(inputGenerator, transformer, options?): AsyncGenerator<[O](langgraph.CompiledStateGraph.html#_transformStreamWithConfig._transformStreamWithConfig-1.O-3), any, unknown>[](#_transformStreamWithConfig._transformStreamWithConfig-1)
  * Helper method to transform an Iterator of Input values into an Iterator of Output values, with callbacks. Use this to implement `stream()` or `transform()` in Runnable subclasses.

#### Type Parameters

    * I
    * O

#### Parameters

    * inputGenerator: AsyncGenerator<[I](langgraph.CompiledStateGraph.html#_transformStreamWithConfig._transformStreamWithConfig-1.I-2), any, unknown>
    * transformer: ((generator, runManager?, options?) => AsyncGenerator<[O](langgraph.CompiledStateGraph.html#_transformStreamWithConfig._transformStreamWithConfig-1.O-3), any, unknown>)
      *         * (generator, runManager?, options?): AsyncGenerator<[O](langgraph.CompiledStateGraph.html#_transformStreamWithConfig._transformStreamWithConfig-1.O-3), any, unknown>
        * #### Parameters

          * generator: AsyncGenerator<[I](langgraph.CompiledStateGraph.html#_transformStreamWithConfig._transformStreamWithConfig-1.I-2), any, unknown>
          * `Optional` runManager: CallbackManagerForChainRun
          * `Optional` options: Partial<RunnableConfig<Record<string, any>>>

#### Returns AsyncGenerator<[O](langgraph.CompiledStateGraph.html#_transformStreamWithConfig._transformStreamWithConfig-1.O-3), any, unknown>

    * `Optional` options: Partial<RunnableConfig<Record<string, any>>> & { runType?: string; }

#### Returns AsyncGenerator<[O](langgraph.CompiledStateGraph.html#_transformStreamWithConfig._transformStreamWithConfig-1.O-3), any, unknown>

Inherited from RunnableCallable._transformStreamWithConfig

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:119



### asTool[](#asTool)

  * asTool<[T](langgraph_prebuilt.ToolNode.html#asTool.asTool-1.T-4)>(fields): RunnableToolLike<ZodType<ToolCall | [T](langgraph.CompiledStateGraph.html#asTool.asTool-1.T-2), ZodTypeDef, ToolCall | [T](langgraph.CompiledStateGraph.html#asTool.asTool-1.T-2)>, [T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1)>[](#asTool.asTool-1)
  * Convert a runnable to a tool. Return a new instance of `RunnableToolLike` which contains the runnable, name, description and schema.

#### Type Parameters

    * T = [T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1)

#### Parameters

    * fields: { description?: string; name?: string; schema: ZodType<[T](langgraph.CompiledStateGraph.html#asTool.asTool-1.T-2), ZodTypeDef, [T](langgraph.CompiledStateGraph.html#asTool.asTool-1.T-2)>; }
      * ##### `Optional` description?: string

The description of the tool. Falls back to the description on the Zod schema if not provided, or undefined if neither are provided.

      * ##### `Optional` name?: string

The name of the tool. If not provided, it will default to the name of the runnable.

      * ##### schema: ZodType<[T](langgraph.CompiledStateGraph.html#asTool.asTool-1.T-2), ZodTypeDef, [T](langgraph.CompiledStateGraph.html#asTool.asTool-1.T-2)>

The Zod schema for the input of the tool. Infers the Zod type from the input type of the runnable.

#### Returns RunnableToolLike<ZodType<ToolCall | [T](langgraph.CompiledStateGraph.html#asTool.asTool-1.T-2), ZodTypeDef, ToolCall | [T](langgraph.CompiledStateGraph.html#asTool.asTool-1.T-2)>, [T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1)>

An instance of `RunnableToolLike` which is a runnable that can be used as a tool.

Inherited from RunnableCallable.asTool

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:305



### assign[](#assign)

  * assign(mapping): Runnable<any, any, RunnableConfig<Record<string, any>>>[](#assign.assign-1)
  * Assigns new fields to the dict output of this runnable. Returns a new runnable.

#### Parameters

    * mapping: RunnableMapLike<Record<string, unknown>, Record<string, unknown>>

#### Returns Runnable<any, any, RunnableConfig<Record<string, any>>>

Inherited from RunnableCallable.assign

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:137



### batch[](#batch)

  * batch(inputs, options?, batchOptions?): Promise<[T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1)[]>[](#batch.batch-1)
  * Default implementation of batch, which calls invoke N times. Subclasses should override this method if they can batch more efficiently.

#### Parameters

    * inputs: [T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1)[]

Array of inputs to each batch call.

    * `Optional` options: Partial<RunnableConfig<Record<string, any>>> | Partial<RunnableConfig<Record<string, any>>>[]

Either a single call options object to apply to each batch call or an array for each call.

    * `Optional` batchOptions: RunnableBatchOptions & { returnExceptions?: false; }

#### Returns Promise<[T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1)[]>

An array of RunOutputs, or mixed RunOutputs and errors if batchOptions.returnExceptions is set

Inherited from RunnableCallable.batch

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:75
  * batch(inputs, options?, batchOptions?): Promise<(Error | [T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1))[]>[](#batch.batch-2)
  * #### Parameters

    * inputs: [T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1)[]
    * `Optional` options: Partial<RunnableConfig<Record<string, any>>> | Partial<RunnableConfig<Record<string, any>>>[]
    * `Optional` batchOptions: RunnableBatchOptions & { returnExceptions: true; }

#### Returns Promise<(Error | [T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1))[]>

Inherited from RunnableCallable.batch

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:78
  * batch(inputs, options?, batchOptions?): Promise<(Error | [T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1))[]>[](#batch.batch-3)
  * #### Parameters

    * inputs: [T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1)[]
    * `Optional` options: Partial<RunnableConfig<Record<string, any>>> | Partial<RunnableConfig<Record<string, any>>>[]
    * `Optional` batchOptions: RunnableBatchOptions

#### Returns Promise<(Error | [T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1))[]>

Inherited from RunnableCallable.batch

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:81



### bind[](#bind)

  * bind(kwargs): Runnable<[T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1), [T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1), RunnableConfig<Record<string, any>>>[](#bind.bind-1)
  * Bind arguments to a Runnable, returning a new Runnable.

#### Parameters

    * kwargs: Partial<RunnableConfig<Record<string, any>>>

#### Returns Runnable<[T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1), [T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1), RunnableConfig<Record<string, any>>>

A new RunnableBinding that, when invoked, will apply the bound args.

Inherited from RunnableCallable.bind

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:34



### getGraph[](#getGraph)

  * getGraph(_?): Graph[](#getGraph.getGraph-1)
  * #### Parameters

    * `Optional` _: RunnableConfig<Record<string, any>>

#### Returns Graph

Inherited from RunnableCallable.getGraph

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:122



### getName[](#getName)

  * getName(suffix?): string[](#getName.getName-1)
  * #### Parameters

    * `Optional` suffix: string

#### Returns string

Inherited from RunnableCallable.getName

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:27



### invoke[](#invoke)

  * invoke(input, options?): Promise<[T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1)>[](#invoke.invoke-1)
  * #### Parameters

    * input: [T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1)
    * `Optional` options: Partial<RunnableConfig<Record<string, any>>>

#### Returns Promise<[T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1)>

Inherited from RunnableCallable.invoke

    * Defined in libs/langgraph/dist/utils.d.ts:19



### map[](#map)

  * map(): Runnable<[T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1)[], [T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1)[], RunnableConfig<Record<string, any>>>[](#map.map-1)
  * Return a new Runnable that maps a list of inputs to a list of outputs, by calling invoke() with each input.

#### Returns Runnable<[T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1)[], [T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1)[], RunnableConfig<Record<string, any>>>

Inherited from RunnableCallable.map

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:39



### pick[](#pick)

  * pick(keys): Runnable<any, any, RunnableConfig<Record<string, any>>>[](#pick.pick-1)
  * Pick keys from the dict output of this runnable. Returns a new runnable.

#### Parameters

    * keys: string | string[]

#### Returns Runnable<any, any, RunnableConfig<Record<string, any>>>

Inherited from RunnableCallable.pick

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:133



### pipe[](#pipe)

  * pipe<[NewRunOutput](langgraph_prebuilt.ToolNode.html#pipe.pipe-1.NewRunOutput)>(coerceable): Runnable<[T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1), Exclude<[NewRunOutput](langgraph.CompiledStateGraph.html#pipe.pipe-1.NewRunOutput), Error>, RunnableConfig<Record<string, any>>>[](#pipe.pipe-1)
  * Create a new runnable sequence that runs each individual runnable in series, piping the output of one runnable into another runnable or runnable-like.

#### Type Parameters

    * NewRunOutput

#### Parameters

    * coerceable: RunnableLike<[T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1), [NewRunOutput](langgraph.CompiledStateGraph.html#pipe.pipe-1.NewRunOutput), RunnableConfig<Record<string, any>>>

A runnable, function, or object whose values are functions or runnables.

#### Returns Runnable<[T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1), Exclude<[NewRunOutput](langgraph.CompiledStateGraph.html#pipe.pipe-1.NewRunOutput), Error>, RunnableConfig<Record<string, any>>>

A new runnable sequence.

Inherited from RunnableCallable.pipe

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:129



### `Protected` run[](#run)

  * run(input, config): Promise<[T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1)>[](#run.run-1)
  * #### Parameters

    * input: any
    * config: RunnableConfig<Record<string, any>>

#### Returns Promise<[T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1)>

    * Defined in libs/langgraph/dist/prebuilt/tool_node.d.ts:134



### stream[](#stream)

  * stream(input, options?): Promise<IterableReadableStream<[T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1)>>[](#stream.stream-1)
  * Stream output in chunks.

#### Parameters

    * input: [T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1)
    * `Optional` options: Partial<RunnableConfig<Record<string, any>>>

#### Returns Promise<IterableReadableStream<[T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1)>>

A readable stream that is also an iterable.

Inherited from RunnableCallable.stream

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:95



### streamEvents[](#streamEvents)

  * streamEvents(input, options, streamOptions?): IterableReadableStream<StreamEvent>[](#streamEvents.streamEvents-1)
  * Generate a stream of events emitted by the internal steps of the runnable.

Use to create an iterator over StreamEvents that provide real-time information about the progress of the runnable, including StreamEvents from intermediate results.

A StreamEvent is a dictionary with the following schema:

    * `event`: string - Event names are of the format: on_[runnable_type]_(start|stream|end).
    * `name`: string - The name of the runnable that generated the event.
    * `run_id`: string - Randomly generated ID associated with the given execution of the runnable that emitted the event. A child runnable that gets invoked as part of the execution of a parent runnable is assigned its own unique ID.
    * `tags`: string[] - The tags of the runnable that generated the event.
    * `metadata`: Record<string, any> - The metadata of the runnable that generated the event.
    * `data`: Record<string, any>

Below is a table that illustrates some events that might be emitted by various chains. Metadata fields have been omitted from the table for brevity. Chain definitions have been included after the table.

**ATTENTION** This reference table is for the V2 version of the schema.

```
+----------------------+-----------------------------+------------------------------------------+| event        | input            | output/chunk               |+======================+=============================+==========================================+| on_chat_model_start | {"messages": BaseMessage[]} |                     |+----------------------+-----------------------------+------------------------------------------+| on_chat_model_stream |               | AIMessageChunk("hello")         |+----------------------+-----------------------------+------------------------------------------+| on_chat_model_end  | {"messages": BaseMessage[]} | AIMessageChunk("hello world")      |+----------------------+-----------------------------+------------------------------------------+| on_llm_start     | {'input': 'hello'}     |                     |+----------------------+-----------------------------+------------------------------------------+| on_llm_stream    |               | 'Hello'                 |+----------------------+-----------------------------+------------------------------------------+| on_llm_end      | 'Hello human!'       |                     |+----------------------+-----------------------------+------------------------------------------+| on_chain_start    |               |                     |+----------------------+-----------------------------+------------------------------------------+| on_chain_stream   |               | "hello world!"              |+----------------------+-----------------------------+------------------------------------------+| on_chain_end     | [Document(...)]       | "hello world!, goodbye world!"      |+----------------------+-----------------------------+------------------------------------------+| on_tool_start    | {"x": 1, "y": "2"}     |                     |+----------------------+-----------------------------+------------------------------------------+| on_tool_end     |               | {"x": 1, "y": "2"}            |+----------------------+-----------------------------+------------------------------------------+| on_retriever_start  | {"query": "hello"}     |                     |+----------------------+-----------------------------+------------------------------------------+| on_retriever_end   | {"query": "hello"}     | [Document(...), ..]           |+----------------------+-----------------------------+------------------------------------------+| on_prompt_start   | {"question": "hello"}    |                     |+----------------------+-----------------------------+------------------------------------------+| on_prompt_end    | {"question": "hello"}    | ChatPromptValue(messages: BaseMessage[]) |+----------------------+-----------------------------+------------------------------------------+
Copy
```


The "on_chain_*" events are the default for Runnables that don't fit one of the above categories.

In addition to the standard events above, users can also dispatch custom events.

Custom events will be only be surfaced with in the `v2` version of the API!

A custom event has following format:

```
+-----------+------+------------------------------------------------------------+| Attribute | Type | Description                        |+===========+======+============================================================+| name   | str | A user defined name for the event.             |+-----------+------+------------------------------------------------------------+| data   | Any | The data associated with the event. This can be anything. |+-----------+------+------------------------------------------------------------+
Copy
```


Here's an example:

```
import { RunnableLambda } from"@langchain/core/runnables";import { dispatchCustomEvent } from"@langchain/core/callbacks/dispatch";// Use this import for web environments that don't support "async_hooks"// and manually pass config to child runs.// import { dispatchCustomEvent } from "@langchain/core/callbacks/dispatch/web";constslowThing = RunnableLambda.from(async (someInput: string) => {// Placeholder for some slow operationawaitnewPromise((resolve) =>setTimeout(resolve, 100));awaitdispatchCustomEvent("progress_event", {message:"Finished step 1 of 2", });awaitnewPromise((resolve) =>setTimeout(resolve, 100));return"Done";});consteventStream = awaitslowThing.streamEvents("hello world", {version:"v2",});forawait (consteventofeventStream) {if (event.event === "on_custom_event") {console.log(event); }}
Copy
```


#### Parameters

    * input: [T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1)
    * options: Partial<RunnableConfig<Record<string, any>>> & { version: "v1" | "v2"; }
    * `Optional` streamOptions: Omit<EventStreamCallbackHandlerInput, "autoClose">

#### Returns IterableReadableStream<StreamEvent>

Inherited from RunnableCallable.streamEvents

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:267
  * streamEvents(input, options, streamOptions?): IterableReadableStream<Uint8Array>[](#streamEvents.streamEvents-2)
  * #### Parameters

    * input: [T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1)
    * options: Partial<RunnableConfig<Record<string, any>>> & { encoding: "text/event-stream"; version: "v1" | "v2"; }
    * `Optional` streamOptions: Omit<EventStreamCallbackHandlerInput, "autoClose">

#### Returns IterableReadableStream<Uint8Array>

Inherited from RunnableCallable.streamEvents

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:270



### streamLog[](#streamLog)

  * streamLog(input, options?, streamOptions?): AsyncGenerator<RunLogPatch, any, unknown>[](#streamLog.streamLog-1)
  * Stream all output from a runnable, as reported to the callback system. This includes all inner runs of LLMs, Retrievers, Tools, etc. Output is streamed as Log objects, which include a list of jsonpatch ops that describe how the state of the run has changed in each step, and the final state of the run. The jsonpatch ops can be applied in order to construct state.

#### Parameters

    * input: [T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1)
    * `Optional` options: Partial<RunnableConfig<Record<string, any>>>
    * `Optional` streamOptions: Omit<LogStreamCallbackHandlerInput, "autoClose">

#### Returns AsyncGenerator<RunLogPatch, any, unknown>

Inherited from RunnableCallable.streamLog

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:157



### toJSON[](#toJSON)

  * toJSON(): Serialized[](#toJSON.toJSON-1)
  * #### Returns Serialized

Inherited from RunnableCallable.toJSON

    * Defined in node_modules/@langchain/core/dist/load/serializable.d.ts:69



### toJSONNotImplemented[](#toJSONNotImplemented)

  * toJSONNotImplemented(): SerializedNotImplemented[](#toJSONNotImplemented.toJSONNotImplemented-1)
  * #### Returns SerializedNotImplemented

Inherited from RunnableCallable.toJSONNotImplemented

    * Defined in node_modules/@langchain/core/dist/load/serializable.d.ts:70



### transform[](#transform)

  * transform(generator, options): AsyncGenerator<[T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1), any, unknown>[](#transform.transform-1)
  * Default implementation of transform, which buffers input and then calls stream. Subclasses should override this method if they can start producing output while input is still being generated.

#### Parameters

    * generator: AsyncGenerator<[T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1), any, unknown>
    * options: Partial<RunnableConfig<Record<string, any>>>

#### Returns AsyncGenerator<[T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1), any, unknown>

Inherited from RunnableCallable.transform

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:145



### withConfig[](#withConfig)

  * withConfig(config): Runnable<[T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1), [T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1), RunnableConfig<Record<string, any>>>[](#withConfig.withConfig-1)
  * Bind config to a Runnable, returning a new Runnable.

#### Parameters

    * config: RunnableConfig<Record<string, any>>

New configuration parameters to attach to the new runnable.

#### Returns Runnable<[T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1), [T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1), RunnableConfig<Record<string, any>>>

A new RunnableBinding with a config matching what's passed.

Inherited from RunnableCallable.withConfig

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:54



### withFallbacks[](#withFallbacks)

  * withFallbacks(fields): RunnableWithFallbacks<[T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1), [T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1)>[](#withFallbacks.withFallbacks-1)
  * Create a new runnable from the current one that will try invoking other passed fallback runnables if the initial invocation fails.

#### Parameters

    * fields: { fallbacks: Runnable<[T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1), [T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1), RunnableConfig<Record<string, any>>>[]; } | Runnable<[T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1), [T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1), RunnableConfig<Record<string, any>>>[]

#### Returns RunnableWithFallbacks<[T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1), [T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1)>

A new RunnableWithFallbacks.

Inherited from RunnableCallable.withFallbacks

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:61



### withListeners[](#withListeners)

  * withListeners(params): Runnable<[T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1), [T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1), RunnableConfig<Record<string, any>>>[](#withListeners.withListeners-1)
  * Bind lifecycle listeners to a Runnable, returning a new Runnable. The Run object contains information about the run, including its id, type, input, output, error, startTime, endTime, and any tags or metadata added to the run.

#### Parameters

    * params: { onEnd?: ((run, config?) => void | Promise<void>); onError?: ((run, config?) => void | Promise<void>); onStart?: ((run, config?) => void | Promise<void>); }

The object containing the callback functions.

      * ##### `Optional` onEnd?: ((run, config?) => void | Promise<void>)

Called after the runnable finishes running, with the Run object.

        *           * (run, config?): void | Promise<void>
          * #### Parameters

            * run: Run
            * `Optional` config: RunnableConfig<Record<string, any>>

#### Returns void | Promise<void>

      * ##### `Optional` onError?: ((run, config?) => void | Promise<void>)

Called if the runnable throws an error, with the Run object.

        *           * (run, config?): void | Promise<void>
          * #### Parameters

            * run: Run
            * `Optional` config: RunnableConfig<Record<string, any>>

#### Returns void | Promise<void>

      * ##### `Optional` onStart?: ((run, config?) => void | Promise<void>)

Called before the runnable starts running, with the Run object.

        *           * (run, config?): void | Promise<void>
          * #### Parameters

            * run: Run
            * `Optional` config: RunnableConfig<Record<string, any>>

#### Returns void | Promise<void>

#### Returns Runnable<[T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1), [T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1), RunnableConfig<Record<string, any>>>

Inherited from RunnableCallable.withListeners

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:288



### withRetry[](#withRetry)

  * withRetry(fields?): RunnableRetry<[T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1), [T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1), RunnableConfig<Record<string, any>>>[](#withRetry.withRetry-1)
  * Add retry logic to an existing runnable.

#### Parameters

    * `Optional` fields: { onFailedAttempt?: RunnableRetryFailedAttemptHandler; stopAfterAttempt?: number; }
      * ##### `Optional` onFailedAttempt?: RunnableRetryFailedAttemptHandler

      * ##### `Optional` stopAfterAttempt?: number

#### Returns RunnableRetry<[T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1), [T](langgraph_prebuilt.ToolNode.html#constructor.new_ToolNode.T-1), RunnableConfig<Record<string, any>>>

A new RunnableRetry that, when invoked, will retry according to the parameters.

Inherited from RunnableCallable.withRetry

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:45



### `Static` isRunnable[](#isRunnable)

  * isRunnable(thing): thing is Runnable<any, any, RunnableConfig<Record<string, any>>>[](#isRunnable.isRunnable-1)
  * #### Parameters

    * thing: any

#### Returns thing is Runnable<any, any, RunnableConfig<Record<string, any>>>

Inherited from RunnableCallable.isRunnable

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:276



### `Static` lc_name[](#lc_name)

  * lc_name(): string[](#lc_name.lc_name-1)
  * The name of the serializable. Override to provide an alias or to preserve the serialized module name in minified environments.

Implemented as a static method to support loading logic.

#### Returns string

Inherited from RunnableCallable.lc_name

    * Defined in node_modules/@langchain/core/dist/load/serializable.d.ts:39



### Settings

#### Member Visibility

  * Protected
  * Private
  * Inherited
  * External



#### Theme

OSLightDark

### On This Page

[constructor](#constructor)[config](#config)[func](#func)[handleToolErrors](#handleToolErrors)[lc_kwargs](#lc_kwargs)[lc_namespace](#lc_namespace)[lc_runnable](#lc_runnable)[lc_serializable](#lc_serializable)[name](#name)[recurse](#recurse)[tags](#tags)[tools](#tools)[trace](#trace)[lc_aliases](#lc_aliases)[lc_attributes](#lc_attributes)[lc_id](#lc_id)[lc_secrets](#lc_secrets)[_batchWithConfig](#_batchWithConfig)[_callWithConfig](#_callWithConfig)[_getOptionsList](#_getOptionsList)[_separateRunnableConfigFromCallOptions](#_separateRunnableConfigFromCallOptions)[_streamIterator](#_streamIterator)[_streamLog](#_streamLog)[_tracedInvoke](#_tracedInvoke)[_transformStreamWithConfig](#_transformStreamWithConfig)[asTool](#asTool)[assign](#assign)[batch](#batch)[bind](#bind)[getGraph](#getGraph)[getName](#getName)[invoke](#invoke)[map](#map)[pick](#pick)[pipe](#pipe)[run](#run)[stream](#stream)[streamEvents](#streamEvents)[streamLog](#streamLog)[toJSON](#toJSON)[toJSONNotImplemented](#toJSONNotImplemented)[transform](#transform)[withConfig](#withConfig)[withFallbacks](#withFallbacks)[withListeners](#withListeners)[withRetry](#withRetry)[isRunnable](#isRunnable)[lc_name](#lc_name)

[API Reference](../index.html)

  * [checkpoint](../modules/checkpoint.html)

    * [AsyncBatchedStore](../classes/checkpoint.AsyncBatchedStore.html)
    * [BaseCheckpointSaver](../classes/checkpoint.BaseCheckpointSaver.html)
    * [BaseStore](../classes/checkpoint.BaseStore.html)
    * [InMemoryStore](../classes/checkpoint.InMemoryStore.html)
    * [InvalidNamespaceError](../classes/checkpoint.InvalidNamespaceError.html)
    * [MemorySaver](../classes/checkpoint.MemorySaver.html)
    * [MemoryStore](../classes/checkpoint.MemoryStore.html)
    * [ChannelProtocol](../interfaces/checkpoint.ChannelProtocol.html)
    * [Checkpoint](../interfaces/checkpoint.Checkpoint.html)
    * [CheckpointMetadata](../interfaces/checkpoint.CheckpointMetadata.html)
    * [CheckpointTuple](../interfaces/checkpoint.CheckpointTuple.html)
    * [GetOperation](../interfaces/checkpoint.GetOperation.html)
    * [IndexConfig](../interfaces/checkpoint.IndexConfig.html)
    * [Item](../interfaces/checkpoint.Item.html)
    * [ListNamespacesOperation](../interfaces/checkpoint.ListNamespacesOperation.html)
    * [MatchCondition](../interfaces/checkpoint.MatchCondition.html)
    * [PutOperation](../interfaces/checkpoint.PutOperation.html)
    * [ReadonlyCheckpoint](../interfaces/checkpoint.ReadonlyCheckpoint.html)
    * [SearchItem](../interfaces/checkpoint.SearchItem.html)
    * [SearchOperation](../interfaces/checkpoint.SearchOperation.html)
    * [SendProtocol](../interfaces/checkpoint.SendProtocol.html)
    * [SerializerProtocol](../interfaces/checkpoint.SerializerProtocol.html)
    * [All](../types/checkpoint.All.html)
    * [ChannelVersions](../types/checkpoint.ChannelVersions.html)
    * [CheckpointListOptions](../types/checkpoint.CheckpointListOptions.html)
    * [CheckpointPendingWrite](../types/checkpoint.CheckpointPendingWrite.html)
    * [NameSpacePath](../types/checkpoint.NameSpacePath.html)
    * [NamespaceMatchType](../types/checkpoint.NamespaceMatchType.html)
    * [Operation](../types/checkpoint.Operation.html)
    * [OperationResults](../types/checkpoint.OperationResults.html)
    * [PendingWrite](../types/checkpoint.PendingWrite.html)
    * [PendingWriteValue](../types/checkpoint.PendingWriteValue.html)
    * [ERROR](../variables/checkpoint.ERROR.html)
    * [INTERRUPT](../variables/checkpoint.INTERRUPT.html)
    * [RESUME](../variables/checkpoint.RESUME.html)
    * [SCHEDULED](../variables/checkpoint.SCHEDULED.html)
    * [TASKS](../variables/checkpoint.TASKS.html)
    * [WRITES_IDX_MAP](../variables/checkpoint.WRITES_IDX_MAP.html)
    * [compareChannelVersions](../functions/checkpoint.compareChannelVersions.html)
    * [deepCopy](../functions/checkpoint.deepCopy.html)
    * [getCheckpointId](../functions/checkpoint.getCheckpointId.html)
    * [getTextAtPath](../functions/checkpoint.getTextAtPath.html)
    * [maxChannelVersion](../functions/checkpoint.maxChannelVersion.html)
    * [tokenizePath](../functions/checkpoint.tokenizePath.html)
    * [uuid5](../functions/checkpoint.uuid5.html)
    * [uuid6](../functions/checkpoint.uuid6.html)

  * [checkpoint-mongodb](../modules/checkpoint_mongodb.html)

    * [MongoDBSaver](../classes/checkpoint_mongodb.MongoDBSaver.html)
    * [MongoDBSaverParams](../types/checkpoint_mongodb.MongoDBSaverParams.html)

  * [checkpoint-postgres](../modules/checkpoint_postgres.html)

    * [PostgresSaver](../classes/checkpoint_postgres.PostgresSaver.html)

  * [checkpoint-sqlite](../modules/checkpoint_sqlite.html)

    * [SqliteSaver](../classes/checkpoint_sqlite.SqliteSaver.html)

  * [checkpoint-validation](../modules/checkpoint_validation.html)

    * [CheckpointSaverTestInitializer](../interfaces/checkpoint_validation.CheckpointSaverTestInitializer.html)
    * [getTupleTests](../functions/checkpoint_validation.getTupleTests.html)
    * [listTests](../functions/checkpoint_validation.listTests.html)
    * [putTests](../functions/checkpoint_validation.putTests.html)
    * [putWritesTests](../functions/checkpoint_validation.putWritesTests.html)
    * [specTest](../functions/checkpoint_validation.specTest.html)
    * [validate](../functions/checkpoint_validation.validate.html)

  * [langgraph](../modules/langgraph.html)

    * [AsyncBatchedStore](../modules/langgraph.html#AsyncBatchedStore)
    * [BaseCheckpointSaver](../modules/langgraph.html#BaseCheckpointSaver)
    * [BaseStore](../modules/langgraph.html#BaseStore)
    * [Checkpoint](../modules/langgraph.html#Checkpoint)
    * [CheckpointMetadata](../modules/langgraph.html#CheckpointMetadata)
    * [CheckpointTuple](../modules/langgraph.html#CheckpointTuple)
    * [GetOperation](../modules/langgraph.html#GetOperation)
    * [InMemoryStore](../modules/langgraph.html#InMemoryStore)
    * [Item](../modules/langgraph.html#Item)
    * [ListNamespacesOperation](../modules/langgraph.html#ListNamespacesOperation)
    * [MatchCondition](../modules/langgraph.html#MatchCondition)
    * [MemorySaver](../modules/langgraph.html#MemorySaver)
    * [NameSpacePath](../modules/langgraph.html#NameSpacePath)
    * [NamespaceMatchType](../modules/langgraph.html#NamespaceMatchType)
    * [Operation](../modules/langgraph.html#Operation)
    * [OperationResults](../modules/langgraph.html#OperationResults)
    * [PutOperation](../modules/langgraph.html#PutOperation)
    * [SearchOperation](../modules/langgraph.html#SearchOperation)
    * [addMessages](../modules/langgraph.html#addMessages)
    * [Annotation](../modules/langgraph.Annotation.html)

      * [Root](../functions/langgraph.Annotation.Root.html)

    * [AnnotationRoot](../classes/langgraph.AnnotationRoot.html)
    * [AnyValue](../classes/langgraph.AnyValue.html)
    * [BaseChannel](../classes/langgraph.BaseChannel.html)
    * [BaseLangGraphError](../classes/langgraph.BaseLangGraphError.html)
    * [BinaryOperatorAggregate](../classes/langgraph.BinaryOperatorAggregate.html)
    * [Command](../classes/langgraph.Command.html)
    * [CompiledGraph](../classes/langgraph.CompiledGraph.html)
    * [CompiledStateGraph](../classes/langgraph.CompiledStateGraph.html)
    * [DynamicBarrierValue](../classes/langgraph.DynamicBarrierValue.html)
    * [EmptyChannelError](../classes/langgraph.EmptyChannelError.html)
    * [EmptyInputError](../classes/langgraph.EmptyInputError.html)
    * [EphemeralValue](../classes/langgraph.EphemeralValue.html)
    * [Graph](../classes/langgraph.Graph.html)
    * [GraphBubbleUp](../classes/langgraph.GraphBubbleUp.html)
    * [GraphInterrupt](../classes/langgraph.GraphInterrupt.html)
    * [GraphRecursionError](../classes/langgraph.GraphRecursionError.html)
    * [GraphValueError](../classes/langgraph.GraphValueError.html)
    * [InvalidUpdateError](../classes/langgraph.InvalidUpdateError.html)
    * [IsLastStepManager](../classes/langgraph.IsLastStepManager.html)
    * [LastValue](../classes/langgraph.LastValue.html)
    * [ManagedValue](../classes/langgraph.ManagedValue.html)
    * [ManagedValueMapping](../classes/langgraph.ManagedValueMapping.html)
    * [MultipleSubgraphsError](../classes/langgraph.MultipleSubgraphsError.html)
    * [NamedBarrierValue](../classes/langgraph.NamedBarrierValue.html)
    * [NodeInterrupt](../classes/langgraph.NodeInterrupt.html)
    * [NoopManagedValue](../classes/langgraph.NoopManagedValue.html)
    * [ParentCommand](../classes/langgraph.ParentCommand.html)
    * [Pregel](../classes/langgraph.Pregel.html)
    * [PregelNode](../classes/langgraph.PregelNode.html)
    * [RemoteException](../classes/langgraph.RemoteException.html)
    * [Send](../classes/langgraph.Send.html)
    * [SharedValue](../classes/langgraph.SharedValue.html)
    * [StateGraph](../classes/langgraph.StateGraph.html)
    * [Topic](../classes/langgraph.Topic.html)
    * [UnreachableNodeError](../classes/langgraph.UnreachableNodeError.html)
    * [WritableManagedValue](../classes/langgraph.WritableManagedValue.html)
    * [ConfiguredManagedValue](../interfaces/langgraph.ConfiguredManagedValue.html)
    * [LangGraphRunnableConfig](../interfaces/langgraph.LangGraphRunnableConfig.html)
    * [ManagedValueParams](../interfaces/langgraph.ManagedValueParams.html)
    * [PregelOptions](../interfaces/langgraph.PregelOptions.html)
    * [SharedValueParams](../interfaces/langgraph.SharedValueParams.html)
    * [StateDefinition](../interfaces/langgraph.StateDefinition.html)
    * [StateGraphArgs](../interfaces/langgraph.StateGraphArgs.html)
    * [StateSnapshot](../interfaces/langgraph.StateSnapshot.html)
    * [WaitForNames](../interfaces/langgraph.WaitForNames.html)
    * [BaseLangGraphErrorFields](../types/langgraph.BaseLangGraphErrorFields.html)
    * [BinaryOperator](../types/langgraph.BinaryOperator.html)
    * [CommandParams](../types/langgraph.CommandParams.html)
    * [EntrypointOptions](../types/langgraph.EntrypointOptions.html)
    * [Interrupt](../types/langgraph.Interrupt.html)
    * [ManagedValueSpec](../types/langgraph.ManagedValueSpec.html)
    * [Messages](../types/langgraph.Messages.html)
    * [NodeType](../types/langgraph.NodeType.html)
    * [PregelParams](../types/langgraph.PregelParams.html)
    * [RetryPolicy](../types/langgraph.RetryPolicy.html)
    * [SingleReducer](../types/langgraph.SingleReducer.html)
    * [StateType](../types/langgraph.StateType.html)
    * [StreamMode](../types/langgraph.StreamMode.html)
    * [TaskOptions](../types/langgraph.TaskOptions.html)
    * [UpdateType](../types/langgraph.UpdateType.html)
    * [ChannelKeyPlaceholder](../variables/langgraph.ChannelKeyPlaceholder.html)
    * [END](../variables/langgraph.END.html)
    * [MessagesAnnotation](../variables/langgraph.MessagesAnnotation.html)
    * [START](../variables/langgraph.START.html)
    * [entrypoint](../functions/langgraph.entrypoint.html)
    * [getPreviousState](../functions/langgraph.getPreviousState.html)
    * [getStore](../functions/langgraph.getStore.html)
    * [getSubgraphsSeenSet](../functions/langgraph.getSubgraphsSeenSet.html)
    * [getWriter](../functions/langgraph.getWriter.html)
    * [interrupt](../functions/langgraph.interrupt-1.html)
    * [isCommand](../functions/langgraph.isCommand.html)
    * [isConfiguredManagedValue](../functions/langgraph.isConfiguredManagedValue.html)
    * [isGraphBubbleUp](../functions/langgraph.isGraphBubbleUp.html)
    * [isGraphInterrupt](../functions/langgraph.isGraphInterrupt.html)
    * [isManagedValue](../functions/langgraph.isManagedValue.html)
    * [isParentCommand](../functions/langgraph.isParentCommand.html)
    * [messagesStateReducer](../functions/langgraph.messagesStateReducer.html)
    * [task](../functions/langgraph.task.html)
    * [prebuilt](../modules/langgraph_prebuilt.html)

      * [ToolExecutor](../classes/langgraph_prebuilt.ToolExecutor.html)
      * [ToolNode](../classes/langgraph_prebuilt.ToolNode.html)
      * [ActionRequest](../interfaces/langgraph_prebuilt.ActionRequest.html)
      * [AgentState](../interfaces/langgraph_prebuilt.AgentState.html)
      * [HumanInterrupt](../interfaces/langgraph_prebuilt.HumanInterrupt.html)
      * [HumanInterruptConfig](../interfaces/langgraph_prebuilt.HumanInterruptConfig.html)
      * [ToolExecutorArgs](../interfaces/langgraph_prebuilt.ToolExecutorArgs.html)
      * [ToolInvocationInterface](../interfaces/langgraph_prebuilt.ToolInvocationInterface.html)
      * [CreateReactAgentParams](../types/langgraph_prebuilt.CreateReactAgentParams.html)
      * [FunctionCallingExecutorState](../types/langgraph_prebuilt.FunctionCallingExecutorState.html)
      * [HumanResponse](../types/langgraph_prebuilt.HumanResponse.html)
      * [ToolNodeOptions](../types/langgraph_prebuilt.ToolNodeOptions.html)
      * [createFunctionCallingExecutor](../functions/langgraph_prebuilt.createFunctionCallingExecutor.html)
      * [createReactAgent](../functions/langgraph_prebuilt.createReactAgent.html)
      * [toolsCondition](../functions/langgraph_prebuilt.toolsCondition.html)

    * [pregel](../modules/langgraph_pregel.html)

      * [Pregel](../modules/langgraph_pregel.html#Pregel)
      * [PregelOptions](../modules/langgraph_pregel.html#PregelOptions)
      * [Channel](../classes/langgraph_pregel.Channel.html)
      * [PregelInputType](../types/langgraph_pregel.PregelInputType.html)
      * [PregelOutputType](../types/langgraph_pregel.PregelOutputType.html)

    * [remote](../modules/langgraph_remote.html)

      * [RemoteGraph](../classes/langgraph_remote.RemoteGraph.html)
      * [RemoteGraphParams](../types/langgraph_remote.RemoteGraphParams.html)

    * [web](../modules/langgraph_web.html)

      * [Annotation](../modules/langgraph_web.html#Annotation)
      * [AnnotationRoot](../modules/langgraph_web.html#AnnotationRoot)
      * [AnyValue](../modules/langgraph_web.html#AnyValue)
      * [AsyncBatchedStore](../modules/langgraph_web.html#AsyncBatchedStore)
      * [BaseChannel](../modules/langgraph_web.html#BaseChannel)
      * [BaseCheckpointSaver](../modules/langgraph_web.html#BaseCheckpointSaver)
      * [BaseLangGraphError](../modules/langgraph_web.html#BaseLangGraphError)
      * [BaseLangGraphErrorFields](../modules/langgraph_web.html#BaseLangGraphErrorFields)
      * [BaseStore](../modules/langgraph_web.html#BaseStore)
      * [BinaryOperator](../modules/langgraph_web.html#BinaryOperator)
      * [BinaryOperatorAggregate](../modules/langgraph_web.html#BinaryOperatorAggregate)
      * [ChannelKeyPlaceholder](../modules/langgraph_web.html#ChannelKeyPlaceholder)
      * [Checkpoint](../modules/langgraph_web.html#Checkpoint)
      * [CheckpointMetadata](../modules/langgraph_web.html#CheckpointMetadata)
      * [CheckpointTuple](../modules/langgraph_web.html#CheckpointTuple)
      * [Command](../modules/langgraph_web.html#Command)
      * [CommandParams](../modules/langgraph_web.html#CommandParams)
      * [CompiledGraph](../modules/langgraph_web.html#CompiledGraph)
      * [CompiledStateGraph](../modules/langgraph_web.html#CompiledStateGraph)
      * [ConfiguredManagedValue](../modules/langgraph_web.html#ConfiguredManagedValue)
      * [DynamicBarrierValue](../modules/langgraph_web.html#DynamicBarrierValue)
      * [END](../modules/langgraph_web.html#END)
      * [EmptyChannelError](../modules/langgraph_web.html#EmptyChannelError)
      * [EmptyInputError](../modules/langgraph_web.html#EmptyInputError)
      * [EntrypointOptions](../modules/langgraph_web.html#EntrypointOptions)
      * [EphemeralValue](../modules/langgraph_web.html#EphemeralValue)
      * [GetOperation](../modules/langgraph_web.html#GetOperation)
      * [Graph](../modules/langgraph_web.html#Graph)
      * [GraphBubbleUp](../modules/langgraph_web.html#GraphBubbleUp)
      * [GraphInterrupt](../modules/langgraph_web.html#GraphInterrupt)
      * [GraphRecursionError](../modules/langgraph_web.html#GraphRecursionError)
      * [GraphValueError](../modules/langgraph_web.html#GraphValueError)
      * [InMemoryStore](../modules/langgraph_web.html#InMemoryStore)
      * [Interrupt](../modules/langgraph_web.html#Interrupt)
      * [InvalidUpdateError](../modules/langgraph_web.html#InvalidUpdateError)
      * [IsLastStepManager](../modules/langgraph_web.html#IsLastStepManager)
      * [Item](../modules/langgraph_web.html#Item)
      * [LangGraphRunnableConfig](../modules/langgraph_web.html#LangGraphRunnableConfig)
      * [LastValue](../modules/langgraph_web.html#LastValue)
      * [ListNamespacesOperation](../modules/langgraph_web.html#ListNamespacesOperation)
      * [ManagedValue](../modules/langgraph_web.html#ManagedValue)
      * [ManagedValueMapping](../modules/langgraph_web.html#ManagedValueMapping)
      * [ManagedValueParams](../modules/langgraph_web.html#ManagedValueParams)
      * [ManagedValueSpec](../modules/langgraph_web.html#ManagedValueSpec)
      * [MatchCondition](../modules/langgraph_web.html#MatchCondition)
      * [MemorySaver](../modules/langgraph_web.html#MemorySaver)
      * [Messages](../modules/langgraph_web.html#Messages)
      * [MessagesAnnotation](../modules/langgraph_web.html#MessagesAnnotation)
      * [MultipleSubgraphsError](../modules/langgraph_web.html#MultipleSubgraphsError)
      * [NameSpacePath](../modules/langgraph_web.html#NameSpacePath)
      * [NamedBarrierValue](../modules/langgraph_web.html#NamedBarrierValue)
      * [NamespaceMatchType](../modules/langgraph_web.html#NamespaceMatchType)
      * [NodeInterrupt](../modules/langgraph_web.html#NodeInterrupt)
      * [NodeType](../modules/langgraph_web.html#NodeType)
      * [NoopManagedValue](../modules/langgraph_web.html#NoopManagedValue)
      * [Operation](../modules/langgraph_web.html#Operation)
      * [OperationResults](../modules/langgraph_web.html#OperationResults)
      * [ParentCommand](../modules/langgraph_web.html#ParentCommand)
      * [Pregel](../modules/langgraph_web.html#Pregel)
      * [PregelNode](../modules/langgraph_web.html#PregelNode)
      * [PregelOptions](../modules/langgraph_web.html#PregelOptions)
      * [PregelParams](../modules/langgraph_web.html#PregelParams)
      * [PutOperation](../modules/langgraph_web.html#PutOperation)
      * [RemoteException](../modules/langgraph_web.html#RemoteException)
      * [RetryPolicy](../modules/langgraph_web.html#RetryPolicy)
      * [START](../modules/langgraph_web.html#START)
      * [SearchOperation](../modules/langgraph_web.html#SearchOperation)
      * [Send](../modules/langgraph_web.html#Send)
      * [SharedValue](../modules/langgraph_web.html#SharedValue)
      * [SharedValueParams](../modules/langgraph_web.html#SharedValueParams)
      * [SingleReducer](../modules/langgraph_web.html#SingleReducer)
      * [StateDefinition](../modules/langgraph_web.html#StateDefinition)
      * [StateGraph](../modules/langgraph_web.html#StateGraph)
      * [StateGraphArgs](../modules/langgraph_web.html#StateGraphArgs)
      * [StateSnapshot](../modules/langgraph_web.html#StateSnapshot)
      * [StateType](../modules/langgraph_web.html#StateType)
      * [StreamMode](../modules/langgraph_web.html#StreamMode)
      * [TaskOptions](../modules/langgraph_web.html#TaskOptions)
      * [Topic](../modules/langgraph_web.html#Topic)
      * [UnreachableNodeError](../modules/langgraph_web.html#UnreachableNodeError)
      * [UpdateType](../modules/langgraph_web.html#UpdateType)
      * [WaitForNames](../modules/langgraph_web.html#WaitForNames)
      * [WritableManagedValue](../modules/langgraph_web.html#WritableManagedValue)
      * [addMessages](../modules/langgraph_web.html#addMessages)
      * [entrypoint](../modules/langgraph_web.html#entrypoint)
      * [getSubgraphsSeenSet](../modules/langgraph_web.html#getSubgraphsSeenSet)
      * [isCommand](../modules/langgraph_web.html#isCommand)
      * [isConfiguredManagedValue](../modules/langgraph_web.html#isConfiguredManagedValue)
      * [isGraphBubbleUp](../modules/langgraph_web.html#isGraphBubbleUp)
      * [isGraphInterrupt](../modules/langgraph_web.html#isGraphInterrupt)
      * [isManagedValue](../modules/langgraph_web.html#isManagedValue)
      * [isParentCommand](../modules/langgraph_web.html#isParentCommand)
      * [messagesStateReducer](../modules/langgraph_web.html#messagesStateReducer)
      * [task](../modules/langgraph_web.html#task)




Generated using [TypeDoc](https://typedoc.org/)
