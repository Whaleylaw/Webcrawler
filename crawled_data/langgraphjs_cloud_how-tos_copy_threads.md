---
url: https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#copying-threads)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

Copying Threads 

[ ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/?q= "Share")

Type to start searching

[ GitHub  ](https://github.com/langchain-ai/langgraphjs "Go to repository")

  * [ Home ](https://langchain-ai.github.io/langgraphjs/)
  * [ API reference ](https://langchain-ai.github.io/langgraphjs/reference/)
  * [ Versions ](https://langchain-ai.github.io/langgraphjs/versions/)



[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

[ GitHub  ](https://github.com/langchain-ai/langgraphjs "Go to repository")

  * [ Home  ](https://langchain-ai.github.io/langgraphjs/)

Home 
    * Get started  Get started 
      * [ Learn the basics  ](https://langchain-ai.github.io/langgraphjs/tutorials/quickstart/)
      * [ Deployment  ](https://langchain-ai.github.io/langgraphjs/tutorials/deployment/)
    * Guides  Guides 
      * [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)

How-to Guides 
        * [ Installation  ](https://langchain-ai.github.io/langgraphjs/how-tos#installation)
        * [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
        * LangGraph Platform  LangGraph Platform 
          * [ LangGraph Platform  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph-platform)
          * [ Application Structure  ](https://langchain-ai.github.io/langgraphjs/how-tos#application-structure)
          * [ Deployment  ](https://langchain-ai.github.io/langgraphjs/how-tos#deployment)
          * [ Authentication & Access Control  ](https://langchain-ai.github.io/langgraphjs/how-tos#authentication-access-control)
          * [ Assistants  ](https://langchain-ai.github.io/langgraphjs/how-tos#assistants)
          * Threads  Threads 
            * [ Threads  ](https://langchain-ai.github.io/langgraphjs/how-tos#threads)
            * Copying Threads  [ Copying Threads  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#setup)
                * [ SDK initialization  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#sdk-initialization)
              * [ Copying a thread  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#copying-a-thread)
                * [ Create copy  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#create-copy)
                * [ Verify copy  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#verify-copy)
            * [ Check the Status of your Threads  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/check_thread_status/)
          * [ Runs  ](https://langchain-ai.github.io/langgraphjs/how-tos#runs)
          * [ Streaming  ](https://langchain-ai.github.io/langgraphjs/how-tos#streaming_1)
          * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraphjs/how-tos#human-in-the-loop_1)
          * [ Double-texting  ](https://langchain-ai.github.io/langgraphjs/how-tos#double-texting)
          * [ Webhooks  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/webhooks/)
          * [ Cron Jobs  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/cron_jobs/)
          * [ LangGraph Studio  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph-studio)
      * [ Concepts  ](https://langchain-ai.github.io/langgraphjs/concepts/)
      * [ Tutorials  ](https://langchain-ai.github.io/langgraphjs/tutorials/)
    * Resources  Resources 
      * [ Adopters  ](https://langchain-ai.github.io/langgraphjs/adopters/)
      * [ FAQ  ](https://langchain-ai.github.io/langgraphjs/concepts/faq/)
      * [ Troubleshooting  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraphjs/reference/)
  * [ Versions  ](https://langchain-ai.github.io/langgraphjs/versions/)



Table of contents 

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#setup)
    * [ SDK initialization  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#sdk-initialization)
  * [ Copying a thread  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#copying-a-thread)
    * [ Create copy  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#create-copy)
    * [ Verify copy  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#verify-copy)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph Platform  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph-platform)
  5. [ Threads  ](https://langchain-ai.github.io/langgraphjs/how-tos#threads)



# Copying Threads[¶](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#copying-threads "Permanent link")

You may wish to copy (i.e. "fork") an existing thread in order to keep the existing thread's history and create independent runs that do not affect the original thread. This guide shows how you can do that.

## Setup[¶](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#setup "Permanent link")

This code assumes you already have a thread to copy. You can read about what a thread is [here](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_server/#threads) and learn how to stream a run on a thread in [these how-to guides](https://langchain-ai.github.io/langgraphjs/how-tos/#streaming_1).

### SDK initialization[¶](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#sdk-initialization "Permanent link")

First, we need to setup our client so that we can communicate with our hosted graph:

[Python](#__tabbed_1_1)[Javascript](#__tabbed_1_2)[CURL](#__tabbed_1_3)

```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-0-1)fromlanggraph_sdkimport get_client
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-0-2)client = get_client(url="<DEPLOYMENT_URL>")
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-0-3)assistant_id = "agent"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-0-4)thread = await client.threads.create()

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-1-1)import{Client}from"@langchain/langgraph-sdk";
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-1-2)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-1-3)constclient=newClient({apiUrl:"<DEPLOYMENT_URL>"});
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-1-4)constassistantId="agent";
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-1-5)constthread=awaitclient.threads.create();

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-2-1)curl--requestPOST\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-2-2)--url<DEPLOYMENT_URL>/threads\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-2-3)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-2-4)--data'{
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-2-5)  "metadata": {}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-2-6) }'

```


## Copying a thread[¶](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#copying-a-thread "Permanent link")

The code below assumes that a thread you'd like to copy already exists.

Copying a thread will create a new thread with the same history as the existing thread, and then allow you to continue executing runs.

### Create copy[¶](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#create-copy "Permanent link")

[Python](#__tabbed_2_1)[Javascript](#__tabbed_2_2)[CURL](#__tabbed_2_3)

```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-3-1)copied_thread = await client.threads.copy(<THREAD_ID>)

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-4-1)letcopiedThread=awaitclient.threads.copy(<THREAD_ID>);

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-5-1)curl--requestPOST--url<DEPLOYMENT_URL>/threads/<THREAD_ID>/copy\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-5-2)--header'Content-Type: application/json'

```


### Verify copy[¶](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#verify-copy "Permanent link")

We can verify that the history from the prior thread did indeed copy over correctly:

[Python](#__tabbed_3_1)[Javascript](#__tabbed_3_2)[CURL](#__tabbed_3_3)

```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-6-1)defremove_thread_id(d):
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-6-2) if 'metadata' in d and 'thread_id' in d['metadata']:
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-6-3)   del d
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-6-4) return d
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-6-5)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-6-6)original_thread_history = list(map(remove_thread_id,await client.threads.get_history(<THREAD_ID>)))
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-6-7)copied_thread_history = list(map(remove_thread_id,await client.threads.get_history(copied_thread['thread_id'])))
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-6-8)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-6-9)# Compare the two histories
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-6-10)assert original_thread_history == copied_thread_history
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-6-11)# if we made it here the assertion passed!
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-6-12)print("The histories are the same.")

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-7-1)functionremoveThreadId(d){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-7-2)if(d.metadata&&d.metadata.thread_id){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-7-3)deleted.metadata.thread_id;
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-7-4)}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-7-5)returnd;
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-7-6)}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-7-7)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-7-8)// Assuming `client.threads.getHistory(threadId)` is an async function that returns a list of dicts
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-7-9)asyncfunctioncompareThreadHistories(threadId,copiedThreadId){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-7-10)constoriginalThreadHistory=(awaitclient.threads.getHistory(threadId)).map(removeThreadId);
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-7-11)constcopiedThreadHistory=(awaitclient.threads.getHistory(copiedThreadId)).map(removeThreadId);
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-7-12)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-7-13)// Compare the two histories
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-7-14)console.assert(JSON.stringify(originalThreadHistory)===JSON.stringify(copiedThreadHistory));
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-7-15)// if we made it here the assertion passed!
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-7-16)console.log("The histories are the same.");
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-7-17)}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-7-18)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-7-19)// Example usage
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-7-20)compareThreadHistories(<THREAD_ID>,copiedThread.thread_id);

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-8-1)ifdiff<(
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-8-2)curl--requestGET--url<DEPLOYMENT_URL>/threads/<THREAD_ID>/history|jq-S'map(del(.metadata.thread_id))'
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-8-3))<(
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-8-4)curl--requestGET--url<DEPLOYMENT_URL>/threads/<COPIED_THREAD_ID>/history|jq-S'map(del(.metadata.thread_id))'
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-8-5))>/dev/null;then
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-8-6)echo"The histories are the same."
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-8-7)else
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-8-8)echo"The histories are different."
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__codelineno-8-9)fi

```


Output:

```
The histories are the same.

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to version assistants  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/assistant_versioning/) [ Next  Check the Status of your Threads  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/check_thread_status/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/copy_threads/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
