---
url: https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#basic-multi-agent-collaboration)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

Basic Multi-agent Collaboration 

[ ](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/?q= "Share")

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
        * [ Quick Start  ](https://langchain-ai.github.io/langgraphjs/tutorials#quick-start)
        * [ Chatbots  ](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/)
        * [ RAG  ](https://langchain-ai.github.io/langgraphjs/tutorials#rag)
        * Agent Architectures  Agent Architectures 
          * [ Agent Architectures  ](https://langchain-ai.github.io/langgraphjs/tutorials#agent-architectures)
          * Multi-Agent Systems  Multi-Agent Systems 
            * [ Multi-Agent Systems  ](https://langchain-ai.github.io/langgraphjs/tutorials#multi-agent-systems)
            * Basic Multi-agent Collaboration  [ Basic Multi-agent Collaboration  ](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/) Table of contents 
              * [ Helper Utilities  ](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#helper-utilities)
                * [ Define State  ](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#define-state)
              * [ Define tools  ](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#define-tools)
              * [ Create graph  ](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#create-graph)
                * [ Define Agent Nodes  ](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#define-agent-nodes)
                * [ Define Tool Node  ](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#define-tool-node)
                * [ Define Edge Logic  ](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#define-edge-logic)
                * [ Define the Graph  ](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#define-the-graph)
              * [ Invoke  ](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#invoke)
            * [ Agent Supervisor  ](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/)
            * [ Hierarchical Agent Teams  ](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/hierarchical_agent_teams/)
          * [ Planning Agents  ](https://langchain-ai.github.io/langgraphjs/tutorials#planning-agents)
          * [ Reflection & Critique  ](https://langchain-ai.github.io/langgraphjs/tutorials#reflection-critique)
        * [ Evaluation & Analysis  ](https://langchain-ai.github.io/langgraphjs/tutorials#evaluation)
    * Resources  Resources 
      * [ Adopters  ](https://langchain-ai.github.io/langgraphjs/adopters/)
      * [ FAQ  ](https://langchain-ai.github.io/langgraphjs/concepts/faq/)
      * [ Troubleshooting  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraphjs/reference/)
  * [ Versions  ](https://langchain-ai.github.io/langgraphjs/versions/)



Table of contents 

  * [ Helper Utilities  ](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#helper-utilities)
    * [ Define State  ](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#define-state)
  * [ Define tools  ](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#define-tools)
  * [ Create graph  ](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#create-graph)
    * [ Define Agent Nodes  ](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#define-agent-nodes)
    * [ Define Tool Node  ](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#define-tool-node)
    * [ Define Edge Logic  ](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#define-edge-logic)
    * [ Define the Graph  ](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#define-the-graph)
  * [ Invoke  ](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#invoke)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ Tutorials  ](https://langchain-ai.github.io/langgraphjs/tutorials/)
  4. [ Agent Architectures  ](https://langchain-ai.github.io/langgraphjs/tutorials#agent-architectures)
  5. [ Multi-Agent Systems  ](https://langchain-ai.github.io/langgraphjs/tutorials#multi-agent-systems)



# Basic Multi-agent Collaboration[¶](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#basic-multi-agent-collaboration "Permanent link")

A single agent can usually operate effectively using a handful of tools within a single domain, but even using powerful models like `gpt-4`, it can be less effective at using many tools.

One way to approach complicated tasks is through a "divide-and-conquer" approach: create an specialized agent for each task or domain and route tasks to the correct "expert".

This notebook (inspired by the paper [AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation](https://arxiv.org/abs/2308.08155), by Wu, et. al.) shows one way to do this using LangGraph.

The resulting graph will look something like the following diagram:

![](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/img/simple_multi_agent_diagram.png)

Before we get started, a quick note: this and other multi-agent notebooks are designed to show _how_ you can implement certain design patterns in LangGraph. If the pattern suits your needs, we recommend combining it with some of the other fundamental patterns described elsewhere in the docs for best performance.

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-0-1)// process.env.OPENAI_API_KEY = "sk_...";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-0-2)// process.env.TAVILY_API_KEY = "sk_...";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-0-3)// process.env.LANGCHAIN_API_KEY = "sk_...";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-0-4)// process.env.LANGCHAIN_TRACING_V2 = "true";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-0-5)// process.env.LANGCHAIN_PROJECT = "Multi-agent Collaboration: LangGraphJS";

```


## Helper Utilities[¶](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#helper-utilities "Permanent link")

The following helper functions will help create agents. These agents will then be nodes in the graph.

You can skip ahead if you just want to see what the graph looks like.

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-1-1)import{
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-1-2)ChatPromptTemplate,
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-1-3)MessagesPlaceholder,
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-1-4)}from"@langchain/core/prompts";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-1-5)import{StructuredTool}from"@langchain/core/tools";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-1-6)import{convertToOpenAITool}from"@langchain/core/utils/function_calling";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-1-7)import{Runnable}from"@langchain/core/runnables";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-1-8)import{ChatOpenAI}from"@langchain/openai";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-1-10)/**
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-1-11) * Create an agent that can run a set of tools.
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-1-12) */
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-1-13)asyncfunctioncreateAgent({
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-1-14)llm,
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-1-15)tools,
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-1-16)systemMessage,
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-1-17)}:{
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-1-18)llm:ChatOpenAI;
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-1-19)tools:StructuredTool[];
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-1-20)systemMessage:string;
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-1-21)}):Promise<Runnable>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-1-22)consttoolNames=tools.map((tool)=>tool.name).join(", ");
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-1-23)constformattedTools=tools.map((t)=>convertToOpenAITool(t));
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-1-24)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-1-25)letprompt=ChatPromptTemplate.fromMessages([
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-1-26)[
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-1-27)"system",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-1-28)"You are a helpful AI assistant, collaborating with other assistants."+
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-1-29)" Use the provided tools to progress towards answering the question."+
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-1-30)" If you are unable to fully answer, that's OK, another assistant with different tools "+
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-1-31)" will help where you left off. Execute what you can to make progress."+
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-1-32)" If you or any of the other assistants have the final answer or deliverable,"+
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-1-33)" prefix your response with FINAL ANSWER so the team knows to stop."+
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-1-34)" You have access to the following tools: {tool_names}.\n{system_message}",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-1-35)],
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-1-36)newMessagesPlaceholder("messages"),
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-1-37)]);
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-1-38)prompt=awaitprompt.partial({
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-1-39)system_message:systemMessage,
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-1-40)tool_names:toolNames,
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-1-41)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-1-42)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-1-43)returnprompt.pipe(llm.bind({tools:formattedTools}));
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-1-44)}

```


### Define State[¶](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#define-state "Permanent link")

We first define the state of the graph. This will just a list of messages, along with a key to track the most recent sender

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-2-1)import{BaseMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-2-2)import{Annotation}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-2-3)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-2-4)// This defines the object that is passed between each node
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-2-5)// in the graph. We will create different nodes for each agent and tool
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-2-6)constAgentState=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-2-7)messages:Annotation<BaseMessage[]>({
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-2-8)reducer:(x,y)=>x.concat(y),
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-2-9)}),
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-2-10)sender:Annotation<string>({
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-2-11)reducer:(x,y)=>y??x??"user",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-2-12)default:()=>"user",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-2-13)}),
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-2-14)})

```


## Define tools[¶](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#define-tools "Permanent link")

These tools will be used by our worker agents to answer our questions.

We will create a chart tool (using d3.js), and the LangChain TavilySearchResults tool for web search functionality.

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-1)require("esm-hook");// Only for running this in TSLab. See: https://github.com/yunabe/tslab/issues/72
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-2)import{TavilySearchResults}from"@langchain/community/tools/tavily_search";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-3)import{tool}from"@langchain/core/tools";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-4)import*asd3from"d3";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-5)// ----------ATTENTION----------
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-6)// If attempting to run this notebook locally, you must follow these instructions
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-7)// to install the necessary system dependencies for the `canvas` package.
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-8)// https://www.npmjs.com/package/canvas#compiling
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-9)// -----------------------------
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-10)import{createCanvas}from"canvas";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-11)import{z}from"zod";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-12)import*astslabfrom"tslab";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-13)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-14)constchartTool=tool(
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-15)({data})=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-16)constwidth=500;
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-17)constheight=500;
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-18)constmargin={top:20,right:30,bottom:30,left:40};
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-19)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-20)constcanvas=createCanvas(width,height);
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-21)constctx=canvas.getContext("2d");
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-22)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-23)constx=d3
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-24).scaleBand()
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-25).domain(data.map((d)=>d.label))
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-26).range([margin.left,width-margin.right])
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-27).padding(0.1);
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-28)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-29)consty=d3
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-30).scaleLinear()
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-31).domain([0,d3.max(data,(d)=>d.value)??0])
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-32).nice()
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-33).range([height-margin.bottom,margin.top]);
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-34)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-35)constcolorPalette=[
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-36)"#e6194B",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-37)"#3cb44b",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-38)"#ffe119",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-39)"#4363d8",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-40)"#f58231",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-41)"#911eb4",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-42)"#42d4f4",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-43)"#f032e6",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-44)"#bfef45",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-45)"#fabebe",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-46)];
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-47)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-48)data.forEach((d,idx)=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-49)ctx.fillStyle=colorPalette[idx%colorPalette.length];
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-50)ctx.fillRect(
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-51)x(d.label)??0,
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-52)y(d.value),
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-53)x.bandwidth(),
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-54)height-margin.bottom-y(d.value),
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-55));
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-56)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-57)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-58)ctx.beginPath();
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-59)ctx.strokeStyle="black";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-60)ctx.moveTo(margin.left,height-margin.bottom);
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-61)ctx.lineTo(width-margin.right,height-margin.bottom);
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-62)ctx.stroke();
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-63)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-64)ctx.textAlign="center";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-65)ctx.textBaseline="top";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-66)x.domain().forEach((d)=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-67)constxCoord=(x(d)??0)+x.bandwidth()/2;
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-68)ctx.fillText(d,xCoord,height-margin.bottom+6);
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-69)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-70)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-71)ctx.beginPath();
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-72)ctx.moveTo(margin.left,height-margin.top);
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-73)ctx.lineTo(margin.left,height-margin.bottom);
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-74)ctx.stroke();
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-75)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-76)ctx.textAlign="right";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-77)ctx.textBaseline="middle";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-78)constticks=y.ticks();
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-79)ticks.forEach((d)=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-80)constyCoord=y(d);// height - margin.bottom - y(d);
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-81)ctx.moveTo(margin.left,yCoord);
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-82)ctx.lineTo(margin.left-6,yCoord);
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-83)ctx.stroke();
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-84)ctx.fillText(d.toString(),margin.left-8,yCoord);
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-85)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-86)tslab.display.png(canvas.toBuffer());
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-87)return"Chart has been generated and displayed to the user!";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-88)},
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-89){
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-90)name:"generate_bar_chart",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-91)description:
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-92)"Generates a bar chart from an array of data points using D3.js and displays it for the user.",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-93)schema:z.object({
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-94)data:z
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-95).object({
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-96)label:z.string(),
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-97)value:z.number(),
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-98)})
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-99).array(),
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-100)}),
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-101)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-102))
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-103)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-3-104)consttavilyTool=newTavilySearchResults();

```


## Create graph[¶](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#create-graph "Permanent link")

Now that we've defined our tools and made some helper functions, will create the individual agents below and tell them how to talk to each other using LangGraph.

### Define Agent Nodes[¶](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#define-agent-nodes "Permanent link")

In LangGraph, nodes represent functions that perform the work. In our example, we will have "agent" nodes and a "callTool" node.

The input for every node is the graph's state. In our case, the state will have a list of messages as input, as well as the name of the previous node.

First, let's define the nodes for the agents.

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-1)import{HumanMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-2)importtype{RunnableConfig}from"@langchain/core/runnables";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-3)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-4)// Helper function to run a node for a given agent
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-5)asyncfunctionrunAgentNode(props:{
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-6)state:typeofAgentState.State;
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-7)agent:Runnable;
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-8)name:string;
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-9)config?:RunnableConfig;
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-10)}){
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-11)const{state,agent,name,config}=props;
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-12)letresult=awaitagent.invoke(state,config);
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-13)// We convert the agent output into a format that is suitable
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-14)// to append to the global state
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-15)if(!result?.tool_calls||result.tool_calls.length===0){
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-16)// If the agent is NOT calling a tool, we want it to
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-17)// look like a human message.
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-18)result=newHumanMessage({...result,name:name});
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-19)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-20)return{
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-21)messages:[result],
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-22)// Since we have a strict workflow, we can
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-23)// track the sender so we know who to pass to next.
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-24)sender:name,
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-25)};
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-26)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-27)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-28)constllm=newChatOpenAI({modelName:"gpt-4o"});
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-29)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-30)// Research agent and node
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-31)constresearchAgent=awaitcreateAgent({
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-32)llm,
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-33)tools:[tavilyTool],
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-34)systemMessage:
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-35)"You should provide accurate data for the chart generator to use.",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-36)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-37)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-38)asyncfunctionresearchNode(
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-39)state:typeofAgentState.State,
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-40)config?:RunnableConfig,
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-41)){
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-42)returnrunAgentNode({
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-43)state:state,
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-44)agent:researchAgent,
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-45)name:"Researcher",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-46)config,
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-47)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-48)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-49)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-50)// Chart Generator
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-51)constchartAgent=awaitcreateAgent({
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-52)llm,
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-53)tools:[chartTool],
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-54)systemMessage:"Any charts you display will be visible by the user.",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-55)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-56)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-57)asyncfunctionchartNode(state:typeofAgentState.State){
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-58)returnrunAgentNode({
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-59)state:state,
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-60)agent:chartAgent,
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-61)name:"ChartGenerator",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-62)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-4-63)}

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-5-1)// Example invocation
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-5-2)constresearchResults=awaitresearchNode({
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-5-3)messages:[newHumanMessage("Research the US primaries in 2024")],
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-5-4)sender:"User",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-5-5)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-5-6)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-5-7)researchResults;

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-6-1){
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-6-2) messages: [
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-6-3)  AIMessage {
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-6-4)   "id": "chatcmpl-9yopin5fBlXtA15wWiUlDyiKT9T9P",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-6-5)   "content": "",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-6-6)   "additional_kwargs": {
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-6-7)    "tool_calls": [
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-6-8)     {
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-6-9)      "id": "call_SRihR0BFFtw3TlHQtiBDPR3v",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-6-10)      "type": "function",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-6-11)      "function": "[Object]"
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-6-12)     }
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-6-13)    ]
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-6-14)   },
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-6-15)   "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-6-16)    "tokenUsage": {
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-6-17)     "completionTokens": 22,
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-6-18)     "promptTokens": 192,
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-6-19)     "totalTokens": 214
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-6-20)    },
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-6-21)    "finish_reason": "tool_calls",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-6-22)    "system_fingerprint": "fp_3aa7262c27"
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-6-23)   },
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-6-24)   "tool_calls": [
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-6-25)    {
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-6-26)     "name": "tavily_search_results_json",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-6-27)     "args": {
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-6-28)      "input": "US primaries 2024 updates"
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-6-29)     },
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-6-30)     "type": "tool_call",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-6-31)     "id": "call_SRihR0BFFtw3TlHQtiBDPR3v"
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-6-32)    }
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-6-33)   ],
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-6-34)   "invalid_tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-6-35)   "usage_metadata": {
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-6-36)    "input_tokens": 192,
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-6-37)    "output_tokens": 22,
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-6-38)    "total_tokens": 214
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-6-39)   }
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-6-40)  }
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-6-41) ],
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-6-42) sender: 'Researcher'
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-6-43)}

