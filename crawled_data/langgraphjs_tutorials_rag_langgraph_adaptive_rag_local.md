---
url: https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#adaptive-rag-with-local-llms)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

Adaptive RAG with local LLMs 

[ ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/?q= "Share")

Type to start searching

[ GitHub  ](https://github.com/langchain-ai/langgraphjs "Go to repository")

  * [ Home ](https://langchain-ai.github.io/langgraphjs/)
  * [ API reference ](https://langchain-ai.github.io/langgraphjs/reference/)
  * [ Versions ](https://langchain-ai.github.io/langgraphjs/versions/)



[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

[ GitHub  ](https://github.com/langchain-ai/langgraphjs "Go to repository")

  * [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  * [ API reference  ](https://langchain-ai.github.io/langgraphjs/reference/)
  * [ Versions  ](https://langchain-ai.github.io/langgraphjs/versions/)



Table of contents 

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#setup)
    * [ Models  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#models)
      * [ Local Embeddings  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#local-embeddings)
      * [ Local LLM  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#local-llm)
    * [ Tracing  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#tracing)
  * [ Index  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#index)
  * [ Creating components  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#creating-components)
    * [ Question router  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#question-router)
    * [ Retrieval grader  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#retrieval-grader)
    * [ Generation  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#generation)
    * [ Hallucination grader  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#hallucination-grader)
    * [ Answer Grader  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#answer-grader)
    * [ Question rewriter  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#question-rewriter)
    * [ Web Search Tool  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#web-search-tool)
  * [ Graph  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#graph)
    * [ Graph state  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#graph-state)
    * [ Preparing nodes and edges  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#preparing-nodes-and-edges)
  * [ Build the graph  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#build-the-graph)
  * [ Running the graph  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#running-the-graph)



# Adaptive RAG with local LLMs[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#adaptive-rag-with-local-llms "Permanent link")

Adaptive RAG is a strategy for RAG that unites (1) [query analysis](https://blog.langchain.dev/query-construction/) with (2) [active / self-corrective RAG](https://blog.langchain.dev/agentic-rag-with-langgraph/).

In the [paper](https://arxiv.org/abs/2403.14403), they report query analysis to route across:

  * No Retrieval
  * Single-shot RAG
  * Iterative RAG



Let's build on this using LangGraph.

In our implementation, we will route between:

  * Web search: for questions related to recent events
  * Self-corrective RAG: for questions related to our index



![Adaptive RAG graph]()

## Setup[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#setup "Permanent link")

First, you'll need to install some required dependencies:

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-0-1)npminstallcheeriolangchain@langchain/community@langchain/ollama@langchain/core

```


For the fallback web search, you'll also need to obtain a [Tavily API key](https://tavily.com) and set it as an environment variable named `TAVILY_API_KEY`.

### Models[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#models "Permanent link")

Next, choose which local models you'll use.

#### Local Embeddings[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#local-embeddings "Permanent link")

We'll be using the `mxbai-embed-large`[](https://ollama.com/library/mxbai-embed-large) embeddings model from Ollama.

#### Local LLM[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#local-llm "Permanent link")

(1) Download [Ollama app](https://ollama.ai/).

(2) Pull a `Llama 3` model [here](https://ollama.com/library/llama3). You can also try `Mistral` models [here](https://ollama.ai/library/mixtral), one of the [quantized Cohere Command-R models](https://ollama.com/library/command-r), or any other model you'd like to try from the [Ollama library](https://ollama.com/library) - just be sure that your computer has sufficient RAM.

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-1-1)ollamapullllama3mxbai-embed-large

```


### Tracing[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#tracing "Permanent link")

Optionally, use [LangSmith](https://docs.smith.langchain.com/) for tracing (shown at bottom)

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-2-1)// process.env.LANGCHAIN_TRACING_V2 = "true";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-2-2)// process.env.LANGCHAIN_ENDPOINT = "https://api.smith.langchain.com";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-2-3)// process.env.LANGCHAIN_API_KEY = "<your-api-key>"

```


## Index[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#index "Permanent link")

Now that you've chosen and set up your local models, load and index some source documents. The code below uses some of [Lilian Weng's blog posts](https://lilianweng.github.io/) on LLMs and agents as a data source, then loads them into a demo `MemoryVectorStore`[](https://js.langchain.com/docs/integrations/vectorstores/memory) instance. It then creates a [retriever](https://js.langchain.com/docs/concepts#retrievers) from that vector store for later use.

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-3-1)import{RecursiveCharacterTextSplitter}from"langchain/text_splitter";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-3-2)import{CheerioWebBaseLoader}from"@langchain/community/document_loaders/web/cheerio";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-3-3)import{MemoryVectorStore}from"langchain/vectorstores/memory";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-3-4)import{OllamaEmbeddings}from"@langchain/ollama";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-3-5)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-3-6)consturls=[
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-3-7)"https://lilianweng.github.io/posts/2023-06-23-agent/",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-3-8)"https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-3-9)"https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-3-10)];
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-3-11)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-3-12)constdocs=awaitPromise.all(urls.map((url)=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-3-13)constloader=newCheerioWebBaseLoader(url);
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-3-14)returnloader.load();
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-3-15)}));
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-3-16)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-3-17)constdocsList=docs.flat();
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-3-18)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-3-19)consttextSplitter=newRecursiveCharacterTextSplitter({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-3-20)chunkSize:250,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-3-21)chunkOverlap:0,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-3-22)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-3-23)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-3-24)constsplitDocs=awaittextSplitter.splitDocuments(docsList);
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-3-25)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-3-26)constembeddings=newOllamaEmbeddings({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-3-27)model:"mxbai-embed-large",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-3-28)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-3-29)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-3-30)// Add to vector store
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-3-31)constvectorStore=awaitMemoryVectorStore.fromDocuments(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-3-32)splitDocs,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-3-33)embeddings,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-3-34));
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-3-35)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-3-36)constretriever=vectorStore.asRetriever();

```


## Creating components[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#creating-components "Permanent link")

Here, you'll create the components of the graph.

### Question router[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#question-router "Permanent link")

First, create a chain that will route incoming questions towards either your vector store if they are related to LLMs or agents, or to a general web search if they are not.

You'll use Ollama's [JSON mode](https://js.langchain.com/docs/integrations/chat/ollama/#json-mode) to help keep the output format consistent.

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-4-1)import{ChatPromptTemplate}from"@langchain/core/prompts";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-4-2)import{JsonOutputParser}from"@langchain/core/output_parsers";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-4-3)import{ChatOllama}from"@langchain/ollama";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-4-4)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-4-5)constjsonModeLlm=newChatOllama({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-4-6)model:"llama3",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-4-7)format:"json",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-4-8)temperature:0,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-4-9)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-4-10)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-4-11)constQUESTION_ROUTER_SYSTEM_TEMPLATE=
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-4-12)`You are an expert at routing a user question to a vectorstore or web search.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-4-13)Use the vectorstore for questions on LLM agents, prompt engineering, and adversarial attacks.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-4-14)You do not need to be stringent with the keywords in the question related to these topics.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-4-15)Otherwise, use web-search. Give a binary choice 'web_search' or 'vectorstore' based on the question.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-4-16)Return the a JSON with a single key 'datasource' and no preamble or explanation.`;
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-4-17)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-4-18)constquestionRouterPrompt=ChatPromptTemplate.fromMessages([
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-4-19)["system",QUESTION_ROUTER_SYSTEM_TEMPLATE],
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-4-20)["human","{question}"],
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-4-21)]);
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-4-22)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-4-23)constquestionRouter=questionRouterPrompt.pipe(jsonModeLlm).pipe(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-4-24)newJsonOutputParser(),
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-4-25));
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-4-26)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-4-27)awaitquestionRouter.invoke({question:"llm agent memory"});

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-5-1){ datasource: 'vectorstore' }

```


Above, notice that you invoked the router with a query related to the knowledge our vector store contains, so it responds accordingly. Here's what happens if you ask something irrelevant: 

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-6-1)awaitquestionRouter.invoke({question:"red robin"});

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-7-1){ datasource: 'web_search' }

```


In this case, you can see that execution would be routed to our web search. 

### Retrieval grader[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#retrieval-grader "Permanent link")

Create a grader that will check retrieved documents from our vector store for relevancy:

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-1)constGRADER_TEMPLATE=
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-2)`You are a grader assessing relevance of a retrieved document to a user question.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-3)Here is the retrieved document:
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-4)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-5)<document>
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-6){content}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-7)</document>
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-8)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-9)Here is the user question:
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-10)<question>
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-11){question}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-12)</question>
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-13)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-14)If the document contains keywords related to the user question, grade it as relevant.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-15)It does not need to be a stringent test. The goal is to filter out erroneous retrievals.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-16)Give a binary score 'yes' or 'no' score to indicate whether the document is relevant to the question.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-17)Provide the binary score as a JSON with a single key 'score' and no preamble or explanation.`;
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-18)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-19)constgraderPrompt=ChatPromptTemplate.fromTemplate(GRADER_TEMPLATE);
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-20)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-21)constretrievalGrader=graderPrompt.pipe(jsonModeLlm).pipe(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-22)newJsonOutputParser(),
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-23));
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-24)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-25)// Test run
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-26)consttestQuestion="agent memory";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-27)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-28)constdocs2=awaitretriever.invoke(testQuestion);
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-29)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-30)awaitretrievalGrader.invoke({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-31)question:testQuestion,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-32)content:docs2[0].pageContent,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-33)});

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-9-1){ score: 'yes' }

