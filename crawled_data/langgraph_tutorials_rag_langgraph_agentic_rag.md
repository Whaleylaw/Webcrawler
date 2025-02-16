---
url: https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#agentic-rag)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Agentic RAG 

[ ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/?q= "Share")

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
          * Agentic RAG  [ Agentic RAG  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/) Table of contents 
            * [ Setup  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#setup)
            * [ Retriever  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#retriever)
            * [ Agent State  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#agent-state)
            * [ Nodes and Edges  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#nodes-and-edges)
            * [ Graph  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#graph)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#setup)
  * [ Retriever  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#retriever)
  * [ Agent State  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#agent-state)
  * [ Nodes and Edges  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#nodes-and-edges)
  * [ Graph  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#graph)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ Tutorials  ](https://langchain-ai.github.io/langgraph/tutorials/)
  4. [ RAG  ](https://langchain-ai.github.io/langgraph/tutorials#rag)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/tutorials/rag/langgraph_agentic_rag.ipynb "Edit this page")

# Agentic RAG[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#agentic-rag "Permanent link")

[Retrieval Agents](https://python.langchain.com/docs/tutorials/qa_chat_history/#agents) are useful when we want to make decisions about whether to retrieve from an index.

To implement a retrieval agent, we simply need to give an LLM access to a retriever tool.

We can incorporate this into [LangGraph](https://langchain-ai.github.io/langgraph/).

## Setup[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#setup "Permanent link")

First, let's download the required packages and set our API keys:

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-0-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-0-2)%pip install -U --quiet langchain-community tiktoken langchain-openai langchainhub chromadb langchain langgraph langchain-text-splitters beautifulsoup4

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-1-1)importgetpass
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-1-2)importos
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-1-5)def_set_env(key: str):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-1-6)  if key not in os.environ:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-1-7)    os.environ[key] = getpass.getpass(f"{key}:")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-1-8)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-1-10)_set_env("OPENAI_API_KEY")

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Retriever[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#retriever "Permanent link")

First, we index 3 blog posts.

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-2-1)fromlangchain_community.document_loadersimport WebBaseLoader
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-2-2)fromlangchain_community.vectorstoresimport Chroma
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-2-3)fromlangchain_openaiimport OpenAIEmbeddings
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-2-4)fromlangchain_text_splittersimport RecursiveCharacterTextSplitter
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-2-5)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-2-6)urls = [
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-2-7)  "https://lilianweng.github.io/posts/2023-06-23-agent/",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-2-8)  "https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-2-9)  "https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-2-10)]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-2-11)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-2-12)docs = [WebBaseLoader(url).load() for url in urls]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-2-13)docs_list = [item for sublist in docs for item in sublist]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-2-14)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-2-15)text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-2-16)  chunk_size=100, chunk_overlap=50
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-2-17))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-2-18)doc_splits = text_splitter.split_documents(docs_list)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-2-19)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-2-20)# Add to vectorDB
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-2-21)vectorstore = Chroma.from_documents(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-2-22)  documents=doc_splits,
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-2-23)  collection_name="rag-chroma",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-2-24)  embedding=OpenAIEmbeddings(),
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-2-25))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-2-26)retriever = vectorstore.as_retriever()

```


API Reference: [WebBaseLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.web_base.WebBaseLoader.html) | [Chroma](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.chroma.Chroma.html) | [OpenAIEmbeddings](https://python.langchain.com/api_reference/openai/embeddings/langchain_openai.embeddings.base.OpenAIEmbeddings.html) | [RecursiveCharacterTextSplitter](https://python.langchain.com/api_reference/text_splitters/character/langchain_text_splitters.character.RecursiveCharacterTextSplitter.html)

Then we create a retriever tool.

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-3-1)fromlangchain.tools.retrieverimport create_retriever_tool
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-3-2)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-3-3)retriever_tool = create_retriever_tool(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-3-4)  retriever,
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-3-5)  "retrieve_blog_posts",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-3-6)  "Search and return information about Lilian Weng blog posts on LLM agents, prompt engineering, and adversarial attacks on LLMs.",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-3-7))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-3-8)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-3-9)tools = [retriever_tool]

```


API Reference: [create_retriever_tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.retriever.create_retriever_tool.html)

## Agent State[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#agent-state "Permanent link")

We will define a graph.

A `state` object that it passes around to each node.

