---
url: https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#corrective-rag-crag-using-local-llms)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Corrective RAG (CRAG) using local LLMs 

[ ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/?q= "Share")

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
          * Corrective RAG (CRAG) using local LLMs  [ Corrective RAG (CRAG) using local LLMs  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/) Table of contents 
            * [ Setup  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#setup)
              * [ LLM  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#llm)
            * [ Create Index  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#create-index)
            * [ Define Tools  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#define-tools)
            * [ Create the Graph  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#create-the-graph)
            * [ Evaluation  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#evaluation)
              * [ Response  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#response)
              * [ Trajectory  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#trajectory)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#setup)
    * [ LLM  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#llm)
  * [ Create Index  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#create-index)
  * [ Define Tools  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#define-tools)
  * [ Create the Graph  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#create-the-graph)
  * [ Evaluation  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#evaluation)
    * [ Response  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#response)
    * [ Trajectory  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#trajectory)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ Tutorials  ](https://langchain-ai.github.io/langgraph/tutorials/)
  4. [ RAG  ](https://langchain-ai.github.io/langgraph/tutorials#rag)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/tutorials/rag/langgraph_crag_local.ipynb "Edit this page")

# Corrective RAG (CRAG) using local LLMs[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#corrective-rag-crag-using-local-llms "Permanent link")

[Corrective-RAG (CRAG)](https://arxiv.org/abs/2401.15884) is a strategy for RAG that incorporates self-reflection / self-grading on retrieved documents. 

The paper follows this general flow:

  * If at least one document exceeds the threshold for `relevance`, then it proceeds to generation
  * If all documents fall below the `relevance` threshold or if the grader is unsure, then it uses web search to supplement retrieval
  * Before generation, it performs knowledge refinement of the search or retrieved documents
  * This partitions the document into `knowledge strips`
  * It grades each strip, and filters out irrelevant ones



We will implement some of these ideas from scratch using [LangGraph](https://langchain-ai.github.io/langgraph/):

  * If _any_ documents are irrelevant, we'll supplement retrieval with web search. 
  * We'll skip the knowledge refinement, but this can be added back as a node if desired. 
  * We'll use [Tavily Search](https://python.langchain.com/docs/integrations/tools/tavily_search/) for web search.



![Screenshot 2024-06-24 at 3.03.16 PM.png]()

## Setup[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#setup "Permanent link")

We'll use [Ollama](https://ollama.ai/) to access a local LLM:

  * Download [Ollama app](https://ollama.ai/).
  * Pull your model of choice, e.g.: `ollama pull llama3`



We'll use [Tavily](https://python.langchain.com/docs/integrations/tools/tavily_search/) for web search.

We'll use a vectorstore with [Nomic local embeddings](https://blog.nomic.ai/posts/nomic-embed-text-v1) or, optionally, OpenAI embeddings.

Let's install our required packages and set our API keys:

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-0-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-0-2)%pip install -U langchain_community tiktoken langchainhub scikit-learn langchain langgraph tavily-python nomic[local] langchain-nomic langchain_openai

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-1-1)importgetpass
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-1-2)importos
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-1-5)def_set_env(key: str):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-1-6)  if key not in os.environ:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-1-7)    os.environ[key] = getpass.getpass(f"{key}:")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-1-8)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-1-10)_set_env("OPENAI_API_KEY")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-1-11)_set_env("TAVILY_API_KEY")

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

### LLM[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#llm "Permanent link")

You can select from [Ollama LLMs](https://ollama.com/library).

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-2-1)local_llm = "llama3"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-2-2)model_tested = "llama3-8b"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-2-3)metadata = f"CRAG, {model_tested}"

```


## Create Index[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#create-index "Permanent link")

Let's index 3 blog posts.

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-3-1)fromlangchain.text_splitterimport RecursiveCharacterTextSplitter
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-3-2)fromlangchain_community.document_loadersimport WebBaseLoader
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-3-3)fromlangchain_community.vectorstoresimport SKLearnVectorStore
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-3-4)fromlangchain_nomic.embeddingsimport NomicEmbeddings # local
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-3-5)fromlangchain_openaiimport OpenAIEmbeddings # api
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-3-6)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-3-7)# List of URLs to load documents from
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-3-8)urls = [
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-3-9)  "https://lilianweng.github.io/posts/2023-06-23-agent/",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-3-10)  "https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-3-11)  "https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-3-12)]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-3-13)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-3-14)# Load documents from the URLs
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-3-15)docs = [WebBaseLoader(url).load() for url in urls]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-3-16)docs_list = [item for sublist in docs for item in sublist]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-3-17)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-3-18)# Initialize a text splitter with specified chunk size and overlap
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-3-19)text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-3-20)  chunk_size=250, chunk_overlap=0
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-3-21))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-3-22)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-3-23)# Split the documents into chunks
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-3-24)doc_splits = text_splitter.split_documents(docs_list)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-3-25)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-3-26)# Embedding
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-3-27)"""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-3-28)embedding=NomicEmbeddings(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-3-29)  model="nomic-embed-text-v1.5",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-3-30)  inference_mode="local",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-3-31))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-3-32)"""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-3-33)embedding = OpenAIEmbeddings()
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-3-34)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-3-35)# Add the document chunks to the "vector store"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-3-36)vectorstore = SKLearnVectorStore.from_documents(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-3-37)  documents=doc_splits,
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-3-38)  embedding=embedding,
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-3-39))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-3-40)retriever = vectorstore.as_retriever(k=4)

```


API Reference: [RecursiveCharacterTextSplitter](https://python.langchain.com/api_reference/text_splitters/character/langchain_text_splitters.character.RecursiveCharacterTextSplitter.html) | [WebBaseLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.web_base.WebBaseLoader.html) | [SKLearnVectorStore](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.sklearn.SKLearnVectorStore.html) | [NomicEmbeddings](https://python.langchain.com/api_reference/nomic/embeddings/langchain_nomic.embeddings.NomicEmbeddings.html) | [OpenAIEmbeddings](https://python.langchain.com/api_reference/openai/embeddings/langchain_openai.embeddings.base.OpenAIEmbeddings.html)

## Define Tools[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#define-tools "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-4-1)### Retrieval Grader
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-4-2)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-4-3)fromlangchain.promptsimport PromptTemplate
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-4-4)fromlangchain_community.chat_modelsimport ChatOllama
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-4-5)fromlangchain_core.output_parsersimport JsonOutputParser
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-4-6)fromlangchain_mistralai.chat_modelsimport ChatMistralAI
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-4-7)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-4-8)# LLM
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-4-9)llm = ChatOllama(model=local_llm, format="json", temperature=0)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-4-10)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-4-11)# Prompt
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-4-12)prompt = PromptTemplate(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-4-13)  template="""You are a teacher grading a quiz. You will be given: 
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-4-14)  1/ a QUESTION
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-4-15)  2/ A FACT provided by the student
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-4-16)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-4-17)  You are grading RELEVANCE RECALL:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-4-18)  A score of 1 means that ANY of the statements in the FACT are relevant to the QUESTION. 
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-4-19)  A score of 0 means that NONE of the statements in the FACT are relevant to the QUESTION. 
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-4-20)  1 is the highest (best) score. 0 is the lowest score you can give. 
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-4-21)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-4-22)  Explain your reasoning in a step-by-step manner. Ensure your reasoning and conclusion are correct. 
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-4-23)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-4-24)  Avoid simply stating the correct answer at the outset.
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-4-25)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-4-26)  Question: {question}\n
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-4-27)  Fact: \n\n{documents}\n\n
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-4-28)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-4-29)  Give a binary score 'yes' or 'no' score to indicate whether the document is relevant to the question. \n
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-4-30)  Provide the binary score as a JSON with a single key 'score' and no premable or explanation.
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-4-31)  """,
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-4-32)  input_variables=["question", "documents"],
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-4-33))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-4-34)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-4-35)retrieval_grader = prompt | llm | JsonOutputParser()
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-4-36)question = "agent memory"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-4-37)docs = retriever.invoke(question)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-4-38)doc_txt = docs[1].page_content
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-4-39)print(retrieval_grader.invoke({"question": question, "documents": doc_txt}))

