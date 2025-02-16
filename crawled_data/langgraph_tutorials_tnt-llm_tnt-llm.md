---
url: https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#tnt-llm-text-mining-at-scale)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

TNT-LLM: Text Mining at Scale 

[ ](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/?q= "Share")

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
          * [ Web Research (STORM)  ](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/)
          * TNT-LLM: Text Mining at Scale  [ TNT-LLM: Text Mining at Scale  ](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/) Table of contents 
            * [ Setup  ](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#setup)
            * [ Define the graph  ](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#define-the-graph)
              * [ Graph State  ](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#graph-state)
              * [ Define nodes  ](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#define-nodes)
                * [ 1. Summarize Docs  ](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#1-summarize-docs)
                * [ 2. Split into Minibatches  ](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#2-split-into-minibatches)
                * [ 3.a Taxonomy Generation Utilities  ](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#3a-taxonomy-generation-utilities)
                * [ 3. Generate initial taxonomy  ](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#3-generate-initial-taxonomy)
                * [ 4. Update Taxonomy  ](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#4-update-taxonomy)
                * [ 5. Review Taxonomy  ](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#5-review-taxonomy)
              * [ Compile the Graph  ](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#compile-the-graph)
            * [ Use the graph  ](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#use-the-graph)
              * [ Invoke  ](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#invoke)
            * [ Final Result  ](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#final-result)
            * [ Final Taxonomy  ](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#final-taxonomy)
            * [ Phase 2: Labeling  ](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#phase-2-labeling)
              * [ Label Training Data  ](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#label-training-data)
              * [ Train Classifier  ](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#train-classifier)
            * [ Phase 3: Deploy  ](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#phase-3-deploy)
              * [ To deploy  ](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#to-deploy)
              * [ Example:  ](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#example)
            * [ Conclusion  ](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#conclusion)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#setup)
  * [ Define the graph  ](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#define-the-graph)
    * [ Graph State  ](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#graph-state)
    * [ Define nodes  ](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#define-nodes)
      * [ 1. Summarize Docs  ](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#1-summarize-docs)
      * [ 2. Split into Minibatches  ](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#2-split-into-minibatches)
      * [ 3.a Taxonomy Generation Utilities  ](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#3a-taxonomy-generation-utilities)
      * [ 3. Generate initial taxonomy  ](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#3-generate-initial-taxonomy)
      * [ 4. Update Taxonomy  ](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#4-update-taxonomy)
      * [ 5. Review Taxonomy  ](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#5-review-taxonomy)
    * [ Compile the Graph  ](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#compile-the-graph)
  * [ Use the graph  ](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#use-the-graph)
    * [ Invoke  ](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#invoke)
  * [ Final Result  ](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#final-result)
  * [ Final Taxonomy  ](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#final-taxonomy)
  * [ Phase 2: Labeling  ](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#phase-2-labeling)
    * [ Label Training Data  ](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#label-training-data)
    * [ Train Classifier  ](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#train-classifier)
  * [ Phase 3: Deploy  ](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#phase-3-deploy)
    * [ To deploy  ](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#to-deploy)
    * [ Example:  ](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#example)
  * [ Conclusion  ](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#conclusion)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ Tutorials  ](https://langchain-ai.github.io/langgraph/tutorials/)
  4. [ Experimental  ](https://langchain-ai.github.io/langgraph/tutorials#experimental)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/tutorials/tnt-llm/tnt-llm.ipynb "Edit this page")

# TNT-LLM: Text Mining at Scale[¶](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#tnt-llm-text-mining-at-scale "Permanent link")

[TNT-LLM](https://arxiv.org/abs/2403.12173) by Wan, et. al describes a taxonomy generation and classification system developed by Microsoft for their Bing Copilot application.

It generates a rich, interpretable taxonomy of user intents (or other categories) from raw conversation logs. This taxonomy can then be used downstream by LLMs to label logs, which in turn can be used as training data to adapt a cheap classifier (such as logistic regression classifier on embeddings) that can be deployed in your app.

TNT-LLM has three main phases:

  1. Generate Taxonomy
  2. Label Training Data
  3. Finetune classifier + deploy



When applying LangGraph in this notebook, we will focus on the first phase: taxonomy generation (blue in the diagram below). We then show how to label and fit the classifier in subsequent steps below.

![](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/img/tnt_llm.png)

To generate the taxonomy, TNT-LLM proposes 5 steps:

  1. **Summarize** chat logs using a lower-cost LLM (batched over all logs in the sample)
  2. **Batch** the logs into random minibatches
  3. **Generate** an initial taxonomy from the first minibatch
  4. **Update** the taxonomy on each subsequent minibatch via a ritique and revise prompt
  5. **Review** the final taxonomy, scoring its quality and generating a final value using a final sample.



## Setup[¶](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#setup "Permanent link")

First, let's install our required packages and set our API keys

```
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-0-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-0-2)%pip install -U langgraph langchain_anthropic langsmith langchain-community
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-0-3)%pip install -U sklearn langchain_openai

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-1-1)importgetpass
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-1-2)importos
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-1-5)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-1-6)  if os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-1-7)    return
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-1-8)  os.environ[var] = getpass.getpass(var + ":")
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-1-10)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-1-11)_set_env("ANTHROPIC_API_KEY")

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Define the graph[¶](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#define-the-graph "Permanent link")

### Graph State[¶](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#graph-state "Permanent link")

Since each node of a StateGraph accepts the state (and returns an updated state), we'll define that at the outset.

Our flow takes in a list of documents, batches them, and then generates and refines candidate taxonomies as interpretable "clusters".

```
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-2-1)importlogging
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-2-2)importoperator
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-2-3)fromtypingimport Annotated, List, Optional
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-2-4)fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-2-5)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-2-6)logging.basicConfig(level=logging.WARNING)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-2-7)logger = logging.getLogger("tnt-llm")
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-2-8)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-2-9)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-2-10)classDoc(TypedDict):
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-2-11)  id: str
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-2-12)  content: str
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-2-13)  summary: Optional[str]
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-2-14)  explanation: Optional[str]
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-2-15)  category: Optional[str]
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-2-16)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-2-17)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-2-18)classTaxonomyGenerationState(TypedDict):
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-2-19)  # The raw docs; we inject summaries within them in the first step
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-2-20)  documents: List[Doc]
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-2-21)  # Indices to be concise
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-2-22)  minibatches: List[List[int]]
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-2-23)  # Candidate Taxonomies (full trajectory)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-2-24)  clusters: Annotated[List[List[dict]], operator.add]

```


### Define nodes[¶](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#define-nodes "Permanent link")

#### 1. Summarize Docs[¶](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#1-summarize-docs "Permanent link")

Chat logs can get quite long. Our taxonomy generation step needs to see large, diverse minibatches to be able to adequately capture the distribution of categories. To ensure they can all fit efficiently into the context window, we first summarize each chat log. Downstream steps will use these summaries instead of the raw doc content.

```
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-1)importre
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-2)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-3)fromlangchainimport hub
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-4)fromlangchain_anthropicimport ChatAnthropic
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-5)fromlangchain_core.output_parsersimport StrOutputParser
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-6)fromlangchain_core.runnablesimport RunnableConfig, RunnableLambda, RunnablePassthrough
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-7)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-8)summary_prompt = hub.pull("wfh/tnt-llm-summary-generation").partial(
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-9)  summary_length=20, explanation_length=30
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-10))
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-11)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-12)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-13)defparse_summary(xml_string: str) -> dict:
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-14)  summary_pattern = r"<summary>(.*?)</summary>"
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-15)  explanation_pattern = r"<explanation>(.*?)</explanation>"
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-16)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-17)  summary_match = re.search(summary_pattern, xml_string, re.DOTALL)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-18)  explanation_match = re.search(explanation_pattern, xml_string, re.DOTALL)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-19)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-20)  summary = summary_match.group(1).strip() if summary_match else ""
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-21)  explanation = explanation_match.group(1).strip() if explanation_match else ""
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-22)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-23)  return {"summary": summary, "explanation": explanation}
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-24)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-25)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-26)summary_llm_chain = (
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-27)  summary_prompt | ChatAnthropic(model="claude-3-haiku-20240307") | StrOutputParser()
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-28)  # Customize the tracing name for easier organization
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-29)).with_config(run_name="GenerateSummary")
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-30)summary_chain = summary_llm_chain | parse_summary
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-31)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-32)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-33)# Now combine as a "map" operation in a map-reduce chain
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-34)# Input: state
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-35)# Output: state U summaries
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-36)# Processes docs in parallel
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-37)defget_content(state: TaxonomyGenerationState):
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-38)  docs = state["documents"]
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-39)  return [{"content": doc["content"]} for doc in docs]
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-40)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-41)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-42)map_step = RunnablePassthrough.assign(
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-43)  summaries=get_content
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-44)  # This effectively creates a "map" operation
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-45)  # Note you can make this more robust by handling individual errors
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-46)  | RunnableLambda(func=summary_chain.batch, afunc=summary_chain.abatch)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-47))
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-48)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-49)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-50)defreduce_summaries(combined: dict) -> TaxonomyGenerationState:
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-51)  summaries = combined["summaries"]
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-52)  documents = combined["documents"]
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-53)  return {
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-54)    "documents": [
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-55)      {
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-56)        "id": doc["id"],
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-57)        "content": doc["content"],
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-58)        "summary": summ_info["summary"],
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-59)        "explanation": summ_info["explanation"],
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-60)      }
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-61)      for doc, summ_info in zip(documents, summaries)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-62)    ]
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-63)  }
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-64)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-65)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-66)# This is actually the node itself!
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-3-67)map_reduce_chain = map_step | reduce_summaries