```


And you can see that it marks the first retrieved document as related to `"agent memory"`. 

### Generation[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#generation "Permanent link")

Next, create a chain that generates an answer based on retrieved documents.

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-10-1)import*ashubfrom"langchain/hub";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-10-2)import{StringOutputParser}from"@langchain/core/output_parsers";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-10-3)importtype{Document}from"@langchain/core/documents";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-10-4)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-10-5)// https://smith.langchain.com/hub/rlm/rag-prompt
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-10-6)constragPrompt=awaithub.pull("rlm/rag-prompt");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-10-7)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-10-8)// Post-processing
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-10-9)constformatDocs=(docs:Document[])=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-10-10)returndocs.map((doc)=>doc.pageContent).join("\n\n");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-10-11)};
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-10-12)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-10-13)// Initialize a new model without JSON mode active
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-10-14)constllm=newChatOllama({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-10-15)model:"llama3",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-10-16)temperature:0,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-10-17)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-10-18)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-10-19)// Chain
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-10-20)constragChain=ragPrompt.pipe(llm).pipe(newStringOutputParser());
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-10-21)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-10-22)// Test run
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-10-23)consttestQuestion2="agent memory";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-10-24)constdocs3=awaitretriever.invoke(testQuestion2);
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-10-25)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-10-26)awaitragChain.invoke({context:formatDocs(docs3),question:testQuestion2});

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-11-1)Based on the provided context, it appears that an agent's memory refers to its ability to record and reflect on past experiences, using both long-term and short-term memory modules. The long-term memory module, or "memory stream," stores a comprehensive list of agents' experiences in natural language, while the reflection mechanism synthesizes these memories into higher-level inferences over time to guide future behavior.

```


