---
url: https://langchain-ai.github.io/langgraph/tutorials/storm/storm/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#web-research-storm)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Web Research (STORM) 

[ ](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/?q= "Share")

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
        * [ Agent Architectures  ](https://langchain-ai.github.io/langgraph/tutorials#agent-architectures)
        * [ Evaluation & Analysis  ](https://langchain-ai.github.io/langgraph/tutorials#evaluation)
        * Experimental  Experimental 
          * [ Experimental  ](https://langchain-ai.github.io/langgraph/tutorials#experimental)
          * Web Research (STORM)  [ Web Research (STORM)  ](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/) Table of contents 
            * [ Setup  ](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#setup)
              * [ Select LLMs  ](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#select-llms)
            * [ Generate Initial Outline  ](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#generate-initial-outline)
            * [ Expand Topics  ](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#expand-topics)
            * [ Generate Perspectives  ](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#generate-perspectives)
            * [ Expert Dialog  ](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#expert-dialog)
              * [ Interview State  ](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#interview-state)
                * [ Dialog Roles  ](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#dialog-roles)
                * [ Answer questions  ](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#answer-questions)
                * [ Construct the Interview Graph  ](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#construct-the-interview-graph)
            * [ Refine Outline  ](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#refine-outline)
            * [ Generate Article  ](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#generate-article)
              * [ Create Retriever  ](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#create-retriever)
              * [ Generate Sections  ](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#generate-sections)
              * [ Generate final article  ](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#generate-final-article)
            * [ Final Flow  ](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#final-flow)
              * [ Create the graph  ](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#create-the-graph)
            * [ Render the Wiki  ](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#render-the-wiki)
          * [ TNT-LLM: Text Mining at Scale  ](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/)
          * [ Web Voyager  ](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/)
          * [ Competitive Programming  ](https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/)
          * [ Complex data extraction with function calling  ](https://langchain-ai.github.io/langgraph/tutorials/extraction/retries/)
        * [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/concepts#langgraph-platform)
    * Resources  Resources 
      * [ Prebuilt Agents  ](https://langchain-ai.github.io/langgraph/prebuilt/)
      * [ Adopters  ](https://langchain-ai.github.io/langgraph/adopters/)
      * [ FAQ  ](https://langchain-ai.github.io/langgraph/concepts/faq/)
      * [ Troubleshooting  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraph/reference/graphs/)



Table of contents 

  * [ Setup  ](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#setup)
    * [ Select LLMs  ](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#select-llms)
  * [ Generate Initial Outline  ](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#generate-initial-outline)
  * [ Expand Topics  ](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#expand-topics)
  * [ Generate Perspectives  ](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#generate-perspectives)
  * [ Expert Dialog  ](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#expert-dialog)
    * [ Interview State  ](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#interview-state)
      * [ Dialog Roles  ](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#dialog-roles)
      * [ Answer questions  ](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#answer-questions)
      * [ Construct the Interview Graph  ](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#construct-the-interview-graph)
  * [ Refine Outline  ](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#refine-outline)
  * [ Generate Article  ](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#generate-article)
    * [ Create Retriever  ](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#create-retriever)
    * [ Generate Sections  ](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#generate-sections)
    * [ Generate final article  ](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#generate-final-article)
  * [ Final Flow  ](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#final-flow)
    * [ Create the graph  ](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#create-the-graph)
  * [ Render the Wiki  ](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#render-the-wiki)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ Tutorials  ](https://langchain-ai.github.io/langgraph/tutorials/)
  4. [ Experimental  ](https://langchain-ai.github.io/langgraph/tutorials#experimental)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/tutorials/storm/storm.ipynb "Edit this page")

# Web Research (STORM)[¶](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#web-research-storm "Permanent link")

[STORM](https://arxiv.org/abs/2402.14207) is a research assistant designed by Shao, et. al that extends the idea of "outline-driven RAG" for richer article generation.

STORM is designed to generate Wikipedia-style ariticles on a user-provided topic. It applies two main insights to produce more organized and comprehensive articles:

  1. Creating an outline (planning) by querying similar topics helps improve coverage.
  2. Multi-perspective, grounded (in search) conversation simulation helps increase the reference count and information density. 



The control flow looks like the diagram below.

![storm.png]()

STORM has a few main stages:

  1. Generate initial outline + Survey related subjects
  2. Identify distinct perspectives
  3. "Interview subject matter experts" (role-playing LLMs)
  4. Refine outline (using references)
  5. Write sections, then write article



The expert interviews stage occurs between the role-playing article writer and a research expert. The "expert" is able to query external knowledge and respond to pointed questions, saving cited sources to a vectorstore so that the later refinement stages can synthesize the full article.

There are a couple hyperparameters you can set to restrict the (potentially) infinite research breadth:

N: Number of perspectives to survey / use (Steps 2->3) M: Max number of conversation turns in step (Step 3)

## Setup[¶](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#setup "Permanent link")

First, let's install the required packages and set our API keys

```
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-0-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-0-2)%pip install -U langchain_community langchain_openai langchain_fireworks langgraph wikipedia duckduckgo-search tavily-python

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-1-1)# Uncomment if you want to draw the pretty graph diagrams.
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-1-2)# If you are on MacOS, you will need to run brew install graphviz before installing and update some environment flags
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-1-3)# ! brew install graphviz
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-1-4)# !CFLAGS="-I $(brew --prefix graphviz)/include" LDFLAGS="-L $(brew --prefix graphviz)/lib" pip install -U pygraphviz

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-2-1)importgetpass
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-2-2)importos
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-2-3)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-2-4)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-2-5)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-2-6)  if os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-2-7)    return
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-2-8)  os.environ[var] = getpass.getpass(var + ":")
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-2-9)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-2-10)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-2-11)_set_env("OPENAI_API_KEY")
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-2-12)_set_env("TAVILY_API_KEY")

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

### Select LLMs[¶](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#select-llms "Permanent link")

We will have a faster LLM do most of the work, but a slower, long-context model to distill the conversations and write the final report.

```
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-3-1)fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-3-2)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-3-3)fast_llm = ChatOpenAI(model="gpt-4o-mini")
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-3-4)# Uncomment for a Fireworks model
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-3-5)# fast_llm = ChatFireworks(model="accounts/fireworks/models/firefunction-v1", max_tokens=32_000)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-3-6)long_context_llm = ChatOpenAI(model="gpt-4o")

```


API Reference: [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html)

## Generate Initial Outline[¶](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#generate-initial-outline "Permanent link")

For many topics, your LLM may have an initial idea of the important and related topics. We can generate an initial outline to be refined after our research. Below, we will use our "fast" llm to generate the outline.

Using Pydantic with LangChain

This notebook uses Pydantic v2 `BaseModel`, which requires `langchain-core >= 0.3`. Using `langchain-core < 0.3` will result in errors due to mixing of Pydantic v1 and v2 `BaseModels`. 

```
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-1)fromtypingimport List, Optional
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-2)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-3)fromlangchain_core.promptsimport ChatPromptTemplate
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-4)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-5)frompydanticimport BaseModel, Field
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-6)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-7)direct_gen_outline_prompt = ChatPromptTemplate.from_messages(
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-8)  [
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-9)    (
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-10)      "system",
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-11)      "You are a Wikipedia writer. Write an outline for a Wikipedia page about a user-provided topic. Be comprehensive and specific.",
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-12)    ),
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-13)    ("user", "{topic}"),
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-14)  ]
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-15))
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-16)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-17)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-18)classSubsection(BaseModel):
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-19)  subsection_title: str = Field(..., title="Title of the subsection")
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-20)  description: str = Field(..., title="Content of the subsection")
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-21)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-22)  @property
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-23)  defas_str(self) -> str:
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-24)    return f"### {self.subsection_title}\n\n{self.description}".strip()
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-25)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-26)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-27)classSection(BaseModel):
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-28)  section_title: str = Field(..., title="Title of the section")
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-29)  description: str = Field(..., title="Content of the section")
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-30)  subsections: Optional[List[Subsection]] = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-31)    default=None,
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-32)    title="Titles and descriptions for each subsection of the Wikipedia page.",
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-33)  )
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-34)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-35)  @property
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-36)  defas_str(self) -> str:
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-37)    subsections = "\n\n".join(
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-38)      f"### {subsection.subsection_title}\n\n{subsection.description}"
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-39)      for subsection in self.subsections or []
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-40)    )
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-41)    return f"## {self.section_title}\n\n{self.description}\n\n{subsections}".strip()
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-42)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-43)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-44)classOutline(BaseModel):
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-45)  page_title: str = Field(..., title="Title of the Wikipedia page")
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-46)  sections: List[Section] = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-47)    default_factory=list,
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-48)    title="Titles and descriptions for each section of the Wikipedia page.",
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-49)  )
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-50)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-51)  @property
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-52)  defas_str(self) -> str:
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-53)    sections = "\n\n".join(section.as_str for section in self.sections)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-54)    return f"# {self.page_title}\n\n{sections}".strip()
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-55)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-56)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-57)generate_outline_direct = direct_gen_outline_prompt | fast_llm.with_structured_output(
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-58)  Outline
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-4-59))

