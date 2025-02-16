---
url: https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#self-rag)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Self-RAG 

[ ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/?q= "Share")

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
          * [ Corrective RAG (CRAG)  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/)
          * [ Corrective RAG (CRAG) using local LLMs  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/)
          * Self-RAG  [ Self-RAG  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/) Table of contents 
            * [ Setup  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#setup)
            * [ Retriever  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#retriever)
            * [ LLMs  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#llms)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#setup)
  * [ Retriever  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#retriever)
  * [ LLMs  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#llms)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ Tutorials  ](https://langchain-ai.github.io/langgraph/tutorials/)
  4. [ RAG  ](https://langchain-ai.github.io/langgraph/tutorials#rag)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/tutorials/rag/langgraph_self_rag.ipynb "Edit this page")

# Self-RAG[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#self-rag "Permanent link")

Self-RAG is a strategy for RAG that incorporates self-reflection / self-grading on retrieved documents and generations. 

In the [paper](https://arxiv.org/abs/2310.11511), a few decisions are made:

  1. Should I retrieve from retriever, `R` -

  2. Input: `x (question)` OR `x (question)`, `y (generation)`

  3. Decides when to retrieve `D` chunks with `R`
  4. Output: `yes, no, continue`

  5. Are the retrieved passages `D` relevant to the question `x` -

  6.      * Input: (`x (question)`, `d (chunk)`) for `d` in `D`
  7. `d` provides useful information to solve `x`
  8. Output: `relevant, irrelevant`

  9. Are the LLM generation from each chunk in `D` is relevant to the chunk (hallucinations, etc) -

  10. Input: `x (question)`, `d (chunk)`, `y (generation)` for `d` in `D`

  11. All of the verification-worthy statements in `y (generation)` are supported by `d`
  12. Output: `{fully supported, partially supported, no support`

  13. The LLM generation from each chunk in `D` is a useful response to `x (question)` -

  14. Input: `x (question)`, `y (generation)` for `d` in `D`

  15. `y (generation)` is a useful response to `x (question)`.
  16. Output: `{5, 4, 3, 2, 1}`



We will implement some of these ideas from scratch using [LangGraph](https://langchain-ai.github.io/langgraph/).

![Screenshot 2024-04-01 at 12.41.50 PM.png]()

## Setup[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#setup "Permanent link")

First let's install our required packages and set our API keys

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-0-1)%pip install -U langchain_community tiktoken langchain-openai langchainhub chromadb langchain langgraph

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-1-1)importgetpass
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-1-2)importos
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-1-5)def_set_env(key: str):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-1-6)  if key not in os.environ:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-1-7)    os.environ[key] = getpass.getpass(f"{key}:")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-1-8)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-1-10)_set_env("OPENAI_API_KEY")

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Retriever[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#retriever "Permanent link")

Let's index 3 blog posts.

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-2-1)fromlangchain.text_splitterimport RecursiveCharacterTextSplitter
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-2-2)fromlangchain_community.document_loadersimport WebBaseLoader
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-2-3)fromlangchain_community.vectorstoresimport Chroma
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-2-4)fromlangchain_openaiimport OpenAIEmbeddings
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-2-5)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-2-6)urls = [
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-2-7)  "https://lilianweng.github.io/posts/2023-06-23-agent/",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-2-8)  "https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-2-9)  "https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-2-10)]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-2-11)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-2-12)docs = [WebBaseLoader(url).load() for url in urls]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-2-13)docs_list = [item for sublist in docs for item in sublist]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-2-14)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-2-15)text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-2-16)  chunk_size=250, chunk_overlap=0
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-2-17))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-2-18)doc_splits = text_splitter.split_documents(docs_list)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-2-19)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-2-20)# Add to vectorDB
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-2-21)vectorstore = Chroma.from_documents(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-2-22)  documents=doc_splits,
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-2-23)  collection_name="rag-chroma",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-2-24)  embedding=OpenAIEmbeddings(),
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-2-25))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-2-26)retriever = vectorstore.as_retriever()

