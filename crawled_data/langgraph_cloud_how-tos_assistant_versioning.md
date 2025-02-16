---
url: https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#how-to-version-assistants)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to version assistants 

[ ](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/?q= "Share")

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
            * How to version assistants  [ How to version assistants  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#setup)
              * [ Create an assistant  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#create-an-assistant)
                * [ Using the studio  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#using-the-studio)
              * [ Create a new version for your assistant  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#create-a-new-version-for-your-assistant)
                * [ Using the studio  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#using-the-studio_1)
              * [ Point your assistant to a different version  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#point-your-assistant-to-a-different-version)
                * [ Using the studio  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#using-the-studio_2)
              * [ Using your assistant versions  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#using-your-assistant-versions)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#setup)
  * [ Create an assistant  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#create-an-assistant)
    * [ Using the studio  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#using-the-studio)
  * [ Create a new version for your assistant  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#create-a-new-version-for-your-assistant)
    * [ Using the studio  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#using-the-studio_1)
  * [ Point your assistant to a different version  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#point-your-assistant-to-a-different-version)
    * [ Using the studio  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#using-the-studio_2)
  * [ Using your assistant versions  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#using-your-assistant-versions)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph-platform)
  5. [ Assistants  ](https://langchain-ai.github.io/langgraph/how-tos#assistants)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/cloud/how-tos/assistant_versioning.md "Edit this page")

# How to version assistants[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#how-to-version-assistants "Permanent link")

In this how-to guide we will walk through how you can create and manage different assistant versions. If you haven't already, you can read [this](https://langchain-ai.github.io/langgraph/concepts/assistants/#versioning-assistants) conceptual guide to gain a better understanding of what assistant versioning is. This how-to assumes you have a graph that is configurable, which means you have defined a config schema and passed it to your graph as follows:

[Python](#__tabbed_1_1)[Javascript](#__tabbed_1_2)

```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#__codelineno-0-1)classConfig(BaseModel):
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#__codelineno-0-2)  model_name: Literal["anthropic", "openai"] = "anthropic"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#__codelineno-0-3)  system_prompt: str
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#__codelineno-0-4)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#__codelineno-0-5)agent = StateGraph(State, config_schema=Config)

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#__codelineno-1-1)constConfigAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#__codelineno-1-2)modelName:Annotation<z.enum(["openai","anthropic"])>({
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#__codelineno-1-3)default:()=>"anthropic",
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#__codelineno-1-4)}),
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#__codelineno-1-5)systemPrompt:Annotation<String>
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#__codelineno-1-6)});
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#__codelineno-1-7)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#__codelineno-1-8)// the rest of your code
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#__codelineno-1-10)constagent=newStateGraph(StateAnnotation,ConfigAnnotation);

```


## Setup[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#setup "Permanent link")

First let's set up our client and thread. If you are using the Studio, just open the application to the graph called "agent". If using cURL, you don't need to do anything except copy down your deployment URL and the name of the graph you want to use.

[Python](#__tabbed_2_1)[Javascript](#__tabbed_2_2)

```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#__codelineno-2-1)fromlanggraph_sdkimport get_client
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#__codelineno-2-2)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#__codelineno-2-3)client = get_client(url=<DEPLOYMENT_URL>)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#__codelineno-2-4)# Using the graph deployed with the name "agent"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#__codelineno-2-5)graph_name = "agent"

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#__codelineno-3-1)import{Client}from"@langchain/langgraph-sdk";
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#__codelineno-3-2)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#__codelineno-3-3)constclient=newClient({apiUrl:<DEPLOYMENT_URL>});
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#__codelineno-3-4)// Using the graph deployed with the name "agent"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#__codelineno-3-5)constgraphName="agent";

```


## Create an assistant[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#create-an-assistant "Permanent link")

For this example, we will create an assistant by modifying the model name that is used in our graph. We can create a new assistant called "openai_assistant" for this:

[Python](#__tabbed_3_1)[Javascript](#__tabbed_3_2)[CURL](#__tabbed_3_3)

```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#__codelineno-4-1)openai_assistant = await client.assistants.create(graph_name, config={"configurable": {"model_name": "openai"}}, name="openai_assistant")

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#__codelineno-5-1)constopenaiAssistant=awaitclient.assistants.create({graphId:graphName,config:{configurable:{"modelName":"openai"}},name:"openaiAssistant"});

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#__codelineno-6-1)curl--requestPOST\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#__codelineno-6-2)--url<DEPOLYMENT_URL>/assistants\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#__codelineno-6-3)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#__codelineno-6-4)--data'{
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#__codelineno-6-5)"graph_id": "agent",
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#__codelineno-6-6)"config": {"model_name": "openai"},
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#__codelineno-6-7)"name": "openai_assistant"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#__codelineno-6-8)}'

```


### Using the studio[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#using-the-studio "Permanent link")

To create an assistant using the studio do the following steps:

  1. Click on the "Create New Assistant" button:

![click create](https://langchain-ai.github.io/langgraph/cloud/how-tos/img/click_create_assistant.png)

  2. Use the create assistant pane to enter info for the assistant you wish to create, and then click create:

![create](https://langchain-ai.github.io/langgraph/cloud/how-tos/img/create_assistant.png)

  3. See that your assistant was created and is displayed in the Studio

![view create](https://langchain-ai.github.io/langgraph/cloud/how-tos/img/create_assistant_view.png)

  4. Click on the edit button next to the selected assistant to manage your created assistant:

![create edit](https://langchain-ai.github.io/langgraph/cloud/how-tos/img/edit_created_assistant.png)




## Create a new version for your assistant[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#create-a-new-version-for-your-assistant "Permanent link")

Let's now say we wanted to add a system prompt to our assistant. We can do this by using the `update` endpoint as follows. Please note that you must pass in the ENTIRE config (and metadata if you are using it). The update endpoint creates new versions completely from scratch and does not rely on previously entered config. In this case, we need to continue telling the assistant to use "openai" as the model.

[Python](#__tabbed_4_1)[Javascript](#__tabbed_4_2)[CURL](#__tabbed_4_3)

```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#__codelineno-7-1)openai_assistant_v2 = await client.assistants.update(openai_assistant['assistant_id'], config={"configurable": {"model_name": "openai", "system_prompt": "You are a helpful assistant!"}})

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#__codelineno-8-1)constopenaiAssistantV2=awaitclient.assistants.update(openaiAssistant['assistant_id'],{config:{configurable:{"modelName":"openai","systemPrompt":"You are a helpful assistant!"}}});

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#__codelineno-9-1)curl--requestPATCH\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#__codelineno-9-2)--url<DEPOLYMENT_URL>/assistants/<ASSISTANT_ID>\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#__codelineno-9-3)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#__codelineno-9-4)--data'{
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#__codelineno-9-5)"config": {"model_name": "openai", "system_prompt": "You are a helpful assistant!"}
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#__codelineno-9-6)}'

```


### Using the studio[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#using-the-studio_1 "Permanent link")

  1. First, click on the edit button next to the `openai_assistant`. Then, add a system prompt and click "Save New Version":

![create new version](https://langchain-ai.github.io/langgraph/cloud/how-tos/img/create_new_version.png)

  2. Then you can see it is selected in the assistant dropdown:

![see version dropdown](https://langchain-ai.github.io/langgraph/cloud/how-tos/img/see_new_version.png)

  3. And you can see all the version history in the edit pane for the assistant:

![see versions](https://langchain-ai.github.io/langgraph/cloud/how-tos/img/see_version_history.png)




## Point your assistant to a different version[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#point-your-assistant-to-a-different-version "Permanent link")

After having created multiple versions, we can change the version our assistant points to both by using the SDK and also the Studio. In this case we will be resetting the `openai_assistant` we just created two versions for to point back to the first version. When you create a new version (by using the `update` endpoint) the assistant automatically points to the newly created version, so following the code above our `openai_assistant` is pointing to the second version. Here we will change it to point to the first version:

[Python](#__tabbed_5_1)[Javascript](#__tabbed_5_2)[CURL](#__tabbed_5_3)

```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#__codelineno-10-1)await client.assistants.set_latest(openai_assistant['assistant_id'], 1)

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#__codelineno-11-1)awaitclient.assistants.setLatest(openaiAssistant['assistant_id'],1);

```


```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#__codelineno-12-1)curl--requestPOST\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#__codelineno-12-2)--url<DEPLOYMENT_URL>/assistants/<ASSISTANT_ID>/latest\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#__codelineno-12-3)--header'Content-Type: application/json'\
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#__codelineno-12-4)--data'{
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#__codelineno-12-5)"version": 1
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#__codelineno-12-6)}'

```


### Using the studio[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#using-the-studio_2 "Permanent link")

To change the version, all you have to do is click into the edit pane for an assistant, select the version you want to change to, and then click the "Set As Current Version" button

![set version](https://langchain-ai.github.io/langgraph/cloud/how-tos/img/select_different_version.png)

## Using your assistant versions[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#using-your-assistant-versions "Permanent link")

Whether you are a business user iterating without writing code, or a developer using the SDK - assistant versioning allows you to quickly test different agents in a controlled environment, making it easy to iterate fast. You can use any of the assistant versions just how you would a normal assistant, and can read more about how to stream output from these assistants by reading [these guides](https://langchain-ai.github.io/langgraph/cloud/how-tos/#streaming) or [this one](https://langchain-ai.github.io/langgraph/cloud/how-tos/invoke_studio/) if you are using the Studio.

Deleting Assistants

Deleting as assistant will delete ALL of it's versions, since they all point to the same assistant ID. There is currently no way to just delete a single version, but by pointing your assistant to the correct version you can skip any versions that you don't wish to use.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to create agents with configuration  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/) [ Next  Copying Threads  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/copy_threads/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/cloud/how-tos/assistant_versioning/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