```


API Reference: [ChatAnthropic](https://python.langchain.com/api_reference/anthropic/chat_models/langchain_anthropic.chat_models.ChatAnthropic.html) | [StrOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.string.StrOutputParser.html) | [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html) | [RunnableLambda](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.RunnableLambda.html) | [RunnablePassthrough](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.passthrough.RunnablePassthrough.html)

#### 2. Split into Minibatches[¶](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#2-split-into-minibatches "Permanent link")

Each minibatch contains a random sample of docs. This lets the flow identify inadequacies in the current taxonomy using new data.

```
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-4-1)importrandom
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-4-2)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-4-3)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-4-4)defget_minibatches(state: TaxonomyGenerationState, config: RunnableConfig):
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-4-5)  batch_size = config["configurable"].get("batch_size", 200)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-4-6)  original = state["documents"]
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-4-7)  indices = list(range(len(original)))
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-4-8)  random.shuffle(indices)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-4-9)  if len(indices) < batch_size:
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-4-10)    # Don't pad needlessly if we can't fill a single batch
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-4-11)    return [indices]
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-4-12)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-4-13)  num_full_batches = len(indices) // batch_size
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-4-14)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-4-15)  batches = [
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-4-16)    indices[i * batch_size : (i + 1) * batch_size] for i in range(num_full_batches)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-4-17)  ]
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-4-18)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-4-19)  leftovers = len(indices) % batch_size
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-4-20)  if leftovers:
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-4-21)    last_batch = indices[num_full_batches * batch_size :]
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-4-22)    elements_to_add = batch_size - leftovers
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-4-23)    last_batch += random.sample(indices, elements_to_add)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-4-24)    batches.append(last_batch)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-4-25)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-4-26)  return {
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-4-27)    "minibatches": batches,
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-4-28)  }

