---
url: https://langchain-ai.github.io/langgraph/how-tos/many-tools/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#how-to-handle-large-numbers-of-tools)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to handle large numbers of tools 

[ ](https://langchain-ai.github.io/langgraph/how-tos/many-tools/?q= "Share")

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

How-to Guides 
        * LangGraph  LangGraph 
          * [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
          * [ Graph API Basics  ](https://langchain-ai.github.io/langgraph/how-tos#graph-api-basics)
          * [ Controllability  ](https://langchain-ai.github.io/langgraph/how-tos#controllability)
          * [ Persistence  ](https://langchain-ai.github.io/langgraph/how-tos#persistence)
          * [ Memory  ](https://langchain-ai.github.io/langgraph/how-tos#memory)
          * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraph/how-tos#human-in-the-loop)
          * [ Streaming  ](https://langchain-ai.github.io/langgraph/how-tos#streaming)
          * Tool calling  Tool calling 
            * [ Tool calling  ](https://langchain-ai.github.io/langgraph/how-tos#tool-calling)
            * [ How to call tools using ToolNode  ](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/)
            * [ How to handle tool calling errors  ](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors/)
            * [ How to pass runtime values to tools  ](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/)
            * [ How to update graph state from tools  ](https://langchain-ai.github.io/langgraph/how-tos/update-state-from-tools/)
            * [ How to pass config to tools  ](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/)
            * How to handle large numbers of tools  [ How to handle large numbers of tools  ](https://langchain-ai.github.io/langgraph/how-tos/many-tools/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#setup)
              * [ Define the tools  ](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#define-the-tools)
              * [ Define the graph  ](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#define-the-graph)
                * [ Tool selection  ](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#tool-selection)
                * [ Incorporating with an agent  ](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#incorporating-with-an-agent)
              * [ Repeating tool selection  ](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#repeating-tool-selection)
              * [ Next steps  ](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#next-steps)
          * [ Subgraphs  ](https://langchain-ai.github.io/langgraph/how-tos#subgraphs)
          * [ Multi-agent  ](https://langchain-ai.github.io/langgraph/how-tos#multi-agent)
          * [ State Management  ](https://langchain-ai.github.io/langgraph/how-tos#state-management)
          * [ Other  ](https://langchain-ai.github.io/langgraph/how-tos#other)
          * [ Prebuilt ReAct Agent  ](https://langchain-ai.github.io/langgraph/how-tos#prebuilt-react-agent)
        * [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph-platform)
      * [ Concepts  ](https://langchain-ai.github.io/langgraph/concepts/)
      * [ Tutorials  ](https://langchain-ai.github.io/langgraph/tutorials/)
    * Resources  Resources 
      * [ Prebuilt Agents  ](https://langchain-ai.github.io/langgraph/prebuilt/)
      * [ Adopters  ](https://langchain-ai.github.io/langgraph/adopters/)
      * [ FAQ  ](https://langchain-ai.github.io/langgraph/concepts/faq/)
      * [ Troubleshooting  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraph/reference/graphs/)



Table of contents 

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#setup)
  * [ Define the tools  ](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#define-the-tools)
  * [ Define the graph  ](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#define-the-graph)
    * [ Tool selection  ](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#tool-selection)
    * [ Incorporating with an agent  ](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#incorporating-with-an-agent)
  * [ Repeating tool selection  ](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#repeating-tool-selection)
  * [ Next steps  ](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#next-steps)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
  5. [ Tool calling  ](https://langchain-ai.github.io/langgraph/how-tos#tool-calling)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/many-tools.ipynb "Edit this page")

# How to handle large numbers of tools[¶](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#how-to-handle-large-numbers-of-tools "Permanent link")

Prerequisites

This guide assumes familiarity with the following: 

  * [ Tools ](https://python.langchain.com/docs/concepts/#tools)
  * [ Chat Models ](https://python.langchain.com/docs/concepts/#chat-models/)
  * [ Embedding Models ](https://python.langchain.com/docs/concepts/#embedding-models)
  * [ Vectorstores ](https://python.langchain.com/docs/concepts/#vector-stores)
  * [ Document ](https://python.langchain.com/docs/concepts/#documents)



The subset of available tools to call is generally at the discretion of the model (although many providers also enable the user to [specify or constrain the choice of tool](https://python.langchain.com/docs/how_to/tool_choice/)). As the number of available tools grows, you may want to limit the scope of the LLM's selection, to decrease token consumption and to help manage sources of error in LLM reasoning.

Here we will demonstrate how to dynamically adjust the tools available to a model. Bottom line up front: like [RAG](https://python.langchain.com/docs/concepts/#retrieval) and similar methods, we prefix the model invocation by retrieving over available tools. Although we demonstrate one implementation that searches over tool descriptions, the details of the tool selection can be customized as needed.

## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#setup "Permanent link")

First, let's install the required packages and set our API keys

```
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-0-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-0-2)%pip install --quiet -U langgraph langchain_openai numpy

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-1-1)importgetpass
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-1-2)importos
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-1-5)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-1-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-1-7)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-1-8)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-1-10)_set_env("OPENAI_API_KEY")

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Define the tools[¶](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#define-the-tools "Permanent link")

Let's consider a toy example in which we have one tool for each publicly traded company in the [S&P 500 index](https://en.wikipedia.org/wiki/S%26P_500). Each tool fetches company-specific information based on the year provided as a parameter.

We first construct a registry that associates a unique identifier with a schema for each tool. We will represent the tools using JSON schema, which can be bound directly to chat models supporting tool calling.

```
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-2-1)importre
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-2-2)importuuid
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-2-3)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-2-4)fromlangchain_core.toolsimport StructuredTool
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-2-5)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-2-6)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-2-7)defcreate_tool(company: str) -> dict:
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-2-8)"""Create schema for a placeholder tool."""
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-2-9)  # Remove non-alphanumeric characters and replace spaces with underscores for the tool name
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-2-10)  formatted_company = re.sub(r"[^\w\s]", "", company).replace(" ", "_")
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-2-11)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-2-12)  defcompany_tool(year: int) -> str:
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-2-13)    # Placeholder function returning static revenue information for the company and year
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-2-14)    return f"{company} had revenues of $100 in {year}."
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-2-15)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-2-16)  return StructuredTool.from_function(
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-2-17)    company_tool,
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-2-18)    name=formatted_company,
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-2-19)    description=f"Information about {company}",
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-2-20)  )
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-2-21)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-2-22)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-2-23)# Abbreviated list of S&P 500 companies for demonstration
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-2-24)s_and_p_500_companies = [
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-2-25)  "3M",
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-2-26)  "A.O. Smith",
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-2-27)  "Abbott",
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-2-28)  "Accenture",
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-2-29)  "Advanced Micro Devices",
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-2-30)  "Yum! Brands",
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-2-31)  "Zebra Technologies",
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-2-32)  "Zimmer Biomet",
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-2-33)  "Zoetis",
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-2-34)]
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-2-35)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-2-36)# Create a tool for each company and store it in a registry with a unique UUID as the key
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-2-37)tool_registry = {
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-2-38)  str(uuid.uuid4()): create_tool(company) for company in s_and_p_500_companies
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-2-39)}

```


API Reference: [StructuredTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.structured.StructuredTool.html)

## Define the graph[¶](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#define-the-graph "Permanent link")

### Tool selection[¶](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#tool-selection "Permanent link")

We will construct a node that retrieves a subset of available tools given the information in the state-- such as a recent user message. In general, the full scope of [retrieval solutions](https://python.langchain.com/docs/concepts/#retrieval) are available for this step. As a simple solution, we index embeddings of tool descriptions in a vector store, and associate user queries to tools via semantic search.

```
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-3-1)fromlangchain_core.documentsimport Document
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-3-2)fromlangchain_core.vectorstoresimport InMemoryVectorStore
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-3-3)fromlangchain_openaiimport OpenAIEmbeddings
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-3-4)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-3-5)tool_documents = [
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-3-6)  Document(
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-3-7)    page_content=tool.description,
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-3-8)    id=id,
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-3-9)    metadata={"tool_name": tool.name},
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-3-10)  )
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-3-11)  for id, tool in tool_registry.items()
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-3-12)]
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-3-13)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-3-14)vector_store = InMemoryVectorStore(embedding=OpenAIEmbeddings())
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-3-15)document_ids = vector_store.add_documents(tool_documents)

