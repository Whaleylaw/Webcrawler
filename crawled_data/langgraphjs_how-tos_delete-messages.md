---
url: https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#how-to-delete-messages)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to delete messages 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/?q= "Share")

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
            * How to delete messages  [ How to delete messages  ](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#setup)
              * [ Build the agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#build-the-agent)
              * [ Manually deleting messages  ](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#manually-deleting-messages)
              * [ Programmatically deleting messages  ](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#programmatically-deleting-messages)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#setup)
  * [ Build the agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#build-the-agent)
  * [ Manually deleting messages  ](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#manually-deleting-messages)
  * [ Programmatically deleting messages  ](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#programmatically-deleting-messages)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
  5. [ Memory  ](https://langchain-ai.github.io/langgraphjs/how-tos#memory)



# How to delete messages[¶](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#how-to-delete-messages "Permanent link")

One of the common states for a graph is a list of messages. Usually you only add messages to that state. However, sometimes you may want to remove messages (either by directly modifying the state or as part of the graph). To do that, you can use the `RemoveMessage` modifier. In this guide, we will cover how to do that.

The key idea is that each state key has a `reducer` key. This key specifies how to combine updates to the state. The prebuilt `MessagesAnnotation`[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#messagesannotation) has a messages key, and the reducer for that key accepts these `RemoveMessage` modifiers. That reducer then uses these `RemoveMessage` to delete messages from the key.

So note that just because your graph state has a key that is a list of messages, it doesn't mean that that this `RemoveMessage` modifier will work. You also have to have a `reducer` defined that knows how to work with this.

**NOTE** : Many models expect certain rules around lists of messages. For example, some expect them to start with a `user` message, others expect all messages with tool calls to be followed by a tool message. **When deleting messages, you will want to make sure you don't violate these rules.**

## Setup[¶](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#setup "Permanent link")

First, install the required dependencies for this example:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-0-1)npminstall@langchain/langgraph@langchain/openai@langchain/corezoduuid

```


Next, we need to set API keys for OpenAI (the LLM we will use):

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-1-1)process.env.OPENAI_API_KEY='YOUR_API_KEY';

```


Optionally, we can set API key for [LangSmith tracing](https://smith.langchain.com/), which will give us best-in-class observability.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-2-1)process.env.LANGCHAIN_TRACING_V2="true";
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-2-2)process.env.LANGCHAIN_API_KEY="YOUR_API_KEY";

```


Now, let's build a simple graph that uses messages.

## Build the agent[¶](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#build-the-agent "Permanent link")

Let's now build a simple ReAct style agent.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-1)import{ChatOpenAI}from"@langchain/openai";
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-2)import{tool}from"@langchain/core/tools";
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-3)import{MemorySaver}from"@langchain/langgraph-checkpoint";
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-4)import{MessagesAnnotation,StateGraph,START,END}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-5)import{ToolNode}from"@langchain/langgraph/prebuilt";
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-6)import{z}from"zod";
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-7)
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-8)constmemory=newMemorySaver();
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-9)
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-10)constsearch=tool((_)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-11)// This is a placeholder for the actual implementation
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-12)// Don't let the LLM know this though 😊
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-13)return[
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-14)"It's sunny in San Francisco, but you better look out if you're a Gemini 😈.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-15)];
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-16)},{
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-17)name:"search",
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-18)description:"Call to surf the web.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-19)schema:z.object({
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-20)query:z.string(),
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-21)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-22)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-23)
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-24)consttools=[search];
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-25)consttoolNode=newToolNode<typeofMessagesAnnotation.State>(tools);
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-26)constmodel=newChatOpenAI({model:"gpt-4o"});
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-27)constboundModel=model.bindTools(tools);
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-28)
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-29)functionshouldContinue(state:typeofMessagesAnnotation.State):"action"|typeofEND{
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-30)constlastMessage=state.messages[state.messages.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-31)if(
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-32)"tool_calls"inlastMessage&&
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-33)Array.isArray(lastMessage.tool_calls)&&
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-34)lastMessage.tool_calls.length
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-35)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-36)return"action";
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-37)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-38)// If there is no tool call, then we finish
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-39)returnEND;
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-40)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-41)
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-42)// Define the function that calls the model
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-43)asyncfunctioncallModel(state:typeofMessagesAnnotation.State){
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-44)constresponse=awaitboundModel.invoke(state.messages);
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-45)return{messages:[response]};
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-46)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-47)
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-48)// Define a new graph
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-49)constworkflow=newStateGraph(MessagesAnnotation)
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-50)// Define the two nodes we will cycle between
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-51).addNode("agent",callModel)
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-52).addNode("action",toolNode)
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-53)// Set the entrypoint as `agent`
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-54)// This means that this node is the first one called
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-55).addEdge(START,"agent")
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-56)// We now add a conditional edge
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-57).addConditionalEdges(
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-58)// First, we define the start node. We use `agent`.
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-59)// This means these are the edges taken after the `agent` node is called.
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-60)"agent",
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-61)// Next, we pass in the function that will determine which node is called next.
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-62)shouldContinue
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-63))
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-64)// We now add a normal edge from `tools` to `agent`.
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-65)// This means that after `tools` is called, `agent` node is called next.
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-66).addEdge("action","agent");
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-67)
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-68)// Finally, we compile it!
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-69)// This compiles it into a LangChain Runnable,
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-70)// meaning you can use it as you would any other runnable
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-3-71)constapp=workflow.compile({checkpointer:memory});

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-4-1)import{HumanMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-4-2)import{v4asuuidv4}from"uuid";
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-4-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-4-4)constconfig={configurable:{thread_id:"2"},streamMode:"values"asconst};
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-4-5)constinputMessage=newHumanMessage({
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-4-6)id:uuidv4(),
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-4-7)content:"hi! I'm bob",
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-4-8)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-4-9)
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-4-10)forawait(consteventofawaitapp.stream(
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-4-11){messages:[inputMessage]},
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-4-12)config,
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-4-13))){
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-4-14)constlastMsg=event.messages[event.messages.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-4-15)console.dir(
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-4-16){
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-4-17)type:lastMsg._getType(),
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-4-18)content:lastMsg.content,
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-4-19)tool_calls:lastMsg.tool_calls,
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-4-20)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-4-21){depth:null}
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-4-22))
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-4-23)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-4-24)
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-4-25)constinputMessage2=newHumanMessage({
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-4-26)id:uuidv4(),
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-4-27)content:"What's my name?",
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-4-28)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-4-29)forawait(consteventofawaitapp.stream(
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-4-30){messages:[inputMessage2]},
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-4-31)config,
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-4-32))){
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-4-33)constlastMsg=event.messages[event.messages.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-4-34)console.dir(
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-4-35){
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-4-36)type:lastMsg._getType(),
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-4-37)content:lastMsg.content,
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-4-38)tool_calls:lastMsg.tool_calls,
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-4-39)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-4-40){depth:null}
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-4-41))
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-4-42)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-5-1){ type: 'human', content: "hi! I'm bob", tool_calls: undefined }
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-5-2){
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-5-3) type: 'ai',
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-5-4) content: 'Hi Bob! How can I assist you today?',
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-5-5) tool_calls: []
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-5-6)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-5-7){ type: 'human', content: "What's my name?", tool_calls: undefined }
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-5-8){ type: 'ai', content: 'Your name is Bob.', tool_calls: [] }

```


## Manually deleting messages[¶](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#manually-deleting-messages "Permanent link")

First, we will cover how to manually delete messages. Let's take a look at the current state of the thread:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-6-1)constmessages=(awaitapp.getState(config)).values.messages;
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-6-2)console.dir(
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-6-3)messages.map((msg)=>({
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-6-4)id:msg.id,
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-6-5)type:msg._getType(),
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-6-6)content:msg.content,
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-6-7)tool_calls:
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-6-8)msg.tool_calls,
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-6-9)})),
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-6-10){depth:null}
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-6-11));

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-7-1)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-7-2) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-7-3)  id: '24187daa-00dd-40d8-bc30-f4e24ff78165',
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-7-4)  type: 'human',
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-7-5)  content: "hi! I'm bob",
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-7-6)  tool_calls: undefined
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-7-7) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-7-8) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-7-9)  id: 'chatcmpl-9zYV9yHLiZmR2ZVHEhHcbVEshr3qG',
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-7-10)  type: 'ai',
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-7-11)  content: 'Hi Bob! How can I assist you today?',
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-7-12)  tool_calls: []
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-7-13) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-7-14) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-7-15)  id: 'a67e53c3-5dcf-4ddc-83f5-309b72ac61f4',
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-7-16)  type: 'human',
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-7-17)  content: "What's my name?",
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-7-18)  tool_calls: undefined
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-7-19) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-7-20) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-7-21)  id: 'chatcmpl-9zYV9mmpJrm3SQ7ngMJZ1XBHzHfL6',
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-7-22)  type: 'ai',
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-7-23)  content: 'Your name is Bob.',
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-7-24)  tool_calls: []
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-7-25) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-7-26)]

