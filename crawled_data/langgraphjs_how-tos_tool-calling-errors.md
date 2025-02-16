---
url: https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#how-to-handle-tool-calling-errors)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to handle tool calling errors 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/?q= "Share")

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
          * Tool calling  Tool calling 
            * [ Tool calling  ](https://langchain-ai.github.io/langgraphjs/how-tos#tool-calling)
            * [ How to call tools using ToolNode  ](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/)
            * [ How to force an agent to call a tool  ](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/)
            * How to handle tool calling errors  [ How to handle tool calling errors  ](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/) Table of contents 
              * [ Using the prebuilt ToolNode  ](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#using-the-prebuilt-toolnode)
              * [ Custom strategies  ](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#custom-strategies)
              * [ Next steps  ](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#next-steps)
            * [ How to pass runtime values to tools  ](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/)
            * [ How to update graph state from tools  ](https://langchain-ai.github.io/langgraphjs/how-tos/update-state-from-tools/)
          * [ Subgraphs  ](https://langchain-ai.github.io/langgraphjs/how-tos#subgraphs)
          * [ Multi-agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/)
          * [ State Management  ](https://langchain-ai.github.io/langgraphjs/how-tos#state-management)
          * [ Other  ](https://langchain-ai.github.io/langgraphjs/how-tos#other)
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

  * [ Using the prebuilt ToolNode  ](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#using-the-prebuilt-toolnode)
  * [ Custom strategies  ](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#custom-strategies)
  * [ Next steps  ](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#next-steps)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
  5. [ Tool calling  ](https://langchain-ai.github.io/langgraphjs/how-tos#tool-calling)



# How to handle tool calling errors[¶](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#how-to-handle-tool-calling-errors "Permanent link")

LLMs aren't perfect at calling tools. The model may try to call a tool that doesn't exist or fail to return arguments that match the requested schema. Strategies like keeping schemas simple, reducing the number of tools you pass at once, and having good names and descriptions can help mitigate this risk, but aren't foolproof.

This guide covers some ways to build error handling into your graphs to mitigate these failure modes.

Compatibility

This guide requires `@langchain/langgraph>=0.0.28`, `@langchain/anthropic>=0.2.6`, and `@langchain/core>=0.2.17`. For help upgrading, see [this guide](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/). 

## Using the prebuilt `ToolNode`[¶](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#using-the-prebuilt-toolnode "Permanent link")

To start, define a mock weather tool that has some hidden restrictions on input queries. The intent here is to simulate a real-world case where a model fails to call a tool correctly:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-0-1)$npminstall@langchain/langgraph@langchain/anthropic@langchain/core

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-1-1)import{z}from"zod";
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-1-2)import{tool}from"@langchain/core/tools";
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-1-4)constgetWeather=tool(async({location})=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-1-5)if(location==="SAN FRANCISCO"){
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-1-6)return"It's 60 degrees and foggy";
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-1-7)}elseif(location.toLowerCase()==="san francisco"){
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-1-8)thrownewError("Input queries must be all capitals");
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-1-9)}else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-1-10)thrownewError("Invalid input.");
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-1-11)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-1-12)},{
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-1-13)name:"get_weather",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-1-14)description:"Call to get the current weather",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-1-15)schema:z.object({
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-1-16)location:z.string(),
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-1-17)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-1-18)});