```


API Reference: [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html) | [InMemoryVectorStore](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.in_memory.InMemoryVectorStore.html) | [OpenAIEmbeddings](https://python.langchain.com/api_reference/openai/embeddings/langchain_openai.embeddings.base.OpenAIEmbeddings.html)

### Incorporating with an agent[¶](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#incorporating-with-an-agent "Permanent link")

We will use a typical React agent graph (e.g., as used in the [quickstart](https://langchain-ai.github.io/langgraph/tutorials/introduction/#part-2-enhancing-the-chatbot-with-tools)), with some modifications:

  * We add a `selected_tools` key to the state, which stores our selected subset of tools;
  * We set the entry point of the graph to be a `select_tools` node, which populates this element of the state;
  * We bind the selected subset of tools to the chat model within the `agent` node.



```
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-1)fromtypingimport Annotated
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-2)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-3)fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-4)fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-5)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-6)fromlanggraph.graphimport StateGraph, START
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-7)fromlanggraph.graph.messageimport add_messages
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-8)fromlanggraph.prebuiltimport ToolNode, tools_condition
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-9)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-10)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-11)# Define the state structure using TypedDict.
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-12)# It includes a list of messages (processed by add_messages)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-13)# and a list of selected tool IDs.
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-14)classState(TypedDict):
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-15)  messages: Annotated[list, add_messages]
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-16)  selected_tools: list[str]
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-17)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-18)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-19)builder = StateGraph(State)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-20)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-21)# Retrieve all available tools from the tool registry.
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-22)tools = list(tool_registry.values())
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-23)llm = ChatOpenAI()
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-24)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-25)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-26)# The agent function processes the current state
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-27)# by binding selected tools to the LLM.
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-28)defagent(state: State):
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-29)  # Map tool IDs to actual tools
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-30)  # based on the state's selected_tools list.
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-31)  selected_tools = [tool_registry[id] for id in state["selected_tools"]]
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-32)  # Bind the selected tools to the LLM for the current interaction.
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-33)  llm_with_tools = llm.bind_tools(selected_tools)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-34)  # Invoke the LLM with the current messages and return the updated message list.
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-35)  return {"messages": [llm_with_tools.invoke(state["messages"])]}
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-36)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-37)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-38)# The select_tools function selects tools based on the user's last message content.
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-39)defselect_tools(state: State):
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-40)  last_user_message = state["messages"][-1]
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-41)  query = last_user_message.content
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-42)  tool_documents = vector_store.similarity_search(query)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-43)  return {"selected_tools": [document.id for document in tool_documents]}
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-44)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-45)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-46)builder.add_node("agent", agent)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-47)builder.add_node("select_tools", select_tools)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-48)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-49)tool_node = ToolNode(tools=tools)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-50)builder.add_node("tools", tool_node)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-51)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-52)builder.add_conditional_edges("agent", tools_condition, path_map=["tools", "__end__"])
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-53)builder.add_edge("tools", "agent")
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-54)builder.add_edge("select_tools", "agent")
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-55)builder.add_edge(START, "select_tools")
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-4-56)graph = builder.compile()

