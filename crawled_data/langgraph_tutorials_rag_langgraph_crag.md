---
url: https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#corrective-rag-crag)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Corrective RAG (CRAG) 

[ ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/?q= "Share")

Type to start searching

[ GitHub  ](https://github.com/langchain-ai/langgraph "Go to repository")

  * [ Home ](https://langchain-ai.github.io/langgraph/)
  * [ API reference ](https://langchain-ai.github.io/langgraph/reference/graphs/)



[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

[ GitHub  ](https://github.com/langchain-ai/langgraph "Go to repository")

  * [ Home  ](https://langchain-ai.github.io/langgraph/)

Home 
    * Get started  Get started 
      * [ Learn the basics  ](https://langchain-ai.github.io/langgraph/tutorials/introduction/)
      * [ Deployment  ](https://langchain-ai.github.io/langgraph/tutorials/deployment/)
    * Guides  Guides 
      * [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
      * [ Concepts  ](https://langchain-ai.github.io/langgraph/concepts/)
      * [ Tutorials  ](https://langchain-ai.github.io/langgraph/tutorials/)

Tutorials 
        * [ Quick Start  ](https://langchain-ai.github.io/langgraph/tutorials#quick-start)
        * [ Chatbots  ](https://langchain-ai.github.io/langgraph/tutorials#chatbots)
        * RAG  RAG 
          * [ RAG  ](https://langchain-ai.github.io/langgraph/tutorials#rag)
          * [ Adaptive RAG  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/)
          * [ Langgraph adaptive rag local  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/)
          * [ Agentic RAG  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/)
          * Corrective RAG (CRAG)  [ Corrective RAG (CRAG)  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/) Table of contents 
            * [ Setup  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#setup)
            * [ Create Index  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#create-index)
            * [ LLMs  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#llms)
            * [ Web Search Tool  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#web-search-tool)
            * [ Create Graph  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#create-graph)
              * [ Define Graph State  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#define-graph-state)
              * [ Compile Graph  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#compile-graph)
            * [ Use the graph  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#use-the-graph)
          * [ Corrective RAG (CRAG) using local LLMs  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/)
          * [ Self-RAG  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/)
          * [ Self-RAG using local LLMs  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/)
          * [ An agent for interacting with a SQL database  ](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/)
        * [ Agent Architectures  ](https://langchain-ai.github.io/langgraph/tutorials#agent-architectures)
        * [ Evaluation & Analysis  ](https://langchain-ai.github.io/langgraph/tutorials#evaluation)
        * [ Experimental  ](https://langchain-ai.github.io/langgraph/tutorials#experimental)
        * [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/concepts#langgraph-platform)
    * Resources  Resources 
      * [ Prebuilt Agents  ](https://langchain-ai.github.io/langgraph/prebuilt/)
      * [ Adopters  ](https://langchain-ai.github.io/langgraph/adopters/)
      * [ FAQ  ](https://langchain-ai.github.io/langgraph/concepts/faq/)
      * [ Troubleshooting  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraph/reference/graphs/)



Table of contents 

  * [ Setup  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#setup)
  * [ Create Index  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#create-index)
  * [ LLMs  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#llms)
  * [ Web Search Tool  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#web-search-tool)
  * [ Create Graph  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#create-graph)
    * [ Define Graph State  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#define-graph-state)
    * [ Compile Graph  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#compile-graph)
  * [ Use the graph  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#use-the-graph)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ Tutorials  ](https://langchain-ai.github.io/langgraph/tutorials/)
  4. [ RAG  ](https://langchain-ai.github.io/langgraph/tutorials#rag)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/tutorials/rag/langgraph_crag.ipynb "Edit this page")

# Corrective RAG (CRAG)[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#corrective-rag-crag "Permanent link")

Corrective-RAG (CRAG) is a strategy for RAG that incorporates self-reflection / self-grading on retrieved documents. 

In the paper [here](https://arxiv.org/pdf/2401.15884.pdf), a few steps are taken:

  * If at least one document exceeds the threshold for relevance, then it proceeds to generation
  * Before generation, it performs knowledge refinement
  * This partitions the document into "knowledge strips"
  * It grades each strip, and filters our irrelevant ones
  * If all documents fall below the relevance threshold or if the grader is unsure, then the framework seeks an additional datasource
  * It will use web search to supplement retrieval



We will implement some of these ideas from scratch using [LangGraph](https://langchain-ai.github.io/langgraph/):

  * Let's skip the knowledge refinement phase as a first pass. This can be added back as a node, if desired. 
  * If _any_ documents are irrelevant, let's opt to supplement retrieval with web search. 
  * We'll use [Tavily Search](https://python.langchain.com/docs/integrations/tools/tavily_search/) for web search.
  * Let's use query re-writing to optimize the query for web search.



![Screenshot 2024-04-01 at 9.28.30 AM.png]()

## Setup[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#setup "Permanent link")

First, let's download our required packages and set our API keys

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-0-1)! pip install langchain_community tiktoken langchain-openai langchainhub chromadb langchain langgraph tavily-python

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-1-1)importgetpass
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-1-2)importos
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-1-5)def_set_env(key: str):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-1-6)  if key not in os.environ:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-1-7)    os.environ[key] = getpass.getpass(f"{key}:")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-1-8)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-1-10)_set_env("OPENAI_API_KEY")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-1-11)_set_env("TAVILY_API_KEY")

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Create Index[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#create-index "Permanent link")

Let's index 3 blog posts.

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-2-1)fromlangchain.text_splitterimport RecursiveCharacterTextSplitter
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-2-2)fromlangchain_community.document_loadersimport WebBaseLoader
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-2-3)fromlangchain_community.vectorstoresimport Chroma
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-2-4)fromlangchain_openaiimport OpenAIEmbeddings
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-2-5)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-2-6)urls = [
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-2-7)  "https://lilianweng.github.io/posts/2023-06-23-agent/",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-2-8)  "https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-2-9)  "https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-2-10)]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-2-11)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-2-12)docs = [WebBaseLoader(url).load() for url in urls]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-2-13)docs_list = [item for sublist in docs for item in sublist]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-2-14)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-2-15)text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-2-16)  chunk_size=250, chunk_overlap=0
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-2-17))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-2-18)doc_splits = text_splitter.split_documents(docs_list)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-2-19)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-2-20)# Add to vectorDB
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-2-21)vectorstore = Chroma.from_documents(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-2-22)  documents=doc_splits,
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-2-23)  collection_name="rag-chroma",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-2-24)  embedding=OpenAIEmbeddings(),
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-2-25))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-2-26)retriever = vectorstore.as_retriever()

```


API Reference: [RecursiveCharacterTextSplitter](https://python.langchain.com/api_reference/text_splitters/character/langchain_text_splitters.character.RecursiveCharacterTextSplitter.html) | [WebBaseLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.web_base.WebBaseLoader.html) | [Chroma](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.chroma.Chroma.html) | [OpenAIEmbeddings](https://python.langchain.com/api_reference/openai/embeddings/langchain_openai.embeddings.base.OpenAIEmbeddings.html)

## LLMs[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#llms "Permanent link")

Using Pydantic with LangChain

This notebook uses Pydantic v2 `BaseModel`, which requires `langchain-core >= 0.3`. Using `langchain-core < 0.3` will result in errors due to mixing of Pydantic v1 and v2 `BaseModels`. 

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-3-1)### Retrieval Grader
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-3-2)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-3-3)fromlangchain_core.promptsimport ChatPromptTemplate
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-3-4)fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-3-5)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-3-6)frompydanticimport BaseModel, Field
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-3-7)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-3-8)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-3-9)# Data model
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-3-10)classGradeDocuments(BaseModel):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-3-11)"""Binary score for relevance check on retrieved documents."""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-3-12)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-3-13)  binary_score: str = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-3-14)    description="Documents are relevant to the question, 'yes' or 'no'"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-3-15)  )
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-3-16)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-3-17)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-3-18)# LLM with function call
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-3-19)llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-3-20)structured_llm_grader = llm.with_structured_output(GradeDocuments)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-3-21)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-3-22)# Prompt
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-3-23)system = """You are a grader assessing relevance of a retrieved document to a user question. \n
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-3-24)  If the document contains keyword(s) or semantic meaning related to the question, grade it as relevant. \n
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-3-25)  Give a binary score 'yes' or 'no' score to indicate whether the document is relevant to the question."""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-3-26)grade_prompt = ChatPromptTemplate.from_messages(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-3-27)  [
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-3-28)    ("system", system),
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-3-29)    ("human", "Retrieved document: \n\n{document}\n\n User question: {question}"),
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-3-30)  ]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-3-31))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-3-32)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-3-33)retrieval_grader = grade_prompt | structured_llm_grader
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-3-34)question = "agent memory"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-3-35)docs = retriever.invoke(question)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-3-36)doc_txt = docs[1].page_content
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-3-37)print(retrieval_grader.invoke({"question": question, "document": doc_txt}))

```


API Reference: [ChatPromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html) | [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html)

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-4-1)binary_score='yes'

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-5-1)### Generate
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-5-2)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-5-3)fromlangchainimport hub
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-5-4)fromlangchain_core.output_parsersimport StrOutputParser
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-5-5)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-5-6)# Prompt
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-5-7)prompt = hub.pull("rlm/rag-prompt")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-5-8)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-5-9)# LLM
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-5-10)llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-5-11)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-5-12)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-5-13)# Post-processing
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-5-14)defformat_docs(docs):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-5-15)  return "\n\n".join(doc.page_content for doc in docs)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-5-16)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-5-17)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-5-18)# Chain
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-5-19)rag_chain = prompt | llm | StrOutputParser()
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-5-20)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-5-21)# Run
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-5-22)generation = rag_chain.invoke({"context": docs, "question": question})
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-5-23)print(generation)