```


API Reference: [PromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.prompt.PromptTemplate.html) | [ChatOllama](https://python.langchain.com/api_reference/community/chat_models/langchain_community.chat_models.ollama.ChatOllama.html) | [JsonOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.json.JsonOutputParser.html) | [ChatMistralAI](https://python.langchain.com/api_reference/mistralai/chat_models/langchain_mistralai.chat_models.ChatMistralAI.html)

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-5-1){'score': 1}

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-6-1)### Generate
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-6-2)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-6-3)fromlangchain_core.output_parsersimport StrOutputParser
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-6-4)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-6-5)# Prompt
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-6-6)prompt = PromptTemplate(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-6-7)  template="""You are an assistant for question-answering tasks. 
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-6-8)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-6-9)  Use the following documents to answer the question. 
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-6-10)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-6-11)  If you don't know the answer, just say that you don't know. 
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-6-12)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-6-13)  Use three sentences maximum and keep the answer concise:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-6-14)  Question: {question}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-6-15)  Documents: {documents}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-6-16)  Answer: 
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-6-17)  """,
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-6-18)  input_variables=["question", "documents"],
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-6-19))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-6-20)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-6-21)# LLM
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-6-22)llm = ChatOllama(model=local_llm, temperature=0)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-6-23)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-6-24)# Chain
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-6-25)rag_chain = prompt | llm | StrOutputParser()
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-6-26)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-6-27)# Run
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-6-28)generation = rag_chain.invoke({"documents": docs, "question": question})
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-6-29)print(generation)

```