```


### Define Tool Node[¶](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#define-tool-node "Permanent link")

We now define a node to run the tools

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-7-1)import{ToolNode}from"@langchain/langgraph/prebuilt";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-7-2)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-7-3)consttools=[tavilyTool,chartTool];
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-7-4)// This runs tools in the graph
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-7-5)consttoolNode=newToolNode<typeofAgentState.State>(tools);

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-8-1)// Example invocation
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-8-2)awaittoolNode.invoke(researchResults);

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-9-1){
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-9-2) messages: [
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-9-3)  ToolMessage {
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-9-4)   "content": "[{\"title\":\"Election Results 2024: Live Election Map | Races by State - POLITICO\",\"url\":\"https://www.politico.com/2024-election/results/\",\"content\":\"Live 2024 election results and maps by state. POLITICO's coverage of 2024 primary races for President, Senate, House and Governors.\",\"score\":0.9798227,\"raw_content\":null},{\"title\":\"Presidential Primary Election Results 2024 | Delegate Count Map by ...\",\"url\":\"https://www.politico.com/2024-election/results/president/\",\"content\":\"Live 2024 Presidential election results, maps and delegate counts by state. POLITICO's coverage of 2024 primary races for President, Senate, House and Governors.\",\"score\":0.97666925,\"raw_content\":null},{\"title\":\"Election 2024: Presidential campaign news, polls and results | CNN Politics\",\"url\":\"https://www.cnn.com/election/2024\",\"content\":\"2024 election guide: Presidential candidates, polls, primaries and caucuses, voter information and results for November 5, 2024\",\"score\":0.92455155,\"raw_content\":null},{\"title\":\"2024 Election news: Latest on the presidential race, polls & results\",\"url\":\"https://www.politico.com/news/2024-elections\",\"content\":\"POLITICO\\nPolitico Logo\\nWASHINGTON & POLITICS\\n2024 ELECTIONS\\nSTATE POLITICS & POLICY\\nGLOBAL POLITICS & POLICY\\nPOLICY NEWS\\nNEWSLETTERS\\nCOLUMNISTS\\nSERIES & MORE\\nPOLITICO Live\\nFollow us\\n2024 Elections\\nThe latest coverage of the 2024 presidential, House and Senate elections.\\n It's a question being debated in courtrooms across the country: Does the 14th Amendment of the U.S. Constitution bar Trump from running for president again because he supported or “engaged in insurrection or rebellion” for his role in the Jan. 6 attack on the Capitol?\\nRead More »\\nFormer House Speaker Kevin McCarthy has endorsed Trump in his 2024 run, but he hasn't always had the nicest things to say about the former president. By ERICA ORDEN\\n12/14/2023 03:15 PM EST\\nUpdated 12/14/2023 04:06 PM EST\\nNEW YORK — An appeals court on Thursday rejected former President Donald Trump’s effort to overturn the gag order barring him from making comments about the staff of the judge presiding over his $250 million civil fraud trial, dealing him another setback in his attempts to fight the restrictions.\\n | Charlie Neibergall/AP\\nPlaybook Deep Dive\\nHow Hunter Biden, Jack Smith, and Trump’s legal troubles are setting the stage for 2024\\nA week of new developments in impeachment, Donald Trump’s D.C. case, and Hunter Biden’s congressional inquiry showcased how the collision of law and politics will determine much of Republicans’ and Democrats’ political fortunes in 2024.\\n | Francis Chung/POLITICO\\nPolitics\\nCornel West thinks Biden won’t make it to the general election\\nThe independent candidate rejected the idea he could be a “spoiler” for Biden in an exclusive meeting with POLITICO.\\n\",\"score\":0.9069832,\"raw_content\":null},{\"title\":\"DNC 2024 live updates: Walz speaks tonight ahead of Harris' remarks ...\",\"url\":\"https://www.nbcnews.com/politics/2024-election/live-blog/election-2024-dnc-live-updates-rcna165228\",\"content\":\"Latest news and live updates on the Democratic National Convention and the 2024 presidential election campaigns as Harris and ... Navy, Coast Guard, Air Force Space Force, or the United States ...\",\"score\":0.8344069,\"raw_content\":null}]",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-9-5)   "name": "tavily_search_results_json",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-9-6)   "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-9-7)   "response_metadata": {},
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-9-8)   "tool_call_id": "call_SRihR0BFFtw3TlHQtiBDPR3v"
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-9-9)  }
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-9-10) ]
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-9-11)}

```


