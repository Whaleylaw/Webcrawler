---
url: https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#how-to-add-semantic-search-to-your-agents-memory)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to add semantic search to your agent's memory 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/?q= "Share")

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
            * [ How to add summary of the conversation history  ](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/)
            * How to add semantic search to your agent's memory  [ How to add semantic search to your agent's memory  ](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/) Table of contents 
              * [ Using in your agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#using-in-your-agent)
              * [ Advanced Usage  ](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#advanced-usage)
                * [ Multi-vector indexing  ](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#multi-vector-indexing)
                * [ Override fields at storage time  ](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#override-fields-at-storage-time)
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

  * [ Using in your agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#using-in-your-agent)
  * [ Advanced Usage  ](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#advanced-usage)
    * [ Multi-vector indexing  ](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#multi-vector-indexing)
    * [ Override fields at storage time  ](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#override-fields-at-storage-time)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
  5. [ Memory  ](https://langchain-ai.github.io/langgraphjs/how-tos#memory)



# How to add semantic search to your agent's memory[¶](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#how-to-add-semantic-search-to-your-agents-memory "Permanent link")

This guide shows how to enable semantic search in your agent's memory store. This lets search for items in the store by semantic similarity.

First, install this guide's required dependencies.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-0-1)npminstall@langchain/langgraph@langchain/openai@langchain/coreuuidzod

```


Next, we need to set API keys for OpenAI (the LLM we will use)

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-1-1)exportOPENAI_API_KEY=your-api-key

```


Optionally, we can set API key for [LangSmith tracing](https://smith.langchain.com/), which will give us best-in-class observability.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-2-1)exportLANGCHAIN_TRACING_V2="true"
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-2-2)exportLANGCHAIN_CALLBACKS_BACKGROUND="true"
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-2-3)exportLANGCHAIN_API_KEY=your-api-key

```


Next, create the store with an [index configuration](https://langchain-ai.github.io/langgraphjs/reference/interfaces/checkpoint.IndexConfig.html). By default, stores are configured without semantic/vector search. You can opt in to indexing items when creating the store by providing an [IndexConfig](https://langchain-ai.github.io/langgraphjs/reference/interfaces/checkpoint.IndexConfig.html) to the store's constructor. If your store class does not implement this interface, or if you do not pass in an index configuration, semantic search is disabled, and all `index` arguments passed to `put` will have no effect. Below is an example.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-3-1)import{OpenAIEmbeddings}from"@langchain/openai";
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-3-2)import{InMemoryStore}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-3-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-3-4)constembeddings=newOpenAIEmbeddings({
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-3-5)model:"text-embedding-3-small",
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-3-6)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-3-7)
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-3-8)conststore=newInMemoryStore({
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-3-9)index:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-3-10)embeddings,
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-3-11)dims:1536,
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-3-12)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-3-13)});

```


Now let's store some memories:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-4-1)// Store some memories
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-4-2)awaitstore.put(["user_123","memories"],"1",{"text":"I love pizza"})
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-4-3)awaitstore.put(["user_123","memories"],"2",{"text":"I prefer Italian food"})
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-4-4)awaitstore.put(["user_123","memories"],"3",{"text":"I don't like spicy food"})
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-4-5)awaitstore.put(["user_123","memories"],"3",{"text":"I am studying econometrics"})
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-4-6)awaitstore.put(["user_123","memories"],"3",{"text":"I am a plumber"})

```


Search memories using natural language:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-5-1)// Find memories about food preferences
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-5-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-5-3)constmemories=awaitstore.search(["user_123","memories"],{
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-5-4)query:"I like food?",
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-5-5)limit:5,
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-5-6)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-5-7)
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-5-8)for(constmemoryofmemories){
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-5-9)console.log(`Memory: ${memory.value.text} (similarity: ${memory.score})`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-5-10)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-6-1)Memory: I prefer Italian food (similarity: 0.4657744498860293)
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-6-2)Memory: I love pizza (similarity: 0.3743831559964955)
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-6-3)Memory: I am a plumber (similarity: 0.17918150007138176)

```


## Using in your agent[¶](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#using-in-your-agent "Permanent link")

Add semantic search to any node by injecting the store:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-1)import{ChatOpenAI}from"@langchain/openai";
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-2)import{createReactAgent}from"@langchain/langgraph/prebuilt";
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-3)import{MessagesAnnotation,LangGraphRunnableConfig}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-4)import{tool}from"@langchain/core/tools";
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-5)import{getContextVariable}from"@langchain/core/context";
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-7)import{z}from"zod";
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-8)import{v4asuuidv4}from"uuid";
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-9)
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-10)constaddMemories=async(state:typeofMessagesAnnotation.State,config:LangGraphRunnableConfig)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-11)conststore=config.store;
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-12)// Search based on user's last message
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-13)constitems=awaitstore.search(
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-14)["user_123","memories"],
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-15){
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-16)// Assume it's not a complex message
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-17)query:state.messages[state.messages.length-1].contentasstring,
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-18)limit:2
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-19)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-20));
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-21)
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-22)constmemories=items.length
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-23)?`## Memories of user\n${items.map(item=>item.value.text).join("\n")}`
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-24):"";
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-25)
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-26)// Add retrieved memories to system message
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-27)return[
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-28){role:"system",content:`You are a helpful assistant.\n${memories}`},
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-29)...state.messages
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-30)];
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-31)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-32)
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-33)constupsertMemoryTool=tool(async(
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-34)input,
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-35)config:LangGraphRunnableConfig
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-36)):Promise<string>=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-37)conststore=config.store;
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-38)if(!store){
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-39)thrownewError("No store provided to tool.");
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-40)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-41)constmemoryId=getContextVariable("memoryId")||uuidv4();
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-42)awaitstore.put(
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-43)["user_123","memories"],
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-44)memoryId,
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-45){text:input.content}
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-46));
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-47)return`Stored memory ${memoryId}`;
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-48)},{
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-49)name:"upsert_memory",
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-50)schema:z.object({
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-51)content:z.string(),
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-52)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-53)description:"Upsert a memory in the database.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-54)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-55)
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-56)constagent=createReactAgent({
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-57)llm:newChatOpenAI({model:"gpt-4o-mini"}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-58)tools:[upsertMemoryTool],
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-59)stateModifier:addMemories,
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-60)store:store,
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-7-61)});