### Hallucination grader[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#hallucination-grader "Permanent link")

Create a chain that reviews a generated answer and checks for hallucinations. We'll return to using JSON mode for this one:

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-1)constHALLUCINATION_GRADER_TEMPLATE=
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-2)`You are a grader assessing whether an answer is grounded in / supported by a set of facts.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-3)Here are the facts used as context to generate the answer:
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-4)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-5)<context>
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-6){context} 
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-7)</context>
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-8)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-9)Here is the answer:
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-10)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-11)<answer>
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-12){generation}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-13)</answer>
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-14)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-15)Give a binary score 'yes' or 'no' score to indicate whether the answer is grounded in / supported by a set of facts.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-16)Provide the binary score as a JSON with a single key 'score' and no preamble or explanation.`;
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-17)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-18)consthallucinationGraderPrompt=ChatPromptTemplate.fromTemplate(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-19)HALLUCINATION_GRADER_TEMPLATE,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-20));
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-21)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-22)consthallucinationGrader=hallucinationGraderPrompt.pipe(llm).pipe(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-23)newJsonOutputParser(),
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-24));
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-25)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-26)// Test run
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-27)constgeneration2=awaitragChain.invoke({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-28)context:formatDocs(docs3),
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-29)question:testQuestion2,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-30)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-31)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-32)awaithallucinationGrader.invoke({context:formatDocs(docs3),generation:generation2});

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-13-1){ score: 'yes' }

