---
url: https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#langgraph-cli)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

CLI 

[ ](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/?q= "Share")

Type to start searching

[ GitHub  ](https://github.com/langchain-ai/langgraphjs "Go to repository")

  * [ Home ](https://langchain-ai.github.io/langgraphjs/)
  * [ API reference ](https://langchain-ai.github.io/langgraphjs/reference/)
  * [ Versions ](https://langchain-ai.github.io/langgraphjs/versions/)



[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

[ GitHub  ](https://github.com/langchain-ai/langgraphjs "Go to repository")

  * [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  * [ API reference  ](https://langchain-ai.github.io/langgraphjs/reference/)

API reference 
    * LangGraph Platform  LangGraph Platform 
      * [ Server API  ](https://langchain-ai.github.io/langgraphjs/cloud/reference/api/api_ref/)
      * CLI  [ CLI  ](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/) Table of contents 
        * [ Installation  ](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#installation)
        * [ Configuration File  ](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#configuration-file)
          * [ Examples  ](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#examples)
            * [ Basic Configuration  ](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#basic-configuration)
            * [ Adding semantic search to the store  ](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#adding-semantic-search-to-the-store)
            * [ Semantic search with a custom embedding function  ](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#semantic-search-with-a-custom-embedding-function)
            * [ Adding custom authentication  ](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#adding-custom-authentication)
            * [ Basic Configuration  ](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#basic-configuration_1)
        * [ Commands  ](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#commands)
          * [ dev  ](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#dev)
          * [ build  ](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#build)
          * [ up  ](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#up)
          * [ dockerfile  ](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#dockerfile)
      * [ SDK (Python)  ](https://langchain-ai.github.io/langgraphjs/cloud/reference/sdk/python_sdk_ref/)
      * [ SDK (JS/TS)  ](https://langchain-ai.github.io/langgraphjs/cloud/reference/sdk/js_ts_sdk_ref.md)
      * [ RemoteGraph  ](https://langchain-ai.github.io/langgraphjs/reference/remote_graph.md)
      * [ Environment variables  ](https://langchain-ai.github.io/langgraphjs/cloud/reference/env_var/)
  * [ Versions  ](https://langchain-ai.github.io/langgraphjs/versions/)



Table of contents 

  * [ Installation  ](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#installation)
  * [ Configuration File  ](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#configuration-file)
    * [ Examples  ](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#examples)
      * [ Basic Configuration  ](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#basic-configuration)
      * [ Adding semantic search to the store  ](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#adding-semantic-search-to-the-store)
      * [ Semantic search with a custom embedding function  ](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#semantic-search-with-a-custom-embedding-function)
      * [ Adding custom authentication  ](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#adding-custom-authentication)
      * [ Basic Configuration  ](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#basic-configuration_1)
  * [ Commands  ](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#commands)
    * [ dev  ](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#dev)
    * [ build  ](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#build)
    * [ up  ](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#up)
    * [ dockerfile  ](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#dockerfile)



  1. [ API reference  ](https://langchain-ai.github.io/langgraphjs/reference/)
  2. [ LangGraph Platform  ](https://langchain-ai.github.io/langgraphjs/cloud/reference/api/api_ref/)



# LangGraph CLI[¶](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#langgraph-cli "Permanent link")

The LangGraph command line interface includes commands to build and run a LangGraph Cloud API server locally in [Docker](https://www.docker.com/). For development and testing, you can use the CLI to deploy a local API server as an alternative to the [Studio desktop app](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_studio/).

## Installation[¶](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#installation "Permanent link")

  1. Ensure that Docker is installed (e.g. `docker --version`).
  2. Install the CLI package:

[Python](#__tabbed_1_1)[JS](#__tabbed_1_2)

```
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-0-1)pipinstalllanggraph-cli
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-0-2)
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-0-3)# Install via Homebrew
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-0-4)brewinstalllanggraph-cli

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-1-1)npx@langchain/langgraph-cli
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-1-2)
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-1-3)# Install globally, will be available as `langgraphjs`
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-1-4)npminstall-g@langchain/langgraph-cli

```


  3. Run the command `langgraph --help` or `npx @langchain/langgraph-cli --help` to confirm that the CLI is working correctly.




## Configuration File[¶](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#configuration-file "Permanent link")

The LangGraph CLI requires a JSON configuration file with the following keys:

Note

The LangGraph CLI defaults to using the configuration file **langgraph.json** in the current directory. 

[Python](#__tabbed_2_1)[JS](#__tabbed_2_2)

Key | Description  
---|---  
`dependencies` | **Required**. Array of dependencies for LangGraph Cloud API server. Dependencies can be one of the following: (1) `"."`, which will look for local Python packages, (2) `pyproject.toml`, `setup.py` or `requirements.txt` in the app directory `"./local_package"`, or (3) a package name.  
`graphs` | **Required**. Mapping from graph ID to path where the compiled graph or a function that makes a graph is defined. Example: 

  * `./your_package/your_file.py:variable`, where `variable` is an instance of `langgraph.graph.state.CompiledStateGraph`
  * `./your_package/your_file.py:make_graph`, where `make_graph` is a function that takes a config dictionary (`langchain_core.runnables.RunnableConfig`) and creates an instance of `langgraph.graph.state.StateGraph` / `langgraph.graph.state.CompiledStateGraph`.

  
`auth` | _(Added in v0.0.11)_ Auth configuration containing the path to your authentication handler. Example: `./your_package/auth.py:auth`, where `auth` is an instance of `langgraph_sdk.Auth`. See [authentication guide](https://langchain-ai.github.io/langgraphjs/cloud/concepts/auth.md) for details.  
`env` | Path to `.env` file or a mapping from environment variable to its value.  
`store` | Configuration for adding semantic search to the BaseStore. Contains the following fields: 

  * `index`: Configuration for semantic search indexing with fields:
    * `embed`: Embedding provider (e.g., "openai:text-embedding-3-small") or path to custom embedding function
    * `dims`: Dimension size of the embedding model. Used to initialize the vector table.
    * `fields` (optional): List of fields to index. Defaults to `["$"]`, which means to index entire documents. Can be specific fields like `["text", "summary", "some.value"]`

  
`python_version` | `3.11` or `3.12`. Defaults to `3.11`.  
`node_version` | Specify `node_version: 20` to use LangGraph.js.  
`pip_config_file` | Path to `pip` config file.  
`dockerfile_lines` | Array of additional lines to add to Dockerfile following the import from parent image.  
  
Key | Description  
---|---  
`graphs` | **Required**. Mapping from graph ID to path where the compiled graph or a function that makes a graph is defined. Example: 

  * `./src/graph.ts:variable`, where `variable` is an instance of `CompiledStateGraph`
  * `./src/graph.ts:makeGraph`, where `makeGraph` is a function that takes a config dictionary (`LangGraphRunnableConfig`) and creates an instance of `StateGraph` / `CompiledStateGraph`.

  
`env` | Path to `.env` file or a mapping from environment variable to its value.  
`store` | Configuration for adding semantic search to the BaseStore. Contains the following fields: 

  * `index`: Configuration for semantic search indexing with fields:
    * `embed`: Embedding provider (e.g., "openai:text-embedding-3-small") or path to custom embedding function
    * `dims`: Dimension size of the embedding model. Used to initialize the vector table.
    * `fields` (optional): List of fields to index. Defaults to `["$"]`, which means to index entire documents. Can be specific fields like `["text", "summary", "some.value"]`

  
`node_version` | Specify `node_version: 20` to use LangGraph.js.  
`dockerfile_lines` | Array of additional lines to add to Dockerfile following the import from parent image.  
  
### Examples[¶](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#examples "Permanent link")

[Python](#__tabbed_3_1)[JS](#__tabbed_3_2)

#### Basic Configuration[¶](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#basic-configuration "Permanent link")

```
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-2-1){
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-2-2)"dependencies":["."],
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-2-3)"graphs":{
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-2-4)"chat":"./chat/graph.py:graph"
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-2-5)}
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-2-6)}

```


#### Adding semantic search to the store[¶](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#adding-semantic-search-to-the-store "Permanent link")

All deployments come with a DB-backed BaseStore. Adding an "index" configuration to your `langgraph.json` will enable [semantic search](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/) within the BaseStore of your deployment.

The `fields` configuration determines which parts of your documents to embed:

  * If omitted or set to `["$"]`, the entire document will be embedded
  * To embed specific fields, use JSON path notation: `["metadata.title", "content.text"]`
  * Documents missing specified fields will still be stored but won't have embeddings for those fields
  * You can still override which fields to embed on a specific item at `put` time using the `index` parameter



```
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-3-1){
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-3-2)"dependencies":["."],
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-3-3)"graphs":{
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-3-4)"memory_agent":"./agent/graph.py:graph"
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-3-5)},
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-3-6)"store":{
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-3-7)"index":{
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-3-8)"embed":"openai:text-embedding-3-small",
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-3-9)"dims":1536,
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-3-10)"fields":["$"]
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-3-11)}
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-3-12)}
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-3-13)}

```


Common model dimensions

  * `openai:text-embedding-3-large`: 3072 
  * `openai:text-embedding-3-small`: 1536 
  * `openai:text-embedding-ada-002`: 1536 
  * `cohere:embed-english-v3.0`: 1024 
  * `cohere:embed-english-light-v3.0`: 384 
  * `cohere:embed-multilingual-v3.0`: 1024 
  * `cohere:embed-multilingual-light-v3.0`: 384



#### Semantic search with a custom embedding function[¶](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#semantic-search-with-a-custom-embedding-function "Permanent link")

If you want to use semantic search with a custom embedding function, you can pass a path to a custom embedding function:

```
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-4-1){
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-4-2)"dependencies":["."],
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-4-3)"graphs":{
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-4-4)"memory_agent":"./agent/graph.py:graph"
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-4-5)},
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-4-6)"store":{
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-4-7)"index":{
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-4-8)"embed":"./embeddings.py:embed_texts",
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-4-9)"dims":768,
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-4-10)"fields":["text","summary"]
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-4-11)}
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-4-12)}
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-4-13)}

```


The `embed` field in store configuration can reference a custom function that takes a list of strings and returns a list of embeddings. Example implementation:

```
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-5-1)# embeddings.py
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-5-2)defembed_texts(texts: list[str]) -> list[list[float]]:
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-5-3)"""Custom embedding function for semantic search."""
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-5-4)  # Implementation using your preferred embedding model
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-5-5)  return [[0.1, 0.2, ...] for _ in texts] # dims-dimensional vectors

```


#### Adding custom authentication[¶](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#adding-custom-authentication "Permanent link")

```
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-6-1){
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-6-2)"dependencies":["."],
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-6-3)"graphs":{
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-6-4)"chat":"./chat/graph.py:graph"
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-6-5)},
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-6-6)"auth":{
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-6-7)"path":"./auth.py:auth",
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-6-8)"openapi":{
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-6-9)"securitySchemes":{
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-6-10)"apiKeyAuth":{
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-6-11)"type":"apiKey",
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-6-12)"in":"header",
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-6-13)"name":"X-API-Key"
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-6-14)}
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-6-15)},
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-6-16)"security":[{"apiKeyAuth":[]}]
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-6-17)},
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-6-18)"disable_studio_auth":false
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-6-19)}
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-6-20)}

```


See the [authentication conceptual guide](https://langchain-ai.github.io/langgraphjs/cloud/concepts/auth.md) for details, and the [setting up custom authentication](https://langchain-ai.github.io/langgraphjs/cloud/tutorials/auth/getting_started.md) guide for a practical walk through of the process.

#### Basic Configuration[¶](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#basic-configuration_1 "Permanent link")

```
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-7-1){
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-7-2)"graphs":{
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-7-3)"chat":"./src/graph.ts:graph"
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-7-4)}
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-7-5)}

```


## Commands[¶](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#commands "Permanent link")

**Usage**

[Python](#__tabbed_4_1)[JS](#__tabbed_4_2)

The base command for the LangGraph CLI is `langgraph`.

```
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-8-1)langgraph [OPTIONS] COMMAND [ARGS]

```


The base command for the LangGraph.js CLI is `langgraphjs`. 

```
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-9-1)npx @langchain/langgraph-cli [OPTIONS] COMMAND [ARGS]

```


We recommend using `npx` to always use the latest version of the CLI.

### `dev`[¶](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#dev "Permanent link")

[Python](#__tabbed_5_1)[JS](#__tabbed_5_2)

Run LangGraph API server in development mode with hot reloading and debugging capabilities. This lightweight server requires no Docker installation and is suitable for development and testing. State is persisted to a local directory.

Note

Currently, the CLI only supports Python >= 3.11.

**Installation**

This command requires the "inmem" extra to be installed:

```
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-10-1)pipinstall-U"langgraph-cli[inmem]"

```


**Usage**

```
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-11-1)langgraph dev [OPTIONS]

```


**Options**

Option | Default | Description  
---|---|---  
`-c, --config FILE` | `langgraph.json` | Path to configuration file declaring dependencies, graphs and environment variables  
`--host TEXT` | `127.0.0.1` | Host to bind the server to  
`--port INTEGER` | `2024` | Port to bind the server to  
`--no-reload` | Disable auto-reload  
`--n-jobs-per-worker INTEGER` | Number of jobs per worker. Default is 10  
`--debug-port INTEGER` | Port for debugger to listen on  
`--help` | Display command documentation  
  
Run LangGraph API server in development mode with hot reloading capabilities. This lightweight server requires no Docker installation and is suitable for development and testing. State is persisted to a local directory.

**Usage**

```
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-12-1)npx @langchain/langgraph-cli dev [OPTIONS]

```


**Options**

Option | Default | Description  
---|---|---  
`-c, --config FILE` | `langgraph.json` | Path to configuration file declaring dependencies, graphs and environment variables  
`--host TEXT` | `127.0.0.1` | Host to bind the server to  
`--port INTEGER` | `2024` | Port to bind the server to  
`--no-reload` | Disable auto-reload  
`--n-jobs-per-worker INTEGER` | Number of jobs per worker. Default is 10  
`--debug-port INTEGER` | Port for debugger to listen on  
`--help` | Display command documentation  
  
### `build`[¶](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#build "Permanent link")

[Python](#__tabbed_6_1)[JS](#__tabbed_6_2)

Build LangGraph Cloud API server Docker image.

**Usage**

```
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-13-1)langgraph build [OPTIONS]

```


**Options**

Option | Default | Description  
---|---|---  
`--platform TEXT` | Target platform(s) to build the Docker image for. Example: `langgraph build --platform linux/amd64,linux/arm64`  
`-t, --tag TEXT` | **Required**. Tag for the Docker image. Example: `langgraph build -t my-image`  
`--pull / --no-pull` | `--pull` | Build with latest remote Docker image. Use `--no-pull` for running the LangGraph Cloud API server with locally built images.  
`-c, --config FILE` | `langgraph.json` | Path to configuration file declaring dependencies, graphs and environment variables.  
`--help` | Display command documentation.  
  
Build LangGraph Cloud API server Docker image.

**Usage**

```
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-14-1)npx @langchain/langgraph-cli build [OPTIONS]

```


**Options**

Option | Default | Description  
---|---|---  
`--platform TEXT` | Target platform(s) to build the Docker image for. Example: `langgraph build --platform linux/amd64,linux/arm64`  
`-t, --tag TEXT` | **Required**. Tag for the Docker image. Example: `langgraph build -t my-image`  
`--no-pull` | Use locally built images. Defaults to `false` to build with latest remote Docker image.  
`-c, --config FILE` | `langgraph.json` | Path to configuration file declaring dependencies, graphs and environment variables.  
`--help` | Display command documentation.  
  
### `up`[¶](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#up "Permanent link")

[Python](#__tabbed_7_1)[JS](#__tabbed_7_2)

Start LangGraph API server. For local testing, requires a LangSmith API key with access to LangGraph Cloud closed beta. Requires a license key for production use.

**Usage**

```
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-15-1)langgraph up [OPTIONS]

```


**Options**

Option | Default | Description  
---|---|---  
`--wait` | Wait for services to start before returning. Implies --detach  
`--postgres-uri TEXT` | Local database | Postgres URI to use for the database.  
`--watch` | Restart on file changes  
`--debugger-base-url TEXT` | `http://127.0.0.1:[PORT]` | URL used by the debugger to access LangGraph API.  
`--debugger-port INTEGER` | Pull the debugger image locally and serve the UI on specified port  
`--verbose` | Show more output from the server logs.  
`-c, --config FILE` | `langgraph.json` | Path to configuration file declaring dependencies, graphs and environment variables.  
`-d, --docker-compose FILE` | Path to docker-compose.yml file with additional services to launch.  
`-p, --port INTEGER` | `8123` | Port to expose. Example: `langgraph up --port 8000`  
`--pull / --no-pull` | `pull` | Pull latest images. Use `--no-pull` for running the server with locally-built images. Example: `langgraph up --no-pull`  
`--recreate / --no-recreate` | `no-recreate` | Recreate containers even if their configuration and image haven't changed  
`--help` | Display command documentation.  
  
Start LangGraph API server. For local testing, requires a LangSmith API key with access to LangGraph Cloud closed beta. Requires a license key for production use.

**Usage**

```
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-16-1)npx @langchain/langgraph-cli up [OPTIONS]

```


**Options**

Option | Default | Description  
---|---|---  
`--wait` | Wait for services to start before returning. Implies --detach  
`--postgres-uri TEXT` | Local database | Postgres URI to use for the database.  
`--watch` | Restart on file changes  
`-c, --config FILE` | `langgraph.json` | Path to configuration file declaring dependencies, graphs and environment variables.  
`-d, --docker-compose FILE` | Path to docker-compose.yml file with additional services to launch.  
`-p, --port INTEGER` | `8123` | Port to expose. Example: `langgraph up --port 8000`  
`--no-pull` | Use locally built images. Defaults to `false` to build with latest remote Docker image.  
`--recreate` | Recreate containers even if their configuration and image haven't changed  
`--help` | Display command documentation.  
  
### `dockerfile`[¶](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#dockerfile "Permanent link")

[Python](#__tabbed_8_1)[JS](#__tabbed_8_2)

Generate a Dockerfile for building a LangGraph Cloud API server Docker image.

**Usage**

```
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-17-1)langgraph dockerfile [OPTIONS] SAVE_PATH

```


**Options**

Option | Default | Description  
---|---|---  
`-c, --config FILE` | `langgraph.json` | Path to the [configuration file](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#configuration-file) declaring dependencies, graphs and environment variables.  
`--help` | Show this message and exit.  
  
Example:

```
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-18-1)langgraphdockerfile-clanggraph.jsonDockerfile

```


This generates a Dockerfile that looks similar to:

```
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-19-1)FROMlangchain/langgraph-api:3.11
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-19-2)
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-19-3)ADD./pipconf.txt/pipconfig.txt
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-19-4)
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-19-5)RUNPIP_CONFIG_FILE=/pipconfig.txtPYTHONDONTWRITEBYTECODE=1pipinstall--no-cache-dir-c/api/constraints.txtlangchain_communitylangchain_anthropiclangchain_openaiwikipediascikit-learn
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-19-6)
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-19-7)ADD./graphs/deps/__outer_graphs/src
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-19-8)RUNset-ex&&\
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-19-9)forlinein'[project]'\
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-19-10)'name = "graphs"'\
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-19-11)'version = "0.1"'\
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-19-12)'[tool.setuptools.package-data]'\
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-19-13)'"*" = ["**/*"]';do\
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-19-14)echo"$line">>/deps/__outer_graphs/pyproject.toml;\
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-19-15)done
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-19-16)
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-19-17)RUNPIP_CONFIG_FILE=/pipconfig.txtPYTHONDONTWRITEBYTECODE=1pipinstall--no-cache-dir-c/api/constraints.txt-e/deps/*
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-19-18)
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-19-19)ENVLANGSERVE_GRAPHS='{"agent": "/deps/__outer_graphs/src/agent.py:graph", "storm": "/deps/__outer_graphs/src/storm.py:graph"}'

```


Updating your langgraph.json file

The `langgraph dockerfile` command translates all the configuration in your `langgraph.json` file into Dockerfile commands. When using this command, you will have to re-run it whenever you update your `langgraph.json` file. Otherwise, your changes will not be reflected when you build or run the dockerfile.

Generate a Dockerfile for building a LangGraph Cloud API server Docker image.

**Usage**

```
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-20-1)npx @langchain/langgraph-cli dockerfile [OPTIONS] SAVE_PATH

```


**Options**

Option | Default | Description  
---|---|---  
`-c, --config FILE` | `langgraph.json` | Path to the [configuration file](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#configuration-file) declaring dependencies, graphs and environment variables.  
`--help` | Show this message and exit.  
  
Example:

```
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-21-1)npx@langchain/langgraph-clidockerfile-clanggraph.jsonDockerfile

```


This generates a Dockerfile that looks similar to:

```
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-22-1)FROMlangchain/langgraphjs-api:20
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-22-2)
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-22-3)ADD./deps/agent
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-22-4)
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-22-5)RUNcd/deps/agent&&yarninstall
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-22-6)
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-22-7)ENVLANGSERVE_GRAPHS='{"agent":"./src/react_agent/graph.ts:graph"}'
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-22-8)
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-22-9)WORKDIR/deps/agent
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-22-10)
[](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__codelineno-22-11)RUN(test!-f/api/langgraph_api/js/build.mts&&echo"Prebuild script not found, skipping")||tsx/api/langgraph_api/js/build.mts

```


Updating your langgraph.json file

The `npx @langchain/langgraph-cli dockerfile` command translates all the configuration in your `langgraph.json` file into Dockerfile commands. When using this command, you will have to re-run it whenever you update your `langgraph.json` file. Otherwise, your changes will not be reflected when you build or run the dockerfile.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  Server API  ](https://langchain-ai.github.io/langgraphjs/cloud/reference/api/api_ref/) [ Next  SDK (Python)  ](https://langchain-ai.github.io/langgraphjs/cloud/reference/sdk/python_sdk_ref/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/cloud/reference/cli/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
