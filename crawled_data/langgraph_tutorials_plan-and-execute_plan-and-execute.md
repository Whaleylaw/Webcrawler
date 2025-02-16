---
url: https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#plan-and-execute)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Plan-and-Execute 

[ ](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/?q= "Share")

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
          * [ Multi-Agent Systems  ](https://langchain-ai.github.io/langgraph/tutorials#multi-agent-systems)
          * Planning Agents  Planning Agents 
            * [ Planning Agents  ](https://langchain-ai.github.io/langgraph/tutorials#planning-agents)
            * Plan-and-Execute  [ Plan-and-Execute  ](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#setup)
              * [ Define Tools  ](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#define-tools)
              * [ Define our Execution Agent  ](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#define-our-execution-agent)
              * [ Define the State  ](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#define-the-state)
              * [ Planning Step  ](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#planning-step)
              * [ Re-Plan Step  ](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#re-plan-step)
              * [ Create the Graph  ](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#create-the-graph)
              * [ Conclusion  ](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#conclusion)
            * [ Reasoning without Observation  ](https://langchain-ai.github.io/langgraph/tutorials/rewoo/rewoo/)
            * [ LLMCompiler  ](https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#setup)
  * [ Define Tools  ](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#define-tools)
  * [ Define our Execution Agent  ](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#define-our-execution-agent)
  * [ Define the State  ](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#define-the-state)
  * [ Planning Step  ](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#planning-step)
  * [ Re-Plan Step  ](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#re-plan-step)
  * [ Create the Graph  ](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#create-the-graph)
  * [ Conclusion  ](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#conclusion)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ Tutorials  ](https://langchain-ai.github.io/langgraph/tutorials/)
  4. [ Agent Architectures  ](https://langchain-ai.github.io/langgraph/tutorials#agent-architectures)
  5. [ Planning Agents  ](https://langchain-ai.github.io/langgraph/tutorials#planning-agents)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/tutorials/plan-and-execute/plan-and-execute.ipynb "Edit this page")

# Plan-and-Execute[¶](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#plan-and-execute "Permanent link")

This notebook shows how to create a "plan-and-execute" style agent. This is heavily inspired by the [Plan-and-Solve](https://arxiv.org/abs/2305.04091) paper as well as the [Baby-AGI](https://github.com/yoheinakajima/babyagi) project.

The core idea is to first come up with a multi-step plan, and then go through that plan one item at a time. After accomplishing a particular task, you can then revisit the plan and modify as appropriate.

The general computational graph looks like the following:

![plan-and-execute diagram]()

This compares to a typical [ReAct](https://arxiv.org/abs/2210.03629) style agent where you think one step at a time. The advantages of this "plan-and-execute" style agent are:

  1. Explicit long term planning (which even really strong LLMs can struggle with)
  2. Ability to use smaller/weaker models for the execution step, only using larger/better models for the planning step



The following walkthrough demonstrates how to do so in LangGraph. The resulting agent will leave a trace like the following example: ([link](https://smith.langchain.com/public/d46e24d3-dda6-44d5-9550-b618fca4e0d4/r)).

## Setup[¶](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#setup "Permanent link")

First, we need to install the packages required.

```
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-0-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-0-2)%pip install --quiet -U langgraph langchain-community langchain-openai tavily-python

```


Next, we need to set API keys for OpenAI (the LLM we will use) and Tavily (the search tool we will use)

```
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-1-1)importgetpass
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-1-2)importos
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-1-5)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-1-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-1-7)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-1-8)
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-1-10)_set_env("OPENAI_API_KEY")
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-1-11)_set_env("TAVILY_API_KEY")

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Define Tools[¶](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#define-tools "Permanent link")

We will first define the tools we want to use. For this simple example, we will use a built-in search tool via Tavily. However, it is really easy to create your own tools - see documentation [here](https://python.langchain.com/docs/how_to/custom_tools) on how to do that.

```
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-2-1)fromlangchain_community.tools.tavily_searchimport TavilySearchResults
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-2-2)
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-2-3)tools = [TavilySearchResults(max_results=3)]

```


API Reference: [TavilySearchResults](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.tavily_search.tool.TavilySearchResults.html)

## Define our Execution Agent[¶](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#define-our-execution-agent "Permanent link")

Now we will create the execution agent we want to use to execute tasks. Note that for this example, we will be using the same execution agent for each task, but this doesn't HAVE to be the case.

```
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-3-1)fromlangchainimport hub
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-3-2)fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-3-3)
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-3-4)fromlanggraph.prebuiltimport create_react_agent
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-3-5)
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-3-6)# Choose the LLM that will drive the agent
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-3-7)llm = ChatOpenAI(model="gpt-4-turbo-preview")
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-3-8)prompt = "You are a helpful assistant."
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-3-9)agent_executor = create_react_agent(llm, tools, prompt=prompt)

```


API Reference: [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html) | [create_react_agent](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent)

```
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-4-1)agent_executor.invoke({"messages": [("user", "who is the winnner of the us open")]})

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-5-1){'messages': [HumanMessage(content='who is the winnner of the us open', additional_kwargs={}, response_metadata={}, id='388a14b3-f556-4f91-ad36-def0a075638e'),
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-5-2) AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_5nbeRa0fgh4ZslRkjk75Kzxs', 'function': {'arguments': '{"query":"US Open 2023 winner"}', 'name': 'tavily_search_results_json'}, 'type': 'function'}], 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 23, 'prompt_tokens': 97, 'total_tokens': 120, 'completion_tokens_details': {'reasoning_tokens': 0}}, 'model_name': 'gpt-4-0125-preview', 'system_fingerprint': None, 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-3bb25f7a-49e5-43b7-ad53-718bd0107db1-0', tool_calls=[{'name': 'tavily_search_results_json', 'args': {'query': 'US Open 2023 winner'}, 'id': 'call_5nbeRa0fgh4ZslRkjk75Kzxs', 'type': 'tool_call'}], usage_metadata={'input_tokens': 97, 'output_tokens': 23, 'total_tokens': 120}),
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-5-3) ToolMessage(content='[{"url": "https://www.youtube.com/watch?v=rZ0XQWWFIAo", "content": "The moment Coco Gauff beat Aryna Sabalenka in the final of the 2023 US Open.Don\'t miss a moment of the US Open! Subscribe now: https://bit.ly/2Pdr81iThe 2023..."}, {"url": "https://www.cbssports.com/tennis/news/us-open-2023-scores-novak-djokovic-makes-history-with-24th-grand-slam-title-while-coco-gauff-earns-her-first/", "content": "Here is all you need to know about the 2023 US Open:\\nMen\'s final\\nWomen\'s final\\nMen\'s singles seeds\\nWomen\'s singles seeds\\nOur Latest Tennis Stories\\nUS Open 2023: Schedule, scores, how to watch, seeds\\nRafael Nadal to return next month at Brisbane\\nNovak Djokovic breaks Federer\'s ATP Finals record\\nTennis bettor wins $486,000 off $28 on 10-match parlay\\nTennis player DQ\'d on match point for hitting umpire\\nRafael Nadal says Novak Djokovic is tennis\' GOAT\\nHalep suspended four years for anti-doping violations\\nDjokovic pays tribute to Kobe after winning US Open\\nDjokovic vs. Medvedev odds, US Open final picks, bets\\nAryna Sabalenka-Coco Gauff odds, US Open final picks\\n© 2004-2023 CBS Interactive. Novak Djokovic makes history with 24th Grand Slam title, while Coco Gauff earns her first\\nThe 2023 US Open is officially in the books\\nThe 2023 US open came to a close as Coco Gauff earned her first major title and Novak Djokovic made history with his 24th Grand Slam trophy. Gauff is the first woman to win the Cincinnati Masters 1000 and US Open in the same year since Williams in 2014.\\n Gauff landed in New York as the No. 6 player in the world but will be climbing to a career-best No. 3 when the next rankings get released.\\n He arrived to this competition as the world No. 2 but will improve to No. 1 in the next rankings, extending his record total of 389 weeks at the top.\\n"}, {"url": "https://www.usopen.org/en_US/news/articles/2023-09-10/novak_djokovic_wins_24th_grand_slam_singles_title_at_2023_us_open.html", "content": "Novak Djokovic defeated Daniil Medvedev in three sets to claim his 24th Grand Slam singles title and match Margaret Court\'s all-time record. The Serb saved a set point in the second set and attacked the net to win his fourth US Open crown."}]', name='tavily_search_results_json', id='3ea00623-86b3-4d6f-9978-3503a7eecf0f', tool_call_id='call_5nbeRa0fgh4ZslRkjk75Kzxs', artifact={'query': 'US Open 2023 winner', 'follow_up_questions': None, 'answer': None, 'images': [], 'results': [{'title': "Championship Point | Coco Gauff Wins Women's Singles Title | 2023 US Open", 'url': 'https://www.youtube.com/watch?v=rZ0XQWWFIAo', 'content': "The moment Coco Gauff beat Aryna Sabalenka in the final of the 2023 US Open.Don't miss a moment of the US Open! Subscribe now: https://bit.ly/2Pdr81iThe 2023...", 'score': 0.9975177, 'raw_content': None}, {'title': 'US Open 2023 scores: Novak Djokovic makes history with 24th Grand Slam ...', 'url': 'https://www.cbssports.com/tennis/news/us-open-2023-scores-novak-djokovic-makes-history-with-24th-grand-slam-title-while-coco-gauff-earns-her-first/', 'content': "Here is all you need to know about the 2023 US Open:\nMen's final\nWomen's final\nMen's singles seeds\nWomen's singles seeds\nOur Latest Tennis Stories\nUS Open 2023: Schedule, scores, how to watch, seeds\nRafael Nadal to return next month at Brisbane\nNovak Djokovic breaks Federer's ATP Finals record\nTennis bettor wins $486,000 off $28 on 10-match parlay\nTennis player DQ'd on match point for hitting umpire\nRafael Nadal says Novak Djokovic is tennis' GOAT\nHalep suspended four years for anti-doping violations\nDjokovic pays tribute to Kobe after winning US Open\nDjokovic vs. Medvedev odds, US Open final picks, bets\nAryna Sabalenka-Coco Gauff odds, US Open final picks\n© 2004-2023 CBS Interactive. Novak Djokovic makes history with 24th Grand Slam title, while Coco Gauff earns her first\nThe 2023 US Open is officially in the books\nThe 2023 US open came to a close as Coco Gauff earned her first major title and Novak Djokovic made history with his 24th Grand Slam trophy. Gauff is the first woman to win the Cincinnati Masters 1000 and US Open in the same year since Williams in 2014.\n Gauff landed in New York as the No. 6 player in the world but will be climbing to a career-best No. 3 when the next rankings get released.\n He arrived to this competition as the world No. 2 but will improve to No. 1 in the next rankings, extending his record total of 389 weeks at the top.\n", 'score': 0.9937101, 'raw_content': None}, {'title': 'Novak Djokovic wins 24th Grand Slam singles title at 2023 US Open', 'url': 'https://www.usopen.org/en_US/news/articles/2023-09-10/novak_djokovic_wins_24th_grand_slam_singles_title_at_2023_us_open.html', 'content': "Novak Djokovic defeated Daniil Medvedev in three sets to claim his 24th Grand Slam singles title and match Margaret Court's all-time record. The Serb saved a set point in the second set and attacked the net to win his fourth US Open crown.", 'score': 0.8146434, 'raw_content': None}], 'response_time': 2.24}),
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-5-4) AIMessage(content="The winners of the 2023 US Open are Coco Gauff and Novak Djokovic. Coco Gauff won her first major title at the US Open, making history, while Novak Djokovic secured his 24th Grand Slam title, matching Margaret Court's all-time record and winning his fourth US Open crown. Coco Gauff defeated Aryna Sabalenka in the final, and Novak Djokovic defeated Daniil Medvedev.", additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 93, 'prompt_tokens': 751, 'total_tokens': 844, 'completion_tokens_details': {'reasoning_tokens': 0}}, 'model_name': 'gpt-4-0125-preview', 'system_fingerprint': None, 'finish_reason': 'stop', 'logprobs': None}, id='run-eedb1782-6120-441d-ab5d-ccf6bef75b02-0', usage_metadata={'input_tokens': 751, 'output_tokens': 93, 'total_tokens': 844})]}

```


## Define the State[¶](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#define-the-state "Permanent link")

Let's now start by defining the state the track for this agent.

First, we will need to track the current plan. Let's represent that as a list of strings.

Next, we should track previously executed steps. Let's represent that as a list of tuples (these tuples will contain the step and then the result)

Finally, we need to have some state to represent the final response as well as the original input.

```
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-6-1)importoperator
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-6-2)fromtypingimport Annotated, List, Tuple
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-6-3)fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-6-4)
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-6-5)
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-6-6)classPlanExecute(TypedDict):
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-6-7)  input: str
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-6-8)  plan: List[str]
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-6-9)  past_steps: Annotated[List[Tuple], operator.add]
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-6-10)  response: str