```


### Answer Grader[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#answer-grader "Permanent link")

Create a chain for checking the relevancy of the final answer:

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-1)constANSWER_GRADER_PROMPT_TEMPLATE=
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-2)`You are a grader assessing whether an answer is useful to resolve a question.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-3)Here is the answer:
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-4)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-5)<answer>
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-6){generation} 
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-7)</answer>
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-8)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-9)Here is the question:
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-10)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-11)<question>
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-12){question}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-13)</question>
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-14)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-15)Give a binary score 'yes' or 'no' to indicate whether the answer is useful to resolve a question.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-16)Provide the binary score as a JSON with a single key 'score' and no preamble or explanation.`;
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-17)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-18)constanswerGraderPrompt=ChatPromptTemplate.fromTemplate(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-19)ANSWER_GRADER_PROMPT_TEMPLATE,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-20));
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-21)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-22)constanswerGrader=answerGraderPrompt.pipe(jsonModeLlm).pipe(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-23)newJsonOutputParser(),
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-24));
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-25)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-26)// Test run
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-27)constgeneration3=awaitragChain.invoke({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-28)context:formatDocs(docs3),
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-29)question:testQuestion2,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-30)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-31)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-32)awaitanswerGrader.invoke({question:testQuestion2,generation:generation3});

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-15-1){ score: 'yes' }

```


### Question rewriter[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#question-rewriter "Permanent link")

Create a question rewriter. This chain performs [query analysis](https://js.langchain.com/docs/tutorials/query_analysis/) on the user questions and optimizes them for RAG to help handle difficult queries.

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-1)constREWRITER_PROMPT_TEMPLATE=
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-2)`You a question re-writer that converts an input question to a better version that is optimized
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-3)for vectorstore retrieval. Look at the initial and formulate an improved question.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-4)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-5)Here is the initial question:
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-6)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-7)<question>
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-8){question}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-9)</question>
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-10)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-11)Respond only with an improved question. Do not include any preamble or explanation.`;
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-12)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-13)constrewriterPrompt=ChatPromptTemplate.fromTemplate(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-14)REWRITER_PROMPT_TEMPLATE,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-15));
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-16)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-17)constrewriter=rewriterPrompt.pipe(llm).pipe(newStringOutputParser());
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-18)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-19)// Test run
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-20)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-21)// Test question is "agent memory"
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-22)awaitrewriter.invoke({question:testQuestion2});

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-17-1)What are memories stored in by agents?

```


### Web Search Tool[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#web-search-tool "Permanent link")

Finally, you'll need a web search tool that can handle questions out of scope from the indexed documents. The code below initializes a [Tavily-powered](https://js.langchain.com/docs/integrations/tools/tavily_search) search tool

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-18-1)import{TavilySearchResults}from"@langchain/community/tools/tavily_search";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-18-2)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-18-3)constwebSearchTool=newTavilySearchResults({maxResults:3});
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-18-4)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-18-5)awaitwebSearchTool.invoke("red robin");

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-19-1)[{"title":"Family Friendly Burger Restaurant | Red Robin","url":"https://www.redrobin.com/","content":"Red Robin is donating 10¢ to Make-A-Wish ® for every Kids Meal purchased. You can contribute to life-changing wishes by simply purchasing a Kids Meal at Red Robin for Dine-in or To-Go. Join us for a memorable meal or order online and help transform lives, one wish at a time.","score":0.998043,"raw_content":null},{"title":"Red Robin United States of America Directory","url":"https://locations.redrobin.com/locations-list/us/","content":"Maps, Driving Directions and Local Restaurant Information for Red Robin Restaurants in United States","score":0.99786776,"raw_content":null},{"title":"Red Robin Restaurant Locations","url":"https://locations.redrobin.com/","content":"Maps, Driving Directions and Local Restaurant Information for Red Robin","score":0.99718815,"raw_content":null}]

```


