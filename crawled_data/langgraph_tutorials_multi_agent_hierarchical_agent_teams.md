---
url: https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#hierarchical-agent-teams)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Hierarchical Agent Teams 

[ ](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/?q= "Share")

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
        * [ RAG  ](https://langchain-ai.github.io/langgraph/tutorials#rag)
        * Agent Architectures  Agent Architectures 
          * [ Agent Architectures  ](https://langchain-ai.github.io/langgraph/tutorials#agent-architectures)
          * Multi-Agent Systems  Multi-Agent Systems 
            * [ Multi-Agent Systems  ](https://langchain-ai.github.io/langgraph/tutorials#multi-agent-systems)
            * [ Multi-agent network  ](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/multi-agent-collaboration/)
            * [ Multi-agent supervisor  ](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/agent_supervisor/)
            * Hierarchical Agent Teams  [ Hierarchical Agent Teams  ](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#setup)
              * [ Create Tools  ](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#create-tools)
              * [ Helper Utilities  ](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#helper-utilities)
              * [ Define Agent Teams  ](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#define-agent-teams)
                * [ Research Team  ](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#research-team)
                * [ Document Writing Team  ](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#document-writing-team)
              * [ Add Layers  ](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#add-layers)
          * [ Planning Agents  ](https://langchain-ai.github.io/langgraph/tutorials#planning-agents)
          * [ Reflection & Critique  ](https://langchain-ai.github.io/langgraph/tutorials#reflection-critique)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#setup)
  * [ Create Tools  ](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#create-tools)
  * [ Helper Utilities  ](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#helper-utilities)
  * [ Define Agent Teams  ](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#define-agent-teams)
    * [ Research Team  ](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#research-team)
    * [ Document Writing Team  ](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#document-writing-team)
  * [ Add Layers  ](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#add-layers)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ Tutorials  ](https://langchain-ai.github.io/langgraph/tutorials/)
  4. [ Agent Architectures  ](https://langchain-ai.github.io/langgraph/tutorials#agent-architectures)
  5. [ Multi-Agent Systems  ](https://langchain-ai.github.io/langgraph/tutorials#multi-agent-systems)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/tutorials/multi_agent/hierarchical_agent_teams.ipynb "Edit this page")

# Hierarchical Agent Teams[¶](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#hierarchical-agent-teams "Permanent link")

In our previous example ([Agent Supervisor](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/agent_supervisor)), we introduced the concept of a single [supervisor node](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#supervisor) to route work between different worker nodes.

But what if the job for a single worker becomes too complex? What if the number of workers becomes too large?

For some applications, the system may be more effective if work is distributed _hierarchically_.

You can do this by composing different subgraphs and creating a top-level supervisor, along with mid-level supervisors.

To do this, let's build a simple research assistant! The graph will look something like the following:

![diagram]()

This notebook is inspired by the paper [AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation](https://arxiv.org/abs/2308.08155), by Wu, et. al. In the rest of this notebook, you will:

  1. Define the agents' tools to access the web and write files
  2. Define some utilities to help create the graph and agents
  3. Create and define each team (web research + doc writing)
  4. Compose everything together.



## Setup[¶](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#setup "Permanent link")

First, let's install our required packages and set our API keys

```
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-0-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-0-2)%pip install -U langgraph langchain_community langchain_anthropic langchain_experimental

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-1-1)importgetpass
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-1-2)importos
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-1-5)def_set_if_undefined(var: str):
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-1-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-1-7)    os.environ[var] = getpass.getpass(f"Please provide your {var}")
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-1-8)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-1-10)_set_if_undefined("OPENAI_API_KEY")
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-1-11)_set_if_undefined("TAVILY_API_KEY")

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Create Tools[¶](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#create-tools "Permanent link")

Each team will be composed of one or more agents each with one or more tools. Below, define all the tools to be used by your different teams.

We'll start with the research team.

**ResearchTeam tools**

The research team can use a search engine and url scraper to find information on the web. Feel free to add additional functionality below to boost the team performance!

```
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-2-1)fromtypingimport Annotated, List
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-2-2)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-2-3)fromlangchain_community.document_loadersimport WebBaseLoader
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-2-4)fromlangchain_community.tools.tavily_searchimport TavilySearchResults
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-2-5)fromlangchain_core.toolsimport tool
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-2-6)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-2-7)tavily_tool = TavilySearchResults(max_results=5)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-2-8)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-2-9)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-2-10)@tool
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-2-11)defscrape_webpages(urls: List[str]) -> str:
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-2-12)"""Use requests and bs4 to scrape the provided web pages for detailed information."""
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-2-13)  loader = WebBaseLoader(urls)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-2-14)  docs = loader.load()
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-2-15)  return "\n\n".join(
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-2-16)    [
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-2-17)      f'<Document name="{doc.metadata.get("title","")}">\n{doc.page_content}\n</Document>'
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-2-18)      for doc in docs
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-2-19)    ]
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-2-20)  )

```


API Reference: [WebBaseLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.web_base.WebBaseLoader.html) | [TavilySearchResults](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.tavily_search.tool.TavilySearchResults.html) | [tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html)

**Document writing team tools**

Next up, we will give some tools for the doc writing team to use. We define some bare-bones file-access tools below.

Note that this gives the agents access to your file-system, which can be unsafe. We also haven't optimized the tool descriptions for performance.

```
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-1)frompathlibimport Path
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-2)fromtempfileimport TemporaryDirectory
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-3)fromtypingimport Dict, Optional
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-4)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-5)fromlangchain_experimental.utilitiesimport PythonREPL
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-6)fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-7)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-8)_TEMP_DIRECTORY = TemporaryDirectory()
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-9)WORKING_DIRECTORY = Path(_TEMP_DIRECTORY.name)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-10)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-11)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-12)@tool
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-13)defcreate_outline(
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-14)  points: Annotated[List[str], "List of main points or sections."],
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-15)  file_name: Annotated[str, "File path to save the outline."],
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-16)) -> Annotated[str, "Path of the saved outline file."]:
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-17)"""Create and save an outline."""
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-18)  with (WORKING_DIRECTORY / file_name).open("w") as file:
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-19)    for i, point in enumerate(points):
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-20)      file.write(f"{i+1}. {point}\n")
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-21)  return f"Outline saved to {file_name}"
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-22)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-23)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-24)@tool
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-25)defread_document(
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-26)  file_name: Annotated[str, "File path to read the document from."],
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-27)  start: Annotated[Optional[int], "The start line. Default is 0"] = None,
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-28)  end: Annotated[Optional[int], "The end line. Default is None"] = None,
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-29)) -> str:
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-30)"""Read the specified document."""
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-31)  with (WORKING_DIRECTORY / file_name).open("r") as file:
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-32)    lines = file.readlines()
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-33)  if start is None:
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-34)    start = 0
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-35)  return "\n".join(lines[start:end])
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-36)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-37)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-38)@tool
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-39)defwrite_document(
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-40)  content: Annotated[str, "Text content to be written into the document."],
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-41)  file_name: Annotated[str, "File path to save the document."],
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-42)) -> Annotated[str, "Path of the saved document file."]:
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-43)"""Create and save a text document."""
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-44)  with (WORKING_DIRECTORY / file_name).open("w") as file:
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-45)    file.write(content)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-46)  return f"Document saved to {file_name}"
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-47)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-48)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-49)@tool
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-50)defedit_document(
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-51)  file_name: Annotated[str, "Path of the document to be edited."],
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-52)  inserts: Annotated[
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-53)    Dict[int, str],
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-54)    "Dictionary where key is the line number (1-indexed) and value is the text to be inserted at that line.",
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-55)  ],
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-56)) -> Annotated[str, "Path of the edited document file."]:
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-57)"""Edit a document by inserting text at specific line numbers."""
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-58)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-59)  with (WORKING_DIRECTORY / file_name).open("r") as file:
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-60)    lines = file.readlines()
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-61)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-62)  sorted_inserts = sorted(inserts.items())
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-63)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-64)  for line_number, text in sorted_inserts:
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-65)    if 1 <= line_number <= len(lines) + 1:
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-66)      lines.insert(line_number - 1, text + "\n")
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-67)    else:
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-68)      return f"Error: Line number {line_number} is out of range."
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-69)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-70)  with (WORKING_DIRECTORY / file_name).open("w") as file:
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-71)    file.writelines(lines)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-72)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-73)  return f"Document edited and saved to {file_name}"
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-74)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-75)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-76)# Warning: This executes code locally, which can be unsafe when not sandboxed
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-77)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-78)repl = PythonREPL()
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-79)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-80)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-81)@tool
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-82)defpython_repl_tool(
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-83)  code: Annotated[str, "The python code to execute to generate your chart."],
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-84)):
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-85)"""Use this to execute python code. If you want to see the output of a value,
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-86)  you should print it out with `print(...)`. This is visible to the user."""
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-87)  try:
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-88)    result = repl.run(code)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-89)  except BaseException as e:
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-90)    return f"Failed to execute. Error: {repr(e)}"
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-3-91)  return f"Successfully executed:\n\`\`\`python\n{code}\n\`\`\`\nStdout: {result}"