Our state will be a list of `messages`.

Each node in our graph will append to it.

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-4-1)fromtypingimport Annotated, Sequence
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-4-2)fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-4-3)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-4-4)fromlangchain_core.messagesimport BaseMessage
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-4-5)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-4-6)fromlanggraph.graph.messageimport add_messages
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-4-7)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-4-8)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-4-9)classAgentState(TypedDict):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-4-10)  # The add_messages function defines how an update should be processed
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-4-11)  # Default is to replace. add_messages says "append"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-4-12)  messages: Annotated[Sequence[BaseMessage], add_messages]

```


API Reference: [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html) | [add_messages](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.message.add_messages)

## Nodes and Edges[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#nodes-and-edges "Permanent link")

We can lay out an agentic RAG graph like this:

  * The state is a set of messages
  * Each node will update (append to) state
  * Conditional edges decide which node to visit next



![Screenshot 2024-02-14 at 3.43.58 PM.png]()

Using Pydantic with LangChain

This notebook uses Pydantic v2 `BaseModel`, which requires `langchain-core >= 0.3`. Using `langchain-core < 0.3` will result in errors due to mixing of Pydantic v1 and v2 `BaseModels`. 

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-1)fromtypingimport Annotated, Literal, Sequence
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-2)fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-3)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-4)fromlangchainimport hub
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-5)fromlangchain_core.messagesimport BaseMessage, HumanMessage
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-6)fromlangchain_core.output_parsersimport StrOutputParser
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-7)fromlangchain_core.promptsimport PromptTemplate
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-8)fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-9)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-10)frompydanticimport BaseModel, Field
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-11)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-12)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-13)fromlanggraph.prebuiltimport tools_condition
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-14)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-15)### Edges
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-16)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-17)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-18)defgrade_documents(state) -> Literal["generate", "rewrite"]:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-19)"""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-20)  Determines whether the retrieved documents are relevant to the question.
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-21)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-22)  Args:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-23)    state (messages): The current state
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-24)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-25)  Returns:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-26)    str: A decision for whether the documents are relevant or not
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-27)  """
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-28)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-29)  print("---CHECK RELEVANCE---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-30)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-31)  # Data model
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-32)  classgrade(BaseModel):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-33)"""Binary score for relevance check."""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-34)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-35)    binary_score: str = Field(description="Relevance score 'yes' or 'no'")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-36)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-37)  # LLM
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-38)  model = ChatOpenAI(temperature=0, model="gpt-4o", streaming=True)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-39)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-40)  # LLM with tool and validation
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-41)  llm_with_tool = model.with_structured_output(grade)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-42)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-43)  # Prompt
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-44)  prompt = PromptTemplate(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-45)    template="""You are a grader assessing relevance of a retrieved document to a user question. \n
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-46)    Here is the retrieved document: \n\n{context}\n\n
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-47)    Here is the user question: {question}\n
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-48)    If the document contains keyword(s) or semantic meaning related to the user question, grade it as relevant. \n
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-49)    Give a binary score 'yes' or 'no' score to indicate whether the document is relevant to the question.""",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-50)    input_variables=["context", "question"],
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-51)  )
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-52)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-53)  # Chain
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-54)  chain = prompt | llm_with_tool
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-55)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-56)  messages = state["messages"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-57)  last_message = messages[-1]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-58)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-59)  question = messages[0].content
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-60)  docs = last_message.content
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-61)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-62)  scored_result = chain.invoke({"question": question, "context": docs})
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-63)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-64)  score = scored_result.binary_score
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-65)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-66)  if score == "yes":
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-67)    print("---DECISION: DOCS RELEVANT---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-68)    return "generate"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-69)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-70)  else:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-71)    print("---DECISION: DOCS NOT RELEVANT---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-72)    print(score)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-73)    return "rewrite"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-74)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-75)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-76)### Nodes
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-77)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-78)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-79)defagent(state):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-80)"""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-81)  Invokes the agent model to generate a response based on the current state. Given
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-82)  the question, it will decide to retrieve using the retriever tool, or simply end.
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-83)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-84)  Args:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-85)    state (messages): The current state
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-86)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-87)  Returns:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-88)    dict: The updated state with the agent response appended to messages
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-89)  """
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-90)  print("---CALL AGENT---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-91)  messages = state["messages"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-92)  model = ChatOpenAI(temperature=0, streaming=True, model="gpt-4-turbo")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-93)  model = model.bind_tools(tools)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-94)  response = model.invoke(messages)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-95)  # We return a list, because this will get added to the existing list
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-96)  return {"messages": [response]}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-97)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-98)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-99)defrewrite(state):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-100)"""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-101)  Transform the query to produce a better question.
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-102)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-103)  Args:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-104)    state (messages): The current state
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-105)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-106)  Returns:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-107)    dict: The updated state with re-phrased question
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-108)  """
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-109)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-110)  print("---TRANSFORM QUERY---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-111)  messages = state["messages"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-112)  question = messages[0].content
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-113)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-114)  msg = [
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-115)    HumanMessage(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-116)      content=f""" \n
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-117)  Look at the input and try to reason about the underlying semantic intent / meaning. \n
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-118)  Here is the initial question:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-119)\n ------- \n
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-120){question}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-121)\n ------- \n
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-122)  Formulate an improved question: """,
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-123)    )
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-124)  ]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-125)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-126)  # Grader
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-127)  model = ChatOpenAI(temperature=0, model="gpt-4-0125-preview", streaming=True)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-128)  response = model.invoke(msg)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-129)  return {"messages": [response]}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-130)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-131)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-132)defgenerate(state):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-133)"""
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-134)  Generate answer
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-135)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-136)  Args:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-137)    state (messages): The current state
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-138)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-139)  Returns:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-140)     dict: The updated state with re-phrased question
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-141)  """
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-142)  print("---GENERATE---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-143)  messages = state["messages"]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-144)  question = messages[0].content
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-145)  last_message = messages[-1]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-146)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-147)  docs = last_message.content
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-148)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-149)  # Prompt
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-150)  prompt = hub.pull("rlm/rag-prompt")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-151)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-152)  # LLM
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-153)  llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0, streaming=True)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-154)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-155)  # Post-processing
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-156)  defformat_docs(docs):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-157)    return "\n\n".join(doc.page_content for doc in docs)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-158)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-159)  # Chain
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-160)  rag_chain = prompt | llm | StrOutputParser()
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-161)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-162)  # Run
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-163)  response = rag_chain.invoke({"context": docs, "question": question})
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-164)  return {"messages": [response]}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-165)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-166)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-167)print("*" * 20 + "Prompt[rlm/rag-prompt]" + "*" * 20)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-5-168)prompt = hub.pull("rlm/rag-prompt").pretty_print() # Show what the prompt looks like

```


