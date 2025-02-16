---
url: https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#self-rag)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

Self-RAG 

[ ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/?q= "Share")

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
          * [ Corrective RAG (CRAG)  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/)
          * Self-RAG  [ Self-RAG  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/) Table of contents 
            * [ Dependencies  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#dependencies)
            * [ Self-RAG Detail  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#self-rag-detail)
            * [ - Token: ISREL  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#-token-isrel)
            * [ Setup  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#setup)
              * [ Load env vars  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#load-env-vars)
              * [ Install dependencies  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#install-dependencies)
            * [ State  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#state)
            * [ Nodes and Edges  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#nodes-and-edges)
            * [ Build Graph  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#build-graph)
            * [ Run the graph  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#run-the-graph)
              * [ See the LangSmith trace here.  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#see-the-langsmith-trace-here)
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

  * [ Dependencies  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#dependencies)
  * [ Self-RAG Detail  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#self-rag-detail)
  * [ - Token: ISREL  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#-token-isrel)
  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#setup)
    * [ Load env vars  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#load-env-vars)
    * [ Install dependencies  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#install-dependencies)
  * [ State  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#state)
  * [ Nodes and Edges  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#nodes-and-edges)
  * [ Build Graph  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#build-graph)
  * [ Run the graph  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#run-the-graph)
    * [ See the LangSmith trace here.  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#see-the-langsmith-trace-here)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ Tutorials  ](https://langchain-ai.github.io/langgraphjs/tutorials/)
  4. [ RAG  ](https://langchain-ai.github.io/langgraphjs/tutorials#rag)



# Self-RAG[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#self-rag "Permanent link")

Self-reflection can enhance RAG, enabling correction of poor quality retrieval or generations.

Several recent papers focus on this theme, but implementing the ideas can be tricky.

Here we show how to implement ideas from the `Self RAG` paper [here](https://arxiv.org/abs/2310.11511) using LangGraph.

## Dependencies[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#dependencies "Permanent link")

Set `OPENAI_API_KEY`

## Self-RAG Detail[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#self-rag-detail "Permanent link")

Self-RAG is a recent paper that introduces an interesting approach for self-reflective RAG.

The framework trains an LLM (e.g., LLaMA2-7b or 13b) to generate tokens that govern the RAG process in a few ways:

  1. Should I retrieve from retriever, `R` -

  2. Token: `Retrieve`

  3. Input: `x (question)` OR `x (question)`, `y (generation)`
  4. Decides when to retrieve `D` chunks with `R`
  5. Output: `yes, no, continue`

  6. Are the retrieved passages `D` relevant to the question `x` -




## - Token: `ISREL`[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#-token-isrel "Permanent link")

  * Input: (`x (question)`, `d (chunk)`) for `d` in `D`
  * `d` provides useful information to solve `x`
  * Output: `relevant, irrelevant`

  * Are the LLM generation from each chunk in `D` is relevant to the chunk (hallucinations, etc) -

  * Token: `ISSUP`

  * Input: `x (question)`, `d (chunk)`, `y (generation)` for `d` in `D`
  * All of the verification-worthy statements in `y (generation)` are supported by `d`
  * Output: `{fully supported, partially supported, no support`

  * The LLM generation from each chunk in `D` is a useful response to `x (question)` -

  * Token: `ISUSE`

  * Input: `x (question)`, `y (generation)` for `d` in `D`
  * `y (generation)` is a useful response to `x (question)`.
  * Output: `{5, 4, 3, 2, 1}`



We can represent this as a graph:

![image.png]()

Let's implement some of these ideas from scratch using [LangGraph](https://js.langchain.com/docs/langgraph).

## Setup[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#setup "Permanent link")

### Load env vars[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#load-env-vars "Permanent link")

Add a `.env` variable in the root of the repo folder with your variables.

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-0-1)import"dotenv/config";

```


### Install dependencies[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#install-dependencies "Permanent link")

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-1-1)npminstallcheeriozodlangchain@langchain/community@langchain/openai@langchain/core@langchain/textsplitters

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-2-1)import{CheerioWebBaseLoader}from"@langchain/community/document_loaders/web/cheerio";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-2-2)import{RecursiveCharacterTextSplitter}from"@langchain/textsplitters";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-2-3)import{MemoryVectorStore}from"langchain/vectorstores/memory";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-2-4)import{OpenAIEmbeddings}from"@langchain/openai";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-2-5)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-2-6)consturls=[
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-2-7)"https://lilianweng.github.io/posts/2023-06-23-agent/",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-2-8)"https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-2-9)"https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-2-10)];
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-2-11)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-2-12)constdocs=awaitPromise.all(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-2-13)urls.map((url)=>newCheerioWebBaseLoader(url).load()),
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-2-14));
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-2-15)constdocsList=docs.flat();
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-2-16)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-2-17)consttextSplitter=newRecursiveCharacterTextSplitter({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-2-18)chunkSize:500,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-2-19)chunkOverlap:250,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-2-20)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-2-21)constdocSplits=awaittextSplitter.splitDocuments(docsList);
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-2-22)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-2-23)// Add to vectorDB
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-2-24)constvectorStore=awaitMemoryVectorStore.fromDocuments(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-2-25)docSplits,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-2-26)newOpenAIEmbeddings({model:"text-embedding-3-large"}),
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-2-27));
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-2-28)constretriever=vectorStore.asRetriever();

```


## State[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#state "Permanent link")

We will define a graph.

Our state will be an `object`.

We can access this from any graph node as `state.key`.

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-3-1)import{Annotation}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-3-2)import{typeDocumentInterface}from"@langchain/core/documents";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-3-3)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-3-4)// Represents the state of our graph.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-3-5)constGraphState=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-3-6)documents:Annotation<DocumentInterface[]>({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-3-7)reducer:(x,y)=>y??x??[],
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-3-8)}),
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-3-9)question:Annotation<string>({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-3-10)reducer:(x,y)=>y??x??"",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-3-11)}),
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-3-12)generation:Annotation<string>({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-3-13)reducer:(x,y)=>y??x,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-3-14)default:()=>"",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-3-15)}),
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-3-16)generationVQuestionGrade:Annotation<string>({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-3-17)reducer:(x,y)=>y??x,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-3-18)}),
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-3-19)generationVDocumentsGrade:Annotation<string>({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-3-20)reducer:(x,y)=>y??x,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-3-21)}),
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-3-22)});

