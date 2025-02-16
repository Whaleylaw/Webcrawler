---
url: https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#corrective-rag-crag)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

Corrective RAG (CRAG) 

[ ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/?q= "Share")

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
          * [ LangGraph Retrieval Agent  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/)
          * Corrective RAG (CRAG)  [ Corrective RAG (CRAG)  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/) Table of contents 
            * [ Dependencies  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#dependencies)
            * [ Setup  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#setup)
              * [ Load env vars  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#load-env-vars)
              * [ Install dependencies  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#install-dependencies)
            * [ CRAG Detail  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#crag-detail)
            * [ Retriever  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#retriever)
            * [ State  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#state)
            * [ Nodes and Edges  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#nodes-and-edges)
            * [ Build Graph  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#build-graph)
              * [ See the LangSmith trace here.  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#see-the-langsmith-trace-here)
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

  * [ Dependencies  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#dependencies)
  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#setup)
    * [ Load env vars  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#load-env-vars)
    * [ Install dependencies  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#install-dependencies)
  * [ CRAG Detail  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#crag-detail)
  * [ Retriever  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#retriever)
  * [ State  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#state)
  * [ Nodes and Edges  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#nodes-and-edges)
  * [ Build Graph  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#build-graph)
    * [ See the LangSmith trace here.  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#see-the-langsmith-trace-here)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ Tutorials  ](https://langchain-ai.github.io/langgraphjs/tutorials/)
  4. [ RAG  ](https://langchain-ai.github.io/langgraphjs/tutorials#rag)



# Corrective RAG (CRAG)[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#corrective-rag-crag "Permanent link")

Self-reflection can enhance RAG, enabling correction of poor quality retrieval or generations.

Several recent papers focus on this theme, but implementing the ideas can be tricky.

Here we show how to implement ideas from the `Corrective RAG (CRAG)` paper [here](https://arxiv.org/pdf/2401.15884.pdf) using LangGraph.

## Dependencies[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#dependencies "Permanent link")

Set `OPENAI_API_KEY`

Set `TAVILY_API_KEY` to enable web search [here](https://app.tavily.com/sign-in)

## Setup[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#setup "Permanent link")

### Load env vars[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#load-env-vars "Permanent link")

Add a `.env` variable in the root of the repo with your variables.

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-0-1)import"dotenv/config";

```


### Install dependencies[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#install-dependencies "Permanent link")

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-1-1)npminstallcheeriozodlangchain@langchain/community@langchain/openai@langchain/core@langchain/textsplitters@langchain/langgraph

```


## CRAG Detail[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#crag-detail "Permanent link")

Corrective-RAG (CRAG) is a recent paper that introduces an interesting approach for self-reflective RAG.

The framework grades retrieved documents relative to the question:

  1. Correct documents -

  2. If at least one document exceeds the threshold for relevance, then it proceeds to generation

  3. Before generation, it performns knowledge refinement
  4. This paritions the document into "knowledge strips"
  5. It grades each strip, and filters our irrelevant ones

  6. Ambiguous or incorrect documents -

  7. If all documents fall below the relevance threshold or if the grader is unsure, then the framework seeks an additional datasource

  8. It will use web search to supplement retrieval
  9. The diagrams in the paper also suggest that query re-writing is used here



![image.png]()

Let's implement some of these ideas from scratch using [LangGraph](https://js.langchain.com/docs/langgraph).

## Retriever[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#retriever "Permanent link")

Let's index 3 blog posts.

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-2-1)import{CheerioWebBaseLoader}from"@langchain/community/document_loaders/web/cheerio";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-2-2)import{RecursiveCharacterTextSplitter}from"@langchain/textsplitters";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-2-3)import{MemoryVectorStore}from"langchain/vectorstores/memory";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-2-4)import{OpenAIEmbeddings}from"@langchain/openai";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-2-5)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-2-6)consturls=[
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-2-7)"https://lilianweng.github.io/posts/2023-06-23-agent/",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-2-8)"https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-2-9)"https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-2-10)];
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-2-11)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-2-12)constdocs=awaitPromise.all(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-2-13)urls.map((url)=>newCheerioWebBaseLoader(url).load()),
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-2-14));
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-2-15)constdocsList=docs.flat();
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-2-16)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-2-17)consttextSplitter=newRecursiveCharacterTextSplitter({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-2-18)chunkSize:250,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-2-19)chunkOverlap:0,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-2-20)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-2-21)constdocSplits=awaittextSplitter.splitDocuments(docsList);
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-2-22)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-2-23)// Add to vectorDB
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-2-24)constvectorStore=awaitMemoryVectorStore.fromDocuments(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-2-25)docSplits,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-2-26)newOpenAIEmbeddings(),
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-2-27));
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-2-28)constretriever=vectorStore.asRetriever();