```


We can call `updateState` and pass in the id of the first message. This will delete that message. 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-8-1)import{RemoveMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-8-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-8-3)awaitapp.updateState(config,{messages:newRemoveMessage({id:messages[0].id})})

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-9-1){
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-9-2) configurable: {
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-9-3)  thread_id: '2',
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-9-4)  checkpoint_ns: '',
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-9-5)  checkpoint_id: '1ef61abf-1fc2-6431-8005-92730e9d667c'
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-9-6) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-9-7)}

```


If we now look at the messages, we can verify that the first one was deleted. 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-10-1)constupdatedMessages=(awaitapp.getState(config)).values.messages;
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-10-2)console.dir(
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-10-3)updatedMessages.map((msg)=>({
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-10-4)id:msg.id,
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-10-5)type:msg._getType(),
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-10-6)content:msg.content,
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-10-7)tool_calls:
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-10-8)msg.tool_calls,
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-10-9)})),
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-10-10){depth:null}
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-10-11));

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-11-1)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-11-2) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-11-3)  id: 'chatcmpl-9zYV9yHLiZmR2ZVHEhHcbVEshr3qG',
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-11-4)  type: 'ai',
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-11-5)  content: 'Hi Bob! How can I assist you today?',
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-11-6)  tool_calls: []
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-11-7) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-11-8) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-11-9)  id: 'a67e53c3-5dcf-4ddc-83f5-309b72ac61f4',
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-11-10)  type: 'human',
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-11-11)  content: "What's my name?",
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-11-12)  tool_calls: undefined
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-11-13) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-11-14) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-11-15)  id: 'chatcmpl-9zYV9mmpJrm3SQ7ngMJZ1XBHzHfL6',
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-11-16)  type: 'ai',
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-11-17)  content: 'Your name is Bob.',
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-11-18)  tool_calls: []
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-11-19) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-11-20)]