```


## Nodes and Edges[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#nodes-and-edges "Permanent link")

Each `node` will simply modify the `state`.

Each `edge` will choose which `node` to call next.

We can lay out `self-RAG` as a graph.

Here is our graph flow:

![image.png]()

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-1)import{z}from"zod";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-2)import{ChatPromptTemplate}from"@langchain/core/prompts";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-3)import{pull}from"langchain/hub";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-4)import{ChatOpenAI}from"@langchain/openai";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-5)import{StringOutputParser}from"@langchain/core/output_parsers";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-6)importtype{RunnableConfig}from"@langchain/core/runnables";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-7)import{formatDocumentsAsString}from"langchain/util/document";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-8)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-9)// Define the LLM once. We'll reuse it throughout the graph.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-10)constmodel=newChatOpenAI({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-11)model:"gpt-4o",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-12)temperature:0,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-13)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-14)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-15)/**
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-16) * Retrieve documents
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-17) *
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-18) * @param {typeof GraphState.State} state The current state of the graph.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-19) * @param {RunnableConfig | undefined} config The configuration object for tracing.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-20) * @returns {Promise<Partial<typeof GraphState.State>>} The new state object.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-21) */
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-22)asyncfunctionretrieve(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-23)state:typeofGraphState.State,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-24)config?:RunnableConfig
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-25)):Promise<Partial<typeofGraphState.State>>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-26)console.log("---RETRIEVE---");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-27)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-28)constdocuments=awaitretriever
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-29).withConfig({runName:"FetchRelevantDocuments"})
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-30).invoke(state.question,config);
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-31)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-32)return{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-33)documents,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-34)};
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-35)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-36)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-37)/**
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-38) * Generate answer
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-39) *
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-40) * @param {typeof GraphState.State} state The current state of the graph.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-41) * @param {RunnableConfig | undefined} config The configuration object for tracing.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-42) * @returns {Promise<Partial<typeof GraphState.State>>} The new state object.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-43) */
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-44)asyncfunctiongenerate(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-45)state:typeofGraphState.State
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-46)):Promise<Partial<typeofGraphState.State>>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-47)console.log("---GENERATE---");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-48)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-49)// Pull in the prompt
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-50)constprompt=awaitpull<ChatPromptTemplate>("rlm/rag-prompt");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-51)// Construct the RAG chain by piping the prompt, model, and output parser
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-52)constragChain=prompt.pipe(model).pipe(newStringOutputParser());
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-53)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-54)constgeneration=awaitragChain.invoke({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-55)context:formatDocumentsAsString(state.documents),
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-56)question:state.question,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-57)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-58)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-59)return{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-60)generation,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-61)};
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-62)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-63)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-64)/**
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-65) * Determines whether the retrieved documents are relevant to the question.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-66) *
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-67) * @param {typeof GraphState.State} state The current state of the graph.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-68) * @param {RunnableConfig | undefined} config The configuration object for tracing.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-69) * @returns {Promise<Partial<typeof GraphState.State>>} The new state object.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-70) */
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-71)asyncfunctiongradeDocuments(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-72)state:typeofGraphState.State
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-73)):Promise<Partial<typeofGraphState.State>>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-74)console.log("---CHECK RELEVANCE---");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-75)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-76)// pass the name & schema to `withStructuredOutput` which will force the model to call this tool.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-77)constllmWithTool=model.withStructuredOutput(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-78)z
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-79).object({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-80)binaryScore:z
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-81).enum(["yes","no"])
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-82).describe("Relevance score 'yes' or 'no'"),
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-83)})
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-84).describe(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-85)"Grade the relevance of the retrieved documents to the question. Either 'yes' or 'no'."
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-86)),
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-87){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-88)name:"grade",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-89)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-90));
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-91)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-92)constprompt=ChatPromptTemplate.fromTemplate(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-93)`You are a grader assessing relevance of a retrieved document to a user question.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-94) Here is the retrieved document:
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-95)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-96) {context}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-97)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-98) Here is the user question: {question}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-99)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-100) If the document contains keyword(s) or semantic meaning related to the user question, grade it as relevant.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-101) Give a binary score 'yes' or 'no' score to indicate whether the document is relevant to the question.`
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-102));
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-103)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-104)// Chain
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-105)constchain=prompt.pipe(llmWithTool);
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-106)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-107)constfilteredDocs:Array<DocumentInterface>=[];
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-108)forawait(constdocofstate.documents){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-109)constgrade=awaitchain.invoke({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-110)context:doc.pageContent,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-111)question:state.question,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-112)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-113)if(grade.binaryScore==="yes"){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-114)console.log("---GRADE: DOCUMENT RELEVANT---");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-115)filteredDocs.push(doc);
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-116)}else{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-117)console.log("---GRADE: DOCUMENT NOT RELEVANT---");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-118)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-119)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-120)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-121)return{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-122)documents:filteredDocs,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-123)};
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-124)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-125)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-126)/**
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-127) * Transform the query to produce a better question.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-128) *
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-129) * @param {typeof GraphState.State} state The current state of the graph.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-130) * @param {RunnableConfig | undefined} config The configuration object for tracing.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-131) * @returns {Promise<Partial<typeof GraphState.State>>} The new state object.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-132) */
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-133)asyncfunctiontransformQuery(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-134)state:typeofGraphState.State
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-135)):Promise<Partial<typeofGraphState.State>>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-136)console.log("---TRANSFORM QUERY---");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-137)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-138)// Pull in the prompt
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-139)constprompt=ChatPromptTemplate.fromTemplate(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-140)`You are generating a question that is well optimized for semantic search retrieval.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-141) Look at the input and try to reason about the underlying sematic intent / meaning.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-142) Here is the initial question:
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-143) \n ------- \n
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-144) {question} 
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-145) \n ------- \n
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-146) Formulate an improved question: `
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-147));
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-148)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-149)// Construct the chain
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-150)constchain=prompt.pipe(model).pipe(newStringOutputParser());
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-151)constbetterQuestion=awaitchain.invoke({question:state.question});
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-152)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-153)return{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-154)question:betterQuestion,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-155)};
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-156)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-157)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-158)/**
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-159) * Determines whether to generate an answer, or re-generate a question.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-160) *
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-161) * @param {typeof GraphState.State} state The current state of the graph.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-162) * @returns {"transformQuery" | "generate"} Next node to call
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-163) */
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-164)functiondecideToGenerate(state:typeofGraphState.State){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-165)console.log("---DECIDE TO GENERATE---");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-166)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-167)constfilteredDocs=state.documents;
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-168)if(filteredDocs.length===0){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-169)// All documents have been filtered checkRelevance
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-170)// We will re-generate a new query
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-171)console.log("---DECISION: TRANSFORM QUERY---");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-172)return"transformQuery";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-173)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-174)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-175)// We have relevant documents, so generate answer
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-176)console.log("---DECISION: GENERATE---");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-177)return"generate";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-178)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-179)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-180)/**
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-181) * Determines whether the generation is grounded in the document.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-182) *
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-183) * @param {typeof GraphState.State} state The current state of the graph.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-184) * @param {RunnableConfig | undefined} config The configuration object for tracing.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-185) * @returns {Promise<Partial<typeof GraphState.State>>} The new state object.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-186) */
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-187)asyncfunctiongenerateGenerationVDocumentsGrade(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-188)state:typeofGraphState.State
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-189)):Promise<Partial<typeofGraphState.State>>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-190)console.log("---GENERATE GENERATION vs DOCUMENTS GRADE---");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-191)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-192)constllmWithTool=model.withStructuredOutput(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-193)z
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-194).object({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-195)binaryScore:z
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-196).enum(["yes","no"])
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-197).describe("Relevance score 'yes' or 'no'"),
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-198)})
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-199).describe(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-200)"Grade the relevance of the retrieved documents to the question. Either 'yes' or 'no'."
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-201)),
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-202){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-203)name:"grade",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-204)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-205));
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-206)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-207)constprompt=ChatPromptTemplate.fromTemplate(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-208)`You are a grader assessing whether an answer is grounded in / supported by a set of facts.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-209) Here are the facts:
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-210) \n ------- \n
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-211) {documents} 
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-212) \n ------- \n
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-213) Here is the answer: {generation}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-214) Give a binary score 'yes' or 'no' to indicate whether the answer is grounded in / supported by a set of facts.`
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-215));
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-216)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-217)constchain=prompt.pipe(llmWithTool);
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-218)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-219)constscore=awaitchain.invoke({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-220)documents:formatDocumentsAsString(state.documents),
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-221)generation:state.generation,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-222)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-223)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-224)return{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-225)generationVDocumentsGrade:score.binaryScore,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-226)};
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-227)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-228)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-229)functiongradeGenerationVDocuments(state:typeofGraphState.State){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-230)console.log("---GRADE GENERATION vs DOCUMENTS---");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-231)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-232)constgrade=state.generationVDocumentsGrade;
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-233)if(grade==="yes"){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-234)console.log("---DECISION: SUPPORTED, MOVE TO FINAL GRADE---");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-235)return"supported";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-236)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-237)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-238)console.log("---DECISION: NOT SUPPORTED, GENERATE AGAIN---");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-239)return"not supported";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-240)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-241)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-242)/**
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-243) * Determines whether the generation addresses the question.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-244) *
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-245) * @param {typeof GraphState.State} state The current state of the graph.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-246) * @param {RunnableConfig | undefined} config The configuration object for tracing.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-247) * @returns {Promise<Partial<typeof GraphState.State>>} The new state object.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-248) */
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-249)asyncfunctiongenerateGenerationVQuestionGrade(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-250)state:typeofGraphState.State
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-251)):Promise<Partial<typeofGraphState.State>>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-252)console.log("---GENERATE GENERATION vs QUESTION GRADE---");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-253)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-254)constllmWithTool=model.withStructuredOutput(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-255)z
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-256).object({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-257)binaryScore:z
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-258).enum(["yes","no"])
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-259).describe("Relevance score 'yes' or 'no'"),
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-260)})
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-261).describe(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-262)"Grade the relevance of the retrieved documents to the question. Either 'yes' or 'no'."
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-263)),
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-264){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-265)name:"grade",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-266)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-267));
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-268)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-269)constprompt=ChatPromptTemplate.fromTemplate(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-270)`You are a grader assessing whether an answer is useful to resolve a question.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-271) Here is the answer:
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-272) \n ------- \n
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-273) {generation} 
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-274) \n ------- \n
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-275) Here is the question: {question}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-276) Give a binary score 'yes' or 'no' to indicate whether the answer is useful to resolve a question.`
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-277));
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-278)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-279)constchain=prompt.pipe(llmWithTool);
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-280)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-281)constscore=awaitchain.invoke({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-282)question:state.question,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-283)generation:state.generation,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-284)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-285)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-286)return{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-287)generationVQuestionGrade:score.binaryScore,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-288)};
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-289)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-290)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-291)functiongradeGenerationVQuestion(state:typeofGraphState.State){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-292)console.log("---GRADE GENERATION vs QUESTION---");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-293)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-294)constgrade=state.generationVQuestionGrade;
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-295)if(grade==="yes"){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-296)console.log("---DECISION: USEFUL---");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-297)return"useful";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-298)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-299)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-300)console.log("---DECISION: NOT USEFUL---");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-301)return"not useful";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-4-302)}

```


