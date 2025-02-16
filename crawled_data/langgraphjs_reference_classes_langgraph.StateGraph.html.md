---
url: https://langchain-ai.github.io/langgraphjs/reference/classes/langgraph.StateGraph.html
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
  * [StateGraph](langgraph.StateGraph.html)



# Class StateGraph<SD, S, U, N, I, O, C>

A graph whose nodes communicate by reading and writing to a shared state. Each node takes a defined `State` as input and returns a `Partial<State>`.

Each state key can optionally be annotated with a reducer function that will be used to aggregate the values of that key received from multiple nodes. The signature of a reducer function is (left: Value, right: UpdateValue) => Value.

See [Annotation](../modules/langgraph.Annotation.html) for more on defining state.

After adding nodes and edges to your graph, you must call `.compile()` on it before you can use it.

#### Example

```
import {typeBaseMessage,AIMessage,HumanMessage,} from"@langchain/core/messages";import { StateGraph, Annotation } from"@langchain/langgraph";// Define a state with a single key named "messages" that will// combine a returned BaseMessage or arrays of BaseMessagesconstStateAnnotation = Annotation.Root({sentiment:Annotation<string>,messages:Annotation<BaseMessage[]>({reducer: (left: BaseMessage[], right: BaseMessage | BaseMessage[]) => {if (Array.isArray(right)) {returnleft.concat(right);   }returnleft.concat([right]);  },default: () => [], }),});constgraphBuilder = newStateGraph(StateAnnotation);// A node in the graph that returns an object with a "messages" key// will update the state by combining the existing value with the returned one.constmyNode = (state: typeofStateAnnotation.State) => {return {messages: [newAIMessage("Some new response")],sentiment:"positive", };};constgraph = graphBuilder .addNode("myNode", myNode) .addEdge("__start__", "myNode") .addEdge("myNode", "__end__") .compile();awaitgraph.invoke({ messages: [newHumanMessage("how are you?")] });// {//  messages: [HumanMessage("how are you?"), AIMessage("Some new response")],//  sentiment: "positive",// }
Copy
```


