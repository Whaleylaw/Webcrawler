---
url: https://langchain-ai.github.io/langgraph/tutorials/sql-agent/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#an-agent-for-interacting-with-a-sql-database)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

An agent for interacting with a SQL database 

[ ](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/?q= "Share")

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
          * [ Self-RAG  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/)
          * [ Self-RAG using local LLMs  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/)
          * An agent for interacting with a SQL database  [ An agent for interacting with a SQL database  ](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/) Table of contents 
            * [ Setup  ](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#setup)
            * [ Configure the database  ](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#configure-the-database)
            * [ Utility functions  ](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#utility-functions)
            * [ Define tools for the agent  ](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#define-tools-for-the-agent)
            * [ Define the workflow  ](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#define-the-workflow)
            * [ Visualize the graph  ](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#visualize-the-graph)
            * [ Run the agent  ](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#run-the-agent)
            * [ Eval  ](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#eval)
              * [ Response  ](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#response)
              * [ Trajectory  ](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#trajectory)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#setup)
  * [ Configure the database  ](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#configure-the-database)
  * [ Utility functions  ](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#utility-functions)
  * [ Define tools for the agent  ](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#define-tools-for-the-agent)
  * [ Define the workflow  ](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#define-the-workflow)
  * [ Visualize the graph  ](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#visualize-the-graph)
  * [ Run the agent  ](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#run-the-agent)
  * [ Eval  ](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#eval)
    * [ Response  ](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#response)
    * [ Trajectory  ](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#trajectory)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ Tutorials  ](https://langchain-ai.github.io/langgraph/tutorials/)
  4. [ RAG  ](https://langchain-ai.github.io/langgraph/tutorials#rag)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/tutorials/sql-agent.ipynb "Edit this page")

# An agent for interacting with a SQL database[¶](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#an-agent-for-interacting-with-a-sql-database "Permanent link")

In this tutorial, we will walk through how to build an agent that can answer questions about a SQL database. 

At a high level, the agent will: 1. Fetch the available tables from the database 2. Decide which tables are relevant to the question 3. Fetch the DDL for the relevant tables 4. Generate a query based on the question and information from the DDL 5. Double-check the query for common mistakes using an LLM 6. Execute the query and return the results 7. Correct mistakes surfaced by the database engine until the query is successful 8. Formulate a response based on the results

The end-to-end workflow will look something like below:

![sql-agent-diagram.png]()

## Setup[¶](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#setup "Permanent link")

First let's install our required packages and set our API keys

```
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-0-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-0-2)%pip install -U langgraph langchain_openai langchain_community

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-1-1)importgetpass
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-1-2)importos
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-1-5)def_set_env(key: str):
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-1-6)  if key not in os.environ:
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-1-7)    os.environ[key] = getpass.getpass(f"{key}:")
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-1-8)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-1-10)_set_env("OPENAI_API_KEY")

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Configure the database[¶](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#configure-the-database "Permanent link")

We will be creating a SQLite database for this tutorial. SQLite is a lightweight database that is easy to set up and use. We will be loading the `chinook` database, which is a sample database that represents a digital media store. Find more information about the database [here](https://www.sqlitetutorial.net/sqlite-sample-database/).

For convenience, we have hosted the database (`Chinook.db`) on a public GCS bucket.

```
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-2-1)importrequests
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-2-2)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-2-3)url = "https://storage.googleapis.com/benchmarks-artifacts/chinook/Chinook.db"
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-2-4)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-2-5)response = requests.get(url)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-2-6)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-2-7)if response.status_code == 200:
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-2-8)  # Open a local file in binary write mode
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-2-9)  with open("Chinook.db", "wb") as file:
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-2-10)    # Write the content of the response (the file) to the local file
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-2-11)    file.write(response.content)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-2-12)  print("File downloaded and saved as Chinook.db")
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-2-13)else:
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-2-14)  print(f"Failed to download the file. Status code: {response.status_code}")

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-3-1)File downloaded and saved as Chinook.db

```


We will use a handy SQL database wrapper available in the `langchain_community` package to interact with the database. The wrapper provides a simple interface to execute SQL queries and fetch results. We will also use the `langchain_openai` package to interact with the OpenAI API for language models later in the tutorial. 

```
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-4-1)%%capture --no-stderr --no-display
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-4-2)!pip install langgraph langchain_community langchain_openai

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-5-1)fromlangchain_community.utilitiesimport SQLDatabase
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-5-2)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-5-3)db = SQLDatabase.from_uri("sqlite:///Chinook.db")
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-5-4)print(db.dialect)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-5-5)print(db.get_usable_table_names())
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-5-6)db.run("SELECT * FROM Artist LIMIT 10;")

```


API Reference: [SQLDatabase](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html)

```
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-6-1)sqlite
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-6-2)['Album', 'Artist', 'Customer', 'Employee', 'Genre', 'Invoice', 'InvoiceLine', 'MediaType', 'Playlist', 'PlaylistTrack', 'Track']

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-7-1)"[(1, 'AC/DC'), (2, 'Accept'), (3, 'Aerosmith'), (4, 'Alanis Morissette'), (5, 'Alice In Chains'), (6, 'Antônio Carlos Jobim'), (7, 'Apocalyptica'), (8, 'Audioslave'), (9, 'BackBeat'), (10, 'Billy Cobham')]"

