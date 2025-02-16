---
url: https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#how-to-add-summary-of-the-conversation-history)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to add summary of the conversation history 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/?q= "Share")

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
            * [ How to manage conversation history  ](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/)
            * [ How to delete messages  ](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/)
            * How to add summary of the conversation history  [ How to add summary of the conversation history  ](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#setup)
              * [ Build the chatbot  ](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#build-the-chatbot)
              * [ Using the graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#using-the-graph)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#setup)
  * [ Build the chatbot  ](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#build-the-chatbot)
  * [ Using the graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#using-the-graph)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
  5. [ Memory  ](https://langchain-ai.github.io/langgraphjs/how-tos#memory)



# How to add summary of the conversation history[¶](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#how-to-add-summary-of-the-conversation-history "Permanent link")

One of the most common use cases for persistence is to use it to keep track of conversation history. This is great - it makes it easy to continue conversations. As conversations get longer and longer, however, this conversation history can build up and take up more and more of the context window. This can often be undesirable as it leads to more expensive and longer calls to the LLM, and potentially ones that error. One way to work around that is to create a summary of the conversation to date, and use that with the past N messages. This guide will go through an example of how to do that.

This will involve a few steps: - Check if the conversation is too long (can be done by checking number of messages or length of messages) - If yes, the create summary (will need a prompt for this) - Then remove all except the last N messages

A big part of this is deleting old messages. For an in depth guide on how to do that, see [this guide](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages)

## Setup[¶](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#setup "Permanent link")

First, let's set up the packages we're going to want to use

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-0-1)npminstall@langchain/langgraph@langchain/anthropic@langchain/coreuuid

```


Next, we need to set API keys for Anthropic (the LLM we will use)

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-1-1)process.env.ANTHROPIC_API_KEY='YOUR_API_KEY'

```


Optionally, we can set API key for [LangSmith tracing](https://smith.langchain.com/), which will give us best-in-class observability.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-2-1)process.env.LANGCHAIN_TRACING_V2='true'
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-2-2)process.env.LANGCHAIN_API_KEY='YOUR_API_KEY'

```


## Build the chatbot[¶](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#build-the-chatbot "Permanent link")

Let's now build the chatbot.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-1)import{ChatAnthropic}from"@langchain/anthropic";
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-2)import{SystemMessage,HumanMessage,AIMessage,RemoveMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-3)import{MemorySaver}from"@langchain/langgraph-checkpoint";
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-4)import{MessagesAnnotation,StateGraph,START,END,Annotation}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-5)import{v4asuuidv4}from"uuid";
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-7)constmemory=newMemorySaver();
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-8)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-9)// We will add a `summary` attribute (in addition to `messages` key,
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-10)// which MessagesAnnotation already has)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-11)constGraphAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-12)...MessagesAnnotation.spec,
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-13)summary:Annotation<string>({
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-14)reducer:(_,action)=>action,
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-15)default:()=>"",
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-16)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-17)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-18)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-19)// We will use this model for both the conversation and the summarization
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-20)constmodel=newChatAnthropic({model:"claude-3-haiku-20240307"});
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-21)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-22)// Define the logic to call the model
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-23)asyncfunctioncallModel(state:typeofGraphAnnotation.State):Promise<Partial<typeofGraphAnnotation.State>>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-24)// If a summary exists, we add this in as a system message
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-25)const{summary}=state;
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-26)let{messages}=state;
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-27)if(summary){
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-28)constsystemMessage=newSystemMessage({
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-29)id:uuidv4(),
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-30)content:`Summary of conversation earlier: ${summary}`
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-31)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-32)messages=[systemMessage,...messages];
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-33)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-34)constresponse=awaitmodel.invoke(messages);
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-35)// We return an object, because this will get added to the existing state
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-36)return{messages:[response]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-37)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-38)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-39)// We now define the logic for determining whether to end or summarize the conversation
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-40)functionshouldContinue(state:typeofGraphAnnotation.State):"summarize_conversation"|typeofEND{
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-41)constmessages=state.messages;
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-42)// If there are more than six messages, then we summarize the conversation
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-43)if(messages.length>6){
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-44)return"summarize_conversation";
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-45)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-46)// Otherwise we can just end
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-47)returnEND;
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-48)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-49)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-50)asyncfunctionsummarizeConversation(state:typeofGraphAnnotation.State):Promise<Partial<typeofGraphAnnotation.State>>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-51)// First, we summarize the conversation
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-52)const{summary,messages}=state;
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-53)letsummaryMessage:string;
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-54)if(summary){
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-55)// If a summary already exists, we use a different system prompt
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-56)// to summarize it than if one didn't
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-57)summaryMessage=`This is summary of the conversation to date: ${summary}\n\n`+
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-58)"Extend the summary by taking into account the new messages above:";
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-59)}else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-60)summaryMessage="Create a summary of the conversation above:";
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-61)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-62)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-63)constallMessages=[...messages,newHumanMessage({
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-64)id:uuidv4(),
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-65)content:summaryMessage,
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-66)})];
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-67)constresponse=awaitmodel.invoke(allMessages);
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-68)// We now need to delete messages that we no longer want to show up
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-69)// I will delete all but the last two messages, but you can change this
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-70)constdeleteMessages=messages.slice(0,-2).map((m)=>newRemoveMessage({id:m.id}));
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-71)if(typeofresponse.content!=="string"){
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-72)thrownewError("Expected a string response from the model");
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-73)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-74)return{summary:response.content,messages:deleteMessages};
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-75)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-76)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-77)// Define a new graph
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-78)constworkflow=newStateGraph(GraphAnnotation)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-79)// Define the conversation node and the summarize node
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-80).addNode("conversation",callModel)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-81).addNode("summarize_conversation",summarizeConversation)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-82)// Set the entrypoint as conversation
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-83).addEdge(START,"conversation")
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-84)// We now add a conditional edge
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-85).addConditionalEdges(
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-86)// First, we define the start node. We use `conversation`.
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-87)// This means these are the edges taken after the `conversation` node is called.
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-88)"conversation",
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-89)// Next, we pass in the function that will determine which node is called next.
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-90)shouldContinue
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-91))
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-92)// We now add a normal edge from `summarize_conversation` to END.
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-93)// This means that after `summarize_conversation` is called, we end.
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-94).addEdge("summarize_conversation",END);
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-95)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-96)// Finally, we compile it!
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-3-97)constapp=workflow.compile({checkpointer:memory});

```


## Using the graph[¶](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#using-the-graph "Permanent link")

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-4-1)constprintUpdate=(update:Record<string,any>)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-4-2)Object.keys(update).forEach((key)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-4-3)constvalue=update[key];
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-4-4)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-4-5)if("messages"invalue&&Array.isArray(value.messages)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-4-6)value.messages.forEach((msg)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-4-7)console.log(`\n================================ ${msg._getType()} Message =================================`)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-4-8)console.log(msg.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-4-9)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-4-10)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-4-11)if("summary"invalue&&value.summary){
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-4-12)console.log(value.summary);
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-4-13)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-4-14)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-4-15)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-5-1)import{HumanMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-5-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-5-3)constconfig={configurable:{thread_id:"4"},streamMode:"updates"asconst}
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-5-4)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-5-5)constinputMessage=newHumanMessage("hi! I'm bob")
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-5-6)console.log(inputMessage.content)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-5-7)forawait(consteventofawaitapp.stream({messages:[inputMessage]},config)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-5-8)printUpdate(event)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-5-9)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-5-10)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-5-11)constinputMessage2=newHumanMessage("What did I sat my name was?")
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-5-12)console.log(inputMessage2.content)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-5-13)forawait(consteventofawaitapp.stream({messages:[inputMessage2]},config)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-5-14)printUpdate(event)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-5-15)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-5-16)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-5-17)constinputMessage3=newHumanMessage("i like the celtics!")
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-5-18)console.log(inputMessage3.content)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-5-19)forawait(consteventofawaitapp.stream({messages:[inputMessage3]},config)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-5-20)printUpdate(event)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-5-21)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-6-1)hi! I'm bob
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-6-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-6-3)================================ ai Message =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-6-4)Okay, got it. Hello Bob, it's nice to chat with you again. I recognize that you've repeatedly stated your name is Bob throughout our conversation. Please let me know if there is anything I can assist you with.
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-6-5)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-6-6)================================ remove Message =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-6-7)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-6-8)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-6-9)================================ remove Message =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-6-10)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-6-11)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-6-12)================================ remove Message =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-6-13)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-6-14)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-6-15)================================ ai Message =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-6-16)In our conversation, you have stated multiple times that your name is Bob. For example, you said "I'm Bob", "hi! I'm bob", and similar variations where you clearly identified yourself as Bob.
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-6-17)i like the celtics!
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-6-18)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-6-19)================================ ai Message =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-6-20)Ah I see, you mentioned earlier that you like the Boston Celtics basketball team. That's great, the Celtics have a long and storied history in the NBA. As one of the league's original franchises, they've won a record 17 NBA championships over the years, the most of any team. Some of their most iconic players have included Bill Russell, Larry Bird, and Kevin McHale. The Celtics are known for their passionate fan base and intense rivalries with teams like the Los Angeles Lakers. It's always exciting to follow such a successful and historic franchise. I'm glad to hear you're a fan of the Celtics!