```


API Reference: [PythonREPL](https://python.langchain.com/api_reference/experimental/utilities/langchain_experimental.utilities.python.PythonREPL.html)

## Helper Utilities[¶](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#helper-utilities "Permanent link")

We are going to create a few utility functions to make it more concise when we want to:

  1. Create a worker agent.
  2. Create a supervisor for the sub-graph.



These will simplify the graph compositional code at the end for us so it's easier to see what's going on.

```
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-4-1)fromtypingimport List, Optional, Literal
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-4-2)fromlangchain_core.language_models.chat_modelsimport BaseChatModel
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-4-3)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-4-4)fromlanggraph.graphimport StateGraph, MessagesState, START, END
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-4-5)fromlanggraph.typesimport Command
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-4-6)fromlangchain_core.messagesimport HumanMessage, trim_messages
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-4-7)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-4-8)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-4-9)classState(MessagesState):
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-4-10)  next: str
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-4-11)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-4-12)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-4-13)defmake_supervisor_node(llm: BaseChatModel, members: list[str]) -> str:
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-4-14)  options = ["FINISH"] + members
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-4-15)  system_prompt = (
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-4-16)    "You are a supervisor tasked with managing a conversation between the"
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-4-17)    f" following workers: {members}. Given the following user request,"
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-4-18)    " respond with the worker to act next. Each worker will perform a"
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-4-19)    " task and respond with their results and status. When finished,"
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-4-20)    " respond with FINISH."
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-4-21)  )
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-4-22)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-4-23)  classRouter(TypedDict):
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-4-24)"""Worker to route to next. If no workers needed, route to FINISH."""
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-4-25)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-4-26)    next: Literal[*options]
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-4-27)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-4-28)  defsupervisor_node(state: State) -> Command[Literal[*members, "__end__"]]:
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-4-29)"""An LLM-based router."""
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-4-30)    messages = [
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-4-31)      {"role": "system", "content": system_prompt},
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-4-32)    ] + state["messages"]
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-4-33)    response = llm.with_structured_output(Router).invoke(messages)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-4-34)    goto = response["next"]
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-4-35)    if goto == "FINISH":
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-4-36)      goto = END
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-4-37)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-4-38)    return Command(goto=goto, update={"next": goto})
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-4-39)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-4-40)  return supervisor_node