```


## Utility functions[¶](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#utility-functions "Permanent link")

We will define a few utility functions to help us with the agent implementation. Specifically, we will wrap a `ToolNode` with a fallback to handle errors and surface them to the agent.

```
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-8-1)fromtypingimport Any
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-8-2)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-8-3)fromlangchain_core.messagesimport ToolMessage
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-8-4)fromlangchain_core.runnablesimport RunnableLambda, RunnableWithFallbacks
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-8-5)fromlanggraph.prebuiltimport ToolNode
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-8-6)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-8-7)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-8-8)defcreate_tool_node_with_fallback(tools: list) -> RunnableWithFallbacks[Any, dict]:
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-8-9)"""
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-8-10)  Create a ToolNode with a fallback to handle errors and surface them to the agent.
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-8-11)  """
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-8-12)  return ToolNode(tools).with_fallbacks(
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-8-13)    [RunnableLambda(handle_tool_error)], exception_key="error"
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-8-14)  )
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-8-15)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-8-16)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-8-17)defhandle_tool_error(state) -> dict:
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-8-18)  error = state.get("error")
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-8-19)  tool_calls = state["messages"][-1].tool_calls
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-8-20)  return {
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-8-21)    "messages": [
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-8-22)      ToolMessage(
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-8-23)        content=f"Error: {repr(error)}\n please fix your mistakes.",
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-8-24)        tool_call_id=tc["id"],
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-8-25)      )
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-8-26)      for tc in tool_calls
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-8-27)    ]
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-8-28)  }

```


API Reference: [ToolMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.tool.ToolMessage.html) | [RunnableLambda](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.RunnableLambda.html) | [RunnableWithFallbacks](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.fallbacks.RunnableWithFallbacks.html) | [ToolNode](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.ToolNode)

## Define tools for the agent[¶](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#define-tools-for-the-agent "Permanent link")

We will define a few tools that the agent will use to interact with the database.

  1. `list_tables_tool`: Fetch the available tables from the database
  2. `get_schema_tool`: Fetch the DDL for a table
  3. `db_query_tool`: Execute the query and fetch the results OR return an error message if the query fails



For the first two tools, we will grab them from the `SQLDatabaseToolkit`, also available in the `langchain_community` package.

```
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-9-1)fromlangchain_community.agent_toolkitsimport SQLDatabaseToolkit
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-9-2)fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-9-3)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-9-4)toolkit = SQLDatabaseToolkit(db=db, llm=ChatOpenAI(model="gpt-4o"))
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-9-5)tools = toolkit.get_tools()
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-9-6)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-9-7)list_tables_tool = next(tool for tool in tools if tool.name == "sql_db_list_tables")
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-9-8)get_schema_tool = next(tool for tool in tools if tool.name == "sql_db_schema")
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-9-9)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-9-10)print(list_tables_tool.invoke(""))
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-9-11)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-9-12)print(get_schema_tool.invoke("Artist"))

```


API Reference: [SQLDatabaseToolkit](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.sql.toolkit.SQLDatabaseToolkit.html) | [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html)

```
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-10-1)Album, Artist, Customer, Employee, Genre, Invoice, InvoiceLine, MediaType, Playlist, PlaylistTrack, Track
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-10-2)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-10-3)CREATE TABLE "Artist" (
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-10-4)  "ArtistId" INTEGER NOT NULL, 
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-10-5)  "Name" NVARCHAR(120), 
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-10-6)  PRIMARY KEY ("ArtistId")
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-10-7))
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-10-8)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-10-9)/*
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-10-10)3 rows from Artist table:
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-10-11)ArtistId  Name
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-10-12)1  AC/DC
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-10-13)2  Accept
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-10-14)3  Aerosmith
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-10-15)*/

```


The third will be defined manually. For the `db_query_tool`, we will execute the query against the database and return the results. 

```
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-11-1)fromlangchain_core.toolsimport tool
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-11-2)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-11-3)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-11-4)@tool
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-11-5)defdb_query_tool(query: str) -> str:
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-11-6)"""
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-11-7)  Execute a SQL query against the database and get back the result.
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-11-8)  If the query is not correct, an error message will be returned.
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-11-9)  If an error is returned, rewrite the query, check the query, and try again.
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-11-10)  """
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-11-11)  result = db.run_no_throw(query)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-11-12)  if not result:
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-11-13)    return "Error: Query failed. Please rewrite your query and try again."
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-11-14)  return result
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-11-15)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-11-16)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-11-17)print(db_query_tool.invoke("SELECT * FROM Artist LIMIT 10;"))

```


API Reference: [tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html)

```
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-12-1)[(1, 'AC/DC'), (2, 'Accept'), (3, 'Aerosmith'), (4, 'Alanis Morissette'), (5, 'Alice In Chains'), (6, 'Antônio Carlos Jobim'), (7, 'Apocalyptica'), (8, 'Audioslave'), (9, 'BackBeat'), (10, 'Billy Cobham')]

