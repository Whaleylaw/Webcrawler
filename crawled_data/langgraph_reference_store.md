---
url: https://langchain-ai.github.io/langgraph/reference/store/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/reference/store/#storage)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Storage 

[ ](https://langchain-ai.github.io/langgraph/reference/store/?q= "Share")

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
      * Storage  [ Storage  ](https://langchain-ai.github.io/langgraph/reference/store/) Table of contents 
        * [ NamespacePath  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.NamespacePath)
        * [ NamespaceMatchType  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.NamespaceMatchType)
        * [ Item  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.Item)
        * [ SearchItem  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.SearchItem)
          * [ __init__  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.SearchItem.__init__)
        * [ GetOp  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.GetOp)
          * [ namespace  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.GetOp.namespace)
          * [ key  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.GetOp.key)
        * [ SearchOp  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.SearchOp)
          * [ namespace_prefix  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.SearchOp.namespace_prefix)
          * [ filter  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.SearchOp.filter)
          * [ limit  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.SearchOp.limit)
          * [ offset  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.SearchOp.offset)
          * [ query  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.SearchOp.query)
        * [ MatchCondition  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.MatchCondition)
          * [ match_type  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.MatchCondition.match_type)
          * [ path  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.MatchCondition.path)
        * [ ListNamespacesOp  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.ListNamespacesOp)
          * [ match_conditions  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.ListNamespacesOp.match_conditions)
          * [ max_depth  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.ListNamespacesOp.max_depth)
          * [ limit  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.ListNamespacesOp.limit)
          * [ offset  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.ListNamespacesOp.offset)
        * [ PutOp  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.PutOp)
          * [ namespace  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.PutOp.namespace)
          * [ key  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.PutOp.key)
          * [ value  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.PutOp.value)
          * [ index  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.PutOp.index)
        * [ InvalidNamespaceError  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.InvalidNamespaceError)
        * [ IndexConfig  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.IndexConfig)
          * [ dims  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.IndexConfig.dims)
          * [ embed  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.IndexConfig.embed)
          * [ fields  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.IndexConfig.fields)
        * [ BaseStore  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore)
          * [ batch  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore.batch)
          * [ abatch  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore.abatch)
          * [ get  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore.get)
          * [ search  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore.search)
          * [ put  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore.put)
          * [ delete  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore.delete)
          * [ list_namespaces  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore.list_namespaces)
          * [ aget  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore.aget)
          * [ asearch  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore.asearch)
          * [ aput  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore.aput)
          * [ adelete  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore.adelete)
          * [ alist_namespaces  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore.alist_namespaces)
        * [ ensure_embeddings  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.ensure_embeddings)
        * [ get_text_at_path  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.get_text_at_path)
        * [ tokenize_path  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.tokenize_path)
        * [ AsyncPostgresStore  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.postgres.AsyncPostgresStore)
          * [ from_conn_string  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.postgres.AsyncPostgresStore.from_conn_string)
          * [ setup  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.postgres.AsyncPostgresStore.setup)
        * [ PostgresStore  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.postgres.PostgresStore)
          * [ get  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.postgres.PostgresStore.get)
          * [ search  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.postgres.PostgresStore.search)
          * [ put  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.postgres.PostgresStore.put)
          * [ delete  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.postgres.PostgresStore.delete)
          * [ list_namespaces  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.postgres.PostgresStore.list_namespaces)
          * [ aget  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.postgres.PostgresStore.aget)
          * [ asearch  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.postgres.PostgresStore.asearch)
          * [ aput  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.postgres.PostgresStore.aput)
          * [ adelete  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.postgres.PostgresStore.adelete)
          * [ alist_namespaces  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.postgres.PostgresStore.alist_namespaces)
          * [ from_conn_string  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.postgres.PostgresStore.from_conn_string)
          * [ setup  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.postgres.PostgresStore.setup)
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

  * [ NamespacePath  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.NamespacePath)
  * [ NamespaceMatchType  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.NamespaceMatchType)
  * [ Item  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.Item)
  * [ SearchItem  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.SearchItem)
    * [ __init__  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.SearchItem.__init__)
  * [ GetOp  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.GetOp)
    * [ namespace  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.GetOp.namespace)
    * [ key  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.GetOp.key)
  * [ SearchOp  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.SearchOp)
    * [ namespace_prefix  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.SearchOp.namespace_prefix)
    * [ filter  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.SearchOp.filter)
    * [ limit  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.SearchOp.limit)
    * [ offset  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.SearchOp.offset)
    * [ query  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.SearchOp.query)
  * [ MatchCondition  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.MatchCondition)
    * [ match_type  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.MatchCondition.match_type)
    * [ path  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.MatchCondition.path)
  * [ ListNamespacesOp  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.ListNamespacesOp)
    * [ match_conditions  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.ListNamespacesOp.match_conditions)
    * [ max_depth  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.ListNamespacesOp.max_depth)
    * [ limit  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.ListNamespacesOp.limit)
    * [ offset  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.ListNamespacesOp.offset)
  * [ PutOp  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.PutOp)
    * [ namespace  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.PutOp.namespace)
    * [ key  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.PutOp.key)
    * [ value  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.PutOp.value)
    * [ index  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.PutOp.index)
  * [ InvalidNamespaceError  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.InvalidNamespaceError)
  * [ IndexConfig  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.IndexConfig)
    * [ dims  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.IndexConfig.dims)
    * [ embed  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.IndexConfig.embed)
    * [ fields  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.IndexConfig.fields)
  * [ BaseStore  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore)
    * [ batch  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore.batch)
    * [ abatch  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore.abatch)
    * [ get  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore.get)
    * [ search  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore.search)
    * [ put  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore.put)
    * [ delete  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore.delete)
    * [ list_namespaces  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore.list_namespaces)
    * [ aget  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore.aget)
    * [ asearch  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore.asearch)
    * [ aput  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore.aput)
    * [ adelete  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore.adelete)
    * [ alist_namespaces  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore.alist_namespaces)
  * [ ensure_embeddings  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.ensure_embeddings)
  * [ get_text_at_path  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.get_text_at_path)
  * [ tokenize_path  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.tokenize_path)
  * [ AsyncPostgresStore  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.postgres.AsyncPostgresStore)
    * [ from_conn_string  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.postgres.AsyncPostgresStore.from_conn_string)
    * [ setup  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.postgres.AsyncPostgresStore.setup)
  * [ PostgresStore  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.postgres.PostgresStore)
    * [ get  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.postgres.PostgresStore.get)
    * [ search  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.postgres.PostgresStore.search)
    * [ put  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.postgres.PostgresStore.put)
    * [ delete  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.postgres.PostgresStore.delete)
    * [ list_namespaces  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.postgres.PostgresStore.list_namespaces)
    * [ aget  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.postgres.PostgresStore.aget)
    * [ asearch  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.postgres.PostgresStore.asearch)
    * [ aput  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.postgres.PostgresStore.aput)
    * [ adelete  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.postgres.PostgresStore.adelete)
    * [ alist_namespaces  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.postgres.PostgresStore.alist_namespaces)
    * [ from_conn_string  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.postgres.PostgresStore.from_conn_string)
    * [ setup  ](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.postgres.PostgresStore.setup)



  1. [ API reference  ](https://langchain-ai.github.io/langgraph/reference/graphs/)
  2. [ Library  ](https://langchain-ai.github.io/langgraph/reference/graphs/)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/reference/store.md "Edit this page")

# Storage[¶](https://langchain-ai.github.io/langgraph/reference/store/#storage "Permanent link")

Base classes and types for persistent key-value stores.

Stores provide long-term memory that persists across threads and conversations. Supports hierarchical namespaces, key-value storage, and optional vector search.

Core types

  * BaseStore: Store interface with sync/async operations
  * Item: Stored key-value pairs with metadata
  * Op: Get/Put/Search/List operations



##  `NamespacePath = tuple[Union[str, Literal['*']], ...]` `module-attribute` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.NamespacePath "Permanent link")

A tuple representing a namespace path that can include wildcards.

Examples

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-1)("users",) # Exact users namespace
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-2)("documents", "*") # Any sub-namespace under documents
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-3)("cache", "*", "v1") # Any cache category with v1 version

```


##  `NamespaceMatchType = Literal['prefix', 'suffix']` `module-attribute` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.NamespaceMatchType "Permanent link")

Specifies how to match namespace paths.

Values

"prefix": Match from the start of the namespace "suffix": Match from the end of the namespace

##  `Item` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.Item "Permanent link")

Represents a stored item with metadata.

Parameters:

  * **`value`**(`dict[str, Any]`) – 

The stored data as a dictionary. Keys are filterable.

  * **`key`**(`str`) – 

Unique identifier within the namespace.

  * **`namespace`**(`tuple[str, ...]`) – 

Hierarchical path defining the collection in which this document resides. Represented as a tuple of strings, allowing for nested categorization. For example: ("documents", 'user123')

  * **`created_at`**(`datetime`) – 

Timestamp of item creation.

  * **`updated_at`**(`datetime`) – 

Timestamp of last update.




##  `SearchItem` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.SearchItem "Permanent link")

Bases: `Item`

Represents an item returned from a search operation with additional metadata.

###  `__init__(namespace: tuple[str, ...], key: str, value: dict[str, Any], created_at: datetime, updated_at: datetime, score: Optional[float] = None) -> None` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.SearchItem.__init__ "Permanent link")

Initialize a result item.

Parameters:

  * **`namespace`**(`tuple[str, ...]`) – 

Hierarchical path to the item.

  * **`key`**(`str`) – 

Unique identifier within the namespace.

  * **`value`**(`dict[str, Any]`) – 

The stored value.

  * **`created_at`**(`datetime`) – 

When the item was first created.

  * **`updated_at`**(`datetime`) – 

When the item was last updated.

  * **`score`**(`Optional[float]` , default: `None` ) – 

Relevance/similarity score if from a ranked operation.




##  `GetOp` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.GetOp "Permanent link")

Bases: `NamedTuple`

Operation to retrieve a specific item by its namespace and key.

This operation allows precise retrieval of stored items using their full path (namespace) and unique identifier (key) combination.

Examples

Basic item retrieval: 

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-1)GetOp(namespace=("users", "profiles"), key="user123")
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-2)GetOp(namespace=("cache", "embeddings"), key="doc456")

```


###  `namespace: tuple[str, ...]` `instance-attribute` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.GetOp.namespace "Permanent link")

Hierarchical path that uniquely identifies the item's location.

Examples

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-1)("users",) # Root level users namespace
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-2)("users", "profiles") # Profiles within users namespace