## Build Graph[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#build-graph "Permanent link")

The just follows the flow we outlined in the figure above.

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-5-1)import{END,START,StateGraph}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-5-2)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-5-3)constworkflow=newStateGraph(GraphState)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-5-4)// Define the nodes
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-5-5).addNode("retrieve",retrieve)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-5-6).addNode("gradeDocuments",gradeDocuments)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-5-7).addNode("generate",generate)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-5-8).addNode(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-5-9)"generateGenerationVDocumentsGrade",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-5-10)generateGenerationVDocumentsGrade
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-5-11))
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-5-12).addNode("transformQuery",transformQuery)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-5-13).addNode(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-5-14)"generateGenerationVQuestionGrade",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-5-15)generateGenerationVQuestionGrade
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-5-16));
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-5-17)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-5-18)// Build graph
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-5-19)workflow.addEdge(START,"retrieve");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-5-20)workflow.addEdge("retrieve","gradeDocuments");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-5-21)workflow.addConditionalEdges("gradeDocuments",decideToGenerate,{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-5-22)transformQuery:"transformQuery",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-5-23)generate:"generate",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-5-24)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-5-25)workflow.addEdge("transformQuery","retrieve");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-5-26)workflow.addEdge("generate","generateGenerationVDocumentsGrade");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-5-27)workflow.addConditionalEdges(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-5-28)"generateGenerationVDocumentsGrade",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-5-29)gradeGenerationVDocuments,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-5-30){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-5-31)supported:"generateGenerationVQuestionGrade",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-5-32)"not supported":"generate",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-5-33)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-5-34));
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-5-35)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-5-36)workflow.addConditionalEdges(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-5-37)"generateGenerationVQuestionGrade",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-5-38)gradeGenerationVQuestion,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-5-39){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-5-40)useful:END,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-5-41)"not useful":"transformQuery",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-5-42)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-5-43));
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-5-44)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-5-45)// Compile
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-5-46)constapp=workflow.compile();

