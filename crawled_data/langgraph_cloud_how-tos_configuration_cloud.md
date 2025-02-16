---
url: https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#how-to-create-agents-with-configuration)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to create agents with configuration 

[ ](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/?q= "Share")

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
          * Assistants  Assistants 
            * [ Assistants  ](https://langchain-ai.github.io/langgraph/how-tos#assistants)
            * [ How to create agents with configuration  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/)
            * [ How to version assistants  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/)
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



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph-platform)
  5. [ Assistants  ](https://langchain-ai.github.io/langgraph/how-tos#assistants)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/cloud/how-tos/configuration_cloud.md "Edit this page")

# How to create agents with configuration[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#how-to-create-agents-with-configuration "Permanent link")

One of the benefits of LangGraph API is that it lets you create agents with different configurations. This is useful when you want to:

  * Define a cognitive architecture once as a LangGraph
  * Let that LangGraph be configurable across some attributes (for example, system message or LLM to use)
  * Let users create agents with arbitrary configurations, save them, and then use them in the future



In this guide we will show how to do that for the default agent we have built in.

If you look at the agent we defined, you can see that inside the `call_model` node we have created the model based on some configuration. That node looks like:

[Python](#__tabbed_1_1)[Javascript](#__tabbed_1_2)

```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-0-1)defcall_model(state, config):
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-0-2)  messages = state["messages"]
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-0-3)  model_name = config.get('configurable', {}).get("model_name", "anthropic")
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-0-4)  model = _get_model(model_name)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-0-5)  response = model.invoke(messages)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-0-6)  # We return a list, because this will get added to the existing list
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-0-7)  return {"messages": [response]}

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-1-1)functioncallModel(state:State,config:RunnableConfig){
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-1-2)constmessages=state.messages;
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-1-3)constmodelName=config.configurable?.model_name??"anthropic";
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-1-4)constmodel=_getModel(modelName);
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-1-5)constresponse=model.invoke(messages);
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-1-6)// We return a list, because this will get added to the existing list
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-1-7)return{messages:[response]};
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-1-8)}

```


We are looking inside the config for a `model_name` parameter (which defaults to `anthropic` if none is found). That means that by default we are using Anthropic as our model provider. In this example we will see an example of how to create an example agent that is configured to use OpenAI.

First let's set up our client and thread:

[Python](#__tabbed_2_1)[Javascript](#__tabbed_2_2)[CURL](#__tabbed_2_3)

```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-2-1)fromlanggraph_sdkimport get_client
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-2-2)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-2-3)client = get_client(url=<DEPLOYMENT_URL>)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-2-4)# Select an assistant that is not configured
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-2-5)assistants = await client.assistants.search()
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-2-6)assistant = [a for a in assistants if not a["config"]][0]

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-3-1)import{Client}from"@langchain/langgraph-sdk";
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-3-2)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-3-3)constclient=newClient({apiUrl:<DEPLOYMENT_URL>});
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-3-4)// Select an assistant that is not configured
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-3-5)constassistants=awaitclient.assistants.search();
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-3-6)constassistant=assistants.find(a=>!a.config);

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-4-1)curl--requestPOST\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-4-2)--url<DEPLOYMENT_URL>/assistants/search\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-4-3)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-4-4)--data'{
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-4-5)    "limit": 10,
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-4-6)    "offset": 0
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-4-7)  }'|jq-c'map(select(.config == null or .config == {})) | .[0]'

```


We can now call `.get_schemas` to get schemas associated with this graph:

[Python](#__tabbed_3_1)[Javascript](#__tabbed_3_2)[CURL](#__tabbed_3_3)

```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-5-1)schemas = await client.assistants.get_schemas(
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-5-2)  assistant_id=assistant["assistant_id"]
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-5-3))
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-5-4)# There are multiple types of schemas
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-5-5)# We can get the `config_schema` to look at the configurable parameters
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-5-6)print(schemas["config_schema"])

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-6-1)constschemas=awaitclient.assistants.getSchemas(
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-6-2)assistant["assistant_id"]
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-6-3));
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-6-4)// There are multiple types of schemas
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-6-5)// We can get the `config_schema` to look at the configurable parameters
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-6-6)console.log(schemas.config_schema);

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-7-1)curl--requestGET\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-7-2)--url<DEPLOYMENT_URL>/assistants/<ASSISTANT_ID>/schemas|jq-r'.config_schema'

```


Output:

```
{
  'model_name': 
    {
      'title': 'Model Name',
      'enum': ['anthropic', 'openai'],
      'type': 'string'
    }
}

```


Now we can initialize an assistant with config:

[Python](#__tabbed_4_1)[Javascript](#__tabbed_4_2)[CURL](#__tabbed_4_3)

```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-8-1)openai_assistant = await client.assistants.create(
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-8-2)  # "agent" is the name of a graph we deployed
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-8-3)  "agent", config={"configurable": {"model_name": "openai"}}
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-8-4))
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-8-5)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-8-6)print(openai_assistant)

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-9-1)letopenAIAssistant=awaitclient.assistants.create(
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-9-2)// "agent" is the name of a graph we deployed
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-9-3)"agent",{"configurable":{"model_name":"openai"}}
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-9-4));
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-9-5)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-9-6)console.log(openAIAssistant);

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-10-1)curl--requestPOST\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-10-2)--url<DEPLOYMENT_URL>/assistants\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-10-3)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-10-4)--data'{"graph_id":"agent","config":{"configurable":{"model_name":"open_ai"}}}'

```


Output:

```
{
  "assistant_id": "62e209ca-9154-432a-b9e9-2d75c7a9219b",
  "graph_id": "agent",
  "created_at": "2024-08-31T03:09:10.230718+00:00",
  "updated_at": "2024-08-31T03:09:10.230718+00:00",
  "config": {
    "configurable": {
      "model_name": "open_ai"
    }
  },
  "metadata": {}
}

```


We can verify the config is indeed taking effect:

[Python](#__tabbed_5_1)[Javascript](#__tabbed_5_2)[CURL](#__tabbed_5_3)

```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-11-1)thread = await client.threads.create()
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-11-2)input = {"messages": [{"role": "user", "content": "who made you?"}]}
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-11-3)async for event in client.runs.stream(
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-11-4)  thread["thread_id"],
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-11-5)  openai_assistant["assistant_id"],
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-11-6)  input=input,
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-11-7)  stream_mode="updates",
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-11-8)):
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-11-9)  print(f"Receiving event of type: {event.event}")
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-11-10)  print(event.data)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-11-11)  print("\n\n")

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-12-1)constthread=awaitclient.threads.create();
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-12-2)letinput={"messages":[{"role":"user","content":"who made you?"}]};
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-12-3)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-12-4)conststreamResponse=client.runs.stream(
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-12-5)thread["thread_id"],
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-12-6)openAIAssistant["assistant_id"],
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-12-7){
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-12-8)input,
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-12-9)streamMode:"updates"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-12-10)}
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-12-11));
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-12-12)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-12-13)forawait(consteventofstreamResponse){
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-12-14)console.log(`Receiving event of type: ${event.event}`);
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-12-15)console.log(event.data);
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-12-16)console.log("\n\n");
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-12-17)}

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-13-1)thread_id=$(curl--requestPOST\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-13-2)--url<DEPLOYMENT_URL>/threads\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-13-3)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-13-4)--data'{}'|jq-r'.thread_id')&&\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-13-5)curl--requestPOST\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-13-6)--url"<DEPLOYMENT_URL>/threads/${thread_id}/runs/stream"\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-13-7)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-13-8)--data'{
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-13-9)    "assistant_id": <OPENAI_ASSISTANT_ID>,
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-13-10)    "input": {
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-13-11)      "messages": [
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-13-12)        {
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-13-13)          "role": "user",
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-13-14)          "content": "who made you?"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-13-15)        }
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-13-16)      ]
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-13-17)    },
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-13-18)    "stream_mode": [
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-13-19)      "updates"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-13-20)    ]
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-13-21)  }'|\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-13-22)sed's/\r$//'|\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-13-23)awk'
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-13-24)  /^event:/ {
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-13-25)    if (data_content != "") {
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-13-26)      print data_content "\n"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-13-27)    }
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-13-28)    sub(/^event: /, "Receiving event of type: ", $0)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-13-29)    printf "%s...\n", $0
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-13-30)    data_content = ""
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-13-31)  }
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-13-32)  /^data:/ {
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-13-33)    sub(/^data: /, "", $0)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-13-34)    data_content = $0
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-13-35)  }
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-13-36)  END {
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-13-37)    if (data_content != "") {
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-13-38)      print data_content "\n\n"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-13-39)    }
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-13-40)  }
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__codelineno-13-41)'

```


Output:

```
Receiving event of type: metadata
{'run_id': '1ef6746e-5893-67b1-978a-0f1cd4060e16'}

Receiving event of type: updates
{'agent': {'messages': [{'content': 'I was created by OpenAI, a research organization focused on developing and advancing artificial intelligence technology.', 'additional_kwargs': {}, 'response_metadata': {'finish_reason': 'stop', 'model_name': 'gpt-4o-2024-05-13', 'system_fingerprint': 'fp_157b3831f5'}, 'type': 'ai', 'name': None, 'id': 'run-e1a6b25c-8416-41f2-9981-f9cfe043f414', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}]}}

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to interact with the deployment using RemoteGraph  ](https://langchain-ai.github.io/langgraph/how-tos/use-remote-graph/) [ Next  How to version assistants  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