```


API Reference: [StrOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.string.StrOutputParser.html)

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-6-1)The design of generative agents combines LLM with memory, planning, and reflection mechanisms to enable agents to behave conditioned on past experience. Memory stream is a long-term memory module that records a comprehensive list of agents' experience in natural language. Short-term memory is utilized for in-context learning, while long-term memory allows agents to retain and recall information over extended periods.

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-7-1)### Question Re-writer
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-7-2)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-7-3)# LLM
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-7-4)llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-7-5)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-7-6)# Prompt
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-7-7)system = """You a question re-writer that converts an input question to a better version that is optimized \n
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-7-8)   for web search. Look at the input and try to reason about the underlying semantic intent / meaning."""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-7-9)re_write_prompt = ChatPromptTemplate.from_messages(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-7-10)  [
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-7-11)    ("system", system),
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-7-12)    (
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-7-13)      "human",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-7-14)      "Here is the initial question: \n\n{question}\n Formulate an improved question.",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-7-15)    ),
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-7-16)  ]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-7-17))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-7-18)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-7-19)question_rewriter = re_write_prompt | llm | StrOutputParser()
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-7-20)question_rewriter.invoke({"question": question})

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-8-1)'What is the role of memory in artificial intelligence agents?'

```


## Web Search Tool[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#web-search-tool "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-9-1)### Search
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-9-2)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-9-3)fromlangchain_community.tools.tavily_searchimport TavilySearchResults
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-9-4)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-9-5)web_search_tool = TavilySearchResults(k=3)

