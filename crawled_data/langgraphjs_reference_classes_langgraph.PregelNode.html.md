---
url: https://langchain-ai.github.io/langgraphjs/reference/classes/langgraph.PregelNode.html
title: Untitled
date_crawled: 
---

[Back to documentation](/langgraphjs/)

  * Preparing search index...
  * The search index is not available

[API Reference](/)

[](#)

  * [API Reference](../index.html)
  * [langgraph](../modules/langgraph.html)
  * [PregelNode](langgraph.PregelNode.html)



# Class PregelNode<RunInput, RunOutput>

#### Type Parameters

  * RunInput = PregelNodeInputType
  * RunOutput = PregelNodeOutputType



#### Hierarchy

  * RunnableBinding<[RunInput](langgraph.PregelNode.html#constructor.new_PregelNode.RunInput-1), [RunOutput](langgraph.PregelNode.html#constructor.new_PregelNode.RunOutput-1), RunnableConfig>
    * PregelNode



  * Defined in libs/langgraph/dist/pregel/read.d.ts:28



#####  Index

### Constructors

[constructor](langgraph.PregelNode.html#constructor)

### Properties

[bound](langgraph.PregelNode.html#bound) [channels](langgraph.PregelNode.html#channels) [config](langgraph.PregelNode.html#config) [configFactories?](langgraph.PregelNode.html#configFactories) [ends?](langgraph.PregelNode.html#ends) [kwargs](langgraph.PregelNode.html#kwargs) [lc_graph_name](langgraph.PregelNode.html#lc_graph_name) [lc_kwargs](langgraph.PregelNode.html#lc_kwargs) [lc_namespace](langgraph.PregelNode.html#lc_namespace) [lc_runnable](langgraph.PregelNode.html#lc_runnable) [lc_serializable](langgraph.PregelNode.html#lc_serializable) [mapper?](langgraph.PregelNode.html#mapper) [metadata](langgraph.PregelNode.html#metadata) [name?](langgraph.PregelNode.html#name) [retryPolicy?](langgraph.PregelNode.html#retryPolicy) [subgraphs?](langgraph.PregelNode.html#subgraphs) [tags](langgraph.PregelNode.html#tags) [triggers](langgraph.PregelNode.html#triggers) [writers](langgraph.PregelNode.html#writers)

### Accessors

[lc_aliases](langgraph.PregelNode.html#lc_aliases) [lc_attributes](langgraph.PregelNode.html#lc_attributes) [lc_id](langgraph.PregelNode.html#lc_id) [lc_secrets](langgraph.PregelNode.html#lc_secrets)

### Methods

[_batchWithConfig](langgraph.PregelNode.html#_batchWithConfig) [_callWithConfig](langgraph.PregelNode.html#_callWithConfig) [_getOptionsList](langgraph.PregelNode.html#_getOptionsList) [_mergeConfig](langgraph.PregelNode.html#_mergeConfig) [_separateRunnableConfigFromCallOptions](langgraph.PregelNode.html#_separateRunnableConfigFromCallOptions) [_streamIterator](langgraph.PregelNode.html#_streamIterator) [_streamLog](langgraph.PregelNode.html#_streamLog) [_transformStreamWithConfig](langgraph.PregelNode.html#_transformStreamWithConfig) [asTool](langgraph.PregelNode.html#asTool) [assign](langgraph.PregelNode.html#assign) [batch](langgraph.PregelNode.html#batch) [bind](langgraph.PregelNode.html#bind) [getGraph](langgraph.PregelNode.html#getGraph) [getName](langgraph.PregelNode.html#getName) [getNode](langgraph.PregelNode.html#getNode) [getWriters](langgraph.PregelNode.html#getWriters) [invoke](langgraph.PregelNode.html#invoke) [join](langgraph.PregelNode.html#join) [map](langgraph.PregelNode.html#map) [pick](langgraph.PregelNode.html#pick) [pipe](langgraph.PregelNode.html#pipe) [stream](langgraph.PregelNode.html#stream) [streamEvents](langgraph.PregelNode.html#streamEvents) [streamLog](langgraph.PregelNode.html#streamLog) [toJSON](langgraph.PregelNode.html#toJSON) [toJSONNotImplemented](langgraph.PregelNode.html#toJSONNotImplemented) [transform](langgraph.PregelNode.html#transform) [withConfig](langgraph.PregelNode.html#withConfig) [withFallbacks](langgraph.PregelNode.html#withFallbacks) [withListeners](langgraph.PregelNode.html#withListeners) [withRetry](langgraph.PregelNode.html#withRetry) [isRunnable](langgraph.PregelNode.html#isRunnable) [isRunnableBinding](langgraph.PregelNode.html#isRunnableBinding) [lc_name](langgraph.PregelNode.html#lc_name)

## Constructors

### constructor[](#constructor)

  * new PregelNode<[RunInput](langgraph.PregelNode.html#constructor.new_PregelNode.RunInput-1), [RunOutput](langgraph.PregelNode.html#constructor.new_PregelNode.RunOutput-1)>(fields): [PregelNode](langgraph.PregelNode.html)<[RunInput](langgraph.PregelNode.html#constructor.new_PregelNode.RunInput-1), [RunOutput](langgraph.PregelNode.html#constructor.new_PregelNode.RunOutput-1)>[](#constructor.new_PregelNode)
  * #### Type Parameters

    * RunInput = any
    * RunOutput = any

#### Parameters

    * fields: PregelNodeArgs<[RunInput](langgraph.PregelNode.html#constructor.new_PregelNode.RunInput-1), [RunOutput](langgraph.PregelNode.html#constructor.new_PregelNode.RunOutput-1)>

#### Returns [PregelNode](langgraph.PregelNode.html)<[RunInput](langgraph.PregelNode.html#constructor.new_PregelNode.RunInput-1), [RunOutput](langgraph.PregelNode.html#constructor.new_PregelNode.RunOutput-1)>

Overrides RunnableBinding<RunInput, RunOutput, RunnableConfig>.constructor

    * Defined in libs/langgraph/dist/pregel/read.d.ts:41



## Properties

### bound[](#bound)

bound: Runnable<[RunInput](langgraph.PregelNode.html#constructor.new_PregelNode.RunInput-1), [RunOutput](langgraph.PregelNode.html#constructor.new_PregelNode.RunOutput-1), RunnableConfig<Record<string, any>>>

Overrides RunnableBinding.bound

  * Defined in libs/langgraph/dist/pregel/read.d.ts:34



### channels[](#channels)

channels: string[] | Record<string, string>

  * Defined in libs/langgraph/dist/pregel/read.d.ts:30



### config[](#config)

config: RunnableConfig<Record<string, any>>

Inherited from RunnableBinding.config

  * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:362



### `Optional` configFactories[](#configFactories)

configFactories?: ((config) => RunnableConfig<Record<string, any>> | Promise<RunnableConfig<Record<string, any>>>)[]

#### Type declaration

  *     * (config): RunnableConfig<Record<string, any>> | Promise<RunnableConfig<Record<string, any>>>
    * #### Parameters

      * config: RunnableConfig<Record<string, any>>

#### Returns RunnableConfig<Record<string, any>> | Promise<RunnableConfig<Record<string, any>>>




Inherited from RunnableBinding.configFactories

  * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:364



### `Optional` ends[](#ends)

ends?: string[]

  * Defined in libs/langgraph/dist/pregel/read.d.ts:40



### kwargs[](#kwargs)

kwargs: Record<string, any>

Overrides RunnableBinding.kwargs

  * Defined in libs/langgraph/dist/pregel/read.d.ts:35



### lc_graph_name[](#lc_graph_name)

lc_graph_name: string

  * Defined in libs/langgraph/dist/pregel/read.d.ts:29



### lc_kwargs[](#lc_kwargs)

lc_kwargs: SerializedFields

Inherited from RunnableBinding.lc_kwargs

  * Defined in node_modules/@langchain/core/dist/load/serializable.d.ts:27



### lc_namespace[](#lc_namespace)

lc_namespace: string[]

Inherited from RunnableBinding.lc_namespace

  * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:359



### `Protected` lc_runnable[](#lc_runnable)

lc_runnable: boolean

Inherited from RunnableBinding.lc_runnable

  * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:25



### lc_serializable[](#lc_serializable)

lc_serializable: boolean

Inherited from RunnableBinding.lc_serializable

  * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:360



### `Optional` mapper[](#mapper)

mapper?: ((args) => any)

#### Type declaration

  *     * (args): any
    * #### Parameters

      * args: any

#### Returns any




  * Defined in libs/langgraph/dist/pregel/read.d.ts:32



### metadata[](#metadata)

metadata: Record<string, unknown>

  * Defined in libs/langgraph/dist/pregel/read.d.ts:36



### `Optional` name[](#name)

name?: string

Inherited from RunnableBinding.name

  * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:26



### `Optional` retryPolicy[](#retryPolicy)

retryPolicy?: [RetryPolicy](../types/langgraph.RetryPolicy.html)

  * Defined in libs/langgraph/dist/pregel/read.d.ts:38



### `Optional` subgraphs[](#subgraphs)

subgraphs?: Runnable<any, any, RunnableConfig<Record<string, any>>>[]

  * Defined in libs/langgraph/dist/pregel/read.d.ts:39



### tags[](#tags)

tags: string[]

  * Defined in libs/langgraph/dist/pregel/read.d.ts:37



### triggers[](#triggers)

triggers: string[]

  * Defined in libs/langgraph/dist/pregel/read.d.ts:31



### writers[](#writers)

writers: Runnable<any, any, RunnableConfig<Record<string, any>>>[]

  * Defined in libs/langgraph/dist/pregel/read.d.ts:33



## Accessors

### lc_aliases[](#lc_aliases)

  * get lc_aliases(): undefined | { [key: string]: string; }
  * A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

#### Returns undefined | { [key: string]: string; }

Inherited from RunnableBinding.lc_aliases

    * Defined in node_modules/@langchain/core/dist/load/serializable.d.ts:65



### lc_attributes[](#lc_attributes)

  * get lc_attributes(): undefined | SerializedFields
  * A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

#### Returns undefined | SerializedFields

Inherited from RunnableBinding.lc_attributes

    * Defined in node_modules/@langchain/core/dist/load/serializable.d.ts:58



### lc_id[](#lc_id)

  * get lc_id(): string[]
  * The final serialized identifier for the module.

#### Returns string[]

Inherited from RunnableBinding.lc_id

    * Defined in node_modules/@langchain/core/dist/load/serializable.d.ts:43



### lc_secrets[](#lc_secrets)

  * get lc_secrets(): undefined | { [key: string]: string; }
  * A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

#### Returns undefined | { [key: string]: string; }

Inherited from RunnableBinding.lc_secrets

    * Defined in node_modules/@langchain/core/dist/load/serializable.d.ts:49



## Methods

### _batchWithConfig[](#_batchWithConfig)

  * _batchWithConfig<[T](langgraph.PregelNode.html#_batchWithConfig._batchWithConfig-1.T)>(func, inputs, options?, batchOptions?): Promise<(Error | [RunOutput](langgraph.PregelNode.html#constructor.new_PregelNode.RunOutput-1))[]>[](#_batchWithConfig._batchWithConfig-1)
  * Internal method that handles batching and configuration for a runnable It takes a function, input values, and optional configuration, and returns a promise that resolves to the output values.

#### Type Parameters

    * T

#### Parameters

    * func: ((inputs, options?, runManagers?, batchOptions?) => Promise<(Error | [RunOutput](langgraph.PregelNode.html#constructor.new_PregelNode.RunOutput-1))[]>)

The function to be executed for each input value.

      *         * (inputs, options?, runManagers?, batchOptions?): Promise<(Error | [RunOutput](langgraph.PregelNode.html#constructor.new_PregelNode.RunOutput-1))[]>
        * #### Parameters

          * inputs: [T](langgraph.CompiledStateGraph.html#_batchWithConfig._batchWithConfig-1.T)[]
          * `Optional` options: Partial<RunnableConfig<Record<string, any>>>[]
          * `Optional` runManagers: (undefined | CallbackManagerForChainRun)[]
          * `Optional` batchOptions: RunnableBatchOptions

#### Returns Promise<(Error | [RunOutput](langgraph.PregelNode.html#constructor.new_PregelNode.RunOutput-1))[]>

    * inputs: [T](langgraph.CompiledStateGraph.html#_batchWithConfig._batchWithConfig-1.T)[]
    * `Optional` options: Partial<RunnableConfig<Record<string, any>> & { runType?: string; }> | Partial<RunnableConfig<Record<string, any>> & { runType?: string; }>[]
    * `Optional` batchOptions: RunnableBatchOptions

#### Returns Promise<(Error | [RunOutput](langgraph.PregelNode.html#constructor.new_PregelNode.RunOutput-1))[]>

A promise that resolves to the output values.

Inherited from RunnableBinding._batchWithConfig

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:109



### `Protected` _callWithConfig[](#_callWithConfig)

  * _callWithConfig<[T](langgraph.PregelNode.html#_callWithConfig._callWithConfig-1.T-1)>(func, input, options?): Promise<[RunOutput](langgraph.PregelNode.html#constructor.new_PregelNode.RunOutput-1)>[](#_callWithConfig._callWithConfig-1)
  * #### Type Parameters

    * T

#### Parameters

    * func: ((input) => Promise<[RunOutput](langgraph.PregelNode.html#constructor.new_PregelNode.RunOutput-1)>) | ((input, config?, runManager?) => Promise<[RunOutput](langgraph.PregelNode.html#constructor.new_PregelNode.RunOutput-1)>)
    * input: [T](langgraph.CompiledStateGraph.html#_callWithConfig._callWithConfig-1.T-1)
    * `Optional` options: Partial<RunnableConfig<Record<string, any>>> & { runType?: string; }

#### Returns Promise<[RunOutput](langgraph.PregelNode.html#constructor.new_PregelNode.RunOutput-1)>

Inherited from RunnableBinding._callWithConfig

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:97



### `Protected` _getOptionsList[](#_getOptionsList)

  * _getOptionsList<[O](langgraph.PregelNode.html#_getOptionsList._getOptionsList-1.O)>(options, length?): Partial<[O](langgraph.CompiledStateGraph.html#_getOptionsList._getOptionsList-1.O-2)>[][](#_getOptionsList._getOptionsList-1)
  * #### Type Parameters

    * O extends RunnableConfig<Record<string, any>, [O](langgraph.CompiledStateGraph.html#_getOptionsList._getOptionsList-1.O-2)> & { runType?: string; }

#### Parameters

    * options: Partial<[O](langgraph.CompiledStateGraph.html#_getOptionsList._getOptionsList-1.O-2)> | Partial<[O](langgraph.CompiledStateGraph.html#_getOptionsList._getOptionsList-1.O-2)>[]
    * `Optional` length: number

#### Returns Partial<[O](langgraph.CompiledStateGraph.html#_getOptionsList._getOptionsList-1.O-2)>[]

Inherited from RunnableBinding._getOptionsList

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:64



### _mergeConfig[](#_mergeConfig)

  * _mergeConfig(...options): Promise<Partial<RunnableConfig<Record<string, any>>>>[](#_mergeConfig._mergeConfig-1)
  * #### Parameters

    * `Rest` ...options: (undefined | RunnableConfig<Record<string, any>> | Partial<RunnableConfig<Record<string, any>>>)[]

#### Returns Promise<Partial<RunnableConfig<Record<string, any>>>>

Inherited from RunnableBinding._mergeConfig

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:367



### `Protected` _separateRunnableConfigFromCallOptions[](#_separateRunnableConfigFromCallOptions)

  * _separateRunnableConfigFromCallOptions(options?): [RunnableConfig<Record<string, any>>, Omit<Partial<RunnableConfig<Record<string, any>>>, keyof RunnableConfig<Record<string, any>>>][](#_separateRunnableConfigFromCallOptions._separateRunnableConfigFromCallOptions-1)
  * #### Parameters

    * `Optional` options: Partial<RunnableConfig<Record<string, any>>>

#### Returns [RunnableConfig<Record<string, any>>, Omit<Partial<RunnableConfig<Record<string, any>>>, keyof RunnableConfig<Record<string, any>>>]

Inherited from RunnableBinding._separateRunnableConfigFromCallOptions

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:96



### _streamIterator[](#_streamIterator)

  * _streamIterator(input, options?): AsyncGenerator<Awaited<[RunOutput](langgraph.PregelNode.html#constructor.new_PregelNode.RunOutput-1)>, void, unknown>[](#_streamIterator._streamIterator-1)
  * #### Parameters

    * input: [RunInput](langgraph.PregelNode.html#constructor.new_PregelNode.RunInput-1)
    * `Optional` options: Partial<RunnableConfig<Record<string, any>>>

#### Returns AsyncGenerator<Awaited<[RunOutput](langgraph.PregelNode.html#constructor.new_PregelNode.RunOutput-1)>, void, unknown>

Inherited from RunnableBinding._streamIterator

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:382



### `Protected` _streamLog[](#_streamLog)

  * _streamLog(input, logStreamCallbackHandler, config): AsyncGenerator<RunLogPatch, any, unknown>[](#_streamLog._streamLog-1)
  * #### Parameters

    * input: [RunInput](langgraph.PregelNode.html#constructor.new_PregelNode.RunInput-1)
    * logStreamCallbackHandler: LogStreamCallbackHandler
    * config: Partial<RunnableConfig<Record<string, any>>>

#### Returns AsyncGenerator<RunLogPatch, any, unknown>

Inherited from RunnableBinding._streamLog

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:158



### `Protected` _transformStreamWithConfig[](#_transformStreamWithConfig)

  * _transformStreamWithConfig<[I](langgraph.PregelNode.html#_transformStreamWithConfig._transformStreamWithConfig-1.I), [O](langgraph.PregelNode.html#_transformStreamWithConfig._transformStreamWithConfig-1.O-1)>(inputGenerator, transformer, options?): AsyncGenerator<[O](langgraph.CompiledStateGraph.html#_transformStreamWithConfig._transformStreamWithConfig-1.O-3), any, unknown>[](#_transformStreamWithConfig._transformStreamWithConfig-1)
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

Inherited from RunnableBinding._transformStreamWithConfig

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:119



### asTool[](#asTool)

  * asTool<[T](langgraph.PregelNode.html#asTool.asTool-1.T-2)>(fields): RunnableToolLike<ZodType<ToolCall | [T](langgraph.CompiledStateGraph.html#asTool.asTool-1.T-2), ZodTypeDef, ToolCall | [T](langgraph.CompiledStateGraph.html#asTool.asTool-1.T-2)>, [RunOutput](langgraph.PregelNode.html#constructor.new_PregelNode.RunOutput-1)>[](#asTool.asTool-1)
  * Convert a runnable to a tool. Return a new instance of `RunnableToolLike` which contains the runnable, name, description and schema.

#### Type Parameters

    * T = [RunInput](langgraph.PregelNode.html#constructor.new_PregelNode.RunInput-1)

#### Parameters

    * fields: { description?: string; name?: string; schema: ZodType<[T](langgraph.CompiledStateGraph.html#asTool.asTool-1.T-2), ZodTypeDef, [T](langgraph.CompiledStateGraph.html#asTool.asTool-1.T-2)>; }
      * ##### `Optional` description?: string

The description of the tool. Falls back to the description on the Zod schema if not provided, or undefined if neither are provided.

      * ##### `Optional` name?: string

The name of the tool. If not provided, it will default to the name of the runnable.

      * ##### schema: ZodType<[T](langgraph.CompiledStateGraph.html#asTool.asTool-1.T-2), ZodTypeDef, [T](langgraph.CompiledStateGraph.html#asTool.asTool-1.T-2)>

The Zod schema for the input of the tool. Infers the Zod type from the input type of the runnable.

#### Returns RunnableToolLike<ZodType<ToolCall | [T](langgraph.CompiledStateGraph.html#asTool.asTool-1.T-2), ZodTypeDef, ToolCall | [T](langgraph.CompiledStateGraph.html#asTool.asTool-1.T-2)>, [RunOutput](langgraph.PregelNode.html#constructor.new_PregelNode.RunOutput-1)>

An instance of `RunnableToolLike` which is a runnable that can be used as a tool.

Inherited from RunnableBinding.asTool

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:305



### assign[](#assign)

  * assign(mapping): Runnable<any, any, RunnableConfig<Record<string, any>>>[](#assign.assign-1)
  * Assigns new fields to the dict output of this runnable. Returns a new runnable.

#### Parameters

    * mapping: RunnableMapLike<Record<string, unknown>, Record<string, unknown>>

#### Returns Runnable<any, any, RunnableConfig<Record<string, any>>>

Inherited from RunnableBinding.assign

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:137



### batch[](#batch)

  * batch(inputs, options?, batchOptions?): Promise<[RunOutput](langgraph.PregelNode.html#constructor.new_PregelNode.RunOutput-1)[]>[](#batch.batch-1)
  * #### Parameters

    * inputs: [RunInput](langgraph.PregelNode.html#constructor.new_PregelNode.RunInput-1)[]
    * `Optional` options: Partial<RunnableConfig<Record<string, any>>> | Partial<RunnableConfig<Record<string, any>>>[]
    * `Optional` batchOptions: RunnableBatchOptions & { returnExceptions?: false; }

#### Returns Promise<[RunOutput](langgraph.PregelNode.html#constructor.new_PregelNode.RunOutput-1)[]>

Inherited from RunnableBinding.batch

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:375
  * batch(inputs, options?, batchOptions?): Promise<(Error | [RunOutput](langgraph.PregelNode.html#constructor.new_PregelNode.RunOutput-1))[]>[](#batch.batch-2)
  * #### Parameters

    * inputs: [RunInput](langgraph.PregelNode.html#constructor.new_PregelNode.RunInput-1)[]
    * `Optional` options: Partial<RunnableConfig<Record<string, any>>> | Partial<RunnableConfig<Record<string, any>>>[]
    * `Optional` batchOptions: RunnableBatchOptions & { returnExceptions: true; }

#### Returns Promise<(Error | [RunOutput](langgraph.PregelNode.html#constructor.new_PregelNode.RunOutput-1))[]>

Inherited from RunnableBinding.batch

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:378
  * batch(inputs, options?, batchOptions?): Promise<(Error | [RunOutput](langgraph.PregelNode.html#constructor.new_PregelNode.RunOutput-1))[]>[](#batch.batch-3)
  * #### Parameters

    * inputs: [RunInput](langgraph.PregelNode.html#constructor.new_PregelNode.RunInput-1)[]
    * `Optional` options: Partial<RunnableConfig<Record<string, any>>> | Partial<RunnableConfig<Record<string, any>>>[]
    * `Optional` batchOptions: RunnableBatchOptions

#### Returns Promise<(Error | [RunOutput](langgraph.PregelNode.html#constructor.new_PregelNode.RunOutput-1))[]>

Inherited from RunnableBinding.batch

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:381



### bind[](#bind)

  * bind(kwargs): RunnableBinding<[RunInput](langgraph.PregelNode.html#constructor.new_PregelNode.RunInput-1), [RunOutput](langgraph.PregelNode.html#constructor.new_PregelNode.RunOutput-1), RunnableConfig<Record<string, any>>>[](#bind.bind-1)
  * #### Parameters

    * kwargs: Partial<RunnableConfig<Record<string, any>>>

#### Returns RunnableBinding<[RunInput](langgraph.PregelNode.html#constructor.new_PregelNode.RunInput-1), [RunOutput](langgraph.PregelNode.html#constructor.new_PregelNode.RunOutput-1), RunnableConfig<Record<string, any>>>

Inherited from RunnableBinding.bind

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:368



### getGraph[](#getGraph)

  * getGraph(_?): Graph[](#getGraph.getGraph-1)
  * #### Parameters

    * `Optional` _: RunnableConfig<Record<string, any>>

#### Returns Graph

Inherited from RunnableBinding.getGraph

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:122



### getName[](#getName)

  * getName(suffix?): string[](#getName.getName-1)
  * #### Parameters

    * `Optional` suffix: string

#### Returns string

Inherited from RunnableBinding.getName

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:366



### getNode[](#getNode)

  * getNode(): undefined | Runnable<[RunInput](langgraph.PregelNode.html#constructor.new_PregelNode.RunInput-1), [RunOutput](langgraph.PregelNode.html#constructor.new_PregelNode.RunOutput-1), RunnableConfig<Record<string, any>>>[](#getNode.getNode-1)
  * #### Returns undefined | Runnable<[RunInput](langgraph.PregelNode.html#constructor.new_PregelNode.RunInput-1), [RunOutput](langgraph.PregelNode.html#constructor.new_PregelNode.RunOutput-1), RunnableConfig<Record<string, any>>>

    * Defined in libs/langgraph/dist/pregel/read.d.ts:43



### getWriters[](#getWriters)

  * getWriters(): Runnable<any, any, RunnableConfig<Record<string, any>>>[][](#getWriters.getWriters-1)
  * #### Returns Runnable<any, any, RunnableConfig<Record<string, any>>>[]

    * Defined in libs/langgraph/dist/pregel/read.d.ts:42



### invoke[](#invoke)

  * invoke(input, options?): Promise<[RunOutput](langgraph.PregelNode.html#constructor.new_PregelNode.RunOutput-1)>[](#invoke.invoke-1)
  * #### Parameters

    * input: [RunInput](langgraph.PregelNode.html#constructor.new_PregelNode.RunInput-1)
    * `Optional` options: Partial<RunnableConfig<Record<string, any>>>

#### Returns Promise<[RunOutput](langgraph.PregelNode.html#constructor.new_PregelNode.RunOutput-1)>

Inherited from RunnableBinding.invoke

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:374



### join[](#join)

  * join(channels): [PregelNode](langgraph.PregelNode.html)<[RunInput](langgraph.PregelNode.html#constructor.new_PregelNode.RunInput-1), [RunOutput](langgraph.PregelNode.html#constructor.new_PregelNode.RunOutput-1)>[](#join.join-1)
  * #### Parameters

    * channels: string[]

#### Returns [PregelNode](langgraph.PregelNode.html)<[RunInput](langgraph.PregelNode.html#constructor.new_PregelNode.RunInput-1), [RunOutput](langgraph.PregelNode.html#constructor.new_PregelNode.RunOutput-1)>

    * Defined in libs/langgraph/dist/pregel/read.d.ts:44



### map[](#map)

  * map(): Runnable<[RunInput](langgraph.PregelNode.html#constructor.new_PregelNode.RunInput-1)[], [RunOutput](langgraph.PregelNode.html#constructor.new_PregelNode.RunOutput-1)[], RunnableConfig<Record<string, any>>>[](#map.map-1)
  * Return a new Runnable that maps a list of inputs to a list of outputs, by calling invoke() with each input.

#### Returns Runnable<[RunInput](langgraph.PregelNode.html#constructor.new_PregelNode.RunInput-1)[], [RunOutput](langgraph.PregelNode.html#constructor.new_PregelNode.RunOutput-1)[], RunnableConfig<Record<string, any>>>

Inherited from RunnableBinding.map

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:39



### pick[](#pick)

  * pick(keys): Runnable<any, any, RunnableConfig<Record<string, any>>>[](#pick.pick-1)
  * Pick keys from the dict output of this runnable. Returns a new runnable.

#### Parameters

    * keys: string | string[]

#### Returns Runnable<any, any, RunnableConfig<Record<string, any>>>

Inherited from RunnableBinding.pick

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:133



### pipe[](#pipe)

  * pipe<[NewRunOutput](langgraph.PregelNode.html#pipe.pipe-1.NewRunOutput)>(coerceable): [PregelNode](langgraph.PregelNode.html)<[RunInput](langgraph.PregelNode.html#constructor.new_PregelNode.RunInput-1), Exclude<[NewRunOutput](langgraph.PregelNode.html#pipe.pipe-1.NewRunOutput), Error>>[](#pipe.pipe-1)
  * #### Type Parameters

    * NewRunOutput

#### Parameters

    * coerceable: RunnableLike<any, any, RunnableConfig<Record<string, any>>>

#### Returns [PregelNode](langgraph.PregelNode.html)<[RunInput](langgraph.PregelNode.html#constructor.new_PregelNode.RunInput-1), Exclude<[NewRunOutput](langgraph.PregelNode.html#pipe.pipe-1.NewRunOutput), Error>>

Overrides RunnableBinding.pipe

    * Defined in libs/langgraph/dist/pregel/read.d.ts:45



### stream[](#stream)

  * stream(input, options?): Promise<IterableReadableStream<[RunOutput](langgraph.PregelNode.html#constructor.new_PregelNode.RunOutput-1)>>[](#stream.stream-1)
  * #### Parameters

    * input: [RunInput](langgraph.PregelNode.html#constructor.new_PregelNode.RunInput-1)
    * `Optional` options: Partial<RunnableConfig<Record<string, any>>>

#### Returns Promise<IterableReadableStream<[RunOutput](langgraph.PregelNode.html#constructor.new_PregelNode.RunOutput-1)>>

Inherited from RunnableBinding.stream

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:383



### streamEvents[](#streamEvents)

  * streamEvents(input, options, streamOptions?): IterableReadableStream<StreamEvent>[](#streamEvents.streamEvents-1)
  * #### Parameters

    * input: [RunInput](langgraph.PregelNode.html#constructor.new_PregelNode.RunInput-1)
    * options: Partial<RunnableConfig<Record<string, any>>> & { version: "v1" | "v2"; }
    * `Optional` streamOptions: Omit<LogStreamCallbackHandlerInput, "autoClose">

#### Returns IterableReadableStream<StreamEvent>

Inherited from RunnableBinding.streamEvents

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:385
  * streamEvents(input, options, streamOptions?): IterableReadableStream<Uint8Array>[](#streamEvents.streamEvents-2)
  * #### Parameters

    * input: [RunInput](langgraph.PregelNode.html#constructor.new_PregelNode.RunInput-1)
    * options: Partial<RunnableConfig<Record<string, any>>> & { encoding: "text/event-stream"; version: "v1" | "v2"; }
    * `Optional` streamOptions: Omit<LogStreamCallbackHandlerInput, "autoClose">

#### Returns IterableReadableStream<Uint8Array>

Inherited from RunnableBinding.streamEvents

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:388



### streamLog[](#streamLog)

  * streamLog(input, options?, streamOptions?): AsyncGenerator<RunLogPatch, any, unknown>[](#streamLog.streamLog-1)
  * Stream all output from a runnable, as reported to the callback system. This includes all inner runs of LLMs, Retrievers, Tools, etc. Output is streamed as Log objects, which include a list of jsonpatch ops that describe how the state of the run has changed in each step, and the final state of the run. The jsonpatch ops can be applied in order to construct state.

#### Parameters

    * input: [RunInput](langgraph.PregelNode.html#constructor.new_PregelNode.RunInput-1)
    * `Optional` options: Partial<RunnableConfig<Record<string, any>>>
    * `Optional` streamOptions: Omit<LogStreamCallbackHandlerInput, "autoClose">

#### Returns AsyncGenerator<RunLogPatch, any, unknown>

Inherited from RunnableBinding.streamLog

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:157



### toJSON[](#toJSON)

  * toJSON(): Serialized[](#toJSON.toJSON-1)
  * #### Returns Serialized

Inherited from RunnableBinding.toJSON

    * Defined in node_modules/@langchain/core/dist/load/serializable.d.ts:69



### toJSONNotImplemented[](#toJSONNotImplemented)

  * toJSONNotImplemented(): SerializedNotImplemented[](#toJSONNotImplemented.toJSONNotImplemented-1)
  * #### Returns SerializedNotImplemented

Inherited from RunnableBinding.toJSONNotImplemented

    * Defined in node_modules/@langchain/core/dist/load/serializable.d.ts:70



### transform[](#transform)

  * transform(generator, options?): AsyncGenerator<[RunOutput](langgraph.PregelNode.html#constructor.new_PregelNode.RunOutput-1), any, unknown>[](#transform.transform-1)
  * #### Parameters

    * generator: AsyncGenerator<[RunInput](langgraph.PregelNode.html#constructor.new_PregelNode.RunInput-1), any, unknown>
    * `Optional` options: Partial<RunnableConfig<Record<string, any>>>

#### Returns AsyncGenerator<[RunOutput](langgraph.PregelNode.html#constructor.new_PregelNode.RunOutput-1), any, unknown>

Inherited from RunnableBinding.transform

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:384



### withConfig[](#withConfig)

  * withConfig(config): Runnable<[RunInput](langgraph.PregelNode.html#constructor.new_PregelNode.RunInput-1), [RunOutput](langgraph.PregelNode.html#constructor.new_PregelNode.RunOutput-1), RunnableConfig<Record<string, any>>>[](#withConfig.withConfig-1)
  * #### Parameters

    * config: RunnableConfig<Record<string, any>>

#### Returns Runnable<[RunInput](langgraph.PregelNode.html#constructor.new_PregelNode.RunInput-1), [RunOutput](langgraph.PregelNode.html#constructor.new_PregelNode.RunOutput-1), RunnableConfig<Record<string, any>>>

Inherited from RunnableBinding.withConfig

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:369



### withFallbacks[](#withFallbacks)

  * withFallbacks(fields): RunnableWithFallbacks<[RunInput](langgraph.PregelNode.html#constructor.new_PregelNode.RunInput-1), [RunOutput](langgraph.PregelNode.html#constructor.new_PregelNode.RunOutput-1)>[](#withFallbacks.withFallbacks-1)
  * Create a new runnable from the current one that will try invoking other passed fallback runnables if the initial invocation fails.

#### Parameters

    * fields: { fallbacks: Runnable<[RunInput](langgraph.PregelNode.html#constructor.new_PregelNode.RunInput-1), [RunOutput](langgraph.PregelNode.html#constructor.new_PregelNode.RunOutput-1), RunnableConfig<Record<string, any>>>[]; } | Runnable<[RunInput](langgraph.PregelNode.html#constructor.new_PregelNode.RunInput-1), [RunOutput](langgraph.PregelNode.html#constructor.new_PregelNode.RunOutput-1), RunnableConfig<Record<string, any>>>[]

#### Returns RunnableWithFallbacks<[RunInput](langgraph.PregelNode.html#constructor.new_PregelNode.RunInput-1), [RunOutput](langgraph.PregelNode.html#constructor.new_PregelNode.RunOutput-1)>

A new RunnableWithFallbacks.

Inherited from RunnableBinding.withFallbacks

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:61



### withListeners[](#withListeners)

  * withListeners(params): Runnable<[RunInput](langgraph.PregelNode.html#constructor.new_PregelNode.RunInput-1), [RunOutput](langgraph.PregelNode.html#constructor.new_PregelNode.RunOutput-1), RunnableConfig<Record<string, any>>>[](#withListeners.withListeners-1)
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

#### Returns Runnable<[RunInput](langgraph.PregelNode.html#constructor.new_PregelNode.RunInput-1), [RunOutput](langgraph.PregelNode.html#constructor.new_PregelNode.RunOutput-1), RunnableConfig<Record<string, any>>>

Inherited from RunnableBinding.withListeners

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:404



### withRetry[](#withRetry)

  * withRetry(fields?): RunnableRetry<[RunInput](langgraph.PregelNode.html#constructor.new_PregelNode.RunInput-1), [RunOutput](langgraph.PregelNode.html#constructor.new_PregelNode.RunOutput-1), RunnableConfig<Record<string, any>>>[](#withRetry.withRetry-1)
  * #### Parameters

    * `Optional` fields: { onFailedAttempt?: RunnableRetryFailedAttemptHandler; stopAfterAttempt?: number; }
      * ##### `Optional` onFailedAttempt?: RunnableRetryFailedAttemptHandler

      * ##### `Optional` stopAfterAttempt?: number

#### Returns RunnableRetry<[RunInput](langgraph.PregelNode.html#constructor.new_PregelNode.RunInput-1), [RunOutput](langgraph.PregelNode.html#constructor.new_PregelNode.RunOutput-1), RunnableConfig<Record<string, any>>>

Inherited from RunnableBinding.withRetry

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:370



### `Static` isRunnable[](#isRunnable)

  * isRunnable(thing): thing is Runnable<any, any, RunnableConfig<Record<string, any>>>[](#isRunnable.isRunnable-1)
  * #### Parameters

    * thing: any

#### Returns thing is Runnable<any, any, RunnableConfig<Record<string, any>>>

Inherited from RunnableBinding.isRunnable

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:276



### `Static` isRunnableBinding[](#isRunnableBinding)

  * isRunnableBinding(thing): thing is RunnableBinding<any, any, any>[](#isRunnableBinding.isRunnableBinding-1)
  * #### Parameters

    * thing: any

#### Returns thing is RunnableBinding<any, any, any>

Inherited from RunnableBinding.isRunnableBinding

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:392



### `Static` lc_name[](#lc_name)

  * lc_name(): string[](#lc_name.lc_name-1)
  * #### Returns string

Inherited from RunnableBinding.lc_name

    * Defined in node_modules/@langchain/core/dist/runnables/base.d.ts:358



### Settings

#### Member Visibility

  * Protected
  * Private
  * Inherited
  * External



#### Theme

OSLightDark

### On This Page

[constructor](#constructor)[bound](#bound)[channels](#channels)[config](#config)[configFactories](#configFactories)[ends](#ends)[kwargs](#kwargs)[lc_graph_name](#lc_graph_name)[lc_kwargs](#lc_kwargs)[lc_namespace](#lc_namespace)[lc_runnable](#lc_runnable)[lc_serializable](#lc_serializable)[mapper](#mapper)[metadata](#metadata)[name](#name)[retryPolicy](#retryPolicy)[subgraphs](#subgraphs)[tags](#tags)[triggers](#triggers)[writers](#writers)[lc_aliases](#lc_aliases)[lc_attributes](#lc_attributes)[lc_id](#lc_id)[lc_secrets](#lc_secrets)[_batchWithConfig](#_batchWithConfig)[_callWithConfig](#_callWithConfig)[_getOptionsList](#_getOptionsList)[_mergeConfig](#_mergeConfig)[_separateRunnableConfigFromCallOptions](#_separateRunnableConfigFromCallOptions)[_streamIterator](#_streamIterator)[_streamLog](#_streamLog)[_transformStreamWithConfig](#_transformStreamWithConfig)[asTool](#asTool)[assign](#assign)[batch](#batch)[bind](#bind)[getGraph](#getGraph)[getName](#getName)[getNode](#getNode)[getWriters](#getWriters)[invoke](#invoke)[join](#join)[map](#map)[pick](#pick)[pipe](#pipe)[stream](#stream)[streamEvents](#streamEvents)[streamLog](#streamLog)[toJSON](#toJSON)[toJSONNotImplemented](#toJSONNotImplemented)[transform](#transform)[withConfig](#withConfig)[withFallbacks](#withFallbacks)[withListeners](#withListeners)[withRetry](#withRetry)[isRunnable](#isRunnable)[isRunnableBinding](#isRunnableBinding)[lc_name](#lc_name)

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
