---
url: https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#adaptive-rag)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Adaptive RAG 

[ ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/?q= "Share")

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
          * Adaptive RAG  [ Adaptive RAG  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/) Table of contents 
            * [ Setup  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#setup)
            * [ Create Index  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#create-index)
            * [ LLMs  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#llms)
            * [ Web Search Tool  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#web-search-tool)
            * [ Construct the Graph  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#construct-the-graph)
              * [ Define Graph State  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#define-graph-state)
              * [ Define Graph Flow  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#define-graph-flow)
              * [ Compile Graph  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#compile-graph)
            * [ Use Graph  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#use-graph)
          * [ Langgraph adaptive rag local  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/)
          * [ Agentic RAG  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/)
          * [ Corrective RAG (CRAG)  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#setup)
  * [ Create Index  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#create-index)
  * [ LLMs  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#llms)
  * [ Web Search Tool  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#web-search-tool)
  * [ Construct the Graph  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#construct-the-graph)
    * [ Define Graph State  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#define-graph-state)
    * [ Define Graph Flow  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#define-graph-flow)
    * [ Compile Graph  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#compile-graph)
  * [ Use Graph  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#use-graph)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ Tutorials  ](https://langchain-ai.github.io/langgraph/tutorials/)
  4. [ RAG  ](https://langchain-ai.github.io/langgraph/tutorials#rag)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/tutorials/rag/langgraph_adaptive_rag.ipynb "Edit this page")

# Adaptive RAG[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#adaptive-rag "Permanent link")

Adaptive RAG is a strategy for RAG that unites (1) [query analysis](https://blog.langchain.dev/query-construction/) with (2) [active / self-corrective RAG](https://blog.langchain.dev/agentic-rag-with-langgraph/).

In the [paper](https://arxiv.org/abs/2403.14403), they report query analysis to route across:

  * No Retrieval
  * Single-shot RAG
  * Iterative RAG



Let's build on this using LangGraph. 

In our implementation, we will route between:

  * Web search: for questions related to recent events
  * Self-corrective RAG: for questions related to our index



![Screenshot 2024-03-26 at 1.36.03 PM.png]()

## Setup[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#setup "Permanent link")

First, let's install our required packages and set our API keys

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-0-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-0-2)%pip install -U langchain_community tiktoken langchain-openai langchain-cohere langchainhub chromadb langchain langgraph tavily-python

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-1-1)importgetpass
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-1-2)importos
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-1-5)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-1-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-1-7)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-1-8)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-1-10)_set_env("OPENAI_API_KEY")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-1-11)# _set_env("COHERE_API_KEY")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-1-12)_set_env("TAVILY_API_KEY")

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Create Index[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#create-index "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-2-1)### Build Index
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-2-2)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-2-3)fromlangchain.text_splitterimport RecursiveCharacterTextSplitter
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-2-4)fromlangchain_community.document_loadersimport WebBaseLoader
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-2-5)fromlangchain_community.vectorstoresimport Chroma
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-2-6)fromlangchain_openaiimport OpenAIEmbeddings
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-2-7)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-2-8)### from langchain_cohere import CohereEmbeddings
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-2-9)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-2-10)# Set embeddings
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-2-11)embd = OpenAIEmbeddings()
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-2-12)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-2-13)# Docs to index
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-2-14)urls = [
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-2-15)  "https://lilianweng.github.io/posts/2023-06-23-agent/",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-2-16)  "https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-2-17)  "https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-2-18)]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-2-19)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-2-20)# Load
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-2-21)docs = [WebBaseLoader(url).load() for url in urls]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-2-22)docs_list = [item for sublist in docs for item in sublist]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-2-23)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-2-24)# Split
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-2-25)text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-2-26)  chunk_size=500, chunk_overlap=0
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-2-27))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-2-28)doc_splits = text_splitter.split_documents(docs_list)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-2-29)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-2-30)# Add to vectorstore
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-2-31)vectorstore = Chroma.from_documents(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-2-32)  documents=doc_splits,
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-2-33)  collection_name="rag-chroma",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-2-34)  embedding=embd,
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-2-35))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-2-36)retriever = vectorstore.as_retriever()

