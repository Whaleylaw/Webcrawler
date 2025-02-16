---
url: https://langchain-ai.github.io/langgraphjs/tutorials/workflows/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#workflows-and-agents)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

Workflows and Agents 

[ ](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/?q= "Share")

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
      * [ Concepts  ](https://langchain-ai.github.io/langgraphjs/concepts/)
      * [ Tutorials  ](https://langchain-ai.github.io/langgraphjs/tutorials/)

Tutorials 
        * [ Quick Start  ](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/)

Quick Start 
          * [ Quick Start  ](https://langchain-ai.github.io/langgraphjs/tutorials#quick-start)
          * [ Learn the basics  ](https://langchain-ai.github.io/langgraphjs/tutorials/quickstart/)
          * [ Cloud Deploy  ](https://langchain-ai.github.io/langgraphjs/cloud/quick_start/)
        * [ Chatbots  ](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/)
        * [ RAG  ](https://langchain-ai.github.io/langgraphjs/tutorials#rag)
        * [ Agent Architectures  ](https://langchain-ai.github.io/langgraphjs/tutorials#agent-architectures)
        * [ Evaluation & Analysis  ](https://langchain-ai.github.io/langgraphjs/tutorials#evaluation)
    * Resources  Resources 
      * [ Adopters  ](https://langchain-ai.github.io/langgraphjs/adopters/)
      * [ FAQ  ](https://langchain-ai.github.io/langgraphjs/concepts/faq/)
      * [ Troubleshooting  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraphjs/reference/)
  * [ Versions  ](https://langchain-ai.github.io/langgraphjs/versions/)



Table of contents 

  * [ Set up  ](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#set-up)
  * [ Building Blocks: The Augmented LLM  ](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#building-blocks-the-augmented-llm)
  * [ Prompt chaining  ](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#prompt-chaining)
  * [ Parallelization  ](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#parallelization)
  * [ Routing  ](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#routing)
  * [ Orchestrator-Worker  ](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#orchestrator-worker)
  * [ Evaluator-optimizer  ](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#evaluator-optimizer)
  * [ Agent  ](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#agent)
    * [ Pre-built  ](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#pre-built)
  * [ What LangGraph provides  ](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#what-langgraph-provides)
    * [ Persistence: Human-in-the-Loop  ](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#persistence-human-in-the-loop)
    * [ Persistence: Memory  ](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#persistence-memory)
    * [ Streaming  ](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#streaming)
    * [ Deployment  ](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#deployment)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ Tutorials  ](https://langchain-ai.github.io/langgraphjs/tutorials/)
  4. [ Quick Start  ](https://langchain-ai.github.io/langgraphjs/tutorials#quick-start)



# Workflows and Agents[¶](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#workflows-and-agents "Permanent link")

This guide reviews common patterns for agentic systems. In describing these systems, it can be useful to make a distinction between "workflows" and "agents". One way to think about this difference is nicely explained [here](https://www.anthropic.com/research/building-effective-agents) by Anthropic:

> Workflows are systems where LLMs and tools are orchestrated through predefined code paths. Agents, on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks.

Here is a simple way to visualize these differences:

![Agent Workflow](https://langchain-ai.github.io/langgraphjs/concepts/img/agent_workflow.png)

When building agents and workflows, LangGraph [offers a number of benefits](https://langchain-ai.github.io/langgraphjs/concepts/high_level/) including persistence, streaming, and support for debugging as well as deployment.

## Set up[¶](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#set-up "Permanent link")

Note

The Functional API requires `@langchain/langgraph>=0.2.24`.

You can use [any chat model](https://js.langchain.com/docs/integrations/chat/) that supports structured outputs and tool calling. Below, we show the process of installing the packages, setting API keys, and testing structured outputs / tool calling for Anthropic.

Install dependencies

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-0-1)yarnadd@langchain/langgraph@langchain/anthropic@langchain/core

```


Initialize an LLM

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-1-1)import{ChatAnthropic}from"@langchain/anthropic";
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-1-2)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-1-3)process.env.ANTHROPIC_API_KEY="<your_anthropic_key>";
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-1-5)constllm=newChatAnthropic({
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-1-6)model:"claude-3-5-sonnet-latest",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-1-7)});

```


## Building Blocks: The Augmented LLM[¶](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#building-blocks-the-augmented-llm "Permanent link")

LLM have [augmentations](https://www.anthropic.com/research/building-effective-agents) that support building workflows and agents. These include [structured outputs](https://js.langchain.com/docs/concepts/structured_outputs/) and [tool calling](https://js.langchain.com/docs/concepts/tool_calling/), as shown in this image from the Anthropic [blog](https://www.anthropic.com/research/building-effective-agents):

![augmented_llm.png](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/img/augmented_llm.png)

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-2-1)import{tool}from"@langchain/core/tools";
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-2-2)import{z}from"zod";
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-2-3)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-2-4)constsearchQuerySchema=z.object({
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-2-5)searchQuery:z.string().describe("Query that is optimized web search."),
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-2-6)justification:z.string("Why this query is relevant to the user's request."),
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-2-7)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-2-8)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-2-9)// Augment the LLM with schema for structured output
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-2-10)conststructuredLlm=llm.withStructuredOutput(searchQuerySchema,{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-2-11)name:"searchQuery",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-2-12)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-2-13)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-2-14)// Invoke the augmented LLM
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-2-15)constoutput=awaitstructuredLlm.invoke(
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-2-16)"How does Calcium CT score relate to high cholesterol?"
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-2-17));
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-2-18)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-2-19)constmultiply=tool(
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-2-20)async({a,b})=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-2-21)returna*b;
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-2-22)},
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-2-23){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-2-24)name:"multiply",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-2-25)description:"multiplies two numbers together",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-2-26)schema:z.object({
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-2-27)a:z.number("the first number"),
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-2-28)b:z.number("the second number"),
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-2-29)}),
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-2-30)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-2-31));
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-2-32)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-2-33)// Augment the LLM with tools
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-2-34)constllmWithTools=llm.bindTools([multiply]);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-2-35)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-2-36)// Invoke the LLM with input that triggers the tool call
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-2-37)constmessage=awaitllmWithTools.invoke("What is 2 times 3?");
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-2-38)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-2-39)console.log(message.tool_calls);