### Define Edge Logic[¶](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#define-edge-logic "Permanent link")

We can define some of the edge logic that is needed to decide what to do based on results of the agents

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-10-1)import{AIMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-10-2)// Either agent can decide to end
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-10-3)functionrouter(state:typeofAgentState.State){
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-10-4)constmessages=state.messages;
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-10-5)constlastMessage=messages[messages.length-1]asAIMessage;
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-10-6)if(lastMessage?.tool_calls&&lastMessage.tool_calls.length>0){
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-10-7)// The previous agent is invoking a tool
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-10-8)return"call_tool";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-10-9)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-10-10)if(
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-10-11)typeoflastMessage.content==="string"&&
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-10-12)lastMessage.content.includes("FINAL ANSWER")
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-10-13)){
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-10-14)// Any agent decided the work is done
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-10-15)return"end";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-10-16)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-10-17)return"continue";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-10-18)}

```


### Define the Graph[¶](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#define-the-graph "Permanent link")

We can now put it all together and define the graph!

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-11-1)import{END,START,StateGraph}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-11-2)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-11-3)// 1. Create the graph
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-11-4)constworkflow=newStateGraph(AgentState)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-11-5)// 2. Add the nodes; these will do the work
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-11-6).addNode("Researcher",researchNode)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-11-7).addNode("ChartGenerator",chartNode)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-11-8).addNode("call_tool",toolNode);
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-11-9)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-11-10)// 3. Define the edges. We will define both regular and conditional ones
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-11-11)// After a worker completes, report to supervisor
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-11-12)workflow.addConditionalEdges("Researcher",router,{
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-11-13)// We will transition to the other agent
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-11-14)continue:"ChartGenerator",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-11-15)call_tool:"call_tool",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-11-16)end:END,
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-11-17)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-11-18)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-11-19)workflow.addConditionalEdges("ChartGenerator",router,{
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-11-20)// We will transition to the other agent
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-11-21)continue:"Researcher",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-11-22)call_tool:"call_tool",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-11-23)end:END,
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-11-24)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-11-25)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-11-26)workflow.addConditionalEdges(
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-11-27)"call_tool",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-11-28)// Each agent node updates the 'sender' field
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-11-29)// the tool calling node does not, meaning
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-11-30)// this edge will route back to the original agent
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-11-31)// who invoked the tool
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-11-32)(x)=>x.sender,
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-11-33){
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-11-34)Researcher:"Researcher",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-11-35)ChartGenerator:"ChartGenerator",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-11-36)},
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-11-37));
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-11-38)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-11-39)workflow.addEdge(START,"Researcher");
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-11-40)constgraph=workflow.compile();

```