```


While not strictly a tool, we will prompt an LLM to check for common mistakes in the query and later add this as a node in the workflow. 

```
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-13-1)fromlangchain_core.promptsimport ChatPromptTemplate
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-13-2)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-13-3)query_check_system = """You are a SQL expert with a strong attention to detail.
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-13-4)Double check the SQLite query for common mistakes, including:
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-13-5)- Using NOT IN with NULL values
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-13-6)- Using UNION when UNION ALL should have been used
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-13-7)- Using BETWEEN for exclusive ranges
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-13-8)- Data type mismatch in predicates
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-13-9)- Properly quoting identifiers
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-13-10)- Using the correct number of arguments for functions
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-13-11)- Casting to the correct data type
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-13-12)- Using the proper columns for joins
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-13-13)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-13-14)If there are any of the above mistakes, rewrite the query. If there are no mistakes, just reproduce the original query.
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-13-15)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-13-16)You will call the appropriate tool to execute the query after running this check."""
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-13-17)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-13-18)query_check_prompt = ChatPromptTemplate.from_messages(
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-13-19)  [("system", query_check_system), ("placeholder", "{messages}")]
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-13-20))
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-13-21)query_check = query_check_prompt | ChatOpenAI(model="gpt-4o", temperature=0).bind_tools(
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-13-22)  [db_query_tool], tool_choice="required"
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-13-23))
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-13-24)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-13-25)query_check.invoke({"messages": [("user", "SELECT * FROM Artist LIMIT 10;")]})

```


API Reference: [ChatPromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html)

```
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-14-1)AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_la8JTjHox6P1VjTqc15GSgdk', 'function': {'arguments': '{"query":"SELECT * FROM Artist LIMIT 10;"}', 'name': 'db_query_tool'}, 'type': 'function'}], 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 20, 'prompt_tokens': 221, 'total_tokens': 241}, 'model_name': 'gpt-4o-2024-05-13', 'system_fingerprint': 'fp_a2ff031fb5', 'finish_reason': 'stop', 'logprobs': None}, id='run-dd7873ef-d2f7-4769-a5c0-e6776ec2c515-0', tool_calls=[{'name': 'db_query_tool', 'args': {'query': 'SELECT * FROM Artist LIMIT 10;'}, 'id': 'call_la8JTjHox6P1VjTqc15GSgdk', 'type': 'tool_call'}], usage_metadata={'input_tokens': 221, 'output_tokens': 20, 'total_tokens': 241})

