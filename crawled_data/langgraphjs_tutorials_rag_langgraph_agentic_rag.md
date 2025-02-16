---
url: https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#langgraph-retrieval-agent)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

LangGraph Retrieval Agent 

[ ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/?q= "Share")

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
      * [ Concepts  ](https://langchain-ai.github.io/langgraphjs/concepts/)
      * [ Tutorials  ](https://langchain-ai.github.io/langgraphjs/tutorials/)

Tutorials 
        * [ Quick Start  ](https://langchain-ai.github.io/langgraphjs/tutorials#quick-start)
        * [ Chatbots  ](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/)
        * RAG  RAG 
          * [ RAG  ](https://langchain-ai.github.io/langgraphjs/tutorials#rag)
          * LangGraph Retrieval Agent  [ LangGraph Retrieval Agent  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/) Table of contents 
            * [ Setup  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#setup)
              * [ Load env vars  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#load-env-vars)
              * [ Install dependencies  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#install-dependencies)
            * [ Retriever  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#retriever)
            * [ Agent state  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#agent-state)
            * [ Nodes and Edges  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#nodes-and-edges)
              * [ Edges  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#edges)
            * [ Graph  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#graph)
          * [ Corrective RAG (CRAG)  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/)
          * [ Self-RAG  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/)
        * [ Agent Architectures  ](https://langchain-ai.github.io/langgraphjs/tutorials#agent-architectures)
        * [ Evaluation & Analysis  ](https://langchain-ai.github.io/langgraphjs/tutorials#evaluation)
    * Resources  Resources 
      * [ Adopters  ](https://langchain-ai.github.io/langgraphjs/adopters/)
      * [ FAQ  ](https://langchain-ai.github.io/langgraphjs/concepts/faq/)
      * [ Troubleshooting  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraphjs/reference/)
  * [ Versions  ](https://langchain-ai.github.io/langgraphjs/versions/)



Table of contents 

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#setup)
    * [ Load env vars  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#load-env-vars)
    * [ Install dependencies  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#install-dependencies)
  * [ Retriever  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#retriever)
  * [ Agent state  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#agent-state)
  * [ Nodes and Edges  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#nodes-and-edges)
    * [ Edges  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#edges)
  * [ Graph  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#graph)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ Tutorials  ](https://langchain-ai.github.io/langgraphjs/tutorials/)
  4. [ RAG  ](https://langchain-ai.github.io/langgraphjs/tutorials#rag)



# LangGraph Retrieval Agent[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#langgraph-retrieval-agent "Permanent link")

We can implement [Retrieval Agents](https://js.langchain.com/docs/tutorials/rag/) in [LangGraph](https://js.langchain.com/docs/langgraph).

## Setup[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#setup "Permanent link")

### Load env vars[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#load-env-vars "Permanent link")

Add a `.env` variable in the root of the `./examples` folder with your variables.

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-0-1)// import dotenv from 'dotenv';
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-0-2)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-0-3)// dotenv.config();

```


### Install dependencies[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#install-dependencies "Permanent link")

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-1-1)npminstallcheeriozodzod-to-json-schemalangchain@langchain/openai@langchain/core@langchain/community@langchain/textsplitters

```


## Retriever[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#retriever "Permanent link")

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-2-1)import{CheerioWebBaseLoader}from"@langchain/community/document_loaders/web/cheerio";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-2-2)import{RecursiveCharacterTextSplitter}from"@langchain/textsplitters";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-2-3)import{MemoryVectorStore}from"langchain/vectorstores/memory";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-2-4)import{OpenAIEmbeddings}from"@langchain/openai";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-2-5)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-2-6)consturls=[
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-2-7)"https://lilianweng.github.io/posts/2023-06-23-agent/",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-2-8)"https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-2-9)"https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-2-10)];
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-2-11)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-2-12)constdocs=awaitPromise.all(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-2-13)urls.map((url)=>newCheerioWebBaseLoader(url).load()),
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-2-14));
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-2-15)constdocsList=docs.flat();
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-2-16)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-2-17)consttextSplitter=newRecursiveCharacterTextSplitter({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-2-18)chunkSize:500,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-2-19)chunkOverlap:50,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-2-20)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-2-21)constdocSplits=awaittextSplitter.splitDocuments(docsList);
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-2-22)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-2-23)// Add to vectorDB
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-2-24)constvectorStore=awaitMemoryVectorStore.fromDocuments(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-2-25)docSplits,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-2-26)newOpenAIEmbeddings(),
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-2-27));
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-2-28)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-2-29)constretriever=vectorStore.asRetriever();