```


## Prompt chaining[¶](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#prompt-chaining "Permanent link")

In prompt chaining, each LLM call processes the output of the previous one.

As noted in the [Anthropic blog](https://www.anthropic.com/research/building-effective-agents):

> Prompt chaining decomposes a task into a sequence of steps, where each LLM call processes the output of the previous one. You can add programmatic checks (see "gate” in the diagram below) on any intermediate steps to ensure that the process is still on track.
> 
> When to use this workflow: This workflow is ideal for situations where the task can be easily and cleanly decomposed into fixed subtasks. The main goal is to trade off latency for higher accuracy, by making each LLM call an easier task.

![prompt_chain.png](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/img/prompt_chain.png)

[Graph API](#__tabbed_1_1)[Functional API (beta)](#__tabbed_1_2)

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-1)import{StateGraph,Annotation}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-2)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-3)// Graph state
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-4)constStateAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-5)topic:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-6)joke:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-7)improvedJoke:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-8)finalJoke:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-9)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-10)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-11)// Define node functions
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-12)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-13)// First LLM call to generate initial joke
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-14)asyncfunctiongenerateJoke(state:typeofStateAnnotation.State){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-15)constmsg=awaitllm.invoke(`Write a short joke about ${state.topic}`);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-16)return{joke:msg.content};
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-17)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-18)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-19)// Gate function to check if the joke has a punchline
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-20)functioncheckPunchline(state:typeofStateAnnotation.State){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-21)// Simple check - does the joke contain "?" or "!"
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-22)if(state.joke?.includes("?")||state.joke?.includes("!")){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-23)return"Pass";
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-24)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-25)return"Fail";
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-26)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-27)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-28)// Second LLM call to improve the joke
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-29)asyncfunctionimproveJoke(state:typeofStateAnnotation.State){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-30)constmsg=awaitllm.invoke(
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-31)`Make this joke funnier by adding wordplay: ${state.joke}`
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-32));
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-33)return{improvedJoke:msg.content};
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-34)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-35)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-36)// Third LLM call for final polish
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-37)asyncfunctionpolishJoke(state:typeofStateAnnotation.State){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-38)constmsg=awaitllm.invoke(
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-39)`Add a surprising twist to this joke: ${state.improvedJoke}`
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-40));
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-41)return{finalJoke:msg.content};
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-42)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-43)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-44)// Build workflow
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-45)constchain=newStateGraph(StateAnnotation)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-46).addNode("generateJoke",generateJoke)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-47).addNode("improveJoke",improveJoke)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-48).addNode("polishJoke",polishJoke)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-49).addEdge("__start__","generateJoke")
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-50).addConditionalEdges("generateJoke",checkPunchline,{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-51)Pass:"improveJoke",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-52)Fail:"__end__"
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-53)})
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-54).addEdge("improveJoke","polishJoke")
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-55).addEdge("polishJoke","__end__")
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-56).compile();
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-57)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-58)// Invoke
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-59)conststate=awaitchain.invoke({topic:"cats"});
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-60)console.log("Initial joke:");
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-61)console.log(state.joke);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-62)console.log("\n--- --- ---\n");
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-63)if(state.improvedJoke!==undefined){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-64)console.log("Improved joke:");
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-65)console.log(state.improvedJoke);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-66)console.log("\n--- --- ---\n");
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-67)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-68)console.log("Final joke:");
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-69)console.log(state.finalJoke);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-70)}else{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-71)console.log("Joke failed quality gate - no punchline detected!");
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-3-72)}

```


**LangSmith Trace**

<https://smith.langchain.com/public/a0281fca-3a71-46de-beee-791468607b75/r>

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-4-1)import{task,entrypoint}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-4-2)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-4-3)// Tasks
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-4-4)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-4-5)// First LLM call to generate initial joke
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-4-6)constgenerateJoke=task("generateJoke",async(topic:string)=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-4-7)constmsg=awaitllm.invoke(`Write a short joke about ${topic}`);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-4-8)returnmsg.content;
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-4-9)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-4-10)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-4-11)// Gate function to check if the joke has a punchline
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-4-12)functioncheckPunchline(joke:string){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-4-13)// Simple check - does the joke contain "?" or "!"
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-4-14)if(joke.includes("?")||joke.includes("!")){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-4-15)return"Pass";
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-4-16)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-4-17)return"Fail";
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-4-18)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-4-19)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-4-20)// Second LLM call to improve the joke
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-4-21)constimproveJoke=task("improveJoke",async(joke:string)=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-4-22)constmsg=awaitllm.invoke(
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-4-23)`Make this joke funnier by adding wordplay: ${joke}`
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-4-24));
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-4-25)returnmsg.content;
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-4-26)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-4-27)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-4-28)// Third LLM call for final polish
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-4-29)constpolishJoke=task("polishJoke",async(joke:string)=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-4-30)constmsg=awaitllm.invoke(
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-4-31)`Add a surprising twist to this joke: ${joke}`
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-4-32));
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-4-33)returnmsg.content;
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-4-34)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-4-35)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-4-36)constworkflow=entrypoint(
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-4-37)"jokeMaker",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-4-38)async(topic:string)=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-4-39)constoriginalJoke=awaitgenerateJoke(topic);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-4-40)if(checkPunchline(originalJoke)==="Pass"){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-4-41)returnoriginalJoke;
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-4-42)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-4-43)constimprovedJoke=awaitimproveJoke(originalJoke);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-4-44)constpolishedJoke=awaitpolishJoke(improvedJoke);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-4-45)returnpolishedJoke;
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-4-46)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-4-47));
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-4-48)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-4-49)conststream=awaitworkflow.stream("cats",{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-4-50)streamMode:"updates",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-4-51)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-4-52)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-4-53)forawait(conststepofstream){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-4-54)console.log(step);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-4-55)}