```


If we run the agent, we can see that it remembers that we added a memory about liking Italian food.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-8-1)conststream=awaitagent.stream({
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-8-2)messages:[{
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-8-3)role:"user",
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-8-4)content:"I'm hungry",
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-8-5)}],
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-8-6)},{
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-8-7)streamMode:"messages",
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-8-8)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-8-9)
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-8-10)forawait(const[message,_metadata]ofstream){
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-8-11)console.log(message.content);
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-8-12)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-9-1)What are you in the mood for? Maybe some Italian food or pizza?

```


## Advanced Usage[¶](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#advanced-usage "Permanent link")

### Multi-vector indexing[¶](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#multi-vector-indexing "Permanent link")

Store and search different aspects of memories separately to improve recall or omit certain fields from being indexed.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-10-1)import{InMemoryStore}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-10-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-10-3)// Configure store to embed both memory content and emotional context
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-10-4)constmultiVectorStore=newInMemoryStore({
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-10-5)index:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-10-6)embeddings:embeddings,
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-10-7)dims:1536,
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-10-8)fields:["memory","emotional_context"],
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-10-9)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-10-10)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-10-11)
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-10-12)// Store memories with different content/emotion pairs
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-10-13)awaitmultiVectorStore.put(["user_123","memories"],"mem1",{
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-10-14)memory:"Had pizza with friends at Mario's",
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-10-15)emotional_context:"felt happy and connected",
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-10-16)this_isnt_indexed:"I prefer ravioli though",
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-10-17)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-10-18)awaitmultiVectorStore.put(["user_123","memories"],"mem2",{
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-10-19)memory:"Ate alone at home",
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-10-20)emotional_context:"felt a bit lonely",
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-10-21)this_isnt_indexed:"I like pie",
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-10-22)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-10-23)
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-10-24)// Search focusing on emotional state - matches mem2
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-10-25)constresults=awaitmultiVectorStore.search(["user_123","memories"],{
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-10-26)query:"times they felt isolated",
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-10-27)limit:1,
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-10-28)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-10-29)
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-10-30)console.log("Expect mem 2");
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-10-31)
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-10-32)for(constrofresults){
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-10-33)console.log(`Item: ${r.key}; Score(${r.score})`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-10-34)console.log(`Memory: ${r.value.memory}`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-10-35)console.log(`Emotion: ${r.value.emotional_context}`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-10-36)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-11-1)Expect mem 2
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-11-2)Item: mem2; Score(0.5895009051069847)
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-11-3)Memory: Ate alone at home
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-11-4)Emotion: felt a bit lonely

