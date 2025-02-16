---
url: https://langchain-ai.github.io/langgraph/cloud/reference/api/api_ref.html
title: Untitled
date_crawled: 
---

Open Menu

Open Search(Keyboard Shortcut)`⌘k`

  * Collapse Assistants

[Assistants](/langgraph/cloud/reference/api/api_ref.html#tag/assistants)

    * [Create Assistant HTTP Method: POST](/langgraph/cloud/reference/api/api_ref.html#tag/assistants/POST/assistants)

    * [Search Assistants HTTP Method: POST](/langgraph/cloud/reference/api/api_ref.html#tag/assistants/POST/assistants/search)

    * [Get Assistant HTTP Method: GET](/langgraph/cloud/reference/api/api_ref.html#tag/assistants/GET/assistants/{assistant_id})

    * [Delete Assistant HTTP Method: DEL](/langgraph/cloud/reference/api/api_ref.html#tag/assistants/DELETE/assistants/{assistant_id})

    * [Patch Assistant HTTP Method: PATCH](/langgraph/cloud/reference/api/api_ref.html#tag/assistants/PATCH/assistants/{assistant_id})

    * [Get Assistant Graph HTTP Method: GET](/langgraph/cloud/reference/api/api_ref.html#tag/assistants/GET/assistants/{assistant_id}/graph)

    * [Get Assistant Subgraphs HTTP Method: GET](/langgraph/cloud/reference/api/api_ref.html#tag/assistants/GET/assistants/{assistant_id}/subgraphs)

    * [Get Assistant Subgraphs by Namespace HTTP Method: GET](/langgraph/cloud/reference/api/api_ref.html#tag/assistants/GET/assistants/{assistant_id}/subgraphs/{namespace})

    * [Get Assistant Schemas HTTP Method: GET](/langgraph/cloud/reference/api/api_ref.html#tag/assistants/GET/assistants/{assistant_id}/schemas)

    * [Get Assistant Versions HTTP Method: POST](/langgraph/cloud/reference/api/api_ref.html#tag/assistants/POST/assistants/{assistant_id}/versions)

    * [Set Latest Assistant Version HTTP Method: POST](/langgraph/cloud/reference/api/api_ref.html#tag/assistants/POST/assistants/{assistant_id}/latest)

  * Expand Threads

[Threads](/langgraph/cloud/reference/api/api_ref.html#tag/threads)

  * Expand Thread Runs

[Thread Runs](/langgraph/cloud/reference/api/api_ref.html#tag/thread-runs)

  * Expand Stateless Runs

[Stateless Runs](/langgraph/cloud/reference/api/api_ref.html#tag/stateless-runs)

  * Expand Crons (Enterprise-only)

[Crons (Enterprise-only)](/langgraph/cloud/reference/api/api_ref.html#tag/crons-enterprise-only)

  * Expand Store

[Store](/langgraph/cloud/reference/api/api_ref.html#tag/store)

  * Expand Models

[Models](/langgraph/cloud/reference/api/api_ref.html#models)




[ Open API Client ](https://client.scalar.com/?url=https%3A%2F%2Flangchain-ai.github.io%2Flanggraph%2Fcloud%2Freference%2Fapi%2Fopenapi.json&integration=html&utm_source=api-reference&utm_medium=button&utm_campaign=sidebar)

[ Powered by Scalar ](https://www.scalar.com)

v0.1.0

OAS 3.1.0

# LangGraph Platform

[ Download OpenAPI Document ](./openapi.json)

Server 

Server: https://langchain-ai.github.io 

Client Libraries

ShellRubyNode.jsPHPPythonSelect Client LibraryLibcurlHttpClientRestSharpclj-httpHttpNewRequestHTTP/1.1AsyncHttpjava.net.httpOkHttpUnirestFetchAxiosofetchjQueryXHROkHttpFetchAxiosofetchundiciNSURLSessionCohttpcURLGuzzleInvoke-WebRequestInvoke-RestMethodhttp.clientRequestshttrnet::httpCurlWgetHTTPieNSURLSession More 

Curl Shell

## Assistants​#Copy link to "Assistants"

An assistant is a configured instance of a graph.

Assistants Endpoints 

  * [POST/assistants](#tag/assistants/POST/assistants)
  * [POST/assistants/search](#tag/assistants/POST/assistants/search)
  * [GET/assistants/{assistant_id}](#tag/assistants/GET/assistants/{assistant_id})
  * [DELETE/assistants/{assistant_id}](#tag/assistants/DELETE/assistants/{assistant_id})
  * [PATCH/assistants/{assistant_id}](#tag/assistants/PATCH/assistants/{assistant_id})
  * [GET/assistants/{assistant_id}/graph](#tag/assistants/GET/assistants/{assistant_id}/graph)
  * [GET/assistants/{assistant_id}/subgraphs](#tag/assistants/GET/assistants/{assistant_id}/subgraphs)
  * [GET/assistants/{assistant_id}/subgraphs/{namespace}](#tag/assistants/GET/assistants/{assistant_id}/subgraphs/{namespace})
  * [GET/assistants/{assistant_id}/schemas](#tag/assistants/GET/assistants/{assistant_id}/schemas)
  * [POST/assistants/{assistant_id}/versions](#tag/assistants/POST/assistants/{assistant_id}/versions)
  * [POST/assistants/{assistant_id}/latest](#tag/assistants/POST/assistants/{assistant_id}/latest)



### Create Assistant​#Copy link to "Create Assistant"

Create an assistant.

An initial version of the assistant will be created and the assistant is set to that version. To change versions, use the `POST /assistants/{assistant_id}/latest` endpoint.

Body

application/json

Payload for creating an assistant.

Hide AssistantCreate

assistant_id

string uuid

The ID of the assistant. If not provided, a random UUID will be generated.

graph_id

string 

required 

The ID of the graph the assistant should use. The graph ID is normally set in your langgraph.json configuration.

config

object 

Configuration to use for the graph. Useful when graph is configurable and you want to create different assistants based on different configurations.

metadata

object 

Metadata to add to assistant.

if_exists

string enum

default: 

raise

How to handle duplicate creation. Must be either 'raise' (raise error if duplicate), or 'do_nothing' (return existing assistant).

  * raise
  * do_nothing



name

string 

The name of the assistant. Defaults to 'Untitled'.

Responses

  * Expand200Success

application/json

  * Expand404Not Found

application/json

  * Expand409Conflict

application/json

  * Expand422Validation Error

application/json




POST/assistants

Selected HTTP client: Shell CurlLibcurlHttpClientRestSharpclj-httpHttpNewRequestHTTP/1.1AsyncHttpjava.net.httpOkHttpUnirestFetchAxiosofetchjQueryXHROkHttpFetchAxiosofetchundiciNSURLSessionCohttpcURLGuzzleInvoke-WebRequestInvoke-RestMethodhttp.clientRequestshttrnet::httpCurlWgetHTTPieNSURLSession

Copy content

```
curl https://langchain-ai.github.io/assistants \
 --request POST \
 --header 'Content-Type: application/json' \
 --data '{
 "assistant_id": "",
 "graph_id": "",
 "config": {},
 "metadata": {},
 "if_exists": "raise",
 "name": ""
}'

```


Test Request(post /assistants)

200404409422

Show Schema 

Copy content

```
{
 "assistant_id": "123e4567-e89b-12d3-a456-426614174000",
 "graph_id": "…",
 "config": {
  "tags": [
   "…"
  ],
  "recursion_limit": 1,
  "configurable": {}
 },
 "created_at": "2025-02-15T23:43:15.654Z",
 "updated_at": "2025-02-15T23:43:15.654Z",
 "metadata": {},
 "version": 1,
 "name": "…"
}
```


Success

### Search Assistants​#Copy link to "Search Assistants"

Search for assistants.

This endpoint also functions as the endpoint to list all assistants.

Body

application/json

Payload for listing assistants.

Hide AssistantSearchRequest

metadata

object 

Metadata to filter by. Exact match filter for each KV pair.

graph_id

string 

The ID of the graph to filter by. The graph ID is normally set in your langgraph.json configuration.

limit

integer 

min: 

1

max: 

1000

default: 

10

The maximum number of results to return.

offset

integer 

min: 

0

default: 

0

The number of results to skip.

Responses

  * Expand200Success

application/json

  * Expand404Not Found

application/json

  * Expand422Validation Error

application/json




POST/assistants/search

Selected HTTP client: Shell CurlLibcurlHttpClientRestSharpclj-httpHttpNewRequestHTTP/1.1AsyncHttpjava.net.httpOkHttpUnirestFetchAxiosofetchjQueryXHROkHttpFetchAxiosofetchundiciNSURLSessionCohttpcURLGuzzleInvoke-WebRequestInvoke-RestMethodhttp.clientRequestshttrnet::httpCurlWgetHTTPieNSURLSession

Copy content

```
curl https://langchain-ai.github.io/assistants/search \
 --request POST \
 --header 'Content-Type: application/json' \
 --data '{
 "metadata": {},
 "graph_id": "",
 "limit": 10,
 "offset": 0
}'

```


Test Request(post /assistants/search)

200404422

Show Schema 

Copy content

```
[
 {
  "assistant_id": "123e4567-e89b-12d3-a456-426614174000",
  "graph_id": "…",
  "config": {
   "tags": [
    "…"
   ],
   "recursion_limit": 1,
   "configurable": {}
  },
  "created_at": "2025-02-15T23:43:15.654Z",
  "updated_at": "2025-02-15T23:43:15.654Z",
  "metadata": {},
  "version": 1,
  "name": "…"
 }
]
```


Success

### Get Assistant​#Copy link to "Get Assistant"

Get an assistant by ID.

Path Parameters

  * assistant_id

string uuid

required 

The ID of the assistant.




Responses

  * Expand200Success

application/json

  * Expand404Not Found

application/json




GET/assistants/_{assistant_id}_

Selected HTTP client: Shell CurlLibcurlHttpClientRestSharpclj-httpHttpNewRequestHTTP/1.1AsyncHttpjava.net.httpOkHttpUnirestFetchAxiosofetchjQueryXHROkHttpFetchAxiosofetchundiciNSURLSessionCohttpcURLGuzzleInvoke-WebRequestInvoke-RestMethodhttp.clientRequestshttrnet::httpCurlWgetHTTPieNSURLSession

Copy content

```
curl 'https://langchain-ai.github.io/assistants/{assistant_id}'

```


Test Request(get /assistants/{assistant_id})

200404

Show Schema 

Copy content

```
{
 "assistant_id": "123e4567-e89b-12d3-a456-426614174000",
 "graph_id": "…",
 "config": {
  "tags": [
   "…"
  ],
  "recursion_limit": 1,
  "configurable": {}
 },
 "created_at": "2025-02-15T23:43:15.654Z",
 "updated_at": "2025-02-15T23:43:15.654Z",
 "metadata": {},
 "version": 1,
 "name": "…"
}
```


Success

### Delete Assistant​#Copy link to "Delete Assistant"

Delete an assistant by ID.

All versions of the assistant will be deleted as well.

Path Parameters

  * assistant_id

string uuid

required 

The ID of the assistant.




Responses

  * Expand200Success

application/json

  * Expand404Not Found

application/json

  * Expand422Validation Error

application/json




DELETE/assistants/_{assistant_id}_

Selected HTTP client: Shell CurlLibcurlHttpClientRestSharpclj-httpHttpNewRequestHTTP/1.1AsyncHttpjava.net.httpOkHttpUnirestFetchAxiosofetchjQueryXHROkHttpFetchAxiosofetchundiciNSURLSessionCohttpcURLGuzzleInvoke-WebRequestInvoke-RestMethodhttp.clientRequestshttrnet::httpCurlWgetHTTPieNSURLSession

Copy content

```
curl 'https://langchain-ai.github.io/assistants/{assistant_id}' \
 --request DELETE

```


Test Request(delete /assistants/{assistant_id})

200404422

Show Schema 

```
null
```


Success

### Patch Assistant​#Copy link to "Patch Assistant"

Update an assistant.

Path Parameters

  * assistant_id

string uuid

required 

The ID of the assistant.




Body

application/json

Payload for updating an assistant.

Hide AssistantPatch

graph_id

string 

The ID of the graph the assistant should use. The graph ID is normally set in your langgraph.json configuration. If not provided, assistant will keep pointing to same graph.

config

object 

Configuration to use for the graph. Useful when graph is configurable and you want to update the assistant's configuration.

metadata

object 

Metadata to merge with existing assistant metadata.

name

string 

The new name for the assistant. If not provided, assistant will keep its current name.

Responses

  * Expand200Success

application/json

  * Expand404Not Found

application/json

  * Expand422Validation Error

application/json




PATCH/assistants/_{assistant_id}_

Selected HTTP client: Shell CurlLibcurlHttpClientRestSharpclj-httpHttpNewRequestHTTP/1.1AsyncHttpjava.net.httpOkHttpUnirestFetchAxiosofetchjQueryXHROkHttpFetchAxiosofetchundiciNSURLSessionCohttpcURLGuzzleInvoke-WebRequestInvoke-RestMethodhttp.clientRequestshttrnet::httpCurlWgetHTTPieNSURLSession

Copy content

```
curl 'https://langchain-ai.github.io/assistants/{assistant_id}' \
 --request PATCH \
 --header 'Content-Type: application/json' \
 --data '{
 "graph_id": "",
 "config": {},
 "metadata": {},
 "name": ""
}'

```


Test Request(patch /assistants/{assistant_id})

200404422

Show Schema 

Copy content

```
{
 "assistant_id": "123e4567-e89b-12d3-a456-426614174000",
 "graph_id": "…",
 "config": {
  "tags": [
   "…"
  ],
  "recursion_limit": 1,
  "configurable": {}
 },
 "created_at": "2025-02-15T23:43:15.654Z",
 "updated_at": "2025-02-15T23:43:15.654Z",
 "metadata": {},
 "version": 1,
 "name": "…"
}
```


Success

### Get Assistant Graph​#Copy link to "Get Assistant Graph"

Get an assistant by ID.

Path Parameters

  * assistant_id

anyOf

required 

The ID of the assistant.

The ID of the assistant.

Show Assistant ID

The ID of the graph.

Show Graph ID




Query Parameters

  * xray

oneOf

Include graph representation of subgraphs. If an integer value is provided, only subgraphs with a depth less than or equal to the value will be included.

Show Child Attributes

Show Child Attributes




Responses

  * Expand200Success

application/json

  * Expand404Not Found

application/json

  * Expand422Validation Error

application/json




GET/assistants/_{assistant_id}_ /graph

Selected HTTP client: Shell CurlLibcurlHttpClientRestSharpclj-httpHttpNewRequestHTTP/1.1AsyncHttpjava.net.httpOkHttpUnirestFetchAxiosofetchjQueryXHROkHttpFetchAxiosofetchundiciNSURLSessionCohttpcURLGuzzleInvoke-WebRequestInvoke-RestMethodhttp.clientRequestshttrnet::httpCurlWgetHTTPieNSURLSession

Copy content

```
curl 'https://langchain-ai.github.io/assistants/{assistant_id}/graph'

```


Test Request(get /assistants/{assistant_id}/graph)

200404422

Show Schema 

Copy content

```
{
 "ANY_ADDITIONAL_PROPERTY": [
  {}
 ]
}
```


Success

### Get Assistant Subgraphs​#Copy link to "Get Assistant Subgraphs"

Get an assistant's subgraphs.

Path Parameters

  * assistant_id

string uuid

required 

The ID of the assistant.




Query Parameters

  * recurse

boolean 

default: 

false

Recursively retrieve subgraphs of subgraphs.




Responses

  * Expand200Success

application/json

  * Expand404Not Found

application/json

  * Expand422Validation Error

application/json




GET/assistants/_{assistant_id}_ /subgraphs

Selected HTTP client: Shell CurlLibcurlHttpClientRestSharpclj-httpHttpNewRequestHTTP/1.1AsyncHttpjava.net.httpOkHttpUnirestFetchAxiosofetchjQueryXHROkHttpFetchAxiosofetchundiciNSURLSessionCohttpcURLGuzzleInvoke-WebRequestInvoke-RestMethodhttp.clientRequestshttrnet::httpCurlWgetHTTPieNSURLSession

Copy content

```
curl 'https://langchain-ai.github.io/assistants/{assistant_id}/subgraphs'

```


Test Request(get /assistants/{assistant_id}/subgraphs)

200404422

Show Schema 

Copy content

```
{
 "ANY_ADDITIONAL_PROPERTY": {
  "input_schema": {},
  "output_schema": {},
  "state_schema": {},
  "config_schema": {}
 }
}
```


Success

### Get Assistant Subgraphs by Namespace​#Copy link to "Get Assistant Subgraphs by Namespace"

Get an assistant's subgraphs filtered by namespace.

Path Parameters

  * assistant_id

string uuid

required 

The ID of the assistant.

  * namespace

string 

required 

Namespace of the subgraph to filter by.




Query Parameters

  * recurse

boolean 

default: 

false

Recursively retrieve subgraphs of subgraphs.




Responses

  * Expand200Success

application/json

  * Expand422Validation Error

application/json




GET/assistants/_{assistant_id}_ /subgraphs/_{namespace}_

Selected HTTP client: Shell CurlLibcurlHttpClientRestSharpclj-httpHttpNewRequestHTTP/1.1AsyncHttpjava.net.httpOkHttpUnirestFetchAxiosofetchjQueryXHROkHttpFetchAxiosofetchundiciNSURLSessionCohttpcURLGuzzleInvoke-WebRequestInvoke-RestMethodhttp.clientRequestshttrnet::httpCurlWgetHTTPieNSURLSession

Copy content

```
curl 'https://langchain-ai.github.io/assistants/{assistant_id}/subgraphs/{namespace}'

```


Test Request(get /assistants/{assistant_id}/subgraphs/{namespace})

200422

Show Schema 

Copy content

```
{
 "ANY_ADDITIONAL_PROPERTY": {
  "input_schema": {},
  "output_schema": {},
  "state_schema": {},
  "config_schema": {}
 }
}
```


Success

### Get Assistant Schemas​#Copy link to "Get Assistant Schemas"

Get an assistant by ID.

Path Parameters

  * assistant_id

string uuid

required 

The ID of the assistant.




Responses

  * Expand200Success

application/json

  * Expand404Not Found

application/json

  * Expand422Validation Error

application/json




GET/assistants/_{assistant_id}_ /schemas

Selected HTTP client: Shell CurlLibcurlHttpClientRestSharpclj-httpHttpNewRequestHTTP/1.1AsyncHttpjava.net.httpOkHttpUnirestFetchAxiosofetchjQueryXHROkHttpFetchAxiosofetchundiciNSURLSessionCohttpcURLGuzzleInvoke-WebRequestInvoke-RestMethodhttp.clientRequestshttrnet::httpCurlWgetHTTPieNSURLSession

Copy content

```
curl 'https://langchain-ai.github.io/assistants/{assistant_id}/schemas'

```


Test Request(get /assistants/{assistant_id}/schemas)

200404422

Show Schema 

Copy content

```
{
 "graph_id": "…",
 "input_schema": {},
 "output_schema": {},
 "state_schema": {},
 "config_schema": {}
}
```


Success

### Get Assistant Versions​#Copy link to "Get Assistant Versions"

Get all versions of an assistant.

Path Parameters

  * assistant_id

string uuid

required 

The ID of the assistant.




Responses

  * Expand200Success

application/json

  * Expand422Validation Error

application/json




POST/assistants/_{assistant_id}_ /versions

Selected HTTP client: Shell CurlLibcurlHttpClientRestSharpclj-httpHttpNewRequestHTTP/1.1AsyncHttpjava.net.httpOkHttpUnirestFetchAxiosofetchjQueryXHROkHttpFetchAxiosofetchundiciNSURLSessionCohttpcURLGuzzleInvoke-WebRequestInvoke-RestMethodhttp.clientRequestshttrnet::httpCurlWgetHTTPieNSURLSession

Copy content

```
curl 'https://langchain-ai.github.io/assistants/{assistant_id}/versions' \
 --request POST

```


Test Request(post /assistants/{assistant_id}/versions)

200422

Show Schema 

Copy content

```
[
 {
  "assistant_id": "123e4567-e89b-12d3-a456-426614174000",
  "graph_id": "…",
  "config": {
   "tags": [
    "…"
   ],
   "recursion_limit": 1,
   "configurable": {}
  },
  "created_at": "2025-02-15T23:43:15.654Z",
  "updated_at": "2025-02-15T23:43:15.654Z",
  "metadata": {},
  "version": 1,
  "name": "…"
 }
]
```


Success

### Set Latest Assistant Version​#Copy link to "Set Latest Assistant Version"

Set the latest version for an assistant.

Path Parameters

  * assistant_id

string uuid

required 

The ID of the assistant.




Query Parameters

  * version

integer 

required 

The version to change to.




Responses

  * Expand200Success

application/json

  * Expand404Not Found

application/json

  * Expand422Validation Error

application/json




POST/assistants/_{assistant_id}_ /latest

Selected HTTP client: Shell CurlLibcurlHttpClientRestSharpclj-httpHttpNewRequestHTTP/1.1AsyncHttpjava.net.httpOkHttpUnirestFetchAxiosofetchjQueryXHROkHttpFetchAxiosofetchundiciNSURLSessionCohttpcURLGuzzleInvoke-WebRequestInvoke-RestMethodhttp.clientRequestshttrnet::httpCurlWgetHTTPieNSURLSession

Copy content

```
curl 'https://langchain-ai.github.io/assistants/{assistant_id}/latest?version=' \
 --request POST

```


Test Request(post /assistants/{assistant_id}/latest)

200404422

Show Schema 

Copy content

```
{
 "assistant_id": "123e4567-e89b-12d3-a456-426614174000",
 "graph_id": "…",
 "config": {
  "tags": [
   "…"
  ],
  "recursion_limit": 1,
  "configurable": {}
 },
 "created_at": "2025-02-15T23:43:15.654Z",
 "updated_at": "2025-02-15T23:43:15.654Z",
 "metadata": {},
 "version": 1,
 "name": "…"
}
```


Success

## Threads​#Copy link to "Threads"

A thread contains the accumulated outputs of a group of runs.

Threads Endpoints 

  * [POST/threads](#tag/threads/POST/threads)
  * [POST/threads/search](#tag/threads/POST/threads/search)
  * [GET/threads/{thread_id}/state](#tag/threads/GET/threads/{thread_id}/state)
  * [POST/threads/{thread_id}/state](#tag/threads/POST/threads/{thread_id}/state)
  * [POST/threads/{thread_id}/state/checkpoint](#tag/threads/POST/threads/{thread_id}/state/checkpoint)
  * [GET/threads/{thread_id}/history](#tag/threads/GET/threads/{thread_id}/history)
  * [POST/threads/{thread_id}/history](#tag/threads/POST/threads/{thread_id}/history)
  * [POST/threads/{thread_id}/copy](#tag/threads/POST/threads/{thread_id}/copy)
  * [GET/threads/{thread_id}](#tag/threads/GET/threads/{thread_id})
  * [DELETE/threads/{thread_id}](#tag/threads/DELETE/threads/{thread_id})
  * [PATCH/threads/{thread_id}](#tag/threads/PATCH/threads/{thread_id})



Show More 

## Thread Runs​#Copy link to "Thread Runs"

A run is an invocation of a graph / assistant on a thread. It updates the state of the thread.

Thread Runs Endpoints 

  * [GET/threads/{thread_id}/runs](#tag/thread-runs/GET/threads/{thread_id}/runs)
  * [POST/threads/{thread_id}/runs](#tag/thread-runs/POST/threads/{thread_id}/runs)
  * [POST/threads/{thread_id}/runs/stream](#tag/thread-runs/POST/threads/{thread_id}/runs/stream)
  * [POST/threads/{thread_id}/runs/wait](#tag/thread-runs/POST/threads/{thread_id}/runs/wait)
  * [GET/threads/{thread_id}/runs/{run_id}](#tag/thread-runs/GET/threads/{thread_id}/runs/{run_id})
  * [DELETE/threads/{thread_id}/runs/{run_id}](#tag/thread-runs/DELETE/threads/{thread_id}/runs/{run_id})
  * [GET/threads/{thread_id}/runs/{run_id}/join](#tag/thread-runs/GET/threads/{thread_id}/runs/{run_id}/join)
  * [GET/threads/{thread_id}/runs/{run_id}/stream](#tag/thread-runs/GET/threads/{thread_id}/runs/{run_id}/stream)
  * [POST/threads/{thread_id}/runs/{run_id}/cancel](#tag/thread-runs/POST/threads/{thread_id}/runs/{run_id}/cancel)



Show More 

## Stateless Runs​#Copy link to "Stateless Runs"

A run is an invocation of a graph / assistant, with no state or memory persistence.

Stateless Runs Endpoints 

  * [POST/runs/stream](#tag/stateless-runs/POST/runs/stream)
  * [POST/runs/wait](#tag/stateless-runs/POST/runs/wait)
  * [POST/runs](#tag/stateless-runs/POST/runs)
  * [POST/runs/batch](#tag/stateless-runs/POST/runs/batch)



Show More 

## Crons (Enterprise-only)​#Copy link to "Crons (Enterprise-only)"

A cron is a periodic run that recurs on a given schedule. The repeats can be isolated, or share state in a thread

Crons (Enterprise-only) Endpoints 

  * [POST/threads/{thread_id}/runs/crons](#tag/crons-enterprise-only/POST/threads/{thread_id}/runs/crons)
  * [POST/runs/crons](#tag/crons-enterprise-only/POST/runs/crons)
  * [POST/runs/crons/search](#tag/crons-enterprise-only/POST/runs/crons/search)
  * [DELETE/runs/crons/{cron_id}](#tag/crons-enterprise-only/DELETE/runs/crons/{cron_id})



Show More 

## Store​#Copy link to "Store"

Store is an API for managing persistent key-value store (long-term memory) that is available from any thread.

Store Endpoints 

  * [PUT/store/items](#tag/store/PUT/store/items)
  * [DELETE/store/items](#tag/store/DELETE/store/items)
  * [GET/store/items](#tag/store/GET/store/items)
  * [POST/store/items/search](#tag/store/POST/store/items/search)
  * [POST/store/namespaces](#tag/store/POST/store/namespaces)



Show More 

## Models

{} Assistant​#Copy link to " {} Assistant"

{} AssistantCreate​#Copy link to " {} AssistantCreate"

{} AssistantPatch​#Copy link to " {} AssistantPatch"

{} AssistantVersionChange​#Copy link to " {} AssistantVersionChange"

{} Config​#Copy link to " {} Config"

{} Cron​#Copy link to " {} Cron"

{} CronCreate​#Copy link to " {} CronCreate"

{} CronSearch​#Copy link to " {} CronSearch"

{} GraphSchema​#Copy link to " {} GraphSchema"

{} GraphSchemaNoId​#Copy link to " {} GraphSchemaNoId"

Show More 

Show sidebar

*   * Close Group 

Assistants

    * [Create Assistant HTTP Method:POST](/workspace/default/request/fDzOqHUmXz7AzKrquZUUL)

    * [Search Assistants HTTP Method:POST](/workspace/default/request/t7ugKHVP4zgoCd2Uqtn3U)

    * [Get Assistant HTTP Method:GET](/workspace/default/request/O7VvxfXpl5bcZ4WjGrIeA)

    * [Delete Assistant HTTP Method:DEL](/workspace/default/request/gMcCetXR9qBnLycEeU6La)

    * [Patch Assistant HTTP Method:PATCH](/workspace/default/request/sp1QdTUQTZ1KyNX9ptMXu)

    * [Get Assistant Graph HTTP Method:GET](/workspace/default/request/MMqfIg7zj5j_13_5HqCiR)

    * [Get Assistant Subgraphs HTTP Method:GET](/workspace/default/request/YkQdkWvG2qUQBa4OrhL68)

    * [Get Assistant Subgraphs by Namespace HTTP Method:GET](/workspace/default/request/ll-8-uvPG5yRA6tOOHl_I)

    * [Get Assistant Schemas HTTP Method:GET](/workspace/default/request/s9Znz_ildbFwsYF0s4pxX)

    * [Get Assistant Versions HTTP Method:POST](/workspace/default/request/aXl3KI-T_qYCMaRmVs0jV)

    * [Set Latest Assistant Version HTTP Method:POST](/workspace/default/request/FOn-jGblUZfdAXbgUcFh3)

  * Open Group 

Threads

  * Open Group 

Thread Runs

  * Open Group 

Stateless Runs

  * Open Group 

Crons (Enterprise-only)

  * Open Group 

Store




,\ \\\\\,_ \\` ,\ __,.-" =__) ." ),_/ , \/\\_\\_| )_-\ \\_-` `-----` `--`

__ // \,_ \\` ,\ __,.-" =__) ." ),_/ , \/\ \\_| // / / / / / 

**Let's Get Started**

Create request, folder, collection or import from OpenAPI/Postman 

Show sidebar

POST

Server: https://langchain-ai.github.io 

/assistants

Send Send Request 

[ Open API Client ](https://client.scalar.com/?url=https%3A%2F%2Flangchain-ai.github.io%2Flanggraph%2Fcloud%2Freference%2Fapi%2Fopenapi.json&integration=html&utm_source=api-reference&utm_medium=button&utm_campaign=modal)Close ClientClose Client

Create Assistant

Filter Sections

All Query Auth Cookies Headers Body 

All

Variables

Cookies

Row DisabledKey| Value  
---|---  
  
Headers

Clear All Headers

Row EnabledAccept| */*  
---|---  
Row EnabledContent-Type| application/json  
Row DisabledKey| Value  
  
Query Parameters

Row DisabledKey| Value  
---|---  
  
Body

JSON  
---  
  
9

1

2

3

4

5

6

7

8

{

"assistant_id": "",

"graph_id": "",

"config": {},

"metadata": {},

"if_exists": "raise",

"name": ""

}  
  
Code Snippet

Curl

Response 

Filter Sections

All Cookies Headers Body 

All

[ Powered By Scalar.com ](https://www.scalar.com)

.,,uod8B8bou,,. ..,uod8BBBBBBBBBBBBBBBBRPFT?l!i:. ||||||||||||||!?TFPRBBBBBBBBBBBBBBB8m=, |||| '""^^!!||||||||||TFPRBBBVT!:...! |||| '""^^!!|||||?!:.......! |||| ||||.........! |||| ||||.........! |||| ||||.........! |||| ||||.........! |||| ||||.........! |||| ||||.........! ||||, ||||.........` |||||!!-._ ||||.......;. ':!|||||||||!!-._ ||||.....bBBBBWdou,. bBBBBB86foi!|||||||!!-..:|||!..bBBBBBBBBBBBBBBY! ::!?TFPRBBBBBB86foi!||||||||!!bBBBBBBBBBBBBBBY..! :::::::::!?TFPRBBBBBB86ftiaabBBBBBBBBBBBBBBY....! :::;`"^!:;::::::!?TFPRBBBBBBBBBBBBBBBBBBBY......! ;::::::...''^::::::::::!?TFPRBBBBBBBBBBY........! .ob86foi;::::::::::::::::::::::::!?TFPRBY..........` .b888888888886foi;:::::::::::::::::::::::..........` .b888888888888888888886foi;::::::::::::::::...........b888888888888888888888888888886foi;:::::::::......`!Tf998888888888888888888888888888888886foi;:::....` '"^!|Tf9988888888888888888888888888888888!::..` '"^!|Tf998888888888888888888888889!! '` '"^!|Tf9988888888888888888!!` iBBbo. '"^!|Tf998888888889!` WBBBBbo. '"^!|Tf9989!` YBBBP^' '"^!` `

Send Request 

⌘ ↵
