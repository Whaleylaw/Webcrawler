---
url: https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#reasoning-without-observation)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

Reasoning without Observation 

[ ](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/?q= "Share")

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
          * [ Multi-Agent Systems  ](https://langchain-ai.github.io/langgraphjs/tutorials#multi-agent-systems)
          * [ Planning Agents  ](https://langchain-ai.github.io/langgraphjs/tutorials#planning-agents)
          * Reflection & Critique  Reflection & Critique 
            * [ Reflection & Critique  ](https://langchain-ai.github.io/langgraphjs/tutorials#reflection-critique)
            * [ Reflection  ](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/)
            * Reasoning without Observation  [ Reasoning without Observation  ](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/) Table of contents 
              * [ 0. Prerequisites  ](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#0-prerequisites)
                * [ Install dependencies  ](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#install-dependencies)
              * [ 1. Planner  ](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#1-planner)
                * [ Planner Node  ](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#planner-node)
              * [ 2. Executor  ](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#2-executor)
              * [ 3. Solver  ](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#3-solver)
              * [ 4. Define Graph  ](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#4-define-graph)
                * [ See the LangSmith trace here  ](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#see-the-langsmith-trace-here)
              * [ Conclusion  ](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#conclusion)
        * [ Evaluation & Analysis  ](https://langchain-ai.github.io/langgraphjs/tutorials#evaluation)
    * Resources  Resources 
      * [ Adopters  ](https://langchain-ai.github.io/langgraphjs/adopters/)
      * [ FAQ  ](https://langchain-ai.github.io/langgraphjs/concepts/faq/)
      * [ Troubleshooting  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraphjs/reference/)
  * [ Versions  ](https://langchain-ai.github.io/langgraphjs/versions/)



Table of contents 

  * [ 0. Prerequisites  ](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#0-prerequisites)
    * [ Install dependencies  ](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#install-dependencies)
  * [ 1. Planner  ](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#1-planner)
    * [ Planner Node  ](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#planner-node)
  * [ 2. Executor  ](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#2-executor)
  * [ 3. Solver  ](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#3-solver)
  * [ 4. Define Graph  ](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#4-define-graph)
    * [ See the LangSmith trace here  ](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#see-the-langsmith-trace-here)
  * [ Conclusion  ](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#conclusion)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ Tutorials  ](https://langchain-ai.github.io/langgraphjs/tutorials/)
  4. [ Agent Architectures  ](https://langchain-ai.github.io/langgraphjs/tutorials#agent-architectures)
  5. [ Reflection & Critique  ](https://langchain-ai.github.io/langgraphjs/tutorials#reflection-critique)



# Reasoning without Observation[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#reasoning-without-observation "Permanent link")

In [ReWOO](https://arxiv.org/abs/2305.18323), Xu, et. al, propose an agent that combines a multi-step planner and variable substitution for effective tool use. It was designed to improve on the ReACT-style agent architecture in the following ways:

  1. Reduce token consumption and execution time by generating the full chain of tools used in a single pass. (_ReACT-style agent architecture requires many LLM calls with redundant prefixes (since the system prompt and previous steps are provided to the LLM for each reasoning step_)
  2. Simplify the fine-tuning process. Since the planning data doesn't depend on the outputs of the tool, models can be fine-tuned without actually invoking the tools (in theory).



The following diagram outlines ReWOO's overall computation graph:

![ReWoo Diagram](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/img/rewoo.png)

ReWOO is made of 3 modules:

  1. 🧠**Planner** : Generate the plan in the following format:



```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-0-1)Plan: <reasoning>
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-0-2)#E1 = Tool[argument for tool]
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-0-3)Plan: <reasoning>
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-0-4)#E2 = Tool[argument for tool with #E1 variable substitution]
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-0-5)...

```


  1. **Worker** : executes the tool with the provided arguments.
  2. 🧠**Solver** : generates the answer for the initial task based on the tool observations.



The modules with a 🧠 emoji depend on an LLM call. Notice that we avoid redundant calls to the planner LLM by using variable substitution.

In this example, each module is represented by a LangGraph node. The end result will leave a trace that looks [like this one](https://smith.langchain.com/public/39dbdcf8-fbcc-4479-8e28-15377ca5e653/r). Let's get started!

## 0. Prerequisites[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#0-prerequisites "Permanent link")

For this example, we will provide the agent with a Tavily search engine tool. You can get an API key [here](https://app.tavily.com/sign-in) or replace with a free tool option (e.g., [duck duck go search](https://python.langchain.com/docs/integrations/tools/ddg)).

For this notebook, you should add a `.env` file at the root of the repo with `TAVILY_API_KEY`:

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-1-1)import"dotenv/config";

```


### Install dependencies[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#install-dependencies "Permanent link")

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-2-1)npminstalllangchain@langchain/community@langchain/openai@langchain/core

```


**Graph State** : In LangGraph, every node updates a shared graph state. The state is the input to any node whenever it is invoked.

Below, we will define a state object to contain the task, plan, steps, and other variables.

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-3-1)import{Annotation}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-3-2)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-3-3)constGraphState=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-3-4)task:Annotation<string>({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-3-5)reducer:(x,y)=>(y??x),
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-3-6)default:()=>"",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-3-7)}),
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-3-8)planString:Annotation<string>({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-3-9)reducer:(x,y)=>(y??x),
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-3-10)default:()=>"",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-3-11)}),
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-3-12)steps:Annotation<string[][]>({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-3-13)reducer:(x,y)=>x.concat(y),
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-3-14)default:()=>[],
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-3-15)}),
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-3-16)results:Annotation<Record<string,any>>({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-3-17)reducer:(x,y)=>({...x,...y}),
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-3-18)default:()=>({}),
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-3-19)}),
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-3-20)result:Annotation<string>({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-3-21)reducer:(x,y)=>(y??x),
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-3-22)default:()=>"",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-3-23)}),
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-3-24)})

```


## 1. Planner[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#1-planner "Permanent link")

The planner prompts an LLM to generate a plan in the form of a task list. The arguments to each task are strings that may contain special variables (`#E{{0-9}}+`) that are used for variable substitution from other task results.

![ReWOO workflow](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/img/rewoo-paper-workflow.png)

Our example agent will have two tools:

  1. Google - a search engine (in this case Tavily)
  2. LLM - an LLM call to reason about previous outputs.



The LLM tool receives less of the prompt context and so can be more token-efficient than the ReACT paradigm.

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-4-1)import{ChatOpenAI}from"@langchain/openai";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-4-2)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-4-3)constmodel=newChatOpenAI({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-4-4)model:"gpt-4o",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-4-5)temperature:0,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-4-6)});

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-5-1)import{ChatPromptTemplate}from"@langchain/core/prompts";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-5-2)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-5-3)consttemplate=
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-5-4)`For the following task, make plans that can solve the problem step by step. For each plan, indicate
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-5-5)which external tool together with tool input to retrieve evidence. You can store the evidence into a 
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-5-6)variable #E that can be called by later tools. (Plan, #E1, Plan, #E2, Plan, ...)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-5-7)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-5-8)Tools can be one of the following:
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-5-9)(1) Google[input]: Worker that searches results from Google. Useful when you need to find short
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-5-10)and succinct answers about a specific topic. The input should be a search query.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-5-11)(2) LLM[input]: A pre-trained LLM like yourself. Useful when you need to act with general 
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-5-12)world knowledge and common sense. Prioritize it when you are confident in solving the problem
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-5-13)yourself. Input can be any instruction.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-5-14)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-5-15)For example,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-5-16)Task: Thomas, Toby, and Rebecca worked a total of 157 hours in one week. Thomas worked x 
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-5-17)hours. Toby worked 10 hours less than twice what Thomas worked, and Rebecca worked 8 hours 
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-5-18)less than Toby. How many hours did Rebecca work? 
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-5-19)Plan: Given Thomas worked x hours, translate the problem into algebraic expressions and solve with Wolfram Alpha.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-5-20)#E1 = WolframAlpha[Solve x + (2x - 10) + ((2x - 10) - 8) = 157]
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-5-21)Plan: Find out the number of hours Thomas worked.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-5-22)#E2 = LLM[What is x, given #E1]
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-5-23)Plan: Calculate the number of hours Rebecca worked.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-5-24)#E3 = Calculator[(2 * #E2 - 10) - 8]
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-5-25)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-5-26)Important!
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-5-27)Variables/results MUST be referenced using the # symbol!
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-5-28)The plan will be executed as a program, so no coreference resolution apart from naive variable replacement is allowed.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-5-29)The ONLY way for steps to share context is by including #E<step> within the arguments of the tool.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-5-30)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-5-31)Begin! 
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-5-32)Describe your plans with rich details. Each Plan should be followed by only one #E.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-5-33)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-5-34)Task: {task}`;
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-5-35)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-5-36)constpromptTemplate=ChatPromptTemplate.fromMessages([["human",template]]);
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-5-37)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-5-38)constplanner=promptTemplate.pipe(model);
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-5-39)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-5-40)consttask="what is the hometown of the winner of the 2023 australian open?";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-5-41)awaitplanner.invoke({task});

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-6-1)AIMessage {
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-6-2) "id": "chatcmpl-9z88bDgCFkpWbYitlBSkuEaUU0YA2",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-6-3) "content": "Plan: Identify the winner of the 2023 Australian Open.\n#E1 = Google[\"winner of the 2023 Australian Open\"]\n\nPlan: Find the hometown of the winner identified in #E1.\n#E2 = Google[\"hometown of #E1\"]",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-6-4) "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-6-5) "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-6-6)  "tokenUsage": {
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-6-7)   "completionTokens": 55,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-6-8)   "promptTokens": 438,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-6-9)   "totalTokens": 493
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-6-10)  },
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-6-11)  "finish_reason": "stop",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-6-12)  "system_fingerprint": "fp_3aa7262c27"
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-6-13) },
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-6-14) "tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-6-15) "invalid_tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-6-16) "usage_metadata": {
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-6-17)  "input_tokens": 438,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-6-18)  "output_tokens": 55,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-6-19)  "total_tokens": 493
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-6-20) }
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-6-21)}