```


API Reference: [BaseChatModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html) | [HumanMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.human.HumanMessage.html) | [trim_messages](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.utils.trim_messages.html) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END) | [Command](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Command)

## Define Agent Teams[¶](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#define-agent-teams "Permanent link")

Now we can get to define our hierarchical teams. "Choose your player!"

### Research Team[¶](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#research-team "Permanent link")

The research team will have a search agent and a web scraping "research_agent" as the two worker nodes. Let's create those, as well as the team supervisor.

```
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-5-1)fromlangchain_core.messagesimport HumanMessage
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-5-2)fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-5-3)fromlanggraph.prebuiltimport create_react_agent
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-5-4)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-5-5)llm = ChatOpenAI(model="gpt-4o")
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-5-6)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-5-7)search_agent = create_react_agent(llm, tools=[tavily_tool])
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-5-8)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-5-9)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-5-10)defsearch_node(state: State) -> Command[Literal["supervisor"]]:
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-5-11)  result = search_agent.invoke(state)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-5-12)  return Command(
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-5-13)    update={
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-5-14)      "messages": [
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-5-15)        HumanMessage(content=result["messages"][-1].content, name="search")
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-5-16)      ]
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-5-17)    },
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-5-18)    # We want our workers to ALWAYS "report back" to the supervisor when done
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-5-19)    goto="supervisor",
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-5-20)  )
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-5-21)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-5-22)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-5-23)web_scraper_agent = create_react_agent(llm, tools=[scrape_webpages])
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-5-24)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-5-25)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-5-26)defweb_scraper_node(state: State) -> Command[Literal["supervisor"]]:
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-5-27)  result = web_scraper_agent.invoke(state)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-5-28)  return Command(
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-5-29)    update={
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-5-30)      "messages": [
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-5-31)        HumanMessage(content=result["messages"][-1].content, name="web_scraper")
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-5-32)      ]
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-5-33)    },
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-5-34)    # We want our workers to ALWAYS "report back" to the supervisor when done
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-5-35)    goto="supervisor",
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-5-36)  )
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-5-37)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-5-38)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-5-39)research_supervisor_node = make_supervisor_node(llm, ["search", "web_scraper"])

