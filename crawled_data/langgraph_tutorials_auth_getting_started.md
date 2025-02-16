---
url: https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#setting-up-custom-authentication-part-13)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Setting up Custom Authentication (Part ⅓) 

[ ](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/?q= "Share")

Type to start searching

[ GitHub  ](https://github.com/langchain-ai/langgraph "Go to repository")

  * [ Home ](https://langchain-ai.github.io/langgraph/)
  * [ API reference ](https://langchain-ai.github.io/langgraph/reference/graphs/)



[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

[ GitHub  ](https://github.com/langchain-ai/langgraph "Go to repository")

  * [ Home  ](https://langchain-ai.github.io/langgraph/)

Home 
    * Get started  Get started 
      * [ Learn the basics  ](https://langchain-ai.github.io/langgraph/tutorials/introduction/)
      * [ Deployment  ](https://langchain-ai.github.io/langgraph/tutorials/deployment/)
    * Guides  Guides 
      * [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
      * [ Concepts  ](https://langchain-ai.github.io/langgraph/concepts/)
      * [ Tutorials  ](https://langchain-ai.github.io/langgraph/tutorials/)

Tutorials 
        * [ Quick Start  ](https://langchain-ai.github.io/langgraph/tutorials#quick-start)
        * [ Chatbots  ](https://langchain-ai.github.io/langgraph/tutorials#chatbots)
        * [ RAG  ](https://langchain-ai.github.io/langgraph/tutorials#rag)
        * [ Agent Architectures  ](https://langchain-ai.github.io/langgraph/tutorials#agent-architectures)
        * [ Evaluation & Analysis  ](https://langchain-ai.github.io/langgraph/tutorials#evaluation)
        * [ Experimental  ](https://langchain-ai.github.io/langgraph/tutorials#experimental)
        * LangGraph Platform  LangGraph Platform 
          * [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/concepts#langgraph-platform)
          * Setting up Custom Authentication (Part ⅓)  [ Setting up Custom Authentication (Part ⅓)  ](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/) Table of contents 
            * [ Setting up our project  ](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#setting-up-our-project)
            * [ Adding Authentication  ](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#adding-authentication)
            * [ Testing Our "Secure" Bot  ](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#testing-our-secure-bot)
            * [ What's Next?  ](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#whats-next)
          * [ Making Conversations Private (Part ⅔)  ](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/)
          * [ Connecting an Authentication Provider (Part 3/3)  ](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/)
    * Resources  Resources 
      * [ Prebuilt Agents  ](https://langchain-ai.github.io/langgraph/prebuilt/)
      * [ Adopters  ](https://langchain-ai.github.io/langgraph/adopters/)
      * [ FAQ  ](https://langchain-ai.github.io/langgraph/concepts/faq/)
      * [ Troubleshooting  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraph/reference/graphs/)



Table of contents 

  * [ Setting up our project  ](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#setting-up-our-project)
  * [ Adding Authentication  ](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#adding-authentication)
  * [ Testing Our "Secure" Bot  ](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#testing-our-secure-bot)
  * [ What's Next?  ](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#whats-next)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ Tutorials  ](https://langchain-ai.github.io/langgraph/tutorials/)
  4. [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/concepts#langgraph-platform)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/tutorials/auth/getting_started.md "Edit this page")

# Setting up Custom Authentication (Part ⅓)[¶](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#setting-up-custom-authentication-part-13 "Permanent link")

This is part 1 of our authentication series:

  1. Basic Authentication (you are here) - Control who can access your bot
  2. [Resource Authorization](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/) - Let users have private conversations
  3. [Production Auth](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/) - Add real user accounts and validate using OAuth2



Prerequisites

This guide assumes basic familiarity with the following concepts:

  * [**Authentication & Access Control**](https://langchain-ai.github.io/langgraph/concepts/auth/)
  * [**LangGraph Platform**](https://langchain-ai.github.io/langgraph/concepts/#langgraph-platform)



Python only

We currently only support custom authentication and authorization in Python deployments with `langgraph-api>=0.0.11`. Support for LangGraph.JS will be added soon.

Support by deployment type

Custom auth is supported for all deployments in the **managed LangGraph Cloud** , as well as **Enterprise** self-hosted plans. It is not supported for **Lite** self-hosted plans.

In this tutorial, we will build a chatbot that only lets specific users access it. We'll start with the LangGraph template and add token-based security step by step. By the end, you'll have a working chatbot that checks for valid tokens before allowing access.

## Setting up our project[¶](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#setting-up-our-project "Permanent link")

First, let's create a new chatbot using the LangGraph starter template:

```
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-0-1)pipinstall-U"langgraph-cli[inmem]"
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-0-2)langgraphnew--template=new-langgraph-project-pythoncustom-auth
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-0-3)cdcustom-auth

```


The template gives us a placeholder LangGraph app. Let's try it out by installing the local dependencies and running the development server. 

```
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-1-1)pipinstall-e.
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-1-2)langgraphdev

```


If everything works, the server should start and open the studio in your browser. 

>   * 🚀 API: <http://127.0.0.1:2024>
>   * 🎨 Studio UI: <https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024>
>   * 📚 API Docs: <http://127.0.0.1:2024/docs>
> 

> 
> This in-memory server is designed for development and testing. For production use, please use LangGraph Cloud.

The graph should run, and if you were to self-host this on the public internet, anyone could access it!

![No auth](https://langchain-ai.github.io/langgraph/tutorials/auth/img/no_auth.png)

Now that we've seen the base LangGraph app, let's add authentication to it! 

Placeholder token

In part 1, we will start with a hard-coded token for illustration purposes. We will get to a "production-ready" authentication scheme in part 3, after mastering the basics.

## Adding Authentication[¶](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#adding-authentication "Permanent link")

The `Auth`[](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/#langgraph_sdk.auth.Auth) object lets you register an authentication function that the LangGraph platform will run on every request. This function receives each request and decides whether to accept or reject.

Create a new file `src/security/auth.py`. This is where our code will live to check if users are allowed to access our bot:

src/security/auth.py```
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-2-1)fromlanggraph_sdkimport Auth
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-2-2)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-2-3)# This is our toy user database. Do not do this in production
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-2-4)VALID_TOKENS = {
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-2-5)  "user1-token": {"id": "user1", "name": "Alice"},
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-2-6)  "user2-token": {"id": "user2", "name": "Bob"},
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-2-7)}
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-2-8)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-2-9)# The "Auth" object is a container that LangGraph will use to mark our authentication function
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-2-10)auth = Auth()
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-2-11)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-2-12)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-2-13)# The `authenticate` decorator tells LangGraph to call this function as middleware
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-2-14)# for every request. This will determine whether the request is allowed or not
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-2-15)@auth.authenticate
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-2-16)async defget_current_user(authorization: str | None) -> Auth.types.MinimalUserDict:
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-2-17)"""Check if the user's token is valid."""
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-2-18)  assert authorization
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-2-19)  scheme, token = authorization.split()
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-2-20)  assert scheme.lower() == "bearer"
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-2-21)  # Check if token is valid
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-2-22)  if token not in VALID_TOKENS:
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-2-23)    raise Auth.exceptions.HTTPException(status_code=401, detail="Invalid token")
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-2-24)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-2-25)  # Return user info if valid
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-2-26)  user_data = VALID_TOKENS[token]
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-2-27)  return {
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-2-28)    "identity": user_data["id"],
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-2-29)  }

```


Notice that our [authentication](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/#langgraph_sdk.auth.Auth.authenticate) handler does two important things:

  1. Checks if a valid token is provided in the request's [Authorization header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization)
  2. Returns the user's [identity](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/#langgraph_sdk.auth.types.MinimalUserDict)



Now tell LangGraph to use our authentication by adding the following to the `langgraph.json`[](https://langchain-ai.github.io/langgraph/cloud/reference/cli/#configuration-file) configuration:

langgraph.json```
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-3-1){
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-3-2)"dependencies":["."],
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-3-3)"graphs":{
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-3-4)"agent":"./src/agent/graph.py:graph"
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-3-5)},
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-3-6)"env":".env",
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-3-7)"auth":{
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-3-8)"path":"src/security/auth.py:auth"
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-3-9)}
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-3-10)}

```


## Testing Our "Secure" Bot[¶](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#testing-our-secure-bot "Permanent link")

Let's start the server again to test everything out!

```
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-4-1)langgraphdev--no-browser

```


Custom auth in the studio

If you didn't add the `--no-browser`, the studio UI will open in the browser. You may wonder, how is the studio able to still connect to our server? By default, we also permit access from the LangGraph studio, even when using custom auth. This makes it easier to develop and test your bot in the studio. You can remove this alternative authentication option by setting `disable_studio_auth: "true"` in your auth configuration: 

```
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-5-1){
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-5-2)"auth":{
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-5-3)"path":"src/security/auth.py:auth",
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-5-4)"disable_studio_auth":"true"
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-5-5)}
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-5-6)}

```


Now let's try to chat with our bot. If we've implemented authentication correctly, we should only be able to access the bot if we provide a valid token in the request header. Users will still, however, be able to access each other's resources until we add [resource authorization handlers](https://langchain-ai.github.io/langgraph/concepts/auth/#resource-authorization) in the next section of our tutorial.

![Authentication, no authorization handlers](https://langchain-ai.github.io/langgraph/tutorials/auth/img/authentication.png)

Run the following code in a file or notebook:

```
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-6-1)fromlanggraph_sdkimport get_client
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-6-2)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-6-3)# Try without a token (should fail)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-6-4)client = get_client(url="http://localhost:2024")
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-6-5)try:
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-6-6)  thread = await client.threads.create()
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-6-7)  print("❌ Should have failed without token!")
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-6-8)except Exception as e:
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-6-9)  print("✅ Correctly blocked access:", e)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-6-10)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-6-11)# Try with a valid token
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-6-12)client = get_client(
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-6-13)  url="http://localhost:2024", headers={"Authorization": "Bearer user1-token"}
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-6-14))
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-6-15)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-6-16)# Create a thread and chat
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-6-17)thread = await client.threads.create()
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-6-18)print(f"✅ Created thread as Alice: {thread['thread_id']}")
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-6-19)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-6-20)response = await client.runs.create(
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-6-21)  thread_id=thread["thread_id"],
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-6-22)  assistant_id="agent",
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-6-23)  input={"messages": [{"role": "user", "content": "Hello!"}]},
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-6-24))
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-6-25)print("✅ Bot responded:")
[](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__codelineno-6-26)print(response)

```


You should see that:

  1. Without a valid token, we can't access the bot
  2. With a valid token, we can create threads and chat



Congratulations! You've built a chatbot that only lets "authenticated" users access it. While this system doesn't (yet) implement a production-ready security scheme, we've learned the basic mechanics of how to control access to our bot. In the next tutorial, we'll learn how to give each user their own private conversations.

## What's Next?[¶](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#whats-next "Permanent link")

Now that you can control who accesses your bot, you might want to:

  1. Continue the tutorial by going to [Making Conversations Private (Part ⅔)](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/) to learn about resource authorization.
  2. Read more about [authentication concepts](https://langchain-ai.github.io/langgraph/concepts/auth/).
  3. Check out the [API reference](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/) for more authentication details.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Complex data extraction with function calling  ](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/) [ Next  Making Conversations Private (Part ⅔)  ](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