## Invoke[¶](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#invoke "Permanent link")

With the graph created, you can invoke it! Let's have it chart some stats for us.

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-12-1)conststreamResults=awaitgraph.stream(
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-12-2){
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-12-3)messages:[
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-12-4)newHumanMessage({
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-12-5)content:"Generate a bar chart of the US gdp over the past 3 years.",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-12-6)}),
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-12-7)],
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-12-8)},
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-12-9){recursionLimit:150},
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-12-10));
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-12-11)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-12-12)constprettifyOutput=(output:Record<string,any>)=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-12-13)constkeys=Object.keys(output);
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-12-14)constfirstItem=output[keys[0]];
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-12-15)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-12-16)if("messages"infirstItem&&Array.isArray(firstItem.messages)){
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-12-17)constlastMessage=firstItem.messages[firstItem.messages.length-1];
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-12-18)console.dir({
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-12-19)type:lastMessage._getType(),
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-12-20)content:lastMessage.content,
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-12-21)tool_calls:lastMessage.tool_calls,
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-12-22)},{depth:null});
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-12-23)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-12-24)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-12-25)if("sender"infirstItem){
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-12-26)console.log({
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-12-27)sender:firstItem.sender,
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-12-28)})
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-12-29)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-12-30)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-12-31)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-12-32)forawait(constoutputofawaitstreamResults){
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-12-33)if(!output?.__end__){
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-12-34)prettifyOutput(output);
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-12-35)console.log("----");
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-12-36)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-12-37)}

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-13-1){
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-13-2) type: 'ai',
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-13-3) content: '',
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-13-4) tool_calls: [
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-13-5)  {
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-13-6)   name: 'tavily_search_results_json',
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-13-7)   args: { input: 'US GDP over the past 3 years' },
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-13-8)   type: 'tool_call',
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-13-9)   id: 'call_ZrmEsfu4B8SKpDhUJY5vcps8'
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-13-10)  }
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-13-11) ]
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-13-12)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-13-13){ sender: 'Researcher' }
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-13-14)----
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-13-15){
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-13-16) type: 'tool',
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-13-17) content: `[{"title":"United States GDP Annual Growth Rate - TRADING ECONOMICS","url":"https://tradingeconomics.com/united-states/gdp-growth-annual","content":"The Gross Domestic Product (GDP) in the United States expanded 3.10 percent in the second quarter of 2024 over the same quarter of the previous year. This page provides the latest reported value for - United States GDP Annual Growth Rate - plus previous releases, historical high and low, short-term forecast and long-term prediction, economic calendar, survey consensus and news.","score":0.88798404,"raw_content":null},{"title":"U.S. GDP 1960-2024 | MacroTrends","url":"https://www.macrotrends.net/global-metrics/countries/USA/united-states/gdp-gross-domestic-product","content":"U.S. gdp for 2021 was $23,315.08B, a 10.71% increase from 2020. U.S. gdp for 2020 was $21,060.47B, a 1.5% decline from 2019. U.S. gdp for 2019 was $21,380.98B, a 4.13% increase from 2018. GDP at purchaser's prices is the sum of gross value added by all resident producers in the economy plus any product taxes and minus any subsidies not included ...","score":0.7666432,"raw_content":null},{"title":"U.S. GDP Growth Rate 1960-2024 | MacroTrends","url":"https://www.macrotrends.net/global-metrics/countries/USA/united-states/gdp-growth-rate","content":"U.S. gdp growth rate for 2021 was 5.95%, a 8.71% increase from 2020. U.S. gdp growth rate for 2020 was -2.77%, a 5.06% decline from 2019. U.S. gdp growth rate for 2019 was 2.29%, a 0.65% decline from 2018. Annual percentage growth rate of GDP at market prices based on constant local currency. Aggregates are based on constant 2010 U.S. dollars.","score":0.6904547,"raw_content":null},{"title":"U.S. GDP by Year, Compared to Recessions and Events - The Balance","url":"https://www.thebalancemoney.com/us-gdp-by-year-3305543","content":"U.S. GDP by Year, Compared to Recessions and Events\\nThe Strange Ups and Downs of the U.S. Economy Since 1929\\nThe Balance / Julie Bang\\nU.S. gross domestic product (GDP) by year is a good overview of economic growth in the United States. Rebasing changes the reference year (or base year) for the real (chained dollar and quantity index) estimates and price indexes and expresses GDP and other NIPA aggregates in terms of the prices of one year. You can compare the GDP by year to fiscal and monetary policies to get a complete picture of what works and what doesn't in the U.S. economy.\\n Real GDP is important because without canceling out the effects of inflation, the GDP could appear to grow, when really all that's happened is an increase in prices.\\n Key Takeaways\\nTypes of GDP\\nThe Bureau of Economic Analysis compiles the data.","score":0.5998954,"raw_content":null},{"title":"US GDP over time - USAFacts","url":"https://usafacts.org/data/topics/economy/economic-indicators/gdp/gross-domestic-product/","content":"Data Adjustments\\nIs the economy growing?\\nRelated Metrics\\nAnnual percent change in real GDP\\n5.7%\\n2021\\nAnnual percent change in real GDP\\n5.7%\\n2021\\nExplore Gross domestic product\\nInteract with the data\\nData Adjustments\\nState Display\\nOur nation, in numbers\\nUSAFacts is a not-for-profit, nonpartisan civic initiative making government data easy for all Americans to access and understand.\\n • Check your spelling\\n• Try other search terms\\n• Use fewer words\\nGross domestic product\\nGross domestic product\\nGross domestic product (GDP) is the value of all goods and services produced in the US. All topics\\nExplore articles, data and trends by topic\\nAbout\\nWhat makes USAFacts different\\nWe frequently add data and we're interested in what would be useful to people. Newsletter\\nData delivered to your inbox\\nKeep up with the latest data and most popular content. But only the official BEA inflation-adjusted \\"real GDP\\" value is used to calculate annual percent change in GDP and therefore how well the economy is doing.","score":0.42083758,"raw_content":null}]`,
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-13-18) tool_calls: undefined
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-13-19)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-13-20)----
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-13-21){
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-13-22) type: 'human',
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-13-23) content: 'Here are the U.S. GDP values over the past 3 years:\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-13-24)  '\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-13-25)  '1. **2021**: $23,315.08 billion\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-13-26)  '2. **2022:** No specific value obtained from the search, but we can infer trends from growth rates\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-13-27)  '3. **2023:** No specific value obtained from the search, but we can infer trends from growth rates\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-13-28)  '\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-13-29)  'Given this, further insight can be derived from additional data sources, economic reports, or databases to fill in the missing GDP values for 2022 and 2023.',
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-13-30) tool_calls: undefined
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-13-31)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-13-32){ sender: 'Researcher' }
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-13-33)----
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-13-34){
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-13-35) type: 'ai',
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-13-36) content: '',
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-13-37) tool_calls: [
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-13-38)  {
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-13-39)   name: 'generate_bar_chart',
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-13-40)   args: {
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-13-41)    data: [
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-13-42)     { label: '2021', value: 23315.08 },
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-13-43)     { label: '2022', value: 25514.3 },
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-13-44)     { label: '2023', value: 27857.73 }
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-13-45)    ]
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-13-46)   },
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-13-47)   type: 'tool_call',
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-13-48)   id: 'call_CKH68vipCp9DshSVmw2vIZpK'
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-13-49)  }
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-13-50) ]
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-13-51)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-13-52){ sender: 'ChartGenerator' }
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-13-53)----

```


![]()

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-14-1){
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-14-2) type: 'tool',
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-14-3) content: 'Chart has been generated and displayed to the user!',
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-14-4) tool_calls: undefined
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-14-5)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-14-6)----
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-14-7){
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-14-8) type: 'human',
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-14-9) content: 'FINAL ANSWER: The bar chart displaying the U.S. GDP over the past 3 years has been generated and displayed. The values used are as follows:\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-14-10)  '\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-14-11)  '- **2021**: $23,315.08 billion\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-14-12)  '- **2022**: $25,514.3 billion (approximate)\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-14-13)  '- **2023**: $27,857.73 billion (approximate)\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-14-14)  '\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-14-15)  'Please refer to the chart for a visual representation of the data.\n',
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-14-16) tool_calls: undefined
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-14-17)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-14-18){ sender: 'ChartGenerator' }
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__codelineno-14-19)----

```


[Click here](https://smith.langchain.com/public/a79e2a74-5993-4542-b041-c77f1aa02200/r) to see a LangSmith trace of the above run.  Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  Self-RAG  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_self_rag/) [ Next  Agent Supervisor  ](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