```


## Planning Step[¶](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#planning-step "Permanent link")

Let's now think about creating the planning step. This will use function calling to create a plan.

Using Pydantic with LangChain

This notebook uses Pydantic v2 `BaseModel`, which requires `langchain-core >= 0.3`. Using `langchain-core < 0.3` will result in errors due to mixing of Pydantic v1 and v2 `BaseModels`. 

```
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-1)frompydanticimport BaseModel, Field
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-2)
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-3)
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-4)classPlan(BaseModel):
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-5)"""Plan to follow in future"""
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-6)
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-7)  steps: List[str] = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-8)    description="different steps to follow, should be in sorted order"
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-7-9)  )

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-8-1)fromlangchain_core.promptsimport ChatPromptTemplate
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-8-2)
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-8-3)planner_prompt = ChatPromptTemplate.from_messages(
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-8-4)  [
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-8-5)    (
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-8-6)      "system",
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-8-7)"""For the given objective, come up with a simple step by step plan. \
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-8-8)This plan should involve individual tasks, that if executed correctly will yield the correct answer. Do not add any superfluous steps. \
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-8-9)The result of the final step should be the final answer. Make sure that each step has all the information needed - do not skip steps.""",
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-8-10)    ),
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-8-11)    ("placeholder", "{messages}"),
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-8-12)  ]
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-8-13))
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-8-14)planner = planner_prompt | ChatOpenAI(
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-8-15)  model="gpt-4o", temperature=0
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-8-16)).with_structured_output(Plan)