API Reference: [StrOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.string.StrOutputParser.html)

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-7-1)The document mentions "memory stream" which is a long-term memory module that records a comprehensive list of agents' experience in natural language. It also discusses short-term memory and long-term memory, with the latter providing the agent with the capability to retain and recall information over extended periods. Additionally, it mentions planning and reflection mechanisms that enable agents to behave conditioned on past experience.

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-8-1)### Search
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-8-2)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-8-3)fromlangchain_community.tools.tavily_searchimport TavilySearchResults
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-8-4)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-8-5)web_search_tool = TavilySearchResults(k=3)

```


API Reference: [TavilySearchResults](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.tavily_search.tool.TavilySearchResults.html)

## Create the Graph[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#create-the-graph "Permanent link")

Here we'll explicitly define the majority of the control flow, only using an LLM to define a single branch point following grading.

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-1)fromtypingimport List
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-2)fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-3)fromIPython.displayimport Image, display
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-4)fromlangchain.schemaimport Document
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-5)fromlanggraph.graphimport START, END, StateGraph
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-6)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-7)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-8)classGraphState(TypedDict):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-9)"""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-10)  Represents the state of our graph.
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-11)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-12)  Attributes:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-13)    question: question
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-14)    generation: LLM generation
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-15)    search: whether to add search
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-16)    documents: list of documents
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-17)  """
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-18)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-19)  question: str
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-20)  generation: str
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-21)  search: str
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-22)  documents: List[str]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-23)  steps: List[str]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-24)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-25)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-26)defretrieve(state):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-27)"""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-28)  Retrieve documents
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-29)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-30)  Args:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-31)    state (dict): The current graph state
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-32)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-33)  Returns:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-34)    state (dict): New key added to state, documents, that contains retrieved documents
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-35)  """
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-36)  question = state["question"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-37)  documents = retriever.invoke(question)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-38)  steps = state["steps"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-39)  steps.append("retrieve_documents")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-40)  return {"documents": documents, "question": question, "steps": steps}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-41)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-42)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-43)defgenerate(state):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-44)"""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-45)  Generate answer
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-46)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-47)  Args:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-48)    state (dict): The current graph state
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-49)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-50)  Returns:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-51)    state (dict): New key added to state, generation, that contains LLM generation
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-52)  """
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-53)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-54)  question = state["question"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-55)  documents = state["documents"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-56)  generation = rag_chain.invoke({"documents": documents, "question": question})
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-57)  steps = state["steps"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-58)  steps.append("generate_answer")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-59)  return {
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-60)    "documents": documents,
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-61)    "question": question,
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-62)    "generation": generation,
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-63)    "steps": steps,
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-64)  }
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-65)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-66)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-67)defgrade_documents(state):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-68)"""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-69)  Determines whether the retrieved documents are relevant to the question.
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-70)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-71)  Args:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-72)    state (dict): The current graph state
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-73)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-74)  Returns:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-75)    state (dict): Updates documents key with only filtered relevant documents
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-76)  """
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-77)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-78)  question = state["question"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-79)  documents = state["documents"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-80)  steps = state["steps"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-81)  steps.append("grade_document_retrieval")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-82)  filtered_docs = []
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-83)  search = "No"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-84)  for d in documents:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-85)    score = retrieval_grader.invoke(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-86)      {"question": question, "documents": d.page_content}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-87)    )
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-88)    grade = score["score"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-89)    if grade == "yes":
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-90)      filtered_docs.append(d)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-91)    else:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-92)      search = "Yes"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-93)      continue
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-94)  return {
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-95)    "documents": filtered_docs,
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-96)    "question": question,
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-97)    "search": search,
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-98)    "steps": steps,
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-99)  }
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-100)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-101)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-102)defweb_search(state):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-103)"""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-104)  Web search based on the re-phrased question.
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-105)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-106)  Args:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-107)    state (dict): The current graph state
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-108)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-109)  Returns:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-110)    state (dict): Updates documents key with appended web results
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-111)  """
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-112)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-113)  question = state["question"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-114)  documents = state.get("documents", [])
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-115)  steps = state["steps"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-116)  steps.append("web_search")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-117)  web_results = web_search_tool.invoke({"query": question})
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-118)  documents.extend(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-119)    [
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-120)      Document(page_content=d["content"], metadata={"url": d["url"]})
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-121)      for d in web_results
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-122)    ]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-123)  )
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-124)  return {"documents": documents, "question": question, "steps": steps}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-125)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-126)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-127)defdecide_to_generate(state):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-128)"""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-129)  Determines whether to generate an answer, or re-generate a question.
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-130)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-131)  Args:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-132)    state (dict): The current graph state
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-133)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-134)  Returns:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-135)    str: Binary decision for next node to call
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-136)  """
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-137)  search = state["search"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-138)  if search == "Yes":
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-139)    return "search"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-140)  else:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-141)    return "generate"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-142)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-143)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-144)# Graph
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-145)workflow = StateGraph(GraphState)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-146)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-147)# Define the nodes
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-148)workflow.add_node("retrieve", retrieve) # retrieve
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-149)workflow.add_node("grade_documents", grade_documents) # grade documents
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-150)workflow.add_node("generate", generate) # generatae
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-151)workflow.add_node("web_search", web_search) # web search
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-152)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-153)# Build graph
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-154)workflow.add_edge(START, "retrieve")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-155)workflow.add_edge("retrieve", "grade_documents")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-156)workflow.add_conditional_edges(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-157)  "grade_documents",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-158)  decide_to_generate,
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-159)  {
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-160)    "search": "web_search",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-161)    "generate": "generate",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-162)  },
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-163))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-164)workflow.add_edge("web_search", "generate")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-165)workflow.add_edge("generate", END)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-166)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-167)custom_graph = workflow.compile()
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-168)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-9-169)display(Image(custom_graph.get_graph(xray=True).draw_mermaid_png()))

```