```


API Reference: [TavilySearchResults](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.tavily_search.tool.TavilySearchResults.html)

## Create Graph[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#create-graph "Permanent link")

Now let's create our graph that will use CRAG

### Define Graph State[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#define-graph-state "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-10-1)fromtypingimport List
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-10-2)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-10-3)fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-10-4)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-10-5)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-10-6)classGraphState(TypedDict):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-10-7)"""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-10-8)  Represents the state of our graph.
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-10-9)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-10-10)  Attributes:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-10-11)    question: question
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-10-12)    generation: LLM generation
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-10-13)    web_search: whether to add search
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-10-14)    documents: list of documents
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-10-15)  """
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-10-16)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-10-17)  question: str
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-10-18)  generation: str
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-10-19)  web_search: str
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-10-20)  documents: List[str]

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-1)fromlangchain.schemaimport Document
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-2)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-3)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-4)defretrieve(state):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-5)"""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-6)  Retrieve documents
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-7)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-8)  Args:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-9)    state (dict): The current graph state
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-10)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-11)  Returns:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-12)    state (dict): New key added to state, documents, that contains retrieved documents
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-13)  """
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-14)  print("---RETRIEVE---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-15)  question = state["question"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-16)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-17)  # Retrieval
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-18)  documents = retriever.invoke(question)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-19)  return {"documents": documents, "question": question}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-20)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-21)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-22)defgenerate(state):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-23)"""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-24)  Generate answer
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-25)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-26)  Args:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-27)    state (dict): The current graph state
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-28)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-29)  Returns:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-30)    state (dict): New key added to state, generation, that contains LLM generation
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-31)  """
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-32)  print("---GENERATE---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-33)  question = state["question"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-34)  documents = state["documents"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-35)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-36)  # RAG generation
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-37)  generation = rag_chain.invoke({"context": documents, "question": question})
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-38)  return {"documents": documents, "question": question, "generation": generation}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-39)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-40)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-41)defgrade_documents(state):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-42)"""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-43)  Determines whether the retrieved documents are relevant to the question.
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-44)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-45)  Args:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-46)    state (dict): The current graph state
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-47)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-48)  Returns:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-49)    state (dict): Updates documents key with only filtered relevant documents
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-50)  """
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-51)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-52)  print("---CHECK DOCUMENT RELEVANCE TO QUESTION---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-53)  question = state["question"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-54)  documents = state["documents"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-55)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-56)  # Score each doc
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-57)  filtered_docs = []
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-58)  web_search = "No"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-59)  for d in documents:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-60)    score = retrieval_grader.invoke(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-61)      {"question": question, "document": d.page_content}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-62)    )
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-63)    grade = score.binary_score
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-64)    if grade == "yes":
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-65)      print("---GRADE: DOCUMENT RELEVANT---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-66)      filtered_docs.append(d)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-67)    else:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-68)      print("---GRADE: DOCUMENT NOT RELEVANT---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-69)      web_search = "Yes"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-70)      continue
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-71)  return {"documents": filtered_docs, "question": question, "web_search": web_search}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-72)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-73)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-74)deftransform_query(state):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-75)"""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-76)  Transform the query to produce a better question.
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-77)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-78)  Args:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-79)    state (dict): The current graph state
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-80)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-81)  Returns:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-82)    state (dict): Updates question key with a re-phrased question
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-83)  """
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-84)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-85)  print("---TRANSFORM QUERY---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-86)  question = state["question"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-87)  documents = state["documents"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-88)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-89)  # Re-write question
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-90)  better_question = question_rewriter.invoke({"question": question})
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-91)  return {"documents": documents, "question": better_question}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-92)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-93)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-94)defweb_search(state):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-95)"""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-96)  Web search based on the re-phrased question.
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-97)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-98)  Args:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-99)    state (dict): The current graph state
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-100)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-101)  Returns:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-102)    state (dict): Updates documents key with appended web results
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-103)  """
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-104)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-105)  print("---WEB SEARCH---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-106)  question = state["question"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-107)  documents = state["documents"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-108)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-109)  # Web search
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-110)  docs = web_search_tool.invoke({"query": question})
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-111)  web_results = "\n".join([d["content"] for d in docs])
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-112)  web_results = Document(page_content=web_results)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-113)  documents.append(web_results)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-114)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-115)  return {"documents": documents, "question": question}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-116)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-117)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-118)### Edges
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-119)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-120)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-121)defdecide_to_generate(state):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-122)"""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-123)  Determines whether to generate an answer, or re-generate a question.
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-124)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-125)  Args:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-126)    state (dict): The current graph state
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-127)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-128)  Returns:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-129)    str: Binary decision for next node to call
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-130)  """
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-131)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-132)  print("---ASSESS GRADED DOCUMENTS---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-133)  state["question"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-134)  web_search = state["web_search"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-135)  state["documents"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-136)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-137)  if web_search == "Yes":
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-138)    # All documents have been filtered check_relevance
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-139)    # We will re-generate a new query
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-140)    print(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-141)      "---DECISION: ALL DOCUMENTS ARE NOT RELEVANT TO QUESTION, TRANSFORM QUERY---"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-142)    )
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-143)    return "transform_query"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-144)  else:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-145)    # We have relevant documents, so generate answer
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-146)    print("---DECISION: GENERATE---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-11-147)    return "generate"

```