```


#### Planner Node[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#planner-node "Permanent link")

To connect the planner to our graph, we will create a `getPlan` node that accepts the `ReWOO` state and returns with a state update for the `steps` and `planString` fields.

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-7-1)import{RunnableConfig}from"@langchain/core/runnables";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-7-2)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-7-3)constregexPattern=newRegExp(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-7-4)"Plan\\s*\\d*:\\s*([^#]+)\\s*(#E\\d+)\\s*=\\s*(\\w+)\\s*\\[([^\\]]+)\\]",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-7-5)"g",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-7-6));
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-7-7)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-7-8)asyncfunctiongetPlan(state:typeofGraphState.State,config?:RunnableConfig){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-7-9)console.log("---GET PLAN---");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-7-10)consttask=state.task;
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-7-11)constresult=awaitplanner.invoke({task},config);
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-7-12)// Find all matches in the sample text.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-7-13)constmatches=result.content.toString().matchAll(regexPattern);
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-7-14)letsteps:string[][]=[];
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-7-15)for(constmatchofmatches){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-7-16)constitem=[match[1],match[2],match[3],match[4],match[0]];
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-7-17)if(item.some((i)=>i===undefined)){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-7-18)thrownewError("Invalid match");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-7-19)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-7-20)steps.push(itemasstring[]);
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-7-21)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-7-22)return{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-7-23)steps,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-7-24)planString:result.content.toString(),
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-7-25)};
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-7-26)}

```