```


Next, set up a graph implementation of the [ReAct agent](https://langchain-ai.github.io/langgraphjs/concepts/). This agent takes some query as input, then repeatedly call tools until it has enough information to resolve the query. We'll use the prebuilt `ToolNode`[](https://langchain-ai.github.io/langgraphjs/reference/classes/langgraph_prebuilt.ToolNode.html) to execute called tools, and a small, fast model powered by Anthropic:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-2-1)import{StateGraph,MessagesAnnotation}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-2-2)import{ToolNode}from"@langchain/langgraph/prebuilt";
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-2-3)import{ChatAnthropic}from"@langchain/anthropic";
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-2-4)import{BaseMessage,isAIMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-2-5)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-2-6)consttoolNode=newToolNode([getWeather]);
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-2-7)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-2-8)constmodelWithTools=newChatAnthropic({
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-2-9)model:"claude-3-haiku-20240307",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-2-10)temperature:0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-2-11)}).bindTools([getWeather]);
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-2-12)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-2-13)constshouldContinue=async(state:typeofMessagesAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-2-14)const{messages}=state;
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-2-15)constlastMessage=messages[messages.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-2-16)if(isAIMessage(lastMessage)&&lastMessage.tool_calls?.length){
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-2-17)return"tools";
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-2-18)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-2-19)return"__end__";
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-2-20)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-2-21)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-2-22)constcallModel=async(state:typeofMessagesAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-2-23)const{messages}=state;
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-2-24)constresponse=awaitmodelWithTools.invoke(messages);
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-2-25)return{messages:[response]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-2-26)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-2-27)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-2-28)constapp=newStateGraph(MessagesAnnotation)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-2-29).addNode("agent",callModel)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-2-30).addNode("tools",toolNode)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-2-31).addEdge("__start__","agent")
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-2-32).addEdge("tools","agent")
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-2-33).addConditionalEdges("agent",shouldContinue,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-2-34)// Explicitly list possible destinations so that
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-2-35)// we can automatically draw the graph below.
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-2-36)tools:"tools",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-2-37)__end__:"__end__",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-2-38)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-2-39).compile();

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-3-1)import*astslabfrom"tslab";
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-3-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-3-3)constgraph=app.getGraph();
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-3-4)constimage=awaitgraph.drawMermaidPng();
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-3-5)constarrayBuffer=awaitimage.arrayBuffer();
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-3-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-3-7)awaittslab.display.png(newUint8Array(arrayBuffer));

```


![]()

When you try to call the tool, you can see that the model calls the tool with a bad input, causing the tool to throw an error. The prebuilt `ToolNode` that executes the tool has some built-in error handling that captures the error and passes it back to the model so that it can try again:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-4-1)constresponse=awaitapp.invoke({
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-4-2)messages:[
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-4-3){role:"user",content:"what is the weather in san francisco?"},
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-4-4)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-4-5)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-4-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-4-7)for(constmessageofresponse.messages){
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-4-8)// Anthropic returns tool calls in content as well as in `AIMessage.tool_calls`
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-4-9)constcontent=JSON.stringify(message.content,null,2);
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-4-10)console.log(`${message._getType().toUpperCase()}: ${content}`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-4-11)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-5-1)HUMAN: "what is the weather in san francisco?"
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-5-2)AI: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-5-3) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-5-4)  "type": "text",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-5-5)  "text": "Okay, let's check the weather in San Francisco:"
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-5-6) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-5-7) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-5-8)  "type": "tool_use",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-5-9)  "id": "toolu_015dywEMjSJsjkgP91VDbm52",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-5-10)  "name": "get_weather",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-5-11)  "input": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-5-12)   "location": "San Francisco"
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-5-13)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-5-14) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-5-15)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-5-16)TOOL: "Error: Input queries must be all capitals\n Please fix your mistakes."
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-5-17)AI: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-5-18) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-5-19)  "type": "text",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-5-20)  "text": "Apologies, let me try that again with the location in all capital letters:"
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-5-21) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-5-22) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-5-23)  "type": "tool_use",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-5-24)  "id": "toolu_01Qw6t7p9UGk8aHQh7qtLJZT",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-5-25)  "name": "get_weather",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-5-26)  "input": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-5-27)   "location": "SAN FRANCISCO"
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-5-28)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-5-29) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-5-30)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-5-31)TOOL: "It's 60 degrees and foggy"
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-5-32)AI: "The weather in San Francisco is 60 degrees and foggy."

