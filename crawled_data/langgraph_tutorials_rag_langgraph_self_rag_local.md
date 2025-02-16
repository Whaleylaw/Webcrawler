---
url: https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#self-rag-using-local-llms)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Self-RAG using local LLMs 

[ ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/?q= "Share")

Initializing search 

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
          * [ Self-RAG  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/)
          * Self-RAG using local LLMs  [ Self-RAG using local LLMs  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/) Table of contents 
            * [ Setup  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#setup)
              * [ LLMs  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#llms)
                * [ Local Embeddings  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#local-embeddings)
                * [ Local LLM  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#local-llm)
            * [ Create Index  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#create-index)
            * [ LLMs  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#llms_1)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#setup)
    * [ LLMs  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#llms)
      * [ Local Embeddings  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#local-embeddings)
      * [ Local LLM  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#local-llm)
  * [ Create Index  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#create-index)
  * [ LLMs  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#llms_1)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ Tutorials  ](https://langchain-ai.github.io/langgraph/tutorials/)
  4. [ RAG  ](https://langchain-ai.github.io/langgraph/tutorials#rag)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/tutorials/rag/langgraph_self_rag_local.ipynb "Edit this page")

# Self-RAG using local LLMs[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#self-rag-using-local-llms "Permanent link")

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

![Screenshot 2024-04-01 at 12.42.59 PM.png]()

## Setup[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#setup "Permanent link")

First let's install our required packages and set our API keys

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-0-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-0-2)%pip install -U langchain-nomic langchain_community tiktoken langchainhub chromadb langchain langgraph nomic[local]

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-1-1)importgetpass
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-1-2)importos
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-1-5)def_set_env(key: str):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-1-6)  if key not in os.environ:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-1-7)    os.environ[key] = getpass.getpass(f"{key}:")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-1-8)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-1-10)_set_env("NOMIC_API_KEY")

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

### LLMs[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#llms "Permanent link")

#### Local Embeddings[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#local-embeddings "Permanent link")

You can use `GPT4AllEmbeddings()` from Nomic, which can access use Nomic's recently released [v1](https://blog.nomic.ai/posts/nomic-embed-text-v1) and [v1.5](https://blog.nomic.ai/posts/nomic-embed-matryoshka) embeddings.

Follow the documentation [here](https://docs.gpt4all.io/gpt4all_python_embedding.html#supported-embedding-models).

#### Local LLM[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#local-llm "Permanent link")

(1) Download [Ollama app](https://ollama.ai/).

(2) Download a `Mistral` model from various Mistral versions [here](https://ollama.ai/library/mistral) and Mixtral versions [here](https://ollama.ai/library/mixtral) available. 

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-2-1)ollama pull mistral

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-3-1)# Ollama model name
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-3-2)local_llm = "mistral"

```


## Create Index[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#create-index "Permanent link")

Let's index 3 blog posts.

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-4-1)fromlangchain.text_splitterimport RecursiveCharacterTextSplitter
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-4-2)fromlangchain_community.document_loadersimport WebBaseLoader
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-4-3)fromlangchain_community.vectorstoresimport Chroma
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-4-4)fromlangchain_nomic.embeddingsimport NomicEmbeddings
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-4-5)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-4-6)urls = [
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-4-7)  "https://lilianweng.github.io/posts/2023-06-23-agent/",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-4-8)  "https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-4-9)  "https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-4-10)]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-4-11)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-4-12)docs = [WebBaseLoader(url).load() for url in urls]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-4-13)docs_list = [item for sublist in docs for item in sublist]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-4-14)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-4-15)text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-4-16)  chunk_size=250, chunk_overlap=0
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-4-17))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-4-18)doc_splits = text_splitter.split_documents(docs_list)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-4-19)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-4-20)# Add to vectorDB
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-4-21)vectorstore = Chroma.from_documents(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-4-22)  documents=doc_splits,
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-4-23)  collection_name="rag-chroma",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-4-24)  embedding=NomicEmbeddings(model="nomic-embed-text-v1.5", inference_mode="local"),
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-4-25))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-4-26)retriever = vectorstore.as_retriever()

```


API Reference: [RecursiveCharacterTextSplitter](https://python.langchain.com/api_reference/text_splitters/character/langchain_text_splitters.character.RecursiveCharacterTextSplitter.html) | [WebBaseLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.web_base.WebBaseLoader.html) | [Chroma](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.chroma.Chroma.html) | [NomicEmbeddings](https://python.langchain.com/api_reference/nomic/embeddings/langchain_nomic.embeddings.NomicEmbeddings.html)

## LLMs[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#llms_1 "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-5-1)### Retrieval Grader
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-5-2)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-5-3)fromlangchain.promptsimport PromptTemplate
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-5-4)fromlangchain_community.chat_modelsimport ChatOllama
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-5-5)fromlangchain_core.output_parsersimport JsonOutputParser
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-5-6)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-5-7)# LLM
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-5-8)llm = ChatOllama(model=local_llm, format="json", temperature=0)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-5-9)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-5-10)prompt = PromptTemplate(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-5-11)  template="""You are a grader assessing relevance of a retrieved document to a user question. \n
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-5-12)  Here is the retrieved document: \n\n{document}\n\n
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-5-13)  Here is the user question: {question}\n
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-5-14)  If the document contains keywords related to the user question, grade it as relevant. \n
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-5-15)  It does not need to be a stringent test. The goal is to filter out erroneous retrievals. \n
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-5-16)  Give a binary score 'yes' or 'no' score to indicate whether the document is relevant to the question. \n
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-5-17)  Provide the binary score as a JSON with a single key 'score' and no premable or explanation.""",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-5-18)  input_variables=["question", "document"],
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-5-19))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-5-20)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-5-21)retrieval_grader = prompt | llm | JsonOutputParser()
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-5-22)question = "agent memory"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-5-23)docs = retriever.invoke(question)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-5-24)doc_txt = docs[1].page_content
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-5-25)print(retrieval_grader.invoke({"question": question, "document": doc_txt}))

