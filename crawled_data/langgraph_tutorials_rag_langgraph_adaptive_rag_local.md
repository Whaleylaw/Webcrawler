---
url: https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#local-rag-agent-with-llama3)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Langgraph adaptive rag local 

[ ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/?q= "Share")

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
          * Langgraph adaptive rag local  [ Langgraph adaptive rag local  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/) Table of contents 
            * [ Local models  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#local-models)
              * [ Embedding  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#embedding)
              * [ LLM  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#llm)
              * [ Search  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#search)
              * [ Tracing  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#tracing)
              * [ Vectorstore  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#vectorstore)
              * [ Components  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#components)
            * [ Web Search Tool  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#web-search-tool)
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

  * [ Local models  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#local-models)
    * [ Embedding  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#embedding)
    * [ LLM  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#llm)
    * [ Search  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#search)
    * [ Tracing  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#tracing)
    * [ Vectorstore  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#vectorstore)
    * [ Components  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#components)
  * [ Web Search Tool  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#web-search-tool)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ Tutorials  ](https://langchain-ai.github.io/langgraph/tutorials/)
  4. [ RAG  ](https://langchain-ai.github.io/langgraph/tutorials#rag)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/tutorials/rag/langgraph_adaptive_rag_local.ipynb "Edit this page")

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-0-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-0-2)%pip install --quiet -U langchain langchain_community tiktoken langchain-nomic "nomic[local]" langchain-ollama scikit-learn langgraph tavily-python bs4

```


# Local RAG agent with LLaMA3[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#local-rag-agent-with-llama3 "Permanent link")

We'll combine ideas from paper RAG papers into a RAG agent:

  * **Routing:** Adaptive RAG ([paper](https://arxiv.org/abs/2403.14403)). Route questions to different retrieval approaches
  * **Fallback:** Corrective RAG ([paper](https://arxiv.org/pdf/2401.15884.pdf)). Fallback to web search if docs are not relevant to query
  * **Self-correction:** Self-RAG ([paper](https://arxiv.org/abs/2310.11511)). Fix answers w/ hallucinations or don’t address question



![langgraph_adaptive_rag.png]()

## Local models[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#local-models "Permanent link")

### Embedding[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#embedding "Permanent link")

[GPT4All Embeddings](https://blog.nomic.ai/posts/nomic-embed-text-v1):

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-1-1)pip install langchain-nomic

```


### LLM[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#llm "Permanent link")

Use [Ollama](https://x.com/ollama/status/1839007158865899651) and [llama3.2](https://ai.meta.com/blog/llama-3-2-connect-2024-vision-edge-mobile-devices/):

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-2-1)ollama pull llama3.2:3b-instruct-fp16 

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-3-1)### LLM
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-3-2)fromlangchain_ollamaimport ChatOllama
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-3-3)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-3-4)local_llm = "llama3.2:3b-instruct-fp16"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-3-5)llm = ChatOllama(model=local_llm, temperature=0)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-3-6)llm_json_mode = ChatOllama(model=local_llm, temperature=0, format="json")

```


API Reference: [ChatOllama](https://python.langchain.com/api_reference/ollama/chat_models/langchain_ollama.chat_models.ChatOllama.html)

### Search[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#search "Permanent link")

For search, we use [Tavily](https://tavily.com/), which is a search engine optimized for LLMs and RAG.

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-4-1)importos
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-4-2)importgetpass
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-4-3)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-4-4)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-4-5)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-4-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-4-7)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-4-8)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-4-9)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-4-10)_set_env("TAVILY_API_KEY")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-4-11)os.environ["TOKENIZERS_PARALLELISM"] = "true"

```


### Tracing[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#tracing "Permanent link")

Optionally, use [LangSmith](https://www.langchain.com/langsmith) for tracing. 

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-5-1)_set_env("LANGSMITH_API_KEY")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-5-2)os.environ["LANGCHAIN_TRACING_V2"] = "true"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-5-3)os.environ["LANGCHAIN_PROJECT"] = "local-llama32-rag"

```


### Vectorstore[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#vectorstore "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-6-1)fromlangchain.text_splitterimport RecursiveCharacterTextSplitter
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-6-2)fromlangchain_community.document_loadersimport WebBaseLoader
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-6-3)fromlangchain_community.vectorstoresimport SKLearnVectorStore
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-6-4)fromlangchain_nomic.embeddingsimport NomicEmbeddings
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-6-5)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-6-6)urls = [
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-6-7)  "https://lilianweng.github.io/posts/2023-06-23-agent/",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-6-8)  "https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-6-9)  "https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-6-10)]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-6-11)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-6-12)# Load documents
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-6-13)docs = [WebBaseLoader(url).load() for url in urls]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-6-14)docs_list = [item for sublist in docs for item in sublist]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-6-15)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-6-16)# Split documents
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-6-17)text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-6-18)  chunk_size=1000, chunk_overlap=200
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-6-19))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-6-20)doc_splits = text_splitter.split_documents(docs_list)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-6-21)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-6-22)# Add to vectorDB
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-6-23)vectorstore = SKLearnVectorStore.from_documents(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-6-24)  documents=doc_splits,
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-6-25)  embedding=NomicEmbeddings(model="nomic-embed-text-v1.5", inference_mode="local"),
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-6-26))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-6-27)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-6-28)# Create retriever
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-6-29)retriever = vectorstore.as_retriever(k=3)

```


API Reference: [RecursiveCharacterTextSplitter](https://python.langchain.com/api_reference/text_splitters/character/langchain_text_splitters.character.RecursiveCharacterTextSplitter.html) | [WebBaseLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.web_base.WebBaseLoader.html) | [SKLearnVectorStore](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.sklearn.SKLearnVectorStore.html) | [NomicEmbeddings](https://python.langchain.com/api_reference/nomic/embeddings/langchain_nomic.embeddings.NomicEmbeddings.html)

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-7-1)USER_AGENT environment variable not set, consider setting it to identify your requests.

```


### Components[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#components "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-1)### Router
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-2)importjson
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-3)fromlangchain_core.messagesimport HumanMessage, SystemMessage
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-4)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-5)# Prompt
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-6)router_instructions = """You are an expert at routing a user question to a vectorstore or web search.
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-7)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-8)The vectorstore contains documents related to agents, prompt engineering, and adversarial attacks.
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-9)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-10)Use the vectorstore for questions on these topics. For all else, and especially for current events, use web-search.
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-11)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-12)Return JSON with single key, datasource, that is 'websearch' or 'vectorstore' depending on the question."""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-13)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-14)# Test router
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-15)test_web_search = llm_json_mode.invoke(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-16)  [SystemMessage(content=router_instructions)]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-17)  + [
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-18)    HumanMessage(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-19)      content="Who is favored to win the NFC Championship game in the 2024 season?"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-20)    )
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-21)  ]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-22))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-23)test_web_search_2 = llm_json_mode.invoke(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-24)  [SystemMessage(content=router_instructions)]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-25)  + [HumanMessage(content="What are the models released today for llama3.2?")]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-26))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-27)test_vector_store = llm_json_mode.invoke(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-28)  [SystemMessage(content=router_instructions)]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-29)  + [HumanMessage(content="What are the types of agent memory?")]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-30))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-31)print(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-32)  json.loads(test_web_search.content),
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-33)  json.loads(test_web_search_2.content),
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-34)  json.loads(test_vector_store.content),
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-8-35))

```


API Reference: [HumanMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.human.HumanMessage.html) | [SystemMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.system.SystemMessage.html)

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-9-1){'datasource': 'websearch'} {'datasource': 'websearch'} {'datasource': 'vectorstore'}

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-10-1)### Retrieval Grader
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-10-2)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-10-3)# Doc grader instructions
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-10-4)doc_grader_instructions = """You are a grader assessing relevance of a retrieved document to a user question.
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-10-5)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-10-6)If the document contains keyword(s) or semantic meaning related to the question, grade it as relevant."""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-10-7)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-10-8)# Grader prompt
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-10-9)doc_grader_prompt = """Here is the retrieved document: \n\n{document}\n\n Here is the user question: \n\n{question}. 
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-10-10)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-10-11)This carefully and objectively assess whether the document contains at least some information that is relevant to the question.
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-10-12)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-10-13)Return JSON with single key, binary_score, that is 'yes' or 'no' score to indicate whether the document contains at least some information that is relevant to the question."""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-10-14)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-10-15)# Test
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-10-16)question = "What is Chain of thought prompting?"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-10-17)docs = retriever.invoke(question)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-10-18)doc_txt = docs[1].page_content
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-10-19)doc_grader_prompt_formatted = doc_grader_prompt.format(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-10-20)  document=doc_txt, question=question
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-10-21))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-10-22)result = llm_json_mode.invoke(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-10-23)  [SystemMessage(content=doc_grader_instructions)]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-10-24)  + [HumanMessage(content=doc_grader_prompt_formatted)]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-10-25))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-10-26)json.loads(result.content)

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-11-1){'binary_score': 'yes'}

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-1)### Generate
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-2)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-3)# Prompt
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-4)rag_prompt = """You are an assistant for question-answering tasks. 
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-5)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-6)Here is the context to use to answer the question:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-7)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-8){context}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-9)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-10)Think carefully about the above context. 
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-11)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-12)Now, review the user question:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-13)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-14){question}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-15)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-16)Provide an answer to this questions using only the above context. 
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-17)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-18)Use three sentences maximum and keep the answer concise.
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-19)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-20)Answer:"""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-21)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-22)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-23)# Post-processing
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-24)defformat_docs(docs):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-25)  return "\n\n".join(doc.page_content for doc in docs)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-26)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-27)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-28)# Test
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-29)docs = retriever.invoke(question)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-30)docs_txt = format_docs(docs)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-31)rag_prompt_formatted = rag_prompt.format(context=docs_txt, question=question)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-32)generation = llm.invoke([HumanMessage(content=rag_prompt_formatted)])
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-12-33)print(generation.content)

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-13-1)Chain of Thought (CoT) prompting is a technique used in natural language processing to generate human-like responses by iteratively asking questions and refining the search space through external search queries, such as Wikipedia APIs. CoT prompting involves decomposing problems into multiple thought steps, generating multiple thoughts per step, and evaluating each state using a classifier or majority vote. The goal is to find an optimal instruction that leads to the desired output, which can be achieved by optimizing prompt parameters directly on the embedding space via gradient descent or searching over a pool of model-generated instruction candidates.

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-1)### Hallucination Grader
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-2)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-3)# Hallucination grader instructions
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-4)hallucination_grader_instructions = """
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-5)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-6)You are a teacher grading a quiz. 
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-7)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-8)You will be given FACTS and a STUDENT ANSWER. 
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-9)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-10)Here is the grade criteria to follow:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-11)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-12)(1) Ensure the STUDENT ANSWER is grounded in the FACTS. 
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-13)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-14)(2) Ensure the STUDENT ANSWER does not contain "hallucinated" information outside the scope of the FACTS.
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-15)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-16)Score:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-17)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-18)A score of yes means that the student's answer meets all of the criteria. This is the highest (best) score. 
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-19)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-20)A score of no means that the student's answer does not meet all of the criteria. This is the lowest possible score you can give.
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-21)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-22)Explain your reasoning in a step-by-step manner to ensure your reasoning and conclusion are correct. 
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-23)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-24)Avoid simply stating the correct answer at the outset."""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-25)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-26)# Grader prompt
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-27)hallucination_grader_prompt = """FACTS: \n\n{documents}\n\n STUDENT ANSWER: {generation}. 
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-28)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-29)Return JSON with two two keys, binary_score is 'yes' or 'no' score to indicate whether the STUDENT ANSWER is grounded in the FACTS. And a key, explanation, that contains an explanation of the score."""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-30)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-31)# Test using documents and generation from above
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-32)hallucination_grader_prompt_formatted = hallucination_grader_prompt.format(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-33)  documents=docs_txt, generation=generation.content
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-34))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-35)result = llm_json_mode.invoke(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-36)  [SystemMessage(content=hallucination_grader_instructions)]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-37)  + [HumanMessage(content=hallucination_grader_prompt_formatted)]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-38))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-14-39)json.loads(result.content)

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-15-1){'binary_score': 'yes',
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-15-2) 'explanation': 'The student answer provides a clear and accurate description of Chain of Thought (CoT) prompting, its components, and its goals. It also mentions various techniques used in CoT prompting, such as external search queries, prompt tuning, and automatic prompt engineering. The answer demonstrates an understanding of the concept and its applications in natural language processing.'}

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-1)### Answer Grader
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-2)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-3)# Answer grader instructions
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-4)answer_grader_instructions = """You are a teacher grading a quiz. 
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-5)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-6)You will be given a QUESTION and a STUDENT ANSWER. 
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-7)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-8)Here is the grade criteria to follow:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-9)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-10)(1) The STUDENT ANSWER helps to answer the QUESTION
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-11)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-12)Score:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-13)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-14)A score of yes means that the student's answer meets all of the criteria. This is the highest (best) score. 
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-15)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-16)The student can receive a score of yes if the answer contains extra information that is not explicitly asked for in the question.
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-17)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-18)A score of no means that the student's answer does not meet all of the criteria. This is the lowest possible score you can give.
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-19)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-20)Explain your reasoning in a step-by-step manner to ensure your reasoning and conclusion are correct. 
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-21)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-22)Avoid simply stating the correct answer at the outset."""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-23)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-24)# Grader prompt
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-25)answer_grader_prompt = """QUESTION: \n\n{question}\n\n STUDENT ANSWER: {generation}. 
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-26)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-27)Return JSON with two two keys, binary_score is 'yes' or 'no' score to indicate whether the STUDENT ANSWER meets the criteria. And a key, explanation, that contains an explanation of the score."""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-28)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-29)# Test
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-30)question = "What are the vision models released today as part of Llama 3.2?"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-31)answer = "The Llama 3.2 models released today include two vision models: Llama 3.2 11B Vision Instruct and Llama 3.2 90B Vision Instruct, which are available on Azure AI Model Catalog via managed compute. These models are part of Meta's first foray into multimodal AI and rival closed models like Anthropic's Claude 3 Haiku and OpenAI's GPT-4o mini in visual reasoning. They replace the older text-only Llama 3.1 models."
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-32)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-33)# Test using question and generation from above
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-34)answer_grader_prompt_formatted = answer_grader_prompt.format(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-35)  question=question, generation=answer
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-36))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-37)result = llm_json_mode.invoke(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-38)  [SystemMessage(content=answer_grader_instructions)]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-39)  + [HumanMessage(content=answer_grader_prompt_formatted)]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-40))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-16-41)json.loads(result.content)

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-17-1){'binary_score': 'yes',
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-17-2) 'explanation': "The student's answer helps to answer the question by providing specific details about the vision models released as part of Llama 3.2. The answer mentions two vision models (Llama 3.2 11B Vision Instruct and Llama 3.2 90B Vision Instruct) and their availability on Azure AI Model Catalog via managed compute. Additionally, the student provides context about Meta's first foray into multimodal AI and compares these models to other visual reasoning models like Claude 3 Haiku and GPT-4o mini. This extra information is not explicitly asked for in the question, but it demonstrates a thorough understanding of the topic. The answer also correctly states that these models replace the older text-only Llama 3.1 models, which meets all the criteria specified in the question."}

