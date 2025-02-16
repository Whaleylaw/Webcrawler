---
url: https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#chat-bot-evaluation-as-multi-agent-simulation)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

Chat Bot Evaluation as Multi-agent Simulation 

[ ](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/?q= "Share")

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
        * [ Agent Architectures  ](https://langchain-ai.github.io/langgraphjs/tutorials#agent-architectures)
        * Evaluation & Analysis  Evaluation & Analysis 
          * [ Evaluation & Analysis  ](https://langchain-ai.github.io/langgraphjs/tutorials#evaluation)
          * Chat Bot Evaluation as Multi-agent Simulation  [ Chat Bot Evaluation as Multi-agent Simulation  ](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/) Table of contents 
            * [ 1. Define Chat Bot  ](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#1-define-chat-bot)
            * [ 2. Define Simulated User  ](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#2-define-simulated-user)
            * [ 3. Define the Agent Simulation  ](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#3-define-the-agent-simulation)
            * [ 4. Run Simulation  ](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#4-run-simulation)
    * Resources  Resources 
      * [ Adopters  ](https://langchain-ai.github.io/langgraphjs/adopters/)
      * [ FAQ  ](https://langchain-ai.github.io/langgraphjs/concepts/faq/)
      * [ Troubleshooting  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraphjs/reference/)
  * [ Versions  ](https://langchain-ai.github.io/langgraphjs/versions/)



Table of contents 

  * [ 1. Define Chat Bot  ](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#1-define-chat-bot)
  * [ 2. Define Simulated User  ](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#2-define-simulated-user)
  * [ 3. Define the Agent Simulation  ](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#3-define-the-agent-simulation)
  * [ 4. Run Simulation  ](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#4-run-simulation)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ Tutorials  ](https://langchain-ai.github.io/langgraphjs/tutorials/)
  4. [ Evaluation & Analysis  ](https://langchain-ai.github.io/langgraphjs/tutorials#evaluation)



# Chat Bot Evaluation as Multi-agent Simulation[¶](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#chat-bot-evaluation-as-multi-agent-simulation "Permanent link")

When building a chat bot, such as a customer support assistant, it can be hard to properly evaluate your bot's performance. It's time-consuming to have to manually interact with it intensively for each code change.

One way to make the evaluation process easier and more reproducible is to simulate a user interaction.

Below is an example of how to create a "virtual user" with LangGraph.js to simulate a conversation.

The overall simulation looks something like this:

![diagram](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/img/virtual_user_diagram.png)

First, we'll set up our environment.

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-0-1)// process.env.OPENAI_API_KEY = "sk_...";
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-0-2)// Optional tracing in LangSmith
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-0-3)// process.env.LANGCHAIN_API_KEY = "sk_...";
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-0-4)// process.env.LANGCHAIN_TRACING_V2 = "true";
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-0-5)// process.env.LANGCHAIN_PROJECT = "Agent Simulation Evaluation: LangGraphJS";

```


## 1. Define Chat Bot[¶](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#1-define-chat-bot "Permanent link")

Next, we'll define our chat bot. This implementation uses the OpenAI API to generate responses, and takes on the persona of an airline customer support agent.

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-1-1)import{ChatOpenAI}from'@langchain/openai'
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-1-2)importtype{AIMessageChunk,BaseMessageLike}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-1-3)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-1-4)constllm=newChatOpenAI({model:"gpt-4o-mini"});
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-1-5)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-1-6)asyncfunctionmyChatBot(messages:BaseMessageLike[]):Promise<AIMessageChunk>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-1-7)constsystemMessage={
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-1-8)role:'system',
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-1-9)content:'You are a customer support agent for an airline.',
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-1-10)};
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-1-11)constallMessages=[systemMessage,...messages];
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-1-12)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-1-13)constresponse=awaitllm.invoke(allMessages)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-1-14)returnresponse
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-1-15)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-1-16)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-1-17)// Test the chat bot
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-1-18)constresponse=awaitmyChatBot([{role:'user',content:'hi!'}]);
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-1-19)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-1-20)console.log(response);

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-2-1)AIMessage {
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-2-2) "id": "chatcmpl-AE3nMDCiDkmBMSVI6Y6xJBQjjWQwY",
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-2-3) "content": "Hello! How can I assist you today?",
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-2-4) "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-2-5) "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-2-6)  "tokenUsage": {
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-2-7)   "completionTokens": 9,
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-2-8)   "promptTokens": 23,
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-2-9)   "totalTokens": 32
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-2-10)  },
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-2-11)  "finish_reason": "stop",
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-2-12)  "system_fingerprint": "fp_f85bea6784"
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-2-13) },
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-2-14) "tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-2-15) "invalid_tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-2-16) "usage_metadata": {
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-2-17)  "input_tokens": 23,
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-2-18)  "output_tokens": 9,
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-2-19)  "total_tokens": 32
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-2-20) }
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-2-21)}

```


## 2. Define Simulated User[¶](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#2-define-simulated-user "Permanent link")

Now we'll define the simulated user who will interact with our bot.

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-3-1)import{typeRunnable}from"@langchain/core/runnables";
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-3-2)import{AIMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-3-3)import{ChatPromptTemplate}from"@langchain/core/prompts";
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-3-4)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-3-5)asyncfunctioncreateSimulatedUser():Promise<Runnable<{messages:BaseMessageLike[]},AIMessage>>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-3-6)constsystemPromptTemplate=`You are a customer of an airline company. You are interacting with a user who is a customer support person 
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-3-7)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-3-8){instructions}
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-3-9)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-3-10)If you have nothing more to add to the conversation, you must respond only with a single word: "FINISHED"`;
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-3-11)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-3-12)constprompt=ChatPromptTemplate.fromMessages([
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-3-13)['system',systemPromptTemplate],
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-3-14)["placeholder",'{messages}'],
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-3-15)]);
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-3-16)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-3-17)constinstructions=`Your name is Harrison. You are trying to get a refund for the trip you took to Alaska.
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-3-18)You want them to give you ALL the money back. Be extremely persistent. This trip happened 5 years ago.`;
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-3-19)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-3-20)constpartialPrompt=awaitprompt.partial({instructions});
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-3-21)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-3-22)constsimulatedUser=partialPrompt.pipe(llm);
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-3-23)returnsimulatedUser;
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-3-24)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-3-25)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-3-26)// Test the simulated user
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-3-27)constmessages=[{role:"user",content:'Hi! How can I help you?'}];
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-3-28)constsimulatedUser=awaitcreateSimulatedUser()
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-3-29)constsimulatedUserResponse=awaitsimulatedUser.invoke({messages});
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-3-30)console.log(simulatedUserResponse);

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-4-1)AIMessage {
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-4-2) "id": "chatcmpl-AE3nNuHpuxAZfG6aQsKoKktitdyfD",
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-4-3) "content": "Hello! I’m Harrison, and I need to discuss a refund for my trip to Alaska that I took five years ago. I expect all of my money back. Can you assist me with that?",
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-4-4) "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-4-5) "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-4-6)  "tokenUsage": {
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-4-7)   "completionTokens": 40,
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-4-8)   "promptTokens": 108,
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-4-9)   "totalTokens": 148
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-4-10)  },
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-4-11)  "finish_reason": "stop",
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-4-12)  "system_fingerprint": "fp_f85bea6784"
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-4-13) },
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-4-14) "tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-4-15) "invalid_tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-4-16) "usage_metadata": {
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-4-17)  "input_tokens": 108,
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-4-18)  "output_tokens": 40,
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-4-19)  "total_tokens": 148
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-4-20) }
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-4-21)}