```


API Reference: [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [add_messages](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.message.add_messages) | [ToolNode](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.ToolNode) | [tools_condition](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.tools_condition)

```
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-5-1)fromIPython.displayimport Image, display
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-5-2)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-5-3)try:
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-5-4)  display(Image(graph.get_graph().draw_mermaid_png()))
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-5-5)except Exception:
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-5-6)  # This requires some extra dependencies and is optional
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-5-7)  pass

```


![]()

```
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-6-1)user_input = "Can you give me some information about AMD in 2022?"
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-6-2)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-6-3)result = graph.invoke({"messages": [("user", user_input)]})

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-7-1)print(result["selected_tools"])

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-8-1)['ab9c0d59-3d16-448d-910c-73cf10a26020', 'f5eff8f6-7fb9-47b6-b54f-19872a52db84', '2962e168-9ef4-48dc-8b7c-9227e7956d39', '24a9fb82-19fe-4a88-944e-47bc4032e94a']

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-9-1)for message in result["messages"]:
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-9-2)  message.pretty_print()

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-10-1)================================[1m Human Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-10-2)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-10-3)Can you give me some information about AMD in 2022?
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-10-4)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-10-5)Tool Calls:
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-10-6) Advanced_Micro_Devices (call_CRxQ0oT7NY7lqf35DaRNTJ35)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-10-7) Call ID: call_CRxQ0oT7NY7lqf35DaRNTJ35
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-10-8) Args:
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-10-9)  year: 2022
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-10-10)=================================[1m Tool Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-10-11)Name: Advanced_Micro_Devices
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-10-12)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-10-13)Advanced Micro Devices had revenues of $100 in 2022.
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-10-14)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-10-15)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-10-16)In 2022, Advanced Micro Devices (AMD) had revenues of $100.