```


We can see that so far no summarization has happened - this is because there are only six messages in the list. 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-7-1)constvalues=(awaitapp.getState(config)).values
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-7-2)console.log(values)

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-1){
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-2) messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-3)  HumanMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-4)   "content": "hi! I'm bob",
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-5)   "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-6)   "response_metadata": {}
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-7)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-8)  AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-9)   "id": "msg_01G6WKqKHK8W371793Hm6eNM",
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-10)   "content": "Okay, got it. Hello Bob, it's nice to chat with you again. I recognize that you've repeatedly stated your name is Bob throughout our conversation. Please let me know if there is anything I can assist you with.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-11)   "additional_kwargs": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-12)    "id": "msg_01G6WKqKHK8W371793Hm6eNM",
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-13)    "type": "message",
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-14)    "role": "assistant",
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-15)    "model": "claude-3-haiku-20240307",
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-16)    "stop_reason": "end_turn",
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-17)    "stop_sequence": null,
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-18)    "usage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-19)     "input_tokens": 579,
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-20)     "output_tokens": 50
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-21)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-22)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-23)   "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-24)    "id": "msg_01G6WKqKHK8W371793Hm6eNM",
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-25)    "model": "claude-3-haiku-20240307",
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-26)    "stop_reason": "end_turn",
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-27)    "stop_sequence": null,
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-28)    "usage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-29)     "input_tokens": 579,
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-30)     "output_tokens": 50
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-31)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-32)    "type": "message",
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-33)    "role": "assistant"
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-34)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-35)   "tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-36)   "invalid_tool_calls": []
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-37)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-38)  HumanMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-39)   "content": "What did I sat my name was?",
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-40)   "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-41)   "response_metadata": {}
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-42)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-43)  AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-44)   "id": "msg_0118BAsHL4Ew8N2926aYQaot",
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-45)   "content": "In our conversation, you have stated multiple times that your name is Bob. For example, you said \"I'm Bob\", \"hi! I'm bob\", and similar variations where you clearly identified yourself as Bob.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-46)   "additional_kwargs": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-47)    "id": "msg_0118BAsHL4Ew8N2926aYQaot",
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-48)    "type": "message",
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-49)    "role": "assistant",
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-50)    "model": "claude-3-haiku-20240307",
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-51)    "stop_reason": "end_turn",
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-52)    "stop_sequence": null,
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-53)    "usage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-54)     "input_tokens": 310,
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-55)     "output_tokens": 46
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-56)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-57)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-58)   "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-59)    "id": "msg_0118BAsHL4Ew8N2926aYQaot",
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-60)    "model": "claude-3-haiku-20240307",
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-61)    "stop_reason": "end_turn",
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-62)    "stop_sequence": null,
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-63)    "usage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-64)     "input_tokens": 310,
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-65)     "output_tokens": 46
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-66)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-67)    "type": "message",
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-68)    "role": "assistant"
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-69)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-70)   "tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-71)   "invalid_tool_calls": []
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-72)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-73)  HumanMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-74)   "content": "i like the celtics!",
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-75)   "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-76)   "response_metadata": {}
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-77)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-78)  AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-79)   "id": "msg_01RVrMuSvr17kZdepJZb7rZM",
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-80)   "content": "Ah I see, you mentioned earlier that you like the Boston Celtics basketball team. That's great, the Celtics have a long and storied history in the NBA. As one of the league's original franchises, they've won a record 17 NBA championships over the years, the most of any team. Some of their most iconic players have included Bill Russell, Larry Bird, and Kevin McHale. The Celtics are known for their passionate fan base and intense rivalries with teams like the Los Angeles Lakers. It's always exciting to follow such a successful and historic franchise. I'm glad to hear you're a fan of the Celtics!",
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-81)   "additional_kwargs": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-82)    "id": "msg_01RVrMuSvr17kZdepJZb7rZM",
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-83)    "type": "message",
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-84)    "role": "assistant",
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-85)    "model": "claude-3-haiku-20240307",
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-86)    "stop_reason": "end_turn",
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-87)    "stop_sequence": null,
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-88)    "usage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-89)     "input_tokens": 365,
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-90)     "output_tokens": 141
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-91)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-92)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-93)   "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-94)    "id": "msg_01RVrMuSvr17kZdepJZb7rZM",
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-95)    "model": "claude-3-haiku-20240307",
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-96)    "stop_reason": "end_turn",
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-97)    "stop_sequence": null,
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-98)    "usage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-99)     "input_tokens": 365,
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-100)     "output_tokens": 141
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-101)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-102)    "type": "message",
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-103)    "role": "assistant"
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-104)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-105)   "tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-106)   "invalid_tool_calls": []
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-107)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-108) ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-109) summary: 'Got it, let me extend the summary further:\n' +
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-110)  '\n' +
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-111)  `The conversation began with you introducing yourself as Bob, which I acknowledged and said I was happy to chat with you again. You then repeated "I'm Bob", and I confirmed I recognized your name.\n` +
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-112)  '\n' +
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-113)  "You next stated that you like the Boston Celtics basketball team, which prompted me to provide some background information about the team's history and success. \n" +
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-114)  '\n' +
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-115)  'You then summarized the conversation up to that point, which I expanded upon in detail, recapping the key points of our exchange so far.\n' +
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-116)  '\n' +
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-117)  `In the most recent messages, you greeted me again by saying "hi! I'm bob", which I recognized as you reiterating your name, consistent with how you had introduced yourself earlier.\n` +
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-118)  '\n' +
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-119)  `Now, in the latest message, you have simply stated "hi! I'm bob" once more. I continue to understand your name is Bob based on you stating that multiple times throughout our conversation.\n` +
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-120)  '\n' +
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-121)  "Please let me know if I'm still missing anything or if you have any other points you'd like me to add to the summary. I'm happy to keep building on it."
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-8-122)}

```