```


###  `key: str` `instance-attribute` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.GetOp.key "Permanent link")

Unique identifier for the item within its specific namespace.

Examples

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-1)"user123" # For a user profile
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-2)"doc456" # For a document

```


##  `SearchOp` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.SearchOp "Permanent link")

Bases: `NamedTuple`

Operation to search for items within a specified namespace hierarchy.

This operation supports both structured filtering and natural language search within a given namespace prefix. It provides pagination through limit and offset parameters.

Note

Natural language search support depends on your store implementation.

Examples

Search with filters and pagination: 

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-1)SearchOp(
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-2)  namespace_prefix=("documents",),
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-3)  filter={"type": "report", "status": "active"},
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-4)  limit=5,
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-5)  offset=10
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-6))

```


Natural language search: 

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-1)SearchOp(
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-2)  namespace_prefix=("users", "content"),
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-3)  query="technical documentation about APIs",
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-4)  limit=20
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-5))

```


###  `namespace_prefix: tuple[str, ...]` `instance-attribute` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.SearchOp.namespace_prefix "Permanent link")

Hierarchical path prefix defining the search scope.

Examples

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-1)() # Search entire store
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-2)("documents",) # Search all documents
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-3)("users", "content") # Search within user content

```


###  `filter: Optional[dict[str, Any]] = None` `class-attribute` `instance-attribute` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.SearchOp.filter "Permanent link")

Key-value pairs for filtering results based on exact matches or comparison operators.

The filter supports both exact matches and operator-based comparisons.

Supported Operators

  * $eq: Equal to (same as direct value comparison)
  * $ne: Not equal to
  * $gt: Greater than
  * $gte: Greater than or equal to
  * $lt: Less than
  * $lte: Less than or equal to

Examples

Simple exact match:

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-1){"status": "active"}

```


Comparison operators:

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-1){"score": {"$gt": 4.99}} # Score greater than 4.99

```


Multiple conditions:

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-1){
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-2)  "score": {"$gte": 3.0},
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-3)  "color": "red"
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-4)}

```


###  `limit: int = 10` `class-attribute` `instance-attribute` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.SearchOp.limit "Permanent link")

Maximum number of items to return in the search results.

###  `offset: int = 0` `class-attribute` `instance-attribute` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.SearchOp.offset "Permanent link")

Number of matching items to skip for pagination.

###  `query: Optional[str] = None` `class-attribute` `instance-attribute` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.SearchOp.query "Permanent link")

Natural language search query for semantic search capabilities.

Examples

  * "technical documentation about REST APIs"
  * "machine learning papers from 2023"



##  `MatchCondition` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.MatchCondition "Permanent link")

Bases: `NamedTuple`

Represents a pattern for matching namespaces in the store.

This class combines a match type (prefix or suffix) with a namespace path pattern that can include wildcards to flexibly match different namespace hierarchies.

Examples

Prefix matching: 

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-1)MatchCondition(match_type="prefix", path=("users", "profiles"))

```


Suffix matching with wildcard: 

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-1)MatchCondition(match_type="suffix", path=("cache", "*"))

```


Simple suffix matching: 

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-1)MatchCondition(match_type="suffix", path=("v1",))

```


###  `match_type: NamespaceMatchType` `instance-attribute` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.MatchCondition.match_type "Permanent link")

Type of namespace matching to perform.

###  `path: NamespacePath` `instance-attribute` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.MatchCondition.path "Permanent link")

Namespace path pattern that can include wildcards.

##  `ListNamespacesOp` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.ListNamespacesOp "Permanent link")

Bases: `NamedTuple`

Operation to list and filter namespaces in the store.

This operation allows exploring the organization of data, finding specific collections, and navigating the namespace hierarchy.

Examples

List all namespaces under the "documents" path: 

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-1)ListNamespacesOp(
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-2)  match_conditions=(MatchCondition(match_type="prefix", path=("documents",)),),
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-3)  max_depth=2
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-4))

```


List all namespaces that end with "v1": 

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-1)ListNamespacesOp(
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-2)  match_conditions=(MatchCondition(match_type="suffix", path=("v1",)),),
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-3)  limit=50
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-4))

```


###  `match_conditions: Optional[tuple[MatchCondition, ...]] = None` `class-attribute` `instance-attribute` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.ListNamespacesOp.match_conditions "Permanent link")

Optional conditions for filtering namespaces.

Examples

All user namespaces: 

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-1)(MatchCondition(match_type="prefix", path=("users",)),)

```