API Reference: [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph)

![]()

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-10-1)importuuid
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-10-2)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-10-3)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-10-4)defpredict_custom_agent_local_answer(example: dict):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-10-5)  config = {"configurable": {"thread_id": str(uuid.uuid4())}}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-10-6)  state_dict = custom_graph.invoke(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-10-7)    {"question": example["input"], "steps": []}, config
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-10-8)  )
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-10-9)  return {"response": state_dict["generation"], "steps": state_dict["steps"]}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-10-10)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-10-11)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-10-12)example = {"input": "What are the types of agent memory?"}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-10-13)response = predict_custom_agent_local_answer(example)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-10-14)response

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-11-1){'response': 'According to the documents, there are two types of agent memory:\n\n* Short-term memory (STM): This is a data structure that holds information temporarily and allows the agent to process it when needed.\n* Long-term memory (LTM): This provides the agent with the capability to retain and recall information over extended periods.\n\nThese types of memories allow the agent to learn, reason, and make decisions.',
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-11-2) 'steps': ['retrieve_documents',
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-11-3) 'grade_document_retrieval',
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-11-4) 'web_search',
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-11-5) 'generate_answer']}

```


Trace: 

<https://smith.langchain.com/public/88e7579e-2571-4cf6-98d2-1f9ce3359967/r>

## Evaluation[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#evaluation "Permanent link")

Now we've defined two different agent architectures that do roughly the same thing!

We can evaluate them. See our [conceptual guide](https://docs.smith.langchain.com/concepts/evaluation#agents) for context on agent evaluation.

### Response[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#response "Permanent link")

First, we can assess how well [our agent performs on a set of question-answer pairs](https://docs.smith.langchain.com/tutorials/Developers/agents#response-evaluation).

We'll create a dataset and save it in LangSmith.

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-12-1)fromlangsmithimport Client
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-12-2)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-12-3)client = Client()
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-12-4)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-12-5)# Create a dataset
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-12-6)examples = [
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-12-7)  (
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-12-8)    "How does the ReAct agent use self-reflection? ",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-12-9)    "ReAct integrates reasoning and acting, performing actions - such tools like Wikipedia search API - and then observing / reasoning about the tool outputs.",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-12-10)  ),
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-12-11)  (
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-12-12)    "What are the types of biases that can arise with few-shot prompting?",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-12-13)    "The biases that can arise with few-shot prompting include (1) Majority label bias, (2) Recency bias, and (3) Common token bias.",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-12-14)  ),
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-12-15)  (
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-12-16)    "What are five types of adversarial attacks?",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-12-17)    "Five types of adversarial attacks are (1) Token manipulation, (2) Gradient based attack, (3) Jailbreak prompting, (4) Human red-teaming, (5) Model red-teaming.",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-12-18)  ),
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-12-19)  (
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-12-20)    "Who did the Chicago Bears draft first in the 2024 NFL draft”?",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-12-21)    "The Chicago Bears drafted Caleb Williams first in the 2024 NFL draft.",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-12-22)  ),
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-12-23)  ("Who won the 2024 NBA finals?", "The Boston Celtics on the 2024 NBA finals"),
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-12-24)]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-12-25)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-12-26)# Save it
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-12-27)dataset_name = "Corrective RAG Agent Testing"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-12-28)if not client.has_dataset(dataset_name=dataset_name):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-12-29)  dataset = client.create_dataset(dataset_name=dataset_name)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-12-30)  inputs, outputs = zip(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-12-31)    *[({"input": text}, {"output": label}) for text, label in examples]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-12-32)  )
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-12-33)  client.create_examples(inputs=inputs, outputs=outputs, dataset_id=dataset.id)

```