```


**LangSmith Trace**

<https://smith.langchain.com/public/332fa4fc-b6ca-416e-baa3-161625e69163/r>

## Parallelization[¶](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#parallelization "Permanent link")

With parallelization, LLMs work simultaneously on a task:

> LLMs can sometimes work simultaneously on a task and have their outputs aggregated programmatically. This workflow, parallelization, manifests in two key variations: Sectioning: Breaking a task into independent subtasks run in parallel. Voting: Running the same task multiple times to get diverse outputs.
> 
> When to use this workflow: Parallelization is effective when the divided subtasks can be parallelized for speed, or when multiple perspectives or attempts are needed for higher confidence results. For complex tasks with multiple considerations, LLMs generally perform better when each consideration is handled by a separate LLM call, allowing focused attention on each specific aspect.

![parallelization.png](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/img/parallelization.png)

[Graph API](#__tabbed_2_1)[Functional API (beta)](#__tabbed_2_2)

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-1)import{StateGraph,Annotation}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-2)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-3)// Graph state
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-4)constStateAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-5)topic:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-6)joke:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-7)story:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-8)poem:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-9)combinedOutput:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-10)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-11)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-12)// Nodes
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-13)// First LLM call to generate initial joke
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-14)asyncfunctioncallLlm1(state:typeofStateAnnotation.State){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-15)constmsg=awaitllm.invoke(`Write a joke about ${state.topic}`);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-16)return{joke:msg.content};
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-17)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-18)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-19)// Second LLM call to generate story
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-20)asyncfunctioncallLlm2(state:typeofStateAnnotation.State){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-21)constmsg=awaitllm.invoke(`Write a story about ${state.topic}`);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-22)return{story:msg.content};
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-23)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-24)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-25)// Third LLM call to generate poem
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-26)asyncfunctioncallLlm3(state:typeofStateAnnotation.State){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-27)constmsg=awaitllm.invoke(`Write a poem about ${state.topic}`);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-28)return{poem:msg.content};
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-29)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-30)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-31)// Combine the joke, story and poem into a single output
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-32)asyncfunctionaggregator(state:typeofStateAnnotation.State){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-33)constcombined=`Here's a story, joke, and poem about ${state.topic}!\n\n`+
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-34)`STORY:\n${state.story}\n\n`+
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-35)`JOKE:\n${state.joke}\n\n`+
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-36)`POEM:\n${state.poem}`;
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-37)return{combinedOutput:combined};
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-38)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-39)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-40)// Build workflow
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-41)constparallelWorkflow=newStateGraph(StateAnnotation)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-42).addNode("callLlm1",callLlm1);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-43).addNode("callLlm2",callLlm2);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-44).addNode("callLlm3",callLlm3);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-45).addNode("aggregator",aggregator);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-46).addEdge("__start__","callLlm1");
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-47).addEdge("__start__","callLlm2");
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-48).addEdge("__start__","callLlm3");
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-49).addEdge("callLlm1","aggregator");
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-50).addEdge("callLlm2","aggregator");
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-51).addEdge("callLlm3","aggregator");
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-52).addEdge("aggregator","__end__");
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-53).compile();
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-54)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-55)// Invoke
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-56)constresult=awaitparallelWorkflow.invoke({topic:"cats"});
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-5-57)console.log(result.combinedOutput);

```


**LangSmith Trace**

<https://smith.langchain.com/public/3be2e53c-ca94-40dd-934f-82ff87fac277/r>

**Resources:**

**Documentation**

See our documentation on parallelization [here](https://langchain-ai.github.io/langgraphjs/how-tos/branching/).

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-1)import{task,entrypoint}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-2)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-3)// Tasks
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-4)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-5)// First LLM call to generate initial joke
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-6)constcallLlm1=task("generateJoke",async(topic:string)=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-7)constmsg=awaitllm.invoke(`Write a joke about ${topic}`);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-8)returnmsg.content;
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-9)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-10)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-11)// Second LLM call to generate story
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-12)constcallLlm2=task("generateStory",async(topic:string)=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-13)constmsg=awaitllm.invoke(`Write a story about ${topic}`);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-14)returnmsg.content;
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-15)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-16)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-17)// Third LLM call to generate poem
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-18)constcallLlm3=task("generatePoem",async(topic:string)=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-19)constmsg=awaitllm.invoke(`Write a poem about ${topic}`);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-20)returnmsg.content;
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-21)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-22)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-23)// Combine outputs
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-24)constaggregator=task("aggregator",async(params:{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-25)topic:string;
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-26)joke:string;
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-27)story:string;
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-28)poem:string;
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-29)})=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-30)const{topic,joke,story,poem}=params;
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-31)return`Here's a story, joke, and poem about ${topic}!\n\n`+
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-32)`STORY:\n${story}\n\n`+
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-33)`JOKE:\n${joke}\n\n`+
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-34)`POEM:\n${poem}`;
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-35)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-36)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-37)// Build workflow
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-38)constworkflow=entrypoint(
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-39)"parallelWorkflow",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-40)async(topic:string)=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-41)const[joke,story,poem]=awaitPromise.all([
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-42)callLlm1(topic),
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-43)callLlm2(topic),
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-44)callLlm3(topic),
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-45)]);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-46)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-47)returnaggregator({topic,joke,story,poem});
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-48)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-49));
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-50)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-51)// Invoke
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-52)conststream=awaitworkflow.stream("cats",{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-53)streamMode:"updates",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-54)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-55)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-56)forawait(conststepofstream){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-57)console.log(step);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-6-58)}

