---
url: https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#how-to-add-custom-authentication)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to add custom authentication 

[ ](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/?q= "Share")

Type to start searching

[ GitHub  ](https://github.com/langchain-ai/langgraph "Go to repository")

  * [ Home ](https://langchain-ai.github.io/langgraph/)
  * [ API reference ](https://langchain-ai.github.io/langgraph/reference/graphs/)



[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

[ GitHub  ](https://github.com/langchain-ai/langgraph "Go to repository")

  * [ Home  ](https://langchain-ai.github.io/langgraph/)
  * [ API reference  ](https://langchain-ai.github.io/langgraph/reference/graphs/)



Table of contents 

  * [ 1. Implement authentication  ](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#1-implement-authentication)
  * [ 2. Update configuration  ](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#2-update-configuration)
  * [ 3. Connect from the client  ](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#3-connect-from-the-client)



[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/auth/custom_auth.md "Edit this page")

# How to add custom authentication[¶](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#how-to-add-custom-authentication "Permanent link")

Prerequisites

This guide assumes familiarity with the following concepts:

  * [**Authentication & Access Control**](https://langchain-ai.github.io/langgraph/concepts/auth/)
  * [**LangGraph Platform**](https://langchain-ai.github.io/langgraph/concepts/#langgraph-platform)



For a more guided walkthrough, see [**setting up custom authentication**](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/) tutorial.

Python only

We currently only support custom authentication and authorization in Python deployments with `langgraph-api>=0.0.11`. Support for LangGraph.JS will be added soon.

Support by deployment type

Custom auth is supported for all deployments in the **managed LangGraph Cloud** , as well as **Enterprise** self-hosted plans. It is not supported for **Lite** self-hosted plans.

This guide shows how to add custom authentication to your LangGraph Platform application. This guide applies to both LangGraph Cloud, BYOC, and self-hosted deployments. It does not apply to isolated usage of the LangGraph open source library in your own custom server.

## 1. Implement authentication[¶](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#1-implement-authentication "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-0-1)fromlanggraph_sdkimport Auth
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-0-2)
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-0-3)my_auth = Auth()
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-0-4)
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-0-5)@my_auth.authenticate
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-0-6)async defauthenticate(authorization: str) -> str:
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-0-7)  token = authorization.split(" ", 1)[-1] # "Bearer <token>"
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-0-8)  try:
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-0-9)    # Verify token with your auth provider
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-0-10)    user_id = await verify_token(token)
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-0-11)    return user_id
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-0-12)  except Exception:
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-0-13)    raise Auth.exceptions.HTTPException(
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-0-14)      status_code=401,
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-0-15)      detail="Invalid token"
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-0-16)    )
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-0-17)
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-0-18)# Add authorization rules to actually control access to resources
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-0-19)@my_auth.on
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-0-20)async defadd_owner(
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-0-21)  ctx: Auth.types.AuthContext,
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-0-22)  value: dict,
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-0-23)):
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-0-24)"""Add owner to resource metadata and filter by owner."""
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-0-25)  filters = {"owner": ctx.user.identity}
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-0-26)  metadata = value.setdefault("metadata", {})
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-0-27)  metadata.update(filters)
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-0-28)  return filters
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-0-29)
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-0-30)# Assumes you organize information in store like (user_id, resource_type, resource_id)
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-0-31)@my_auth.on.store()
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-0-32)async defauthorize_store(ctx: Auth.types.AuthContext, value: dict):
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-0-33)  namespace: tuple = value["namespace"]
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-0-34)  assert namespace[0] == ctx.user.identity, "Not authorized"

```


## 2. Update configuration[¶](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#2-update-configuration "Permanent link")

In your `langgraph.json`, add the path to your auth file:

```
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-1-1){
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-1-2)"dependencies":["."],
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-1-3)"graphs":{
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-1-4)"agent":"./agent.py:graph"
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-1-5)},
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-1-6)"env":".env",
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-1-7)"auth":{
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-1-8)"path":"./auth.py:my_auth"
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-1-9)}
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-1-10)}

```


## 3. Connect from the client[¶](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#3-connect-from-the-client "Permanent link")

Once you've set up authentication in your server, requests must include the the required authorization information based on your chosen scheme. Assuming you are using JWT token authentication, you could access your deployments using any of the following methods:

[Python Client](#__tabbed_1_1)[Python RemoteGraph](#__tabbed_1_2)[JavaScript Client](#__tabbed_1_3)[JavaScript RemoteGraph](#__tabbed_1_4)[CURL](#__tabbed_1_5)

```
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-2-1)fromlanggraph_sdkimport get_client
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-2-2)
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-2-3)my_token = "your-token" # In practice, you would generate a signed token with your auth provider
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-2-4)client = get_client(
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-2-5)  url="http://localhost:2024",
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-2-6)  headers={"Authorization": f"Bearer {my_token}"}
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-2-7))
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-2-8)threads = await client.threads.search()

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-3-1)fromlanggraph.pregel.remoteimport RemoteGraph
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-3-2)
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-3-3)my_token = "your-token" # In practice, you would generate a signed token with your auth provider
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-3-4)remote_graph = RemoteGraph(
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-3-5)  "agent",
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-3-6)  url="http://localhost:2024",
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-3-7)  headers={"Authorization": f"Bearer {my_token}"}
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-3-8))
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-3-9)threads = await remote_graph.ainvoke(...)

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-4-1)import{Client}from"@langchain/langgraph-sdk";
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-4-2)
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-4-3)constmy_token="your-token";// In practice, you would generate a signed token with your auth provider
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-4-4)constclient=newClient({
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-4-5)apiUrl:"http://localhost:2024",
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-4-6)headers:{Authorization:`Bearer ${my_token}`},
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-4-7)});
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-4-8)constthreads=awaitclient.threads.search();

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-5-1)import{RemoteGraph}from"@langchain/langgraph/remote";
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-5-2)
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-5-3)constmy_token="your-token";// In practice, you would generate a signed token with your auth provider
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-5-4)constremoteGraph=newRemoteGraph({
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-5-5)graphId:"agent",
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-5-6)url:"http://localhost:2024",
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-5-7)headers:{Authorization:`Bearer ${my_token}`},
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-5-8)});
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-5-9)constthreads=awaitremoteGraph.invoke(...);

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__codelineno-6-1)curl-H"Authorization: Bearer ${your-token}"http://localhost:2024/threads

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top 

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
