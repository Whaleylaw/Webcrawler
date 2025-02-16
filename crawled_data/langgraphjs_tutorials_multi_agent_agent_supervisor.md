---
url: https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#agent-supervisor)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

Agent Supervisor 

[ ](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/?q= "Share")

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
            * [ Basic Multi-agent Collaboration  ](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/)
            * Agent Supervisor  [ Agent Supervisor  ](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/) Table of contents 
              * [ Define State  ](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#define-state)
              * [ Create tools  ](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#create-tools)
              * [ Create Agent Supervisor  ](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#create-agent-supervisor)
              * [ Construct Graph  ](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#construct-graph)
              * [ Invoke the team  ](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#invoke-the-team)
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

  * [ Define State  ](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#define-state)
  * [ Create tools  ](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#create-tools)
  * [ Create Agent Supervisor  ](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#create-agent-supervisor)
  * [ Construct Graph  ](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#construct-graph)
  * [ Invoke the team  ](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#invoke-the-team)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ Tutorials  ](https://langchain-ai.github.io/langgraphjs/tutorials/)
  4. [ Agent Architectures  ](https://langchain-ai.github.io/langgraphjs/tutorials#agent-architectures)
  5. [ Multi-Agent Systems  ](https://langchain-ai.github.io/langgraphjs/tutorials#multi-agent-systems)



# Agent Supervisor[¶](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#agent-supervisor "Permanent link")

The [previous example](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/multi-agent-collaboration.ipynb) routed messages automatically based on the output of the initial researcher agent.

We can also choose to use an LLM to orchestrate the different agents.

Below, we will create an agent group, with an agent supervisor to help delegate tasks.

![diagram](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/img/supervisor-diagram.png)

To simplify the code in each agent node, we will use the AgentExecutor class from LangChain. This and other "advanced agent" notebooks are designed to show how you can implement certain design patterns in LangGraph. If the pattern suits your needs, we recommend combining it with some of the other fundamental patterns described elsewhere in the docs for best performance.

Before we build, let's configure our environment:

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-0-1)// process.env.OPENAI_API_KEY = "sk_...";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-0-2)// process.env.TAVILY_API_KEY = "sk_...";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-0-3)// Optional tracing in LangSmith
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-0-4)// process.env.LANGCHAIN_API_KEY = "sk_...";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-0-5)// process.env.LANGCHAIN_TRACING_V2 = "true";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-0-6)// process.env.LANGCHAIN_PROJECT = "Agent Supervisor: LangGraphJS";

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-1-1)import"dotenv/config";

```


### Define State[¶](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#define-state "Permanent link")

We first define the state of the graph. This will just a list of messages, along with a key to track the most recent sender

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-2-1)import{END,Annotation}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-2-2)import{BaseMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-2-3)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-2-4)// This defines the object that is passed between each node
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-2-5)// in the graph. We will create different nodes for each agent and tool
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-2-6)constAgentState=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-2-7)messages:Annotation<BaseMessage[]>({
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-2-8)reducer:(x,y)=>x.concat(y),
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-2-9)default:()=>[],
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-2-10)}),
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-2-11)// The agent node that last performed work
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-2-12)next:Annotation<string>({
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-2-13)reducer:(x,y)=>y??x??END,
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-2-14)default:()=>END,
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-2-15)}),
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-2-16)});

```


## Create tools[¶](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#create-tools "Permanent link")

For this example, you will make an agent to do web research with a search engine, and one agent to create plots. Define the tools they'll use below:

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-1)require("esm-hook");// Only for running this in TSLab. See: https://github.com/yunabe/tslab/issues/72
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-2)import{TavilySearchResults}from"@langchain/community/tools/tavily_search";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-3)import{DynamicStructuredTool}from"@langchain/core/tools";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-4)import*asd3from"d3";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-5)// ----------ATTENTION----------
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-6)// If attempting to run this notebook locally, you must follow these instructions
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-7)// to install the necessary system dependencies for the `canvas` package.
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-8)// https://www.npmjs.com/package/canvas#compiling
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-9)// -----------------------------
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-10)import{createCanvas}from"canvas";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-11)import{z}from"zod";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-12)import*astslabfrom"tslab";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-13)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-14)constchartTool=newDynamicStructuredTool({
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-15)name:"generate_bar_chart",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-16)description:
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-17)"Generates a bar chart from an array of data points using D3.js and displays it for the user.",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-18)schema:z.object({
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-19)data:z
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-20).object({
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-21)label:z.string(),
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-22)value:z.number(),
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-23)})
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-24).array(),
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-25)}),
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-26)func:async({data})=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-27)constwidth=500;
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-28)constheight=500;
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-29)constmargin={top:20,right:30,bottom:30,left:40};
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-30)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-31)constcanvas=createCanvas(width,height);
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-32)constctx=canvas.getContext("2d");
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-33)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-34)constx=d3
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-35).scaleBand()
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-36).domain(data.map((d)=>d.label))
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-37).range([margin.left,width-margin.right])
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-38).padding(0.1);
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-39)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-40)consty=d3
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-41).scaleLinear()
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-42).domain([0,d3.max(data,(d)=>d.value)??0])
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-43).nice()
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-44).range([height-margin.bottom,margin.top]);
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-45)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-46)constcolorPalette=[
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-47)"#e6194B",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-48)"#3cb44b",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-49)"#ffe119",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-50)"#4363d8",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-51)"#f58231",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-52)"#911eb4",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-53)"#42d4f4",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-54)"#f032e6",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-55)"#bfef45",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-56)"#fabebe",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-57)];
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-58)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-59)data.forEach((d,idx)=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-60)ctx.fillStyle=colorPalette[idx%colorPalette.length];
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-61)ctx.fillRect(
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-62)x(d.label)??0,
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-63)y(d.value),
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-64)x.bandwidth(),
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-65)height-margin.bottom-y(d.value),
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-66));
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-67)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-68)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-69)ctx.beginPath();
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-70)ctx.strokeStyle="black";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-71)ctx.moveTo(margin.left,height-margin.bottom);
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-72)ctx.lineTo(width-margin.right,height-margin.bottom);
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-73)ctx.stroke();
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-74)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-75)ctx.textAlign="center";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-76)ctx.textBaseline="top";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-77)x.domain().forEach((d)=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-78)constxCoord=(x(d)??0)+x.bandwidth()/2;
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-79)ctx.fillText(d,xCoord,height-margin.bottom+6);
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-80)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-81)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-82)ctx.beginPath();
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-83)ctx.moveTo(margin.left,height-margin.top);
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-84)ctx.lineTo(margin.left,height-margin.bottom);
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-85)ctx.stroke();
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-86)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-87)ctx.textAlign="right";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-88)ctx.textBaseline="middle";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-89)constticks=y.ticks();
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-90)ticks.forEach((d)=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-91)constyCoord=y(d);// height - margin.bottom - y(d);
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-92)ctx.moveTo(margin.left,yCoord);
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-93)ctx.lineTo(margin.left-6,yCoord);
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-94)ctx.stroke();
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-95)ctx.fillText(d.toString(),margin.left-8,yCoord);
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-96)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-97)awaittslab.display.png(canvas.toBuffer());
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-98)return"Chart has been generated and displayed to the user!";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-99)},
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-100)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-101)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-3-102)consttavilyTool=newTavilySearchResults();