```


API Reference: [PromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.prompt.PromptTemplate.html) | [ChatOllama](https://python.langchain.com/api_reference/community/chat_models/langchain_community.chat_models.ollama.ChatOllama.html) | [JsonOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.json.JsonOutputParser.html)

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-6-1){'score': 'yes'}

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-7-1)### Generate
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-7-2)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-7-3)fromlangchainimport hub
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-7-4)fromlangchain_core.output_parsersimport StrOutputParser
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-7-5)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-7-6)# Prompt
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-7-7)prompt = hub.pull("rlm/rag-prompt")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-7-8)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-7-9)# LLM
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-7-10)llm = ChatOllama(model=local_llm, temperature=0)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-7-11)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-7-12)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-7-13)# Post-processing
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-7-14)defformat_docs(docs):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-7-15)  return "\n\n".join(doc.page_content for doc in docs)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-7-16)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-7-17)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-7-18)# Chain
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-7-19)rag_chain = prompt | llm | StrOutputParser()
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-7-20)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-7-21)# Run
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-7-22)generation = rag_chain.invoke({"context": docs, "question": question})
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-7-23)print(generation)

```


API Reference: [StrOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.string.StrOutputParser.html)

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-8-1) In an LLM-powered autonomous agent system, the Large Language Model (LLM) functions as the agent's brain. The agent has key components including memory, planning, and reflection mechanisms. The memory component is a long-term memory module that records a comprehensive list of agents’ experience in natural language. It includes a memory stream, which is an external database for storing past experiences. The reflection mechanism synthesizes memories into higher-level inferences over time and guides the agent's future behavior.

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-9-1)### Hallucination Grader
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-9-2)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-9-3)# LLM
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-9-4)llm = ChatOllama(model=local_llm, format="json", temperature=0)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-9-5)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-9-6)# Prompt
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-9-7)prompt = PromptTemplate(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-9-8)  template="""You are a grader assessing whether an answer is grounded in / supported by a set of facts. \n
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-9-9)  Here are the facts:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-9-10)\n ------- \n
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-9-11){documents}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-9-12)\n ------- \n
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-9-13)  Here is the answer: {generation}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-9-14)  Give a binary score 'yes' or 'no' score to indicate whether the answer is grounded in / supported by a set of facts. \n
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-9-15)  Provide the binary score as a JSON with a single key 'score' and no preamble or explanation.""",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-9-16)  input_variables=["generation", "documents"],
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-9-17))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-9-18)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-9-19)hallucination_grader = prompt | llm | JsonOutputParser()
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-9-20)hallucination_grader.invoke({"documents": docs, "generation": generation})

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-10-1){'score': 'yes'}

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-11-1)### Answer Grader
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-11-2)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-11-3)# LLM
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-11-4)llm = ChatOllama(model=local_llm, format="json", temperature=0)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-11-5)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-11-6)# Prompt
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-11-7)prompt = PromptTemplate(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-11-8)  template="""You are a grader assessing whether an answer is useful to resolve a question. \n
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-11-9)  Here is the answer:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-11-10)\n ------- \n
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-11-11){generation}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-11-12)\n ------- \n
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-11-13)  Here is the question: {question}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-11-14)  Give a binary score 'yes' or 'no' to indicate whether the answer is useful to resolve a question. \n
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-11-15)  Provide the binary score as a JSON with a single key 'score' and no preamble or explanation.""",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-11-16)  input_variables=["generation", "question"],
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-11-17))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-11-18)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-11-19)answer_grader = prompt | llm | JsonOutputParser()
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-11-20)answer_grader.invoke({"question": question, "generation": generation})

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-12-1){'score': 'yes'}

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-13-1)### Question Re-writer
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-13-2)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-13-3)# LLM
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-13-4)llm = ChatOllama(model=local_llm, temperature=0)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-13-5)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-13-6)# Prompt
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-13-7)re_write_prompt = PromptTemplate(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-13-8)  template="""You a question re-writer that converts an input question to a better version that is optimized \n
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-13-9)   for vectorstore retrieval. Look at the initial and formulate an improved question. \n
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-13-10)   Here is the initial question: \n\n{question}. Improved question with no preamble: \n """,
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-13-11)  input_variables=["generation", "question"],
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-13-12))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-13-13)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-13-14)question_rewriter = re_write_prompt | llm | StrOutputParser()
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-13-15)question_rewriter.invoke({"question": question})

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-14-1)' What is agent memory and how can it be effectively utilized in vector database retrieval?'