Now let's send another message in 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-9-1)constinputMessage4=newHumanMessage("i like how much they win")
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-9-2)console.log(inputMessage4.content)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-9-3)forawait(consteventofawaitapp.stream({messages:[inputMessage4]},config)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-9-4)printUpdate(event)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-9-5)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-10-1)i like how much they win
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-10-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-10-3)================================ ai Message =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-10-4)I agree, the Celtics' impressive track record of wins and championships is a big part of what makes them such an iconic and beloved team. Their sustained success over decades is really remarkable. 
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-10-5)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-10-6)Some key reasons why the Celtics have been so dominant:
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-10-7)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-10-8)- Great coaching - They've had legendary coaches like Red Auerbach, Doc Rivers, and Brad Stevens who have led the team to titles.
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-10-9)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-10-10)- Hall of Fame players - Superstars like Bill Russell, Larry Bird, Kevin Garnett, and Paul Pierce have powered the Celtics' championship runs.
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-10-11)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-10-12)- Winning culture - The Celtics have built a winning mentality and tradition of excellence that gets passed down to each new generation of players.
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-10-13)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-10-14)- Loyal fanbase - The passionate Celtics fans pack the stands and provide a strong home court advantage.
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-10-15)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-10-16)The combination of top-tier talent, smart management, and devoted supporters has allowed the Celtics to reign as one of the NBA's premier franchises for generations. Their ability to consistently win at the highest level is truly impressive. I can understand why you as a fan really appreciate and enjoy that aspect of the team.
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-10-17)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-10-18)================================ remove Message =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-10-19)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-10-20)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-10-21)================================ remove Message =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-10-22)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-10-23)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-10-24)================================ remove Message =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-10-25)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-10-26)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-10-27)================================ remove Message =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-10-28)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-10-29)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-10-30)================================ remove Message =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-10-31)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-10-32)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-10-33)================================ remove Message =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-10-34)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-10-35)Okay, let me extend the summary further based on the latest messages:
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-10-36)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-10-37)The conversation began with you introducing yourself as Bob, which I acknowledged. You then repeated "I'm Bob" a few times, and I confirmed I recognized your name.
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-10-38)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-10-39)You then expressed that you like the Boston Celtics basketball team, which led me to provide some background information about the team's history and success. You agreed that you appreciate how much the Celtics win.
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-10-40)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-10-41)In the most recent messages, you greeted me again by saying "hi! I'm bob", reiterating your name just as you had done earlier. I reiterated that I understand your name is Bob based on you stating that multiple times throughout our conversation.
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-10-42)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-10-43)In your latest message, you simply stated "hi! I'm bob" once more, further confirming your name. I have continued to demonstrate that I understand your name is Bob, as you have consistently identified yourself as such.
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-10-44)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-10-45)Please let me know if I'm still missing anything or if you have any other points you'd like me to add to this extended summary of our discussion so far. I'm happy to keep building on it.