```


## Repeating tool selection[¶](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#repeating-tool-selection "Permanent link")

To manage errors from incorrect tool selection, we could revisit the `select_tools` node. One option for implementing this is to modify `select_tools` to generate the vector store query using all messages in the state (e.g., with a chat model) and add an edge routing from `tools` to `select_tools`.

We implement this change below. For demonstration purposes, we simulate an error in the initial tool selection by adding a `hack_remove_tool_condition` to the `select_tools` node, which removes the correct tool on the first iteration of the node. Note that on the second iteration, the agent finishes the run as it has access to the correct tool.

Using Pydantic with LangChain

This notebook uses Pydantic v2 `BaseModel`, which requires `langchain-core >= 0.3`. Using `langchain-core < 0.3` will result in errors due to mixing of Pydantic v1 and v2 `BaseModels`. 

```
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-1)fromlangchain_core.messagesimport HumanMessage, SystemMessage, ToolMessage
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-2)fromlanggraph.pregel.retryimport RetryPolicy
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-3)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-4)frompydanticimport BaseModel, Field
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-5)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-6)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-7)classQueryForTools(BaseModel):
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-8)"""Generate a query for additional tools."""
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-9)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-10)  query: str = Field(..., description="Query for additional tools.")
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-11)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-12)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-13)defselect_tools(state: State):
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-14)"""Selects tools based on the last message in the conversation state.
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-15)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-16)  If the last message is from a human, directly uses the content of the message
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-17)  as the query. Otherwise, constructs a query using a system message and invokes
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-18)  the LLM to generate tool suggestions.
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-19)  """
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-20)  last_message = state["messages"][-1]
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-21)  hack_remove_tool_condition = False # Simulate an error in the first tool selection
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-22)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-23)  if isinstance(last_message, HumanMessage):
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-24)    query = last_message.content
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-25)    hack_remove_tool_condition = True # Simulate wrong tool selection
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-26)  else:
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-27)    assert isinstance(last_message, ToolMessage)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-28)    system = SystemMessage(
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-29)      "Given this conversation, generate a query for additional tools. "
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-30)      "The query should be a short string containing what type of information "
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-31)      "is needed. If no further information is needed, "
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-32)      "set more_information_needed False and populate a blank string for the query."
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-33)    )
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-34)    input_messages = [system] + state["messages"]
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-35)    response = llm.bind_tools([QueryForTools], tool_choice=True).invoke(
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-36)      input_messages
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-37)    )
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-38)    query = response.tool_calls[0]["args"]["query"]
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-39)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-40)  # Search the tool vector store using the generated query
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-41)  tool_documents = vector_store.similarity_search(query)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-42)  if hack_remove_tool_condition:
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-43)    # Simulate error by removing the correct tool from the selection
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-44)    selected_tools = [
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-45)      document.id
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-46)      for document in tool_documents
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-47)      if document.metadata["tool_name"] != "Advanced_Micro_Devices"
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-48)    ]
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-49)  else:
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-50)    selected_tools = [document.id for document in tool_documents]
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-51)  return {"selected_tools": selected_tools}
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-52)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-53)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-54)graph_builder = StateGraph(State)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-55)graph_builder.add_node("agent", agent)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-56)graph_builder.add_node("select_tools", select_tools, retry=RetryPolicy(max_attempts=3))
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-57)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-58)tool_node = ToolNode(tools=tools)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-59)graph_builder.add_node("tools", tool_node)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-60)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-61)graph_builder.add_conditional_edges(
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-62)  "agent",
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-63)  tools_condition,
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-64))
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-65)graph_builder.add_edge("tools", "select_tools")
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-66)graph_builder.add_edge("select_tools", "agent")
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-67)graph_builder.add_edge(START, "select_tools")
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-11-68)graph = graph_builder.compile()