```


API Reference: [RecursiveCharacterTextSplitter](https://python.langchain.com/api_reference/text_splitters/character/langchain_text_splitters.character.RecursiveCharacterTextSplitter.html) | [WebBaseLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.web_base.WebBaseLoader.html) | [Chroma](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.chroma.Chroma.html) | [OpenAIEmbeddings](https://python.langchain.com/api_reference/openai/embeddings/langchain_openai.embeddings.base.OpenAIEmbeddings.html) | [CohereEmbeddings](https://python.langchain.com/api_reference/cohere/embeddings/langchain_cohere.embeddings.CohereEmbeddings.html)

## LLMs[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#llms "Permanent link")

Using Pydantic with LangChain

This notebook uses Pydantic v2 `BaseModel`, which requires `langchain-core >= 0.3`. Using `langchain-core < 0.3` will result in errors due to mixing of Pydantic v1 and v2 `BaseModels`. 

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-3-1)### Router
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-3-2)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-3-3)fromtypingimport Literal
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-3-4)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-3-5)fromlangchain_core.promptsimport ChatPromptTemplate
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-3-6)fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-3-7)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-3-8)frompydanticimport BaseModel, Field
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-3-9)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-3-10)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-3-11)# Data model
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-3-12)classRouteQuery(BaseModel):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-3-13)"""Route a user query to the most relevant datasource."""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-3-14)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-3-15)  datasource: Literal["vectorstore", "web_search"] = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-3-16)    ...,
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-3-17)    description="Given a user question choose to route it to web search or a vectorstore.",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-3-18)  )
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-3-19)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-3-20)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-3-21)# LLM with function call
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-3-22)llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-3-23)structured_llm_router = llm.with_structured_output(RouteQuery)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-3-24)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-3-25)# Prompt
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-3-26)system = """You are an expert at routing a user question to a vectorstore or web search.
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-3-27)The vectorstore contains documents related to agents, prompt engineering, and adversarial attacks.
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-3-28)Use the vectorstore for questions on these topics. Otherwise, use web-search."""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-3-29)route_prompt = ChatPromptTemplate.from_messages(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-3-30)  [
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-3-31)    ("system", system),
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-3-32)    ("human", "{question}"),
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-3-33)  ]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-3-34))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-3-35)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-3-36)question_router = route_prompt | structured_llm_router
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-3-37)print(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-3-38)  question_router.invoke(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-3-39)    {"question": "Who will the Bears draft first in the NFL draft?"}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-3-40)  )
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-3-41))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-3-42)print(question_router.invoke({"question": "What are the types of agent memory?"}))

```


API Reference: [ChatPromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html) | [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html)

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-4-1)datasource='web_search'
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-4-2)datasource='vectorstore'

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-5-1)### Retrieval Grader
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-5-2)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-5-3)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-5-4)# Data model
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-5-5)classGradeDocuments(BaseModel):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-5-6)"""Binary score for relevance check on retrieved documents."""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-5-7)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-5-8)  binary_score: str = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-5-9)    description="Documents are relevant to the question, 'yes' or 'no'"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-5-10)  )
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-5-11)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-5-12)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-5-13)# LLM with function call
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-5-14)llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-5-15)structured_llm_grader = llm.with_structured_output(GradeDocuments)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-5-16)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-5-17)# Prompt
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-5-18)system = """You are a grader assessing relevance of a retrieved document to a user question. \n
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-5-19)  If the document contains keyword(s) or semantic meaning related to the user question, grade it as relevant. \n
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-5-20)  It does not need to be a stringent test. The goal is to filter out erroneous retrievals. \n
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-5-21)  Give a binary score 'yes' or 'no' score to indicate whether the document is relevant to the question."""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-5-22)grade_prompt = ChatPromptTemplate.from_messages(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-5-23)  [
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-5-24)    ("system", system),
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-5-25)    ("human", "Retrieved document: \n\n{document}\n\n User question: {question}"),
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-5-26)  ]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-5-27))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-5-28)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-5-29)retrieval_grader = grade_prompt | structured_llm_grader
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-5-30)question = "agent memory"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-5-31)docs = retriever.invoke(question)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-5-32)doc_txt = docs[1].page_content
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-5-33)print(retrieval_grader.invoke({"question": question, "document": doc_txt}))

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-6-1)binary_score='yes'

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-7-1)### Generate
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-7-2)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-7-3)fromlangchainimport hub
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-7-4)fromlangchain_core.output_parsersimport StrOutputParser
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-7-5)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-7-6)# Prompt
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-7-7)prompt = hub.pull("rlm/rag-prompt")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-7-8)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-7-9)# LLM
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-7-10)llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-7-11)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-7-12)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-7-13)# Post-processing
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-7-14)defformat_docs(docs):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-7-15)  return "\n\n".join(doc.page_content for doc in docs)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-7-16)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-7-17)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-7-18)# Chain
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-7-19)rag_chain = prompt | llm | StrOutputParser()
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-7-20)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-7-21)# Run
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-7-22)generation = rag_chain.invoke({"context": docs, "question": question})
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-7-23)print(generation)