## Graph[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#graph "Permanent link")

Now that you've created all the necessary components, it's time to capture the flow as a graph.

### Graph state[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#graph-state "Permanent link")

Define the graph state like this. Since `question` and `generation` are simple strings, we can use `null` as a shorthand for default behavior:

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-1)importtype{Document}from"@langchain/core/documents";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-2)import{Annotation}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-3)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-4)// This defines the agent state.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-5)// Returned documents from a node will override the current
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-6)// "documents" value in the state object.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-7)constGraphState=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-8)question:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-9)generation:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-10)documents:Annotation<Document[]>({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-11)reducer:(_,y)=>y,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-12)default:()=>[],
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-13)})
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-14)})

```


### Preparing nodes and edges[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#preparing-nodes-and-edges "Permanent link")

Let's wrap our components in functions that match the interfaces required by LangGraph. These functions will handle formatting inputs and outputs.

We'll use some components within nodes, and others to define conditional edges. Each will take the graph state as a parameter. Nodes return state properties to be updated, while conditional edges return the name of the next node to execute.

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-1)import{Document}from"@langchain/core/documents";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-2)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-3)/* ---Nodes--- */
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-4)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-5)// Retrieve documents for a question
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-6)constretrieve=async(state:typeofGraphState.State):Promise<Partial<typeofGraphState.State>>=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-7)console.log("---RETRIEVE---");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-8)constdocuments=awaitretriever.invoke(state.question);
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-9)// Add sources to the state
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-10)return{documents};
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-11)};
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-12)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-13)// RAG generation
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-14)constgenerate=async(state:typeofGraphState.State):Promise<Partial<typeofGraphState.State>>=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-15)console.log("---GENERATE---");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-16)constgeneration=awaitragChain.invoke({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-17)context:formatDocs(state.documents),
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-18)question:state.question,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-19)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-20)// Add generation to the state
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-21)return{generation};
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-22)};
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-23)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-24)// Determines whether the retrieved documents are relevant to the question.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-25)constgradeDocuments=async(state:typeofGraphState.State):Promise<Partial<typeofGraphState.State>>=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-26)console.log("---CHECK DOCUMENT RELEVANCE TO QUESTION---");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-27)// Score each doc
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-28)constrelevantDocs:Document[]=[];
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-29)for(constdocofstate.documents){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-30)constgrade:{score:string}=awaitretrievalGrader.invoke({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-31)question:state.question,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-32)content:doc.pageContent,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-33)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-34)if(grade.score==="yes"){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-35)console.log("---GRADE: DOCUMENT RELEVANT---");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-36)relevantDocs.push(doc);
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-37)}else{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-38)console.log("---GRADE: DOCUMENT NOT RELEVANT---");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-39)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-40)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-41)return{documents:relevantDocs};
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-42)};
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-43)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-44)// Re-write question
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-45)consttransformQuery=async(state:typeofGraphState.State):Promise<Partial<typeofGraphState.State>>=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-46)console.log("---TRANSFORM QUERY---");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-47)constbetterQuestion=awaitrewriter.invoke({question:state.question});
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-48)return{question:betterQuestion};
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-49)};
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-50)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-51)// Web search based on the re-phrased question
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-52)constwebSearch=async(state:typeofGraphState.State):Promise<Partial<typeofGraphState.State>>=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-53)console.log("---WEB SEARCH---");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-54)conststringifiedSearchResults=awaitwebSearchTool.invoke(state.question);
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-55)return{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-56)documents:[newDocument({pageContent:stringifiedSearchResults})],
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-57)};
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-58)};
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-59)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-60)/* ---Edges--- */
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-61)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-62)// Decide on the datasource to route the initial question to.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-63)constrouteQuestion=async(state:typeofGraphState.State)=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-64)constsource:{datasource:string}=awaitquestionRouter.invoke({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-65)question:state.question,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-66)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-67)if(source.datasource==="web_search"){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-68)console.log(`---ROUTING QUESTION "${state.question} TO WEB SEARCH---`);
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-69)return"web_search";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-70)}else{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-71)console.log(`---ROUTING QUESTION "${state.question} TO RAG---`);
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-72)return"retrieve";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-73)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-74)};
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-75)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-76)// Decide whether the current documents are sufficiently relevant
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-77)// to come up with a good answer.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-78)constdecideToGenerate=async(state:typeofGraphState.State)=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-79)constfilteredDocuments=state.documents;
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-80)// All documents have been filtered as irrelevant
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-81)// Regenerate a new query and try again
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-82)if(filteredDocuments.length===0){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-83)console.log(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-84)"---DECISION: ALL DOCUMENTS ARE NOT RELEVANT TO QUESTION, TRANSFORM QUERY---",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-85));
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-86)return"transform_query";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-87)}else{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-88)// We have relevant documents, so generate answer.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-89)console.log("---DECISION: GENERATE---");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-90)return"generate";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-91)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-92)};
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-93)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-94)// Determines whether the generation is grounded in the document and answers question.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-95)constgradeGenerationDocumentsAndQuestion=async(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-96)state:typeofGraphState.State,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-97))=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-98)consthallucinationGrade:{score:string}=awaithallucinationGrader
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-99).invoke({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-100)generation:state.generation,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-101)context:formatDocs(state.documents),
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-102)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-103)// Check for hallucination
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-104)if(hallucinationGrade.score==="yes"){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-105)console.log("---DECISION: GENERATION IS GROUNDED IN DOCUMENTS---");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-106)// Check question answering
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-107)console.log("---GRADING GENERATION vs. QUESTION---");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-108)constonTopicGrade:{score:string}=awaitanswerGrader.invoke({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-109)question:state.question,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-110)generation:state.generation,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-111)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-112)if(onTopicGrade.score==="yes"){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-113)console.log("---DECISION: GENERATION ADDRESSES QUESTION---");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-114)return"useful";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-115)}else{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-116)console.log("---DECISION: GENERATION DOES NOT ADDRESS QUESTION---");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-117)return"not_useful";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-118)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-119)}else{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-120)console.log(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-121)"---DECISION: GENERATION IS NOT GROUNDED IN DOCUMENTS, RETRY---",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-122));
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-123)return"not_supported";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-124)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-125)};

