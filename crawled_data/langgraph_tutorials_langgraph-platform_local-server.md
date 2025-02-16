---
url: https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#quickstart-launch-local-langgraph-server)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Local Deploy 

[ ](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/?q= "Share")

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
      * [ Concepts  ](https://langchain-ai.github.io/langgraph/concepts/)
      * [ Tutorials  ](https://langchain-ai.github.io/langgraph/tutorials/)

Tutorials 
        * [ Quick Start  ](https://langchain-ai.github.io/langgraph/tutorials/workflows/)

Quick Start 
          * [ Quick Start  ](https://langchain-ai.github.io/langgraph/tutorials#quick-start)
          * [ Learn the basics  ](https://langchain-ai.github.io/langgraph/tutorials/introduction/)
          * Local Deploy  [ Local Deploy  ](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/) Table of contents 
            * [ Install the LangGraph CLI  ](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#install-the-langgraph-cli)
            * [ 🌱 Create a LangGraph App  ](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#create-a-langgraph-app)
            * [ Install Dependencies  ](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#install-dependencies)
            * [ Create a .env file  ](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#create-a-env-file)
            * [ 🚀 Launch LangGraph Server  ](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#launch-langgraph-server)
            * [ LangGraph Studio Web UI  ](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#langgraph-studio-web-ui)
            * [ Test the API  ](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#test-the-api)
            * [ Next Steps  ](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#next-steps)
              * [ 🌐 Deploy to LangGraph Cloud  ](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#deploy-to-langgraph-cloud)
              * [ 📚 Learn More about LangGraph Platform  ](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#learn-more-about-langgraph-platform)
              * [ 🛠️ Developer References  ](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#developer-references)
          * [ Cloud Deploy  ](https://langchain-ai.github.io/langgraph/cloud/quick_start/)
        * [ Chatbots  ](https://langchain-ai.github.io/langgraph/tutorials#chatbots)
        * [ RAG  ](https://langchain-ai.github.io/langgraph/tutorials#rag)
        * [ Agent Architectures  ](https://langchain-ai.github.io/langgraph/tutorials#agent-architectures)
        * [ Evaluation & Analysis  ](https://langchain-ai.github.io/langgraph/tutorials#evaluation)
        * [ Experimental  ](https://langchain-ai.github.io/langgraph/tutorials#experimental)
        * [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/concepts#langgraph-platform)
    * Resources  Resources 
      * [ Prebuilt Agents  ](https://langchain-ai.github.io/langgraph/prebuilt/)
      * [ Adopters  ](https://langchain-ai.github.io/langgraph/adopters/)
      * [ FAQ  ](https://langchain-ai.github.io/langgraph/concepts/faq/)
      * [ Troubleshooting  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraph/reference/graphs/)



Table of contents 

  * [ Install the LangGraph CLI  ](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#install-the-langgraph-cli)
  * [ 🌱 Create a LangGraph App  ](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#create-a-langgraph-app)
  * [ Install Dependencies  ](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#install-dependencies)
  * [ Create a .env file  ](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#create-a-env-file)
  * [ 🚀 Launch LangGraph Server  ](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#launch-langgraph-server)
  * [ LangGraph Studio Web UI  ](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#langgraph-studio-web-ui)
  * [ Test the API  ](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#test-the-api)
  * [ Next Steps  ](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#next-steps)
    * [ 🌐 Deploy to LangGraph Cloud  ](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#deploy-to-langgraph-cloud)
    * [ 📚 Learn More about LangGraph Platform  ](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#learn-more-about-langgraph-platform)
    * [ 🛠️ Developer References  ](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#developer-references)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ Tutorials  ](https://langchain-ai.github.io/langgraph/tutorials/)
  4. [ Quick Start  ](https://langchain-ai.github.io/langgraph/tutorials#quick-start)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/tutorials/langgraph-platform/local-server.md "Edit this page")

# Quickstart: Launch Local LangGraph Server[¶](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#quickstart-launch-local-langgraph-server "Permanent link")

This is a quick start guide to help you get a LangGraph app up and running locally.

Requirements

  * Python >= 3.11
  * [LangGraph CLI](https://langchain-ai.github.io/langgraph/cloud/reference/cli/): Requires langchain-cli[inmem] >= 0.1.58



## Install the LangGraph CLI[¶](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#install-the-langgraph-cli "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-0-1)pipinstall--upgrade"langgraph-cli[inmem]"

```


## 🌱 Create a LangGraph App[¶](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#create-a-langgraph-app "Permanent link")

Create a new app from the `react-agent` template. This template is a simple agent that can be flexibly extended to many tools.

[Python Server](#__tabbed_1_1)[Node Server](#__tabbed_1_2)

```
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-1-1)langgraphnewpath/to/your/app--templatereact-agent-python

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-2-1)langgraphnewpath/to/your/app--templatereact-agent-js

```


Additional Templates

If you use `langgraph new` without specifying a template, you will be presented with an interactive menu that will allow you to choose from a list of available templates.

## Install Dependencies[¶](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#install-dependencies "Permanent link")

In the root of your new LangGraph app, install the dependencies in `edit` mode so your local changes are used by the server:

```
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-3-1)pipinstall-e.

```


## Create a `.env` file[¶](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#create-a-env-file "Permanent link")

You will find a `.env.example` in the root of your new LangGraph app. Create a `.env` file in the root of your new LangGraph app and copy the contents of the `.env.example` file into it, filling in the necessary API keys:

```
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-4-1)LANGSMITH_API_KEY=lsv2...
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-4-2)TAVILY_API_KEY=tvly-...
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-4-3)ANTHROPIC_API_KEY=sk-
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-4-4)OPENAI_API_KEY=sk-...

```


Get API Keys

  * **LANGSMITH_API_KEY** : Go to the [LangSmith Settings page](https://smith.langchain.com/settings). Then clck **Create API Key**.
  * **ANTHROPIC_API_KEY** : Get an API key from [Anthropic](https://console.anthropic.com/).
  * **OPENAI_API_KEY** : Get an API key from [OpenAI](https://openai.com/).
  * **TAVILY_API_KEY** : Get an API key on the [Tavily website](https://app.tavily.com/).



## 🚀 Launch LangGraph Server[¶](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#launch-langgraph-server "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-5-1)langgraphdev

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

## LangGraph Studio Web UI[¶](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#langgraph-studio-web-ui "Permanent link")

LangGraph Studio Web is a specialized UI that you can connect to LangGraph API server to enable visualization, interaction, and debugging of your application locally. Test your graph in the LangGraph Studio Web UI by visiting the URL provided in the output of the `langgraph dev` command.

>   * LangGraph Studio Web UI: <https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024>
> 


Connecting to a server with a custom host/port

If you are running the LangGraph API server with a custom host / port, you can point the Studio Web UI at it by changing the `baseUrl` URL param. For example, if you are running your server on port 8000, you can change the above URL to the following:

```
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-6-1)https://smith.langchain.com/studio/baseUrl=http://127.0.0.1:8000

```


Safari Compatibility

Currently, LangGraph Studio Web does not support Safari when running a server locally.

## Test the API[¶](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#test-the-api "Permanent link")

[Python SDK (Async)](#__tabbed_2_1)[Python SDK (Sync)](#__tabbed_2_2)[Javascript SDK](#__tabbed_2_3)[Rest API](#__tabbed_2_4)

**Install the LangGraph Python SDK**

```
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-7-1)pipinstalllanggraph-sdk

```


**Send a message to the assistant (threadless run)**

```
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-8-1)fromlanggraph_sdkimport get_client
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-8-2)
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-8-3)client = get_client(url="http://localhost:2024")
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-8-4)
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-8-5)async for chunk in client.runs.stream(
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-8-6)  None, # Threadless run
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-8-7)  "agent", # Name of assistant. Defined in langgraph.json.
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-8-8)  input={
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-8-9)    "messages": [{
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-8-10)      "role": "human",
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-8-11)      "content": "What is LangGraph?",
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-8-12)    }],
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-8-13)  },
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-8-14)  stream_mode="updates",
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-8-15)):
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-8-16)  print(f"Receiving new event of type: {chunk.event}...")
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-8-17)  print(chunk.data)
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-8-18)  print("\n\n")

```


**Install the LangGraph Python SDK**

```
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-9-1)pipinstalllanggraph-sdk

```


**Send a message to the assistant (threadless run)**

```
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-10-1)fromlanggraph_sdkimport get_sync_client
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-10-2)
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-10-3)client = get_sync_client(url="http://localhost:2024")
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-10-4)
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-10-5)for chunk in client.runs.stream(
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-10-6)  None, # Threadless run
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-10-7)  "agent", # Name of assistant. Defined in langgraph.json.
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-10-8)  input={
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-10-9)    "messages": [{
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-10-10)      "role": "human",
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-10-11)      "content": "What is LangGraph?",
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-10-12)    }],
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-10-13)  },
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-10-14)  stream_mode="updates",
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-10-15)):
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-10-16)  print(f"Receiving new event of type: {chunk.event}...")
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-10-17)  print(chunk.data)
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-10-18)  print("\n\n")