```


API Reference: [StrOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.string.StrOutputParser.html)

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-8-1)Agent memory in LLM-powered autonomous systems consists of short-term and long-term memory. Short-term memory utilizes in-context learning for immediate tasks, while long-term memory allows agents to retain and recall information over extended periods, often using external storage for efficient retrieval. This memory structure supports the agent's ability to reflect on past actions and improve future performance.

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-9-1)### Hallucination Grader
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-9-2)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-9-3)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-9-4)# Data model
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-9-5)classGradeHallucinations(BaseModel):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-9-6)"""Binary score for hallucination present in generation answer."""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-9-7)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-9-8)  binary_score: str = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-9-9)    description="Answer is grounded in the facts, 'yes' or 'no'"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-9-10)  )
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-9-11)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-9-12)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-9-13)# LLM with function call
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-9-14)llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-9-15)structured_llm_grader = llm.with_structured_output(GradeHallucinations)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-9-16)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-9-17)# Prompt
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-9-18)system = """You are a grader assessing whether an LLM generation is grounded in / supported by a set of retrieved facts. \n
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-9-19)   Give a binary score 'yes' or 'no'. 'Yes' means that the answer is grounded in / supported by the set of facts."""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-9-20)hallucination_prompt = ChatPromptTemplate.from_messages(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-9-21)  [
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-9-22)    ("system", system),
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-9-23)    ("human", "Set of facts: \n\n{documents}\n\n LLM generation: {generation}"),
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-9-24)  ]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-9-25))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-9-26)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-9-27)hallucination_grader = hallucination_prompt | structured_llm_grader
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-9-28)hallucination_grader.invoke({"documents": docs, "generation": generation})

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-10-1)GradeHallucinations(binary_score='yes')

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-11-1)### Answer Grader
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-11-2)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-11-3)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-11-4)# Data model
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-11-5)classGradeAnswer(BaseModel):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-11-6)"""Binary score to assess answer addresses question."""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-11-7)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-11-8)  binary_score: str = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-11-9)    description="Answer addresses the question, 'yes' or 'no'"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-11-10)  )
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-11-11)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-11-12)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-11-13)# LLM with function call
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-11-14)llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-11-15)structured_llm_grader = llm.with_structured_output(GradeAnswer)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-11-16)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-11-17)# Prompt
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-11-18)system = """You are a grader assessing whether an answer addresses / resolves a question \n
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-11-19)   Give a binary score 'yes' or 'no'. Yes' means that the answer resolves the question."""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-11-20)answer_prompt = ChatPromptTemplate.from_messages(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-11-21)  [
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-11-22)    ("system", system),
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-11-23)    ("human", "User question: \n\n{question}\n\n LLM generation: {generation}"),
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-11-24)  ]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-11-25))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-11-26)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-11-27)answer_grader = answer_prompt | structured_llm_grader
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-11-28)answer_grader.invoke({"question": question, "generation": generation})

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-12-1)GradeAnswer(binary_score='yes')

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-13-1)### Question Re-writer
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-13-2)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-13-3)# LLM
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-13-4)llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-13-5)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-13-6)# Prompt
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-13-7)system = """You a question re-writer that converts an input question to a better version that is optimized \n
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-13-8)   for vectorstore retrieval. Look at the input and try to reason about the underlying semantic intent / meaning."""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-13-9)re_write_prompt = ChatPromptTemplate.from_messages(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-13-10)  [
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-13-11)    ("system", system),
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-13-12)    (
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-13-13)      "human",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-13-14)      "Here is the initial question: \n\n{question}\n Formulate an improved question.",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-13-15)    ),
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-13-16)  ]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-13-17))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-13-18)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-13-19)question_rewriter = re_write_prompt | llm | StrOutputParser()
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-13-20)question_rewriter.invoke({"question": question})

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-14-1)'What are the key concepts and techniques related to agent memory in artificial intelligence?'

```


