---
url: https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#how-to-use-langgraph-platform-to-deploy-crewai-autogen-and-other-frameworks)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to use LangGraph Platform to deploy CrewAI, AutoGen, and other frameworks 

[ ](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/?q= "Share")

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

How-to Guides 
        * [ LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph)
        * LangGraph Platform  LangGraph Platform 
          * [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph-platform)
          * Application Structure  Application Structure 
            * [ Application Structure  ](https://langchain-ai.github.io/langgraph/how-tos#application-structure)
            * [ How to Set Up a LangGraph Application for Deployment  ](https://langchain-ai.github.io/langgraph/cloud/deployment/setup/)
            * [ How to Set Up a LangGraph Application for Deployment  ](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_pyproject/)
            * [ How to Set Up a LangGraph.js Application for Deployment  ](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_javascript/)
            * [ How to add semantic search to your LangGraph deployment  ](https://langchain-ai.github.io/langgraph/cloud/deployment/semantic_search/)
            * [ How to customize Dockerfile  ](https://langchain-ai.github.io/langgraph/cloud/deployment/custom_docker/)
            * [ How to test a LangGraph app locally  ](https://langchain-ai.github.io/langgraph/cloud/deployment/test_locally/)
            * [ Rebuild Graph at Runtime  ](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/)
            * How to use LangGraph Platform to deploy CrewAI, AutoGen, and other frameworks  [ How to use LangGraph Platform to deploy CrewAI, AutoGen, and other frameworks  ](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/) Table of contents 
              * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#setup)
              * [ Define autogen agent  ](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#define-autogen-agent)
              * [ Wrap in LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#wrap-in-langgraph)
              * [ Deploy with LangGraph Platform  ](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#deploy-with-langgraph-platform)
          * [ Deployment  ](https://langchain-ai.github.io/langgraph/how-tos#deployment)
          * [ Authentication & Access Control  ](https://langchain-ai.github.io/langgraph/how-tos#authentication-access-control)
          * [ Assistants  ](https://langchain-ai.github.io/langgraph/how-tos#assistants)
          * [ Threads  ](https://langchain-ai.github.io/langgraph/how-tos#threads)
          * [ Runs  ](https://langchain-ai.github.io/langgraph/how-tos#runs)
          * [ Streaming  ](https://langchain-ai.github.io/langgraph/how-tos#streaming_1)
          * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraph/how-tos#human-in-the-loop_1)
          * [ Double-texting  ](https://langchain-ai.github.io/langgraph/how-tos#double-texting)
          * [ Webhooks  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/webhooks/)
          * [ Cron Jobs  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/cron_jobs/)
          * [ LangGraph Studio  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph-studio)
      * [ Concepts  ](https://langchain-ai.github.io/langgraph/concepts/)
      * [ Tutorials  ](https://langchain-ai.github.io/langgraph/tutorials/)
    * Resources  Resources 
      * [ Prebuilt Agents  ](https://langchain-ai.github.io/langgraph/prebuilt/)
      * [ Adopters  ](https://langchain-ai.github.io/langgraph/adopters/)
      * [ FAQ  ](https://langchain-ai.github.io/langgraph/concepts/faq/)
      * [ Troubleshooting  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraph/reference/graphs/)



Table of contents 

  * [ Setup  ](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#setup)
  * [ Define autogen agent  ](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#define-autogen-agent)
  * [ Wrap in LangGraph  ](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#wrap-in-langgraph)
  * [ Deploy with LangGraph Platform  ](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#deploy-with-langgraph-platform)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph-platform)
  5. [ Application Structure  ](https://langchain-ai.github.io/langgraph/how-tos#application-structure)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/how-tos/autogen-langgraph-platform.ipynb "Edit this page")

# How to use LangGraph Platform to deploy CrewAI, AutoGen, and other frameworks[¶](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#how-to-use-langgraph-platform-to-deploy-crewai-autogen-and-other-frameworks "Permanent link")

[LangGraph Platform](https://langchain-ai.github.io/langgraph/concepts/langgraph_platform/) provides infrastructure for deploying agents. This integrates seamlessly with LangGraph, but can also work with other frameworks. The way to make this work is to wrap the agent in a single LangGraph node, and have that be the entire graph.

Doing so will allow you to deploy to LangGraph Platform, and allows you to get a lot of the [benefits](https://langchain-ai.github.io/langgraph/concepts/langgraph_platform/). You get horizontally scalable infrastructure, a task queue to handle bursty operations, a persistence layer to power short term memory, and long term memory support.

In this guide we show how to do this with an AutoGen agent, but this method should work for agents defined in other frameworks like CrewAI, LlamaIndex, and others as well.

## Setup[¶](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#setup "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__codelineno-0-1)%pip install autogen langgraph

```


```
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__codelineno-1-1)importgetpass
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__codelineno-1-2)importos
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__codelineno-1-5)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__codelineno-1-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__codelineno-1-7)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__codelineno-1-8)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__codelineno-1-10)_set_env("OPENAI_API_KEY")

```


## Define autogen agent[¶](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#define-autogen-agent "Permanent link")

Here we define our AutoGen agent. From <https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_web_info.ipynb>

```
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__codelineno-2-1)importautogen
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__codelineno-2-2)importos
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__codelineno-2-3)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__codelineno-2-4)config_list = [{"model": "gpt-4o", "api_key": os.environ["OPENAI_API_KEY"]}]
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__codelineno-2-5)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__codelineno-2-6)llm_config = {
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__codelineno-2-7)  "timeout": 600,
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__codelineno-2-8)  "cache_seed": 42,
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__codelineno-2-9)  "config_list": config_list,
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__codelineno-2-10)  "temperature": 0,
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__codelineno-2-11)}
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__codelineno-2-12)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__codelineno-2-13)autogen_agent = autogen.AssistantAgent(
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__codelineno-2-14)  name="assistant",
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__codelineno-2-15)  llm_config=llm_config,
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__codelineno-2-16))
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__codelineno-2-17)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__codelineno-2-18)user_proxy = autogen.UserProxyAgent(
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__codelineno-2-19)  name="user_proxy",
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__codelineno-2-20)  human_input_mode="NEVER",
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__codelineno-2-21)  max_consecutive_auto_reply=10,
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__codelineno-2-22)  is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__codelineno-2-23)  code_execution_config={
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__codelineno-2-24)    "work_dir": "web",
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__codelineno-2-25)    "use_docker": False,
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__codelineno-2-26)  }, # Please set use_docker=True if docker is available to run the generated code. Using docker is safer than running the generated code directly.
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__codelineno-2-27)  llm_config=llm_config,
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__codelineno-2-28)  system_message="Reply TERMINATE if the task has been solved at full satisfaction. Otherwise, reply CONTINUE, or the reason why the task is not solved yet.",
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__codelineno-2-29))