```


## Web Search Tool[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#web-search-tool "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-18-1)### Search
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-18-2)fromlangchain_community.tools.tavily_searchimport TavilySearchResults
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-18-3)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-18-4)web_search_tool = TavilySearchResults(k=3)

```


API Reference: [TavilySearchResults](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.tavily_search.tool.TavilySearchResults.html)

# Graph[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#graph "Permanent link")

We build the above workflow as a graph using [LangGraph](https://langchain-ai.github.io/langgraph/).

### Graph state[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#graph-state "Permanent link")

The graph `state` schema contains keys that we want to:

  * Pass to each node in our graph
  * Optionally, modify in each node of our graph 



See conceptual docs [here](https://langchain-ai.github.io/langgraph/concepts/low_level/#state).

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-19-1)importoperator
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-19-2)fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-19-3)fromtypingimport List, Annotated
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-19-4)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-19-5)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-19-6)classGraphState(TypedDict):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-19-7)"""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-19-8)  Graph state is a dictionary that contains information we want to propagate to, and modify in, each graph node.
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-19-9)  """
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-19-10)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-19-11)  question: str # User question
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-19-12)  generation: str # LLM generation
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-19-13)  web_search: str # Binary decision to run web search
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-19-14)  max_retries: int # Max number of retries for answer generation
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-19-15)  answers: int # Number of answers generated
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-19-16)  loop_step: Annotated[int, operator.add]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-19-17)  documents: List[str] # List of retrieved documents