```


## State[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#state "Permanent link")

We will define a graph.

Our state will be an `object`.

We can access this from any graph node as `state.key`.

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-3-1)import{Annotation}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-3-2)import{DocumentInterface}from"@langchain/core/documents";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-3-3)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-3-4)// Represents the state of our graph.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-3-5)constGraphState=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-3-6)documents:Annotation<DocumentInterface[]>({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-3-7)reducer:(x,y)=>y??x??[],
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-3-8)}),
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-3-9)question:Annotation<string>({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-3-10)reducer:(x,y)=>y??x??"",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-3-11)}),
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-3-12)generation:Annotation<string>({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-3-13)reducer:(x,y)=>y??x,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-3-14)}),
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-3-15)});

```


## Nodes and Edges[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#nodes-and-edges "Permanent link")

Each `node` will simply modify the `state`.

Each `edge` will choose which `node` to call next.

We can make some simplifications from the paper:

  * Let's skip the knowledge refinement phase as a first pass. This can be added back as a node, if desired.
  * If _any_ document is irrelevant, let's opt to supplement retrieval with web search.
  * We'll use [Tavily Search](https://js.langchain.com/docs/integrations/tools/tavily_search) for web search.
  * Let's use query re-writing to optimize the query for web search.



Here is our graph flow:

![image.png]()

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-1)import{TavilySearchResults}from"@langchain/community/tools/tavily_search";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-2)import{Document}from"@langchain/core/documents";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-3)import{z}from"zod";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-4)import{ChatPromptTemplate}from"@langchain/core/prompts";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-5)import{pull}from"langchain/hub";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-6)import{ChatOpenAI}from"@langchain/openai";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-7)import{StringOutputParser}from"@langchain/core/output_parsers";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-8)import{formatDocumentsAsString}from"langchain/util/document";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-9)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-10)// Define the LLM once. We'll reuse it throughout the graph.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-11)constmodel=newChatOpenAI({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-12)model:"gpt-4o",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-13)temperature:0,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-14)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-15)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-16)/**
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-17) * Retrieve documents
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-18) *
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-19) * @param {typeof GraphState.State} state The current state of the graph.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-20) * @param {RunnableConfig | undefined} config The configuration object for tracing.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-21) * @returns {Promise<Partial<typeof GraphState.State>>} The new state object.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-22) */
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-23)asyncfunctionretrieve(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-24)state:typeofGraphState.State
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-25)):Promise<Partial<typeofGraphState.State>>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-26)console.log("---RETRIEVE---");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-27)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-28)constdocuments=awaitretriever
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-29).withConfig({runName:"FetchRelevantDocuments"})
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-30).invoke(state.question);
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-31)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-32)return{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-33)documents,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-34)};
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-35)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-36)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-37)/**
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-38) * Generate answer
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-39) *
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-40) * @param {typeof GraphState.State} state The current state of the graph.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-41) * @param {RunnableConfig | undefined} config The configuration object for tracing.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-42) * @returns {Promise<Partial<typeof GraphState.State>>} The new state object.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-43) */
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-44)asyncfunctiongenerate(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-45)state:typeofGraphState.State
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-46)):Promise<Partial<typeofGraphState.State>>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-47)console.log("---GENERATE---");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-48)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-49)constprompt=awaitpull<ChatPromptTemplate>("rlm/rag-prompt");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-50)// Construct the RAG chain by piping the prompt, model, and output parser
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-51)constragChain=prompt.pipe(model).pipe(newStringOutputParser());
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-52)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-53)constgeneration=awaitragChain.invoke({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-54)context:formatDocumentsAsString(state.documents),
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-55)question:state.question,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-56)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-57)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-58)return{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-59)generation,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-60)};
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-61)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-62)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-63)/**
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-64) * Determines whether the retrieved documents are relevant to the question.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-65) *
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-66) * @param {typeof GraphState.State} state The current state of the graph.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-67) * @param {RunnableConfig | undefined} config The configuration object for tracing.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-68) * @returns {Promise<Partial<typeof GraphState.State>>} The new state object.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-69) */
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-70)asyncfunctiongradeDocuments(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-71)state:typeofGraphState.State
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-72)):Promise<Partial<typeofGraphState.State>>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-73)console.log("---CHECK RELEVANCE---");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-74)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-75)// pass the name & schema to `withStructuredOutput` which will force the model to call this tool.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-76)constllmWithTool=model.withStructuredOutput(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-77)z
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-78).object({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-79)binaryScore:z
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-80).enum(["yes","no"])
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-81).describe("Relevance score 'yes' or 'no'"),
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-82)})
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-83).describe(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-84)"Grade the relevance of the retrieved documents to the question. Either 'yes' or 'no'."
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-85)),
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-86){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-87)name:"grade",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-88)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-89));
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-90)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-91)constprompt=ChatPromptTemplate.fromTemplate(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-92)`You are a grader assessing relevance of a retrieved document to a user question.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-93) Here is the retrieved document:
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-94)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-95) {context}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-96)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-97) Here is the user question: {question}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-98)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-99) If the document contains keyword(s) or semantic meaning related to the user question, grade it as relevant.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-100) Give a binary score 'yes' or 'no' score to indicate whether the document is relevant to the question.`
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-101));
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-102)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-103)// Chain
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-104)constchain=prompt.pipe(llmWithTool);
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-105)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-106)constfilteredDocs:Array<DocumentInterface>=[];
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-107)forawait(constdocofstate.documents){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-108)constgrade=awaitchain.invoke({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-109)context:doc.pageContent,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-110)question:state.question,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-111)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-112)if(grade.binaryScore==="yes"){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-113)console.log("---GRADE: DOCUMENT RELEVANT---");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-114)filteredDocs.push(doc);
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-115)}else{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-116)console.log("---GRADE: DOCUMENT NOT RELEVANT---");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-117)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-118)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-119)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-120)return{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-121)documents:filteredDocs,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-122)};
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-123)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-124)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-125)/**
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-126) * Transform the query to produce a better question.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-127) *
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-128) * @param {typeof GraphState.State} state The current state of the graph.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-129) * @param {RunnableConfig | undefined} config The configuration object for tracing.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-130) * @returns {Promise<Partial<typeof GraphState.State>>} The new state object.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-131) */
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-132)asyncfunctiontransformQuery(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-133)state:typeofGraphState.State
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-134)):Promise<Partial<typeofGraphState.State>>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-135)console.log("---TRANSFORM QUERY---");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-136)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-137)// Pull in the prompt
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-138)constprompt=ChatPromptTemplate.fromTemplate(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-139)`You are generating a question that is well optimized for semantic search retrieval.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-140) Look at the input and try to reason about the underlying sematic intent / meaning.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-141) Here is the initial question:
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-142) \n ------- \n
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-143) {question} 
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-144) \n ------- \n
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-145) Formulate an improved question: `
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-146));
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-147)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-148)// Prompt
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-149)constchain=prompt.pipe(model).pipe(newStringOutputParser());
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-150)constbetterQuestion=awaitchain.invoke({question:state.question});
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-151)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-152)return{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-153)question:betterQuestion,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-154)};
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-155)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-156)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-157)/**
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-158) * Web search based on the re-phrased question using Tavily API.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-159) *
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-160) * @param {typeof GraphState.State} state The current state of the graph.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-161) * @param {RunnableConfig | undefined} config The configuration object for tracing.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-162) * @returns {Promise<Partial<typeof GraphState.State>>} The new state object.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-163) */
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-164)asyncfunctionwebSearch(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-165)state:typeofGraphState.State
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-166)):Promise<Partial<typeofGraphState.State>>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-167)console.log("---WEB SEARCH---");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-168)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-169)consttool=newTavilySearchResults();
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-170)constdocs=awaittool.invoke({input:state.question});
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-171)constwebResults=newDocument({pageContent:docs});
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-172)constnewDocuments=state.documents.concat(webResults);
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-173)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-174)return{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-175)documents:newDocuments,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-176)};
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-177)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-178)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-179)/**
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-180) * Determines whether to generate an answer, or re-generate a question.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-181) *
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-182) * @param {typeof GraphState.State} state The current state of the graph.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-183) * @returns {"transformQuery" | "generate"} Next node to call
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-184) */
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-185)functiondecideToGenerate(state:typeofGraphState.State){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-186)console.log("---DECIDE TO GENERATE---");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-187)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-188)constfilteredDocs=state.documents;
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-189)if(filteredDocs.length===0){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-190)// All documents have been filtered checkRelevance
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-191)// We will re-generate a new query
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-192)console.log("---DECISION: TRANSFORM QUERY---");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-193)return"transformQuery";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-194)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-195)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-196)// We have relevant documents, so generate answer
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-197)console.log("---DECISION: GENERATE---");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-198)return"generate";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-4-199)}