```


API Reference: [ChatPromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html)

```
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-5-1)example_topic = "Impact of million-plus token context window language models on RAG"
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-5-2)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-5-3)initial_outline = generate_outline_direct.invoke({"topic": example_topic})
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-5-4)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-5-5)print(initial_outline.as_str)

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-6-1)# Impact of million-plus token context window language models on RAG
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-6-2)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-6-3)## Introduction
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-6-4)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-6-5)Brief overview of million-plus token context window language models and RAG.
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-6-6)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-6-7)## Million-Plus Token Context Window Language Models
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-6-8)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-6-9)Explanation of million-plus token context window language models, their architecture, training process, and capabilities.
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-6-10)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-6-11)## Retrieval-Augmented Generation (RAG)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-6-12)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-6-13)Explanation of RAG model, its components, and how it combines information retrieval with text generation.
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-6-14)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-6-15)## Impact on RAG
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-6-16)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-6-17)Discussion on how million-plus token context window language models impact RAG, including improvements in performance, efficiency, and potential challenges.

```


## Expand Topics[¶](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#expand-topics "Permanent link")

While language models do store some Wikipedia-like knowledge in their parameters, you will get better results by incorporating relevant and recent information using a search engine.

We will start our search by generating a list of related topics, sourced from Wikipedia.

```
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-7-1)gen_related_topics_prompt = ChatPromptTemplate.from_template(
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-7-2)"""I'm writing a Wikipedia page for a topic mentioned below. Please identify and recommend some Wikipedia pages on closely related subjects. I'm looking for examples that provide insights into interesting aspects commonly associated with this topic, or examples that help me understand the typical content and structure included in Wikipedia pages for similar topics.
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-7-3)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-7-4)Please list the as many subjects and urls as you can.
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-7-5)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-7-6)Topic of interest: {topic}
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-7-7)"""
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-7-8))
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-7-9)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-7-10)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-7-11)classRelatedSubjects(BaseModel):
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-7-12)  topics: List[str] = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-7-13)    description="Comprehensive list of related subjects as background research.",
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-7-14)  )
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-7-15)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-7-16)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-7-17)expand_chain = gen_related_topics_prompt | fast_llm.with_structured_output(
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-7-18)  RelatedSubjects
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-7-19))

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-8-1)related_subjects = await expand_chain.ainvoke({"topic": example_topic})
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-8-2)related_subjects

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-9-1)RelatedSubjects(topics=['million-plus token context window language models', 'RAG'])

```


## Generate Perspectives[¶](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#generate-perspectives "Permanent link")

From these related subjects, we can select representative Wikipedia editors as "subject matter experts" with distinct backgrounds and affiliations. These will help distribute the search process to encourage a more well-rounded final report.

```
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-10-1)classEditor(BaseModel):
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-10-2)  affiliation: str = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-10-3)    description="Primary affiliation of the editor.",
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-10-4)  )
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-10-5)  name: str = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-10-6)    description="Name of the editor.", pattern=r"^[a-zA-Z0-9_-]{1,64}$"
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-10-7)  )
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-10-8)  role: str = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-10-9)    description="Role of the editor in the context of the topic.",
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-10-10)  )
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-10-11)  description: str = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-10-12)    description="Description of the editor's focus, concerns, and motives.",
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-10-13)  )
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-10-14)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-10-15)  @property
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-10-16)  defpersona(self) -> str:
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-10-17)    return f"Name: {self.name}\nRole: {self.role}\nAffiliation: {self.affiliation}\nDescription: {self.description}\n"
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-10-18)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-10-19)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-10-20)classPerspectives(BaseModel):
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-10-21)  editors: List[Editor] = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-10-22)    description="Comprehensive list of editors with their roles and affiliations.",
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-10-23)    # Add a pydantic validation/restriction to be at most M editors
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-10-24)  )
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-10-25)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-10-26)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-10-27)gen_perspectives_prompt = ChatPromptTemplate.from_messages(
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-10-28)  [
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-10-29)    (
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-10-30)      "system",
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-10-31)"""You need to select a diverse (and distinct) group of Wikipedia editors who will work together to create a comprehensive article on the topic. Each of them represents a different perspective, role, or affiliation related to this topic.\
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-10-32)  You can use other Wikipedia pages of related topics for inspiration. For each editor, add a description of what they will focus on.
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-10-33)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-10-34)  Wiki page outlines of related topics for inspiration:
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-10-35)  {examples}""",
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-10-36)    ),
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-10-37)    ("user", "Topic of interest: {topic}"),
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-10-38)  ]
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-10-39))
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-10-40)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-10-41)gen_perspectives_chain = gen_perspectives_prompt | ChatOpenAI(
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-10-42)  model="gpt-3.5-turbo"
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-10-43)).with_structured_output(Perspectives)

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-11-1)fromlangchain_community.retrieversimport WikipediaRetriever
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-11-2)fromlangchain_core.runnablesimport RunnableLambda
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-11-3)fromlangchain_core.runnablesimport chain as as_runnable
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-11-4)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-11-5)wikipedia_retriever = WikipediaRetriever(load_all_available_meta=True, top_k_results=1)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-11-6)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-11-7)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-11-8)defformat_doc(doc, max_length=1000):
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-11-9)  related = "- ".join(doc.metadata["categories"])
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-11-10)  return f"### {doc.metadata['title']}\n\nSummary: {doc.page_content}\n\nRelated\n{related}"[
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-11-11)    :max_length
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-11-12)  ]
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-11-13)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-11-14)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-11-15)defformat_docs(docs):
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-11-16)  return "\n\n".join(format_doc(doc) for doc in docs)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-11-17)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-11-18)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-11-19)@as_runnable
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-11-20)async defsurvey_subjects(topic: str):
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-11-21)  related_subjects = await expand_chain.ainvoke({"topic": topic})
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-11-22)  retrieved_docs = await wikipedia_retriever.abatch(
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-11-23)    related_subjects.topics, return_exceptions=True
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-11-24)  )
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-11-25)  all_docs = []
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-11-26)  for docs in retrieved_docs:
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-11-27)    if isinstance(docs, BaseException):
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-11-28)      continue
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-11-29)    all_docs.extend(docs)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-11-30)  formatted = format_docs(all_docs)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-11-31)  return await gen_perspectives_chain.ainvoke({"examples": formatted, "topic": topic})

```


API Reference: [WikipediaRetriever](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.wikipedia.WikipediaRetriever.html) | [RunnableLambda](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.RunnableLambda.html) | [chain](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.chain.html)

```
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-12-1)perspectives = await survey_subjects.ainvoke(example_topic)

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-13-1)perspectives.dict()

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-14-1){'editors': [{'affiliation': 'Research Institution',
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-14-2)  'name': 'AliceResearcher',
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-14-3)  'role': 'Researcher',
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-14-4)  'description': 'AliceResearcher focuses on the impact of million-plus token context window language models on the Retrieval-Augmented Generation (RAG) framework. They analyze the effectiveness of large language models within the RAG framework and investigate how these models influence information retrieval and generation tasks.'},
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-14-5) {'affiliation': 'Tech Company',
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-14-6)  'name': 'BobEngineer',
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-14-7)  'role': 'Engineer',
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-14-8)  'description': 'BobEngineer specializes in implementing million-plus token context window language models in practical applications, particularly within the Retrieval-Augmented Generation (RAG) framework. They focus on optimizing the performance and efficiency of these models for real-world usage.'},
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-14-9) {'affiliation': 'Academic Institution',
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-14-10)  'name': 'CharlieAcademic',
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-14-11)  'role': 'Academic',
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-14-12)  'description': 'CharlieAcademic studies the theoretical implications of integrating million-plus token context window language models with the RAG framework. They explore the broader implications of using such large models for natural language processing and information retrieval.'},
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-14-13) {'affiliation': 'Industry Expert',
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-14-14)  'name': 'DianaExpert',
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-14-15)  'role': 'Industry Expert',
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-14-16)  'description': 'DianaExpert provides insights from the industry perspective on the impact of million-plus token context window language models on RAG. They focus on practical applications, challenges, and opportunities that arise when utilizing these models in commercial settings.'},
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-14-17) {'affiliation': 'AI Ethics Organization',
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-14-18)  'name': 'EveEthicist',
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-14-19)  'role': 'Ethicist',
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-14-20)  'description': 'EveEthicist examines the ethical considerations surrounding the use of million-plus token context window language models in the context of RAG. They focus on potential biases, fairness, and transparency issues that may arise from the deployment of such models.'}]}

