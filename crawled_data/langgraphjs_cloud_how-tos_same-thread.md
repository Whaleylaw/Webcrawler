---
url: https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#how-to-run-multiple-agents-on-the-same-thread)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to run multiple agents on the same thread 

[ ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/?q= "Share")

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
            * How to run multiple agents on the same thread  [ How to run multiple agents on the same thread  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#setup)
              * [ Run assistants on thread  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#run-assistants-on-thread)
                * [ Run OpenAI assistant  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#run-openai-assistant)
                * [ Run default assistant  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#run-default-assistant)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#setup)
  * [ Run assistants on thread  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#run-assistants-on-thread)
    * [ Run OpenAI assistant  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#run-openai-assistant)
    * [ Run default assistant  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#run-default-assistant)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph Platform  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph-platform)
  5. [ Runs  ](https://langchain-ai.github.io/langgraphjs/how-tos#runs)



# How to run multiple agents on the same thread[¶](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#how-to-run-multiple-agents-on-the-same-thread "Permanent link")

In LangGraph Cloud, a thread is not explicitly associated with a particular agent. This means that you can run multiple agents on the same thread, which allows a different agent to continue from an initial agent's progress.

In this example, we will create two agents and then call them both on the same thread. You'll see that the second agent will respond using information from the [checkpoint](https://langchain-ai.github.io/langgraph/concepts/low_level/#checkpointer-state) generated in the thread by the first agent as context.

## Setup[¶](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#setup "Permanent link")

[Python](#__tabbed_1_1)[Javascript](#__tabbed_1_2)[CURL](#__tabbed_1_3)

```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-0-1)fromlanggraph_sdkimport get_client
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-0-2)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-0-3)client = get_client(url=<DEPLOYMENT_URL>)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-0-4)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-0-5)openai_assistant = await client.assistants.create(
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-0-6)  graph_id="agent", config={"configurable": {"model_name": "openai"}}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-0-7))
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-0-8)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-0-9)# There should always be a default assistant with no configuration
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-0-10)assistants = await client.assistants.search()
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-0-11)default_assistant = [a for a in assistants if not a["config"]][0]

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-1-1)import{Client}from"@langchain/langgraph-sdk";
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-1-2)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-1-3)constclient=newClient({apiUrl:<DEPLOYMENT_URL>});
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-1-5)constopenAIAssistant=awaitclient.assistants.create(
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-1-6){graphId:"agent",config:{"configurable":{"model_name":"openai"}}}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-1-7));
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-1-8)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-1-9)constassistants=awaitclient.assistants.search();
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-1-10)constdefaultAssistant=assistants.find(a=>!a.config);

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-2-1)curl--requestPOST\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-2-2)--url<DEPLOYMENT_URL>/assistants\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-2-3)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-2-4)--data'{
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-2-5)    "graph_id": "agent",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-2-6)    "config": { "configurable": { "model_name": "openai" } }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-2-7)  }'&&\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-2-8)curl--requestPOST\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-2-9)--url<DEPLOYMENT_URL>/assistants/search\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-2-10)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-2-11)--data'{
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-2-12)    "limit": 10,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-2-13)    "offset": 0
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-2-14)  }'|jq-c'map(select(.config == null or .config == {})) | .[0]'

```


We can see that these agents are different:

[Python](#__tabbed_2_1)[Javascript](#__tabbed_2_2)[CURL](#__tabbed_2_3)

```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-3-1)print(openai_assistant)

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-4-1)console.log(openAIAssistant);

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-5-1)curl--requestGET\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-5-2)--url<DEPLOYMENT_URL>/assistants/<OPENAI_ASSISTANT_ID>

```


Output:

```
{
  "assistant_id": "db87f39d-b2b1-4da8-ac65-cf81beb3c766",
  "graph_id": "agent",
  "created_at": "2024-08-30T21:18:51.850581+00:00",
  "updated_at": "2024-08-30T21:18:51.850581+00:00",
  "config": {
    "configurable": {
      "model_name": "openai"
    }
  },
  "metadata": {}
}

```


[Python](#__tabbed_3_1)[Javascript](#__tabbed_3_2)[CURL](#__tabbed_3_3)

```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-6-1)print(default_assistant)

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-7-1)console.log(defaultAssistant);

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-8-1)curl--requestGET\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-8-2)--url<DEPLOYMENT_URL>/assistants/<DEFAULT_ASSISTANT_ID>

```


Output:

```
{
  "assistant_id": "fe096781-5601-53d2-b2f6-0d3403f7e9ca",
  "graph_id": "agent",
  "created_at": "2024-08-08T22:45:24.562906+00:00",
  "updated_at": "2024-08-08T22:45:24.562906+00:00",
  "config": {},
  "metadata": {
    "created_by": "system"
  }
}

```


## Run assistants on thread[¶](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#run-assistants-on-thread "Permanent link")

### Run OpenAI assistant[¶](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#run-openai-assistant "Permanent link")

We can now run the OpenAI assistant on the thread first.

[Python](#__tabbed_4_1)[Javascript](#__tabbed_4_2)[CURL](#__tabbed_4_3)

```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-9-1)thread = await client.threads.create()
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-9-2)input = {"messages": [{"role": "user", "content": "who made you?"}]}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-9-3)async for event in client.runs.stream(
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-9-4)  thread["thread_id"],
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-9-5)  openai_assistant["assistant_id"],
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-9-6)  input=input,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-9-7)  stream_mode="updates",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-9-8)):
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-9-9)  print(f"Receiving event of type: {event.event}")
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-9-10)  print(event.data)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-9-11)  print("\n\n")

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-10-1)constthread=awaitclient.threads.create();
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-10-2)letinput={"messages":[{"role":"user","content":"who made you?"}]}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-10-3)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-10-4)conststreamResponse=client.runs.stream(
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-10-5)thread["thread_id"],
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-10-6)openAIAssistant["assistant_id"],
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-10-7){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-10-8)input,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-10-9)streamMode:"updates"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-10-10)}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-10-11));
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-10-12)forawait(consteventofstreamResponse){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-10-13)console.log(`Receiving event of type: ${event.event}`);
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-10-14)console.log(event.data);
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-10-15)console.log("\n\n");
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-10-16)}

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-11-1)thread_id=$(curl--requestPOST\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-11-2)--url<DEPLOYMENT_URL>/threads\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-11-3)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-11-4)--data'{}'|jq-r'.thread_id')&&\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-11-5)curl--requestPOST\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-11-6)--url"<DEPLOYMENT_URL>/threads/${thread_id}/runs/stream"\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-11-7)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-11-8)--data'{
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-11-9)    "assistant_id": <OPENAI_ASSISTANT_ID>,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-11-10)    "input": {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-11-11)      "messages": [
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-11-12)        {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-11-13)          "role": "user",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-11-14)          "content": "who made you?"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-11-15)        }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-11-16)      ]
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-11-17)    },
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-11-18)    "stream_mode": [
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-11-19)      "updates"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-11-20)    ]
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-11-21)  }'|\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-11-22)sed's/\r$//'|\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-11-23)awk'
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-11-24)  /^event:/ {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-11-25)    if (data_content != "") {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-11-26)      print data_content "\n"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-11-27)    }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-11-28)    sub(/^event: /, "Receiving event of type: ", $0)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-11-29)    printf "%s...\n", $0
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-11-30)    data_content = ""
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-11-31)  }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-11-32)  /^data:/ {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-11-33)    sub(/^data: /, "", $0)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-11-34)    data_content = $0
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-11-35)  }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-11-36)  END {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-11-37)    if (data_content != "") {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-11-38)      print data_content "\n\n"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-11-39)    }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-11-40)  }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-11-41)'

```


Output:

```
Receiving event of type: metadata
{'run_id': '1ef671c5-fb83-6e70-b698-44dba2d9213e'}

Receiving event of type: updates
{'agent': {'messages': [{'content': 'I was created by OpenAI, a research organization focused on developing and advancing artificial intelligence technology.', 'additional_kwargs': {}, 'response_metadata': {'finish_reason': 'stop', 'model_name': 'gpt-4o-2024-05-13', 'system_fingerprint': 'fp_157b3831f5'}, 'type': 'ai', 'name': None, 'id': 'run-f5735b86-b80d-4c71-8dc3-4782b5a9c7c8', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}]}}

```


### Run default assistant[¶](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#run-default-assistant "Permanent link")

Now, we can run it on the default assistant and see that this second assistant is aware of the initial question, and can answer the question, "and you?":

[Python](#__tabbed_5_1)[Javascript](#__tabbed_5_2)[CURL](#__tabbed_5_3)

```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-12-1)input = {"messages": [{"role": "user", "content": "and you?"}]}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-12-2)async for event in client.runs.stream(
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-12-3)  thread["thread_id"],
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-12-4)  default_assistant["assistant_id"],
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-12-5)  input=input,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-12-6)  stream_mode="updates",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-12-7)):
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-12-8)  print(f"Receiving event of type: {event.event}")
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-12-9)  print(event.data)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-12-10)  print("\n\n")

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-13-1)letinput={"messages":[{"role":"user","content":"and you?"}]}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-13-2)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-13-3)conststreamResponse=client.runs.stream(
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-13-4)thread["thread_id"],
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-13-5)defaultAssistant["assistant_id"],
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-13-6){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-13-7)input,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-13-8)streamMode:"updates"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-13-9)}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-13-10));
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-13-11)forawait(consteventofstreamResponse){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-13-12)console.log(`Receiving event of type: ${event.event}`);
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-13-13)console.log(event.data);
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-13-14)console.log("\n\n");
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-13-15)}

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-14-1)curl--requestPOST\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-14-2)--url<DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/stream\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-14-3)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-14-4)--data'{
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-14-5)    "assistant_id": <DEFAULT_ASSISTANT_ID>,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-14-6)    "input": {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-14-7)      "messages": [
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-14-8)        {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-14-9)          "role": "user",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-14-10)          "content": "and you?"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-14-11)        }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-14-12)      ]
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-14-13)    },
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-14-14)    "stream_mode": [
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-14-15)      "updates"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-14-16)    ]
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-14-17)  }'|\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-14-18)sed's/\r$//'|\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-14-19)awk'
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-14-20)  /^event:/ {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-14-21)    if (data_content != "") {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-14-22)      print data_content "\n"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-14-23)    }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-14-24)    sub(/^event: /, "Receiving event of type: ", $0)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-14-25)    printf "%s...\n", $0
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-14-26)    data_content = ""
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-14-27)  }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-14-28)  /^data:/ {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-14-29)    sub(/^data: /, "", $0)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-14-30)    data_content = $0
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-14-31)  }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-14-32)  END {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-14-33)    if (data_content != "") {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-14-34)      print data_content "\n\n"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-14-35)    }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-14-36)  }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__codelineno-14-37)'

```


Output:

```
Receiving event of type: metadata
{'run_id': '1ef6722d-80b3-6fbb-9324-253796b1cd13'}

Receiving event of type: updates
{'agent': {'messages': [{'content': [{'text': 'I am an artificial intelligence created by Anthropic, not by OpenAI. I should not have stated that OpenAI created me, as that is incorrect. Anthropic is the company that developed and trained me using advanced language models and AI technology. I will be more careful about providing accurate information regarding my origins in the future.', 'type': 'text', 'index': 0}], 'additional_kwargs': {}, 'response_metadata': {'stop_reason': 'end_turn', 'stop_sequence': None}, 'type': 'ai', 'name': None, 'id': 'run-ebaacf62-9dd9-4165-9535-db432e4793ec', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': {'input_tokens': 302, 'output_tokens': 72, 'total_tokens': 374}}]}}

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to kick off background runs  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/background_run/) [ Next  Cron Jobs  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/cron_jobs/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/same-thread/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