```


## Programmatically deleting messages[¶](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#programmatically-deleting-messages "Permanent link")

We can also delete messages programmatically from inside the graph. Here we'll modify the graph to delete any old messages (longer than 3 messages ago) at the end of a graph run.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-12-1)import{RemoveMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-12-2)import{StateGraph,START,END}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-12-3)import{MessagesAnnotation}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-12-4)
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-12-5)functiondeleteMessages(state:typeofMessagesAnnotation.State){
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-12-6)constmessages=state.messages;
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-12-7)if(messages.length>3){
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-12-8)return{messages:messages.slice(0,-3).map(m=>newRemoveMessage({id:m.id}))};
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-12-9)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-12-10)return{};
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-12-11)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-12-12)
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-12-13)// We need to modify the logic to call deleteMessages rather than end right away
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-12-14)functionshouldContinue2(state:typeofMessagesAnnotation.State):"action"|"delete_messages"{
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-12-15)constlastMessage=state.messages[state.messages.length-1];
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-12-16)if(
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-12-17)"tool_calls"inlastMessage&&
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-12-18)Array.isArray(lastMessage.tool_calls)&&
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-12-19)lastMessage.tool_calls.length
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-12-20)){
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-12-21)return"action";
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-12-22)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-12-23)// Otherwise if there aren't, we finish
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-12-24)return"delete_messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-12-25)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-12-26)
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-12-27)// Define a new graph
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-12-28)constworkflow2=newStateGraph(MessagesAnnotation)
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-12-29).addNode("agent",callModel)
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-12-30).addNode("action",toolNode)
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-12-31)// This is our new node we're defining
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-12-32).addNode("delete_messages",deleteMessages)
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-12-33).addEdge(START,"agent")
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-12-34).addConditionalEdges(
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-12-35)"agent",
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-12-36)shouldContinue2
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-12-37))
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-12-38).addEdge("action","agent")
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-12-39)// This is the new edge we're adding: after we delete messages, we finish
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-12-40).addEdge("delete_messages",END);
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-12-41)
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-12-42)constapp2=workflow2.compile({checkpointer:memory});

```