```


## Expert Dialog[¶](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#expert-dialog "Permanent link")

Now the true fun begins, each wikipedia writer is primed to role-play using the perspectives presented above. It will ask a series of questions of a second "domain expert" with access to a search engine. This generate content to generate a refined outline as well as an updated index of reference documents.

### Interview State[¶](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#interview-state "Permanent link")

The conversation is cyclic, so we will construct it within its own graph. The State will contain messages, the reference docs, and the editor (with its own "persona") to make it easy to parallelize these conversations.

```
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-15-1)fromtypingimport Annotated
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-15-2)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-15-3)fromlangchain_core.messagesimport AnyMessage
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-15-4)fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-15-5)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-15-6)fromlanggraph.graphimport END, StateGraph, START
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-15-7)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-15-8)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-15-9)defadd_messages(left, right):
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-15-10)  if not isinstance(left, list):
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-15-11)    left = [left]
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-15-12)  if not isinstance(right, list):
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-15-13)    right = [right]
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-15-14)  return left + right
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-15-15)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-15-16)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-15-17)defupdate_references(references, new_references):
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-15-18)  if not references:
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-15-19)    references = {}
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-15-20)  references.update(new_references)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-15-21)  return references
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-15-22)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-15-23)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-15-24)defupdate_editor(editor, new_editor):
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-15-25)  # Can only set at the outset
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-15-26)  if not editor:
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-15-27)    return new_editor
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-15-28)  return editor
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-15-29)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-15-30)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-15-31)classInterviewState(TypedDict):
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-15-32)  messages: Annotated[List[AnyMessage], add_messages]
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-15-33)  references: Annotated[Optional[dict], update_references]
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-15-34)  editor: Annotated[Optional[Editor], update_editor]

```


API Reference: [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START)

#### Dialog Roles[¶](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#dialog-roles "Permanent link")

The graph will have two participants: the wikipedia editor (`generate_question`), who asks questions based on its assigned role, and a domain expert (`gen_answer_chain), who uses a search engine to answer the questions as accurately as possible.

```
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-16-1)fromlangchain_core.messagesimport AIMessage, HumanMessage, ToolMessage
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-16-2)fromlangchain_core.promptsimport MessagesPlaceholder
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-16-3)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-16-4)gen_qn_prompt = ChatPromptTemplate.from_messages(
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-16-5)  [
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-16-6)    (
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-16-7)      "system",
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-16-8)"""You are an experienced Wikipedia writer and want to edit a specific page. \
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-16-9)Besides your identity as a Wikipedia writer, you have a specific focus when researching the topic. \
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-16-10)Now, you are chatting with an expert to get information. Ask good questions to get more useful information.
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-16-11)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-16-12)When you have no more questions to ask, say "Thank you so much for your help!" to end the conversation.\
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-16-13)Please only ask one question at a time and don't ask what you have asked before.\
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-16-14)Your questions should be related to the topic you want to write.
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-16-15)Be comprehensive and curious, gaining as much unique insight from the expert as possible.\
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-16-16)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-16-17)Stay true to your specific perspective:
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-16-18)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-16-19){persona}""",
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-16-20)    ),
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-16-21)    MessagesPlaceholder(variable_name="messages", optional=True),
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-16-22)  ]
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-16-23))
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-16-24)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-16-25)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-16-26)deftag_with_name(ai_message: AIMessage, name: str):
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-16-27)  ai_message.name = name
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-16-28)  return ai_message
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-16-29)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-16-30)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-16-31)defswap_roles(state: InterviewState, name: str):
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-16-32)  converted = []
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-16-33)  for message in state["messages"]:
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-16-34)    if isinstance(message, AIMessage) and message.name != name:
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-16-35)      message = HumanMessage(**message.dict(exclude={"type"}))
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-16-36)    converted.append(message)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-16-37)  return {"messages": converted}
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-16-38)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-16-39)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-16-40)@as_runnable
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-16-41)async defgenerate_question(state: InterviewState):
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-16-42)  editor = state["editor"]
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-16-43)  gn_chain = (
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-16-44)    RunnableLambda(swap_roles).bind(name=editor.name)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-16-45)    | gen_qn_prompt.partial(persona=editor.persona)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-16-46)    | fast_llm
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-16-47)    | RunnableLambda(tag_with_name).bind(name=editor.name)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-16-48)  )
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-16-49)  result = await gn_chain.ainvoke(state)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-16-50)  return {"messages": [result]}

```


API Reference: [AIMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.AIMessage.html) | [HumanMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.human.HumanMessage.html) | [ToolMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.tool.ToolMessage.html) | [MessagesPlaceholder](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.MessagesPlaceholder.html)

```
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-17-1)messages = [
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-17-2)  HumanMessage(f"So you said you were writing an article on {example_topic}?")
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-17-3)]
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-17-4)question = await generate_question.ainvoke(
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-17-5)  {
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-17-6)    "editor": perspectives.editors[0],
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-17-7)    "messages": messages,
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-17-8)  }
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-17-9))
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-17-10)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-17-11)question["messages"][0].content

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-18-1)"Yes, that's correct. I focus on studying the impact of million-plus token context window language models on the Retrieval-Augmented Generation (RAG) framework. I analyze how these large language models affect information retrieval and generation tasks within the RAG framework. Is there a specific aspect of this topic that you would like to know more about?"

```


#### Answer questions[¶](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#answer-questions "Permanent link")

The `gen_answer_chain` first generates queries (query expansion) to answer the editor's question, then responds with citations.

```
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-19-1)classQueries(BaseModel):
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-19-2)  queries: List[str] = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-19-3)    description="Comprehensive list of search engine queries to answer the user's questions.",
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-19-4)  )
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-19-5)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-19-6)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-19-7)gen_queries_prompt = ChatPromptTemplate.from_messages(
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-19-8)  [
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-19-9)    (
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-19-10)      "system",
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-19-11)      "You are a helpful research assistant. Query the search engine to answer the user's questions.",
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-19-12)    ),
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-19-13)    MessagesPlaceholder(variable_name="messages", optional=True),
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-19-14)  ]
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-19-15))
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-19-16)gen_queries_chain = gen_queries_prompt | ChatOpenAI(
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-19-17)  model="gpt-3.5-turbo"
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-19-18)).with_structured_output(Queries, include_raw=True)

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-20-1)queries = await gen_queries_chain.ainvoke(
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-20-2)  {"messages": [HumanMessage(content=question["messages"][0].content)]}
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-20-3))
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-20-4)queries["parsed"].queries

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-21-1)['impact of million-plus token context window language models on Retrieval-Augmented Generation (RAG) framework',
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-21-2) 'information retrieval tasks in the RAG framework with large language models',
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-21-3) 'generation tasks in the RAG framework with million-plus token context window models']

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-22-1)classAnswerWithCitations(BaseModel):
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-22-2)  answer: str = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-22-3)    description="Comprehensive answer to the user's question with citations.",
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-22-4)  )
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-22-5)  cited_urls: List[str] = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-22-6)    description="List of urls cited in the answer.",
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-22-7)  )
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-22-8)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-22-9)  @property
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-22-10)  defas_str(self) -> str:
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-22-11)    return f"{self.answer}\n\nCitations:\n\n" + "\n".join(
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-22-12)      f"[{i+1}]: {url}" for i, url in enumerate(self.cited_urls)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-22-13)    )
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-22-14)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-22-15)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-22-16)gen_answer_prompt = ChatPromptTemplate.from_messages(
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-22-17)  [
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-22-18)    (
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-22-19)      "system",
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-22-20)"""You are an expert who can use information effectively. You are chatting with a Wikipedia writer who wants\
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-22-21) to write a Wikipedia page on the topic you know. You have gathered the related information and will now use the information to form a response.
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-22-22)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-22-23)Make your response as informative as possible and make sure every sentence is supported by the gathered information.
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-22-24)Each response must be backed up by a citation from a reliable source, formatted as a footnote, reproducing the URLS after your response.""",
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-22-25)    ),
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-22-26)    MessagesPlaceholder(variable_name="messages", optional=True),
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-22-27)  ]
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-22-28))
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-22-29)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-22-30)gen_answer_chain = gen_answer_prompt | fast_llm.with_structured_output(
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-22-31)  AnswerWithCitations, include_raw=True
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-22-32)).with_config(run_name="GenerateAnswer")

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-23-1)fromlangchain_community.utilities.duckduckgo_searchimport DuckDuckGoSearchAPIWrapper
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-23-2)fromlangchain_core.toolsimport tool
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-23-3)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-23-4)'''
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-23-5)# Tavily is typically a better search engine, but your free queries are limited
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-23-6)search_engine = TavilySearchResults(max_results=4)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-23-7)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-23-8)@tool
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-23-9)async def search_engine(query: str):
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-23-10)  """Search engine to the internet."""
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-23-11)  results = tavily_search.invoke(query)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-23-12)  return [{"content": r["content"], "url": r["url"]} for r in results]
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-23-13)'''
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-23-14)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-23-15)# DDG
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-23-16)search_engine = DuckDuckGoSearchAPIWrapper()
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-23-17)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-23-18)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-23-19)@tool
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-23-20)async defsearch_engine(query: str):
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-23-21)"""Search engine to the internet."""
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-23-22)  results = DuckDuckGoSearchAPIWrapper()._ddgs_text(query)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-23-23)  return [{"content": r["body"], "url": r["href"]} for r in results]

```


