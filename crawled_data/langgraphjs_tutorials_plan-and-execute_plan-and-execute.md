---
url: https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#plan-and-execute)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

Plan-and-Execute 

[ ](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/?q= "Share")

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
          * Planning Agents  Planning Agents 
            * [ Planning Agents  ](https://langchain-ai.github.io/langgraphjs/tutorials#planning-agents)
            * Plan-and-Execute  [ Plan-and-Execute  ](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#setup)
              * [ Define the State  ](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#define-the-state)
              * [ Define Tools  ](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#define-tools)
              * [ Define our Execution Agent  ](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#define-our-execution-agent)
              * [ Planning Step  ](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#planning-step)
              * [ Re-Plan Step  ](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#re-plan-step)
              * [ Create the Graph  ](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#create-the-graph)
                * [ See the LangSmith trace here.  ](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#see-the-langsmith-trace-here)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#setup)
  * [ Define the State  ](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#define-the-state)
  * [ Define Tools  ](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#define-tools)
  * [ Define our Execution Agent  ](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#define-our-execution-agent)
  * [ Planning Step  ](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#planning-step)
  * [ Re-Plan Step  ](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#re-plan-step)
  * [ Create the Graph  ](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#create-the-graph)
    * [ See the LangSmith trace here.  ](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#see-the-langsmith-trace-here)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ Tutorials  ](https://langchain-ai.github.io/langgraphjs/tutorials/)
  4. [ Agent Architectures  ](https://langchain-ai.github.io/langgraphjs/tutorials#agent-architectures)
  5. [ Planning Agents  ](https://langchain-ai.github.io/langgraphjs/tutorials#planning-agents)



# Plan-and-Execute[¶](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#plan-and-execute "Permanent link")

This notebook shows how to create a "plan-and-execute" style agent. This is heavily inspired by the [Plan-and-Solve](https://arxiv.org/abs/2305.04091) paper as well as the [Baby-AGI](https://github.com/yoheinakajima/babyagi) project.

The core idea is to first come up with a multi-step plan, and then go through that plan one item at a time. After accomplishing a particular task, you can then revisit the plan and modify as appropriate.

This compares to a typical [ReAct](https://arxiv.org/abs/2210.03629) style agent where you think one step at a time. The advantages of this "plan-and-execute" style agent are:

  1. Explicit long term planning (which even really strong LLMs can struggle with)
  2. Ability to use smaller/weaker models for the execution step, only using larger/better models for the planning step



## Setup[¶](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#setup "Permanent link")

First, we need to install the packages required.

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-0-1)npminstall@langchain/langgraph@langchain/openailangchain@langchain/core

```


Next, we need to set API keys for OpenAI (the LLM we will use) and Tavily (the search tool we will use)

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-1-1)// process.env.OPENAI_API_KEY = "YOUR_API_KEY"
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-1-2)// process.env.TAVILY_API_KEY = "YOUR_API_KEY"

```


Optionally, we can set API key for LangSmith tracing, which will give us best-in-class observability.

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-2-1)// process.env.LANGCHAIN_TRACING_V2 = "true"
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-2-2)// process.env.LANGCHAIN_API_KEY = "YOUR_API_KEY"
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-2-3)// process.env.LANGCHAIN_PROJECT = "YOUR_PROJECT_NAME"

```


## Define the State[¶](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#define-the-state "Permanent link")

Let's start by defining the state to track for this agent.

First, we will need to track the current plan. Let's represent that as a list of strings.

Next, we should track previously executed steps. Let's represent that as a list of tuples (these tuples will contain the step and then the result)

Finally, we need to have some state to represent the final response as well as the original input.

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-3-1)import{Annotation}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-3-2)
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-3-3)constPlanExecuteState=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-3-4)input:Annotation<string>({
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-3-5)reducer:(x,y)=>y??x??"",
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-3-6)}),
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-3-7)plan:Annotation<string[]>({
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-3-8)reducer:(x,y)=>y??x??[],
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-3-9)}),
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-3-10)pastSteps:Annotation<[string,string][]>({
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-3-11)reducer:(x,y)=>x.concat(y),
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-3-12)}),
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-3-13)response:Annotation<string>({
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-3-14)reducer:(x,y)=>y??x,
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-3-15)}),
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-3-16)})

```


## Define Tools[¶](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#define-tools "Permanent link")

We will first define the tools we want to use. For this simple example, we will use a built-in search tool via Tavily. However, it is really easy to create your own tools - see documentation [here](https://js.langchain.com/docs/modules/agents/tools/dynamic) on how to do that.

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-4-1)import{TavilySearchResults}from"@langchain/community/tools/tavily_search";
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-4-2)
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-4-3)consttools=[newTavilySearchResults({maxResults:3})];

```


## Define our Execution Agent[¶](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#define-our-execution-agent "Permanent link")

Now we will create the execution agent we want to use to execute tasks. Note that for this example, we will be using the same execution agent for each task, but this doesn't HAVE to be the case.

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-5-1)import{ChatOpenAI}from"@langchain/openai";
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-5-2)import{createReactAgent}from"@langchain/langgraph/prebuilt";
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-5-3)
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-5-4)constagentExecutor=createReactAgent({
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-5-5)llm:newChatOpenAI({model:"gpt-4o"}),
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-5-6)tools:tools,
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-5-7)});

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-6-1)import{HumanMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-6-2)
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-6-3)awaitagentExecutor.invoke({
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-6-4)messages:[newHumanMessage("who is the winner of the us open")],
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-6-5)});

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-1){
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-2) messages: [
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-3)  HumanMessage {
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-4)   "content": "who is the winner of the us open",
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-5)   "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-6)   "response_metadata": {}
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-7)  },
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-8)  AIMessage {
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-9)   "content": "",
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-10)   "additional_kwargs": {
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-11)    "tool_calls": [
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-12)     {
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-13)      "id": "call_c2N7Z1RX31qKJaSlpOJ0K7Wm",
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-14)      "type": "function",
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-15)      "function": "[Object]"
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-16)     }
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-17)    ]
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-18)   },
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-19)   "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-20)    "tokenUsage": {
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-21)     "completionTokens": 25,
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-22)     "promptTokens": 80,
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-23)     "totalTokens": 105
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-24)    },
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-25)    "finish_reason": "tool_calls"
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-26)   },
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-27)   "tool_calls": [
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-28)    {
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-29)     "name": "tavily_search_results_json",
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-30)     "args": {
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-31)      "input": "winner of the US Open 2023"
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-32)     },
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-33)     "type": "tool_call",
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-34)     "id": "call_c2N7Z1RX31qKJaSlpOJ0K7Wm"
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-35)    }
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-36)   ],
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-37)   "invalid_tool_calls": []
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-38)  },
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-39)  ToolMessage {
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-40)   "content": "[{\"title\":\"How Wyndham Clark won the 2023 U.S. Open over Rory McIlroy, Scottie ...\",\"url\":\"https://www.nytimes.com/athletic/live-blogs/us-open-leaderboard-live-scores-results-tee-times/mhPUFgLsyFfM/\",\"content\":\"Wyndham Clark is your 2023 U.S. Open champion. Wyndham Clark has won his first major championship, besting some of the best players in the world on Sunday at Los Angeles Country Club to claim the ...\",\"score\":0.9981324,\"raw_content\":null},{\"title\":\"Championship Point | Coco Gauff Wins Women's Singles Title | 2023 US Open\",\"url\":\"https://www.youtube.com/watch?v=rZ0XQWWFIAo\",\"content\":\"The moment Coco Gauff beat Aryna Sabalenka in the final of the 2023 US Open.Don't miss a moment of the US Open! Subscribe now: https://bit.ly/2Pdr81iThe 2023...\",\"score\":0.997459,\"raw_content\":null},{\"title\":\"2023 U.S. Open leaderboard: Wyndham Clark breaks through edging Rory ...\",\"url\":\"https://www.cbssports.com/golf/news/2023-u-s-open-leaderboard-wyndham-clark-breaks-through-edging-rory-mcilroy-for-first-major-championship/live/\",\"content\":\"College Pick'em\\nA Daily SportsLine Betting Podcast\\nNFL Playoff Time!\\n2023 U.S. Open leaderboard: Wyndham Clark breaks through edging Rory McIlroy for first major championship\\nClark beat one of the game's best clinching his second PGA Tour victory, both in the last six weeks\\nWith Rickie Fowler, Rory McIlroy and Scottie Scheffler atop the 2023 U.S. Open leaderboard, it appeared as if Los Angeles Country Club was set to crown a shining star as its national champion. After making birdie on No. 1 to momentarily pull even with the leaders, McIlroy was unable to take advantage of the short par-4 6th before leaving one on the table on the par-5 8th when his birdie putt from less than four feet failed to even touch the hole.\\n The shot on 14 was kind of the shot of the week for me -- to make a birdie there and grind it on the way in. The Champion Golfer of the Year now goes to defend the Claret Jug at Hoylake where he will relish the opportunity to put his creativity and imagination on display again.\\n Instead, the City of Angels saw a breakout performance from perhaps one of the game's rising stars as 29-year-old Wyndham Clark (-10) outlasted the veteran McIlroy (-9) to capture his first major championship and clinch his second professional victory.\\n\",\"score\":0.99586606,\"raw_content\":null}]",
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-41)   "name": "tavily_search_results_json",
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-42)   "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-43)   "response_metadata": {},
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-44)   "tool_call_id": "call_c2N7Z1RX31qKJaSlpOJ0K7Wm"
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-45)  },
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-46)  AIMessage {
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-47)   "content": "The winners of the 2023 US Open are:\n\n- **Men's Singles**: Wyndham Clark, who won his first major championship.\n- **Women's Singles**: Coco Gauff, who defeated Aryna Sabalenka in the final.",
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-48)   "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-49)   "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-50)    "tokenUsage": {
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-51)     "completionTokens": 50,
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-52)     "promptTokens": 717,
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-53)     "totalTokens": 767
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-54)    },
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-55)    "finish_reason": "stop"
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-56)   },
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-57)   "tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-58)   "invalid_tool_calls": []
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-59)  }
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-60) ]
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-61)}

```


## Planning Step[¶](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#planning-step "Permanent link")

Let's now think about creating the planning step. This will use function calling to create a plan.

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-8-1)import{z}from"zod";
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-8-2)import{zodToJsonSchema}from"zod-to-json-schema";
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-8-3)
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-8-4)constplan=zodToJsonSchema(
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-8-5)z.object({
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-8-6)steps:z
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-8-7).array(z.string())
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-8-8).describe("different steps to follow, should be in sorted order"),
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-8-9)}),
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-8-10));
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-8-11)constplanFunction={
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-8-12)name:"plan",
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-8-13)description:"This tool is used to plan the steps to follow",
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-8-14)parameters:plan,
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-8-15)};
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-8-16)
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-8-17)constplanTool={
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-8-18)type:"function",
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-8-19)function:planFunction,
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-8-20)};

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-9-1)import{ChatPromptTemplate}from"@langchain/core/prompts";
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-9-2)
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-9-3)constplannerPrompt=ChatPromptTemplate.fromTemplate(
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-9-4)`For the given objective, come up with a simple step by step plan. \
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-9-5)This plan should involve individual tasks, that if executed correctly will yield the correct answer. Do not add any superfluous steps. \
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-9-6)The result of the final step should be the final answer. Make sure that each step has all the information needed - do not skip steps.
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-9-7)
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-9-8){objective}`,
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-9-9));
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-9-10)
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-9-11)constmodel=newChatOpenAI({
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-9-12)modelName:"gpt-4-0125-preview",
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-9-13)}).withStructuredOutput(planFunction);
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-9-14)
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-9-15)constplanner=plannerPrompt.pipe(model);

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-10-1)awaitplanner.invoke({
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-10-2)objective:"what is the hometown of the current Australia open winner?",
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-10-3)});

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-11-1){
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-11-2) steps: [
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-11-3)  [32m"Identify the current Australia Open winner."[39m,
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-11-4)  [32m"Research the hometown of the identified Australia Open winner."[39m,
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-11-5)  [32m"Report the hometown of the Australia Open winner."[39m
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-11-6) ]
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-11-7)}