```


# Graph[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#graph "Permanent link")

Capture the flow in as a graph.

## Graph state[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#graph-state "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-15-1)fromtypingimport List
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-15-2)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-15-3)fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-15-4)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-15-5)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-15-6)classGraphState(TypedDict):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-15-7)"""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-15-8)  Represents the state of our graph.
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-15-9)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-15-10)  Attributes:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-15-11)    question: question
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-15-12)    generation: LLM generation
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-15-13)    documents: list of documents
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-15-14)  """
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-15-15)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-15-16)  question: str
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-15-17)  generation: str
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-15-18)  documents: List[str]

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-1)### Nodes
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-2)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-3)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-4)defretrieve(state):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-5)"""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-6)  Retrieve documents
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-7)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-8)  Args:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-9)    state (dict): The current graph state
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-10)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-11)  Returns:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-12)    state (dict): New key added to state, documents, that contains retrieved documents
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-13)  """
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-14)  print("---RETRIEVE---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-15)  question = state["question"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-16)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-17)  # Retrieval
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-18)  documents = retriever.invoke(question)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-19)  return {"documents": documents, "question": question}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-20)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-21)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-22)defgenerate(state):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-23)"""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-24)  Generate answer
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-25)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-26)  Args:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-27)    state (dict): The current graph state
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-28)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-29)  Returns:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-30)    state (dict): New key added to state, generation, that contains LLM generation
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-31)  """
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-32)  print("---GENERATE---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-33)  question = state["question"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-34)  documents = state["documents"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-35)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-36)  # RAG generation
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-37)  generation = rag_chain.invoke({"context": documents, "question": question})
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-38)  return {"documents": documents, "question": question, "generation": generation}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-39)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-40)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-41)defgrade_documents(state):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-42)"""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-43)  Determines whether the retrieved documents are relevant to the question.
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-44)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-45)  Args:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-46)    state (dict): The current graph state
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-47)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-48)  Returns:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-49)    state (dict): Updates documents key with only filtered relevant documents
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-50)  """
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-51)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-52)  print("---CHECK DOCUMENT RELEVANCE TO QUESTION---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-53)  question = state["question"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-54)  documents = state["documents"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-55)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-56)  # Score each doc
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-57)  filtered_docs = []
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-58)  for d in documents:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-59)    score = retrieval_grader.invoke(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-60)      {"question": question, "document": d.page_content}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-61)    )
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-62)    grade = score["score"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-63)    if grade == "yes":
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-64)      print("---GRADE: DOCUMENT RELEVANT---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-65)      filtered_docs.append(d)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-66)    else:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-67)      print("---GRADE: DOCUMENT NOT RELEVANT---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-68)      continue
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-69)  return {"documents": filtered_docs, "question": question}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-70)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-71)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-72)deftransform_query(state):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-73)"""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-74)  Transform the query to produce a better question.
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-75)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-76)  Args:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-77)    state (dict): The current graph state
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-78)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-79)  Returns:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-80)    state (dict): Updates question key with a re-phrased question
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-81)  """
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-82)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-83)  print("---TRANSFORM QUERY---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-84)  question = state["question"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-85)  documents = state["documents"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-86)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-87)  # Re-write question
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-88)  better_question = question_rewriter.invoke({"question": question})
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-89)  return {"documents": documents, "question": better_question}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-90)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-91)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-92)### Edges
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-93)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-94)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-95)defdecide_to_generate(state):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-96)"""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-97)  Determines whether to generate an answer, or re-generate a question.
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-98)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-99)  Args:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-100)    state (dict): The current graph state
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-101)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-102)  Returns:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-103)    str: Binary decision for next node to call
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-104)  """
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-105)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-106)  print("---ASSESS GRADED DOCUMENTS---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-107)  state["question"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-108)  filtered_documents = state["documents"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-109)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-110)  if not filtered_documents:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-111)    # All documents have been filtered check_relevance
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-112)    # We will re-generate a new query
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-113)    print(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-114)      "---DECISION: ALL DOCUMENTS ARE NOT RELEVANT TO QUESTION, TRANSFORM QUERY---"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-115)    )
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-116)    return "transform_query"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-117)  else:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-118)    # We have relevant documents, so generate answer
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-119)    print("---DECISION: GENERATE---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-120)    return "generate"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-121)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-122)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-123)defgrade_generation_v_documents_and_question(state):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-124)"""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-125)  Determines whether the generation is grounded in the document and answers question.
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-126)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-127)  Args:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-128)    state (dict): The current graph state
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-129)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-130)  Returns:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-131)    str: Decision for next node to call
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-132)  """
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-133)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-134)  print("---CHECK HALLUCINATIONS---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-135)  question = state["question"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-136)  documents = state["documents"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-137)  generation = state["generation"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-138)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-139)  score = hallucination_grader.invoke(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-140)    {"documents": documents, "generation": generation}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-141)  )
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-142)  grade = score["score"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-143)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-144)  # Check hallucination
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-145)  if grade == "yes":
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-146)    print("---DECISION: GENERATION IS GROUNDED IN DOCUMENTS---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-147)    # Check question-answering
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-148)    print("---GRADE GENERATION vs QUESTION---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-149)    score = answer_grader.invoke({"question": question, "generation": generation})
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-150)    grade = score["score"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-151)    if grade == "yes":
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-152)      print("---DECISION: GENERATION ADDRESSES QUESTION---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-153)      return "useful"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-154)    else:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-155)      print("---DECISION: GENERATION DOES NOT ADDRESS QUESTION---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-156)      return "not useful"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-157)  else:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-158)    print("---DECISION: GENERATION IS NOT GROUNDED IN DOCUMENTS, RE-TRY---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-16-159)    return "not supported"

```