All namespaces that start with "docs" and end with "draft": 

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-1)(
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-2)  MatchCondition(match_type="prefix", path=("docs",)),
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-3)  MatchCondition(match_type="suffix", path=("draft",))
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-4)) 

```


###  `max_depth: Optional[int] = None` `class-attribute` `instance-attribute` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.ListNamespacesOp.max_depth "Permanent link")

Maximum depth of namespace hierarchy to return.

Note

Namespaces deeper than this level will be truncated.

###  `limit: int = 100` `class-attribute` `instance-attribute` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.ListNamespacesOp.limit "Permanent link")

Maximum number of namespaces to return.

###  `offset: int = 0` `class-attribute` `instance-attribute` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.ListNamespacesOp.offset "Permanent link")

Number of namespaces to skip for pagination.

##  `PutOp` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.PutOp "Permanent link")

Bases: `NamedTuple`

Operation to store, update, or delete an item in the store.

This class represents a single operation to modify the store's contents, whether adding new items, updating existing ones, or removing them.

###  `namespace: tuple[str, ...]` `instance-attribute` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.PutOp.namespace "Permanent link")

Hierarchical path that identifies the location of the item.

The namespace acts as a folder-like structure to organize items. Each element in the tuple represents one level in the hierarchy.

Examples

Root level documents 

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-1)("documents",)

```


User-specific documents 

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-1)("documents", "user123")

```


Nested cache structure 

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-1)("cache", "embeddings", "v1")

```


###  `key: str` `instance-attribute` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.PutOp.key "Permanent link")

Unique identifier for the item within its namespace.

The key must be unique within the specific namespace to avoid conflicts. Together with the namespace, it forms a complete path to the item.

Example

If namespace is ("documents", "user123") and key is "report1", the full path would effectively be "documents/user123/report1"

###  `value: Optional[dict[str, Any]]` `instance-attribute` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.PutOp.value "Permanent link")

The data to store, or None to mark the item for deletion.

The value must be a dictionary with string keys and JSON-serializable values. Setting this to None signals that the item should be deleted.

Example

{ "field1": "string value", "field2": 123, "nested": {"can": "contain", "any": "serializable data"} }

###  `index: Optional[Union[Literal[False], list[str]]] = None` `class-attribute` `instance-attribute` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.PutOp.index "Permanent link")

Controls how the item's fields are indexed for search operations.

Indexing configuration determines how the item can be found through search

  * None (default): Uses the store's default indexing configuration (if provided)
  * False: Disables indexing for this item
  * list[str]: Specifies which json path fields to index for search



The item remains accessible through direct get() operations regardless of indexing. When indexed, fields can be searched using natural language queries through vector similarity search (if supported by the store implementation).

Path Syntax

  * Simple field access: "field"
  * Nested fields: "parent.child.grandchild"
  * Array indexing:
  * Specific index: "array[0]"
  * Last element: "array[-1]"
  * All elements (each individually): "array[*]"

Examples

  * None - Use store defaults (whole item)
  * list[str] - List of fields to index



```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-1)[
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-2)  "metadata.title",          # Nested field access
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-3)  "context[*].content",        # Index content from all context as separate vectors
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-4)  "authors[0].name",          # First author's name
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-5)  "revisions[-1].changes",       # Most recent revision's changes
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-6)  "sections[*].paragraphs[*].text",  # All text from all paragraphs in all sections
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-7)  "metadata.tags[*]",         # All tags in metadata
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-8)]

```


##  `InvalidNamespaceError` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.InvalidNamespaceError "Permanent link")

Bases: `ValueError`

Provided namespace is invalid.

##  `IndexConfig` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.IndexConfig "Permanent link")

Bases: `TypedDict`

Configuration for indexing documents for semantic search in the store.

If not provided to the store, the store will not support vector search. In that case, all `index` arguments to put() and `aput()` operations will be ignored.

###  `dims: int` `instance-attribute` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.IndexConfig.dims "Permanent link")

Number of dimensions in the embedding vectors.

Common embedding models have the following dimensions

  * openai:text-embedding-3-large: 3072
  * openai:text-embedding-3-small: 1536
  * openai:text-embedding-ada-002: 1536
  * cohere:embed-english-v3.0: 1024
  * cohere:embed-english-light-v3.0: 384
  * cohere:embed-multilingual-v3.0: 1024
  * cohere:embed-multilingual-light-v3.0: 384



###  `embed: Union[Embeddings, EmbeddingsFunc, AEmbeddingsFunc, str]` `instance-attribute` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.IndexConfig.embed "Permanent link")

Optional function to generate embeddings from text.

Can be specified in three ways

  1. A LangChain Embeddings instance
  2. A synchronous embedding function (EmbeddingsFunc)
  3. An asynchronous embedding function (AEmbeddingsFunc)
  4. A provider string (e.g., "openai:text-embedding-3-small")

Examples

Using LangChain's initialization with InMemoryStore: 

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-1)fromlangchain.embeddingsimport init_embeddings
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-2)fromlanggraph.store.memoryimport InMemoryStore
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-3)
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-4)store = InMemoryStore(
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-5)  index={
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-6)    "dims": 1536,
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-7)    "embed": init_embeddings("openai:text-embedding-3-small")
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-8)  }
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-9))

```


Using a custom embedding function with InMemoryStore: 

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-1)fromopenaiimport OpenAI
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-2)fromlanggraph.store.memoryimport InMemoryStore
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-4)client = OpenAI()
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-5)
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-6)defembed_texts(texts: list[str]) -> list[list[float]]:
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-7)  response = client.embeddings.create(
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-8)    model="text-embedding-3-small",
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-9)    input=texts
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-10)  )
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-11)  return [e.embedding for e in response.data]
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-12)
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-13)store = InMemoryStore(
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-14)  index={
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-15)    "dims": 1536,
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-16)    "embed": embed_texts
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-17)  }
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-18))

```


Using an asynchronous embedding function with InMemoryStore: 

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-1)fromopenaiimport AsyncOpenAI
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-2)fromlanggraph.store.memoryimport InMemoryStore
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-3)
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-4)client = AsyncOpenAI()
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-5)
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-6)async defaembed_texts(texts: list[str]) -> list[list[float]]:
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-7)  response = await client.embeddings.create(
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-8)    model="text-embedding-3-small",
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-9)    input=texts
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-10)  )
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-11)  return [e.embedding for e in response.data]
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-12)
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-13)store = InMemoryStore(
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-14)  index={
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-15)    "dims": 1536,
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-16)    "embed": aembed_texts
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-17)  }
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-18))

```


###  `fields: Optional[list[str]]` `instance-attribute` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.IndexConfig.fields "Permanent link")

Fields to extract text from for embedding generation.

Controls which parts of stored items are embedded for semantic search. Follows JSON path syntax:

```
- ["$"]: Embeds the entire JSON object as one vector (default)
- ["field1", "field2"]: Embeds specific top-level fields
- ["parent.child"]: Embeds nested fields using dot notation
- ["array[*].field"]: Embeds field from each array element separately

```


Note

You can always override this behavior when storing an item using the `index` parameter in the `put` or `aput` operations.

Examples

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-1)# Embed entire document (default)
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-2)fields=["$"]
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-3)
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-4)# Embed specific fields
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-5)fields=["text", "summary"]
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-6)
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-7)# Embed nested fields
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-8)fields=["metadata.title", "content.body"]
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-9)
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-10)# Embed from arrays
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-11)fields=["messages[*].content"] # Each message content separately
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-12)fields=["context[0].text"]   # First context item's text

```