API Reference: [DuckDuckGoSearchAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.duckduckgo_search.DuckDuckGoSearchAPIWrapper.html) | [tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html)

```
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-24-1)importjson
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-24-2)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-24-3)fromlangchain_core.runnablesimport RunnableConfig
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-24-4)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-24-5)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-24-6)async defgen_answer(
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-24-7)  state: InterviewState,
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-24-8)  config: Optional[RunnableConfig] = None,
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-24-9)  name: str = "Subject_Matter_Expert",
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-24-10)  max_str_len: int = 15000,
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-24-11)):
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-24-12)  swapped_state = swap_roles(state, name) # Convert all other AI messages
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-24-13)  queries = await gen_queries_chain.ainvoke(swapped_state)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-24-14)  query_results = await search_engine.abatch(
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-24-15)    queries["parsed"].queries, config, return_exceptions=True
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-24-16)  )
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-24-17)  successful_results = [
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-24-18)    res for res in query_results if not isinstance(res, Exception)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-24-19)  ]
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-24-20)  all_query_results = {
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-24-21)    res["url"]: res["content"] for results in successful_results for res in results
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-24-22)  }
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-24-23)  # We could be more precise about handling max token length if we wanted to here
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-24-24)  dumped = json.dumps(all_query_results)[:max_str_len]
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-24-25)  ai_message: AIMessage = queries["raw"]
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-24-26)  tool_call = queries["raw"].tool_calls[0]
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-24-27)  tool_id = tool_call["id"]
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-24-28)  tool_message = ToolMessage(tool_call_id=tool_id, content=dumped)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-24-29)  swapped_state["messages"].extend([ai_message, tool_message])
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-24-30)  # Only update the shared state with the final answer to avoid
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-24-31)  # polluting the dialogue history with intermediate messages
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-24-32)  generated = await gen_answer_chain.ainvoke(swapped_state)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-24-33)  cited_urls = set(generated["parsed"].cited_urls)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-24-34)  # Save the retrieved information to a the shared state for future reference
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-24-35)  cited_references = {k: v for k, v in all_query_results.items() if k in cited_urls}
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-24-36)  formatted_message = AIMessage(name=name, content=generated["parsed"].as_str)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-24-37)  return {"messages": [formatted_message], "references": cited_references}

```


API Reference: [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html)

```
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-25-1)example_answer = await gen_answer(
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-25-2)  {"messages": [HumanMessage(content=question["messages"][0].content)]}
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-25-3))
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-25-4)example_answer["messages"][-1].content

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-26-1)'Studying the impact of million-plus token context window language models on the Retrieval-Augmented Generation (RAG) framework involves analyzing how these large language models affect information retrieval and generation tasks within the RAG framework. The introduction of large language models with extensive context windows, such as Google Gemini 1.5 Pro with a record 1 million token context window, has sparked discussions in the AI community about the potential implications for RAG. While there are concerns about the negative impact of supermassive context windows on RAG, there is also a recognition of the benefits they bring, enabling more use cases and enhancing performance in knowledge-intensive tasks. Retrieval-Augmented Generation (RAG) combines the generative capabilities of transformer architectures with dynamic information retrieval, allowing large language models to access and integrate relevant external knowledge during text generation, leading to more accurate and credible outputs. RAG has been identified as a valuable solution to address challenges faced by Large Language Models (LLMs), such as hallucination, outdated knowledge, lack of transparency, and untraceable reasoning processes. By incorporating external databases, RAG improves the consistency and coherence of generated content, especially in conversational question answering tasks. RAG has also been recognized as a powerful tool for large language models to efficiently process overly lengthy contexts, with recent LLMs like Gemini-1.5 and GPT-4 showcasing exceptional capabilities in understanding long contexts directly. There is ongoing research and benchmarking to compare the strengths of RAG and long-context LLMs, aiming to leverage the advantages of both approaches for enhanced performance in information retrieval and generation tasks within the RAG framework.\n\nCitations:\n\n[1]: https://thenewstack.io/do-enormous-llm-context-windows-spell-the-end-of-rag/\n[2]: https://medium.com/enterprise-rag/why-gemini-1-5-and-other-large-context-models-are-bullish-for-rag-ce3218930bb4\n[3]: https://medium.com/@amanatulla1606/rag-is-here-to-stay-four-reasons-why-large-context-windows-cant-replace-it-ad112013de25\n[4]: https://www.freecodecamp.org/news/retrieval-augmented-generation-rag-handbook/\n[5]: https://www.deepset.ai/blog/long-context-llms-rag\n[6]: https://arxiv.org/abs/2312.10997\n[7]: https://arxiv.org/abs/2409.13385\n[8]: https://irisagent.com/blog/enhancing-large-language-models-a-deep-dive-into-rag-llm-technology/\n[9]: https://arxiv.org/abs/2407.16833'

```


#### Construct the Interview Graph[¶](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#construct-the-interview-graph "Permanent link")

Now that we've defined the editor and domain expert, we can compose them in a graph.

```
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-27-1)max_num_turns = 5
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-27-2)fromlanggraph.pregelimport RetryPolicy
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-27-3)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-27-4)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-27-5)defroute_messages(state: InterviewState, name: str = "Subject_Matter_Expert"):
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-27-6)  messages = state["messages"]
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-27-7)  num_responses = len(
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-27-8)    [m for m in messages if isinstance(m, AIMessage) and m.name == name]
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-27-9)  )
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-27-10)  if num_responses >= max_num_turns:
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-27-11)    return END
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-27-12)  last_question = messages[-2]
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-27-13)  if last_question.content.endswith("Thank you so much for your help!"):
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-27-14)    return END
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-27-15)  return "ask_question"
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-27-16)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-27-17)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-27-18)builder = StateGraph(InterviewState)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-27-19)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-27-20)builder.add_node("ask_question", generate_question, retry=RetryPolicy(max_attempts=5))
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-27-21)builder.add_node("answer_question", gen_answer, retry=RetryPolicy(max_attempts=5))
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-27-22)builder.add_conditional_edges("answer_question", route_messages)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-27-23)builder.add_edge("ask_question", "answer_question")
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-27-24)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-27-25)builder.add_edge(START, "ask_question")
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-27-26)interview_graph = builder.compile(checkpointer=False).with_config(
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-27-27)  run_name="Conduct Interviews"
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-27-28))

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-28-1)fromIPython.displayimport Image, display
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-28-2)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-28-3)try:
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-28-4)  display(Image(interview_graph.get_graph().draw_mermaid_png()))
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-28-5)except Exception:
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-28-6)  # This requires some extra dependencies and is optional
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-28-7)  pass

```


![]()