```


API Reference: [ChatPromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html)

```
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-9-1)planner.invoke(
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-9-2)  {
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-9-3)    "messages": [
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-9-4)      ("user", "what is the hometown of the current Australia open winner?")
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-9-5)    ]
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-9-6)  }
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-9-7))

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-10-1)Plan(steps=['Identify the current winner of the Australia Open.', 'Find the hometown of the identified winner.'])

```


## Re-Plan Step[¶](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#re-plan-step "Permanent link")

Now, let's create a step that re-does the plan based on the result of the previous step.

```
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-11-1)fromtypingimport Union
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-11-2)
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-11-3)
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-11-4)classResponse(BaseModel):
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-11-5)"""Response to user."""
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-11-6)
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-11-7)  response: str
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-11-8)
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-11-9)
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-11-10)classAct(BaseModel):
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-11-11)"""Action to perform."""
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-11-12)
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-11-13)  action: Union[Response, Plan] = Field(
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-11-14)    description="Action to perform. If you want to respond to user, use Response. "
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-11-15)    "If you need to further use tools to get the answer, use Plan."
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-11-16)  )
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-11-17)
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-11-18)
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-11-19)replanner_prompt = ChatPromptTemplate.from_template(
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-11-20)"""For the given objective, come up with a simple step by step plan. \
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-11-21)This plan should involve individual tasks, that if executed correctly will yield the correct answer. Do not add any superfluous steps. \
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-11-22)The result of the final step should be the final answer. Make sure that each step has all the information needed - do not skip steps.
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-11-23)
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-11-24)Your objective was this:
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-11-25){input}
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-11-26)
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-11-27)Your original plan was this:
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-11-28){plan}
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-11-29)
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-11-30)You have currently done the follow steps:
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-11-31){past_steps}
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-11-32)
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-11-33)Update your plan accordingly. If no more steps are needed and you can return to the user, then respond with that. Otherwise, fill out the plan. Only add steps to the plan that still NEED to be done. Do not return previously done steps as part of the plan."""
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-11-34))
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-11-35)
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-11-36)
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-11-37)replanner = replanner_prompt | ChatOpenAI(
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-11-38)  model="gpt-4o", temperature=0
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-11-39)).with_structured_output(Act)