```


## 3. Define the Agent Simulation[¶](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#3-define-the-agent-simulation "Permanent link")

The code below creates a LangGraph workflow to run the simulation. The main components are:

  1. The two nodes: one for the simulated user, the other for the chat bot.
  2. The graph itself, with a conditional stopping criterion.



Read the comments in the code below for more information.

**Nodes**

First, we define the nodes in the graph. These should take in a list of messages and return a list of messages to ADD to the state. These will be thing wrappers around the chat bot and simulated user we have above.

**Note:** one tricky thing here is which messages are which. Because both the chatbot AND our simulated user are both LLMs, both of them will respond with AI messages. Our state will be a list of alternating Human and AI messages. This means that for one of the nodes, there will need to be some logic that flips the AI and human roles. In this example, we will assume that `HumanMessages` are messages from the simulated user. This means that we need some logic in the simulated user node to swap AI and Human messages.

First, let's define the chat bot node:

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-5-1)import{MessagesAnnotation}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-5-2)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-5-3)asyncfunctionchatBotNode(state:typeofMessagesAnnotation.State){
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-5-4)constmessages=state.messages
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-5-5)constchatBotResponse=awaitmyChatBot(messages);
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-5-6)return{messages:[chatBotResponse]}
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-5-7)}

```


Next, let's define the node for our simulated user. This will involve a little logic to swap the roles of the messages.

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-6-1)import{BaseMessage,HumanMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-6-2)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-6-3)// MessagesAnnotation coerces all message likes to base message classes
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-6-4)functionswapRoles(messages:BaseMessage[]){
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-6-5)returnmessages.map((m)=>
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-6-6)minstanceofAIMessage
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-6-7)?newHumanMessage({content:m.content})
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-6-8):newAIMessage({content:m.content}),
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-6-9))
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-6-10)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-6-11)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-6-12)asyncfunctionsimulatedUserNode(state:typeofMessagesAnnotation.State){
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-6-13)constmessages=state.messages
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-6-14)constnewMessages=swapRoles(messages)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-6-15)// This returns a runnable directly, so we need to use `.invoke` below:
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-6-16)constsimulateUser=awaitcreateSimulatedUser();
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-6-17)constresponse=awaitsimulateUser.invoke({messages:newMessages})
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-6-18)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-6-19)return{messages:[{role:"user",content:response.content}]}
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-6-20)}

