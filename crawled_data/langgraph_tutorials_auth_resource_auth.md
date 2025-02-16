---
url: https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#making-conversations-private-part-23)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Making Conversations Private (Part ⅔) 

[ ](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/?q= "Share")

Initializing search 

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
          * Making Conversations Private (Part ⅔)  [ Making Conversations Private (Part ⅔)  ](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/) Table of contents 
            * [ Understanding Resource Authorization  ](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#understanding-resource-authorization)
            * [ Adding Resource Authorization  ](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#adding-resource-authorization)
            * [ Testing Private Conversations  ](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#testing-private-conversations)
            * [ Adding scoped authorization handlers  ](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#scoped-authorization)
            * [ What's Next?  ](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#whats-next)
          * [ Connecting an Authentication Provider (Part 3/3)  ](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/)
    * Resources  Resources 
      * [ Prebuilt Agents  ](https://langchain-ai.github.io/langgraph/prebuilt/)
      * [ Adopters  ](https://langchain-ai.github.io/langgraph/adopters/)
      * [ FAQ  ](https://langchain-ai.github.io/langgraph/concepts/faq/)
      * [ Troubleshooting  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraph/reference/graphs/)



Table of contents 

  * [ Understanding Resource Authorization  ](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#understanding-resource-authorization)
  * [ Adding Resource Authorization  ](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#adding-resource-authorization)
  * [ Testing Private Conversations  ](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#testing-private-conversations)
  * [ Adding scoped authorization handlers  ](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#scoped-authorization)
  * [ What's Next?  ](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#whats-next)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ Tutorials  ](https://langchain-ai.github.io/langgraph/tutorials/)
  4. [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/concepts#langgraph-platform)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/tutorials/auth/resource_auth.md "Edit this page")

# Making Conversations Private (Part ⅔)[¶](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#making-conversations-private-part-23 "Permanent link")

This is part 2 of our authentication series:

  1. [Basic Authentication](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/) - Control who can access your bot 
  2. Resource Authorization (you are here) - Let users have private conversations
  3. [Production Auth](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/) - Add real user accounts and validate using OAuth2



In this tutorial, we will extend our chatbot to give each user their own private conversations. We'll add [resource-level access control](https://langchain-ai.github.io/langgraph/concepts/auth/#resource-level-access-control) so users can only see their own threads.

![Authorization handlers](https://langchain-ai.github.io/langgraph/tutorials/auth/img/authorization.png)

Placeholder token

As we did in [part 1](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/), for this section, we will use a hard-coded token for illustration purposes. We will get to a "production-ready" authentication scheme in part 3, after mastering the basics.

## Understanding Resource Authorization[¶](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#understanding-resource-authorization "Permanent link")

In the last tutorial, we controlled who could access our bot. But right now, any authenticated user can see everyone else's conversations! Let's fix that by adding [resource authorization](https://langchain-ai.github.io/langgraph/concepts/auth/#resource-authorization).

First, make sure you have completed the [Basic Authentication](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/) tutorial and that your secure bot can be run without errors:

```
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-0-1)cdcustom-auth
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-0-2)pipinstall-e.
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-0-3)langgraphdev--no-browser

```


>   * 🚀 API: <http://127.0.0.1:2024>
>   * 🎨 Studio UI: <https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024>
>   * 📚 API Docs: <http://127.0.0.1:2024/docs>
> 


## Adding Resource Authorization[¶](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#adding-resource-authorization "Permanent link")

Recall that in the last tutorial, the `Auth`[](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/#langgraph_sdk.auth.Auth) object let us register an [authentication function](https://langchain-ai.github.io/langgraph/concepts/auth/#authentication), which the LangGraph platform uses to validate the bearer tokens in incoming requests. Now we'll use it to register an **authorization** handler.

Authorization handlers are functions that run **after** authentication succeeds. These handlers can add [metadata](https://langchain-ai.github.io/langgraph/concepts/auth/#resource-metadata) to resources (like who owns them) and filter what each user can see.

Let's update our `src/security/auth.py` and add one authorization handler that is run on every request:

src/security/auth.py```
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-1)fromlanggraph_sdkimport Auth
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-2)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-3)# Keep our test users from the previous tutorial
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-4)VALID_TOKENS = {
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-5)  "user1-token": {"id": "user1", "name": "Alice"},
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-6)  "user2-token": {"id": "user2", "name": "Bob"},
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-7)}
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-8)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-9)auth = Auth()
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-10)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-11)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-12)@auth.authenticate
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-13)async defget_current_user(authorization: str | None) -> Auth.types.MinimalUserDict:
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-14)"""Our authentication handler from the previous tutorial."""
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-15)  assert authorization
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-16)  scheme, token = authorization.split()
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-17)  assert scheme.lower() == "bearer"
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-18)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-19)  if token not in VALID_TOKENS:
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-20)    raise Auth.exceptions.HTTPException(status_code=401, detail="Invalid token")
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-21)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-22)  user_data = VALID_TOKENS[token]
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-23)  return {
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-24)    "identity": user_data["id"],
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-25)  }
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-26)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-27)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-28)@auth.on
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-29)async defadd_owner(
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-30)  ctx: Auth.types.AuthContext, # Contains info about the current user
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-31)  value: dict, # The resource being created/accessed
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-32)):
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-33)"""Make resources private to their creator."""
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-34)  # Examples:
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-35)  # ctx: AuthContext(
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-36)  #   permissions=[],
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-37)  #   user=ProxyUser(
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-38)  #     identity='user1',
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-39)  #     is_authenticated=True,
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-40)  #     display_name='user1'
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-41)  #   ),
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-42)  #   resource='threads',
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-43)  #   action='create_run'
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-44)  # )
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-45)  # value: 
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-46)  # {
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-47)  #   'thread_id': UUID('1e1b2733-303f-4dcd-9620-02d370287d72'),
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-48)  #   'assistant_id': UUID('fe096781-5601-53d2-b2f6-0d3403f7e9ca'),
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-49)  #   'run_id': UUID('1efbe268-1627-66d4-aa8d-b956b0f02a41'),
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-50)  #   'status': 'pending',
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-51)  #   'metadata': {},
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-52)  #   'prevent_insert_if_inflight': True,
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-53)  #   'multitask_strategy': 'reject',
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-54)  #   'if_not_exists': 'reject',
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-55)  #   'after_seconds': 0,
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-56)  #   'kwargs': {
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-57)  #     'input': {'messages': [{'role': 'user', 'content': 'Hello!'}]},
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-58)  #     'command': None,
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-59)  #     'config': {
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-60)  #       'configurable': {
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-61)  #         'langgraph_auth_user': ... Your user object...
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-62)  #         'langgraph_auth_user_id': 'user1'
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-63)  #       }
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-64)  #     },
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-65)  #     'stream_mode': ['values'],
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-66)  #     'interrupt_before': None,
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-67)  #     'interrupt_after': None,
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-68)  #     'webhook': None,
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-69)  #     'feedback_keys': None,
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-70)  #     'temporary': False,
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-71)  #     'subgraphs': False
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-72)  #   }
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-73)  # }
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-74)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-75)  # Do 2 things:
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-76)  # 1. Add the user's ID to the resource's metadata. Each LangGraph resource has a `metadata` dict that persists with the resource.
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-77)  # this metadata is useful for filtering in read and update operations
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-78)  # 2. Return a filter that lets users only see their own resources
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-79)  filters = {"owner": ctx.user.identity}
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-80)  metadata = value.setdefault("metadata", {})
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-81)  metadata.update(filters)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-82)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-83)  # Only let users see their own resources
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-1-84)  return filters

```


The handler receives two parameters:

  1. `ctx` ([AuthContext](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/#langgraph_sdk.auth.types.AuthContext)): contains info about the current `user`, the user's `permissions`, the `resource` ("threads", "crons", "assistants"), and the `action` being taken ("create", "read", "update", "delete", "search", "create_run")
  2. `value` (`dict`): data that is being created or accessed. The contents of this dict depend on the resource and action being accessed. See [adding scoped authorization handlers](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#scoped-authorization) below for information on how to get more tightly scoped access control.



Notice that our simple handler does two things:

  1. Adds the user's ID to the resource's metadata.
  2. Returns a metadata filter so users only see resources they own.



## Testing Private Conversations[¶](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#testing-private-conversations "Permanent link")

Let's test our authorization. If we have set things up correctly, we should expect to see all ✅ messages. Be sure to have your development server running (run `langgraph dev`):

```
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-2-1)fromlanggraph_sdkimport get_client
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-2-2)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-2-3)# Create clients for both users
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-2-4)alice = get_client(
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-2-5)  url="http://localhost:2024",
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-2-6)  headers={"Authorization": "Bearer user1-token"}
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-2-7))
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-2-8)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-2-9)bob = get_client(
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-2-10)  url="http://localhost:2024",
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-2-11)  headers={"Authorization": "Bearer user2-token"}
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-2-12))
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-2-13)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-2-14)# Alice creates an assistant
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-2-15)alice_assistant = await alice.assistants.create()
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-2-16)print(f"✅ Alice created assistant: {alice_assistant['assistant_id']}")
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-2-17)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-2-18)# Alice creates a thread and chats
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-2-19)alice_thread = await alice.threads.create()
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-2-20)print(f"✅ Alice created thread: {alice_thread['thread_id']}")
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-2-21)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-2-22)await alice.runs.create(
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-2-23)  thread_id=alice_thread["thread_id"],
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-2-24)  assistant_id="agent",
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-2-25)  input={"messages": [{"role": "user", "content": "Hi, this is Alice's private chat"}]}
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-2-26))
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-2-27)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-2-28)# Bob tries to access Alice's thread
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-2-29)try:
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-2-30)  await bob.threads.get(alice_thread["thread_id"])
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-2-31)  print("❌ Bob shouldn't see Alice's thread!")
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-2-32)except Exception as e:
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-2-33)  print("✅ Bob correctly denied access:", e)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-2-34)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-2-35)# Bob creates his own thread
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-2-36)bob_thread = await bob.threads.create()
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-2-37)await bob.runs.create(
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-2-38)  thread_id=bob_thread["thread_id"],
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-2-39)  assistant_id="agent",
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-2-40)  input={"messages": [{"role": "user", "content": "Hi, this is Bob's private chat"}]}
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-2-41))
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-2-42)print(f"✅ Bob created his own thread: {bob_thread['thread_id']}")
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-2-43)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-2-44)# List threads - each user only sees their own
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-2-45)alice_threads = await alice.threads.search()
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-2-46)bob_threads = await bob.threads.search()
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-2-47)print(f"✅ Alice sees {len(alice_threads)} thread")
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-2-48)print(f"✅ Bob sees {len(bob_threads)} thread")

```


Run the test code and you should see output like this:

```
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-3-1)✅Alicecreatedassistant:fc50fb08-78da-45a9-93cc-1d3928a3fc37
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-3-2)✅Alicecreatedthread:533179b7-05bc-4d48-b47a-a83cbdb5781d
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-3-3)✅Bobcorrectlydeniedaccess:Clienterror'404 Not Found'forurl'http://localhost:2024/threads/533179b7-05bc-4d48-b47a-a83cbdb5781d'
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-3-4)Formoreinformationcheck:https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-3-5)✅Bobcreatedhisownthread:437c36ed-dd45-4a1e-b484-28ba6eca8819
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-3-6)✅Alicesees1thread
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-3-7)✅Bobsees1thread

```


This means:

  1. Each user can create and chat in their own threads
  2. Users can't see each other's threads
  3. Listing threads only shows your own



## Adding scoped authorization handlers[¶](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#scoped-authorization "Permanent link")

The broad `@auth.on` handler matches on all [authorization events](https://langchain-ai.github.io/langgraph/concepts/auth/#authorization-events). This is concise, but it means the contents of the `value` dict are not well-scoped, and we apply the same user-level access control to every resource. If we want to be more fine-grained, we can also control specific actions on resources.

Update `src/security/auth.py` to add handlers for specific resource types:

```
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-1)# Keep our previous handlers...
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-2)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-3)fromlanggraph_sdkimport Auth
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-4)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-5)@auth.on.threads.create
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-6)async defon_thread_create(
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-7)  ctx: Auth.types.AuthContext,
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-8)  value: Auth.types.on.threads.create.value,
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-9)):
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-10)"""Add owner when creating threads.
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-11)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-12)  This handler runs when creating new threads and does two things:
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-13)  1. Sets metadata on the thread being created to track ownership
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-14)  2. Returns a filter that ensures only the creator can access it
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-15)  """
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-16)  # Example value:
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-17)  # {'thread_id': UUID('99b045bc-b90b-41a8-b882-dabc541cf740'), 'metadata': {}, 'if_exists': 'raise'}
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-18)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-19)  # Add owner metadata to the thread being created
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-20)  # This metadata is stored with the thread and persists
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-21)  metadata = value.setdefault("metadata", {})
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-22)  metadata["owner"] = ctx.user.identity
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-23)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-24)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-25)  # Return filter to restrict access to just the creator
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-26)  return {"owner": ctx.user.identity}
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-27)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-28)@auth.on.threads.read
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-29)async defon_thread_read(
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-30)  ctx: Auth.types.AuthContext,
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-31)  value: Auth.types.on.threads.read.value,
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-32)):
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-33)"""Only let users read their own threads.
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-34)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-35)  This handler runs on read operations. We don't need to set
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-36)  metadata since the thread already exists - we just need to
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-37)  return a filter to ensure users can only see their own threads.
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-38)  """
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-39)  return {"owner": ctx.user.identity}
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-40)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-41)@auth.on.assistants
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-42)async defon_assistants(
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-43)  ctx: Auth.types.AuthContext,
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-44)  value: Auth.types.on.assistants.value,
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-45)):
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-46)  # For illustration purposes, we will deny all requests
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-47)  # that touch the assistants resource
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-48)  # Example value:
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-49)  # {
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-50)  #   'assistant_id': UUID('63ba56c3-b074-4212-96e2-cc333bbc4eb4'),
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-51)  #   'graph_id': 'agent',
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-52)  #   'config': {},
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-53)  #   'metadata': {},
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-54)  #   'name': 'Untitled'
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-55)  # }
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-56)  raise Auth.exceptions.HTTPException(
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-57)    status_code=403,
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-58)    detail="User lacks the required permissions.",
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-59)  )
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-60)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-61)# Assumes you organize information in store like (user_id, resource_type, resource_id)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-62)@auth.on.store()
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-63)async defauthorize_store(ctx: Auth.types.AuthContext, value: dict):
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-64)  # The "namespace" field for each store item is a tuple you can think of as the directory of an item.
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-65)  namespace: tuple = value["namespace"]
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-4-66)  assert namespace[0] == ctx.user.identity, "Not authorized"

```


Notice that instead of one global handler, we now have specific handlers for:

  1. Creating threads
  2. Reading threads
  3. Accessing assistants



The first three of these match specific **actions** on each resource (see [resource actions](https://langchain-ai.github.io/langgraph/concepts/auth/#resource-actions)), while the last one (`@auth.on.assistants`) matches _any_ action on the `assistants` resource. For each request, LangGraph will run the most specific handler that matches the resource and action being accessed. This means that the four handlers above will run rather than the broadly scoped "`@auth.on`" handler.

Try adding the following test code to your test file:

```
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-5-1)# ... Same as before
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-5-2)# Try creating an assistant. This should fail
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-5-3)try:
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-5-4)  await alice.assistants.create("agent")
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-5-5)  print("❌ Alice shouldn't be able to create assistants!")
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-5-6)except Exception as e:
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-5-7)  print("✅ Alice correctly denied access:", e)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-5-8)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-5-9)# Try searching for assistants. This also should fail
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-5-10)try:
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-5-11)  await alice.assistants.search()
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-5-12)  print("❌ Alice shouldn't be able to search assistants!")
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-5-13)except Exception as e:
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-5-14)  print("✅ Alice correctly denied access to searching assistants:", e)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-5-15)
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-5-16)# Alice can still create threads
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-5-17)alice_thread = await alice.threads.create()
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-5-18)print(f"✅ Alice created thread: {alice_thread['thread_id']}")

```


And then run the test code again:

```
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-6-1)✅Alicecreatedthread:dcea5cd8-eb70-4a01-a4b6-643b14e8f754
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-6-2)✅Bobcorrectlydeniedaccess:Clienterror'404 Not Found'forurl'http://localhost:2024/threads/dcea5cd8-eb70-4a01-a4b6-643b14e8f754'
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-6-3)Formoreinformationcheck:https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-6-4)✅Bobcreatedhisownthread:400f8d41-e946-429f-8f93-4fe395bc3eed
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-6-5)✅Alicesees1thread
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-6-6)✅Bobsees1thread
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-6-7)✅Alicecorrectlydeniedaccess:
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-6-8)Formoreinformationcheck:https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500
[](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__codelineno-6-9)✅Alicecorrectlydeniedaccesstosearchingassistants:

```


Congratulations! You've built a chatbot where each user has their own private conversations. While this system uses simple token-based authentication, the authorization patterns we've learned will work with implementing any real authentication system. In the next tutorial, we'll replace our test users with real user accounts using OAuth2.

## What's Next?[¶](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#whats-next "Permanent link")

Now that you can control access to resources, you might want to:

  1. Move on to [Production Auth](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/) to add real user accounts
  2. Read more about [authorization patterns](https://langchain-ai.github.io/langgraph/concepts/auth/#authorization)
  3. Check out the [API reference](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/#langgraph_sdk.auth.Auth) for details about the interfaces and methods used in this tutorial

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Setting up Custom Authentication (Part ⅓)  ](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/) [ Next  Connecting an Authentication Provider (Part 3/3)  ](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