#### Type Parameters

  * SD extends [StateDefinition](../interfaces/langgraph.StateDefinition.html) | unknown
  * S = [SD](langgraph.StateGraph.html#constructor.new_StateGraph.SD-1) extends [StateDefinition](../interfaces/langgraph.StateDefinition.html)? [StateType](../types/langgraph.StateType.html)<[SD](langgraph.StateGraph.html#constructor.new_StateGraph.SD-1)>: [SD](langgraph.StateGraph.html#constructor.new_StateGraph.SD-1)
  * U = [SD](langgraph.StateGraph.html#constructor.new_StateGraph.SD-1) extends [StateDefinition](../interfaces/langgraph.StateDefinition.html)? [UpdateType](../types/langgraph.UpdateType.html)<[SD](langgraph.StateGraph.html#constructor.new_StateGraph.SD-1)>: Partial<[S](langgraph.StateGraph.html#constructor.new_StateGraph.S-1)>
  * N extends string = typeof [START](../variables/langgraph.START.html)
  * I extends [StateDefinition](../interfaces/langgraph.StateDefinition.html) = [SD](langgraph.StateGraph.html#constructor.new_StateGraph.SD-1) extends [StateDefinition](../interfaces/langgraph.StateDefinition.html)? [SD](langgraph.StateGraph.html#constructor.new_StateGraph.SD-1): [StateDefinition](../interfaces/langgraph.StateDefinition.html)
  * O extends [StateDefinition](../interfaces/langgraph.StateDefinition.html) = [SD](langgraph.StateGraph.html#constructor.new_StateGraph.SD-1) extends [StateDefinition](../interfaces/langgraph.StateDefinition.html)? [SD](langgraph.StateGraph.html#constructor.new_StateGraph.SD-1): [StateDefinition](../interfaces/langgraph.StateDefinition.html)
  * C extends [StateDefinition](../interfaces/langgraph.StateDefinition.html) = [StateDefinition](../interfaces/langgraph.StateDefinition.html)



#### Hierarchy ([view full](../hierarchy.html#langgraph.StateGraph))

  * [Graph](langgraph.Graph.html)<[N](langgraph.StateGraph.html#constructor.new_StateGraph.N-1), [S](langgraph.StateGraph.html#constructor.new_StateGraph.S-1), [U](langgraph.StateGraph.html#constructor.new_StateGraph.U-1), StateGraphNodeSpec<[S](langgraph.StateGraph.html#constructor.new_StateGraph.S-1), [U](langgraph.StateGraph.html#constructor.new_StateGraph.U-1)>, [C](langgraph.StateGraph.html#constructor.new_StateGraph.C-1)>
    * StateGraph



  * Defined in libs/langgraph/dist/graph/state.d.ts:99



#####  Index

### Constructors

[constructor](langgraph.StateGraph.html#constructor)

### Properties

[_configSchema](langgraph.StateGraph.html#_configSchema) [_inputDefinition](langgraph.StateGraph.html#_inputDefinition) [_outputDefinition](langgraph.StateGraph.html#_outputDefinition) [_schemaDefinition](langgraph.StateGraph.html#_schemaDefinition) [_schemaDefinitions](langgraph.StateGraph.html#_schemaDefinitions) [branches](langgraph.StateGraph.html#branches) [channels](langgraph.StateGraph.html#channels) [compiled](langgraph.StateGraph.html#compiled) [edges](langgraph.StateGraph.html#edges) [entryPoint?](langgraph.StateGraph.html#entryPoint) [nodes](langgraph.StateGraph.html#nodes) [waitingEdges](langgraph.StateGraph.html#waitingEdges)

### Accessors

[allEdges](langgraph.StateGraph.html#allEdges)

### Methods

[_addSchema](langgraph.StateGraph.html#_addSchema) [addConditionalEdges](langgraph.StateGraph.html#addConditionalEdges) [addEdge](langgraph.StateGraph.html#addEdge) [addNode](langgraph.StateGraph.html#addNode) [compile](langgraph.StateGraph.html#compile) [setEntryPoint](langgraph.StateGraph.html#setEntryPoint) [setFinishPoint](langgraph.StateGraph.html#setFinishPoint) [validate](langgraph.StateGraph.html#validate) [warnIfCompiled](langgraph.StateGraph.html#warnIfCompiled)

## Constructors

### constructor[](#constructor)

  * new StateGraph<[SD](langgraph.StateGraph.html#constructor.new_StateGraph.SD-1), [S](langgraph.StateGraph.html#constructor.new_StateGraph.S-1), [U](langgraph.StateGraph.html#constructor.new_StateGraph.U-1), [N](langgraph.StateGraph.html#constructor.new_StateGraph.N-1), [I](langgraph.StateGraph.html#constructor.new_StateGraph.I-1), [O](langgraph.StateGraph.html#constructor.new_StateGraph.O-1), [C](langgraph.StateGraph.html#constructor.new_StateGraph.C-1)>(fields, configSchema?): [StateGraph](langgraph.StateGraph.html)<[SD](langgraph.StateGraph.html#constructor.new_StateGraph.SD-1), [S](langgraph.StateGraph.html#constructor.new_StateGraph.S-1), [U](langgraph.StateGraph.html#constructor.new_StateGraph.U-1), [N](langgraph.StateGraph.html#constructor.new_StateGraph.N-1), [I](langgraph.StateGraph.html#constructor.new_StateGraph.I-1), [O](langgraph.StateGraph.html#constructor.new_StateGraph.O-1), [C](langgraph.StateGraph.html#constructor.new_StateGraph.C-1)>[](#constructor.new_StateGraph)
  * #### Type Parameters

    * SD extends unknown
    * S = [SD](langgraph.StateGraph.html#constructor.new_StateGraph.SD-1) extends [StateDefinition](../interfaces/langgraph.StateDefinition.html)? [StateType](../types/langgraph.StateType.html)<[SD](langgraph.StateGraph.html#constructor.new_StateGraph.SD-1)<[SD](langgraph.StateGraph.html#constructor.new_StateGraph.SD-1)>>: [SD](langgraph.StateGraph.html#constructor.new_StateGraph.SD-1)
    * U = [SD](langgraph.StateGraph.html#constructor.new_StateGraph.SD-1) extends [StateDefinition](../interfaces/langgraph.StateDefinition.html)? [UpdateType](../types/langgraph.UpdateType.html)<[SD](langgraph.StateGraph.html#constructor.new_StateGraph.SD-1)<[SD](langgraph.StateGraph.html#constructor.new_StateGraph.SD-1)>>: Partial<[S](langgraph.StateGraph.html#constructor.new_StateGraph.S-1)>
    * N extends string = "__start__"
    * I extends [StateDefinition](../interfaces/langgraph.StateDefinition.html) = [SD](langgraph.StateGraph.html#constructor.new_StateGraph.SD-1) extends [StateDefinition](../interfaces/langgraph.StateDefinition.html)? [SD](langgraph.StateGraph.html#constructor.new_StateGraph.SD-1)<[SD](langgraph.StateGraph.html#constructor.new_StateGraph.SD-1)>: [StateDefinition](../interfaces/langgraph.StateDefinition.html)
    * O extends [StateDefinition](../interfaces/langgraph.StateDefinition.html) = [SD](langgraph.StateGraph.html#constructor.new_StateGraph.SD-1) extends [StateDefinition](../interfaces/langgraph.StateDefinition.html)? [SD](langgraph.StateGraph.html#constructor.new_StateGraph.SD-1)<[SD](langgraph.StateGraph.html#constructor.new_StateGraph.SD-1)>: [StateDefinition](../interfaces/langgraph.StateDefinition.html)
    * C extends [StateDefinition](../interfaces/langgraph.StateDefinition.html) = [StateDefinition](../interfaces/langgraph.StateDefinition.html)

#### Parameters

    * fields: [SD](langgraph.StateGraph.html#constructor.new_StateGraph.SD-1) extends [StateDefinition](../interfaces/langgraph.StateDefinition.html)? [SD](langgraph.StateGraph.html#constructor.new_StateGraph.SD-1)<[SD](langgraph.StateGraph.html#constructor.new_StateGraph.SD-1)> | [AnnotationRoot](langgraph.AnnotationRoot.html)<[SD](langgraph.StateGraph.html#constructor.new_StateGraph.SD-1)<[SD](langgraph.StateGraph.html#constructor.new_StateGraph.SD-1)>> | [StateGraphArgs](../interfaces/langgraph.StateGraphArgs.html)<[S](langgraph.StateGraph.html#constructor.new_StateGraph.S-1)> | StateGraphArgsWithStateSchema<[SD](langgraph.StateGraph.html#constructor.new_StateGraph.SD-1)<[SD](langgraph.StateGraph.html#constructor.new_StateGraph.SD-1)>, [I](langgraph.StateGraph.html#constructor.new_StateGraph.I-1), [O](langgraph.StateGraph.html#constructor.new_StateGraph.O-1)> | StateGraphArgsWithInputOutputSchemas<[SD](langgraph.StateGraph.html#constructor.new_StateGraph.SD-1)<[SD](langgraph.StateGraph.html#constructor.new_StateGraph.SD-1)>, [O](langgraph.StateGraph.html#constructor.new_StateGraph.O-1)>: [StateGraphArgs](../interfaces/langgraph.StateGraphArgs.html)<[S](langgraph.StateGraph.html#constructor.new_StateGraph.S-1)>
    * `Optional` configSchema: [AnnotationRoot](langgraph.AnnotationRoot.html)<[C](langgraph.StateGraph.html#constructor.new_StateGraph.C-1)>

#### Returns [StateGraph](langgraph.StateGraph.html)<[SD](langgraph.StateGraph.html#constructor.new_StateGraph.SD-1), [S](langgraph.StateGraph.html#constructor.new_StateGraph.S-1), [U](langgraph.StateGraph.html#constructor.new_StateGraph.U-1), [N](langgraph.StateGraph.html#constructor.new_StateGraph.N-1), [I](langgraph.StateGraph.html#constructor.new_StateGraph.I-1), [O](langgraph.StateGraph.html#constructor.new_StateGraph.O-1), [C](langgraph.StateGraph.html#constructor.new_StateGraph.C-1)>

Overrides [Graph](langgraph.Graph.html).[constructor](langgraph.Graph.html#constructor)

    * Defined in libs/langgraph/dist/graph/state.d.ts:115



## Properties

### `Internal` _configSchema[](#_configSchema)

_configSchema: undefined | [C](langgraph.StateGraph.html#constructor.new_StateGraph.C-1)

Used only for typing.

  * Defined in libs/langgraph/dist/graph/state.d.ts:114



### `Internal` _inputDefinition[](#_inputDefinition)

_inputDefinition: [I](langgraph.StateGraph.html#constructor.new_StateGraph.I-1)

  * Defined in libs/langgraph/dist/graph/state.d.ts:105



### `Internal` _outputDefinition[](#_outputDefinition)

_outputDefinition: [O](langgraph.StateGraph.html#constructor.new_StateGraph.O-1)

  * Defined in libs/langgraph/dist/graph/state.d.ts:107



### `Internal` _schemaDefinition[](#_schemaDefinition)

_schemaDefinition: [StateDefinition](../interfaces/langgraph.StateDefinition.html)

  * Defined in libs/langgraph/dist/graph/state.d.ts:103



### `Internal` _schemaDefinitions[](#_schemaDefinitions)

_schemaDefinitions: Map<any, any>

Map schemas to managed values

  * Defined in libs/langgraph/dist/graph/state.d.ts:112



### branches[](#branches)

branches: Record<string, Record<string, Branch<[S](langgraph.StateGraph.html#constructor.new_StateGraph.S-1), [N](langgraph.StateGraph.html#constructor.new_StateGraph.N-1), any>>>

Inherited from [Graph](langgraph.Graph.html).[branches](langgraph.Graph.html#branches)

  * Defined in libs/langgraph/dist/graph/graph.d.ts:39



### channels[](#channels)

channels: Record<string, [BaseChannel](langgraph.BaseChannel.html)<unknown, unknown, unknown> | [ManagedValueSpec](../types/langgraph.ManagedValueSpec.html)>

  * Defined in libs/langgraph/dist/graph/state.d.ts:100



### compiled[](#compiled)

compiled: boolean

Inherited from [Graph](langgraph.Graph.html).[compiled](langgraph.Graph.html#compiled)

  * Defined in libs/langgraph/dist/graph/graph.d.ts:41



### edges[](#edges)

edges: Set<["__start__" | [N](langgraph.StateGraph.html#constructor.new_StateGraph.N-1), "__end__" | [N](langgraph.StateGraph.html#constructor.new_StateGraph.N-1)]>

Inherited from [Graph](langgraph.Graph.html).[edges](langgraph.Graph.html#edges)

  * Defined in libs/langgraph/dist/graph/graph.d.ts:38



### `Optional` entryPoint[](#entryPoint)

entryPoint?: string

Inherited from [Graph](langgraph.Graph.html).[entryPoint](langgraph.Graph.html#entryPoint)

  * Defined in libs/langgraph/dist/graph/graph.d.ts:40



### nodes[](#nodes)

nodes: Record<[N](langgraph.StateGraph.html#constructor.new_StateGraph.N-1), StateGraphNodeSpec<[S](langgraph.StateGraph.html#constructor.new_StateGraph.S-1), [U](langgraph.StateGraph.html#constructor.new_StateGraph.U-1)>>

Inherited from [Graph](langgraph.Graph.html).[nodes](langgraph.Graph.html#nodes)

  * Defined in libs/langgraph/dist/graph/graph.d.ts:37



### waitingEdges[](#waitingEdges)

waitingEdges: Set<[[N](langgraph.StateGraph.html#constructor.new_StateGraph.N-1)[], [N](langgraph.StateGraph.html#constructor.new_StateGraph.N-1)]>

  * Defined in libs/langgraph/dist/graph/state.d.ts:101



## Accessors

### allEdges[](#allEdges)

  * get allEdges(): Set<[string, string]>
  * #### Returns Set<[string, string]>

Overrides Graph.allEdges

    * Defined in libs/langgraph/dist/graph/state.d.ts:116



## Methods

### _addSchema[](#_addSchema)

  * _addSchema(stateDefinition): void[](#_addSchema._addSchema-1)
  * #### Parameters

    * stateDefinition: [StateDefinition](../interfaces/langgraph.StateDefinition.html)

#### Returns void

    * Defined in libs/langgraph/dist/graph/state.d.ts:117



### addConditionalEdges[](#addConditionalEdges)

  * addConditionalEdges(source): this[](#addConditionalEdges.addConditionalEdges-1)
  * #### Parameters

    * source: BranchOptions<[S](langgraph.StateGraph.html#constructor.new_StateGraph.S-1), [N](langgraph.StateGraph.html#constructor.new_StateGraph.N-1), [LangGraphRunnableConfig](../interfaces/langgraph.LangGraphRunnableConfig.html)<[StateType](../types/langgraph.StateType.html)<[C](langgraph.StateGraph.html#constructor.new_StateGraph.C-1)>>>

#### Returns this

Inherited from [Graph](langgraph.Graph.html).[addConditionalEdges](langgraph.Graph.html#addConditionalEdges)

    * Defined in libs/langgraph/dist/graph/graph.d.ts:47
  * addConditionalEdges(source, path, pathMap?): this[](#addConditionalEdges.addConditionalEdges-2)
  * #### Parameters

    * source: [N](langgraph.StateGraph.html#constructor.new_StateGraph.N-1)
    * path: RunnableLike<[S](langgraph.StateGraph.html#constructor.new_StateGraph.S-1), BranchPathReturnValue, [LangGraphRunnableConfig](../interfaces/langgraph.LangGraphRunnableConfig.html)<[StateType](../types/langgraph.StateType.html)<[C](langgraph.StateGraph.html#constructor.new_StateGraph.C-1)>>>
    * `Optional` pathMap: Record<string, "__end__" | [N](langgraph.StateGraph.html#constructor.new_StateGraph.N-1)> | ("__end__" | [N](langgraph.StateGraph.html#constructor.new_StateGraph.N-1))[]

#### Returns this

Inherited from [Graph](langgraph.Graph.html).[addConditionalEdges](langgraph.Graph.html#addConditionalEdges)

    * Defined in libs/langgraph/dist/graph/graph.d.ts:48



### addEdge[](#addEdge)

  * addEdge(startKey, endKey): this[](#addEdge.addEdge-1)
  * #### Parameters

    * startKey: "__start__" | [N](langgraph.StateGraph.html#constructor.new_StateGraph.N-1) | [N](langgraph.StateGraph.html#constructor.new_StateGraph.N-1)[]
    * endKey: "__end__" | [N](langgraph.StateGraph.html#constructor.new_StateGraph.N-1)

#### Returns this

Overrides [Graph](langgraph.Graph.html).[addEdge](langgraph.Graph.html#addEdge)

    * Defined in libs/langgraph/dist/graph/state.d.ts:119



### addNode[](#addNode)

  * addNode<[K](langgraph.StateGraph.html#addNode.addNode-1.K), [NodeInput](langgraph.StateGraph.html#addNode.addNode-1.NodeInput)>(key, action, options?): [StateGraph](langgraph.StateGraph.html)<[SD](langgraph.StateGraph.html#constructor.new_StateGraph.SD-1), [S](langgraph.StateGraph.html#constructor.new_StateGraph.S-1), [U](langgraph.StateGraph.html#constructor.new_StateGraph.U-1), [N](langgraph.StateGraph.html#constructor.new_StateGraph.N-1) | [K](langgraph.StateGraph.html#addNode.addNode-1.K), [I](langgraph.StateGraph.html#constructor.new_StateGraph.I-1), [O](langgraph.StateGraph.html#constructor.new_StateGraph.O-1), [C](langgraph.StateGraph.html#constructor.new_StateGraph.C-1)>[](#addNode.addNode-1)
  * #### Type Parameters

    * K extends string
    * NodeInput = [S](langgraph.StateGraph.html#constructor.new_StateGraph.S-1)

#### Parameters

    * key: [K](langgraph.StateGraph.html#addNode.addNode-1.K)
    * action: RunnableLike<[NodeInput](langgraph.StateGraph.html#addNode.addNode-1.NodeInput), [U](langgraph.StateGraph.html#constructor.new_StateGraph.U-1) extends object? [U](langgraph.StateGraph.html#constructor.new_StateGraph.U-1)<[U](langgraph.StateGraph.html#constructor.new_StateGraph.U-1)> & Record<string, any>: [U](langgraph.StateGraph.html#constructor.new_StateGraph.U-1), [LangGraphRunnableConfig](../interfaces/langgraph.LangGraphRunnableConfig.html)<[StateType](../types/langgraph.StateType.html)<[C](langgraph.StateGraph.html#constructor.new_StateGraph.C-1)>>>
    * `Optional` options: StateGraphAddNodeOptions

#### Returns [StateGraph](langgraph.StateGraph.html)<[SD](langgraph.StateGraph.html#constructor.new_StateGraph.SD-1), [S](langgraph.StateGraph.html#constructor.new_StateGraph.S-1), [U](langgraph.StateGraph.html#constructor.new_StateGraph.U-1), [N](langgraph.StateGraph.html#constructor.new_StateGraph.N-1) | [K](langgraph.StateGraph.html#addNode.addNode-1.K), [I](langgraph.StateGraph.html#constructor.new_StateGraph.I-1), [O](langgraph.StateGraph.html#constructor.new_StateGraph.O-1), [C](langgraph.StateGraph.html#constructor.new_StateGraph.C-1)>

Overrides [Graph](langgraph.Graph.html).[addNode](langgraph.Graph.html#addNode)

    * Defined in libs/langgraph/dist/graph/state.d.ts:118



### compile[](#compile)

  * compile(__namedParameters?): [CompiledStateGraph](langgraph.CompiledStateGraph.html)<[S](langgraph.StateGraph.html#constructor.new_StateGraph.S-1), [U](langgraph.StateGraph.html#constructor.new_StateGraph.U-1), [N](langgraph.StateGraph.html#constructor.new_StateGraph.N-1), [I](langgraph.StateGraph.html#constructor.new_StateGraph.I-1), [O](langgraph.StateGraph.html#constructor.new_StateGraph.O-1), [C](langgraph.StateGraph.html#constructor.new_StateGraph.C-1)>[](#compile.compile-1)
  * #### Parameters

    * `Optional` __namedParameters: { checkpointer?: false | [BaseCheckpointSaver](checkpoint.BaseCheckpointSaver.html)<number>; interruptAfter?: "*" | [N](langgraph.StateGraph.html#constructor.new_StateGraph.N-1)[]; interruptBefore?: "*" | [N](langgraph.StateGraph.html#constructor.new_StateGraph.N-1)[]; name?: string; store?: [BaseStore](checkpoint.BaseStore.html); }
      * ##### `Optional` checkpointer?: false | [BaseCheckpointSaver](checkpoint.BaseCheckpointSaver.html)<number>

      * ##### `Optional` interruptAfter?: "*" | [N](langgraph.StateGraph.html#constructor.new_StateGraph.N-1)[]

      * ##### `Optional` interruptBefore?: "*" | [N](langgraph.StateGraph.html#constructor.new_StateGraph.N-1)[]

      * ##### `Optional` name?: string

      * ##### `Optional` store?: [BaseStore](checkpoint.BaseStore.html)

#### Returns [CompiledStateGraph](langgraph.CompiledStateGraph.html)<[S](langgraph.StateGraph.html#constructor.new_StateGraph.S-1), [U](langgraph.StateGraph.html#constructor.new_StateGraph.U-1), [N](langgraph.StateGraph.html#constructor.new_StateGraph.N-1), [I](langgraph.StateGraph.html#constructor.new_StateGraph.I-1), [O](langgraph.StateGraph.html#constructor.new_StateGraph.O-1), [C](langgraph.StateGraph.html#constructor.new_StateGraph.C-1)>

Overrides [Graph](langgraph.Graph.html).[compile](langgraph.Graph.html#compile)

    * Defined in libs/langgraph/dist/graph/state.d.ts:120



### setEntryPoint[](#setEntryPoint)

  * setEntryPoint(key): this[](#setEntryPoint.setEntryPoint-1)
  * #### Parameters

    * key: [N](langgraph.StateGraph.html#constructor.new_StateGraph.N-1)

#### Returns this

#### Deprecated

use `addEdge(START, key)` instead

Inherited from [Graph](langgraph.Graph.html).[setEntryPoint](langgraph.Graph.html#setEntryPoint)

    * Defined in libs/langgraph/dist/graph/graph.d.ts:52



### setFinishPoint[](#setFinishPoint)

  * setFinishPoint(key): this[](#setFinishPoint.setFinishPoint-1)
  * #### Parameters

    * key: [N](langgraph.StateGraph.html#constructor.new_StateGraph.N-1)

#### Returns this

#### Deprecated

use `addEdge(key, END)` instead

Inherited from [Graph](langgraph.Graph.html).[setFinishPoint](langgraph.Graph.html#setFinishPoint)

    * Defined in libs/langgraph/dist/graph/graph.d.ts:56



### validate[](#validate)

  * validate(interrupt?): void[](#validate.validate-1)
  * #### Parameters

    * `Optional` interrupt: string[]

#### Returns void

Inherited from [Graph](langgraph.Graph.html).[validate](langgraph.Graph.html#validate)

    * Defined in libs/langgraph/dist/graph/graph.d.ts:63



### `Protected` warnIfCompiled[](#warnIfCompiled)

  * warnIfCompiled(message): void[](#warnIfCompiled.warnIfCompiled-1)
  * #### Parameters

    * message: string

#### Returns void

Inherited from [Graph](langgraph.Graph.html).[warnIfCompiled](langgraph.Graph.html#warnIfCompiled)

    * Defined in libs/langgraph/dist/graph/graph.d.ts:43



### Settings

#### Member Visibility

  * Protected
  * Private
  * Inherited
  * External



#### Theme

OSLightDark

### On This Page

[constructor](#constructor)[_configSchema](#_configSchema)[_inputDefinition](#_inputDefinition)[_outputDefinition](#_outputDefinition)[_schemaDefinition](#_schemaDefinition)[_schemaDefinitions](#_schemaDefinitions)[branches](#branches)[channels](#channels)[compiled](#compiled)[edges](#edges)[entryPoint](#entryPoint)[nodes](#nodes)[waitingEdges](#waitingEdges)[allEdges](#allEdges)[_addSchema](#_addSchema)[addConditionalEdges](#addConditionalEdges)[addEdge](#addEdge)[addNode](#addNode)[compile](#compile)[setEntryPoint](#setEntryPoint)[setFinishPoint](#setFinishPoint)[validate](#validate)[warnIfCompiled](#warnIfCompiled)

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