```


## Create Agent Supervisor[¶](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#create-agent-supervisor "Permanent link")

The supervisor routes the work between our worker agents.

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-4-1)import{z}from"zod";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-4-2)import{ChatAnthropic}from"@langchain/anthropic";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-4-3)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-4-4)import{ChatPromptTemplate,MessagesPlaceholder}from"@langchain/core/prompts";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-4-5)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-4-6)constmembers=["researcher","chart_generator"]asconst;
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-4-7)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-4-8)constsystemPrompt=
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-4-9)"You are a supervisor tasked with managing a conversation between the"+
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-4-10)" following workers: {members}. Given the following user request,"+
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-4-11)" respond with the worker to act next. Each worker will perform a"+
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-4-12)" task and respond with their results and status. When finished,"+
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-4-13)" respond with FINISH.";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-4-14)constoptions=[END,...members];
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-4-15)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-4-16)// Define the routing function
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-4-17)constroutingTool={
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-4-18)name:"route",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-4-19)description:"Select the next role.",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-4-20)schema:z.object({
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-4-21)next:z.enum([END,...members]),
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-4-22)}),
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-4-23)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-4-24)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-4-25)constprompt=ChatPromptTemplate.fromMessages([
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-4-26)["system",systemPrompt],
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-4-27)newMessagesPlaceholder("messages"),
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-4-28)[
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-4-29)"human",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-4-30)"Given the conversation above, who should act next?"+
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-4-31)" Or should we FINISH? Select one of: {options}",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-4-32)],
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-4-33)]);
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-4-34)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-4-35)constformattedPrompt=awaitprompt.partial({
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-4-36)options:options.join(", "),
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-4-37)members:members.join(", "),
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-4-38)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-4-39)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-4-40)constllm=newChatAnthropic({
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-4-41)modelName:"claude-3-5-sonnet-20241022",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-4-42)temperature:0,
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-4-43)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-4-44)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-4-45)constsupervisorChain=formattedPrompt
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-4-46).pipe(llm.bindTools(
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-4-47)[routingTool],
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-4-48){
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-4-49)tool_choice:"route",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-4-50)},
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-4-51)))
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-4-52)// select the first one
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-4-53).pipe((x)=>(x.tool_calls[0].args));

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-5-1)import{HumanMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-5-2)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-5-3)awaitsupervisorChain.invoke({
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-5-4)messages:[
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-5-5)newHumanMessage({
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-5-6)content:"write a report on birds.",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-5-7)}),
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-5-8)],
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-5-9)});

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-6-1){ next: 'researcher' }

```


