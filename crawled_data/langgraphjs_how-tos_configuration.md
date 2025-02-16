---
url: https://langchain-ai.github.io/langgraphjs/how-tos/configuration/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#how-to-add-runtime-configuration-to-your-graph)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to add runtime configuration to your graph 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/?q= "Share")

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
            * How to add runtime configuration to your graph  [ How to add runtime configuration to your graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#setup)
              * [ Define the graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#define-the-graph)
              * [ Call with config  ](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#call-with-config)
              * [ Change the config  ](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#change-the-config)
              * [ Config schema  ](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#config-schema)
            * [ How to add node retry policies  ](https://langchain-ai.github.io/langgraphjs/how-tos/node-retry-policies/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#setup)
  * [ Define the graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#define-the-graph)
  * [ Call with config  ](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#call-with-config)
  * [ Change the config  ](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#change-the-config)
  * [ Config schema  ](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#config-schema)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
  5. [ Other  ](https://langchain-ai.github.io/langgraphjs/how-tos#other)



# How to add runtime configuration to your graph[¶](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#how-to-add-runtime-configuration-to-your-graph "Permanent link")

Once you've created an app in LangGraph, you likely will want to permit configuration at runtime.

For instance, you may want to let the LLM or prompt be selected dynamically, configure a user's `user_id` to enforce row-level security, etc.

In LangGraph, configuration and other ["out-of-band" communication](https://en.wikipedia.org/wiki/Out-of-band) is done via the [RunnableConfig](https://v02.api.js.langchain.com/interfaces/langchain_core_runnables.RunnableConfig.html), which is always the second positional arg when invoking your application.

Below, we walk through an example of letting you configure a user ID and pick which model to use.

## Setup[¶](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#setup "Permanent link")

This guide will use Anthropic's Claude 3 Haiku and OpenAI's GPT-4o model. We will optionally set our API key for [LangSmith tracing](https://smith.langchain.com/), which will give us best-in-class observability.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-0-1)// process.env.OPENAI_API_KEY = "sk_...";
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-0-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-0-3)// Optional, add tracing in LangSmith
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-0-4)// process.env.LANGCHAIN_API_KEY = "ls__...";
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-0-5)// process.env.LANGCHAIN_CALLBACKS_BACKGROUND = "true";
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-0-6)process.env.LANGCHAIN_TRACING_V2="true";
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-0-7)process.env.LANGCHAIN_PROJECT="Configuration: LangGraphJS";

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-1-1)Configuration: LangGraphJS

```


## Define the graph[¶](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#define-the-graph "Permanent link")

We will create an exceedingly simple message graph for this example.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-1)import{BaseMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-2)import{ChatOpenAI}from"@langchain/openai";
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-3)import{ChatAnthropic}from"@langchain/anthropic";
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-4)import{ChatPromptTemplate}from"@langchain/core/prompts";
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-5)import{RunnableConfig}from"@langchain/core/runnables";
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-6)import{
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-7)END,
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-8)START,
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-9)StateGraph,
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-10)Annotation,
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-11)}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-12)
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-13)constAgentState=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-14)messages:Annotation<BaseMessage[]>({
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-15)reducer:(x,y)=>x.concat(y),
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-16)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-17)userInfo:Annotation<string|undefined>({
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-18)reducer:(x,y)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-19)returny?y:x?x:"N/A";
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-20)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-21)default:()=>"N/A",
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-22)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-23)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-24)
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-25)constpromptTemplate=ChatPromptTemplate.fromMessages([
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-26)["system","You are a helpful assistant.\n\n## User Info:\n{userInfo}"],
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-27)["placeholder","{messages}"],
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-28)]);
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-29)
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-30)constcallModel=async(
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-31)state:typeofAgentState.State,
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-32)config?:RunnableConfig,
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-33))=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-34)const{messages,userInfo}=state;
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-35)constmodelName=config?.configurable?.model;
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-36)constmodel=modelName==="claude"
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-37)?newChatAnthropic({model:"claude-3-haiku-20240307"})
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-38):newChatOpenAI({model:"gpt-4o"});
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-39)constchain=promptTemplate.pipe(model);
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-40)constresponse=awaitchain.invoke(
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-41){
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-42)messages,
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-43)userInfo,
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-44)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-45)config,
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-46));
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-47)return{messages:[response]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-48)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-49)
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-50)constfetchUserInformation=async(
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-51)_:typeofAgentState.State,
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-52)config?:RunnableConfig,
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-53))=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-54)constuserDB={
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-55)user1:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-56)name:"John Doe",
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-57)email:"jod@langchain.ai",
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-58)phone:"+1234567890",
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-59)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-60)user2:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-61)name:"Jane Doe",
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-62)email:"jad@langchain.ai",
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-63)phone:"+0987654321",
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-64)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-65)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-66)constuserId=config?.configurable?.user;
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-67)if(userId){
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-68)constuser=userDB[userIdaskeyoftypeofuserDB];
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-69)if(user){
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-70)return{
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-71)userInfo:
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-72)`Name: ${user.name}\nEmail: ${user.email}\nPhone: ${user.phone}`,
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-73)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-74)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-75)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-76)return{userInfo:"N/A"};
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-77)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-78)
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-79)constworkflow=newStateGraph(AgentState)
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-80).addNode("fetchUserInfo",fetchUserInformation)
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-81).addNode("agent",callModel)
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-82).addEdge(START,"fetchUserInfo")
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-83).addEdge("fetchUserInfo","agent")
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-84).addEdge("agent",END);
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-85)
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-2-86)constgraph=workflow.compile();

```


## Call with config[¶](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#call-with-config "Permanent link")

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-3-1)import{HumanMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-3-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-3-3)constconfig={
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-3-4)configurable:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-3-5)model:"openai",
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-3-6)user:"user1",
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-3-7)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-3-8)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-3-9)constinputs={
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-3-10)messages:[newHumanMessage("Could you remind me of my email??")],
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-3-11)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-3-12)forawait(
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-3-13)const{messages}ofawaitgraph.stream(inputs,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-3-14)...config,
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-3-15)streamMode:"values",
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-3-16)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-3-17)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-3-18)letmsg=messages[messages?.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-3-19)if(msg?.content){
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-3-20)console.log(msg.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-3-21)}elseif(msg?.tool_calls?.length>0){
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-3-22)console.log(msg.tool_calls);
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-3-23)}else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-3-24)console.log(msg);
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-3-25)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-3-26)console.log("-----\n");
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-3-27)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-4-1)Could you remind me of my email??
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-4-2)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-4-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-4-4)Could you remind me of my email??
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-4-5)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-4-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-4-7)Your email is jod@langchain.ai.
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-4-8)-----