```


**LangSmith Trace**

<https://smith.langchain.com/public/623d033f-e814-41e9-80b1-75e6abb67801/r>

## Routing[¶](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#routing "Permanent link")

Routing classifies an input and directs it to a followup task. As noted in the [Anthropic blog](https://www.anthropic.com/research/building-effective-agents):

> Routing classifies an input and directs it to a specialized followup task. This workflow allows for separation of concerns, and building more specialized prompts. Without this workflow, optimizing for one kind of input can hurt performance on other inputs.
> 
> When to use this workflow: Routing works well for complex tasks where there are distinct categories that are better handled separately, and where classification can be handled accurately, either by an LLM or a more traditional classification model/algorithm.

![routing.png](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/img/routing.png)

[Graph API](#__tabbed_3_1)[Functional API (beta)](#__tabbed_3_2)

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-1)import{StateGraph,Annotation}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-2)import{z}from"zod";
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-3)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-4)// Schema for structured output to use as routing logic
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-5)constrouteSchema=z.object({
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-6)step:z.enum(["poem","story","joke"]).describe(
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-7)"The next step in the routing process"
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-8)),
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-9)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-10)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-11)// Augment the LLM with schema for structured output
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-12)constrouter=llm.withStructuredOutput(routeSchema);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-13)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-14)// Graph state
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-15)constStateAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-16)input:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-17)decision:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-18)output:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-19)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-20)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-21)// Nodes
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-22)// Write a story
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-23)asyncfunctionllmCall1(state:typeofStateAnnotation.State){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-24)constresult=awaitllm.invoke([{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-25)role:"system",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-26)content:"You are an expert storyteller.",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-27)},{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-28)role:"user",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-29)content:state.input
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-30)}]);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-31)return{output:result.content};
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-32)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-33)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-34)// Write a joke
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-35)asyncfunctionllmCall2(state:typeofStateAnnotation.State){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-36)constresult=awaitllm.invoke([{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-37)role:"system",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-38)content:"You are an expert comedian.",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-39)},{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-40)role:"user",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-41)content:state.input
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-42)}]);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-43)return{output:result.content};
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-44)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-45)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-46)// Write a poem
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-47)asyncfunctionllmCall3(state:typeofStateAnnotation.State){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-48)constresult=awaitllm.invoke([{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-49)role:"system",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-50)content:"You are an expert poet.",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-51)},{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-52)role:"user",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-53)content:state.input
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-54)}]);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-55)return{output:result.content};
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-56)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-57)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-58)asyncfunctionllmCallRouter(state:typeofStateAnnotation.State){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-59)// Route the input to the appropriate node
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-60)constdecision=awaitrouter.invoke([
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-61){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-62)role:"system",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-63)content:"Route the input to story, joke, or poem based on the user's request."
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-64)},
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-65){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-66)role:"user",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-67)content:state.input
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-68)},
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-69)]);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-70)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-71)return{decision:decision.step};
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-72)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-73)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-74)// Conditional edge function to route to the appropriate node
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-75)functionrouteDecision(state:typeofStateAnnotation.State){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-76)// Return the node name you want to visit next
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-77)if(state.decision==="story"){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-78)return"llmCall1";
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-79)}elseif(state.decision==="joke"){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-80)return"llmCall2";
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-81)}elseif(state.decision==="poem"){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-82)return"llmCall3";
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-83)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-84)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-85)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-86)// Build workflow
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-87)constrouterWorkflow=newStateGraph(StateAnnotation)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-88).addNode("llmCall1",llmCall1)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-89).addNode("llmCall2",llmCall2)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-90).addNode("llmCall3",llmCall3)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-91).addNode("llmCallRouter",llmCallRouter)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-92).addEdge("__start__","llmCallRouter")
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-93).addConditionalEdges(
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-94)"llmCallRouter",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-95)routeDecision,
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-96)["llmCall1","llmCall2","llmCall3"],
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-97))
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-98).addEdge("llmCall1","__end__")
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-99).addEdge("llmCall2","__end__")
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-100).addEdge("llmCall3","__end__")
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-101).compile();
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-102)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-103)// Invoke
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-104)conststate=awaitrouterWorkflow.invoke({
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-105)input:"Write me a joke about cats"
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-106)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-7-107)console.log(state.output);

```


**LangSmith Trace**

<https://smith.langchain.com/public/c4580b74-fe91-47e4-96fe-7fac598d509c/r>

**Examples**

[Here](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/) is RAG workflow that routes questions. See our video [here](https://www.youtube.com/watch?v=bq1Plo2RhYI).

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-1)import{z}from"zod";
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-2)import{task,entrypoint}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-3)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-4)// Schema for structured output to use as routing logic
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-5)constrouteSchema=z.object({
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-6)step:z.enum(["poem","story","joke"]).describe(
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-7)"The next step in the routing process"
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-8)),
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-9)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-10)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-11)// Augment the LLM with schema for structured output
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-12)constrouter=llm.withStructuredOutput(routeSchema);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-13)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-14)// Tasks
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-15)// Write a story
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-16)constllmCall1=task("generateStory",async(input:string)=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-17)constresult=awaitllm.invoke([{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-18)role:"system",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-19)content:"You are an expert storyteller.",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-20)},{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-21)role:"user",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-22)content:input
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-23)}]);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-24)returnresult.content;
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-25)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-26)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-27)// Write a joke
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-28)constllmCall2=task("generateJoke",async(input:string)=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-29)constresult=awaitllm.invoke([{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-30)role:"system",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-31)content:"You are an expert comedian.",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-32)},{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-33)role:"user",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-34)content:input
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-35)}]);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-36)returnresult.content;
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-37)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-38)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-39)// Write a poem
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-40)constllmCall3=task("generatePoem",async(input:string)=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-41)constresult=awaitllm.invoke([{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-42)role:"system",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-43)content:"You are an expert poet.",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-44)},{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-45)role:"user",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-46)content:input
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-47)}]);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-48)returnresult.content;
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-49)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-50)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-51)// Route the input to the appropriate node
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-52)constllmCallRouter=task("router",async(input:string)=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-53)constdecision=awaitrouter.invoke([
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-54){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-55)role:"system",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-56)content:"Route the input to story, joke, or poem based on the user's request."
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-57)},
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-58){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-59)role:"user",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-60)content:input
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-61)},
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-62)]);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-63)returndecision.step;
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-64)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-65)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-66)// Build workflow
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-67)constworkflow=entrypoint(
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-68)"routerWorkflow",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-69)async(input:string)=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-70)constnextStep=awaitllmCallRouter(input);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-71)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-72)letllmCall;
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-73)if(nextStep==="story"){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-74)llmCall=llmCall1;
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-75)}elseif(nextStep==="joke"){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-76)llmCall=llmCall2;
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-77)}elseif(nextStep==="poem"){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-78)llmCall=llmCall3;
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-79)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-80)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-81)constfinalResult=awaitllmCall(input);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-82)returnfinalResult;
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-83)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-84));
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-85)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-86)// Invoke
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-87)conststream=awaitworkflow.stream("Write me a joke about cats",{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-88)streamMode:"updates",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-89)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-90)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-91)forawait(conststepofstream){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-92)console.log(step);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-8-93)}

