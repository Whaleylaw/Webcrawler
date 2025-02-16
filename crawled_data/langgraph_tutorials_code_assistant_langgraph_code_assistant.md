---
url: https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#code-generation-with-rag-and-self-correction)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Code generation with RAG and self-correction 

[ ](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/?q= "Share")

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
        * Chatbots  Chatbots 
          * [ Chatbots  ](https://langchain-ai.github.io/langgraph/tutorials#chatbots)
          * [ Build a Customer Support Bot  ](https://langchain-ai.github.io/langgraph/tutorials/customer-support/customer-support/)
          * [ Prompt Generation from User Requirements  ](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/)
          * Code generation with RAG and self-correction  [ Code generation with RAG and self-correction  ](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/) Table of contents 
            * [ Setup  ](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#setup)
            * [ Docs  ](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#docs)
            * [ LLMs  ](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#llms)
              * [ Code solution  ](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#code-solution)
            * [ State  ](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#state)
            * [ Graph  ](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#graph)
            * [ Eval  ](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#eval)
        * [ RAG  ](https://langchain-ai.github.io/langgraph/tutorials#rag)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#setup)
  * [ Docs  ](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#docs)
  * [ LLMs  ](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#llms)
    * [ Code solution  ](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#code-solution)
  * [ State  ](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#state)
  * [ Graph  ](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#graph)
  * [ Eval  ](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#eval)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ Tutorials  ](https://langchain-ai.github.io/langgraph/tutorials/)
  4. [ Chatbots  ](https://langchain-ai.github.io/langgraph/tutorials#chatbots)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/tutorials/code_assistant/langgraph_code_assistant.ipynb "Edit this page")

# Code generation with RAG and self-correction[¶](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#code-generation-with-rag-and-self-correction "Permanent link")

AlphaCodium presented an approach for code generation that uses control flow.

Main idea: [construct an answer to a coding question iteratively.](https://x.com/karpathy/status/1748043513156272416?s=20). 

[AlphaCodium](https://github.com/Codium-ai/AlphaCodium) iteravely tests and improves an answer on public and AI-generated tests for a particular question. 

We will implement some of these ideas from scratch using [LangGraph](https://langchain-ai.github.io/langgraph/):

  1. We start with a set of documentation specified by a user
  2. We use a long context LLM to ingest it and perform RAG to answer a question based upon it
  3. We will invoke a tool to produce a structured output
  4. We will perform two unit tests (check imports and code execution) prior returning the solution to the user 



![Screenshot 2024-05-23 at 2.17.42 PM.png]()

## Setup[¶](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#setup "Permanent link")

First, let's install our required packages and set the API keys we will need

```
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-0-1)! pip install -U langchain_community langchain-openai langchain-anthropic langchain langgraph bs4

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-1-1)importgetpass
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-1-2)importos
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-1-5)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-1-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-1-7)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-1-8)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-1-10)_set_env("OPENAI_API_KEY")
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-1-11)_set_env("ANTHROPIC_API_KEY")

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Docs[¶](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#docs "Permanent link")

Load [LangChain Expression Language](https://python.langchain.com/docs/concepts/#langchain-expression-language-lcel) (LCEL) docs as an example.

```
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-2-1)frombs4import BeautifulSoup as Soup
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-2-2)fromlangchain_community.document_loaders.recursive_url_loaderimport RecursiveUrlLoader
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-2-3)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-2-4)# LCEL docs
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-2-5)url = "https://python.langchain.com/docs/concepts/lcel/"
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-2-6)loader = RecursiveUrlLoader(
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-2-7)  url=url, max_depth=20, extractor=lambda x: Soup(x, "html.parser").text
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-2-8))
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-2-9)docs = loader.load()
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-2-10)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-2-11)# Sort the list based on the URLs and get the text
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-2-12)d_sorted = sorted(docs, key=lambda x: x.metadata["source"])
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-2-13)d_reversed = list(reversed(d_sorted))
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-2-14)concatenated_content = "\n\n\n --- \n\n\n".join(
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-2-15)  [doc.page_content for doc in d_reversed]
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-2-16))

```


API Reference: [RecursiveUrlLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.recursive_url_loader.RecursiveUrlLoader.html)

## LLMs[¶](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#llms "Permanent link")

### Code solution[¶](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#code-solution "Permanent link")

First, we will try OpenAI and [Claude3](https://docs.anthropic.com/en/docs/about-claude/models) with function calling.

We will create a `code_gen_chain` w/ either OpenAI or Claude and test them here.

Using Pydantic with LangChain

This notebook uses Pydantic v2 `BaseModel`, which requires `langchain-core >= 0.3`. Using `langchain-core < 0.3` will result in errors due to mixing of Pydantic v1 and v2 `BaseModels`. 

```
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-3-1)fromlangchain_core.promptsimport ChatPromptTemplate
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-3-2)fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-3-3)frompydanticimport BaseModel, Field
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-3-4)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-3-5)### OpenAI
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-3-6)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-3-7)# Grader prompt
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-3-8)code_gen_prompt = ChatPromptTemplate.from_messages(
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-3-9)  [
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-3-10)    (
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-3-11)      "system",
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-3-12)"""You are a coding assistant with expertise in LCEL, LangChain expression language. \n 
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-3-13)  Here is a full set of LCEL documentation: \n ------- \n {context} \n ------- \n Answer the user 
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-3-14)  question based on the above provided documentation. Ensure any code you provide can be executed \n 
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-3-15)  with all required imports and variables defined. Structure your answer with a description of the code solution. \n
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-3-16)  Then list the imports. And finally list the functioning code block. Here is the user question:""",
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-3-17)    ),
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-3-18)    ("placeholder", "{messages}"),
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-3-19)  ]
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-3-20))
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-3-21)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-3-22)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-3-23)# Data model
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-3-24)classcode(BaseModel):
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-3-25)"""Schema for code solutions to questions about LCEL."""
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-3-26)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-3-27)  prefix: str = Field(description="Description of the problem and approach")
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-3-28)  imports: str = Field(description="Code block import statements")
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-3-29)  code: str = Field(description="Code block not including import statements")
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-3-30)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-3-31)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-3-32)expt_llm = "gpt-4o-mini"
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-3-33)llm = ChatOpenAI(temperature=0, model=expt_llm)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-3-34)code_gen_chain_oai = code_gen_prompt | llm.with_structured_output(code)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-3-35)question = "How do I build a RAG chain in LCEL?"
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-3-36)solution = code_gen_chain_oai.invoke(
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-3-37)  {"context": concatenated_content, "messages": [("user", question)]}
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-3-38))
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-3-39)solution