API Reference: [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html) | [HumanMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.human.HumanMessage.html) | [StrOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.string.StrOutputParser.html) | [PromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.prompt.PromptTemplate.html) | [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html) | [tools_condition](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.tools_condition)

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-6-1)********************Prompt[rlm/rag-prompt]********************
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-6-2)================================[1m Human Message [0m=================================
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-6-3)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-6-4)You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-6-5)Question: [33;1m[1;3m{question}[0m 
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-6-6)Context: [33;1m[1;3m{context}[0m 
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-6-7)Answer:

```


## Graph[¶](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#graph "Permanent link")

  * Start with an agent, `call_model`
  * Agent make a decision to call a function
  * If so, then `action` to call tool (retriever)
  * Then call agent with the tool output added to messages (`state`)



```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-1)fromlanggraph.graphimport END, StateGraph, START
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-2)fromlanggraph.prebuiltimport ToolNode
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-3)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-4)# Define a new graph
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-5)workflow = StateGraph(AgentState)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-6)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-7)# Define the nodes we will cycle between
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-8)workflow.add_node("agent", agent) # agent
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-9)retrieve = ToolNode([retriever_tool])
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-10)workflow.add_node("retrieve", retrieve) # retrieval
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-11)workflow.add_node("rewrite", rewrite) # Re-writing the question
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-12)workflow.add_node(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-13)  "generate", generate
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-14)) # Generating a response after we know the documents are relevant
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-15)# Call agent node to decide to retrieve or not
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-16)workflow.add_edge(START, "agent")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-17)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-18)# Decide whether to retrieve
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-19)workflow.add_conditional_edges(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-20)  "agent",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-21)  # Assess agent decision
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-22)  tools_condition,
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-23)  {
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-24)    # Translate the condition outputs to nodes in our graph
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-25)    "tools": "retrieve",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-26)    END: END,
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-27)  },
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-28))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-29)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-30)# Edges taken after the `action` node is called.
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-31)workflow.add_conditional_edges(
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-32)  "retrieve",
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-33)  # Assess agent decision
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-34)  grade_documents,
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-35))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-36)workflow.add_edge("generate", END)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-37)workflow.add_edge("rewrite", "agent")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-38)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-39)# Compile
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-7-40)graph = workflow.compile()

