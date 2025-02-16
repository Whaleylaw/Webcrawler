---
url: https://langchain-ai.github.io/langgraphjs/reference/classes/checkpoint_postgres.PostgresSaver.html
title: Untitled
date_crawled: 
---

[Back to documentation](/langgraphjs/)

  * Preparing search index...
  * The search index is not available

[API Reference](/)

[](#)

  * [API Reference](../index.html)
  * [checkpoint-postgres](../modules/checkpoint_postgres.html)
  * [PostgresSaver](checkpoint_postgres.PostgresSaver.html)



# Class PostgresSaver

LangGraph checkpointer that uses a Postgres instance as the backing store. Uses the [node-postgres](https://node-postgres.com/) package internally to connect to a Postgres instance.

#### Example

```
import { ChatOpenAI } from"@langchain/openai";import { PostgresSaver } from"@langchain/langgraph-checkpoint-postgres";import { createReactAgent } from"@langchain/langgraph/prebuilt";constcheckpointer = PostgresSaver.fromConnString("postgresql://user:password@localhost:5432/db");// NOTE: you need to call .setup() the first time you're using your checkpointerawaitcheckpointer.setup();constgraph = createReactAgent({tools: [getWeather],llm:newChatOpenAI({model:"gpt-4o-mini", }),checkpointSaver:checkpointer,});constconfig = { configurable: { thread_id:"1" } };awaitgraph.invoke({messages: [{role:"user",content:"what's the weather in sf" }],}, config);
Copy
```


#### Hierarchy ([view full](../hierarchy.html#checkpoint-postgres.PostgresSaver))

  * [BaseCheckpointSaver](checkpoint.BaseCheckpointSaver.html)
    * PostgresSaver



  * Defined in libs/checkpoint-postgres/dist/index.d.ts:39



#####  Index

### Constructors

[constructor](checkpoint_postgres.PostgresSaver.html#constructor)

### Properties

[isSetup](checkpoint_postgres.PostgresSaver.html#isSetup) [pool](checkpoint_postgres.PostgresSaver.html#pool) [serde](checkpoint_postgres.PostgresSaver.html#serde)

### Methods

[_dumpBlobs](checkpoint_postgres.PostgresSaver.html#_dumpBlobs) [_dumpCheckpoint](checkpoint_postgres.PostgresSaver.html#_dumpCheckpoint) [_dumpMetadata](checkpoint_postgres.PostgresSaver.html#_dumpMetadata) [_dumpWrites](checkpoint_postgres.PostgresSaver.html#_dumpWrites) [_loadBlobs](checkpoint_postgres.PostgresSaver.html#_loadBlobs) [_loadCheckpoint](checkpoint_postgres.PostgresSaver.html#_loadCheckpoint) [_loadMetadata](checkpoint_postgres.PostgresSaver.html#_loadMetadata) [_loadWrites](checkpoint_postgres.PostgresSaver.html#_loadWrites) [_searchWhere](checkpoint_postgres.PostgresSaver.html#_searchWhere) [end](checkpoint_postgres.PostgresSaver.html#end) [get](checkpoint_postgres.PostgresSaver.html#get) [getNextVersion](checkpoint_postgres.PostgresSaver.html#getNextVersion) [getTuple](checkpoint_postgres.PostgresSaver.html#getTuple) [list](checkpoint_postgres.PostgresSaver.html#list) [put](checkpoint_postgres.PostgresSaver.html#put) [putWrites](checkpoint_postgres.PostgresSaver.html#putWrites) [setup](checkpoint_postgres.PostgresSaver.html#setup) [fromConnString](checkpoint_postgres.PostgresSaver.html#fromConnString)

## Constructors

### constructor[](#constructor)

  * new PostgresSaver(pool, serde?): [PostgresSaver](checkpoint_postgres.PostgresSaver.html)[](#constructor.new_PostgresSaver)
  * #### Parameters

    * pool: Pool
    * `Optional` serde: [SerializerProtocol](../interfaces/checkpoint.SerializerProtocol.html)

#### Returns [PostgresSaver](checkpoint_postgres.PostgresSaver.html)

Overrides [BaseCheckpointSaver](checkpoint.BaseCheckpointSaver.html).[constructor](checkpoint.BaseCheckpointSaver.html#constructor)

    * Defined in libs/checkpoint-postgres/dist/index.d.ts:42



## Properties

### `Protected` isSetup[](#isSetup)

isSetup: boolean

  * Defined in libs/checkpoint-postgres/dist/index.d.ts:41



### `Private` pool[](#pool)

pool: any

  * Defined in libs/checkpoint-postgres/dist/index.d.ts:40



### serde[](#serde)

serde: [SerializerProtocol](../interfaces/checkpoint.SerializerProtocol.html)

Inherited from [BaseCheckpointSaver](checkpoint.BaseCheckpointSaver.html).[serde](checkpoint.BaseCheckpointSaver.html#serde)

  * Defined in libs/checkpoint/dist/base.d.ts:61



## Methods

### `Protected` _dumpBlobs[](#_dumpBlobs)

  * _dumpBlobs(threadId, checkpointNs, values, versions): [string, string, string, string, string, undefined | Uint8Array][][](#_dumpBlobs._dumpBlobs-1)
  * #### Parameters

    * threadId: string
    * checkpointNs: string
    * values: Record<string, unknown>
    * versions: [ChannelVersions](../types/checkpoint.ChannelVersions.html)

#### Returns [string, string, string, string, string, undefined | Uint8Array][]

    * Defined in libs/checkpoint-postgres/dist/index.d.ts:56



### `Protected` _dumpCheckpoint[](#_dumpCheckpoint)

  * _dumpCheckpoint(checkpoint): Record<string, unknown>[](#_dumpCheckpoint._dumpCheckpoint-1)
  * #### Parameters

    * checkpoint: [Checkpoint](../interfaces/checkpoint.Checkpoint.html)<string, string>

#### Returns Record<string, unknown>

    * Defined in libs/checkpoint-postgres/dist/index.d.ts:57



### `Protected` _dumpMetadata[](#_dumpMetadata)

  * _dumpMetadata(metadata): any[](#_dumpMetadata._dumpMetadata-1)
  * #### Parameters

    * metadata: [CheckpointMetadata](../interfaces/checkpoint.CheckpointMetadata.html)

#### Returns any

    * Defined in libs/checkpoint-postgres/dist/index.d.ts:58



### `Protected` _dumpWrites[](#_dumpWrites)

  * _dumpWrites(threadId, checkpointNs, checkpointId, taskId, writes): [string, string, string, string, number, string, string, Uint8Array][][](#_dumpWrites._dumpWrites-1)
  * #### Parameters

    * threadId: string
    * checkpointNs: string
    * checkpointId: string
    * taskId: string
    * writes: [string, unknown][]

#### Returns [string, string, string, string, number, string, string, Uint8Array][]

    * Defined in libs/checkpoint-postgres/dist/index.d.ts:59



### `Protected` _loadBlobs[](#_loadBlobs)

  * _loadBlobs(blobValues): Promise<Record<string, unknown>>[](#_loadBlobs._loadBlobs-1)
  * #### Parameters

    * blobValues: [Uint8Array, Uint8Array, Uint8Array][]

#### Returns Promise<Record<string, unknown>>

    * Defined in libs/checkpoint-postgres/dist/index.d.ts:53



### `Protected` _loadCheckpoint[](#_loadCheckpoint)

  * _loadCheckpoint(checkpoint, channelValues, pendingSends): Promise<[Checkpoint](../interfaces/checkpoint.Checkpoint.html)<string, string>>[](#_loadCheckpoint._loadCheckpoint-1)
  * #### Parameters

    * checkpoint: Omit<[Checkpoint](../interfaces/checkpoint.Checkpoint.html)<string, string>, "channel_values" | "pending_sends">
    * channelValues: [Uint8Array, Uint8Array, Uint8Array][]
    * pendingSends: [Uint8Array, Uint8Array][]

#### Returns Promise<[Checkpoint](../interfaces/checkpoint.Checkpoint.html)<string, string>>

    * Defined in libs/checkpoint-postgres/dist/index.d.ts:52



### `Protected` _loadMetadata[](#_loadMetadata)

  * _loadMetadata(metadata): Promise<any>[](#_loadMetadata._loadMetadata-1)
  * #### Parameters

    * metadata: Record<string, unknown>

#### Returns Promise<any>

    * Defined in libs/checkpoint-postgres/dist/index.d.ts:54



### `Protected` _loadWrites[](#_loadWrites)

  * _loadWrites(writes): Promise<[string, string, unknown][]>[](#_loadWrites._loadWrites-1)
  * #### Parameters

    * writes: [Uint8Array, Uint8Array, Uint8Array, Uint8Array][]

#### Returns Promise<[string, string, unknown][]>

    * Defined in libs/checkpoint-postgres/dist/index.d.ts:55



### `Protected` _searchWhere[](#_searchWhere)

  * _searchWhere(config?, filter?, before?): [string, unknown[]][](#_searchWhere._searchWhere-1)
  * Return WHERE clause predicates for a given list() config, filter, cursor.

This method returns a tuple of a string and a tuple of values. The string is the parameterized WHERE clause predicate (including the WHERE keyword): "WHERE column1 = $1 AND column2 IS $2". The list of values contains the values for each of the corresponding parameters.

#### Parameters

    * `Optional` config: RunnableConfig<Record<string, any>>
    * `Optional` filter: Record<string, unknown>
    * `Optional` before: RunnableConfig<Record<string, any>>

#### Returns [string, unknown[]]

    * Defined in libs/checkpoint-postgres/dist/index.d.ts:68



### end[](#end)

  * end(): Promise<void>[](#end.end-1)
  * #### Returns Promise<void>

    * Defined in libs/checkpoint-postgres/dist/index.d.ts:107



### get[](#get)

  * get(config): Promise<undefined | [Checkpoint](../interfaces/checkpoint.Checkpoint.html)<string, string>>[](#get.get-1)
  * #### Parameters

    * config: RunnableConfig<Record<string, any>>

#### Returns Promise<undefined | [Checkpoint](../interfaces/checkpoint.Checkpoint.html)<string, string>>

Inherited from [BaseCheckpointSaver](checkpoint.BaseCheckpointSaver.html).[get](checkpoint.BaseCheckpointSaver.html#get)

    * Defined in libs/checkpoint/dist/base.d.ts:63



### getNextVersion[](#getNextVersion)

  * getNextVersion(current, _channel): number[](#getNextVersion.getNextVersion-1)
  * Generate the next version ID for a channel.

Default is to use integer versions, incrementing by 1. If you override, you can use str/int/float versions, as long as they are monotonically increasing.

#### Parameters

    * current: undefined | number
    * _channel: [ChannelProtocol](../interfaces/checkpoint.ChannelProtocol.html)<unknown, unknown, unknown>

#### Returns number

Inherited from [BaseCheckpointSaver](checkpoint.BaseCheckpointSaver.html).[getNextVersion](checkpoint.BaseCheckpointSaver.html#getNextVersion)

    * Defined in libs/checkpoint/dist/base.d.ts:77



### getTuple[](#getTuple)

  * getTuple(config): Promise<undefined | [CheckpointTuple](../interfaces/checkpoint.CheckpointTuple.html)>[](#getTuple.getTuple-1)
  * Get a checkpoint tuple from the database. This method retrieves a checkpoint tuple from the Postgres database based on the provided config. If the config's configurable field contains a "checkpoint_id" key, the checkpoint with the matching thread_id and namespace is retrieved. Otherwise, the latest checkpoint for the given thread_id is retrieved.

#### Parameters

    * config: RunnableConfig<Record<string, any>>

The config to use for retrieving the checkpoint.

#### Returns Promise<undefined | [CheckpointTuple](../interfaces/checkpoint.CheckpointTuple.html)>

The retrieved checkpoint tuple, or undefined.

Overrides [BaseCheckpointSaver](checkpoint.BaseCheckpointSaver.html).[getTuple](checkpoint.BaseCheckpointSaver.html#getTuple)

    * Defined in libs/checkpoint-postgres/dist/index.d.ts:79



### list[](#list)

  * list(config, options?): AsyncGenerator<[CheckpointTuple](../interfaces/checkpoint.CheckpointTuple.html), any, unknown>[](#list.list-1)
  * List checkpoints from the database.

This method retrieves a list of checkpoint tuples from the Postgres database based on the provided config. The checkpoints are ordered by checkpoint ID in descending order (newest first).

#### Parameters

    * config: RunnableConfig<Record<string, any>>
    * `Optional` options: [CheckpointListOptions](../types/checkpoint.CheckpointListOptions.html)

#### Returns AsyncGenerator<[CheckpointTuple](../interfaces/checkpoint.CheckpointTuple.html), any, unknown>

Overrides [BaseCheckpointSaver](checkpoint.BaseCheckpointSaver.html).[list](checkpoint.BaseCheckpointSaver.html#list)

    * Defined in libs/checkpoint-postgres/dist/index.d.ts:86



### put[](#put)

  * put(config, checkpoint, metadata, newVersions): Promise<RunnableConfig<Record<string, any>>>[](#put.put-1)
  * Save a checkpoint to the database.

This method saves a checkpoint to the Postgres database. The checkpoint is associated with the provided config and its parent config (if any).

#### Parameters

    * config: RunnableConfig<Record<string, any>>
    * checkpoint: [Checkpoint](../interfaces/checkpoint.Checkpoint.html)<string, string>
    * metadata: [CheckpointMetadata](../interfaces/checkpoint.CheckpointMetadata.html)
    * newVersions: [ChannelVersions](../types/checkpoint.ChannelVersions.html)

#### Returns Promise<RunnableConfig<Record<string, any>>>

Overrides [BaseCheckpointSaver](checkpoint.BaseCheckpointSaver.html).[put](checkpoint.BaseCheckpointSaver.html#put)

    * Defined in libs/checkpoint-postgres/dist/index.d.ts:97



### putWrites[](#putWrites)

  * putWrites(config, writes, taskId): Promise<void>[](#putWrites.putWrites-1)
  * Store intermediate writes linked to a checkpoint.

This method saves intermediate writes associated with a checkpoint to the Postgres database.

#### Parameters

    * config: RunnableConfig<Record<string, any>>

Configuration of the related checkpoint.

    * writes: [PendingWrite](../types/checkpoint.PendingWrite.html)<string>[]

List of writes to store.

    * taskId: string

Identifier for the task creating the writes.

#### Returns Promise<void>

Overrides [BaseCheckpointSaver](checkpoint.BaseCheckpointSaver.html).[putWrites](checkpoint.BaseCheckpointSaver.html#putWrites)

    * Defined in libs/checkpoint-postgres/dist/index.d.ts:106



### setup[](#setup)

  * setup(): Promise<void>[](#setup.setup-1)
  * Set up the checkpoint database asynchronously.

This method creates the necessary tables in the Postgres database if they don't already exist and runs database migrations. It MUST be called directly by the user the first time checkpointer is used.

#### Returns Promise<void>

    * Defined in libs/checkpoint-postgres/dist/index.d.ts:51



### `Static` fromConnString[](#fromConnString)

  * fromConnString(connString): [PostgresSaver](checkpoint_postgres.PostgresSaver.html)[](#fromConnString.fromConnString-1)
  * #### Parameters

    * connString: string

#### Returns [PostgresSaver](checkpoint_postgres.PostgresSaver.html)

    * Defined in libs/checkpoint-postgres/dist/index.d.ts:43



### Settings

#### Member Visibility

  * Protected
  * Private
  * Inherited
  * External



#### Theme

OSLightDark

### On This Page

[constructor](#constructor)[isSetup](#isSetup)[pool](#pool)[serde](#serde)[_dumpBlobs](#_dumpBlobs)[_dumpCheckpoint](#_dumpCheckpoint)[_dumpMetadata](#_dumpMetadata)[_dumpWrites](#_dumpWrites)[_loadBlobs](#_loadBlobs)[_loadCheckpoint](#_loadCheckpoint)[_loadMetadata](#_loadMetadata)[_loadWrites](#_loadWrites)[_searchWhere](#_searchWhere)[end](#end)[get](#get)[getNextVersion](#getNextVersion)[getTuple](#getTuple)[list](#list)[put](#put)[putWrites](#putWrites)[setup](#setup)[fromConnString](#fromConnString)

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