```
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-29-1)final_step = None
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-29-2)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-29-3)initial_state = {
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-29-4)  "editor": perspectives.editors[0],
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-29-5)  "messages": [
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-29-6)    AIMessage(
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-29-7)      content=f"So you said you were writing an article on {example_topic}?",
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-29-8)      name="Subject_Matter_Expert",
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-29-9)    )
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-29-10)  ],
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-29-11)}
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-29-12)async for step in interview_graph.astream(initial_state):
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-29-13)  name = next(iter(step))
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-29-14)  print(name)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-29-15)  print("-- ", str(step[name]["messages"])[:300])
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-29-16)final_step = step

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-30-1)ask_question
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-30-2)-- [AIMessage(content="Yes, that's correct. My focus is on how million-plus token context window language models impact the Retrieval-Augmented Generation (RAG) framework. I'm interested in understanding how the size and scope of these language models influence the effectiveness of the RAG framework in
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-30-3)answer_question
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-30-4)-- [AIMessage(content='The integration of million-plus token context window language models in the Retrieval-Augmented Generation (RAG) framework has emerged as a significant advancement in natural language processing. RAG has been a reliable solution for context-based answer generation, overcoming the
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-30-5)ask_question
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-30-6)-- [AIMessage(content='Can you elaborate on how the retrieval-augmented techniques in the RAG framework enhance the accuracy and relevance of the generated text by accessing external knowledge dynamically? How does this process differ from traditional language modeling approaches, and what specific ben
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-30-7)answer_question
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-30-8)-- [AIMessage(content='The integration of retrieval-augmented techniques in the RAG framework enhances the accuracy and relevance of generated text by dynamically accessing external knowledge sources to enrich the generation process. Unlike traditional language modeling approaches that rely solely on i
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-30-9)ask_question
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-30-10)-- [AIMessage(content='Thank you for the insightful information on how retrieval-augmented techniques enhance the accuracy and relevance of text generation in the RAG framework by incorporating external knowledge sources. How do these external knowledge sources impact the overall performance and adapta
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-30-11)answer_question
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-30-12)-- [AIMessage(content='External knowledge sources significantly impact the overall performance and adaptability of RAG models in handling various types of information retrieval and generation tasks. By leveraging external knowledge, RAG models access up-to-date information, reduce the incidence of gene
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-30-13)ask_question
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-30-14)-- [AIMessage(content='Thank you for sharing insights on how external knowledge sources impact the performance and adaptability of RAG models in handling diverse information retrieval and generation tasks. This information will be valuable for my research on the impact of million-plus token context win
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-30-15)answer_question
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-30-16)-- [AIMessage(content="The integration of million-plus token context window language models in the Retrieval-Augmented Generation (RAG) framework has sparked discussions in the AI community, with some concerns about the potential impact on RAG's relevance. However, RAG continues to be a valuable soluti

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-31-1)final_state = next(iter(final_step.values()))

```


## Refine Outline[¶](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#refine-outline "Permanent link")

At this point in STORM, we've conducted a large amount of research from different perspectives. It's time to refine the original outline based on these investigations. Below, create a chain using the LLM with a long context window to update the original outline.

```
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-32-1)refine_outline_prompt = ChatPromptTemplate.from_messages(
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-32-2)  [
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-32-3)    (
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-32-4)      "system",
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-32-5)"""You are a Wikipedia writer. You have gathered information from experts and search engines. Now, you are refining the outline of the Wikipedia page. \
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-32-6)You need to make sure that the outline is comprehensive and specific. \
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-32-7)Topic you are writing about: {topic} 
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-32-8)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-32-9)Old outline:
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-32-10)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-32-11){old_outline}""",
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-32-12)    ),
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-32-13)    (
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-32-14)      "user",
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-32-15)      "Refine the outline based on your conversations with subject-matter experts:\n\nConversations:\n\n{conversations}\n\nWrite the refined Wikipedia outline:",
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-32-16)    ),
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-32-17)  ]
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-32-18))
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-32-19)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-32-20)# Using turbo preview since the context can get quite long
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-32-21)refine_outline_chain = refine_outline_prompt | long_context_llm.with_structured_output(
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-32-22)  Outline
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-32-23))

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-33-1)refined_outline = refine_outline_chain.invoke(
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-33-2)  {
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-33-3)    "topic": example_topic,
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-33-4)    "old_outline": initial_outline.as_str,
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-33-5)    "conversations": "\n\n".join(
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-33-6)      f"### {m.name}\n\n{m.content}" for m in final_state["messages"]
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-33-7)    ),
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-33-8)  }
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-33-9))

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-34-1)print(refined_outline.as_str)

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-35-1)# Impact of million-plus token context window language models on RAG
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-35-2)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-35-3)## Introduction
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-35-4)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-35-5)Provides a brief overview of million-plus token context window language models and their relevance to Retrieval-Augmented Generation (RAG) systems, setting the stage for a deeper exploration of their impact.
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-35-6)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-35-7)## Background
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-35-8)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-35-9)A foundational section to understand the core concepts involved.
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-35-10)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-35-11)### Million-Plus Token Context Window Language Models
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-35-12)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-35-13)Explains what million-plus token context window language models are, including notable examples like Gemini 1.5, focusing on their architecture, training data, and the evolution of their applications.
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-35-14)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-35-15)### Retrieval-Augmented Generation (RAG)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-35-16)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-35-17)Describes the RAG framework, its unique approach of combining retrieval and generation models for enhanced natural language processing, and its significance in the AI landscape.
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-35-18)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-35-19)## Impact on RAG Systems
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-35-20)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-35-21)Delves into the effects of million-plus token context window language models on RAG, highlighting both the challenges and opportunities presented.
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-35-22)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-35-23)### Performance and Efficiency
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-35-24)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-35-25)Discusses how large context window models influence RAG performance, including aspects of latency, computational demands, and overall efficiency.
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-35-26)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-35-27)### Generation Quality and Diversity
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-35-28)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-35-29)Explores the impact on generation quality, the potential for more accurate and diverse outputs, and how these models address data biases and factual accuracy.
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-35-30)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-35-31)### Technical Challenges
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-35-32)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-35-33)Identifies specific technical hurdles such as prompt template design, context length limitations, and similarity searches in vector databases, and how they affect RAG systems.
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-35-34)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-35-35)### Opportunities and Advancements
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-35-36)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-35-37)Outlines the new capabilities and improvements in agent interaction, information retrieval, and response relevance that these models bring to RAG systems.
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-35-38)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-35-39)## Future Directions
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-35-40)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-35-41)Considers ongoing research and potential future developments in the integration of million-plus token context window language models with RAG systems, including speculation on emerging trends and technologies.
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-35-42)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-35-43)## Conclusion
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-35-44)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-35-45)Summarizes the key points discussed in the article, reaffirming the significant impact of million-plus token context window language models on RAG systems.

```


## Generate Article[¶](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#generate-article "Permanent link")

Now it's time to generate the full article. We will first divide-and-conquer, so that each section can be tackled by an individual llm. Then we will prompt the long-form LLM to refine the finished article (since each section may use an inconsistent voice).

#### Create Retriever[¶](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#create-retriever "Permanent link")

The research process uncovers a large number of reference documents that we may want to query during the final article-writing process.

First, create the retriever:

```
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-36-1)fromlangchain_community.vectorstoresimport InMemoryVectorStore
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-36-2)fromlangchain_core.documentsimport Document
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-36-3)fromlangchain_openaiimport OpenAIEmbeddings
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-36-4)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-36-5)embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-36-6)reference_docs = [
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-36-7)  Document(page_content=v, metadata={"source": k})
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-36-8)  for k, v in final_state["references"].items()
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-36-9)]
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-36-10)# This really doesn't need to be a vectorstore for this size of data.
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-36-11)# It could just be a numpy matrix. Or you could store documents
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-36-12)# across requests if you want.
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-36-13)vectorstore = InMemoryVectorStore.from_documents(
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-36-14)  reference_docs,
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-36-15)  embedding=embeddings,
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-36-16))
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-36-17)retriever = vectorstore.as_retriever(k=3)

```