```


## Change the config[¶](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#change-the-config "Permanent link")

Now let's try the same input with a different user.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-5-1)constconfig2={
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-5-2)configurable:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-5-3)model:"openai",
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-5-4)user:"user2",
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-5-5)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-5-6)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-5-7)constinputs2={
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-5-8)messages:[newHumanMessage("Could you remind me of my email??")],
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-5-9)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-5-10)forawait(
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-5-11)const{messages}ofawaitgraph.stream(inputs2,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-5-12)...config2,
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-5-13)streamMode:"values",
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-5-14)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-5-15)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-5-16)letmsg=messages[messages?.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-5-17)if(msg?.content){
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-5-18)console.log(msg.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-5-19)}elseif(msg?.tool_calls?.length>0){
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-5-20)console.log(msg.tool_calls);
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-5-21)}else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-5-22)console.log(msg);
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-5-23)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-5-24)console.log("-----\n");
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-5-25)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-6-1)Could you remind me of my email??
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-6-2)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-6-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-6-4)Could you remind me of my email??
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-6-5)-----
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-6-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-6-7)Your email address is jad@langchain.ai.
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-6-8)-----

```


Check out the [LangSmith Trace (link)](https://smith.langchain.com/public/bbd3561f-c0d1-4886-ae18-a6626c6b8670/r/946098b5-84d3-4456-a03c-5dbc8591e76b) for this run to "see what the LLM sees". 

## Config schema[¶](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#config-schema "Permanent link")

You can also pass an annotation defining the shape of `config.configurable` into your graph. This will currently only expose type information on the compiled graph, and will not filter out keys:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-7-1)import{MessagesAnnotation}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-7-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-7-3)constConfigurableAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-7-4)expectedField:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-7-5)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-7-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-7-7)constprintNode=async(
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-7-8)state:typeofMessagesAnnotation.State,
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-7-9)config:RunnableConfig<typeofConfigurableAnnotation.State>
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-7-10))=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-7-11)console.log("Expected",config.configurable?.expectedField);
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-7-12)// @ts-expect-error This type will be present even though is not in the typing
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-7-13)console.log("Unexpected",config.configurable?.unexpectedField);
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-7-14)return{};
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-7-15)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-7-16)
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-7-17)constgraphWithConfigSchema=newStateGraph(MessagesAnnotation,ConfigurableAnnotation)
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-7-18).addNode("printNode",printNode)
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-7-19).addEdge(START,"printNode")
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-7-20).compile();
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-7-21)
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-7-22)constresult=awaitgraphWithConfigSchema.invoke({
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-7-23)messages:[{role:"user",content:"Echo!"}]
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-7-24)},{configurable:{expectedField:"I am expected",unexpectedField:"I am unexpected but present"}});

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-8-1)Expected I am expected
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-8-2)Unexpected I am unexpected but present

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__codelineno-9-1)

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to pass private state  ](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/) [ Next  How to add node retry policies  ](https://langchain-ai.github.io/langgraphjs/how-tos/node-retry-policies/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
