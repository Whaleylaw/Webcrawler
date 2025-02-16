---
url: https://langchain-ai.github.io/langgraphjs/how-tos/node-retry-policies/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/node-retry-policies/#how-to-add-node-retry-policies)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to add node retry policies 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/node-retry-policies/?q= "Share")

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
        * LangGraph  LangGraph 
          * [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
          * [ Controllability  ](https://langchain-ai.github.io/langgraphjs/how-tos#controllability)
          * [ Persistence  ](https://langchain-ai.github.io/langgraphjs/how-tos#persistence)
          * [ Memory  ](https://langchain-ai.github.io/langgraphjs/how-tos#memory)
          * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraphjs/how-tos#human-in-the-loop)
          * [ Streaming  ](https://langchain-ai.github.io/langgraphjs/how-tos#streaming)
          * [ Tool calling  ](https://langchain-ai.github.io/langgraphjs/how-tos#tool-calling)
          * [ Subgraphs  ](https://langchain-ai.github.io/langgraphjs/how-tos#subgraphs)
          * [ Multi-agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/)
          * [ State Management  ](https://langchain-ai.github.io/langgraphjs/how-tos#state-management)
          * Other  Other 
            * [ Other  ](https://langchain-ai.github.io/langgraphjs/how-tos#other)
            * [ How to add runtime configuration to your graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/)
            * How to add node retry policies  [ How to add node retry policies  ](https://langchain-ai.github.io/langgraphjs/how-tos/node-retry-policies/) Table of contents 
              * [ Passing a retry policy to a node  ](https://langchain-ai.github.io/langgraphjs/how-tos/node-retry-policies/#passing-a-retry-policy-to-a-node)
            * [ How to let agent return tool results directly  ](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/)
            * [ How to have agent respond in structured format  ](https://langchain-ai.github.io/langgraphjs/how-tos/respond-in-format/)
            * [ How to manage agent steps  ](https://langchain-ai.github.io/langgraphjs/how-tos/managing-agent-steps/)
          * [ Prebuilt ReAct Agent  ](https://langchain-ai.github.io/langgraphjs/how-tos#prebuilt-react-agent)
        * [ LangGraph Platform  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph-platform)
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

  * [ Passing a retry policy to a node  ](https://langchain-ai.github.io/langgraphjs/how-tos/node-retry-policies/#passing-a-retry-policy-to-a-node)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
  5. [ Other  ](https://langchain-ai.github.io/langgraphjs/how-tos#other)



# How to add node retry policies[¶](https://langchain-ai.github.io/langgraphjs/how-tos/node-retry-policies/#how-to-add-node-retry-policies "Permanent link")

There are many use cases where you may wish for your node to have a custom retry policy. Some examples of when you may wish to do this is if you are calling an API, querying a database, or calling an LLM, etc. 

In order to configure the retry policy, you have to pass the `retryPolicy` parameter to the `addNode` function. The `retryPolicy` parameter takes in a `RetryPolicy` named tuple object. Below we instantiate a `RetryPolicy` object with the default parameters:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/node-retry-policies/#__codelineno-0-1)import{RetryPolicy}from"@langchain/langgraph"
[](https://langchain-ai.github.io/langgraphjs/how-tos/node-retry-policies/#__codelineno-0-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/node-retry-policies/#__codelineno-0-3)constretryPolicy:RetryPolicy={};

```


If you want more information on what each of the parameters does, be sure to read the [reference](https://langchain-ai.github.io/langgraphjs/reference/types/langgraph.RetryPolicy.html).

## Passing a retry policy to a node[¶](https://langchain-ai.github.io/langgraphjs/how-tos/node-retry-policies/#passing-a-retry-policy-to-a-node "Permanent link")

Lastly, we can pass `RetryPolicy` objects when we call the `addNode` function. In the example below we pass two different retry policies to each of our nodes:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/node-retry-policies/#__codelineno-1-1)importDatabasefrom"better-sqlite3"
[](https://langchain-ai.github.io/langgraphjs/how-tos/node-retry-policies/#__codelineno-1-2)import{ChatAnthropic}from"@langchain/anthropic"
[](https://langchain-ai.github.io/langgraphjs/how-tos/node-retry-policies/#__codelineno-1-3)import{MessagesAnnotation,StateGraph,START,END}from"@langchain/langgraph"
[](https://langchain-ai.github.io/langgraphjs/how-tos/node-retry-policies/#__codelineno-1-4)import{AIMessage}from"@langchain/core/messages"
[](https://langchain-ai.github.io/langgraphjs/how-tos/node-retry-policies/#__codelineno-1-5)
[](https://langchain-ai.github.io/langgraphjs/how-tos/node-retry-policies/#__codelineno-1-6)// Create an in-memory database
[](https://langchain-ai.github.io/langgraphjs/how-tos/node-retry-policies/#__codelineno-1-7)constdb:typeofDatabase.prototype=newDatabase(':memory:');
[](https://langchain-ai.github.io/langgraphjs/how-tos/node-retry-policies/#__codelineno-1-8)
[](https://langchain-ai.github.io/langgraphjs/how-tos/node-retry-policies/#__codelineno-1-9)constmodel=newChatAnthropic({model:"claude-3-5-sonnet-20240620"});
[](https://langchain-ai.github.io/langgraphjs/how-tos/node-retry-policies/#__codelineno-1-10)
[](https://langchain-ai.github.io/langgraphjs/how-tos/node-retry-policies/#__codelineno-1-11)constcallModel=async(state:typeofMessagesAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/node-retry-policies/#__codelineno-1-12)constresponse=awaitmodel.invoke(state.messages);
[](https://langchain-ai.github.io/langgraphjs/how-tos/node-retry-policies/#__codelineno-1-13)return{messages:[response]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/node-retry-policies/#__codelineno-1-14)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/node-retry-policies/#__codelineno-1-15)
[](https://langchain-ai.github.io/langgraphjs/how-tos/node-retry-policies/#__codelineno-1-16)constqueryDatabase=async(state:typeofMessagesAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/node-retry-policies/#__codelineno-1-17)constqueryResult:string=JSON.stringify(db.prepare("SELECT * FROM Artist LIMIT 10;").all());
[](https://langchain-ai.github.io/langgraphjs/how-tos/node-retry-policies/#__codelineno-1-18)
[](https://langchain-ai.github.io/langgraphjs/how-tos/node-retry-policies/#__codelineno-1-19)return{messages:[newAIMessage({content:"queryResult"})]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/node-retry-policies/#__codelineno-1-20)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/node-retry-policies/#__codelineno-1-21)
[](https://langchain-ai.github.io/langgraphjs/how-tos/node-retry-policies/#__codelineno-1-22)constworkflow=newStateGraph(MessagesAnnotation)
[](https://langchain-ai.github.io/langgraphjs/how-tos/node-retry-policies/#__codelineno-1-23)// Define the two nodes we will cycle between
[](https://langchain-ai.github.io/langgraphjs/how-tos/node-retry-policies/#__codelineno-1-24).addNode("call_model",callModel,{retryPolicy:{maxAttempts:5}})
[](https://langchain-ai.github.io/langgraphjs/how-tos/node-retry-policies/#__codelineno-1-25).addNode("query_database",queryDatabase,{retryPolicy:{retryOn:(e:any):boolean=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/node-retry-policies/#__codelineno-1-26)if(einstanceofDatabase.SqliteError){
[](https://langchain-ai.github.io/langgraphjs/how-tos/node-retry-policies/#__codelineno-1-27)// Retry on "SQLITE_BUSY" error
[](https://langchain-ai.github.io/langgraphjs/how-tos/node-retry-policies/#__codelineno-1-28)returne.code==='SQLITE_BUSY';
[](https://langchain-ai.github.io/langgraphjs/how-tos/node-retry-policies/#__codelineno-1-29)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/node-retry-policies/#__codelineno-1-30)returnfalse;// Don't retry on other errors
[](https://langchain-ai.github.io/langgraphjs/how-tos/node-retry-policies/#__codelineno-1-31)}}})
[](https://langchain-ai.github.io/langgraphjs/how-tos/node-retry-policies/#__codelineno-1-32).addEdge(START,"call_model")
[](https://langchain-ai.github.io/langgraphjs/how-tos/node-retry-policies/#__codelineno-1-33).addEdge("call_model","query_database")
[](https://langchain-ai.github.io/langgraphjs/how-tos/node-retry-policies/#__codelineno-1-34).addEdge("query_database",END);
[](https://langchain-ai.github.io/langgraphjs/how-tos/node-retry-policies/#__codelineno-1-35)
[](https://langchain-ai.github.io/langgraphjs/how-tos/node-retry-policies/#__codelineno-1-36)constgraph=workflow.compile();

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to add runtime configuration to your graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/) [ Next  How to let agent return tool results directly  ](https://langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/node-retry-policies/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
