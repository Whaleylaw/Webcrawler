---
url: https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#prompt-generation-from-user-requirements)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Prompt Generation from User Requirements 

[ ](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/?q= "Share")

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
        * Chatbots  Chatbots 
          * [ Chatbots  ](https://langchain-ai.github.io/langgraph/tutorials#chatbots)
          * [ Build a Customer Support Bot  ](https://langchain-ai.github.io/langgraph/tutorials/customer-support/customer-support/)
          * Prompt Generation from User Requirements  [ Prompt Generation from User Requirements  ](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/) Table of contents 
            * [ Setup  ](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#setup)
            * [ Gather information  ](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#gather-information)
            * [ Generate Prompt  ](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#generate-prompt)
            * [ Define the state logic  ](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#define-the-state-logic)
            * [ Create the graph  ](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#create-the-graph)
            * [ Use the graph  ](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#use-the-graph)
          * [ Code generation with RAG and self-correction  ](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/)
        * [ RAG  ](https://langchain-ai.github.io/langgraph/tutorials#rag)
        * [ Agent Architectures  ](https://langchain-ai.github.io/langgraph/tutorials#agent-architectures)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#setup)
  * [ Gather information  ](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#gather-information)
  * [ Generate Prompt  ](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#generate-prompt)
  * [ Define the state logic  ](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#define-the-state-logic)
  * [ Create the graph  ](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#create-the-graph)
  * [ Use the graph  ](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#use-the-graph)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ Tutorials  ](https://langchain-ai.github.io/langgraph/tutorials/)
  4. [ Chatbots  ](https://langchain-ai.github.io/langgraph/tutorials#chatbots)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/tutorials/chatbots/information-gather-prompting.ipynb "Edit this page")

# Prompt Generation from User Requirements[¶](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#prompt-generation-from-user-requirements "Permanent link")

In this example we will create a chat bot that helps a user generate a prompt. It will first collect requirements from the user, and then will generate the prompt (and refine it based on user input). These are split into two separate states, and the LLM decides when to transition between them.

A graphical representation of the system can be found below.

![prompt-generator.png]()

## Setup[¶](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#setup "Permanent link")

First, let's install our required packages and set our OpenAI API key (the LLM we will use)

```
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-0-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-0-2)% pip install -U langgraph langchain_openai

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-1-1)importgetpass
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-1-2)importos
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-1-5)def_set_env(var: str):
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-1-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-1-7)    os.environ[var] = getpass.getpass(f"{var}: ")
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-1-8)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-1-10)_set_env("OPENAI_API_KEY")

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Gather information[¶](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#gather-information "Permanent link")

First, let's define the part of the graph that will gather user requirements. This will be an LLM call with a specific system message. It will have access to a tool that it can call when it is ready to generate the prompt.

Using Pydantic with LangChain

This notebook uses Pydantic v2 `BaseModel`, which requires `langchain-core >= 0.3`. Using `langchain-core < 0.3` will result in errors due to mixing of Pydantic v1 and v2 `BaseModels`. 

```
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-2-1)fromtypingimport List
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-2-2)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-2-3)fromlangchain_core.messagesimport SystemMessage
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-2-4)fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-2-5)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-2-6)frompydanticimport BaseModel

```


API Reference: [SystemMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.system.SystemMessage.html) | [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html)

```
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-3-1)template = """Your job is to get information from a user about what type of prompt template they want to create.
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-3-2)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-3-3)You should get the following information from them:
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-3-4)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-3-5)- What the objective of the prompt is
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-3-6)- What variables will be passed into the prompt template
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-3-7)- Any constraints for what the output should NOT do
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-3-8)- Any requirements that the output MUST adhere to
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-3-9)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-3-10)If you are not able to discern this info, ask them to clarify! Do not attempt to wildly guess.
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-3-11)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-3-12)After you are able to discern all the information, call the relevant tool."""
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-3-13)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-3-14)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-3-15)defget_messages_info(messages):
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-3-16)  return [SystemMessage(content=template)] + messages
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-3-17)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-3-18)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-3-19)classPromptInstructions(BaseModel):
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-3-20)"""Instructions on how to prompt the LLM."""
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-3-21)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-3-22)  objective: str
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-3-23)  variables: List[str]
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-3-24)  constraints: List[str]
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-3-25)  requirements: List[str]
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-3-26)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-3-27)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-3-28)llm = ChatOpenAI(temperature=0)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-3-29)llm_with_tool = llm.bind_tools([PromptInstructions])
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-3-30)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-3-31)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-3-32)definfo_chain(state):
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-3-33)  messages = get_messages_info(state["messages"])
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-3-34)  response = llm_with_tool.invoke(messages)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-3-35)  return {"messages": [response]}

