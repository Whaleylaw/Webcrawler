---
url: https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#how-to-add-breakpoints)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to Add Breakpoints 

[ ](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/?q= "Share")

Initializing search 

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
            * How to Add Breakpoints  [ How to Add Breakpoints  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#setup)
                * [ Code for your graph  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#code-for-your-graph)
                * [ SDK Initialization  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#sdk-initialization)
              * [ Adding a breakpoint  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#adding-a-breakpoint)
            * [ How to Wait for User Input  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_user_input/)
            * [ How to Edit State of a Deployed Graph  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_edit_state/)
            * [ How to Replay and Branch from Prior States  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_time_travel/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#setup)
    * [ Code for your graph  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#code-for-your-graph)
    * [ SDK Initialization  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#sdk-initialization)
  * [ Adding a breakpoint  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#adding-a-breakpoint)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph-platform)
  5. [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraph/how-tos#human-in-the-loop_1)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/cloud/how-tos/human_in_the_loop_breakpoint.md "Edit this page")

# How to Add Breakpoints[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#how-to-add-breakpoints "Permanent link")

When creating LangGraph agents, it is often nice to add a human-in-the-loop component. This can be helpful when giving them access to tools. Often in these situations you may want to manually approve an action before taking.

This can be in several ways, but the primary supported way is to add an "interrupt" before a node is executed. This interrupts execution at that node. You can then resume from that spot to continue. 

## Setup[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#setup "Permanent link")

### Code for your graph[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#code-for-your-graph "Permanent link")

In this how-to we use a simple ReAct style hosted graph (you can see the full code for defining it [here](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/)). The important thing is that there are two nodes (one named `agent` that calls the LLM, and one named `action` that calls the tool), and a routing function from `agent` that determines whether to call `action` next or just end the graph run (the `action` node always calls the `agent` node after execution).

### SDK Initialization[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#sdk-initialization "Permanent link")

[Python](#__tabbed_1_1)[Javascript](#__tabbed_1_2)[CURL](#__tabbed_1_3)

```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-0-1)fromlanggraph_sdkimport get_client
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-0-2)client = get_client(url=<DEPLOYMENT_URL>)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-0-3)# Using the graph deployed with the name "agent"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-0-4)assistant_id = "agent"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-0-5)thread = await client.threads.create()

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-1-1)import{Client}from"@langchain/langgraph-sdk";
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-1-2)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-1-3)constclient=newClient({apiUrl:<DEPLOYMENT_URL>});
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-1-4)// Using the graph deployed with the name "agent"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-1-5)constassistantId="agent";
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-1-6)constthread=awaitclient.threads.create();

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-2-1)curl--requestPOST\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-2-2)--url<DEPLOYMENT_URL>/threads\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-2-3)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-2-4)--data'{}'

```


## Adding a breakpoint[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#adding-a-breakpoint "Permanent link")

We now want to add a breakpoint in our graph run, which we will do before a tool is called. We can do this by adding `interrupt_before=["action"]`, which tells us to interrupt before calling the action node. We can do this either when compiling the graph or when kicking off a run. Here we will do it when kicking of a run, if you would like to to do it at compile time you need to edit the python file where your graph is defined and add the `interrupt_before` parameter when you call `.compile`.

First let's access our hosted LangGraph instance through the SDK:

And, now let's compile it with a breakpoint before the tool node:

[Python](#__tabbed_2_1)[Javascript](#__tabbed_2_2)[CURL](#__tabbed_2_3)

```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-3-1)input = {"messages": [{"role": "user", "content": "what's the weather in sf"}]}
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-3-2)async for chunk in client.runs.stream(
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-3-3)  thread["thread_id"],
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-3-4)  assistant_id,
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-3-5)  input=input,
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-3-6)  stream_mode="updates",
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-3-7)  interrupt_before=["action"],
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-3-8)):
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-3-9)  print(f"Receiving new event of type: {chunk.event}...")
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-3-10)  print(chunk.data)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-3-11)  print("\n\n")

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-4-1)constinput={messages:[{role:"human",content:"what's the weather in sf"}]};
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-4-2)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-4-3)conststreamResponse=client.runs.stream(
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-4-4)thread["thread_id"],
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-4-5)assistantId,
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-4-6){
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-4-7)input:input,
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-4-8)streamMode:"updates",
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-4-9)interruptBefore:["action"]
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-4-10)}
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-4-11));
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-4-12)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-4-13)forawait(constchunkofstreamResponse){
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-4-14)console.log(`Receiving new event of type: ${chunk.event}...`);
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-4-15)console.log(chunk.data);
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-4-16)console.log("\n\n");
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-4-17)}

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-5-1)curl--requestPOST\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-5-2)--url<DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/stream\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-5-3)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-5-4)--data"{
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-5-5)  \"assistant_id\": \"agent\",
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-5-6)  \"input\": {\"messages\": [{\"role\": \"human\", \"content\": \"what's the weather in sf\"}]},
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-5-7)  \"interrupt_before\": [\"action\"],
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-5-8)  \"stream_mode\": [
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-5-9)   \"messages\"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-5-10)  ]
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-5-11) }"|\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-5-12)sed's/\r$//'|\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-5-13)awk'
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-5-14) /^event:/ {
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-5-15)   if (data_content != "") {
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-5-16)     print data_content "\n"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-5-17)   }
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-5-18)   sub(/^event: /, "Receiving event of type: ", $0)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-5-19)   printf "%s...\n", $0
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-5-20)   data_content = ""
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-5-21) }
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-5-22) /^data:/ {
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-5-23)   sub(/^data: /, "", $0)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-5-24)   data_content = $0
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-5-25) }
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-5-26) END {
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-5-27)   if (data_content != "") {
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-5-28)     print data_content "\n"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-5-29)   }
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-5-30) }
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__codelineno-5-31) '

```


Output:

```
Receiving new event of type: metadata...
{'run_id': '3b77ef83-687a-4840-8858-0371f91a92c3'}

Receiving new event of type: data...
{'agent': {'messages': [{'content': [{'id': 'toolu_01HwZqM1ptX6E15A5LAmyZTB', 'input': {'query': 'weather in san francisco'}, 'name': 'tavily_search_results_json', 'type': 'tool_use'}], 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-e5d17791-4d37-4ad2-815f-a0c4cba62585', 'example': False, 'tool_calls': [{'name': 'tavily_search_results_json', 'args': {'query': 'weather in san francisco'}, 'id': 'toolu_01HwZqM1ptX6E15A5LAmyZTB'}], 'invalid_tool_calls': []}]}}

Receiving new event of type: end...
None

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to integrate LangGraph into your React application  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/) [ Next  How to Wait for User Input  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_user_input/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