## Build Graph[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#build-graph "Permanent link")

This just follows the flow we outlined in the figure above.

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-17-1)fromlanggraph.graphimport END, StateGraph, START
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-17-2)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-17-3)workflow = StateGraph(GraphState)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-17-4)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-17-5)# Define the nodes
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-17-6)workflow.add_node("retrieve", retrieve) # retrieve
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-17-7)workflow.add_node("grade_documents", grade_documents) # grade documents
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-17-8)workflow.add_node("generate", generate) # generatae
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-17-9)workflow.add_node("transform_query", transform_query) # transform_query
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-17-10)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-17-11)# Build graph
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-17-12)workflow.add_edge(START, "retrieve")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-17-13)workflow.add_edge("retrieve", "grade_documents")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-17-14)workflow.add_conditional_edges(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-17-15)  "grade_documents",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-17-16)  decide_to_generate,
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-17-17)  {
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-17-18)    "transform_query": "transform_query",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-17-19)    "generate": "generate",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-17-20)  },
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-17-21))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-17-22)workflow.add_edge("transform_query", "retrieve")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-17-23)workflow.add_conditional_edges(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-17-24)  "generate",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-17-25)  grade_generation_v_documents_and_question,
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-17-26)  {
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-17-27)    "not supported": "generate",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-17-28)    "useful": END,
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-17-29)    "not useful": "transform_query",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-17-30)  },
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-17-31))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-17-32)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-17-33)# Compile
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-17-34)app = workflow.compile()