```


## Custom strategies[¶](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#custom-strategies "Permanent link")

This is a fine default in many cases, but there are cases where custom fallbacks may be better.

For example, the below tool requires as input a list of elements of a specific length - tricky for a small model! We'll also intentionally avoid pluralizing `topic` to trick the model into thinking it should pass a string:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-1)import{StringOutputParser}from"@langchain/core/output_parsers";
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-3)consthaikuRequestSchema=z.object({
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-4)topic:z.array(z.string()).length(3),
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-5)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-7)constmasterHaikuGenerator=tool(async({topic})=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-8)constmodel=newChatAnthropic({
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-9)model:"claude-3-haiku-20240307",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-10)temperature:0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-11)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-12)constchain=model.pipe(newStringOutputParser());
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-13)consttopics=topic.join(", ");
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-14)consthaiku=awaitchain.invoke(`Write a haiku about ${topics}`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-15)returnhaiku;
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-16)},{
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-17)name:"master_haiku_generator",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-18)description:"Generates a haiku based on the provided topics.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-19)schema:haikuRequestSchema,
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-20)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-21)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-22)constcustomStrategyToolNode=newToolNode([masterHaikuGenerator]);
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-23)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-24)constcustomStrategyModel=newChatAnthropic({
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-25)model:"claude-3-haiku-20240307",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-26)temperature:0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-27)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-28)constcustomStrategyModelWithTools=customStrategyModel.bindTools([masterHaikuGenerator]);
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-29)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-30)constcustomStrategyShouldContinue=async(state:typeofMessagesAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-31)const{messages}=state;
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-32)constlastMessage=messages[messages.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-33)if(isAIMessage(lastMessage)&&lastMessage.tool_calls?.length){
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-34)return"tools";
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-35)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-36)return"__end__";
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-37)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-38)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-39)constcustomStrategyCallModel=async(state:typeofMessagesAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-40)const{messages}=state;
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-41)constresponse=awaitcustomStrategyModelWithTools.invoke(messages);
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-42)return{messages:[response]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-43)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-44)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-45)constcustomStrategyApp=newStateGraph(MessagesAnnotation)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-46).addNode("tools",customStrategyToolNode)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-47).addNode("agent",customStrategyCallModel)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-48).addEdge("__start__","agent")
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-49).addEdge("tools","agent")
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-50).addConditionalEdges("agent",customStrategyShouldContinue,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-51)// Explicitly list possible destinations so that
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-52)// we can automatically draw the graph below.
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-53)tools:"tools",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-54)__end__:"__end__",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-55)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-56).compile();
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-57)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-58)constresponse2=awaitcustomStrategyApp.invoke(
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-59){
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-60)messages:[{role:"user",content:"Write me an incredible haiku about water."}],
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-61)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-62){recursionLimit:10}
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-63));
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-64)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-65)for(constmessageofresponse2.messages){
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-66)// Anthropic returns tool calls in content as well as in `AIMessage.tool_calls`
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-67)constcontent=JSON.stringify(message.content,null,2);
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-68)console.log(`${message._getType().toUpperCase()}: ${content}`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-6-69)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-7-1)HUMAN: "Write me an incredible haiku about water."
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-7-2)AI: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-7-3) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-7-4)  "type": "text",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-7-5)  "text": "Okay, let's generate a haiku about water using the master haiku generator tool:"
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-7-6) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-7-7) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-7-8)  "type": "tool_use",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-7-9)  "id": "toolu_01CMvVu3MhPeCk5X7F8GBv8f",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-7-10)  "name": "master_haiku_generator",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-7-11)  "input": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-7-12)   "topic": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-7-13)    "water"
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-7-14)   ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-7-15)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-7-16) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-7-17)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-7-18)TOOL: "Error: Received tool input did not match expected schema\n Please fix your mistakes."
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-7-19)AI: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-7-20) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-7-21)  "type": "text",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-7-22)  "text": "Oops, looks like I need to provide 3 topics for the haiku generator. Let me try again with 3 water-related topics:"
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-7-23) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-7-24) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-7-25)  "type": "tool_use",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-7-26)  "id": "toolu_0158Nz2scGSWvYor4vmJbSDZ",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-7-27)  "name": "master_haiku_generator",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-7-28)  "input": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-7-29)   "topic": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-7-30)    "ocean",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-7-31)    "waves",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-7-32)    "rain"
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-7-33)   ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-7-34)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-7-35) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-7-36)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-7-37)TOOL: "Here is a haiku about the ocean, waves, and rain:\n\nWaves crash on the shore,\nRhythmic dance of water's song,\nRain falls from the sky."
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-7-38)AI: "The haiku generator has produced a beautiful and evocative poem about the different aspects of water - the ocean, waves, and rain. I hope you enjoy this creative take on a water-themed haiku!"

```


We can see that the model takes two attempts. 