```


## Build the graph[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#build-the-graph "Permanent link")

Now we build the graph. For fun, let's add a checkpointer and have the compiled graph pause before making a web search. This will simulate asking for permission.

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-22-1)import{END,MemorySaver,START,StateGraph}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-22-2)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-22-3)constgraph=newStateGraph(GraphState)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-22-4).addNode("web_search",webSearch)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-22-5).addNode("retrieve",retrieve)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-22-6).addNode("grade_documents",gradeDocuments)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-22-7).addNode("generate",generate)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-22-8).addNode("transform_query",transformQuery)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-22-9).addConditionalEdges(START,routeQuestion)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-22-10).addEdge("web_search","generate")
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-22-11).addEdge("retrieve","grade_documents")
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-22-12).addConditionalEdges("grade_documents",decideToGenerate)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-22-13).addEdge("transform_query","retrieve")
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-22-14).addConditionalEdges("generate",gradeGenerationDocumentsAndQuestion,{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-22-15)not_supported:"generate",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-22-16)useful:END,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-22-17)not_useful:"transform_query",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-22-18)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-22-19)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-22-20)constapp=graph.compile({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-22-21)checkpointer:newMemorySaver(),
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-22-22)interruptBefore:["web_search"],
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-22-23)});

```


## Running the graph[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#running-the-graph "Permanent link")