```


## Define the workflow[¶](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#define-the-workflow "Permanent link")

We will then define the workflow for the agent. The agent will first force-call the `list_tables_tool` to fetch the available tables from the database, then follow the steps mentioned at the beginning of the tutorial.

Using Pydantic with LangChain

This notebook uses Pydantic v2 `BaseModel`, which requires `langchain-core >= 0.3`. Using `langchain-core < 0.3` will result in errors due to mixing of Pydantic v1 and v2 `BaseModels`. 

```
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-1)fromtypingimport Annotated, Literal
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-2)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-3)fromlangchain_core.messagesimport AIMessage
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-4)fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-5)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-6)frompydanticimport BaseModel, Field
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-7)fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-8)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-9)fromlanggraph.graphimport END, StateGraph, START
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-10)fromlanggraph.graph.messageimport AnyMessage, add_messages
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-11)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-12)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-13)# Define the state for the agent
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-14)classState(TypedDict):
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-15)  messages: Annotated[list[AnyMessage], add_messages]
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-16)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-17)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-18)# Define a new graph
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-19)workflow = StateGraph(State)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-20)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-21)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-22)# Add a node for the first tool call
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-23)deffirst_tool_call(state: State) -> dict[str, list[AIMessage]]:
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-24)  return {
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-25)    "messages": [
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-26)      AIMessage(
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-27)        content="",
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-28)        tool_calls=[
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-29)          {
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-30)            "name": "sql_db_list_tables",
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-31)            "args": {},
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-32)            "id": "tool_abcd123",
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-33)          }
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-34)        ],
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-35)      )
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-36)    ]
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-37)  }
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-38)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-39)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-40)defmodel_check_query(state: State) -> dict[str, list[AIMessage]]:
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-41)"""
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-42)  Use this tool to double-check if your query is correct before executing it.
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-43)  """
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-44)  return {"messages": [query_check.invoke({"messages": [state["messages"][-1]]})]}
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-45)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-46)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-47)workflow.add_node("first_tool_call", first_tool_call)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-48)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-49)# Add nodes for the first two tools
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-50)workflow.add_node(
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-51)  "list_tables_tool", create_tool_node_with_fallback([list_tables_tool])
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-52))
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-53)workflow.add_node("get_schema_tool", create_tool_node_with_fallback([get_schema_tool]))
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-54)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-55)# Add a node for a model to choose the relevant tables based on the question and available tables
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-56)model_get_schema = ChatOpenAI(model="gpt-4o", temperature=0).bind_tools(
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-57)  [get_schema_tool]
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-58))
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-59)workflow.add_node(
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-60)  "model_get_schema",
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-61)  lambda state: {
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-62)    "messages": [model_get_schema.invoke(state["messages"])],
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-63)  },
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-64))
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-65)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-66)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-67)# Describe a tool to represent the end state
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-68)classSubmitFinalAnswer(BaseModel):
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-69)"""Submit the final answer to the user based on the query results."""
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-70)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-71)  final_answer: str = Field(..., description="The final answer to the user")
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-72)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-73)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-74)# Add a node for a model to generate a query based on the question and schema
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-75)query_gen_system = """You are a SQL expert with a strong attention to detail.
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-76)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-77)Given an input question, output a syntactically correct SQLite query to run, then look at the results of the query and return the answer.
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-78)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-79)DO NOT call any tool besides SubmitFinalAnswer to submit the final answer.
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-80)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-81)When generating the query:
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-82)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-83)Output the SQL query that answers the input question without a tool call.
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-84)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-85)Unless the user specifies a specific number of examples they wish to obtain, always limit your query to at most 5 results.
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-86)You can order the results by a relevant column to return the most interesting examples in the database.
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-87)Never query for all the columns from a specific table, only ask for the relevant columns given the question.
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-88)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-89)If you get an error while executing a query, rewrite the query and try again.
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-90)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-91)If you get an empty result set, you should try to rewrite the query to get a non-empty result set. 
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-92)NEVER make stuff up if you don't have enough information to answer the query... just say you don't have enough information.
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-93)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-94)If you have enough information to answer the input question, simply invoke the appropriate tool to submit the final answer to the user.
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-95)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-96)DO NOT make any DML statements (INSERT, UPDATE, DELETE, DROP etc.) to the database."""
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-97)query_gen_prompt = ChatPromptTemplate.from_messages(
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-98)  [("system", query_gen_system), ("placeholder", "{messages}")]
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-99))
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-100)query_gen = query_gen_prompt | ChatOpenAI(model="gpt-4o", temperature=0).bind_tools(
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-101)  [SubmitFinalAnswer]
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-102))
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-103)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-104)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-105)defquery_gen_node(state: State):
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-106)  message = query_gen.invoke(state)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-107)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-108)  # Sometimes, the LLM will hallucinate and call the wrong tool. We need to catch this and return an error message.
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-109)  tool_messages = []
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-110)  if message.tool_calls:
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-111)    for tc in message.tool_calls:
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-112)      if tc["name"] != "SubmitFinalAnswer":
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-113)        tool_messages.append(
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-114)          ToolMessage(
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-115)            content=f"Error: The wrong tool was called: {tc['name']}. Please fix your mistakes. Remember to only call SubmitFinalAnswer to submit the final answer. Generated queries should be outputted WITHOUT a tool call.",
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-116)            tool_call_id=tc["id"],
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-117)          )
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-118)        )
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-119)  else:
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-120)    tool_messages = []
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-121)  return {"messages": [message] + tool_messages}
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-122)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-123)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-124)workflow.add_node("query_gen", query_gen_node)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-125)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-126)# Add a node for the model to check the query before executing it
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-127)workflow.add_node("correct_query", model_check_query)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-128)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-129)# Add node for executing the query
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-130)workflow.add_node("execute_query", create_tool_node_with_fallback([db_query_tool]))
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-131)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-132)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-133)# Define a conditional edge to decide whether to continue or end the workflow
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-134)defshould_continue(state: State) -> Literal[END, "correct_query", "query_gen"]:
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-135)  messages = state["messages"]
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-136)  last_message = messages[-1]
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-137)  # If there is a tool call, then we finish
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-138)  if getattr(last_message, "tool_calls", None):
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-139)    return END
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-140)  if last_message.content.startswith("Error:"):
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-141)    return "query_gen"
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-142)  else:
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-143)    return "correct_query"
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-144)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-145)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-146)# Specify the edges between the nodes
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-147)workflow.add_edge(START, "first_tool_call")
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-148)workflow.add_edge("first_tool_call", "list_tables_tool")
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-149)workflow.add_edge("list_tables_tool", "model_get_schema")
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-150)workflow.add_edge("model_get_schema", "get_schema_tool")
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-151)workflow.add_edge("get_schema_tool", "query_gen")
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-152)workflow.add_conditional_edges(
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-153)  "query_gen",
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-154)  should_continue,
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-155))
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-156)workflow.add_edge("correct_query", "execute_query")
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-157)workflow.add_edge("execute_query", "query_gen")
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-158)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-159)# Compile the workflow into a runnable
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-15-160)app = workflow.compile()

```


API Reference: [AIMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.AIMessage.html) | [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html) | [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [add_messages](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.message.add_messages)

## Visualize the graph[¶](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#visualize-the-graph "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-16-1)fromIPython.displayimport Image, display
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-16-2)fromlangchain_core.runnables.graphimport MermaidDrawMethod
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-16-3)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-16-4)display(
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-16-5)  Image(
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-16-6)    app.get_graph().draw_mermaid_png(
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-16-7)      draw_method=MermaidDrawMethod.API,
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-16-8)    )
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-16-9)  )
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-16-10))

```


API Reference: [MermaidDrawMethod](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.MermaidDrawMethod.html)

![]()