API Reference: [InMemoryVectorStore](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.in_memory.InMemoryVectorStore.html) | [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html) | [OpenAIEmbeddings](https://python.langchain.com/api_reference/openai/embeddings/langchain_openai.embeddings.base.OpenAIEmbeddings.html)

```
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-37-1)retriever.invoke("What's a long context LLM anyway?")

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-38-1)[Document(page_content='In Retrieval Augmented Generation (RAG), a longer context augments our model with more information. For LLMs that power agents, such as chatbots, longer context means more tools and capabilities. When summarizing, longer context means more comprehensive summaries. There exist plenty of use-cases for LLMs that are unlocked by longer context lengths.', metadata={'id': '20454848-23ac-4649-b083-81980532a77b', 'source': 'https://www.anyscale.com/blog/fine-tuning-llms-for-longer-context-and-better-rag-systems'}),
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-38-2) Document(page_content='By the way, the context limits differ among models: two Claude models offer a 100K token context window, which works out to about 75,000 words, which is much higher than most other LLMs. The ...', metadata={'id': '1ee2d2bb-8f8e-4a7e-b45e-608b0804fe4c', 'source': 'https://www.infoworld.com/article/3712227/what-is-rag-more-accurate-and-reliable-llms.html'}),
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-38-3) Document(page_content='Figure 1: LLM response accuracy goes down when context needed to answer correctly is found in the middle of the context window. The problem gets worse with larger context models. The problem gets ...', metadata={'id': 'a41d69e6-62eb-4abd-90ad-0892a2836cba', 'source': 'https://medium.com/@jm_51428/long-context-window-models-vs-rag-a73c35a763f2'}),
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-38-4) Document(page_content='To improve performance, we used retrieval-augmented generation (RAG) to prompt an LLM with accurate up-to-date information. As a result of using RAG, the writing quality of the LLM improves substantially, which has implications for the practical usability of LLMs in clinical trial-related writing.', metadata={'id': 'e1af6e30-8c2b-495b-b572-ac6a29067a94', 'source': 'https://arxiv.org/abs/2402.16406'})]

```


#### Generate Sections[¶](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#generate-sections "Permanent link")

Now you can generate the sections using the indexed docs.

```
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-1)classSubSection(BaseModel):
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-2)  subsection_title: str = Field(..., title="Title of the subsection")
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-3)  content: str = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-4)    ...,
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-5)    title="Full content of the subsection. Include [#] citations to the cited sources where relevant.",
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-6)  )
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-7)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-8)  @property
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-9)  defas_str(self) -> str:
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-10)    return f"### {self.subsection_title}\n\n{self.content}".strip()
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-11)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-12)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-13)classWikiSection(BaseModel):
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-14)  section_title: str = Field(..., title="Title of the section")
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-15)  content: str = Field(..., title="Full content of the section")
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-16)  subsections: Optional[List[Subsection]] = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-17)    default=None,
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-18)    title="Titles and descriptions for each subsection of the Wikipedia page.",
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-19)  )
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-20)  citations: List[str] = Field(default_factory=list)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-21)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-22)  @property
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-23)  defas_str(self) -> str:
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-24)    subsections = "\n\n".join(
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-25)      subsection.as_str for subsection in self.subsections or []
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-26)    )
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-27)    citations = "\n".join([f" [{i}] {cit}" for i, cit in enumerate(self.citations)])
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-28)    return (
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-29)      f"## {self.section_title}\n\n{self.content}\n\n{subsections}".strip()
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-30)      + f"\n\n{citations}".strip()
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-31)    )
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-32)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-33)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-34)section_writer_prompt = ChatPromptTemplate.from_messages(
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-35)  [
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-36)    (
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-37)      "system",
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-38)      "You are an expert Wikipedia writer. Complete your assigned WikiSection from the following outline:\n\n"
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-39)      "{outline}\n\nCite your sources, using the following references:\n\n<Documents>\n{docs}\n<Documents>",
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-40)    ),
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-41)    ("user", "Write the full WikiSection for the {section} section."),
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-42)  ]
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-43))
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-44)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-45)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-46)async defretrieve(inputs: dict):
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-47)  docs = await retriever.ainvoke(inputs["topic"] + ": " + inputs["section"])
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-48)  formatted = "\n".join(
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-49)    [
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-50)      f'<Document href="{doc.metadata["source"]}"/>\n{doc.page_content}\n</Document>'
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-51)      for doc in docs
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-52)    ]
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-53)  )
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-54)  return {"docs": formatted, **inputs}
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-55)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-56)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-57)section_writer = (
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-58)  retrieve
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-59)  | section_writer_prompt
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-60)  | long_context_llm.with_structured_output(WikiSection)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-39-61))

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-40-1)section = await section_writer.ainvoke(
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-40-2)  {
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-40-3)    "outline": refined_outline.as_str,
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-40-4)    "section": refined_outline.sections[1].section_title,
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-40-5)    "topic": example_topic,
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-40-6)  }
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-40-7))
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-40-8)print(section.as_str)

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-41-1)## Background
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-41-2)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-41-3)To fully appreciate the impact of million-plus token context window language models on Retrieval-Augmented Generation (RAG) systems, it's essential to first understand the foundational concepts that underpin these technologies. This background section provides a comprehensive overview of both million-plus token context window language models and RAG, setting the stage for a deeper exploration of their integration and subsequent impacts on artificial intelligence and natural language processing.
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-41-4)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-41-5)### Million-Plus Token Context Window Language Models
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-41-6)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-41-7)Million-plus token context window language models, such as Gemini 1.5, represent a significant leap forward in the field of language modeling. These models are designed to process and understand large swathes of text, sometimes exceeding a million tokens in a single pass. The ability to handle such vast amounts of information at once allows for a deeper understanding of context and nuance, which is crucial for generating coherent and relevant text outputs. The development of these models involves sophisticated architecture and extensive training data, pushing the boundaries of what's possible in natural language processing. Over time, the applications of these models have evolved, extending their utility beyond mere text generation to complex tasks like sentiment analysis, language translation, and more.
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-41-8)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-41-9)### Retrieval-Augmented Generation (RAG)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-41-10)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-41-11)The Retrieval-Augmented Generation framework represents a novel approach in the realm of artificial intelligence, blending the strengths of both retrieval and generation models to enhance natural language processing capabilities. At its core, RAG leverages a two-step process: initially, it uses a query to retrieve relevant documents or data from a knowledge base; this information is then utilized to inform and guide the generation of responses by a language model. This method addresses the limitations of fixed context windows by converting text to vector embeddings, facilitating a dynamic and flexible interaction with a vast array of information. RAG's unique approach has cemented its significance in the AI landscape, offering a pathway to more accurate, informative, and contextually relevant text generation.

```


#### Generate final article[¶](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#generate-final-article "Permanent link")

Now we can rewrite the draft to appropriately group all the citations and maintain a consistent voice.

```
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-42-1)fromlangchain_core.output_parsersimport StrOutputParser
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-42-2)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-42-3)writer_prompt = ChatPromptTemplate.from_messages(
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-42-4)  [
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-42-5)    (
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-42-6)      "system",
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-42-7)      "You are an expert Wikipedia author. Write the complete wiki article on {topic} using the following section drafts:\n\n"
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-42-8)      "{draft}\n\nStrictly follow Wikipedia format guidelines.",
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-42-9)    ),
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-42-10)    (
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-42-11)      "user",
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-42-12)      'Write the complete Wiki article using markdown format. Organize citations using footnotes like "[1]",'
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-42-13)      " avoiding duplicates in the footer. Include URLs in the footer.",
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-42-14)    ),
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-42-15)  ]
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-42-16))
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-42-17)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-42-18)writer = writer_prompt | long_context_llm | StrOutputParser()

```


API Reference: [StrOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.string.StrOutputParser.html)

```
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-43-1)for tok in writer.stream({"topic": example_topic, "draft": section.as_str}):
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-43-2)  print(tok, end="")

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-1)# Impact of Million-Plus Token Context Window Language Models on Retrieval-Augmented Generation (RAG)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-2)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-3)The integration of million-plus token context window language models into Retrieval-Augmented Generation (RAG) systems marks a pivotal advancement in the field of artificial intelligence (AI) and natural language processing (NLP). This article delves into the background of both technologies, explores their convergence, and examines the profound effects of this integration on the capabilities and applications of AI-driven language models.
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-4)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-5)## Contents
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-6)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-7)1. [Background](#Background)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-8)  1. [Million-Plus Token Context Window Language Models](#Million-Plus-Token-Context-Window-Language-Models)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-9)  2. [Retrieval-Augmented Generation (RAG)](#Retrieval-Augmented-Generation-(RAG))
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-10)2. [Integration of Million-Plus Token Context Window Models and RAG](#Integration-of-Million-Plus-Token-Context-Window-Models-and-RAG)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-11)3. [Impact on Natural Language Processing](#Impact-on-Natural-Language-Processing)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-12)4. [Applications](#Applications)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-13)5. [Challenges and Limitations](#Challenges-and-Limitations)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-14)6. [Future Directions](#Future-Directions)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-15)7. [Conclusion](#Conclusion)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-16)8. [References](#References)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-17)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-18)## Background
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-19)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-20)### Million-Plus Token Context Window Language Models
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-21)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-22)Million-plus token context window language models, exemplified by systems like Gemini 1.5, have revolutionized language modeling by their ability to process and interpret extensive texts, potentially exceeding a million tokens in a single analysis[1]. The capacity to manage such large volumes of data enables these models to grasp context and subtlety to a degree previously unattainable, enhancing their effectiveness in generating text that is coherent, relevant, and nuanced. The development of these models has been characterized by innovative architecture and the utilization of vast training datasets, pushing the envelope of natural language processing capabilities[2].
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-23)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-24)### Retrieval-Augmented Generation (RAG)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-25)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-26)RAG systems represent an innovative paradigm in AI, merging the strengths of retrieval-based and generative models to improve the quality and relevance of text generation[3]. By initially retrieving related documents or data in response to a query, and subsequently using this information to guide the generation process, RAG overcomes the limitations inherent in fixed context windows. This methodology allows for dynamic access to a broad range of information, significantly enhancing the model's ability to generate accurate, informative, and contextually appropriate responses[4].
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-27)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-28)## Integration of Million-Plus Token Context Window Models and RAG
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-29)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-30)The integration of million-plus token context window models with RAG systems has been a natural progression in the quest for more sophisticated NLP solutions. By combining the extensive contextual understanding afforded by large context window models with the dynamic, information-rich capabilities of RAG, researchers and developers have been able to create AI systems that exhibit unprecedented levels of understanding, coherence, and relevance in text generation[5].
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-31)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-32)## Impact on Natural Language Processing
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-33)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-34)The fusion of these technologies has had a significant impact on the field of NLP, leading to advancements in several key areas:
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-35)- **Enhanced Understanding**: The combined system exhibits a deeper comprehension of both the immediate context and broader subject matter[6].
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-36)- **Improved Coherence**: Generated text is more coherent over longer passages, maintaining consistency and relevance[7].
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-37)- **Increased Relevance**: Outputs are more contextually relevant, drawing accurately from a wider range of sources[8].
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-38)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-39)## Applications
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-40)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-41)This technological convergence has broadened the applicability of NLP systems in numerous fields, including but not limited to:
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-42)- **Automated Content Creation**: Generating written content that is both informative and contextually appropriate for various platforms[9].
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-43)- **Customer Support**: Providing answers that are not only accurate but also tailored to the specific context of user inquiries[10].
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-44)- **Research Assistance**: Assisting in literature review and data analysis by retrieving and synthesizing relevant information from vast databases[11].
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-45)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-46)## Challenges and Limitations
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-47)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-48)Despite their advancements, the integration of these technologies faces several challenges:
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-49)- **Computational Resources**: The processing of million-plus tokens and the dynamic retrieval of relevant information require significant computational power[12].
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-50)- **Data Privacy and Security**: Ensuring the confidentiality and integrity of the data accessed by these systems poses ongoing concerns[13].
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-51)- **Bias and Fairness**: The potential for inheriting and amplifying biases from training data remains a critical issue to address[14].
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-52)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-53)## Future Directions
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-54)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-55)Future research is likely to focus on optimizing computational efficiency, enhancing the models' ability to understand and generate more diverse and nuanced text, and addressing ethical considerations associated with AI and NLP technologies[15].
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-56)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-57)## Conclusion
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-58)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-59)The integration of million-plus token context window language models with RAG systems represents a milestone in the evolution of natural language processing, offering enhanced capabilities that have significant implications across various applications. As these technologies continue to evolve, they promise to further transform the landscape of AI-driven language models.
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-60)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-61)## References
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-62)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-63)1. Gemini 1.5 Documentation. (n.d.).
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-64)2. The Evolution of Language Models. (2022).
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-65)3. Introduction to Retrieval-Augmented Generation. (2021).
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-66)4. Leveraging Large Context Windows for NLP. (2023).
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-67)5. Integrating Context Window Models with RAG. (2023).
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-68)6. Deep Learning in NLP. (2020).
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-69)7. Coherence in Text Generation. (2019).
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-70)8. Contextual Relevance in AI. (2021).
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-71)9. Applications of NLP in Content Creation. (2022).
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-72)10. AI in Customer Support. (2023).
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-73)11. NLP for Research Assistance. (2021).
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-74)12. Computational Challenges in NLP. (2022).
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-75)13. Data Privacy in AI Systems. (2020).
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-76)14. Addressing Bias in AI. (2021).
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-44-77)15. Future of NLP Technologies. (2023).

```


## Final Flow[¶](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#final-flow "Permanent link")

Now it's time to string everything together. We will have 6 main stages in sequence: . 1. Generate the initial outline + perspectives 2. Batch converse with each perspective to expand the content for the article 3. Refine the outline based on the conversations 4. Index the reference docs from the conversations 5. Write the individual sections of the article 6. Write the final wiki

The state tracks the outputs of each stage.

```
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-45-1)classResearchState(TypedDict):
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-45-2)  topic: str
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-45-3)  outline: Outline
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-45-4)  editors: List[Editor]
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-45-5)  interview_results: List[InterviewState]
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-45-6)  # The final sections output
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-45-7)  sections: List[WikiSection]
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-45-8)  article: str

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-1)importasyncio
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-2)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-3)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-4)async definitialize_research(state: ResearchState):
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-5)  topic = state["topic"]
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-6)  coros = (
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-7)    generate_outline_direct.ainvoke({"topic": topic}),
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-8)    survey_subjects.ainvoke(topic),
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-9)  )
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-10)  results = await asyncio.gather(*coros)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-11)  return {
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-12)    **state,
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-13)    "outline": results[0],
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-14)    "editors": results[1].editors,
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-15)  }
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-16)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-17)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-18)async defconduct_interviews(state: ResearchState):
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-19)  topic = state["topic"]
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-20)  initial_states = [
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-21)    {
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-22)      "editor": editor,
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-23)      "messages": [
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-24)        AIMessage(
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-25)          content=f"So you said you were writing an article on {topic}?",
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-26)          name="Subject_Matter_Expert",
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-27)        )
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-28)      ],
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-29)    }
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-30)    for editor in state["editors"]
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-31)  ]
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-32)  # We call in to the sub-graph here to parallelize the interviews
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-33)  interview_results = await interview_graph.abatch(initial_states)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-34)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-35)  return {
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-36)    **state,
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-37)    "interview_results": interview_results,
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-38)  }
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-39)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-40)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-41)defformat_conversation(interview_state):
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-42)  messages = interview_state["messages"]
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-43)  convo = "\n".join(f"{m.name}: {m.content}" for m in messages)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-44)  return f'Conversation with {interview_state["editor"].name}\n\n' + convo
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-45)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-46)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-47)async defrefine_outline(state: ResearchState):
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-48)  convos = "\n\n".join(
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-49)    [
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-50)      format_conversation(interview_state)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-51)      for interview_state in state["interview_results"]
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-52)    ]
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-53)  )
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-54)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-55)  updated_outline = await refine_outline_chain.ainvoke(
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-56)    {
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-57)      "topic": state["topic"],
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-58)      "old_outline": state["outline"].as_str,
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-59)      "conversations": convos,
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-60)    }
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-61)  )
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-62)  return {**state, "outline": updated_outline}
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-63)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-64)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-65)async defindex_references(state: ResearchState):
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-66)  all_docs = []
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-67)  for interview_state in state["interview_results"]:
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-68)    reference_docs = [
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-69)      Document(page_content=v, metadata={"source": k})
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-70)      for k, v in interview_state["references"].items()
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-71)    ]
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-72)    all_docs.extend(reference_docs)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-73)  await vectorstore.aadd_documents(all_docs)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-74)  return state
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-75)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-76)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-77)async defwrite_sections(state: ResearchState):
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-78)  outline = state["outline"]
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-79)  sections = await section_writer.abatch(
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-80)    [
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-81)      {
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-82)        "outline": refined_outline.as_str,
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-83)        "section": section.section_title,
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-84)        "topic": state["topic"],
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-85)      }
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-86)      for section in outline.sections
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-87)    ]
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-88)  )
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-89)  return {
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-90)    **state,
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-91)    "sections": sections,
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-92)  }
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-93)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-94)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-95)async defwrite_article(state: ResearchState):
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-96)  topic = state["topic"]
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-97)  sections = state["sections"]
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-98)  draft = "\n\n".join([section.as_str for section in sections])
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-99)  article = await writer.ainvoke({"topic": topic, "draft": draft})
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-100)  return {
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-101)    **state,
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-102)    "article": article,
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-46-103)  }

```


#### Create the graph[¶](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#create-the-graph "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-47-1)fromlanggraph.checkpoint.memoryimport MemorySaver
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-47-2)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-47-3)builder_of_storm = StateGraph(ResearchState)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-47-4)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-47-5)nodes = [
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-47-6)  ("init_research", initialize_research),
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-47-7)  ("conduct_interviews", conduct_interviews),
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-47-8)  ("refine_outline", refine_outline),
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-47-9)  ("index_references", index_references),
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-47-10)  ("write_sections", write_sections),
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-47-11)  ("write_article", write_article),
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-47-12)]
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-47-13)for i in range(len(nodes)):
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-47-14)  name, node = nodes[i]
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-47-15)  builder_of_storm.add_node(name, node, retry=RetryPolicy(max_attempts=3))
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-47-16)  if i > 0:
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-47-17)    builder_of_storm.add_edge(nodes[i - 1][0], name)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-47-18)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-47-19)builder_of_storm.add_edge(START, nodes[0][0])
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-47-20)builder_of_storm.add_edge(nodes[-1][0], END)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-47-21)storm = builder_of_storm.compile(checkpointer=MemorySaver())