```


### Override fields at storage time[¶](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#override-fields-at-storage-time "Permanent link")

You can override which fields to embed when storing a specific memory using `put(..., { index: [...fields] })`, regardless of the store's default configuration.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-12-1)import{InMemoryStore}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-12-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-12-3)constoverrideStore=newInMemoryStore({
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-12-4)index:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-12-5)embeddings:embeddings,
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-12-6)dims:1536,
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-12-7)// Default to embed memory field
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-12-8)fields:["memory"],
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-12-9)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-12-10)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-12-11)
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-12-12)// Store one memory with default indexing
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-12-13)awaitoverrideStore.put(["user_123","memories"],"mem1",{
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-12-14)memory:"I love spicy food",
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-12-15)context:"At a Thai restaurant",
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-12-16)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-12-17)
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-12-18)// Store another overriding which fields to embed
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-12-19)awaitoverrideStore.put(["user_123","memories"],"mem2",{
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-12-20)memory:"I love spicy food",
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-12-21)context:"At a Thai restaurant",
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-12-22)// Override: only embed the context
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-12-23)index:["context"]
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-12-24)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-12-25)
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-12-26)// Search about food - matches mem1 (using default field)
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-12-27)console.log("Expect mem1");
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-12-28)constresults2=awaitoverrideStore.search(["user_123","memories"],{
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-12-29)query:"what food do they like",
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-12-30)limit:1,
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-12-31)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-12-32)
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-12-33)for(constrofresults2){
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-12-34)console.log(`Item: ${r.key}; Score(${r.score})`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-12-35)console.log(`Memory: ${r.value.memory}`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-12-36)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-12-37)
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-12-38)// Search about restaurant atmosphere - matches mem2 (using overridden field)
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-12-39)console.log("Expect mem2");
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-12-40)constresults3=awaitoverrideStore.search(["user_123","memories"],{
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-12-41)query:"restaurant environment",
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-12-42)limit:1,
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-12-43)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-12-44)
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-12-45)for(constrofresults3){
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-12-46)console.log(`Item: ${r.key}; Score(${r.score})`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-12-47)console.log(`Memory: ${r.value.memory}`);
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-12-48)}

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-13-1)Expect mem1
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-13-2)Item: mem1; Score(0.337496867367478)
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-13-3)Memory: I love spicy food
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-13-4)Expect mem2
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-13-5)Item: mem1; Score(0.1921202784760764)
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-13-6)Memory: I love spicy food

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__codelineno-14-1)

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to add summary of the conversation history  ](https://langchain-ai.github.io/langgraphjs/how-tos/add-summary-conversation-history/) [ Next  How to add breakpoints  ](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/semantic-search/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