Note

  * Fields missing from a document are skipped
  * Array notation creates separate embeddings for each element
  * Complex nested paths are supported (e.g., "a.b[*].c.d")



##  `BaseStore` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore "Permanent link")

Bases: `ABC`

Abstract base class for persistent key-value stores.

Stores enable persistence and memory that can be shared across threads, scoped to user IDs, assistant IDs, or other arbitrary namespaces. Some implementations may support semantic search capabilities through an optional `index` configuration.

Note

Semantic search capabilities vary by implementation and are typically disabled by default. Stores that support this feature can be configured by providing an `index` configuration at creation time. Without this configuration, semantic search is disabled and any `index` arguments to storage operations will have no effect.

###  `batch(ops: Iterable[Op]) -> list[Result]` `abstractmethod` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore.batch "Permanent link")

Execute multiple operations synchronously in a single batch.

Parameters:

  * **`ops`**(`Iterable[Op]`) – 

An iterable of operations to execute.




Returns:

  * `list[Result]` – 

A list of results, where each result corresponds to an operation in the input.

  * `list[Result]` – 

The order of results matches the order of input operations.




###  `abatch(ops: Iterable[Op]) -> list[Result]` `abstractmethod` `async` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore.abatch "Permanent link")

Execute multiple operations asynchronously in a single batch.

Parameters:

  * **`ops`**(`Iterable[Op]`) – 

An iterable of operations to execute.




Returns:

  * `list[Result]` – 

A list of results, where each result corresponds to an operation in the input.

  * `list[Result]` – 

The order of results matches the order of input operations.




###  `get(namespace: tuple[str, ...], key: str) -> Optional[Item]` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore.get "Permanent link")

Retrieve a single item.

Parameters:

  * **`namespace`**(`tuple[str, ...]`) – 

Hierarchical path for the item.

  * **`key`**(`str`) – 

Unique identifier within the namespace.




Returns:

  * `Optional[Item]` – 

The retrieved item or None if not found.




###  `search(namespace_prefix: tuple[str, ...], /, *, query: Optional[str] = None, filter: Optional[dict[str, Any]] = None, limit: int = 10, offset: int = 0) -> list[SearchItem]` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore.search "Permanent link")

Search for items within a namespace prefix.

Parameters:

  * **`namespace_prefix`**(`tuple[str, ...]`) – 

Hierarchical path prefix to search within.

  * **`query`**(`Optional[str]` , default: `None` ) – 

Optional query for natural language search.

  * **`filter`**(`Optional[dict[str, Any]]` , default: `None` ) – 

Key-value pairs to filter results.

  * **`limit`**(`int` , default: `10` ) – 

Maximum number of items to return.

  * **`offset`**(`int` , default: `0` ) – 

Number of items to skip before returning results.




Returns:

  * `list[SearchItem]` – 

List of items matching the search criteria.


Examples

Basic filtering: 

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-1)# Search for documents with specific metadata
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-2)results = store.search(
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-3)  ("docs",),
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-4)  filter={"type": "article", "status": "published"}
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-5))

```


Natural language search (requires vector store implementation): 

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-1)# Initialize store with embedding configuration
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-2)store = YourStore( # e.g., InMemoryStore, AsyncPostgresStore
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-3)  index={
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-4)    "dims": 1536, # embedding dimensions
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-5)    "embed": your_embedding_function, # function to create embeddings
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-6)    "fields": ["text"] # fields to embed. Defaults to ["$"]
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-7)  }
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-8))
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-10)# Search for semantically similar documents
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-11)results = store.search(
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-12)  ("docs",),
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-13)  query="machine learning applications in healthcare",
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-14)  filter={"type": "research_paper"},
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-15)  limit=5
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-16))

```


Note: Natural language search support depends on your store implementation and requires proper embedding configuration.

###  `put(namespace: tuple[str, ...], key: str, value: dict[str, Any], index: Optional[Union[Literal[False], list[str]]] = None) -> None` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore.put "Permanent link")

Store or update an item in the store.

Parameters:

  * **`namespace`**(`tuple[str, ...]`) – 

Hierarchical path for the item, represented as a tuple of strings. Example: ("documents", "user123")

  * **`key`**(`str`) – 

Unique identifier within the namespace. Together with namespace forms the complete path to the item.

  * **`value`**(`dict[str, Any]`) – 

Dictionary containing the item's data. Must contain string keys and JSON-serializable values.

  * **`index`**(`Optional[Union[Literal[False], list[str]]]` , default: `None` ) – 

Controls how the item's fields are indexed for search:

    * None (default): Use `fields` you configured when creating the store (if any) If you do not initialize the store with indexing capabilities, the `index` parameter will be ignored
    * False: Disable indexing for this item
    * list[str]: List of field paths to index, supporting:
      * Nested fields: "metadata.title"
      * Array access: "chapters[*].content" (each indexed separately)
      * Specific indices: "authors[0].name"


Note

Indexing support depends on your store implementation. If you do not initialize the store with indexing capabilities, the `index` parameter will be ignored.

Examples

Store item. Indexing depends on how you configure the store. 

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-1)store.put(("docs",), "report", {"memory": "Will likes ai"})

```


Do not index item for semantic search. Still accessible through get() and search() operations but won't have a vector representation. 

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-1)store.put(("docs",), "report", {"memory": "Will likes ai"}, index=False)

```


Index specific fields for search. 

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-1)store.put(("docs",), "report", {"memory": "Will likes ai"}, index=["memory"])

```


###  `delete(namespace: tuple[str, ...], key: str) -> None` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore.delete "Permanent link")

Delete an item.

Parameters:

  * **`namespace`**(`tuple[str, ...]`) – 

Hierarchical path for the item.

  * **`key`**(`str`) – 

Unique identifier within the namespace.




###  `list_namespaces(*, prefix: Optional[NamespacePath] = None, suffix: Optional[NamespacePath] = None, max_depth: Optional[int] = None, limit: int = 100, offset: int = 0) -> list[tuple[str, ...]]` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore.list_namespaces "Permanent link")

List and filter namespaces in the store.

Used to explore the organization of data, find specific collections, or navigate the namespace hierarchy.

Parameters:

  * **`prefix`**(`Optional[Tuple[str, ...]]` , default: `None` ) – 

Filter namespaces that start with this path.

  * **`suffix`**(`Optional[Tuple[str, ...]]` , default: `None` ) – 

Filter namespaces that end with this path.

  * **`max_depth`**(`Optional[int]` , default: `None` ) – 

Return namespaces up to this depth in the hierarchy. Namespaces deeper than this level will be truncated.

  * **`limit`**(`int` , default: `100` ) – 

Maximum number of namespaces to return (default 100).

  * **`offset`**(`int` , default: `0` ) – 

Number of namespaces to skip for pagination (default 0).




Returns:

  * `list[tuple[str, ...]]` – 

List[Tuple[str, ...]]: A list of namespace tuples that match the criteria.

  * `list[tuple[str, ...]]` – 

Each tuple represents a full namespace path up to `max_depth`.




???+ example "Examples": Setting max_depth=3. Given the namespaces: 

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-1)# Example if you have the following namespaces:
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-2)# ("a", "b", "c")
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-3)# ("a", "b", "d", "e")
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-4)# ("a", "b", "d", "i")
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-5)# ("a", "b", "f")
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-6)# ("a", "c", "f")
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-7)store.list_namespaces(prefix=("a", "b"), max_depth=3)
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-8)# [("a", "b", "c"), ("a", "b", "d"), ("a", "b", "f")]

```