```


API Reference: [ChatPromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html) | [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html)

```
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-4-1)code(prefix='To build a Retrieval-Augmented Generation (RAG) chain in LCEL, you will need to set up a chain that combines a retriever and a language model (LLM). The retriever will fetch relevant documents based on a query, and the LLM will generate a response using the retrieved documents as context. Here’s how you can do it:', imports='from langchain_core.prompts import ChatPromptTemplate\nfrom langchain_openai import ChatOpenAI\nfrom langchain_core.output_parsers import StrOutputParser\nfrom langchain_core.retrievers import MyRetriever', code='# Define the retriever\nretriever = MyRetriever() # Replace with your specific retriever implementation\n\n# Define the LLM model\nmodel = ChatOpenAI(model="gpt-4")\n\n# Create a prompt template for the LLM\nprompt_template = ChatPromptTemplate.from_template("Given the following documents, answer the question: {question}\nDocuments: {documents}")\n\n# Create the RAG chain\nrag_chain = prompt_template | retriever | model | StrOutputParser()\n\n# Example usage\nquery = "What are the benefits of using RAG?"\nresponse = rag_chain.invoke({"question": query})\nprint(response)')

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-1)fromlangchain_anthropicimport ChatAnthropic
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-2)fromlangchain_core.promptsimport ChatPromptTemplate
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-3)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-4)### Anthropic
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-5)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-6)# Prompt to enforce tool use
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-7)code_gen_prompt_claude = ChatPromptTemplate.from_messages(
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-8)  [
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-9)    (
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-10)      "system",
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-11)"""<instructions> You are a coding assistant with expertise in LCEL, LangChain expression language. \n 
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-12)  Here is the LCEL documentation: \n ------- \n {context} \n ------- \n Answer the user question based on the \n 
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-13)  above provided documentation. Ensure any code you provide can be executed with all required imports and variables \n
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-14)  defined. Structure your answer: 1) a prefix describing the code solution, 2) the imports, 3) the functioning code block. \n
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-15)  Invoke the code tool to structure the output correctly. </instructions> \n Here is the user question:""",
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-16)    ),
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-17)    ("placeholder", "{messages}"),
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-18)  ]
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-19))
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-20)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-21)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-22)# LLM
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-23)expt_llm = "claude-3-opus-20240229"
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-24)llm = ChatAnthropic(
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-25)  model=expt_llm,
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-26)  default_headers={"anthropic-beta": "tools-2024-04-04"},
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-27))
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-28)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-29)structured_llm_claude = llm.with_structured_output(code, include_raw=True)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-30)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-31)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-32)# Optional: Check for errors in case tool use is flaky
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-33)defcheck_claude_output(tool_output):
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-34)"""Check for parse error or failure to call the tool"""
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-35)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-36)  # Error with parsing
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-37)  if tool_output["parsing_error"]:
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-38)    # Report back output and parsing errors
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-39)    print("Parsing error!")
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-40)    raw_output = str(tool_output["raw"].content)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-41)    error = tool_output["parsing_error"]
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-42)    raise ValueError(
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-43)      f"Error parsing your output! Be sure to invoke the tool. Output: {raw_output}. \n Parse error: {error}"
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-44)    )
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-45)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-46)  # Tool was not invoked
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-47)  elif not tool_output["parsed"]:
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-48)    print("Failed to invoke tool!")
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-49)    raise ValueError(
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-50)      "You did not use the provided tool! Be sure to invoke the tool to structure the output."
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-51)    )
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-52)  return tool_output
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-53)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-54)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-55)# Chain with output check
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-56)code_chain_claude_raw = (
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-57)  code_gen_prompt_claude | structured_llm_claude | check_claude_output
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-58))
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-59)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-60)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-61)definsert_errors(inputs):
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-62)"""Insert errors for tool parsing in the messages"""
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-63)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-64)  # Get errors
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-65)  error = inputs["error"]
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-66)  messages = inputs["messages"]
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-67)  messages += [
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-68)    (
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-69)      "assistant",
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-70)      f"Retry. You are required to fix the parsing errors: {error}\n\n You must invoke the provided tool.",
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-71)    )
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-72)  ]
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-73)  return {
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-74)    "messages": messages,
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-75)    "context": inputs["context"],
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-76)  }
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-77)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-78)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-79)# This will be run as a fallback chain
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-80)fallback_chain = insert_errors | code_chain_claude_raw
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-81)N = 3 # Max re-tries
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-82)code_gen_chain_re_try = code_chain_claude_raw.with_fallbacks(
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-83)  fallbacks=[fallback_chain] * N, exception_key="error"
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-84))
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-85)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-86)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-87)defparse_output(solution):
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-88)"""When we add 'include_raw=True' to structured output,
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-89)  it will return a dict w 'raw', 'parsed', 'parsing_error'."""
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-90)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-91)  return solution["parsed"]
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-92)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-93)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-94)# Optional: With re-try to correct for failure to invoke tool
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-95)code_gen_chain = code_gen_chain_re_try | parse_output
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-96)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-97)# No re-try
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-5-98)code_gen_chain = code_gen_prompt_claude | structured_llm_claude | parse_output