```


**LangSmith Trace**

<https://smith.langchain.com/public/5e2eb979-82dd-402c-b1a0-a8cceaf2a28a/r>

## Orchestrator-Worker[¶](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#orchestrator-worker "Permanent link")

With orchestrator-worker, an orchestrator breaks down a task and delegates each sub-task to workers. As noted in the [Anthropic blog](https://www.anthropic.com/research/building-effective-agents):

> In the orchestrator-workers workflow, a central LLM dynamically breaks down tasks, delegates them to worker LLMs, and synthesizes their results.
> 
> When to use this workflow: This workflow is well-suited for complex tasks where you can’t predict the subtasks needed (in coding, for example, the number of files that need to be changed and the nature of the change in each file likely depend on the task). Whereas it’s topographically similar, the key difference from parallelization is its flexibility—subtasks aren't pre-defined, but determined by the orchestrator based on the specific input.

![worker.png](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/img/worker.png)

[Graph API](#__tabbed_4_1)[Functional API (beta)](#__tabbed_4_2)

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-9-1)import{z}from"zod";
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-9-2)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-9-3)// Schema for structured output to use in planning
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-9-4)constsectionSchema=z.object({
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-9-5)name:z.string().describe("Name for this section of the report."),
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-9-6)description:z.string().describe(
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-9-7)"Brief overview of the main topics and concepts to be covered in this section."
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-9-8)),
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-9-9)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-9-10)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-9-11)constsectionsSchema=z.object({
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-9-12)sections:z.array(sectionSchema).describe("Sections of the report."),
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-9-13)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-9-14)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-9-15)// Augment the LLM with schema for structured output
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-9-16)constplanner=llm.withStructuredOutput(sectionsSchema);

```


**Creating Workers in LangGraph**

Because orchestrator-worker workflows are common, LangGraph **has the`Send` API to support this**. It lets you dynamically create worker nodes and send each one a specific input. Each worker has its own state, and all worker outputs are written to a _shared state key_ that is accessible to the orchestrator graph. This gives the orchestrator access to all worker output and allows it to synthesize them into a final output. As you can see below, we iterate over a list of sections and `Send` each to a worker node. See further documentation [here](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/) and [here](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#send).

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-1)import{Annotation,StateGraph,Send}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-2)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-3)// Graph state
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-4)constStateAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-5)topic:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-6)sections:Annotation<Array<z.infer<typeofsectionSchema>>>,
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-7)completedSections:Annotation<string[]>({
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-8)default:()=>[],
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-9)reducer:(a,b)=>a.concat(b),
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-10)}),
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-11)finalReport:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-12)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-13)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-14)// Worker state
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-15)constWorkerStateAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-16)section:Annotation<z.infer<typeofsectionSchema>>,
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-17)completedSections:Annotation<string[]>({
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-18)default:()=>[],
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-19)reducer:(a,b)=>a.concat(b),
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-20)}),
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-21)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-22)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-23)// Nodes
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-24)asyncfunctionorchestrator(state:typeofStateAnnotation.State){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-25)// Generate queries
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-26)constreportSections=awaitplanner.invoke([
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-27){role:"system",content:"Generate a plan for the report."},
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-28){role:"user",content:`Here is the report topic: ${state.topic}`},
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-29)]);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-30)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-31)return{sections:reportSections.sections};
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-32)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-33)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-34)asyncfunctionllmCall(state:typeofWorkerStateAnnotation.State){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-35)// Generate section
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-36)constsection=awaitllm.invoke([
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-37){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-38)role:"system",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-39)content:"Write a report section following the provided name and description. Include no preamble for each section. Use markdown formatting.",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-40)},
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-41){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-42)role:"user",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-43)content:`Here is the section name: ${state.section.name} and description: ${state.section.description}`,
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-44)},
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-45)]);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-46)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-47)// Write the updated section to completed sections
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-48)return{completedSections:[section.content]};
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-49)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-50)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-51)asyncfunctionsynthesizer(state:typeofStateAnnotation.State){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-52)// List of completed sections
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-53)constcompletedSections=state.completedSections;
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-54)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-55)// Format completed section to str to use as context for final sections
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-56)constcompletedReportSections=completedSections.join("\n\n---\n\n");
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-57)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-58)return{finalReport:completedReportSections};
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-59)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-60)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-61)// Conditional edge function to create llm_call workers that each write a section of the report
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-62)functionassignWorkers(state:typeofStateAnnotation.State){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-63)// Kick off section writing in parallel via Send() API
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-64)returnstate.sections.map((section)=>
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-65)newSend("llmCall",{section})
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-66));
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-67)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-68)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-69)// Build workflow
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-70)constorchestratorWorker=newStateGraph(StateAnnotation)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-71).addNode("orchestrator",orchestrator)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-72).addNode("llmCall",llmCall)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-73).addNode("synthesizer",synthesizer)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-74).addEdge("__start__","orchestrator")
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-75).addConditionalEdges(
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-76)"orchestrator",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-77)assignWorkers,
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-78)["llmCall"]
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-79))
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-80).addEdge("llmCall","synthesizer")
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-81).addEdge("synthesizer","__end__")
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-82).compile();
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-83)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-84)// Invoke
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-85)conststate=awaitorchestratorWorker.invoke({
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-86)topic:"Create a report on LLM scaling laws"
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-87)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-10-88)console.log(state.finalReport);