```


API Reference: [RecursiveCharacterTextSplitter](https://python.langchain.com/api_reference/text_splitters/character/langchain_text_splitters.character.RecursiveCharacterTextSplitter.html) | [WebBaseLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.web_base.WebBaseLoader.html) | [Chroma](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.chroma.Chroma.html) | [OpenAIEmbeddings](https://python.langchain.com/api_reference/openai/embeddings/langchain_openai.embeddings.base.OpenAIEmbeddings.html)

## LLMs[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#llms "Permanent link")

Using Pydantic with LangChain

This notebook uses Pydantic v2 `BaseModel`, which requires `langchain-core >= 0.3`. Using `langchain-core < 0.3` will result in errors due to mixing of Pydantic v1 and v2 `BaseModels`. 

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-3-1)### Retrieval Grader
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-3-2)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-3-3)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-3-4)fromlangchain_core.promptsimport ChatPromptTemplate
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-3-5)fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-3-6)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-3-7)frompydanticimport BaseModel, Field
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-3-8)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-3-9)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-3-10)# Data model
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-3-11)classGradeDocuments(BaseModel):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-3-12)"""Binary score for relevance check on retrieved documents."""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-3-13)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-3-14)  binary_score: str = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-3-15)    description="Documents are relevant to the question, 'yes' or 'no'"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-3-16)  )
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-3-17)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-3-18)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-3-19)# LLM with function call
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-3-20)llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-3-21)structured_llm_grader = llm.with_structured_output(GradeDocuments)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-3-22)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-3-23)# Prompt
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-3-24)system = """You are a grader assessing relevance of a retrieved document to a user question. \n
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-3-25)  It does not need to be a stringent test. The goal is to filter out erroneous retrievals. \n
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-3-26)  If the document contains keyword(s) or semantic meaning related to the user question, grade it as relevant. \n
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-3-27)  Give a binary score 'yes' or 'no' score to indicate whether the document is relevant to the question."""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-3-28)grade_prompt = ChatPromptTemplate.from_messages(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-3-29)  [
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-3-30)    ("system", system),
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-3-31)    ("human", "Retrieved document: \n\n{document}\n\n User question: {question}"),
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-3-32)  ]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-3-33))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-3-34)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-3-35)retrieval_grader = grade_prompt | structured_llm_grader
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-3-36)question = "agent memory"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-3-37)docs = retriever.invoke(question)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-3-38)doc_txt = docs[1].page_content
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-3-39)print(retrieval_grader.invoke({"question": question, "document": doc_txt}))

```


API Reference: [ChatPromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html) | [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html)

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-4-1)binary_score='no'

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-5-1)### Generate
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-5-2)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-5-3)fromlangchainimport hub
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-5-4)fromlangchain_core.output_parsersimport StrOutputParser
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-5-5)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-5-6)# Prompt
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-5-7)prompt = hub.pull("rlm/rag-prompt")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-5-8)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-5-9)# LLM
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-5-10)llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-5-11)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-5-12)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-5-13)# Post-processing
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-5-14)defformat_docs(docs):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-5-15)  return "\n\n".join(doc.page_content for doc in docs)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-5-16)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-5-17)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-5-18)# Chain
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-5-19)rag_chain = prompt | llm | StrOutputParser()
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-5-20)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-5-21)# Run
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-5-22)generation = rag_chain.invoke({"context": docs, "question": question})
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-5-23)print(generation)

