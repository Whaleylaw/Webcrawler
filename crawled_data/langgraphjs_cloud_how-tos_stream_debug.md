---
url: https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#how-to-stream-debug-events)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to stream debug events 

[ ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/?q= "Share")

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
          * [ Runs  ](https://langchain-ai.github.io/langgraphjs/how-tos#runs)
          * Streaming  Streaming 
            * [ Streaming  ](https://langchain-ai.github.io/langgraphjs/how-tos#streaming_1)
            * [ How to stream full state of your graph  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_values/)
            * [ How to stream state updates of your graph  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_updates/)
            * [ How to stream messages from your graph  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_messages/)
            * [ How to stream events  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_events/)
            * How to stream debug events  [ How to stream debug events  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#setup)
              * [ Stream graph in debug mode  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#stream-graph-in-debug-mode)
            * [ How to configure multiple streaming modes at the same time  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#setup)
  * [ Stream graph in debug mode  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#stream-graph-in-debug-mode)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph Platform  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph-platform)
  5. [ Streaming  ](https://langchain-ai.github.io/langgraphjs/how-tos#streaming_1)



# How to stream debug events[¶](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#how-to-stream-debug-events "Permanent link")

Prerequisites

  * [Streaming](https://langchain-ai.github.io/langgraphjs/concepts/streaming/)



This guide covers how to stream debug events from your graph (`stream_mode="debug"`). Streaming debug events produces responses containing `type` and `timestamp` keys. Debug events correspond to different steps in the graph's execution, and there are three different types of steps that will get streamed back to you:

  * `checkpoint`: These events will get streamed anytime the graph saves its state, which occurs after every super-step. Read more about checkpoints [here](https://langchain-ai.github.io/langgraph/concepts/low_level/#checkpointer)
  * `task`: These events will get streamed before each super-step, and will contain information about a single task. Each super-step works by executing a list of tasks, where each task is scoped to a specific node and input. Below we will discuss the format of these tasks in more detail. 
  * `task_result`: After each `task` event, you will see a corresponding `task_result` event which as the name suggests contains information on the results of the task executed in the super-step. Scroll more to learn about the exact structure of these events.



## Setup[¶](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#setup "Permanent link")

First let's set up our client and thread:

[Python](#__tabbed_1_1)[Javascript](#__tabbed_1_2)[CURL](#__tabbed_1_3)

```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-0-1)fromlanggraph_sdkimport get_client
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-0-2)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-0-3)client = get_client(url=<DEPLOYMENT_URL>)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-0-4)# Using the graph deployed with the name "agent"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-0-5)assistant_id = "agent"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-0-6)# create thread
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-0-7)thread = await client.threads.create()
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-0-8)print(thread)

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-1-1)import{Client}from"@langchain/langgraph-sdk";
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-1-2)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-1-3)constclient=newClient({apiUrl:<DEPLOYMENT_URL>});
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-1-4)// Using the graph deployed with the name "agent"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-1-5)constassistantID="agent";
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-1-6)// create thread
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-1-7)constthread=awaitclient.threads.create();
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-1-8)console.log(thread);

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-2-1)curl--requestPOST\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-2-2)--url<DEPLOYMENT_URL>/threads\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-2-3)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-2-4)--data'{}'

```


Output:

```
{
  'thread_id': 'd0cbe9ad-f11c-443a-9f6f-dca0ae5a0dd3',
  'created_at': '2024-06-21T22:10:27.696862+00:00',
  'updated_at': '2024-06-21T22:10:27.696862+00:00',
  'metadata': {},
  'status': 'idle',
  'config': {},
  'values': None
}

```


## Stream graph in debug mode[¶](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#stream-graph-in-debug-mode "Permanent link")

[Python](#__tabbed_2_1)[Javascript](#__tabbed_2_2)[CURL](#__tabbed_2_3)

```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-3-1)# create input
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-3-2)input = {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-3-3)  "messages": [
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-3-4)    {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-3-5)      "role": "user",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-3-6)      "content": "What's the weather in SF?",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-3-7)    }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-3-8)  ]
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-3-9)}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-3-10)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-3-11)# stream debug
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-3-12)async for chunk in client.runs.stream(
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-3-13)  thread_id=thread["thread_id"],
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-3-14)  assistant_id=assistant_id,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-3-15)  input=input,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-3-16)  stream_mode="debug",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-3-17)):
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-3-18)  print(f"Receiving new event of type: {chunk.event}...")
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-3-19)  print(chunk.data)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-3-20)  print("\n\n")

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-4-1)// create input
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-4-2)constinput={
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-4-3)messages:[
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-4-4){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-4-5)role:"human",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-4-6)content:"What's the weather in SF?",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-4-7)}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-4-8)]
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-4-9)};
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-4-10)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-4-11)// stream debug
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-4-12)conststreamResponse=client.runs.stream(
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-4-13)thread["thread_id"],
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-4-14)assistantID,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-4-15){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-4-16)input,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-4-17)streamMode:"debug"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-4-18)}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-4-19));
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-4-20)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-4-21)forawait(constchunkofstreamResponse){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-4-22)console.log(`Receiving new event of type: ${chunk.event}...`);
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-4-23)console.log(chunk.data);
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-4-24)console.log("\n\n");
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-4-25)}

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-5-1)curl--requestPOST\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-5-2)--url<DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/stream\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-5-3)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-5-4)--data"{
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-5-5)  \"assistant_id\": \"agent\",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-5-6)  \"input\": {\"messages\": [{\"role\": \"human\", \"content\": \"What's the weather in SF?\"}]},
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-5-7)  \"stream_mode\": [
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-5-8)   \"debug\"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-5-9)  ]
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-5-10) }"|\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-5-11)sed's/\r$//'|\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-5-12)awk'
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-5-13) /^event:/ {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-5-14)   if (data_content != "") {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-5-15)     print data_content "\n"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-5-16)   }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-5-17)   sub(/^event: /, "Receiving event of type: ", $0)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-5-18)   printf "%s...\n", $0
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-5-19)   data_content = ""
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-5-20) }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-5-21) /^data:/ {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-5-22)   sub(/^data: /, "", $0)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-5-23)   data_content = $0
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-5-24) }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-5-25) END {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-5-26)   if (data_content != "") {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-5-27)     print data_content "\n"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-5-28)   }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-5-29) }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__codelineno-5-30) '

```


Output:

```
Receiving new event of type: metadata...
{'run_id': '1ef65938-d7c7-68db-b786-011aa1cb3cd2'}

Receiving new event of type: debug...
{'type': 'checkpoint', 'timestamp': '2024-08-28T23:16:28.134680+00:00', 'step': -1, 'payload': {'config': {'tags': [], 'metadata': {'created_by': 'system', 'run_id': '1ef65938-d7c7-68db-b786-011aa1cb3cd2', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'be4fd54d-ff22-4e9e-8876-d5cccc0e8048', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca'}, 'callbacks': [None], 'recursion_limit': 25, 'configurable': {'run_id': '1ef65938-d7c7-68db-b786-011aa1cb3cd2', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'be4fd54d-ff22-4e9e-8876-d5cccc0e8048', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca', 'checkpoint_id': '1ef65938-d8f3-6b25-bfff-30a8ed6460bd', 'checkpoint_ns': ''}, 'run_id': '1ef65938-d7c7-68db-b786-011aa1cb3cd2'}, 'values': {'messages': [], 'search_results': []}, 'metadata': {'source': 'input', 'writes': {'messages': [{'role': 'human', 'content': "What's the weather in SF?"}]}, 'step': -1}, 'next': ['__start__'], 'tasks': [{'id': 'b40d2c90-dc1e-52db-82d6-08751b769c55', 'name': '__start__', 'interrupts': []}]}}

Receiving new event of type: debug...
{'type': 'checkpoint', 'timestamp': '2024-08-28T23:16:28.139821+00:00', 'step': 0, 'payload': {'config': {'tags': [], 'metadata': {'created_by': 'system', 'run_id': '1ef65938-d7c7-68db-b786-011aa1cb3cd2', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'be4fd54d-ff22-4e9e-8876-d5cccc0e8048', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca'}, 'callbacks': [None], 'recursion_limit': 25, 'configurable': {'run_id': '1ef65938-d7c7-68db-b786-011aa1cb3cd2', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'be4fd54d-ff22-4e9e-8876-d5cccc0e8048', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca', 'checkpoint_id': '1ef65938-d900-63f1-8000-70fe53e0da5c', 'checkpoint_ns': ''}, 'run_id': '1ef65938-d7c7-68db-b786-011aa1cb3cd2'}, 'values': {'messages': [{'content': "What's the weather in SF?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': '4123a12c-46cb-4815-bdcc-32537af0cb5b', 'example': False}], 'search_results': []}, 'metadata': {'source': 'loop', 'writes': None, 'step': 0}, 'next': ['call_model'], 'tasks': [{'id': '685d89f6-542b-5e11-8cff-2963e7f4ea63', 'name': 'call_model', 'interrupts': []}]}}

Receiving new event of type: debug...
{'type': 'task', 'timestamp': '2024-08-28T23:16:28.139928+00:00', 'step': 1, 'payload': {'id': '600a6ff3-7ff1-570a-b626-f887e9a70f1c', 'name': 'call_model', 'input': {'messages': [{'content': "What's the weather in SF?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': '4123a12c-46cb-4815-bdcc-32537af0cb5b', 'example': False}], 'search_results': [], 'final_answer': None}, 'triggers': ['start:call_model']}}

Receiving new event of type: debug...
{'type': 'task_result', 'timestamp': '2024-08-28T23:16:28.584833+00:00', 'step': 1, 'payload': {'id': '600a6ff3-7ff1-570a-b626-f887e9a70f1c', 'name': 'call_model', 'error': None, 'result': [['messages', {'content': 'Current weather in San Francisco', 'additional_kwargs': {}, 'response_metadata': {'finish_reason': 'stop', 'model_name': 'gpt-4o-2024-05-13', 'system_fingerprint': 'fp_a2ff031fb5'}, 'type': 'ai', 'name': None, 'id': 'run-0407bff9-3692-4ab5-9e57-2e9f396a3ee4', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}]], 'interrupts': []}}

Receiving new event of type: debug...
{'type': 'checkpoint', 'timestamp': '2024-08-28T23:16:28.584991+00:00', 'step': 1, 'payload': {'config': {'tags': [], 'metadata': {'created_by': 'system', 'run_id': '1ef65938-d7c7-68db-b786-011aa1cb3cd2', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'be4fd54d-ff22-4e9e-8876-d5cccc0e8048', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca'}, 'callbacks': [None], 'recursion_limit': 25, 'configurable': {'run_id': '1ef65938-d7c7-68db-b786-011aa1cb3cd2', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'be4fd54d-ff22-4e9e-8876-d5cccc0e8048', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca', 'checkpoint_id': '1ef65938-dd3f-616f-8001-ce1c6f31e130', 'checkpoint_ns': ''}, 'run_id': '1ef65938-d7c7-68db-b786-011aa1cb3cd2'}, 'values': {'messages': [{'content': "What's the weather in SF?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': '4123a12c-46cb-4815-bdcc-32537af0cb5b', 'example': False}, {'content': 'Current weather in San Francisco', 'additional_kwargs': {}, 'response_metadata': {'finish_reason': 'stop', 'model_name': 'gpt-4o-2024-05-13', 'system_fingerprint': 'fp_a2ff031fb5'}, 'type': 'ai', 'name': None, 'id': 'run-0407bff9-3692-4ab5-9e57-2e9f396a3ee4', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}], 'search_results': []}, 'metadata': {'source': 'loop', 'writes': {'call_model': {'messages': {'content': 'Current weather in San Francisco', 'additional_kwargs': {}, 'response_metadata': {'finish_reason': 'stop', 'model_name': 'gpt-4o-2024-05-13', 'system_fingerprint': 'fp_a2ff031fb5'}, 'type': 'ai', 'name': None, 'id': 'run-0407bff9-3692-4ab5-9e57-2e9f396a3ee4', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}}}, 'step': 1}, 'next': ['exa_search', 'tavily_search'], 'tasks': [{'id': '43865935-be38-5f6e-8d38-d44ef369c278', 'name': 'exa_search', 'interrupts': []}, {'id': 'dc220677-2720-56c7-a524-caaff60fce2c', 'name': 'tavily_search', 'interrupts': []}]}}

Receiving new event of type: debug...
{'type': 'task', 'timestamp': '2024-08-28T23:16:28.585219+00:00', 'step': 2, 'payload': {'id': '870b5854-2f84-533d-8e7d-87158ee948fc', 'name': 'exa_search', 'input': {'messages': [{'content': "What's the weather in SF?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': '4123a12c-46cb-4815-bdcc-32537af0cb5b', 'example': False}, {'content': 'Current weather in San Francisco', 'additional_kwargs': {}, 'response_metadata': {'finish_reason': 'stop', 'model_name': 'gpt-4o-2024-05-13', 'system_fingerprint': 'fp_a2ff031fb5'}, 'type': 'ai', 'name': None, 'id': 'run-0407bff9-3692-4ab5-9e57-2e9f396a3ee4', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}], 'search_results': [], 'final_answer': None}, 'triggers': ['call_model']}}

Receiving new event of type: debug...
{'type': 'task', 'timestamp': '2024-08-28T23:16:28.585219+00:00', 'step': 2, 'payload': {'id': '7589abfc-04df-58c6-8835-be172f84a7ff', 'name': 'tavily_search', 'input': {'messages': [{'content': "What's the weather in SF?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': '4123a12c-46cb-4815-bdcc-32537af0cb5b', 'example': False}, {'content': 'Current weather in San Francisco', 'additional_kwargs': {}, 'response_metadata': {'finish_reason': 'stop', 'model_name': 'gpt-4o-2024-05-13', 'system_fingerprint': 'fp_a2ff031fb5'}, 'type': 'ai', 'name': None, 'id': 'run-0407bff9-3692-4ab5-9e57-2e9f396a3ee4', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}], 'search_results': [], 'final_answer': None}, 'triggers': ['call_model']}}

Receiving new event of type: debug...
{'type': 'task_result', 'timestamp': '2024-08-28T23:16:32.422243+00:00', 'step': 2, 'payload': {'id': '7589abfc-04df-58c6-8835-be172f84a7ff', 'name': 'tavily_search', 'error': None, 'result': [['search_results', ["{'location': {'name': 'San Francisco', 'region': 'California', 'country': 'United States of America', 'lat': 37.78, 'lon': -122.42, 'tz_id': 'America/Los_Angeles', 'localtime_epoch': 1724886988, 'localtime': '2024-08-28 16:16'}, 'current': {'last_updated_epoch': 1724886900, 'last_updated': '2024-08-28 16:15', 'temp_c': 22.2, 'temp_f': 72.0, 'is_day': 1, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/day/116.png', 'code': 1003}, 'wind_mph': 16.1, 'wind_kph': 25.9, 'wind_degree': 300, 'wind_dir': 'WNW', 'pressure_mb': 1013.0, 'pressure_in': 29.91, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 61, 'cloud': 25, 'feelslike_c': 24.6, 'feelslike_f': 76.4, 'windchill_c': 19.6, 'windchill_f': 67.2, 'heatindex_c': 19.7, 'heatindex_f': 67.4, 'dewpoint_c': 13.0, 'dewpoint_f': 55.5, 'vis_km': 16.0, 'vis_miles': 9.0, 'uv': 5.0, 'gust_mph': 18.7, 'gust_kph': 30.0}}"]]], 'interrupts': []}}

Receiving new event of type: debug...
{'type': 'task_result', 'timestamp': '2024-08-28T23:16:34.750124+00:00', 'step': 2, 'payload': {'id': '870b5854-2f84-533d-8e7d-87158ee948fc', 'name': 'exa_search', 'error': None, 'result': [['search_results', ['The time period when the sun is no more than 6 degrees below the horizon at either sunrise or sunset. The horizon should be clearly defined and the brightest stars should be visible under good atmospheric conditions (i.e. no moonlight, or other lights). One still should be able to carry on ordinary outdoor activities. The time period when the sun is between 6 and 12 degrees below the horizon at either sunrise or sunset. The horizon is well defined and the outline of objects might be visible without artificial light. Ordinary outdoor activities are not possible at this time without extra illumination. The time period when the sun is between 12 and 18 degrees below the horizon at either sunrise or sunset. The sun does not contribute to the illumination of the sky before this time in the morning, or after this time in the evening. In the beginning of morning astronomical twilight and at the end of astronomical twilight in the evening, sky illumination is very faint, and might be undetectable. The time of Civil Sunset minus the time of Civil Sunrise. The time of Actual Sunset minus the time of Actual Sunrise. The change in length of daylight between today and tomorrow is also listed when available.']]], 'interrupts': []}}

Receiving new event of type: debug...
{'type': 'checkpoint', 'timestamp': '2024-08-28T23:16:34.750266+00:00', 'step': 2, 'payload': {'config': {'tags': [], 'metadata': {'created_by': 'system', 'run_id': '1ef65938-d7c7-68db-b786-011aa1cb3cd2', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'be4fd54d-ff22-4e9e-8876-d5cccc0e8048', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca'}, 'callbacks': [None], 'recursion_limit': 25, 'configurable': {'run_id': '1ef65938-d7c7-68db-b786-011aa1cb3cd2', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'be4fd54d-ff22-4e9e-8876-d5cccc0e8048', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca', 'checkpoint_id': '1ef65939-180b-6087-8002-f969296f8e3d', 'checkpoint_ns': ''}, 'run_id': '1ef65938-d7c7-68db-b786-011aa1cb3cd2'}, 'values': {'messages': [{'content': "What's the weather in SF?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': '4123a12c-46cb-4815-bdcc-32537af0cb5b', 'example': False}, {'content': 'Current weather in San Francisco', 'additional_kwargs': {}, 'response_metadata': {'finish_reason': 'stop', 'model_name': 'gpt-4o-2024-05-13', 'system_fingerprint': 'fp_a2ff031fb5'}, 'type': 'ai', 'name': None, 'id': 'run-0407bff9-3692-4ab5-9e57-2e9f396a3ee4', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}], 'search_results': ['The time period when the sun is no more than 6 degrees below the horizon at either sunrise or sunset. The horizon should be clearly defined and the brightest stars should be visible under good atmospheric conditions (i.e. no moonlight, or other lights). One still should be able to carry on ordinary outdoor activities. The time period when the sun is between 6 and 12 degrees below the horizon at either sunrise or sunset. The horizon is well defined and the outline of objects might be visible without artificial light. Ordinary outdoor activities are not possible at this time without extra illumination. The time period when the sun is between 12 and 18 degrees below the horizon at either sunrise or sunset. The sun does not contribute to the illumination of the sky before this time in the morning, or after this time in the evening. In the beginning of morning astronomical twilight and at the end of astronomical twilight in the evening, sky illumination is very faint, and might be undetectable. The time of Civil Sunset minus the time of Civil Sunrise. The time of Actual Sunset minus the time of Actual Sunrise. The change in length of daylight between today and tomorrow is also listed when available.', "{'location': {'name': 'San Francisco', 'region': 'California', 'country': 'United States of America', 'lat': 37.78, 'lon': -122.42, 'tz_id': 'America/Los_Angeles', 'localtime_epoch': 1724886988, 'localtime': '2024-08-28 16:16'}, 'current': {'last_updated_epoch': 1724886900, 'last_updated': '2024-08-28 16:15', 'temp_c': 22.2, 'temp_f': 72.0, 'is_day': 1, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/day/116.png', 'code': 1003}, 'wind_mph': 16.1, 'wind_kph': 25.9, 'wind_degree': 300, 'wind_dir': 'WNW', 'pressure_mb': 1013.0, 'pressure_in': 29.91, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 61, 'cloud': 25, 'feelslike_c': 24.6, 'feelslike_f': 76.4, 'windchill_c': 19.6, 'windchill_f': 67.2, 'heatindex_c': 19.7, 'heatindex_f': 67.4, 'dewpoint_c': 13.0, 'dewpoint_f': 55.5, 'vis_km': 16.0, 'vis_miles': 9.0, 'uv': 5.0, 'gust_mph': 18.7, 'gust_kph': 30.0}}"]}, 'metadata': {'source': 'loop', 'writes': {'exa_search': {'search_results': ['The time period when the sun is no more than 6 degrees below the horizon at either sunrise or sunset. The horizon should be clearly defined and the brightest stars should be visible under good atmospheric conditions (i.e. no moonlight, or other lights). One still should be able to carry on ordinary outdoor activities. The time period when the sun is between 6 and 12 degrees below the horizon at either sunrise or sunset. The horizon is well defined and the outline of objects might be visible without artificial light. Ordinary outdoor activities are not possible at this time without extra illumination. The time period when the sun is between 12 and 18 degrees below the horizon at either sunrise or sunset. The sun does not contribute to the illumination of the sky before this time in the morning, or after this time in the evening. In the beginning of morning astronomical twilight and at the end of astronomical twilight in the evening, sky illumination is very faint, and might be undetectable. The time of Civil Sunset minus the time of Civil Sunrise. The time of Actual Sunset minus the time of Actual Sunrise. The change in length of daylight between today and tomorrow is also listed when available.']}, 'tavily_search': {'search_results': ["{'location': {'name': 'San Francisco', 'region': 'California', 'country': 'United States of America', 'lat': 37.78, 'lon': -122.42, 'tz_id': 'America/Los_Angeles', 'localtime_epoch': 1724886988, 'localtime': '2024-08-28 16:16'}, 'current': {'last_updated_epoch': 1724886900, 'last_updated': '2024-08-28 16:15', 'temp_c': 22.2, 'temp_f': 72.0, 'is_day': 1, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/day/116.png', 'code': 1003}, 'wind_mph': 16.1, 'wind_kph': 25.9, 'wind_degree': 300, 'wind_dir': 'WNW', 'pressure_mb': 1013.0, 'pressure_in': 29.91, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 61, 'cloud': 25, 'feelslike_c': 24.6, 'feelslike_f': 76.4, 'windchill_c': 19.6, 'windchill_f': 67.2, 'heatindex_c': 19.7, 'heatindex_f': 67.4, 'dewpoint_c': 13.0, 'dewpoint_f': 55.5, 'vis_km': 16.0, 'vis_miles': 9.0, 'uv': 5.0, 'gust_mph': 18.7, 'gust_kph': 30.0}}"]}}, 'step': 2}, 'next': ['summarize_search_results'], 'tasks': [{'id': '7263c738-516d-5708-b318-2c8ef54d4a33', 'name': 'summarize_search_results', 'interrupts': []}]}}

Receiving new event of type: debug...
{'type': 'task', 'timestamp': '2024-08-28T23:16:34.750394+00:00', 'step': 3, 'payload': {'id': '5beaa05d-57d4-5acd-95c1-c7093990910f', 'name': 'summarize_search_results', 'input': {'messages': [{'content': "What's the weather in SF?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': '4123a12c-46cb-4815-bdcc-32537af0cb5b', 'example': False}, {'content': 'Current weather in San Francisco', 'additional_kwargs': {}, 'response_metadata': {'finish_reason': 'stop', 'model_name': 'gpt-4o-2024-05-13', 'system_fingerprint': 'fp_a2ff031fb5'}, 'type': 'ai', 'name': None, 'id': 'run-0407bff9-3692-4ab5-9e57-2e9f396a3ee4', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}], 'search_results': ['The time period when the sun is no more than 6 degrees below the horizon at either sunrise or sunset. The horizon should be clearly defined and the brightest stars should be visible under good atmospheric conditions (i.e. no moonlight, or other lights). One still should be able to carry on ordinary outdoor activities. The time period when the sun is between 6 and 12 degrees below the horizon at either sunrise or sunset. The horizon is well defined and the outline of objects might be visible without artificial light. Ordinary outdoor activities are not possible at this time without extra illumination. The time period when the sun is between 12 and 18 degrees below the horizon at either sunrise or sunset. The sun does not contribute to the illumination of the sky before this time in the morning, or after this time in the evening. In the beginning of morning astronomical twilight and at the end of astronomical twilight in the evening, sky illumination is very faint, and might be undetectable. The time of Civil Sunset minus the time of Civil Sunrise. The time of Actual Sunset minus the time of Actual Sunrise. The change in length of daylight between today and tomorrow is also listed when available.', "{'location': {'name': 'San Francisco', 'region': 'California', 'country': 'United States of America', 'lat': 37.78, 'lon': -122.42, 'tz_id': 'America/Los_Angeles', 'localtime_epoch': 1724886988, 'localtime': '2024-08-28 16:16'}, 'current': {'last_updated_epoch': 1724886900, 'last_updated': '2024-08-28 16:15', 'temp_c': 22.2, 'temp_f': 72.0, 'is_day': 1, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/day/116.png', 'code': 1003}, 'wind_mph': 16.1, 'wind_kph': 25.9, 'wind_degree': 300, 'wind_dir': 'WNW', 'pressure_mb': 1013.0, 'pressure_in': 29.91, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 61, 'cloud': 25, 'feelslike_c': 24.6, 'feelslike_f': 76.4, 'windchill_c': 19.6, 'windchill_f': 67.2, 'heatindex_c': 19.7, 'heatindex_f': 67.4, 'dewpoint_c': 13.0, 'dewpoint_f': 55.5, 'vis_km': 16.0, 'vis_miles': 9.0, 'uv': 5.0, 'gust_mph': 18.7, 'gust_kph': 30.0}}"], 'final_answer': None}, 'triggers': ['exa_search', 'tavily_search']}}

Receiving new event of type: debug...
{'type': 'task_result', 'timestamp': '2024-08-28T23:16:35.851058+00:00', 'step': 3, 'payload': {'id': '5beaa05d-57d4-5acd-95c1-c7093990910f', 'name': 'summarize_search_results', 'error': None, 'result': [['final_answer', {'content': "The provided data details various twilight periods based on the sun's position relative to the horizon, alongside current weather information for San Francisco, California, as of August 28, 2024. The weather is partly cloudy with a temperature of 22.2°C (72.0°F), moderate wind from the WNW at 16.1 mph, and the UV index is 5.", 'additional_kwargs': {}, 'response_metadata': {'finish_reason': 'stop', 'model_name': 'gpt-4o-2024-05-13', 'system_fingerprint': 'fp_157b3831f5'}, 'type': 'ai', 'name': None, 'id': 'run-928c997b-9d85-4664-bd20-97ade4cc655e', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}]], 'interrupts': []}}

Receiving new event of type: debug...
{'type': 'checkpoint', 'timestamp': '2024-08-28T23:16:35.851194+00:00', 'step': 3, 'payload': {'config': {'tags': [], 'metadata': {'created_by': 'system', 'run_id': '1ef65938-d7c7-68db-b786-011aa1cb3cd2', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'be4fd54d-ff22-4e9e-8876-d5cccc0e8048', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca'}, 'callbacks': [None], 'recursion_limit': 25, 'configurable': {'run_id': '1ef65938-d7c7-68db-b786-011aa1cb3cd2', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'be4fd54d-ff22-4e9e-8876-d5cccc0e8048', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca', 'checkpoint_id': '1ef65939-228a-6d93-8003-8b06d7483024', 'checkpoint_ns': ''}, 'run_id': '1ef65938-d7c7-68db-b786-011aa1cb3cd2'}, 'values': {'messages': [{'content': "What's the weather in SF?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': '4123a12c-46cb-4815-bdcc-32537af0cb5b', 'example': False}, {'content': 'Current weather in San Francisco', 'additional_kwargs': {}, 'response_metadata': {'finish_reason': 'stop', 'model_name': 'gpt-4o-2024-05-13', 'system_fingerprint': 'fp_a2ff031fb5'}, 'type': 'ai', 'name': None, 'id': 'run-0407bff9-3692-4ab5-9e57-2e9f396a3ee4', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}], 'search_results': ['The time period when the sun is no more than 6 degrees below the horizon at either sunrise or sunset. The horizon should be clearly defined and the brightest stars should be visible under good atmospheric conditions (i.e. no moonlight, or other lights). One still should be able to carry on ordinary outdoor activities. The time period when the sun is between 6 and 12 degrees below the horizon at either sunrise or sunset. The horizon is well defined and the outline of objects might be visible without artificial light. Ordinary outdoor activities are not possible at this time without extra illumination. The time period when the sun is between 12 and 18 degrees below the horizon at either sunrise or sunset. The sun does not contribute to the illumination of the sky before this time in the morning, or after this time in the evening. In the beginning of morning astronomical twilight and at the end of astronomical twilight in the evening, sky illumination is very faint, and might be undetectable. The time of Civil Sunset minus the time of Civil Sunrise. The time of Actual Sunset minus the time of Actual Sunrise. The change in length of daylight between today and tomorrow is also listed when available.', "{'location': {'name': 'San Francisco', 'region': 'California', 'country': 'United States of America', 'lat': 37.78, 'lon': -122.42, 'tz_id': 'America/Los_Angeles', 'localtime_epoch': 1724886988, 'localtime': '2024-08-28 16:16'}, 'current': {'last_updated_epoch': 1724886900, 'last_updated': '2024-08-28 16:15', 'temp_c': 22.2, 'temp_f': 72.0, 'is_day': 1, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/day/116.png', 'code': 1003}, 'wind_mph': 16.1, 'wind_kph': 25.9, 'wind_degree': 300, 'wind_dir': 'WNW', 'pressure_mb': 1013.0, 'pressure_in': 29.91, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 61, 'cloud': 25, 'feelslike_c': 24.6, 'feelslike_f': 76.4, 'windchill_c': 19.6, 'windchill_f': 67.2, 'heatindex_c': 19.7, 'heatindex_f': 67.4, 'dewpoint_c': 13.0, 'dewpoint_f': 55.5, 'vis_km': 16.0, 'vis_miles': 9.0, 'uv': 5.0, 'gust_mph': 18.7, 'gust_kph': 30.0}}"], 'final_answer': {'content': "The provided data details various twilight periods based on the sun's position relative to the horizon, alongside current weather information for San Francisco, California, as of August 28, 2024. The weather is partly cloudy with a temperature of 22.2°C (72.0°F), moderate wind from the WNW at 16.1 mph, and the UV index is 5.", 'additional_kwargs': {}, 'response_metadata': {'finish_reason': 'stop', 'model_name': 'gpt-4o-2024-05-13', 'system_fingerprint': 'fp_157b3831f5'}, 'type': 'ai', 'name': None, 'id': 'run-928c997b-9d85-4664-bd20-97ade4cc655e', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}}, 'metadata': {'source': 'loop', 'writes': {'summarize_search_results': {'final_answer': {'content': "The provided data details various twilight periods based on the sun's position relative to the horizon, alongside current weather information for San Francisco, California, as of August 28, 2024. The weather is partly cloudy with a temperature of 22.2°C (72.0°F), moderate wind from the WNW at 16.1 mph, and the UV index is 5.", 'additional_kwargs': {}, 'response_metadata': {'finish_reason': 'stop', 'model_name': 'gpt-4o-2024-05-13', 'system_fingerprint': 'fp_157b3831f5'}, 'type': 'ai', 'name': None, 'id': 'run-928c997b-9d85-4664-bd20-97ade4cc655e', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}}}, 'step': 3}, 'next': [], 'tasks': []}}

```


We see that our debug events start with two `checkpoint` events at step 0 and 1, which represent checkpointing before the graph is created and after it has been created. We then see a single `task` and corresponding `task_result` which corresponds to our first node, `call_model`, being triggered. After it has finished, the entire super-step is over so the graph saves another checkpoint and we see the corresponding `checkpoint` event. 

The next super-step executed two search nodes [in parallel](https://langchain-ai.github.io/langgraph/how-tos/branching/) - specifically one node will execute an Exa search, while the other will use Tavily. Executing these nodes in parallel in the same super-step creates 2 `task` events and two corresponding `task_result` events. After we receive both of those `task_result` events, we see another `checkpoint` event as we would expect.

Lastly, we see a final `task` and `task_result` pair corresponding to the `summarize_search_results` node, which is the last node in our graph. As soon as this super-step is done we see one final `checkpoint` event corresponding to the final checkpoint of this run.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to stream events  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_events/) [ Next  How to configure multiple streaming modes at the same time  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