```


**LangSmith Trace**

<https://smith.langchain.com/public/78cbcfc3-38bf-471d-b62a-b299b144237d/r>

**Resources:**

**Examples**

[Here](https://github.com/langchain-ai/report-mAIstro) is a project that uses orchestrator-worker for report planning and writing. See our video [here](https://www.youtube.com/watch?v=wSxZ7yFbbas).

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-1)import{z}from"zod";
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-2)import{task,entrypoint}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-3)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-4)// Schema for structured output to use in planning
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-5)constsectionSchema=z.object({
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-6)name:z.string().describe("Name for this section of the report."),
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-7)description:z.string().describe(
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-8)"Brief overview of the main topics and concepts to be covered in this section."
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-9)),
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-10)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-11)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-12)constsectionsSchema=z.object({
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-13)sections:z.array(sectionSchema).describe("Sections of the report."),
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-14)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-15)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-16)// Augment the LLM with schema for structured output
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-17)constplanner=llm.withStructuredOutput(sectionsSchema);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-18)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-19)// Tasks
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-20)constorchestrator=task("orchestrator",async(topic:string)=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-21)// Generate queries
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-22)constreportSections=awaitplanner.invoke([
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-23){role:"system",content:"Generate a plan for the report."},
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-24){role:"user",content:`Here is the report topic: ${topic}`},
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-25)]);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-26)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-27)returnreportSections.sections;
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-28)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-29)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-30)constllmCall=task("sectionWriter",async(section:z.infer<typeofsectionSchema>)=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-31)// Generate section
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-32)constresult=awaitllm.invoke([
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-33){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-34)role:"system",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-35)content:"Write a report section.",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-36)},
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-37){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-38)role:"user",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-39)content:`Here is the section name: ${section.name} and description: ${section.description}`,
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-40)},
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-41)]);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-42)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-43)returnresult.content;
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-44)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-45)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-46)constsynthesizer=task("synthesizer",async(completedSections:string[])=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-47)// Synthesize full report from sections
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-48)returncompletedSections.join("\n\n---\n\n");
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-49)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-50)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-51)// Build workflow
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-52)constworkflow=entrypoint(
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-53)"orchestratorWorker",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-54)async(topic:string)=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-55)constsections=awaitorchestrator(topic);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-56)constcompletedSections=awaitPromise.all(
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-57)sections.map((section)=>llmCall(section))
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-58));
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-59)returnsynthesizer(completedSections);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-60)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-61));
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-62)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-63)// Invoke
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-64)conststream=awaitworkflow.stream("Create a report on LLM scaling laws",{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-65)streamMode:"updates",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-66)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-67)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-68)forawait(conststepofstream){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-69)console.log(step);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-11-70)}

```


**LangSmith Trace**

<https://smith.langchain.com/public/75a636d0-6179-4a12-9836-e0aa571e87c5/r>

## Evaluator-optimizer[¶](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#evaluator-optimizer "Permanent link")

In the evaluator-optimizer workflow, one LLM call generates a response while another provides evaluation and feedback in a loop:

> In the evaluator-optimizer workflow, one LLM call generates a response while another provides evaluation and feedback in a loop.
> 
> When to use this workflow: This workflow is particularly effective when we have clear evaluation criteria, and when iterative refinement provides measurable value. The two signs of good fit are, first, that LLM responses can be demonstrably improved when a human articulates their feedback; and second, that the LLM can provide such feedback. This is analogous to the iterative writing process a human writer might go through when producing a polished document.

![evaluator_optimizer.png](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/img/evaluator_optimizer.png)

[Graph API](#__tabbed_5_1)[Functional API (beta)](#__tabbed_5_2)

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-1)import{z}from"zod";
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-2)import{Annotation,StateGraph}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-3)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-4)// Graph state
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-5)constStateAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-6)joke:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-7)topic:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-8)feedback:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-9)funnyOrNot:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-10)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-11)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-12)// Schema for structured output to use in evaluation
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-13)constfeedbackSchema=z.object({
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-14)grade:z.enum(["funny","not funny"]).describe(
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-15)"Decide if the joke is funny or not."
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-16)),
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-17)feedback:z.string().describe(
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-18)"If the joke is not funny, provide feedback on how to improve it."
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-19)),
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-20)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-21)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-22)// Augment the LLM with schema for structured output
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-23)constevaluator=llm.withStructuredOutput(feedbackSchema);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-24)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-25)// Nodes
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-26)asyncfunctionllmCallGenerator(state:typeofStateAnnotation.State){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-27)// LLM generates a joke
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-28)letmsg;
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-29)if(state.feedback){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-30)msg=awaitllm.invoke(
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-31)`Write a joke about ${state.topic} but take into account the feedback: ${state.feedback}`
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-32));
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-33)}else{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-34)msg=awaitllm.invoke(`Write a joke about ${state.topic}`);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-35)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-36)return{joke:msg.content};
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-37)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-38)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-39)asyncfunctionllmCallEvaluator(state:typeofStateAnnotation.State){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-40)// LLM evaluates the joke
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-41)constgrade=awaitevaluator.invoke(`Grade the joke ${state.joke}`);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-42)return{funnyOrNot:grade.grade,feedback:grade.feedback};
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-43)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-44)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-45)// Conditional edge function to route back to joke generator or end based upon feedback from the evaluator
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-46)functionrouteJoke(state:typeofStateAnnotation.State){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-47)// Route back to joke generator or end based upon feedback from the evaluator
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-48)if(state.funnyOrNot==="funny"){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-49)return"Accepted";
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-50)}elseif(state.funnyOrNot==="not funny"){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-51)return"Rejected + Feedback";
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-52)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-53)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-54)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-55)// Build workflow
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-56)constoptimizerWorkflow=newStateGraph(StateAnnotation)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-57).addNode("llmCallGenerator",llmCallGenerator)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-58).addNode("llmCallEvaluator",llmCallEvaluator)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-59).addEdge("__start__","llmCallGenerator")
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-60).addEdge("llmCallGenerator","llmCallEvaluator")
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-61).addConditionalEdges(
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-62)"llmCallEvaluator",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-63)routeJoke,
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-64){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-65)// Name returned by routeJoke : Name of next node to visit
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-66)"Accepted":"__end__",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-67)"Rejected + Feedback":"llmCallGenerator",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-68)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-69))
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-70).compile();
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-71)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-72)// Invoke
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-73)conststate=awaitoptimizerWorkflow.invoke({topic:"Cats"});
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-12-74)console.log(state.joke);