```


## Re-Plan Step[¶](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#re-plan-step "Permanent link")

Now, let's create a step that re-does the plan based on the result of the previous step.

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-1)import{JsonOutputToolsParser}from"@langchain/core/output_parsers/openai_tools";
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-2)
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-3)constresponse=zodToJsonSchema(
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-4)z.object({
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-5)response:z.string().describe("Response to user."),
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-6)}),
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-7));
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-8)
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-9)constresponseTool={
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-10)type:"function",
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-11)function:{
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-12)name:"response",
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-13)description:"Response to user.",
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-14)parameters:response,
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-15)},
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-16)};
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-17)
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-18)constreplannerPrompt=ChatPromptTemplate.fromTemplate(
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-19)`For the given objective, come up with a simple step by step plan. 
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-20)This plan should involve individual tasks, that if executed correctly will yield the correct answer. Do not add any superfluous steps.
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-21)The result of the final step should be the final answer. Make sure that each step has all the information needed - do not skip steps.
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-22)
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-23)Your objective was this:
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-24){input}
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-25)
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-26)Your original plan was this:
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-27){plan}
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-28)
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-29)You have currently done the follow steps:
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-30){pastSteps}
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-31)
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-32)Update your plan accordingly. If no more steps are needed and you can return to the user, then respond with that and use the 'response' function.
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-33)Otherwise, fill out the plan. 
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-34)Only add steps to the plan that still NEED to be done. Do not return previously done steps as part of the plan.`,
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-35));
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-36)
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-37)constparser=newJsonOutputToolsParser();
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-38)constreplanner=replannerPrompt
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-39).pipe(
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-40)newChatOpenAI({model:"gpt-4o"}).bindTools([
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-41)planTool,
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-42)responseTool,
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-43)]),
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-44))
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-45).pipe(parser);

```


