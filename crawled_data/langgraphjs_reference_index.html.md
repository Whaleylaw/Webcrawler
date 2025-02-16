---
url: https://langchain-ai.github.io/langgraphjs/reference/index.html
title: Untitled
date_crawled: 
---

[Back to documentation](/langgraphjs/)

  * Preparing search index...
  * The search index is not available

[API Reference](/)

[](#)

## API Reference

# [🦜🕸️LangGraph.js](#md:🦜🕸️langgraphjs)

[![Docs](https://img.shields.io/badge/docs-latest-blue)](https://langchain-ai.github.io/langgraphjs/) ![Version](https://img.shields.io/npm/v/@langchain/langgraph?logo=npm)[![Downloads](https://img.shields.io/npm/dm/@langchain/langgraph)](https://www.npmjs.com/package/@langchain/langgraph) [![Open Issues](https://img.shields.io/github/issues-raw/langchain-ai/langgraphjs)](https://github.com/langchain-ai/langgraphjs/issues)

⚡ Building language agents as graphs ⚡

> [!NOTE] Looking for the Python version? See the [Python repo](https://github.com/langchain-ai/langgraph) and the [Python docs](https://langchain-ai.github.io/langgraph/).

## [Overview](#md:overview)

[LangGraph](https://langchain-ai.github.io/langgraphjs/) is a library for building stateful, multi-actor applications with LLMs, used to create agent and multi-agent workflows. Check out an introductory tutorial [here](https://langchain-ai.github.io/langgraphjs/tutorials/quickstart/).

LangGraph is inspired by [Pregel](https://research.google/pubs/pub37252/) and [Apache Beam](https://beam.apache.org/). The public interface draws inspiration from [NetworkX](https://networkx.org/documentation/latest/). LangGraph is built by LangChain Inc, the creators of LangChain, but can be used without LangChain.

### [Why use LangGraph?](#md:why-use-langgraph)

LangGraph powers [production-grade agents](https://www.langchain.com/built-with-langgraph), trusted by Linkedin, Uber, Klarna, GitLab, and many more. LangGraph provides fine-grained control over both the flow and state of your agent applications. It implements a central [persistence layer](https://langchain-ai.github.io/langgraphjs/concepts/persistence/), enabling features that are common to most agent architectures:

  * **Memory** : LangGraph persists arbitrary aspects of your application's state, supporting memory of conversations and other updates within and across user interactions;
  * **Human-in-the-loop** : Because state is checkpointed, execution can be interrupted and resumed, allowing for decisions, validation, and corrections at key stages via human input.



Standardizing these components allows individuals and teams to focus on the behavior of their agent, instead of its supporting infrastructure.

Through [LangGraph Platform](#md:langgraph-platform), LangGraph also provides tooling for the development, deployment, debugging, and monitoring of your applications.

LangGraph integrates seamlessly with [LangChain](https://js.langchain.com/docs/introduction/) and [LangSmith](https://docs.smith.langchain.com/) (but does not require them).

To learn more about LangGraph, check out our first LangChain Academy course, _Introduction to LangGraph_ , available for free [here](https://academy.langchain.com/courses/intro-to-langgraph).

### [LangGraph Platform](#md:langgraph-platform)

[LangGraph Platform](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_platform) is infrastructure for deploying LangGraph agents. It is a commercial solution for deploying agentic applications to production, built on the open-source LangGraph framework. The LangGraph Platform consists of several components that work together to support the development, deployment, debugging, and monitoring of LangGraph applications: [LangGraph Server](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_server) (APIs), [LangGraph SDKs](https://langchain-ai.github.io/langgraphjs/concepts/sdk) (clients for the APIs), [LangGraph CLI](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_cli) (command line tool for building the server), and [LangGraph Studio](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_studio) (UI/debugger).

See deployment options [here](https://langchain-ai.github.io/langgraphjs/concepts/deployment_options/) (includes a free tier).

Here are some common issues that arise in complex deployments, which LangGraph Platform addresses:

  * **Streaming support** : LangGraph Server provides [multiple streaming modes](https://langchain-ai.github.io/langgraphjs/concepts/streaming) optimized for various application needs
  * **Background runs** : Runs agents asynchronously in the background
  * **Support for long running agents** : Infrastructure that can handle long running processes
  * **[Double texting](https://langchain-ai.github.io/langgraphjs/concepts/double_texting)** : Handle the case where you get two messages from the user before the agent can respond
  * **Handle burstiness** : Task queue for ensuring requests are handled consistently without loss, even under heavy loads



## [Installation](#md:installation)

```
npminstall@langchain/langgraph@langchain/core
Copy
```


## [Example](#md:example)

Let's build a tool-calling [ReAct-style](https://langchain-ai.github.io/langgraphjs/concepts/agentic_concepts/#react-implementation) agent that uses a search tool!

```
npminstall@langchain/anthropiczod
Copy
```
```
exportANTHROPIC_API_KEY=sk-...
Copy
```


Optionally, we can set up [LangSmith](https://docs.smith.langchain.com/) for best-in-class observability.

```
exportLANGSMITH_TRACING=trueexportLANGSMITH_API_KEY=lsv2_sk_...
Copy
```


The simplest way to create a tool-calling agent in LangGraph is to use `createReactAgent`[](https://langchain-ai.github.io/langgraphjs/reference/functions/langgraph_prebuilt.createReactAgent.html):

High-level implementation ```
import { createReactAgent } from"@langchain/langgraph/prebuilt";import { MemorySaver } from"@langchain/langgraph";import { ChatAnthropic } from"@langchain/anthropic";import { tool } from"@langchain/core/tools";import { z } from"zod";// Define the tools for the agent to useconstsearch = tool(async ({ query }) => {// This is a placeholder, but don't tell the LLM that...if (query.toLowerCase().includes("sf") || query.toLowerCase().includes("san francisco")) {return"It's 60 degrees and foggy." }return"It's 90 degrees and sunny."}, {name:"search",description:"Call to surf the web.",schema:z.object({query:z.string().describe("The query to use in your search."), }),});consttools = [search];constmodel = newChatAnthropic({model:"claude-3-5-sonnet-latest"});// Initialize memory to persist state between graph runsconstcheckpointer = newMemorySaver();constapp = createReactAgent({llm:model,tools,checkpointSaver:checkpointer,});// Use the agentconstresult = awaitapp.invoke( {messages: [{role:"user",content:"what is the weather in sf"  }] }, { configurable: { thread_id:42 } });console.log(result.messages.at(-1)?.content);
Copy
```
```
"Based on the search results, it's currently 60 degrees Fahrenheit and foggy in San Francisco, which is quite typical weather for the city."
Copy
```


Now when we pass the same `"thread_id"`, the conversation context is retained via the saved state (i.e. stored list of messages)

```
constfollowup = awaitapp.invoke( {messages: [{role:"user",content:"what about ny"  }] }, { configurable: { thread_id:42 } });console.log(followup.messages.at(-1)?.content);
Copy
```
```
"According to the search results, it's currently 90 degrees Fahrenheit and sunny in New York City. That's quite a warm day for New York!"
Copy
```


> [!TIP] LangGraph is a **low-level** framework that allows you to implement any custom agent architectures. Click on the low-level implementation below to see how to implement a tool-calling agent from scratch.

Low-level implementation ```
import { AIMessage, BaseMessage, HumanMessage } from"@langchain/core/messages";import { tool } from"@langchain/core/tools";import { z } from"zod";import { ChatAnthropic } from"@langchain/anthropic";import { StateGraph } from"@langchain/langgraph";import { MemorySaver, Annotation, messagesStateReducer } from"@langchain/langgraph";import { ToolNode } from"@langchain/langgraph/prebuilt";// Define the graph state// See here for more info: https://langchain-ai.github.io/langgraphjs/how-tos/define-state/constStateAnnotation = Annotation.Root({messages:Annotation<BaseMessage[]>({// `messagesStateReducer` function defines how `messages` state key should be updated// (in this case it appends new messages to the list and overwrites messages with the same ID)reducer:messagesStateReducer, }),});// Define the tools for the agent to useconstweatherTool = tool(async ({ query }) => {// This is a placeholder for the actual implementationif (query.toLowerCase().includes("sf") || query.toLowerCase().includes("san francisco")) {return"It's 60 degrees and foggy." }return"It's 90 degrees and sunny."}, {name:"weather",description:"Call to get the current weather for a location.",schema:z.object({query:z.string().describe("The query to use in your search."), }),});consttools = [weatherTool];consttoolNode = newToolNode(tools);constmodel = newChatAnthropic({model:"claude-3-5-sonnet-20240620",temperature:0,}).bindTools(tools);// Define the function that determines whether to continue or not// We can extract the state typing via `StateAnnotation.State`functionshouldContinue(state: typeofStateAnnotation.State) {constmessages = state.messages;constlastMessage = messages[messages.length - 1] asAIMessage;// If the LLM makes a tool call, then we route to the "tools" nodeif (lastMessage.tool_calls?.length) {return"tools"; }// Otherwise, we stop (reply to the user)return"__end__";}// Define the function that calls the modelasyncfunctioncallModel(state: typeofStateAnnotation.State) {constmessages = state.messages;constresponse = awaitmodel.invoke(messages);// We return a list, because this will get added to the existing listreturn { messages: [response] };}// Define a new graphconstworkflow = newStateGraph(StateAnnotation) .addNode("agent", callModel) .addNode("tools", toolNode) .addEdge("__start__", "agent") .addConditionalEdges("agent", shouldContinue) .addEdge("tools", "agent");// Initialize memory to persist state between graph runsconstcheckpointer = newMemorySaver();// Finally, we compile it!// This compiles it into a LangChain Runnable.// Note that we're (optionally) passing the memory when compiling the graphconstapp = workflow.compile({ checkpointer });// Use the RunnableconstfinalState = awaitapp.invoke( { messages: [newHumanMessage("what is the weather in sf")] }, { configurable: { thread_id:"42" } });console.log(finalState.messages[finalState.messages.length - 1].content);
Copy
```


**Step-by-step Breakdown** :

Initialize the model and tools.

  * We use `ChatAnthropic` as our LLM. **NOTE:** we need to make sure the model knows that it has these tools available to call. We can do this by converting the LangChain tools into the format for OpenAI tool calling using the `.bindTools()` method. 
  * We define the tools we want to use - a search tool in our case. It is really easy to create your own tools - see documentation here on how to do that [here](https://js.langchain.com/docs/how_to/custom_tools). 

Initialize graph with state.

  * We initialize the graph (`StateGraph`) by passing state schema with a reducer that defines how the state should be updated. In our case, we want to append new messages to the list and overwrite messages with the same ID, so we use the prebuilt `messagesStateReducer`.

Define graph nodes.

There are two main nodes we need:

  * The `agent` node: responsible for deciding what (if any) actions to take.
  * The `tools` node that invokes tools: if the agent decides to take an action, this node will then execute that action.

Define entry point and graph edges.

First, we need to set the entry point for graph execution - `agent` node.

Then we define one normal and one conditional edge. Conditional edge means that the destination depends on the contents of the graph's state. In our case, the destination is not known until the agent (LLM) decides.

  * Conditional edge: after the agent is called, we should either: 
    * a. Run tools if the agent said to take an action, OR
    * b. Finish (respond to the user) if the agent did not ask to run tools
  * Normal edge: after the tools are invoked, the graph should always return to the agent to decide what to do next

Compile the graph.

  * When we compile the graph, we turn it into a LangChain [Runnable](https://js.langchain.com/docs/concepts/runnables), which automatically enables calling `.invoke()`, `.stream()` and `.batch()` with your inputs 
  * We can also optionally pass checkpointer object for persisting state between graph runs, and enabling memory, human-in-the-loop workflows, time travel and more. In our case we use `MemorySaver` - a simple in-memory checkpointer 

Execute the graph.

  1. LangGraph adds the input message to the internal state, then passes the state to the entrypoint node, `"agent"`.
  2. The `"agent"` node executes, invoking the chat model.
  3. The chat model returns an `AIMessage`. LangGraph adds this to the state.
  4. Graph cycles the following steps until there are no more `tool_calls` on `AIMessage`: 
     * If `AIMessage` has `tool_calls`, `"tools"` node executes
     * The `"agent"` node executes again and returns `AIMessage`
  5. Execution progresses to the special `END` value and outputs the final state. And as a result, we get a list of all our chat messages as output.



## [Documentation](#md:documentation)

  * [Tutorials](https://langchain-ai.github.io/langgraphjs/tutorials/): Learn to build with LangGraph through guided examples.
  * [How-to Guides](https://langchain-ai.github.io/langgraphjs/how-tos/): Accomplish specific things within LangGraph, from streaming, to adding memory & persistence, to common design patterns (branching, subgraphs, etc.), these are the place to go if you want to copy and run a specific code snippet.
  * [Conceptual Guides](https://langchain-ai.github.io/langgraphjs/concepts/high_level/): In-depth explanations of the key concepts and principles behind LangGraph, such as nodes, edges, state and more.
  * [API Reference](https://langchain-ai.github.io/langgraphjs/reference/): Review important classes and methods, simple examples of how to use the graph and checkpointing APIs, higher-level prebuilt components and more.
  * [LangGraph Platform](https://langchain-ai.github.io/langgraphjs/concepts/#langgraph-platform): LangGraph Platform is a commercial solution for deploying agentic applications in production, built on the open-source LangGraph framework.



## [Resources](#md:resources)

  * [Built with LangGraph](https://www.langchain.com/built-with-langgraph): Hear how industry leaders use LangGraph to ship powerful, production-ready AI applications.



## [Contributing](#md:contributing)

For more information on how to contribute, see [here](https://github.com/langchain-ai/langgraphjs/blob/main/CONTRIBUTING.md).

### Settings

#### Member Visibility

  * Protected
  * Private
  * Inherited
  * External



#### Theme

OSLightDark

### On This Page

[🦜🕸️LangGraph.js](#md:🦜🕸️langgraphjs)

  * [Overview](#md:overview)
  *     * [Why use LangGraph?](#md:why-use-langgraph)
    * [LangGraph Platform](#md:langgraph-platform)
  * [Installation](#md:installation)
  * [Example](#md:example)
  * [Documentation](#md:documentation)
  * [Resources](#md:resources)
  * [Contributing](#md:contributing)



[API Reference](index.html)

  * [checkpoint](./modules/checkpoint.html)

    * [AsyncBatchedStore](./classes/checkpoint.AsyncBatchedStore.html)
    * [BaseCheckpointSaver](./classes/checkpoint.BaseCheckpointSaver.html)
    * [BaseStore](./classes/checkpoint.BaseStore.html)
    * [InMemoryStore](./classes/checkpoint.InMemoryStore.html)
    * [InvalidNamespaceError](./classes/checkpoint.InvalidNamespaceError.html)
    * [MemorySaver](./classes/checkpoint.MemorySaver.html)
    * [MemoryStore](./classes/checkpoint.MemoryStore.html)
    * [ChannelProtocol](./interfaces/checkpoint.ChannelProtocol.html)
    * [Checkpoint](./interfaces/checkpoint.Checkpoint.html)
    * [CheckpointMetadata](./interfaces/checkpoint.CheckpointMetadata.html)
    * [CheckpointTuple](./interfaces/checkpoint.CheckpointTuple.html)
    * [GetOperation](./interfaces/checkpoint.GetOperation.html)
    * [IndexConfig](./interfaces/checkpoint.IndexConfig.html)
    * [Item](./interfaces/checkpoint.Item.html)
    * [ListNamespacesOperation](./interfaces/checkpoint.ListNamespacesOperation.html)
    * [MatchCondition](./interfaces/checkpoint.MatchCondition.html)
    * [PutOperation](./interfaces/checkpoint.PutOperation.html)
    * [ReadonlyCheckpoint](./interfaces/checkpoint.ReadonlyCheckpoint.html)
    * [SearchItem](./interfaces/checkpoint.SearchItem.html)
    * [SearchOperation](./interfaces/checkpoint.SearchOperation.html)
    * [SendProtocol](./interfaces/checkpoint.SendProtocol.html)
    * [SerializerProtocol](./interfaces/checkpoint.SerializerProtocol.html)
    * [All](./types/checkpoint.All.html)
    * [ChannelVersions](./types/checkpoint.ChannelVersions.html)
    * [CheckpointListOptions](./types/checkpoint.CheckpointListOptions.html)
    * [CheckpointPendingWrite](./types/checkpoint.CheckpointPendingWrite.html)
    * [NameSpacePath](./types/checkpoint.NameSpacePath.html)
    * [NamespaceMatchType](./types/checkpoint.NamespaceMatchType.html)
    * [Operation](./types/checkpoint.Operation.html)
    * [OperationResults](./types/checkpoint.OperationResults.html)
    * [PendingWrite](./types/checkpoint.PendingWrite.html)
    * [PendingWriteValue](./types/checkpoint.PendingWriteValue.html)
    * [ERROR](./variables/checkpoint.ERROR.html)
    * [INTERRUPT](./variables/checkpoint.INTERRUPT.html)
    * [RESUME](./variables/checkpoint.RESUME.html)
    * [SCHEDULED](./variables/checkpoint.SCHEDULED.html)
    * [TASKS](./variables/checkpoint.TASKS.html)
    * [WRITES_IDX_MAP](./variables/checkpoint.WRITES_IDX_MAP.html)
    * [compareChannelVersions](./functions/checkpoint.compareChannelVersions.html)
    * [deepCopy](./functions/checkpoint.deepCopy.html)
    * [getCheckpointId](./functions/checkpoint.getCheckpointId.html)
    * [getTextAtPath](./functions/checkpoint.getTextAtPath.html)
    * [maxChannelVersion](./functions/checkpoint.maxChannelVersion.html)
    * [tokenizePath](./functions/checkpoint.tokenizePath.html)
    * [uuid5](./functions/checkpoint.uuid5.html)
    * [uuid6](./functions/checkpoint.uuid6.html)

  * [checkpoint-mongodb](./modules/checkpoint_mongodb.html)

    * [MongoDBSaver](./classes/checkpoint_mongodb.MongoDBSaver.html)
    * [MongoDBSaverParams](./types/checkpoint_mongodb.MongoDBSaverParams.html)

  * [checkpoint-postgres](./modules/checkpoint_postgres.html)

    * [PostgresSaver](./classes/checkpoint_postgres.PostgresSaver.html)

  * [checkpoint-sqlite](./modules/checkpoint_sqlite.html)

    * [SqliteSaver](./classes/checkpoint_sqlite.SqliteSaver.html)

  * [checkpoint-validation](./modules/checkpoint_validation.html)

    * [CheckpointSaverTestInitializer](./interfaces/checkpoint_validation.CheckpointSaverTestInitializer.html)
    * [getTupleTests](./functions/checkpoint_validation.getTupleTests.html)
    * [listTests](./functions/checkpoint_validation.listTests.html)
    * [putTests](./functions/checkpoint_validation.putTests.html)
    * [putWritesTests](./functions/checkpoint_validation.putWritesTests.html)
    * [specTest](./functions/checkpoint_validation.specTest.html)
    * [validate](./functions/checkpoint_validation.validate.html)

  * [langgraph](./modules/langgraph.html)

    * [AsyncBatchedStore](./modules/langgraph.html#AsyncBatchedStore)
    * [BaseCheckpointSaver](./modules/langgraph.html#BaseCheckpointSaver)
    * [BaseStore](./modules/langgraph.html#BaseStore)
    * [Checkpoint](./modules/langgraph.html#Checkpoint)
    * [CheckpointMetadata](./modules/langgraph.html#CheckpointMetadata)
    * [CheckpointTuple](./modules/langgraph.html#CheckpointTuple)
    * [GetOperation](./modules/langgraph.html#GetOperation)
    * [InMemoryStore](./modules/langgraph.html#InMemoryStore)
    * [Item](./modules/langgraph.html#Item)
    * [ListNamespacesOperation](./modules/langgraph.html#ListNamespacesOperation)
    * [MatchCondition](./modules/langgraph.html#MatchCondition)
    * [MemorySaver](./modules/langgraph.html#MemorySaver)
    * [NameSpacePath](./modules/langgraph.html#NameSpacePath)
    * [NamespaceMatchType](./modules/langgraph.html#NamespaceMatchType)
    * [Operation](./modules/langgraph.html#Operation)
    * [OperationResults](./modules/langgraph.html#OperationResults)
    * [PutOperation](./modules/langgraph.html#PutOperation)
    * [SearchOperation](./modules/langgraph.html#SearchOperation)
    * [addMessages](./modules/langgraph.html#addMessages)
    * [Annotation](./modules/langgraph.Annotation.html)

      * [Root](./functions/langgraph.Annotation.Root.html)

    * [AnnotationRoot](./classes/langgraph.AnnotationRoot.html)
    * [AnyValue](./classes/langgraph.AnyValue.html)
    * [BaseChannel](./classes/langgraph.BaseChannel.html)
    * [BaseLangGraphError](./classes/langgraph.BaseLangGraphError.html)
    * [BinaryOperatorAggregate](./classes/langgraph.BinaryOperatorAggregate.html)
    * [Command](./classes/langgraph.Command.html)
    * [CompiledGraph](./classes/langgraph.CompiledGraph.html)
    * [CompiledStateGraph](./classes/langgraph.CompiledStateGraph.html)
    * [DynamicBarrierValue](./classes/langgraph.DynamicBarrierValue.html)
    * [EmptyChannelError](./classes/langgraph.EmptyChannelError.html)
    * [EmptyInputError](./classes/langgraph.EmptyInputError.html)
    * [EphemeralValue](./classes/langgraph.EphemeralValue.html)
    * [Graph](./classes/langgraph.Graph.html)
    * [GraphBubbleUp](./classes/langgraph.GraphBubbleUp.html)
    * [GraphInterrupt](./classes/langgraph.GraphInterrupt.html)
    * [GraphRecursionError](./classes/langgraph.GraphRecursionError.html)
    * [GraphValueError](./classes/langgraph.GraphValueError.html)
    * [InvalidUpdateError](./classes/langgraph.InvalidUpdateError.html)
    * [IsLastStepManager](./classes/langgraph.IsLastStepManager.html)
    * [LastValue](./classes/langgraph.LastValue.html)
    * [ManagedValue](./classes/langgraph.ManagedValue.html)
    * [ManagedValueMapping](./classes/langgraph.ManagedValueMapping.html)
    * [MultipleSubgraphsError](./classes/langgraph.MultipleSubgraphsError.html)
    * [NamedBarrierValue](./classes/langgraph.NamedBarrierValue.html)
    * [NodeInterrupt](./classes/langgraph.NodeInterrupt.html)
    * [NoopManagedValue](./classes/langgraph.NoopManagedValue.html)
    * [ParentCommand](./classes/langgraph.ParentCommand.html)
    * [Pregel](./classes/langgraph.Pregel.html)
    * [PregelNode](./classes/langgraph.PregelNode.html)
    * [RemoteException](./classes/langgraph.RemoteException.html)
    * [Send](./classes/langgraph.Send.html)
    * [SharedValue](./classes/langgraph.SharedValue.html)
    * [StateGraph](./classes/langgraph.StateGraph.html)
    * [Topic](./classes/langgraph.Topic.html)
    * [UnreachableNodeError](./classes/langgraph.UnreachableNodeError.html)
    * [WritableManagedValue](./classes/langgraph.WritableManagedValue.html)
    * [ConfiguredManagedValue](./interfaces/langgraph.ConfiguredManagedValue.html)
    * [LangGraphRunnableConfig](./interfaces/langgraph.LangGraphRunnableConfig.html)
    * [ManagedValueParams](./interfaces/langgraph.ManagedValueParams.html)
    * [PregelOptions](./interfaces/langgraph.PregelOptions.html)
    * [SharedValueParams](./interfaces/langgraph.SharedValueParams.html)
    * [StateDefinition](./interfaces/langgraph.StateDefinition.html)
    * [StateGraphArgs](./interfaces/langgraph.StateGraphArgs.html)
    * [StateSnapshot](./interfaces/langgraph.StateSnapshot.html)
    * [WaitForNames](./interfaces/langgraph.WaitForNames.html)
    * [BaseLangGraphErrorFields](./types/langgraph.BaseLangGraphErrorFields.html)
    * [BinaryOperator](./types/langgraph.BinaryOperator.html)
    * [CommandParams](./types/langgraph.CommandParams.html)
    * [EntrypointOptions](./types/langgraph.EntrypointOptions.html)
    * [Interrupt](./types/langgraph.Interrupt.html)
    * [ManagedValueSpec](./types/langgraph.ManagedValueSpec.html)
    * [Messages](./types/langgraph.Messages.html)
    * [NodeType](./types/langgraph.NodeType.html)
    * [PregelParams](./types/langgraph.PregelParams.html)
    * [RetryPolicy](./types/langgraph.RetryPolicy.html)
    * [SingleReducer](./types/langgraph.SingleReducer.html)
    * [StateType](./types/langgraph.StateType.html)
    * [StreamMode](./types/langgraph.StreamMode.html)
    * [TaskOptions](./types/langgraph.TaskOptions.html)
    * [UpdateType](./types/langgraph.UpdateType.html)
    * [ChannelKeyPlaceholder](./variables/langgraph.ChannelKeyPlaceholder.html)
    * [END](./variables/langgraph.END.html)
    * [MessagesAnnotation](./variables/langgraph.MessagesAnnotation.html)
    * [START](./variables/langgraph.START.html)
    * [entrypoint](./functions/langgraph.entrypoint.html)
    * [getPreviousState](./functions/langgraph.getPreviousState.html)
    * [getStore](./functions/langgraph.getStore.html)
    * [getSubgraphsSeenSet](./functions/langgraph.getSubgraphsSeenSet.html)
    * [getWriter](./functions/langgraph.getWriter.html)
    * [interrupt](./functions/langgraph.interrupt-1.html)
    * [isCommand](./functions/langgraph.isCommand.html)
    * [isConfiguredManagedValue](./functions/langgraph.isConfiguredManagedValue.html)
    * [isGraphBubbleUp](./functions/langgraph.isGraphBubbleUp.html)
    * [isGraphInterrupt](./functions/langgraph.isGraphInterrupt.html)
    * [isManagedValue](./functions/langgraph.isManagedValue.html)
    * [isParentCommand](./functions/langgraph.isParentCommand.html)
    * [messagesStateReducer](./functions/langgraph.messagesStateReducer.html)
    * [task](./functions/langgraph.task.html)
    * [prebuilt](./modules/langgraph_prebuilt.html)

      * [ToolExecutor](./classes/langgraph_prebuilt.ToolExecutor.html)
      * [ToolNode](./classes/langgraph_prebuilt.ToolNode.html)
      * [ActionRequest](./interfaces/langgraph_prebuilt.ActionRequest.html)
      * [AgentState](./interfaces/langgraph_prebuilt.AgentState.html)
      * [HumanInterrupt](./interfaces/langgraph_prebuilt.HumanInterrupt.html)
      * [HumanInterruptConfig](./interfaces/langgraph_prebuilt.HumanInterruptConfig.html)
      * [ToolExecutorArgs](./interfaces/langgraph_prebuilt.ToolExecutorArgs.html)
      * [ToolInvocationInterface](./interfaces/langgraph_prebuilt.ToolInvocationInterface.html)
      * [CreateReactAgentParams](./types/langgraph_prebuilt.CreateReactAgentParams.html)
      * [FunctionCallingExecutorState](./types/langgraph_prebuilt.FunctionCallingExecutorState.html)
      * [HumanResponse](./types/langgraph_prebuilt.HumanResponse.html)
      * [ToolNodeOptions](./types/langgraph_prebuilt.ToolNodeOptions.html)
      * [createFunctionCallingExecutor](./functions/langgraph_prebuilt.createFunctionCallingExecutor.html)
      * [createReactAgent](./functions/langgraph_prebuilt.createReactAgent.html)
      * [toolsCondition](./functions/langgraph_prebuilt.toolsCondition.html)

    * [pregel](./modules/langgraph_pregel.html)

      * [Pregel](./modules/langgraph_pregel.html#Pregel)
      * [PregelOptions](./modules/langgraph_pregel.html#PregelOptions)
      * [Channel](./classes/langgraph_pregel.Channel.html)
      * [PregelInputType](./types/langgraph_pregel.PregelInputType.html)
      * [PregelOutputType](./types/langgraph_pregel.PregelOutputType.html)

    * [remote](./modules/langgraph_remote.html)

      * [RemoteGraph](./classes/langgraph_remote.RemoteGraph.html)
      * [RemoteGraphParams](./types/langgraph_remote.RemoteGraphParams.html)

    * [web](./modules/langgraph_web.html)

      * [Annotation](./modules/langgraph_web.html#Annotation)
      * [AnnotationRoot](./modules/langgraph_web.html#AnnotationRoot)
      * [AnyValue](./modules/langgraph_web.html#AnyValue)
      * [AsyncBatchedStore](./modules/langgraph_web.html#AsyncBatchedStore)
      * [BaseChannel](./modules/langgraph_web.html#BaseChannel)
      * [BaseCheckpointSaver](./modules/langgraph_web.html#BaseCheckpointSaver)
      * [BaseLangGraphError](./modules/langgraph_web.html#BaseLangGraphError)
      * [BaseLangGraphErrorFields](./modules/langgraph_web.html#BaseLangGraphErrorFields)
      * [BaseStore](./modules/langgraph_web.html#BaseStore)
      * [BinaryOperator](./modules/langgraph_web.html#BinaryOperator)
      * [BinaryOperatorAggregate](./modules/langgraph_web.html#BinaryOperatorAggregate)
      * [ChannelKeyPlaceholder](./modules/langgraph_web.html#ChannelKeyPlaceholder)
      * [Checkpoint](./modules/langgraph_web.html#Checkpoint)
      * [CheckpointMetadata](./modules/langgraph_web.html#CheckpointMetadata)
      * [CheckpointTuple](./modules/langgraph_web.html#CheckpointTuple)
      * [Command](./modules/langgraph_web.html#Command)
      * [CommandParams](./modules/langgraph_web.html#CommandParams)
      * [CompiledGraph](./modules/langgraph_web.html#CompiledGraph)
      * [CompiledStateGraph](./modules/langgraph_web.html#CompiledStateGraph)
      * [ConfiguredManagedValue](./modules/langgraph_web.html#ConfiguredManagedValue)
      * [DynamicBarrierValue](./modules/langgraph_web.html#DynamicBarrierValue)
      * [END](./modules/langgraph_web.html#END)
      * [EmptyChannelError](./modules/langgraph_web.html#EmptyChannelError)
      * [EmptyInputError](./modules/langgraph_web.html#EmptyInputError)
      * [EntrypointOptions](./modules/langgraph_web.html#EntrypointOptions)
      * [EphemeralValue](./modules/langgraph_web.html#EphemeralValue)
      * [GetOperation](./modules/langgraph_web.html#GetOperation)
      * [Graph](./modules/langgraph_web.html#Graph)
      * [GraphBubbleUp](./modules/langgraph_web.html#GraphBubbleUp)
      * [GraphInterrupt](./modules/langgraph_web.html#GraphInterrupt)
      * [GraphRecursionError](./modules/langgraph_web.html#GraphRecursionError)
      * [GraphValueError](./modules/langgraph_web.html#GraphValueError)
      * [InMemoryStore](./modules/langgraph_web.html#InMemoryStore)
      * [Interrupt](./modules/langgraph_web.html#Interrupt)
      * [InvalidUpdateError](./modules/langgraph_web.html#InvalidUpdateError)
      * [IsLastStepManager](./modules/langgraph_web.html#IsLastStepManager)
      * [Item](./modules/langgraph_web.html#Item)
      * [LangGraphRunnableConfig](./modules/langgraph_web.html#LangGraphRunnableConfig)
      * [LastValue](./modules/langgraph_web.html#LastValue)
      * [ListNamespacesOperation](./modules/langgraph_web.html#ListNamespacesOperation)
      * [ManagedValue](./modules/langgraph_web.html#ManagedValue)
      * [ManagedValueMapping](./modules/langgraph_web.html#ManagedValueMapping)
      * [ManagedValueParams](./modules/langgraph_web.html#ManagedValueParams)
      * [ManagedValueSpec](./modules/langgraph_web.html#ManagedValueSpec)
      * [MatchCondition](./modules/langgraph_web.html#MatchCondition)
      * [MemorySaver](./modules/langgraph_web.html#MemorySaver)
      * [Messages](./modules/langgraph_web.html#Messages)
      * [MessagesAnnotation](./modules/langgraph_web.html#MessagesAnnotation)
      * [MultipleSubgraphsError](./modules/langgraph_web.html#MultipleSubgraphsError)
      * [NameSpacePath](./modules/langgraph_web.html#NameSpacePath)
      * [NamedBarrierValue](./modules/langgraph_web.html#NamedBarrierValue)
      * [NamespaceMatchType](./modules/langgraph_web.html#NamespaceMatchType)
      * [NodeInterrupt](./modules/langgraph_web.html#NodeInterrupt)
      * [NodeType](./modules/langgraph_web.html#NodeType)
      * [NoopManagedValue](./modules/langgraph_web.html#NoopManagedValue)
      * [Operation](./modules/langgraph_web.html#Operation)
      * [OperationResults](./modules/langgraph_web.html#OperationResults)
      * [ParentCommand](./modules/langgraph_web.html#ParentCommand)
      * [Pregel](./modules/langgraph_web.html#Pregel)
      * [PregelNode](./modules/langgraph_web.html#PregelNode)
      * [PregelOptions](./modules/langgraph_web.html#PregelOptions)
      * [PregelParams](./modules/langgraph_web.html#PregelParams)
      * [PutOperation](./modules/langgraph_web.html#PutOperation)
      * [RemoteException](./modules/langgraph_web.html#RemoteException)
      * [RetryPolicy](./modules/langgraph_web.html#RetryPolicy)
      * [START](./modules/langgraph_web.html#START)
      * [SearchOperation](./modules/langgraph_web.html#SearchOperation)
      * [Send](./modules/langgraph_web.html#Send)
      * [SharedValue](./modules/langgraph_web.html#SharedValue)
      * [SharedValueParams](./modules/langgraph_web.html#SharedValueParams)
      * [SingleReducer](./modules/langgraph_web.html#SingleReducer)
      * [StateDefinition](./modules/langgraph_web.html#StateDefinition)
      * [StateGraph](./modules/langgraph_web.html#StateGraph)
      * [StateGraphArgs](./modules/langgraph_web.html#StateGraphArgs)
      * [StateSnapshot](./modules/langgraph_web.html#StateSnapshot)
      * [StateType](./modules/langgraph_web.html#StateType)
      * [StreamMode](./modules/langgraph_web.html#StreamMode)
      * [TaskOptions](./modules/langgraph_web.html#TaskOptions)
      * [Topic](./modules/langgraph_web.html#Topic)
      * [UnreachableNodeError](./modules/langgraph_web.html#UnreachableNodeError)
      * [UpdateType](./modules/langgraph_web.html#UpdateType)
      * [WaitForNames](./modules/langgraph_web.html#WaitForNames)
      * [WritableManagedValue](./modules/langgraph_web.html#WritableManagedValue)
      * [addMessages](./modules/langgraph_web.html#addMessages)
      * [entrypoint](./modules/langgraph_web.html#entrypoint)
      * [getSubgraphsSeenSet](./modules/langgraph_web.html#getSubgraphsSeenSet)
      * [isCommand](./modules/langgraph_web.html#isCommand)
      * [isConfiguredManagedValue](./modules/langgraph_web.html#isConfiguredManagedValue)
      * [isGraphBubbleUp](./modules/langgraph_web.html#isGraphBubbleUp)
      * [isGraphInterrupt](./modules/langgraph_web.html#isGraphInterrupt)
      * [isManagedValue](./modules/langgraph_web.html#isManagedValue)
      * [isParentCommand](./modules/langgraph_web.html#isParentCommand)
      * [messagesStateReducer](./modules/langgraph_web.html#messagesStateReducer)
      * [task](./modules/langgraph_web.html#task)




Generated using [TypeDoc](https://typedoc.org/)
