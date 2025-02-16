---
url: https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#review-tool-calls)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

Review Tool Calls 

[ ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/?q= "Share")

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
            * [ How to Edit State of a Deployed Graph  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_edit_state/)
            * [ How to Replay and Branch from Prior States  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_time_travel/)
            * Review Tool Calls  [ Review Tool Calls  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#setup)
                * [ SDK initialization  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#sdk-initialization)
              * [ Example with no review  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#example-with-no-review)
              * [ Example of approving tool  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#example-of-approving-tool)
              * [ Edit Tool Call  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#edit-tool-call)
              * [ Give feedback to a tool call  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#give-feedback-to-a-tool-call)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#setup)
    * [ SDK initialization  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#sdk-initialization)
  * [ Example with no review  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#example-with-no-review)
  * [ Example of approving tool  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#example-of-approving-tool)
  * [ Edit Tool Call  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#edit-tool-call)
  * [ Give feedback to a tool call  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#give-feedback-to-a-tool-call)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph Platform  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph-platform)
  5. [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraphjs/how-tos#human-in-the-loop_1)



# Review Tool Calls[¶](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#review-tool-calls "Permanent link")

Human-in-the-loop (HIL) interactions are crucial for [agentic systems](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#human-in-the-loop). A common pattern is to add some human in the loop step after certain tool calls. These tool calls often lead to either a function call or saving of some information. Examples include:

  * A tool call to execute SQL, which will then be run by the tool
  * A tool call to generate a summary, which will then be saved to the State of the graph



Note that using tool calls is common **whether actually calling tools or not**.

There are typically a few different interactions you may want to do here:

  1. Approve the tool call and continue
  2. Modify the tool call manually and then continue
  3. Give natural language feedback, and then pass that back to the agent instead of continuing



We can implement this in LangGraph using a [breakpoint](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/): breakpoints allow us to interrupt graph execution before a specific step. At this breakpoint, we can manually update the graph state taking one of the three options above

## Setup[¶](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#setup "Permanent link")

We are not going to show the full code for the graph we are hosting, but you can see it [here](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop/review-tool-calls.ipynb#simple-usage) if you want to. Once this graph is hosted, we are ready to invoke it and wait for user input. 

### SDK initialization[¶](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#sdk-initialization "Permanent link")

First, we need to setup our client so that we can communicate with our hosted graph:

[Python](#__tabbed_1_1)[Javascript](#__tabbed_1_2)[CURL](#__tabbed_1_3)

```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-0-1)fromlanggraph_sdkimport get_client
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-0-2)client = get_client(url=<DEPLOYMENT_URL>)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-0-3)# Using the graph deployed with the name "agent"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-0-4)assistant_id = "agent"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-0-5)thread = await client.threads.create()

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-1-1)import{Client}from"@langchain/langgraph-sdk";
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-1-2)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-1-3)constclient=newClient({apiUrl:<DEPLOYMENT_URL>});
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-1-4)// Using the graph deployed with the name "agent"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-1-5)constassistantId="agent";
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-1-6)constthread=awaitclient.threads.create();

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-2-1)curl--requestPOST\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-2-2)--url<DEPLOYMENT_URL>/threads\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-2-3)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-2-4)--data'{}'

```


## Example with no review[¶](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#example-with-no-review "Permanent link")

Let's look at an example when no review is required (because no tools are called)

[Python](#__tabbed_2_1)[Javascript](#__tabbed_2_2)[CURL](#__tabbed_2_3)

```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-3-1)input = { 'messages':[{ "role":"user", "content":"hi!" }] }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-3-2)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-3-3)async for chunk in client.runs.stream(
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-3-4)  thread["thread_id"],
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-3-5)  assistant_id,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-3-6)  input=input,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-3-7)  stream_mode="updates",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-3-8)  interrupt_before=["action"],
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-3-9)):
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-3-10)  if chunk.data and chunk.event != "metadata": 
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-3-11)    print(chunk.data)

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-4-1)constinput={"messages":[{"role":"user","content":"hi!"}]};
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-4-2)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-4-3)conststreamResponse=client.runs.stream(
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-4-4)thread["thread_id"],
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-4-5)assistantId,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-4-6){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-4-7)input:input,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-4-8)streamMode:"updates",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-4-9)interruptBefore:["action"],
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-4-10)}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-4-11));
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-4-12)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-4-13)forawait(constchunkofstreamResponse){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-4-14)if(chunk.data&&chunk.event!=="metadata"){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-4-15)console.log(chunk.data);
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-4-16)}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-4-17)}

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-5-1)curl--requestPOST\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-5-2)--url<DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/stream\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-5-3)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-5-4)--data"{
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-5-5)  \"assistant_id\": \"agent\",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-5-6)  \"input\": {\"messages\": [{\"role\": \"human\", \"content\": \"hi!\"}]},
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-5-7)  \"stream_mode\": [
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-5-8)   \"updates\"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-5-9)  ],
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-5-10)  \"interrupt_before\": [\"action\"]
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-5-11) }"|\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-5-12)sed's/\r$//'|\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-5-13)awk'
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-5-14) /^event:/ {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-5-15)   if (data_content != "" && event_type != "metadata") {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-5-16)     print data_content "\n"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-5-17)   }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-5-18)   sub(/^event: /, "", $0)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-5-19)   event_type = $0
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-5-20)   data_content = ""
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-5-21) }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-5-22) /^data:/ {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-5-23)   sub(/^data: /, "", $0)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-5-24)   data_content = $0
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-5-25) }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-5-26) END {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-5-27)   if (data_content != "" && event_type != "metadata") {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-5-28)     print data_content "\n"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-5-29)   }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-5-30) }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-5-31) '

```


Output:

```
{'messages': [{'content': 'hi!', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': '39c51f14-2d5c-4690-883a-d940854b1845', 'example': False}]}
{'messages': [{'content': 'hi!', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': '39c51f14-2d5c-4690-883a-d940854b1845', 'example': False}, {'content': [{'text': "Hello! Welcome. How can I assist you today? Is there anything specific you'd like to know or any information you're looking for?", 'type': 'text', 'index': 0}], 'additional_kwargs': {}, 'response_metadata': {'stop_reason': 'end_turn', 'stop_sequence': None}, 'type': 'ai', 'name': None, 'id': 'run-d65e07fb-43ff-4d98-ab6b-6316191b9c8b', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': {'input_tokens': 355, 'output_tokens': 31, 'total_tokens': 386}}]}

```


If we check the state, we can see that it is finished

[Python](#__tabbed_3_1)[Javascript](#__tabbed_3_2)[CURL](#__tabbed_3_3)

```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-6-1)state = await client.threads.get_state(thread["thread_id"])
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-6-2)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-6-3)print(state['next'])

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-7-1)conststate=awaitclient.threads.getState(thread["thread_id"]);
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-7-2)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-7-3)console.log(state.next);

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-8-1)curl--requestGET\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-8-2)--url<DEPLOYMENT_URL>/threads/<THREAD_ID>/state|jq-c'.next'

```


Output:

```
[]

```


## Example of approving tool[¶](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#example-of-approving-tool "Permanent link")

Let's now look at what it looks like to approve a tool call. Note that we don't need to pass an interrupt to our streaming calls because the graph (defined [here](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop/review-tool-calls.ipynb#simple-usage)) was already compiled with an interrupt before the `human_review_node`.

[Python](#__tabbed_4_1)[Javascript](#__tabbed_4_2)[CURL](#__tabbed_4_3)

```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-9-1)input = {"messages": [{"role": "user", "content": "what's the weather in sf?"}]}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-9-2)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-9-3)async for chunk in client.runs.stream(
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-9-4)  thread["thread_id"],
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-9-5)  assistant_id,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-9-6)  input=input,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-9-7)):
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-9-8)  if chunk.data and chunk.event != "metadata": 
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-9-9)    print(chunk.data)

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-10-1)constinput={"messages":[{"role":"user","content":"what's the weather in sf?"}]};
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-10-2)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-10-3)conststreamResponse=client.runs.stream(
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-10-4)thread["thread_id"],
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-10-5)assistantId,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-10-6){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-10-7)input:input,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-10-8)}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-10-9));
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-10-10)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-10-11)forawait(constchunkofstreamResponse){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-10-12)if(chunk.data&&chunk.event!=="metadata"){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-10-13)console.log(chunk.data);
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-10-14)}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-10-15)}

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-11-1)curl--requestPOST\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-11-2)--url<DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/stream\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-11-3)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-11-4)--data"{
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-11-5)  \"assistant_id\": \"agent\",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-11-6)  \"input\": {\"messages\": [{\"role\": \"human\", \"content\": \"what's the weather in sf?\"}]}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-11-7) }"|\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-11-8)sed's/\r$//'|\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-11-9)awk'
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-11-10) /^event:/ {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-11-11)   if (data_content != "" && event_type != "metadata") {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-11-12)     print data_content "\n"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-11-13)   }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-11-14)   sub(/^event: /, "", $0)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-11-15)   event_type = $0
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-11-16)   data_content = ""
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-11-17) }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-11-18) /^data:/ {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-11-19)   sub(/^data: /, "", $0)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-11-20)   data_content = $0
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-11-21) }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-11-22) END {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-11-23)   if (data_content != "" && event_type != "metadata") {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-11-24)     print data_content "\n"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-11-25)   }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-11-26) }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-11-27) '

```


Output:

```
{'messages': [{'content': "what's the weather in sf?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': '54e19d6e-89fa-44fb-b92c-12e7dd4ddf08', 'example': False}]}
{'messages': [{'content': "what's the weather in sf?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': '54e19d6e-89fa-44fb-b92c-12e7dd4ddf08', 'example': False}, {'content': [{'text': "Certainly! I can help you check the weather in San Francisco. To get this information, I'll use the weather search function. Let me do that for you right away.", 'type': 'text', 'index': 0}, {'id': 'toolu_015yrR3GMDXe6X8m2p9CsEDN', 'input': {}, 'name': 'weather_search', 'type': 'tool_use', 'index': 1, 'partial_json': '{"city": "San Francisco"}'}], 'additional_kwargs': {}, 'response_metadata': {'stop_reason': 'tool_use', 'stop_sequence': None}, 'type': 'ai', 'name': None, 'id': 'run-45a6b6c3-ac69-42a4-8957-d982203d6392', 'example': False, 'tool_calls': [{'name': 'weather_search', 'args': {'city': 'San Francisco'}, 'id': 'toolu_015yrR3GMDXe6X8m2p9CsEDN', 'type': 'tool_call'}], 'invalid_tool_calls': [], 'usage_metadata': {'input_tokens': 360, 'output_tokens': 90, 'total_tokens': 450}}]}

```


If we now check, we can see that it is waiting on human review:

[Python](#__tabbed_5_1)[Javascript](#__tabbed_5_2)[CURL](#__tabbed_5_3)

```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-12-1)state = await client.threads.get_state(thread["thread_id"])
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-12-2)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-12-3)print(state['next'])

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-13-1)conststate=awaitclient.threads.getState(thread["thread_id"]);
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-13-2)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-13-3)console.log(state.next);

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-14-1)curl--requestGET\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-14-2)--url<DELPOYMENT_URL>/threads/<THREAD_ID>/state|jq-c'.next'

```


Output:

```
['human_review_node']

```


To approve the tool call, we can just continue the thread with no edits. To do this, we just create a new run with no inputs.

[Python](#__tabbed_6_1)[Javascript](#__tabbed_6_2)[CURL](#__tabbed_6_3)

```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-15-1)async for chunk in client.runs.stream(
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-15-2)  thread["thread_id"],
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-15-3)  assistant_id,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-15-4)  input=None,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-15-5)  stream_mode="values",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-15-6)):
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-15-7)  if chunk.data and chunk.event != "metadata": 
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-15-8)    print(chunk.data)

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-16-1)conststreamResponse=client.runs.stream(
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-16-2)thread["thread_id"],
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-16-3)assistantId,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-16-4){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-16-5)input:null,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-16-6)streamMode:"values",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-16-7)}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-16-8));
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-16-9)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-16-10)forawait(constchunkofstreamResponse){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-16-11)if(chunk.data&&chunk.event!=="metadata"){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-16-12)console.log(chunk.data);
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-16-13)}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-16-14)}

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-17-1)curl--requestPOST\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-17-2)--url<DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/stream\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-17-3)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-17-4)--data"{
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-17-5)  \"assistant_id\": \"agent\"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-17-6) }"|\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-17-7)sed's/\r$//'|\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-17-8)awk'
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-17-9) /^event:/ {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-17-10)   if (data_content != "" && event_type != "metadata") {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-17-11)     print data_content "\n"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-17-12)   }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-17-13)   sub(/^event: /, "", $0)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-17-14)   event_type = $0
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-17-15)   data_content = ""
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-17-16) }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-17-17) /^data:/ {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-17-18)   sub(/^data: /, "", $0)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-17-19)   data_content = $0
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-17-20) }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-17-21) END {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-17-22)   if (data_content != "" && event_type != "metadata") {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-17-23)     print data_content "\n"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-17-24)   }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-17-25) }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-17-26) '

```


Output:

```
{'messages': [{'content': "what's the weather in sf?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': '54e19d6e-89fa-44fb-b92c-12e7dd4ddf08', 'example': False}, {'content': [{'text': "Certainly! I can help you check the weather in San Francisco. To get this information, I'll use the weather search function. Let me do that for you right away.", 'type': 'text', 'index': 0}, {'id': 'toolu_015yrR3GMDXe6X8m2p9CsEDN', 'input': {}, 'name': 'weather_search', 'type': 'tool_use', 'index': 1, 'partial_json': '{"city": "San Francisco"}'}], 'additional_kwargs': {}, 'response_metadata': {'stop_reason': 'tool_use', 'stop_sequence': None}, 'type': 'ai', 'name': None, 'id': 'run-45a6b6c3-ac69-42a4-8957-d982203d6392', 'example': False, 'tool_calls': [{'name': 'weather_search', 'args': {'city': 'San Francisco'}, 'id': 'toolu_015yrR3GMDXe6X8m2p9CsEDN', 'type': 'tool_call'}], 'invalid_tool_calls': [], 'usage_metadata': {'input_tokens': 360, 'output_tokens': 90, 'total_tokens': 450}}, {'content': 'Sunny!', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'tool', 'name': 'weather_search', 'id': '826cd0f2-9cc6-46f0-b7df-daa6a05d13d2', 'tool_call_id': 'toolu_015yrR3GMDXe6X8m2p9CsEDN', 'artifact': None, 'status': 'success'}]}
{'messages': [{'content': "what's the weather in sf?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': '54e19d6e-89fa-44fb-b92c-12e7dd4ddf08', 'example': False}, {'content': [{'text': "Certainly! I can help you check the weather in San Francisco. To get this information, I'll use the weather search function. Let me do that for you right away.", 'type': 'text', 'index': 0}, {'id': 'toolu_015yrR3GMDXe6X8m2p9CsEDN', 'input': {}, 'name': 'weather_search', 'type': 'tool_use', 'index': 1, 'partial_json': '{"city": "San Francisco"}'}], 'additional_kwargs': {}, 'response_metadata': {'stop_reason': 'tool_use', 'stop_sequence': None}, 'type': 'ai', 'name': None, 'id': 'run-45a6b6c3-ac69-42a4-8957-d982203d6392', 'example': False, 'tool_calls': [{'name': 'weather_search', 'args': {'city': 'San Francisco'}, 'id': 'toolu_015yrR3GMDXe6X8m2p9CsEDN', 'type': 'tool_call'}], 'invalid_tool_calls': [], 'usage_metadata': {'input_tokens': 360, 'output_tokens': 90, 'total_tokens': 450}}, {'content': 'Sunny!', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'tool', 'name': 'weather_search', 'id': '826cd0f2-9cc6-46f0-b7df-daa6a05d13d2', 'tool_call_id': 'toolu_015yrR3GMDXe6X8m2p9CsEDN', 'artifact': None, 'status': 'success'}, {'content': [{'text': "\n\nGreat news! The weather in San Francisco is sunny today. It's a beautiful day in the city by the bay. Is there anything else you'd like to know about the weather or any other information I can help you with?", 'type': 'text', 'index': 0}], 'additional_kwargs': {}, 'response_metadata': {'stop_reason': 'end_turn', 'stop_sequence': None}, 'type': 'ai', 'name': None, 'id': 'run-5d5fd0f1-a939-447e-801a-9aaa812322d3', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': {'input_tokens': 464, 'output_tokens': 50, 'total_tokens': 514}}]}

```


## Edit Tool Call[¶](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#edit-tool-call "Permanent link")

Let's now say we want to edit the tool call. E.g. change some of the parameters (or even the tool called!) but then execute that tool.

[Python](#__tabbed_7_1)[Javascript](#__tabbed_7_2)[CURL](#__tabbed_7_3)

```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-18-1)input = {"messages": [{"role": "user", "content": "what's the weather in sf?"}]}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-18-2)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-18-3)async for chunk in client.runs.stream(
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-18-4)  thread["thread_id"],
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-18-5)  assistant_id,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-18-6)  input=input,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-18-7)  stream_mode="values",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-18-8)):
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-18-9)  if chunk.data and chunk.event != "metadata": 
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-18-10)    print(chunk.data)

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-19-1)constinput={"messages":[{"role":"user","content":"what's the weather in sf?"}]};
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-19-2)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-19-3)conststreamResponse=client.runs.stream(
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-19-4)thread["thread_id"],
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-19-5)assistantId,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-19-6){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-19-7)input:input,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-19-8)streamMode:"values",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-19-9)}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-19-10));
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-19-11)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-19-12)forawait(constchunkofstreamResponse){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-19-13)if(chunk.data&&chunk.event!=="metadata"){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-19-14)console.log(chunk.data);
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-19-15)}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-19-16)}

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-20-1)curl--requestPOST\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-20-2)--url<DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/stream\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-20-3)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-20-4)--data"{
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-20-5)  \"assistant_id\": \"agent\",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-20-6)  \"input\": {\"messages\": [{\"role\": \"human\", \"content\": \"what's the weather in sf?\"}]}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-20-7) }"|\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-20-8)sed's/\r$//'|\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-20-9)awk'
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-20-10) /^event:/ {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-20-11)   if (data_content != "" && event_type != "metadata") {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-20-12)     print data_content "\n"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-20-13)   }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-20-14)   sub(/^event: /, "", $0)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-20-15)   event_type = $0
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-20-16)   data_content = ""
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-20-17) }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-20-18) /^data:/ {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-20-19)   sub(/^data: /, "", $0)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-20-20)   data_content = $0
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-20-21) }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-20-22) END {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-20-23)   if (data_content != "" && event_type != "metadata") {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-20-24)     print data_content "\n"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-20-25)   }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-20-26) }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-20-27) '

```


Output:

```
{'messages': [{'content': "what's the weather in sf?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': 'cec11391-84da-464b-bd2a-bd4f0d93b9ee', 'example': False}]}
{'messages': [{'content': "what's the weather in sf?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': 'cec11391-84da-464b-bd2a-bd4f0d93b9ee', 'example': False}, {'content': [{'text': 'To get the weather information for San Francisco, I can use the weather_search function. Let me do that for you.', 'type': 'text', 'index': 0}, {'id': 'toolu_01SunSpDurNfcnXppWLPrtjC', 'input': {}, 'name': 'weather_search', 'type': 'tool_use', 'index': 1, 'partial_json': '{"city": "San Francisco"}'}], 'additional_kwargs': {}, 'response_metadata': {'stop_reason': 'tool_use', 'stop_sequence': None}, 'type': 'ai', 'name': None, 'id': 'run-6326da9f-6061-4e12-8586-482e32ab4cab', 'example': False, 'tool_calls': [{'name': 'weather_search', 'args': {'city': 'San Francisco'}, 'id': 'toolu_01SunSpDurNfcnXppWLPrtjC', 'type': 'tool_call'}], 'invalid_tool_calls': [], 'usage_metadata': {'input_tokens': 360, 'output_tokens': 80, 'total_tokens': 440}}]}

```


To do this, we first need to update the state. We can do this by passing a message in with the **same** id of the message we want to overwrite. This will have the effect of **replacing** that old message. Note that this is only possible because of the **reducer** we are using that replaces messages with the same ID - read more about that [here](https://langchain-ai.github.io/langgraph/concepts/low_level/#working-with-messages-in-graph-state).

[Python](#__tabbed_8_1)[Javascript](#__tabbed_8_2)[CURL](#__tabbed_8_3)

```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-21-1)# To get the ID of the message we want to replace, we need to fetch the current state and find it there.
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-21-2)state = await client.threads.get_state(thread['thread_id'])
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-21-3)print("Current State:")
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-21-4)print(state['values'])
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-21-5)print("\nCurrent Tool Call ID:")
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-21-6)current_content = state
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-21-7)current_id = state
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-21-8)tool_call_id = state
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-21-9)print(tool_call_id)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-21-10)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-21-11)# We now need to construct a replacement tool call.
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-21-12)# We will change the argument to be `San Francisco, USA`
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-21-13)# Note that we could change any number of arguments or tool names - it just has to be a valid one
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-21-14)new_message = {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-21-15)  "role": "assistant", 
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-21-16)  "content": current_content,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-21-17)  "tool_calls": [
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-21-18)    {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-21-19)      "id": tool_call_id,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-21-20)      "name": "weather_search",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-21-21)      "args": {"city": "San Francisco, USA"}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-21-22)    }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-21-23)  ],
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-21-24)  # This is important - this needs to be the same as the message you replacing!
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-21-25)  # Otherwise, it will show up as a separate message
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-21-26)  "id": current_id
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-21-27)}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-21-28)await client.threads.update_state(
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-21-29)  # This is the config which represents this thread
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-21-30)  thread['thread_id'], 
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-21-31)  # This is the updated value we want to push
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-21-32)  {"messages": [new_message]}, 
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-21-33)  # We push this update acting as our human_review_node
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-21-34)  as_node="human_review_node"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-21-35))
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-21-36)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-21-37)print("\nResuming Execution")
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-21-38)# Let's now continue executing from here
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-21-39)async for chunk in client.runs.stream(
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-21-40)  thread["thread_id"],
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-21-41)  assistant_id,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-21-42)  input=None,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-21-43)):
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-21-44)  if chunk.data and chunk.event != "metadata": 
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-21-45)    print(chunk.data)

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-22-1)conststate=awaitclient.threads.getState(thread.thread_id);
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-22-2)console.log("Current State:");
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-22-3)console.log(state.values);
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-22-4)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-22-5)console.log("\nCurrent Tool Call ID:");
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-22-6)constlastMessage=state.values.messages[state.values.messages.length-1];
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-22-7)constcurrentContent=lastMessage.content;
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-22-8)constcurrentId=lastMessage.id;
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-22-9)consttoolCallId=lastMessage.tool_calls[0].id;
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-22-10)console.log(toolCallId);
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-22-11)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-22-12)// Construct a replacement tool call
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-22-13)constnewMessage={
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-22-14)role:"assistant",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-22-15)content:currentContent,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-22-16)tool_calls:[
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-22-17){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-22-18)id:toolCallId,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-22-19)name:"weather_search",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-22-20)args:{city:"San Francisco, USA"}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-22-21)}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-22-22)],
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-22-23)// Ensure the ID is the same as the message you're replacing
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-22-24)id:currentId
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-22-25)};
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-22-26)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-22-27)awaitclient.threads.updateState(
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-22-28)thread.thread_id,// Thread ID
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-22-29){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-22-30)values:{"messages":[newMessage]},// Updated message
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-22-31)asNode:"human_review_node"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-22-32)}// Acting as human_review_node
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-22-33));
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-22-34)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-22-35)console.log("\nResuming Execution");
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-22-36)// Continue executing from here
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-22-37)conststreamResponseResumed=client.runs.stream(
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-22-38)thread["thread_id"],
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-22-39)assistantId,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-22-40){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-22-41)input:null,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-22-42)}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-22-43));
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-22-44)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-22-45)forawait(constchunkofstreamResponseResumed){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-22-46)if(chunk.data&&chunk.event!=="metadata"){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-22-47)console.log(chunk.data);
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-22-48)}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-22-49)}

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-23-1)curl--requestPOST\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-23-2)--url<DEPLOYMENT_URL>/threads/<THREAD_ID>/state\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-23-3)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-23-4)--data"{
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-23-5)  \"values\": { \"messages\": [$(curl--requestGET\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-23-6)--url<DEPLOYMENT_URL>/threads/<THREAD_ID>/state|
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-23-7)jq-c'{
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-23-8)    role: "assistant",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-23-9)    content: .values.messages[-1].content,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-23-10)    tool_calls: [
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-23-11)      {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-23-12)      id: .values.messages[-1].tool_calls[0].id,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-23-13)      name: "weather_search",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-23-14)      args: { city: "San Francisco, USA" }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-23-15)      }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-23-16)    ],
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-23-17)    id: .values.messages[-1].id
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-23-18)    }')
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-23-19)  ]},
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-23-20)  \"as_node\": \"human_review_node\"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-23-21)}"&&echo"Resuming Execution"&&curl--requestPOST\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-23-22)--url<DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/stream\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-23-23)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-23-24)--data'{
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-23-25)"assistant_id": "agent"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-23-26)}'|\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-23-27)sed's/\r$//'|\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-23-28)awk'
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-23-29)/^event:/ {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-23-30)  if (data_content != "" && event_type != "metadata") {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-23-31)    print data_content "\n"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-23-32)  }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-23-33)  sub(/^event: /, "", $0)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-23-34)  event_type = $0
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-23-35)  data_content = ""
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-23-36)}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-23-37)/^data:/ {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-23-38)  sub(/^data: /, "", $0)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-23-39)  data_content = $0
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-23-40)}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-23-41)END {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-23-42)  if (data_content != "" && event_type != "metadata") {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-23-43)    print data_content "\n"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-23-44)  }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-23-45)}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-23-46)'

```


Output:

```
Current State:
{'messages': [{'content': "what's the weather in sf?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': '8713d1fa-9b26-4eab-b768-dafdaac70590', 'example': False}, {'content': [{'text': 'To get the weather information for San Francisco, I can use the weather_search function. Let me do that for you.', 'type': 'text', 'index': 0}, {'id': 'toolu_01VzagzsUGZsNMwW1wHkcw7h', 'input': {}, 'name': 'weather_search', 'type': 'tool_use', 'index': 1, 'partial_json': '{"city": "San Francisco"}'}], 'additional_kwargs': {}, 'response_metadata': {'stop_reason': 'tool_use', 'stop_sequence': None}, 'type': 'ai', 'name': None, 'id': 'run-ede13f26-daf5-4d8f-817a-7611075bbcf1', 'example': False, 'tool_calls': [{'name': 'weather_search', 'args': {'city': 'San Francisco'}, 'id': 'toolu_01VzagzsUGZsNMwW1wHkcw7h', 'type': 'tool_call'}], 'invalid_tool_calls': [], 'usage_metadata': {'input_tokens': 360, 'output_tokens': 80, 'total_tokens': 440}}]}
Current Tool Call ID:
toolu_01VzagzsUGZsNMwW1wHkcw7h
Resuming Execution
{'messages': [{'content': "what's the weather in sf?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': '8713d1fa-9b26-4eab-b768-dafdaac70590', 'example': False}, {'content': [{'text': 'To get the weather information for San Francisco, I can use the weather_search function. Let me do that for you.', 'type': 'text', 'index': 0}, {'id': 'toolu_01VzagzsUGZsNMwW1wHkcw7h', 'input': {}, 'name': 'weather_search', 'type': 'tool_use', 'index': 1, 'partial_json': '{"city": "San Francisco"}'}], 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-ede13f26-daf5-4d8f-817a-7611075bbcf1', 'example': False, 'tool_calls': [{'name': 'weather_search', 'args': {'city': 'San Francisco, USA'}, 'id': 'toolu_01VzagzsUGZsNMwW1wHkcw7h', 'type': 'tool_call'}], 'invalid_tool_calls': [], 'usage_metadata': None}, {'content': 'Sunny!', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'tool', 'name': 'weather_search', 'id': '7fc7d463-66bf-4555-9929-6af483de169b', 'tool_call_id': 'toolu_01VzagzsUGZsNMwW1wHkcw7h', 'artifact': None, 'status': 'success'}]}
{'messages': [{'content': "what's the weather in sf?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': '8713d1fa-9b26-4eab-b768-dafdaac70590', 'example': False}, {'content': [{'text': 'To get the weather information for San Francisco, I can use the weather_search function. Let me do that for you.', 'type': 'text', 'index': 0}, {'id': 'toolu_01VzagzsUGZsNMwW1wHkcw7h', 'input': {}, 'name': 'weather_search', 'type': 'tool_use', 'index': 1, 'partial_json': '{"city": "San Francisco"}'}], 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-ede13f26-daf5-4d8f-817a-7611075bbcf1', 'example': False, 'tool_calls': [{'name': 'weather_search', 'args': {'city': 'San Francisco, USA'}, 'id': 'toolu_01VzagzsUGZsNMwW1wHkcw7h', 'type': 'tool_call'}], 'invalid_tool_calls': [], 'usage_metadata': None}, {'content': 'Sunny!', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'tool', 'name': 'weather_search', 'id': '7fc7d463-66bf-4555-9929-6af483de169b', 'tool_call_id': 'toolu_01VzagzsUGZsNMwW1wHkcw7h', 'artifact': None, 'status': 'success'}, {'content': [{'text': "\n\nBased on the search result, the weather in San Francisco is sunny! It's a beautiful day in the city by the bay. Is there anything else you'd like to know about the weather or any other information I can help you with?", 'type': 'text', 'index': 0}], 'additional_kwargs': {}, 'response_metadata': {'stop_reason': 'end_turn', 'stop_sequence': None}, 'type': 'ai', 'name': None, 'id': 'run-d90ce97a-39f9-4330-985e-67c5f351a0c5', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': {'input_tokens': 455, 'output_tokens': 52, 'total_tokens': 507}}]}

```


## Give feedback to a tool call[¶](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#give-feedback-to-a-tool-call "Permanent link")

Sometimes, you may not want to execute a tool call, but you also may not want to ask the user to manually modify the tool call. In that case it may be better to get natural language feedback from the user. You can then insert these feedback as a mock **RESULT** of the tool call.

There are multiple ways to do this:

You could add a new message to the state (representing the "result" of a tool call) You could add TWO new messages to the state - one representing an "error" from the tool call, other HumanMessage representing the feedback Both are similar in that they involve adding messages to the state. The main difference lies in the logic AFTER the `human_node` and how it handles different types of messages.

For this example we will just add a single tool call representing the feedback. Let's see this in action!

[Python](#__tabbed_9_1)[Javascript](#__tabbed_9_2)[CURL](#__tabbed_9_3)

```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-24-1)input = {"messages": [{"role": "user", "content": "what's the weather in sf?"}]}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-24-2)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-24-3)async for chunk in client.runs.stream(
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-24-4)  thread["thread_id"],
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-24-5)  assistant_id,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-24-6)  input=input,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-24-7)):
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-24-8)  if chunk.data and chunk.event != "metadata": 
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-24-9)    print(chunk.data)

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-25-1)constinput={"messages":[{"role":"user","content":"what's the weather in sf?"}]};
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-25-2)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-25-3)conststreamResponse=client.runs.stream(
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-25-4)thread["thread_id"],
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-25-5)assistantId,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-25-6){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-25-7)input:input,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-25-8)}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-25-9));
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-25-10)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-25-11)forawait(constchunkofstreamResponse){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-25-12)if(chunk.data&&chunk.event!=="metadata"){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-25-13)console.log(chunk.data);
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-25-14)}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-25-15)}

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-26-1)curl--requestPOST\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-26-2)--url<DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/stream\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-26-3)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-26-4)--data"{
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-26-5)  \"assistant_id\": \"agent\",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-26-6)  \"input\": {\"messages\": [{\"role\": \"human\", \"content\": \"what's the weather in sf?\"}]}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-26-7) }"|\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-26-8)sed's/\r$//'|\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-26-9)awk'
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-26-10) /^event:/ {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-26-11)   if (data_content != "" && event_type != "metadata") {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-26-12)     print data_content "\n"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-26-13)   }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-26-14)   sub(/^event: /, "", $0)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-26-15)   event_type = $0
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-26-16)   data_content = ""
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-26-17) }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-26-18) /^data:/ {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-26-19)   sub(/^data: /, "", $0)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-26-20)   data_content = $0
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-26-21) }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-26-22) END {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-26-23)   if (data_content != "" && event_type != "metadata") {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-26-24)     print data_content "\n"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-26-25)   }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-26-26) }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-26-27) '

```


Output:

```
{'messages': [{'content': "what's the weather in sf?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': 'c80f13d0-674d-4233-b6a0-3940509d3cf3', 'example': False}]}
{'messages': [{'content': "what's the weather in sf?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': 'c80f13d0-674d-4233-b6a0-3940509d3cf3', 'example': False}, {'content': [{'text': 'To get the weather information for San Francisco, I can use the weather_search function. Let me do that for you.', 'type': 'text', 'index': 0}, {'id': 'toolu_016XyTdFA8NuPWeLyZPSzoM3', 'input': {}, 'name': 'weather_search', 'type': 'tool_use', 'index': 1, 'partial_json': '{"city": "San Francisco"}'}], 'additional_kwargs': {}, 'response_metadata': {'stop_reason': 'tool_use', 'stop_sequence': None}, 'type': 'ai', 'name': None, 'id': 'run-4911ac27-3d7c-4edf-a3ca-c2908e3922eb', 'example': False, 'tool_calls': [{'name': 'weather_search', 'args': {'city': 'San Francisco'}, 'id': 'toolu_016XyTdFA8NuPWeLyZPSzoM3', 'type': 'tool_call'}], 'invalid_tool_calls': [], 'usage_metadata': {'input_tokens': 360, 'output_tokens': 80, 'total_tokens': 440}}]}

```


To do this, we first need to update the state. We can do this by passing a message in with the same **tool call id** of the tool call we want to respond to. Note that this is a **different*** ID from above

[Python](#__tabbed_10_1)[Javascript](#__tabbed_10_2)[CURL](#__tabbed_10_3)

```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-27-1)# To get the ID of the message we want to replace, we need to fetch the current state and find it there.
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-27-2)state = await client.threads.get_state(thread['thread_id'])
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-27-3)print("Current State:")
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-27-4)print(state['values'])
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-27-5)print("\nCurrent Tool Call ID:")
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-27-6)tool_call_id = state
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-27-7)print(tool_call_id)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-27-8)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-27-9)# We now need to construct a replacement tool call.
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-27-10)# We will change the argument to be `San Francisco, USA`
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-27-11)# Note that we could change any number of arguments or tool names - it just has to be a valid one
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-27-12)new_message = {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-27-13)  "role": "tool", 
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-27-14)  # This is our natural language feedback
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-27-15)  "content": "User requested changes: pass in the country as well",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-27-16)  "name": "weather_search",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-27-17)  "tool_call_id": tool_call_id
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-27-18)}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-27-19)await client.threads.update_state(
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-27-20)  # This is the config which represents this thread
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-27-21)  thread['thread_id'], 
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-27-22)  # This is the updated value we want to push
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-27-23)  {"messages": [new_message]}, 
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-27-24)  # We push this update acting as our human_review_node
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-27-25)  as_node="human_review_node"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-27-26))
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-27-27)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-27-28)print("\nResuming execution")
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-27-29)# Let's now continue executing from here
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-27-30)async for chunk in client.runs.stream(
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-27-31)  thread["thread_id"],
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-27-32)  assistant_id,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-27-33)  input=None,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-27-34)  stream_mode="values",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-27-35)):
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-27-36)  if chunk.data and chunk.event != "metadata": 
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-27-37)    print(chunk.data)

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-28-1)conststate=awaitclient.threads.getState(thread.thread_id);
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-28-2)console.log("Current State:");
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-28-3)console.log(state.values);
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-28-4)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-28-5)console.log("\nCurrent Tool Call ID:");
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-28-6)constlastMessage=state.values.messages[state.values.messages.length-1];
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-28-7)consttoolCallId=lastMessage.tool_calls[0].id;
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-28-8)console.log(toolCallId);
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-28-9)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-28-10)// Construct a replacement tool call
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-28-11)constnewMessage={
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-28-12)role:"tool",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-28-13)content:"User requested changes: pass in the country as well",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-28-14)name:"weather_search",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-28-15)tool_call_id:toolCallId,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-28-16)};
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-28-17)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-28-18)awaitclient.threads.updateState(
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-28-19)thread.thread_id,// Thread ID
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-28-20){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-28-21)values:{"messages":[newMessage]},// Updated message
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-28-22)asNode:"human_review_node"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-28-23)}// Acting as human_review_node
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-28-24));
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-28-25)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-28-26)console.log("\nResuming Execution");
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-28-27)// Continue executing from here
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-28-28)conststreamResponseEdited=client.runs.stream(
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-28-29)thread["thread_id"],
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-28-30)assistantId,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-28-31){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-28-32)input:null,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-28-33)streamMode:"values",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-28-34)interruptBefore:["action"],
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-28-35)}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-28-36));
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-28-37)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-28-38)forawait(constchunkofstreamResponseEdited){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-28-39)if(chunk.data&&chunk.event!=="metadata"){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-28-40)console.log(chunk.data);
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-28-41)}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-28-42)}

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-29-1)curl--requestPOST\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-29-2)--url<DEPLOYMENT_URL>/threads/<THREAD_ID>/state\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-29-3)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-29-4)--data"{
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-29-5)  \"values\": { \"messages\": [$(curl--requestGET\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-29-6)--url<DEPLOYMENT_URL>/threads/<THREAD_ID>/state|
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-29-7)jq-c'{
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-29-8)    role: "tool",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-29-9)    content: "User requested changes: pass in the country as well",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-29-10)    name: "get_weather",
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-29-11)    tool_call_id: .values.messages[-1].id.tool_calls[0].id
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-29-12)    }')
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-29-13)  ]},
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-29-14)  \"as_node\": \"human_review_node\"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-29-15)}"&&echo"Resuming Execution"&&curl--requestPOST\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-29-16)--url<DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/stream\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-29-17)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-29-18)--data'{
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-29-19)"assistant_id": "agent"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-29-20)}'|\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-29-21)sed's/\r$//'|\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-29-22)awk'
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-29-23)/^event:/ {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-29-24)  if (data_content != "" && event_type != "metadata") {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-29-25)    print data_content "\n"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-29-26)  }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-29-27)  sub(/^event: /, "", $0)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-29-28)  event_type = $0
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-29-29)  data_content = ""
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-29-30)}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-29-31)/^data:/ {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-29-32)  sub(/^data: /, "", $0)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-29-33)  data_content = $0
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-29-34)}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-29-35)END {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-29-36)  if (data_content != "" && event_type != "metadata") {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-29-37)    print data_content "\n"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-29-38)  }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-29-39)}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-29-40)'

```


Output:

```
Current State:
{'messages': [{'content': "what's the weather in sf?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': '3b2bbc38-d11b-49eb-80c0-c24a40dab5a8', 'example': False}, {'content': [{'text': 'To get the weather information for San Francisco, I can use the weather_search function. Let me do that for you.', 'type': 'text', 'index': 0}, {'id': 'toolu_01NNw18j57GEGPZvsa9f1wvX', 'input': {}, 'name': 'weather_search', 'type': 'tool_use', 'index': 1, 'partial_json': '{"city": "San Francisco"}'}], 'additional_kwargs': {}, 'response_metadata': {'stop_reason': 'tool_use', 'stop_sequence': None}, 'type': 'ai', 'name': None, 'id': 'run-c5a50900-abf5-4885-9cdb-da2bf0d892ac', 'example': False, 'tool_calls': [{'name': 'weather_search', 'args': {'city': 'San Francisco'}, 'id': 'toolu_01NNw18j57GEGPZvsa9f1wvX', 'type': 'tool_call'}], 'invalid_tool_calls': [], 'usage_metadata': {'input_tokens': 360, 'output_tokens': 80, 'total_tokens': 440}}]}
Current Tool Call ID:
toolu_01NNw18j57GEGPZvsa9f1wvX
Resuming execution
{'messages': [{'content': "what's the weather in sf?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': '3b2bbc38-d11b-49eb-80c0-c24a40dab5a8', 'example': False}, {'content': [{'text': 'To get the weather information for San Francisco, I can use the weather_search function. Let me do that for you.', 'type': 'text', 'index': 0}, {'id': 'toolu_01NNw18j57GEGPZvsa9f1wvX', 'input': {}, 'name': 'weather_search', 'type': 'tool_use', 'index': 1, 'partial_json': '{"city": "San Francisco"}'}], 'additional_kwargs': {}, 'response_metadata': {'stop_reason': 'tool_use', 'stop_sequence': None}, 'type': 'ai', 'name': None, 'id': 'run-c5a50900-abf5-4885-9cdb-da2bf0d892ac', 'example': False, 'tool_calls': [{'name': 'weather_search', 'args': {'city': 'San Francisco'}, 'id': 'toolu_01NNw18j57GEGPZvsa9f1wvX', 'type': 'tool_call'}], 'invalid_tool_calls': [], 'usage_metadata': {'input_tokens': 360, 'output_tokens': 80, 'total_tokens': 440}}, {'content': 'User requested changes: pass in the country as well', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'tool', 'name': 'weather_search', 'id': '787288be-213c-4fd3-8503-4a009bdb1b00', 'tool_call_id': 'toolu_01NNw18j57GEGPZvsa9f1wvX', 'artifact': None, 'status': 'success'}, {'content': [{'text': '\n\nI apologize for the oversight. It seems the function requires additional information. Let me try again with a more specific request.', 'type': 'text', 'index': 0}, {'id': 'toolu_01YAbLBoKozJyRQnB8LUMpXC', 'input': {}, 'name': 'weather_search', 'type': 'tool_use', 'index': 1, 'partial_json': '{"city": "San Francisco, USA"}'}], 'additional_kwargs': {}, 'response_metadata': {'stop_reason': 'tool_use', 'stop_sequence': None}, 'type': 'ai', 'name': None, 'id': 'run-5c355a56-cfe3-4046-b49f-f5b09fc397ef', 'example': False, 'tool_calls': [{'name': 'weather_search', 'args': {'city': 'San Francisco, USA'}, 'id': 'toolu_01YAbLBoKozJyRQnB8LUMpXC', 'type': 'tool_call'}], 'invalid_tool_calls': [], 'usage_metadata': {'input_tokens': 461, 'output_tokens': 83, 'total_tokens': 544}}]}

```


We can see that we now get to another breakpoint - because it went back to the model and got an entirely new prediction of what to call. Let's now approve this one and continue

[Python](#__tabbed_11_1)[Javascript](#__tabbed_11_2)[CURL](#__tabbed_11_3)

```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-30-1)async for chunk in client.runs.stream(
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-30-2)  thread["thread_id"],
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-30-3)  assistant_id,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-30-4)  input=None,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-30-5)):
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-30-6)  if chunk.data and chunk.event != "metadata": 
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-30-7)    print(chunk.data)

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-31-1)conststreamResponseResumed=client.runs.stream(
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-31-2)thread["thread_id"],
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-31-3)assistantId,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-31-4){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-31-5)input:null,
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-31-6)}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-31-7));
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-31-8)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-31-9)forawait(constchunkofstreamResponseResumed){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-31-10)if(chunk.data&&chunk.event!=="metadata"){
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-31-11)console.log(chunk.data);
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-31-12)}
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-31-13)}

```


```
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-32-1)curl--requestPOST\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-32-2)--url<DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/stream\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-32-3)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-32-4)--data"{
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-32-5)  \"assistant_id\": \"agent\"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-32-6) }"|\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-32-7)sed's/\r$//'|\
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-32-8)awk'
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-32-9) /^event:/ {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-32-10)   if (data_content != "" && event_type != "metadata") {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-32-11)     print data_content "\n"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-32-12)   }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-32-13)   sub(/^event: /, "", $0)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-32-14)   event_type = $0
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-32-15)   data_content = ""
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-32-16) }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-32-17) /^data:/ {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-32-18)   sub(/^data: /, "", $0)
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-32-19)   data_content = $0
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-32-20) }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-32-21) END {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-32-22)   if (data_content != "" && event_type != "metadata") {
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-32-23)     print data_content "\n"
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-32-24)   }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-32-25) }
[](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__codelineno-32-26) '

```


Output:

```
{'messages': [{'content': "what's the weather in sf?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': '3b2bbc38-d11b-49eb-80c0-c24a40dab5a8', 'example': False}, {'content': [{'text': 'To get the weather information for San Francisco, I can use the weather_search function. Let me do that for you.', 'type': 'text', 'index': 0}, {'id': 'toolu_01NNw18j57GEGPZvsa9f1wvX', 'input': {}, 'name': 'weather_search', 'type': 'tool_use', 'index': 1, 'partial_json': '{"city": "San Francisco"}'}], 'additional_kwargs': {}, 'response_metadata': {'stop_reason': 'tool_use', 'stop_sequence': None}, 'type': 'ai', 'name': None, 'id': 'run-c5a50900-abf5-4885-9cdb-da2bf0d892ac', 'example': False, 'tool_calls': [{'name': 'weather_search', 'args': {'city': 'San Francisco'}, 'id': 'toolu_01NNw18j57GEGPZvsa9f1wvX', 'type': 'tool_call'}], 'invalid_tool_calls': [], 'usage_metadata': {'input_tokens': 360, 'output_tokens': 80, 'total_tokens': 440}}, {'content': 'User requested changes: pass in the country as well', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'tool', 'name': 'weather_search', 'id': '787288be-213c-4fd3-8503-4a009bdb1b00', 'tool_call_id': 'toolu_01NNw18j57GEGPZvsa9f1wvX', 'artifact': None, 'status': 'success'}, {'content': [{'text': '\n\nI apologize for the oversight. It seems the function requires additional information. Let me try again with a more specific request.', 'type': 'text', 'index': 0}, {'id': 'toolu_01YAbLBoKozJyRQnB8LUMpXC', 'input': {}, 'name': 'weather_search', 'type': 'tool_use', 'index': 1, 'partial_json': '{"city": "San Francisco, USA"}'}], 'additional_kwargs': {}, 'response_metadata': {'stop_reason': 'tool_use', 'stop_sequence': None}, 'type': 'ai', 'name': None, 'id': 'run-5c355a56-cfe3-4046-b49f-f5b09fc397ef', 'example': False, 'tool_calls': [{'name': 'weather_search', 'args': {'city': 'San Francisco, USA'}, 'id': 'toolu_01YAbLBoKozJyRQnB8LUMpXC', 'type': 'tool_call'}], 'invalid_tool_calls': [], 'usage_metadata': {'input_tokens': 461, 'output_tokens': 83, 'total_tokens': 544}}, {'content': 'Sunny!', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'tool', 'name': 'weather_search', 'id': '3b857482-bca2-4a73-a9ab-1f35a3e43e5f', 'tool_call_id': 'toolu_01YAbLBoKozJyRQnB8LUMpXC', 'artifact': None, 'status': 'success'}]}
{'messages': [{'content': "what's the weather in sf?", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': '3b2bbc38-d11b-49eb-80c0-c24a40dab5a8', 'example': False}, {'content': [{'text': 'To get the weather information for San Francisco, I can use the weather_search function. Let me do that for you.', 'type': 'text', 'index': 0}, {'id': 'toolu_01NNw18j57GEGPZvsa9f1wvX', 'input': {}, 'name': 'weather_search', 'type': 'tool_use', 'index': 1, 'partial_json': '{"city": "San Francisco"}'}], 'additional_kwargs': {}, 'response_metadata': {'stop_reason': 'tool_use', 'stop_sequence': None}, 'type': 'ai', 'name': None, 'id': 'run-c5a50900-abf5-4885-9cdb-da2bf0d892ac', 'example': False, 'tool_calls': [{'name': 'weather_search', 'args': {'city': 'San Francisco'}, 'id': 'toolu_01NNw18j57GEGPZvsa9f1wvX', 'type': 'tool_call'}], 'invalid_tool_calls': [], 'usage_metadata': {'input_tokens': 360, 'output_tokens': 80, 'total_tokens': 440}}, {'content': 'User requested changes: pass in the country as well', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'tool', 'name': 'weather_search', 'id': '787288be-213c-4fd3-8503-4a009bdb1b00', 'tool_call_id': 'toolu_01NNw18j57GEGPZvsa9f1wvX', 'artifact': None, 'status': 'success'}, {'content': [{'text': '\n\nI apologize for the oversight. It seems the function requires additional information. Let me try again with a more specific request.', 'type': 'text', 'index': 0}, {'id': 'toolu_01YAbLBoKozJyRQnB8LUMpXC', 'input': {}, 'name': 'weather_search', 'type': 'tool_use', 'index': 1, 'partial_json': '{"city": "San Francisco, USA"}'}], 'additional_kwargs': {}, 'response_metadata': {'stop_reason': 'tool_use', 'stop_sequence': None}, 'type': 'ai', 'name': None, 'id': 'run-5c355a56-cfe3-4046-b49f-f5b09fc397ef', 'example': False, 'tool_calls': [{'name': 'weather_search', 'args': {'city': 'San Francisco, USA'}, 'id': 'toolu_01YAbLBoKozJyRQnB8LUMpXC', 'type': 'tool_call'}], 'invalid_tool_calls': [], 'usage_metadata': {'input_tokens': 461, 'output_tokens': 83, 'total_tokens': 544}}, {'content': 'Sunny!', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'tool', 'name': 'weather_search', 'id': '3b857482-bca2-4a73-a9ab-1f35a3e43e5f', 'tool_call_id': 'toolu_01YAbLBoKozJyRQnB8LUMpXC', 'artifact': None, 'status': 'success'}, {'content': [{'text': "\n\nGreat news! The weather in San Francisco is sunny today. Is there anything else you'd like to know about the weather or any other information I can help you with?", 'type': 'text', 'index': 0}], 'additional_kwargs': {}, 'response_metadata': {'stop_reason': 'end_turn', 'stop_sequence': None}, 'type': 'ai', 'name': None, 'id': 'run-6a857bb1-f65b-4b86-93d6-c025e003c777', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': {'input_tokens': 557, 'output_tokens': 38, 'total_tokens': 595}}]}

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to Replay and Branch from Prior States  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_time_travel/) [ Next  Interrupt  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/interrupt_concurrent/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/human_in_the_loop_review_tool_calls/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