We can now try this out. We can call the graph twice and then check the state

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-13-1)import{HumanMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-13-2)import{v4asuuidv4}from"uuid";
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-13-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-13-4)constconfig2={configurable:{thread_id:"3"},streamMode:"values"asconst};
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-13-5)
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-13-6)constinputMessage3=newHumanMessage({
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-13-7)id:uuidv4(),
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-13-8)content:"hi! I'm bob",
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-13-9)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-13-10)
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-13-11)console.log("--- FIRST ITERATION ---\n");
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-13-12)forawait(consteventofawaitapp2.stream(
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-13-13){messages:[inputMessage3]},
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-13-14)config2
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-13-15))){
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-13-16)console.log(event.messages.map((message)=>[message._getType(),message.content]));
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-13-17)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-13-18)
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-13-19)constinputMessage4=newHumanMessage({
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-13-20)id:uuidv4(),
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-13-21)content:"what's my name?",
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-13-22)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-13-23)
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-13-24)console.log("\n\n--- SECOND ITERATION ---\n");
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-13-25)forawait(consteventofawaitapp2.stream(
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-13-26){messages:[inputMessage4]},
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-13-27)config2
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-13-28))){
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-13-29)console.log(event.messages.map((message)=>[message._getType(),message.content]),"\n");
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-13-30)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-14-1)--- FIRST ITERATION ---
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-14-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-14-3)[ [ 'human', "hi! I'm bob" ] ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-14-4)``````output
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-14-5)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-14-6) [ 'human', "hi! I'm bob" ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-14-7) [ 'ai', 'Hi Bob! How can I assist you today?' ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-14-8)]
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-14-9)
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-14-10)
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-14-11)--- SECOND ITERATION ---
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-14-12)
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-14-13)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-14-14) [ 'human', "hi! I'm bob" ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-14-15) [ 'ai', 'Hi Bob! How can I assist you today?' ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-14-16) [ 'human', "what's my name?" ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-14-17)] 
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-14-18)
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-14-19)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-14-20) [ 'human', "hi! I'm bob" ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-14-21) [ 'ai', 'Hi Bob! How can I assist you today?' ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-14-22) [ 'human', "what's my name?" ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-14-23) [ 'ai', "Based on what you've told me, your name is Bob." ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-14-24)] 
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-14-25)
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-14-26)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-14-27) [ 'ai', 'Hi Bob! How can I assist you today?' ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-14-28) [ 'human', "what's my name?" ],
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-14-29) [ 'ai', "Based on what you've told me, your name is Bob." ]
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-14-30)]

```


If we now check the state, we should see that it is only three messages long. This is because we just deleted the earlier messages - otherwise it would be four! 

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-15-1)constmessages3=(awaitapp.getState(config2)).values["messages"]
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-15-2)console.dir(
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-15-3)messages3.map((msg)=>({
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-15-4)id:msg.id,
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-15-5)type:msg._getType(),
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-15-6)content:msg.content,
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-15-7)tool_calls:
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-15-8)msg.tool_calls,
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-15-9)})),
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-15-10){depth:null}
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-15-11));

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-16-1)[
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-16-2) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-16-3)  id: 'chatcmpl-9zYVAEiiC9D7bb0wF4KLXgY0OAG8O',
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-16-4)  type: 'ai',
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-16-5)  content: 'Hi Bob! How can I assist you today?',
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-16-6)  tool_calls: []
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-16-7) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-16-8) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-16-9)  id: 'b93e5f35-cfa3-4ca6-9b59-154ce2bd476b',
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-16-10)  type: 'human',
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-16-11)  content: "what's my name?",
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-16-12)  tool_calls: undefined
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-16-13) },
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-16-14) {
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-16-15)  id: 'chatcmpl-9zYVBHJWtEM6pw2koE8dykzSA0XSO',
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-16-16)  type: 'ai',
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-16-17)  content: "Based on what you've told me, your name is Bob.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-16-18)  tool_calls: []
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-16-19) }
[](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__codelineno-16-20)]

```


Remember, when deleting messages you will want to make sure that the remaining message list is still valid. This message list **may actually not be** - this is because it currently starts with an AI message, which some models do not allow.  Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to manage conversation history  ](https://langchain-ai.github.io/langgraphjs/how-tos/manage-conversation-history/) [ Next  How to add summary of the conversation history  ](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