Now, we'll use an `LLM as a grader` to compare both agent responses to our ground truth reference answer.

[Here](https://smith.langchain.com/hub/rlm/rag-answer-vs-reference) is the default prompt that we can use.

We'll use `gpt-4o` as our LLM grader.

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-13-1)fromlangchainimport hub
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-13-2)fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-13-3)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-13-4)# Grade prompt
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-13-5)grade_prompt_answer_accuracy = hub.pull("langchain-ai/rag-answer-vs-reference")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-13-6)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-13-7)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-13-8)defanswer_evaluator(run, example) -> dict:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-13-9)"""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-13-10)  A simple evaluator for RAG answer accuracy
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-13-11)  """
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-13-12)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-13-13)  # Get the question, the ground truth reference answer, RAG chain answer prediction
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-13-14)  input_question = example.inputs["input"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-13-15)  reference = example.outputs["output"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-13-16)  prediction = run.outputs["response"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-13-17)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-13-18)  # Define an LLM grader
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-13-19)  llm = ChatOpenAI(model="gpt-4o", temperature=0)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-13-20)  answer_grader = grade_prompt_answer_accuracy | llm
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-13-21)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-13-22)  # Run evaluator
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-13-23)  score = answer_grader.invoke(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-13-24)    {
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-13-25)      "question": input_question,
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-13-26)      "correct_answer": reference,
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-13-27)      "student_answer": prediction,
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-13-28)    }
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-13-29)  )
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-13-30)  score = score["Score"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-13-31)  return {"key": "answer_v_reference_score", "score": score}