## 2. Executor[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#2-executor "Permanent link")

The executor receives the plan and executes the tools in sequence.

Below, instantiate the search engine and define the tools execution node.

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-8-1)import{TavilySearchResults}from"@langchain/community/tools/tavily_search";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-8-2)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-8-3)constsearch=newTavilySearchResults();

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-9-1)const_getCurrentTask=(state:typeofGraphState.State)=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-9-2)console.log("_getCurrentTask",state);
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-9-3)if(!state.results){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-9-4)return1;
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-9-5)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-9-6)if(Object.entries(state.results).length===state.steps.length){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-9-7)returnnull;
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-9-8)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-9-9)returnObject.entries(state.results).length+1;
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-9-10)};
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-9-11)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-9-12)const_parseResult=(input:unknown)=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-9-13)if(typeofinput==="string"){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-9-14)constparsedInput=JSON.parse(input);
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-9-15)if(Array.isArray(parsedInput)&&"content"inparsedInput[0]){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-9-16)// This means it is a tool result.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-9-17)returnparsedInput.map(({content})=>content).join("\n");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-9-18)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-9-19)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-9-20)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-9-21)if(input&&typeofinput==="object"&&"content"ininput){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-9-22)// If it's not a tool, we know it's an LLM result.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-9-23)const{content}=input;
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-9-24)returncontent;
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-9-25)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-9-26)thrownewError("Invalid input received");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-9-27)};
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-9-28)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-9-29)asyncfunctiontoolExecution(state:typeofGraphState.State,config?:RunnableConfig){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-9-30)console.log("---EXECUTE TOOL---");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-9-31)const_step=_getCurrentTask(state);
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-9-32)if(_step===null){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-9-33)thrownewError("No current task found");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-9-34)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-9-35)const[_,stepName,tool,toolInputTemplate]=state.steps[_step-1];
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-9-36)lettoolInput=toolInputTemplate;
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-9-37)const_results=state.results||{};
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-9-38)for(const[k,v]ofObject.entries(_results)){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-9-39)toolInput=toolInput.replace(k,v);
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-9-40)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-9-41)letresult;
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-9-42)if(tool==="Google"){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-9-43)result=awaitsearch.invoke(toolInput,config);
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-9-44)}elseif(tool==="LLM"){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-9-45)result=awaitmodel.invoke(toolInput,config);
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-9-46)}else{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-9-47)thrownewError("Invalid tool specified");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-9-48)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-9-49)_results[stepName]=JSON.stringify(_parseResult(result),null,2);
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-9-50)return{results:_results};
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-9-51)}

