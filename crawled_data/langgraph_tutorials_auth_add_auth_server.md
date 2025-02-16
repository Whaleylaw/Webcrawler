---
url: https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#connecting-an-authentication-provider-part-33)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Connecting an Authentication Provider (Part 3/3) 

[ ](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/?q= "Share")

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
          * [ Setting up Custom Authentication (Part ⅓)  ](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/)
          * [ Making Conversations Private (Part ⅔)  ](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/)
          * Connecting an Authentication Provider (Part 3/3)  [ Connecting an Authentication Provider (Part 3/3)  ](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/) Table of contents 
            * [ Requirements  ](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#requirements)
            * [ Background  ](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#background)
            * [ Setting Up Authentication Provider  ](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#setup-auth-provider)
            * [ Implementing Token Validation  ](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#implementing-token-validation)
            * [ Testing Authentication Flow  ](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#testing-authentication-flow)
            * [ Congratulations! 🎉  ](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#congratulations)
            * [ What's Next?  ](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#whats-next)
    * Resources  Resources 
      * [ Prebuilt Agents  ](https://langchain-ai.github.io/langgraph/prebuilt/)
      * [ Adopters  ](https://langchain-ai.github.io/langgraph/adopters/)
      * [ FAQ  ](https://langchain-ai.github.io/langgraph/concepts/faq/)
      * [ Troubleshooting  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraph/reference/graphs/)



Table of contents 

  * [ Requirements  ](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#requirements)
  * [ Background  ](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#background)
  * [ Setting Up Authentication Provider  ](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#setup-auth-provider)
  * [ Implementing Token Validation  ](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#implementing-token-validation)
  * [ Testing Authentication Flow  ](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#testing-authentication-flow)
  * [ Congratulations! 🎉  ](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#congratulations)
  * [ What's Next?  ](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#whats-next)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ Tutorials  ](https://langchain-ai.github.io/langgraph/tutorials/)
  4. [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/concepts#langgraph-platform)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/tutorials/auth/add_auth_server.md "Edit this page")

# Connecting an Authentication Provider (Part 3/3)[¶](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#connecting-an-authentication-provider-part-33 "Permanent link")

This is part 3 of our authentication series:

  1. [Basic Authentication](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/) - Control who can access your bot
  2. [Resource Authorization](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/) - Let users have private conversations
  3. Production Auth (you are here) - Add real user accounts and validate using OAuth2



In the [Making Conversations Private](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/) tutorial, we added [resource authorization](https://langchain-ai.github.io/langgraph/concepts/auth/#resource-authorization) to give users private conversations. However, we were still using hard-coded tokens for authentication, which is not secure. Now we'll replace those tokens with real user accounts using [OAuth2](https://langchain-ai.github.io/langgraph/concepts/auth/#oauth2-authentication).

We'll keep the same `Auth`[](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/#langgraph_sdk.auth.Auth) object and [resource-level access control](https://langchain-ai.github.io/langgraph/concepts/auth/#resource-level-access-control), but upgrade our authentication to use Supabase as our identity provider. While we use Supabase in this tutorial, the concepts apply to any OAuth2 provider. You'll learn how to:

  1. Replace test tokens with real [JWT tokens](https://langchain-ai.github.io/langgraph/concepts/auth/#jwt-tokens)
  2. Integrate with OAuth2 providers for secure user authentication
  3. Handle user sessions and metadata while maintaining our existing authorization logic



## Requirements[¶](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#requirements "Permanent link")

You will need to set up a Supabase project to use its authentication server for this tutorial. You can do so [here](https://supabase.com/dashboard).

## Background[¶](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#background "Permanent link")

OAuth2 involves three main roles:

  1. **Authorization server** : The identity provider (e.g., Supabase, Auth0, Google) that handles user authentication and issues tokens
  2. **Application backend** : Your LangGraph application. This validates tokens and serves protected resources (conversation data)
  3. **Client application** : The web or mobile app where users interact with your service



A standard OAuth2 flow works something like this:

In the following example, we'll use Supabase as our auth server. The LangGraph application will provide the backend for your app, and we will write test code for the client app. Let's get started!

## Setting Up Authentication Provider[¶](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#setup-auth-provider "Permanent link")

First, let's install the required dependencies. Start in your `custom-auth` directory and ensure you have the `langgraph-cli` installed:

```
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-0-1)cdcustom-auth
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-0-2)pipinstall-U"langgraph-cli[inmem]"

```


Next, we'll need to fech the URL of our auth server and the private key for authentication. Since we're using Supabase for this, we can do this in the Supabase dashboard:

  1. In the left sidebar, click on t️⚙ Project Settings" and then click "API"
  2. Copy your project URL and add it to your `.env` file



```
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-1-1)echo"SUPABASE_URL=your-project-url">>.env

```


3. Next, copy your service role secret key and add it to your `.env` file 

```
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-2-1)echo"SUPABASE_SERVICE_KEY=your-service-role-key">>.env

```


4. Finally, copy your "anon public" key and note it down. This will be used later when we set up our client code. 

```
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-3-1)SUPABASE_URL=your-project-url
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-3-2)SUPABASE_SERVICE_KEY=your-service-role-key

```


## Implementing Token Validation[¶](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#implementing-token-validation "Permanent link")

In the previous tutorials, we used the `Auth`[](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/#langgraph_sdk.auth.Auth) object to:

  1. Validate hard-coded tokens in the [authentication tutorial](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/)
  2. Add resource ownership in the [authorization tutorial](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/)



Now we'll upgrade our authentication to validate real JWT tokens from Supabase. The key changes will all be in the `@auth.authenticate`[](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/#langgraph_sdk.auth.Auth.authenticate) decorated function:

  1. Instead of checking against a hard-coded list of tokens, we'll make an HTTP request to Supabase to validate the token
  2. We'll extract real user information (ID, email) from the validated token



And we'll keep our existing resource authorization logic unchanged

Let's update `src/security/auth.py` to implement this:

src/security/auth.py```
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-4-1)importos
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-4-2)importhttpx
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-4-3)fromlanggraph_sdkimport Auth
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-4-4)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-4-5)auth = Auth()
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-4-6)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-4-7)# This is loaded from the `.env` file you created above
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-4-8)SUPABASE_URL = os.environ["SUPABASE_URL"]
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-4-9)SUPABASE_SERVICE_KEY = os.environ["SUPABASE_SERVICE_KEY"]
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-4-10)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-4-11)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-4-12)@auth.authenticate
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-4-13)async defget_current_user(authorization: str | None):
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-4-14)"""Validate JWT tokens and extract user information."""
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-4-15)  assert authorization
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-4-16)  scheme, token = authorization.split()
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-4-17)  assert scheme.lower() == "bearer"
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-4-18)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-4-19)  try:
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-4-20)    # Verify token with auth provider
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-4-21)    async with httpx.AsyncClient() as client:
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-4-22)      response = await client.get(
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-4-23)        f"{SUPABASE_URL}/auth/v1/user",
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-4-24)        headers={
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-4-25)          "Authorization": authorization,
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-4-26)          "apiKey": SUPABASE_SERVICE_KEY,
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-4-27)        },
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-4-28)      )
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-4-29)      assert response.status_code == 200
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-4-30)      user = response.json()
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-4-31)      return {
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-4-32)        "identity": user["id"], # Unique user identifier
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-4-33)        "email": user["email"],
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-4-34)        "is_authenticated": True,
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-4-35)      }
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-4-36)  except Exception as e:
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-4-37)    raise Auth.exceptions.HTTPException(status_code=401, detail=str(e))
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-4-38)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-4-39)# ... the rest is the same as before
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-4-40)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-4-41)# Keep our resource authorization from the previous tutorial
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-4-42)@auth.on
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-4-43)async defadd_owner(ctx, value):
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-4-44)"""Make resources private to their creator using resource metadata."""
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-4-45)  filters = {"owner": ctx.user.identity}
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-4-46)  metadata = value.setdefault("metadata", {})
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-4-47)  metadata.update(filters)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-4-48)  return filters

```


The most important change is that we're now validating tokens with a real authentication server. Our authentication handler has the private key for our Supabase project, which we can use to validate the user's token and extract their information.

Let's test this with a real user account!

## Testing Authentication Flow[¶](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#testing-authentication-flow "Permanent link")

Let's test out our new authentication flow. You can run the following code in a file or notebook. You will need to provide:

  * A valid email address
  * A Supabase project URL (from [above](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#setup-auth-provider))
  * A Supabase anon **public key** (also from [above](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#setup-auth-provider))



```
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-5-1)importos
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-5-2)importhttpx
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-5-3)fromgetpassimport getpass
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-5-4)fromlanggraph_sdkimport get_client
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-5-5)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-5-6)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-5-7)# Get email from command line
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-5-8)email = getpass("Enter your email: ")
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-5-9)base_email = email.split("@")
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-5-10)password = "secure-password" # CHANGEME
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-5-11)email1 = f"{base_email[0]}+1@{base_email[1]}"
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-5-12)email2 = f"{base_email[0]}+2@{base_email[1]}"
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-5-13)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-5-14)SUPABASE_URL = os.environ.get("SUPABASE_URL")
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-5-15)if not SUPABASE_URL:
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-5-16)  SUPABASE_URL = getpass("Enter your Supabase project URL: ")
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-5-17)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-5-18)# This is your PUBLIC anon key (which is safe to use client-side)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-5-19)# Do NOT mistake this for the secret service role key
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-5-20)SUPABASE_ANON_KEY = os.environ.get("SUPABASE_ANON_KEY")
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-5-21)if not SUPABASE_ANON_KEY:
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-5-22)  SUPABASE_ANON_KEY = getpass("Enter your public Supabase anon key: ")
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-5-23)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-5-24)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-5-25)async defsign_up(email: str, password: str):
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-5-26)"""Create a new user account."""
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-5-27)  async with httpx.AsyncClient() as client:
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-5-28)    response = await client.post(
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-5-29)      f"{SUPABASE_URL}/auth/v1/signup",
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-5-30)      json={"email": email, "password": password},
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-5-31)      headers={"apiKey": SUPABASE_ANON_KEY},
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-5-32)    )
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-5-33)    assert response.status_code == 200
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-5-34)    return response.json()
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-5-35)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-5-36)# Create two test users
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-5-37)print(f"Creating test users: {email1} and {email2}")
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-5-38)await sign_up(email1, password)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-5-39)await sign_up(email2, password)

```


Then run the code.

About test emails

We'll create two test accounts by adding "+1" and "+2" to your email. For example, if you use "myemail@gmail.com", we'll create "myemail+1@gmail.com" and "myemail+2@gmail.com". All emails will be delivered to your original address.

⚠️ Before continuing: Check your email and click both confirmation links. Supabase will will reject `/login` requests until after you have confirmed your users' email.

Now let's test that users can only see their own data. Make sure the server is running (run `langgraph dev`) before proceeding. The following snippet requires the "anon public" key that you copied from the Supabase dashboard while [setting up the auth provider](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#setup-auth-provider) previously. 

```
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-6-1)async deflogin(email: str, password: str):
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-6-2)"""Get an access token for an existing user."""
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-6-3)  async with httpx.AsyncClient() as client:
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-6-4)    response = await client.post(
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-6-5)      f"{SUPABASE_URL}/auth/v1/token?grant_type=password",
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-6-6)      json={
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-6-7)        "email": email,
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-6-8)        "password": password
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-6-9)      },
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-6-10)      headers={
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-6-11)        "apikey": SUPABASE_ANON_KEY,
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-6-12)        "Content-Type": "application/json"
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-6-13)      },
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-6-14)    )
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-6-15)    assert response.status_code == 200
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-6-16)    return response.json()["access_token"]
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-6-17)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-6-18)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-6-19)# Log in as user 1
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-6-20)user1_token = await login(email1, password)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-6-21)user1_client = get_client(
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-6-22)  url="http://localhost:2024", headers={"Authorization": f"Bearer {user1_token}"}
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-6-23))
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-6-24)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-6-25)# Create a thread as user 1
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-6-26)thread = await user1_client.threads.create()
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-6-27)print(f"✅ User 1 created thread: {thread['thread_id']}")
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-6-28)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-6-29)# Try to access without a token
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-6-30)unauthenticated_client = get_client(url="http://localhost:2024")
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-6-31)try:
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-6-32)  await unauthenticated_client.threads.create()
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-6-33)  print("❌ Unauthenticated access should fail!")
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-6-34)except Exception as e:
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-6-35)  print("✅ Unauthenticated access blocked:", e)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-6-36)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-6-37)# Try to access user 1's thread as user 2
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-6-38)user2_token = await login(email2, password)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-6-39)user2_client = get_client(
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-6-40)  url="http://localhost:2024", headers={"Authorization": f"Bearer {user2_token}"}
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-6-41))
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-6-42)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-6-43)try:
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-6-44)  await user2_client.threads.get(thread["thread_id"])
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-6-45)  print("❌ User 2 shouldn't see User 1's thread!")
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-6-46)except Exception as e:
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-6-47)  print("✅ User 2 blocked from User 1's thread:", e)

```


The output should look like this: 

```
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-7-1)✅User1createdthread:d6af3754-95df-4176-aa10-dbd8dca40f1a
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-7-2)✅Unauthenticatedaccessblocked:Clienterror'403 Forbidden'forurl'http://localhost:2024/threads'
[](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__codelineno-7-3)✅User2blockedfromUser1's thread: Client error '404NotFound' for url 'http://localhost:2024/threads/d6af3754-95df-4176-aa10-dbd8dca40f1a'

```


Perfect! Our authentication and authorization are working together: 1. Users must log in to access the bot 2. Each user can only see their own threads

All our users are managed by the Supabase auth provider, so we don't need to implement any additional user management logic.

## Congratulations! 🎉[¶](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#congratulations "Permanent link")

You've successfully built a production-ready authentication system for your LangGraph application! Let's review what you've accomplished:

  1. Set up an authentication provider (Supabase in this case)
  2. Added real user accounts with email/password authentication
  3. Integrated JWT token validation into your LangGraph server
  4. Implemented proper authorization to ensure users can only access their own data
  5. Created a foundation that's ready to handle your next authentication challenge 🚀



This completes our authentication tutorial series. You now have the building blocks for a secure, production-ready LangGraph application.

## What's Next?[¶](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#whats-next "Permanent link")

Now that you have production authentication, consider:

  1. Building a web UI with your preferred framework (see the [Custom Auth](https://github.com/langchain-ai/custom-auth) template for an example)
  2. Learn more about the other aspects of authentication and authorization in the [conceptual guide on authentication](https://langchain-ai.github.io/langgraph/concepts/auth/).
  3. Customize your handlers and setup further after reading the [reference docs](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/#langgraph_sdk.auth.Auth).

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Making Conversations Private (Part ⅔)  ](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/) [ Next  Prebuilt Agents  ](https://langchain-ai.github.io/langgraph/prebuilt/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
