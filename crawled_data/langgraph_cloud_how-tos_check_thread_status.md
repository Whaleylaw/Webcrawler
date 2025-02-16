---
url: https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#check-the-status-of-your-threads)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Check the Status of your Threads 

[ ](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/?q= "Share")

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

How-to Guides 
        * [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
        * LangGraph Platform  LangGraph Platform 
          * [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph-platform)
          * [ Application Structure  ](https://langchain-ai.github.io/langgraph/how-tos#application-structure)
          * [ Deployment  ](https://langchain-ai.github.io/langgraph/how-tos#deployment)
          * [ Authentication & Access Control  ](https://langchain-ai.github.io/langgraph/how-tos#authentication-access-control)
          * [ Assistants  ](https://langchain-ai.github.io/langgraph/how-tos#assistants)
          * Threads  Threads 
            * [ Threads  ](https://langchain-ai.github.io/langgraph/how-tos#threads)
            * [ Copying Threads  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/copy_threads/)
            * Check the Status of your Threads  [ Check the Status of your Threads  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#setup)
                * [ SDK initialization  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#sdk-initialization)
              * [ Find idle threads  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#find-idle-threads)
              * [ Find interrupted threads  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#find-interrupted-threads)
              * [ Find busy threads  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#find-busy-threads)
              * [ Find specific threads  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#find-specific-threads)
                * [ Find by ID  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#find-by-id)
                * [ Find by metadata  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#find-by-metadata)
          * [ Runs  ](https://langchain-ai.github.io/langgraph/how-tos#runs)
          * [ Streaming  ](https://langchain-ai.github.io/langgraph/how-tos#streaming_1)
          * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraph/how-tos#human-in-the-loop_1)
          * [ Double-texting  ](https://langchain-ai.github.io/langgraph/how-tos#double-texting)
          * [ Webhooks  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/webhooks/)
          * [ Cron Jobs  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/cron_jobs/)
          * [ LangGraph Studio  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph-studio)
      * [ Concepts  ](https://langchain-ai.github.io/langgraph/concepts/)
      * [ Tutorials  ](https://langchain-ai.github.io/langgraph/tutorials/)
    * Resources  Resources 
      * [ Prebuilt Agents  ](https://langchain-ai.github.io/langgraph/prebuilt/)
      * [ Adopters  ](https://langchain-ai.github.io/langgraph/adopters/)
      * [ FAQ  ](https://langchain-ai.github.io/langgraph/concepts/faq/)
      * [ Troubleshooting  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraph/reference/graphs/)



Table of contents 

  * [ Setup  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#setup)
    * [ SDK initialization  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#sdk-initialization)
  * [ Find idle threads  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#find-idle-threads)
  * [ Find interrupted threads  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#find-interrupted-threads)
  * [ Find busy threads  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#find-busy-threads)
  * [ Find specific threads  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#find-specific-threads)
    * [ Find by ID  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#find-by-id)
    * [ Find by metadata  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#find-by-metadata)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph-platform)
  5. [ Threads  ](https://langchain-ai.github.io/langgraph/how-tos#threads)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/cloud/how-tos/check_thread_status.md "Edit this page")

# Check the Status of your Threads[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#check-the-status-of-your-threads "Permanent link")

## Setup[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#setup "Permanent link")

To start, we can setup our client with whatever URL you are hosting your graph from:

### SDK initialization[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#sdk-initialization "Permanent link")

First, we need to setup our client so that we can communicate with our hosted graph:

[Python](#__tabbed_1_1)[Javascript](#__tabbed_1_2)[CURL](#__tabbed_1_3)

```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__codelineno-0-1)fromlanggraph_sdkimport get_client
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__codelineno-0-2)client = get_client(url=<DEPLOYMENT_URL>)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__codelineno-0-3)# Using the graph deployed with the name "agent"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__codelineno-0-4)assistant_id = "agent"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__codelineno-0-5)thread = await client.threads.create()

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__codelineno-1-1)import{Client}from"@langchain/langgraph-sdk";
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__codelineno-1-2)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__codelineno-1-3)constclient=newClient({apiUrl:<DEPLOYMENT_URL>});
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__codelineno-1-4)// Using the graph deployed with the name "agent"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__codelineno-1-5)constassistantId="agent";
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__codelineno-1-6)constthread=awaitclient.threads.create();

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__codelineno-2-1)curl--requestPOST\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__codelineno-2-2)--url<DEPLOYMENT_URL>/threads\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__codelineno-2-3)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__codelineno-2-4)--data'{}'

```


## Find idle threads[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#find-idle-threads "Permanent link")

We can use the following commands to find threads that are idle, which means that all runs executed on the thread have finished running:

[Python](#__tabbed_2_1)[Javascript](#__tabbed_2_2)[CURL](#__tabbed_2_3)

```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__codelineno-3-1)print(await client.threads.search(status="idle",limit=1))

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__codelineno-4-1)console.log(awaitclient.threads.search({status:"idle",limit:1}));

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__codelineno-5-1)curl--requestPOST\ 
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__codelineno-5-2)--url<DEPLOYMENT_URL>/threads/search\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__codelineno-5-3)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__codelineno-5-4)--data'{"status": "idle", "limit": 1}'

```


Output:

```
[{'thread_id': 'cacf79bb-4248-4d01-aabc-938dbd60ed2c',
'created_at': '2024-08-14T17:36:38.921660+00:00',
'updated_at': '2024-08-14T17:36:38.921660+00:00',
'metadata': {'graph_id': 'agent'},
'status': 'idle',
'config': {'configurable': {}}}]

```


## Find interrupted threads[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#find-interrupted-threads "Permanent link")

We can use the following commands to find threads that have been interrupted in the middle of a run, which could either mean an error occurred before the run finished or a human-in-the-loop breakpoint was reached and the run is waiting to continue: 

[Python](#__tabbed_3_1)[Javascript](#__tabbed_3_2)[CURL](#__tabbed_3_3)

```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__codelineno-6-1)print(await client.threads.search(status="interrupted",limit=1))

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__codelineno-7-1)console.log(awaitclient.threads.search({status:"interrupted",limit:1}));

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__codelineno-8-1)curl--requestPOST\ 
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__codelineno-8-2)--url<DEPLOYMENT_URL>/threads/search\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__codelineno-8-3)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__codelineno-8-4)--data'{"status": "interrupted", "limit": 1}'

```


Output:

```
[{'thread_id': '0d282b22-bbd5-4d95-9c61-04dcc2e302a5',
'created_at': '2024-08-14T17:41:50.235455+00:00',
'updated_at': '2024-08-14T17:41:50.235455+00:00',
'metadata': {'graph_id': 'agent'},
'status': 'interrupted',
'config': {'configurable': {}}}]

```


## Find busy threads[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#find-busy-threads "Permanent link")

We can use the following commands to find threads that are busy, meaning they are currently handling the execution of a run:

[Python](#__tabbed_4_1)[Javascript](#__tabbed_4_2)[CURL](#__tabbed_4_3)

```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__codelineno-9-1)print(await client.threads.search(status="busy",limit=1))

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__codelineno-10-1)console.log(awaitclient.threads.search({status:"busy",limit:1}));

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__codelineno-11-1)curl--requestPOST\ 
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__codelineno-11-2)--url<DEPLOYMENT_URL>/threads/search\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__codelineno-11-3)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__codelineno-11-4)--data'{"status": "busy", "limit": 1}'

```


Output:

```
[{'thread_id': '0d282b22-bbd5-4d95-9c61-04dcc2e302a5',
'created_at': '2024-08-14T17:41:50.235455+00:00',
'updated_at': '2024-08-14T17:41:50.235455+00:00',
'metadata': {'graph_id': 'agent'},
'status': 'busy',
'config': {'configurable': {}}}]

```


## Find specific threads[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#find-specific-threads "Permanent link")

You may also want to check the status of specific threads, which you can do in a few ways:

### Find by ID[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#find-by-id "Permanent link")

You can use the `get` function to find the status of a specific thread, as long as you have the ID saved

[Python](#__tabbed_5_1)[Javascript](#__tabbed_5_2)[CURL](#__tabbed_5_3)

```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__codelineno-12-1)print((await client.threads.get(<THREAD_ID>))['status'])

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__codelineno-13-1)console.log((awaitclient.threads.get(<THREAD_ID>)).status);

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__codelineno-14-1)curl--requestGET\ 
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__codelineno-14-2)--url<DEPLOYMENT_URL>/threads/<THREAD_ID>\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__codelineno-14-3)--header'Content-Type: application/json'|jq-r'.status'

```


Output:

```
'idle'

```


### Find by metadata[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#find-by-metadata "Permanent link")

The search endpoint for threads also allows you to filter on metadata, which can be helpful if you use metadata to tag threads in order to keep them organized:

[Python](#__tabbed_6_1)[Javascript](#__tabbed_6_2)[CURL](#__tabbed_6_3)

```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__codelineno-15-1)print((await client.threads.search(metadata={"foo":"bar"},limit=1))[0]['status'])

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__codelineno-16-1)console.log((awaitclient.threads.search({metadata:{"foo":"bar"},limit:1}))[0].status);

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__codelineno-17-1)curl--requestPOST\ 
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__codelineno-17-2)--url<DEPLOYMENT_URL>/threads/search\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__codelineno-17-3)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__codelineno-17-4)--data'{"metadata": {"foo":"bar"}, "limit": 1}'|jq-r'.[0].status'

```


Output:

```
'idle'

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Copying Threads  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/copy_threads/) [ Next  How to kick off background runs  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/background_run/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/cloud/how-tos/check_thread_status/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