```


## Run the graph[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#run-the-graph "Permanent link")

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-6-1)constinputs={
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-6-2)question:"Explain how the different types of agent memory work.",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-6-3)};
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-6-4)constconfig={recursionLimit:50};
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-6-5)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-6-6)constprettifyOutput=(output:Record<string,any>)=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-6-7)constkey=Object.keys(output)[0];
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-6-8)constvalue=output[key];
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-6-9)console.log(`Node: '${key}'`);
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-6-10)if(key==="retrieve"&&"documents"invalue){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-6-11)console.log(`Retrieved ${value.documents.length} documents.`);
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-6-12)}elseif(key==="gradeDocuments"&&"documents"invalue){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-6-13)console.log(`Graded documents. Found ${value.documents.length} relevant document(s).`);
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-6-14)}else{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-6-15)console.dir(value,{depth:null});
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-6-16)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-6-17)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-6-18)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-6-19)forawait(constoutputofawaitapp.stream(inputs,config)){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-6-20)prettifyOutput(output);
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-6-21)console.log("\n---ITERATION END---\n");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-6-22)}

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-7-1)---RETRIEVE---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-7-2)Node: 'retrieve'
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-7-3)Retrieved 4 documents.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-7-4)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-7-5)---ITERATION END---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-7-6)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-7-7)---CHECK RELEVANCE---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-7-8)---GRADE: DOCUMENT RELEVANT---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-7-9)---GRADE: DOCUMENT NOT RELEVANT---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-7-10)---GRADE: DOCUMENT RELEVANT---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-7-11)---GRADE: DOCUMENT RELEVANT---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-7-12)---DECIDE TO GENERATE---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-7-13)---DECISION: GENERATE---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-7-14)Node: 'gradeDocuments'
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-7-15)Graded documents. Found 3 relevant document(s).
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-7-16)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-7-17)---ITERATION END---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-7-18)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-7-19)---GENERATE---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-7-20)Node: 'generate'
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-7-21){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-7-22) generation: 'Short-term memory in agents involves in-context learning, which is limited by the finite context window length of the model. Long-term memory allows the agent to retain and recall extensive information over extended periods by using an external vector store and fast retrieval mechanisms. Sensory memory involves learning embedding representations for raw inputs like text and images.'
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-7-23)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-7-24)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-7-25)---ITERATION END---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-7-26)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-7-27)---GENERATE GENERATION vs DOCUMENTS GRADE---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-7-28)---GRADE GENERATION vs DOCUMENTS---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-7-29)---DECISION: SUPPORTED, MOVE TO FINAL GRADE---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-7-30)Node: 'generateGenerationVDocumentsGrade'
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-7-31){ generationVDocumentsGrade: 'yes' }
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-7-32)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-7-33)---ITERATION END---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-7-34)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-7-35)---GENERATE GENERATION vs QUESTION GRADE---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-7-36)---GRADE GENERATION vs QUESTION---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-7-37)---DECISION: USEFUL---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-7-38)Node: 'generateGenerationVQuestionGrade'
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-7-39){ generationVQuestionGrade: 'yes' }
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-7-40)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__codelineno-7-41)---ITERATION END---

```


> #### See the LangSmith trace [here](https://smith.langchain.com/public/cbf3c09a-5104-45f4-bd32-6e992e67f67a/r).[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#see-the-langsmith-trace-here "Permanent link")

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  Corrective RAG (CRAG)  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_crag/) [ Next  Basic Multi-agent Collaboration  ](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