## Run the agent[¶](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#run-the-agent "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-17-1)messages = app.invoke(
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-17-2)  {"messages": [("user", "Which sales agent made the most in sales in 2009?")]}
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-17-3))
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-17-4)json_str = messages["messages"][-1].tool_calls[0]["args"]["final_answer"]
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-17-5)json_str

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-18-1)'The sales agent who made the most in sales in 2009 is Steve Johnson with total sales of 164.34.'

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-19-1)for event in app.stream(
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-19-2)  {"messages": [("user", "Which sales agent made the most in sales in 2009?")]}
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-19-3)):
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-19-4)  print(event)

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-20-1){'first_tool_call': {'messages': [AIMessage(content='', tool_calls=[{'name': 'sql_db_list_tables', 'args': {}, 'id': 'tool_abcd123', 'type': 'tool_call'}])]}}
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-20-2){'list_tables_tool': {'messages': [ToolMessage(content='Album, Artist, Customer, Employee, Genre, Invoice, InvoiceLine, MediaType, Playlist, PlaylistTrack, Track', name='sql_db_list_tables', tool_call_id='tool_abcd123')]}}
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-20-3){'model_get_schema': {'messages': [AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_z1tyC7cEAawi5oIQn731Uknp', 'function': {'arguments': '{"table_names":"Employee, Invoice"}', 'name': 'sql_db_schema'}, 'type': 'function'}], 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 18, 'prompt_tokens': 177, 'total_tokens': 195}, 'model_name': 'gpt-4o-2024-05-13', 'system_fingerprint': 'fp_a2ff031fb5', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-c91a5aad-fc05-4881-87f9-0662d703c3c8-0', tool_calls=[{'name': 'sql_db_schema', 'args': {'table_names': 'Employee, Invoice'}, 'id': 'call_z1tyC7cEAawi5oIQn731Uknp', 'type': 'tool_call'}], usage_metadata={'input_tokens': 177, 'output_tokens': 18, 'total_tokens': 195})]}}
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-20-4){'get_schema_tool': {'messages': [ToolMessage(content='\nCREATE TABLE "Employee" (\n\t"EmployeeId" INTEGER NOT NULL, \n\t"LastName" NVARCHAR(20) NOT NULL, \n\t"FirstName" NVARCHAR(20) NOT NULL, \n\t"Title" NVARCHAR(30), \n\t"ReportsTo" INTEGER, \n\t"BirthDate" DATETIME, \n\t"HireDate" DATETIME, \n\t"Address" NVARCHAR(70), \n\t"City" NVARCHAR(40), \n\t"State" NVARCHAR(40), \n\t"Country" NVARCHAR(40), \n\t"PostalCode" NVARCHAR(10), \n\t"Phone" NVARCHAR(24), \n\t"Fax" NVARCHAR(24), \n\t"Email" NVARCHAR(60), \n\tPRIMARY KEY ("EmployeeId"), \n\tFOREIGN KEY("ReportsTo") REFERENCES "Employee" ("EmployeeId")\n)\n\n/*\n3 rows from Employee table:\nEmployeeId\tLastName\tFirstName\tTitle\tReportsTo\tBirthDate\tHireDate\tAddress\tCity\tState\tCountry\tPostalCode\tPhone\tFax\tEmail\n1\tAdams\tAndrew\tGeneral Manager\tNone\t1962-02-18 00:00:00\t2002-08-14 00:00:00\t11120 Jasper Ave NW\tEdmonton\tAB\tCanada\tT5K 2N1\t+1 (780) 428-9482\t+1 (780) 428-3457\tandrew@chinookcorp.com\n2\tEdwards\tNancy\tSales Manager\t1\t1958-12-08 00:00:00\t2002-05-01 00:00:00\t825 8 Ave SW\tCalgary\tAB\tCanada\tT2P 2T3\t+1 (403) 262-3443\t+1 (403) 262-3322\tnancy@chinookcorp.com\n3\tPeacock\tJane\tSales Support Agent\t2\t1973-08-29 00:00:00\t2002-04-01 00:00:00\t1111 6 Ave SW\tCalgary\tAB\tCanada\tT2P 5M5\t+1 (403) 262-3443\t+1 (403) 262-6712\tjane@chinookcorp.com\n*/\n\n\nCREATE TABLE "Invoice" (\n\t"InvoiceId" INTEGER NOT NULL, \n\t"CustomerId" INTEGER NOT NULL, \n\t"InvoiceDate" DATETIME NOT NULL, \n\t"BillingAddress" NVARCHAR(70), \n\t"BillingCity" NVARCHAR(40), \n\t"BillingState" NVARCHAR(40), \n\t"BillingCountry" NVARCHAR(40), \n\t"BillingPostalCode" NVARCHAR(10), \n\t"Total" NUMERIC(10, 2) NOT NULL, \n\tPRIMARY KEY ("InvoiceId"), \n\tFOREIGN KEY("CustomerId") REFERENCES "Customer" ("CustomerId")\n)\n\n/*\n3 rows from Invoice table:\nInvoiceId\tCustomerId\tInvoiceDate\tBillingAddress\tBillingCity\tBillingState\tBillingCountry\tBillingPostalCode\tTotal\n1\t2\t2009-01-01 00:00:00\tTheodor-Heuss-Straße 34\tStuttgart\tNone\tGermany\t70174\t1.98\n2\t4\t2009-01-02 00:00:00\tUllevålsveien 14\tOslo\tNone\tNorway\t0171\t3.96\n3\t8\t2009-01-03 00:00:00\tGrétrystraat 63\tBrussels\tNone\tBelgium\t1000\t5.94\n*/', name='sql_db_schema', tool_call_id='call_z1tyC7cEAawi5oIQn731Uknp')]}}
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-20-5){'query_gen': {'messages': [AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_ErWLktUfxKsHGNGr74m72yYD', 'function': {'arguments': '{"table_names":"Customer"}', 'name': 'sql_db_schema'}, 'type': 'function'}], 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 16, 'prompt_tokens': 1179, 'total_tokens': 1195}, 'model_name': 'gpt-4o-2024-05-13', 'system_fingerprint': 'fp_a2ff031fb5', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-19e02169-5e1e-40d9-90a2-384336ca5069-0', tool_calls=[{'name': 'sql_db_schema', 'args': {'table_names': 'Customer'}, 'id': 'call_ErWLktUfxKsHGNGr74m72yYD', 'type': 'tool_call'}], usage_metadata={'input_tokens': 1179, 'output_tokens': 16, 'total_tokens': 1195}), ToolMessage(content='Error: The wrong tool was called: sql_db_schema. Please fix your mistakes. Remember to only call SubmitFinalAnswer to submit the final answer. Generated queries should be outputted WITHOUT a tool call.', id='de5d25f5-b891-4e47-8282-d04dc9b93e9e', tool_call_id='call_ErWLktUfxKsHGNGr74m72yYD')]}}
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-20-6){'query_gen': {'messages': [AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_TFaA52SbhgEqm3ElEAd4HCsn', 'function': {'arguments': '{"table_names":["Customer"]}', 'name': 'sql_db_schema'}, 'type': 'function'}], 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 17, 'prompt_tokens': 1245, 'total_tokens': 1262}, 'model_name': 'gpt-4o-2024-05-13', 'system_fingerprint': 'fp_a2ff031fb5', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-2c5f800f-43dc-4224-847b-49b5079efd2a-0', tool_calls=[{'name': 'sql_db_schema', 'args': {'table_names': ['Customer']}, 'id': 'call_TFaA52SbhgEqm3ElEAd4HCsn', 'type': 'tool_call'}], usage_metadata={'input_tokens': 1245, 'output_tokens': 17, 'total_tokens': 1262}), ToolMessage(content='Error: The wrong tool was called: sql_db_schema. Please fix your mistakes. Remember to only call SubmitFinalAnswer to submit the final answer. Generated queries should be outputted WITHOUT a tool call.', id='6c962a35-fc24-4f27-86f0-6ec05256d478', tool_call_id='call_TFaA52SbhgEqm3ElEAd4HCsn')]}}
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-20-7){'query_gen': {'messages': [AIMessage(content="To determine which sales agent made the most in sales in 2009, we need to join the `Invoice`, `Customer`, and `Employee` tables. Here is the query to find the top sales agent:\n\n\`\`\`sql\nSELECT e.FirstName, e.LastName, SUM(i.Total) as TotalSales\nFROM Invoice i\nJOIN Customer c ON i.CustomerId = c.CustomerId\nJOIN Employee e ON c.SupportRepId = e.EmployeeId\nWHERE strftime('%Y', i.InvoiceDate) = '2009'\nGROUP BY e.EmployeeId\nORDER BY TotalSales DESC\nLIMIT 1;\n\`\`\`", additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 125, 'prompt_tokens': 1312, 'total_tokens': 1437}, 'model_name': 'gpt-4o-2024-05-13', 'system_fingerprint': 'fp_3aa7262c27', 'finish_reason': 'stop', 'logprobs': None}, id='run-6cacd10d-d3aa-49ae-b9d7-8cc209fc4ccc-0', usage_metadata={'input_tokens': 1312, 'output_tokens': 125, 'total_tokens': 1437})]}}
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-20-8){'correct_query': {'messages': [AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_FwCE2c7WORU7lKHdSWqMv0ON', 'function': {'arguments': '{"query":"SELECT e.FirstName, e.LastName, SUM(i.Total) as TotalSales\\nFROM Invoice i\\nJOIN Customer c ON i.CustomerId = c.CustomerId\\nJOIN Employee e ON c.SupportRepId = e.EmployeeId\\nWHERE strftime(\'%Y\', i.InvoiceDate) = \'2009\'\\nGROUP BY e.EmployeeId\\nORDER BY TotalSales DESC\\nLIMIT 1;"}', 'name': 'db_query_tool'}, 'type': 'function'}], 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 90, 'prompt_tokens': 337, 'total_tokens': 427}, 'model_name': 'gpt-4o-2024-05-13', 'system_fingerprint': 'fp_a2ff031fb5', 'finish_reason': 'stop', 'logprobs': None}, id='run-71067e75-80f6-4356-8239-518e466b3526-0', tool_calls=[{'name': 'db_query_tool', 'args': {'query': "SELECT e.FirstName, e.LastName, SUM(i.Total) as TotalSales\nFROM Invoice i\nJOIN Customer c ON i.CustomerId = c.CustomerId\nJOIN Employee e ON c.SupportRepId = e.EmployeeId\nWHERE strftime('%Y', i.InvoiceDate) = '2009'\nGROUP BY e.EmployeeId\nORDER BY TotalSales DESC\nLIMIT 1;"}, 'id': 'call_FwCE2c7WORU7lKHdSWqMv0ON', 'type': 'tool_call'}], usage_metadata={'input_tokens': 337, 'output_tokens': 90, 'total_tokens': 427})]}}
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-20-9){'execute_query': {'messages': [ToolMessage(content="[('Steve', 'Johnson', 164.34)]", name='db_query_tool', tool_call_id='call_FwCE2c7WORU7lKHdSWqMv0ON')]}}
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-20-10){'query_gen': {'messages': [AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_fHJ4lvdiFM9HY6gupE6vLZV4', 'function': {'arguments': '{"final_answer":"The sales agent who made the most in sales in 2009 is Steve Johnson with total sales of 164.34."}', 'name': 'SubmitFinalAnswer'}, 'type': 'function'}], 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 41, 'prompt_tokens': 1553, 'total_tokens': 1594}, 'model_name': 'gpt-4o-2024-05-13', 'system_fingerprint': 'fp_cb7cc8e106', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-2ec7bf3a-2a16-47bd-aa9c-b7d6dc531c1b-0', tool_calls=[{'name': 'SubmitFinalAnswer', 'args': {'final_answer': 'The sales agent who made the most in sales in 2009 is Steve Johnson with total sales of 164.34.'}, 'id': 'call_fHJ4lvdiFM9HY6gupE6vLZV4', 'type': 'tool_call'}], usage_metadata={'input_tokens': 1553, 'output_tokens': 41, 'total_tokens': 1594})]}}