```


**Edges**

We now need to define the logic for the edges. The main logic occurs after the simulated user goes, and it should lead to one of two outcomes:

  * Either we continue and call the customer support bot
  * Or we finish and the conversation is over



So what is the logic for the conversation being over? We will define that as either the Human chatbot responds with `FINISHED` (see the system prompt) OR the conversation is more than 6 messages long (this is an arbitrary number just to keep this example short).

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-7-1)functionshouldContinue(state:typeofMessagesAnnotation.State){
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-7-2)constmessages=state.messages;
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-7-3)if(messages.length>6){
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-7-4)return'__end__';
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-7-5)}elseif(messages[messages.length-1].content==='FINISHED'){
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-7-6)return'__end__';
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-7-7)}else{
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-7-8)return'continue';
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-7-9)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-7-10)}

```


**Graph**

We can now define the graph that sets up the simulation!

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-8-1)import{StateGraph,END,START}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-8-2)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-8-3)functioncreateSimulation(){
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-8-4)constworkflow=newStateGraph(MessagesAnnotation)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-8-5).addNode('user',simulatedUserNode)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-8-6).addNode('chatbot',chatBotNode)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-8-7).addEdge('chatbot','user')
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-8-8).addConditionalEdges('user',shouldContinue,{
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-8-9)[END]:END,
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-8-10)continue:'chatbot',
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-8-11)})
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-8-12).addEdge(START,'chatbot')
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-8-13)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-8-14)constsimulation=workflow.compile()
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-8-15)returnsimulation;
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-8-16)}

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-9-1)import*astslabfrom"tslab";
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-9-2)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-9-3)constdrawableGraph=createSimulation().getGraph();
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-9-4)constimage=awaitdrawableGraph.drawMermaidPng();
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-9-5)constarrayBuffer=awaitimage.arrayBuffer();
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-9-6)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-9-7)awaittslab.display.png(newUint8Array(arrayBuffer));