```


API Reference: [StrOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.string.StrOutputParser.html)

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-6-1)The design of generative agents combines LLM with memory, planning, and reflection mechanisms to enable agents to behave conditioned on past experience. Memory stream is a long-term memory module that records a comprehensive list of agents' experience in natural language. LLM functions as the agent's brain in an autonomous agent system.

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-7-1)### Hallucination Grader
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-7-2)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-7-3)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-7-4)# Data model
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-7-5)classGradeHallucinations(BaseModel):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-7-6)"""Binary score for hallucination present in generation answer."""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-7-7)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-7-8)  binary_score: str = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-7-9)    description="Answer is grounded in the facts, 'yes' or 'no'"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-7-10)  )
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-7-11)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-7-12)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-7-13)# LLM with function call
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-7-14)llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-7-15)structured_llm_grader = llm.with_structured_output(GradeHallucinations)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-7-16)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-7-17)# Prompt
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-7-18)system = """You are a grader assessing whether an LLM generation is grounded in / supported by a set of retrieved facts. \n
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-7-19)   Give a binary score 'yes' or 'no'. 'Yes' means that the answer is grounded in / supported by the set of facts."""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-7-20)hallucination_prompt = ChatPromptTemplate.from_messages(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-7-21)  [
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-7-22)    ("system", system),
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-7-23)    ("human", "Set of facts: \n\n{documents}\n\n LLM generation: {generation}"),
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-7-24)  ]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-7-25))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-7-26)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-7-27)hallucination_grader = hallucination_prompt | structured_llm_grader
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-7-28)hallucination_grader.invoke({"documents": docs, "generation": generation})

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-8-1)GradeHallucinations(binary_score='yes')

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-9-1)### Answer Grader
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-9-2)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-9-3)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-9-4)# Data model
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-9-5)classGradeAnswer(BaseModel):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-9-6)"""Binary score to assess answer addresses question."""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-9-7)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-9-8)  binary_score: str = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-9-9)    description="Answer addresses the question, 'yes' or 'no'"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-9-10)  )
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-9-11)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-9-12)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-9-13)# LLM with function call
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-9-14)llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-9-15)structured_llm_grader = llm.with_structured_output(GradeAnswer)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-9-16)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-9-17)# Prompt
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-9-18)system = """You are a grader assessing whether an answer addresses / resolves a question \n
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-9-19)   Give a binary score 'yes' or 'no'. Yes' means that the answer resolves the question."""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-9-20)answer_prompt = ChatPromptTemplate.from_messages(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-9-21)  [
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-9-22)    ("system", system),
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-9-23)    ("human", "User question: \n\n{question}\n\n LLM generation: {generation}"),
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-9-24)  ]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-9-25))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-9-26)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-9-27)answer_grader = answer_prompt | structured_llm_grader
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-9-28)answer_grader.invoke({"question": question, "generation": generation})

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-10-1)GradeAnswer(binary_score='yes')

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-11-1)### Question Re-writer
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-11-2)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-11-3)# LLM
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-11-4)llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-11-5)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-11-6)# Prompt
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-11-7)system = """You a question re-writer that converts an input question to a better version that is optimized \n
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-11-8)   for vectorstore retrieval. Look at the input and try to reason about the underlying semantic intent / meaning."""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-11-9)re_write_prompt = ChatPromptTemplate.from_messages(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-11-10)  [
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-11-11)    ("system", system),
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-11-12)    (
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-11-13)      "human",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-11-14)      "Here is the initial question: \n\n{question}\n Formulate an improved question.",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-11-15)    ),
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-11-16)  ]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-11-17))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-11-18)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-11-19)question_rewriter = re_write_prompt | llm | StrOutputParser()
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-11-20)question_rewriter.invoke({"question": question})

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-12-1)"What is the role of memory in an agent's functioning?"

```


# Graph[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#graph "Permanent link")

Capture the flow in as a graph.