```


## Wrap in LangGraph[¶](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#wrap-in-langgraph "Permanent link")

We now wrap the AutoGen agent in a single LangGraph node, and make that the entire graph. The main thing this involves is defining an Input and Output schema for the node, which you would need to do if deploying this manually, so it's no extra work

```
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__codelineno-3-1)fromlanggraph.graphimport StateGraph, MessagesState
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__codelineno-3-2)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__codelineno-3-3)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__codelineno-3-4)defcall_autogen_agent(state: MessagesState):
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__codelineno-3-5)  last_message = state["messages"][-1]
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__codelineno-3-6)  response = user_proxy.initiate_chat(autogen_agent, message=last_message.content)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__codelineno-3-7)  # get the final response from the agent
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__codelineno-3-8)  content = response.chat_history[-1]["content"]
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__codelineno-3-9)  return {"messages": {"role": "assistant", "content": content}}
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__codelineno-3-10)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__codelineno-3-11)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__codelineno-3-12)graph = StateGraph(MessagesState)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__codelineno-3-13)graph.add_node(call_autogen_agent)
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__codelineno-3-14)graph.set_entry_point("call_autogen_agent")
[](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__codelineno-3-15)graph = graph.compile()

```


API Reference: [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph)

## Deploy with LangGraph Platform[¶](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#deploy-with-langgraph-platform "Permanent link")

You can now deploy this as you normally would with LangGraph Platform. See [these instructions](https://langchain-ai.github.io/langgraph/concepts/deployment_options/) for more details.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Rebuild Graph at Runtime  ](https://langchain-ai.github.io/langgraph/cloud/deployment/graph_rebuild/) [ Next  How to Deploy to LangGraph Cloud  ](https://langchain-ai.github.io/langgraph/cloud/deployment/cloud/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