## Web Search Tool[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#web-search-tool "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-15-1)### Search
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-15-2)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-15-3)fromlangchain_community.tools.tavily_searchimport TavilySearchResults
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-15-4)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-15-5)web_search_tool = TavilySearchResults(k=3)

```


API Reference: [TavilySearchResults](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.tavily_search.tool.TavilySearchResults.html)

## Construct the Graph[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#construct-the-graph "Permanent link")

Capture the flow in as a graph.

### Define Graph State[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#define-graph-state "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-16-1)fromtypingimport List
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-16-2)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-16-3)fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-16-4)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-16-5)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-16-6)classGraphState(TypedDict):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-16-7)"""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-16-8)  Represents the state of our graph.
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-16-9)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-16-10)  Attributes:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-16-11)    question: question
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-16-12)    generation: LLM generation
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-16-13)    documents: list of documents
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-16-14)  """
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-16-15)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-16-16)  question: str
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-16-17)  generation: str
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-16-18)  documents: List[str]

```


### Define Graph Flow[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#define-graph-flow "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-1)fromlangchain.schemaimport Document
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-2)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-3)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-4)defretrieve(state):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-5)"""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-6)  Retrieve documents
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-7)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-8)  Args:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-9)    state (dict): The current graph state
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-10)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-11)  Returns:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-12)    state (dict): New key added to state, documents, that contains retrieved documents
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-13)  """
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-14)  print("---RETRIEVE---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-15)  question = state["question"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-16)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-17)  # Retrieval
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-18)  documents = retriever.invoke(question)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-19)  return {"documents": documents, "question": question}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-20)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-21)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-22)defgenerate(state):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-23)"""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-24)  Generate answer
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-25)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-26)  Args:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-27)    state (dict): The current graph state
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-28)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-29)  Returns:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-30)    state (dict): New key added to state, generation, that contains LLM generation
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-31)  """
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-32)  print("---GENERATE---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-33)  question = state["question"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-34)  documents = state["documents"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-35)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-36)  # RAG generation
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-37)  generation = rag_chain.invoke({"context": documents, "question": question})
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-38)  return {"documents": documents, "question": question, "generation": generation}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-39)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-40)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-41)defgrade_documents(state):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-42)"""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-43)  Determines whether the retrieved documents are relevant to the question.
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-44)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-45)  Args:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-46)    state (dict): The current graph state
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-47)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-48)  Returns:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-49)    state (dict): Updates documents key with only filtered relevant documents
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-50)  """
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-51)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-52)  print("---CHECK DOCUMENT RELEVANCE TO QUESTION---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-53)  question = state["question"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-54)  documents = state["documents"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-55)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-56)  # Score each doc
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-57)  filtered_docs = []
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-58)  for d in documents:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-59)    score = retrieval_grader.invoke(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-60)      {"question": question, "document": d.page_content}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-61)    )
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-62)    grade = score.binary_score
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-63)    if grade == "yes":
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-64)      print("---GRADE: DOCUMENT RELEVANT---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-65)      filtered_docs.append(d)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-66)    else:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-67)      print("---GRADE: DOCUMENT NOT RELEVANT---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-68)      continue
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-69)  return {"documents": filtered_docs, "question": question}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-70)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-71)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-72)deftransform_query(state):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-73)"""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-74)  Transform the query to produce a better question.
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-75)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-76)  Args:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-77)    state (dict): The current graph state
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-78)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-79)  Returns:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-80)    state (dict): Updates question key with a re-phrased question
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-81)  """
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-82)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-83)  print("---TRANSFORM QUERY---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-84)  question = state["question"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-85)  documents = state["documents"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-86)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-87)  # Re-write question
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-88)  better_question = question_rewriter.invoke({"question": question})
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-89)  return {"documents": documents, "question": better_question}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-90)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-91)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-92)defweb_search(state):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-93)"""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-94)  Web search based on the re-phrased question.
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-95)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-96)  Args:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-97)    state (dict): The current graph state
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-98)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-99)  Returns:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-100)    state (dict): Updates documents key with appended web results
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-101)  """
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-102)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-103)  print("---WEB SEARCH---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-104)  question = state["question"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-105)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-106)  # Web search
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-107)  docs = web_search_tool.invoke({"query": question})
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-108)  web_results = "\n".join([d["content"] for d in docs])
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-109)  web_results = Document(page_content=web_results)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-110)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-111)  return {"documents": web_results, "question": question}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-112)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-113)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-114)### Edges ###
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-115)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-116)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-117)defroute_question(state):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-118)"""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-119)  Route question to web search or RAG.
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-120)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-121)  Args:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-122)    state (dict): The current graph state
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-123)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-124)  Returns:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-125)    str: Next node to call
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-126)  """
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-127)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-128)  print("---ROUTE QUESTION---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-129)  question = state["question"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-130)  source = question_router.invoke({"question": question})
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-131)  if source.datasource == "web_search":
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-132)    print("---ROUTE QUESTION TO WEB SEARCH---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-133)    return "web_search"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-134)  elif source.datasource == "vectorstore":
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-135)    print("---ROUTE QUESTION TO RAG---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-136)    return "vectorstore"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-137)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-138)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-139)defdecide_to_generate(state):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-140)"""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-141)  Determines whether to generate an answer, or re-generate a question.
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-142)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-143)  Args:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-144)    state (dict): The current graph state
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-145)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-146)  Returns:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-147)    str: Binary decision for next node to call
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-148)  """
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-149)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-150)  print("---ASSESS GRADED DOCUMENTS---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-151)  state["question"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-152)  filtered_documents = state["documents"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-153)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-154)  if not filtered_documents:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-155)    # All documents have been filtered check_relevance
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-156)    # We will re-generate a new query
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-157)    print(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-158)      "---DECISION: ALL DOCUMENTS ARE NOT RELEVANT TO QUESTION, TRANSFORM QUERY---"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-159)    )
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-160)    return "transform_query"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-161)  else:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-162)    # We have relevant documents, so generate answer
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-163)    print("---DECISION: GENERATE---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-164)    return "generate"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-165)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-166)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-167)defgrade_generation_v_documents_and_question(state):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-168)"""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-169)  Determines whether the generation is grounded in the document and answers question.
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-170)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-171)  Args:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-172)    state (dict): The current graph state
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-173)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-174)  Returns:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-175)    str: Decision for next node to call
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-176)  """
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-177)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-178)  print("---CHECK HALLUCINATIONS---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-179)  question = state["question"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-180)  documents = state["documents"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-181)  generation = state["generation"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-182)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-183)  score = hallucination_grader.invoke(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-184)    {"documents": documents, "generation": generation}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-185)  )
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-186)  grade = score.binary_score
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-187)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-188)  # Check hallucination
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-189)  if grade == "yes":
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-190)    print("---DECISION: GENERATION IS GROUNDED IN DOCUMENTS---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-191)    # Check question-answering
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-192)    print("---GRADE GENERATION vs QUESTION---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-193)    score = answer_grader.invoke({"question": question, "generation": generation})
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-194)    grade = score.binary_score
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-195)    if grade == "yes":
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-196)      print("---DECISION: GENERATION ADDRESSES QUESTION---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-197)      return "useful"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-198)    else:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-199)      print("---DECISION: GENERATION DOES NOT ADDRESS QUESTION---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-200)      return "not useful"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-201)  else:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-202)    pprint("---DECISION: GENERATION IS NOT GROUNDED IN DOCUMENTS, RE-TRY---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-17-203)    return "not supported"

```


API Reference: [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html)

### Compile Graph[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#compile-graph "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-18-1)fromlanggraph.graphimport END, StateGraph, START
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-18-2)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-18-3)workflow = StateGraph(GraphState)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-18-4)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-18-5)# Define the nodes
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-18-6)workflow.add_node("web_search", web_search) # web search
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-18-7)workflow.add_node("retrieve", retrieve) # retrieve
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-18-8)workflow.add_node("grade_documents", grade_documents) # grade documents
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-18-9)workflow.add_node("generate", generate) # generatae
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-18-10)workflow.add_node("transform_query", transform_query) # transform_query
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-18-11)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-18-12)# Build graph
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-18-13)workflow.add_conditional_edges(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-18-14)  START,
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-18-15)  route_question,
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-18-16)  {
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-18-17)    "web_search": "web_search",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-18-18)    "vectorstore": "retrieve",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-18-19)  },
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-18-20))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-18-21)workflow.add_edge("web_search", "generate")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-18-22)workflow.add_edge("retrieve", "grade_documents")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-18-23)workflow.add_conditional_edges(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-18-24)  "grade_documents",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-18-25)  decide_to_generate,
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-18-26)  {
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-18-27)    "transform_query": "transform_query",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-18-28)    "generate": "generate",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-18-29)  },
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-18-30))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-18-31)workflow.add_edge("transform_query", "retrieve")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-18-32)workflow.add_conditional_edges(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-18-33)  "generate",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-18-34)  grade_generation_v_documents_and_question,
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-18-35)  {
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-18-36)    "not supported": "generate",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-18-37)    "useful": END,
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-18-38)    "not useful": "transform_query",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-18-39)  },
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-18-40))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-18-41)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-18-42)# Compile
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-18-43)app = workflow.compile()

```


API Reference: [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START)

## Use Graph[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#use-graph "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-19-1)frompprintimport pprint
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-19-2)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-19-3)# Run
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-19-4)inputs = {
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-19-5)  "question": "What player at the Bears expected to draft first in the 2024 NFL draft?"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-19-6)}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-19-7)for output in app.stream(inputs):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-19-8)  for key, value in output.items():
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-19-9)    # Node
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-19-10)    pprint(f"Node '{key}':")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-19-11)    # Optional: print full state at each node
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-19-12)    # pprint.pprint(value["keys"], indent=2, width=80, depth=None)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-19-13)  pprint("\n---\n")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-19-14)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-19-15)# Final generation
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-19-16)pprint(value["generation"])

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-20-1)---ROUTE QUESTION---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-20-2)---ROUTE QUESTION TO WEB SEARCH---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-20-3)---WEB SEARCH---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-20-4)"Node 'web_search':"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-20-5)'\n---\n'
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-20-6)---GENERATE---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-20-7)---CHECK HALLUCINATIONS---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-20-8)---DECISION: GENERATION IS GROUNDED IN DOCUMENTS---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-20-9)---GRADE GENERATION vs QUESTION---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-20-10)---DECISION: GENERATION ADDRESSES QUESTION---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-20-11)"Node 'generate':"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-20-12)'\n---\n'
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-20-13)('The Chicago Bears are expected to draft quarterback Caleb Williams first '
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-20-14) 'overall in the 2024 NFL Draft. They also have a second first-round pick, '
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-20-15) 'where they selected wide receiver Rome Odunze.')

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-21-1)# Run
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-21-2)inputs = {"question": "What are the types of agent memory?"}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-21-3)for output in app.stream(inputs):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-21-4)  for key, value in output.items():
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-21-5)    # Node
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-21-6)    pprint(f"Node '{key}':")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-21-7)    # Optional: print full state at each node
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-21-8)    # pprint.pprint(value["keys"], indent=2, width=80, depth=None)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-21-9)  pprint("\n---\n")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-21-10)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-21-11)# Final generation
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-21-12)pprint(value["generation"])

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-22-1)---ROUTE QUESTION---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-22-2)---ROUTE QUESTION TO RAG---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-22-3)---RETRIEVE---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-22-4)"Node 'retrieve':"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-22-5)'\n---\n'
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-22-6)---CHECK DOCUMENT RELEVANCE TO QUESTION---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-22-7)---GRADE: DOCUMENT NOT RELEVANT---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-22-8)---GRADE: DOCUMENT RELEVANT---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-22-9)---GRADE: DOCUMENT NOT RELEVANT---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-22-10)---GRADE: DOCUMENT RELEVANT---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-22-11)---ASSESS GRADED DOCUMENTS---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-22-12)---DECISION: GENERATE---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-22-13)"Node 'grade_documents':"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-22-14)'\n---\n'
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-22-15)---GENERATE---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-22-16)---CHECK HALLUCINATIONS---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-22-17)---DECISION: GENERATION IS GROUNDED IN DOCUMENTS---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-22-18)---GRADE GENERATION vs QUESTION---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-22-19)---DECISION: GENERATION ADDRESSES QUESTION---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-22-20)"Node 'generate':"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-22-21)'\n---\n'
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-22-22)('The types of agent memory include short-term memory, long-term memory, and '
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-22-23) 'sensory memory. Short-term memory is utilized for in-context learning, while '
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-22-24) 'long-term memory allows for the retention and recall of information over '
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-22-25) 'extended periods. Sensory memory involves learning embedding representations '
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__codelineno-22-26) 'for various raw inputs, such as text and images.')

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Code generation with RAG and self-correction  ](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/) [ Next  Langgraph adaptive rag local  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