```


## Eval[¶](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#eval "Permanent link")

Now, we can evaluate this agent! We previously defined [simple SQL agent](https://github.com/langchain-ai/langsmith-cookbook/blob/main/testing-examples/agent-evals-with-langgraph/langgraph_sql_agent_eval.ipynb) as part of our LangSmith evaluation cookbooks, and evaluated responses to 5 questions about our database. We can compare this agent to our prior one on the same dataset. [Agent evaluation](https://docs.smith.langchain.com/concepts/evaluation#agents) can focus on 3 things:

  * `Response`: The inputs are a prompt and a list of tools. The output is the agent response.
  * `Single tool`: As before, the inputs are a prompt and a list of tools. The output the tool call.
  * `Trajectory`: As before, the inputs are a prompt and a list of tools. The output is the list of tool calls



![Screenshot 2024-06-13 at 2.13.30 PM.png]()

### Response[¶](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#response "Permanent link")

We'll evaluate end-to-end responses of our agent relative to reference answers. Let's run [response evaluation](https://docs.smith.langchain.com/concepts/evaluation#evaluating-an-agents-final-response) [on the same dataset](https://smith.langchain.com/public/20808486-67c3-4e30-920b-6d49d6f2b6b8/d).

```
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-21-1)importjson
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-21-2)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-21-3)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-21-4)defpredict_sql_agent_answer(example: dict):
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-21-5)"""Use this for answer evaluation"""
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-21-6)  msg = {"messages": ("user", example["input"])}
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-21-7)  messages = app.invoke(msg)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-21-8)  json_str = messages["messages"][-1].tool_calls[0]["args"]
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-21-9)  response = json_str["final_answer"]
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-21-10)  return {"response": response}

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-22-1)fromlangchainimport hub
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-22-2)fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-22-3)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-22-4)# Grade prompt
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-22-5)grade_prompt_answer_accuracy = prompt = hub.pull("langchain-ai/rag-answer-vs-reference")
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-22-6)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-22-7)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-22-8)defanswer_evaluator(run, example) -> dict:
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-22-9)"""
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-22-10)  A simple evaluator for RAG answer accuracy
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-22-11)  """
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-22-12)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-22-13)  # Get question, ground truth answer, chain
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-22-14)  input_question = example.inputs["input"]
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-22-15)  reference = example.outputs["output"]
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-22-16)  prediction = run.outputs["response"]
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-22-17)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-22-18)  # LLM grader
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-22-19)  llm = ChatOpenAI(model="gpt-4-turbo", temperature=0)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-22-20)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-22-21)  # Structured prompt
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-22-22)  answer_grader = grade_prompt_answer_accuracy | llm
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-22-23)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-22-24)  # Run evaluator
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-22-25)  score = answer_grader.invoke(
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-22-26)    {
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-22-27)      "question": input_question,
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-22-28)      "correct_answer": reference,
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-22-29)      "student_answer": prediction,
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-22-30)    }
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-22-31)  )
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-22-32)  score = score["Score"]
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-22-33)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-22-34)  return {"key": "answer_v_reference_score", "score": score}

