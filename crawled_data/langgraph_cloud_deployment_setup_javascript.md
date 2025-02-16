---
url: https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#how-to-set-up-a-langgraphjs-application-for-deployment)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to Set Up a LangGraph.js Application for Deployment 

[ ](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/?q= "Share")

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
            * How to Set Up a LangGraph.js Application for Deployment  [ How to Set Up a LangGraph.js Application for Deployment  ](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/) Table of contents 
              * [ Specify Dependencies  ](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#specify-dependencies)
              * [ Specify Environment Variables  ](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#specify-environment-variables)
              * [ Define Graphs  ](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#define-graphs)
              * [ Create LangGraph API Config  ](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#create-langgraph-api-config)
              * [ Next  ](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#next)
            * [ How to add semantic search to your LangGraph deployment  ](https://langchain-ai.github.io/langgraph/cloud/deployment/semantic_search/)
            * [ How to customize Dockerfile  ](https://langchain-ai.github.io/langgraph/cloud/deployment/custom_docker/)
            * [ How to test a LangGraph app locally  ](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/)
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

  * [ Specify Dependencies  ](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#specify-dependencies)
  * [ Specify Environment Variables  ](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#specify-environment-variables)
  * [ Define Graphs  ](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#define-graphs)
  * [ Create LangGraph API Config  ](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#create-langgraph-api-config)
  * [ Next  ](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#next)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph-platform)
  5. [ Application Structure  ](https://langchain-ai.github.io/langgraph/how-tos#application-structure)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/cloud/deployment/setup_javascript.md "Edit this page")

# How to Set Up a LangGraph.js Application for Deployment[¶](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#how-to-set-up-a-langgraphjs-application-for-deployment "Permanent link")

A [LangGraph.js](https://langchain-ai.github.io/langgraphjs/) application must be configured with a [LangGraph API configuration file](https://langchain-ai.github.io/langgraph/cloud/reference/cli/#configuration-file) in order to be deployed to LangGraph Cloud (or to be self-hosted). This how-to guide discusses the basic steps to setup a LangGraph.js application for deployment using `package.json` to specify project dependencies.

This walkthrough is based on [this repository](https://github.com/langchain-ai/langgraphjs-studio-starter), which you can play around with to learn more about how to setup your LangGraph application for deployment.

The final repo structure will look something like this:

```
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-0-1)my-app/
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-0-2)├──src# all project code lies within here
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-0-3)│├──utils# optional utilities for your graph
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-0-4)││├──tools.ts# tools for your graph
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-0-5)││├──nodes.ts# node functions for you graph
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-0-6)││└──state.ts# state definition of your graph
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-0-7)│└──agent.ts# code for constructing your graph
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-0-8)├──package.json# package dependencies
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-0-9)├──.env# environment variables
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-0-10)└──langgraph.json# configuration file for LangGraph

```


After each step, an example file directory is provided to demonstrate how code can be organized.

## Specify Dependencies[¶](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#specify-dependencies "Permanent link")

Dependencies can be specified in a `package.json`. If none of these files is created, then dependencies can be specified later in the [LangGraph API configuration file](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#create-langgraph-api-config).

Example `package.json` file:

```
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-1-1){
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-1-2)"name":"langgraphjs-studio-starter",
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-1-3)"packageManager":"yarn@1.22.22",
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-1-4)"dependencies":{
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-1-5)"@langchain/community":"^0.2.31",
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-1-6)"@langchain/core":"^0.2.31",
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-1-7)"@langchain/langgraph":"^0.2.0",
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-1-8)"@langchain/openai":"^0.2.8"
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-1-9)}
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-1-10)}

```


Example file directory:

```
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-2-1)my-app/
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-2-2)└──package.json# package dependencies

```


## Specify Environment Variables[¶](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#specify-environment-variables "Permanent link")

Environment variables can optionally be specified in a file (e.g. `.env`). See the [Environment Variables reference](https://langchain-ai.github.io/langgraph/cloud/reference/env_var/) to configure additional variables for a deployment.

Example `.env` file:

```
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-3-1)MY_ENV_VAR_1=foo
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-3-2)MY_ENV_VAR_2=bar
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-3-3)OPENAI_API_KEY=key
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-3-4)TAVILY_API_KEY=key_2

```


Example file directory:

```
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-4-1)my-app/
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-4-2)├──package.json
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-4-3)└──.env# environment variables

```


## Define Graphs[¶](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#define-graphs "Permanent link")

Implement your graphs! Graphs can be defined in a single file or multiple files. Make note of the variable names of each compiled graph to be included in the LangGraph application. The variable names will be used later when creating the [LangGraph API configuration file](https://langchain-ai.github.io/langgraph/cloud/reference/cli/#configuration-file).

Here is an example `agent.ts`:

```
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-1)importtype{AIMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-2)import{TavilySearchResults}from"@langchain/community/tools/tavily_search";
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-3)import{ChatOpenAI}from"@langchain/openai";
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-4)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-5)import{MessagesAnnotation,StateGraph}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-6)import{ToolNode}from"@langchain/langgraph/prebuilt";
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-7)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-8)consttools=[
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-9)newTavilySearchResults({maxResults:3,}),
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-10)];
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-11)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-12)// Define the function that calls the model
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-13)asyncfunctioncallModel(
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-14)state:typeofMessagesAnnotation.State,
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-15)){
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-16)/**
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-17)  * Call the LLM powering our agent.
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-18)  * Feel free to customize the prompt, model, and other logic!
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-19)  */
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-20)constmodel=newChatOpenAI({
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-21)model:"gpt-4o",
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-22)}).bindTools(tools);
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-23)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-24)constresponse=awaitmodel.invoke([
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-25){
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-26)role:"system",
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-27)content:`You are a helpful assistant. The current date is ${newDate().getTime()}.`
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-28)},
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-29)...state.messages
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-30)]);
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-31)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-32)// MessagesAnnotation supports returning a single message or array of messages
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-33)return{messages:response};
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-34)}
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-35)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-36)// Define the function that determines whether to continue or not
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-37)functionrouteModelOutput(state:typeofMessagesAnnotation.State){
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-38)constmessages=state.messages;
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-39)constlastMessage:AIMessage=messages[messages.length-1];
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-40)// If the LLM is invoking tools, route there.
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-41)if((lastMessage?.tool_calls?.length??0)>0){
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-42)return"tools";
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-43)}
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-44)// Otherwise end the graph.
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-45)return"__end__";
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-46)}
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-47)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-48)// Define a new graph.
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-49)// See https://langchain-ai.github.io/langgraphjs/how-tos/define-state/#getting-started for
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-50)// more on defining custom graph states.
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-51)constworkflow=newStateGraph(MessagesAnnotation)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-52)// Define the two nodes we will cycle between
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-53).addNode("callModel",callModel)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-54).addNode("tools",newToolNode(tools))
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-55)// Set the entrypoint as `callModel`
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-56)// This means that this node is the first one called
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-57).addEdge("__start__","callModel")
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-58).addConditionalEdges(
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-59)// First, we define the edges' source node. We use `callModel`.
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-60)// This means these are the edges taken after the `callModel` node is called.
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-61)"callModel",
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-62)// Next, we pass in the function that will determine the sink node(s), which
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-63)// will be called after the source node is called.
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-64)routeModelOutput,
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-65)// List of the possible destinations the conditional edge can route to.
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-66)// Required for conditional edges to properly render the graph in Studio
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-67)[
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-68)"tools",
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-69)"__end__"
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-70)],
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-71))
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-72)// This means that after `tools` is called, `callModel` node is called next.
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-73).addEdge("tools","callModel");
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-74)
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-75)// Finally, we compile it!
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-76)// This compiles it into a graph you can invoke and deploy.
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-5-77)exportconstgraph=workflow.compile();

```


Assign `CompiledGraph` to Variable

The build process for LangGraph Cloud requires that the `CompiledGraph` object be assigned to a variable at the top-level of a JavaScript module (alternatively, you can provide [a function that creates a graph](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/)).

Example file directory:

```
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-6-1)my-app/
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-6-2)├──src# all project code lies within here
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-6-3)│├──utils# optional utilities for your graph
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-6-4)││├──tools.ts# tools for your graph
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-6-5)││├──nodes.ts# node functions for you graph
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-6-6)││└──state.ts# state definition of your graph
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-6-7)│└──agent.ts# code for constructing your graph
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-6-8)├──package.json# package dependencies
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-6-9)├──.env# environment variables
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-6-10)└──langgraph.json# configuration file for LangGraph

```


## Create LangGraph API Config[¶](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#create-langgraph-api-config "Permanent link")

Create a [LangGraph API configuration file](https://langchain-ai.github.io/langgraph/cloud/reference/cli/#configuration-file) called `langgraph.json`. See the [LangGraph CLI reference](https://langchain-ai.github.io/langgraph/cloud/reference/cli/#configuration-file) for detailed explanations of each key in the JSON object of the configuration file.

Example `langgraph.json` file:

```
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-7-1){
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-7-2)"node_version":"20",
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-7-3)"dockerfile_lines":[],
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-7-4)"dependencies":["."],
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-7-5)"graphs":{
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-7-6)"agent":"./src/agent.ts:graph"
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-7-7)},
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-7-8)"env":".env"
[](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__codelineno-7-9)}

```


Note that the variable name of the `CompiledGraph` appears at the end of the value of each subkey in the top-level `graphs` key (i.e. `:<variable_name>`).

Configuration Location

The LangGraph API configuration file must be placed in a directory that is at the same level or higher than the TypeScript files that contain compiled graphs and associated dependencies.

## Next[¶](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#next "Permanent link")

After you setup your project and place it in a github repo, it's time to [deploy your app](https://langchain-ai.github.io/langgraph/cloud/deployment/cloud/).

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to Set Up a LangGraph Application for Deployment  ](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_pyproject/) [ Next  How to add semantic search to your LangGraph deployment  ](https://langchain-ai.github.io/langgraph/cloud/deployment/semantic_search/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