###  `aget(namespace: tuple[str, ...], key: str) -> Optional[Item]` `async` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore.aget "Permanent link")

Asynchronously retrieve a single item.

Parameters:

  * **`namespace`**(`tuple[str, ...]`) – 

Hierarchical path for the item.

  * **`key`**(`str`) – 

Unique identifier within the namespace.




Returns:

  * `Optional[Item]` – 

The retrieved item or None if not found.




###  `asearch(namespace_prefix: tuple[str, ...], /, *, query: Optional[str] = None, filter: Optional[dict[str, Any]] = None, limit: int = 10, offset: int = 0) -> list[SearchItem]` `async` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore.asearch "Permanent link")

Asynchronously search for items within a namespace prefix.

Parameters:

  * **`namespace_prefix`**(`tuple[str, ...]`) – 

Hierarchical path prefix to search within.

  * **`query`**(`Optional[str]` , default: `None` ) – 

Optional query for natural language search.

  * **`filter`**(`Optional[dict[str, Any]]` , default: `None` ) – 

Key-value pairs to filter results.

  * **`limit`**(`int` , default: `10` ) – 

Maximum number of items to return.

  * **`offset`**(`int` , default: `0` ) – 

Number of items to skip before returning results.




Returns:

  * `list[SearchItem]` – 

List of items matching the search criteria.


Examples

Basic filtering: 

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-1)# Search for documents with specific metadata
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-2)results = await store.asearch(
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-3)  ("docs",),
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-4)  filter={"type": "article", "status": "published"}
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-5))

```


Natural language search (requires vector store implementation): 

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-1)# Initialize store with embedding configuration
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-2)store = YourStore( # e.g., InMemoryStore, AsyncPostgresStore
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-3)  index={
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-4)    "dims": 1536, # embedding dimensions
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-5)    "embed": your_embedding_function, # function to create embeddings
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-6)    "fields": ["text"] # fields to embed
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-7)  }
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-8))
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-10)# Search for semantically similar documents
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-11)results = await store.asearch(
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-12)  ("docs",),
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-13)  query="machine learning applications in healthcare",
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-14)  filter={"type": "research_paper"},
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-15)  limit=5
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-16))

```


Note: Natural language search support depends on your store implementation and requires proper embedding configuration.

###  `aput(namespace: tuple[str, ...], key: str, value: dict[str, Any], index: Optional[Union[Literal[False], list[str]]] = None) -> None` `async` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore.aput "Permanent link")

Asynchronously store or update an item in the store.

Parameters:

  * **`namespace`**(`tuple[str, ...]`) – 

Hierarchical path for the item, represented as a tuple of strings. Example: ("documents", "user123")

  * **`key`**(`str`) – 

Unique identifier within the namespace. Together with namespace forms the complete path to the item.

  * **`value`**(`dict[str, Any]`) – 

Dictionary containing the item's data. Must contain string keys and JSON-serializable values.

  * **`index`**(`Optional[Union[Literal[False], list[str]]]` , default: `None` ) – 

Controls how the item's fields are indexed for search:

    * None (default): Use `fields` you configured when creating the store (if any) If you do not initialize the store with indexing capabilities, the `index` parameter will be ignored
    * False: Disable indexing for this item
    * list[str]: List of field paths to index, supporting:
      * Nested fields: "metadata.title"
      * Array access: "chapters[*].content" (each indexed separately)
      * Specific indices: "authors[0].name"


Note

Indexing support depends on your store implementation. If you do not initialize the store with indexing capabilities, the `index` parameter will be ignored.

Examples

Store item. Indexing depends on how you configure the store. 

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-1)await store.aput(("docs",), "report", {"memory": "Will likes ai"})

```


Do not index item for semantic search. Still accessible through get() and search() operations but won't have a vector representation. 

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-1)await store.aput(("docs",), "report", {"memory": "Will likes ai"}, index=False)

```


Index specific fields for search (if store configured to index items): 

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-1)await store.aput(
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-2)  ("docs",),
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-3)  "report",
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-4)  {
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-5)    "memory": "Will likes ai",
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-6)    "context": [{"content": "..."}, {"content": "..."}]
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-7)  },
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-8)  index=["memory", "context[*].content"]
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-9))

```


###  `adelete(namespace: tuple[str, ...], key: str) -> None` `async` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore.adelete "Permanent link")

Asynchronously delete an item.

Parameters:

  * **`namespace`**(`tuple[str, ...]`) – 

Hierarchical path for the item.

  * **`key`**(`str`) – 

Unique identifier within the namespace.




###  `alist_namespaces(*, prefix: Optional[NamespacePath] = None, suffix: Optional[NamespacePath] = None, max_depth: Optional[int] = None, limit: int = 100, offset: int = 0) -> list[tuple[str, ...]]` `async` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore.alist_namespaces "Permanent link")

List and filter namespaces in the store asynchronously.

Used to explore the organization of data, find specific collections, or navigate the namespace hierarchy.

Parameters:

  * **`prefix`**(`Optional[Tuple[str, ...]]` , default: `None` ) – 

Filter namespaces that start with this path.

  * **`suffix`**(`Optional[Tuple[str, ...]]` , default: `None` ) – 

Filter namespaces that end with this path.

  * **`max_depth`**(`Optional[int]` , default: `None` ) – 

Return namespaces up to this depth in the hierarchy. Namespaces deeper than this level will be truncated to this depth.

  * **`limit`**(`int` , default: `100` ) – 

Maximum number of namespaces to return (default 100).

  * **`offset`**(`int` , default: `0` ) – 

Number of namespaces to skip for pagination (default 0).




Returns:

  * `list[tuple[str, ...]]` – 

List[Tuple[str, ...]]: A list of namespace tuples that match the criteria.

  * `list[tuple[str, ...]]` – 

Each tuple represents a full namespace path up to `max_depth`.


Examples

Setting max_depth=3 with existing namespaces: 

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-1)# Given the following namespaces:
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-2)# ("a", "b", "c")
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-3)# ("a", "b", "d", "e")
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-4)# ("a", "b", "d", "i")
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-5)# ("a", "b", "f")
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-6)# ("a", "c", "f")
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-7)
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-8)await store.alist_namespaces(prefix=("a", "b"), max_depth=3)
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-9)# Returns: [("a", "b", "c"), ("a", "b", "d"), ("a", "b", "f")]

```


##  `ensure_embeddings(embed: Union[Embeddings, EmbeddingsFunc, AEmbeddingsFunc, str, None]) -> Embeddings` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.ensure_embeddings "Permanent link")

Ensure that an embedding function conforms to LangChain's Embeddings interface.

This function wraps arbitrary embedding functions to make them compatible with LangChain's Embeddings interface. It handles both synchronous and asynchronous functions.

Parameters:

  * **`embed`**(`Union[Embeddings, EmbeddingsFunc, AEmbeddingsFunc, str, None]`) – 

Either an existing Embeddings instance, or a function that converts text to embeddings. If the function is async, it will be used for both sync and async operations.




Returns:

  * `Embeddings` – 

An Embeddings instance that wraps the provided function(s).


Examples

Wrap a synchronous embedding function: 

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-1)defmy_embed_fn(texts):
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-2)  return [[0.1, 0.2] for _ in texts]
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-3)
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-4)embeddings = ensure_embeddings(my_embed_fn)
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-5)result = embeddings.embed_query("hello") # Returns [0.1, 0.2]