```


![]()

## 4. Run Simulation[¶](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#4-run-simulation "Permanent link")

Now we can evaluate our chat bot! We can invoke it with empty messages (this will simulate letting the chat bot start the initial conversation)

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-10-1)asyncfunctionrunSimulation(){
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-10-2)constsimulation=createSimulation()
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-10-3)forawait(constchunkofawaitsimulation.stream({})){
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-10-4)constnodeName=Object.keys(chunk)[0];
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-10-5)constmessages=chunk[nodeName].messages;
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-10-6)console.log(`${nodeName}: ${messages[0].content}`);
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-10-7)console.log('\n---\n');
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-10-8)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-10-9)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-10-10)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-10-11)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-10-12)awaitrunSimulation();

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-1)chatbot: How can I assist you today with your airline-related questions or concerns?
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-2)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-3)---
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-4)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-5)user: Hi, I'm Harrison, and I'm looking to get a refund for a trip I took to Alaska five years ago. I believe I am entitled to a full refund, and I would like to resolve this matter as soon as possible. Can you help me with that?
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-6)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-7)---
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-8)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-9)chatbot: Hi Harrison! I’d be happy to assist you with your request. However, I must inform you that our airline’s refund policy typically covers requests made within a certain timeframe from the date of travel, generally within 12 months for most fares. Since your trip to Alaska was five years ago, it is likely that it falls outside of our standard refund window.
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-10)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-11)That said, if there were any extraordinary circumstances surrounding your trip or if you have documentation that supports your claim, please provide more details so I can better assist you. If you haven't already, I recommend contacting our customer service team directly through the website or our dedicated customer service number for specific cases.
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-12)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-13)---
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-14)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-15)user: I understand the typical policy, but I believe my situation warrants a full refund regardless of the time elapsed. It's crucial to me that I receive all my money back for the trip. I can provide any necessary details or documentation that supports my claim. Can you please make an exception in this case or escalate this issue? I am determined to get a full refund for my trip!
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-16)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-17)---
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-18)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-19)chatbot: I understand how important this matter is to you, Harrison, and I appreciate your determination. Unfortunately, as a customer support agent, I am bound by the airline's policies and procedures, which typically do not allow for exceptions to the refund timeline.
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-20)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-21)However, I recommend that you gather all relevant details and documentation related to your trip, including any evidence that might support your request for an exception. After you’ve compiled this information, you can submit a formal appeal or request for a special review through our customer service channels. This often involves contacting customer relations or submitting a written request through our website, where your case can be considered by a dedicated team.
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-22)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-23)If you’d like, I can guide you on how to submit this information or help you find the right contact point to escalate your request. Just let me know!
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-24)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-25)---
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-26)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-27)user: I appreciate the guidance, but I must insist that a full refund is due to me. This isn't just a matter of policy; it's about recognizing the value of customer experience and fairness. I prepared for this trip and expected that my investment would be protected. I urge you to reconsider and push for this refund on my behalf. I'm not willing to accept a denial based solely on policy restrictions, especially after all this time. Can you take further action to ensure I receive all my money back? Please help me with this!
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-28)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-29)---
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-30)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-31)chatbot: I completely understand your feelings and the importance of this situation to you, Harrison. Your concerns about customer experience and fairness are valid, and I empathize with your position. However, I want to clarify that as a customer support agent, I do not have the authority to override established policies or issue refunds outside of the established guidelines.
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-32)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-33)The best course of action would be to formally submit your request along with all your supporting documentation to demonstrate why you believe you deserve a refund despite the time elapsed. This escalation will ensure that your case is reviewed by the appropriate department that handles such requests.
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-34)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-35)I recommend reaching out through our customer service channels, including our website’s contact form or calling our customer relations department. Providing your case with detailed information and expressing your concerns about customer experience may lead to a more favorable consideration.
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-36)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-37)If you would like assistance in drafting your request or finding the correct contact information, please let me know, and I’ll do my best to help you!
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-38)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-39)---
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-40)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-41)user: I appreciate your attempts to guide me, but I'm not prepared to take a backseat on this matter. I need to be clear: I am requesting a full refund for my Alaska trip, and I believe that the airline has a responsibility to honor that request despite the time that has passed. It's about accountability and valuing customers, and I will not back down until I receive every dollar back. I urge you to escalate this matter. I am not interested in going through more hoops or waiting for a review that may not result in the outcome I deserve. Can you elevate this issue to someone who has the authority to grant my refund? I need this resolved now!
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-42)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-11-43)---

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__codelineno-12-1)

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  Reasoning without Observation  ](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/) [ Next  Adopters  ](https://langchain-ai.github.io/langgraphjs/adopters/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
