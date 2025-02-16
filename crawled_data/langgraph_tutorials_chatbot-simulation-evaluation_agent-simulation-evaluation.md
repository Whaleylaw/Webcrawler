---
url: https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#chat-bot-evaluation-as-multi-agent-simulation)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Chat Bot Evaluation as Multi-agent Simulation 

[ ](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/?q= "Share")

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
        * [ Agent Architectures  ](https://langchain-ai.github.io/langgraph/tutorials#agent-architectures)
        * Evaluation & Analysis  Evaluation & Analysis 
          * [ Evaluation & Analysis  ](https://langchain-ai.github.io/langgraph/tutorials#evaluation)
          * Chat Bot Evaluation as Multi-agent Simulation  [ Chat Bot Evaluation as Multi-agent Simulation  ](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/) Table of contents 
            * [ Setup  ](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#setup)
            * [ Define Chat Bot  ](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#define-chat-bot)
            * [ Define Simulated User  ](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#define-simulated-user)
            * [ Define the Agent Simulation  ](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#define-the-agent-simulation)
              * [ Define nodes  ](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#define-nodes)
              * [ Define edges  ](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#define-edges)
              * [ Define graph  ](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#define-graph)
            * [ Run Simulation  ](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#run-simulation)
          * [ Chat Bot Benchmarking using Simulation  ](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/langsmith-agent-simulation-evaluation/)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#setup)
  * [ Define Chat Bot  ](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#define-chat-bot)
  * [ Define Simulated User  ](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#define-simulated-user)
  * [ Define the Agent Simulation  ](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#define-the-agent-simulation)
    * [ Define nodes  ](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#define-nodes)
    * [ Define edges  ](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#define-edges)
    * [ Define graph  ](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#define-graph)
  * [ Run Simulation  ](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#run-simulation)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ Tutorials  ](https://langchain-ai.github.io/langgraph/tutorials/)
  4. [ Evaluation & Analysis  ](https://langchain-ai.github.io/langgraph/tutorials#evaluation)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation.ipynb "Edit this page")

# Chat Bot Evaluation as Multi-agent Simulation[¶](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#chat-bot-evaluation-as-multi-agent-simulation "Permanent link")

When building a chat bot, such as a customer support assistant, it can be hard to properly evaluate your bot's performance. It's time-consuming to have to manually interact with it intensively for each code change.

One way to make the evaluation process easier and more reproducible is to simulate a user interaction.

With LangGraph, it's easy to set this up. Below is an example of how to create a "virtual user" to simulate a conversation.

The overall simulation looks something like this:

![diagram]()

## Setup[¶](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#setup "Permanent link")

First, let's install the required packages and set our API keys

```
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-0-1)%%capture --no-stderr
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-0-2)%pip install -U langgraph langchain langchain_openai

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-1-1)importgetpass
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-1-2)importos
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-1-4)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-1-5)def_set_if_undefined(var: str):
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-1-6)  if not os.environ.get(var):
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-1-7)    os.environ[var] = getpass.getpass(f"Please provide your {var}")
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-1-8)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-1-9)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-1-10)_set_if_undefined("OPENAI_API_KEY")

```


Set up [LangSmith](https://smith.langchain.com) for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com). 

## Define Chat Bot[¶](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#define-chat-bot "Permanent link")

Next, we will define our chat bot. For this notebook, we assume the bot's API accepts a list of messages and responds with a message. If you want to update this, all you'll have to change is this section and the "get_messages_for_agent" function in the simulator below.

The implementation within `my_chat_bot` is configurable and can even be run on another system (e.g., if your system isn't running in python).

```
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-2-1)fromtypingimport List
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-2-2)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-2-3)importopenai
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-2-4)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-2-5)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-2-6)# This is flexible, but you can define your agent here, or call your agent API here.
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-2-7)defmy_chat_bot(messages: List[dict]) -> dict:
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-2-8)  system_message = {
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-2-9)    "role": "system",
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-2-10)    "content": "You are a customer support agent for an airline.",
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-2-11)  }
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-2-12)  messages = [system_message] + messages
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-2-13)  completion = openai.chat.completions.create(
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-2-14)    messages=messages, model="gpt-3.5-turbo"
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-2-15)  )
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-2-16)  return completion.choices[0].message.model_dump()

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-3-1)my_chat_bot([{"role": "user", "content": "hi!"}])

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-4-1){'content': 'Hello! How can I assist you today?',
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-4-2) 'role': 'assistant',
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-4-3) 'function_call': None,
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-4-4) 'tool_calls': None}

```


## Define Simulated User[¶](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#define-simulated-user "Permanent link")

We're now going to define the simulated user. This can be anything we want, but we're going to build it as a LangChain bot.

```
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-5-1)fromlangchain_core.promptsimport ChatPromptTemplate, MessagesPlaceholder
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-5-2)fromlangchain_openaiimport ChatOpenAI
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-5-3)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-5-4)system_prompt_template = """You are a customer of an airline company. \
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-5-5)You are interacting with a user who is a customer support person. \
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-5-6)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-5-7){instructions}
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-5-8)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-5-9)When you are finished with the conversation, respond with a single word 'FINISHED'"""
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-5-10)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-5-11)prompt = ChatPromptTemplate.from_messages(
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-5-12)  [
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-5-13)    ("system", system_prompt_template),
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-5-14)    MessagesPlaceholder(variable_name="messages"),
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-5-15)  ]
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-5-16))
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-5-17)instructions = """Your name is Harrison. You are trying to get a refund for the trip you took to Alaska. \
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-5-18)You want them to give you ALL the money back. \
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-5-19)This trip happened 5 years ago."""
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-5-20)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-5-21)prompt = prompt.partial(name="Harrison", instructions=instructions)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-5-22)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-5-23)model = ChatOpenAI()
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-5-24)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-5-25)simulated_user = prompt | model

```


API Reference: [ChatPromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html) | [MessagesPlaceholder](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.MessagesPlaceholder.html) | [ChatOpenAI](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html)

```
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-6-1)fromlangchain_core.messagesimport HumanMessage
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-6-2)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-6-3)messages = [HumanMessage(content="Hi! How can I help you?")]
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-6-4)simulated_user.invoke({"messages": messages})

```


API Reference: [HumanMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.human.HumanMessage.html)

```
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-7-1)AIMessage(content='Hi, I would like to request a refund for a trip I took with your airline company to Alaska. Is it possible to get a refund for that trip?')

```


## Define the Agent Simulation[¶](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#define-the-agent-simulation "Permanent link")

The code below creates a LangGraph workflow to run the simulation. The main components are:

  1. The two nodes: one for the simulated user, the other for the chat bot.
  2. The graph itself, with a conditional stopping criterion.



Read the comments in the code below for more information.

### Define nodes[¶](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#define-nodes "Permanent link")

First, we define the nodes in the graph. These should take in a list of messages and return a list of messages to ADD to the state. These will be thing wrappers around the chat bot and simulated user we have above.

**Note:** one tricky thing here is which messages are which. Because both the chat bot AND our simulated user are both LLMs, both of them will resond with AI messages. Our state will be a list of alternating Human and AI messages. This means that for one of the nodes, there will need to be some logic that flips the AI and human roles. In this example, we will assume that HumanMessages are messages from the simulated user. This means that we need some logic in the simulated user node to swap AI and Human messages.

First, let's define the chat bot node

```
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-8-1)fromlangchain_community.adapters.openaiimport convert_message_to_dict
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-8-2)fromlangchain_core.messagesimport AIMessage
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-8-3)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-8-4)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-8-5)defchat_bot_node(state):
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-8-6)  messages = state["messages"]
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-8-7)  # Convert from LangChain format to the OpenAI format, which our chatbot function expects.
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-8-8)  messages = [convert_message_to_dict(m) for m in messages]
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-8-9)  # Call the chat bot
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-8-10)  chat_bot_response = my_chat_bot(messages)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-8-11)  # Respond with an AI Message
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-8-12)  return {"messages": [AIMessage(content=chat_bot_response["content"])]}

```


API Reference: [convert_message_to_dict](https://python.langchain.com/api_reference/community/adapters/langchain_community.adapters.openai.convert_message_to_dict.html) | [AIMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.AIMessage.html)

Next, let's define the node for our simulated user. This will involve a little logic to swap the roles of the messages.

```
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-9-1)def_swap_roles(messages):
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-9-2)  new_messages = []
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-9-3)  for m in messages:
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-9-4)    if isinstance(m, AIMessage):
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-9-5)      new_messages.append(HumanMessage(content=m.content))
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-9-6)    else:
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-9-7)      new_messages.append(AIMessage(content=m.content))
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-9-8)  return new_messages
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-9-9)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-9-10)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-9-11)defsimulated_user_node(state):
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-9-12)  messages = state["messages"]
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-9-13)  # Swap roles of messages
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-9-14)  new_messages = _swap_roles(messages)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-9-15)  # Call the simulated user
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-9-16)  response = simulated_user.invoke({"messages": new_messages})
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-9-17)  # This response is an AI message - we need to flip this to be a human message
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-9-18)  return {"messages": [HumanMessage(content=response.content)]}

```


### Define edges[¶](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#define-edges "Permanent link")

We now need to define the logic for the edges. The main logic occurs after the simulated user goes, and it should lead to one of two outcomes:

  * Either we continue and call the customer support bot
  * Or we finish and the conversation is over



So what is the logic for the conversation being over? We will define that as either the Human chatbot responds with `FINISHED` (see the system prompt) OR the conversation is more than 6 messages long (this is an arbitrary number just to keep this example short).

```
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-10-1)defshould_continue(state):
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-10-2)  messages = state["messages"]
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-10-3)  if len(messages) > 6:
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-10-4)    return "end"
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-10-5)  elif messages[-1].content == "FINISHED":
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-10-6)    return "end"
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-10-7)  else:
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-10-8)    return "continue"

```


### Define graph[¶](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#define-graph "Permanent link")

We can now define the graph that sets up the simulation!

```
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-1)fromlanggraph.graphimport END, StateGraph, START
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-2)fromlanggraph.graph.messageimport add_messages
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-3)fromtypingimport Annotated
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-4)fromtyping_extensionsimport TypedDict
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-5)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-6)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-7)classState(TypedDict):
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-8)  messages: Annotated[list, add_messages]
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-9)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-10)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-11)graph_builder = StateGraph(State)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-12)graph_builder.add_node("user", simulated_user_node)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-13)graph_builder.add_node("chat_bot", chat_bot_node)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-14)# Every response from your chat bot will automatically go to the
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-15)# simulated user
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-16)graph_builder.add_edge("chat_bot", "user")
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-17)graph_builder.add_conditional_edges(
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-18)  "user",
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-19)  should_continue,
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-20)  # If the finish criteria are met, we will stop the simulation,
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-21)  # otherwise, the virtual user's message will be sent to your chat bot
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-22)  {
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-23)    "end": END,
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-24)    "continue": "chat_bot",
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-25)  },
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-26))
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-27)# The input will first go to your chat bot
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-28)graph_builder.add_edge(START, "chat_bot")
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-29)simulation = graph_builder.compile()

```


API Reference: [END](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.END) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [add_messages](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.message.add_messages)

## Run Simulation[¶](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#run-simulation "Permanent link")

Now we can evaluate our chat bot! We can invoke it with empty messages (this will simulate letting the chat bot start the initial conversation)

```
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-12-1)for chunk in simulation.stream({"messages": []}):
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-12-2)  # Print out all events aside from the final end chunk
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-12-3)  if END not in chunk:
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-12-4)    print(chunk)
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-12-5)    print("----")

```


```
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-13-1){'chat_bot': AIMessage(content='How may I assist you today regarding your flight or any other concerns?')}
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-13-2)----
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-13-3){'user': HumanMessage(content='Hi, my name is Harrison. I am reaching out to request a refund for a trip I took to Alaska with your airline company. The trip occurred about 5 years ago. I would like to receive a refund for the entire amount I paid for the trip. Can you please assist me with this?')}
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-13-4)----
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-13-5){'chat_bot': AIMessage(content="Hello, Harrison. Thank you for reaching out to us. I understand you would like to request a refund for a trip you took to Alaska five years ago. I'm afraid that our refund policy typically has a specific timeframe within which refund requests must be made. Generally, refund requests need to be submitted within 24 to 48 hours after the booking is made, or in certain cases, within a specified cancellation period.\n\nHowever, I will do my best to assist you. Could you please provide me with some additional information? Can you recall any specific details about the booking, such as the flight dates, booking reference or confirmation number? This will help me further look into the possibility of processing a refund for you.")}
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-13-6)----
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-13-7){'user': HumanMessage(content="Hello, thank you for your response. I apologize for not requesting the refund earlier. Unfortunately, I don't have the specific details such as the flight dates, booking reference, or confirmation number at the moment. Is there any other way we can proceed with the refund request without these specific details? I would greatly appreciate your assistance in finding a solution.")}
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-13-8)----
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-13-9){'chat_bot': AIMessage(content="I understand the situation, Harrison. Without specific details like flight dates, booking reference, or confirmation number, it becomes challenging to locate and process the refund accurately. However, I can still try to help you.\n\nTo proceed further, could you please provide me with any additional information you might remember? This could include the approximate date of travel, the departure and arrival airports, the names of the passengers, or any other relevant details related to the booking. The more information you can provide, the better we can investigate the possibility of processing a refund for you.\n\nAdditionally, do you happen to have any documentation related to your trip, such as receipts, boarding passes, or emails from our airline? These documents could assist in verifying your trip and processing the refund request.\n\nI apologize for any inconvenience caused, and I'll do my best to assist you further based on the information you can provide.")}
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-13-10)----
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-13-11){'user': HumanMessage(content="I apologize for the inconvenience caused. Unfortunately, I don't have any additional information or documentation related to the trip. It seems that I am unable to provide you with the necessary details to process the refund request. I understand that this may limit your ability to assist me further, but I appreciate your efforts in trying to help. Thank you for your time. \n\nFINISHED")}
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-13-12)----
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-13-13){'chat_bot': AIMessage(content="I understand, Harrison. I apologize for any inconvenience caused, and I appreciate your understanding. If you happen to locate any additional information or documentation in the future, please don't hesitate to reach out to us again. Our team will be more than happy to assist you with your refund request or any other travel-related inquiries. Thank you for contacting us, and have a great day!")}
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-13-14)----
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-13-15){'user': HumanMessage(content='FINISHED')}
[](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-13-16)----

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Self-Discover Agent  ](https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/) [ Next  Chat Bot Benchmarking using Simulation  ](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/langsmith-agent-simulation-evaluation/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
