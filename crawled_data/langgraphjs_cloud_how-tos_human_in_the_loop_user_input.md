---
url: https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#how-to-wait-for-user-input)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to Wait for User Input 

[ ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/?q= "Share")

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
            * How to Wait for User Input  [ How to Wait for User Input  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#setup)
                * [ SDK initialization  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#sdk-initialization)
              * [ Waiting for user input  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#waiting-for-user-input)
                * [ Initial invocation  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#initial-invocation)
                * [ Adding user input to state  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#adding-user-input-to-state)
                * [ Invoking after receiving human input  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#invoking-after-receiving-human-input)
            * [ How to Edit State of a Deployed Graph  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#setup)
    * [ SDK initialization  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#sdk-initialization)
  * [ Waiting for user input  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#waiting-for-user-input)
    * [ Initial invocation  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#initial-invocation)
    * [ Adding user input to state  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#adding-user-input-to-state)
    * [ Invoking after receiving human input  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#invoking-after-receiving-human-input)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph Platform  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph-platform)
  5. [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraphjs/how-tos#human-in-the-loop_1)



# How to Wait for User Input[¶](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#how-to-wait-for-user-input "Permanent link")

One of the main human-in-the-loop interaction patterns is waiting for human input. A key use case involves asking the user clarifying questions. One way to accomplish this is simply go to the `END` node and exit the graph. Then, any user response comes back in as fresh invocation of the graph. This is basically just creating a chatbot architecture.

The issue with this is it is tough to resume back in a particular point in the graph. Often times the agent is halfway through some process, and just needs a bit of a user input. Although it is possible to design your graph in such a way where you have a `conditional_entry_point` to route user messages back to the right place, that is not super scalable (as it essentially involves having a routing function that can end up almost anywhere).

A separate way to do this is to have a node explicitly for getting user input. This is easy to implement in a notebook setting - you just put an `input()` call in the node. But that isn't exactly production ready.

Luckily, LangGraph makes it possible to do similar things in a production way. The basic idea is:

  * Set up a node that represents human input. This can have specific incoming/outgoing edges (as you desire). There shouldn't actually be any logic inside this node.
  * Add a breakpoint before the node. This will stop the graph before this node executes (which is good, because there's no real logic in it anyways)
  * Use `.update_state` to update the state of the graph. Pass in whatever human response you get. The key here is to use the `as_node` parameter to apply this update **as if you were that node**. This will have the effect of making it so that when you resume execution next it resumes as if that node just acted, and not from the beginning.



## Setup[¶](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#setup "Permanent link")

We are not going to show the full code for the graph we are hosting, but you can see it [here](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop/wait-user-input.ipynb#agent) if you want to. Once this graph is hosted, we are ready to invoke it and wait for user input.

### SDK initialization[¶](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#sdk-initialization "Permanent link")

First, we need to setup our client so that we can communicate with our hosted graph:

[Python](#__tabbed_1_1)[Javascript](#__tabbed_1_2)[CURL](#__tabbed_1_3)

```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-0-1)fromlanggraph_sdkimport get_client
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-0-2)client = get_client(url=<DEPLOYMENT_URL>)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-0-3)# Using the graph deployed with the name "agent"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-0-4)assistant_id = "agent"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-0-5)thread = await client.threads.create()

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-1-1)import{Client}from"@langchain/langgraph-sdk";
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-1-2)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-1-3)constclient=newClient({apiUrl:<DEPLOYMENT_URL>});
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-1-4)// Using the graph deployed with the name "agent"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-1-5)constassistantId="agent";
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-1-6)constthread=awaitclient.threads.create();

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-2-1)curl--requestPOST\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-2-2)--url<DEPLOYMENT_URL>/threads\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-2-3)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-2-4)--data'{}'

```


## Waiting for user input[¶](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#waiting-for-user-input "Permanent link")

### Initial invocation[¶](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#initial-invocation "Permanent link")

Now, let's invoke our graph by interrupting before `ask_human` node:

[Python](#__tabbed_2_1)[Javascript](#__tabbed_2_2)[CURL](#__tabbed_2_3)

```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-3-1)input = {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-3-2)  "messages": [
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-3-3)    {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-3-4)      "role": "user",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-3-5)      "content": "Use the search tool to ask the user where they are, then look up the weather there",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-3-6)    }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-3-7)  ]
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-3-8)}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-3-9)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-3-10)async for chunk in client.runs.stream(
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-3-11)  thread["thread_id"],
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-3-12)  assistant_id,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-3-13)  input=input,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-3-14)  stream_mode="updates",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-3-15)  interrupt_before=["ask_human"],
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-3-16)):
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-3-17)  if chunk.data and chunk.event != "metadata": 
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-3-18)    print(chunk.data)

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-4-1)constinput={
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-4-2)messages:[
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-4-3){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-4-4)role:"human",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-4-5)content:"Use the search tool to ask the user where they are, then look up the weather there"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-4-6)}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-4-7)]
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-4-8)};
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-4-9)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-4-10)conststreamResponse=client.runs.stream(
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-4-11)thread["thread_id"],
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-4-12)assistantId,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-4-13){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-4-14)input:input,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-4-15)streamMode:"updates",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-4-16)interruptBefore:["ask_human"]
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-4-17)}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-4-18));
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-4-19)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-4-20)forawait(constchunkofstreamResponse){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-4-21)if(chunk.data&&chunk.event!=="metadata"){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-4-22)console.log(chunk.data);
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-4-23)}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-4-24)}

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-5-1)curl--requestPOST\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-5-2)--url<DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/stream\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-5-3)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-5-4)--data"{
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-5-5)  \"assistant_id\": \"agent\",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-5-6)  \"input\": {\"messages\": [{\"role\": \"human\", \"content\": \"Use the search tool to ask the user where they are, then look up the weather there\"}]},
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-5-7)  \"interrupt_before\": [\"ask_human\"],
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-5-8)  \"stream_mode\": [
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-5-9)   \"updates\"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-5-10)  ]
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-5-11) }"|\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-5-12)sed's/\r$//'|\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-5-13)awk'
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-5-14) /^event:/ {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-5-15)   if (data_content != "" && event_type != "metadata") {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-5-16)     print data_content "\n"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-5-17)   }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-5-18)   sub(/^event: /, "", $0)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-5-19)   event_type = $0
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-5-20)   data_content = ""
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-5-21) }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-5-22) /^data:/ {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-5-23)   sub(/^data: /, "", $0)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-5-24)   data_content = $0
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-5-25) }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-5-26) END {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-5-27)   if (data_content != "" && event_type != "metadata") {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-5-28)     print data_content "\n"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-5-29)   }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-5-30) }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-5-31) '

```


Output:

```
{'agent': {'messages': [{'content': [{'text': "Certainly! I'll use the AskHuman function to ask the user about their location, and then I'll use the search function to look up the weather for that location. Let's start by asking the user where they are.", 'type': 'text'}, {'id': 'toolu_01RFahzYPvnPWTb2USk2RdKR', 'input': {'question': 'Where are you currently located?'}, 'name': 'AskHuman', 'type': 'tool_use'}], 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-a8422215-71d3-4093-afb4-9db141c94ddb', 'example': False, 'tool_calls': [{'name': 'AskHuman', 'args': {'question': 'Where are you currently located?'}, 'id': 'toolu_01RFahzYPvnPWTb2USk2RdKR'}], 'invalid_tool_calls': [], 'usage_metadata': None}]}}

```


### Adding user input to state[¶](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#adding-user-input-to-state "Permanent link")

We now want to update this thread with a response from the user. We then can kick off another run.

Because we are treating this as a tool call, we will need to update the state as if it is a response from a tool call. In order to do this, we will need to check the state to get the ID of the tool call.

[Python](#__tabbed_3_1)[Javascript](#__tabbed_3_2)[CURL](#__tabbed_3_3)

```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-6-1)state = await client.threads.get_state(thread['thread_id'])
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-6-2)tool_call_id = state
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-6-3)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-6-4)# We now create the tool call with the id and the response we want
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-6-5)tool_message = [{"tool_call_id": tool_call_id, "type": "tool", "content": "san francisco"}]
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-6-6)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-6-7)await client.threads.update_state(thread['thread_id'], {"messages": tool_message}, as_node="ask_human")

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-7-1)conststate=awaitclient.threads.getState(thread["thread_id"]);
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-7-2)consttoolCallId=state.values.messages[state.values.messages.length-1].tool_calls[0].id;
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-7-3)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-7-4)// We now create the tool call with the id and the response we want
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-7-5)consttoolMessage=[
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-7-6){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-7-7)tool_call_id:toolCallId,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-7-8)type:"tool",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-7-9)content:"san francisco"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-7-10)}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-7-11)];
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-7-12)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-7-13)awaitclient.threads.updateState(
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-7-14)thread["thread_id"],
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-7-15){values:{messages:toolMessage}},
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-7-16){asNode:"ask_human"}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-7-17));

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-8-1)curl--requestGET\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-8-2)--url<DEPLOYMENT_URL>/threads/<THREAD_ID>/state\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-8-3)|jq-r'.values.messages[-1].tool_calls[0].id'\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-8-4)|sh-c'
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-8-5)   TOOL_CALL_ID="$1"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-8-6)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-8-7)   # Construct the JSON payload
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-8-8)   JSON_PAYLOAD=$(printf "{\"messages\": [{\"tool_call_id\": \"%s\", \"type\": \"tool\", \"content\": \"san francisco\"}], \"as_node\": \"ask_human\"}" "$TOOL_CALL_ID")
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-8-9)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-8-10)   # Send the updated state
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-8-11)   curl --request POST \
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-8-12)     --url <DEPLOYMENT_URL>/threads/<THREAD_ID>/state \
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-8-13)     --header "Content-Type: application/json" \
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-8-14)     --data "${JSON_PAYLOAD}"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-8-15) '_

```


Output:

```
{'configurable': {'thread_id': 'a9f322ae-4ed1-41ec-942b-38cb3d342c3a',
'checkpoint_ns': '',
'checkpoint_id': '1ef58e97-a623-63dd-8002-39a9a9b20be3'}}

```


### Invoking after receiving human input[¶](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#invoking-after-receiving-human-input "Permanent link")

We can now tell the agent to continue. We can just pass in None as the input to the graph, since no additional input is needed:

[Python](#__tabbed_4_1)[Javascript](#__tabbed_4_2)[CURL](#__tabbed_4_3)

```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-9-1)async for chunk in client.runs.stream(
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-9-2)  thread["thread_id"],
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-9-3)  assistant_id,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-9-4)  input=None,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-9-5)  stream_mode="updates",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-9-6)):
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-9-7)  if chunk.data and chunk.event != "metadata": 
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-9-8)    print(chunk.data)

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-10-1)conststreamResponse=client.runs.stream(
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-10-2)thread["thread_id"],
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-10-3)assistantId,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-10-4){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-10-5)input:null,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-10-6)streamMode:"updates"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-10-7)}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-10-8));
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-10-9)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-10-10)forawait(constchunkofstreamResponse){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-10-11)if(chunk.data&&chunk.event!=="metadata"){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-10-12)console.log(chunk.data);
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-10-13)}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-10-14)}

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-11-1)curl--requestPOST\ 
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-11-2)--url<DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/stream\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-11-3)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-11-4)--data"{
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-11-5)  \"assistant_id\": \"agent\",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-11-6)  \"stream_mode\": [
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-11-7)   \"updates\"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-11-8)  ]
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-11-9) }"|\ 
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-11-10)sed's/\r$//'|\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-11-11)awk'
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-11-12) /^event:/ {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-11-13)   if (data_content != "" && event_type != "metadata") {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-11-14)     print data_content "\n"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-11-15)   }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-11-16)   sub(/^event: /, "", $0)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-11-17)   event_type = $0
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-11-18)   data_content = ""
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-11-19) }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-11-20) /^data:/ {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-11-21)   sub(/^data: /, "", $0)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-11-22)   data_content = $0
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-11-23) }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-11-24) END {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-11-25)   if (data_content != "" && event_type != "metadata") {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-11-26)     print data_content "\n"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-11-27)   }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-11-28) }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__codelineno-11-29) '

```


Output:

```
{'agent': {'messages': [{'content': [{'text': "Thank you for letting me know that you're in San Francisco. Now, I'll use the search function to look up the weather in San Francisco.", 'type': 'text'}, {'id': 'toolu_01K57ofmgG2wyJ8tYJjbq5k7', 'input': {'query': 'current weather in San Francisco'}, 'name': 'search', 'type': 'tool_use'}], 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-241baed7-db5e-44ce-ac3c-56431705c22b', 'example': False, 'tool_calls': [{'name': 'search', 'args': {'query': 'current weather in San Francisco'}, 'id': 'toolu_01K57ofmgG2wyJ8tYJjbq5k7'}], 'invalid_tool_calls': [], 'usage_metadata': None}]}}
{'action': {'messages': [{'content': '["I looked up: current weather in San Francisco. Result: It\'s sunny in San Francisco, but you better look out if you\'re a Gemini 😈."]', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'tool', 'name': 'search', 'id': '8b699b95-8546-4557-8e66-14ea71a15ed8', 'tool_call_id': 'toolu_01K57ofmgG2wyJ8tYJjbq5k7'}]}}
{'agent': {'messages': [{'content': "Based on the search results, I can provide you with information about the current weather in San Francisco:\n\nThe weather in San Francisco is currently sunny. It's a beautiful day in the city! \n\nHowever, I should note that the search result included an unusual comment about Gemini zodiac signs. This appears to be either a joke or potentially irrelevant information added by the search engine. For accurate and detailed weather information, you might want to check a reliable weather service or app for San Francisco.\n\nIs there anything else you'd like to know about the weather or San Francisco?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-b4d7309f-f849-46aa-b6ef-475bcabd2be9', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}]}}

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to Add Breakpoints  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_breakpoint/) [ Next  How to Edit State of a Deployed Graph  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_user_input/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