```


## Build Graph[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#build-graph "Permanent link")

The just follows the flow we outlined in the figure above.

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-5-1)import{END,START,StateGraph}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-5-2)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-5-3)constworkflow=newStateGraph(GraphState)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-5-4)// Define the nodes
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-5-5).addNode("retrieve",retrieve)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-5-6).addNode("gradeDocuments",gradeDocuments)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-5-7).addNode("generate",generate)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-5-8).addNode("transformQuery",transformQuery)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-5-9).addNode("webSearch",webSearch);
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-5-10)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-5-11)// Build graph
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-5-12)workflow.addEdge(START,"retrieve");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-5-13)workflow.addEdge("retrieve","gradeDocuments");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-5-14)workflow.addConditionalEdges(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-5-15)"gradeDocuments",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-5-16)decideToGenerate,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-5-17));
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-5-18)workflow.addEdge("transformQuery","webSearch");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-5-19)workflow.addEdge("webSearch","generate");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-5-20)workflow.addEdge("generate",END);
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-5-21)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-5-22)// Compile
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-5-23)constapp=workflow.compile();

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-6-1)constinputs={
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-6-2)question:"Explain how the different types of agent memory work.",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-6-3)};
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-6-4)constconfig={recursionLimit:50};
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-6-5)letfinalGeneration;
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-6-6)forawait(constoutputofawaitapp.stream(inputs,config)){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-6-7)for(const[key,value]ofObject.entries(output)){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-6-8)console.log(`Node: '${key}'`);
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-6-9)// Optional: log full state at each node
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-6-10)// console.log(JSON.stringify(value, null, 2));
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-6-11)finalGeneration=value;
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-6-12)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-6-13)console.log("\n---\n");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-6-14)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-6-15)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-6-16)// Log the final generation.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-6-17)console.log(JSON.stringify(finalGeneration,null,2));

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-7-1)---RETRIEVE---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-7-2)Node: 'retrieve'
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-7-3)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-7-4)---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-7-5)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-7-6)---CHECK RELEVANCE---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-7-7)---GRADE: DOCUMENT RELEVANT---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-7-8)---GRADE: DOCUMENT NOT RELEVANT---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-7-9)---GRADE: DOCUMENT NOT RELEVANT---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-7-10)---GRADE: DOCUMENT RELEVANT---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-7-11)---DECIDE TO GENERATE---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-7-12)---DECISION: GENERATE---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-7-13)Node: 'gradeDocuments'
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-7-14)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-7-15)---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-7-16)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-7-17)---GENERATE---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-7-18)Node: 'generate'
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-7-19)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-7-20)---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-7-21)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-7-22){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-7-23) "generation": "Different types of agent memory include long-term memory, which allows the agent to retain and recall information over extended periods, often using an external vector store for fast retrieval. This enables the agent to remember and utilize vast amounts of information efficiently."
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__codelineno-7-24)}

```


> #### See the LangSmith trace [here](https://smith.langchain.com/public/d2160835-8610-467f-a91a-ff19a34d1f5b/r).[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#see-the-langsmith-trace-here "Permanent link")

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  LangGraph Retrieval Agent  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/) [ Next  Self-RAG  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