```


## Agent state[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#agent-state "Permanent link")

We will define a graph.

You may pass a custom `state` object to the graph, or use a simple list of `messages`.

Our state will be a list of `messages`.

Each node in our graph will append to it.

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-3-1)import{Annotation}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-3-2)import{BaseMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-3-3)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-3-4)constGraphState=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-3-5)messages:Annotation<BaseMessage[]>({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-3-6)reducer:(x,y)=>x.concat(y),
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-3-7)default:()=>[],
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-3-8)})
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-3-9)})

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-4-1)import{createRetrieverTool}from"langchain/tools/retriever";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-4-2)import{ToolNode}from"@langchain/langgraph/prebuilt";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-4-3)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-4-4)consttool=createRetrieverTool(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-4-5)retriever,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-4-6){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-4-7)name:"retrieve_blog_posts",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-4-8)description:
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-4-9)"Search and return information about Lilian Weng blog posts on LLM agents, prompt engineering, and adversarial attacks on LLMs.",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-4-10)},
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-4-11));
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-4-12)consttools=[tool];
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-4-13)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-4-14)consttoolNode=newToolNode<typeofGraphState.State>(tools);

```


## Nodes and Edges[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#nodes-and-edges "Permanent link")

Each node will -

1/ Either be a function or a runnable.

2/ Modify the `state`.

The edges choose which node to call next.

We can lay out an agentic RAG graph like this:

![image-2.png]()