```


**Install the LangGraph JS SDK**

```
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-11-1)npminstall@langchain/langgraph-sdk

```


**Send a message to the assistant (threadless run)**

```
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-12-1)const{Client}=awaitimport("@langchain/langgraph-sdk");
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-12-2)
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-12-3)// only set the apiUrl if you changed the default port when calling langgraph dev
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-12-4)constclient=newClient({apiUrl:"http://localhost:2024"});
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-12-5)
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-12-6)conststreamResponse=client.runs.stream(
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-12-7)null,// Threadless run
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-12-8)"agent",// Assistant ID
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-12-9){
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-12-10)input:{
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-12-11)"messages":[
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-12-12){"role":"user","content":"What is LangGraph?"}
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-12-13)]
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-12-14)},
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-12-15)streamMode:"messages",
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-12-16)}
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-12-17));
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-12-18)
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-12-19)forawait(constchunkofstreamResponse){
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-12-20)console.log(`Receiving new event of type: ${chunk.event}...`);
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-12-21)console.log(JSON.stringify(chunk.data));
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-12-22)console.log("\n\n");
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-12-23)}

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-13-1)curl-s--requestPOST\
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-13-2)--url"http://localhost:2024/runs/stream"\
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-13-3)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-13-4)--data"{
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-13-5)    \"assistant_id\": \"agent\",
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-13-6)    \"input\": {
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-13-7)      \"messages\": [
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-13-8)        {
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-13-9)          \"role\": \"human\",
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-13-10)          \"content\": \"What is LangGraph?\"
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-13-11)        }
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-13-12)      ]
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-13-13)    },
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-13-14)    \"stream_mode\": \"updates\"
[](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__codelineno-13-15)  }"