You're all set! Time to ask some questions. First, try a question about something related to agents:

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-23-1)awaitapp.invoke(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-23-2){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-23-3)question:"What are some features of long-term memory?",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-23-4)},
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-23-5){configurable:{thread_id:"1"}},
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-23-6));

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-24-1)---ROUTING QUESTION "What are some features of long-term memory? TO WEB SEARCH---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-24-2){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-24-3) question: 'What are some features of long-term memory?',
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-24-4) documents: []
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-24-5)}

```


You can see that your graph correctly routes the query to the vector store and answers the question, filtering out some documents as necessary. 

If you ask something not related to agents or LLMs, the graph should fall back to information gleaned from the web. The graph will pause before executing, as specified above:

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-25-1)awaitapp.invoke(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-25-2){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-25-3)question:"Where are the 2024 Euros being held?",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-25-4)},
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-25-5){configurable:{thread_id:"2"}},
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-25-6));

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-26-1)---ROUTING QUESTION "Where are the 2024 Euros being held? TO WEB SEARCH---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-26-2){ question: 'Where are the 2024 Euros being held?', documents: [] }

```


You can see the graph paused before running the web search. And now we continue by invoking the graph with `null`: 

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-27-1)awaitapp.invoke(null,{configurable:{thread_id:"2"}});

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-28-1)---WEB SEARCH---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-28-2)---GENERATE---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-28-3)---DECISION: GENERATION IS GROUNDED IN DOCUMENTS---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-28-4)---GRADING GENERATION vs. QUESTION---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-28-5)---DECISION: GENERATION ADDRESSES QUESTION---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-28-6){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-28-7) question: 'Where are the 2024 Euros being held?',
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-28-8) generation: 'The 2024 Euros are being held in Germany. The final match will take place at Olympiastadion Berlin on July 14, 2024.',
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-28-9) documents: [
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-28-10)  Document {
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-28-11)   pageContent: `[{"title":"Where is Euro 2024? Country, host cities and venues","url":"https://www.radiotimes.com/tv/sport/football/euro-2024-location/","content":"Euro 2024 stadiums The Olympiastadion Berlin, the biggest stadium in Germany with a capacity of around 74,000, will host games as well as the final on Sunday, 14th July, 2024.","score":0.99743915,"raw_content":null},{"title":"UEFA EURO 2024 venues - complete list: When and where will the opening ...","url":"https://olympics.com/en/news/uefa-euro-2024-venues-complete-list-when-where-final-opening-game","content":"UEFA EURO 2024 will be held in Germany across June and July, with 10 host cities staging the major football tournament.. It all begins in Munich on June 14, when hosts Germany take on Scotland in the tournament's opening game at Bayern Munich's stadium.. The final takes place a month later on July 14 at Olympiastadion Berlin in the German capital, which hosted the 2006 FIFA World Cup final ...","score":0.9973061,"raw_content":null},{"title":"EURO 2024: All you need to know | UEFA EURO 2024","url":"https://www.uefa.com/euro2024/news/0257-0e13b161b2e8-4a3fd5615e0c-1000--euro-2024-all-you-need-to-know/","content":"Article top media content\\nArticle body\\nWhere will EURO 2024 be held?\\nGermany will host EURO 2024, having been chosen to stage the 17th edition of the UEFA European Championship at a UEFA Executive Committee meeting in Nyon on 27 September 2018. Host cities\\nEURO 2024 fixtures by venue\\nEURO 2024 fixtures by team\\nAlso visit\\nChange language\\nServices links and disclaimer\\n© 1998-2024 UEFA. Where and when will the final of UEFA EURO 2024 be played?\\nBerlin's Olympiastadion will stage the final on Sunday 14 July 2024.\\n The ten venues chosen to host games at the tournament include nine of the stadiums used at the 2006 World Cup plus the Düsseldorf Arena.\\n All you need to know\\nThursday, January 11, 2024\\nArticle summary\\nThree-time winners Germany will stage the UEFA European Championship in 2024.\\n","score":0.99497885,"raw_content":null}]`,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-28-12)   metadata: {},
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-28-13)   id: undefined
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-28-14)  }
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-28-15) ]
[](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-28-16)}

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top 

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