```


Each node in our graph is simply a function that:

(1) Take `state` as an input

(2) Modifies `state`

(3) Write the modified `state` to the state schema (dict)

See conceptual docs [here](https://langchain-ai.github.io/langgraph/concepts/low_level/#nodes).

Each edge routes between nodes in the graph.

See conceptual docs [here](https://langchain-ai.github.io/langgraph/concepts/low_level/#edges).

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-1)fromlangchain.schemaimport Document
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-2)fromlanggraph.graphimport END
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-3)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-4)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-5)### Nodes
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-6)defretrieve(state):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-7)"""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-8)  Retrieve documents from vectorstore
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-9)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-10)  Args:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-11)    state (dict): The current graph state
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-12)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-13)  Returns:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-14)    state (dict): New key added to state, documents, that contains retrieved documents
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-15)  """
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-16)  print("---RETRIEVE---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-17)  question = state["question"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-18)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-19)  # Write retrieved documents to documents key in state
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-20)  documents = retriever.invoke(question)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-21)  return {"documents": documents}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-22)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-23)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-24)defgenerate(state):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-25)"""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-26)  Generate answer using RAG on retrieved documents
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-27)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-28)  Args:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-29)    state (dict): The current graph state
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-30)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-31)  Returns:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-32)    state (dict): New key added to state, generation, that contains LLM generation
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-33)  """
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-34)  print("---GENERATE---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-35)  question = state["question"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-36)  documents = state["documents"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-37)  loop_step = state.get("loop_step", 0)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-38)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-39)  # RAG generation
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-40)  docs_txt = format_docs(documents)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-41)  rag_prompt_formatted = rag_prompt.format(context=docs_txt, question=question)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-42)  generation = llm.invoke([HumanMessage(content=rag_prompt_formatted)])
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-43)  return {"generation": generation, "loop_step": loop_step + 1}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-44)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-45)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-46)defgrade_documents(state):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-47)"""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-48)  Determines whether the retrieved documents are relevant to the question
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-49)  If any document is not relevant, we will set a flag to run web search
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-50)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-51)  Args:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-52)    state (dict): The current graph state
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-53)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-54)  Returns:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-55)    state (dict): Filtered out irrelevant documents and updated web_search state
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-56)  """
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-57)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-58)  print("---CHECK DOCUMENT RELEVANCE TO QUESTION---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-59)  question = state["question"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-60)  documents = state["documents"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-61)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-62)  # Score each doc
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-63)  filtered_docs = []
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-64)  web_search = "No"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-65)  for d in documents:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-66)    doc_grader_prompt_formatted = doc_grader_prompt.format(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-67)      document=d.page_content, question=question
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-68)    )
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-69)    result = llm_json_mode.invoke(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-70)      [SystemMessage(content=doc_grader_instructions)]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-71)      + [HumanMessage(content=doc_grader_prompt_formatted)]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-72)    )
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-73)    grade = json.loads(result.content)["binary_score"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-74)    # Document relevant
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-75)    if grade.lower() == "yes":
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-76)      print("---GRADE: DOCUMENT RELEVANT---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-77)      filtered_docs.append(d)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-78)    # Document not relevant
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-79)    else:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-80)      print("---GRADE: DOCUMENT NOT RELEVANT---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-81)      # We do not include the document in filtered_docs
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-82)      # We set a flag to indicate that we want to run web search
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-83)      web_search = "Yes"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-84)      continue
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-85)  return {"documents": filtered_docs, "web_search": web_search}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-86)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-87)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-88)defweb_search(state):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-89)"""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-90)  Web search based based on the question
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-91)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-92)  Args:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-93)    state (dict): The current graph state
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-94)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-95)  Returns:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-96)    state (dict): Appended web results to documents
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-97)  """
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-98)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-99)  print("---WEB SEARCH---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-100)  question = state["question"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-101)  documents = state.get("documents", [])
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-102)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-103)  # Web search
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-104)  docs = web_search_tool.invoke({"query": question})
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-105)  web_results = "\n".join([d["content"] for d in docs])
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-106)  web_results = Document(page_content=web_results)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-107)  documents.append(web_results)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-108)  return {"documents": documents}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-109)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-110)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-111)### Edges
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-112)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-113)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-114)defroute_question(state):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-115)"""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-116)  Route question to web search or RAG
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-117)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-118)  Args:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-119)    state (dict): The current graph state
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-120)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-121)  Returns:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-122)    str: Next node to call
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-123)  """
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-124)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-125)  print("---ROUTE QUESTION---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-126)  route_question = llm_json_mode.invoke(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-127)    [SystemMessage(content=router_instructions)]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-128)    + [HumanMessage(content=state["question"])]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-129)  )
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-130)  source = json.loads(route_question.content)["datasource"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-131)  if source == "websearch":
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-132)    print("---ROUTE QUESTION TO WEB SEARCH---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-133)    return "websearch"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-134)  elif source == "vectorstore":
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-135)    print("---ROUTE QUESTION TO RAG---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-136)    return "vectorstore"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-137)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-138)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-139)defdecide_to_generate(state):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-140)"""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-141)  Determines whether to generate an answer, or add web search
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-142)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-143)  Args:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-144)    state (dict): The current graph state
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-145)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-146)  Returns:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-147)    str: Binary decision for next node to call
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-148)  """
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-149)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-150)  print("---ASSESS GRADED DOCUMENTS---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-151)  question = state["question"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-152)  web_search = state["web_search"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-153)  filtered_documents = state["documents"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-154)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-155)  if web_search == "Yes":
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-156)    # All documents have been filtered check_relevance
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-157)    # We will re-generate a new query
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-158)    print(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-159)      "---DECISION: NOT ALL DOCUMENTS ARE RELEVANT TO QUESTION, INCLUDE WEB SEARCH---"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-160)    )
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-161)    return "websearch"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-162)  else:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-163)    # We have relevant documents, so generate answer
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-164)    print("---DECISION: GENERATE---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-165)    return "generate"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-166)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-167)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-168)defgrade_generation_v_documents_and_question(state):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-169)"""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-170)  Determines whether the generation is grounded in the document and answers question
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-171)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-172)  Args:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-173)    state (dict): The current graph state
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-174)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-175)  Returns:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-176)    str: Decision for next node to call
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-177)  """
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-178)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-179)  print("---CHECK HALLUCINATIONS---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-180)  question = state["question"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-181)  documents = state["documents"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-182)  generation = state["generation"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-183)  max_retries = state.get("max_retries", 3) # Default to 3 if not provided
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-184)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-185)  hallucination_grader_prompt_formatted = hallucination_grader_prompt.format(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-186)    documents=format_docs(documents), generation=generation.content
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-187)  )
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-188)  result = llm_json_mode.invoke(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-189)    [SystemMessage(content=hallucination_grader_instructions)]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-190)    + [HumanMessage(content=hallucination_grader_prompt_formatted)]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-191)  )
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-192)  grade = json.loads(result.content)["binary_score"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-193)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-194)  # Check hallucination
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-195)  if grade == "yes":
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-196)    print("---DECISION: GENERATION IS GROUNDED IN DOCUMENTS---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-197)    # Check question-answering
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-198)    print("---GRADE GENERATION vs QUESTION---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-199)    # Test using question and generation from above
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-200)    answer_grader_prompt_formatted = answer_grader_prompt.format(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-201)      question=question, generation=generation.content
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-202)    )
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-203)    result = llm_json_mode.invoke(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-204)      [SystemMessage(content=answer_grader_instructions)]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-205)      + [HumanMessage(content=answer_grader_prompt_formatted)]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-206)    )
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-207)    grade = json.loads(result.content)["binary_score"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-208)    if grade == "yes":
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-209)      print("---DECISION: GENERATION ADDRESSES QUESTION---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-210)      return "useful"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-211)    elif state["loop_step"] <= max_retries:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-212)      print("---DECISION: GENERATION DOES NOT ADDRESS QUESTION---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-213)      return "not useful"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-214)    else:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-215)      print("---DECISION: MAX RETRIES REACHED---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-216)      return "max retries"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-217)  elif state["loop_step"] <= max_retries:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-218)    print("---DECISION: GENERATION IS NOT GROUNDED IN DOCUMENTS, RE-TRY---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-219)    return "not supported"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-220)  else:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-221)    print("---DECISION: MAX RETRIES REACHED---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-20-222)    return "max retries"

```