```


## Generate Prompt[¶](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#generate-prompt "Permanent link")

We now set up the state that will generate the prompt. This will require a separate system message, as well as a function to filter out all message PRIOR to the tool invocation (as that is when the previous state decided it was time to generate the prompt

```
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-4-1)fromlangchain_core.messagesimport AIMessage, HumanMessage, ToolMessage
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-4-2)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-4-3)# New system prompt
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-4-4)prompt_system = """Based on the following requirements, write a good prompt template:
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-4-5)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-4-6){reqs}"""
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-4-7)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-4-8)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-4-9)# Function to get the messages for the prompt
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-4-10)# Will only get messages AFTER the tool call
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-4-11)defget_prompt_messages(messages: list):
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-4-12)  tool_call = None
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-4-13)  other_msgs = []
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-4-14)  for m in messages:
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-4-15)    if isinstance(m, AIMessage) and m.tool_calls:
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-4-16)      tool_call = m.tool_calls[0]["args"]
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-4-17)    elif isinstance(m, ToolMessage):
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-4-18)      continue
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-4-19)    elif tool_call is not None:
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-4-20)      other_msgs.append(m)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-4-21)  return [SystemMessage(content=prompt_system.format(reqs=tool_call))] + other_msgs
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-4-22)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-4-23)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-4-24)defprompt_gen_chain(state):
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-4-25)  messages = get_prompt_messages(state["messages"])
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-4-26)  response = llm.invoke(messages)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-4-27)  return {"messages": [response]}

```


API Reference: [AIMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.AIMessage.html) | [HumanMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.human.HumanMessage.html) | [ToolMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.tool.ToolMessage.html)

## Define the state logic[¶](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#define-the-state-logic "Permanent link")

This is the logic for what state the chatbot is in. If the last message is a tool call, then we are in the state where the "prompt creator" (`prompt`) should respond. Otherwise, if the last message is not a HumanMessage, then we know the human should respond next and so we are in the `END` state. If the last message is a HumanMessage, then if there was a tool call previously we are in the `prompt` state. Otherwise, we are in the "info gathering" (`info`) state.

```
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-5-1)fromtypingimport Literal
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-5-2)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-5-3)fromlanggraph.graphimport END
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-5-4)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-5-5)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-5-6)defget_state(state):
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-5-7)  messages = state["messages"]
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-5-8)  if isinstance(messages[-1], AIMessage) and messages[-1].tool_calls:
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-5-9)    return "add_tool_message"
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-5-10)  elif not isinstance(messages[-1], HumanMessage):
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-5-11)    return END
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-5-12)  return "info"

```


API Reference: [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END)

## Create the graph[¶](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#create-the-graph "Permanent link")

We can now the create the graph. We will use a SqliteSaver to persist conversation history.

```
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-6-1)fromlanggraph.checkpoint.memoryimport MemorySaver
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-6-2)fromlanggraph.graphimport StateGraph, START
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-6-3)fromlanggraph.graph.messageimport add_messages
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-6-4)fromtypingimport Annotated
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-6-5)fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-6-6)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-6-7)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-6-8)classState(TypedDict):
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-6-9)  messages: Annotated[list, add_messages]
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-6-10)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-6-11)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-6-12)memory = MemorySaver()
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-6-13)workflow = StateGraph(State)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-6-14)workflow.add_node("info", info_chain)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-6-15)workflow.add_node("prompt", prompt_gen_chain)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-6-16)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-6-17)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-6-18)@workflow.add_node
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-6-19)defadd_tool_message(state: State):
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-6-20)  return {
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-6-21)    "messages": [
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-6-22)      ToolMessage(
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-6-23)        content="Prompt generated!",
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-6-24)        tool_call_id=state["messages"][-1].tool_calls[0]["id"],
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-6-25)      )
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-6-26)    ]
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-6-27)  }
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-6-28)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-6-29)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-6-30)workflow.add_conditional_edges("info", get_state, ["add_tool_message", "info", END])
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-6-31)workflow.add_edge("add_tool_message", "prompt")
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-6-32)workflow.add_edge("prompt", END)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-6-33)workflow.add_edge(START, "info")
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-6-34)graph = workflow.compile(checkpointer=memory)