```


## 3. Solver[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#3-solver "Permanent link")

The solver receives the full plan and generates the final response based on the responses of the tool calls from the worker.

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-10-1)constsolvePrompt=ChatPromptTemplate.fromTemplate(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-10-2)`Solve the following task or problem. To solve the problem, we have made step-by-step Plan and
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-10-3)retrieved corresponding Evidence to each Plan. Use them with caution since long evidence might
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-10-4)contain irrelevant information.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-10-5)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-10-6){plan}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-10-7)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-10-8)Now solve the question or task according to provided Evidence above. Respond with the answer
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-10-9)directly with no extra words.
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-10-10)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-10-11)Task: {task}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-10-12)Response:`,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-10-13));
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-10-14)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-10-15)asyncfunctionsolve(state:typeofGraphState.State,config?:RunnableConfig){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-10-16)console.log("---SOLVE---");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-10-17)letplan="";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-10-18)const_results=state.results||{};
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-10-19)for(let[_plan,stepName,tool,toolInput]ofstate.steps){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-10-20)for(const[k,v]ofObject.entries(_results)){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-10-21)toolInput=toolInput.replace(k,v);
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-10-22)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-10-23)plan+=`Plan: ${_plan}\n${stepName} = ${tool}[${toolInput}]\n`;
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-10-24)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-10-25)constmodel=newChatOpenAI({
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-10-26)temperature:0,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-10-27)model:"gpt-4o",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-10-28)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-10-29)constresult=awaitsolvePrompt
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-10-30).pipe(model)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-10-31).invoke({plan,task:state.task},config);
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-10-32)return{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-10-33)result:result.content.toString(),
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-10-34)};
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-10-35)}

```