```


API Reference: [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html)

```
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-23-1)fromlangsmith.evaluationimport evaluate
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-23-2)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-23-3)dataset_name = "SQL Agent Response"
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-23-4)try:
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-23-5)  experiment_results = evaluate(
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-23-6)    predict_sql_agent_answer,
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-23-7)    data=dataset_name,
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-23-8)    evaluators=[answer_evaluator],
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-23-9)    num_repetitions=3,
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-23-10)    experiment_prefix="sql-agent-multi-step-response-v-reference",
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-23-11)    metadata={"version": "Chinook, gpt-4o multi-step-agent"},
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-23-12)  )
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-23-13)except:
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-23-14)  print("Please setup LangSmith")

```


Summary metrics (see dataset [here](https://smith.langchain.com/public/20808486-67c3-4e30-920b-6d49d6f2b6b8/d)):

  * The `multi-step` agent here out performs the previously defined [base case SQL agent](https://github.com/langchain-ai/langsmith-cookbook/blob/main/testing-examples/agent-evals-with-langgraph/langgraph_sql_agent_eval.ipynb)



![Screenshot 2024-06-13 at 2.09.57 PM.png]()

### Trajectory[¶](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#trajectory "Permanent link")

Let's run [trajectory evaluation](https://docs.smith.langchain.com/concepts/evaluation#evaluating-an-agents-trajectory) on this same dataset.

```
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-24-1)# These are the tools that we expect the agent to use
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-24-2)expected_trajectory = [
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-24-3)  "sql_db_list_tables", # first: list_tables_tool node
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-24-4)  "sql_db_schema", # second: get_schema_tool node
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-24-5)  "db_query_tool", # third: execute_query node
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-24-6)  "SubmitFinalAnswer",
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-24-7)] # fourth: query_gen

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-25-1)defpredict_sql_agent_messages(example: dict):
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-25-2)"""Use this for answer evaluation"""
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-25-3)  msg = {"messages": ("user", example["input"])}
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-25-4)  messages = app.invoke(msg)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-25-5)  return {"response": messages}

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-1)fromlangsmith.schemasimport Example, Run
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-2)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-3)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-4)deffind_tool_calls(messages):
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-5)"""
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-6)  Find all tool calls in the messages returned
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-7)  """
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-8)  tool_calls = [
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-9)    tc["name"] for m in messages["messages"] for tc in getattr(m, "tool_calls", [])
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-10)  ]
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-11)  return tool_calls
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-12)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-13)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-14)defcontains_all_tool_calls_in_order_exact_match(
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-15)  root_run: Run, example: Example
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-16)) -> dict:
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-17)"""
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-18)  Check if all expected tools are called in exact order and without any additional tool calls.
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-19)  """
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-20)  expected_trajectory = [
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-21)    "sql_db_list_tables",
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-22)    "sql_db_schema",
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-23)    "db_query_tool",
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-24)    "SubmitFinalAnswer",
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-25)  ]
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-26)  messages = root_run.outputs["response"]
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-27)  tool_calls = find_tool_calls(messages)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-28)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-29)  # Print the tool calls for debugging
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-30)  print("Here are my tool calls:")
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-31)  print(tool_calls)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-32)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-33)  # Check if the tool calls match the expected trajectory exactly
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-34)  if tool_calls == expected_trajectory:
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-35)    score = 1
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-36)  else:
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-37)    score = 0
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-38)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-39)  return {"score": int(score), "key": "multi_tool_call_in_exact_order"}
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-40)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-41)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-42)defcontains_all_tool_calls_in_order(root_run: Run, example: Example) -> dict:
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-43)"""
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-44)  Check if all expected tools are called in order,
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-45)  but it allows for other tools to be called in between the expected ones.
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-46)  """
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-47)  messages = root_run.outputs["response"]
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-48)  tool_calls = find_tool_calls(messages)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-49)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-50)  # Print the tool calls for debugging
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-51)  print("Here are my tool calls:")
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-52)  print(tool_calls)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-53)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-54)  it = iter(tool_calls)
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-55)  if all(elem in it for elem in expected_trajectory):
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-56)    score = 1
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-57)  else:
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-58)    score = 0
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-26-59)  return {"score": int(score), "key": "multi_tool_call_in_order"}

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-27-1)try:
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-27-2)  experiment_results = evaluate(
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-27-3)    predict_sql_agent_messages,
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-27-4)    data=dataset_name,
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-27-5)    evaluators=[
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-27-6)      contains_all_tool_calls_in_order,
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-27-7)      contains_all_tool_calls_in_order_exact_match,
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-27-8)    ],
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-27-9)    num_repetitions=3,
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-27-10)    experiment_prefix="sql-agent-multi-step-tool-calling-trajecory-in-order",
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-27-11)    metadata={"version": "Chinook, gpt-4o multi-step-agent"},
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-27-12)  )
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-27-13)except:
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-27-14)  print("Please setup LangSmith")

```


The aggregate scores show that we never correctly call the tools in exact order:

![Screenshot 2024-06-13 at 2.46.34 PM.png]()

Looking at the logging, we can see something interesting - 

```
[](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__codelineno-28-1)['sql_db_list_tables', 'sql_db_schema', 'sql_db_query', 'db_query_tool', 'SubmitFinalAnswer']

```


We appear to inject a hallucinated tool call, `sql_db_query`, into our trajectory for most of the runs.

This is why `multi_tool_call_in_exact_order` fails, but `multi_tool_call_in_order` still passes. 

We will explore ways to resolve this using LangGraph in future cookbooks!

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Self-RAG using local LLMs  ](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/) [ Next  Multi-agent network  ](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/multi-agent-collaboration/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
