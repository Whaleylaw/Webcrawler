---
url: https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#how-to-configure-multiple-streaming-modes-at-the-same-time)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to configure multiple streaming modes at the same time 

[ ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/?q= "Share")

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
            * [ How to stream debug events  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/)
            * How to configure multiple streaming modes at the same time  [ How to configure multiple streaming modes at the same time  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#setup)
              * [ Stream graph with multiple modes  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#stream-graph-with-multiple-modes)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#setup)
  * [ Stream graph with multiple modes  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#stream-graph-with-multiple-modes)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph Platform  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph-platform)
  5. [ Streaming  ](https://langchain-ai.github.io/langgraphjs/how-tos#streaming_1)



# How to configure multiple streaming modes at the same time[¶](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#how-to-configure-multiple-streaming-modes-at-the-same-time "Permanent link")

Prerequisites

  * [Streaming](https://langchain-ai.github.io/langgraphjs/concepts/streaming/)



This guide covers how to configure multiple streaming modes at the same time.

## Setup[¶](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#setup "Permanent link")

First let's set up our client and thread:

[Python](#__tabbed_1_1)[Javascript](#__tabbed_1_2)[CURL](#__tabbed_1_3)

```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-0-1)fromlanggraph_sdkimport get_client
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-0-2)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-0-3)client = get_client(url=<DEPLOYMENT_URL>)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-0-4)# Using the graph deployed with the name "agent"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-0-5)assistant_id = "agent"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-0-6)# create thread
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-0-7)thread = await client.threads.create()
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-0-8)print(thread)

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-1-1)import{Client}from"@langchain/langgraph-sdk";
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-1-2)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-1-3)constclient=newClient({apiUrl:<DEPLOYMENT_URL>});
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-1-4)// Using the graph deployed with the name "agent"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-1-5)constassistantID="agent";
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-1-6)// create thread
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-1-7)constthread=awaitclient.threads.create();
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-1-8)console.log(thread);

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-2-1)curl--requestPOST\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-2-2)--url<DEPLOYMENT_URL>/threads\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-2-3)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-2-4)--data'{}'

```


Output:

```
{
  'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4',
  'created_at': '2024-06-24T21:30:07.980789+00:00',
  'updated_at': '2024-06-24T21:30:07.980789+00:00',
  'metadata': {},
  'status': 'idle',
  'config': {},
  'values': None
}

```


## Stream graph with multiple modes[¶](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#stream-graph-with-multiple-modes "Permanent link")

When configuring multiple streaming modes for a run, responses for each respective mode will be produced. In the following example, note that a `list` of modes (`messages`, `events`, `debug`) is passed to the `stream_mode` parameter and the response contains `events`, `debug`, `messages/complete`, `messages/metadata`, and `messages/partial` event types.

[Python](#__tabbed_2_1)[Javascript](#__tabbed_2_2)[CURL](#__tabbed_2_3)

```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-3-1)# create input
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-3-2)input = {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-3-3)  "messages": [
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-3-4)    {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-3-5)      "role": "user",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-3-6)      "content": "What's the weather in SF?",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-3-7)    }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-3-8)  ]
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-3-9)}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-3-10)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-3-11)# stream events with multiple streaming modes
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-3-12)async for chunk in client.runs.stream(
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-3-13)  thread_id=thread["thread_id"],
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-3-14)  assistant_id=assistant_id,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-3-15)  input=input,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-3-16)  stream_mode=["messages", "events", "debug"],
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-3-17)):
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-3-18)  print(f"Receiving new event of type: {chunk.event}...")
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-3-19)  print(chunk.data)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-3-20)  print("\n\n")

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-4-1)// create input
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-4-2)constinput={
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-4-3)messages:[
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-4-4){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-4-5)role:"human",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-4-6)content:"What's the weather in SF?",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-4-7)}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-4-8)]
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-4-9)};
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-4-10)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-4-11)// stream events with multiple streaming modes
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-4-12)conststreamResponse=client.runs.stream(
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-4-13)thread["thread_id"],
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-4-14)assistantID,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-4-15){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-4-16)input,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-4-17)streamMode:["messages","events","debug"]
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-4-18)}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-4-19));
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-4-20)forawait(constchunkofstreamResponse){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-4-21)console.log(`Receiving new event of type: ${chunk.event}...`);
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-4-22)console.log(chunk.data);
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-4-23)console.log("\n\n");
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-4-24)}

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-5-1)curl--requestPOST\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-5-2)--url<DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/stream\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-5-3)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-5-4)--data"{
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-5-5)  \"assistant_id\": \"agent\",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-5-6)  \"input\": {\"messages\": [{\"role\": \"human\", \"content\": \"What's the weather in SF?\"}]},
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-5-7)  \"stream_mode\": [
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-5-8)   \"messages\",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-5-9)   \"events\",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-5-10)   \"debug\"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-5-11)  ]
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-5-12) }"|\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-5-13)sed's/\r$//'|\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-5-14)awk'
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-5-15) /^event:/ {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-5-16)   if (data_content != "") {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-5-17)     print data_content "\n"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-5-18)   }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-5-19)   sub(/^event: /, "Receiving event of type: ", $0)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-5-20)   printf "%s...\n", $0
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-5-21)   data_content = ""
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-5-22) }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-5-23) /^data:/ {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-5-24)   sub(/^data: /, "", $0)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-5-25)   data_content = $0
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-5-26) }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-5-27) END {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-5-28)   if (data_content != "") {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-5-29)     print data_content "\n"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-5-30)   }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-5-31) }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__codelineno-5-32) '

```


Output:

```
Receiving new event of type: metadata...
{'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25'}

Receiving new event of type: events...
{'event': 'on_chain_start', 'data': {'input': {'messages': [{'role': 'human', 'content': "What's the weather in SF?"}]}}, 'name': 'LangGraph', 'tags': [], 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'metadata': {'created_by': 'system', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca'}, 'parent_ids': []}

Receiving new event of type: debug...
{'type': 'checkpoint', 'timestamp': '2024-06-24T21:34:06.116009+00:00', 'step': -1, 'payload': {'config': {'tags': [], 'metadata': {'created_by': 'system', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca'}, 'callbacks': [None], 'recursion_limit': 25, 'configurable': {'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'thread_ts': '1ef32717-bc7c-6daa-bfff-6b9027c1a50e', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca'}, 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25'}, 'values': {'messages': []}, 'metadata': {'source': 'input', 'step': -1, 'writes': {'messages': [{'role': 'human', 'content': "What's the weather in SF?"}]}}}}

Receiving new event of type: events...
{'event': 'on_chain_stream', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'name': 'LangGraph', 'tags': [], 'metadata': {'created_by': 'system', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca'}, 'data': {'chunk': ['debug', {'type': 'checkpoint', 'timestamp': '2024-06-24T21:34:06.116009+00:00', 'step': -1, 'payload': {'config': {'tags': [], 'metadata': {'created_by': 'system', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca'}, 'callbacks': [None], 'recursion_limit': 25, 'configurable': {'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'thread_ts': '1ef32717-bc7c-6daa-bfff-6b9027c1a50e', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca'}, 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25'}, 'values': {'messages': []}, 'metadata': {'source': 'input', 'step': -1, 'writes': {'messages': [{'role': 'human', 'content': "What's the weather in SF?"}]}}}}]}, 'parent_ids': []}

Receiving new event of type: events...
{'event': 'on_chain_stream', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'name': 'LangGraph', 'tags': [], 'metadata': {'created_by': 'system', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca'}, 'data': {'chunk': ['values', {'messages': [{'content': "What's the weather in SF?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': '7da1bafa-f53c-4df8-ba63-8dd517140b9f', 'example': False}]}]}, 'parent_ids': []}

Receiving new event of type: debug...
{'type': 'checkpoint', 'timestamp': '2024-06-24T21:34:06.117924+00:00', 'step': 0, 'payload': {'config': {'tags': [], 'metadata': {'created_by': 'system', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca'}, 'callbacks': [None], 'recursion_limit': 25, 'configurable': {'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'thread_ts': '1ef32717-bc81-68c8-8000-4e18ae7d67a5', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca'}, 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25'}, 'values': {'messages': [{'content': "What's the weather in SF?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': '7da1bafa-f53c-4df8-ba63-8dd517140b9f', 'example': False}]}, 'metadata': {'source': 'loop', 'step': 0, 'writes': None}}}

Receiving new event of type: events...
{'event': 'on_chain_stream', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'name': 'LangGraph', 'tags': [], 'metadata': {'created_by': 'system', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca'}, 'data': {'chunk': ['debug', {'type': 'checkpoint', 'timestamp': '2024-06-24T21:34:06.117924+00:00', 'step': 0, 'payload': {'config': {'tags': [], 'metadata': {'created_by': 'system', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca'}, 'callbacks': [None], 'recursion_limit': 25, 'configurable': {'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'thread_ts': '1ef32717-bc81-68c8-8000-4e18ae7d67a5', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca'}, 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25'}, 'values': {'messages': [{'content': "What's the weather in SF?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': '7da1bafa-f53c-4df8-ba63-8dd517140b9f', 'example': False}]}, 'metadata': {'source': 'loop', 'step': 0, 'writes': None}}}]}, 'parent_ids': []}

Receiving new event of type: debug...
{'type': 'task', 'timestamp': '2024-06-24T21:34:06.118042+00:00', 'step': 1, 'payload': {'id': '212ed9c2-a454-50c5-a202-12066bbbe7b8', 'name': 'agent', 'input': {'some_bytes': None, 'some_byte_array': None, 'dict_with_bytes': None, 'messages': [{'content': "What's the weather in SF?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': '7da1bafa-f53c-4df8-ba63-8dd517140b9f', 'example': False}], 'sleep': None}, 'triggers': ['start:agent']}}

Receiving new event of type: events...
{'event': 'on_chain_stream', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'name': 'LangGraph', 'tags': [], 'metadata': {'created_by': 'system', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca'}, 'data': {'chunk': ['debug', {'type': 'task', 'timestamp': '2024-06-24T21:34:06.118042+00:00', 'step': 1, 'payload': {'id': '212ed9c2-a454-50c5-a202-12066bbbe7b8', 'name': 'agent', 'input': {'some_bytes': None, 'some_byte_array': None, 'dict_with_bytes': None, 'messages': [{'content': "What's the weather in SF?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': '7da1bafa-f53c-4df8-ba63-8dd517140b9f', 'example': False}], 'sleep': None}, 'triggers': ['start:agent']}}]}, 'parent_ids': []}

Receiving new event of type: events...
{'event': 'on_chain_start', 'data': {}, 'name': 'agent', 'tags': ['graph:step:1'], 'run_id': '72b74d24-5792-48da-a887-102100d6e2c0', 'metadata': {'created_by': 'system', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca', 'langgraph_step': 1, 'langgraph_node': 'agent', 'langgraph_triggers': ['start:agent'], 'langgraph_task_idx': 0}, 'parent_ids': ['1ef32717-bc30-6cf2-8a26-33f63567bc25']}

Receiving new event of type: events...
{'event': 'on_chat_model_start', 'data': {'input': {'messages': [[{'content': "What's the weather in SF?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': '7da1bafa-f53c-4df8-ba63-8dd517140b9f', 'example': False}]]}}, 'name': 'FakeListChatModel', 'tags': ['seq:step:1'], 'run_id': '2424dd6d-5cf5-4244-8d98-357640ce6e12', 'metadata': {'created_by': 'system', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca', 'langgraph_step': 1, 'langgraph_node': 'agent', 'langgraph_triggers': ['start:agent'], 'langgraph_task_idx': 0, 'ls_model_type': 'chat'}, 'parent_ids': ['1ef32717-bc30-6cf2-8a26-33f63567bc25', '72b74d24-5792-48da-a887-102100d6e2c0']}

Receiving new event of type: events...
{'event': 'on_chat_model_stream', 'data': {'chunk': {'content': 'b', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'AIMessageChunk', 'name': None, 'id': 'run-2424dd6d-5cf5-4244-8d98-357640ce6e12', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None, 'tool_call_chunks': []}}, 'run_id': '2424dd6d-5cf5-4244-8d98-357640ce6e12', 'name': 'FakeListChatModel', 'tags': ['seq:step:1'], 'metadata': {'created_by': 'system', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca', 'langgraph_step': 1, 'langgraph_node': 'agent', 'langgraph_triggers': ['start:agent'], 'langgraph_task_idx': 0, 'ls_model_type': 'chat'}, 'parent_ids': ['1ef32717-bc30-6cf2-8a26-33f63567bc25', '72b74d24-5792-48da-a887-102100d6e2c0']}

Receiving new event of type: messages/metadata...
{'run-2424dd6d-5cf5-4244-8d98-357640ce6e12': {'metadata': {'created_by': 'system', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca', 'langgraph_step': 1, 'langgraph_node': 'agent', 'langgraph_triggers': ['start:agent'], 'langgraph_task_idx': 0, 'ls_model_type': 'chat'}}}

Receiving new event of type: messages/partial...
[{'content': 'b', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-2424dd6d-5cf5-4244-8d98-357640ce6e12', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}]

Receiving new event of type: events...
{'event': 'on_chat_model_stream', 'data': {'chunk': {'content': 'e', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'AIMessageChunk', 'name': None, 'id': 'run-2424dd6d-5cf5-4244-8d98-357640ce6e12', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None, 'tool_call_chunks': []}}, 'run_id': '2424dd6d-5cf5-4244-8d98-357640ce6e12', 'name': 'FakeListChatModel', 'tags': ['seq:step:1'], 'metadata': {'created_by': 'system', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca', 'langgraph_step': 1, 'langgraph_node': 'agent', 'langgraph_triggers': ['start:agent'], 'langgraph_task_idx': 0, 'ls_model_type': 'chat'}, 'parent_ids': ['1ef32717-bc30-6cf2-8a26-33f63567bc25', '72b74d24-5792-48da-a887-102100d6e2c0']}

Receiving new event of type: messages/partial...
[{'content': 'be', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-2424dd6d-5cf5-4244-8d98-357640ce6e12', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}]

Receiving new event of type: events...
{'event': 'on_chat_model_stream', 'data': {'chunk': {'content': 'g', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'AIMessageChunk', 'name': None, 'id': 'run-2424dd6d-5cf5-4244-8d98-357640ce6e12', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None, 'tool_call_chunks': []}}, 'run_id': '2424dd6d-5cf5-4244-8d98-357640ce6e12', 'name': 'FakeListChatModel', 'tags': ['seq:step:1'], 'metadata': {'created_by': 'system', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca', 'langgraph_step': 1, 'langgraph_node': 'agent', 'langgraph_triggers': ['start:agent'], 'langgraph_task_idx': 0, 'ls_model_type': 'chat'}, 'parent_ids': ['1ef32717-bc30-6cf2-8a26-33f63567bc25', '72b74d24-5792-48da-a887-102100d6e2c0']}

Receiving new event of type: messages/partial...
[{'content': 'beg', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-2424dd6d-5cf5-4244-8d98-357640ce6e12', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}]

Receiving new event of type: events...
{'event': 'on_chat_model_stream', 'data': {'chunk': {'content': 'i', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'AIMessageChunk', 'name': None, 'id': 'run-2424dd6d-5cf5-4244-8d98-357640ce6e12', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None, 'tool_call_chunks': []}}, 'run_id': '2424dd6d-5cf5-4244-8d98-357640ce6e12', 'name': 'FakeListChatModel', 'tags': ['seq:step:1'], 'metadata': {'created_by': 'system', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca', 'langgraph_step': 1, 'langgraph_node': 'agent', 'langgraph_triggers': ['start:agent'], 'langgraph_task_idx': 0, 'ls_model_type': 'chat'}, 'parent_ids': ['1ef32717-bc30-6cf2-8a26-33f63567bc25', '72b74d24-5792-48da-a887-102100d6e2c0']}

Receiving new event of type: messages/partial...
[{'content': 'begi', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-2424dd6d-5cf5-4244-8d98-357640ce6e12', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}]

Receiving new event of type: events...
{'event': 'on_chat_model_stream', 'data': {'chunk': {'content': 'n', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'AIMessageChunk', 'name': None, 'id': 'run-2424dd6d-5cf5-4244-8d98-357640ce6e12', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None, 'tool_call_chunks': []}}, 'run_id': '2424dd6d-5cf5-4244-8d98-357640ce6e12', 'name': 'FakeListChatModel', 'tags': ['seq:step:1'], 'metadata': {'created_by': 'system', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca', 'langgraph_step': 1, 'langgraph_node': 'agent', 'langgraph_triggers': ['start:agent'], 'langgraph_task_idx': 0, 'ls_model_type': 'chat'}, 'parent_ids': ['1ef32717-bc30-6cf2-8a26-33f63567bc25', '72b74d24-5792-48da-a887-102100d6e2c0']}

Receiving new event of type: messages/partial...
[{'content': 'begin', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-2424dd6d-5cf5-4244-8d98-357640ce6e12', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}]

Receiving new event of type: events...
{'event': 'on_chat_model_end', 'data': {'output': {'content': 'begin', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-2424dd6d-5cf5-4244-8d98-357640ce6e12', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}, 'input': {'messages': [[{'content': "What's the weather in SF?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': '7da1bafa-f53c-4df8-ba63-8dd517140b9f', 'example': False}]]}}, 'run_id': '2424dd6d-5cf5-4244-8d98-357640ce6e12', 'name': 'FakeListChatModel', 'tags': ['seq:step:1'], 'metadata': {'created_by': 'system', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca', 'langgraph_step': 1, 'langgraph_node': 'agent', 'langgraph_triggers': ['start:agent'], 'langgraph_task_idx': 0, 'ls_model_type': 'chat'}, 'parent_ids': ['1ef32717-bc30-6cf2-8a26-33f63567bc25', '72b74d24-5792-48da-a887-102100d6e2c0']}

Receiving new event of type: events...
{'event': 'on_chain_start', 'data': {'input': {'messages': [{'content': "What's the weather in SF?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': '7da1bafa-f53c-4df8-ba63-8dd517140b9f', 'example': False}, {'content': 'begin', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-2424dd6d-5cf5-4244-8d98-357640ce6e12', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}], 'some_bytes': 'c29tZV9ieXRlcw==', 'some_byte_array': 'c29tZV9ieXRlX2FycmF5', 'dict_with_bytes': {'more_bytes': 'bW9yZV9ieXRlcw=='}}}, 'name': 'should_continue', 'tags': ['seq:step:3'], 'run_id': '227afb0f-f909-4d54-a042-556ca6d98a69', 'metadata': {'created_by': 'system', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca', 'langgraph_step': 1, 'langgraph_node': 'agent', 'langgraph_triggers': ['start:agent'], 'langgraph_task_idx': 0}, 'parent_ids': ['1ef32717-bc30-6cf2-8a26-33f63567bc25', '72b74d24-5792-48da-a887-102100d6e2c0']}

Receiving new event of type: events...
{'event': 'on_chain_end', 'data': {'output': 'tool', 'input': {'messages': [{'content': "What's the weather in SF?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': '7da1bafa-f53c-4df8-ba63-8dd517140b9f', 'example': False}, {'content': 'begin', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-2424dd6d-5cf5-4244-8d98-357640ce6e12', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}], 'some_bytes': 'c29tZV9ieXRlcw==', 'some_byte_array': 'c29tZV9ieXRlX2FycmF5', 'dict_with_bytes': {'more_bytes': 'bW9yZV9ieXRlcw=='}}}, 'run_id': '227afb0f-f909-4d54-a042-556ca6d98a69', 'name': 'should_continue', 'tags': ['seq:step:3'], 'metadata': {'created_by': 'system', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca', 'langgraph_step': 1, 'langgraph_node': 'agent', 'langgraph_triggers': ['start:agent'], 'langgraph_task_idx': 0}, 'parent_ids': ['1ef32717-bc30-6cf2-8a26-33f63567bc25', '72b74d24-5792-48da-a887-102100d6e2c0']}

Receiving new event of type: events...
{'event': 'on_chain_stream', 'run_id': '72b74d24-5792-48da-a887-102100d6e2c0', 'name': 'agent', 'tags': ['graph:step:1'], 'metadata': {'created_by': 'system', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca', 'langgraph_step': 1, 'langgraph_node': 'agent', 'langgraph_triggers': ['start:agent'], 'langgraph_task_idx': 0}, 'data': {'chunk': {'messages': [{'content': 'begin', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-2424dd6d-5cf5-4244-8d98-357640ce6e12', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}], 'some_bytes': 'c29tZV9ieXRlcw==', 'some_byte_array': 'c29tZV9ieXRlX2FycmF5', 'dict_with_bytes': {'more_bytes': 'bW9yZV9ieXRlcw=='}}}, 'parent_ids': ['1ef32717-bc30-6cf2-8a26-33f63567bc25']}

Receiving new event of type: events...
{'event': 'on_chain_end', 'data': {'output': {'messages': [{'content': 'begin', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-2424dd6d-5cf5-4244-8d98-357640ce6e12', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}], 'some_bytes': 'c29tZV9ieXRlcw==', 'some_byte_array': 'c29tZV9ieXRlX2FycmF5', 'dict_with_bytes': {'more_bytes': 'bW9yZV9ieXRlcw=='}}, 'input': {'some_bytes': None, 'some_byte_array': None, 'dict_with_bytes': None, 'messages': [{'content': "What's the weather in SF?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': '7da1bafa-f53c-4df8-ba63-8dd517140b9f', 'example': False}], 'sleep': None}}, 'run_id': '72b74d24-5792-48da-a887-102100d6e2c0', 'name': 'agent', 'tags': ['graph:step:1'], 'metadata': {'created_by': 'system', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca', 'langgraph_step': 1, 'langgraph_node': 'agent', 'langgraph_triggers': ['start:agent'], 'langgraph_task_idx': 0}, 'parent_ids': ['1ef32717-bc30-6cf2-8a26-33f63567bc25']}

Receiving new event of type: debug...
{'type': 'task_result', 'timestamp': '2024-06-24T21:34:06.124350+00:00', 'step': 1, 'payload': {'id': '212ed9c2-a454-50c5-a202-12066bbbe7b8', 'name': 'agent', 'result': [['some_bytes', 'c29tZV9ieXRlcw=='], ['some_byte_array', 'c29tZV9ieXRlX2FycmF5'], ['dict_with_bytes', {'more_bytes': 'bW9yZV9ieXRlcw=='}], ['messages', [{'content': 'begin', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-2424dd6d-5cf5-4244-8d98-357640ce6e12', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}]]]}}

Receiving new event of type: events...
{'event': 'on_chain_stream', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'name': 'LangGraph', 'tags': [], 'metadata': {'created_by': 'system', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca'}, 'data': {'chunk': ['debug', {'type': 'task_result', 'timestamp': '2024-06-24T21:34:06.124350+00:00', 'step': 1, 'payload': {'id': '212ed9c2-a454-50c5-a202-12066bbbe7b8', 'name': 'agent', 'result': [['some_bytes', 'c29tZV9ieXRlcw=='], ['some_byte_array', 'c29tZV9ieXRlX2FycmF5'], ['dict_with_bytes', {'more_bytes': 'bW9yZV9ieXRlcw=='}], ['messages', [{'content': 'begin', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-2424dd6d-5cf5-4244-8d98-357640ce6e12', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}]]]}}]}, 'parent_ids': []}

Receiving new event of type: events...
{'event': 'on_chain_stream', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'name': 'LangGraph', 'tags': [], 'metadata': {'created_by': 'system', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca'}, 'data': {'chunk': ['values', {'some_bytes': 'c29tZV9ieXRlcw==', 'some_byte_array': 'c29tZV9ieXRlX2FycmF5', 'dict_with_bytes': {'more_bytes': 'bW9yZV9ieXRlcw=='}, 'messages': [{'content': "What's the weather in SF?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': '7da1bafa-f53c-4df8-ba63-8dd517140b9f', 'example': False}, {'content': 'begin', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-2424dd6d-5cf5-4244-8d98-357640ce6e12', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}]}]}, 'parent_ids': []}

Receiving new event of type: debug...
{'type': 'checkpoint', 'timestamp': '2024-06-24T21:34:06.124510+00:00', 'step': 1, 'payload': {'config': {'tags': [], 'metadata': {'created_by': 'system', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca'}, 'callbacks': [None], 'recursion_limit': 25, 'configurable': {'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'thread_ts': '1ef32717-bc91-6a34-8001-26353c117c25', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca'}, 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25'}, 'values': {'some_bytes': 'c29tZV9ieXRlcw==', 'some_byte_array': 'c29tZV9ieXRlX2FycmF5', 'dict_with_bytes': {'more_bytes': 'bW9yZV9ieXRlcw=='}, 'messages': [{'content': "What's the weather in SF?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': '7da1bafa-f53c-4df8-ba63-8dd517140b9f', 'example': False}, {'content': 'begin', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-2424dd6d-5cf5-4244-8d98-357640ce6e12', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}]}, 'metadata': {'source': 'loop', 'step': 1, 'writes': {'agent': {'some_bytes': 'c29tZV9ieXRlcw==', 'some_byte_array': 'c29tZV9ieXRlX2FycmF5', 'dict_with_bytes': {'more_bytes': 'bW9yZV9ieXRlcw=='}, 'messages': [{'content': 'begin', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-2424dd6d-5cf5-4244-8d98-357640ce6e12', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}]}}}}}

Receiving new event of type: events...
{'event': 'on_chain_stream', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'name': 'LangGraph', 'tags': [], 'metadata': {'created_by': 'system', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca'}, 'data': {'chunk': ['debug', {'type': 'checkpoint', 'timestamp': '2024-06-24T21:34:06.124510+00:00', 'step': 1, 'payload': {'config': {'tags': [], 'metadata': {'created_by': 'system', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca'}, 'callbacks': [None], 'recursion_limit': 25, 'configurable': {'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'thread_ts': '1ef32717-bc91-6a34-8001-26353c117c25', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca'}, 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25'}, 'values': {'some_bytes': 'c29tZV9ieXRlcw==', 'some_byte_array': 'c29tZV9ieXRlX2FycmF5', 'dict_with_bytes': {'more_bytes': 'bW9yZV9ieXRlcw=='}, 'messages': [{'content': "What's the weather in SF?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': '7da1bafa-f53c-4df8-ba63-8dd517140b9f', 'example': False}, {'content': 'begin', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-2424dd6d-5cf5-4244-8d98-357640ce6e12', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}]}, 'metadata': {'source': 'loop', 'step': 1, 'writes': {'agent': {'some_bytes': 'c29tZV9ieXRlcw==', 'some_byte_array': 'c29tZV9ieXRlX2FycmF5', 'dict_with_bytes': {'more_bytes': 'bW9yZV9ieXRlcw=='}, 'messages': [{'content': 'begin', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-2424dd6d-5cf5-4244-8d98-357640ce6e12', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}]}}}}}]}, 'parent_ids': []}

Receiving new event of type: debug...
{'type': 'task', 'timestamp': '2024-06-24T21:34:06.124572+00:00', 'step': 2, 'payload': {'id': '44139125-a1be-57c2-9cb2-19eb62bbaf2f', 'name': 'tool', 'input': {'some_bytes': 'c29tZV9ieXRlcw==', 'some_byte_array': 'c29tZV9ieXRlX2FycmF5', 'dict_with_bytes': {'more_bytes': 'bW9yZV9ieXRlcw=='}, 'messages': [{'content': "What's the weather in SF?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': '7da1bafa-f53c-4df8-ba63-8dd517140b9f', 'example': False}, {'content': 'begin', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-2424dd6d-5cf5-4244-8d98-357640ce6e12', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}], 'sleep': None}, 'triggers': ['branch:agent:should_continue:tool']}}

Receiving new event of type: events...
{'event': 'on_chain_stream', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'name': 'LangGraph', 'tags': [], 'metadata': {'created_by': 'system', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca'}, 'data': {'chunk': ['debug', {'type': 'task', 'timestamp': '2024-06-24T21:34:06.124572+00:00', 'step': 2, 'payload': {'id': '44139125-a1be-57c2-9cb2-19eb62bbaf2f', 'name': 'tool', 'input': {'some_bytes': 'c29tZV9ieXRlcw==', 'some_byte_array': 'c29tZV9ieXRlX2FycmF5', 'dict_with_bytes': {'more_bytes': 'bW9yZV9ieXRlcw=='}, 'messages': [{'content': "What's the weather in SF?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': '7da1bafa-f53c-4df8-ba63-8dd517140b9f', 'example': False}, {'content': 'begin', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-2424dd6d-5cf5-4244-8d98-357640ce6e12', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}], 'sleep': None}, 'triggers': ['branch:agent:should_continue:tool']}}]}, 'parent_ids': []}

Receiving new event of type: events...
{'event': 'on_chain_start', 'data': {}, 'name': 'tool', 'tags': ['graph:step:2'], 'run_id': '91575720-886e-485e-ae2d-d6817e5346bf', 'metadata': {'created_by': 'system', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca', 'langgraph_step': 2, 'langgraph_node': 'tool', 'langgraph_triggers': ['branch:agent:should_continue:tool'], 'langgraph_task_idx': 0}, 'parent_ids': ['1ef32717-bc30-6cf2-8a26-33f63567bc25']}

Receiving new event of type: events...
{'event': 'on_chain_stream', 'run_id': '91575720-886e-485e-ae2d-d6817e5346bf', 'name': 'tool', 'tags': ['graph:step:2'], 'metadata': {'created_by': 'system', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca', 'langgraph_step': 2, 'langgraph_node': 'tool', 'langgraph_triggers': ['branch:agent:should_continue:tool'], 'langgraph_task_idx': 0}, 'data': {'chunk': {'messages': [{'content': 'tool_call__begin', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'tool', 'name': None, 'id': None, 'tool_call_id': 'tool_call_id'}]}}, 'parent_ids': ['1ef32717-bc30-6cf2-8a26-33f63567bc25']}

Receiving new event of type: events...
{'event': 'on_chain_end', 'data': {'output': {'messages': [{'content': 'tool_call__begin', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'tool', 'name': None, 'id': '639ca779-403d-4915-a066-327e1f634c8b', 'tool_call_id': 'tool_call_id'}]}, 'input': {'some_bytes': 'c29tZV9ieXRlcw==', 'some_byte_array': 'c29tZV9ieXRlX2FycmF5', 'dict_with_bytes': {'more_bytes': 'bW9yZV9ieXRlcw=='}, 'messages': [{'content': "What's the weather in SF?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': '7da1bafa-f53c-4df8-ba63-8dd517140b9f', 'example': False}, {'content': 'begin', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-2424dd6d-5cf5-4244-8d98-357640ce6e12', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}], 'sleep': None}}, 'run_id': '91575720-886e-485e-ae2d-d6817e5346bf', 'name': 'tool', 'tags': ['graph:step:2'], 'metadata': {'created_by': 'system', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca', 'langgraph_step': 2, 'langgraph_node': 'tool', 'langgraph_triggers': ['branch:agent:should_continue:tool'], 'langgraph_task_idx': 0}, 'parent_ids': ['1ef32717-bc30-6cf2-8a26-33f63567bc25']}

Receiving new event of type: debug...
{'type': 'task_result', 'timestamp': '2024-06-24T21:34:06.126828+00:00', 'step': 2, 'payload': {'id': '44139125-a1be-57c2-9cb2-19eb62bbaf2f', 'name': 'tool', 'result': [['messages', [{'content': 'tool_call__begin', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'tool', 'name': None, 'id': '639ca779-403d-4915-a066-327e1f634c8b', 'tool_call_id': 'tool_call_id'}]]]}}

Receiving new event of type: events...
{'event': 'on_chain_stream', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'name': 'LangGraph', 'tags': [], 'metadata': {'created_by': 'system', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca'}, 'data': {'chunk': ['debug', {'type': 'task_result', 'timestamp': '2024-06-24T21:34:06.126828+00:00', 'step': 2, 'payload': {'id': '44139125-a1be-57c2-9cb2-19eb62bbaf2f', 'name': 'tool', 'result': [['messages', [{'content': 'tool_call__begin', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'tool', 'name': None, 'id': '639ca779-403d-4915-a066-327e1f634c8b', 'tool_call_id': 'tool_call_id'}]]]}}]}, 'parent_ids': []}

Receiving new event of type: events...
{'event': 'on_chain_stream', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'name': 'LangGraph', 'tags': [], 'metadata': {'created_by': 'system', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca'}, 'data': {'chunk': ['values', {'some_bytes': 'c29tZV9ieXRlcw==', 'some_byte_array': 'c29tZV9ieXRlX2FycmF5', 'dict_with_bytes': {'more_bytes': 'bW9yZV9ieXRlcw=='}, 'messages': [{'content': "What's the weather in SF?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': '7da1bafa-f53c-4df8-ba63-8dd517140b9f', 'example': False}, {'content': 'begin', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-2424dd6d-5cf5-4244-8d98-357640ce6e12', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}, {'content': 'tool_call__begin', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'tool', 'name': None, 'id': '639ca779-403d-4915-a066-327e1f634c8b', 'tool_call_id': 'tool_call_id'}]}]}, 'parent_ids': []}

Receiving new event of type: messages/complete...
[{'content': 'tool_call__begin', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'tool', 'name': None, 'id': '639ca779-403d-4915-a066-327e1f634c8b', 'tool_call_id': 'tool_call_id'}]

Receiving new event of type: debug...
{'type': 'checkpoint', 'timestamp': '2024-06-24T21:34:06.126966+00:00', 'step': 2, 'payload': {'config': {'tags': [], 'metadata': {'created_by': 'system', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca'}, 'callbacks': [None], 'recursion_limit': 25, 'configurable': {'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'thread_ts': '1ef32717-bc97-6a06-8002-8e9ffc1ea75a', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca'}, 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25'}, 'values': {'some_bytes': 'c29tZV9ieXRlcw==', 'some_byte_array': 'c29tZV9ieXRlX2FycmF5', 'dict_with_bytes': {'more_bytes': 'bW9yZV9ieXRlcw=='}, 'messages': [{'content': "What's the weather in SF?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': '7da1bafa-f53c-4df8-ba63-8dd517140b9f', 'example': False}, {'content': 'begin', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-2424dd6d-5cf5-4244-8d98-357640ce6e12', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}, {'content': 'tool_call__begin', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'tool', 'name': None, 'id': '639ca779-403d-4915-a066-327e1f634c8b', 'tool_call_id': 'tool_call_id'}]}, 'metadata': {'source': 'loop', 'step': 2, 'writes': {'tool': {'messages': [{'content': 'tool_call__begin', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'tool', 'name': None, 'id': '639ca779-403d-4915-a066-327e1f634c8b', 'tool_call_id': 'tool_call_id'}]}}}}}

Receiving new event of type: events...
{'event': 'on_chain_stream', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'name': 'LangGraph', 'tags': [], 'metadata': {'created_by': 'system', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca'}, 'data': {'chunk': ['debug', {'type': 'checkpoint', 'timestamp': '2024-06-24T21:34:06.126966+00:00', 'step': 2, 'payload': {'config': {'tags': [], 'metadata': {'created_by': 'system', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca'}, 'callbacks': [None], 'recursion_limit': 25, 'configurable': {'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'thread_ts': '1ef32717-bc97-6a06-8002-8e9ffc1ea75a', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca'}, 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25'}, 'values': {'some_bytes': 'c29tZV9ieXRlcw==', 'some_byte_array': 'c29tZV9ieXRlX2FycmF5', 'dict_with_bytes': {'more_bytes': 'bW9yZV9ieXRlcw=='}, 'messages': [{'content': "What's the weather in SF?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': '7da1bafa-f53c-4df8-ba63-8dd517140b9f', 'example': False}, {'content': 'begin', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-2424dd6d-5cf5-4244-8d98-357640ce6e12', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}, {'content': 'tool_call__begin', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'tool', 'name': None, 'id': '639ca779-403d-4915-a066-327e1f634c8b', 'tool_call_id': 'tool_call_id'}]}, 'metadata': {'source': 'loop', 'step': 2, 'writes': {'tool': {'messages': [{'content': 'tool_call__begin', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'tool', 'name': None, 'id': '639ca779-403d-4915-a066-327e1f634c8b', 'tool_call_id': 'tool_call_id'}]}}}}}]}, 'parent_ids': []}

Receiving new event of type: debug...
{'type': 'task', 'timestamp': '2024-06-24T21:34:06.127034+00:00', 'step': 3, 'payload': {'id': 'f1ccf371-63b3-5268-a837-7f360a93c4ec', 'name': 'agent', 'input': {'some_bytes': 'c29tZV9ieXRlcw==', 'some_byte_array': 'c29tZV9ieXRlX2FycmF5', 'dict_with_bytes': {'more_bytes': 'bW9yZV9ieXRlcw=='}, 'messages': [{'content': "What's the weather in SF?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': '7da1bafa-f53c-4df8-ba63-8dd517140b9f', 'example': False}, {'content': 'begin', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-2424dd6d-5cf5-4244-8d98-357640ce6e12', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}, {'content': 'tool_call__begin', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'tool', 'name': None, 'id': '639ca779-403d-4915-a066-327e1f634c8b', 'tool_call_id': 'tool_call_id'}], 'sleep': None}, 'triggers': ['tool']}}

Receiving new event of type: events...
{'event': 'on_chain_stream', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'name': 'LangGraph', 'tags': [], 'metadata': {'created_by': 'system', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca'}, 'data': {'chunk': ['debug', {'type': 'task', 'timestamp': '2024-06-24T21:34:06.127034+00:00', 'step': 3, 'payload': {'id': 'f1ccf371-63b3-5268-a837-7f360a93c4ec', 'name': 'agent', 'input': {'some_bytes': 'c29tZV9ieXRlcw==', 'some_byte_array': 'c29tZV9ieXRlX2FycmF5', 'dict_with_bytes': {'more_bytes': 'bW9yZV9ieXRlcw=='}, 'messages': [{'content': "What's the weather in SF?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': '7da1bafa-f53c-4df8-ba63-8dd517140b9f', 'example': False}, {'content': 'begin', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-2424dd6d-5cf5-4244-8d98-357640ce6e12', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}, {'content': 'tool_call__begin', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'tool', 'name': None, 'id': '639ca779-403d-4915-a066-327e1f634c8b', 'tool_call_id': 'tool_call_id'}], 'sleep': None}, 'triggers': ['tool']}}]}, 'parent_ids': []}

Receiving new event of type: events...
{'event': 'on_chain_start', 'data': {}, 'name': 'agent', 'tags': ['graph:step:3'], 'run_id': 'b7d0900c-bfc2-43e4-b760-99bbc5bad84e', 'metadata': {'created_by': 'system', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca', 'langgraph_step': 3, 'langgraph_node': 'agent', 'langgraph_triggers': ['tool'], 'langgraph_task_idx': 0}, 'parent_ids': ['1ef32717-bc30-6cf2-8a26-33f63567bc25']}

Receiving new event of type: events...
{'event': 'on_chat_model_start', 'data': {'input': {'messages': [[{'content': "What's the weather in SF?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': '7da1bafa-f53c-4df8-ba63-8dd517140b9f', 'example': False}, {'content': 'begin', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-2424dd6d-5cf5-4244-8d98-357640ce6e12', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}, {'content': 'tool_call__begin', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'tool', 'name': None, 'id': '639ca779-403d-4915-a066-327e1f634c8b', 'tool_call_id': 'tool_call_id'}]]}}, 'name': 'FakeListChatModel', 'tags': ['seq:step:1'], 'run_id': '0f2ef0a1-0fc7-445c-9df4-55e8bb284575', 'metadata': {'created_by': 'system', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca', 'langgraph_step': 3, 'langgraph_node': 'agent', 'langgraph_triggers': ['tool'], 'langgraph_task_idx': 0, 'ls_model_type': 'chat'}, 'parent_ids': ['1ef32717-bc30-6cf2-8a26-33f63567bc25', 'b7d0900c-bfc2-43e4-b760-99bbc5bad84e']}

Receiving new event of type: events...
{'event': 'on_chat_model_stream', 'data': {'chunk': {'content': 'e', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'AIMessageChunk', 'name': None, 'id': 'run-0f2ef0a1-0fc7-445c-9df4-55e8bb284575', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None, 'tool_call_chunks': []}}, 'run_id': '0f2ef0a1-0fc7-445c-9df4-55e8bb284575', 'name': 'FakeListChatModel', 'tags': ['seq:step:1'], 'metadata': {'created_by': 'system', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca', 'langgraph_step': 3, 'langgraph_node': 'agent', 'langgraph_triggers': ['tool'], 'langgraph_task_idx': 0, 'ls_model_type': 'chat'}, 'parent_ids': ['1ef32717-bc30-6cf2-8a26-33f63567bc25', 'b7d0900c-bfc2-43e4-b760-99bbc5bad84e']}

Receiving new event of type: messages/metadata...
{'run-0f2ef0a1-0fc7-445c-9df4-55e8bb284575': {'metadata': {'created_by': 'system', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca', 'langgraph_step': 3, 'langgraph_node': 'agent', 'langgraph_triggers': ['tool'], 'langgraph_task_idx': 0, 'ls_model_type': 'chat'}}}

Receiving new event of type: messages/partial...
[{'content': 'e', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-0f2ef0a1-0fc7-445c-9df4-55e8bb284575', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}]

Receiving new event of type: events...
{'event': 'on_chat_model_stream', 'data': {'chunk': {'content': 'n', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'AIMessageChunk', 'name': None, 'id': 'run-0f2ef0a1-0fc7-445c-9df4-55e8bb284575', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None, 'tool_call_chunks': []}}, 'run_id': '0f2ef0a1-0fc7-445c-9df4-55e8bb284575', 'name': 'FakeListChatModel', 'tags': ['seq:step:1'], 'metadata': {'created_by': 'system', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca', 'langgraph_step': 3, 'langgraph_node': 'agent', 'langgraph_triggers': ['tool'], 'langgraph_task_idx': 0, 'ls_model_type': 'chat'}, 'parent_ids': ['1ef32717-bc30-6cf2-8a26-33f63567bc25', 'b7d0900c-bfc2-43e4-b760-99bbc5bad84e']}

Receiving new event of type: messages/partial...
[{'content': 'en', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-0f2ef0a1-0fc7-445c-9df4-55e8bb284575', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}]

Receiving new event of type: events...
{'event': 'on_chat_model_stream', 'data': {'chunk': {'content': 'd', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'AIMessageChunk', 'name': None, 'id': 'run-0f2ef0a1-0fc7-445c-9df4-55e8bb284575', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None, 'tool_call_chunks': []}}, 'run_id': '0f2ef0a1-0fc7-445c-9df4-55e8bb284575', 'name': 'FakeListChatModel', 'tags': ['seq:step:1'], 'metadata': {'created_by': 'system', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca', 'langgraph_step': 3, 'langgraph_node': 'agent', 'langgraph_triggers': ['tool'], 'langgraph_task_idx': 0, 'ls_model_type': 'chat'}, 'parent_ids': ['1ef32717-bc30-6cf2-8a26-33f63567bc25', 'b7d0900c-bfc2-43e4-b760-99bbc5bad84e']}

Receiving new event of type: messages/partial...
[{'content': 'end', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-0f2ef0a1-0fc7-445c-9df4-55e8bb284575', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}]

Receiving new event of type: events...
{'event': 'on_chat_model_end', 'data': {'output': {'content': 'end', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-0f2ef0a1-0fc7-445c-9df4-55e8bb284575', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}, 'input': {'messages': [[{'content': "What's the weather in SF?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': '7da1bafa-f53c-4df8-ba63-8dd517140b9f', 'example': False}, {'content': 'begin', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-2424dd6d-5cf5-4244-8d98-357640ce6e12', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}, {'content': 'tool_call__begin', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'tool', 'name': None, 'id': '639ca779-403d-4915-a066-327e1f634c8b', 'tool_call_id': 'tool_call_id'}]]}}, 'run_id': '0f2ef0a1-0fc7-445c-9df4-55e8bb284575', 'name': 'FakeListChatModel', 'tags': ['seq:step:1'], 'metadata': {'created_by': 'system', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca', 'langgraph_step': 3, 'langgraph_node': 'agent', 'langgraph_triggers': ['tool'], 'langgraph_task_idx': 0, 'ls_model_type': 'chat'}, 'parent_ids': ['1ef32717-bc30-6cf2-8a26-33f63567bc25', 'b7d0900c-bfc2-43e4-b760-99bbc5bad84e']}

Receiving new event of type: events...
{'event': 'on_chain_start', 'data': {'input': {'messages': [{'content': "What's the weather in SF?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': '7da1bafa-f53c-4df8-ba63-8dd517140b9f', 'example': False}, {'content': 'begin', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-2424dd6d-5cf5-4244-8d98-357640ce6e12', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}, {'content': 'tool_call__begin', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'tool', 'name': None, 'id': '639ca779-403d-4915-a066-327e1f634c8b', 'tool_call_id': 'tool_call_id'}, {'content': 'end', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-0f2ef0a1-0fc7-445c-9df4-55e8bb284575', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}], 'some_bytes': 'c29tZV9ieXRlcw==', 'some_byte_array': 'c29tZV9ieXRlX2FycmF5', 'dict_with_bytes': {'more_bytes': 'bW9yZV9ieXRlcw=='}}}, 'name': 'should_continue', 'tags': ['seq:step:3'], 'run_id': '8af814e9-8136-4aab-acbc-dffc5bcafdfd', 'metadata': {'created_by': 'system', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca', 'langgraph_step': 3, 'langgraph_node': 'agent', 'langgraph_triggers': ['tool'], 'langgraph_task_idx': 0}, 'parent_ids': ['1ef32717-bc30-6cf2-8a26-33f63567bc25', 'b7d0900c-bfc2-43e4-b760-99bbc5bad84e']}

Receiving new event of type: events...
{'event': 'on_chain_end', 'data': {'output': '__end__', 'input': {'messages': [{'content': "What's the weather in SF?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': '7da1bafa-f53c-4df8-ba63-8dd517140b9f', 'example': False}, {'content': 'begin', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-2424dd6d-5cf5-4244-8d98-357640ce6e12', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}, {'content': 'tool_call__begin', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'tool', 'name': None, 'id': '639ca779-403d-4915-a066-327e1f634c8b', 'tool_call_id': 'tool_call_id'}, {'content': 'end', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-0f2ef0a1-0fc7-445c-9df4-55e8bb284575', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}], 'some_bytes': 'c29tZV9ieXRlcw==', 'some_byte_array': 'c29tZV9ieXRlX2FycmF5', 'dict_with_bytes': {'more_bytes': 'bW9yZV9ieXRlcw=='}}}, 'run_id': '8af814e9-8136-4aab-acbc-dffc5bcafdfd', 'name': 'should_continue', 'tags': ['seq:step:3'], 'metadata': {'created_by': 'system', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca', 'langgraph_step': 3, 'langgraph_node': 'agent', 'langgraph_triggers': ['tool'], 'langgraph_task_idx': 0}, 'parent_ids': ['1ef32717-bc30-6cf2-8a26-33f63567bc25', 'b7d0900c-bfc2-43e4-b760-99bbc5bad84e']}

Receiving new event of type: events...
{'event': 'on_chain_stream', 'run_id': 'b7d0900c-bfc2-43e4-b760-99bbc5bad84e', 'name': 'agent', 'tags': ['graph:step:3'], 'metadata': {'created_by': 'system', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca', 'langgraph_step': 3, 'langgraph_node': 'agent', 'langgraph_triggers': ['tool'], 'langgraph_task_idx': 0}, 'data': {'chunk': {'messages': [{'content': 'end', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-0f2ef0a1-0fc7-445c-9df4-55e8bb284575', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}], 'some_bytes': 'c29tZV9ieXRlcw==', 'some_byte_array': 'c29tZV9ieXRlX2FycmF5', 'dict_with_bytes': {'more_bytes': 'bW9yZV9ieXRlcw=='}}}, 'parent_ids': ['1ef32717-bc30-6cf2-8a26-33f63567bc25']}

Receiving new event of type: events...
{'event': 'on_chain_end', 'data': {'output': {'messages': [{'content': 'end', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-0f2ef0a1-0fc7-445c-9df4-55e8bb284575', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}], 'some_bytes': 'c29tZV9ieXRlcw==', 'some_byte_array': 'c29tZV9ieXRlX2FycmF5', 'dict_with_bytes': {'more_bytes': 'bW9yZV9ieXRlcw=='}}, 'input': {'some_bytes': 'c29tZV9ieXRlcw==', 'some_byte_array': 'c29tZV9ieXRlX2FycmF5', 'dict_with_bytes': {'more_bytes': 'bW9yZV9ieXRlcw=='}, 'messages': [{'content': "What's the weather in SF?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': '7da1bafa-f53c-4df8-ba63-8dd517140b9f', 'example': False}, {'content': 'begin', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-2424dd6d-5cf5-4244-8d98-357640ce6e12', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}, {'content': 'tool_call__begin', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'tool', 'name': None, 'id': '639ca779-403d-4915-a066-327e1f634c8b', 'tool_call_id': 'tool_call_id'}], 'sleep': None}}, 'run_id': 'b7d0900c-bfc2-43e4-b760-99bbc5bad84e', 'name': 'agent', 'tags': ['graph:step:3'], 'metadata': {'created_by': 'system', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca', 'langgraph_step': 3, 'langgraph_node': 'agent', 'langgraph_triggers': ['tool'], 'langgraph_task_idx': 0}, 'parent_ids': ['1ef32717-bc30-6cf2-8a26-33f63567bc25']}

Receiving new event of type: debug...
{'type': 'task_result', 'timestamp': '2024-06-24T21:34:06.133991+00:00', 'step': 3, 'payload': {'id': 'f1ccf371-63b3-5268-a837-7f360a93c4ec', 'name': 'agent', 'result': [['some_bytes', 'c29tZV9ieXRlcw=='], ['some_byte_array', 'c29tZV9ieXRlX2FycmF5'], ['dict_with_bytes', {'more_bytes': 'bW9yZV9ieXRlcw=='}], ['messages', [{'content': 'end', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-0f2ef0a1-0fc7-445c-9df4-55e8bb284575', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}]]]}}

Receiving new event of type: events...
{'event': 'on_chain_stream', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'name': 'LangGraph', 'tags': [], 'metadata': {'created_by': 'system', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca'}, 'data': {'chunk': ['debug', {'type': 'task_result', 'timestamp': '2024-06-24T21:34:06.133991+00:00', 'step': 3, 'payload': {'id': 'f1ccf371-63b3-5268-a837-7f360a93c4ec', 'name': 'agent', 'result': [['some_bytes', 'c29tZV9ieXRlcw=='], ['some_byte_array', 'c29tZV9ieXRlX2FycmF5'], ['dict_with_bytes', {'more_bytes': 'bW9yZV9ieXRlcw=='}], ['messages', [{'content': 'end', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-0f2ef0a1-0fc7-445c-9df4-55e8bb284575', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}]]]}}]}, 'parent_ids': []}

Receiving new event of type: events...
{'event': 'on_chain_stream', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'name': 'LangGraph', 'tags': [], 'metadata': {'created_by': 'system', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca'}, 'data': {'chunk': ['values', {'some_bytes': 'c29tZV9ieXRlcw==', 'some_byte_array': 'c29tZV9ieXRlX2FycmF5', 'dict_with_bytes': {'more_bytes': 'bW9yZV9ieXRlcw=='}, 'messages': [{'content': "What's the weather in SF?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': '7da1bafa-f53c-4df8-ba63-8dd517140b9f', 'example': False}, {'content': 'begin', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-2424dd6d-5cf5-4244-8d98-357640ce6e12', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}, {'content': 'tool_call__begin', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'tool', 'name': None, 'id': '639ca779-403d-4915-a066-327e1f634c8b', 'tool_call_id': 'tool_call_id'}, {'content': 'end', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-0f2ef0a1-0fc7-445c-9df4-55e8bb284575', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}]}]}, 'parent_ids': []}

Receiving new event of type: debug...
{'type': 'checkpoint', 'timestamp': '2024-06-24T21:34:06.134190+00:00', 'step': 3, 'payload': {'config': {'tags': [], 'metadata': {'created_by': 'system', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca'}, 'callbacks': [None], 'recursion_limit': 25, 'configurable': {'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'thread_ts': '1ef32717-bca9-6418-8003-8d0d0b06845c', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca'}, 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25'}, 'values': {'some_bytes': 'c29tZV9ieXRlcw==', 'some_byte_array': 'c29tZV9ieXRlX2FycmF5', 'dict_with_bytes': {'more_bytes': 'bW9yZV9ieXRlcw=='}, 'messages': [{'content': "What's the weather in SF?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': '7da1bafa-f53c-4df8-ba63-8dd517140b9f', 'example': False}, {'content': 'begin', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-2424dd6d-5cf5-4244-8d98-357640ce6e12', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}, {'content': 'tool_call__begin', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'tool', 'name': None, 'id': '639ca779-403d-4915-a066-327e1f634c8b', 'tool_call_id': 'tool_call_id'}, {'content': 'end', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-0f2ef0a1-0fc7-445c-9df4-55e8bb284575', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}]}, 'metadata': {'source': 'loop', 'step': 3, 'writes': {'agent': {'some_bytes': 'c29tZV9ieXRlcw==', 'some_byte_array': 'c29tZV9ieXRlX2FycmF5', 'dict_with_bytes': {'more_bytes': 'bW9yZV9ieXRlcw=='}, 'messages': [{'content': 'end', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-0f2ef0a1-0fc7-445c-9df4-55e8bb284575', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}]}}}}}

Receiving new event of type: events...
{'event': 'on_chain_stream', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'name': 'LangGraph', 'tags': [], 'metadata': {'created_by': 'system', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca'}, 'data': {'chunk': ['debug', {'type': 'checkpoint', 'timestamp': '2024-06-24T21:34:06.134190+00:00', 'step': 3, 'payload': {'config': {'tags': [], 'metadata': {'created_by': 'system', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca'}, 'callbacks': [None], 'recursion_limit': 25, 'configurable': {'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'thread_ts': '1ef32717-bca9-6418-8003-8d0d0b06845c', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca'}, 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25'}, 'values': {'some_bytes': 'c29tZV9ieXRlcw==', 'some_byte_array': 'c29tZV9ieXRlX2FycmF5', 'dict_with_bytes': {'more_bytes': 'bW9yZV9ieXRlcw=='}, 'messages': [{'content': "What's the weather in SF?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': '7da1bafa-f53c-4df8-ba63-8dd517140b9f', 'example': False}, {'content': 'begin', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-2424dd6d-5cf5-4244-8d98-357640ce6e12', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}, {'content': 'tool_call__begin', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'tool', 'name': None, 'id': '639ca779-403d-4915-a066-327e1f634c8b', 'tool_call_id': 'tool_call_id'}, {'content': 'end', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-0f2ef0a1-0fc7-445c-9df4-55e8bb284575', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}]}, 'metadata': {'source': 'loop', 'step': 3, 'writes': {'agent': {'some_bytes': 'c29tZV9ieXRlcw==', 'some_byte_array': 'c29tZV9ieXRlX2FycmF5', 'dict_with_bytes': {'more_bytes': 'bW9yZV9ieXRlcw=='}, 'messages': [{'content': 'end', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-0f2ef0a1-0fc7-445c-9df4-55e8bb284575', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}]}}}}}]}, 'parent_ids': []}

Receiving new event of type: events...
{'event': 'on_chain_end', 'data': {'output': {'some_bytes': 'c29tZV9ieXRlcw==', 'some_byte_array': 'c29tZV9ieXRlX2FycmF5', 'dict_with_bytes': {'more_bytes': 'bW9yZV9ieXRlcw=='}, 'messages': [{'content': "What's the weather in SF?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': '7da1bafa-f53c-4df8-ba63-8dd517140b9f', 'example': False}, {'content': 'begin', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-2424dd6d-5cf5-4244-8d98-357640ce6e12', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}, {'content': 'tool_call__begin', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'tool', 'name': None, 'id': '639ca779-403d-4915-a066-327e1f634c8b', 'tool_call_id': 'tool_call_id'}, {'content': 'end', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-0f2ef0a1-0fc7-445c-9df4-55e8bb284575', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}]}}, 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'name': 'LangGraph', 'tags': [], 'metadata': {'created_by': 'system', 'run_id': '1ef32717-bc30-6cf2-8a26-33f63567bc25', 'user_id': '', 'graph_id': 'agent', 'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4', 'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca'}, 'parent_ids': []}

Receiving new event of type: end...
None

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to stream debug events  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_debug/) [ Next  How to Add Breakpoints  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_breakpoint/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stream_multiple/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
