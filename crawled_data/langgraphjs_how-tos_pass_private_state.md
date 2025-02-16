---
url: https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#how-to-pass-private-state)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to pass private state 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/?q= "Share")

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
        * LangGraph  LangGraph 
          * [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
          * [ Controllability  ](https://langchain-ai.github.io/langgraphjs/how-tos#controllability)
          * [ Persistence  ](https://langchain-ai.github.io/langgraphjs/how-tos#persistence)
          * [ Memory  ](https://langchain-ai.github.io/langgraphjs/how-tos#memory)
          * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraphjs/how-tos#human-in-the-loop)
          * [ Streaming  ](https://langchain-ai.github.io/langgraphjs/how-tos#streaming)
          * [ Tool calling  ](https://langchain-ai.github.io/langgraphjs/how-tos#tool-calling)
          * [ Subgraphs  ](https://langchain-ai.github.io/langgraphjs/how-tos#subgraphs)
          * [ Multi-agent  ](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-network/)
          * State Management  State Management 
            * [ State Management  ](https://langchain-ai.github.io/langgraphjs/how-tos#state-management)
            * [ How to define graph state  ](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/)
            * [ How to define input/output schema for your graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/input_output_schema/)
            * [ How to pass private state  ](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/)
          * [ Other  ](https://langchain-ai.github.io/langgraphjs/how-tos#other)
          * [ Prebuilt ReAct Agent  ](https://langchain-ai.github.io/langgraphjs/how-tos#prebuilt-react-agent)
        * [ LangGraph Platform  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph-platform)
      * [ Concepts  ](https://langchain-ai.github.io/langgraphjs/concepts/)
      * [ Tutorials  ](https://langchain-ai.github.io/langgraphjs/tutorials/)
    * Resources  Resources 
      * [ Adopters  ](https://langchain-ai.github.io/langgraphjs/adopters/)
      * [ FAQ  ](https://langchain-ai.github.io/langgraphjs/concepts/faq/)
      * [ Troubleshooting  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraphjs/reference/)
  * [ Versions  ](https://langchain-ai.github.io/langgraphjs/versions/)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/how-tos#langgraph)
  5. [ State Management  ](https://langchain-ai.github.io/langgraphjs/how-tos#state-management)



# How to pass private state[¶](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#how-to-pass-private-state "Permanent link")

Oftentimes, you may want nodes to be able to pass state to each other that should NOT be part of the main schema of the graph. This is often useful because there may be information that is not needed as input/output (and therefore doesn't really make sense to have in the main schema) but is needed as part of the intermediate working logic.

Let's take a look at an example below. In this example, we will create a RAG pipeline that: 1. Takes in a user question 2. Uses an LLM to generate a search query 3. Retrieves documents for that generated query 4. Generates a final answer based on those documents

We will have a separate node for each step. We will only have the `question` and `answer` on the overall state. However, we will need separate states for the `search_query` and the `documents` - we will pass these as private state keys by defining an `input` annotation on each relevant node.

Let's look at an example!

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-1)import{Annotation,StateGraph}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-4)// The overall state of the graph
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-5)constOverallStateAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-6)question:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-7)answer:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-8)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-9)
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-10)// This is what the node that generates the query will return
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-11)constQueryOutputAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-12)query:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-13)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-14)
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-15)// This is what the node that retrieves the documents will return
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-16)constDocumentOutputAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-17)docs:Annotation<string[]>,
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-18)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-19)
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-20)// This is what the node that retrieves the documents will return
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-21)constGenerateOutputAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-22)...OverallStateAnnotation.spec,
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-23)...DocumentOutputAnnotation.spec
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-24)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-25)
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-26)// Node to generate query
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-27)constgenerateQuery=async(state:typeofOverallStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-28)// Replace this with real logic
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-29)return{
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-30)query:state.question+" rephrased as a query!",
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-31)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-32)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-33)
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-34)// Node to retrieve documents
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-35)constretrieveDocuments=async(state:typeofQueryOutputAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-36)// Replace this with real logic
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-37)return{
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-38)docs:[state.query,"some random document"],
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-39)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-40)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-41)
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-42)// Node to generate answer
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-43)constgenerate=async(state:typeofGenerateOutputAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-44)return{
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-45)answer:state.docs.concat([state.question]).join("\n\n"),
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-46)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-47)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-48)
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-49)constgraph=newStateGraph(OverallStateAnnotation)
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-50).addNode("generate_query",generateQuery)
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-51).addNode("retrieve_documents",retrieveDocuments,{input:QueryOutputAnnotation})
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-52).addNode("generate",generate,{input:GenerateOutputAnnotation})
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-53).addEdge("__start__","generate_query")
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-54).addEdge("generate_query","retrieve_documents")
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-55).addEdge("retrieve_documents","generate")
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-56).compile();
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-57)
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-58)awaitgraph.invoke({
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-59)question:"How are you?",
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-0-60)});

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-1-1){
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-1-2) question: 'How are you?',
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-1-3) answer: 'How are you? rephrased as a query!\n\nsome random document\n\nHow are you?'
[](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__codelineno-1-4)}

```


Above, the original `question` value in the input has been preserved, but that the `generate_query` node rephrased it, the `retrieve_documents` node added `"some random document"`, and finally the `generate` node combined the `docs` in the state with the original question to create an `answer`. The intermediate steps populated by the `input` annotations passed to the individual nodes are not present in the final output.  Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to define input/output schema for your graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/input_output_schema/) [ Next  How to add runtime configuration to your graph  ](https://langchain-ai.github.io/langgraphjs/how-tos/configuration/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
