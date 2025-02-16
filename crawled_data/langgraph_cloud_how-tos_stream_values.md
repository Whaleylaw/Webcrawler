---
url: https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#how-to-stream-full-state-of-your-graph)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to stream full state of your graph 

[ ](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/?q= "Share")

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
          * [ Threads  ](https://langchain-ai.github.io/langgraph/how-tos#threads)
          * [ Runs  ](https://langchain-ai.github.io/langgraph/how-tos#runs)
          * Streaming  Streaming 
            * [ Streaming  ](https://langchain-ai.github.io/langgraph/how-tos#streaming_1)
            * How to stream full state of your graph  [ How to stream full state of your graph  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#setup)
              * [ Stream graph in values mode  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#stream-graph-in-values-mode)
            * [ How to stream state updates of your graph  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_updates/)
            * [ How to stream messages from your graph  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_messages/)
            * [ How to stream events  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_events/)
            * [ How to stream debug events  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_debug/)
            * [ How to configure multiple streaming modes at the same time  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_multiple/)
            * [ How to integrate LangGraph into your React application  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#setup)
  * [ Stream graph in values mode  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#stream-graph-in-values-mode)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph-platform)
  5. [ Streaming  ](https://langchain-ai.github.io/langgraph/how-tos#streaming_1)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/cloud/how-tos/stream_values.md "Edit this page")

# How to stream full state of your graph[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#how-to-stream-full-state-of-your-graph "Permanent link")

Prerequisites

  * [Streaming](https://langchain-ai.github.io/langgraph/concepts/streaming/)



This guide covers how to use `stream_mode="values"`, which streams the value of the state at each superstep. This differs from using `stream_mode="updates"`: instead of streaming just the updates to the state from each node, it streams the entire graph state at that superstep.

## Setup[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#setup "Permanent link")

First let's set up our client and thread:

[Python](#__tabbed_1_1)[Javascript](#__tabbed_1_2)[CURL](#__tabbed_1_3)

```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-0-1)fromlanggraph_sdkimport get_client
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-0-2)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-0-3)client = get_client(url=<DEPLOYMENT_URL>)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-0-4)# Using the graph deployed with the name "agent"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-0-5)assistant_id = "agent"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-0-6)# create thread
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-0-7)thread = await client.threads.create()
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-0-8)print(thread)

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-1-1)import{Client}from"@langchain/langgraph-sdk";
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-1-2)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-1-3)constclient=newClient({apiUrl:<DEPLOYMENT_URL>});
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-1-4)// Using the graph deployed with the name "agent"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-1-5)constassistantID="agent";
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-1-6)// create thread
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-1-7)constthread=awaitclient.threads.create();
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-1-8)console.log(thread);

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-2-1)curl--requestPOST\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-2-2)--url<DEPLOYMENT_URL>/threads\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-2-3)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-2-4)--data'{}'

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


## Stream graph in values mode[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#stream-graph-in-values-mode "Permanent link")

Now we can stream by values, which streams the full state of the graph after each node has finished executing:

[Python](#__tabbed_2_1)[Javascript](#__tabbed_2_2)[CURL](#__tabbed_2_3)

```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-3-1)input = {"messages": [{"role": "user", "content": "what's the weather in la"}]}
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-3-2)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-3-3)# stream values
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-3-4)async for chunk in client.runs.stream(
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-3-5)  thread["thread_id"],
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-3-6)  assistant_id, 
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-3-7)  input=input,
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-3-8)  stream_mode="values"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-3-9)):
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-3-10)  print(f"Receiving new event of type: {chunk.event}...")
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-3-11)  print(chunk.data)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-3-12)  print("\n\n")

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-4-1)constinput={"messages":[{"role":"user","content":"what's the weather in la"}]}
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-4-2)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-4-3)conststreamResponse=client.runs.stream(
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-4-4)thread["thread_id"],
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-4-5)assistantID,
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-4-6){
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-4-7)input,
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-4-8)streamMode:"values"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-4-9)}
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-4-10));
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-4-11)forawait(constchunkofstreamResponse){
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-4-12)console.log(`Receiving new event of type: ${chunk.event}...`);
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-4-13)console.log(chunk.data);
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-4-14)console.log("\n\n");
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-4-15)}

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-5-1)curl--requestPOST\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-5-2)--url<DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/stream\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-5-3)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-5-4)--data"{
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-5-5)  \"assistant_id\": \"agent\",
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-5-6)  \"input\": {\"messages\": [{\"role\": \"human\", \"content\": \"what's the weather in la\"}]},
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-5-7)  \"stream_mode\": [
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-5-8)   \"values\"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-5-9)  ]
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-5-10) }"|\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-5-11)sed's/\r$//'|\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-5-12)awk'
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-5-13) /^event:/ {
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-5-14)   if (data_content != "") {
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-5-15)     print data_content "\n"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-5-16)   }
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-5-17)   sub(/^event: /, "Receiving event of type: ", $0)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-5-18)   printf "%s...\n", $0
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-5-19)   data_content = ""
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-5-20) }
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-5-21) /^data:/ {
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-5-22)   sub(/^data: /, "", $0)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-5-23)   data_content = $0
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-5-24) }
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-5-25) END {
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-5-26)   if (data_content != "") {
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-5-27)     print data_content "\n"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-5-28)   }
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-5-29) }
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-5-30) '

