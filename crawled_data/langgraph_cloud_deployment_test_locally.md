---
url: https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#how-to-test-a-langgraph-app-locally)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to test a LangGraph app locally 

[ ](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/?q= "Share")

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
          * Application Structure  Application Structure 
            * [ Application Structure  ](https://langchain-ai.github.io/langgraph/how-tos#application-structure)
            * [ How to Set Up a LangGraph Application for Deployment  ](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/)
            * [ How to Set Up a LangGraph Application for Deployment  ](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_pyproject/)
            * [ How to Set Up a LangGraph.js Application for Deployment  ](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/)
            * [ How to add semantic search to your LangGraph deployment  ](https://langchain-ai.github.io/langgraph/cloud/deployment/semantic_search/)
            * [ How to customize Dockerfile  ](https://langchain-ai.github.io/langgraph/cloud/deployment/custom_docker/)
            * How to test a LangGraph app locally  [ How to test a LangGraph app locally  ](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#setup)
              * [ Start the API server  ](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#start-the-api-server)
                * [ Interact with the server  ](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#interact-with-the-server)
                  * [ Initialize with authentication  ](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#initialize-with-authentication)
                  * [ Initialize with environment variables  ](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#initialize-with-environment-variables)
            * [ Rebuild Graph at Runtime  ](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/)
            * [ How to use LangGraph Platform to deploy CrewAI, AutoGen, and other frameworks  ](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/)
          * [ Deployment  ](https://langchain-ai.github.io/langgraph/how-tos#deployment)
          * [ Authentication & Access Control  ](https://langchain-ai.github.io/langgraph/how-tos#authentication-access-control)
          * [ Assistants  ](https://langchain-ai.github.io/langgraph/how-tos#assistants)
          * [ Threads  ](https://langchain-ai.github.io/langgraph/how-tos#threads)
          * [ Runs  ](https://langchain-ai.github.io/langgraph/how-tos#runs)
          * [ Streaming  ](https://langchain-ai.github.io/langgraph/how-tos#streaming_1)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#setup)
  * [ Start the API server  ](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#start-the-api-server)
    * [ Interact with the server  ](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#interact-with-the-server)
      * [ Initialize with authentication  ](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#initialize-with-authentication)
      * [ Initialize with environment variables  ](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#initialize-with-environment-variables)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph-platform)
  5. [ Application Structure  ](https://langchain-ai.github.io/langgraph/how-tos#application-structure)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/cloud/deployment/test_locally.md "Edit this page")

# How to test a LangGraph app locally[¶](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#how-to-test-a-langgraph-app-locally "Permanent link")

This guide assumes you have a LangGraph app correctly set up with a proper configuration file and a corresponding compiled graph, and that you have a proper LangChain API key.

Testing locally ensures that there are no errors or conflicts with Python dependencies and confirms that the configuration file is specified correctly.

## Setup[¶](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#setup "Permanent link")

Install the LangGraph CLI package:

```
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-0-1)pipinstall-U"langgraph-cli[inmem]"

```


Ensure you have an API key, which you can create from the [LangSmith UI](https://smith.langchain.com) (Settings > API Keys). This is required to authenticate that you have LangGraph Cloud access. After you have saved the key to a safe place, place the following line in your `.env` file:

```
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-1-1)LANGSMITH_API_KEY = *********

```


## Start the API server[¶](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#start-the-api-server "Permanent link")

Once you have installed the CLI, you can run the following command to start the API server for local testing:

```
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-2-1)langgraphdev

```


This will start up the LangGraph API server locally. If this runs successfully, you should see something like:

> Ready!
> 
>   * API: [http://localhost:2024](http://localhost:2024/)
> 
>   * Docs: <http://localhost:2024/docs>
> 
>   * LangGraph Studio Web UI: <https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024>
> 
> 


In-Memory Mode

The `langgraph dev` command starts LangGraph Server in an in-memory mode. This mode is suitable for development and testing purposes. For production use, you should deploy LangGraph Server with access to a persistent storage backend.

If you want to test your application with a persistent storage backend, you can use the `langgraph up` command instead of `langgraph dev`. You will need to have `docker` installed on your machine to use this command.

### Interact with the server[¶](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#interact-with-the-server "Permanent link")

We can now interact with the API server using the LangGraph SDK. First, we need to start our client, select our assistant (in this case a graph we called "agent", make sure to select the proper assistant you wish to test).

You can either initialize by passing authentication or by setting an environment variable.

#### Initialize with authentication[¶](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#initialize-with-authentication "Permanent link")

[Python](#__tabbed_1_1)[Javascript](#__tabbed_1_2)[CURL](#__tabbed_1_3)

```
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-3-1)fromlanggraph_sdkimport get_client
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-3-2)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-3-3)# only pass the url argument to get_client() if you changed the default port when calling langgraph dev
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-3-4)client = get_client(url=<DEPLOYMENT_URL>,api_key=<LANGSMITH_API_KEY>)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-3-5)# Using the graph deployed with the name "agent"
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-3-6)assistant_id = "agent"
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-3-7)thread = await client.threads.create()

```


```
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-4-1)import{Client}from"@langchain/langgraph-sdk";
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-4-2)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-4-3)// only set the apiUrl if you changed the default port when calling langgraph dev
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-4-4)constclient=newClient({apiUrl:<DEPLOYMENT_URL>,apiKey:<LANGSMITH_API_KEY>});
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-4-5)// Using the graph deployed with the name "agent"
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-4-6)constassistantId="agent";
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-4-7)constthread=awaitclient.threads.create();

```


```
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-5-1)curl--requestPOST\
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-5-2)--url<DEPLOYMENT_URL>/threads\
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-5-3)--header'Content-Type: application/json'
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-5-4)--header'x-api-key: <LANGSMITH_API_KEY>'

```


#### Initialize with environment variables[¶](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#initialize-with-environment-variables "Permanent link")

If you have a `LANGSMITH_API_KEY` set in your environment, you do not need to explicitly pass authentication to the client

[Python](#__tabbed_2_1)[Javascript](#__tabbed_2_2)[CURL](#__tabbed_2_3)

```
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-6-1)fromlanggraph_sdkimport get_client
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-6-2)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-6-3)# only pass the url argument to get_client() if you changed the default port when calling langgraph dev
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-6-4)client = get_client()
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-6-5)# Using the graph deployed with the name "agent"
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-6-6)assistant_id = "agent"
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-6-7)thread = await client.threads.create()

```


```
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-7-1)import{Client}from"@langchain/langgraph-sdk";
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-7-2)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-7-3)// only set the apiUrl if you changed the default port when calling langgraph dev
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-7-4)constclient=newClient();
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-7-5)// Using the graph deployed with the name "agent"
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-7-6)constassistantId="agent";
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-7-7)constthread=awaitclient.threads.create();

```


```
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-8-1)curl--requestPOST\
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-8-2)--url<DEPLOYMENT_URL>/threads\
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-8-3)--header'Content-Type: application/json'

```


Now we can invoke our graph to ensure it is working. Make sure to change the input to match the proper schema for your graph. 

[Python](#__tabbed_3_1)[Javascript](#__tabbed_3_2)[CURL](#__tabbed_3_3)

```
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-9-1)input = {"messages": [{"role": "user", "content": "what's the weather in sf"}]}
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-9-2)async for chunk in client.runs.stream(
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-9-3)  thread["thread_id"],
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-9-4)  assistant_id,
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-9-5)  input=input,
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-9-6)  stream_mode="updates",
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-9-7)):
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-9-8)  print(f"Receiving new event of type: {chunk.event}...")
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-9-9)  print(chunk.data)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-9-10)  print("\n\n")

```


```
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-10-1)constinput={"messages":[{"role":"user","content":"what's the weather in sf"}]}
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-10-2)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-10-3)conststreamResponse=client.runs.stream(
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-10-4)thread["thread_id"],
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-10-5)assistantId,
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-10-6){
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-10-7)input:input,
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-10-8)streamMode:"updates",
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-10-9)}
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-10-10));
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-10-11)forawait(constchunkofstreamResponse){
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-10-12)console.log(`Receiving new event of type: ${chunk.event}...`);
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-10-13)console.log(chunk.data);
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-10-14)console.log("\n\n");
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-10-15)}

```


```
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-11-1)curl--requestPOST\
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-11-2)--url<DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/stream\
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-11-3)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-11-4)--data"{
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-11-5)  \"assistant_id\": \"agent\",
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-11-6)  \"input\": {\"messages\": [{\"role\": \"human\", \"content\": \"what's the weather in sf\"}]},
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-11-7)  \"stream_mode\": [
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-11-8)   \"events\"
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-11-9)  ]
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-11-10) }"|\
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-11-11)sed's/\r$//'|\
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-11-12)awk'
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-11-13) /^event:/ {
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-11-14)   if (data_content != "") {
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-11-15)     print data_content "\n"
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-11-16)   }
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-11-17)   sub(/^event: /, "Receiving event of type: ", $0)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-11-18)   printf "%s...\n", $0
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-11-19)   data_content = ""
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-11-20) }
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-11-21) /^data:/ {
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-11-22)   sub(/^data: /, "", $0)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-11-23)   data_content = $0
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-11-24) }
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-11-25) END {
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-11-26)   if (data_content != "") {
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-11-27)     print data_content "\n"
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-11-28)   }
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-11-29) }
[](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__codelineno-11-30) '

```


If your graph works correctly, you should see your graph output displayed in the console. Of course, there are many more ways you might need to test your graph, for a full list of commands you can send with the SDK, see the [Python](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/) and [JS/TS](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/) references.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to customize Dockerfile  ](https://langchain-ai.github.io/langgraph/cloud/deployment/custom_docker/) [ Next  Rebuild Graph at Runtime  ](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