```


## Create the Graph[¶](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#create-the-graph "Permanent link")

We can now create the graph!

```
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-1)fromtypingimport Literal
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-2)fromlanggraph.graphimport END
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-3)
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-4)
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-5)async defexecute_step(state: PlanExecute):
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-6)  plan = state["plan"]
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-7)  plan_str = "\n".join(f"{i+1}. {step}" for i, step in enumerate(plan))
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-8)  task = plan[0]
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-9)  task_formatted = f"""For the following plan:
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-10){plan_str}\n\nYou are tasked with executing step {1}, {task}."""
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-11)  agent_response = await agent_executor.ainvoke(
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-12)    {"messages": [("user", task_formatted)]}
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-13)  )
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-14)  return {
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-15)    "past_steps": [(task, agent_response["messages"][-1].content)],
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-16)  }
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-17)
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-18)
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-19)async defplan_step(state: PlanExecute):
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-20)  plan = await planner.ainvoke({"messages": [("user", state["input"])]})
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-21)  return {"plan": plan.steps}
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-22)
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-23)
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-24)async defreplan_step(state: PlanExecute):
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-25)  output = await replanner.ainvoke(state)
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-26)  if isinstance(output.action, Response):
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-27)    return {"response": output.action.response}
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-28)  else:
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-29)    return {"plan": output.action.steps}
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-30)
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-31)
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-32)defshould_end(state: PlanExecute):
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-33)  if "response" in state and state["response"]:
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-34)    return END
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-35)  else:
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-12-36)    return "agent"