```


#### 3.a Taxonomy Generation Utilities[¶](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#3a-taxonomy-generation-utilities "Permanent link")

This section of the graph is a generate -> update 🔄 -> review cycle. Each node shares a LOT of logic, which we have factored out into the shared functions below.

```
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-1)fromtypingimport Dict
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-2)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-3)fromlangchain_core.runnablesimport Runnable
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-4)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-5)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-6)defparse_taxa(output_text: str) -> Dict:
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-7)"""Extract the taxonomy from the generated output."""
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-8)  cluster_matches = re.findall(
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-9)    r"\s*<id>(.*?)</id>\s*<name>(.*?)</name>\s*<description>(.*?)</description>\s*",
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-10)    output_text,
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-11)    re.DOTALL,
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-12)  )
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-13)  clusters = [
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-14)    {"id": id.strip(), "name": name.strip(), "description": description.strip()}
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-15)    for id, name, description in cluster_matches
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-16)  ]
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-17)  # We don't parse the explanation since it isn't used downstream
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-18)  return {"clusters": clusters}
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-19)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-20)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-21)defformat_docs(docs: List[Doc]) -> str:
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-22)  xml_table = "<conversations>\n"
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-23)  for doc in docs:
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-24)    xml_table += f'<conv_summ id={doc["id"]}>{doc["summary"]}</conv_summ>\n'
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-25)  xml_table += "</conversations>"
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-26)  return xml_table
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-27)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-28)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-29)defformat_taxonomy(clusters):
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-30)  xml = "<cluster_table>\n"
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-31)  for label in clusters:
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-32)    xml += " <cluster>\n"
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-33)    xml += f'  <id>{label["id"]}</id>\n'
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-34)    xml += f'  <name>{label["name"]}</name>\n'
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-35)    xml += f'  <description>{label["description"]}</description>\n'
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-36)    xml += " </cluster>\n"
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-37)  xml += "</cluster_table>"
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-38)  return xml
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-39)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-40)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-41)definvoke_taxonomy_chain(
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-42)  chain: Runnable,
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-43)  state: TaxonomyGenerationState,
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-44)  config: RunnableConfig,
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-45)  mb_indices: List[int],
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-46)) -> TaxonomyGenerationState:
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-47)  configurable = config["configurable"]
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-48)  docs = state["documents"]
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-49)  minibatch = [docs[idx] for idx in mb_indices]
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-50)  data_table_xml = format_docs(minibatch)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-51)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-52)  previous_taxonomy = state["clusters"][-1] if state["clusters"] else []
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-53)  cluster_table_xml = format_taxonomy(previous_taxonomy)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-54)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-55)  updated_taxonomy = chain.invoke(
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-56)    {
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-57)      "data_xml": data_table_xml,
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-58)      "use_case": configurable["use_case"],
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-59)      "cluster_table_xml": cluster_table_xml,
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-60)      "suggestion_length": configurable.get("suggestion_length", 30),
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-61)      "cluster_name_length": configurable.get("cluster_name_length", 10),
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-62)      "cluster_description_length": configurable.get(
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-63)        "cluster_description_length", 30
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-64)      ),
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-65)      "explanation_length": configurable.get("explanation_length", 20),
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-66)      "max_num_clusters": configurable.get("max_num_clusters", 25),
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-67)    }
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-68)  )
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-69)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-70)  return {
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-71)    "clusters": [updated_taxonomy["clusters"]],
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-5-72)  }