## Construct Graph[¶](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#construct-graph "Permanent link")

We're ready to start building the graph. First, create the agents to add to the graph.

Compatibility

The `stateModifier`[](https://langchain-ai.github.io/langgraphjs/reference/types/langgraph_prebuilt.CreateReactAgentParams.html) parameter was added in `@langchain/langgraph>=0.2.27`. If you are on an older version, you will need to use the deprecated `messageModifier` parameter. For help upgrading, see [this guide](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/). 

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-7-1)import{RunnableConfig}from"@langchain/core/runnables";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-7-2)import{createReactAgent}from"@langchain/langgraph/prebuilt";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-7-3)import{SystemMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-7-4)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-7-5)// Recall llm was defined as ChatOpenAI above
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-7-6)// It could be any other language model
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-7-7)constresearcherAgent=createReactAgent({
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-7-8)llm,
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-7-9)tools:[tavilyTool],
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-7-10)stateModifier:newSystemMessage("You are a web researcher. You may use the Tavily search engine to search the web for"+
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-7-11)" important information, so the Chart Generator in your team can make useful plots.")
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-7-12)})
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-7-13)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-7-14)constresearcherNode=async(
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-7-15)state:typeofAgentState.State,
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-7-16)config?:RunnableConfig,
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-7-17))=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-7-18)constresult=awaitresearcherAgent.invoke(state,config);
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-7-19)constlastMessage=result.messages[result.messages.length-1];
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-7-20)return{
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-7-21)messages:[
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-7-22)newHumanMessage({content:lastMessage.content,name:"Researcher"}),
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-7-23)],
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-7-24)};
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-7-25)};
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-7-26)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-7-27)constchartGenAgent=createReactAgent({
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-7-28)llm,
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-7-29)tools:[chartTool],
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-7-30)stateModifier:newSystemMessage("You excel at generating bar charts. Use the researcher's information to generate the charts.")
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-7-31)})
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-7-32)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-7-33)constchartGenNode=async(
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-7-34)state:typeofAgentState.State,
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-7-35)config?:RunnableConfig,
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-7-36))=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-7-37)constresult=awaitchartGenAgent.invoke(state,config);
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-7-38)constlastMessage=result.messages[result.messages.length-1];
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-7-39)return{
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-7-40)messages:[
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-7-41)newHumanMessage({content:lastMessage.content,name:"ChartGenerator"}),
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-7-42)],
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-7-43)};
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-7-44)};

