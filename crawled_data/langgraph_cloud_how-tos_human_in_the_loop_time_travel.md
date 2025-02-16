---
url: https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#how-to-replay-and-branch-from-prior-states)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to Replay and Branch from Prior States 

[ ](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/?q= "Share")

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
          * [ Streaming  ](https://langchain-ai.github.io/langgraph/how-tos#streaming_1)
          * Human-in-the-loop  Human-in-the-loop 
            * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraph/how-tos#human-in-the-loop_1)
            * [ How to Add Breakpoints  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/)
            * [ How to Wait for User Input  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_user_input/)
            * [ How to Edit State of a Deployed Graph  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_edit_state/)
            * How to Replay and Branch from Prior States  [ How to Replay and Branch from Prior States  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#setup)
                * [ SDK initialization  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#sdk-initialization)
              * [ Replay a state  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#replay-a-state)
                * [ Initial invocation  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#initial-invocation)
              * [ Branch off from previous state  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#branch-off-from-previous-state)
            * [ Review Tool Calls  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_review_tool_calls/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#setup)
    * [ SDK initialization  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#sdk-initialization)
  * [ Replay a state  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#replay-a-state)
    * [ Initial invocation  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#initial-invocation)
  * [ Branch off from previous state  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#branch-off-from-previous-state)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph-platform)
  5. [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraph/how-tos#human-in-the-loop_1)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/cloud/how-tos/human_in_the_loop_time_travel.md "Edit this page")

# How to Replay and Branch from Prior States[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#how-to-replay-and-branch-from-prior-states "Permanent link")

With LangGraph Cloud you have the ability to return to any of your prior states and either re-run the graph to reproduce issues noticed during testing, or branch out in a different way from what was originally done in the prior states. In this guide we will show a quick example of how to rerun past states and how to branch off from previous states as well.

## Setup[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#setup "Permanent link")

We are not going to show the full code for the graph we are hosting, but you can see it [here](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/#build-the-agent) if you want to. Once this graph is hosted, we are ready to invoke it and wait for user input. 

### SDK initialization[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#sdk-initialization "Permanent link")

First, we need to setup our client so that we can communicate with our hosted graph:

[Python](#__tabbed_1_1)[Javascript](#__tabbed_1_2)[CURL](#__tabbed_1_3)

```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-0-1)fromlanggraph_sdkimport get_client
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-0-2)client = get_client(url=<DEPLOYMENT_URL>)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-0-3)# Using the graph deployed with the name "agent"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-0-4)assistant_id = "agent"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-0-5)thread = await client.threads.create()

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-1-1)import{Client}from"@langchain/langgraph-sdk";
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-1-2)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-1-3)constclient=newClient({apiUrl:<DEPLOYMENT_URL>});
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-1-4)// Using the graph deployed with the name "agent"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-1-5)constassistantId="agent";
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-1-6)constthread=awaitclient.threads.create();

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-2-1)curl--requestPOST\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-2-2)--url<DEPLOYMENT_URL>/threads\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-2-3)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-2-4)--data'{}'

```


## Replay a state[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#replay-a-state "Permanent link")

### Initial invocation[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#initial-invocation "Permanent link")

Before replaying a state - we need to create states to replay from! In order to do this, let's invoke our graph with a simple message:

[Python](#__tabbed_2_1)[Javascript](#__tabbed_2_2)[CURL](#__tabbed_2_3)

```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-3-1)input = {"messages": [{"role": "user", "content": "Please search the weather in SF"}]}
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-3-2)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-3-3)async for chunk in client.runs.stream(
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-3-4)  thread["thread_id"],
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-3-5)  assistant_id,
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-3-6)  input=input,
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-3-7)  stream_mode="updates",
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-3-8)):
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-3-9)  if chunk.data and chunk.event != "metadata": 
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-3-10)    print(chunk.data)

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-4-1)constinput={"messages":[{"role":"user","content":"Please search the weather in SF"}]}
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-4-2)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-4-3)conststreamResponse=client.runs.stream(
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-4-4)thread["thread_id"],
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-4-5)assistantId,
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-4-6){
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-4-7)input:input,
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-4-8)streamMode:"updates",
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-4-9)}
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-4-10));
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-4-11)forawait(constchunkofstreamResponse){
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-4-12)if(chunk.data&&chunk.event!=="metadata"){
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-4-13)console.log(chunk.data);
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-4-14)}
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-4-15)}

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-5-1)curl--requestPOST\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-5-2)--url<DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/stream\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-5-3)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-5-4)--data"{
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-5-5)  \"assistant_id\": \"agent\",
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-5-6)  \"input\": {\"messages\": [{\"role\": \"human\", \"content\": \"Please search the weather in SF\"}]},
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-5-7)  \"stream_mode\": [
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-5-8)   \"updates\"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-5-9)  ]
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-5-10) }"|\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-5-11)sed's/\r$//'|\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-5-12)awk'
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-5-13) /^event:/ {
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-5-14)   if (data_content != "" && event_type != "metadata") {
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-5-15)     print data_content "\n"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-5-16)   }
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-5-17)   sub(/^event: /, "", $0)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-5-18)   event_type = $0
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-5-19)   data_content = ""
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-5-20) }
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-5-21) /^data:/ {
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-5-22)   sub(/^data: /, "", $0)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-5-23)   data_content = $0
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-5-24) }
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-5-25) END {
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-5-26)   if (data_content != "" && event_type != "metadata") {
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-5-27)     print data_content "\n"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-5-28)   }
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-5-29) }
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-5-30) '

```


Output:

```
{'agent': {'messages': [{'content': [{'text': "Certainly! I'll use the search function to look up the current weather in San Francisco for you. Let me do that now.", 'type': 'text'}, {'id': 'toolu_011vroKUtWU7SBdrngpgpFMn', 'input': {'query': 'current weather in San Francisco'}, 'name': 'search', 'type': 'tool_use'}], 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-ee639877-d97d-40f8-96dc-d0d1ae22d203', 'example': False, 'tool_calls': [{'name': 'search', 'args': {'query': 'current weather in San Francisco'}, 'id': 'toolu_011vroKUtWU7SBdrngpgpFMn'}], 'invalid_tool_calls': [], 'usage_metadata': None}]}}
{'action': {'messages': [{'content': '["I looked up: current weather in San Francisco. Result: It\'s sunny in San Francisco, but you better look out if you\'re a Gemini 😈."]', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'tool', 'name': 'search', 'id': '7bad0e72-5ebe-4b08-9b8a-b99b0fe22fb7', 'tool_call_id': 'toolu_011vroKUtWU7SBdrngpgpFMn'}]}}
{'agent': {'messages': [{'content': "Based on the search results, I can provide you with information about the current weather in San Francisco:\n\nThe weather in San Francisco is currently sunny. This is great news for outdoor activities and enjoying the city's beautiful sights.\n\nIt's worth noting that the search result included an unusual comment about Geminis, which isn't typically part of a weather report. This might be due to the search engine including some astrological information or a joke in its results. However, for the purpose of answering your question about the weather, we can focus on the fact that it's sunny in San Francisco.\n\nIf you need any more specific information about the weather in San Francisco, such as temperature, wind speed, or forecast for the coming days, please let me know, and I'd be happy to search for that information for you.", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-dbac539a-33c8-4f0c-9e20-91f318371e7c', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}]}}

```


Now let's get our list of states, and invoke from the third state (right before the tool get called):

[Python](#__tabbed_3_1)[Javascript](#__tabbed_3_2)[CURL](#__tabbed_3_3)

```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-6-1)states = await client.threads.get_history(thread['thread_id'])
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-6-2)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-6-3)# We can confirm that this state is correct by checking the 'next' attribute and seeing that it is the tool call node
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-6-4)state_to_replay = states[2]
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-6-5)print(state_to_replay['next'])

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-7-1)conststates=awaitclient.threads.getHistory(thread['thread_id']);
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-7-2)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-7-3)// We can confirm that this state is correct by checking the 'next' attribute and seeing that it is the tool call node
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-7-4)conststateToReplay=states[2];
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-7-5)console.log(stateToReplay['next']);

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-8-1)curl--requestGET--url<DEPLOYMENT_URL>/threads/<THREAD_ID>/history|jq-r'.[2].next'

```


Output:

```
['action']

```


To rerun from a state, we need first issue an empty update to the thread state. Then we need to pass in the resulting `checkpoint_id` as follows:

[Python](#__tabbed_4_1)[Javascript](#__tabbed_4_2)[CURL](#__tabbed_4_3)

```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-9-1)state_to_replay = states[2]
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-9-2)updated_config = await client.threads.update_state(
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-9-3)  thread["thread_id"],
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-9-4)  {"messages": []},
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-9-5)  checkpoint_id=state_to_replay["checkpoint_id"]
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-9-6))
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-9-7)async for chunk in client.runs.stream(
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-9-8)  thread["thread_id"],
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-9-9)  assistant_id, # graph_id
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-9-10)  input=None,
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-9-11)  stream_mode="updates",
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-9-12)  checkpoint_id=updated_config["checkpoint_id"]
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-9-13)):
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-9-14)  if chunk.data and chunk.event != "metadata": 
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-9-15)    print(chunk.data)

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-10-1)conststateToReplay=states[2];
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-10-2)constconfig=awaitclient.threads.updateState(thread["thread_id"],{values:{"messages":[]},checkpointId:stateToReplay["checkpoint_id"]});
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-10-3)conststreamResponse=client.runs.stream(
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-10-4)thread["thread_id"],
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-10-5)assistantId,
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-10-6){
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-10-7)input:null,
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-10-8)streamMode:"updates",
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-10-9)checkpointId:config["checkpoint_id"]
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-10-10)}
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-10-11));
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-10-12)forawait(constchunkofstreamResponse){
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-10-13)if(chunk.data&&chunk.event!=="metadata"){
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-10-14)console.log(chunk.data);
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-10-15)}
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-10-16)}

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-11-1)curl--requestGET--url<DEPLOYMENT_URL>/threads/<THREAD_ID>/history|jq-c'
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-11-2)  .[2] as $state_to_replay |
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-11-3)  {
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-11-4)    values: { messages: .[2].values.messages[-1] },
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-11-5)    checkpoint_id: $state_to_replay.checkpoint_id
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-11-6)  }'|\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-11-7)curl--requestPOST\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-11-8)--url<DEPLOYMENT_URL>/threads/<THREAD_ID>/state\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-11-9)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-11-10)--data@-|jq.checkpoint_id|\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-11-11)curl--requestPOST\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-11-12)--url<DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/stream\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-11-13)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-11-14)--data"{
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-11-15)  \"assistant_id\": \"agent\",
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-11-16)  \"checkpoint_id\": \"$1\",
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-11-17)  \"stream_mode\": [
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-11-18)   \"updates\"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-11-19)  ]
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-11-20) }"|\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-11-21)sed's/\r$//'|\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-11-22)awk'
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-11-23) /^event:/ {
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-11-24)   if (data_content != "" && event_type != "metadata") {
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-11-25)     print data_content "\n"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-11-26)   }
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-11-27)   sub(/^event: /, "", $0)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-11-28)   event_type = $0
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-11-29)   data_content = ""
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-11-30) }
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-11-31) /^data:/ {
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-11-32)   sub(/^data: /, "", $0)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-11-33)   data_content = $0
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-11-34) }
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-11-35) END {
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-11-36)   if (data_content != "" && event_type != "metadata") {
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-11-37)     print data_content "\n"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-11-38)   }
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-11-39) }
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-11-40) '

```


Output:

```
{'action': {'messages': [{'content': '["I looked up: current weather in San Francisco. Result: It\'s sunny in San Francisco, but you better look out if you\'re a Gemini 😈."]', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'tool', 'name': 'search', 'id': 'eba650e5-400e-4938-8508-f878dcbcc532', 'tool_call_id': 'toolu_011vroKUtWU7SBdrngpgpFMn'}]}}
{'agent': {'messages': [{'content': "Based on the search results, I can provide you with information about the current weather in San Francisco:\n\nThe weather in San Francisco is currently sunny. This is great news if you're planning any outdoor activities or simply want to enjoy a pleasant day in the city.\n\nIt's worth noting that the search result included an unusual comment about Geminis, which doesn't seem directly related to the weather. This appears to be a playful or humorous addition to the weather report, possibly from the source where this information was obtained.\n\nIs there anything else you'd like to know about the weather in San Francisco or any other information you need?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-bc6dca3f-a1e2-4f59-a69b-fe0515a348bb', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}]}}

```


As we can see, the graph restarted from the tool node with the same input as our original graph run.

## Branch off from previous state[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#branch-off-from-previous-state "Permanent link")

Using LangGraph's checkpointing, you can do more than just replay past states. You can branch off previous locations to let the agent explore alternate trajectories or to let a user "version control" changes in a workflow.

Let's show how to do this to edit the state at a particular point in time. Let's update the state to change the input to the tool

[Python](#__tabbed_5_1)[Javascript](#__tabbed_5_2)[CURL](#__tabbed_5_3)

```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-12-1)# Let's now get the last message in the state
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-12-2)# This is the one with the tool calls that we want to update
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-12-3)last_message = state_to_replay['values']['messages'][-1]
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-12-4)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-12-5)# Let's now update the args for that tool call
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-12-6)last_message['tool_calls'][0]['args'] = {'query': 'current weather in SF'}
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-12-7)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-12-8)config = await client.threads.update_state(thread['thread_id'],{"messages":[last_message]},checkpoint_id=state_to_replay['checkpoint_id'])

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-13-1)// Let's now get the last message in the state
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-13-2)// This is the one with the tool calls that we want to update
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-13-3)letlastMessage=stateToReplay['values']['messages'][-1];
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-13-4)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-13-5)// Let's now update the args for that tool call
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-13-6)lastMessage['tool_calls'][0]['args']={'query':'current weather in SF'};
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-13-7)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-13-8)constconfig=awaitclient.threads.updateState(thread['thread_id'],{values:{"messages":[lastMessage]},checkpointId:stateToReplay['checkpoint_id']});

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-14-1)curl-s--requestGET--url<DEPLOYMENT_URL>/threads/<THREAD_ID>/history|\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-14-2)jq-c'
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-14-3)  .[2] as $state_to_replay |
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-14-4)  .[2].values.messages[-1].tool_calls[0].args.query = "current weather in SF" |
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-14-5)  {
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-14-6)    values: { messages: .[2].values.messages[-1] },
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-14-7)    checkpoint_id: $state_to_replay.checkpoint_id
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-14-8)  }'|\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-14-9)curl--requestPOST\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-14-10)--url<DEPLOYMENT_URL>/threads/<THREAD_ID>/state\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-14-11)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-14-12)--data@-

```


Now we can rerun our graph with this new config, starting from the `new_state`, which is a branch of our `state_to_replay`:

[Python](#__tabbed_6_1)[Javascript](#__tabbed_6_2)[CURL](#__tabbed_6_3)

```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-15-1)async for chunk in client.runs.stream(
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-15-2)  thread["thread_id"],
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-15-3)  assistant_id,
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-15-4)  input=None,
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-15-5)  stream_mode="updates",
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-15-6)  checkpoint_id=config['checkpoint_id']
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-15-7)):
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-15-8)  if chunk.data and chunk.event != "metadata": 
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-15-9)    print(chunk.data)

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-16-1)conststreamResponse=client.runs.stream(
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-16-2)thread["thread_id"],
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-16-3)assistantId,
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-16-4){
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-16-5)input:null,
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-16-6)streamMode:"updates",
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-16-7)checkpointId:config['checkpoint_id'],
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-16-8)}
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-16-9));
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-16-10)forawait(constchunkofstreamResponse){
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-16-11)if(chunk.data&&chunk.event!=="metadata"){
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-16-12)console.log(chunk.data);
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-16-13)}
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-16-14)}

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-17-1)curl-s--requestGET--url<DEPLOYMENT_URL>/threads/<THREAD_ID>/state|\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-17-2)jq-c'.checkpoint_id'|\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-17-3)curl--requestPOST\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-17-4)--url<DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/stream\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-17-5)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-17-6)--data"{
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-17-7)  \"assistant_id\": \"agent\",
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-17-8)  \"checkpoint_id\": \"$1\",
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-17-9)  \"stream_mode\": [
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-17-10)   \"updates\"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-17-11)  ]
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-17-12) }"|\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-17-13)sed's/\r$//'|\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-17-14)awk'
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-17-15) /^event:/ {
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-17-16)   if (data_content != "" && event_type != "metadata") {
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-17-17)     print data_content "\n"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-17-18)   }
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-17-19)   sub(/^event: /, "", $0)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-17-20)   event_type = $0
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-17-21)   data_content = ""
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-17-22) }
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-17-23) /^data:/ {
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-17-24)   sub(/^data: /, "", $0)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-17-25)   data_content = $0
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-17-26) }
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-17-27) END {
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-17-28)   if (data_content != "" && event_type != "metadata") {
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-17-29)     print data_content "\n"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-17-30)   }
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-17-31) }
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__codelineno-17-32) '

```


Output:

```
{'action': {'messages': [{'content': '["I looked up: current weather in SF. Result: It\'s sunny in San Francisco, but you better look out if you\'re a Gemini 😈."]', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'tool', 'name': 'search', 'id': '2baf9941-4fda-4081-9f87-d76795d289f1', 'tool_call_id': 'toolu_011vroKUtWU7SBdrngpgpFMn'}]}}
{'agent': {'messages': [{'content': "Based on the search results, I can provide you with information about the current weather in San Francisco (SF):\n\nThe weather in San Francisco is currently sunny. This means it's a clear day with plenty of sunshine. \n\nIt's worth noting that the specific temperature wasn't provided in the search result, but sunny weather in San Francisco typically means comfortable temperatures. San Francisco is known for its mild climate, so even on sunny days, it's often not too hot.\n\nThe search result also included a playful reference to astrological signs, mentioning Gemini. However, this is likely just a joke or part of the search engine's presentation and not related to the actual weather conditions.\n\nIs there any specific information about the weather in San Francisco you'd like to know more about? I'd be happy to perform another search if you need details on temperature, wind conditions, or the forecast for the coming days.", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-a83de52d-ed18-4402-9384-75c462485743', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}]}}

```


As we can see, the search query changed from San Francisco to SF, just as we had hoped!

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to Edit State of a Deployed Graph  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_edit_state/) [ Next  Review Tool Calls  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_review_tool_calls/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