```


API Reference: [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html)

#### 3. Generate initial taxonomy[¶](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#3-generate-initial-taxonomy "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-6-1)# We will share an LLM for each step of the generate -> update -> review cycle
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-6-2)# You may want to consider using Opus or another more powerful model for this
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-6-3)taxonomy_generation_llm = ChatAnthropic(
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-6-4)  model="claude-3-haiku-20240307", max_tokens_to_sample=2000
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-6-5))
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-6-6)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-6-7)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-6-8)## Initial generation
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-6-9)taxonomy_generation_prompt = hub.pull("wfh/tnt-llm-taxonomy-generation").partial(
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-6-10)  use_case="Generate the taxonomy that can be used to label the user intent in the conversation.",
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-6-11))
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-6-12)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-6-13)taxa_gen_llm_chain = (
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-6-14)  taxonomy_generation_prompt | taxonomy_generation_llm | StrOutputParser()
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-6-15)).with_config(run_name="GenerateTaxonomy")
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-6-16)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-6-17)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-6-18)generate_taxonomy_chain = taxa_gen_llm_chain | parse_taxa
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-6-19)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-6-20)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-6-21)defgenerate_taxonomy(
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-6-22)  state: TaxonomyGenerationState, config: RunnableConfig
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-6-23)) -> TaxonomyGenerationState:
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-6-24)  return invoke_taxonomy_chain(
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-6-25)    generate_taxonomy_chain, state, config, state["minibatches"][0]
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-6-26)  )

```


#### 4. Update Taxonomy[¶](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#4-update-taxonomy "Permanent link")

This is a "critique -> revise" step that is repeated N times.

```
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-7-1)taxonomy_update_prompt = hub.pull("wfh/tnt-llm-taxonomy-update")
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-7-2)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-7-3)taxa_update_llm_chain = (
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-7-4)  taxonomy_update_prompt | taxonomy_generation_llm | StrOutputParser()
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-7-5)).with_config(run_name="UpdateTaxonomy")
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-7-6)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-7-7)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-7-8)update_taxonomy_chain = taxa_update_llm_chain | parse_taxa
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-7-9)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-7-10)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-7-11)defupdate_taxonomy(
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-7-12)  state: TaxonomyGenerationState, config: RunnableConfig
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-7-13)) -> TaxonomyGenerationState:
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-7-14)  which_mb = len(state["clusters"]) % len(state["minibatches"])
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-7-15)  return invoke_taxonomy_chain(
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-7-16)    update_taxonomy_chain, state, config, state["minibatches"][which_mb]
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-7-17)  )

```


#### 5. Review Taxonomy[¶](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#5-review-taxonomy "Permanent link")

This runs once we've processed all the minibatches.

```
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-8-1)taxonomy_review_prompt = hub.pull("wfh/tnt-llm-taxonomy-review")
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-8-2)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-8-3)taxa_review_llm_chain = (
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-8-4)  taxonomy_review_prompt | taxonomy_generation_llm | StrOutputParser()
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-8-5)).with_config(run_name="ReviewTaxonomy")
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-8-6)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-8-7)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-8-8)review_taxonomy_chain = taxa_review_llm_chain | parse_taxa
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-8-9)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-8-10)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-8-11)defreview_taxonomy(
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-8-12)  state: TaxonomyGenerationState, config: RunnableConfig
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-8-13)) -> TaxonomyGenerationState:
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-8-14)  batch_size = config["configurable"].get("batch_size", 200)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-8-15)  original = state["documents"]
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-8-16)  indices = list(range(len(original)))
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-8-17)  random.shuffle(indices)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-8-18)  return invoke_taxonomy_chain(
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-8-19)    review_taxonomy_chain, state, config, indices[:batch_size]
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-8-20)  )

```


### Compile the Graph[¶](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#compile-the-graph "Permanent link")

With all the functionality defined, we can build the graph!

