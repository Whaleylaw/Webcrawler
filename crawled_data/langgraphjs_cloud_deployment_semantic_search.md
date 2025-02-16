---
url: https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#how-to-add-semantic-search-to-your-langgraph-deployment)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to add semantic search to your LangGraph deployment 

[ ](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/?q= "Share")

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

How-to Guides 
        * [ Installation  ](https://langchain-ai.github.io/langgraphjs/how-tos#installation)
        * [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
        * LangGraph Platform  LangGraph Platform 
          * [ LangGraph Platform  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph-platform)
          * Application Structure  Application Structure 
            * [ Application Structure  ](https://langchain-ai.github.io/langgraphjs/how-tos#application-structure)
            * [ How to Set Up a LangGraph Application for Deployment  ](https://langchain-ai.github.io/langgraphjs/cloud/deployment/setup/)
            * [ How to Set Up a LangGraph Application for Deployment  ](https://langchain-ai.github.io/langgraphjs/cloud/deployment/setup_pyproject/)
            * [ How to Set Up a LangGraph.js Application for Deployment  ](https://langchain-ai.github.io/langgraphjs/cloud/deployment/setup_javascript/)
            * How to add semantic search to your LangGraph deployment  [ How to add semantic search to your LangGraph deployment  ](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/) Table of contents 
              * [ Prerequisites  ](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#prerequisites)
              * [ Steps  ](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#steps)
              * [ Usage  ](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#usage)
              * [ Custom Embeddings  ](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#custom-embeddings)
              * [ Querying via the API  ](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#querying-via-the-api)
            * [ How to customize Dockerfile  ](https://langchain-ai.github.io/langgraphjs/cloud/deployment/custom_docker/)
            * [ How to test a LangGraph app locally  ](https://langchain-ai.github.io/langgraphjs/cloud/deployment/test_locally/)
            * [ Rebuild Graph at Runtime  ](https://langchain-ai.github.io/langgraphjs/cloud/deployment/graph_rebuild/)
          * [ Deployment  ](https://langchain-ai.github.io/langgraphjs/how-tos#deployment)
          * [ Authentication & Access Control  ](https://langchain-ai.github.io/langgraphjs/how-tos#authentication-access-control)
          * [ Assistants  ](https://langchain-ai.github.io/langgraphjs/how-tos#assistants)
          * [ Threads  ](https://langchain-ai.github.io/langgraphjs/how-tos#threads)
          * [ Runs  ](https://langchain-ai.github.io/langgraphjs/how-tos#runs)
          * [ Streaming  ](https://langchain-ai.github.io/langgraphjs/how-tos#streaming_1)
          * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraphjs/how-tos#human-in-the-loop_1)
          * [ Double-texting  ](https://langchain-ai.github.io/langgraphjs/how-tos#double-texting)
          * [ Webhooks  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/webhooks/)
          * [ Cron Jobs  ](https://langchain-ai.github.io/langgraphjs/cloud/how-tos/cron_jobs/)
          * [ LangGraph Studio  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph-studio)
      * [ Concepts  ](https://langchain-ai.github.io/langgraphjs/concepts/)
      * [ Tutorials  ](https://langchain-ai.github.io/langgraphjs/tutorials/)
    * Resources  Resources 
      * [ Adopters  ](https://langchain-ai.github.io/langgraphjs/adopters/)
      * [ FAQ  ](https://langchain-ai.github.io/langgraphjs/concepts/faq/)
      * [ Troubleshooting  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraphjs/reference/)
  * [ Versions  ](https://langchain-ai.github.io/langgraphjs/versions/)



Table of contents 

  * [ Prerequisites  ](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#prerequisites)
  * [ Steps  ](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#steps)
  * [ Usage  ](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#usage)
  * [ Custom Embeddings  ](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#custom-embeddings)
  * [ Querying via the API  ](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#querying-via-the-api)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph Platform  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph-platform)
  5. [ Application Structure  ](https://langchain-ai.github.io/langgraphjs/how-tos#application-structure)



# How to add semantic search to your LangGraph deployment[¶](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#how-to-add-semantic-search-to-your-langgraph-deployment "Permanent link")

This guide explains how to add semantic search to your LangGraph deployment's cross-thread [store](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#memory-store), so that your agent can search for memories and other documents by semantic similarity.

## Prerequisites[¶](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#prerequisites "Permanent link")

  * A LangGraph deployment (see [how to deploy](https://langchain-ai.github.io/langgraphjs/cloud/deployment/setup_pyproject/))
  * API keys for your embedding provider (in this case, OpenAI)
  * `langchain >= 0.3.8` (if you specify using the string format below)



## Steps[¶](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#steps "Permanent link")

  1. Update your `langgraph.json` configuration file to include the store configuration:



```
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-0-1){
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-0-2)...
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-0-3)"store":{
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-0-4)"index":{
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-0-5)"embed":"openai:text-embeddings-3-small",
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-0-6)"dims":1536,
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-0-7)"fields":["$"]
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-0-8)}
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-0-9)}
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-0-10)}

```


This configuration:

  * Uses OpenAI's text-embeddings-3-small model for generating embeddings
  * Sets the embedding dimension to 1536 (matching the model's output)
  * Indexes all fields in your stored data (`["$"]` means index everything, or specify specific fields like `["text", "metadata.title"]`)

  * To use the string embedding format above, make sure your dependencies include `langchain >= 0.3.8`:




```
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-1-1)# In pyproject.toml
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-1-2)[project]
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-1-3)dependencies=[
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-1-4)"langchain>=0.3.8"
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-1-5)]

```


Or if using requirements.txt:

```
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-2-1)langchain>=0.3.8

```


## Usage[¶](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#usage "Permanent link")

Once configured, you can use semantic search in your LangGraph nodes. The store requires a namespace tuple to organize memories:

```
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-3-1)defsearch_memory(state: State, *, store: BaseStore):
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-3-2)  # Search the store using semantic similarity
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-3-3)  # The namespace tuple helps organize different types of memories
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-3-4)  # e.g., ("user_facts", "preferences") or ("conversation", "summaries")
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-3-5)  results = store.search(
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-3-6)    namespace=("memory", "facts"), # Organize memories by type
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-3-7)    query="your search query",
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-3-8)    limit=3 # number of results to return
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-3-9)  )
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-3-10)  return results

```


## Custom Embeddings[¶](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#custom-embeddings "Permanent link")

If you want to use custom embeddings, you can pass a path to a custom embedding function:

```
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-4-1){
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-4-2)...
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-4-3)"store":{
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-4-4)"index":{
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-4-5)"embed":"path/to/embedding_function.py:embed",
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-4-6)"dims":1536,
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-4-7)"fields":["$"]
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-4-8)}
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-4-9)}
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-4-10)}

```


The deployment will look for the function in the specified path. The function must be async and accept a list of strings:

```
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-5-1)# path/to/embedding_function.py
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-5-2)fromopenaiimport AsyncOpenAI
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-5-3)
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-5-4)client = AsyncOpenAI()
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-5-5)
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-5-6)async defaembed_texts(texts: list[str]) -> list[list[float]]:
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-5-7)"""Custom embedding function that must:
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-5-8)  1. Be async
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-5-9)  2. Accept a list of strings
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-5-10)  3. Return a list of float arrays (embeddings)
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-5-11)  """
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-5-12)  response = await client.embeddings.create(
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-5-13)    model="text-embedding-3-small",
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-5-14)    input=texts
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-5-15)  )
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-5-16)  return [e.embedding for e in response.data]

```


## Querying via the API[¶](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#querying-via-the-api "Permanent link")

You can also query the store using the LangGraph SDK. Since the SDK uses async operations:

```
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-6-1)fromlanggraph_sdkimport get_client
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-6-2)
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-6-3)async defsearch_store():
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-6-4)  client = get_client()
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-6-5)  results = await client.store.search_items(
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-6-6)    ("memory", "facts"),
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-6-7)    query="your search query",
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-6-8)    limit=3 # number of results to return
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-6-9)  )
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-6-10)  return results
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-6-11)
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-6-12)# Use in an async context
[](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__codelineno-6-13)results = await search_store()

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to Set Up a LangGraph.js Application for Deployment  ](https://langchain-ai.github.io/langgraphjs/cloud/deployment/setup_javascript/) [ Next  How to customize Dockerfile  ](https://langchain-ai.github.io/langgraphjs/cloud/deployment/custom_docker/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/cloud/deployment/semantic_search/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