```


API Reference: [MemorySaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.MemorySaver) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [add_messages](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.message.add_messages)

```
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-7-1)fromIPython.displayimport Image, display
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-7-2)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-7-3)display(Image(graph.get_graph().draw_mermaid_png()))

```


![]()

## Use the graph[¶](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#use-the-graph "Permanent link")

We can now use the created chatbot.

```
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-8-1)importuuid
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-8-2)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-8-3)cached_human_responses = ["hi!", "rag prompt", "1 rag, 2 none, 3 no, 4 no", "red", "q"]
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-8-4)cached_response_index = 0
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-8-5)config = {"configurable": {"thread_id": str(uuid.uuid4())}}
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-8-6)while True:
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-8-7)  try:
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-8-8)    user = input("User (q/Q to quit): ")
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-8-9)  except:
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-8-10)    user = cached_human_responses[cached_response_index]
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-8-11)    cached_response_index += 1
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-8-12)  print(f"User (q/Q to quit): {user}")
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-8-13)  if user in {"q", "Q"}:
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-8-14)    print("AI: Byebye")
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-8-15)    break
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-8-16)  output = None
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-8-17)  for output in graph.stream(
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-8-18)    {"messages": [HumanMessage(content=user)]}, config=config, stream_mode="updates"
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-8-19)  ):
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-8-20)    last_message = next(iter(output.values()))["messages"][-1]
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-8-21)    last_message.pretty_print()
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-8-22)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-8-23)  if output and "prompt" in output:
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-8-24)    print("Done!")

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-9-1)User (q/Q to quit): hi!
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-9-2)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-9-3)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-9-4)Hello! How can I assist you today?
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-9-5)User (q/Q to quit): rag prompt
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-9-6)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-9-7)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-9-8)Sure! I can help you create a prompt template. To get started, could you please provide me with the following information:
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-9-9)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-9-10)1. What is the objective of the prompt?
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-9-11)2. What variables will be passed into the prompt template?
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-9-12)3. Any constraints for what the output should NOT do?
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-9-13)4. Any requirements that the output MUST adhere to?
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-9-14)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-9-15)Once I have this information, I can assist you in creating the prompt template.
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-9-16)User (q/Q to quit): 1 rag, 2 none, 3 no, 4 no
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-9-17)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-9-18)Tool Calls:
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-9-19) PromptInstructions (call_tcz0foifsaGKPdZmsZxNnepl)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-9-20) Call ID: call_tcz0foifsaGKPdZmsZxNnepl
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-9-21) Args:
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-9-22)  objective: rag
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-9-23)  variables: ['none']
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-9-24)  constraints: ['no']
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-9-25)  requirements: ['no']
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-9-26)=================================[1m Tool Message [0m=================================
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-9-27)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-9-28)Prompt generated!
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-9-29)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-9-30)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-9-31)Please write a response using the RAG (Red, Amber, Green) rating system.
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-9-32)Done!
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-9-33)User (q/Q to quit): red
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-9-34)==================================[1m Ai Message [0m==================================
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-9-35)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-9-36)Response: The status is RED.
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-9-37)User (q/Q to quit): q
[](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__codelineno-9-38)AI: Byebye

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Build a Customer Support Bot  ](https://langchain-ai.github.io/langgraph/tutorials/customer-support/customer-support/) [ Next  Code generation with RAG and self-correction  ](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgraph_code_assistant/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/tutorials/chatbots/information-gather-prompting/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