```
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-9-1)fromlanggraph.graphimport StateGraph, START, END
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-9-2)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-9-3)graph = StateGraph(TaxonomyGenerationState)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-9-4)graph.add_node("summarize", map_reduce_chain)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-9-5)graph.add_node("get_minibatches", get_minibatches)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-9-6)graph.add_node("generate_taxonomy", generate_taxonomy)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-9-7)graph.add_node("update_taxonomy", update_taxonomy)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-9-8)graph.add_node("review_taxonomy", review_taxonomy)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-9-9)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-9-10)graph.add_edge("summarize", "get_minibatches")
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-9-11)graph.add_edge("get_minibatches", "generate_taxonomy")
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-9-12)graph.add_edge("generate_taxonomy", "update_taxonomy")
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-9-13)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-9-14)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-9-15)defshould_review(state: TaxonomyGenerationState) -> str:
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-9-16)  num_minibatches = len(state["minibatches"])
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-9-17)  num_revisions = len(state["clusters"])
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-9-18)  if num_revisions < num_minibatches:
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-9-19)    return "update_taxonomy"
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-9-20)  return "review_taxonomy"
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-9-21)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-9-22)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-9-23)graph.add_conditional_edges(
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-9-24)  "update_taxonomy",
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-9-25)  should_review,
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-9-26)  # Optional (but required for the diagram to be drawn correctly below)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-9-27)  {"update_taxonomy": "update_taxonomy", "review_taxonomy": "review_taxonomy"},
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-9-28))
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-9-29)graph.add_edge("review_taxonomy", END)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-9-30)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-9-31)graph.add_edge(START, "summarize")
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-9-32)app = graph.compile()

```


API Reference: [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END)

```
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-10-1)fromIPython.displayimport Image, display
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-10-2)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-10-3)try:
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-10-4)  display(Image(app.get_graph().draw_mermaid_png()))
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-10-5)except Exception:
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-10-6)  # This requires some extra dependencies and is optional
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-10-7)  pass

```


![]()

## Use the graph[¶](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#use-the-graph "Permanent link")

The docs can contain **any** content, but we've found it works really well on chat bot logs, such as those captured by [LangSmith](https://smith.langchain.com).

We will use that as an example below. Update the `project_name` to your own LangSmith project.

You will likely have to customize the `run_to_doc` function below, since your expected keys may differ from those of this notebook's author.

```
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-11-1)fromdatetimeimport datetime, timedelta
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-11-2)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-11-3)fromlangsmithimport Client
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-11-4)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-11-5)project_name = "YOUR PROJECT NAME" # Update to your own project
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-11-6)client = Client()
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-11-7)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-11-8)past_week = datetime.now() - timedelta(days=7)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-11-9)runs = list(
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-11-10)  client.list_runs(
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-11-11)    project_name=project_name,
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-11-12)    filter="eq(is_root, true)",
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-11-13)    start_time=past_week,
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-11-14)    # We only need to return the inputs + outputs
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-11-15)    select=["inputs", "outputs"],
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-11-16)  )
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-11-17))
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-11-18)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-11-19)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-11-20)# Convert the langsmith traces to our graph's Doc object.
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-11-21)defrun_to_doc(run) -> Doc:
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-11-22)  turns = []
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-11-23)  idx = 0
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-11-24)  for turn in run.inputs.get("chat_history") or []:
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-11-25)    key, value = next(iter(turn.items()))
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-11-26)    turns.append(f"<{key} idx={idx}>\n{value}\n</{key}>")
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-11-27)    idx += 1
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-11-28)  turns.append(
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-11-29)    f"""
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-11-30)<human idx={idx}>
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-11-31){run.inputs['question']}
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-11-32)</human>"""
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-11-33)  )
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-11-34)  if run.outputs and run.outputs["output"]:
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-11-35)    turns.append(
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-11-36)      f"""<ai idx={idx+1}>
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-11-37){run.outputs['output']}
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-11-38)</ai>"""
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-11-39)    )
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-11-40)  return {
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-11-41)    "id": str(run.id),
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-11-42)    "content": ("\n".join(turns)),
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-11-43)  }

```


#### Invoke[¶](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#invoke "Permanent link")

Now convert the runs to docs and kick off your graph flow. This will take some time! The summary step takes the longest. If you want to speed things up, you could try splitting the load across model providers.

```
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-12-1)fromlangchain_community.cacheimport InMemoryCache
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-12-2)fromlangchain.globalsimport set_llm_cache
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-12-3)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-12-4)# Optional. If you are running into errors or rate limits and want to avoid repeated computation,
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-12-5)# you can set this while debugging
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-12-6)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-12-7)set_llm_cache(InMemoryCache())

```