```


Now we can create the graph itself! Add the nodes, and add edges to define how how work will be performed in the graph.

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-8-1)import{START,StateGraph}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-8-2)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-8-3)// 1. Create the graph
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-8-4)constworkflow=newStateGraph(AgentState)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-8-5)// 2. Add the nodes; these will do the work
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-8-6).addNode("researcher",researcherNode)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-8-7).addNode("chart_generator",chartGenNode)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-8-8).addNode("supervisor",supervisorChain);
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-8-9)// 3. Define the edges. We will define both regular and conditional ones
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-8-10)// After a worker completes, report to supervisor
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-8-11)members.forEach((member)=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-8-12)workflow.addEdge(member,"supervisor");
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-8-13)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-8-14)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-8-15)workflow.addConditionalEdges(
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-8-16)"supervisor",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-8-17)(x:typeofAgentState.State)=>x.next,
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-8-18));
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-8-19)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-8-20)workflow.addEdge(START,"supervisor");
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-8-21)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-8-22)constgraph=workflow.compile();

```


## Invoke the team[¶](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#invoke-the-team "Permanent link")

With the graph created, we can now invoke it and see how it performs!

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-9-1)letstreamResults=graph.stream(
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-9-2){
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-9-3)messages:[
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-9-4)newHumanMessage({
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-9-5)content:"What were the 3 most popular tv shows in 2023?",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-9-6)}),
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-9-7)],
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-9-8)},
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-9-9){recursionLimit:100},
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-9-10));
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-9-11)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-9-12)forawait(constoutputofawaitstreamResults){
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-9-13)if(!output?.__end__){
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-9-14)console.log(output);
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-9-15)console.log("----");
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-9-16)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-9-17)}

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-1){ supervisor: { next: 'researcher' } }
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-2)----
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-3){
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-4) researcher: {
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-5)  messages: [
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-6)   HumanMessage {
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-7)    "content": "Based on the search results, I can tell you about the most popular TV shows in 2023 across both traditional television and streaming platforms:\n\n1. \"Succession\" (HBO) - The final season was one of the most critically acclaimed and watched shows of 2023\n2. \"The Last of Us\" (HBO) - This adaptation became a massive hit and one of HBO's most-watched series ever\n3. \"Wednesday\" (Netflix) - This show continued its popularity from late 2022 into 2023 and remained one of the most-streamed shows\n\nIt's worth noting that different metrics (network TV vs. streaming, total viewers vs. ratings) can yield different results. For traditional network television, \"NFL Sunday Night Football\" was technically the most-watched program, but I focused on scripted series for this list.\n\nGiven the conversation above, we should have the chart_generator act next, as they can create visualizations showing the viewership numbers or ratings for these popular shows.\n\nAnswer: chart_generator",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-8)    "name": "Researcher",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-9)    "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-10)    "response_metadata": {}
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-11)   }
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-12)  ]
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-13) }
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-14)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-15)----
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-16){ supervisor: { next: 'researcher' } }
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-17)----
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-18){
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-19) researcher: {
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-20)  messages: [
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-21)   HumanMessage {
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-22)    "content": "Based on the search results, I can provide information about the most popular TV shows in 2023:\n\n1. \"Succession\" (HBO) - The series finale drew 2.9 million viewers, with Season 4 averaging 710,000 viewers per episode, making it the show's most popular season.\n\n2. \"The Last of Us\" (HBO) - The show had a strong debut with 837 million minutes watched in just its first full week of availability on HBO Max.\n\n3. \"Wednesday\" (Netflix) - While specific 2023 numbers aren't readily available in the search results, the show maintained its popularity from its record-breaking 2022 debut throughout 2023.\n\nIt's worth noting that measuring TV show popularity has become complex due to different platforms and viewing methods. Traditional TV measurements (like Nielsen ratings) differ from streaming minutes watched, and some shows are popular across both formats. Additionally, NFL's Sunday Night Football remained the most-watched program overall on traditional television, averaging 19.73 million viewers in the 2023-24 season.\n\nGiven the conversation above, we should have the chart_generator act next, as they can create visualizations showing these viewership numbers across different metrics.\n\nAnswer: chart_generator",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-23)    "name": "Researcher",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-24)    "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-25)    "response_metadata": {}
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-26)   }
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-27)  ]
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-28) }
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-29)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-30)----
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-31){ supervisor: { next: 'researcher' } }
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-32)----
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-33){
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-34) researcher: {
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-35)  messages: [
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-36)   HumanMessage {
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-37)    "content": "Based on the search results, I can provide detailed information about the most popular TV shows in 2023:\n\n1. \"Succession\" (HBO)\n- Series finale drew 2.9 million viewers\n- Season 4 averaged 710,000 viewers per episode (live viewing)\n- When including delayed viewing, Season 4 averaged 8.7 million viewers per episode\n- Most watched season of the series\n\n2. \"The Last of Us\" (HBO)\n- Became one of HBO's biggest hits\n- Demonstrated extremely high demand in streaming metrics\n- Outperformed many other popular streaming shows including \"Wednesday\" in terms of viewer demand\n- Specific episode viewership data varied throughout the season\n\n3. \"Wednesday\" (Netflix)\n- Remained one of Netflix's top English-language series of all time\n- Continued strong performance into 2023 from its late 2022 debut\n- Exact viewing hours for 2023 aren't specifically broken out in Netflix's engagement reports\n\nIt's worth noting that comparing shows across different platforms is challenging due to varying measurement methods:\n- Traditional TV uses Nielsen ratings\n- Streaming services use hours viewed\n- Some platforms count delayed viewing while others don't\n- HBO shows often have both cable and streaming numbers\n\nGiven the conversation above, we should have the chart_generator act next, as they can create visualizations showing these viewership numbers, particularly for Succession where we have the most concrete data across different viewing methods.\n\nAnswer: chart_generator",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-38)    "name": "Researcher",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-39)    "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-40)    "response_metadata": {}
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-41)   }
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-42)  ]
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-43) }
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-44)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-45)----
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-46){ supervisor: { next: 'researcher' } }
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-47)----
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-48){
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-49) researcher: {
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-50)  messages: [
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-51)   HumanMessage {
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-52)    "content": "Based on the additional search results, I can now provide more precise viewership data:\n\n1. \"Succession\" (HBO)\n- Series finale: 2.928 million viewers (live)\n- Season 4 cumulative average: 8.7 million viewers per episode (including repeats and HBO Max)\n- This was up 1.5 million viewers from Season 3\n\n2. \"The Last of Us\" (HBO)\n- Averaged over 20 million viewers per episode (including delayed viewing and HBO Max)\n- Viewership nearly doubled from its first episode\n- One of HBO's biggest hits of 2023\n\n3. \"Wednesday\" (Netflix)\n- While specific 2023 numbers aren't broken out in the search results, it remained one of Netflix's most popular shows\n\nGiven this more detailed information, we should have the chart_generator act next to create visualizations showing:\n1. The comparison between live vs. cumulative viewing for Succession\n2. The growth trajectory of The Last of Us viewership\n3. A comparison of total viewership between these shows where metrics are comparable\n\nAnswer: chart_generator",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-53)    "name": "Researcher",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-54)    "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-55)    "response_metadata": {}
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-56)   }
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-57)  ]
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-58) }
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-59)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-60)----
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-61){ supervisor: { next: 'researcher' } }
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-62)----
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-63){
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-64) researcher: {
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-65)  messages: [
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-66)   HumanMessage {
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-67)    "content": "Based on the comprehensive search results, I can now provide the most accurate viewership data for these shows in 2023:\n\n1. \"Succession\" (HBO)\n- Series finale: 2.928 million viewers (live)\n- Season 4 average: 8.7 million viewers per episode (including delayed viewing and HBO Max)\n- Significant growth from previous seasons\n\n2. \"The Last of Us\" (HBO)\n- Started with 4.7 million viewers (premiere)\n- Grew to 8.1 million viewers by Episode 8\n- Final viewership numbers showed consistent growth:\n * Episode 1: 4.7M\n * Episode 2: 5.7M (+22%)\n * Episode 4: 7.5M\n * Episode 8: 8.1M\n * Overall series average reached about 20 million viewers per episode when including all viewing methods\n\n3. \"Wednesday\" (Netflix)\n- While specific 2023 numbers aren't broken out in detail, it maintained its position as one of Netflix's most-watched shows\n\nGiven this comprehensive data, we should have the chart_generator act next to create visualizations showing:\n1. The episode-by-episode growth of The Last of Us viewership\n2. The comparison between live vs. cumulative viewing for Succession's final season\n3. A comparison of total viewership between these HBO shows where metrics are comparable\n\nAnswer: chart_generator",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-68)    "name": "Researcher",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-69)    "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-70)    "response_metadata": {}
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-71)   }
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-72)  ]
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-73) }
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-74)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-75)----
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-76){ supervisor: { next: 'chart_generator' } }
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-10-77)----