```


Wrap an asynchronous embedding function: 

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-1)async defmy_async_fn(texts):
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-2)  return [[0.1, 0.2] for _ in texts]
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-4)embeddings = ensure_embeddings(my_async_fn)
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-5)result = await embeddings.aembed_query("hello") # Returns [0.1, 0.2]

```


Initialize embeddings using a provider string: 

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-1)# Requires langchain>=0.3.9 and langgraph-checkpoint>=2.0.11
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-2)embeddings = ensure_embeddings("openai:text-embedding-3-small")
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-3)result = embeddings.embed_query("hello")

```


##  `get_text_at_path(obj: Any, path: Union[str, list[str]]) -> list[str]` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.get_text_at_path "Permanent link")

Extract text from an object using a path expression or pre-tokenized path.

Parameters:

  * **`obj`**(`Any`) – 

The object to extract text from

  * **`path`**(`Union[str, list[str]]`) – 

Either a path string or pre-tokenized path list.




Path types handled

  * Simple paths: "field1.field2"
  * Array indexing: "[0]", "[*]", "[-1]"
  * Wildcards: "*"
  * Multi-field selection: "{field1,field2}"
  * Nested paths in multi-field: "{field1,nested.field2}"



##  `tokenize_path(path: str) -> list[str]` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.tokenize_path "Permanent link")

Tokenize a path into components.

Types handled

  * Simple paths: "field1.field2"
  * Array indexing: "[0]", "[*]", "[-1]"
  * Wildcards: "*"
  * Multi-field selection: "{field1,field2}"



##  `AsyncPostgresStore` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.postgres.AsyncPostgresStore "Permanent link")

Bases: `AsyncBatchedBaseStore`, `BasePostgresStore[Conn]`

Asynchronous Postgres-backed store with optional vector search using pgvector.

Examples

Basic setup and usage: 

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-1)fromlanggraph.store.postgresimport AsyncPostgresStore
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-2)
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-3)conn_string = "postgresql://user:pass@localhost:5432/dbname"
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-4)
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-5)async with AsyncPostgresStore.from_conn_string(conn_string) as store:
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-6)  await store.setup() # Run migrations. Done once
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-7)
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-8)  # Store and retrieve data
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-9)  await store.aput(("users", "123"), "prefs", {"theme": "dark"})
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-10)  item = await store.aget(("users", "123"), "prefs")

```


Vector search using LangChain embeddings: 

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-1)fromlangchain.embeddingsimport init_embeddings
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-2)fromlanggraph.store.postgresimport AsyncPostgresStore
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-4)conn_string = "postgresql://user:pass@localhost:5432/dbname"
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-5)
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-6)async with AsyncPostgresStore.from_conn_string(
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-7)  conn_string,
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-8)  index={
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-9)    "dims": 1536,
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-10)    "embed": init_embeddings("openai:text-embedding-3-small"),
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-11)    "fields": ["text"] # specify which fields to embed. Default is the whole serialized value
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-12)  }
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-13)) as store:
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-14)  await store.setup() # Run migrations. Done once
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-15)
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-16)  # Store documents
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-17)  await store.aput(("docs",), "doc1", {"text": "Python tutorial"})
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-18)  await store.aput(("docs",), "doc2", {"text": "TypeScript guide"})
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-19)  await store.aput(("docs",), "doc3", {"text": "Other guide"}, index=False) # don't index
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-20)
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-21)  # Search by similarity
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-22)  results = await store.asearch(("docs",), "programming guides", limit=2)

```


Using connection pooling for better performance: 

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-1)fromlanggraph.store.postgresimport AsyncPostgresStore, PoolConfig
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-2)
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-3)conn_string = "postgresql://user:pass@localhost:5432/dbname"
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-4)
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-5)async with AsyncPostgresStore.from_conn_string(
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-6)  conn_string,
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-7)  pool_config=PoolConfig(
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-8)    min_size=5,
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-9)    max_size=20
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-10)  )
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-11)) as store:
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-12)  await store.setup() # Run migrations. Done once
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-13)  # Use store with connection pooling...

```


Warning

Make sure to: 1. Call `setup()` before first use to create necessary tables and indexes 2. Have the pgvector extension available to use vector search 3. Use Python 3.10+ for async functionality

Note

Semantic search is disabled by default. You can enable it by providing an `index` configuration when creating the store. Without this configuration, all `index` arguments passed to `put` or `aput` will have no effect.

###  `from_conn_string(conn_string: str, *, pipeline: bool = False, pool_config: Optional[PoolConfig] = None, index: Optional[PostgresIndexConfig] = None) -> AsyncIterator[AsyncPostgresStore]` `async` `classmethod` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.postgres.AsyncPostgresStore.from_conn_string "Permanent link")

Create a new AsyncPostgresStore instance from a connection string.

Parameters:

  * **`conn_string`**(`str`) – 

The Postgres connection info string.

  * **`pipeline`**(`bool` , default: `False` ) – 

Whether to use AsyncPipeline (only for single connections)

  * **`pool_config`**(`Optional[PoolConfig]` , default: `None` ) – 

Configuration for the connection pool. If provided, will create a connection pool and use it instead of a single connection. This overrides the `pipeline` argument.

  * **`index`**(`Optional[PostgresIndexConfig]` , default: `None` ) – 

The embedding config.




Returns:

  * **`AsyncPostgresStore`**(`AsyncIterator[AsyncPostgresStore]` ) – 

A new AsyncPostgresStore instance.




###  `setup() -> None` `async` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.postgres.AsyncPostgresStore.setup "Permanent link")

Set up the store database asynchronously.

This method creates the necessary tables in the Postgres database if they don't already exist and runs database migrations. It MUST be called directly by the user the first time the store is used.

##  `PostgresStore` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.postgres.PostgresStore "Permanent link")

Bases: `BaseStore`, `BasePostgresStore[Conn]`

Postgres-backed store with optional vector search using pgvector.

Examples

Basic setup and usage: 

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-1)fromlanggraph.store.postgresimport PostgresStore
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-2)frompsycopgimport Connection
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-3)
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-4)conn_string = "postgresql://user:pass@localhost:5432/dbname"
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-5)
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-6)# Using direct connection
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-7)with Connection.connect(conn_string) as conn:
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-8)  store = PostgresStore(conn)
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-9)  store.setup() # Run migrations. Done once
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-10)
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-11)  # Store and retrieve data
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-12)  store.put(("users", "123"), "prefs", {"theme": "dark"})
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-13)  item = store.get(("users", "123"), "prefs")

```


Or using the convenient from_conn_string helper: 

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-1)fromlanggraph.store.postgresimport PostgresStore
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-2)
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-3)conn_string = "postgresql://user:pass@localhost:5432/dbname"
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-5)with PostgresStore.from_conn_string(conn_string) as store:
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-6)  store.setup()
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-7)
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-8)  # Store and retrieve data
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-9)  store.put(("users", "123"), "prefs", {"theme": "dark"})
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-10)  item = store.get(("users", "123"), "prefs")

```