### Edges[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#edges "Permanent link")

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-1)import{END}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-2)import{pull}from"langchain/hub";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-3)import{z}from"zod";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-4)import{ChatPromptTemplate}from"@langchain/core/prompts";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-5)import{ChatOpenAI}from"@langchain/openai";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-6)import{AIMessage,BaseMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-7)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-8)/**
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-9) * Decides whether the agent should retrieve more information or end the process.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-10) * This function checks the last message in the state for a function call. If a tool call is
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-11) * present, the process continues to retrieve information. Otherwise, it ends the process.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-12) * @param {typeof GraphState.State} state - The current state of the agent, including all messages.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-13) * @returns {string} - A decision to either "continue" the retrieval process or "end" it.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-14) */
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-15)functionshouldRetrieve(state:typeofGraphState.State):string{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-16)const{messages}=state;
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-17)console.log("---DECIDE TO RETRIEVE---");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-18)constlastMessage=messages[messages.length-1];
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-19)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-20)if("tool_calls"inlastMessage&&Array.isArray(lastMessage.tool_calls)&&lastMessage.tool_calls.length){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-21)console.log("---DECISION: RETRIEVE---");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-22)return"retrieve";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-23)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-24)// If there are no tool calls then we finish.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-25)returnEND;
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-26)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-27)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-28)/**
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-29) * Determines whether the Agent should continue based on the relevance of retrieved documents.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-30) * This function checks if the last message in the conversation is of type FunctionMessage, indicating
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-31) * that document retrieval has been performed. It then evaluates the relevance of these documents to the user's
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-32) * initial question using a predefined model and output parser. If the documents are relevant, the conversation
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-33) * is considered complete. Otherwise, the retrieval process is continued.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-34) * @param {typeof GraphState.State} state - The current state of the agent, including all messages.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-35) * @returns {Promise<Partial<typeof GraphState.State>>} - The updated state with the new message added to the list of messages.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-36) */
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-37)asyncfunctiongradeDocuments(state:typeofGraphState.State):Promise<Partial<typeofGraphState.State>>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-38)console.log("---GET RELEVANCE---");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-39)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-40)const{messages}=state;
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-41)consttool={
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-42)name:"give_relevance_score",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-43)description:"Give a relevance score to the retrieved documents.",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-44)schema:z.object({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-45)binaryScore:z.string().describe("Relevance score 'yes' or 'no'"),
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-46)})
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-47)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-48)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-49)constprompt=ChatPromptTemplate.fromTemplate(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-50)`You are a grader assessing relevance of retrieved docs to a user question.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-51) Here are the retrieved docs:
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-52) \n ------- \n
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-53) {context} 
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-54) \n ------- \n
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-55) Here is the user question: {question}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-56) If the content of the docs are relevant to the users question, score them as relevant.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-57) Give a binary score 'yes' or 'no' score to indicate whether the docs are relevant to the question.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-58) Yes: The docs are relevant to the question.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-59) No: The docs are not relevant to the question.`,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-60));
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-61)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-62)constmodel=newChatOpenAI({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-63)model:"gpt-4o",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-64)temperature:0,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-65)}).bindTools([tool],{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-66)tool_choice:tool.name,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-67)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-68)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-69)constchain=prompt.pipe(model);
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-70)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-71)constlastMessage=messages[messages.length-1];
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-72)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-73)constscore=awaitchain.invoke({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-74)question:messages[0].contentasstring,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-75)context:lastMessage.contentasstring,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-76)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-77)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-78)return{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-79)messages:[score]
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-80)};
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-81)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-82)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-83)/**
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-84) * Check the relevance of the previous LLM tool call.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-85) *
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-86) * @param {typeof GraphState.State} state - The current state of the agent, including all messages.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-87) * @returns {string} - A directive to either "yes" or "no" based on the relevance of the documents.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-88) */
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-89)functioncheckRelevance(state:typeofGraphState.State):string{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-90)console.log("---CHECK RELEVANCE---");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-91)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-92)const{messages}=state;
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-93)constlastMessage=messages[messages.length-1];
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-94)if(!("tool_calls"inlastMessage)){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-95)thrownewError("The 'checkRelevance' node requires the most recent message to contain tool calls.")
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-96)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-97)consttoolCalls=(lastMessageasAIMessage).tool_calls;
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-98)if(!toolCalls||!toolCalls.length){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-99)thrownewError("Last message was not a function message");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-100)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-101)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-102)if(toolCalls[0].args.binaryScore==="yes"){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-103)console.log("---DECISION: DOCS RELEVANT---");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-104)return"yes";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-105)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-106)console.log("---DECISION: DOCS NOT RELEVANT---");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-107)return"no";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-108)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-109)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-110)// Nodes
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-111)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-112)/**
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-113) * Invokes the agent model to generate a response based on the current state.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-114) * This function calls the agent model to generate a response to the current conversation state.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-115) * The response is added to the state's messages.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-116) * @param {typeof GraphState.State} state - The current state of the agent, including all messages.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-117) * @returns {Promise<Partial<typeof GraphState.State>>} - The updated state with the new message added to the list of messages.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-118) */
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-119)asyncfunctionagent(state:typeofGraphState.State):Promise<Partial<typeofGraphState.State>>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-120)console.log("---CALL AGENT---");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-121)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-122)const{messages}=state;
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-123)// Find the AIMessage which contains the `give_relevance_score` tool call,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-124)// and remove it if it exists. This is because the agent does not need to know
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-125)// the relevance score.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-126)constfilteredMessages=messages.filter((message)=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-127)if("tool_calls"inmessage&&Array.isArray(message.tool_calls)&&message.tool_calls.length>0){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-128)returnmessage.tool_calls[0].name!=="give_relevance_score";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-129)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-130)returntrue;
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-131)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-132)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-133)constmodel=newChatOpenAI({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-134)model:"gpt-4o",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-135)temperature:0,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-136)streaming:true,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-137)}).bindTools(tools);
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-138)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-139)constresponse=awaitmodel.invoke(filteredMessages);
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-140)return{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-141)messages:[response],
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-142)};
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-143)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-144)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-145)/**
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-146) * Transform the query to produce a better question.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-147) * @param {typeof GraphState.State} state - The current state of the agent, including all messages.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-148) * @returns {Promise<Partial<typeof GraphState.State>>} - The updated state with the new message added to the list of messages.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-149) */
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-150)asyncfunctionrewrite(state:typeofGraphState.State):Promise<Partial<typeofGraphState.State>>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-151)console.log("---TRANSFORM QUERY---");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-152)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-153)const{messages}=state;
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-154)constquestion=messages[0].contentasstring;
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-155)constprompt=ChatPromptTemplate.fromTemplate(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-156)`Look at the input and try to reason about the underlying semantic intent / meaning. \n 
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-157)Here is the initial question:
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-158)\n ------- \n
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-159){question} 
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-160)\n ------- \n
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-161)Formulate an improved question:`,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-162));
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-163)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-164)// Grader
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-165)constmodel=newChatOpenAI({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-166)model:"gpt-4o",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-167)temperature:0,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-168)streaming:true,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-169)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-170)constresponse=awaitprompt.pipe(model).invoke({question});
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-171)return{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-172)messages:[response],
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-173)};
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-174)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-175)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-176)/**
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-177) * Generate answer
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-178) * @param {typeof GraphState.State} state - The current state of the agent, including all messages.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-179) * @returns {Promise<Partial<typeof GraphState.State>>} - The updated state with the new message added to the list of messages.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-180) */
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-181)asyncfunctiongenerate(state:typeofGraphState.State):Promise<Partial<typeofGraphState.State>>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-182)console.log("---GENERATE---");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-183)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-184)const{messages}=state;
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-185)constquestion=messages[0].contentasstring;
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-186)// Extract the most recent ToolMessage
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-187)constlastToolMessage=messages.slice().reverse().find((msg)=>msg._getType()==="tool");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-188)if(!lastToolMessage){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-189)thrownewError("No tool message found in the conversation history");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-190)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-191)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-192)constdocs=lastToolMessage.contentasstring;
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-193)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-194)constprompt=awaitpull<ChatPromptTemplate>("rlm/rag-prompt");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-195)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-196)constllm=newChatOpenAI({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-197)model:"gpt-4o",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-198)temperature:0,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-199)streaming:true,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-200)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-201)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-202)constragChain=prompt.pipe(llm);
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-203)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-204)constresponse=awaitragChain.invoke({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-205)context:docs,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-206)question,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-207)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-208)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-209)return{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-210)messages:[response],
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-211)};
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-212)}