```


**LangSmith Trace**

<https://smith.langchain.com/public/86ab3e60-2000-4bff-b988-9b89a3269789/r>

**Resources:**

**Examples**

[Here](https://github.com/langchain-ai/research-rabbit) is an assistant that uses evaluator-optimizer to improve a report. See our video [here](https://www.youtube.com/watch?v=XGuTzHoqlj8).

[Here](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_adaptive_rag_local/) is a RAG workflow that grades answers for hallucinations or errors. See our video [here](https://www.youtube.com/watch?v=bq1Plo2RhYI).

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-1)import{z}from"zod";
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-2)import{task,entrypoint}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-3)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-4)// Schema for structured output to use in evaluation
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-5)constfeedbackSchema=z.object({
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-6)grade:z.enum(["funny","not funny"]).describe(
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-7)"Decide if the joke is funny or not."
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-8)),
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-9)feedback:z.string().describe(
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-10)"If the joke is not funny, provide feedback on how to improve it."
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-11)),
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-12)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-13)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-14)// Augment the LLM with schema for structured output
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-15)constevaluator=llm.withStructuredOutput(feedbackSchema);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-16)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-17)// Tasks
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-18)constllmCallGenerator=task("jokeGenerator",async(params:{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-19)topic:string;
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-20)feedback?:z.infer<typeoffeedbackSchema>;
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-21)})=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-22)// LLM generates a joke
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-23)constmsg=params.feedback
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-24)?awaitllm.invoke(
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-25)`Write a joke about ${params.topic} but take into account the feedback: ${params.feedback.feedback}`
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-26))
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-27):awaitllm.invoke(`Write a joke about ${params.topic}`);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-28)returnmsg.content;
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-29)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-30)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-31)constllmCallEvaluator=task("jokeEvaluator",async(joke:string)=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-32)// LLM evaluates the joke
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-33)returnevaluator.invoke(`Grade the joke ${joke}`);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-34)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-35)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-36)// Build workflow
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-37)constworkflow=entrypoint(
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-38)"optimizerWorkflow",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-39)async(topic:string)=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-40)letfeedback:z.infer<typeoffeedbackSchema>|undefined;
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-41)letjoke:string;
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-42)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-43)while(true){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-44)joke=awaitllmCallGenerator({topic,feedback});
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-45)feedback=awaitllmCallEvaluator(joke);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-46)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-47)if(feedback.grade==="funny"){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-48)break;
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-49)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-50)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-51)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-52)returnjoke;
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-53)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-54));
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-55)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-56)// Invoke
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-57)conststream=awaitworkflow.stream("Cats",{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-58)streamMode:"updates",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-59)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-60)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-61)forawait(conststepofstream){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-62)console.log(step);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-63)console.log("\n");
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-13-64)}

```


**LangSmith Trace**

<https://smith.langchain.com/public/f66830be-4339-4a6b-8a93-389ce5ae27b4/r>

## Agent[¶](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#agent "Permanent link")

Agents are typically implemented as an LLM performing actions (via tool-calling) based on environmental feedback in a loop. As noted in the [Anthropic blog](https://www.anthropic.com/research/building-effective-agents):

> Agents can handle sophisticated tasks, but their implementation is often straightforward. They are typically just LLMs using tools based on environmental feedback in a loop. It is therefore crucial to design toolsets and their documentation clearly and thoughtfully.
> 
> When to use agents: Agents can be used for open-ended problems where it’s difficult or impossible to predict the required number of steps, and where you can’t hardcode a fixed path. The LLM will potentially operate for many turns, and you must have some level of trust in its decision-making. Agents' autonomy makes them ideal for scaling tasks in trusted environments.

![agent.png](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/img/agent.png)

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-14-1)import{tool}from"@langchain/core/tools";
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-14-2)import{z}from"zod";
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-14-3)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-14-4)// Define tools
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-14-5)constmultiply=tool(
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-14-6)async({a,b}:{a:number;b:number})=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-14-7)returna*b;
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-14-8)},
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-14-9){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-14-10)name:"multiply",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-14-11)description:"Multiply two numbers together",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-14-12)schema:z.object({
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-14-13)a:z.number().describe("first number"),
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-14-14)b:z.number().describe("second number"),
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-14-15)}),
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-14-16)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-14-17));
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-14-18)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-14-19)constadd=tool(
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-14-20)async({a,b}:{a:number;b:number})=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-14-21)returna+b;
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-14-22)},
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-14-23){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-14-24)name:"add",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-14-25)description:"Add two numbers together",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-14-26)schema:z.object({
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-14-27)a:z.number().describe("first number"),
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-14-28)b:z.number().describe("second number"),
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-14-29)}),
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-14-30)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-14-31));
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-14-32)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-14-33)constdivide=tool(
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-14-34)async({a,b}:{a:number;b:number})=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-14-35)returna/b;
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-14-36)},
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-14-37){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-14-38)name:"divide",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-14-39)description:"Divide two numbers",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-14-40)schema:z.object({
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-14-41)a:z.number().describe("first number"),
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-14-42)b:z.number().describe("second number"),
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-14-43)}),
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-14-44)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-14-45));
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-14-46)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-14-47)// Augment the LLM with tools
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-14-48)consttools=[add,multiply,divide];
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-14-49)consttoolsByName=Object.fromEntries(tools.map((tool)=>[tool.name,tool]));
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-14-50)constllmWithTools=llm.bindTools(tools);

```


[Graph API](#__tabbed_6_1)[Functional API (beta)](#__tabbed_6_2)

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-1)import{MessagesAnnotation,StateGraph}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-2)import{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-3)SystemMessage,
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-4)ToolMessage
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-5)}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-6)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-7)// Nodes
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-8)asyncfunctionllmCall(state:typeofMessagesAnnotation.State){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-9)// LLM decides whether to call a tool or not
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-10)constresult=awaitllmWithTools.invoke([
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-11){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-12)role:"system",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-13)content:"You are a helpful assistant tasked with performing arithmetic on a set of inputs."
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-14)},
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-15)...state.messages
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-16)]);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-17)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-18)return{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-19)messages:[result]
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-20)};
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-21)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-22)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-23)asyncfunctiontoolNode(state:typeofMessagesAnnotation.State){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-24)// Performs the tool call
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-25)constresults:ToolMessage[]=[];
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-26)constlastMessage=state.messages.at(-1);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-27)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-28)if(lastMessage?.tool_calls?.length){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-29)for(consttoolCalloflastMessage.tool_calls){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-30)consttool=toolsByName[toolCall.name];
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-31)constobservation=awaittool.invoke(toolCall.args);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-32)results.push(
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-33)newToolMessage({
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-34)content:observation,
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-35)tool_call_id:toolCall.id,
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-36)})
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-37));
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-38)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-39)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-40)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-41)return{messages:results};
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-42)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-43)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-44)// Conditional edge function to route to the tool node or end
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-45)functionshouldContinue(state:typeofMessagesAnnotation.State){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-46)constmessages=state.messages;
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-47)constlastMessage=messages.at(-1);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-48)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-49)// If the LLM makes a tool call, then perform an action
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-50)if(lastMessage?.tool_calls?.length){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-51)return"Action";
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-52)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-53)// Otherwise, we stop (reply to the user)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-54)return"__end__";
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-55)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-56)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-57)// Build workflow
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-58)constagentBuilder=newStateGraph(MessagesAnnotation)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-59).addNode("llmCall",llmCall)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-60).addNode("tools",toolNode)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-61)// Add edges to connect nodes
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-62).addEdge("__start__","llmCall")
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-63).addConditionalEdges(
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-64)"llmCall",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-65)shouldContinue,
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-66){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-67)// Name returned by shouldContinue : Name of next node to visit
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-68)"Action":"tools",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-69)"__end__":"__end__",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-70)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-71))
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-72).addEdge("tools","llmCall")
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-73).compile();
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-74)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-75)// Invoke
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-76)constmessages=[{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-77)role:"user",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-78)content:"Add 3 and 4."
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-79)}];
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-80)constresult=awaitagentBuilder.invoke({messages});
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-15-81)console.log(result.messages);

```


