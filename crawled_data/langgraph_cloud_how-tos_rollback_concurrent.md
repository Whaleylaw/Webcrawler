---
url: https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#rollback)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Rollback 

[ ](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/?q= "Share")

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
            * [ Interrupt  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/)
            * Rollback  [ Rollback  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#setup)
              * [ Create runs  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#create-runs)
              * [ View run results  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#view-run-results)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#setup)
  * [ Create runs  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#create-runs)
  * [ View run results  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#view-run-results)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph-platform)
  5. [ Double-texting  ](https://langchain-ai.github.io/langgraph/how-tos#double-texting)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/cloud/how-tos/rollback_concurrent.md "Edit this page")

# Rollback[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#rollback "Permanent link")

This guide assumes knowledge of what double-texting is, which you can learn about in the [double-texting conceptual guide](https://langchain-ai.github.io/langgraph/concepts/double_texting/).

The guide covers the `rollback` option for double texting, which interrupts the prior run of the graph and starts a new one with the double-text. This option is very similar to the `interrupt` option, but in this case the first run is completely deleted from the database and cannot be restarted. Below is a quick example of using the `rollback` option.

## Setup[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#setup "Permanent link")

First, we will define a quick helper function for printing out JS and CURL model outputs (you can skip this if using Python):

[Javascript](#__tabbed_1_1)[CURL](#__tabbed_1_2)

```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-0-1)functionprettyPrint(m){
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-0-2)constpadded=" "+m['type']+" ";
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-0-3)constsepLen=Math.floor((80-padded.length)/2);
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-0-4)constsep="=".repeat(sepLen);
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-0-5)constsecondSep=sep+(padded.length%2?"=":"");
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-0-6)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-0-7)console.log(`${sep}${padded}${secondSep}`);
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-0-8)console.log("\n\n");
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-0-9)console.log(m.content);
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-0-10)}

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-1-1)# PLACE THIS IN A FILE CALLED pretty_print.sh
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-1-2)pretty_print(){
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-1-3)localtype="$1"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-1-4)localcontent="$2"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-1-5)localpadded=" $type "
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-1-6)localtotal_width=80
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-1-7)localsep_len=$(((total_width-${#padded})/2))
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-1-8)localsep=$(printf'=%.0s'$(eval"echo {1.."${sep_len}"}"))
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-1-9)localsecond_sep=$sep
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-1-10)if(((total_width-${#padded})%2));then
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-1-11)second_sep="${second_sep}="
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-1-12)fi
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-1-13)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-1-14)echo"${sep}${padded}${second_sep}"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-1-15)echo
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-1-16)echo"$content"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-1-17)}

```


Now, let's import our required packages and instantiate our client, assistant, and thread.

[Python](#__tabbed_2_1)[Javascript](#__tabbed_2_2)[CURL](#__tabbed_2_3)

```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-2-1)importasyncio
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-2-2)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-2-3)importhttpx
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-2-4)fromlangchain_core.messagesimport convert_to_messages
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-2-5)fromlanggraph_sdkimport get_client
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-2-6)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-2-7)client = get_client(url=<DEPLOYMENT_URL>)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-2-8)# Using the graph deployed with the name "agent"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-2-9)assistant_id = "agent"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-2-10)thread = await client.threads.create()

```


API Reference: [convert_to_messages](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.utils.convert_to_messages.html)

```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-3-1)import{Client}from"@langchain/langgraph-sdk";
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-3-2)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-3-3)constclient=newClient({apiUrl:<DEPLOYMENT_URL>});
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-3-4)// Using the graph deployed with the name "agent"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-3-5)constassistantId="agent";
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-3-6)constthread=awaitclient.threads.create();

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-4-1)curl--requestPOST\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-4-2)--url<DEPLOYMENT_URL>/threads\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-4-3)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-4-4)--data'{}'

```


## Create runs[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#create-runs "Permanent link")

Now let's run a thread with the multitask parameter set to "rollback":

[Python](#__tabbed_3_1)[Javascript](#__tabbed_3_2)[CURL](#__tabbed_3_3)

```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-5-1)# the first run will be rolled back
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-5-2)rolled_back_run = await client.runs.create(
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-5-3)  thread["thread_id"],
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-5-4)  assistant_id,
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-5-5)  input={"messages": [{"role": "user", "content": "what's the weather in sf?"}]},
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-5-6))
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-5-7)run = await client.runs.create(
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-5-8)  thread["thread_id"],
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-5-9)  assistant_id,
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-5-10)  input={"messages": [{"role": "user", "content": "what's the weather in nyc?"}]},
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-5-11)  multitask_strategy="rollback",
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-5-12))
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-5-13)# wait until the second run completes
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-5-14)await client.runs.join(thread["thread_id"], run["run_id"])

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-6-1)// the first run will be interrupted
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-6-2)letrolledBackRun=awaitclient.runs.create(
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-6-3)thread["thread_id"],
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-6-4)assistantId,
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-6-5){input:{messages:[{role:"human",content:"what's the weather in sf?"}]}}
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-6-6));
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-6-7)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-6-8)letrun=awaitclient.runs.create(
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-6-9)thread["thread_id"],
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-6-10)assistant_id,
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-6-11){
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-6-12)input:{messages:[{role:"human",content:"what's the weather in nyc?"}]},
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-6-13)multitaskStrategy:"rollback"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-6-14)}
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-6-15));
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-6-16)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-6-17)// wait until the second run completes
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-6-18)awaitclient.runs.join(thread["thread_id"],run["run_id"]);

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-7-1)curl--requestPOST\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-7-2)--url<DEPLOY<ENT_URL>>/threads/<THREAD_ID>/runs\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-7-3)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-7-4)--data"{
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-7-5) \"assistant_id\": \"agent\",
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-7-6) \"input\": {\"messages\": [{\"role\": \"human\", \"content\": \"what\'s the weather in sf?\"}]},
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-7-7)}"&&curl--requestPOST\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-7-8)--url<DEPLOY<ENT_URL>>/threads/<THREAD_ID>/runs\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-7-9)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-7-10)--data"{
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-7-11) \"assistant_id\": \"agent\",
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-7-12) \"input\": {\"messages\": [{\"role\": \"human\", \"content\": \"what\'s the weather in nyc?\"}]},
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-7-13) \"multitask_strategy\": \"rollback\"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-7-14)}"&&curl--requestGET\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-7-15)--url<DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/<RUN_ID>/join

```


## View run results[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#view-run-results "Permanent link")

We can see that the thread has data only from the second run

[Python](#__tabbed_4_1)[Javascript](#__tabbed_4_2)[CURL](#__tabbed_4_3)

```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-8-1)state = await client.threads.get_state(thread["thread_id"])
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-8-2)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-8-3)for m in convert_to_messages(state["values"]["messages"]):
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-8-4)  m.pretty_print()

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-9-1)conststate=awaitclient.threads.getState(thread["thread_id"]);
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-9-2)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-9-3)for(constmofstate['values']['messages']){
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-9-4)prettyPrint(m);
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-9-5)}

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-10-1)sourcepretty_print.sh&&curl--requestGET\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-10-2)--url<DEPLOYMENT_URL>/threads/<THREAD_ID>/state|\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-10-3)jq-c'.values.messages[]'|whileread-relement;do
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-10-4)type=$(echo"$element"|jq-r'.type')
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-10-5)content=$(echo"$element"|jq-r'.content | if type == "array" then tostring else . end')
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-10-6)pretty_print"$type""$content"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-10-7)done

```


Output:

```
================================ Human Message =================================
what's the weather in nyc?
================================== Ai Message ==================================
[{'id': 'toolu_01JzPqefao1gxwajHQ3Yh3JD', 'input': {'query': 'weather in nyc'}, 'name': 'tavily_search_results_json', 'type': 'tool_use'}]
Tool Calls:
 tavily_search_results_json (toolu_01JzPqefao1gxwajHQ3Yh3JD)
 Call ID: toolu_01JzPqefao1gxwajHQ3Yh3JD
 Args:
  query: weather in nyc
================================= Tool Message =================================
Name: tavily_search_results_json
[{"url": "https://www.weatherapi.com/", "content": "{'location': {'name': 'New York', 'region': 'New York', 'country': 'United States of America', 'lat': 40.71, 'lon': -74.01, 'tz_id': 'America/New_York', 'localtime_epoch': 1718734479, 'localtime': '2024-06-18 14:14'}, 'current': {'last_updated_epoch': 1718733600, 'last_updated': '2024-06-18 14:00', 'temp_c': 29.4, 'temp_f': 84.9, 'is_day': 1, 'condition': {'text': 'Sunny', 'icon': '//cdn.weatherapi.com/weather/64x64/day/113.png', 'code': 1000}, 'wind_mph': 2.2, 'wind_kph': 3.6, 'wind_degree': 158, 'wind_dir': 'SSE', 'pressure_mb': 1025.0, 'pressure_in': 30.26, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 63, 'cloud': 0, 'feelslike_c': 31.3, 'feelslike_f': 88.3, 'windchill_c': 28.3, 'windchill_f': 82.9, 'heatindex_c': 29.6, 'heatindex_f': 85.3, 'dewpoint_c': 18.4, 'dewpoint_f': 65.2, 'vis_km': 16.0, 'vis_miles': 9.0, 'uv': 7.0, 'gust_mph': 16.5, 'gust_kph': 26.5}}"}]
================================== Ai Message ==================================
The weather API results show that the current weather in New York City is sunny with a temperature of around 85°F (29°C). The wind is light at around 2-3 mph from the south-southeast. Overall it looks like a nice sunny summer day in NYC.

```


Verify that the original, rolled back run was deleted

[Python](#__tabbed_5_1)[Javascript](#__tabbed_5_2)

```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-11-1)try:
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-11-2)  await client.runs.get(thread["thread_id"], rolled_back_run["run_id"])
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-11-3)except httpx.HTTPStatusError as _:
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-11-4)  print("Original run was correctly deleted")

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-12-1)try{
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-12-2)awaitclient.runs.get(thread["thread_id"],rolledBackRun["run_id"]);
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-12-3)}catch(e){
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-12-4)console.log("Original run was correctly deleted");
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__codelineno-12-5)}

```


Output:

```
Original run was correctly deleted

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Interrupt  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/interrupt_concurrent/) [ Next  Reject  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/reject_concurrent/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/cloud/how-tos/rollback_concurrent/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
