---
url: https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#how-to-kick-off-background-runs)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to kick off background runs 

[ ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/?q= "Share")

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
            * How to kick off background runs  [ How to kick off background runs  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#setup)
              * [ Check runs on thread  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#check-runs-on-thread)
              * [ Start runs on thread  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#start-runs-on-thread)
            * [ How to run multiple agents on the same thread  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/)
            * [ Cron Jobs  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/cron_jobs/)
            * [ Stateless Runs  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/stateless_runs/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#setup)
  * [ Check runs on thread  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#check-runs-on-thread)
  * [ Start runs on thread  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#start-runs-on-thread)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph Platform  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph-platform)
  5. [ Runs  ](https://langchain-ai.github.io/langgraphjs/how-tos#runs)



# How to kick off background runs[¶](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#how-to-kick-off-background-runs "Permanent link")

This guide covers how to kick off background runs for your agent. This can be useful for long running jobs.

## Setup[¶](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#setup "Permanent link")

First let's set up our client and thread:

[Python](#__tabbed_1_1)[Javascript](#__tabbed_1_2)[CURL](#__tabbed_1_3)

```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-0-1)fromlanggraph_sdkimport get_client
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-0-2)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-0-3)client = get_client(url=<DEPLOYMENT_URL>)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-0-4)# Using the graph deployed with the name "agent"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-0-5)assistant_id = "agent"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-0-6)# create thread
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-0-7)thread = await client.threads.create()
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-0-8)print(thread)

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-1-1)import{Client}from"@langchain/langgraph-sdk";
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-1-2)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-1-3)constclient=newClient({apiUrl:<DEPLOYMENT_URL>});
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-1-4)// Using the graph deployed with the name "agent"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-1-5)constassistantID="agent";
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-1-6)// create thread
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-1-7)constthread=awaitclient.threads.create();
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-1-8)console.log(thread);

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-2-1)curl--requestPOST\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-2-2)--url<DEPLOYMENT_URL>/threads\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-2-3)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-2-4)--data'{}'

```


Output:

```
{
  'thread_id': '5cb1e8a1-34b3-4a61-a34e-71a9799bd00d',
  'created_at': '2024-08-30T20:35:52.062934+00:00',
  'updated_at': '2024-08-30T20:35:52.062934+00:00',
  'metadata': {},
  'status': 'idle',
  'config': {},
  'values': None
}

```


## Check runs on thread[¶](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#check-runs-on-thread "Permanent link")

If we list the current runs on this thread, we will see that it's empty:

[Python](#__tabbed_2_1)[Javascript](#__tabbed_2_2)[CURL](#__tabbed_2_3)

```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-3-1)runs = await client.runs.list(thread["thread_id"])
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-3-2)print(runs)

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-4-1)letruns=awaitclient.runs.list(thread['thread_id']);
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-4-2)console.log(runs);

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-5-1)curl--requestGET\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-5-2)--url<DEPLOYMENT_URL>/threads/<THREAD_ID>/runs

```


Output:

```
[]

```


## Start runs on thread[¶](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#start-runs-on-thread "Permanent link")

Now let's kick off a run:

[Python](#__tabbed_3_1)[Javascript](#__tabbed_3_2)[CURL](#__tabbed_3_3)

```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-6-1)input = {"messages": [{"role": "user", "content": "what's the weather in sf"}]}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-6-2)run = await client.runs.create(thread["thread_id"], assistant_id, input=input)

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-7-1)letinput={"messages":[{"role":"user","content":"what's the weather in sf"}]};
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-7-2)letrun=awaitclient.runs.create(thread["thread_id"],assistantID,{input});

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-8-1)curl--requestPOST\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-8-2)--url<DEPLOYMENT_URL>/threads/<THREAD_ID>/runs\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-8-3)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-8-4)--data'{
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-8-5)    "assistant_id": <ASSISTANT_ID>
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-8-6)  }'

```


The first time we poll it, we can see `status=pending`:

[Python](#__tabbed_4_1)[Javascript](#__tabbed_4_2)[CURL](#__tabbed_4_3)

```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-9-1)print(await client.runs.get(thread["thread_id"], run["run_id"]))

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-10-1)console.log(awaitclient.runs.get(thread["thread_id"],run["run_id"]));

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-11-1)curl--requestGET\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-11-2)--url<DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/<RUN_ID>

```


Output:

```
  {
    "run_id": "1ef6a5f8-bd86-6763-bbd6-bff042db7b1b",
    "thread_id": "7885f0cf-94ad-4040-91d7-73f7ba007c8a",
    "assistant_id": "fe096781-5601-53d2-b2f6-0d3403f7e9ca",
    "created_at": "2024-09-04T01:46:47.244887+00:00",
    "updated_at": "2024-09-04T01:46:47.244887+00:00",
    "metadata": {},
    "status": "pending",
    "kwargs": {
      "input": {
        "messages": [
          {
            "role": "user",
            "content": "what's the weather in sf"
          }
        ]
      },
      "config": {
        "metadata": {
          "created_by": "system"
        },
        "configurable": {
          "run_id": "1ef6a5f8-bd86-6763-bbd6-bff042db7b1b",
          "user_id": "",
          "graph_id": "agent",
          "thread_id": "7885f0cf-94ad-4040-91d7-73f7ba007c8a",
          "assistant_id": "fe096781-5601-53d2-b2f6-0d3403f7e9ca",
          "checkpoint_id": null
        }
      },
      "webhook": null,
      "temporary": false,
      "stream_mode": [
        "values"
      ],
      "feedback_keys": null,
      "interrupt_after": null,
      "interrupt_before": null
    },
    "multitask_strategy": "reject"
  }

```


Now we can join the run, wait for it to finish and check that status again:

[Python](#__tabbed_5_1)[Javascript](#__tabbed_5_2)[CURL](#__tabbed_5_3)

```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-12-1)await client.runs.join(thread["thread_id"], run["run_id"])
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-12-2)print(await client.runs.get(thread["thread_id"], run["run_id"]))

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-13-1)awaitclient.runs.join(thread["thread_id"],run["run_id"]);
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-13-2)console.log(awaitclient.runs.get(thread["thread_id"],run["run_id"]));

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-14-1)curl--requestGET\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-14-2)--url<DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/<RUN_ID>/join&&
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-14-3)curl--requestGET\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-14-4)--url<DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/<RUN_ID>

```


Output:

```
{
  "run_id": "1ef6a5f8-bd86-6763-bbd6-bff042db7b1b",
  "thread_id": "7885f0cf-94ad-4040-91d7-73f7ba007c8a",
  "assistant_id": "fe096781-5601-53d2-b2f6-0d3403f7e9ca",
  "created_at": "2024-09-04T01:46:47.244887+00:00",
  "updated_at": "2024-09-04T01:46:47.244887+00:00",
  "metadata": {},
  "status": "success",
  "kwargs": {
    "input": {
      "messages": [
        {
          "role": "user",
          "content": "what's the weather in sf"
        }
      ]
    },
    "config": {
      "metadata": {
        "created_by": "system"
      },
      "configurable": {
        "run_id": "1ef6a5f8-bd86-6763-bbd6-bff042db7b1b",
        "user_id": "",
        "graph_id": "agent",
        "thread_id": "7885f0cf-94ad-4040-91d7-73f7ba007c8a",
        "assistant_id": "fe096781-5601-53d2-b2f6-0d3403f7e9ca",
        "checkpoint_id": null
      }
    },
    "webhook": null,
    "temporary": false,
    "stream_mode": [
      "values"
    ],
    "feedback_keys": null,
    "interrupt_after": null,
    "interrupt_before": null
  },
  "multitask_strategy": "reject"
}

```


Perfect! The run succeeded as we would expect. We can double check that the run worked as expected by printing out the final state:

[Python](#__tabbed_6_1)[Javascript](#__tabbed_6_2)[CURL](#__tabbed_6_3)

```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-15-1)final_result = await client.threads.get_state(thread["thread_id"])
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-15-2)print(final_result)

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-16-1)letfinalResult=awaitclient.threads.getState(thread["thread_id"]);
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-16-2)console.log(finalResult);

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-17-1)curl--requestGET\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-17-2)--url<DEPLOYMENT_URL>/threads/<THREAD_ID>/state

```


Output:

```
{
  "values": {
    "messages": [
      {
        "content": "what's the weather in sf",
        "additional_kwargs": {},
        "response_metadata": {},
        "type": "human",
        "name": null,
        "id": "beba31bf-320d-4125-9c37-cadf526ac47a",
        "example": false
      },
      {
        "content": [
          {
            "id": "toolu_01AaNPSPzqia21v7aAKwbKYm",
            "input": {},
            "name": "tavily_search_results_json",
            "type": "tool_use",
            "index": 0,
            "partial_json": "{\"query\": \"weather in san francisco\"}"
          }
        ],
        "additional_kwargs": {},
        "response_metadata": {
          "stop_reason": "tool_use",
          "stop_sequence": null
        },
        "type": "ai",
        "name": null,
        "id": "run-f220faf8-1d27-4f73-ad91-6bb3f47e8639",
        "example": false,
        "tool_calls": [
          {
            "name": "tavily_search_results_json",
            "args": {
              "query": "weather in san francisco"
            },
            "id": "toolu_01AaNPSPzqia21v7aAKwbKYm",
            "type": "tool_call"
          }
        ],
        "invalid_tool_calls": [],
        "usage_metadata": {
          "input_tokens": 273,
          "output_tokens": 61,
          "total_tokens": 334
        }
      },
      {
        "content": "[{\"url\": \"https://www.weatherapi.com/\", \"content\": \"{'location': {'name': 'San Francisco', 'region': 'California', 'country': 'United States of America', 'lat': 37.78, 'lon': -122.42, 'tz_id': 'America/Los_Angeles', 'localtime_epoch': 1725052131, 'localtime': '2024-08-30 14:08'}, 'current': {'last_updated_epoch': 1725051600, 'last_updated': '2024-08-30 14:00', 'temp_c': 21.1, 'temp_f': 70.0, 'is_day': 1, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/day/116.png', 'code': 1003}, 'wind_mph': 11.9, 'wind_kph': 19.1, 'wind_degree': 290, 'wind_dir': 'WNW', 'pressure_mb': 1018.0, 'pressure_in': 30.07, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 59, 'cloud': 25, 'feelslike_c': 21.1, 'feelslike_f': 70.0, 'windchill_c': 18.6, 'windchill_f': 65.5, 'heatindex_c': 18.6, 'heatindex_f': 65.5, 'dewpoint_c': 12.2, 'dewpoint_f': 54.0, 'vis_km': 16.0, 'vis_miles': 9.0, 'uv': 5.0, 'gust_mph': 15.0, 'gust_kph': 24.2}}\"}]",
        "additional_kwargs": {},
        "response_metadata": {},
        "type": "tool",
        "name": "tavily_search_results_json",
        "id": "686b2487-f332-4e58-9508-89b3a814cd81",
        "tool_call_id": "toolu_01AaNPSPzqia21v7aAKwbKYm",
        "artifact": {
          "query": "weather in san francisco",
          "follow_up_questions": null,
          "answer": null,
          "images": [],
          "results": [
            {
              "title": "Weather in San Francisco",
              "url": "https://www.weatherapi.com/",
              "content": "{'location': {'name': 'San Francisco', 'region': 'California', 'country': 'United States of America', 'lat': 37.78, 'lon': -122.42, 'tz_id': 'America/Los_Angeles', 'localtime_epoch': 1725052131, 'localtime': '2024-08-30 14:08'}, 'current': {'last_updated_epoch': 1725051600, 'last_updated': '2024-08-30 14:00', 'temp_c': 21.1, 'temp_f': 70.0, 'is_day': 1, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/day/116.png', 'code': 1003}, 'wind_mph': 11.9, 'wind_kph': 19.1, 'wind_degree': 290, 'wind_dir': 'WNW', 'pressure_mb': 1018.0, 'pressure_in': 30.07, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 59, 'cloud': 25, 'feelslike_c': 21.1, 'feelslike_f': 70.0, 'windchill_c': 18.6, 'windchill_f': 65.5, 'heatindex_c': 18.6, 'heatindex_f': 65.5, 'dewpoint_c': 12.2, 'dewpoint_f': 54.0, 'vis_km': 16.0, 'vis_miles': 9.0, 'uv': 5.0, 'gust_mph': 15.0, 'gust_kph': 24.2}}",
              "score": 0.976148,
              "raw_content": null
            }
          ],
          "response_time": 3.07
        },
        "status": "success"
      },
      {
        "content": [
          {
            "text": "\n\nThe search results provide the current weather conditions in San Francisco. According to the data, as of 2:00 PM on August 30, 2024, the temperature in San Francisco is 70\u00b0F (21.1\u00b0C) with partly cloudy skies. The wind is blowing from the west-northwest at around 12 mph (19 km/h). The humidity is 59% and visibility is 9 miles (16 km). Overall, it looks like a nice late summer day in San Francisco with comfortable temperatures and partly sunny conditions.",
            "type": "text",
            "index": 0
          }
        ],
        "additional_kwargs": {},
        "response_metadata": {
          "stop_reason": "end_turn",
          "stop_sequence": null
        },
        "type": "ai",
        "name": null,
        "id": "run-8fecc61d-3d9f-4e16-8e8a-92f702be498a",
        "example": false,
        "tool_calls": [],
        "invalid_tool_calls": [],
        "usage_metadata": {
          "input_tokens": 837,
          "output_tokens": 124,
          "total_tokens": 961
        }
      }
    ]
  },
  "next": [],
  "tasks": [],
  "metadata": {
    "step": 3,
    "run_id": "1ef67140-eb23-684b-8253-91d4c90bb05e",
    "source": "loop",
    "writes": {
      "agent": {
        "messages": [
          {
            "id": "run-8fecc61d-3d9f-4e16-8e8a-92f702be498a",
            "name": null,
            "type": "ai",
            "content": [
              {
                "text": "\n\nThe search results provide the current weather conditions in San Francisco. According to the data, as of 2:00 PM on August 30, 2024, the temperature in San Francisco is 70\u00b0F (21.1\u00b0C) with partly cloudy skies. The wind is blowing from the west-northwest at around 12 mph (19 km/h). The humidity is 59% and visibility is 9 miles (16 km). Overall, it looks like a nice late summer day in San Francisco with comfortable temperatures and partly sunny conditions.",
                "type": "text",
                "index": 0
              }
            ],
            "example": false,
            "tool_calls": [],
            "usage_metadata": {
              "input_tokens": 837,
              "total_tokens": 961,
              "output_tokens": 124
            },
            "additional_kwargs": {},
            "response_metadata": {
              "stop_reason": "end_turn",
              "stop_sequence": null
            },
            "invalid_tool_calls": []
          }
        ]
      }
    },
    "user_id": "",
    "graph_id": "agent",
    "thread_id": "5cb1e8a1-34b3-4a61-a34e-71a9799bd00d",
    "created_by": "system",
    "assistant_id": "fe096781-5601-53d2-b2f6-0d3403f7e9ca"
  },
  "created_at": "2024-08-30T21:09:00.079909+00:00",
  "checkpoint_id": "1ef67141-3ca2-6fae-8003-fe96832e57d6",
  "parent_checkpoint_id": "1ef67141-2129-6b37-8002-61fc3bf69cb5"
}

```


We can also just print the content of the last AIMessage:

[Python](#__tabbed_7_1)[Javascript](#__tabbed_7_2)[CURL](#__tabbed_7_3)

```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-18-1)print(final_result)

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-19-1)console.log(finalResult.length-1]['text']);

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-20-1)curl--requestGET\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__codelineno-20-2)--url<DEPLOYMENT_URL>/threads/<THREAD_ID>/state|jq-r'.values.messages[-1].content.[0].text'

```


Output:

```
The search results provide the current weather conditions in San Francisco. According to the data, as of 2:00 PM on August 30, 2024, the temperature in San Francisco is 70°F (21.1°C) with partly cloudy skies. The wind is blowing from the west-northwest at around 12 mph (19 km/h). The humidity is 59% and visibility is 9 miles (16 km). Overall, it looks like a nice late summer day in San Francisco with comfortable temperatures and partly sunny conditions.

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  Check the Status of your Threads  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/check_thread_status/) [ Next  How to run multiple agents on the same thread  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