```


API Reference: [ChatAnthropic](https://python.langchain.com/api_reference/anthropic/chat_models/langchain_anthropic.chat_models.ChatAnthropic.html) | [ChatPromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html)

```
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-6-1)# Test
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-6-2)question = "How do I build a RAG chain in LCEL?"
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-6-3)solution = code_gen_chain.invoke(
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-6-4)  {"context": concatenated_content, "messages": [("user", question)]}
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-6-5))
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-6-6)solution

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-7-1)code(prefix="To build a RAG (Retrieval Augmented Generation) chain in LCEL, you can use a retriever to fetch relevant documents and then pass those documents to a chat model to generate a response based on the retrieved context. Here's an example of how to do this:", imports='from langchain_expressions import retrieve, chat_completion', code='question = "What is the capital of France?"\n\nrelevant_docs = retrieve(question)\n\nresult = chat_completion(\n  model=\'openai-gpt35\', \n  messages=[\n    {{{"role": "system", "content": "Answer the question based on the retrieved context.}}},\n    {{{"role": "user", "content": \'\'\'\n      Context: {relevant_docs}\n      Question: {question}\n    \'\'\'}}\n  ]\n)\n\nprint(result)')

```


## State[¶](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#state "Permanent link")

Our state is a dict that will contain keys (errors, question, code generation) relevant to code generation.

```
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-8-1)fromtypingimport List
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-8-2)fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-8-3)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-8-4)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-8-5)classGraphState(TypedDict):
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-8-6)"""
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-8-7)  Represents the state of our graph.
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-8-8)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-8-9)  Attributes:
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-8-10)    error : Binary flag for control flow to indicate whether test error was tripped
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-8-11)    messages : With user question, error messages, reasoning
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-8-12)    generation : Code solution
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-8-13)    iterations : Number of tries
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-8-14)  """
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-8-15)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-8-16)  error: str
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-8-17)  messages: List
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-8-18)  generation: str
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-8-19)  iterations: int