```


API Reference: [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START)

## Run[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#run "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-18-1)frompprintimport pprint
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-18-2)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-18-3)# Run
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-18-4)inputs = {"question": "Explain how the different types of agent memory work?"}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-18-5)for output in app.stream(inputs):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-18-6)  for key, value in output.items():
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-18-7)    # Node
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-18-8)    pprint(f"Node '{key}':")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-18-9)    # Optional: print full state at each node
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-18-10)    # pprint.pprint(value["keys"], indent=2, width=80, depth=None)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-18-11)  pprint("\n---\n")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-18-12)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-18-13)# Final generation
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-18-14)pprint(value["generation"])

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-19-1)---RETRIEVE---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-19-2)"Node 'retrieve':"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-19-3)'\n---\n'
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-19-4)---CHECK DOCUMENT RELEVANCE TO QUESTION---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-19-5)---GRADE: DOCUMENT RELEVANT---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-19-6)---GRADE: DOCUMENT RELEVANT---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-19-7)---GRADE: DOCUMENT RELEVANT---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-19-8)---GRADE: DOCUMENT RELEVANT---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-19-9)"Node 'grade_documents':"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-19-10)'\n---\n'
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-19-11)---ASSESS GRADED DOCUMENTS---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-19-12)---DECISION: GENERATE---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-19-13)---GENERATE---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-19-14)"Node 'generate':"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-19-15)'\n---\n'
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-19-16)---CHECK HALLUCINATIONS---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-19-17)---DECISION: GENERATION IS GROUNDED IN DOCUMENTS---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-19-18)---GRADE GENERATION vs QUESTION---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-19-19)---DECISION: GENERATION ADDRESSES QUESTION---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-19-20)"Node '__end__':"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-19-21)'\n---\n'
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-19-22)(' In a LLM-powered autonomous agent system, memory is a key component that '
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-19-23) 'enables agents to store and retrieve information. There are different types '
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-19-24) 'of memory in human brains, such as sensory memory which retains impressions '
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-19-25) 'of sensory information for a few seconds, and long-term memory which records '
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-19-26) "experiences for extended periods (Lil'Log, 2023). In the context of LLM "
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-19-27) 'agents, memory is often implemented as an external database or memory stream '
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-19-28) "(Lil'Log, 2023). The agent can consult this memory to inform its behavior "
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-19-29) 'based on relevance, recency, and importance. Additionally, reflection '
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-19-30) 'mechanisms synthesize memories into higher-level inferences over time and '
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__codelineno-19-31) "guide the agent's future behavior (Lil'Log, 2023).")

```


Trace: 

<https://smith.langchain.com/public/4163a342-5260-4852-8602-bda3f95177e7/r>

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Self-RAG  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/) [ Next  An agent for interacting with a SQL database  ](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