```


API Reference: [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html)

### Trajectory[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#trajectory "Permanent link")

Second, [we can assess the list of tool calls](https://docs.smith.langchain.com/tutorials/Developers/agents#trajectory) that each agent makes relative to expected trajectories.

This evaluates the specific reasoning traces taken by our agents!

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-14-1)fromlangsmith.schemasimport Example, Run
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-14-2)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-14-3)# Reasoning traces that we expect the agents to take
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-14-4)expected_trajectory_1 = [
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-14-5)  "retrieve_documents",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-14-6)  "grade_document_retrieval",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-14-7)  "web_search",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-14-8)  "generate_answer",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-14-9)]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-14-10)expected_trajectory_2 = [
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-14-11)  "retrieve_documents",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-14-12)  "grade_document_retrieval",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-14-13)  "generate_answer",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-14-14)]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-14-15)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-14-16)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-14-17)deffind_tool_calls_react(messages):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-14-18)"""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-14-19)  Find all tool calls in the messages returned
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-14-20)  """
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-14-21)  tool_calls = [
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-14-22)    tc["name"] for m in messages["messages"] for tc in getattr(m, "tool_calls", [])
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-14-23)  ]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-14-24)  return tool_calls
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-14-25)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-14-26)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-14-27)defcheck_trajectory_react(root_run: Run, example: Example) -> dict:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-14-28)"""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-14-29)  Check if all expected tools are called in exact order and without any additional tool calls.
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-14-30)  """
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-14-31)  messages = root_run.outputs["messages"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-14-32)  tool_calls = find_tool_calls_react(messages)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-14-33)  print(f"Tool calls ReAct agent: {tool_calls}")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-14-34)  if tool_calls == expected_trajectory_1 or tool_calls == expected_trajectory_2:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-14-35)    score = 1
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-14-36)  else:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-14-37)    score = 0
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-14-38)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-14-39)  return {"score": int(score), "key": "tool_calls_in_exact_order"}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-14-40)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-14-41)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-14-42)defcheck_trajectory_custom(root_run: Run, example: Example) -> dict:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-14-43)"""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-14-44)  Check if all expected tools are called in exact order and without any additional tool calls.
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-14-45)  """
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-14-46)  tool_calls = root_run.outputs["steps"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-14-47)  print(f"Tool calls custom agent: {tool_calls}")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-14-48)  if tool_calls == expected_trajectory_1 or tool_calls == expected_trajectory_2:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-14-49)    score = 1
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-14-50)  else:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-14-51)    score = 0
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-14-52)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-14-53)  return {"score": int(score), "key": "tool_calls_in_exact_order"}

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-15-1)fromlangsmith.evaluationimport evaluate
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-15-2)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-15-3)experiment_prefix = f"custom-agent-{model_tested}"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-15-4)experiment_results = evaluate(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-15-5)  predict_custom_agent_local_answer,
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-15-6)  data=dataset_name,
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-15-7)  evaluators=[answer_evaluator, check_trajectory_custom],
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-15-8)  experiment_prefix=experiment_prefix + "-answer-and-tool-use",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-15-9)  num_repetitions=3,
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-15-10)  max_concurrency=1, # Use when running locally
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-15-11)  metadata={"version": metadata},
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-15-12))

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-16-1)View the evaluation results for experiment: 'custom-agent-llama3-8b-answer-and-tool-use-d6006159' at:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-16-2)https://smith.langchain.com/o/1fa8b1f4-fcb9-4072-9aa9-983e35ad61b8/datasets/a8b9273b-ca33-4e2f-9f69-9bbc37f6f51b/compare?selectedSessions=83c60822-ef22-43e8-ac85-4488af279c6f

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-17-1)0it [00:00, ?it/s]

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-18-1)Tool calls custom agent: ['retrieve_documents', 'grade_document_retrieval', 'web_search', 'generate_answer']
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-18-2)Tool calls custom agent: ['retrieve_documents', 'grade_document_retrieval', 'web_search', 'generate_answer']
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-18-3)Tool calls custom agent: ['retrieve_documents', 'grade_document_retrieval', 'web_search', 'generate_answer']
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-18-4)Tool calls custom agent: ['retrieve_documents', 'grade_document_retrieval', 'web_search', 'generate_answer']
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-18-5)Tool calls custom agent: ['retrieve_documents', 'grade_document_retrieval', 'web_search', 'generate_answer']
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-18-6)Tool calls custom agent: ['retrieve_documents', 'grade_document_retrieval', 'web_search', 'generate_answer']
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-18-7)Tool calls custom agent: ['retrieve_documents', 'grade_document_retrieval', 'web_search', 'generate_answer']
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-18-8)Tool calls custom agent: ['retrieve_documents', 'grade_document_retrieval', 'web_search', 'generate_answer']
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-18-9)Tool calls custom agent: ['retrieve_documents', 'grade_document_retrieval', 'web_search', 'generate_answer']
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-18-10)Tool calls custom agent: ['retrieve_documents', 'grade_document_retrieval', 'web_search', 'generate_answer']
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-18-11)Tool calls custom agent: ['retrieve_documents', 'grade_document_retrieval', 'web_search', 'generate_answer']
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-18-12)Tool calls custom agent: ['retrieve_documents', 'grade_document_retrieval', 'web_search', 'generate_answer']
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-18-13)Tool calls custom agent: ['retrieve_documents', 'grade_document_retrieval', 'web_search', 'generate_answer']
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-18-14)Tool calls custom agent: ['retrieve_documents', 'grade_document_retrieval', 'web_search', 'generate_answer']
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__codelineno-18-15)Tool calls custom agent: ['retrieve_documents', 'grade_document_retrieval', 'web_search', 'generate_answer']

```


We can see the results benchmarked against `GPT-4o` and `Llama-3-70b` using `Custom` agent (as shown here) and ReAct. 

![Screenshot 2024-06-24 at 4.14.04 PM.png]()

The `local custom agent` performs well in terms of tool calling reliability: it follows the expected reasoning traces.

However, the answer accuracy performance lags the larger models with `custom agent` implementations.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Corrective RAG (CRAG)  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/) [ Next  Self-RAG  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag_local/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