```


## Graph[¶](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#graph "Permanent link")

Our graph lays out the logical flow shown in the figure above.

```
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-1)### Parameter
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-2)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-3)# Max tries
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-4)max_iterations = 3
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-5)# Reflect
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-6)# flag = 'reflect'
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-7)flag = "do not reflect"
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-8)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-9)### Nodes
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-10)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-11)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-12)defgenerate(state: GraphState):
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-13)"""
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-14)  Generate a code solution
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-15)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-16)  Args:
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-17)    state (dict): The current graph state
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-18)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-19)  Returns:
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-20)    state (dict): New key added to state, generation
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-21)  """
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-22)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-23)  print("---GENERATING CODE SOLUTION---")
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-24)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-25)  # State
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-26)  messages = state["messages"]
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-27)  iterations = state["iterations"]
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-28)  error = state["error"]
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-29)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-30)  # We have been routed back to generation with an error
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-31)  if error == "yes":
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-32)    messages += [
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-33)      (
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-34)        "user",
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-35)        "Now, try again. Invoke the code tool to structure the output with a prefix, imports, and code block:",
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-36)      )
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-37)    ]
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-38)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-39)  # Solution
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-40)  code_solution = code_gen_chain.invoke(
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-41)    {"context": concatenated_content, "messages": messages}
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-42)  )
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-43)  messages += [
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-44)    (
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-45)      "assistant",
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-46)      f"{code_solution.prefix}\n Imports: {code_solution.imports}\n Code: {code_solution.code}",
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-47)    )
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-48)  ]
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-49)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-50)  # Increment
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-51)  iterations = iterations + 1
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-52)  return {"generation": code_solution, "messages": messages, "iterations": iterations}
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-53)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-54)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-55)defcode_check(state: GraphState):
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-56)"""
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-57)  Check code
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-58)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-59)  Args:
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-60)    state (dict): The current graph state
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-61)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-62)  Returns:
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-63)    state (dict): New key added to state, error
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-64)  """
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-65)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-66)  print("---CHECKING CODE---")
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-67)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-68)  # State
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-69)  messages = state["messages"]
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-70)  code_solution = state["generation"]
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-71)  iterations = state["iterations"]
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-72)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-73)  # Get solution components
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-74)  imports = code_solution.imports
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-75)  code = code_solution.code
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-76)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-77)  # Check imports
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-78)  try:
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-79)    exec(imports)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-80)  except Exception as e:
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-81)    print("---CODE IMPORT CHECK: FAILED---")
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-82)    error_message = [("user", f"Your solution failed the import test: {e}")]
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-83)    messages += error_message
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-84)    return {
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-85)      "generation": code_solution,
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-86)      "messages": messages,
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-87)      "iterations": iterations,
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-88)      "error": "yes",
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-89)    }
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-90)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-91)  # Check execution
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-92)  try:
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-93)    exec(imports + "\n" + code)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-94)  except Exception as e:
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-95)    print("---CODE BLOCK CHECK: FAILED---")
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-96)    error_message = [("user", f"Your solution failed the code execution test: {e}")]
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-97)    messages += error_message
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-98)    return {
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-99)      "generation": code_solution,
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-100)      "messages": messages,
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-101)      "iterations": iterations,
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-102)      "error": "yes",
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-103)    }
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-104)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-105)  # No errors
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-106)  print("---NO CODE TEST FAILURES---")
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-107)  return {
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-108)    "generation": code_solution,
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-109)    "messages": messages,
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-110)    "iterations": iterations,
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-111)    "error": "no",
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-112)  }
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-113)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-114)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-115)defreflect(state: GraphState):
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-116)"""
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-117)  Reflect on errors
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-118)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-119)  Args:
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-120)    state (dict): The current graph state
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-121)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-122)  Returns:
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-123)    state (dict): New key added to state, generation
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-124)  """
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-125)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-126)  print("---GENERATING CODE SOLUTION---")
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-127)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-128)  # State
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-129)  messages = state["messages"]
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-130)  iterations = state["iterations"]
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-131)  code_solution = state["generation"]
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-132)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-133)  # Prompt reflection
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-134)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-135)  # Add reflection
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-136)  reflections = code_gen_chain.invoke(
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-137)    {"context": concatenated_content, "messages": messages}
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-138)  )
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-139)  messages += [("assistant", f"Here are reflections on the error: {reflections}")]
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-140)  return {"generation": code_solution, "messages": messages, "iterations": iterations}
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-141)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-142)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-143)### Edges
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-144)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-145)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-146)defdecide_to_finish(state: GraphState):
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-147)"""
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-148)  Determines whether to finish.
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-149)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-150)  Args:
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-151)    state (dict): The current graph state
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-152)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-153)  Returns:
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-154)    str: Next node to call
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-155)  """
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-156)  error = state["error"]
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-157)  iterations = state["iterations"]
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-158)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-159)  if error == "no" or iterations == max_iterations:
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-160)    print("---DECISION: FINISH---")
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-161)    return "end"
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-162)  else:
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-163)    print("---DECISION: RE-TRY SOLUTION---")
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-164)    if flag == "reflect":
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-165)      return "reflect"
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-166)    else:
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-9-167)      return "generate"

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-10-1)fromlanggraph.graphimport END, StateGraph, START
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-10-2)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-10-3)workflow = StateGraph(GraphState)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-10-4)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-10-5)# Define the nodes
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-10-6)workflow.add_node("generate", generate) # generation solution
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-10-7)workflow.add_node("check_code", code_check) # check code
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-10-8)workflow.add_node("reflect", reflect) # reflect
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-10-9)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-10-10)# Build graph
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-10-11)workflow.add_edge(START, "generate")
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-10-12)workflow.add_edge("generate", "check_code")
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-10-13)workflow.add_conditional_edges(
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-10-14)  "check_code",
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-10-15)  decide_to_finish,
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-10-16)  {
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-10-17)    "end": END,
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-10-18)    "reflect": "reflect",
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-10-19)    "generate": "generate",
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-10-20)  },
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-10-21))
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-10-22)workflow.add_edge("reflect", "generate")
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-10-23)app = workflow.compile()

