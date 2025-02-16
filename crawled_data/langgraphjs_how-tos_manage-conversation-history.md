---
url: https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#how-to-manage-conversation-history)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to manage conversation history 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/?q= "Share")

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
          * Memory  Memory 
            * [ Memory  ](https://langchain-ai.github.io/langgraphjs/how-tos#memory)
            * How to manage conversation history  [ How to manage conversation history  ](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#setup)
              * [ Build the agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#build-the-agent)
              * [ Filtering messages  ](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#filtering-messages)
            * [ How to delete messages  ](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/)
            * [ How to add summary of the conversation history  ](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/)
            * [ How to add semantic search to your agent's memory  ](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/)
          * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraphjs/how-tos#human-in-the-loop)
          * [ Streaming  ](https://langchain-ai.github.io/langgraphjs/how-tos#streaming)
          * [ Tool calling  ](https://langchain-ai.github.io/langgraphjs/how-tos#tool-calling)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#setup)
  * [ Build the agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#build-the-agent)
  * [ Filtering messages  ](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#filtering-messages)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
  5. [ Memory  ](https://langchain-ai.github.io/langgraphjs/how-tos#memory)



# How to manage conversation history[¶](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#how-to-manage-conversation-history "Permanent link")

One of the most common use cases for persistence is to use it to keep track of conversation history. This is great - it makes it easy to continue conversations. As conversations get longer and longer, however, this conversation history can build up and take up more and more of the context window. This can often be undesirable as it leads to more expensive and longer calls to the LLM, and potentially ones that error. In order to prevent this from happening, you need to probably manage the conversation history.

Note: this guide focuses on how to do this in LangGraph, where you can fully customize how this is done. If you want a more off-the-shelf solution, you can look into functionality provided in LangChain:

  * [How to filter messages](https://js.langchain.com/docs/how_to/filter_messages/)
  * [How to trim messages](https://js.langchain.com/docs/how_to/trim_messages/)



## Setup[¶](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#setup "Permanent link")

First, let's set up the packages we're going to want to use

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-0-1)yarnaddlangchain@langchain/anthropic@langchain/core

```


Next, we need to set API keys for Anthropic (the LLM we will use)

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-1-1)exportANTHROPIC_API_KEY=your_api_key

```


Optionally, we can set API key for [LangSmith tracing](https://smith.langchain.com/), which will give us best-in-class observability.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-2-1)exportLANGCHAIN_TRACING_V2="true"
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-2-2)exportLANGCHAIN_CALLBACKS_BACKGROUND="true"
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-2-3)exportLANGCHAIN_API_KEY=your_api_key

```


## Build the agent[¶](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#build-the-agent "Permanent link")

Let's now build a simple ReAct style agent.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-1)import{ChatAnthropic}from"@langchain/anthropic";
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-2)import{tool}from"@langchain/core/tools";
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-3)import{BaseMessage,AIMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-4)import{StateGraph,Annotation,START,END}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-5)import{ToolNode}from"@langchain/langgraph/prebuilt";
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-6)import{MemorySaver}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-7)import{z}from"zod";
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-8)
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-9)constAgentState=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-10)messages:Annotation<BaseMessage[]>({
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-11)reducer:(x,y)=>x.concat(y),
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-12)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-13)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-14)
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-15)constmemory=newMemorySaver();
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-16)
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-17)constsearchTool=tool((_):string=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-18)// This is a placeholder for the actual implementation
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-19)// Don't let the LLM know this though 😊
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-20)return"It's sunny in San Francisco, but you better look out if you're a Gemini 😈."
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-21)},{
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-22)name:"search",
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-23)description:"Call to surf the web.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-24)schema:z.object({
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-25)query:z.string()
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-26)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-27)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-28)
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-29)
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-30)consttools=[searchTool]
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-31)consttoolNode=newToolNode<typeofAgentState.State>(tools)
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-32)constmodel=newChatAnthropic({model:"claude-3-haiku-20240307"})
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-33)constboundModel=model.bindTools(tools)
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-34)
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-35)functionshouldContinue(state:typeofAgentState.State):"action"|typeofEND{
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-36)constlastMessage=state.messages[state.messages.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-37)// If there is no function call, then we finish
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-38)if(lastMessage&&!(lastMessageasAIMessage).tool_calls?.length){
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-39)returnEND;
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-40)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-41)// Otherwise if there is, we continue
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-42)return"action";
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-43)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-44)
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-45)// Define the function that calls the model
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-46)asyncfunctioncallModel(state:typeofAgentState.State){
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-47)constresponse=awaitmodel.invoke(state.messages);
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-48)// We return an object, because this will get merged with the existing state
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-49)return{messages:[response]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-50)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-51)
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-52)// Define a new graph
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-53)constworkflow=newStateGraph(AgentState)
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-54)// Define the two nodes we will cycle between
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-55).addNode("agent",callModel)
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-56).addNode("action",toolNode)
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-57)// We now add a conditional edge
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-58).addConditionalEdges(
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-59)// First, we define the start node. We use `agent`.
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-60)// This means these are the edges taken after the `agent` node is called.
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-61)"agent",
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-62)// Next, we pass in the function that will determine which node is called next.
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-63)shouldContinue
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-64))
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-65)// We now add a normal edge from `action` to `agent`.
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-66)// This means that after `action` is called, `agent` node is called next.
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-67).addEdge("action","agent")
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-68)// Set the entrypoint as `agent`
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-69)// This means that this node is the first one called
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-70).addEdge(START,"agent");
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-71)
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-72)// Finally, we compile it!
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-73)// This compiles it into a LangChain Runnable,
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-74)// meaning you can use it as you would any other runnable
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-75)constapp=workflow.compile({
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-76)checkpointer:memory,
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-3-77)});

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-4-1)import{HumanMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-4-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-4-3)constconfig={configurable:{thread_id:"2"},streamMode:"values"asconst}
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-4-4)
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-4-5)constinputMessage=newHumanMessage("hi! I'm bob");
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-4-6)forawait(consteventofawaitapp.stream({
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-4-7)messages:[inputMessage]
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-4-8)},config)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-4-9)constrecentMsg=event.messages[event.messages.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-4-10)console.log(`================================ ${recentMsg._getType()} Message (1) =================================`)
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-4-11)console.log(recentMsg.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-4-12)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-4-13)
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-4-14)console.log("\n\n================================= END =================================\n\n")
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-4-15)
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-4-16)constinputMessage2=newHumanMessage("what's my name?");
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-4-17)forawait(consteventofawaitapp.stream({
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-4-18)messages:[inputMessage2]
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-4-19)},config)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-4-20)constrecentMsg=event.messages[event.messages.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-4-21)console.log(`================================ ${recentMsg._getType()} Message (2) =================================`)
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-4-22)console.log(recentMsg.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-4-23)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-5-1)================================ human Message (1) =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-5-2)hi! I'm bob
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-5-3)================================ ai Message (1) =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-5-4)Hello Bob! It's nice to meet you. I'm an AI assistant created by Anthropic. I'm here to help with any questions or tasks you may have. Please let me know if there's anything I can assist you with.
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-5-5)
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-5-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-5-7)================================= END =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-5-8)
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-5-9)
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-5-10)================================ human Message (2) =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-5-11)what's my name?
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-5-12)================================ ai Message (2) =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-5-13)Your name is Bob, as you introduced yourself earlier.

```


## Filtering messages[¶](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#filtering-messages "Permanent link")

The most straight-forward thing to do to prevent conversation history from blowing up is to filter the list of messages before they get passed to the LLM. This involves two parts: defining a function to filter messages, and then adding it to the graph. See the example below which defines a really simple `filterMessages` function and then uses it.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-1)import{ChatAnthropic}from"@langchain/anthropic";
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-2)import{tool}from"@langchain/core/tools";
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-3)import{BaseMessage,AIMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-4)import{StateGraph,Annotation,START,END}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-5)import{ToolNode}from"@langchain/langgraph/prebuilt";
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-6)import{MemorySaver}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-7)import{z}from"zod";
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-8)
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-9)constMessageFilteringAgentState=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-10)messages:Annotation<BaseMessage[]>({
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-11)reducer:(x,y)=>x.concat(y),
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-12)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-13)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-14)
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-15)constmessageFilteringMemory=newMemorySaver();
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-16)
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-17)constmessageFilteringSearchTool=tool((_):string=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-18)// This is a placeholder for the actual implementation
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-19)// Don't let the LLM know this though 😊
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-20)return"It's sunny in San Francisco, but you better look out if you're a Gemini 😈."
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-21)},{
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-22)name:"search",
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-23)description:"Call to surf the web.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-24)schema:z.object({
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-25)query:z.string()
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-26)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-27)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-28)
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-29)// We can re-use the same search tool as above as we don't need to change it for this example.
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-30)constmessageFilteringTools=[messageFilteringSearchTool]
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-31)constmessageFilteringToolNode=newToolNode<typeofMessageFilteringAgentState.State>(messageFilteringTools)
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-32)constmessageFilteringModel=newChatAnthropic({model:"claude-3-haiku-20240307"})
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-33)constboundMessageFilteringModel=messageFilteringModel.bindTools(messageFilteringTools)
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-34)
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-35)
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-36)asyncfunctionshouldContinueMessageFiltering(state:typeofMessageFilteringAgentState.State):Promise<"action"|typeofEND>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-37)constlastMessage=state.messages[state.messages.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-38)// If there is no function call, then we finish
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-39)if(lastMessage&&!(lastMessageasAIMessage).tool_calls?.length){
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-40)returnEND;
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-41)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-42)// Otherwise if there is, we continue
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-43)return"action";
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-44)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-45)
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-46)constfilterMessages=(messages:BaseMessage[]):BaseMessage[]=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-47)// This is very simple helper function which only ever uses the last message
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-48)returnmessages.slice(-1);
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-49)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-50)
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-51)// Define the function that calls the model
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-52)asyncfunctioncallModelMessageFiltering(state:typeofMessageFilteringAgentState.State){
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-53)constresponse=awaitboundMessageFilteringModel.invoke(filterMessages(state.messages));
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-54)// We return an object, because this will get merged with the existing state
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-55)return{messages:[response]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-56)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-57)
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-58)
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-59)// Define a new graph
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-60)constmessageFilteringWorkflow=newStateGraph(MessageFilteringAgentState)
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-61)// Define the two nodes we will cycle between
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-62).addNode("agent",callModelMessageFiltering)
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-63).addNode("action",messageFilteringToolNode)
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-64)// We now add a conditional edge
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-65).addConditionalEdges(
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-66)// First, we define the start node. We use `agent`.
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-67)// This means these are the edges taken after the `agent` node is called.
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-68)"agent",
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-69)// Next, we pass in the function that will determine which node is called next.
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-70)shouldContinueMessageFiltering
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-71))
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-72)// We now add a normal edge from `action` to `agent`.
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-73)// This means that after `action` is called, `agent` node is called next.
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-74).addEdge("action","agent")
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-75)// Set the entrypoint as `agent`
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-76)// This means that this node is the first one called
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-77).addEdge(START,"agent");
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-78)
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-79)// Finally, we compile it!
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-80)// This compiles it into a LangChain Runnable,
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-81)// meaning you can use it as you would any other runnable
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-82)constmessageFilteringApp=messageFilteringWorkflow.compile({
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-83)checkpointer:messageFilteringMemory,
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-6-84)});

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-7-1)import{HumanMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-7-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-7-3)constmessageFilteringConfig={configurable:{thread_id:"2"},streamMode:"values"asconst}
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-7-4)
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-7-5)constmessageFilteringInput=newHumanMessage("hi! I'm bob");
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-7-6)forawait(consteventofawaitmessageFilteringApp.stream({
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-7-7)messages:[messageFilteringInput]
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-7-8)},messageFilteringConfig)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-7-9)constrecentMsg=event.messages[event.messages.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-7-10)console.log(`================================ ${recentMsg._getType()} Message (1) =================================`)
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-7-11)console.log(recentMsg.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-7-12)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-7-13)
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-7-14)console.log("\n\n================================= END =================================\n\n")
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-7-15)
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-7-16)constmessageFilteringInput2=newHumanMessage("what's my name?");
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-7-17)forawait(consteventofawaitmessageFilteringApp.stream(
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-7-18){
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-7-19)messages:[messageFilteringInput2]
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-7-20)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-7-21)messageFilteringConfig
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-7-22))){
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-7-23)constrecentMsg=event.messages[event.messages.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-7-24)console.log(`================================ ${recentMsg._getType()} Message (2) =================================`)
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-7-25)console.log(recentMsg.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-7-26)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-8-1)================================ human Message (1) =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-8-2)hi! I'm bob
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-8-3)================================ ai Message (1) =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-8-4)Hello, nice to meet you Bob! I'm an AI assistant here to help out. Feel free to let me know if you have any questions or if there's anything I can assist with.
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-8-5)
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-8-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-8-7)================================= END =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-8-8)
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-8-9)
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-8-10)================================ human Message (2) =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-8-11)what's my name?
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-8-12)================================ ai Message (2) =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__codelineno-8-13)I'm afraid I don't actually know your name, since you haven't provided that information to me. As an AI assistant, I don't have access to personal details about you unless you share them with me directly. I'm happy to continue our conversation, but I don't have enough context to know your specific name. Please feel free to introduce yourself if you'd like me to address you by name.

```


In the above example we defined the `filter_messages` function ourselves. We also provide off-the-shelf ways to trim and filter messages in LangChain. 

  * [How to filter messages](https://js.langchain.com/docs/how_to/filter_messages/)
  * [How to trim messages](https://js.langchain.com/docs/how_to/trim_messages/)

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to use Postgres checkpointer for persistence  ](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-postgres/) [ Next  How to delete messages  ](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
