---
url: https://langchain-ai.github.io/langgraphjs/how-tos/input_output_schema/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/input_output_schema/#how-to-define-inputoutput-schema-for-your-graph)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to define input/output schema for your graph 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/input_output_schema/?q= "Share")

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



# How to define input/output schema for your graph[¶](https://langchain-ai.github.io/langgraphjs/how-tos/input_output_schema/#how-to-define-inputoutput-schema-for-your-graph "Permanent link")

By default, `StateGraph` takes in a single schema and all nodes are expected to communicate with that schema. However, it is also possible to define explicit input and output schemas for a graph. This is helpful if you want to draw a distinction between input and output keys.

In this notebook we'll walk through an example of this. At a high level, in order to do this you simply have to pass in separate `Annotation.Root({})`[](https://langchain-ai.github.io/langgraphjs/reference/functions/langgraph.Annotation.Root.html) objets as `{ input: Annotation.Root({}), output: Annotation.Root({}) }` when defining the graph. Let's see an example below!

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/input_output_schema/#__codelineno-0-1)import{Annotation,StateGraph}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/how-tos/input_output_schema/#__codelineno-0-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/input_output_schema/#__codelineno-0-3)constInputAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/how-tos/input_output_schema/#__codelineno-0-4)question:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/how-tos/input_output_schema/#__codelineno-0-5)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/input_output_schema/#__codelineno-0-6)
[](https://langchain-ai.github.io/langgraphjs/how-tos/input_output_schema/#__codelineno-0-7)constOutputAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/how-tos/input_output_schema/#__codelineno-0-8)answer:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/how-tos/input_output_schema/#__codelineno-0-9)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/input_output_schema/#__codelineno-0-10)
[](https://langchain-ai.github.io/langgraphjs/how-tos/input_output_schema/#__codelineno-0-11)constanswerNode=(_state:typeofInputAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/input_output_schema/#__codelineno-0-12)return{answer:"bye"};
[](https://langchain-ai.github.io/langgraphjs/how-tos/input_output_schema/#__codelineno-0-13)};
[](https://langchain-ai.github.io/langgraphjs/how-tos/input_output_schema/#__codelineno-0-14)
[](https://langchain-ai.github.io/langgraphjs/how-tos/input_output_schema/#__codelineno-0-15)constgraph=newStateGraph({
[](https://langchain-ai.github.io/langgraphjs/how-tos/input_output_schema/#__codelineno-0-16)input:InputAnnotation,
[](https://langchain-ai.github.io/langgraphjs/how-tos/input_output_schema/#__codelineno-0-17)output:OutputAnnotation,
[](https://langchain-ai.github.io/langgraphjs/how-tos/input_output_schema/#__codelineno-0-18)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/input_output_schema/#__codelineno-0-19).addNode("answerNode",answerNode)
[](https://langchain-ai.github.io/langgraphjs/how-tos/input_output_schema/#__codelineno-0-20).addEdge("__start__","answerNode")
[](https://langchain-ai.github.io/langgraphjs/how-tos/input_output_schema/#__codelineno-0-21).compile();
[](https://langchain-ai.github.io/langgraphjs/how-tos/input_output_schema/#__codelineno-0-22)
[](https://langchain-ai.github.io/langgraphjs/how-tos/input_output_schema/#__codelineno-0-23)awaitgraph.invoke({
[](https://langchain-ai.github.io/langgraphjs/how-tos/input_output_schema/#__codelineno-0-24)question:"hi",
[](https://langchain-ai.github.io/langgraphjs/how-tos/input_output_schema/#__codelineno-0-25)});

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/input_output_schema/#__codelineno-1-1){ answer: 'bye' }

```


Notice that the output of invoke only includes the output schema.  Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  How to define graph state  ](https://langchain-ai.github.io/langgraphjs/how-tos/define-state/) [ Next  How to pass private state  ](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/input_output_schema/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