```


API Reference: [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [ToolNode](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.ToolNode)

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-8-1)fromIPython.displayimport Image, display
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-8-2)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-8-3)try:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-8-4)  display(Image(graph.get_graph(xray=True).draw_mermaid_png()))
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-8-5)except Exception:
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-8-6)  # This requires some extra dependencies and is optional
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-8-7)  pass

```


![]()

```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-1)importpprint
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-2)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-3)inputs = {
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-4)  "messages": [
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-5)    ("user", "What does Lilian Weng say about the types of agent memory?"),
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-6)  ]
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-7)}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-8)for output in graph.stream(inputs):
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-9)  for key, value in output.items():
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-10)    pprint.pprint(f"Output from node '{key}':")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-11)    pprint.pprint("---")
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-12)    pprint.pprint(value, indent=2, width=80, depth=None)
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-9-13)  pprint.pprint("\n---\n")

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-10-1)---CALL AGENT---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-10-2)"Output from node 'agent':"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-10-3)'---'
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-10-4){ 'messages': [ AIMessage(content='', additional_kwargs={'tool_calls': [{'index': 0, 'id': 'call_z36oPZN8l1UC6raxrebqc1bH', 'function': {'arguments': '{"query":"types of agent memory"}', 'name': 'retrieve_blog_posts'}, 'type': 'function'}]}, response_metadata={'finish_reason': 'tool_calls'}, id='run-2bad2518-8187-4d8f-8e23-2b9501becb6f-0', tool_calls=[{'name': 'retrieve_blog_posts', 'args': {'query': 'types of agent memory'}, 'id': 'call_z36oPZN8l1UC6raxrebqc1bH'}])]}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-10-5)'\n---\n'
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-10-6)---CHECK RELEVANCE---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-10-7)---DECISION: DOCS RELEVANT---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-10-8)"Output from node 'retrieve':"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-10-9)'---'
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-10-10){ 'messages': [ ToolMessage(content='Table of Contents\n\n\n\nAgent System Overview\n\nComponent One: Planning\n\nTask Decomposition\n\nSelf-Reflection\n\n\nComponent Two: Memory\n\nTypes of Memory\n\nMaximum Inner Product Search (MIPS)\n\n\nComponent Three: Tool Use\n\nCase Studies\n\nScientific Discovery Agent\n\nGenerative Agents Simulation\n\nProof-of-Concept Examples\n\n\nChallenges\n\nCitation\n\nReferences\n\nPlanning\n\nSubgoal and decomposition: The agent breaks down large tasks into smaller, manageable subgoals, enabling efficient handling of complex tasks.\nReflection and refinement: The agent can do self-criticism and self-reflection over past actions, learn from mistakes and refine them for future steps, thereby improving the quality of final results.\n\n\nMemory\n\nMemory\n\nShort-term memory: I would consider all the in-context learning (See Prompt Engineering) as utilizing short-term memory of the model to learn.\nLong-term memory: This provides the agent with the capability to retain and recall (infinite) information over extended periods, often by leveraging an external vector store and fast retrieval.\n\n\nTool use\n\nThe design of generative agents combines LLM with memory, planning and reflection mechanisms to enable agents to behave conditioned on past experience, as well as to interact with other agents.', name='retrieve_blog_posts', id='d815f283-868c-4660-a1c6-5f6e5373ca06', tool_call_id='call_z36oPZN8l1UC6raxrebqc1bH')]}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-10-11)'\n---\n'
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-10-12)---GENERATE---
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-10-13)"Output from node 'generate':"
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-10-14)'---'
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-10-15){ 'messages': [ 'Lilian Weng discusses short-term and long-term memory in '
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-10-16)        'agent systems. Short-term memory is used for in-context '
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-10-17)        'learning, while long-term memory allows agents to retain and '
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-10-18)        'recall information over extended periods.']}
[](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__codelineno-10-19)'\n---\n'

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Langgraph adaptive rag local  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/) [ Next  Corrective RAG (CRAG)  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