```


Auth

If you're connecting to a remote server, you will need to provide a LangSmith API Key for authorization. Please see the API Reference for the clients for more information.

## Next Steps[¶](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#next-steps "Permanent link")

Now that you have a LangGraph app running locally, take your journey further by exploring deployment and advanced features:

### 🌐 Deploy to LangGraph Cloud[¶](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#deploy-to-langgraph-cloud "Permanent link")

  * **[LangGraph Cloud Quickstart](https://langchain-ai.github.io/langgraph/cloud/quick_start/)** : Deploy your LangGraph app using LangGraph Cloud.



### 📚 Learn More about LangGraph Platform[¶](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#learn-more-about-langgraph-platform "Permanent link")

Expand your knowledge with these resources:

  * **[LangGraph Platform Concepts](https://langchain-ai.github.io/langgraph/concepts/#langgraph-platform)** : Understand the foundational concepts of the LangGraph Platform. 
  * **[LangGraph Platform How-to Guides](https://langchain-ai.github.io/langgraph/how-tos/#langgraph-platform)** : Discover step-by-step guides to build and deploy applications.



### 🛠️ Developer References[¶](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#developer-references "Permanent link")

Access detailed documentation for development and API usage:

  * **[LangGraph Server API Reference](https://langchain-ai.github.io/langgraph/cloud/reference/api/api_ref.html)** : Explore the LangGraph Server API documentation. 
  * **[Python SDK Reference](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/)** : Explore the Python SDK API Reference.
  * **[JS/TS SDK Reference](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/)** : Explore the JS/TS SDK API Reference.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Workflows and Agents  ](https://langchain-ai.github.io/langgraph/tutorials/workflows/) [ Next  Cloud Deploy  ](https://langchain-ai.github.io/langgraph/cloud/quick_start/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