## 4. Define Graph[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#4-define-graph "Permanent link")

Our graph defines the workflow. Each of the planner, tool executor, and solver modules are added as nodes.

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-11-1)import{END,START,StateGraph}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-11-2)import{MemorySaver}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-11-3)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-11-4)const_route=(state:typeofGraphState.State)=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-11-5)console.log("---ROUTE TASK---");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-11-6)const_step=_getCurrentTask(state);
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-11-7)if(_step===null){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-11-8)// We have executed all tasks
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-11-9)return"solve";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-11-10)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-11-11)// We are still executing tasks, loop back to the "tool" node
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-11-12)return"tool";
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-11-13)};
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-11-14)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-11-15)constworkflow=newStateGraph(GraphState)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-11-16).addNode("plan",getPlan)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-11-17).addNode("tool",toolExecution)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-11-18).addNode("solve",solve)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-11-19).addEdge("plan","tool")
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-11-20).addEdge("solve",END)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-11-21).addConditionalEdges("tool",_route)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-11-22).addEdge(START,"plan");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-11-23)
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-11-24)// Compile
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-11-25)constapp=workflow.compile({checkpointer:newMemorySaver()});

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-12-1)constthreadConfig={configurable:{thread_id:"123"}};
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-12-2)letfinalResult;
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-12-3)conststream=awaitapp.stream(
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-12-4){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-12-5)task:"what is the hometown of the winner of the 2023 australian open?",
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-12-6)},
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-12-7)threadConfig,
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-12-8));
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-12-9)forawait(constitemofstream){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-12-10)console.log(item);
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-12-11)console.log("-----");
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-12-12)finalResult=item;
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-12-13)}

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-1)---GET PLAN---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-2){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-3) plan: {
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-4)  planString: 'Plan: Identify the winner of the 2023 Australian Open.\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-5)   '#E1 = Google["winner of the 2023 Australian Open"]\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-6)   '\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-7)   'Plan: Find the hometown of the winner identified in #E1.\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-8)   '#E2 = Google["hometown of #E1"]',
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-9)  steps: [ [Array] ]
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-10) }
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-11)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-12)-----
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-13)---EXECUTE TOOL---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-14)_getCurrentTask {
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-15) task: 'what is the hometown of the winner of the 2023 australian open?',
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-16) planString: 'Plan: Identify the winner of the 2023 Australian Open.\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-17)  '#E1 = Google["winner of the 2023 Australian Open"]\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-18)  '\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-19)  'Plan: Find the hometown of the winner identified in #E1.\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-20)  '#E2 = Google["hometown of #E1"]',
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-21) steps: [
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-22)  [
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-23)   'Identify the winner of the 2023 Australian Open.\n',
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-24)   '#E1',
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-25)   'Google',
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-26)   '"winner of the 2023 Australian Open"',
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-27)   'Plan: Identify the winner of the 2023 Australian Open.\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-28)    '#E1 = Google["winner of the 2023 Australian Open"]'
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-29)  ]
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-30) ],
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-31) results: {},
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-32) result: ''
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-33)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-34)---ROUTE TASK---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-35)_getCurrentTask {
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-36) task: 'what is the hometown of the winner of the 2023 australian open?',
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-37) planString: 'Plan: Identify the winner of the 2023 Australian Open.\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-38)  '#E1 = Google["winner of the 2023 Australian Open"]\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-39)  '\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-40)  'Plan: Find the hometown of the winner identified in #E1.\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-41)  '#E2 = Google["hometown of #E1"]',
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-42) steps: [
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-43)  [
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-44)   'Identify the winner of the 2023 Australian Open.\n',
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-45)   '#E1',
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-46)   'Google',
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-47)   '"winner of the 2023 Australian Open"',
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-48)   'Plan: Identify the winner of the 2023 Australian Open.\n' +
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-49)    '#E1 = Google["winner of the 2023 Australian Open"]'
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-50)  ]
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-51) ],
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-52) results: {
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-53)  '#E1': `"A one-set shoot-off to decide the winner of the 2023 Australian Open. There could not have been a better script. SECOND SET (* denotes server) Sabalenka* 6-3 Rybakina - Wide second serve into the deuce court from Sabalenka and forehand return from Rybakina is long. Deep backhand crosscourt return from Rybakina draws a shot ball from Sabalenka ...\\nThe Crossword Solver found 30 answers to \\"Tennis player Sabalenka, winner of the 2023 Australian Open\\", 5 letters crossword clue. The Crossword Solver finds answers to classic crosswords and cryptic crossword puzzles. Enter the length or pattern for better results. Click the answer to find similar crossword clues .\\nAccording to bet365, Djokovic has even odds of winning the title at Melbourne Park -- meaning that the 35-year-old has a 50% chance of being the winner of the 2023 Australian Open men's singles ...\\nWe found 40 solutions for Tennis player Sabalenka, winner of the 2023 Australian Open. The top solutions are determined by popularity, ratings and frequency of searches. The most likely answer for the clue is ARYNA. How many solutions does Tennis player Sabalenka, winner of the 2023 Australian Open have?"`
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-54) },
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-55) result: ''
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-56)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-57){
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-58) tool: {
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-59)  results: {
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-60)   '#E1': `"A one-set shoot-off to decide the winner of the 2023 Australian Open. There could not have been a better script. SECOND SET (* denotes server) Sabalenka* 6-3 Rybakina - Wide second serve into the deuce court from Sabalenka and forehand return from Rybakina is long. Deep backhand crosscourt return from Rybakina draws a shot ball from Sabalenka ...\\nThe Crossword Solver found 30 answers to \\"Tennis player Sabalenka, winner of the 2023 Australian Open\\", 5 letters crossword clue. The Crossword Solver finds answers to classic crosswords and cryptic crossword puzzles. Enter the length or pattern for better results. Click the answer to find similar crossword clues .\\nAccording to bet365, Djokovic has even odds of winning the title at Melbourne Park -- meaning that the 35-year-old has a 50% chance of being the winner of the 2023 Australian Open men's singles ...\\nWe found 40 solutions for Tennis player Sabalenka, winner of the 2023 Australian Open. The top solutions are determined by popularity, ratings and frequency of searches. The most likely answer for the clue is ARYNA. How many solutions does Tennis player Sabalenka, winner of the 2023 Australian Open have?"`
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-61)  }
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-62) }
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-63)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-64)-----
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-65)---SOLVE---
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-66){ solve: { result: 'Belgrade, Serbia' } }
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-13-67)-----

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-14-1)constsnapshot=awaitapp.getState(threadConfig);
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-14-2)console.log(snapshot.values.result);

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-15-1)Belgrade, Serbia

```


> #### See the LangSmith trace [here](https://smith.langchain.com/public/730ea730-d896-450e-ac85-3c7e228c79f4/r)[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#see-the-langsmith-trace-here "Permanent link")

## Conclusion[¶](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#conclusion "Permanent link")

Congratulations on implementing ReWOO! Before you leave, I'll leave you with a couple limitations of the current implementation from the paper:

  1. If little context of the environment is available, the planner will be ineffective in its tool use. This can typically be ameliorated through few-shot prompting and/or fine-tuning.
  2. The tasks are still executed in sequence, meaning the total execution time is impacted by _every_ tool call, not just the longest-running in a given step.



```
[](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__codelineno-16-1)

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  Reflection  ](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/) [ Next  Chat Bot Evaluation as Multi-agent Simulation  ](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