## Create the Graph[¶](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#create-the-graph "Permanent link")

We can now create the graph!

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-1)import{END,START,StateGraph}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-2)import{RunnableConfig}from"@langchain/core/runnables";
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-3)
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-4)asyncfunctionexecuteStep(
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-5)state:typeofPlanExecuteState.State,
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-6)config?:RunnableConfig,
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-7)):Promise<Partial<typeofPlanExecuteState.State>>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-8)consttask=state.plan[0];
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-9)constinput={
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-10)messages:[newHumanMessage(task)],
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-11)};
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-12)const{messages}=awaitagentExecutor.invoke(input,config);
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-13)
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-14)return{
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-15)pastSteps:[[task,messages[messages.length-1].content.toString()]],
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-16)plan:state.plan.slice(1),
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-17)};
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-18)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-19)
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-20)asyncfunctionplanStep(
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-21)state:typeofPlanExecuteState.State,
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-22)):Promise<Partial<typeofPlanExecuteState.State>>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-23)constplan=awaitplanner.invoke({objective:state.input});
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-24)return{plan:plan.steps};
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-25)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-26)
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-27)asyncfunctionreplanStep(
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-28)state:typeofPlanExecuteState.State,
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-29)):Promise<Partial<typeofPlanExecuteState.State>>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-30)constoutput=awaitreplanner.invoke({
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-31)input:state.input,
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-32)plan:state.plan.join("\n"),
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-33)pastSteps:state.pastSteps
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-34).map(([step,result])=>`${step}: ${result}`)
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-35).join("\n"),
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-36)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-37)consttoolCall=output[0];
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-38)
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-39)if(toolCall.type=="response"){
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-40)return{response:toolCall.args?.response};
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-41)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-42)
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-43)return{plan:toolCall.args?.steps};
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-44)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-45)
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-46)functionshouldEnd(state:typeofPlanExecuteState.State){
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-47)returnstate.response?"true":"false";
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-48)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-49)
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-50)constworkflow=newStateGraph(PlanExecuteState)
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-51).addNode("planner",planStep)
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-52).addNode("agent",executeStep)
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-53).addNode("replan",replanStep)
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-54).addEdge(START,"planner")
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-55).addEdge("planner","agent")
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-56).addEdge("agent","replan")
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-57).addConditionalEdges("replan",shouldEnd,{
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-58)true:END,
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-59)false:"agent",
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-60)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-61)
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-62)// Finally, we compile it!
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-63)// This compiles it into a LangChain Runnable,
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-64)// meaning you can use it as you would any other runnable
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-65)constapp=workflow.compile();

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-14-1)constconfig={recursionLimit:50};
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-14-2)constinputs={
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-14-3)input:"what is the hometown of the 2024 Australian open winner?",
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-14-4)};
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-14-5)
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-14-6)forawait(consteventofawaitapp.stream(inputs,config)){
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-14-7)console.log(event);
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-14-8)}

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-15-1){
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-15-2) planner: {
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-15-3)  plan: [
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-15-4)   "Identify the winner of the 2024 Australian Open.",
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-15-5)   "Research the hometown of the identified winner."
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-15-6)  ]
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-15-7) }
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-15-8)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-15-9){
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-15-10) agent: {
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-15-11)  plan: [ "Research the hometown of the identified winner." ],
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-15-12)  pastSteps: [
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-15-13)   [
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-15-14)    "Identify the winner of the 2024 Australian Open.",
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-15-15)    "The winner of the 2024 Australian Open men's singles title is Jannik Sinner of Italy. He achieved a "... 175 more characters
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-15-16)   ]
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-15-17)  ]
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-15-18) }
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-15-19)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-15-20){ replan: { plan: [ "Research the hometown of Jannik Sinner." ] } }
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-15-21){
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-15-22) agent: {
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-15-23)  plan: [],
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-15-24)  pastSteps: [
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-15-25)   [
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-15-26)    "Research the hometown of Jannik Sinner.",
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-15-27)    "Jannik Sinner's hometown is Sexten (also known as Sesto) in northern Italy. Located in the Dolomites"... 126 more characters
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-15-28)   ]
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-15-29)  ]
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-15-30) }
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-15-31)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-15-32){
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-15-33) replan: {
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-15-34)  response: "The objective has been achieved. The hometown of the 2024 Australian Open winner, Jannik Sinner, is "... 47 more characters
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-15-35) }
[](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__codelineno-15-36)}

```


> #### See the LangSmith trace [here](https://smith.langchain.com/public/5bb4f582-d111-417d-ba91-29bcced272bb/r).[¶](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#see-the-langsmith-trace-here "Permanent link")

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  Hierarchical Agent Teams  ](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/hierarchical_agent_teams/) [ Next  Reflection  ](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