```


If we check the state now, we can see that we have a summary of the conversation, as well as the last two messages 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-11-1)constvalues2=(awaitapp.getState(config)).values
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-11-2)console.log(values2)

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-12-1){
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-12-2) messages: [
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-12-3)  HumanMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-12-4)   "content": "i like how much they win",
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-12-5)   "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-12-6)   "response_metadata": {}
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-12-7)  },
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-12-8)  AIMessage {
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-12-9)   "id": "msg_01W8C1nXeydqM3E31uCCeJXt",
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-12-10)   "content": "I agree, the Celtics' impressive track record of wins and championships is a big part of what makes them such an iconic and beloved team. Their sustained success over decades is really remarkable. \n\nSome key reasons why the Celtics have been so dominant:\n\n- Great coaching - They've had legendary coaches like Red Auerbach, Doc Rivers, and Brad Stevens who have led the team to titles.\n\n- Hall of Fame players - Superstars like Bill Russell, Larry Bird, Kevin Garnett, and Paul Pierce have powered the Celtics' championship runs.\n\n- Winning culture - The Celtics have built a winning mentality and tradition of excellence that gets passed down to each new generation of players.\n\n- Loyal fanbase - The passionate Celtics fans pack the stands and provide a strong home court advantage.\n\nThe combination of top-tier talent, smart management, and devoted supporters has allowed the Celtics to reign as one of the NBA's premier franchises for generations. Their ability to consistently win at the highest level is truly impressive. I can understand why you as a fan really appreciate and enjoy that aspect of the team.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-12-11)   "additional_kwargs": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-12-12)    "id": "msg_01W8C1nXeydqM3E31uCCeJXt",
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-12-13)    "type": "message",
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-12-14)    "role": "assistant",
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-12-15)    "model": "claude-3-haiku-20240307",
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-12-16)    "stop_reason": "end_turn",
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-12-17)    "stop_sequence": null,
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-12-18)    "usage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-12-19)     "input_tokens": 516,
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-12-20)     "output_tokens": 244
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-12-21)    }
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-12-22)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-12-23)   "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-12-24)    "id": "msg_01W8C1nXeydqM3E31uCCeJXt",
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-12-25)    "model": "claude-3-haiku-20240307",
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-12-26)    "stop_reason": "end_turn",
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-12-27)    "stop_sequence": null,
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-12-28)    "usage": {
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-12-29)     "input_tokens": 516,
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-12-30)     "output_tokens": 244
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-12-31)    },
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-12-32)    "type": "message",
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-12-33)    "role": "assistant"
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-12-34)   },
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-12-35)   "tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-12-36)   "invalid_tool_calls": []
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-12-37)  }
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-12-38) ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-12-39) summary: 'Okay, let me extend the summary further based on the latest messages:\n' +
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-12-40)  '\n' +
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-12-41)  `The conversation began with you introducing yourself as Bob, which I acknowledged. You then repeated "I'm Bob" a few times, and I confirmed I recognized your name.\n` +
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-12-42)  '\n' +
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-12-43)  "You then expressed that you like the Boston Celtics basketball team, which led me to provide some background information about the team's history and success. You agreed that you appreciate how much the Celtics win.\n" +
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-12-44)  '\n' +
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-12-45)  `In the most recent messages, you greeted me again by saying "hi! I'm bob", reiterating your name just as you had done earlier. I reiterated that I understand your name is Bob based on you stating that multiple times throughout our conversation.\n` +
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-12-46)  '\n' +
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-12-47)  `In your latest message, you simply stated "hi! I'm bob" once more, further confirming your name. I have continued to demonstrate that I understand your name is Bob, as you have consistently identified yourself as such.\n` +
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-12-48)  '\n' +
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-12-49)  "Please let me know if I'm still missing anything or if you have any other points you'd like me to add to this extended summary of our discussion so far. I'm happy to keep building on it."
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-12-50)}

```


