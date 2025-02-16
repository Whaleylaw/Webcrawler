---
url: https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#stateless-runs)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

Stateless Runs 

[ ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/?q= "Share")

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
          * [ Threads  ](https://langchain-ai.github.io/langgraphjs/how-tos#threads)
          * Runs  Runs 
            * [ Runs  ](https://langchain-ai.github.io/langgraphjs/how-tos#runs)
            * [ How to kick off background runs  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/)
            * [ How to run multiple agents on the same thread  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/)
            * [ Cron Jobs  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/cron_jobs/)
            * Stateless Runs  [ Stateless Runs  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#setup)
              * [ Stateless streaming  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#stateless-streaming)
              * [ Waiting for stateless results  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#waiting-for-stateless-results)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#setup)
  * [ Stateless streaming  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#stateless-streaming)
  * [ Waiting for stateless results  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#waiting-for-stateless-results)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph Platform  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph-platform)
  5. [ Runs  ](https://langchain-ai.github.io/langgraphjs/how-tos#runs)



# Stateless Runs[¶](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#stateless-runs "Permanent link")

Most of the time, you provide a `thread_id` to your client when you run your graph in order to keep track of prior runs through the persistent state implemented in LangGraph Cloud. However, if you don't need to persist the runs you don't need to use the built in persistent state and can create stateless runs.

## Setup[¶](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#setup "Permanent link")

First, let's setup our client:

[Python](#__tabbed_1_1)[Javascript](#__tabbed_1_2)[CURL](#__tabbed_1_3)

```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-0-1)fromlanggraph_sdkimport get_client
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-0-2)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-0-3)client = get_client(url=<DEPLOYMENT_URL>)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-0-4)# Using the graph deployed with the name "agent"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-0-5)assistant_id = "agent"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-0-6)# create thread
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-0-7)thread = await client.threads.create()

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-1-1)import{Client}from"@langchain/langgraph-sdk";
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-1-2)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-1-3)constclient=newClient({apiUrl:<DEPLOYMENT_URL>});
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-1-4)// Using the graph deployed with the name "agent"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-1-5)constassistantId="agent";
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-1-6)// create thread
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-1-7)constthread=awaitclient.threads.create();

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-2-1)curl--requestPOST\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-2-2)--url<DEPLOYMENT_URL>/assistants/search\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-2-3)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-2-4)--data'{
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-2-5)    "limit": 10,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-2-6)    "offset": 0
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-2-7)  }'|jq-c'map(select(.config == null or .config == {})) | .[0].graph_id'&&\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-2-8)curl--requestPOST\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-2-9)--url<DEPLOYMENT_URL>/threads\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-2-10)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-2-11)--data'{}'

```


## Stateless streaming[¶](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#stateless-streaming "Permanent link")

We can stream the results of a stateless run in an almost identical fashion to how we stream from a run with the state attribute, but instead of passing a value to the `thread_id` parameter, we pass `None`:

[Python](#__tabbed_2_1)[Javascript](#__tabbed_2_2)[CURL](#__tabbed_2_3)

```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-3-1)input = {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-3-2)  "messages": [
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-3-3)    {"role": "user", "content": "Hello! My name is Bagatur and I am 26 years old."}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-3-4)  ]
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-3-5)}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-3-6)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-3-7)async for chunk in client.runs.stream(
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-3-8)  # Don't pass in a thread_id and the stream will be stateless
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-3-9)  None,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-3-10)  assistant_id,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-3-11)  input=input,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-3-12)  stream_mode="updates",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-3-13)):
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-3-14)  if chunk.data and "run_id" not in chunk.data:
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-3-15)    print(chunk.data)

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-4-1)letinput={
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-4-2)messages:[
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-4-3){role:"user",content:"Hello! My name is Bagatur and I am 26 years old."}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-4-4)]
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-4-5)};
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-4-6)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-4-7)conststreamResponse=client.runs.stream(
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-4-8)// Don't pass in a thread_id and the stream will be stateless
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-4-9)null,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-4-10)assistantId,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-4-11){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-4-12)input,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-4-13)streamMode:"updates"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-4-14)}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-4-15));
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-4-16)forawait(constchunkofstreamResponse){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-4-17)if(chunk.data&&!("run_id"inchunk.data)){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-4-18)console.log(chunk.data);
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-4-19)}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-4-20)}

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-5-1)curl--requestPOST\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-5-2)--url<DEPLOYMENT_URL>/runs/stream\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-5-3)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-5-4)--data"{
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-5-5)    \"assistant_id\": \"agent\",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-5-6)    \"input\": {\"messages\": [{\"role\": \"human\", \"content\": \"Hello! My name is Bagatur and I am 26 years old.\"}]},
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-5-7)    \"stream_mode\": [
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-5-8)      \"updates\"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-5-9)    ]
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-5-10)  }"|jq-c'select(.data and (.data | has("run_id") | not)) | .data'

```


Output:

```
{'agent': {'messages': [{'content': "Hello Bagatur! It's nice to meet you. Thank you for introducing yourself and sharing your age. Is there anything specific you'd like to know or discuss? I'm here to help with any questions or topics you're interested in.", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-489ec573-1645-4ce2-a3b8-91b391d50a71', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}]}}

```


## Waiting for stateless results[¶](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#waiting-for-stateless-results "Permanent link")

In addition to streaming, you can also wait for a stateless result by using the `.wait` function like follows:

[Python](#__tabbed_3_1)[Javascript](#__tabbed_3_2)[CURL](#__tabbed_3_3)

```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-6-1)stateless_run_result = await client.runs.wait(
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-6-2)  None,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-6-3)  assistant_id,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-6-4)  input=input,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-6-5))
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-6-6)print(stateless_run_result)

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-7-1)letstatelessRunResult=awaitclient.runs.wait(
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-7-2)null,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-7-3)assistantId,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-7-4){input:input}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-7-5));
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-7-6)console.log(statelessRunResult);

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-8-1)curl--requestPOST\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-8-2)--url<DEPLOYMENT_URL>/runs/wait\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-8-3)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-8-4)--data'{
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-8-5)    "assistant_id": <ASSISTANT_IDD>,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__codelineno-8-6)  }'

```


Output:

```
{
  'messages': [
    {
      'content': 'Hello! My name is Bagatur and I am 26 years old.',
      'additional_kwargs': {},
      'response_metadata': {},
      'type': 'human',
      'name': None,
      'id': '5e088543-62c2-43de-9d95-6086ad7f8b48',
      'example': False}
    ,
    {
      'content': "Hello Bagatur! It's nice to meet you. Thank you for introducing yourself and sharing your age. Is there anything specific you'd like to know or discuss? I'm here to help with any questions or topics you'd like to explore.",
      'additional_kwargs': {},
      'response_metadata': {},
      'type': 'ai',
      'name': None,
      'id': 'run-d6361e8d-4d4c-45bd-ba47-39520257f773',
      'example': False,
      'tool_calls': [],
      'invalid_tool_calls': [],
      'usage_metadata': None
    }
  ]
}

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  Cron Jobs  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/cron_jobs/) [ Next  How to stream full state of your graph  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_values/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