```


API Reference: [HumanMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.human.HumanMessage.html) | [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html) | [create_react_agent](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent)

Now that we've created the necessary components, defining their interactions is easy. Add the nodes to the team graph, and define the edges, which determine the transition criteria.

```
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-6-1)research_builder = StateGraph(State)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-6-2)research_builder.add_node("supervisor", research_supervisor_node)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-6-3)research_builder.add_node("search", search_node)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-6-4)research_builder.add_node("web_scraper", web_scraper_node)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-6-5)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-6-6)research_builder.add_edge(START, "supervisor")
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-6-7)research_graph = research_builder.compile()

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-7-1)fromIPython.displayimport Image, display
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-7-2)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-7-3)display(Image(research_graph.get_graph().draw_mermaid_png()))

```


![]()

We can give this team work directly. Try it out below.

```
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-8-1)for s in research_graph.stream(
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-8-2)  {"messages": [("user", "when is Taylor Swift's next tour?")]},
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-8-3)  {"recursion_limit": 100},
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-8-4)):
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-8-5)  print(s)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-8-6)  print("---")

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-9-1){'supervisor': {'next': 'search'}}
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-9-2)---
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-9-3){'search': {'messages': [HumanMessage(content="Taylor Swift's next tour is The Eras Tour, which includes both U.S. and international dates. She announced additional U.S. dates for 2024. You can find more details about the tour and ticket information on platforms like Ticketmaster and official announcements.", additional_kwargs={}, response_metadata={}, name='search', id='4df8687b-50a8-4342-aad5-680732c4a10f')]}}
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-9-4)---
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-9-5){'supervisor': {'next': 'web_scraper'}}
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-9-6)---
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-9-7){'web_scraper': {'messages': [HumanMessage(content='Taylor Swift\'s next tour is "The Eras Tour." Here are some of the upcoming international dates for 2024 that were listed on Ticketmaster:\n\n1. **Toronto, ON, Canada** at Rogers Centre\n  - November 21, 2024\n  - November 22, 2024\n  - November 23, 2024\n\n2. **Vancouver, BC, Canada** at BC Place\n  - December 6, 2024\n  - December 7, 2024\n  - December 8, 2024\n\nFor the most current information and additional dates, you can check platforms like Ticketmaster or Taylor Swift\'s [official website](https://www.taylorswift.com/events).', additional_kwargs={}, response_metadata={}, name='web_scraper', id='27524ebc-d179-4733-831d-ee10a58a2528')]}}
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-9-8)---
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-9-9){'supervisor': {'next': '__end__'}}
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-9-10)---