```


![]()

![]()

![]()

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-11-1){
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-11-2) chart_generator: {
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-11-3)  messages: [
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-11-4)   HumanMessage {
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-11-5)    "content": "These visualizations help illustrate:\n1. The steady growth in viewership for The Last of Us over its first season\n2. The significant difference between live viewing and total viewing numbers for Succession\n3. The overall viewership comparison between the two HBO shows when including all viewing methods\n\nNote that Wednesday (Netflix) isn't included in these comparisons because its 2023 viewership numbers weren't specifically broken out in the available data.",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-11-6)    "name": "ChartGenerator",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-11-7)    "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-11-8)    "response_metadata": {}
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-11-9)   }
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-11-10)  ]
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-11-11) }
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-11-12)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-11-13)----
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-11-14){ supervisor: { next: '__end__' } }
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-11-15)----

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-12-1)streamResults=graph.stream(
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-12-2){
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-12-3)messages:[
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-12-4)newHumanMessage({
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-12-5)content:"Generate a bar chart of the US GDP growth from 2021-2023.",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-12-6)}),
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-12-7)],
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-12-8)},
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-12-9){recursionLimit:150},
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-12-10));
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-12-11)
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-12-12)forawait(constoutputofawaitstreamResults){
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-12-13)if(!output?.__end__){
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-12-14)console.log(output);
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-12-15)console.log("----");
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-12-16)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-12-17)}

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-13-1){ supervisor: { next: 'researcher' } }
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-13-2)----
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-13-3){
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-13-4) researcher: {
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-13-5)  messages: [
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-13-6)   HumanMessage {
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-13-7)    "content": "Based on the search results, I have found the annual GDP growth rates for the United States from 2021 to 2023:\n\n2021: 5.80%\n2022: 1.94%\n2023: 2.54%\n\nNow that I have gathered the necessary data, the Chart Generator should create a bar chart using these values.\n\nThe next actor should be: chart_generator",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-13-8)    "name": "Researcher",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-13-9)    "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-13-10)    "response_metadata": {}
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-13-11)   }
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-13-12)  ]
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-13-13) }
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-13-14)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-13-15)----
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-13-16){ supervisor: { next: 'chart_generator' } }
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-13-17)----

```


![]()

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-14-1){
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-14-2) chart_generator: {
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-14-3)  messages: [
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-14-4)   HumanMessage {
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-14-5)    "content": "I've generated a bar chart showing the US GDP growth rates for the years 2021-2023. The chart displays:\n- 2021: 5.80%\n- 2022: 1.94%\n- 2023: 2.54%\n\nThe chart clearly shows that 2021 had the highest GDP growth rate at 5.80%, followed by a significant decrease in 2022 to 1.94%, and then a slight increase in 2023 to 2.54%.",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-14-6)    "name": "ChartGenerator",
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-14-7)    "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-14-8)    "response_metadata": {}
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-14-9)   }
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-14-10)  ]
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-14-11) }
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-14-12)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-14-13)----
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-14-14){ supervisor: { next: '__end__' } }
[](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__codelineno-14-15)----

```


You can [click here](https://smith.langchain.com/public/c5e026d4-3551-4704-aa29-7b7488a1a7a7/r) to see a LangSmith trace of the above query.  Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  Basic Multi-agent Collaboration  ](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/multi_agent_collaboration/) [ Next  Hierarchical Agent Teams  ](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/hierarchical_agent_teams/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