## Graph state[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#graph-state "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-13-1)fromtypingimport List
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-13-2)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-13-3)fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-13-4)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-13-5)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-13-6)classGraphState(TypedDict):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-13-7)"""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-13-8)  Represents the state of our graph.
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-13-9)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-13-10)  Attributes:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-13-11)    question: question
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-13-12)    generation: LLM generation
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-13-13)    documents: list of documents
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-13-14)  """
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-13-15)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-13-16)  question: str
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-13-17)  generation: str
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-13-18)  documents: List[str]

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-1)### Nodes
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-2)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-3)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-4)defretrieve(state):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-5)"""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-6)  Retrieve documents
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-7)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-8)  Args:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-9)    state (dict): The current graph state
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-10)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-11)  Returns:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-12)    state (dict): New key added to state, documents, that contains retrieved documents
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-13)  """
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-14)  print("---RETRIEVE---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-15)  question = state["question"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-16)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-17)  # Retrieval
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-18)  documents = retriever.invoke(question)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-19)  return {"documents": documents, "question": question}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-20)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-21)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-22)defgenerate(state):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-23)"""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-24)  Generate answer
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-25)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-26)  Args:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-27)    state (dict): The current graph state
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-28)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-29)  Returns:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-30)    state (dict): New key added to state, generation, that contains LLM generation
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-31)  """
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-32)  print("---GENERATE---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-33)  question = state["question"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-34)  documents = state["documents"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-35)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-36)  # RAG generation
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-37)  generation = rag_chain.invoke({"context": documents, "question": question})
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-38)  return {"documents": documents, "question": question, "generation": generation}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-39)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-40)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-41)defgrade_documents(state):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-42)"""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-43)  Determines whether the retrieved documents are relevant to the question.
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-44)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-45)  Args:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-46)    state (dict): The current graph state
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-47)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-48)  Returns:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-49)    state (dict): Updates documents key with only filtered relevant documents
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-50)  """
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-51)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-52)  print("---CHECK DOCUMENT RELEVANCE TO QUESTION---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-53)  question = state["question"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-54)  documents = state["documents"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-55)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-56)  # Score each doc
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-57)  filtered_docs = []
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-58)  for d in documents:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-59)    score = retrieval_grader.invoke(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-60)      {"question": question, "document": d.page_content}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-61)    )
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-62)    grade = score.binary_score
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-63)    if grade == "yes":
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-64)      print("---GRADE: DOCUMENT RELEVANT---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-65)      filtered_docs.append(d)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-66)    else:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-67)      print("---GRADE: DOCUMENT NOT RELEVANT---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-68)      continue
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-69)  return {"documents": filtered_docs, "question": question}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-70)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-71)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-72)deftransform_query(state):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-73)"""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-74)  Transform the query to produce a better question.
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-75)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-76)  Args:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-77)    state (dict): The current graph state
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-78)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-79)  Returns:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-80)    state (dict): Updates question key with a re-phrased question
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-81)  """
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-82)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-83)  print("---TRANSFORM QUERY---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-84)  question = state["question"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-85)  documents = state["documents"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-86)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-87)  # Re-write question
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-88)  better_question = question_rewriter.invoke({"question": question})
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-89)  return {"documents": documents, "question": better_question}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-90)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-91)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-92)### Edges
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-93)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-94)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-95)defdecide_to_generate(state):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-96)"""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-97)  Determines whether to generate an answer, or re-generate a question.
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-98)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-99)  Args:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-100)    state (dict): The current graph state
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-101)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-102)  Returns:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-103)    str: Binary decision for next node to call
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-104)  """
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-105)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-106)  print("---ASSESS GRADED DOCUMENTS---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-107)  state["question"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-108)  filtered_documents = state["documents"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-109)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-110)  if not filtered_documents:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-111)    # All documents have been filtered check_relevance
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-112)    # We will re-generate a new query
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-113)    print(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-114)      "---DECISION: ALL DOCUMENTS ARE NOT RELEVANT TO QUESTION, TRANSFORM QUERY---"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-115)    )
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-116)    return "transform_query"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-117)  else:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-118)    # We have relevant documents, so generate answer
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-119)    print("---DECISION: GENERATE---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-120)    return "generate"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-121)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-122)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-123)defgrade_generation_v_documents_and_question(state):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-124)"""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-125)  Determines whether the generation is grounded in the document and answers question.
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-126)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-127)  Args:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-128)    state (dict): The current graph state
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-129)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-130)  Returns:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-131)    str: Decision for next node to call
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-132)  """
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-133)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-134)  print("---CHECK HALLUCINATIONS---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-135)  question = state["question"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-136)  documents = state["documents"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-137)  generation = state["generation"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-138)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-139)  score = hallucination_grader.invoke(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-140)    {"documents": documents, "generation": generation}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-141)  )
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-142)  grade = score.binary_score
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-143)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-144)  # Check hallucination
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-145)  if grade == "yes":
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-146)    print("---DECISION: GENERATION IS GROUNDED IN DOCUMENTS---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-147)    # Check question-answering
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-148)    print("---GRADE GENERATION vs QUESTION---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-149)    score = answer_grader.invoke({"question": question, "generation": generation})
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-150)    grade = score.binary_score
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-151)    if grade == "yes":
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-152)      print("---DECISION: GENERATION ADDRESSES QUESTION---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-153)      return "useful"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-154)    else:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-155)      print("---DECISION: GENERATION DOES NOT ADDRESS QUESTION---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-156)      return "not useful"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-157)  else:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-158)    pprint("---DECISION: GENERATION IS NOT GROUNDED IN DOCUMENTS, RE-TRY---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-14-159)    return "not supported"

```


## Build Graph[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#build-graph "Permanent link")

The just follows the flow we outlined in the figure above.

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-15-1)fromlanggraph.graphimport END, StateGraph, START
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-15-2)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-15-3)workflow = StateGraph(GraphState)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-15-4)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-15-5)# Define the nodes
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-15-6)workflow.add_node("retrieve", retrieve) # retrieve
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-15-7)workflow.add_node("grade_documents", grade_documents) # grade documents
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-15-8)workflow.add_node("generate", generate) # generatae
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-15-9)workflow.add_node("transform_query", transform_query) # transform_query
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-15-10)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-15-11)# Build graph
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-15-12)workflow.add_edge(START, "retrieve")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-15-13)workflow.add_edge("retrieve", "grade_documents")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-15-14)workflow.add_conditional_edges(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-15-15)  "grade_documents",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-15-16)  decide_to_generate,
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-15-17)  {
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-15-18)    "transform_query": "transform_query",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-15-19)    "generate": "generate",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-15-20)  },
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-15-21))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-15-22)workflow.add_edge("transform_query", "retrieve")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-15-23)workflow.add_conditional_edges(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-15-24)  "generate",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-15-25)  grade_generation_v_documents_and_question,
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-15-26)  {
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-15-27)    "not supported": "generate",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-15-28)    "useful": END,
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-15-29)    "not useful": "transform_query",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-15-30)  },
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-15-31))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-15-32)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-15-33)# Compile
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-15-34)app = workflow.compile()

```


API Reference: [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START)

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-16-1)frompprintimport pprint
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-16-2)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-16-3)# Run
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-16-4)inputs = {"question": "Explain how the different types of agent memory work?"}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-16-5)for output in app.stream(inputs):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-16-6)  for key, value in output.items():
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-16-7)    # Node
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-16-8)    pprint(f"Node '{key}':")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-16-9)    # Optional: print full state at each node
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-16-10)    # pprint.pprint(value["keys"], indent=2, width=80, depth=None)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-16-11)  pprint("\n---\n")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-16-12)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-16-13)# Final generation
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-16-14)pprint(value["generation"])

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-17-1)---RETRIEVE---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-17-2)"Node 'retrieve':"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-17-3)'\n---\n'
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-17-4)---CHECK DOCUMENT RELEVANCE TO QUESTION---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-17-5)---GRADE: DOCUMENT NOT RELEVANT---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-17-6)---GRADE: DOCUMENT RELEVANT---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-17-7)---GRADE: DOCUMENT NOT RELEVANT---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-17-8)---GRADE: DOCUMENT RELEVANT---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-17-9)---ASSESS GRADED DOCUMENTS---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-17-10)---DECISION: GENERATE---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-17-11)"Node 'grade_documents':"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-17-12)'\n---\n'
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-17-13)---GENERATE---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-17-14)---CHECK HALLUCINATIONS---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-17-15)---DECISION: GENERATION IS GROUNDED IN DOCUMENTS---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-17-16)---GRADE GENERATION vs QUESTION---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-17-17)---DECISION: GENERATION ADDRESSES QUESTION---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-17-18)"Node 'generate':"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-17-19)'\n---\n'
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-17-20)('Short-term memory is used for in-context learning in agents, allowing them '
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-17-21) 'to learn quickly. Long-term memory enables agents to retain and recall vast '
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-17-22) 'amounts of information over extended periods. Agents can also utilize '
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-17-23) 'external tools like APIs to access additional information beyond what is '
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-17-24) 'stored in their memory.')

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-18-1)inputs = {"question": "Explain how chain of thought prompting works?"}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-18-2)for output in app.stream(inputs):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-18-3)  for key, value in output.items():
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-18-4)    # Node
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-18-5)    pprint(f"Node '{key}':")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-18-6)    # Optional: print full state at each node
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-18-7)    # pprint.pprint(value["keys"], indent=2, width=80, depth=None)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-18-8)  pprint("\n---\n")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-18-9)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-18-10)# Final generation
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-18-11)pprint(value["generation"])

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-19-1)---RETRIEVE---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-19-2)"Node 'retrieve':"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-19-3)'\n---\n'
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-19-4)---CHECK DOCUMENT RELEVANCE TO QUESTION---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-19-5)---GRADE: DOCUMENT RELEVANT---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-19-6)---GRADE: DOCUMENT NOT RELEVANT---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-19-7)---GRADE: DOCUMENT RELEVANT---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-19-8)---GRADE: DOCUMENT RELEVANT---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-19-9)---ASSESS GRADED DOCUMENTS---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-19-10)---DECISION: GENERATE---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-19-11)"Node 'grade_documents':"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-19-12)'\n---\n'
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-19-13)---GENERATE---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-19-14)---CHECK HALLUCINATIONS---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-19-15)---DECISION: GENERATION IS GROUNDED IN DOCUMENTS---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-19-16)---GRADE GENERATION vs QUESTION---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-19-17)---DECISION: GENERATION ADDRESSES QUESTION---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-19-18)"Node 'generate':"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-19-19)'\n---\n'
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-19-20)('Chain of thought prompting works by repeatedly prompting the model to ask '
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-19-21) 'follow-up questions to construct the thought process iteratively. This '
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-19-22) 'method can be combined with queries to search for relevant entities and '
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-19-23) 'content to add back into the context. It extends the thought process by '
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-19-24) 'exploring multiple reasoning possibilities at each step, creating a tree '
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__codelineno-19-25) 'structure of thoughts.')

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Corrective RAG (CRAG) using local LLMs  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/) [ Next  Self-RAG using local LLMs  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
