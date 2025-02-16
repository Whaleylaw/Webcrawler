---
url: https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#how-to-document-api-authentication-in-openapi)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to document API authentication in OpenAPI 

[ ](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/?q= "Share")

Type to start searching

[ GitHub  ](https://github.com/langchain-ai/langgraph "Go to repository")

  * [ Home ](https://langchain-ai.github.io/langgraph/)
  * [ API reference ](https://langchain-ai.github.io/langgraph/reference/graphs/)



[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

[ GitHub  ](https://github.com/langchain-ai/langgraph "Go to repository")

  * [ Home  ](https://langchain-ai.github.io/langgraph/)
  * [ API reference  ](https://langchain-ai.github.io/langgraph/reference/graphs/)



Table of contents 

  * [ Default Schema  ](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#default-schema)
  * [ Custom Security Schema  ](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#custom-security-schema)
  * [ Testing  ](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#testing)



[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/auth/openapi_security.md "Edit this page")

# How to document API authentication in OpenAPI[¶](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#how-to-document-api-authentication-in-openapi "Permanent link")

This guide shows how to customize the OpenAPI security schema for your LangGraph Platform API documentation. A well-documented security schema helps API consumers understand how to authenticate with your API and even enables automatic client generation. See the [Authentication & Access Control conceptual guide](https://langchain-ai.github.io/langgraph/concepts/auth/) for more details about LangGraph's authentication system.

Implementation vs Documentation

This guide only covers how to document your security requirements in OpenAPI. To implement the actual authentication logic, see [How to add custom authentication](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/).

This guide applies to all LangGraph Platform deployments (Cloud, BYOC, and self-hosted). It does not apply to usage of the LangGraph open source library if you are not using LangGraph Platform.

## Default Schema[¶](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#default-schema "Permanent link")

The default security scheme varies by deployment type:

[LangGraph Cloud](#__tabbed_1_1)

By default, LangGraph Cloud requires a LangSmith API key in the `x-api-key` header:

```
[](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#__codelineno-0-1)components:
[](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#__codelineno-0-2)securitySchemes:
[](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#__codelineno-0-3)apiKeyAuth:
[](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#__codelineno-0-4)type:apiKey
[](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#__codelineno-0-5)in:header
[](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#__codelineno-0-6)name:x-api-key
[](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#__codelineno-0-7)security:
[](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#__codelineno-0-8)-apiKeyAuth:[]

```


When using one of the LangGraph SDK's, this can be inferred from environment variables.

[Self-hosted](#__tabbed_2_1)

By default, self-hosted deployments have no security scheme. This means they are to be deployed only on a secured network or with authentication. To add custom authentication, see [How to add custom authentication](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/).

## Custom Security Schema[¶](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#custom-security-schema "Permanent link")

To customize the security schema in your OpenAPI documentation, add an `openapi` field to your `auth` configuration in `langgraph.json`. Remember that this only updates the API documentation - you must also implement the corresponding authentication logic as shown in [How to add custom authentication](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/).

Note that LangGraph Platform does not provide authentication endpoints - you'll need to handle user authentication in your client application and pass the resulting credentials to the LangGraph API.

[OAuth2 with Bearer Token](#__tabbed_3_1)[API Key](#__tabbed_3_2)

```
[](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#__codelineno-1-1){
[](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#__codelineno-1-2)"auth":{
[](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#__codelineno-1-3)"path":"./auth.py:my_auth",// Implement auth logic here
[](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#__codelineno-1-4)"openapi":{
[](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#__codelineno-1-5)"securitySchemes":{
[](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#__codelineno-1-6)"OAuth2":{
[](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#__codelineno-1-7)"type":"oauth2",
[](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#__codelineno-1-8)"flows":{
[](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#__codelineno-1-9)"implicit":{
[](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#__codelineno-1-10)"authorizationUrl":"https://your-auth-server.com/oauth/authorize",
[](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#__codelineno-1-11)"scopes":{
[](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#__codelineno-1-12)"me":"Read information about the current user",
[](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#__codelineno-1-13)"threads":"Access to create and manage threads"
[](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#__codelineno-1-14)}
[](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#__codelineno-1-15)}
[](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#__codelineno-1-16)}
[](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#__codelineno-1-17)}
[](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#__codelineno-1-18)},
[](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#__codelineno-1-19)"security":[
[](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#__codelineno-1-20){"OAuth2":["me","threads"]}
[](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#__codelineno-1-21)]
[](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#__codelineno-1-22)}
[](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#__codelineno-1-23)}
[](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#__codelineno-1-24)}

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#__codelineno-2-1){
[](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#__codelineno-2-2)"auth":{
[](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#__codelineno-2-3)"path":"./auth.py:my_auth",// Implement auth logic here
[](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#__codelineno-2-4)"openapi":{
[](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#__codelineno-2-5)"securitySchemes":{
[](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#__codelineno-2-6)"apiKeyAuth":{
[](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#__codelineno-2-7)"type":"apiKey",
[](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#__codelineno-2-8)"in":"header",
[](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#__codelineno-2-9)"name":"X-API-Key"
[](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#__codelineno-2-10)}
[](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#__codelineno-2-11)},
[](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#__codelineno-2-12)"security":[
[](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#__codelineno-2-13){"apiKeyAuth":[]}
[](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#__codelineno-2-14)]
[](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#__codelineno-2-15)}
[](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#__codelineno-2-16)}
[](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#__codelineno-2-17)}

```


## Testing[¶](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#testing "Permanent link")

After updating your configuration:

  1. Deploy your application
  2. Visit `/docs` to see the updated OpenAPI documentation
  3. Try out the endpoints using credentials from your authentication server (make sure you've implemented the authentication logic first)

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top 

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/auth/openapi_security/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