**LangSmith Trace**

<https://smith.langchain.com/public/051f0391-6761-4f8c-a53b-22231b016690/r>

**Examples**

[Here](https://github.com/langchain-ai/memory-agent) is a project that uses a tool calling agent to create / store long-term memories.

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-1)import{task,entrypoint,addMessages}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-2)import{BaseMessageLike,ToolCall}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-3)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-4)constcallLlm=task("llmCall",async(messages:BaseMessageLike[])=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-5)// LLM decides whether to call a tool or not
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-6)returnllmWithTools.invoke([
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-7){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-8)role:"system",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-9)content:"You are a helpful assistant tasked with performing arithmetic on a set of inputs."
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-10)},
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-11)...messages
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-12)]);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-13)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-14)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-15)constcallTool=task("toolCall",async(toolCall:ToolCall)=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-16)// Performs the tool call
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-17)consttool=toolsByName[toolCall.name];
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-18)returntool.invoke(toolCall.args);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-19)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-20)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-21)constagent=entrypoint(
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-22)"agent",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-23)async(messages:BaseMessageLike[])=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-24)letllmResponse=awaitcallLlm(messages);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-25)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-26)while(true){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-27)if(!llmResponse.tool_calls?.length){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-28)break;
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-29)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-30)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-31)// Execute tools
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-32)consttoolResults=awaitPromise.all(
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-33)llmResponse.tool_calls.map((toolCall)=>callTool(toolCall))
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-34));
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-35)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-36)messages=addMessages(messages,[llmResponse,...toolResults]);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-37)llmResponse=awaitcallLlm(messages);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-38)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-39)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-40)messages=addMessages(messages,[llmResponse]);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-41)returnmessages;
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-42)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-43));
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-44)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-45)// Invoke
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-46)constmessages=[{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-47)role:"user",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-48)content:"Add 3 and 4."
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-49)}];
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-50)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-51)conststream=awaitagent.stream([messages],{
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-52)streamMode:"updates",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-53)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-54)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-55)forawait(conststepofstream){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-56)console.log(step);
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-16-57)}

```


**LangSmith Trace**

<https://smith.langchain.com/public/42ae8bf9-3935-4504-a081-8ddbcbfc8b2e/r>

#### Pre-built[¶](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#pre-built "Permanent link")

LangGraph also provides a **pre-built method** for creating an agent as defined above (using the `createReactAgent`[](https://langchain-ai.github.io/langgraphjs/reference/functions/langgraph_prebuilt.createReactAgent.html) function):

<https://langchain-ai.github.io/langgraphjs/how-tos/create-react-agent/>

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-17-1)import{createReactAgent}from"@langchain/langgraph/prebuilt";
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-17-2)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-17-3)// Pass in:
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-17-4)// (1) an LLM instance
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-17-5)// (2) the tools list (which is used to create the tool node)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-17-6)constprebuiltAgent=createReactAgent({
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-17-7)llm:llmWithTools,
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-17-8)tools,
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-17-9)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-17-10)
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-17-11)// invoke
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-17-12)constresult=awaitprebuiltAgent.invoke({
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-17-13)messages:[
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-17-14){
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-17-15)role:"user",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-17-16)content:"Add 3 and 4.",
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-17-17)},
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-17-18)],
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-17-19)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__codelineno-17-20)console.log(result.messages);

```


**LangSmith Trace**

<https://smith.langchain.com/public/abab6a44-29f6-4b97-8164-af77413e494d/r>

## What LangGraph provides[¶](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#what-langgraph-provides "Permanent link")

By constructing each of the above in LangGraph, we get a few things:

### Persistence: Human-in-the-Loop[¶](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#persistence-human-in-the-loop "Permanent link")

LangGraph persistence layer supports interruption and approval of actions (e.g., Human In The Loop). See [Module 3 of LangChain Academy](https://github.com/langchain-ai/langchain-academy/tree/main/module-3).

### Persistence: Memory[¶](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#persistence-memory "Permanent link")

LangGraph persistence layer supports conversational (short-term) memory and long-term memory. See [Modules 2](https://github.com/langchain-ai/langchain-academy/tree/main/module-2) [and 5](https://github.com/langchain-ai/langchain-academy/tree/main/module-5) of LangChain Academy:

### Streaming[¶](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#streaming "Permanent link")

LangGraph provides several ways to stream workflow / agent outputs or intermediate state. See [Module 3 of LangChain Academy](https://github.com/langchain-ai/langchain-academy/blob/main/module-3/streaming-interruption.ipynb).

### Deployment[¶](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#deployment "Permanent link")

LangGraph provides an easy on-ramp for deployment, observability, and evaluation. See [module 6](https://github.com/langchain-ai/langchain-academy/tree/main/module-6) of LangChain Academy.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  Learn the basics  ](https://langchain-ai.github.io/langgraphjs/tutorials/quickstart/) [ Next  Cloud Deploy  ](https://langchain-ai.github.io/langgraphjs/cloud/quick_start/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
