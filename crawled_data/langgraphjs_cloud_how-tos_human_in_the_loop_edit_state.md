---
url: https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#how-to-edit-state-of-a-deployed-graph)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to Edit State of a Deployed Graph 

[ ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/?q= "Share")

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
          * [ Streaming  ](https://langchain-ai.github.io/langgraphjs/how-tos#streaming_1)
          * Human-in-the-loop  Human-in-the-loop 
            * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraphjs/how-tos#human-in-the-loop_1)
            * [ How to Add Breakpoints  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_breakpoint/)
            * [ How to Wait for User Input  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/)
            * How to Edit State of a Deployed Graph  [ How to Edit State of a Deployed Graph  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#setup)
                * [ SDK initialization  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#sdk-initialization)
              * [ Editing state  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#editing-state)
                * [ Initial invocation  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#initial-invocation)
                * [ Edit the state  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#edit-the-state)
                * [ Resume invocation  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#resume-invocation)
            * [ How to Replay and Branch from Prior States  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_time_travel/)
            * [ Review Tool Calls  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#setup)
    * [ SDK initialization  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#sdk-initialization)
  * [ Editing state  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#editing-state)
    * [ Initial invocation  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#initial-invocation)
    * [ Edit the state  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#edit-the-state)
    * [ Resume invocation  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#resume-invocation)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph Platform  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph-platform)
  5. [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraphjs/how-tos#human-in-the-loop_1)



# How to Edit State of a Deployed Graph[¶](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#how-to-edit-state-of-a-deployed-graph "Permanent link")

When creating LangGraph agents, it is often nice to add a human-in-the-loop component. This can be helpful when giving them access to tools. Often in these situations you may want to edit the graph state before continuing (for example, to edit what tool is being called, or how it is being called).

This can be in several ways, but the primary supported way is to add an "interrupt" before a node is executed. This interrupts execution at that node. You can then use update_state to update the state, and then resume from that spot to continue.

## Setup[¶](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#setup "Permanent link")

We are not going to show the full code for the graph we are hosting, but you can see it [here](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop/edit-graph-state.ipynb#agent) if you want to. Once this graph is hosted, we are ready to invoke it and wait for user input.

### SDK initialization[¶](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#sdk-initialization "Permanent link")

First, we need to setup our client so that we can communicate with our hosted graph:

[Python](#__tabbed_1_1)[Javascript](#__tabbed_1_2)[CURL](#__tabbed_1_3)

```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-0-1)fromlanggraph_sdkimport get_client
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-0-2)client = get_client(url=<DEPLOYMENT_URL>)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-0-3)# Using the graph deployed with the name "agent"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-0-4)assistant_id = "agent"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-0-5)thread = await client.threads.create()

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-1-1)import{Client}from"@langchain/langgraph-sdk";
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-1-2)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-1-3)constclient=newClient({apiUrl:<DEPLOYMENT_URL>});
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-1-4)// Using the graph deployed with the name "agent"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-1-5)constassistantId="agent";
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-1-6)constthread=awaitclient.threads.create();

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-2-1)curl--requestPOST\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-2-2)--url<DEPLOYMENT_URL>/threads\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-2-3)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-2-4)--data'{}'

```


## Editing state[¶](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#editing-state "Permanent link")

### Initial invocation[¶](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#initial-invocation "Permanent link")

Now let's invoke our graph, making sure to interrupt before the `action` node.

[Python](#__tabbed_2_1)[Javascript](#__tabbed_2_2)[CURL](#__tabbed_2_3)

```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-3-1)input = { 'messages':[{ "role":"user", "content":"search for weather in SF" }] }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-3-2)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-3-3)async for chunk in client.runs.stream(
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-3-4)  thread["thread_id"],
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-3-5)  assistant_id,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-3-6)  input=input,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-3-7)  stream_mode="updates",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-3-8)  interrupt_before=["action"],
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-3-9)):
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-3-10)  if chunk.data and chunk.event != "metadata": 
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-3-11)    print(chunk.data)

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-4-1)constinput={messages:[{role:"human",content:"search for weather in SF"}]};
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-4-2)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-4-3)conststreamResponse=client.runs.stream(
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-4-4)thread["thread_id"],
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-4-5)assistantId,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-4-6){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-4-7)input:input,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-4-8)streamMode:"updates",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-4-9)interruptBefore:["action"],
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-4-10)}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-4-11));
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-4-12)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-4-13)forawait(constchunkofstreamResponse){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-4-14)if(chunk.data&&chunk.event!=="metadata"){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-4-15)console.log(chunk.data);
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-4-16)}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-4-17)}

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-5-1)curl--requestPOST\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-5-2)--url<DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/stream\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-5-3)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-5-4)--data"{
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-5-5)  \"assistant_id\": \"agent\",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-5-6)  \"input\": {\"messages\": [{\"role\": \"human\", \"content\": \"search for weather in SF\"}]},
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-5-7)  \"interrupt_before\": [\"action\"],
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-5-8)  \"stream_mode\": [
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-5-9)   \"updates\"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-5-10)  ]
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-5-11) }"|\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-5-12)sed's/\r$//'|\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-5-13)awk'
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-5-14) /^event:/ {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-5-15)   if (data_content != "" && event_type != "metadata") {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-5-16)     print data_content "\n"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-5-17)   }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-5-18)   sub(/^event: /, "", $0)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-5-19)   event_type = $0
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-5-20)   data_content = ""
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-5-21) }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-5-22) /^data:/ {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-5-23)   sub(/^data: /, "", $0)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-5-24)   data_content = $0
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-5-25) }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-5-26) END {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-5-27)   if (data_content != "" && event_type != "metadata") {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-5-28)     print data_content "\n"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-5-29)   }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-5-30) }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-5-31) '

```


Output:

```
{'agent': {'messages': [{'content': [{'text': "Certainly! I'll search for the current weather in San Francisco for you using the search function. Here's how I'll do that:", 'type': 'text'}, {'id': 'toolu_01KEJMBFozSiZoS4mAcPZeqQ', 'input': {'query': 'current weather in San Francisco'}, 'name': 'search', 'type': 'tool_use'}], 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-6dbb0167-f8f6-4e2a-ab68-229b2d1fbb64', 'example': False, 'tool_calls': [{'name': 'search', 'args': {'query': 'current weather in San Francisco'}, 'id': 'toolu_01KEJMBFozSiZoS4mAcPZeqQ'}], 'invalid_tool_calls': [], 'usage_metadata': None}]}}

```


### Edit the state[¶](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#edit-the-state "Permanent link")

Now, let's assume we actually meant to search for the weather in Sidi Frej (another city with the initials SF). We can edit the state to properly reflect that:

[Python](#__tabbed_3_1)[Javascript](#__tabbed_3_2)[CURL](#__tabbed_3_3)

```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-6-1)# First, lets get the current state
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-6-2)current_state = await client.threads.get_state(thread['thread_id'])
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-6-3)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-6-4)# Let's now get the last message in the state
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-6-5)# This is the one with the tool calls that we want to update
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-6-6)last_message = current_state[-1]
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-6-7)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-6-8)# Let's now update the args for that tool call
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-6-9)last_message['args'] = {'query': 'current weather in Sidi Frej'}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-6-10)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-6-11)# Let's now call `update_state` to pass in this message in the `messages` key
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-6-12)# This will get treated as any other update to the state
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-6-13)# It will get passed to the reducer function for the `messages` key
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-6-14)# That reducer function will use the ID of the message to update it
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-6-15)# It's important that it has the right ID! Otherwise it would get appended
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-6-16)# as a new message
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-6-17)await client.threads.update_state(thread['thread_id'], {"messages": last_message})

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-7-1)// First, let's get the current state
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-7-2)constcurrentState=awaitclient.threads.getState(thread["thread_id"]);
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-7-3)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-7-4)// Let's now get the last message in the state
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-7-5)// This is the one with the tool calls that we want to update
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-7-6)letlastMessage=currentState.values.messages.slice(-1)[0];
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-7-7)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-7-8)// Let's now update the args for that tool call
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-7-9)lastMessage.tool_calls[0].args={query:"current weather in Sidi Frej"};
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-7-10)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-7-11)// Let's now call `update_state` to pass in this message in the `messages` key
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-7-12)// This will get treated as any other update to the state
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-7-13)// It will get passed to the reducer function for the `messages` key
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-7-14)// That reducer function will use the ID of the message to update it
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-7-15)// It's important that it has the right ID! Otherwise it would get appended
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-7-16)// as a new message
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-7-17)awaitclient.threads.updateState(thread["thread_id"],{values:{messages:lastMessage}});

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-8-1)curl--requestGET--url<DEPLOYMENT_URL>/threads/<THREAD_ID>/state|\ 
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-8-2)jq'.values.messages[-1] | (.tool_calls[0].args = {"query": "current weather in Sidi Frej"})'|\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-8-3)curl--requestPOST\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-8-4)--url<DEPLOYMENT_URL>/threads/<THREAD_ID>/state\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-8-5)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-8-6)--data@-

```


Output:

```
{'configurable': {'thread_id': '9c8f1a43-9dd8-4017-9271-2c53e57cf66a',
 'checkpoint_ns': '',
 'checkpoint_id': '1ef58e7e-3641-649f-8002-8b4305a64858'}}

```


### Resume invocation[¶](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#resume-invocation "Permanent link")

Now we can resume our graph run but with the updated state:

[Python](#__tabbed_4_1)[Javascript](#__tabbed_4_2)[CURL](#__tabbed_4_3)

```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-9-1)async for chunk in client.runs.stream(
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-9-2)  thread["thread_id"],
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-9-3)  assistant_id,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-9-4)  input=None,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-9-5)  stream_mode="updates",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-9-6)):
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-9-7)  if chunk.data and chunk.event != "metadata": 
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-9-8)    print(chunk.data)

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-10-1)conststreamResponse=client.runs.stream(
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-10-2)thread["thread_id"],
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-10-3)assistantId,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-10-4){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-10-5)input:null,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-10-6)streamMode:"updates",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-10-7)}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-10-8));
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-10-9)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-10-10)forawait(constchunkofstreamResponse){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-10-11)if(chunk.data&&chunk.event!=="metadata"){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-10-12)console.log(chunk.data);
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-10-13)}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-10-14)}

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-11-1)curl--requestPOST\ 
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-11-2)--url<DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/stream\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-11-3)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-11-4)--data"{
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-11-5)  \"assistant_id\": \"agent\",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-11-6)  \"stream_mode\": [
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-11-7)   \"updates\"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-11-8)  ]
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-11-9) }"|\ 
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-11-10)sed's/\r$//'|\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-11-11)awk'
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-11-12) /^event:/ {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-11-13)   if (data_content != "" && event_type != "metadata") {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-11-14)     print data_content "\n"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-11-15)   }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-11-16)   sub(/^event: /, "", $0)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-11-17)   event_type = $0
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-11-18)   data_content = ""
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-11-19) }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-11-20) /^data:/ {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-11-21)   sub(/^data: /, "", $0)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-11-22)   data_content = $0
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-11-23) }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-11-24) END {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-11-25)   if (data_content != "" && event_type != "metadata") {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-11-26)     print data_content "\n"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-11-27)   }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-11-28) }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__codelineno-11-29) '

```


Output:

```
{'action': {'messages': [{'content': '["I looked up: current weather in Sidi Frej. Result: It\'s sunny in San Francisco, but you better look out if you\'re a Gemini 😈."]', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'tool', 'name': 'search', 'id': '1161b8d1-bee4-4188-9be8-698aecb69f10', 'tool_call_id': 'toolu_01KEJMBFozSiZoS4mAcPZeqQ'}]}}
{'agent': {'messages': [{'content': [{'text': 'I apologize for the confusion in my search query. It seems the search function interpreted "SF" as "Sidi Frej" instead of "San Francisco" as we intended. Let me search again with the full city name to get the correct information:', 'type': 'text'}, {'id': 'toolu_0111rrwgfAcmurHZn55qjqTR', 'input': {'query': 'current weather in San Francisco'}, 'name': 'search', 'type': 'tool_use'}], 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-b8c25779-cfb4-46fc-a421-48553551242f', 'example': False, 'tool_calls': [{'name': 'search', 'args': {'query': 'current weather in San Francisco'}, 'id': 'toolu_0111rrwgfAcmurHZn55qjqTR'}], 'invalid_tool_calls': [], 'usage_metadata': None}]}}
{'action': {'messages': [{'content': '["I looked up: current weather in San Francisco. Result: It\'s sunny in San Francisco, but you better look out if you\'re a Gemini 😈."]', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'tool', 'name': 'search', 'id': '6bc632ae-5ee6-4d01-9532-79c524a2d443', 'tool_call_id': 'toolu_0111rrwgfAcmurHZn55qjqTR'}]}}
{'agent': {'messages': [{'content': "Now, based on the search results, I can provide you with information about the current weather in San Francisco:\n\nThe weather in San Francisco is currently sunny. \n\nIt's worth noting that the search result included an unusual comment about Gemini, which doesn't seem directly related to the weather. This might be due to the search engine including some astrological information or a joke in its results. However, for the purpose of weather information, we can focus on the fact that it's sunny in San Francisco right now.\n\nIs there anything else you'd like to know about the weather in San Francisco or any other location?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-227a042b-dd97-476e-af32-76a3703af5d8', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}]}}

```


As you can see it now looks up the current weather in Sidi Frej (although our dummy search node still returns results for SF because we don't actually do a search in this example, we just return the same "It's sunny in San Francisco ..." result every time).

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to Wait for User Input  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/) [ Next  How to Replay and Branch from Prior States  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_time_travel/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