API Reference: [InMemoryCache](https://python.langchain.com/api_reference/community/cache/langchain_community.cache.InMemoryCache.html) | [set_llm_cache](https://python.langchain.com/api_reference/langchain/globals/langchain.globals.set_llm_cache.html)

```
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-13-1)# We will randomly sample down to 1K docs to speed things up
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-13-2)docs = [run_to_doc(run) for run in runs if run.inputs]
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-13-3)docs = random.sample(docs, min(len(docs), 1000))
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-13-4)use_case = (
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-13-5)  "Generate the taxonomy that can be used both to label the user intent"
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-13-6)  " as well as to identify any required documentation (references, how-tos, etc.)"
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-13-7)  " that would benefit the user."
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-13-8))
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-13-9)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-13-10)stream = app.stream(
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-13-11)  {"documents": docs},
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-13-12)  {
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-13-13)    "configurable": {
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-13-14)      "use_case": use_case,
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-13-15)      # Optional:
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-13-16)      "batch_size": 400,
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-13-17)      "suggestion_length": 30,
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-13-18)      "cluster_name_length": 10,
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-13-19)      "cluster_description_length": 30,
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-13-20)      "explanation_length": 20,
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-13-21)      "max_num_clusters": 25,
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-13-22)    },
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-13-23)    # We batch summarize the docs. To avoid getting errors, we will limit the
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-13-24)    # degree of parallelism to permit.
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-13-25)    "max_concurrency": 2,
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-13-26)  },
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-13-27))
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-13-28)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-13-29)for step in stream:
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-13-30)  node, state = next(iter(step.items()))
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-13-31)  print(node, str(state)[:20] + " ...")

```


## Final Result[¶](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#final-result "Permanent link")

Below, render the final result as markdown:

```
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-14-1)fromIPython.displayimport Markdown
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-14-2)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-14-3)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-14-4)defformat_taxonomy_md(clusters):
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-14-5)  md = "## Final Taxonomy\n\n"
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-14-6)  md += "| ID | Name | Description |\n"
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-14-7)  md += "|----|------|-------------|\n"
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-14-8)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-14-9)  # Fill the table with cluster data
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-14-10)  for label in clusters:
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-14-11)    id = label["id"]
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-14-12)    name = label["name"].replace(
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-14-13)      "|", "\\|"
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-14-14)    ) # Escape any pipe characters within the content
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-14-15)    description = label["description"].replace(
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-14-16)      "|", "\\|"
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-14-17)    ) # Escape any pipe characters
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-14-18)    md += f"| {id} | {name} | {description} |\n"
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-14-19)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-14-20)  return md
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-14-21)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-14-22)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-14-23)Markdown(format_taxonomy_md(step["__end__"]["clusters"][-1]))

```


## Final Taxonomy[¶](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#final-taxonomy "Permanent link")

ID | Name | Description  
---|---|---  
1 | Troubleshooting Network Connectivity Issues | Resolving problems with DNS, network connections, and GitHub extension activation.  
2 | Extracting and Analyzing Data | Retrieving and processing data from various sources like text files, databases, and APIs.  
3 | Providing Healthcare Insights | Generating medical diagnosis, symptom checking, drug information, and skin condition analysis.  
4 | Configuring and Optimizing Models | Adjusting model parameters and hyperparameters to improve performance for a given task.  
5 | Generating Creative Poetry | Creating poems using language models and AI-powered tools.  
6 | Interacting with Databases | Querying databases, extracting data, and managing errors during data processing.  
7 | Querying Vector Databases | Interacting with vector databases like Milvus to store and retrieve high-dimensional data.  
8 | Generating Synthetic Data | Creating synthetic data using language models and machine learning techniques.  
9 | Integrating Tools and Workflows | Incorporating various tools and libraries into a cohesive workflow for different tasks.  
10 | Improving Information Retrieval | Storing and querying multiple vectors per document for better semantic understanding.  
11 | Processing Documents and Extracting Text | Parsing and extracting text from various document formats like PDF, DOCX, and HTML.  
12 | Building Local Knowledge Bases | Creating knowledge bases from text files, handling text splitting, embeddings, and storage.  
13 | Optimizing Conversational Retrieval | Troubleshooting and improving the performance of the ConversationalRetrievalChain in LangChain.  
14 | Connecting Databases and Using Agents | Connecting to databases, using agents, and understanding the differences between agent types.  
15 | Introspecting LangChain Tools | Accessing and retrieving details about the functions and source code of LangChain tools.  
16 | Generating Styled Answers with Retrieval Augmentation | Creating a QA system that generates well-cited answers in a specific style.  
17 | Using ZERO_SHOT_REACT_DESCRIPTION Agents | Applying the ZERO_SHOT_REACT_DESCRIPTION agent type in LangChain for chat models.  
18 | Automating Microlearning Course Creation | Generating microlearning courses based on input parameters like topic, volume, and learning style.  
19 | Integrating with Chroma Vector Store | Storing and retrieving data in the Chroma vector database, including handling document embeddings.  
20 | Managing LangChain Callback Tokens | Understanding and utilizing the callback token feature in the LCEL chain.  
21 | Troubleshooting FastAPI Deployments | Resolving issues with deploying a React app with a FastAPI backend.  
22 | Analyzing Data with LangChain Agents | Using LangChain agents to interact with Pandas and Spark DataFrames for data exploration.  
23 | Implementing the OpenAI Chat API | Implementing the OpenAI chat completion API and understanding the required inputs and outputs.  
24 | Comparing LangChain and LLMIndex | Evaluating the differences between LangChain and LLMIndex, including their UI support for Markdown.  
25 | Suppressing Tools in AgentExecutor | Temporarily disabling tools in an AgentExecutor for a fixed number of invocations.  
  
## Phase 2: Labeling[¶](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#phase-2-labeling "Permanent link")

Now that we have our taxonomy, it's time to label a subset of our data to train a classifier.

Input classification can be useful for anything from in-line prompt optimization (tailor the prompt for each classified intent), to system improvements (identifying categories for which the system doesn't produce good responses) to product analytics (understand which intent categories could be improved to drive profits).

The problem is that LLM-based tagging can be expensive.

Embeddings can be ~100x cheaper to compute, and a simple logistic regression classifier on top of that would add negligible cost.

Let's tag and train a classifier!

#### Label Training Data[¶](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#label-training-data "Permanent link")

Use an LLM to label the data in a fully-automated fashion. For better accuracy, you can sample a portion of the results to label by hand as well to verify the quality.

```
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-15-1)labeling_prompt = hub.pull("wfh/tnt-llm-classify")
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-15-2)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-15-3)labeling_llm = ChatAnthropic(model="claude-3-haiku-20240307", max_tokens_to_sample=2000)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-15-4)labeling_llm_chain = (labeling_prompt | labeling_llm | StrOutputParser()).with_config(
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-15-5)  run_name="ClassifyDocs"
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-15-6))
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-15-7)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-15-8)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-15-9)defparse_labels(output_text: str) -> Dict:
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-15-10)"""Parse the generated labels from the predictions."""
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-15-11)  category_matches = re.findall(
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-15-12)    r"\s*<category>(.*?)</category>.*",
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-15-13)    output_text,
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-15-14)    re.DOTALL,
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-15-15)  )
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-15-16)  categories = [{"category": category.strip()} for category in category_matches]
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-15-17)  if len(categories) > 1:
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-15-18)    logger.warning(f"Multiple selected categories: {categories}")
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-15-19)  label = categories[0]
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-15-20)  stripped = re.sub(r"^\d+\.\s*", "", label["category"]).strip()
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-15-21)  return {"category": stripped}
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-15-22)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-15-23)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-15-24)labeling_chain = labeling_llm_chain | parse_labels

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-16-1)final_taxonomy = step["__end__"]["clusters"][-1]
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-16-2)xml_taxonomy = format_taxonomy(final_taxonomy)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-16-3)results = labeling_chain.batch(
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-16-4)  [
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-16-5)    {
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-16-6)      "content": doc["content"],
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-16-7)      "taxonomy": xml_taxonomy,
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-16-8)    }
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-16-9)    for doc in docs
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-16-10)  ],
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-16-11)  {"max_concurrency": 5},
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-16-12)  return_exceptions=True,
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-16-13))
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-16-14)# Update the docs to include the categories
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-16-15)updated_docs = [{**doc, **category} for doc, category in zip(docs, results)]

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-17-1)if "OPENAI_API_KEY" not in os.environ:
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-17-2)  os.environ["OPENAI_API_KEY"] = getpass("Enter your OPENAI_API_KEY: ")

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-18-1)fromlangchain_openaiimport OpenAIEmbeddings
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-18-2)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-18-3)# Consider using other embedding models here too!
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-18-4)encoder = OpenAIEmbeddings(model="text-embedding-3-large")
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-18-5)vectors = encoder.embed_documents([doc["content"] for doc in docs])
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-18-6)embedded_docs = [{**doc, "embedding": v} for doc, v in zip(updated_docs, vectors)]

```


API Reference: [OpenAIEmbeddings](https://python.langchain.com/api_reference/openai/embeddings/langchain_openai.embeddings.base.OpenAIEmbeddings.html)

#### Train Classifier[¶](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#train-classifier "Permanent link")

Now that we've extracted the features from the text, we can generate the classifier on them.

```
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-19-1)importnumpyasnp
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-19-2)fromsklearn.linear_modelimport LogisticRegression
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-19-3)fromsklearn.metricsimport accuracy_score, f1_score
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-19-4)fromsklearn.model_selectionimport train_test_split
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-19-5)fromsklearn.utilsimport class_weight
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-19-6)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-19-7)# Create a dictionary mapping category names to their indices in the taxonomy
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-19-8)category_to_index = {d["name"]: i for i, d in enumerate(final_taxonomy)}
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-19-9)category_to_index["Other"] = len(category_to_index)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-19-10)# Convert category strings to numeric labels
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-19-11)labels = [
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-19-12)  category_to_index.get(d["category"], category_to_index["Other"])
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-19-13)  for d in embedded_docs
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-19-14)]
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-19-15)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-19-16)label_vectors = [d["embedding"] for d in embedded_docs]
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-19-17)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-19-18)X_train, X_test, y_train, y_test = train_test_split(
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-19-19)  label_vectors, labels, test_size=0.2, random_state=42
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-19-20))
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-19-21)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-19-22)# Calculate class weights
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-19-23)class_weights = class_weight.compute_class_weight(
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-19-24)  class_weight="balanced", classes=np.unique(y_train), y=y_train
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-19-25))
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-19-26)class_weight_dict = dict(enumerate(class_weights))
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-19-27)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-19-28)# Weight the classes to partially handle imbalanced data
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-19-29)model = LogisticRegression(class_weight=class_weight_dict)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-19-30)model.fit(X_train, y_train)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-19-31)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-19-32)train_preds = model.predict(X_train)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-19-33)test_preds = model.predict(X_test)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-19-34)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-19-35)train_acc = accuracy_score(y_train, train_preds)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-19-36)test_acc = accuracy_score(y_test, test_preds)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-19-37)train_f1 = f1_score(y_train, train_preds, average="weighted")
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-19-38)test_f1 = f1_score(y_test, test_preds, average="weighted")
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-19-39)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-19-40)print(f"Train Accuracy: {train_acc:.3f}")
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-19-41)print(f"Test Accuracy: {test_acc:.3f}")
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-19-42)print(f"Train F1 Score: {train_f1:.3f}")
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-19-43)print(f"Test F1 Score: {test_f1:.3f}")

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-20-1)Train Accuracy: 0.515
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-20-2)Test Accuracy: 0.330
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-20-3)Train F1 Score: 0.493
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-20-4)Test F1 Score: 0.335

```


## Phase 3: Deploy[¶](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#phase-3-deploy "Permanent link")

Now that you have your classifier, you can easily deploy it and apply to future runs! All you need is to embed the input and apply your LogisticRegression classifier. Let's try it. We will use python's [joblib](https://joblib.readthedocs.io/en/stable/) library to serialize our sklearn classifier. Below is an example:

```
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-21-1)fromjoblibimport dump as jl_dump
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-21-2)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-21-3)categories = list(category_to_index)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-21-4)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-21-5)# Save the model and categories to a file
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-21-6)with open("model.joblib", "wb") as file:
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-21-7)  jl_dump((model, categories), file)

```


#### To deploy[¶](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#to-deploy "Permanent link")

When deploying, you can load the classifier and initialize your embeddings encoder. They fit together easily using LCEL:

```
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-22-1)fromjoblibimport load as jl_load
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-22-2)fromlangchain_openaiimport OpenAIEmbeddings
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-22-3)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-22-4)loaded_model, loaded_categories = jl_load("model.joblib")
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-22-5)encoder = OpenAIEmbeddings(model="text-embedding-3-large")
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-22-6)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-22-7)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-22-8)defget_category_name(predictions):
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-22-9)  return [loaded_categories[pred] for pred in predictions]
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-22-10)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-22-11)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-22-12)classifier = (
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-22-13)  RunnableLambda(encoder.embed_documents, encoder.aembed_documents)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-22-14)  | loaded_model.predict
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-22-15)  | get_category_name
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-22-16))

```


API Reference: [OpenAIEmbeddings](https://python.langchain.com/api_reference/openai/embeddings/langchain_openai.embeddings.base.OpenAIEmbeddings.html)

#### Example:[¶](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#example "Permanent link")

Assuming you've had some more data come in, you can fetch it and apply it below

```
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-23-1)client = Client()
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-23-2)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-23-3)past_5_min = datetime.now() - timedelta(minutes=5)
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-23-4)runs = list(
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-23-5)  client.list_runs(
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-23-6)    project_name=project_name,
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-23-7)    filter="eq(is_root, true)",
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-23-8)    start_time=past_5_min,
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-23-9)    # We only need to return the inputs + outputs
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-23-10)    select=["inputs", "outputs"],
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-23-11)    limit=100,
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-23-12)  )
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-23-13))
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-23-14)docs = [run_to_doc(r) for r in runs]

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-24-1)classes = classifier.invoke([doc["content"] for doc in docs])
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-24-2)print(classes[:2])

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-25-1)INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-25-2)``````output
[](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__codelineno-25-3)['Interacting with Databases', 'Optimizing Conversational Retrieval']

```


## Conclusion[¶](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#conclusion "Permanent link")

Congrats on implementing TNT-LLM! While most folks use clustering-based approaches like LDA, k-means, etc. it can often be hard to really interpret what each cluster represents. TNT-LLM generates human-interpretable labels you can use downstream to monitor and improve your application.

The technique also lends itself to hierarchical sub-categorizing: once you have the above taxonomy, use it to label your data, then on each sub-category, generate a new taxonomy using a similar technique to the one described above!

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Web Research (STORM)  ](https://langchain-ai.github.io/langgraph/tutorials/storm/storm/) [ Next  Web Voyager  ](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/tutorials/tnt-llm/tnt-llm/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