A better strategy might be to trim the failed attempt to reduce distraction, then fall back to a more advanced model. Here's an example - note the custom-built tool calling node instead of the prebuilt `ToolNode`:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-1)import{AIMessage,ToolMessage,RemoveMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-3)consthaikuRequestSchema2=z.object({
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-4)topic:z.array(z.string()).length(3),
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-5)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-7)constmasterHaikuGenerator2=tool(async({topic})=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-8)constmodel=newChatAnthropic({
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-9)model:"claude-3-haiku-20240307",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-10)temperature:0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-11)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-12)constchain=model.pipe(newStringOutputParser());
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-13)consttopics=topic.join(", ");
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-14)consthaiku=awaitchain.invoke(`Write a haiku about ${topics}`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-15)returnhaiku;
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-16)},{
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-17)name:"master_haiku_generator",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-18)description:"Generates a haiku based on the provided topics.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-19)schema:haikuRequestSchema2,
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-20)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-21)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-22)constcallTool2=async(state:typeofMessagesAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-23)const{messages}=state;
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-24)consttoolsByName={master_haiku_generator:masterHaikuGenerator};
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-25)constlastMessage=messages[messages.length-1]asAIMessage;
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-26)constoutputMessages:ToolMessage[]=[];
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-27)for(consttoolCalloflastMessage.tool_calls){
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-28)try{
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-29)consttoolResult=awaittoolsByName[toolCall.name].invoke(toolCall);
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-30)outputMessages.push(toolResult);
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-31)}catch(error:any){
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-32)// Return the error if the tool call fails
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-33)outputMessages.push(
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-34)newToolMessage({
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-35)content:error.message,
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-36)name:toolCall.name,
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-37)tool_call_id:toolCall.id!,
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-38)additional_kwargs:{error}
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-39)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-40));
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-41)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-42)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-43)return{messages:outputMessages};
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-44)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-45)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-46)constmodel=newChatAnthropic({
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-47)model:"claude-3-haiku-20240307",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-48)temperature:0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-49)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-50)constmodelWithTools2=model.bindTools([masterHaikuGenerator2]);
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-51)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-52)constbetterModel=newChatAnthropic({
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-53)model:"claude-3-5-sonnet-20240620",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-54)temperature:0,
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-55)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-56)constbetterModelWithTools=betterModel.bindTools([masterHaikuGenerator2]);
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-57)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-58)constshouldContinue2=async(state:typeofMessagesAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-59)const{messages}=state;
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-60)constlastMessage=messages[messages.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-61)if(isAIMessage(lastMessage)&&lastMessage.tool_calls?.length){
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-62)return"tools";
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-63)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-64)return"__end__";
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-65)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-66)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-67)constshouldFallback=async(state:typeofMessagesAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-68)const{messages}=state;
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-69)constfailedToolMessages=messages.find((message)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-70)returnmessage._getType()==="tool"&&message.additional_kwargs.error!==undefined;
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-71)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-72)if(failedToolMessages){
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-73)return"remove_failed_tool_call_attempt";
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-74)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-75)return"agent";
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-76)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-77)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-78)constcallModel2=async(state:typeofMessagesAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-79)const{messages}=state;
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-80)constresponse=awaitmodelWithTools2.invoke(messages);
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-81)return{messages:[response]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-82)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-83)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-84)constremoveFailedToolCallAttempt=async(state:typeofMessagesAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-85)const{messages}=state;
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-86)// Remove all messages from the most recent
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-87)// instance of AIMessage onwards.
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-88)constlastAIMessageIndex=messages
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-89).map((msg,index)=>({msg,index}))
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-90).reverse()
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-91).findIndex(({msg})=>isAIMessage(msg));
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-92)constmessagesToRemove=messages.slice(lastAIMessageIndex);
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-93)return{messages:messagesToRemove.map(m=>newRemoveMessage({id:m.id}))};
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-94)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-95)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-96)constcallFallbackModel=async(state:typeofMessagesAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-97)const{messages}=state;
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-98)constresponse=awaitbetterModelWithTools.invoke(messages);
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-99)return{messages:[response]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-100)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-101)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-102)constapp2=newStateGraph(MessagesAnnotation)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-103).addNode("tools",callTool2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-104).addNode("agent",callModel2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-105).addNode("remove_failed_tool_call_attempt",removeFailedToolCallAttempt)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-106).addNode("fallback_agent",callFallbackModel)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-107).addEdge("__start__","agent")
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-108).addConditionalEdges("agent",shouldContinue2,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-109)// Explicitly list possible destinations so that
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-110)// we can automatically draw the graph below.
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-111)tools:"tools",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-112)__end__:"__end__",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-113)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-114).addConditionalEdges("tools",shouldFallback,{
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-115)remove_failed_tool_call_attempt:"remove_failed_tool_call_attempt",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-116)agent:"agent",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-117)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-118).addEdge("remove_failed_tool_call_attempt","fallback_agent")
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-119).addEdge("fallback_agent","tools")
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-8-120).compile();

```


The `tools` node will now return `ToolMessage`s with an `error` field in `additional_kwargs` if a tool call fails. If that happens, it will go to another node that removes the failed tool messages, and has a better model retry the tool call generation. We also add a trimming step via returning the special message modifier `RemoveMessage` to remove previous messages from the state.

The diagram below shows this visually:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-9-1)import*astslabfrom"tslab";
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-9-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-9-3)constgraph2=app2.getGraph();
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-9-4)constimage2=awaitgraph2.drawMermaidPng();
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-9-5)constarrayBuffer2=awaitimage2.arrayBuffer();
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-9-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-9-7)awaittslab.display.png(newUint8Array(arrayBuffer2));

```