```


### Document Writing Team[¶](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#document-writing-team "Permanent link")

Create the document writing team below using a similar approach. This time, we will give each agent access to different file-writing tools.

Note that we are giving file-system access to our agent here, which is not safe in all cases.

```
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-1)llm = ChatOpenAI(model="gpt-4o")
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-2)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-3)doc_writer_agent = create_react_agent(
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-4)  llm,
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-5)  tools=[write_document, edit_document, read_document],
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-6)  prompt=(
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-7)    "You can read, write and edit documents based on note-taker's outlines. "
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-8)    "Don't ask follow-up questions."
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-9)  ),
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-10))
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-11)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-12)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-13)defdoc_writing_node(state: State) -> Command[Literal["supervisor"]]:
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-14)  result = doc_writer_agent.invoke(state)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-15)  return Command(
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-16)    update={
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-17)      "messages": [
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-18)        HumanMessage(content=result["messages"][-1].content, name="doc_writer")
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-19)      ]
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-20)    },
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-21)    # We want our workers to ALWAYS "report back" to the supervisor when done
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-22)    goto="supervisor",
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-23)  )
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-24)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-25)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-26)note_taking_agent = create_react_agent(
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-27)  llm,
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-28)  tools=[create_outline, read_document],
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-29)  prompt=(
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-30)    "You can read documents and create outlines for the document writer. "
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-31)    "Don't ask follow-up questions."
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-32)  ),
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-33))
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-34)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-35)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-36)defnote_taking_node(state: State) -> Command[Literal["supervisor"]]:
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-37)  result = note_taking_agent.invoke(state)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-38)  return Command(
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-39)    update={
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-40)      "messages": [
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-41)        HumanMessage(content=result["messages"][-1].content, name="note_taker")
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-42)      ]
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-43)    },
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-44)    # We want our workers to ALWAYS "report back" to the supervisor when done
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-45)    goto="supervisor",
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-46)  )
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-47)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-48)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-49)chart_generating_agent = create_react_agent(
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-50)  llm, tools=[read_document, python_repl_tool]
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-51))
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-52)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-53)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-54)defchart_generating_node(state: State) -> Command[Literal["supervisor"]]:
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-55)  result = chart_generating_agent.invoke(state)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-56)  return Command(
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-57)    update={
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-58)      "messages": [
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-59)        HumanMessage(
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-60)          content=result["messages"][-1].content, name="chart_generator"
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-61)        )
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-62)      ]
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-63)    },
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-64)    # We want our workers to ALWAYS "report back" to the supervisor when done
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-65)    goto="supervisor",
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-66)  )
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-67)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-68)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-69)doc_writing_supervisor_node = make_supervisor_node(
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-70)  llm, ["doc_writer", "note_taker", "chart_generator"]
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-10-71))

```


With the objects themselves created, we can form the graph.

```
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-11-1)# Create the graph here
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-11-2)paper_writing_builder = StateGraph(State)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-11-3)paper_writing_builder.add_node("supervisor", doc_writing_supervisor_node)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-11-4)paper_writing_builder.add_node("doc_writer", doc_writing_node)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-11-5)paper_writing_builder.add_node("note_taker", note_taking_node)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-11-6)paper_writing_builder.add_node("chart_generator", chart_generating_node)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-11-7)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-11-8)paper_writing_builder.add_edge(START, "supervisor")
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-11-9)paper_writing_graph = paper_writing_builder.compile()

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-12-1)fromIPython.displayimport Image, display
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-12-2)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-12-3)display(Image(paper_writing_graph.get_graph().draw_mermaid_png()))

```


![]()

```
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-13-1)for s in paper_writing_graph.stream(
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-13-2)  {
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-13-3)    "messages": [
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-13-4)      (
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-13-5)        "user",
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-13-6)        "Write an outline for poem about cats and then write the poem to disk.",
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-13-7)      )
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-13-8)    ]
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-13-9)  },
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-13-10)  {"recursion_limit": 100},
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-13-11)):
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-13-12)  print(s)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-13-13)  print("---")

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-14-1){'supervisor': {'next': 'note_taker'}}
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-14-2)---
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-14-3){'note_taker': {'messages': [HumanMessage(content='The outline for the poem about cats has been created and saved as "cats_poem_outline.txt".', additional_kwargs={}, response_metadata={}, name='note_taker', id='14a5d8ca-9092-416f-96ee-ba16686e8658')]}}
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-14-4)---
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-14-5){'supervisor': {'next': 'doc_writer'}}
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-14-6)---
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-14-7){'doc_writer': {'messages': [HumanMessage(content='The poem about cats has been written and saved as "cats_poem.txt".', additional_kwargs={}, response_metadata={}, name='doc_writer', id='c4e31a94-63ae-4632-9e80-1166f3f138b2')]}}
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-14-8)---
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-14-9){'supervisor': {'next': '__end__'}}
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-14-10)---