```


API Reference: [MemorySaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.MemorySaver)

```
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-48-1)fromIPython.displayimport Image, display
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-48-2)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-48-3)try:
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-48-4)  display(Image(storm.get_graph().draw_mermaid_png()))
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-48-5)except Exception:
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-48-6)  # This requires some extra dependencies and is optional
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-48-7)  pass

```


![]()

```
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-49-1)config = {"configurable": {"thread_id": "my-thread"}}
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-49-2)async for step in storm.astream(
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-49-3)  {
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-49-4)    "topic": "Groq, NVIDIA, Llamma.cpp and the future of LLM Inference",
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-49-5)  },
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-49-6)  config,
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-49-7)):
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-49-8)  name = next(iter(step))
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-49-9)  print(name)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-49-10)  print("-- ", str(step[name])[:300])

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-50-1)init_research
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-50-2)-- {'topic': 'Groq, NVIDIA, Llamma.cpp and the future of LLM Inference', 'outline': Outline(page_title='Groq, NVIDIA, Llamma.cpp and the future of LLM Inference', sections=[Section(section_title='Introduction', description='Overview of Groq, NVIDIA, Llamma.cpp, and their significance in the field of La
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-50-3)conduct_interviews
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-50-4)-- {'topic': 'Groq, NVIDIA, Llamma.cpp and the future of LLM Inference', 'outline': Outline(page_title='Groq, NVIDIA, Llamma.cpp and the future of LLM Inference', sections=[Section(section_title='Introduction', description='Overview of Groq, NVIDIA, Llamma.cpp, and their significance in the field of La
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-50-5)refine_outline
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-50-6)-- {'topic': 'Groq, NVIDIA, Llamma.cpp and the future of LLM Inference', 'outline': Outline(page_title='Groq, NVIDIA, Llamma.cpp and the Future of LLM Inference', sections=[Section(section_title='Introduction', description='An overview of the significance and roles of Groq, NVIDIA, and Llamma.cpp in th
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-50-7)index_references
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-50-8)-- {'topic': 'Groq, NVIDIA, Llamma.cpp and the future of LLM Inference', 'outline': Outline(page_title='Groq, NVIDIA, Llamma.cpp and the Future of LLM Inference', sections=[Section(section_title='Introduction', description='An overview of the significance and roles of Groq, NVIDIA, and Llamma.cpp in th
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-50-9)write_sections
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-50-10)-- {'topic': 'Groq, NVIDIA, Llamma.cpp and the future of LLM Inference', 'outline': Outline(page_title='Groq, NVIDIA, Llamma.cpp and the Future of LLM Inference', sections=[Section(section_title='Introduction', description='An overview of the significance and roles of Groq, NVIDIA, and Llamma.cpp in th
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-50-11)write_article
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-50-12)-- {'topic': 'Groq, NVIDIA, Llamma.cpp and the future of LLM Inference', 'outline': Outline(page_title='Groq, NVIDIA, Llamma.cpp and the Future of LLM Inference', sections=[Section(section_title='Introduction', description='An overview of the significance and roles of Groq, NVIDIA, and Llamma.cpp in th
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-50-13)__end__
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-50-14)-- {'topic': 'Groq, NVIDIA, Llamma.cpp and the future of LLM Inference', 'outline': Outline(page_title='Groq, NVIDIA, Llamma.cpp and the Future of LLM Inference', sections=[Section(section_title='Introduction', description='An overview of the significance and roles of Groq, NVIDIA, and Llamma.cpp in th

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-51-1)checkpoint = storm.get_state(config)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-51-2)article = checkpoint.values["article"]

```


## Render the Wiki[¶](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#render-the-wiki "Permanent link")

Now we can render the final wiki page!

```
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-52-1)fromIPython.displayimport Markdown
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-52-2)
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-52-3)# We will down-header the sections to create less confusion in this notebook
[](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__codelineno-52-4)Markdown(article.replace("\n#", "\n##"))

```


# Large Language Model (LLM) Inference Technologies[¶](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#large-language-model-llm-inference-technologies "Permanent link")

### Contents[¶](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#contents "Permanent link")

  1. [Introduction](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#Introduction)
  2. [Groq's Advancements in LLM Inference](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#Groqs-Advancements-in-LLM-Inference)
  3. [NVIDIA's Contributions to LLM Inference](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#NVIDIAs-Contributions-to-LLM-Inference)
  4. [Hardware Innovations](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#Hardware-Innovations)
  5. [Software Solutions](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#Software-Solutions)
  6. [Research and Development](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#Research-and-Development)
  7. [Llamma.cpp: Accelerating LLM Inference](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#Llammacpp-Accelerating-LLM-Inference)
  8. [The Future of LLM Inference](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#The-Future-of-LLM-Inference)
  9. [References](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#References)



### Introduction[¶](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#introduction "Permanent link")

The advent of million-plus token context window language models, such as Gemini 1.5, has significantly advanced the field of artificial intelligence, particularly in natural language processing (NLP). These models have expanded the capabilities of machine learning in understanding and generating text over vastly larger contexts than previously possible. This leap in technology has paved the way for transformative applications across various domains, including the integration into Retrieval-Augmented Generation (RAG) systems to produce more accurate and contextually rich responses. 

### Groq's Advancements in LLM Inference[¶](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#groqs-advancements-in-llm-inference "Permanent link")

Groq has introduced the Groq Linear Processor Unit (LPU), a purpose-built hardware architecture for LLM inference. This innovation positions Groq as a leader in efficient and high-performance LLM processing by optimizing the hardware specifically for LLM tasks. The Groq LPU dramatically reduces latency and increases the throughput of LLM inferences, facilitating advancements in a wide range of applications, from natural language processing to broader artificial intelligence technologies[1].

### NVIDIA's Contributions to LLM Inference[¶](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#nvidias-contributions-to-llm-inference "Permanent link")

NVIDIA has played a pivotal role in advancing LLM inference through its GPUs, optimized for AI and machine learning workloads, and specialized software frameworks. The company's GPU architecture and software solutions, such as the CUDA Deep Neural Network library (cuDNN) and the TensorRT inference optimizer, are designed to accelerate computational processes and improve LLM performance. NVIDIA's active participation in research and development further underscores its commitment to enhancing the capabilities of LLMs[1].

#### Hardware Innovations[¶](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#hardware-innovations "Permanent link")

NVIDIA's GPU architecture facilitates high throughput and parallel processing for LLM inference tasks, significantly reducing inference time and enabling complex models to be used in real-time applications.

#### Software Solutions[¶](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#software-solutions "Permanent link")

NVIDIA's suite of software tools, including cuDNN and TensorRT, optimizes LLM performance on its hardware, streamlining the deployment of LLMs by improving their efficiency and reducing latency.

#### Research and Development[¶](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#research-and-development "Permanent link")

NVIDIA collaborates with academic and industry partners to develop new techniques and models that push the boundaries of LLM technology, aiming to make LLMs more powerful and applicable across a broader range of tasks.

### Llamma.cpp: Accelerating LLM Inference[¶](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#llammacpp-accelerating-llm-inference "Permanent link")

Llamma.cpp is a framework developed to enhance the speed and efficiency of LLM inference. By integrating specialized hardware, such as Groq's LPU, and optimizing for parallel processing, Llamma.cpp significantly accelerates computation times and reduces energy consumption. The framework supports million-plus token context window models, enabling applications requiring deep contextual understanding and extensive knowledge retrieval[1][2].

### The Future of LLM Inference[¶](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#the-future-of-llm-inference "Permanent link")

The future of LLM inference is poised for transformative changes with advances in purpose-built hardware architectures like Groq's LPU. These innovations promise to enhance the speed and efficiency of LLM processing, leading to more interactive, capable, and integrated AI applications. The potential for advanced hardware and sophisticated LLMs to enable near-instantaneous processing of complex queries and interactions opens new avenues for research and application in various fields, suggesting a future where AI is seamlessly integrated into society[1][2].

### References[¶](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#references "Permanent link")

[1] "Groq's LPU: Advancing LLM Inference Efficiency," Prompt Engineering. <https://promptengineering.org/groqs-lpu-advancing-llm-inference-efficiency/>

[2] "The Speed of Thought: Harnessing the Fastest LLM with Groq's LPU," Medium. <https://medium.com/@anasdavoodtk1/the-speed-of-thought-harnessing-the-fastest-llm-with-groqs-lpu-11bb00864e9c>

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Chat Bot Benchmarking using Simulation  ](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/langsmith-agent-simulation-evaluation/) [ Next  TNT-LLM: Text Mining at Scale  ](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
