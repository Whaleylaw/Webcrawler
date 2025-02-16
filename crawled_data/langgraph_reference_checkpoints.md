---
url: https://langchain-ai.github.io/langgraph/reference/checkpoints/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#checkpointers)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Checkpointing 

[ ](https://langchain-ai.github.io/langgraph/reference/checkpoints/?q= "Share")

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
      * Checkpointing  [ Checkpointing  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/) Table of contents 
        * [ CheckpointMetadata  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.CheckpointMetadata)
          * [ source  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.CheckpointMetadata.source)
          * [ step  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.CheckpointMetadata.step)
          * [ writes  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.CheckpointMetadata.writes)
          * [ parents  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.CheckpointMetadata.parents)
        * [ Checkpoint  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.Checkpoint)
          * [ v  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.Checkpoint.v)
          * [ id  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.Checkpoint.id)
          * [ ts  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.Checkpoint.ts)
          * [ channel_values  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.Checkpoint.channel_values)
          * [ channel_versions  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.Checkpoint.channel_versions)
          * [ versions_seen  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.Checkpoint.versions_seen)
          * [ pending_sends  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.Checkpoint.pending_sends)
        * [ BaseCheckpointSaver  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver)
          * [ config_specs  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver.config_specs)
          * [ get  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver.get)
          * [ get_tuple  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver.get_tuple)
          * [ list  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver.list)
          * [ put  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver.put)
          * [ put_writes  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver.put_writes)
          * [ aget  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver.aget)
          * [ aget_tuple  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver.aget_tuple)
          * [ alist  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver.alist)
          * [ aput  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver.aput)
          * [ aput_writes  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver.aput_writes)
          * [ get_next_version  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver.get_next_version)
        * [ create_checkpoint  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.create_checkpoint)
        * [ SerializerProtocol  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.serde.base.SerializerProtocol)
        * [ JsonPlusSerializer  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.serde.jsonplus.JsonPlusSerializer)
        * [ InMemorySaver  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.InMemorySaver)
          * [ config_specs  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.InMemorySaver.config_specs)
          * [ get  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.InMemorySaver.get)
          * [ aget  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.InMemorySaver.aget)
          * [ get_tuple  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.InMemorySaver.get_tuple)
          * [ list  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.InMemorySaver.list)
          * [ put  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.InMemorySaver.put)
          * [ put_writes  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.InMemorySaver.put_writes)
          * [ aget_tuple  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.InMemorySaver.aget_tuple)
          * [ alist  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.InMemorySaver.alist)
          * [ aput  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.InMemorySaver.aput)
          * [ aput_writes  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.InMemorySaver.aput_writes)
        * [ PersistentDict  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.PersistentDict)
          * [ sync  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.PersistentDict.sync)
        * [ SqliteSaver  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.SqliteSaver)
          * [ config_specs  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.SqliteSaver.config_specs)
          * [ get  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.SqliteSaver.get)
          * [ aget  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.SqliteSaver.aget)
          * [ aput_writes  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.SqliteSaver.aput_writes)
          * [ from_conn_string  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.SqliteSaver.from_conn_string)
          * [ setup  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.SqliteSaver.setup)
          * [ cursor  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.SqliteSaver.cursor)
          * [ get_tuple  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.SqliteSaver.get_tuple)
          * [ list  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.SqliteSaver.list)
          * [ put  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.SqliteSaver.put)
          * [ put_writes  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.SqliteSaver.put_writes)
          * [ aget_tuple  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.SqliteSaver.aget_tuple)
          * [ alist  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.SqliteSaver.alist)
          * [ aput  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.SqliteSaver.aput)
          * [ get_next_version  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.SqliteSaver.get_next_version)
        * [ AsyncSqliteSaver  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.aio.AsyncSqliteSaver)
          * [ config_specs  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.aio.AsyncSqliteSaver.config_specs)
          * [ get  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.aio.AsyncSqliteSaver.get)
          * [ aget  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.aio.AsyncSqliteSaver.aget)
          * [ from_conn_string  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.aio.AsyncSqliteSaver.from_conn_string)
          * [ get_tuple  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.aio.AsyncSqliteSaver.get_tuple)
          * [ list  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.aio.AsyncSqliteSaver.list)
          * [ put  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.aio.AsyncSqliteSaver.put)
          * [ setup  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.aio.AsyncSqliteSaver.setup)
          * [ aget_tuple  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.aio.AsyncSqliteSaver.aget_tuple)
          * [ alist  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.aio.AsyncSqliteSaver.alist)
          * [ aput  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.aio.AsyncSqliteSaver.aput)
          * [ aput_writes  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.aio.AsyncSqliteSaver.aput_writes)
          * [ get_next_version  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.aio.AsyncSqliteSaver.get_next_version)
        * [ BasePostgresSaver  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.BasePostgresSaver)
          * [ config_specs  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.BasePostgresSaver.config_specs)
          * [ get  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.BasePostgresSaver.get)
          * [ get_tuple  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.BasePostgresSaver.get_tuple)
          * [ list  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.BasePostgresSaver.list)
          * [ put  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.BasePostgresSaver.put)
          * [ put_writes  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.BasePostgresSaver.put_writes)
          * [ aget  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.BasePostgresSaver.aget)
          * [ aget_tuple  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.BasePostgresSaver.aget_tuple)
          * [ alist  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.BasePostgresSaver.alist)
          * [ aput  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.BasePostgresSaver.aput)
          * [ aput_writes  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.BasePostgresSaver.aput_writes)
        * [ ShallowPostgresSaver  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.ShallowPostgresSaver)
          * [ config_specs  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.ShallowPostgresSaver.config_specs)
          * [ get  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.ShallowPostgresSaver.get)
          * [ aget  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.ShallowPostgresSaver.aget)
          * [ aget_tuple  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.ShallowPostgresSaver.aget_tuple)
          * [ alist  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.ShallowPostgresSaver.alist)
          * [ aput  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.ShallowPostgresSaver.aput)
          * [ aput_writes  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.ShallowPostgresSaver.aput_writes)
          * [ from_conn_string  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.ShallowPostgresSaver.from_conn_string)
          * [ setup  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.ShallowPostgresSaver.setup)
          * [ list  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.ShallowPostgresSaver.list)
          * [ get_tuple  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.ShallowPostgresSaver.get_tuple)
          * [ put  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.ShallowPostgresSaver.put)
          * [ put_writes  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.ShallowPostgresSaver.put_writes)
        * [ PostgresSaver  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.PostgresSaver)
          * [ config_specs  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.PostgresSaver.config_specs)
          * [ get  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.PostgresSaver.get)
          * [ aget  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.PostgresSaver.aget)
          * [ aget_tuple  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.PostgresSaver.aget_tuple)
          * [ alist  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.PostgresSaver.alist)
          * [ aput  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.PostgresSaver.aput)
          * [ aput_writes  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.PostgresSaver.aput_writes)
          * [ from_conn_string  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.PostgresSaver.from_conn_string)
          * [ setup  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.PostgresSaver.setup)
          * [ list  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.PostgresSaver.list)
          * [ get_tuple  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.PostgresSaver.get_tuple)
          * [ put  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.PostgresSaver.put)
          * [ put_writes  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.PostgresSaver.put_writes)
        * [ AsyncShallowPostgresSaver  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncShallowPostgresSaver)
          * [ config_specs  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncShallowPostgresSaver.config_specs)
          * [ get  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncShallowPostgresSaver.get)
          * [ aget  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncShallowPostgresSaver.aget)
          * [ from_conn_string  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncShallowPostgresSaver.from_conn_string)
          * [ setup  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncShallowPostgresSaver.setup)
          * [ alist  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncShallowPostgresSaver.alist)
          * [ aget_tuple  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncShallowPostgresSaver.aget_tuple)
          * [ aput  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncShallowPostgresSaver.aput)
          * [ aput_writes  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncShallowPostgresSaver.aput_writes)
          * [ list  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncShallowPostgresSaver.list)
          * [ get_tuple  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncShallowPostgresSaver.get_tuple)
          * [ put  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncShallowPostgresSaver.put)
          * [ put_writes  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncShallowPostgresSaver.put_writes)
        * [ AsyncPostgresSaver  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncPostgresSaver)
          * [ config_specs  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncPostgresSaver.config_specs)
          * [ get  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncPostgresSaver.get)
          * [ aget  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncPostgresSaver.aget)
          * [ from_conn_string  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncPostgresSaver.from_conn_string)
          * [ setup  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncPostgresSaver.setup)
          * [ alist  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncPostgresSaver.alist)
          * [ aget_tuple  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncPostgresSaver.aget_tuple)
          * [ aput  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncPostgresSaver.aput)
          * [ aput_writes  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncPostgresSaver.aput_writes)
          * [ list  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncPostgresSaver.list)
          * [ get_tuple  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncPostgresSaver.get_tuple)
          * [ put  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncPostgresSaver.put)
          * [ put_writes  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncPostgresSaver.put_writes)
      * [ Storage  ](https://langchain-ai.github.io/langgraph/reference/store/)
      * [ Prebuilt components  ](https://langchain-ai.github.io/langgraph/reference/prebuilt/)
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

  * [ CheckpointMetadata  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.CheckpointMetadata)
    * [ source  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.CheckpointMetadata.source)
    * [ step  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.CheckpointMetadata.step)
    * [ writes  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.CheckpointMetadata.writes)
    * [ parents  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.CheckpointMetadata.parents)
  * [ Checkpoint  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.Checkpoint)
    * [ v  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.Checkpoint.v)
    * [ id  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.Checkpoint.id)
    * [ ts  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.Checkpoint.ts)
    * [ channel_values  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.Checkpoint.channel_values)
    * [ channel_versions  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.Checkpoint.channel_versions)
    * [ versions_seen  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.Checkpoint.versions_seen)
    * [ pending_sends  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.Checkpoint.pending_sends)
  * [ BaseCheckpointSaver  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver)
    * [ config_specs  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver.config_specs)
    * [ get  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver.get)
    * [ get_tuple  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver.get_tuple)
    * [ list  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver.list)
    * [ put  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver.put)
    * [ put_writes  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver.put_writes)
    * [ aget  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver.aget)
    * [ aget_tuple  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver.aget_tuple)
    * [ alist  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver.alist)
    * [ aput  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver.aput)
    * [ aput_writes  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver.aput_writes)
    * [ get_next_version  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver.get_next_version)
  * [ create_checkpoint  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.create_checkpoint)
  * [ SerializerProtocol  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.serde.base.SerializerProtocol)
  * [ JsonPlusSerializer  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.serde.jsonplus.JsonPlusSerializer)
  * [ InMemorySaver  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.InMemorySaver)
    * [ config_specs  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.InMemorySaver.config_specs)
    * [ get  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.InMemorySaver.get)
    * [ aget  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.InMemorySaver.aget)
    * [ get_tuple  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.InMemorySaver.get_tuple)
    * [ list  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.InMemorySaver.list)
    * [ put  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.InMemorySaver.put)
    * [ put_writes  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.InMemorySaver.put_writes)
    * [ aget_tuple  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.InMemorySaver.aget_tuple)
    * [ alist  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.InMemorySaver.alist)
    * [ aput  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.InMemorySaver.aput)
    * [ aput_writes  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.InMemorySaver.aput_writes)
  * [ PersistentDict  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.PersistentDict)
    * [ sync  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.PersistentDict.sync)
  * [ SqliteSaver  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.SqliteSaver)
    * [ config_specs  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.SqliteSaver.config_specs)
    * [ get  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.SqliteSaver.get)
    * [ aget  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.SqliteSaver.aget)
    * [ aput_writes  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.SqliteSaver.aput_writes)
    * [ from_conn_string  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.SqliteSaver.from_conn_string)
    * [ setup  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.SqliteSaver.setup)
    * [ cursor  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.SqliteSaver.cursor)
    * [ get_tuple  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.SqliteSaver.get_tuple)
    * [ list  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.SqliteSaver.list)
    * [ put  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.SqliteSaver.put)
    * [ put_writes  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.SqliteSaver.put_writes)
    * [ aget_tuple  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.SqliteSaver.aget_tuple)
    * [ alist  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.SqliteSaver.alist)
    * [ aput  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.SqliteSaver.aput)
    * [ get_next_version  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.SqliteSaver.get_next_version)
  * [ AsyncSqliteSaver  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.aio.AsyncSqliteSaver)
    * [ config_specs  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.aio.AsyncSqliteSaver.config_specs)
    * [ get  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.aio.AsyncSqliteSaver.get)
    * [ aget  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.aio.AsyncSqliteSaver.aget)
    * [ from_conn_string  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.aio.AsyncSqliteSaver.from_conn_string)
    * [ get_tuple  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.aio.AsyncSqliteSaver.get_tuple)
    * [ list  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.aio.AsyncSqliteSaver.list)
    * [ put  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.aio.AsyncSqliteSaver.put)
    * [ setup  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.aio.AsyncSqliteSaver.setup)
    * [ aget_tuple  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.aio.AsyncSqliteSaver.aget_tuple)
    * [ alist  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.aio.AsyncSqliteSaver.alist)
    * [ aput  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.aio.AsyncSqliteSaver.aput)
    * [ aput_writes  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.aio.AsyncSqliteSaver.aput_writes)
    * [ get_next_version  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.aio.AsyncSqliteSaver.get_next_version)
  * [ BasePostgresSaver  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.BasePostgresSaver)
    * [ config_specs  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.BasePostgresSaver.config_specs)
    * [ get  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.BasePostgresSaver.get)
    * [ get_tuple  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.BasePostgresSaver.get_tuple)
    * [ list  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.BasePostgresSaver.list)
    * [ put  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.BasePostgresSaver.put)
    * [ put_writes  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.BasePostgresSaver.put_writes)
    * [ aget  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.BasePostgresSaver.aget)
    * [ aget_tuple  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.BasePostgresSaver.aget_tuple)
    * [ alist  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.BasePostgresSaver.alist)
    * [ aput  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.BasePostgresSaver.aput)
    * [ aput_writes  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.BasePostgresSaver.aput_writes)
  * [ ShallowPostgresSaver  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.ShallowPostgresSaver)
    * [ config_specs  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.ShallowPostgresSaver.config_specs)
    * [ get  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.ShallowPostgresSaver.get)
    * [ aget  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.ShallowPostgresSaver.aget)
    * [ aget_tuple  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.ShallowPostgresSaver.aget_tuple)
    * [ alist  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.ShallowPostgresSaver.alist)
    * [ aput  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.ShallowPostgresSaver.aput)
    * [ aput_writes  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.ShallowPostgresSaver.aput_writes)
    * [ from_conn_string  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.ShallowPostgresSaver.from_conn_string)
    * [ setup  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.ShallowPostgresSaver.setup)
    * [ list  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.ShallowPostgresSaver.list)
    * [ get_tuple  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.ShallowPostgresSaver.get_tuple)
    * [ put  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.ShallowPostgresSaver.put)
    * [ put_writes  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.ShallowPostgresSaver.put_writes)
  * [ PostgresSaver  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.PostgresSaver)
    * [ config_specs  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.PostgresSaver.config_specs)
    * [ get  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.PostgresSaver.get)
    * [ aget  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.PostgresSaver.aget)
    * [ aget_tuple  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.PostgresSaver.aget_tuple)
    * [ alist  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.PostgresSaver.alist)
    * [ aput  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.PostgresSaver.aput)
    * [ aput_writes  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.PostgresSaver.aput_writes)
    * [ from_conn_string  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.PostgresSaver.from_conn_string)
    * [ setup  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.PostgresSaver.setup)
    * [ list  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.PostgresSaver.list)
    * [ get_tuple  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.PostgresSaver.get_tuple)
    * [ put  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.PostgresSaver.put)
    * [ put_writes  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.PostgresSaver.put_writes)
  * [ AsyncShallowPostgresSaver  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncShallowPostgresSaver)
    * [ config_specs  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncShallowPostgresSaver.config_specs)
    * [ get  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncShallowPostgresSaver.get)
    * [ aget  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncShallowPostgresSaver.aget)
    * [ from_conn_string  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncShallowPostgresSaver.from_conn_string)
    * [ setup  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncShallowPostgresSaver.setup)
    * [ alist  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncShallowPostgresSaver.alist)
    * [ aget_tuple  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncShallowPostgresSaver.aget_tuple)
    * [ aput  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncShallowPostgresSaver.aput)
    * [ aput_writes  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncShallowPostgresSaver.aput_writes)
    * [ list  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncShallowPostgresSaver.list)
    * [ get_tuple  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncShallowPostgresSaver.get_tuple)
    * [ put  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncShallowPostgresSaver.put)
    * [ put_writes  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncShallowPostgresSaver.put_writes)
  * [ AsyncPostgresSaver  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncPostgresSaver)
    * [ config_specs  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncPostgresSaver.config_specs)
    * [ get  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncPostgresSaver.get)
    * [ aget  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncPostgresSaver.aget)
    * [ from_conn_string  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncPostgresSaver.from_conn_string)
    * [ setup  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncPostgresSaver.setup)
    * [ alist  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncPostgresSaver.alist)
    * [ aget_tuple  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncPostgresSaver.aget_tuple)
    * [ aput  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncPostgresSaver.aput)
    * [ aput_writes  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncPostgresSaver.aput_writes)
    * [ list  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncPostgresSaver.list)
    * [ get_tuple  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncPostgresSaver.get_tuple)
    * [ put  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncPostgresSaver.put)
    * [ put_writes  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncPostgresSaver.put_writes)



  1. [ API reference  ](https://langchain-ai.github.io/langgraph/reference/graphs/)
  2. [ Library  ](https://langchain-ai.github.io/langgraph/reference/graphs/)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/reference/checkpoints.md "Edit this page")

# Checkpointers[¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#checkpointers "Permanent link")

##  `CheckpointMetadata` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.CheckpointMetadata "Permanent link")

Bases: `TypedDict`

Metadata associated with a checkpoint.

###  `source: Literal['input', 'loop', 'update', 'fork']` `instance-attribute` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.CheckpointMetadata.source "Permanent link")

The source of the checkpoint.

  * "input": The checkpoint was created from an input to invoke/stream/batch.
  * "loop": The checkpoint was created from inside the pregel loop.
  * "update": The checkpoint was created from a manual state update.
  * "fork": The checkpoint was created as a copy of another checkpoint.



###  `step: int` `instance-attribute` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.CheckpointMetadata.step "Permanent link")

The step number of the checkpoint.

-1 for the first "input" checkpoint. 0 for the first "loop" checkpoint. ... for the nth checkpoint afterwards.

###  `writes: dict[str, Any]` `instance-attribute` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.CheckpointMetadata.writes "Permanent link")

The writes that were made between the previous checkpoint and this one.

Mapping from node name to writes emitted by that node.

###  `parents: dict[str, str]` `instance-attribute` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.CheckpointMetadata.parents "Permanent link")

The IDs of the parent checkpoints.

Mapping from checkpoint namespace to checkpoint ID.

##  `Checkpoint` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.Checkpoint "Permanent link")

Bases: `TypedDict`

State snapshot at a given point in time.

###  `v: int` `instance-attribute` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.Checkpoint.v "Permanent link")

The version of the checkpoint format. Currently 1.

###  `id: str` `instance-attribute` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.Checkpoint.id "Permanent link")

The ID of the checkpoint. This is both unique and monotonically increasing, so can be used for sorting checkpoints from first to last.

###  `ts: str` `instance-attribute` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.Checkpoint.ts "Permanent link")

The timestamp of the checkpoint in ISO 8601 format.

###  `channel_values: dict[str, Any]` `instance-attribute` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.Checkpoint.channel_values "Permanent link")

The values of the channels at the time of the checkpoint. Mapping from channel name to deserialized channel snapshot value.

###  `channel_versions: ChannelVersions` `instance-attribute` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.Checkpoint.channel_versions "Permanent link")

The versions of the channels at the time of the checkpoint. The keys are channel names and the values are monotonically increasing version strings for each channel.

###  `versions_seen: dict[str, ChannelVersions]` `instance-attribute` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.Checkpoint.versions_seen "Permanent link")

Map from node ID to map from channel name to version seen. This keeps track of the versions of the channels that each node has seen. Used to determine which nodes to execute next.

###  `pending_sends: List[SendProtocol]` `instance-attribute` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.Checkpoint.pending_sends "Permanent link")

List of inputs pushed to nodes but not yet processed. Cleared by the next checkpoint.

##  `BaseCheckpointSaver` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver "Permanent link")

Bases: `Generic[V]`

Base class for creating a graph checkpointer.

Checkpointers allow LangGraph agents to persist their state within and across multiple interactions.

Attributes:

  * **`serde`**(`SerializerProtocol`) – 

Serializer for encoding/decoding checkpoints.


Note

When creating a custom checkpoint saver, consider implementing async versions to avoid blocking the main thread.

###  `config_specs: list[ConfigurableFieldSpec]` `property` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver.config_specs "Permanent link")

Define the configuration options for the checkpoint saver.

Returns:

  * `list[ConfigurableFieldSpec]` – 

list[ConfigurableFieldSpec]: List of configuration field specs.




###  `get(config: RunnableConfig) -> Optional[Checkpoint]` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver.get "Permanent link")

Fetch a checkpoint using the given configuration.

Parameters:

  * **`config`**(`RunnableConfig`) – 

Configuration specifying which checkpoint to retrieve.




Returns:

  * `Optional[Checkpoint]` – 

Optional[Checkpoint]: The requested checkpoint, or None if not found.




###  `get_tuple(config: RunnableConfig) -> Optional[CheckpointTuple]` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver.get_tuple "Permanent link")

Fetch a checkpoint tuple using the given configuration.

Parameters:

  * **`config`**(`RunnableConfig`) – 

Configuration specifying which checkpoint to retrieve.




Returns:

  * `Optional[CheckpointTuple]` – 

Optional[CheckpointTuple]: The requested checkpoint tuple, or None if not found.




Raises:

  * `NotImplementedError` – 

Implement this method in your custom checkpoint saver.




###  `list(config: Optional[RunnableConfig], *, filter: Optional[Dict[str, Any]] = None, before: Optional[RunnableConfig] = None, limit: Optional[int] = None) -> Iterator[CheckpointTuple]` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver.list "Permanent link")

List checkpoints that match the given criteria.

Parameters:

  * **`config`**(`Optional[RunnableConfig]`) – 

Base configuration for filtering checkpoints.

  * **`filter`**(`Optional[Dict[str, Any]]` , default: `None` ) – 

Additional filtering criteria.

  * **`before`**(`Optional[RunnableConfig]` , default: `None` ) – 

List checkpoints created before this configuration.

  * **`limit`**(`Optional[int]` , default: `None` ) – 

Maximum number of checkpoints to return.




Returns:

  * `Iterator[CheckpointTuple]` – 

Iterator[CheckpointTuple]: Iterator of matching checkpoint tuples.




Raises:

  * `NotImplementedError` – 

Implement this method in your custom checkpoint saver.




###  `put(config: RunnableConfig, checkpoint: Checkpoint, metadata: CheckpointMetadata, new_versions: ChannelVersions) -> RunnableConfig` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver.put "Permanent link")

Store a checkpoint with its configuration and metadata.

Parameters:

  * **`config`**(`RunnableConfig`) – 

Configuration for the checkpoint.

  * **`checkpoint`**(`Checkpoint`) – 

The checkpoint to store.

  * **`metadata`**(`CheckpointMetadata`) – 

Additional metadata for the checkpoint.

  * **`new_versions`**(`ChannelVersions`) – 

New channel versions as of this write.




Returns:

  * **`RunnableConfig`**(`RunnableConfig` ) – 

Updated configuration after storing the checkpoint.




Raises:

  * `NotImplementedError` – 

Implement this method in your custom checkpoint saver.




###  `put_writes(config: RunnableConfig, writes: Sequence[Tuple[str, Any]], task_id: str, task_path: str = '') -> None` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver.put_writes "Permanent link")

Store intermediate writes linked to a checkpoint.

Parameters:

  * **`config`**(`RunnableConfig`) – 

Configuration of the related checkpoint.

  * **`writes`**(`List[Tuple[str, Any]]`) – 

List of writes to store.

  * **`task_id`**(`str`) – 

Identifier for the task creating the writes.

  * **`task_path`**(`str` , default: `''` ) – 

Path of the task creating the writes.




Raises:

  * `NotImplementedError` – 

Implement this method in your custom checkpoint saver.




###  `aget(config: RunnableConfig) -> Optional[Checkpoint]` `async` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver.aget "Permanent link")

Asynchronously fetch a checkpoint using the given configuration.

Parameters:

  * **`config`**(`RunnableConfig`) – 

Configuration specifying which checkpoint to retrieve.




Returns:

  * `Optional[Checkpoint]` – 

Optional[Checkpoint]: The requested checkpoint, or None if not found.




###  `aget_tuple(config: RunnableConfig) -> Optional[CheckpointTuple]` `async` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver.aget_tuple "Permanent link")

Asynchronously fetch a checkpoint tuple using the given configuration.

Parameters:

  * **`config`**(`RunnableConfig`) – 

Configuration specifying which checkpoint to retrieve.




Returns:

  * `Optional[CheckpointTuple]` – 

Optional[CheckpointTuple]: The requested checkpoint tuple, or None if not found.




Raises:

  * `NotImplementedError` – 

Implement this method in your custom checkpoint saver.




###  `alist(config: Optional[RunnableConfig], *, filter: Optional[Dict[str, Any]] = None, before: Optional[RunnableConfig] = None, limit: Optional[int] = None) -> AsyncIterator[CheckpointTuple]` `async` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver.alist "Permanent link")

Asynchronously list checkpoints that match the given criteria.

Parameters:

  * **`config`**(`Optional[RunnableConfig]`) – 

Base configuration for filtering checkpoints.

  * **`filter`**(`Optional[Dict[str, Any]]` , default: `None` ) – 

Additional filtering criteria for metadata.

  * **`before`**(`Optional[RunnableConfig]` , default: `None` ) – 

List checkpoints created before this configuration.

  * **`limit`**(`Optional[int]` , default: `None` ) – 

Maximum number of checkpoints to return.




Returns:

  * `AsyncIterator[CheckpointTuple]` – 

AsyncIterator[CheckpointTuple]: Async iterator of matching checkpoint tuples.




Raises:

  * `NotImplementedError` – 

Implement this method in your custom checkpoint saver.




###  `aput(config: RunnableConfig, checkpoint: Checkpoint, metadata: CheckpointMetadata, new_versions: ChannelVersions) -> RunnableConfig` `async` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver.aput "Permanent link")

Asynchronously store a checkpoint with its configuration and metadata.

Parameters:

  * **`config`**(`RunnableConfig`) – 

Configuration for the checkpoint.

  * **`checkpoint`**(`Checkpoint`) – 

The checkpoint to store.

  * **`metadata`**(`CheckpointMetadata`) – 

Additional metadata for the checkpoint.

  * **`new_versions`**(`ChannelVersions`) – 

New channel versions as of this write.




Returns:

  * **`RunnableConfig`**(`RunnableConfig` ) – 

Updated configuration after storing the checkpoint.




Raises:

  * `NotImplementedError` – 

Implement this method in your custom checkpoint saver.




###  `aput_writes(config: RunnableConfig, writes: Sequence[Tuple[str, Any]], task_id: str, task_path: str = '') -> None` `async` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver.aput_writes "Permanent link")

Asynchronously store intermediate writes linked to a checkpoint.

Parameters:

  * **`config`**(`RunnableConfig`) – 

Configuration of the related checkpoint.

  * **`writes`**(`List[Tuple[str, Any]]`) – 

List of writes to store.

  * **`task_id`**(`str`) – 

Identifier for the task creating the writes.

  * **`task_path`**(`str` , default: `''` ) – 

Path of the task creating the writes.




Raises:

  * `NotImplementedError` – 

Implement this method in your custom checkpoint saver.




###  `get_next_version(current: Optional[V], channel: ChannelProtocol) -> V` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver.get_next_version "Permanent link")

Generate the next version ID for a channel.

Default is to use integer versions, incrementing by 1. If you override, you can use str/int/float versions, as long as they are monotonically increasing.

Parameters:

  * **`current`**(`Optional[V]`) – 

The current version identifier (int, float, or str).

  * **`channel`**(`BaseChannel`) – 

The channel being versioned.




Returns:

  * **`V`**(`V` ) – 

The next version identifier, which must be increasing.




##  `create_checkpoint(checkpoint: Checkpoint, channels: Optional[Mapping[str, ChannelProtocol]], step: int, *, id: Optional[str] = None) -> Checkpoint` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.create_checkpoint "Permanent link")

Create a checkpoint for the given channels.

##  `SerializerProtocol` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.serde.base.SerializerProtocol "Permanent link")

Bases: `Protocol`

Protocol for serialization and deserialization of objects.

  * `dumps`: Serialize an object to bytes.
  * `dumps_typed`: Serialize an object to a tuple (type, bytes).
  * `loads`: Deserialize an object from bytes.
  * `loads_typed`: Deserialize an object from a tuple (type, bytes).



Valid implementations include the `pickle`, `json` and `orjson` modules.

##  `JsonPlusSerializer` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.serde.jsonplus.JsonPlusSerializer "Permanent link")

Bases: `SerializerProtocol`

##  `InMemorySaver` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.InMemorySaver "Permanent link")

Bases: `BaseCheckpointSaver[str]`, `AbstractContextManager`, `AbstractAsyncContextManager`

An in-memory checkpoint saver.

This checkpoint saver stores checkpoints in memory using a defaultdict.

Note

Only use `InMemorySaver` for debugging or testing purposes. For production use cases we recommend installing [langgraph-checkpoint-postgres](https://pypi.org/project/langgraph-checkpoint-postgres/) and using `PostgresSaver` / `AsyncPostgresSaver`.

Parameters:

  * **`serde`**(`Optional[SerializerProtocol]` , default: `None` ) – 

The serializer to use for serializing and deserializing checkpoints. Defaults to None.




Examples:

```
  import asyncio
  from langgraph.checkpoint.memory import InMemorySaver
  from langgraph.graph import StateGraph
  builder = StateGraph(int)
  builder.add_node("add_one", lambda x: x + 1)
  builder.set_entry_point("add_one")
  builder.set_finish_point("add_one")
  memory = InMemorySaver()
  graph = builder.compile(checkpointer=memory)
  coro = graph.ainvoke(1, {"configurable": {"thread_id": "thread-1"}})
  asyncio.run(coro) # Output: 2

```


###  `config_specs: list[ConfigurableFieldSpec]` `property` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.InMemorySaver.config_specs "Permanent link")

Define the configuration options for the checkpoint saver.

Returns:

  * `list[ConfigurableFieldSpec]` – 

list[ConfigurableFieldSpec]: List of configuration field specs.




###  `get(config: RunnableConfig) -> Optional[Checkpoint]` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.InMemorySaver.get "Permanent link")

Fetch a checkpoint using the given configuration.

Parameters:

  * **`config`**(`RunnableConfig`) – 

Configuration specifying which checkpoint to retrieve.




Returns:

  * `Optional[Checkpoint]` – 

Optional[Checkpoint]: The requested checkpoint, or None if not found.




###  `aget(config: RunnableConfig) -> Optional[Checkpoint]` `async` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.InMemorySaver.aget "Permanent link")

Asynchronously fetch a checkpoint using the given configuration.

Parameters:

  * **`config`**(`RunnableConfig`) – 

Configuration specifying which checkpoint to retrieve.




Returns:

  * `Optional[Checkpoint]` – 

Optional[Checkpoint]: The requested checkpoint, or None if not found.




###  `get_tuple(config: RunnableConfig) -> Optional[CheckpointTuple]` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.InMemorySaver.get_tuple "Permanent link")

Get a checkpoint tuple from the in-memory storage.

This method retrieves a checkpoint tuple from the in-memory storage based on the provided config. If the config contains a "checkpoint_id" key, the checkpoint with the matching thread ID and timestamp is retrieved. Otherwise, the latest checkpoint for the given thread ID is retrieved.

Parameters:

  * **`config`**(`RunnableConfig`) – 

The config to use for retrieving the checkpoint.




Returns:

  * `Optional[CheckpointTuple]` – 

Optional[CheckpointTuple]: The retrieved checkpoint tuple, or None if no matching checkpoint was found.




###  `list(config: Optional[RunnableConfig], *, filter: Optional[dict[str, Any]] = None, before: Optional[RunnableConfig] = None, limit: Optional[int] = None) -> Iterator[CheckpointTuple]` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.InMemorySaver.list "Permanent link")

List checkpoints from the in-memory storage.

This method retrieves a list of checkpoint tuples from the in-memory storage based on the provided criteria.

Parameters:

  * **`config`**(`Optional[RunnableConfig]`) – 

Base configuration for filtering checkpoints.

  * **`filter`**(`Optional[Dict[str, Any]]` , default: `None` ) – 

Additional filtering criteria for metadata.

  * **`before`**(`Optional[RunnableConfig]` , default: `None` ) – 

List checkpoints created before this configuration.

  * **`limit`**(`Optional[int]` , default: `None` ) – 

Maximum number of checkpoints to return.




Yields:

  * `CheckpointTuple` – 

Iterator[CheckpointTuple]: An iterator of matching checkpoint tuples.




###  `put(config: RunnableConfig, checkpoint: Checkpoint, metadata: CheckpointMetadata, new_versions: ChannelVersions) -> RunnableConfig` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.InMemorySaver.put "Permanent link")

Save a checkpoint to the in-memory storage.

This method saves a checkpoint to the in-memory storage. The checkpoint is associated with the provided config.

Parameters:

  * **`config`**(`RunnableConfig`) – 

The config to associate with the checkpoint.

  * **`checkpoint`**(`Checkpoint`) – 

The checkpoint to save.

  * **`metadata`**(`CheckpointMetadata`) – 

Additional metadata to save with the checkpoint.

  * **`new_versions`**(`dict`) – 

New versions as of this write




Returns:

  * **`RunnableConfig`**(`RunnableConfig` ) – 

The updated config containing the saved checkpoint's timestamp.




###  `put_writes(config: RunnableConfig, writes: Sequence[tuple[str, Any]], task_id: str, task_path: str = '') -> None` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.InMemorySaver.put_writes "Permanent link")

Save a list of writes to the in-memory storage.

This method saves a list of writes to the in-memory storage. The writes are associated with the provided config.

Parameters:

  * **`config`**(`RunnableConfig`) – 

The config to associate with the writes.

  * **`writes`**(`list[tuple[str, Any]]`) – 

The writes to save.

  * **`task_id`**(`str`) – 

Identifier for the task creating the writes.

  * **`task_path`**(`str` , default: `''` ) – 

Path of the task creating the writes.




Returns:

  * **`RunnableConfig`**(`None` ) – 

The updated config containing the saved writes' timestamp.




###  `aget_tuple(config: RunnableConfig) -> Optional[CheckpointTuple]` `async` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.InMemorySaver.aget_tuple "Permanent link")

Asynchronous version of get_tuple.

This method is an asynchronous wrapper around get_tuple that runs the synchronous method in a separate thread using asyncio.

Parameters:

  * **`config`**(`RunnableConfig`) – 

The config to use for retrieving the checkpoint.




Returns:

  * `Optional[CheckpointTuple]` – 

Optional[CheckpointTuple]: The retrieved checkpoint tuple, or None if no matching checkpoint was found.




###  `alist(config: Optional[RunnableConfig], *, filter: Optional[dict[str, Any]] = None, before: Optional[RunnableConfig] = None, limit: Optional[int] = None) -> AsyncIterator[CheckpointTuple]` `async` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.InMemorySaver.alist "Permanent link")

Asynchronous version of list.

This method is an asynchronous wrapper around list that runs the synchronous method in a separate thread using asyncio.

Parameters:

  * **`config`**(`RunnableConfig`) – 

The config to use for listing the checkpoints.




Yields:

  * `AsyncIterator[CheckpointTuple]` – 

AsyncIterator[CheckpointTuple]: An asynchronous iterator of checkpoint tuples.




###  `aput(config: RunnableConfig, checkpoint: Checkpoint, metadata: CheckpointMetadata, new_versions: ChannelVersions) -> RunnableConfig` `async` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.InMemorySaver.aput "Permanent link")

Asynchronous version of put.

Parameters:

  * **`config`**(`RunnableConfig`) – 

The config to associate with the checkpoint.

  * **`checkpoint`**(`Checkpoint`) – 

The checkpoint to save.

  * **`metadata`**(`CheckpointMetadata`) – 

Additional metadata to save with the checkpoint.

  * **`new_versions`**(`dict`) – 

New versions as of this write




Returns:

  * **`RunnableConfig`**(`RunnableConfig` ) – 

The updated config containing the saved checkpoint's timestamp.




###  `aput_writes(config: RunnableConfig, writes: Sequence[tuple[str, Any]], task_id: str, task_path: str = '') -> None` `async` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.InMemorySaver.aput_writes "Permanent link")

Asynchronous version of put_writes.

This method is an asynchronous wrapper around put_writes that runs the synchronous method in a separate thread using asyncio.

Parameters:

  * **`config`**(`RunnableConfig`) – 

The config to associate with the writes.

  * **`writes`**(`List[Tuple[str, Any]]`) – 

The writes to save, each as a (channel, value) pair.

  * **`task_id`**(`str`) – 

Identifier for the task creating the writes.

  * **`task_path`**(`str` , default: `''` ) – 

Path of the task creating the writes.




Returns:

  * `None` – 

None




##  `PersistentDict` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.PersistentDict "Permanent link")

Bases: `defaultdict`

Persistent dictionary with an API compatible with shelve and anydbm.

The dict is kept in memory, so the dictionary operations run as fast as a regular dictionary.

Write to disk is delayed until close or sync (similar to gdbm's fast mode).

Input file format is automatically discovered. Output file format is selectable between pickle, json, and csv. All three serialization formats are backed by fast C implementations.

Adapted from <https://code.activestate.com/recipes/576642-persistent-dict-with-multiple-standard-file-format/>

###  `sync() -> None` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.PersistentDict.sync "Permanent link")

Write dict to disk

##  `SqliteSaver` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.SqliteSaver "Permanent link")

Bases: `BaseCheckpointSaver[str]`

A checkpoint saver that stores checkpoints in a SQLite database.

Note

This class is meant for lightweight, synchronous use cases (demos and small projects) and does not scale to multiple threads. For a similar sqlite saver with `async` support, consider using [AsyncSqliteSaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.aio.AsyncSqliteSaver).

Parameters:

  * **`conn`**(`Connection`) – 

The SQLite database connection.

  * **`serde`**(`Optional[SerializerProtocol]` , default: `None` ) – 

The serializer to use for serializing and deserializing checkpoints. Defaults to JsonPlusSerializerCompat.




Examples:

```
>>> import sqlite3
>>> from langgraph.checkpoint.sqlite import SqliteSaver
>>> from langgraph.graph import StateGraph
>>>
>>> builder = StateGraph(int)
>>> builder.add_node("add_one", lambda x: x + 1)
>>> builder.set_entry_point("add_one")
>>> builder.set_finish_point("add_one")
>>> conn = sqlite3.connect("checkpoints.sqlite")
>>> memory = SqliteSaver(conn)
>>> graph = builder.compile(checkpointer=memory)
>>> config = {"configurable": {"thread_id": "1"}}
>>> graph.get_state(config)
>>> result = graph.invoke(3, config)
>>> graph.get_state(config)
StateSnapshot(values=4, next=(), config={'configurable': {'thread_id': '1', 'checkpoint_ns': '', 'checkpoint_id': '0c62ca34-ac19-445d-bbb0-5b4984975b2a'}}, parent_config=None)

```


###  `config_specs: list[ConfigurableFieldSpec]` `property` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.SqliteSaver.config_specs "Permanent link")

Define the configuration options for the checkpoint saver.

Returns:

  * `list[ConfigurableFieldSpec]` – 

list[ConfigurableFieldSpec]: List of configuration field specs.




###  `get(config: RunnableConfig) -> Optional[Checkpoint]` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.SqliteSaver.get "Permanent link")

Fetch a checkpoint using the given configuration.

Parameters:

  * **`config`**(`RunnableConfig`) – 

Configuration specifying which checkpoint to retrieve.




Returns:

  * `Optional[Checkpoint]` – 

Optional[Checkpoint]: The requested checkpoint, or None if not found.




###  `aget(config: RunnableConfig) -> Optional[Checkpoint]` `async` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.SqliteSaver.aget "Permanent link")

Asynchronously fetch a checkpoint using the given configuration.

Parameters:

  * **`config`**(`RunnableConfig`) – 

Configuration specifying which checkpoint to retrieve.




Returns:

  * `Optional[Checkpoint]` – 

Optional[Checkpoint]: The requested checkpoint, or None if not found.




###  `aput_writes(config: RunnableConfig, writes: Sequence[Tuple[str, Any]], task_id: str, task_path: str = '') -> None` `async` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.SqliteSaver.aput_writes "Permanent link")

Asynchronously store intermediate writes linked to a checkpoint.

Parameters:

  * **`config`**(`RunnableConfig`) – 

Configuration of the related checkpoint.

  * **`writes`**(`List[Tuple[str, Any]]`) – 

List of writes to store.

  * **`task_id`**(`str`) – 

Identifier for the task creating the writes.

  * **`task_path`**(`str` , default: `''` ) – 

Path of the task creating the writes.




Raises:

  * `NotImplementedError` – 

Implement this method in your custom checkpoint saver.




###  `from_conn_string(conn_string: str) -> Iterator[SqliteSaver]` `classmethod` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.SqliteSaver.from_conn_string "Permanent link")

Create a new SqliteSaver instance from a connection string.

Parameters:

  * **`conn_string`**(`str`) – 

The SQLite connection string.




Yields:

  * **`SqliteSaver`**(`SqliteSaver` ) – 

A new SqliteSaver instance.




Examples:

```
In memory:
  with SqliteSaver.from_conn_string(":memory:") as memory:
    ...
To disk:
  with SqliteSaver.from_conn_string("checkpoints.sqlite") as memory:
    ...

```


###  `setup() -> None` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.SqliteSaver.setup "Permanent link")

Set up the checkpoint database.

This method creates the necessary tables in the SQLite database if they don't already exist. It is called automatically when needed and should not be called directly by the user.

###  `cursor(transaction: bool = True) -> Iterator[sqlite3.Cursor]` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.SqliteSaver.cursor "Permanent link")

Get a cursor for the SQLite database.

This method returns a cursor for the SQLite database. It is used internally by the SqliteSaver and should not be called directly by the user.

Parameters:

  * **`transaction`**(`bool` , default: `True` ) – 

Whether to commit the transaction when the cursor is closed. Defaults to True.




Yields:

  * `Cursor` – 

sqlite3.Cursor: A cursor for the SQLite database.




###  `get_tuple(config: RunnableConfig) -> Optional[CheckpointTuple]` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.SqliteSaver.get_tuple "Permanent link")

Get a checkpoint tuple from the database.

This method retrieves a checkpoint tuple from the SQLite database based on the provided config. If the config contains a "checkpoint_id" key, the checkpoint with the matching thread ID and checkpoint ID is retrieved. Otherwise, the latest checkpoint for the given thread ID is retrieved.

Parameters:

  * **`config`**(`RunnableConfig`) – 

The config to use for retrieving the checkpoint.




Returns:

  * `Optional[CheckpointTuple]` – 

Optional[CheckpointTuple]: The retrieved checkpoint tuple, or None if no matching checkpoint was found.




Examples:

```
Basic:
>>> config = {"configurable": {"thread_id": "1"}}
>>> checkpoint_tuple = memory.get_tuple(config)
>>> print(checkpoint_tuple)
CheckpointTuple(...)
With checkpoint ID:
>>> config = {
...  "configurable": {
...    "thread_id": "1",
...    "checkpoint_ns": "",
...    "checkpoint_id": "1ef4f797-8335-6428-8001-8a1503f9b875",
...  }
... }
>>> checkpoint_tuple = memory.get_tuple(config)
>>> print(checkpoint_tuple)
CheckpointTuple(...)

```


###  `list(config: Optional[RunnableConfig], *, filter: Optional[Dict[str, Any]] = None, before: Optional[RunnableConfig] = None, limit: Optional[int] = None) -> Iterator[CheckpointTuple]` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.SqliteSaver.list "Permanent link")

List checkpoints from the database.

This method retrieves a list of checkpoint tuples from the SQLite database based on the provided config. The checkpoints are ordered by checkpoint ID in descending order (newest first).

Parameters:

  * **`config`**(`RunnableConfig`) – 

The config to use for listing the checkpoints.

  * **`filter`**(`Optional[Dict[str, Any]]` , default: `None` ) – 

Additional filtering criteria for metadata. Defaults to None.

  * **`before`**(`Optional[RunnableConfig]` , default: `None` ) – 

If provided, only checkpoints before the specified checkpoint ID are returned. Defaults to None.

  * **`limit`**(`Optional[int]` , default: `None` ) – 

The maximum number of checkpoints to return. Defaults to None.




Yields:

  * `CheckpointTuple` – 

Iterator[CheckpointTuple]: An iterator of checkpoint tuples.




Examples:

```
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-0-1)>>> fromlanggraph.checkpoint.sqliteimport SqliteSaver
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-0-2)>>> with SqliteSaver.from_conn_string(":memory:") as memory:
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-0-3)... # Run a graph, then list the checkpoints
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-0-4)>>>   config = {"configurable": {"thread_id": "1"}}
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-0-5)>>>   checkpoints = list(memory.list(config, limit=2))
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-0-6)>>> print(checkpoints)
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-0-7)[CheckpointTuple(...), CheckpointTuple(...)]

```


```
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-0-1)>>> config = {"configurable": {"thread_id": "1"}}
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-0-2)>>> before = {"configurable": {"checkpoint_id": "1ef4f797-8335-6428-8001-8a1503f9b875"}}
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-0-3)>>> with SqliteSaver.from_conn_string(":memory:") as memory:
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-0-4)... # Run a graph, then list the checkpoints
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-0-5)>>>   checkpoints = list(memory.list(config, before=before))
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-0-6)>>> print(checkpoints)
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-0-7)[CheckpointTuple(...), ...]

```


###  `put(config: RunnableConfig, checkpoint: Checkpoint, metadata: CheckpointMetadata, new_versions: ChannelVersions) -> RunnableConfig` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.SqliteSaver.put "Permanent link")

Save a checkpoint to the database.

This method saves a checkpoint to the SQLite database. The checkpoint is associated with the provided config and its parent config (if any).

Parameters:

  * **`config`**(`RunnableConfig`) – 

The config to associate with the checkpoint.

  * **`checkpoint`**(`Checkpoint`) – 

The checkpoint to save.

  * **`metadata`**(`CheckpointMetadata`) – 

Additional metadata to save with the checkpoint.

  * **`new_versions`**(`ChannelVersions`) – 

New channel versions as of this write.




Returns:

  * **`RunnableConfig`**(`RunnableConfig` ) – 

Updated configuration after storing the checkpoint.




Examples:

```
>>> from langgraph.checkpoint.sqlite import SqliteSaver
>>> with SqliteSaver.from_conn_string(":memory:") as memory:
>>>   config = {"configurable": {"thread_id": "1", "checkpoint_ns": ""}}
>>>   checkpoint = {"ts": "2024-05-04T06:32:42.235444+00:00", "id": "1ef4f797-8335-6428-8001-8a1503f9b875", "channel_values": {"key": "value"}}
>>>   saved_config = memory.put(config, checkpoint, {"source": "input", "step": 1, "writes": {"key": "value"}}, {})
>>> print(saved_config)
{'configurable': {'thread_id': '1', 'checkpoint_ns': '', 'checkpoint_id': '1ef4f797-8335-6428-8001-8a1503f9b875'}}

```


###  `put_writes(config: RunnableConfig, writes: Sequence[Tuple[str, Any]], task_id: str, task_path: str = '') -> None` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.SqliteSaver.put_writes "Permanent link")

Store intermediate writes linked to a checkpoint.

This method saves intermediate writes associated with a checkpoint to the SQLite database.

Parameters:

  * **`config`**(`RunnableConfig`) – 

Configuration of the related checkpoint.

  * **`writes`**(`Sequence[Tuple[str, Any]]`) – 

List of writes to store, each as (channel, value) pair.

  * **`task_id`**(`str`) – 

Identifier for the task creating the writes.

  * **`task_path`**(`str` , default: `''` ) – 

Path of the task creating the writes.




###  `aget_tuple(config: RunnableConfig) -> Optional[CheckpointTuple]` `async` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.SqliteSaver.aget_tuple "Permanent link")

Get a checkpoint tuple from the database asynchronously.

Note

This async method is not supported by the SqliteSaver class. Use get_tuple() instead, or consider using [AsyncSqliteSaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.aio.AsyncSqliteSaver).

###  `alist(config: Optional[RunnableConfig], *, filter: Optional[Dict[str, Any]] = None, before: Optional[RunnableConfig] = None, limit: Optional[int] = None) -> AsyncIterator[CheckpointTuple]` `async` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.SqliteSaver.alist "Permanent link")

List checkpoints from the database asynchronously.

Note

This async method is not supported by the SqliteSaver class. Use list() instead, or consider using [AsyncSqliteSaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.aio.AsyncSqliteSaver).

###  `aput(config: RunnableConfig, checkpoint: Checkpoint, metadata: CheckpointMetadata, new_versions: ChannelVersions) -> RunnableConfig` `async` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.SqliteSaver.aput "Permanent link")

Save a checkpoint to the database asynchronously.

Note

This async method is not supported by the SqliteSaver class. Use put() instead, or consider using [AsyncSqliteSaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.aio.AsyncSqliteSaver).

###  `get_next_version(current: Optional[str], channel: ChannelProtocol) -> str` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.SqliteSaver.get_next_version "Permanent link")

Generate the next version ID for a channel.

This method creates a new version identifier for a channel based on its current version.

Parameters:

  * **`current`**(`Optional[str]`) – 

The current version identifier of the channel.

  * **`channel`**(`BaseChannel`) – 

The channel being versioned.




Returns:

  * **`str`**(`str` ) – 

The next version identifier, which is guaranteed to be monotonically increasing.




##  `AsyncSqliteSaver` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.aio.AsyncSqliteSaver "Permanent link")

Bases: `BaseCheckpointSaver[str]`

An asynchronous checkpoint saver that stores checkpoints in a SQLite database.

This class provides an asynchronous interface for saving and retrieving checkpoints using a SQLite database. It's designed for use in asynchronous environments and offers better performance for I/O-bound operations compared to synchronous alternatives.

Attributes:

  * **`conn`**(`Connection`) – 

The asynchronous SQLite database connection.

  * **`serde`**(`SerializerProtocol`) – 

The serializer used for encoding/decoding checkpoints.


Tip

Requires the [aiosqlite](https://pypi.org/project/aiosqlite/) package. Install it with `pip install aiosqlite`.

Warning

While this class supports asynchronous checkpointing, it is not recommended for production workloads due to limitations in SQLite's write performance. For production use, consider a more robust database like PostgreSQL.

Tip

Remember to **close the database connection** after executing your code, otherwise, you may see the graph "hang" after execution (since the program will not exit until the connection is closed).

The easiest way is to use the `async with` statement as shown in the examples.

```
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-0-1)async with AsyncSqliteSaver.from_conn_string("checkpoints.sqlite") as saver:
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-0-2)  # Your code here
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-0-3)  graph = builder.compile(checkpointer=saver)
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-0-4)  config = {"configurable": {"thread_id": "thread-1"}}
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-0-5)  async for event in graph.astream_events(..., config, version="v1"):
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-0-6)    print(event)

```


Examples:

Usage within StateGraph:

```
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-0-1)>>> importasyncio
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-0-2)>>>
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-0-3)>>> fromlanggraph.checkpoint.sqlite.aioimport AsyncSqliteSaver
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-0-4)>>> fromlanggraph.graphimport StateGraph
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-0-5)>>>
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-0-6)>>> builder = StateGraph(int)
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-0-7)>>> builder.add_node("add_one", lambda x: x + 1)
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-0-8)>>> builder.set_entry_point("add_one")
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-0-9)>>> builder.set_finish_point("add_one")
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-0-10)>>> async with AsyncSqliteSaver.from_conn_string("checkpoints.db") as memory:
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-0-11)>>>   graph = builder.compile(checkpointer=memory)
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-0-12)>>>   coro = graph.ainvoke(1, {"configurable": {"thread_id": "thread-1"}})
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-0-13)>>>   print(asyncio.run(coro))
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-0-14)Output: 2

```


Raw usage: 

```
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-1-1)>>> importasyncio
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-1-2)>>> importaiosqlite
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-1-3)>>> fromlanggraph.checkpoint.sqlite.aioimport AsyncSqliteSaver
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-1-4)>>>
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-1-5)>>> async defmain():
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-1-6)>>>   async with aiosqlite.connect("checkpoints.db") as conn:
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-1-7)...     saver = AsyncSqliteSaver(conn)
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-1-8)...     config = {"configurable": {"thread_id": "1"}}
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-1-9)...     checkpoint = {"ts": "2023-05-03T10:00:00Z", "data": {"key": "value"}}
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-1-10)...     saved_config = await saver.aput(config, checkpoint, {}, {})
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-1-11)...     print(saved_config)
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-1-12)>>> asyncio.run(main())
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-1-13){"configurable": {"thread_id": "1", "checkpoint_id": "0c62ca34-ac19-445d-bbb0-5b4984975b2a"}}

```


###  `config_specs: list[ConfigurableFieldSpec]` `property` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.aio.AsyncSqliteSaver.config_specs "Permanent link")

Define the configuration options for the checkpoint saver.

Returns:

  * `list[ConfigurableFieldSpec]` – 

list[ConfigurableFieldSpec]: List of configuration field specs.




###  `get(config: RunnableConfig) -> Optional[Checkpoint]` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.aio.AsyncSqliteSaver.get "Permanent link")

Fetch a checkpoint using the given configuration.

Parameters:

  * **`config`**(`RunnableConfig`) – 

Configuration specifying which checkpoint to retrieve.




Returns:

  * `Optional[Checkpoint]` – 

Optional[Checkpoint]: The requested checkpoint, or None if not found.




###  `aget(config: RunnableConfig) -> Optional[Checkpoint]` `async` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.aio.AsyncSqliteSaver.aget "Permanent link")

Asynchronously fetch a checkpoint using the given configuration.

Parameters:

  * **`config`**(`RunnableConfig`) – 

Configuration specifying which checkpoint to retrieve.




Returns:

  * `Optional[Checkpoint]` – 

Optional[Checkpoint]: The requested checkpoint, or None if not found.




###  `from_conn_string(conn_string: str) -> AsyncIterator[AsyncSqliteSaver]` `async` `classmethod` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.aio.AsyncSqliteSaver.from_conn_string "Permanent link")

Create a new AsyncSqliteSaver instance from a connection string.

Parameters:

  * **`conn_string`**(`str`) – 

The SQLite connection string.




Yields:

  * **`AsyncSqliteSaver`**(`AsyncIterator[AsyncSqliteSaver]` ) – 

A new AsyncSqliteSaver instance.




###  `get_tuple(config: RunnableConfig) -> Optional[CheckpointTuple]` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.aio.AsyncSqliteSaver.get_tuple "Permanent link")

Get a checkpoint tuple from the database.

This method retrieves a checkpoint tuple from the SQLite database based on the provided config. If the config contains a "checkpoint_id" key, the checkpoint with the matching thread ID and checkpoint ID is retrieved. Otherwise, the latest checkpoint for the given thread ID is retrieved.

Parameters:

  * **`config`**(`RunnableConfig`) – 

The config to use for retrieving the checkpoint.




Returns:

  * `Optional[CheckpointTuple]` – 

Optional[CheckpointTuple]: The retrieved checkpoint tuple, or None if no matching checkpoint was found.




###  `list(config: Optional[RunnableConfig], *, filter: Optional[dict[str, Any]] = None, before: Optional[RunnableConfig] = None, limit: Optional[int] = None) -> Iterator[CheckpointTuple]` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.aio.AsyncSqliteSaver.list "Permanent link")

List checkpoints from the database asynchronously.

This method retrieves a list of checkpoint tuples from the SQLite database based on the provided config. The checkpoints are ordered by checkpoint ID in descending order (newest first).

Parameters:

  * **`config`**(`Optional[RunnableConfig]`) – 

Base configuration for filtering checkpoints.

  * **`filter`**(`Optional[Dict[str, Any]]` , default: `None` ) – 

Additional filtering criteria for metadata.

  * **`before`**(`Optional[RunnableConfig]` , default: `None` ) – 

If provided, only checkpoints before the specified checkpoint ID are returned. Defaults to None.

  * **`limit`**(`Optional[int]` , default: `None` ) – 

Maximum number of checkpoints to return.




Yields:

  * `CheckpointTuple` – 

Iterator[CheckpointTuple]: An iterator of matching checkpoint tuples.




###  `put(config: RunnableConfig, checkpoint: Checkpoint, metadata: CheckpointMetadata, new_versions: ChannelVersions) -> RunnableConfig` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.aio.AsyncSqliteSaver.put "Permanent link")

Save a checkpoint to the database.

This method saves a checkpoint to the SQLite database. The checkpoint is associated with the provided config and its parent config (if any).

Parameters:

  * **`config`**(`RunnableConfig`) – 

The config to associate with the checkpoint.

  * **`checkpoint`**(`Checkpoint`) – 

The checkpoint to save.

  * **`metadata`**(`CheckpointMetadata`) – 

Additional metadata to save with the checkpoint.

  * **`new_versions`**(`ChannelVersions`) – 

New channel versions as of this write.




Returns:

  * **`RunnableConfig`**(`RunnableConfig` ) – 

Updated configuration after storing the checkpoint.




###  `setup() -> None` `async` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.aio.AsyncSqliteSaver.setup "Permanent link")

Set up the checkpoint database asynchronously.

This method creates the necessary tables in the SQLite database if they don't already exist. It is called automatically when needed and should not be called directly by the user.

###  `aget_tuple(config: RunnableConfig) -> Optional[CheckpointTuple]` `async` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.aio.AsyncSqliteSaver.aget_tuple "Permanent link")

Get a checkpoint tuple from the database asynchronously.

This method retrieves a checkpoint tuple from the SQLite database based on the provided config. If the config contains a "checkpoint_id" key, the checkpoint with the matching thread ID and checkpoint ID is retrieved. Otherwise, the latest checkpoint for the given thread ID is retrieved.

Parameters:

  * **`config`**(`RunnableConfig`) – 

The config to use for retrieving the checkpoint.




Returns:

  * `Optional[CheckpointTuple]` – 

Optional[CheckpointTuple]: The retrieved checkpoint tuple, or None if no matching checkpoint was found.




###  `alist(config: Optional[RunnableConfig], *, filter: Optional[dict[str, Any]] = None, before: Optional[RunnableConfig] = None, limit: Optional[int] = None) -> AsyncIterator[CheckpointTuple]` `async` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.aio.AsyncSqliteSaver.alist "Permanent link")

List checkpoints from the database asynchronously.

This method retrieves a list of checkpoint tuples from the SQLite database based on the provided config. The checkpoints are ordered by checkpoint ID in descending order (newest first).

Parameters:

  * **`config`**(`Optional[RunnableConfig]`) – 

Base configuration for filtering checkpoints.

  * **`filter`**(`Optional[Dict[str, Any]]` , default: `None` ) – 

Additional filtering criteria for metadata.

  * **`before`**(`Optional[RunnableConfig]` , default: `None` ) – 

If provided, only checkpoints before the specified checkpoint ID are returned. Defaults to None.

  * **`limit`**(`Optional[int]` , default: `None` ) – 

Maximum number of checkpoints to return.




Yields:

  * `AsyncIterator[CheckpointTuple]` – 

AsyncIterator[CheckpointTuple]: An asynchronous iterator of matching checkpoint tuples.




###  `aput(config: RunnableConfig, checkpoint: Checkpoint, metadata: CheckpointMetadata, new_versions: ChannelVersions) -> RunnableConfig` `async` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.aio.AsyncSqliteSaver.aput "Permanent link")

Save a checkpoint to the database asynchronously.

This method saves a checkpoint to the SQLite database. The checkpoint is associated with the provided config and its parent config (if any).

Parameters:

  * **`config`**(`RunnableConfig`) – 

The config to associate with the checkpoint.

  * **`checkpoint`**(`Checkpoint`) – 

The checkpoint to save.

  * **`metadata`**(`CheckpointMetadata`) – 

Additional metadata to save with the checkpoint.

  * **`new_versions`**(`ChannelVersions`) – 

New channel versions as of this write.




Returns:

  * **`RunnableConfig`**(`RunnableConfig` ) – 

Updated configuration after storing the checkpoint.




###  `aput_writes(config: RunnableConfig, writes: Sequence[tuple[str, Any]], task_id: str, task_path: str = '') -> None` `async` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.aio.AsyncSqliteSaver.aput_writes "Permanent link")

Store intermediate writes linked to a checkpoint asynchronously.

This method saves intermediate writes associated with a checkpoint to the database.

Parameters:

  * **`config`**(`RunnableConfig`) – 

Configuration of the related checkpoint.

  * **`writes`**(`Sequence[Tuple[str, Any]]`) – 

List of writes to store, each as (channel, value) pair.

  * **`task_id`**(`str`) – 

Identifier for the task creating the writes.

  * **`task_path`**(`str` , default: `''` ) – 

Path of the task creating the writes.




###  `get_next_version(current: Optional[str], channel: ChannelProtocol) -> str` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.sqlite.aio.AsyncSqliteSaver.get_next_version "Permanent link")

Generate the next version ID for a channel.

This method creates a new version identifier for a channel based on its current version.

Parameters:

  * **`current`**(`Optional[str]`) – 

The current version identifier of the channel.

  * **`channel`**(`BaseChannel`) – 

The channel being versioned.




Returns:

  * **`str`**(`str` ) – 

The next version identifier, which is guaranteed to be monotonically increasing.




##  `BasePostgresSaver` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.BasePostgresSaver "Permanent link")

Bases: `BaseCheckpointSaver[str]`

###  `config_specs: list[ConfigurableFieldSpec]` `property` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.BasePostgresSaver.config_specs "Permanent link")

Define the configuration options for the checkpoint saver.

Returns:

  * `list[ConfigurableFieldSpec]` – 

list[ConfigurableFieldSpec]: List of configuration field specs.




###  `get(config: RunnableConfig) -> Optional[Checkpoint]` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.BasePostgresSaver.get "Permanent link")

Fetch a checkpoint using the given configuration.

Parameters:

  * **`config`**(`RunnableConfig`) – 

Configuration specifying which checkpoint to retrieve.




Returns:

  * `Optional[Checkpoint]` – 

Optional[Checkpoint]: The requested checkpoint, or None if not found.




###  `get_tuple(config: RunnableConfig) -> Optional[CheckpointTuple]` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.BasePostgresSaver.get_tuple "Permanent link")

Fetch a checkpoint tuple using the given configuration.

Parameters:

  * **`config`**(`RunnableConfig`) – 

Configuration specifying which checkpoint to retrieve.




Returns:

  * `Optional[CheckpointTuple]` – 

Optional[CheckpointTuple]: The requested checkpoint tuple, or None if not found.




Raises:

  * `NotImplementedError` – 

Implement this method in your custom checkpoint saver.




###  `list(config: Optional[RunnableConfig], *, filter: Optional[Dict[str, Any]] = None, before: Optional[RunnableConfig] = None, limit: Optional[int] = None) -> Iterator[CheckpointTuple]` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.BasePostgresSaver.list "Permanent link")

List checkpoints that match the given criteria.

Parameters:

  * **`config`**(`Optional[RunnableConfig]`) – 

Base configuration for filtering checkpoints.

  * **`filter`**(`Optional[Dict[str, Any]]` , default: `None` ) – 

Additional filtering criteria.

  * **`before`**(`Optional[RunnableConfig]` , default: `None` ) – 

List checkpoints created before this configuration.

  * **`limit`**(`Optional[int]` , default: `None` ) – 

Maximum number of checkpoints to return.




Returns:

  * `Iterator[CheckpointTuple]` – 

Iterator[CheckpointTuple]: Iterator of matching checkpoint tuples.




Raises:

  * `NotImplementedError` – 

Implement this method in your custom checkpoint saver.




###  `put(config: RunnableConfig, checkpoint: Checkpoint, metadata: CheckpointMetadata, new_versions: ChannelVersions) -> RunnableConfig` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.BasePostgresSaver.put "Permanent link")

Store a checkpoint with its configuration and metadata.

Parameters:

  * **`config`**(`RunnableConfig`) – 

Configuration for the checkpoint.

  * **`checkpoint`**(`Checkpoint`) – 

The checkpoint to store.

  * **`metadata`**(`CheckpointMetadata`) – 

Additional metadata for the checkpoint.

  * **`new_versions`**(`ChannelVersions`) – 

New channel versions as of this write.




Returns:

  * **`RunnableConfig`**(`RunnableConfig` ) – 

Updated configuration after storing the checkpoint.




Raises:

  * `NotImplementedError` – 

Implement this method in your custom checkpoint saver.




###  `put_writes(config: RunnableConfig, writes: Sequence[Tuple[str, Any]], task_id: str, task_path: str = '') -> None` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.BasePostgresSaver.put_writes "Permanent link")

Store intermediate writes linked to a checkpoint.

Parameters:

  * **`config`**(`RunnableConfig`) – 

Configuration of the related checkpoint.

  * **`writes`**(`List[Tuple[str, Any]]`) – 

List of writes to store.

  * **`task_id`**(`str`) – 

Identifier for the task creating the writes.

  * **`task_path`**(`str` , default: `''` ) – 

Path of the task creating the writes.




Raises:

  * `NotImplementedError` – 

Implement this method in your custom checkpoint saver.




###  `aget(config: RunnableConfig) -> Optional[Checkpoint]` `async` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.BasePostgresSaver.aget "Permanent link")

Asynchronously fetch a checkpoint using the given configuration.

Parameters:

  * **`config`**(`RunnableConfig`) – 

Configuration specifying which checkpoint to retrieve.




Returns:

  * `Optional[Checkpoint]` – 

Optional[Checkpoint]: The requested checkpoint, or None if not found.




###  `aget_tuple(config: RunnableConfig) -> Optional[CheckpointTuple]` `async` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.BasePostgresSaver.aget_tuple "Permanent link")

Asynchronously fetch a checkpoint tuple using the given configuration.

Parameters:

  * **`config`**(`RunnableConfig`) – 

Configuration specifying which checkpoint to retrieve.




Returns:

  * `Optional[CheckpointTuple]` – 

Optional[CheckpointTuple]: The requested checkpoint tuple, or None if not found.




Raises:

  * `NotImplementedError` – 

Implement this method in your custom checkpoint saver.




###  `alist(config: Optional[RunnableConfig], *, filter: Optional[Dict[str, Any]] = None, before: Optional[RunnableConfig] = None, limit: Optional[int] = None) -> AsyncIterator[CheckpointTuple]` `async` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.BasePostgresSaver.alist "Permanent link")

Asynchronously list checkpoints that match the given criteria.

Parameters:

  * **`config`**(`Optional[RunnableConfig]`) – 

Base configuration for filtering checkpoints.

  * **`filter`**(`Optional[Dict[str, Any]]` , default: `None` ) – 

Additional filtering criteria for metadata.

  * **`before`**(`Optional[RunnableConfig]` , default: `None` ) – 

List checkpoints created before this configuration.

  * **`limit`**(`Optional[int]` , default: `None` ) – 

Maximum number of checkpoints to return.




Returns:

  * `AsyncIterator[CheckpointTuple]` – 

AsyncIterator[CheckpointTuple]: Async iterator of matching checkpoint tuples.




Raises:

  * `NotImplementedError` – 

Implement this method in your custom checkpoint saver.




###  `aput(config: RunnableConfig, checkpoint: Checkpoint, metadata: CheckpointMetadata, new_versions: ChannelVersions) -> RunnableConfig` `async` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.BasePostgresSaver.aput "Permanent link")

Asynchronously store a checkpoint with its configuration and metadata.

Parameters:

  * **`config`**(`RunnableConfig`) – 

Configuration for the checkpoint.

  * **`checkpoint`**(`Checkpoint`) – 

The checkpoint to store.

  * **`metadata`**(`CheckpointMetadata`) – 

Additional metadata for the checkpoint.

  * **`new_versions`**(`ChannelVersions`) – 

New channel versions as of this write.




Returns:

  * **`RunnableConfig`**(`RunnableConfig` ) – 

Updated configuration after storing the checkpoint.




Raises:

  * `NotImplementedError` – 

Implement this method in your custom checkpoint saver.




###  `aput_writes(config: RunnableConfig, writes: Sequence[Tuple[str, Any]], task_id: str, task_path: str = '') -> None` `async` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.BasePostgresSaver.aput_writes "Permanent link")

Asynchronously store intermediate writes linked to a checkpoint.

Parameters:

  * **`config`**(`RunnableConfig`) – 

Configuration of the related checkpoint.

  * **`writes`**(`List[Tuple[str, Any]]`) – 

List of writes to store.

  * **`task_id`**(`str`) – 

Identifier for the task creating the writes.

  * **`task_path`**(`str` , default: `''` ) – 

Path of the task creating the writes.




Raises:

  * `NotImplementedError` – 

Implement this method in your custom checkpoint saver.




##  `ShallowPostgresSaver` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.ShallowPostgresSaver "Permanent link")

Bases: `BasePostgresSaver`

A checkpoint saver that uses Postgres to store checkpoints.

This checkpointer ONLY stores the most recent checkpoint and does NOT retain any history. It is meant to be a light-weight drop-in replacement for the PostgresSaver that supports most of the LangGraph persistence functionality with the exception of time travel.

###  `config_specs: list[ConfigurableFieldSpec]` `property` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.ShallowPostgresSaver.config_specs "Permanent link")

Define the configuration options for the checkpoint saver.

Returns:

  * `list[ConfigurableFieldSpec]` – 

list[ConfigurableFieldSpec]: List of configuration field specs.




###  `get(config: RunnableConfig) -> Optional[Checkpoint]` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.ShallowPostgresSaver.get "Permanent link")

Fetch a checkpoint using the given configuration.

Parameters:

  * **`config`**(`RunnableConfig`) – 

Configuration specifying which checkpoint to retrieve.




Returns:

  * `Optional[Checkpoint]` – 

Optional[Checkpoint]: The requested checkpoint, or None if not found.




###  `aget(config: RunnableConfig) -> Optional[Checkpoint]` `async` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.ShallowPostgresSaver.aget "Permanent link")

Asynchronously fetch a checkpoint using the given configuration.

Parameters:

  * **`config`**(`RunnableConfig`) – 

Configuration specifying which checkpoint to retrieve.




Returns:

  * `Optional[Checkpoint]` – 

Optional[Checkpoint]: The requested checkpoint, or None if not found.




###  `aget_tuple(config: RunnableConfig) -> Optional[CheckpointTuple]` `async` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.ShallowPostgresSaver.aget_tuple "Permanent link")

Asynchronously fetch a checkpoint tuple using the given configuration.

Parameters:

  * **`config`**(`RunnableConfig`) – 

Configuration specifying which checkpoint to retrieve.




Returns:

  * `Optional[CheckpointTuple]` – 

Optional[CheckpointTuple]: The requested checkpoint tuple, or None if not found.




Raises:

  * `NotImplementedError` – 

Implement this method in your custom checkpoint saver.




###  `alist(config: Optional[RunnableConfig], *, filter: Optional[Dict[str, Any]] = None, before: Optional[RunnableConfig] = None, limit: Optional[int] = None) -> AsyncIterator[CheckpointTuple]` `async` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.ShallowPostgresSaver.alist "Permanent link")

Asynchronously list checkpoints that match the given criteria.

Parameters:

  * **`config`**(`Optional[RunnableConfig]`) – 

Base configuration for filtering checkpoints.

  * **`filter`**(`Optional[Dict[str, Any]]` , default: `None` ) – 

Additional filtering criteria for metadata.

  * **`before`**(`Optional[RunnableConfig]` , default: `None` ) – 

List checkpoints created before this configuration.

  * **`limit`**(`Optional[int]` , default: `None` ) – 

Maximum number of checkpoints to return.




Returns:

  * `AsyncIterator[CheckpointTuple]` – 

AsyncIterator[CheckpointTuple]: Async iterator of matching checkpoint tuples.




Raises:

  * `NotImplementedError` – 

Implement this method in your custom checkpoint saver.




###  `aput(config: RunnableConfig, checkpoint: Checkpoint, metadata: CheckpointMetadata, new_versions: ChannelVersions) -> RunnableConfig` `async` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.ShallowPostgresSaver.aput "Permanent link")

Asynchronously store a checkpoint with its configuration and metadata.

Parameters:

  * **`config`**(`RunnableConfig`) – 

Configuration for the checkpoint.

  * **`checkpoint`**(`Checkpoint`) – 

The checkpoint to store.

  * **`metadata`**(`CheckpointMetadata`) – 

Additional metadata for the checkpoint.

  * **`new_versions`**(`ChannelVersions`) – 

New channel versions as of this write.




Returns:

  * **`RunnableConfig`**(`RunnableConfig` ) – 

Updated configuration after storing the checkpoint.




Raises:

  * `NotImplementedError` – 

Implement this method in your custom checkpoint saver.




###  `aput_writes(config: RunnableConfig, writes: Sequence[Tuple[str, Any]], task_id: str, task_path: str = '') -> None` `async` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.ShallowPostgresSaver.aput_writes "Permanent link")

Asynchronously store intermediate writes linked to a checkpoint.

Parameters:

  * **`config`**(`RunnableConfig`) – 

Configuration of the related checkpoint.

  * **`writes`**(`List[Tuple[str, Any]]`) – 

List of writes to store.

  * **`task_id`**(`str`) – 

Identifier for the task creating the writes.

  * **`task_path`**(`str` , default: `''` ) – 

Path of the task creating the writes.




Raises:

  * `NotImplementedError` – 

Implement this method in your custom checkpoint saver.




###  `from_conn_string(conn_string: str, *, pipeline: bool = False) -> Iterator[ShallowPostgresSaver]` `classmethod` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.ShallowPostgresSaver.from_conn_string "Permanent link")

Create a new ShallowPostgresSaver instance from a connection string.

Parameters:

  * **`conn_string`**(`str`) – 

The Postgres connection info string.

  * **`pipeline`**(`bool` , default: `False` ) – 

whether to use Pipeline




Returns:

  * **`ShallowPostgresSaver`**(`Iterator[ShallowPostgresSaver]` ) – 

A new ShallowPostgresSaver instance.




###  `setup() -> None` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.ShallowPostgresSaver.setup "Permanent link")

Set up the checkpoint database asynchronously.

This method creates the necessary tables in the Postgres database if they don't already exist and runs database migrations. It MUST be called directly by the user the first time checkpointer is used.

###  `list(config: Optional[RunnableConfig], *, filter: Optional[dict[str, Any]] = None, before: Optional[RunnableConfig] = None, limit: Optional[int] = None) -> Iterator[CheckpointTuple]` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.ShallowPostgresSaver.list "Permanent link")

List checkpoints from the database.

This method retrieves a list of checkpoint tuples from the Postgres database based on the provided config. For ShallowPostgresSaver, this method returns a list with ONLY the most recent checkpoint.

###  `get_tuple(config: RunnableConfig) -> Optional[CheckpointTuple]` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.ShallowPostgresSaver.get_tuple "Permanent link")

Get a checkpoint tuple from the database.

This method retrieves a checkpoint tuple from the Postgres database based on the provided config (matching the thread ID in the config).

Parameters:

  * **`config`**(`RunnableConfig`) – 

The config to use for retrieving the checkpoint.




Returns:

  * `Optional[CheckpointTuple]` – 

Optional[CheckpointTuple]: The retrieved checkpoint tuple, or None if no matching checkpoint was found.




Examples:

```
Basic:
>>> config = {"configurable": {"thread_id": "1"}}
>>> checkpoint_tuple = memory.get_tuple(config)
>>> print(checkpoint_tuple)
CheckpointTuple(...)
With timestamp:
>>> config = {
...  "configurable": {
...    "thread_id": "1",
...    "checkpoint_ns": "",
...    "checkpoint_id": "1ef4f797-8335-6428-8001-8a1503f9b875",
...  }
... }
>>> checkpoint_tuple = memory.get_tuple(config)
>>> print(checkpoint_tuple)
CheckpointTuple(...)

```


###  `put(config: RunnableConfig, checkpoint: Checkpoint, metadata: CheckpointMetadata, new_versions: ChannelVersions) -> RunnableConfig` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.ShallowPostgresSaver.put "Permanent link")

Save a checkpoint to the database.

This method saves a checkpoint to the Postgres database. The checkpoint is associated with the provided config. For ShallowPostgresSaver, this method saves ONLY the most recent checkpoint and overwrites a previous checkpoint, if it exists.

Parameters:

  * **`config`**(`RunnableConfig`) – 

The config to associate with the checkpoint.

  * **`checkpoint`**(`Checkpoint`) – 

The checkpoint to save.

  * **`metadata`**(`CheckpointMetadata`) – 

Additional metadata to save with the checkpoint.

  * **`new_versions`**(`ChannelVersions`) – 

New channel versions as of this write.




Returns:

  * **`RunnableConfig`**(`RunnableConfig` ) – 

Updated configuration after storing the checkpoint.




Examples:

```
>>> from langgraph.checkpoint.postgres import ShallowPostgresSaver
>>> DB_URI = "postgres://postgres:postgres@localhost:5432/postgres?sslmode=disable"
>>> with ShallowPostgresSaver.from_conn_string(DB_URI) as memory:
>>>   config = {"configurable": {"thread_id": "1", "checkpoint_ns": ""}}
>>>   checkpoint = {"ts": "2024-05-04T06:32:42.235444+00:00", "id": "1ef4f797-8335-6428-8001-8a1503f9b875", "channel_values": {"key": "value"}}
>>>   saved_config = memory.put(config, checkpoint, {"source": "input", "step": 1, "writes": {"key": "value"}}, {})
>>> print(saved_config)
{'configurable': {'thread_id': '1', 'checkpoint_ns': '', 'checkpoint_id': '1ef4f797-8335-6428-8001-8a1503f9b875'}}

```


###  `put_writes(config: RunnableConfig, writes: Sequence[tuple[str, Any]], task_id: str, task_path: str = '') -> None` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.ShallowPostgresSaver.put_writes "Permanent link")

Store intermediate writes linked to a checkpoint.

This method saves intermediate writes associated with a checkpoint to the Postgres database.

Parameters:

  * **`config`**(`RunnableConfig`) – 

Configuration of the related checkpoint.

  * **`writes`**(`List[Tuple[str, Any]]`) – 

List of writes to store.

  * **`task_id`**(`str`) – 

Identifier for the task creating the writes.




##  `PostgresSaver` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.PostgresSaver "Permanent link")

Bases: `BasePostgresSaver`

###  `config_specs: list[ConfigurableFieldSpec]` `property` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.PostgresSaver.config_specs "Permanent link")

Define the configuration options for the checkpoint saver.

Returns:

  * `list[ConfigurableFieldSpec]` – 

list[ConfigurableFieldSpec]: List of configuration field specs.




###  `get(config: RunnableConfig) -> Optional[Checkpoint]` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.PostgresSaver.get "Permanent link")

Fetch a checkpoint using the given configuration.

Parameters:

  * **`config`**(`RunnableConfig`) – 

Configuration specifying which checkpoint to retrieve.




Returns:

  * `Optional[Checkpoint]` – 

Optional[Checkpoint]: The requested checkpoint, or None if not found.




###  `aget(config: RunnableConfig) -> Optional[Checkpoint]` `async` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.PostgresSaver.aget "Permanent link")

Asynchronously fetch a checkpoint using the given configuration.

Parameters:

  * **`config`**(`RunnableConfig`) – 

Configuration specifying which checkpoint to retrieve.




Returns:

  * `Optional[Checkpoint]` – 

Optional[Checkpoint]: The requested checkpoint, or None if not found.




###  `aget_tuple(config: RunnableConfig) -> Optional[CheckpointTuple]` `async` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.PostgresSaver.aget_tuple "Permanent link")

Asynchronously fetch a checkpoint tuple using the given configuration.

Parameters:

  * **`config`**(`RunnableConfig`) – 

Configuration specifying which checkpoint to retrieve.




Returns:

  * `Optional[CheckpointTuple]` – 

Optional[CheckpointTuple]: The requested checkpoint tuple, or None if not found.




Raises:

  * `NotImplementedError` – 

Implement this method in your custom checkpoint saver.




###  `alist(config: Optional[RunnableConfig], *, filter: Optional[Dict[str, Any]] = None, before: Optional[RunnableConfig] = None, limit: Optional[int] = None) -> AsyncIterator[CheckpointTuple]` `async` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.PostgresSaver.alist "Permanent link")

Asynchronously list checkpoints that match the given criteria.

Parameters:

  * **`config`**(`Optional[RunnableConfig]`) – 

Base configuration for filtering checkpoints.

  * **`filter`**(`Optional[Dict[str, Any]]` , default: `None` ) – 

Additional filtering criteria for metadata.

  * **`before`**(`Optional[RunnableConfig]` , default: `None` ) – 

List checkpoints created before this configuration.

  * **`limit`**(`Optional[int]` , default: `None` ) – 

Maximum number of checkpoints to return.




Returns:

  * `AsyncIterator[CheckpointTuple]` – 

AsyncIterator[CheckpointTuple]: Async iterator of matching checkpoint tuples.




Raises:

  * `NotImplementedError` – 

Implement this method in your custom checkpoint saver.




###  `aput(config: RunnableConfig, checkpoint: Checkpoint, metadata: CheckpointMetadata, new_versions: ChannelVersions) -> RunnableConfig` `async` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.PostgresSaver.aput "Permanent link")

Asynchronously store a checkpoint with its configuration and metadata.

Parameters:

  * **`config`**(`RunnableConfig`) – 

Configuration for the checkpoint.

  * **`checkpoint`**(`Checkpoint`) – 

The checkpoint to store.

  * **`metadata`**(`CheckpointMetadata`) – 

Additional metadata for the checkpoint.

  * **`new_versions`**(`ChannelVersions`) – 

New channel versions as of this write.




Returns:

  * **`RunnableConfig`**(`RunnableConfig` ) – 

Updated configuration after storing the checkpoint.




Raises:

  * `NotImplementedError` – 

Implement this method in your custom checkpoint saver.




###  `aput_writes(config: RunnableConfig, writes: Sequence[Tuple[str, Any]], task_id: str, task_path: str = '') -> None` `async` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.PostgresSaver.aput_writes "Permanent link")

Asynchronously store intermediate writes linked to a checkpoint.

Parameters:

  * **`config`**(`RunnableConfig`) – 

Configuration of the related checkpoint.

  * **`writes`**(`List[Tuple[str, Any]]`) – 

List of writes to store.

  * **`task_id`**(`str`) – 

Identifier for the task creating the writes.

  * **`task_path`**(`str` , default: `''` ) – 

Path of the task creating the writes.




Raises:

  * `NotImplementedError` – 

Implement this method in your custom checkpoint saver.




###  `from_conn_string(conn_string: str, *, pipeline: bool = False) -> Iterator[PostgresSaver]` `classmethod` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.PostgresSaver.from_conn_string "Permanent link")

Create a new PostgresSaver instance from a connection string.

Parameters:

  * **`conn_string`**(`str`) – 

The Postgres connection info string.

  * **`pipeline`**(`bool` , default: `False` ) – 

whether to use Pipeline




Returns:

  * **`PostgresSaver`**(`Iterator[PostgresSaver]` ) – 

A new PostgresSaver instance.




###  `setup() -> None` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.PostgresSaver.setup "Permanent link")

Set up the checkpoint database asynchronously.

This method creates the necessary tables in the Postgres database if they don't already exist and runs database migrations. It MUST be called directly by the user the first time checkpointer is used.

###  `list(config: Optional[RunnableConfig], *, filter: Optional[dict[str, Any]] = None, before: Optional[RunnableConfig] = None, limit: Optional[int] = None) -> Iterator[CheckpointTuple]` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.PostgresSaver.list "Permanent link")

List checkpoints from the database.

This method retrieves a list of checkpoint tuples from the Postgres database based on the provided config. The checkpoints are ordered by checkpoint ID in descending order (newest first).

Parameters:

  * **`config`**(`RunnableConfig`) – 

The config to use for listing the checkpoints.

  * **`filter`**(`Optional[Dict[str, Any]]` , default: `None` ) – 

Additional filtering criteria for metadata. Defaults to None.

  * **`before`**(`Optional[RunnableConfig]` , default: `None` ) – 

If provided, only checkpoints before the specified checkpoint ID are returned. Defaults to None.

  * **`limit`**(`Optional[int]` , default: `None` ) – 

The maximum number of checkpoints to return. Defaults to None.




Yields:

  * `CheckpointTuple` – 

Iterator[CheckpointTuple]: An iterator of checkpoint tuples.




Examples:

```
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-0-1)>>> fromlanggraph.checkpoint.postgresimport PostgresSaver
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-0-2)>>> DB_URI = "postgres://postgres:postgres@localhost:5432/postgres?sslmode=disable"
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-0-3)>>> with PostgresSaver.from_conn_string(DB_URI) as memory:
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-0-4)... # Run a graph, then list the checkpoints
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-0-5)>>>   config = {"configurable": {"thread_id": "1"}}
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-0-6)>>>   checkpoints = list(memory.list(config, limit=2))
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-0-7)>>> print(checkpoints)
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-0-8)[CheckpointTuple(...), CheckpointTuple(...)]

```


```
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-0-1)>>> config = {"configurable": {"thread_id": "1"}}
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-0-2)>>> before = {"configurable": {"checkpoint_id": "1ef4f797-8335-6428-8001-8a1503f9b875"}}
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-0-3)>>> with PostgresSaver.from_conn_string(DB_URI) as memory:
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-0-4)... # Run a graph, then list the checkpoints
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-0-5)>>>   checkpoints = list(memory.list(config, before=before))
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-0-6)>>> print(checkpoints)
[](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__codelineno-0-7)[CheckpointTuple(...), ...]

```


###  `get_tuple(config: RunnableConfig) -> Optional[CheckpointTuple]` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.PostgresSaver.get_tuple "Permanent link")

Get a checkpoint tuple from the database.

This method retrieves a checkpoint tuple from the Postgres database based on the provided config. If the config contains a "checkpoint_id" key, the checkpoint with the matching thread ID and timestamp is retrieved. Otherwise, the latest checkpoint for the given thread ID is retrieved.

Parameters:

  * **`config`**(`RunnableConfig`) – 

The config to use for retrieving the checkpoint.




Returns:

  * `Optional[CheckpointTuple]` – 

Optional[CheckpointTuple]: The retrieved checkpoint tuple, or None if no matching checkpoint was found.




Examples:

```
Basic:
>>> config = {"configurable": {"thread_id": "1"}}
>>> checkpoint_tuple = memory.get_tuple(config)
>>> print(checkpoint_tuple)
CheckpointTuple(...)
With timestamp:
>>> config = {
...  "configurable": {
...    "thread_id": "1",
...    "checkpoint_ns": "",
...    "checkpoint_id": "1ef4f797-8335-6428-8001-8a1503f9b875",
...  }
... }
>>> checkpoint_tuple = memory.get_tuple(config)
>>> print(checkpoint_tuple)
CheckpointTuple(...)

```


###  `put(config: RunnableConfig, checkpoint: Checkpoint, metadata: CheckpointMetadata, new_versions: ChannelVersions) -> RunnableConfig` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.PostgresSaver.put "Permanent link")

Save a checkpoint to the database.

This method saves a checkpoint to the Postgres database. The checkpoint is associated with the provided config and its parent config (if any).

Parameters:

  * **`config`**(`RunnableConfig`) – 

The config to associate with the checkpoint.

  * **`checkpoint`**(`Checkpoint`) – 

The checkpoint to save.

  * **`metadata`**(`CheckpointMetadata`) – 

Additional metadata to save with the checkpoint.

  * **`new_versions`**(`ChannelVersions`) – 

New channel versions as of this write.




Returns:

  * **`RunnableConfig`**(`RunnableConfig` ) – 

Updated configuration after storing the checkpoint.




Examples:

```
>>> from langgraph.checkpoint.postgres import PostgresSaver
>>> DB_URI = "postgres://postgres:postgres@localhost:5432/postgres?sslmode=disable"
>>> with PostgresSaver.from_conn_string(DB_URI) as memory:
>>>   config = {"configurable": {"thread_id": "1", "checkpoint_ns": ""}}
>>>   checkpoint = {"ts": "2024-05-04T06:32:42.235444+00:00", "id": "1ef4f797-8335-6428-8001-8a1503f9b875", "channel_values": {"key": "value"}}
>>>   saved_config = memory.put(config, checkpoint, {"source": "input", "step": 1, "writes": {"key": "value"}}, {})
>>> print(saved_config)
{'configurable': {'thread_id': '1', 'checkpoint_ns': '', 'checkpoint_id': '1ef4f797-8335-6428-8001-8a1503f9b875'}}

```


###  `put_writes(config: RunnableConfig, writes: Sequence[tuple[str, Any]], task_id: str, task_path: str = '') -> None` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.PostgresSaver.put_writes "Permanent link")

Store intermediate writes linked to a checkpoint.

This method saves intermediate writes associated with a checkpoint to the Postgres database.

Parameters:

  * **`config`**(`RunnableConfig`) – 

Configuration of the related checkpoint.

  * **`writes`**(`List[Tuple[str, Any]]`) – 

List of writes to store.

  * **`task_id`**(`str`) – 

Identifier for the task creating the writes.




##  `AsyncShallowPostgresSaver` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncShallowPostgresSaver "Permanent link")

Bases: `BasePostgresSaver`

A checkpoint saver that uses Postgres to store checkpoints asynchronously.

This checkpointer ONLY stores the most recent checkpoint and does NOT retain any history. It is meant to be a light-weight drop-in replacement for the AsyncPostgresSaver that supports most of the LangGraph persistence functionality with the exception of time travel.

###  `config_specs: list[ConfigurableFieldSpec]` `property` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncShallowPostgresSaver.config_specs "Permanent link")

Define the configuration options for the checkpoint saver.

Returns:

  * `list[ConfigurableFieldSpec]` – 

list[ConfigurableFieldSpec]: List of configuration field specs.




###  `get(config: RunnableConfig) -> Optional[Checkpoint]` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncShallowPostgresSaver.get "Permanent link")

Fetch a checkpoint using the given configuration.

Parameters:

  * **`config`**(`RunnableConfig`) – 

Configuration specifying which checkpoint to retrieve.




Returns:

  * `Optional[Checkpoint]` – 

Optional[Checkpoint]: The requested checkpoint, or None if not found.




###  `aget(config: RunnableConfig) -> Optional[Checkpoint]` `async` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncShallowPostgresSaver.aget "Permanent link")

Asynchronously fetch a checkpoint using the given configuration.

Parameters:

  * **`config`**(`RunnableConfig`) – 

Configuration specifying which checkpoint to retrieve.




Returns:

  * `Optional[Checkpoint]` – 

Optional[Checkpoint]: The requested checkpoint, or None if not found.




###  `from_conn_string(conn_string: str, *, pipeline: bool = False, serde: Optional[SerializerProtocol] = None) -> AsyncIterator[AsyncShallowPostgresSaver]` `async` `classmethod` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncShallowPostgresSaver.from_conn_string "Permanent link")

Create a new AsyncShallowPostgresSaver instance from a connection string.

Parameters:

  * **`conn_string`**(`str`) – 

The Postgres connection info string.

  * **`pipeline`**(`bool` , default: `False` ) – 

whether to use AsyncPipeline




Returns:

  * **`AsyncShallowPostgresSaver`**(`AsyncIterator[AsyncShallowPostgresSaver]` ) – 

A new AsyncShallowPostgresSaver instance.




###  `setup() -> None` `async` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncShallowPostgresSaver.setup "Permanent link")

Set up the checkpoint database asynchronously.

This method creates the necessary tables in the Postgres database if they don't already exist and runs database migrations. It MUST be called directly by the user the first time checkpointer is used.

###  `alist(config: Optional[RunnableConfig], *, filter: Optional[dict[str, Any]] = None, before: Optional[RunnableConfig] = None, limit: Optional[int] = None) -> AsyncIterator[CheckpointTuple]` `async` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncShallowPostgresSaver.alist "Permanent link")

List checkpoints from the database asynchronously.

This method retrieves a list of checkpoint tuples from the Postgres database based on the provided config. For ShallowPostgresSaver, this method returns a list with ONLY the most recent checkpoint.

###  `aget_tuple(config: RunnableConfig) -> Optional[CheckpointTuple]` `async` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncShallowPostgresSaver.aget_tuple "Permanent link")

Get a checkpoint tuple from the database asynchronously.

This method retrieves a checkpoint tuple from the Postgres database based on the provided config (matching the thread ID in the config).

Parameters:

  * **`config`**(`RunnableConfig`) – 

The config to use for retrieving the checkpoint.




Returns:

  * `Optional[CheckpointTuple]` – 

Optional[CheckpointTuple]: The retrieved checkpoint tuple, or None if no matching checkpoint was found.




###  `aput(config: RunnableConfig, checkpoint: Checkpoint, metadata: CheckpointMetadata, new_versions: ChannelVersions) -> RunnableConfig` `async` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncShallowPostgresSaver.aput "Permanent link")

Save a checkpoint to the database asynchronously.

This method saves a checkpoint to the Postgres database. The checkpoint is associated with the provided config. For AsyncShallowPostgresSaver, this method saves ONLY the most recent checkpoint and overwrites a previous checkpoint, if it exists.

Parameters:

  * **`config`**(`RunnableConfig`) – 

The config to associate with the checkpoint.

  * **`checkpoint`**(`Checkpoint`) – 

The checkpoint to save.

  * **`metadata`**(`CheckpointMetadata`) – 

Additional metadata to save with the checkpoint.

  * **`new_versions`**(`ChannelVersions`) – 

New channel versions as of this write.




Returns:

  * **`RunnableConfig`**(`RunnableConfig` ) – 

Updated configuration after storing the checkpoint.




###  `aput_writes(config: RunnableConfig, writes: Sequence[tuple[str, Any]], task_id: str, task_path: str = '') -> None` `async` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncShallowPostgresSaver.aput_writes "Permanent link")

Store intermediate writes linked to a checkpoint asynchronously.

This method saves intermediate writes associated with a checkpoint to the database.

Parameters:

  * **`config`**(`RunnableConfig`) – 

Configuration of the related checkpoint.

  * **`writes`**(`Sequence[Tuple[str, Any]]`) – 

List of writes to store, each as (channel, value) pair.

  * **`task_id`**(`str`) – 

Identifier for the task creating the writes.




###  `list(config: Optional[RunnableConfig], *, filter: Optional[dict[str, Any]] = None, before: Optional[RunnableConfig] = None, limit: Optional[int] = None) -> Iterator[CheckpointTuple]` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncShallowPostgresSaver.list "Permanent link")

List checkpoints from the database.

This method retrieves a list of checkpoint tuples from the Postgres database based on the provided config. For ShallowPostgresSaver, this method returns a list with ONLY the most recent checkpoint.

###  `get_tuple(config: RunnableConfig) -> Optional[CheckpointTuple]` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncShallowPostgresSaver.get_tuple "Permanent link")

Get a checkpoint tuple from the database.

This method retrieves a checkpoint tuple from the Postgres database based on the provided config (matching the thread ID in the config).

Parameters:

  * **`config`**(`RunnableConfig`) – 

The config to use for retrieving the checkpoint.




Returns:

  * `Optional[CheckpointTuple]` – 

Optional[CheckpointTuple]: The retrieved checkpoint tuple, or None if no matching checkpoint was found.




###  `put(config: RunnableConfig, checkpoint: Checkpoint, metadata: CheckpointMetadata, new_versions: ChannelVersions) -> RunnableConfig` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncShallowPostgresSaver.put "Permanent link")

Save a checkpoint to the database.

This method saves a checkpoint to the Postgres database. The checkpoint is associated with the provided config. For AsyncShallowPostgresSaver, this method saves ONLY the most recent checkpoint and overwrites a previous checkpoint, if it exists.

Parameters:

  * **`config`**(`RunnableConfig`) – 

The config to associate with the checkpoint.

  * **`checkpoint`**(`Checkpoint`) – 

The checkpoint to save.

  * **`metadata`**(`CheckpointMetadata`) – 

Additional metadata to save with the checkpoint.

  * **`new_versions`**(`ChannelVersions`) – 

New channel versions as of this write.




Returns:

  * **`RunnableConfig`**(`RunnableConfig` ) – 

Updated configuration after storing the checkpoint.




###  `put_writes(config: RunnableConfig, writes: Sequence[tuple[str, Any]], task_id: str, task_path: str = '') -> None` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncShallowPostgresSaver.put_writes "Permanent link")

Store intermediate writes linked to a checkpoint.

This method saves intermediate writes associated with a checkpoint to the database.

Parameters:

  * **`config`**(`RunnableConfig`) – 

Configuration of the related checkpoint.

  * **`writes`**(`Sequence[Tuple[str, Any]]`) – 

List of writes to store, each as (channel, value) pair.

  * **`task_id`**(`str`) – 

Identifier for the task creating the writes.

  * **`task_path`**(`str` , default: `''` ) – 

Path of the task creating the writes.




##  `AsyncPostgresSaver` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncPostgresSaver "Permanent link")

Bases: `BasePostgresSaver`

###  `config_specs: list[ConfigurableFieldSpec]` `property` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncPostgresSaver.config_specs "Permanent link")

Define the configuration options for the checkpoint saver.

Returns:

  * `list[ConfigurableFieldSpec]` – 

list[ConfigurableFieldSpec]: List of configuration field specs.




###  `get(config: RunnableConfig) -> Optional[Checkpoint]` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncPostgresSaver.get "Permanent link")

Fetch a checkpoint using the given configuration.

Parameters:

  * **`config`**(`RunnableConfig`) – 

Configuration specifying which checkpoint to retrieve.




Returns:

  * `Optional[Checkpoint]` – 

Optional[Checkpoint]: The requested checkpoint, or None if not found.




###  `aget(config: RunnableConfig) -> Optional[Checkpoint]` `async` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncPostgresSaver.aget "Permanent link")

Asynchronously fetch a checkpoint using the given configuration.

Parameters:

  * **`config`**(`RunnableConfig`) – 

Configuration specifying which checkpoint to retrieve.




Returns:

  * `Optional[Checkpoint]` – 

Optional[Checkpoint]: The requested checkpoint, or None if not found.




###  `from_conn_string(conn_string: str, *, pipeline: bool = False, serde: Optional[SerializerProtocol] = None) -> AsyncIterator[AsyncPostgresSaver]` `async` `classmethod` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncPostgresSaver.from_conn_string "Permanent link")

Create a new AsyncPostgresSaver instance from a connection string.

Parameters:

  * **`conn_string`**(`str`) – 

The Postgres connection info string.

  * **`pipeline`**(`bool` , default: `False` ) – 

whether to use AsyncPipeline




Returns:

  * **`AsyncPostgresSaver`**(`AsyncIterator[AsyncPostgresSaver]` ) – 

A new AsyncPostgresSaver instance.




###  `setup() -> None` `async` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncPostgresSaver.setup "Permanent link")

Set up the checkpoint database asynchronously.

This method creates the necessary tables in the Postgres database if they don't already exist and runs database migrations. It MUST be called directly by the user the first time checkpointer is used.

###  `alist(config: Optional[RunnableConfig], *, filter: Optional[dict[str, Any]] = None, before: Optional[RunnableConfig] = None, limit: Optional[int] = None) -> AsyncIterator[CheckpointTuple]` `async` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncPostgresSaver.alist "Permanent link")

List checkpoints from the database asynchronously.

This method retrieves a list of checkpoint tuples from the Postgres database based on the provided config. The checkpoints are ordered by checkpoint ID in descending order (newest first).

Parameters:

  * **`config`**(`Optional[RunnableConfig]`) – 

Base configuration for filtering checkpoints.

  * **`filter`**(`Optional[Dict[str, Any]]` , default: `None` ) – 

Additional filtering criteria for metadata.

  * **`before`**(`Optional[RunnableConfig]` , default: `None` ) – 

If provided, only checkpoints before the specified checkpoint ID are returned. Defaults to None.

  * **`limit`**(`Optional[int]` , default: `None` ) – 

Maximum number of checkpoints to return.




Yields:

  * `AsyncIterator[CheckpointTuple]` – 

AsyncIterator[CheckpointTuple]: An asynchronous iterator of matching checkpoint tuples.




###  `aget_tuple(config: RunnableConfig) -> Optional[CheckpointTuple]` `async` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncPostgresSaver.aget_tuple "Permanent link")

Get a checkpoint tuple from the database asynchronously.

This method retrieves a checkpoint tuple from the Postgres database based on the provided config. If the config contains a "checkpoint_id" key, the checkpoint with the matching thread ID and "checkpoint_id" is retrieved. Otherwise, the latest checkpoint for the given thread ID is retrieved.

Parameters:

  * **`config`**(`RunnableConfig`) – 

The config to use for retrieving the checkpoint.




Returns:

  * `Optional[CheckpointTuple]` – 

Optional[CheckpointTuple]: The retrieved checkpoint tuple, or None if no matching checkpoint was found.




###  `aput(config: RunnableConfig, checkpoint: Checkpoint, metadata: CheckpointMetadata, new_versions: ChannelVersions) -> RunnableConfig` `async` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncPostgresSaver.aput "Permanent link")

Save a checkpoint to the database asynchronously.

This method saves a checkpoint to the Postgres database. The checkpoint is associated with the provided config and its parent config (if any).

Parameters:

  * **`config`**(`RunnableConfig`) – 

The config to associate with the checkpoint.

  * **`checkpoint`**(`Checkpoint`) – 

The checkpoint to save.

  * **`metadata`**(`CheckpointMetadata`) – 

Additional metadata to save with the checkpoint.

  * **`new_versions`**(`ChannelVersions`) – 

New channel versions as of this write.




Returns:

  * **`RunnableConfig`**(`RunnableConfig` ) – 

Updated configuration after storing the checkpoint.




###  `aput_writes(config: RunnableConfig, writes: Sequence[tuple[str, Any]], task_id: str, task_path: str = '') -> None` `async` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncPostgresSaver.aput_writes "Permanent link")

Store intermediate writes linked to a checkpoint asynchronously.

This method saves intermediate writes associated with a checkpoint to the database.

Parameters:

  * **`config`**(`RunnableConfig`) – 

Configuration of the related checkpoint.

  * **`writes`**(`Sequence[Tuple[str, Any]]`) – 

List of writes to store, each as (channel, value) pair.

  * **`task_id`**(`str`) – 

Identifier for the task creating the writes.




###  `list(config: Optional[RunnableConfig], *, filter: Optional[dict[str, Any]] = None, before: Optional[RunnableConfig] = None, limit: Optional[int] = None) -> Iterator[CheckpointTuple]` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncPostgresSaver.list "Permanent link")

List checkpoints from the database.

This method retrieves a list of checkpoint tuples from the Postgres database based on the provided config. The checkpoints are ordered by checkpoint ID in descending order (newest first).

Parameters:

  * **`config`**(`Optional[RunnableConfig]`) – 

Base configuration for filtering checkpoints.

  * **`filter`**(`Optional[Dict[str, Any]]` , default: `None` ) – 

Additional filtering criteria for metadata.

  * **`before`**(`Optional[RunnableConfig]` , default: `None` ) – 

If provided, only checkpoints before the specified checkpoint ID are returned. Defaults to None.

  * **`limit`**(`Optional[int]` , default: `None` ) – 

Maximum number of checkpoints to return.




Yields:

  * `CheckpointTuple` – 

Iterator[CheckpointTuple]: An iterator of matching checkpoint tuples.




###  `get_tuple(config: RunnableConfig) -> Optional[CheckpointTuple]` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncPostgresSaver.get_tuple "Permanent link")

Get a checkpoint tuple from the database.

This method retrieves a checkpoint tuple from the Postgres database based on the provided config. If the config contains a "checkpoint_id" key, the checkpoint with the matching thread ID and "checkpoint_id" is retrieved. Otherwise, the latest checkpoint for the given thread ID is retrieved.

Parameters:

  * **`config`**(`RunnableConfig`) – 

The config to use for retrieving the checkpoint.




Returns:

  * `Optional[CheckpointTuple]` – 

Optional[CheckpointTuple]: The retrieved checkpoint tuple, or None if no matching checkpoint was found.




###  `put(config: RunnableConfig, checkpoint: Checkpoint, metadata: CheckpointMetadata, new_versions: ChannelVersions) -> RunnableConfig` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncPostgresSaver.put "Permanent link")

Save a checkpoint to the database.

This method saves a checkpoint to the Postgres database. The checkpoint is associated with the provided config and its parent config (if any).

Parameters:

  * **`config`**(`RunnableConfig`) – 

The config to associate with the checkpoint.

  * **`checkpoint`**(`Checkpoint`) – 

The checkpoint to save.

  * **`metadata`**(`CheckpointMetadata`) – 

Additional metadata to save with the checkpoint.

  * **`new_versions`**(`ChannelVersions`) – 

New channel versions as of this write.




Returns:

  * **`RunnableConfig`**(`RunnableConfig` ) – 

Updated configuration after storing the checkpoint.




###  `put_writes(config: RunnableConfig, writes: Sequence[tuple[str, Any]], task_id: str, task_path: str = '') -> None` [¶](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncPostgresSaver.put_writes "Permanent link")

Store intermediate writes linked to a checkpoint.

This method saves intermediate writes associated with a checkpoint to the database.

Parameters:

  * **`config`**(`RunnableConfig`) – 

Configuration of the related checkpoint.

  * **`writes`**(`Sequence[Tuple[str, Any]]`) – 

List of writes to store, each as (channel, value) pair.

  * **`task_id`**(`str`) – 

Identifier for the task creating the writes.

  * **`task_path`**(`str` , default: `''` ) – 

Path of the task creating the writes.




Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Graphs  ](https://langchain-ai.github.io/langgraph/reference/graphs/) [ Next  Storage  ](https://langchain-ai.github.io/langgraph/reference/store/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/reference/checkpoints/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
