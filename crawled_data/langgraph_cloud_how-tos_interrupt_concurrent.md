---
url: https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#interrupt)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Interrupt 

[ ](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/?q= "Share")

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
          * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraph/how-tos#human-in-the-loop_1)
          * Double-texting  Double-texting 
            * [ Double-texting  ](https://langchain-ai.github.io/langgraph/how-tos#double-texting)
            * Interrupt  [ Interrupt  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#setup)
              * [ Create runs  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#create-runs)
              * [ View run results  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#view-run-results)
            * [ Rollback  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/)
            * [ Reject  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/reject_concurrent/)
            * [ Enqueue  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/enqueue_concurrent/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#setup)
  * [ Create runs  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#create-runs)
  * [ View run results  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#view-run-results)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph-platform)
  5. [ Double-texting  ](https://langchain-ai.github.io/langgraph/how-tos#double-texting)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/cloud/how-tos/interrupt_concurrent.md "Edit this page")

# Interrupt[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#interrupt "Permanent link")

This guide assumes knowledge of what double-texting is, which you can learn about in the [double-texting conceptual guide](https://langchain-ai.github.io/langgraph/concepts/double_texting/).

The guide covers the `interrupt` option for double texting, which interrupts the prior run of the graph and starts a new one with the double-text. This option does not delete the first run, but rather keeps it in the database but sets its status to `interrupted`. Below is a quick example of using the `interrupt` option.

## Setup[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#setup "Permanent link")

First, we will define a quick helper function for printing out JS and CURL model outputs (you can skip this if using Python):

[Javascript](#__tabbed_1_1)[CURL](#__tabbed_1_2)

```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-0-1)functionprettyPrint(m){
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-0-2)constpadded=" "+m['type']+" ";
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-0-3)constsepLen=Math.floor((80-padded.length)/2);
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-0-4)constsep="=".repeat(sepLen);
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-0-5)constsecondSep=sep+(padded.length%2?"=":"");
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-0-6)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-0-7)console.log(`${sep}${padded}${secondSep}`);
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-0-8)console.log("\n\n");
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-0-9)console.log(m.content);
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-0-10)}

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-1-1)# PLACE THIS IN A FILE CALLED pretty_print.sh
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-1-2)pretty_print(){
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-1-3)localtype="$1"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-1-4)localcontent="$2"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-1-5)localpadded=" $type "
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-1-6)localtotal_width=80
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-1-7)localsep_len=$(((total_width-${#padded})/2))
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-1-8)localsep=$(printf'=%.0s'$(eval"echo {1.."${sep_len}"}"))
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-1-9)localsecond_sep=$sep
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-1-10)if(((total_width-${#padded})%2));then
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-1-11)second_sep="${second_sep}="
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-1-12)fi
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-1-13)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-1-14)echo"${sep}${padded}${second_sep}"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-1-15)echo
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-1-16)echo"$content"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-1-17)}

```


Now, let's import our required packages and instantiate our client, assistant, and thread.

[Python](#__tabbed_2_1)[Javascript](#__tabbed_2_2)[CURL](#__tabbed_2_3)

```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-2-1)importasyncio
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-2-2)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-2-3)fromlangchain_core.messagesimport convert_to_messages
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-2-4)fromlanggraph_sdkimport get_client
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-2-5)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-2-6)client = get_client(url=<DEPLOYMENT_URL>)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-2-7)# Using the graph deployed with the name "agent"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-2-8)assistant_id = "agent"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-2-9)thread = await client.threads.create()

```


API Reference: [convert_to_messages](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.utils.convert_to_messages.html)

```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-3-1)import{Client}from"@langchain/langgraph-sdk";
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-3-2)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-3-3)constclient=newClient({apiUrl:<DEPLOYMENT_URL>});
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-3-4)// Using the graph deployed with the name "agent"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-3-5)constassistantId="agent";
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-3-6)constthread=awaitclient.threads.create();

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-4-1)curl--requestPOST\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-4-2)--url<DEPLOYMENT_URL>/threads\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-4-3)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-4-4)--data'{}'

```


## Create runs[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#create-runs "Permanent link")

Now we can start our two runs and join the second one until it has completed:

[Python](#__tabbed_3_1)[Javascript](#__tabbed_3_2)[CURL](#__tabbed_3_3)

```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-5-1)# the first run will be interrupted
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-5-2)interrupted_run = await client.runs.create(
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-5-3)  thread["thread_id"],
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-5-4)  assistant_id,
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-5-5)  input={"messages": [{"role": "user", "content": "what's the weather in sf?"}]},
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-5-6))
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-5-7)# sleep a bit to get partial outputs from the first run
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-5-8)await asyncio.sleep(2)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-5-9)run = await client.runs.create(
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-5-10)  thread["thread_id"],
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-5-11)  assistant_id,
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-5-12)  input={"messages": [{"role": "user", "content": "what's the weather in nyc?"}]},
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-5-13)  multitask_strategy="interrupt",
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-5-14))
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-5-15)# wait until the second run completes
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-5-16)await client.runs.join(thread["thread_id"], run["run_id"])

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-6-1)// the first run will be interrupted
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-6-2)letinterruptedRun=awaitclient.runs.create(
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-6-3)thread["thread_id"],
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-6-4)assistantId,
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-6-5){input:{messages:[{role:"human",content:"what's the weather in sf?"}]}}
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-6-6));
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-6-7)// sleep a bit to get partial outputs from the first run
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-6-8)awaitnewPromise(resolve=>setTimeout(resolve,2000));
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-6-9)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-6-10)letrun=awaitclient.runs.create(
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-6-11)thread["thread_id"],
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-6-12)assistantId,
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-6-13){
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-6-14)input:{messages:[{role:"human",content:"what's the weather in nyc?"}]},
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-6-15)multitaskStrategy:"interrupt"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-6-16)}
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-6-17));
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-6-18)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-6-19)// wait until the second run completes
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-6-20)awaitclient.runs.join(thread["thread_id"],run["run_id"]);

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-7-1)curl--requestPOST\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-7-2)--url<DEPLOY<ENT_URL>>/threads/<THREAD_ID>/runs\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-7-3)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-7-4)--data"{
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-7-5) \"assistant_id\": \"agent\",
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-7-6) \"input\": {\"messages\": [{\"role\": \"human\", \"content\": \"what\'s the weather in sf?\"}]},
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-7-7)}"&&sleep2&&curl--requestPOST\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-7-8)--url<DEPLOY<ENT_URL>>/threads/<THREAD_ID>/runs\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-7-9)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-7-10)--data"{
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-7-11) \"assistant_id\": \"agent\",
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-7-12) \"input\": {\"messages\": [{\"role\": \"human\", \"content\": \"what\'s the weather in nyc?\"}]},
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-7-13) \"multitask_strategy\": \"interrupt\"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-7-14)}"&&curl--requestGET\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-7-15)--url<DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/<RUN_ID>/join

```


## View run results[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#view-run-results "Permanent link")

We can see that the thread has partial data from the first run + data from the second run

[Python](#__tabbed_4_1)[Javascript](#__tabbed_4_2)[CURL](#__tabbed_4_3)

```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-8-1)state = await client.threads.get_state(thread["thread_id"])
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-8-2)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-8-3)for m in convert_to_messages(state["values"]["messages"]):
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-8-4)  m.pretty_print()

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-9-1)conststate=awaitclient.threads.getState(thread["thread_id"]);
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-9-2)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-9-3)for(constmofstate['values']['messages']){
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-9-4)prettyPrint(m);
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-9-5)}

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-10-1)sourcepretty_print.sh&&curl--requestGET\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-10-2)--url<DEPLOYMENT_URL>/threads/<THREAD_ID>/state|\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-10-3)jq-c'.values.messages[]'|whileread-relement;do
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-10-4)type=$(echo"$element"|jq-r'.type')
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-10-5)content=$(echo"$element"|jq-r'.content | if type == "array" then tostring else . end')
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-10-6)pretty_print"$type""$content"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-10-7)done

```


Output:

```
================================ Human Message =================================
what's the weather in sf?
================================== Ai Message ==================================
[{'id': 'toolu_01MjNtVJwEcpujRGrf3x6Pih', 'input': {'query': 'weather in san francisco'}, 'name': 'tavily_search_results_json', 'type': 'tool_use'}]
Tool Calls:
 tavily_search_results_json (toolu_01MjNtVJwEcpujRGrf3x6Pih)
 Call ID: toolu_01MjNtVJwEcpujRGrf3x6Pih
 Args:
  query: weather in san francisco
================================= Tool Message =================================
Name: tavily_search_results_json
[{"url": "https://www.wunderground.com/hourly/us/ca/san-francisco/KCASANFR2002/date/2024-6-18", "content": "High 64F. Winds W at 10 to 20 mph. A few clouds from time to time. Low 49F. Winds W at 10 to 20 mph. Temp. San Francisco Weather Forecasts. Weather Underground provides local & long-range weather ..."}]
================================ Human Message =================================
what's the weather in nyc?
================================== Ai Message ==================================
[{'id': 'toolu_01KtE1m1ifPLQAx4fQLyZL9Q', 'input': {'query': 'weather in new york city'}, 'name': 'tavily_search_results_json', 'type': 'tool_use'}]
Tool Calls:
 tavily_search_results_json (toolu_01KtE1m1ifPLQAx4fQLyZL9Q)
 Call ID: toolu_01KtE1m1ifPLQAx4fQLyZL9Q
 Args:
  query: weather in new york city
================================= Tool Message =================================
Name: tavily_search_results_json
[{"url": "https://www.accuweather.com/en/us/new-york/10021/june-weather/349727", "content": "Get the monthly weather forecast for New York, NY, including daily high/low, historical averages, to help you plan ahead."}]
================================== Ai Message ==================================
The search results provide weather forecasts and information for New York City. Based on the top result from AccuWeather, here are some key details about the weather in NYC:
- This is a monthly weather forecast for New York City for the month of June.
- It includes daily high and low temperatures to help plan ahead.
- Historical averages for June in NYC are also provided as a reference point.
- More detailed daily or hourly forecasts with precipitation chances, humidity, wind, etc. can be found by visiting the AccuWeather page.
So in summary, the search provides a convenient overview of the expected weather conditions in New York City over the next month to give you an idea of what to prepare for if traveling or making plans there. Let me know if you need any other details!

```


Verify that the original, interrupted run was interrupted

[Python](#__tabbed_5_1)[Javascript](#__tabbed_5_2)

```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-11-1)print((await client.runs.get(thread["thread_id"], interrupted_run["run_id"]))["status"])

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__codelineno-12-1)console.log((awaitclient.runs.get(thread['thread_id'],interruptedRun["run_id"]))["status"])

```


Output:

```
'interrupted'

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Review Tool Calls  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_review_tool_calls/) [ Next  Rollback  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