API Reference: [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html)

### Compile Graph[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#compile-graph "Permanent link")

The just follows the flow we outlined in the figure above.

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-12-1)fromlanggraph.graphimport END, StateGraph, START
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-12-2)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-12-3)workflow = StateGraph(GraphState)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-12-4)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-12-5)# Define the nodes
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-12-6)workflow.add_node("retrieve", retrieve) # retrieve
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-12-7)workflow.add_node("grade_documents", grade_documents) # grade documents
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-12-8)workflow.add_node("generate", generate) # generatae
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-12-9)workflow.add_node("transform_query", transform_query) # transform_query
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-12-10)workflow.add_node("web_search_node", web_search) # web search
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-12-11)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-12-12)# Build graph
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-12-13)workflow.add_edge(START, "retrieve")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-12-14)workflow.add_edge("retrieve", "grade_documents")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-12-15)workflow.add_conditional_edges(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-12-16)  "grade_documents",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-12-17)  decide_to_generate,
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-12-18)  {
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-12-19)    "transform_query": "transform_query",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-12-20)    "generate": "generate",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-12-21)  },
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-12-22))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-12-23)workflow.add_edge("transform_query", "web_search_node")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-12-24)workflow.add_edge("web_search_node", "generate")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-12-25)workflow.add_edge("generate", END)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-12-26)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-12-27)# Compile
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-12-28)app = workflow.compile()