API Reference: [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html) | [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END)

## Control Flow[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#control-flow "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-1)fromlanggraph.graphimport StateGraph
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-2)fromIPython.displayimport Image, display
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-3)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-4)workflow = StateGraph(GraphState)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-5)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-6)# Define the nodes
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-7)workflow.add_node("websearch", web_search) # web search
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-8)workflow.add_node("retrieve", retrieve) # retrieve
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-9)workflow.add_node("grade_documents", grade_documents) # grade documents
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-10)workflow.add_node("generate", generate) # generate
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-11)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-12)# Build graph
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-13)workflow.set_conditional_entry_point(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-14)  route_question,
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-15)  {
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-16)    "websearch": "websearch",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-17)    "vectorstore": "retrieve",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-18)  },
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-19))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-20)workflow.add_edge("websearch", "generate")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-21)workflow.add_edge("retrieve", "grade_documents")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-22)workflow.add_conditional_edges(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-23)  "grade_documents",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-24)  decide_to_generate,
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-25)  {
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-26)    "websearch": "websearch",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-27)    "generate": "generate",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-28)  },
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-29))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-30)workflow.add_conditional_edges(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-31)  "generate",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-32)  grade_generation_v_documents_and_question,
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-33)  {
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-34)    "not supported": "generate",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-35)    "useful": END,
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-36)    "not useful": "websearch",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-37)    "max retries": END,
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-38)  },
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-39))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-40)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-41)# Compile
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-42)graph = workflow.compile()
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-21-43)display(Image(graph.get_graph().draw_mermaid_png()))

```


API Reference: [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph)

![]()

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-22-1)inputs = {"question": "What are the types of agent memory?", "max_retries": 3}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-22-2)for event in graph.stream(inputs, stream_mode="values"):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-22-3)  print(event)

```


Trace:

<https://smith.langchain.com/public/1e01baea-53e9-4341-a6d1-b1614a800a97/r>

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-23-1)# Test on current events
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-23-2)inputs = {
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-23-3)  "question": "What are the models released today for llama3.2?",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-23-4)  "max_retries": 3,
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-23-5)}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-23-6)for event in graph.stream(inputs, stream_mode="values"):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__codelineno-23-7)  print(event)

```


Trace:

<https://smith.langchain.com/public/acdfa49d-aa11-48fb-9d9c-13a687ff311f/r>

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Adaptive RAG  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/) [ Next  Agentic RAG  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