```


Output:

```
Receiving new event of type: metadata...
{"run_id": "f08791ce-0a3d-44e0-836c-ff62cd2e2786"}

Receiving new event of type: values...
{
 "messages": [
  {
   "role": "human",
   "content": "what's the weather in la"
  }
 ]
}

Receiving new event of type: values...
{
 "messages": [
  {
   "content": "what's the weather in la",
   "type": "human",
   ...
  },
  {
   "content": "",
   "type": "ai",
   "tool_calls": [
    {
     "name": "tavily_search_results_json",
     "args": {
      "query": "weather in los angeles"
     },
     "id": "toolu_01E5mSaZWm5rWJnCqmt63v4g"
    }
   ],
   ...
  }
 ]
}
...
Receiving new event of type: values...
{
 "messages": [
  {
   "content": "what's the weather in la",
   "type": "human",
   ...
  },
  {
   "content": "",
   "type": "ai",
   "tool_calls": [
    {
     "name": "tavily_search_results_json",
     "args": {
      "query": "weather in los angeles"
     },
     "id": "toolu_01E5mSaZWm5rWJnCqmt63v4g"
    }
   ],
   ...
  }
  {
   "content": [
    {
     "url": "https://www.weatherapi.com/",
     "content": "{\"location\": {\"name\": \"Los Angeles\", \"region\": \"California\", \"country\": \"United States of America\", \"lat\": 34.05, \"lon\": -118.24, \"tz_id\": \"America/Los_Angeles\", \"localtime_epoch\": 1716310320, \"localtime\": \"2024-05-21 9:52\"}, \"current\": {\"last_updated_epoch\": 1716309900, \"last_updated\": \"2024-05-21 09:45\", \"temp_c\": 16.7, \"temp_f\": 62.1, \"is_day\": 1, \"condition\": {\"text\": \"Overcast\", \"icon\": \"//cdn.weatherapi.com/weather/64x64/day/122.png\", \"code\": 1009}, \"wind_mph\": 8.1, \"wind_kph\": 13.0, \"wind_degree\": 250, \"wind_dir\": \"WSW\", \"pressure_mb\": 1015.0, \"pressure_in\": 29.97, \"precip_mm\": 0.0, \"precip_in\": 0.0, \"humidity\": 65, \"cloud\": 100, \"feelslike_c\": 16.7, \"feelslike_f\": 62.1, \"vis_km\": 16.0, \"vis_miles\": 9.0, \"uv\": 5.0, \"gust_mph\": 12.5, \"gust_kph\": 20.2}}"
    }
   ],
   "type": "tool",
   "name": "tavily_search_results_json",
   "tool_call_id": "toolu_01E5mSaZWm5rWJnCqmt63v4g"
   ...
  },
  {
   "content": "Based on the weather API results, the current weather in Los Angeles is overcast with a temperature of around 62°F (17°C). There are light winds from the west-southwest around 8-13 mph. The humidity is 65% and visibility is good at 9 miles. Overall, mild spring weather conditions in LA.",
   "type": "ai",
   ...
  }
 ]
}

