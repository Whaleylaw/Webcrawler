---
url: https://langchain-ai.github.io/langgraph/cloud/reference/env_var/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/cloud/reference/env_var/#environment-variables)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Environment variables 

[ ](https://langchain-ai.github.io/langgraph/cloud/reference/env_var/?q= "Share")

Initializing search 

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
      * Environment variables  [ Environment variables  ](https://langchain-ai.github.io/langgraph/cloud/reference/env_var/) Table of contents 
        * [ LANGCHAIN_TRACING_SAMPLING_RATE  ](https://langchain-ai.github.io/langgraph/cloud/reference/env_var/#langchain_tracing_sampling_rate)
        * [ LANGGRAPH_AUTH_TYPE  ](https://langchain-ai.github.io/langgraph/cloud/reference/env_var/#langgraph_auth_type)
        * [ LANGSMITH_RUNS_ENDPOINTS  ](https://langchain-ai.github.io/langgraph/cloud/reference/env_var/#langsmith_runs_endpoints)
        * [ N_JOBS_PER_WORKER  ](https://langchain-ai.github.io/langgraph/cloud/reference/env_var/#n_jobs_per_worker)
        * [ POSTGRES_URI_CUSTOM  ](https://langchain-ai.github.io/langgraph/cloud/reference/env_var/#postgres_uri_custom)



Table of contents 

  * [ LANGCHAIN_TRACING_SAMPLING_RATE  ](https://langchain-ai.github.io/langgraph/cloud/reference/env_var/#langchain_tracing_sampling_rate "LANGCHAIN_TRACING_SAMPLING_RATE")
  * [ LANGGRAPH_AUTH_TYPE  ](https://langchain-ai.github.io/langgraph/cloud/reference/env_var/#langgraph_auth_type)
  * [ LANGSMITH_RUNS_ENDPOINTS  ](https://langchain-ai.github.io/langgraph/cloud/reference/env_var/#langsmith_runs_endpoints "LANGSMITH_RUNS_ENDPOINTS")
  * [ N_JOBS_PER_WORKER  ](https://langchain-ai.github.io/langgraph/cloud/reference/env_var/#n_jobs_per_worker)
  * [ POSTGRES_URI_CUSTOM  ](https://langchain-ai.github.io/langgraph/cloud/reference/env_var/#postgres_uri_custom)



  1. [ API reference  ](https://langchain-ai.github.io/langgraph/reference/graphs/)
  2. [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/cloud/reference/api/api_ref/)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/cloud/reference/env_var.md "Edit this page")

# Environment Variables[¶](https://langchain-ai.github.io/langgraph/cloud/reference/env_var/#environment-variables "Permanent link")

The LangGraph Cloud Server supports specific environment variables for configuring a deployment.

## `LANGCHAIN_TRACING_SAMPLING_RATE`[¶](https://langchain-ai.github.io/langgraph/cloud/reference/env_var/#langchain_tracing_sampling_rate "Permanent link")

Sampling rate for traces sent to LangSmith. Valid values: Any float between `0` and `1`.

See [LangSmith documentation](https://docs.smith.langchain.com/how_to_guides/tracing/sample_traces) for more details.

## `LANGGRAPH_AUTH_TYPE`[¶](https://langchain-ai.github.io/langgraph/cloud/reference/env_var/#langgraph_auth_type "Permanent link")

Type of authentication for the LangGraph Cloud Server deployment. Valid values: `langsmith`, `noop`.

For deployments to LangGraph Cloud, this environment variable is set automatically. For local development or deployments where authentication is handled externally (e.g. self-hosted), set this environment variable to `noop`.

## `LANGSMITH_RUNS_ENDPOINTS`[¶](https://langchain-ai.github.io/langgraph/cloud/reference/env_var/#langsmith_runs_endpoints "Permanent link")

For [Bring Your Own Cloud (BYOC)](https://langchain-ai.github.io/langgraph/concepts/bring_your_own_cloud/) deployments with [self-hosted LangSmith](https://docs.smith.langchain.com/self_hosting) only.

Set this environment variable to have a BYOC deployment send traces to a self-hosted LangSmith instance. The value of `LANGSMITH_RUNS_ENDPOINTS` is a JSON string: `{"<SELF_HOSTED_LANGSMITH_HOSTNAME>":"<LANGSMITH_API_KEY>"}`.

`SELF_HOSTED_LANGSMITH_HOSTNAME` is the hostname of the self-hosted LangSmith instance. It must be accessible to the BYOC deployment. `LANGSMITH_API_KEY` is a LangSmith API generated from the self-hosted LangSmith instance.

## `N_JOBS_PER_WORKER`[¶](https://langchain-ai.github.io/langgraph/cloud/reference/env_var/#n_jobs_per_worker "Permanent link")

Number of jobs per worker for the LangGraph Cloud task queue. Defaults to `10`.

## `POSTGRES_URI_CUSTOM`[¶](https://langchain-ai.github.io/langgraph/cloud/reference/env_var/#postgres_uri_custom "Permanent link")

For [Bring Your Own Cloud (BYOC)](https://langchain-ai.github.io/langgraph/concepts/bring_your_own_cloud/) deployments only.

Specify `POSTGRES_URI_CUSTOM` to use an externally managed Postgres instance. The value of `POSTGRES_URI_CUSTOM` must be a valid [Postgres connection URI](https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING-URIS).

Postgres:

  * Version 15.8 or higher.
  * An initial database must be present and the connection URI must reference the database.



Control Plane Functionality:

  * If `POSTGRES_URI_CUSTOM` is specified, the LangGraph Control Plane will not provision a database for the server.
  * If `POSTGRES_URI_CUSTOM` is removed, the LangGraph Control Plane will not provision a database for the server and will not delete the externally managed Postgres instance.
  * If `POSTGRES_URI_CUSTOM` is removed, deployment of the revision will not succeed. Once `POSTGRES_URI_CUSTOM` is specified, it must always be set for the lifecycle of the deployment.
  * If the deployment is deleted, the LangGraph Control Plane will not delete the externally managed Postgres instance.
  * The value of `POSTGRES_URI_CUSTOM` can be updated. For example, a password in the URI can be updated.



Database Connectivity:

  * The externally managed Postgres instance must be accessible by the LangGraph Server service in the ECS cluster. The BYOC user is responsible for ensuring connectivity.
  * For example, if an AWS RDS Postgres instance is provisioned, it can be provisioned in the same VPC (`langgraph-cloud-vpc`) as the ECS cluster with the `langgraph-cloud-service-sg` security group to ensure connectivity.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  RemoteGraph  ](https://langchain-ai.github.io/langgraph/reference/remote_graph/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/cloud/reference/env_var/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