```


API Reference: [HumanMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.human.HumanMessage.html) | [SystemMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.system.SystemMessage.html) | [ToolMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.tool.ToolMessage.html)

```
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-12-1)fromIPython.displayimport Image, display
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-12-2)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-12-3)try:
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-12-4)  display(Image(graph.get_graph().draw_mermaid_png()))
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-12-5)except Exception:
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-12-6)  # This requires some extra dependencies and is optional
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-12-7)  pass

```


![]()

```
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-13-1)user_input = "Can you give me some information about AMD in 2022?"
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-13-2)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-13-3)result = graph.invoke({"messages": [("user", user_input)]})

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-14-1)for message in result["messages"]:
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-14-2)  message.pretty_print()

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-15-1)================================[1m Human Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-15-2)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-15-3)Can you give me some information about AMD in 2022?
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-15-4)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-15-5)Tool Calls:
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-15-6) Accenture (call_qGmwFnENwwzHOYJXiCAaY5Mx)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-15-7) Call ID: call_qGmwFnENwwzHOYJXiCAaY5Mx
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-15-8) Args:
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-15-9)  year: 2022
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-15-10)=================================[1m Tool Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-15-11)Name: Accenture
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-15-12)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-15-13)Accenture had revenues of $100 in 2022.
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-15-14)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-15-15)Tool Calls:
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-15-16) Advanced_Micro_Devices (call_u9e5UIJtiieXVYi7Y9GgyDpn)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-15-17) Call ID: call_u9e5UIJtiieXVYi7Y9GgyDpn
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-15-18) Args:
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-15-19)  year: 2022
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-15-20)=================================[1m Tool Message [0m=================================
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-15-21)Name: Advanced_Micro_Devices
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-15-22)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-15-23)Advanced Micro Devices had revenues of $100 in 2022.
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-15-24)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-15-25)
[](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__codelineno-15-26)In 2022, AMD had revenues of $100.

```


## Next steps[¶](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#next-steps "Permanent link")

This guide provides a minimal implementation for dynamically selecting tools. There is a host of possible improvements and optimizations:

  * **Repeating tool selection** : Here, we repeated tool selection by modifying the `select_tools` node. Another option is to equip the agent with a `reselect_tools` tool, allowing it to re-select tools at its discretion.
  * **Optimizing tool selection** : In general, the full scope of [retrieval solutions](https://python.langchain.com/docs/concepts/#retrieval) are available for tool selection. Additional options include:
  * Group tools and retrieve over groups;
  * Use a chat model to select tools or groups of tool.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to pass config to tools  ](https://langchain-ai.github.io/langgraph/how-tos/pass-config-to-tools/) [ Next  How to use subgraphs  ](https://langchain-ai.github.io/langgraph/how-tos/subgraph/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/many-tools/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