```


## Add Layers[¶](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#add-layers "Permanent link")

In this design, we are enforcing a top-down planning policy. We've created two graphs already, but we have to decide how to route work between the two.

We'll create a _third_ graph to orchestrate the previous two, and add some connectors to define how this top-level state is shared between the different graphs.

```
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-15-1)fromlangchain_core.messagesimport BaseMessage
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-15-2)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-15-3)llm = ChatOpenAI(model="gpt-4o")
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-15-4)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-15-5)teams_supervisor_node = make_supervisor_node(llm, ["research_team", "writing_team"])

```


API Reference: [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html)

```
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-16-1)defcall_research_team(state: State) -> Command[Literal["supervisor"]]:
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-16-2)  response = research_graph.invoke({"messages": state["messages"][-1]})
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-16-3)  return Command(
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-16-4)    update={
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-16-5)      "messages": [
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-16-6)        HumanMessage(
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-16-7)          content=response["messages"][-1].content, name="research_team"
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-16-8)        )
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-16-9)      ]
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-16-10)    },
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-16-11)    goto="supervisor",
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-16-12)  )
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-16-13)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-16-14)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-16-15)defcall_paper_writing_team(state: State) -> Command[Literal["supervisor"]]:
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-16-16)  response = paper_writing_graph.invoke({"messages": state["messages"][-1]})
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-16-17)  return Command(
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-16-18)    update={
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-16-19)      "messages": [
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-16-20)        HumanMessage(
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-16-21)          content=response["messages"][-1].content, name="writing_team"
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-16-22)        )
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-16-23)      ]
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-16-24)    },
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-16-25)    goto="supervisor",
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-16-26)  )
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-16-27)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-16-28)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-16-29)# Define the graph.
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-16-30)super_builder = StateGraph(State)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-16-31)super_builder.add_node("supervisor", teams_supervisor_node)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-16-32)super_builder.add_node("research_team", call_research_team)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-16-33)super_builder.add_node("writing_team", call_paper_writing_team)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-16-34)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-16-35)super_builder.add_edge(START, "supervisor")
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-16-36)super_graph = super_builder.compile()

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-17-1)fromIPython.displayimport Image, display
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-17-2)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-17-3)display(Image(super_graph.get_graph().draw_mermaid_png()))