![]()

Let's try it out. To emphasize the removal steps, let's `stream` the responses from the model so that we can see each executed node:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-10-1)conststream=awaitapp2.stream(
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-10-2){messages:[{role:"user",content:"Write me an incredible haiku about water."}]},
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-10-3){recursionLimit:10},
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-10-4))
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-10-5)
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-10-6)forawait(constchunkofstream){
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-10-7)console.log(chunk);
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-10-8)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-1){
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-2) agent: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-3)  messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-4)   AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-5)    "id": "msg_01HqvhPuubXqerWgYRNFqPrd",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-6)    "content": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-7)     {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-8)      "type": "text",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-9)      "text": "Okay, let's generate a haiku about water using the master haiku generator tool:"
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-10)     },
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-11)     {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-12)      "type": "tool_use",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-13)      "id": "toolu_01QFmyc5vhQBFfzF7hCGTRc1",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-14)      "name": "master_haiku_generator",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-15)      "input": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-16)       "topic": "[Array]"
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-17)      }
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-18)     }
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-19)    ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-20)    "additional_kwargs": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-21)     "id": "msg_01HqvhPuubXqerWgYRNFqPrd",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-22)     "type": "message",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-23)     "role": "assistant",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-24)     "model": "claude-3-haiku-20240307",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-25)     "stop_reason": "tool_use",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-26)     "stop_sequence": null,
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-27)     "usage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-28)      "input_tokens": 392,
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-29)      "output_tokens": 77
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-30)     }
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-31)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-32)    "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-33)     "id": "msg_01HqvhPuubXqerWgYRNFqPrd",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-34)     "model": "claude-3-haiku-20240307",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-35)     "stop_reason": "tool_use",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-36)     "stop_sequence": null,
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-37)     "usage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-38)      "input_tokens": 392,
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-39)      "output_tokens": 77
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-40)     },
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-41)     "type": "message",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-42)     "role": "assistant"
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-43)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-44)    "tool_calls": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-45)     {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-46)      "name": "master_haiku_generator",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-47)      "args": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-48)       "topic": "[Array]"
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-49)      },
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-50)      "id": "toolu_01QFmyc5vhQBFfzF7hCGTRc1",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-51)      "type": "tool_call"
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-52)     }
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-53)    ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-54)    "invalid_tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-55)    "usage_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-56)     "input_tokens": 392,
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-57)     "output_tokens": 77,
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-58)     "total_tokens": 469
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-59)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-60)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-61)  ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-62) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-63)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-64){
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-65) tools: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-66)  messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-67)   ToolMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-68)    "id": "502c7399-4d95-4afd-8a86-ece864d2bc7f",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-69)    "content": "Received tool input did not match expected schema",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-70)    "name": "master_haiku_generator",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-71)    "additional_kwargs": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-72)     "error": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-73)      "output": "{\"topic\":[\"water\"]}"
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-74)     }
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-75)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-76)    "response_metadata": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-77)    "tool_call_id": "toolu_01QFmyc5vhQBFfzF7hCGTRc1"
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-78)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-79)  ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-80) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-81)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-82){
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-83) remove_failed_tool_call_attempt: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-84)  messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-85)   BaseMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-86)    "id": "msg_01HqvhPuubXqerWgYRNFqPrd",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-87)    "content": "",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-88)    "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-89)    "response_metadata": {}
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-90)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-91)   BaseMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-92)    "id": "502c7399-4d95-4afd-8a86-ece864d2bc7f",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-93)    "content": "",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-94)    "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-95)    "response_metadata": {}
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-96)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-97)  ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-98) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-99)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-100){
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-101) fallback_agent: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-102)  messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-103)   AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-104)    "id": "msg_01EQSawL2oxNhph9be99k7Yp",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-105)    "content": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-106)     {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-107)      "type": "text",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-108)      "text": "Certainly! I'd be happy to help you create an incredible haiku about water. To do this, we'll use the master_haiku_generator function, which requires three topics as input. Since you've specified water as the main theme, I'll add two related concepts to create a more vivid and interesting haiku. Let's use \"water,\" \"flow,\" and \"reflection\" as our three topics.\n\nHere's the function call to generate your haiku:"
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-109)     },
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-110)     {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-111)      "type": "tool_use",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-112)      "id": "toolu_017hrp13SsgfdJTdhkJDMaQy",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-113)      "name": "master_haiku_generator",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-114)      "input": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-115)       "topic": "[Array]"
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-116)      }
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-117)     }
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-118)    ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-119)    "additional_kwargs": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-120)     "id": "msg_01EQSawL2oxNhph9be99k7Yp",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-121)     "type": "message",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-122)     "role": "assistant",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-123)     "model": "claude-3-5-sonnet-20240620",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-124)     "stop_reason": "tool_use",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-125)     "stop_sequence": null,
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-126)     "usage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-127)      "input_tokens": 422,
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-128)      "output_tokens": 162
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-129)     }
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-130)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-131)    "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-132)     "id": "msg_01EQSawL2oxNhph9be99k7Yp",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-133)     "model": "claude-3-5-sonnet-20240620",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-134)     "stop_reason": "tool_use",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-135)     "stop_sequence": null,
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-136)     "usage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-137)      "input_tokens": 422,
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-138)      "output_tokens": 162
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-139)     },
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-140)     "type": "message",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-141)     "role": "assistant"
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-142)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-143)    "tool_calls": [
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-144)     {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-145)      "name": "master_haiku_generator",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-146)      "args": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-147)       "topic": "[Array]"
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-148)      },
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-149)      "id": "toolu_017hrp13SsgfdJTdhkJDMaQy",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-150)      "type": "tool_call"
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-151)     }
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-152)    ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-153)    "invalid_tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-154)    "usage_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-155)     "input_tokens": 422,
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-156)     "output_tokens": 162,
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-157)     "total_tokens": 584
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-158)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-159)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-160)  ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-161) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-162)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-163){
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-164) tools: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-165)  messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-166)   ToolMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-167)    "id": "3d24d291-7501-4a65-9286-10dc47239b5b",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-168)    "content": "Here is a haiku about water, flow, and reflection:\n\nRippling waters flow,\nMirroring the sky above,\nTranquil reflection.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-169)    "name": "master_haiku_generator",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-170)    "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-171)    "response_metadata": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-172)    "tool_call_id": "toolu_017hrp13SsgfdJTdhkJDMaQy"
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-173)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-174)  ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-175) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-176)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-177){
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-178) agent: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-179)  messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-180)   AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-181)    "id": "msg_01Jy7Vw8DN77sjVWcB4TcJR6",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-182)    "content": "I hope you enjoy this haiku about the beauty and serenity of water. Please let me know if you would like me to generate another one.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-183)    "additional_kwargs": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-184)     "id": "msg_01Jy7Vw8DN77sjVWcB4TcJR6",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-185)     "type": "message",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-186)     "role": "assistant",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-187)     "model": "claude-3-haiku-20240307",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-188)     "stop_reason": "end_turn",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-189)     "stop_sequence": null,
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-190)     "usage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-191)      "input_tokens": 601,
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-192)      "output_tokens": 35
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-193)     }
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-194)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-195)    "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-196)     "id": "msg_01Jy7Vw8DN77sjVWcB4TcJR6",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-197)     "model": "claude-3-haiku-20240307",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-198)     "stop_reason": "end_turn",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-199)     "stop_sequence": null,
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-200)     "usage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-201)      "input_tokens": 601,
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-202)      "output_tokens": 35
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-203)     },
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-204)     "type": "message",
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-205)     "role": "assistant"
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-206)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-207)    "tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-208)    "invalid_tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-209)    "usage_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-210)     "input_tokens": 601,
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-211)     "output_tokens": 35,
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-212)     "total_tokens": 636
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-213)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-214)   }
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-215)  ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-216) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__codelineno-11-217)}

```


You can see that you get a cleaner response - the more powerful model gets it right on the first try, and the smaller model's failure gets wiped from the graph state. This shorter message history also avoid overpopulating the graph state with attempts. 

You can also inspect this [LangSmith trace](https://smith.langchain.com/public/c94f95d0-97fc-4d4d-a59a-b5161c2f4a90/r), which shows the failed initial call to the smaller model.

## Next steps[¶](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#next-steps "Permanent link")

You've now seen how to implement some strategies to handle tool calling errors.

Next, check out some of the [other LangGraph how-to guides here](https://langchain-ai.github.io/langgraphjs/how-tos/).

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to force an agent to call a tool  ](https://langchain-ai.github.io/langgraphjs/how-tos/force-calling-a-tool-first/) [ Next  How to pass runtime values to tools  ](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