We can now resume having a conversation! Note that even though we only have the last two messages, we can still ask it questions about things mentioned earlier in the conversation (because we summarized those) 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-13-1)constinputMessage5=newHumanMessage("what's my name?");
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-13-2)console.log(inputMessage5.content)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-13-3)forawait(consteventofawaitapp.stream({messages:[inputMessage5]},config)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-13-4)printUpdate(event)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-13-5)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-14-1)what's my name?
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-14-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-14-3)================================ ai Message =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-14-4)Your name is Bob. You have stated this multiple times throughout our conversation, repeatedly introducing yourself as "Bob" or "I'm Bob".

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-15-1)constinputMessage6=newHumanMessage("what NFL team do you think I like?");
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-15-2)console.log(inputMessage6.content)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-15-3)forawait(consteventofawaitapp.stream({messages:[inputMessage6]},config)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-15-4)printUpdate(event)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-15-5)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-16-1)what NFL team do you think I like?
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-16-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-16-3)================================ ai Message =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-16-4)I do not actually have any information about what NFL team you might like. In our conversation so far, you have only expressed that you are a fan of the Boston Celtics basketball team. You have not mentioned any preferences for NFL teams. Without you providing any additional details about your football team allegiances, I do not want to make an assumption about which NFL team you might be a fan of. Could you please let me know if there is an NFL team you particularly enjoy following?

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-17-1)constinputMessage7=newHumanMessage("i like the patriots!");
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-17-2)console.log(inputMessage7.content)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-17-3)forawait(consteventofawaitapp.stream({messages:[inputMessage7]},config)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-17-4)printUpdate(event)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-17-5)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-18-1)i like the patriots!
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-18-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-18-3)================================ ai Message =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-18-4)Okay, got it. Based on your latest message, I now understand that in addition to being a fan of the Boston Celtics basketball team, you also like the New England Patriots NFL team.
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-18-5)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-18-6)That makes a lot of sense given that both the Celtics and Patriots are major sports franchises based in the Boston/New England region. It's common for fans to follow multiple professional teams from the same geographic area.
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-18-7)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-18-8)I appreciate you sharing this additional information about your football team preferences. Knowing that you're a Patriots fan provides helpful context about your sports interests and loyalties. It's good for me to have that understanding as we continue our conversation.
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-18-9)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-18-10)Please let me know if there's anything else you'd like to discuss related to the Patriots, the Celtics, or your overall sports fandom. I'm happy to chat more about those topics.
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-18-11)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-18-12)================================ remove Message =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-18-13)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-18-14)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-18-15)================================ remove Message =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-18-16)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-18-17)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-18-18)================================ remove Message =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-18-19)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-18-20)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-18-21)================================ remove Message =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-18-22)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-18-23)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-18-24)================================ remove Message =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-18-25)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-18-26)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-18-27)================================ remove Message =================================
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-18-28)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-18-29)Okay, got it - let me extend the summary further based on the latest messages:
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-18-30)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-18-31)The conversation began with you introducing yourself as Bob, which I acknowledged. You then repeated "I'm Bob" a few times, and I confirmed I recognized your name.
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-18-32)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-18-33)You then expressed that you like the Boston Celtics basketball team, which led me to provide some background information about the team's history and success. You agreed that you appreciate how much the Celtics win.
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-18-34)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-18-35)In the most recent messages, you greeted me again by saying "hi! I'm Bob", reiterating your name just as you had done earlier. I reiterated that I understand your name is Bob based on you stating that multiple times throughout our conversation.
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-18-36)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-18-37)You then asked what NFL team I think you might like, and I acknowledged that I did not have enough information to make an assumption about your NFL team preferences. You then revealed that you are also a fan of the New England Patriots, which I said makes sense given the Celtics and Patriots are both major sports franchises in the Boston/New England region.
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-18-38)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-18-39)In your latest message, you simply stated "hi! I'm Bob" once more, further confirming your name. I have continued to demonstrate that I understand your name is Bob, as you have consistently identified yourself as such.
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-18-40)
[](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__codelineno-18-41)Please let me know if I'm still missing anything or if you have any other points you'd like me to add to this extended summary of our discussion so far. I'm happy to keep building on it.

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to delete messages  ](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/) [ Next  How to add semantic search to your agent's memory  ](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
