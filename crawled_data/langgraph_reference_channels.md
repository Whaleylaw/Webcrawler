---
url: https://langchain-ai.github.io/langgraph/reference/channels/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/reference/channels/#channels)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Channels 

[ ](https://langchain-ai.github.io/langgraph/reference/channels/?q= "Share")

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
      * [ Prebuilt components  ](https://langchain-ai.github.io/langgraph/reference/prebuilt/)
      * Channels  [ Channels  ](https://langchain-ai.github.io/langgraph/reference/channels/) Table of contents 
        * [ BaseChannel  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.base.BaseChannel)
          * [ ValueType  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.base.BaseChannel.ValueType)
          * [ UpdateType  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.base.BaseChannel.UpdateType)
          * [ checkpoint  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.base.BaseChannel.checkpoint)
          * [ from_checkpoint  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.base.BaseChannel.from_checkpoint)
          * [ update  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.base.BaseChannel.update)
          * [ get  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.base.BaseChannel.get)
          * [ consume  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.base.BaseChannel.consume)
        * [ Topic  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.Topic)
          * [ ValueType  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.Topic.ValueType)
          * [ UpdateType  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.Topic.UpdateType)
          * [ consume  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.Topic.consume)
        * [ LastValue  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.LastValue)
          * [ ValueType  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.LastValue.ValueType)
          * [ UpdateType  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.LastValue.UpdateType)
          * [ checkpoint  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.LastValue.checkpoint)
          * [ consume  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.LastValue.consume)
        * [ EphemeralValue  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.EphemeralValue)
          * [ ValueType  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.EphemeralValue.ValueType)
          * [ UpdateType  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.EphemeralValue.UpdateType)
          * [ checkpoint  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.EphemeralValue.checkpoint)
          * [ consume  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.EphemeralValue.consume)
        * [ BinaryOperatorAggregate  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.BinaryOperatorAggregate)
          * [ ValueType  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.BinaryOperatorAggregate.ValueType)
          * [ UpdateType  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.BinaryOperatorAggregate.UpdateType)
          * [ checkpoint  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.BinaryOperatorAggregate.checkpoint)
          * [ consume  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.BinaryOperatorAggregate.consume)
        * [ AnyValue  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.AnyValue)
          * [ ValueType  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.AnyValue.ValueType)
          * [ UpdateType  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.AnyValue.UpdateType)
          * [ checkpoint  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.AnyValue.checkpoint)
          * [ consume  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.AnyValue.consume)
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

  * [ BaseChannel  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.base.BaseChannel)
    * [ ValueType  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.base.BaseChannel.ValueType)
    * [ UpdateType  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.base.BaseChannel.UpdateType)
    * [ checkpoint  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.base.BaseChannel.checkpoint)
    * [ from_checkpoint  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.base.BaseChannel.from_checkpoint)
    * [ update  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.base.BaseChannel.update)
    * [ get  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.base.BaseChannel.get)
    * [ consume  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.base.BaseChannel.consume)
  * [ Topic  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.Topic)
    * [ ValueType  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.Topic.ValueType)
    * [ UpdateType  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.Topic.UpdateType)
    * [ consume  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.Topic.consume)
  * [ LastValue  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.LastValue)
    * [ ValueType  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.LastValue.ValueType)
    * [ UpdateType  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.LastValue.UpdateType)
    * [ checkpoint  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.LastValue.checkpoint)
    * [ consume  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.LastValue.consume)
  * [ EphemeralValue  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.EphemeralValue)
    * [ ValueType  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.EphemeralValue.ValueType)
    * [ UpdateType  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.EphemeralValue.UpdateType)
    * [ checkpoint  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.EphemeralValue.checkpoint)
    * [ consume  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.EphemeralValue.consume)
  * [ BinaryOperatorAggregate  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.BinaryOperatorAggregate)
    * [ ValueType  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.BinaryOperatorAggregate.ValueType)
    * [ UpdateType  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.BinaryOperatorAggregate.UpdateType)
    * [ checkpoint  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.BinaryOperatorAggregate.checkpoint)
    * [ consume  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.BinaryOperatorAggregate.consume)
  * [ AnyValue  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.AnyValue)
    * [ ValueType  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.AnyValue.ValueType)
    * [ UpdateType  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.AnyValue.UpdateType)
    * [ checkpoint  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.AnyValue.checkpoint)
    * [ consume  ](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.AnyValue.consume)



  1. [ API reference  ](https://langchain-ai.github.io/langgraph/reference/graphs/)
  2. [ Library  ](https://langchain-ai.github.io/langgraph/reference/graphs/)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/reference/channels.md "Edit this page")

# Channels[¶](https://langchain-ai.github.io/langgraph/reference/channels/#channels "Permanent link")

##  `BaseChannel` [¶](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.base.BaseChannel "Permanent link")

Bases: `Generic[Value, Update, C]`, `ABC`

###  `ValueType: Any` `abstractmethod` `property` [¶](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.base.BaseChannel.ValueType "Permanent link")

The type of the value stored in the channel.

###  `UpdateType: Any` `abstractmethod` `property` [¶](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.base.BaseChannel.UpdateType "Permanent link")

The type of the update received by the channel.

###  `checkpoint() -> Optional[C]` [¶](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.base.BaseChannel.checkpoint "Permanent link")

Return a serializable representation of the channel's current state. Raises EmptyChannelError if the channel is empty (never updated yet), or doesn't support checkpoints.

###  `from_checkpoint(checkpoint: Optional[C]) -> Self` `abstractmethod` [¶](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.base.BaseChannel.from_checkpoint "Permanent link")

Return a new identical channel, optionally initialized from a checkpoint. If the checkpoint contains complex data structures, they should be copied.

###  `update(values: Sequence[Update]) -> bool` `abstractmethod` [¶](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.base.BaseChannel.update "Permanent link")

Update the channel's value with the given sequence of updates. The order of the updates in the sequence is arbitrary. This method is called by Pregel for all channels at the end of each step. If there are no updates, it is called with an empty sequence. Raises InvalidUpdateError if the sequence of updates is invalid. Returns True if the channel was updated, False otherwise.

###  `get() -> Value` `abstractmethod` [¶](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.base.BaseChannel.get "Permanent link")

Return the current value of the channel.

Raises EmptyChannelError if the channel is empty (never updated yet).

###  `consume() -> bool` [¶](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.base.BaseChannel.consume "Permanent link")

Mark the current value of the channel as consumed. By default, no-op. This is called by Pregel before the start of the next step, for all channels that triggered a node. If the channel was updated, return True.

##  `Topic` [¶](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.Topic "Permanent link")

Bases: `Generic[Value]`, `BaseChannel[Sequence[Value], Union[Value, list[Value]], tuple[set[Value], list[Value]]]`

A configurable PubSub Topic.

Parameters:

  * **`typ`**(`Type[Value]`) – 

The type of the value stored in the channel.

  * **`accumulate`**(`bool` , default: `False` ) – 

Whether to accumulate values across steps. If False, the channel will be emptied after each step.




###  `ValueType: Any` `property` [¶](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.Topic.ValueType "Permanent link")

The type of the value stored in the channel.

###  `UpdateType: Any` `property` [¶](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.Topic.UpdateType "Permanent link")

The type of the update received by the channel.

###  `consume() -> bool` [¶](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.Topic.consume "Permanent link")

Mark the current value of the channel as consumed. By default, no-op. This is called by Pregel before the start of the next step, for all channels that triggered a node. If the channel was updated, return True.

##  `LastValue` [¶](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.LastValue "Permanent link")

Bases: `Generic[Value]`, `BaseChannel[Value, Value, Value]`

Stores the last value received, can receive at most one value per step.

###  `ValueType: Type[Value]` `property` [¶](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.LastValue.ValueType "Permanent link")

The type of the value stored in the channel.

###  `UpdateType: Type[Value]` `property` [¶](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.LastValue.UpdateType "Permanent link")

The type of the update received by the channel.

###  `checkpoint() -> Optional[C]` [¶](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.LastValue.checkpoint "Permanent link")

Return a serializable representation of the channel's current state. Raises EmptyChannelError if the channel is empty (never updated yet), or doesn't support checkpoints.

###  `consume() -> bool` [¶](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.LastValue.consume "Permanent link")

Mark the current value of the channel as consumed. By default, no-op. This is called by Pregel before the start of the next step, for all channels that triggered a node. If the channel was updated, return True.

##  `EphemeralValue` [¶](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.EphemeralValue "Permanent link")

Bases: `Generic[Value]`, `BaseChannel[Value, Value, Value]`

Stores the value received in the step immediately preceding, clears after.

###  `ValueType: Type[Value]` `property` [¶](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.EphemeralValue.ValueType "Permanent link")

The type of the value stored in the channel.

###  `UpdateType: Type[Value]` `property` [¶](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.EphemeralValue.UpdateType "Permanent link")

The type of the update received by the channel.

###  `checkpoint() -> Optional[C]` [¶](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.EphemeralValue.checkpoint "Permanent link")

Return a serializable representation of the channel's current state. Raises EmptyChannelError if the channel is empty (never updated yet), or doesn't support checkpoints.

###  `consume() -> bool` [¶](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.EphemeralValue.consume "Permanent link")

Mark the current value of the channel as consumed. By default, no-op. This is called by Pregel before the start of the next step, for all channels that triggered a node. If the channel was updated, return True.

##  `BinaryOperatorAggregate` [¶](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.BinaryOperatorAggregate "Permanent link")

Bases: `Generic[Value]`, `BaseChannel[Value, Value, Value]`

Stores the result of applying a binary operator to the current value and each new value.

```
[](https://langchain-ai.github.io/langgraph/reference/channels/#__codelineno-0-1)importoperator
[](https://langchain-ai.github.io/langgraph/reference/channels/#__codelineno-0-2)
[](https://langchain-ai.github.io/langgraph/reference/channels/#__codelineno-0-3)total = Channels.BinaryOperatorAggregate(int, operator.add)

```


###  `ValueType: Type[Value]` `property` [¶](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.BinaryOperatorAggregate.ValueType "Permanent link")

The type of the value stored in the channel.

###  `UpdateType: Type[Value]` `property` [¶](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.BinaryOperatorAggregate.UpdateType "Permanent link")

The type of the update received by the channel.

###  `checkpoint() -> Optional[C]` [¶](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.BinaryOperatorAggregate.checkpoint "Permanent link")

Return a serializable representation of the channel's current state. Raises EmptyChannelError if the channel is empty (never updated yet), or doesn't support checkpoints.

###  `consume() -> bool` [¶](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.BinaryOperatorAggregate.consume "Permanent link")

Mark the current value of the channel as consumed. By default, no-op. This is called by Pregel before the start of the next step, for all channels that triggered a node. If the channel was updated, return True.

##  `AnyValue` [¶](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.AnyValue "Permanent link")

Bases: `Generic[Value]`, `BaseChannel[Value, Value, Value]`

Stores the last value received, assumes that if multiple values are received, they are all equal.

###  `ValueType: Type[Value]` `property` [¶](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.AnyValue.ValueType "Permanent link")

The type of the value stored in the channel.

###  `UpdateType: Type[Value]` `property` [¶](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.AnyValue.UpdateType "Permanent link")

The type of the update received by the channel.

###  `checkpoint() -> Optional[C]` [¶](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.AnyValue.checkpoint "Permanent link")

Return a serializable representation of the channel's current state. Raises EmptyChannelError if the channel is empty (never updated yet), or doesn't support checkpoints.

###  `consume() -> bool` [¶](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.AnyValue.consume "Permanent link")

Mark the current value of the channel as consumed. By default, no-op. This is called by Pregel before the start of the next step, for all channels that triggered a node. If the channel was updated, return True.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Prebuilt components  ](https://langchain-ai.github.io/langgraph/reference/prebuilt/) [ Next  Errors  ](https://langchain-ai.github.io/langgraph/reference/errors/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/reference/channels/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