Vector search using LangChain embeddings: 

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-1)fromlangchain.embeddingsimport init_embeddings
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-2)fromlanggraph.store.postgresimport PostgresStore
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-3)
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-4)conn_string = "postgresql://user:pass@localhost:5432/dbname"
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-5)
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-6)with PostgresStore.from_conn_string(
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-7)  conn_string,
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-8)  index={
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-9)    "dims": 1536,
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-10)    "embed": init_embeddings("openai:text-embedding-3-small"),
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-11)    "fields": ["text"] # specify which fields to embed. Default is the whole serialized value
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-12)  }
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-13)) as store:
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-14)  store.setup() # Do this once to run migrations
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-15)
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-16)  # Store documents
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-17)  store.put(("docs",), "doc1", {"text": "Python tutorial"})
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-18)  store.put(("docs",), "doc2", {"text": "TypeScript guide"})
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-19)  store.put(("docs",), "doc2", {"text": "Other guide"}, index=False) # don't index
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-20)
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-21)  # Search by similarity
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-22)  results = store.search(("docs",), "programming guides", limit=2)

```


Note

Semantic search is disabled by default. You can enable it by providing an `index` configuration when creating the store. Without this configuration, all `index` arguments passed to `put` or `aput`will have no effect.

Warning

Make sure to call `setup()` before first use to create necessary tables and indexes. The pgvector extension must be available to use vector search.

###  `get(namespace: tuple[str, ...], key: str) -> Optional[Item]` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.postgres.PostgresStore.get "Permanent link")

Retrieve a single item.

Parameters:

  * **`namespace`**(`tuple[str, ...]`) – 

Hierarchical path for the item.

  * **`key`**(`str`) – 

Unique identifier within the namespace.




Returns:

  * `Optional[Item]` – 

The retrieved item or None if not found.




###  `search(namespace_prefix: tuple[str, ...], /, *, query: Optional[str] = None, filter: Optional[dict[str, Any]] = None, limit: int = 10, offset: int = 0) -> list[SearchItem]` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.postgres.PostgresStore.search "Permanent link")

Search for items within a namespace prefix.

Parameters:

  * **`namespace_prefix`**(`tuple[str, ...]`) – 

Hierarchical path prefix to search within.

  * **`query`**(`Optional[str]` , default: `None` ) – 

Optional query for natural language search.

  * **`filter`**(`Optional[dict[str, Any]]` , default: `None` ) – 

Key-value pairs to filter results.

  * **`limit`**(`int` , default: `10` ) – 

Maximum number of items to return.

  * **`offset`**(`int` , default: `0` ) – 

Number of items to skip before returning results.




Returns:

  * `list[SearchItem]` – 

List of items matching the search criteria.


Examples

Basic filtering: 

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-1)# Search for documents with specific metadata
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-2)results = store.search(
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-3)  ("docs",),
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-4)  filter={"type": "article", "status": "published"}
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-5))

```


Natural language search (requires vector store implementation): 

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-1)# Initialize store with embedding configuration
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-2)store = YourStore( # e.g., InMemoryStore, AsyncPostgresStore
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-3)  index={
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-4)    "dims": 1536, # embedding dimensions
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-5)    "embed": your_embedding_function, # function to create embeddings
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-6)    "fields": ["text"] # fields to embed. Defaults to ["$"]
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-7)  }
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-8))
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-10)# Search for semantically similar documents
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-11)results = store.search(
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-12)  ("docs",),
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-13)  query="machine learning applications in healthcare",
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-14)  filter={"type": "research_paper"},
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-15)  limit=5
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-16))

```


Note: Natural language search support depends on your store implementation and requires proper embedding configuration.

###  `put(namespace: tuple[str, ...], key: str, value: dict[str, Any], index: Optional[Union[Literal[False], list[str]]] = None) -> None` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.postgres.PostgresStore.put "Permanent link")

Store or update an item in the store.

Parameters:

  * **`namespace`**(`tuple[str, ...]`) – 

Hierarchical path for the item, represented as a tuple of strings. Example: ("documents", "user123")

  * **`key`**(`str`) – 

Unique identifier within the namespace. Together with namespace forms the complete path to the item.

  * **`value`**(`dict[str, Any]`) – 

Dictionary containing the item's data. Must contain string keys and JSON-serializable values.

  * **`index`**(`Optional[Union[Literal[False], list[str]]]` , default: `None` ) – 

Controls how the item's fields are indexed for search:

    * None (default): Use `fields` you configured when creating the store (if any) If you do not initialize the store with indexing capabilities, the `index` parameter will be ignored
    * False: Disable indexing for this item
    * list[str]: List of field paths to index, supporting:
      * Nested fields: "metadata.title"
      * Array access: "chapters[*].content" (each indexed separately)
      * Specific indices: "authors[0].name"


Note

Indexing support depends on your store implementation. If you do not initialize the store with indexing capabilities, the `index` parameter will be ignored.

Examples

Store item. Indexing depends on how you configure the store. 

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-1)store.put(("docs",), "report", {"memory": "Will likes ai"})

```


Do not index item for semantic search. Still accessible through get() and search() operations but won't have a vector representation. 

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-1)store.put(("docs",), "report", {"memory": "Will likes ai"}, index=False)

```


Index specific fields for search. 

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-1)store.put(("docs",), "report", {"memory": "Will likes ai"}, index=["memory"])

```


###  `delete(namespace: tuple[str, ...], key: str) -> None` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.postgres.PostgresStore.delete "Permanent link")

Delete an item.

Parameters:

  * **`namespace`**(`tuple[str, ...]`) – 

Hierarchical path for the item.

  * **`key`**(`str`) – 

Unique identifier within the namespace.




###  `list_namespaces(*, prefix: Optional[NamespacePath] = None, suffix: Optional[NamespacePath] = None, max_depth: Optional[int] = None, limit: int = 100, offset: int = 0) -> list[tuple[str, ...]]` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.postgres.PostgresStore.list_namespaces "Permanent link")

List and filter namespaces in the store.

Used to explore the organization of data, find specific collections, or navigate the namespace hierarchy.

Parameters:

  * **`prefix`**(`Optional[Tuple[str, ...]]` , default: `None` ) – 

Filter namespaces that start with this path.

  * **`suffix`**(`Optional[Tuple[str, ...]]` , default: `None` ) – 

Filter namespaces that end with this path.

  * **`max_depth`**(`Optional[int]` , default: `None` ) – 

Return namespaces up to this depth in the hierarchy. Namespaces deeper than this level will be truncated.

  * **`limit`**(`int` , default: `100` ) – 

Maximum number of namespaces to return (default 100).

  * **`offset`**(`int` , default: `0` ) – 

Number of namespaces to skip for pagination (default 0).




Returns:

  * `list[tuple[str, ...]]` – 

List[Tuple[str, ...]]: A list of namespace tuples that match the criteria.

  * `list[tuple[str, ...]]` – 

Each tuple represents a full namespace path up to `max_depth`.




???+ example "Examples": Setting max_depth=3. Given the namespaces: 

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-1)# Example if you have the following namespaces:
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-2)# ("a", "b", "c")
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-3)# ("a", "b", "d", "e")
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-4)# ("a", "b", "d", "i")
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-5)# ("a", "b", "f")
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-6)# ("a", "c", "f")
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-7)store.list_namespaces(prefix=("a", "b"), max_depth=3)
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-8)# [("a", "b", "c"), ("a", "b", "d"), ("a", "b", "f")]