```


API Reference: [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START)

```
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-11-1)question = "How can I directly pass a string to a runnable and use it to construct the input needed for my prompt?"
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-11-2)solution = app.invoke({"messages": [("user", question)], "iterations": 0, "error": ""})

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-12-1)---GENERATING CODE SOLUTION---
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-12-2)---CHECKING CODE---
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-12-3)---CODE IMPORT CHECK: FAILED---
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-12-4)---DECISION: RE-TRY SOLUTION---
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-12-5)---GENERATING CODE SOLUTION---
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-12-6)---CHECKING CODE---
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-12-7)---CODE IMPORT CHECK: FAILED---
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-12-8)---DECISION: RE-TRY SOLUTION---
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-12-9)---GENERATING CODE SOLUTION---
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-12-10)---CHECKING CODE---
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-12-11)---CODE BLOCK CHECK: FAILED---
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-12-12)---DECISION: FINISH---

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-13-1)solution["generation"]

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-14-1)code(prefix='To directly pass a string to a runnable and use it to construct the input needed for a prompt, you can use the `_from_value` method on a PromptTemplate in LCEL. Create a PromptTemplate with the desired template string, then call `_from_value` on it with a dictionary mapping the input variable names to their values. This will return a PromptValue that you can pass directly to any chain or model that accepts a prompt input.', imports='from langchain_core.prompts import PromptTemplate', code='user_string = "langchain is awesome"\n\nprompt_template = PromptTemplate.from_template("Tell me more about how {user_input}.")\n\nprompt_value = prompt_template._from_value({"user_input": user_string})\n\n# Pass the PromptValue directly to a model or chain \nchain.run(prompt_value)')