```


![]()

```
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-18-1)for s in super_graph.stream(
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-18-2)  {
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-18-3)    "messages": [
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-18-4)      ("user", "Research AI agents and write a brief report about them.")
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-18-5)    ],
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-18-6)  },
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-18-7)  {"recursion_limit": 150},
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-18-8)):
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-18-9)  print(s)
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-18-10)  print("---")

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-19-1){'supervisor': {'next': 'research_team'}}
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-19-2)---
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-19-3){'research_team': {'messages': [HumanMessage(content="**AI Agents Overview 2023**\n\nAI agents are sophisticated technologies that automate and enhance various processes across industries, becoming increasingly integral to business operations. In 2023, these agents are notable for their advanced capabilities in communication, data visualization, and language processing.\n\n**Popular AI Agents in 2023:**\n1. **Auto GPT**: This agent is renowned for its seamless integration abilities, significantly impacting industries by improving communication and operational workflows.\n2. **ChartGPT**: Specializing in data visualization, ChartGPT enables users to interact with data innovatively, providing deeper insights and comprehension.\n3. **LLMops**: With advanced language capabilities, LLMops is a versatile tool seeing widespread use across multiple sectors.\n\n**Market Trends:**\nThe AI agents market is experiencing rapid growth, with significant advancements anticipated by 2030. There's a growing demand for AI agents in personalized interactions, particularly within customer service, healthcare, and marketing sectors. This trend is fueled by the need for more efficient and tailored customer experiences.\n\n**Key Players:**\nLeading companies such as Microsoft, IBM, Google, Oracle, and AWS are key players in the AI agents market, highlighting the widespread adoption and investment in these technologies.\n\n**Technological Innovations:**\nAI agents are being developed alongside simulation technologies for robust testing and deployment environments. Innovations in generative AI are accelerating, supported by advancements in large language models and platforms like ChatGPT.\n\n**Applications in Healthcare:**\nIn healthcare, AI agents are automating routine tasks, allowing medical professionals to focus more on patient care. They're poised to significantly enhance healthcare delivery and efficiency.\n\n**Future Prospects:**\nThe future of AI agents is promising, with continued evolution and integration into various platforms and ecosystems, offering more seamless and intelligent interactions. As these technologies advance, they are expected to redefine business operations and customer interactions.", additional_kwargs={}, response_metadata={}, name='research_team', id='5f6606e0-838c-406c-b50d-9f9f6a076322')]}}
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-19-4)---
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-19-5){'supervisor': {'next': 'writing_team'}}
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-19-6)---
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-19-7){'writing_team': {'messages': [HumanMessage(content="Here are the contents of the documents:\n\n### AI Agents Overview 2023\n\n**AI Agents Overview 2023**\n\nAI agents are sophisticated technologies that automate and enhance various processes across industries, becoming increasingly integral to business operations. In 2023, these agents are notable for their advanced capabilities in communication, data visualization, and language processing.\n\n**Popular AI Agents in 2023:**\n1. **Auto GPT**: This agent is renowned for its seamless integration abilities, significantly impacting industries by improving communication and operational workflows.\n2. **ChartGPT**: Specializing in data visualization, ChartGPT enables users to interact with data innovatively, providing deeper insights and comprehension.\n3. **LLMops**: With advanced language capabilities, LLMops is a versatile tool seeing widespread use across multiple sectors.\n\n**Market Trends:**\nThe AI agents market is experiencing rapid growth, with significant advancements anticipated by 2030. There's a growing demand for AI agents in personalized interactions, particularly within customer service, healthcare, and marketing sectors. This trend is fueled by the need for more efficient and tailored customer experiences.\n\n**Key Players:**\nLeading companies such as Microsoft, IBM, Google, Oracle, and AWS are key players in the AI agents market, highlighting the widespread adoption and investment in these technologies.\n\n**Technological Innovations:**\nAI agents are being developed alongside simulation technologies for robust testing and deployment environments. Innovations in generative AI are accelerating, supported by advancements in large language models and platforms like ChatGPT.\n\n**Applications in Healthcare:**\nIn healthcare, AI agents are automating routine tasks, allowing medical professionals to focus more on patient care. They're poised to significantly enhance healthcare delivery and efficiency.\n\n**Future Prospects:**\nThe future of AI agents is promising, with continued evolution and integration into various platforms and ecosystems, offering more seamless and intelligent interactions. As these technologies advance, they are expected to redefine business operations and customer interactions.\n\n### AI_Agents_Overview_2023_Outline\n\n1. Introduction to AI Agents in 2023\n2. Popular AI Agents: Auto GPT, ChartGPT, LLMops\n3. Market Trends and Growth\n4. Key Players in the AI Agents Market\n5. Technological Innovations: Simulation and Generative AI\n6. Applications of AI Agents in Healthcare\n7. Future Prospects of AI Agents", additional_kwargs={}, response_metadata={}, name='writing_team', id='851bd8a6-740e-488c-8928-1f9e05e96ea0')]}}
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-19-8)---
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-19-9){'supervisor': {'next': 'writing_team'}}
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-19-10)---
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-19-11){'writing_team': {'messages': [HumanMessage(content='The documents have been successfully created and saved:\n\n1. **AI_Agents_Overview_2023.txt** - Contains the detailed overview of AI agents in 2023.\n2. **AI_Agents_Overview_2023_Outline.txt** - Contains the outline of the document.', additional_kwargs={}, response_metadata={}, name='writing_team', id='c87c0778-a085-4a8e-8ee1-9b43b9b0b143')]}}
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-19-12)---
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-19-13){'supervisor': {'next': '__end__'}}
[](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__codelineno-19-14)---

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Multi-agent supervisor  ](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/agent_supervisor/) [ Next  Plan-and-Execute  ](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