```


## Graph[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#graph "Permanent link")

  * Start with an agent, `callModel`
  * Agent make a decision to call a function
  * If so, then `action` to call tool (retriever)
  * Then call agent with the tool output added to messages (`state`)



```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-6-1)import{StateGraph}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-6-2)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-6-3)// Define the graph
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-6-4)constworkflow=newStateGraph(GraphState)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-6-5)// Define the nodes which we'll cycle between.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-6-6).addNode("agent",agent)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-6-7).addNode("retrieve",toolNode)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-6-8).addNode("gradeDocuments",gradeDocuments)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-6-9).addNode("rewrite",rewrite)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-6-10).addNode("generate",generate);

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-1)import{START}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-2)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-3)// Call agent node to decide to retrieve or not
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-4)workflow.addEdge(START,"agent");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-5)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-6)// Decide whether to retrieve
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-7)workflow.addConditionalEdges(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-8)"agent",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-9)// Assess agent decision
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-10)shouldRetrieve,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-11));
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-12)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-13)workflow.addEdge("retrieve","gradeDocuments");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-14)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-15)// Edges taken after the `action` node is called.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-16)workflow.addConditionalEdges(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-17)"gradeDocuments",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-18)// Assess agent decision
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-19)checkRelevance,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-20){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-21)// Call tool node
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-22)yes:"generate",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-23)no:"rewrite",// placeholder
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-24)},
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-25));
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-26)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-27)workflow.addEdge("generate",END);
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-28)workflow.addEdge("rewrite","agent");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-29)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-30)// Compile
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-31)constapp=workflow.compile();

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-8-1)import{HumanMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-8-2)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-8-3)constinputs={
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-8-4)messages:[
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-8-5)newHumanMessage(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-8-6)"What are the types of agent memory based on Lilian Weng's blog post?",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-8-7)),
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-8-8)],
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-8-9)};
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-8-10)letfinalState;
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-8-11)forawait(constoutputofawaitapp.stream(inputs)){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-8-12)for(const[key,value]ofObject.entries(output)){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-8-13)constlastMsg=output[key].messages[output[key].messages.length-1];
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-8-14)console.log(`Output from node: '${key}'`);
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-8-15)console.dir({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-8-16)type:lastMsg._getType(),
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-8-17)content:lastMsg.content,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-8-18)tool_calls:lastMsg.tool_calls,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-8-19)},{depth:null});
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-8-20)console.log("---\n");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-8-21)finalState=value;
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-8-22)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-8-23)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-8-24)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-8-25)console.log(JSON.stringify(finalState,null,2));

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-1)---CALL AGENT---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-2)---DECIDE TO RETRIEVE---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-3)---DECISION: RETRIEVE---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-4)Output from node: 'agent'
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-5){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-6) type: 'ai',
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-7) content: '',
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-8) tool_calls: [
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-9)  {
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-10)   name: 'retrieve_blog_posts',
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-11)   args: { query: 'types of agent memory' },
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-12)   id: 'call_adLYkV7T2ry1EZFboT0jPuwn',
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-13)   type: 'tool_call'
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-14)  }
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-15) ]
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-16)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-17)---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-18)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-19)Output from node: 'retrieve'
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-20){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-21) type: 'tool',
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-22) content: 'Agent System Overview\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-23)  '        \n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-24)  '          Component One: Planning\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-25)  '            \n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-26)  '        \n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-27)  '          Task Decomposition\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-28)  '        \n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-29)  '          Self-Reflection\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-30)  '        \n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-31)  '        \n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-32)  '          Component Two: Memory\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-33)  '            \n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-34)  '        \n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-35)  '          Types of Memory\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-36)  '        \n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-37)  '          Maximum Inner Product Search (MIPS)\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-38)  '\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-39)  'Memory stream: is a long-term memory module (external database) that records a comprehensive list of agents’ experience in natural language.\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-40)  '\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-41)  'Each element is an observation, an event directly provided by the agent.\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-42)  '- Inter-agent communication can trigger new natural language statements.\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-43)  '\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-44)  '\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-45)  'Retrieval model: surfaces the context to inform the agent’s behavior, according to relevance, recency and importance.\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-46)  '\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-47)  'Planning\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-48)  '\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-49)  'Subgoal and decomposition: The agent breaks down large tasks into smaller, manageable subgoals, enabling efficient handling of complex tasks.\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-50)  'Reflection and refinement: The agent can do self-criticism and self-reflection over past actions, learn from mistakes and refine them for future steps, thereby improving the quality of final results.\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-51)  '\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-52)  '\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-53)  'Memory\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-54)  '\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-55)  'The design of generative agents combines LLM with memory, planning and reflection mechanisms to enable agents to behave conditioned on past experience, as well as to interact with other agents.',
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-56) tool_calls: undefined
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-57)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-58)---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-59)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-60)---GET RELEVANCE---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-61)---CHECK RELEVANCE---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-62)---DECISION: DOCS NOT RELEVANT---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-63)Output from node: 'gradeDocuments'
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-64){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-65) type: 'ai',
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-66) content: '',
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-67) tool_calls: [
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-68)  {
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-69)   name: 'give_relevance_score',
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-70)   args: { binaryScore: 'no' },
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-71)   type: 'tool_call',
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-72)   id: 'call_AGE7gORVFubExfJWcjb0C2nV'
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-73)  }
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-74) ]
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-75)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-76)---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-77)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-78)---TRANSFORM QUERY---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-79)Output from node: 'rewrite'
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-80){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-81) type: 'ai',
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-82) content: "What are the different types of agent memory described in Lilian Weng's blog post?",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-83) tool_calls: []
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-84)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-85)---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-86)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-87)---CALL AGENT---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-88)---DECIDE TO RETRIEVE---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-89)Output from node: 'agent'
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-90){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-91) type: 'ai',
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-92) content: "Lilian Weng's blog post describes the following types of agent memory:\n" +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-93)  '\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-94)  '1. **Memory Stream**:\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-95)  '  - This is a long-term memory module (external database) that records a comprehensive list of agents’ experiences in natural language.\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-96)  '  - Each element in the memory stream is an observation or an event directly provided by the agent.\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-97)  '  - Inter-agent communication can trigger new natural language statements to be added to the memory stream.\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-98)  '\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-99)  '2. **Retrieval Model**:\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-100)  '  - This model surfaces the context to inform the agent’s behavior based on relevance, recency, and importance.\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-101)  '\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-102)  'These memory types are part of a broader design that combines generative agents with memory, planning, and reflection mechanisms to enable agents to behave based on past experiences and interact with other agents.',
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-103) tool_calls: []
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-104)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-105)---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-106)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-107){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-108) "messages": [
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-109)  {
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-110)   "lc": 1,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-111)   "type": "constructor",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-112)   "id": [
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-113)    "langchain_core",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-114)    "messages",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-115)    "AIMessageChunk"
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-116)   ],
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-117)   "kwargs": {
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-118)    "content": "Lilian Weng's blog post describes the following types of agent memory:\n\n1. **Memory Stream**:\n  - This is a long-term memory module (external database) that records a comprehensive list of agents’ experiences in natural language.\n  - Each element in the memory stream is an observation or an event directly provided by the agent.\n  - Inter-agent communication can trigger new natural language statements to be added to the memory stream.\n\n2. **Retrieval Model**:\n  - This model surfaces the context to inform the agent’s behavior based on relevance, recency, and importance.\n\nThese memory types are part of a broader design that combines generative agents with memory, planning, and reflection mechanisms to enable agents to behave based on past experiences and interact with other agents.",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-119)    "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-120)    "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-121)     "estimatedTokenUsage": {
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-122)      "promptTokens": 280,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-123)      "completionTokens": 155,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-124)      "totalTokens": 435
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-125)     },
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-126)     "prompt": 0,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-127)     "completion": 0,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-128)     "finish_reason": "stop",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-129)     "system_fingerprint": "fp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3bfp_3cd8b62c3b"
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-130)    },
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-131)    "tool_call_chunks": [],
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-132)    "id": "chatcmpl-9zAaVQGmTLiCaFvtbxUK60qMFsSmU",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-133)    "usage_metadata": {
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-134)     "input_tokens": 363,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-135)     "output_tokens": 156,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-136)     "total_tokens": 519
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-137)    },
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-138)    "tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-139)    "invalid_tool_calls": []
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-140)   }
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-141)  }
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-142) ]
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-143)}

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  Chatbots  ](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/) [ Next  Corrective RAG (CRAG)  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