```


## Eval[¶](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#eval "Permanent link")

[Here](https://smith.langchain.com/public/326674a6-62bd-462d-88ae-eea49d503f9d/d) is a public dataset of LCEL questions. 

I saved this as `lcel-teacher-eval`.

You can also find the csv [here](https://github.com/langchain-ai/lcel-teacher/blob/main/eval/eval.csv).

```
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-15-1)importlangsmith
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-15-2)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-15-3)client = langsmith.Client()

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-16-1)# Clone the dataset to your tenant to use it
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-16-2)try:
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-16-3)  public_dataset = (
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-16-4)    "https://smith.langchain.com/public/326674a6-62bd-462d-88ae-eea49d503f9d/d"
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-16-5)  )
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-16-6)  client.clone_public_dataset(public_dataset)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-16-7)except:
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-16-8)  print("Please setup LangSmith")

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-17-1)Dataset(name='lcel-teacher-eval', description='Eval set for LCEL teacher', data_type=<DataType.kv: 'kv'>, id=UUID('8b57696d-14ea-4f00-9997-b3fc74a16846'), created_at=datetime.datetime(2024, 9, 16, 22, 50, 4, 169288, tzinfo=datetime.timezone.utc), modified_at=datetime.datetime(2024, 9, 16, 22, 50, 4, 169288, tzinfo=datetime.timezone.utc), example_count=0, session_count=0, last_session_start_time=None, inputs_schema=None, outputs_schema=None)

```


Custom evals.

```
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-18-1)fromlangsmith.schemasimport Example, Run
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-18-2)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-18-3)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-18-4)defcheck_import(run: Run, example: Example) -> dict:
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-18-5)  imports = run.outputs.get("imports")
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-18-6)  try:
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-18-7)    exec(imports)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-18-8)    return {"key": "import_check", "score": 1}
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-18-9)  except Exception:
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-18-10)    return {"key": "import_check", "score": 0}
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-18-11)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-18-12)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-18-13)defcheck_execution(run: Run, example: Example) -> dict:
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-18-14)  imports = run.outputs.get("imports")
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-18-15)  code = run.outputs.get("code")
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-18-16)  try:
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-18-17)    exec(imports + "\n" + code)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-18-18)    return {"key": "code_execution_check", "score": 1}
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-18-19)  except Exception:
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-18-20)    return {"key": "code_execution_check", "score": 0}

```


Compare LangGraph to Context Stuffing.

```
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-19-1)defpredict_base_case(example: dict):
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-19-2)"""Context stuffing"""
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-19-3)  solution = code_gen_chain.invoke(
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-19-4)    {"context": concatenated_content, "messages": [("user", example["question"])]}
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-19-5)  )
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-19-6)  return {"imports": solution.imports, "code": solution.code}
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-19-7)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-19-8)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-19-9)defpredict_langgraph(example: dict):
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-19-10)"""LangGraph"""
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-19-11)  graph = app.invoke(
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-19-12)    {"messages": [("user", example["question"])], "iterations": 0, "error": ""}
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-19-13)  )
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-19-14)  solution = graph["generation"]
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-19-15)  return {"imports": solution.imports, "code": solution.code}

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-20-1)fromlangsmith.evaluationimport evaluate
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-20-2)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-20-3)# Evaluator
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-20-4)code_evalulator = [check_import, check_execution]
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-20-5)
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-20-6)# Dataset
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-20-7)dataset_name = "lcel-teacher-eval"

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-21-1)# Run base case
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-21-2)try:
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-21-3)  experiment_results_ = evaluate(
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-21-4)    predict_base_case,
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-21-5)    data=dataset_name,
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-21-6)    evaluators=code_evalulator,
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-21-7)    experiment_prefix=f"test-without-langgraph-{expt_llm}",
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-21-8)    max_concurrency=2,
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-21-9)    metadata={
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-21-10)      "llm": expt_llm,
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-21-11)    },
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-21-12)  )
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-21-13)except:
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-21-14)  print("Please setup LangSmith")

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-22-1)# Run with langgraph
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-22-2)try:
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-22-3)  experiment_results = evaluate(
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-22-4)    predict_langgraph,
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-22-5)    data=dataset_name,
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-22-6)    evaluators=code_evalulator,
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-22-7)    experiment_prefix=f"test-with-langgraph-{expt_llm}-{flag}",
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-22-8)    max_concurrency=2,
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-22-9)    metadata={
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-22-10)      "llm": expt_llm,
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-22-11)      "feedback": flag,
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-22-12)    },
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-22-13)  )
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-22-14)except:
[](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__codelineno-22-15)  print("Please setup LangSmith")

```


`Results:`

  * `LangGraph outperforms base case`: adding re-try loop improve performance
  * `Reflection did not help`: reflection prior to re-try regression vs just passing errors directly back to the LLM
  * `GPT-4 outperforms Claude3`: Claude3 had 3 and 1 run fail due to tool-use error for Opus and Haiku, respectively



<https://smith.langchain.com/public/78a3d858-c811-4e46-91cb-0f10ef56260b/d>

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Prompt Generation from User Requirements  ](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/) [ Next  Adaptive RAG  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