```


###  `aget(namespace: tuple[str, ...], key: str) -> Optional[Item]` `async` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.postgres.PostgresStore.aget "Permanent link")

Asynchronously retrieve a single item.

Parameters:

  * **`namespace`**(`tuple[str, ...]`) – 

Hierarchical path for the item.

  * **`key`**(`str`) – 

Unique identifier within the namespace.




Returns:

  * `Optional[Item]` – 

The retrieved item or None if not found.




###  `asearch(namespace_prefix: tuple[str, ...], /, *, query: Optional[str] = None, filter: Optional[dict[str, Any]] = None, limit: int = 10, offset: int = 0) -> list[SearchItem]` `async` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.postgres.PostgresStore.asearch "Permanent link")

Asynchronously search for items within a namespace prefix.

Parameters:

  * **`namespace_prefix`**(`tuple[str, ...]`) – 

Hierarchical path prefix to search within.

  * **`query`**(`Optional[str]` , default: `None` ) – 

Optional query for natural language search.

  * **`filter`**(`Optional[dict[str, Any]]` , default: `None` ) – 

Key-value pairs to filter results.

  * **`limit`**(`int` , default: `10` ) – 

Maximum number of items to return.

  * **`offset`**(`int` , default: `0` ) – 

Number of items to skip before returning results.




Returns:

  * `list[SearchItem]` – 

List of items matching the search criteria.


Examples

Basic filtering: 

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-1)# Search for documents with specific metadata
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-2)results = await store.asearch(
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-3)  ("docs",),
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-4)  filter={"type": "article", "status": "published"}
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-5))

```


Natural language search (requires vector store implementation): 

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-1)# Initialize store with embedding configuration
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-2)store = YourStore( # e.g., InMemoryStore, AsyncPostgresStore
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-3)  index={
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-4)    "dims": 1536, # embedding dimensions
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-5)    "embed": your_embedding_function, # function to create embeddings
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-6)    "fields": ["text"] # fields to embed
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-7)  }
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-8))
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-10)# Search for semantically similar documents
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-11)results = await store.asearch(
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-12)  ("docs",),
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-13)  query="machine learning applications in healthcare",
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-14)  filter={"type": "research_paper"},
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-15)  limit=5
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-16))

```


Note: Natural language search support depends on your store implementation and requires proper embedding configuration.

###  `aput(namespace: tuple[str, ...], key: str, value: dict[str, Any], index: Optional[Union[Literal[False], list[str]]] = None) -> None` `async` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.postgres.PostgresStore.aput "Permanent link")

Asynchronously store or update an item in the store.

Parameters:

  * **`namespace`**(`tuple[str, ...]`) – 

Hierarchical path for the item, represented as a tuple of strings. Example: ("documents", "user123")

  * **`key`**(`str`) – 

Unique identifier within the namespace. Together with namespace forms the complete path to the item.

  * **`value`**(`dict[str, Any]`) – 

Dictionary containing the item's data. Must contain string keys and JSON-serializable values.

  * **`index`**(`Optional[Union[Literal[False], list[str]]]` , default: `None` ) – 

Controls how the item's fields are indexed for search:

    * None (default): Use `fields` you configured when creating the store (if any) If you do not initialize the store with indexing capabilities, the `index` parameter will be ignored
    * False: Disable indexing for this item
    * list[str]: List of field paths to index, supporting:
      * Nested fields: "metadata.title"
      * Array access: "chapters[*].content" (each indexed separately)
      * Specific indices: "authors[0].name"


Note

Indexing support depends on your store implementation. If you do not initialize the store with indexing capabilities, the `index` parameter will be ignored.

Examples

Store item. Indexing depends on how you configure the store. 

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-1)await store.aput(("docs",), "report", {"memory": "Will likes ai"})

```


Do not index item for semantic search. Still accessible through get() and search() operations but won't have a vector representation. 

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-1-1)await store.aput(("docs",), "report", {"memory": "Will likes ai"}, index=False)

```


Index specific fields for search (if store configured to index items): 

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-1)await store.aput(
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-2)  ("docs",),
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-3)  "report",
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-4)  {
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-5)    "memory": "Will likes ai",
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-6)    "context": [{"content": "..."}, {"content": "..."}]
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-7)  },
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-8)  index=["memory", "context[*].content"]
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-2-9))

```


###  `adelete(namespace: tuple[str, ...], key: str) -> None` `async` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.postgres.PostgresStore.adelete "Permanent link")

Asynchronously delete an item.

Parameters:

  * **`namespace`**(`tuple[str, ...]`) – 

Hierarchical path for the item.

  * **`key`**(`str`) – 

Unique identifier within the namespace.




###  `alist_namespaces(*, prefix: Optional[NamespacePath] = None, suffix: Optional[NamespacePath] = None, max_depth: Optional[int] = None, limit: int = 100, offset: int = 0) -> list[tuple[str, ...]]` `async` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.postgres.PostgresStore.alist_namespaces "Permanent link")

List and filter namespaces in the store asynchronously.

Used to explore the organization of data, find specific collections, or navigate the namespace hierarchy.

Parameters:

  * **`prefix`**(`Optional[Tuple[str, ...]]` , default: `None` ) – 

Filter namespaces that start with this path.

  * **`suffix`**(`Optional[Tuple[str, ...]]` , default: `None` ) – 

Filter namespaces that end with this path.

  * **`max_depth`**(`Optional[int]` , default: `None` ) – 

Return namespaces up to this depth in the hierarchy. Namespaces deeper than this level will be truncated to this depth.

  * **`limit`**(`int` , default: `100` ) – 

Maximum number of namespaces to return (default 100).

  * **`offset`**(`int` , default: `0` ) – 

Number of namespaces to skip for pagination (default 0).




Returns:

  * `list[tuple[str, ...]]` – 

List[Tuple[str, ...]]: A list of namespace tuples that match the criteria.

  * `list[tuple[str, ...]]` – 

Each tuple represents a full namespace path up to `max_depth`.


Examples

Setting max_depth=3 with existing namespaces: 

```
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-1)# Given the following namespaces:
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-2)# ("a", "b", "c")
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-3)# ("a", "b", "d", "e")
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-4)# ("a", "b", "d", "i")
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-5)# ("a", "b", "f")
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-6)# ("a", "c", "f")
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-7)
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-8)await store.alist_namespaces(prefix=("a", "b"), max_depth=3)
[](https://langchain-ai.github.io/langgraph/reference/store/#__codelineno-0-9)# Returns: [("a", "b", "c"), ("a", "b", "d"), ("a", "b", "f")]

```


###  `from_conn_string(conn_string: str, *, pipeline: bool = False, pool_config: Optional[PoolConfig] = None, index: Optional[PostgresIndexConfig] = None) -> Iterator[PostgresStore]` `classmethod` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.postgres.PostgresStore.from_conn_string "Permanent link")

Create a new PostgresStore instance from a connection string.

Parameters:

  * **`conn_string`**(`str`) – 

The Postgres connection info string.

  * **`pipeline`**(`bool` , default: `False` ) – 

whether to use Pipeline

  * **`pool_config`**(`Optional[PoolArgs]` , default: `None` ) – 

Configuration for the connection pool. If provided, will create a connection pool and use it instead of a single connection. This overrides the `pipeline` argument.

  * **`index`**(`Optional[PostgresIndexConfig]` , default: `None` ) – 

The index configuration for the store.




Returns:

  * **`PostgresStore`**(`Iterator[PostgresStore]` ) – 

A new PostgresStore instance.




###  `setup() -> None` [¶](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.postgres.PostgresStore.setup "Permanent link")

Set up the store database.

This method creates the necessary tables in the Postgres database if they don't already exist and runs database migrations. It MUST be called directly by the user the first time the store is used.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Checkpointing  ](https://langchain-ai.github.io/langgraph/reference/checkpoints/) [ Next  Prebuilt components  ](https://langchain-ai.github.io/langgraph/reference/prebuilt/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/reference/store/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