```


API Reference: [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END)

```
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-1)fromlanggraph.graphimport StateGraph, START
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-2)
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-3)workflow = StateGraph(PlanExecute)
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-4)
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-5)# Add the plan node
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-6)workflow.add_node("planner", plan_step)
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-7)
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-8)# Add the execution step
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-9)workflow.add_node("agent", execute_step)
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-10)
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-11)# Add a replan node
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-12)workflow.add_node("replan", replan_step)
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-13)
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-14)workflow.add_edge(START, "planner")
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-15)
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-16)# From plan we go to agent
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-17)workflow.add_edge("planner", "agent")
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-18)
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-19)# From agent, we replan
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-20)workflow.add_edge("agent", "replan")
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-21)
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-22)workflow.add_conditional_edges(
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-23)  "replan",
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-24)  # Next, we pass in the function that will determine which node is called next.
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-25)  should_end,
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-26)  ["agent", END],
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-27))
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-28)
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-29)# Finally, we compile it!
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-30)# This compiles it into a LangChain Runnable,
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-31)# meaning you can use it as you would any other runnable
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-13-32)app = workflow.compile()

```


API Reference: [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START)

```
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-14-1)fromIPython.displayimport Image, display
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-14-2)
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-14-3)display(Image(app.get_graph(xray=True).draw_mermaid_png()))

```


![]()

```
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-15-1)config = {"recursion_limit": 50}
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-15-2)inputs = {"input": "what is the hometown of the mens 2024 Australia open winner?"}
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-15-3)async for event in app.astream(inputs, config=config):
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-15-4)  for k, v in event.items():
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-15-5)    if k != "__end__":
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-15-6)      print(v)

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-16-1){'plan': ["Identify the winner of the men's 2024 Australian Open.", 'Research the hometown of the identified winner.']}
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-16-2){'past_steps': [("Identify the winner of the men's 2024 Australian Open.", "The winner of the men's singles tennis title at the 2024 Australian Open was Jannik Sinner. He defeated Daniil Medvedev in the final with scores of 3-6, 3-6, 6-4, 6-4, 6-3 to win his first major singles title.")]}
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-16-3){'plan': ['Research the hometown of Jannik Sinner.']}
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-16-4){'past_steps': [('Research the hometown of Jannik Sinner.', "Jannik Sinner's hometown is Sexten, which is located in northern Italy.")]}
[](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__codelineno-16-5){'response': "The hometown of the men's 2024 Australian Open winner, Jannik Sinner, is Sexten, located in northern Italy."}

```


## Conclusion[¶](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#conclusion "Permanent link")

Congrats on making a plan-and-execute agent! One known limitations of the above design is that each task is still executed in sequence, meaning embarrassingly parallel operations all add to the total execution time. You could improve on this by having each task represented as a DAG (similar to LLMCompiler), rather than a regular list.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Hierarchical Agent Teams  ](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/hierarchical_agent_teams/) [ Next  Reasoning without Observation  ](https://langchain-ai.github.io/langgraph/tutorials/rewoo/rewoo/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