```


API Reference: [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START)

## Use the graph[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#use-the-graph "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-13-1)frompprintimport pprint
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-13-2)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-13-3)# Run
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-13-4)inputs = {"question": "What are the types of agent memory?"}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-13-5)for output in app.stream(inputs):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-13-6)  for key, value in output.items():
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-13-7)    # Node
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-13-8)    pprint(f"Node '{key}':")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-13-9)    # Optional: print full state at each node
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-13-10)    # pprint.pprint(value["keys"], indent=2, width=80, depth=None)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-13-11)  pprint("\n---\n")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-13-12)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-13-13)# Final generation
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-13-14)pprint(value["generation"])

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-14-1)---RETRIEVE---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-14-2)"Node 'retrieve':"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-14-3)'\n---\n'
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-14-4)---CHECK DOCUMENT RELEVANCE TO QUESTION---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-14-5)---GRADE: DOCUMENT NOT RELEVANT---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-14-6)---GRADE: DOCUMENT NOT RELEVANT---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-14-7)---GRADE: DOCUMENT RELEVANT---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-14-8)---GRADE: DOCUMENT RELEVANT---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-14-9)"Node 'grade_documents':"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-14-10)'\n---\n'
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-14-11)---ASSESS GRADED DOCUMENTS---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-14-12)---DECISION: ALL DOCUMENTS ARE NOT RELEVANT TO QUESTION, TRANSFORM QUERY---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-14-13)---TRANSFORM QUERY---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-14-14)"Node 'transform_query':"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-14-15)'\n---\n'
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-14-16)---WEB SEARCH---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-14-17)"Node 'web_search_node':"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-14-18)'\n---\n'
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-14-19)---GENERATE---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-14-20)"Node 'generate':"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-14-21)'\n---\n'
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-14-22)"Node '__end__':"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-14-23)'\n---\n'
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-14-24)('Agents possess short-term memory, which is utilized for in-context learning, '
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-14-25) 'and long-term memory, allowing them to retain and recall vast amounts of '
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-14-26) 'information over extended periods. Some experts also classify working memory '
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-14-27) 'as a distinct type, although it can be considered a part of short-term '
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-14-28) 'memory in many cases.')

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-15-1)frompprintimport pprint
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-15-2)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-15-3)# Run
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-15-4)inputs = {"question": "How does the AlphaCodium paper work?"}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-15-5)for output in app.stream(inputs):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-15-6)  for key, value in output.items():
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-15-7)    # Node
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-15-8)    pprint(f"Node '{key}':")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-15-9)    # Optional: print full state at each node
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-15-10)    # pprint.pprint(value["keys"], indent=2, width=80, depth=None)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-15-11)  pprint("\n---\n")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-15-12)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-15-13)# Final generation
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-15-14)pprint(value["generation"])

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-16-1)---RETRIEVE---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-16-2)"Node 'retrieve':"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-16-3)'\n---\n'
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-16-4)---CHECK DOCUMENT RELEVANCE TO QUESTION---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-16-5)---GRADE: DOCUMENT NOT RELEVANT---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-16-6)---GRADE: DOCUMENT NOT RELEVANT---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-16-7)---GRADE: DOCUMENT NOT RELEVANT---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-16-8)---GRADE: DOCUMENT RELEVANT---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-16-9)"Node 'grade_documents':"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-16-10)'\n---\n'
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-16-11)---ASSESS GRADED DOCUMENTS---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-16-12)---DECISION: ALL DOCUMENTS ARE NOT RELEVANT TO QUESTION, TRANSFORM QUERY---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-16-13)---TRANSFORM QUERY---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-16-14)"Node 'transform_query':"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-16-15)'\n---\n'
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-16-16)---WEB SEARCH---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-16-17)"Node 'web_search_node':"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-16-18)'\n---\n'
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-16-19)---GENERATE---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-16-20)"Node 'generate':"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-16-21)'\n---\n'
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-16-22)"Node '__end__':"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-16-23)'\n---\n'
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-16-24)('The AlphaCodium paper functions by proposing a code-oriented iterative flow '
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-16-25) 'that involves repeatedly running and fixing generated code against '
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-16-26) 'input-output tests. Its key mechanisms include generating additional data '
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-16-27) 'like problem reflection and test reasoning to aid the iterative process, as '
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-16-28) 'well as enriching the code generation process. AlphaCodium aims to improve '
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-16-29) 'the performance of Large Language Models on code problems by following a '
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__codelineno-16-30) 'test-based, multi-stage approach.')

```


LangSmith Traces - 

  * <https://smith.langchain.com/public/f6b1716c-e842-4282-9112-1026b93e246b/r>

  * <https://smith.langchain.com/public/497c8ed9-d9e2-429e-8ada-e64de3ec26c9/r>


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Agentic RAG  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/) [ Next  Corrective RAG (CRAG) using local LLMs  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