Receiving new event of type: end...
None

```


If we want to just get the final result, we can use this endpoint and just keep track of the last value we received

[Python](#__tabbed_3_1)[Javascript](#__tabbed_3_2)[CURL](#__tabbed_3_3)

```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-6-1)final_answer = None
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-6-2)async for chunk in client.runs.stream(
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-6-3)  thread["thread_id"],
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-6-4)  assistant_id,
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-6-5)  input=input,
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-6-6)  stream_mode="values"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-6-7)):
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-6-8)  if chunk.event == "values":
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-6-9)    final_answer = chunk.data

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-7-1)letfinalAnswer;
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-7-2)conststreamResponse=client.runs.stream(
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-7-3)thread["thread_id"],
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-7-4)assistantID,
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-7-5){
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-7-6)input,
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-7-7)streamMode:"values"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-7-8)}
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-7-9));
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-7-10)forawait(constchunkofstreamResponse){
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-7-11)finalAnswer=chunk.data;
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-7-12)}

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-8-1)curl--requestPOST\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-8-2)--url<DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/stream\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-8-3)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-8-4)--data"{
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-8-5)  \"assistant_id\": \"agent\",
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-8-6)  \"input\": {\"messages\": [{\"role\": \"human\", \"content\": \"what's the weather in la\"}]},
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-8-7)  \"stream_mode\": [
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-8-8)   \"values\"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-8-9)  ]
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-8-10) }"|\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-8-11)sed's/\r$//'|\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-8-12)awk'
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-8-13) /^data:/ { 
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-8-14)   sub(/^data: /, "", $0)  
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-8-15)   data_content = $0     
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-8-16) }  
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-8-17) END {                        
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-8-18)   if (data_content != "") {
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-8-19)     print data_content
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-8-20)   }
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-8-21) }     
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__codelineno-8-22) '

```


Output:

```
{
 "messages": [
  {
   "content": "what's the weather in la",
   "type": "human",
   ...
  },
  {
   "type": "ai",
   "tool_calls": [
    {
     "name": "tavily_search_results_json",
     "args": {
      "query": "weather in los angeles"
     },
     "id": "toolu_01E5mSaZWm5rWJnCqmt63v4g"
    }
   ],
   ...
  }
  {
   "content": [
    {
     "url": "https://www.weatherapi.com/",
     "content": "{\"location\": {\"name\": \"Los Angeles\", \"region\": \"California\", \"country\": \"United States of America\", \"lat\": 34.05, \"lon\": -118.24, \"tz_id\": \"America/Los_Angeles\", \"localtime_epoch\": 1716310320, \"localtime\": \"2024-05-21 9:52\"}, \"current\": {\"last_updated_epoch\": 1716309900, \"last_updated\": \"2024-05-21 09:45\", \"temp_c\": 16.7, \"temp_f\": 62.1, \"is_day\": 1, \"condition\": {\"text\": \"Overcast\", \"icon\": \"//cdn.weatherapi.com/weather/64x64/day/122.png\", \"code\": 1009}, \"wind_mph\": 8.1, \"wind_kph\": 13.0, \"wind_degree\": 250, \"wind_dir\": \"WSW\", \"pressure_mb\": 1015.0, \"pressure_in\": 29.97, \"precip_mm\": 0.0, \"precip_in\": 0.0, \"humidity\": 65, \"cloud\": 100, \"feelslike_c\": 16.7, \"feelslike_f\": 62.1, \"vis_km\": 16.0, \"vis_miles\": 9.0, \"uv\": 5.0, \"gust_mph\": 12.5, \"gust_kph\": 20.2}}"
    }
   ],
   "type": "tool",
   "name": "tavily_search_results_json",
   "tool_call_id": "toolu_01E5mSaZWm5rWJnCqmt63v4g"
   ...
  },
  {
   "content": "Based on the weather API results, the current weather in Los Angeles is overcast with a temperature of around 62°F (17°C). There are light winds from the west-southwest around 8-13 mph. The humidity is 65% and visibility is good at 9 miles. Overall, mild spring weather conditions in LA.",
   "type": "ai",
   ...
  }
 ]
}

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Stateless Runs  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/stateless_runs/) [ Next  How to stream state updates of your graph  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_updates/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
