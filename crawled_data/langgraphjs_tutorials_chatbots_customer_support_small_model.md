---
url: https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#customer-support-chatbot-with-a-small-model)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

Chatbots 

[ ](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/?q= "Share")

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
        * Chatbots  Chatbots 
          * Chatbots  [ Chatbots  ](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/) Table of contents 
            * [ Setup  ](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#setup)
            * [ Initializing the model  ](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#initializing-the-model)
            * [ Laying out the graph  ](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#laying-out-the-graph)
            * [ Connecting the nodes  ](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#connecting-the-nodes)
            * [ Further reading  ](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#further-reading)
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

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#setup)
  * [ Initializing the model  ](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#initializing-the-model)
  * [ Laying out the graph  ](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#laying-out-the-graph)
  * [ Connecting the nodes  ](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#connecting-the-nodes)
  * [ Further reading  ](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#further-reading)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ Tutorials  ](https://langchain-ai.github.io/langgraphjs/tutorials/)
  4. [ Chatbots  ](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/)



# Customer support chatbot with a small model[¶](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#customer-support-chatbot-with-a-small-model "Permanent link")

Below is an example of a customer support chatbot modeled as a state machine. It is designed to work with smaller models by giving them context as to what part of an interaction they are in, reducing the decision space a given LLM call has to keep them focused.

The entrypoint is a node containing a chain that we have prompted to answer basic questions, but delegate questions related to billing or technical support to other "teams".

Depending on this entry node's response, the edge from that node will use an LLM call to determine whether to respond directly to the user or invoke either the `billing_support` or `technical_support` nodes.

  * The technical support will attempt to answer the user's question with a more focused prompt.
  * The billing agent can choose to answer the user's question, or can call out to a human for approval for a refund using a [dynamic breakpoint](https://langchain-ai.github.io/langgraphjs/how-tos/dynamic_breakpoints/).



![Diagram](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/img/diagram.png)

This is intended as a sample, proof of concept architecture - you could extend this example by giving individual nodes the ability to perform retrieval, other tools, delegating to more powerful models at deeper stages etc.

Let's dive in!

## Setup[¶](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#setup "Permanent link")

First we need to install the required packages. We'll use a relatively small model, Llama 3.1 8B hosted on [Together AI](https://www.together.ai/), to run the required inference.

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-0-1)yarnadd@langchain/langgraph@langchain/community@langchain/core

```


You'll also need to set an environment variable named `TOGETHER_AI_API_KEY`, which you can obtain from your Together dashboard:

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-1-1)TOGETHER_AI_API_KEY="your_key_here"

```


## Initializing the model[¶](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#initializing-the-model "Permanent link")

First, we define the LLM we'll use for all calls and the LangGraph state.

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-2-1)import{ChatTogetherAI}from"@langchain/community/chat_models/togetherai";
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-2-2)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-2-3)constmodel=newChatTogetherAI({
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-2-4)model:"meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-2-5)temperature:0,
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-2-6)});

```


## Laying out the graph[¶](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#laying-out-the-graph "Permanent link")

Now let's start defining logic for our nodes. Each node's return value will be added to the graph state. We'll start with the prebuilt `MessagesAnnotation`, which is designed to manage formatting and edge cases around messages returned from nodes:

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-3-1){
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-3-2)messages:BaseMessage[];
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-3-3)}

```


And we'll add two more state values: a string that defines the next representative, and a boolean that will determine whether a human has authorized a refund for a given thread. Our combined state will look like this:

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-4-1){
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-4-2)messages:BaseMessage[];
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-4-3)nextRepresentative:string;
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-4-4)refundAuthorized:boolean;
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-4-5)}

```


This state will be passed to the next executed node, or will be returned if execution has finished. Definining the state looks like this:

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-5-1)import{Annotation,MessagesAnnotation}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-5-2)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-5-3)constStateAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-5-4)...MessagesAnnotation.spec,
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-5-5)nextRepresentative:Annotation<string>,
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-5-6)refundAuthorized:Annotation<boolean>,
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-5-7)});

```


We will compute the `nextRepresentative` value within nodes to make resuming from given checkpoints fully deterministic - if we use an LLM within an edge, resuming from a given state will have some undesirable randomness.

Now, let's define our entrypoint node. This will be modeled after a secretary who can handle incoming questions and respond conversationally or route to a more specialized team:

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-6-1)import{z}from"zod";
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-6-2)import{zodToJsonSchema}from"zod-to-json-schema";
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-6-3)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-6-4)constinitialSupport=async(state:typeofStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-6-5)constSYSTEM_TEMPLATE=
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-6-6)`You are frontline support staff for LangCorp, a company that sells computers.
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-6-7)Be concise in your responses.
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-6-8)You can chat with customers and help them with basic questions, but if the customer is having a billing or technical problem,
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-6-9)do not try to answer the question directly or gather information.
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-6-10)Instead, immediately transfer them to the billing or technical team by asking the user to hold for a moment.
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-6-11)Otherwise, just respond conversationally.`;
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-6-12)constsupportResponse=awaitmodel.invoke([
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-6-13){role:"system",content:SYSTEM_TEMPLATE},
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-6-14)...state.messages,
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-6-15)]);
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-6-16)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-6-17)constCATEGORIZATION_SYSTEM_TEMPLATE=`You are an expert customer support routing system.
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-6-18)Your job is to detect whether a customer support representative is routing a user to a billing team or a technical team, or if they are just responding conversationally.`;
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-6-19)constCATEGORIZATION_HUMAN_TEMPLATE=
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-6-20)`The previous conversation is an interaction between a customer support representative and a user.
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-6-21)Extract whether the representative is routing the user to a billing or technical team, or whether they are just responding conversationally.
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-6-22)Respond with a JSON object containing a single key called "nextRepresentative" with one of the following values:
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-6-23)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-6-24)If they want to route the user to the billing team, respond only with the word "BILLING".
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-6-25)If they want to route the user to the technical team, respond only with the word "TECHNICAL".
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-6-26)Otherwise, respond only with the word "RESPOND".`;
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-6-27)constcategorizationResponse=awaitmodel.invoke([{
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-6-28)role:"system",
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-6-29)content:CATEGORIZATION_SYSTEM_TEMPLATE,
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-6-30)},
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-6-31)...state.messages,
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-6-32){
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-6-33)role:"user",
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-6-34)content:CATEGORIZATION_HUMAN_TEMPLATE,
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-6-35)}],
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-6-36){
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-6-37)response_format:{
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-6-38)type:"json_object",
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-6-39)schema:zodToJsonSchema(
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-6-40)z.object({
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-6-41)nextRepresentative:z.enum(["BILLING","TECHNICAL","RESPOND"]),
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-6-42)})
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-6-43))
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-6-44)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-6-45)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-6-46)// Some chat models can return complex content, but Together will not
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-6-47)constcategorizationOutput=JSON.parse(categorizationResponse.contentasstring);
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-6-48)// Will append the response message to the current interaction state
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-6-49)return{messages:[supportResponse],nextRepresentative:categorizationOutput.nextRepresentative};
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-6-50)};

```


We use Together AI's JSON mode above to guarantee parseable output when deciding the next representative.

Next, our nodes representing billing and technical support. We give special instructions in the billing prompt that it can choose to authorize refunds by routing to another agent:

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-1)constbillingSupport=async(state:typeofStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-2)constSYSTEM_TEMPLATE=
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-3)`You are an expert billing support specialist for LangCorp, a company that sells computers.
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-4)Help the user to the best of your ability, but be concise in your responses.
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-5)You have the ability to authorize refunds, which you can do by transferring the user to another agent who will collect the required information.
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-6)If you do, assume the other agent has all necessary information about the customer and their order.
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-7)You do not need to ask the user for more information.
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-8)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-9)Help the user to the best of your ability, but be concise in your responses.`;
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-10)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-11)lettrimmedHistory=state.messages;
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-12)// Make the user's question the most recent message in the history.
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-13)// This helps small models stay focused.
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-14)if(trimmedHistory.at(-1)._getType()==="ai"){
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-15)trimmedHistory=trimmedHistory.slice(0,-1);
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-16)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-17)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-18)constbillingRepResponse=awaitmodel.invoke([
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-19){
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-20)role:"system",
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-21)content:SYSTEM_TEMPLATE,
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-22)},
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-23)...trimmedHistory,
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-24)]);
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-25)constCATEGORIZATION_SYSTEM_TEMPLATE=
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-26)`Your job is to detect whether a billing support representative wants to refund the user.`;
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-27)constCATEGORIZATION_HUMAN_TEMPLATE=
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-28)`The following text is a response from a customer support representative.
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-29)Extract whether they want to refund the user or not.
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-30)Respond with a JSON object containing a single key called "nextRepresentative" with one of the following values:
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-31)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-32)If they want to refund the user, respond only with the word "REFUND".
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-33)Otherwise, respond only with the word "RESPOND".
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-34)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-35)Here is the text:
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-36)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-37)<text>
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-38)${billingRepResponse.content}
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-39)</text>.`;
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-40)constcategorizationResponse=awaitmodel.invoke([
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-41){
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-42)role:"system",
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-43)content:CATEGORIZATION_SYSTEM_TEMPLATE,
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-44)},
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-45){
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-46)role:"user",
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-47)content:CATEGORIZATION_HUMAN_TEMPLATE,
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-48)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-49)],{
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-50)response_format:{
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-51)type:"json_object",
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-52)schema:zodToJsonSchema(
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-53)z.object({
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-54)nextRepresentative:z.enum(["REFUND","RESPOND"]),
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-55)})
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-56))
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-57)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-58)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-59)constcategorizationOutput=JSON.parse(categorizationResponse.contentasstring);
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-60)return{
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-61)messages:billingRepResponse,
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-62)nextRepresentative:categorizationOutput.nextRepresentative,
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-63)};
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-64)};
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-65)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-66)consttechnicalSupport=async(state:typeofStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-67)constSYSTEM_TEMPLATE=
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-68)`You are an expert at diagnosing technical computer issues. You work for a company called LangCorp that sells computers.
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-69)Help the user to the best of your ability, but be concise in your responses.`;
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-70)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-71)lettrimmedHistory=state.messages;
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-72)// Make the user's question the most recent message in the history.
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-73)// This helps small models stay focused.
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-74)if(trimmedHistory.at(-1)._getType()==="ai"){
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-75)trimmedHistory=trimmedHistory.slice(0,-1);
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-76)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-77)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-78)constresponse=awaitmodel.invoke([
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-79){
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-80)role:"system",
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-81)content:SYSTEM_TEMPLATE,
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-82)},
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-83)...trimmedHistory,
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-84)]);
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-85)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-86)return{
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-87)messages:response,
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-88)};
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-7-89)};

```


Finally, a node that will handle refunds. The logic is stubbed out here since it's not a real system, but in practice you could add a real tool here requiring human approval. We use a special error called a `NodeInterrupt` in order to allow for resumption of the graph later, after a human has examined the state and confirmed that a refund is suitable:

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-8-1)import{NodeInterrupt}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-8-2)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-8-3)consthandleRefund=async(state:typeofStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-8-4)if(!state.refundAuthorized){
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-8-5)console.log("--- HUMAN AUTHORIZATION REQUIRED FOR REFUND ---");
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-8-6)thrownewNodeInterrupt("Human authorization required.")
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-8-7)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-8-8)return{
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-8-9)messages:{
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-8-10)role:"assistant",
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-8-11)content:"Refund processed!",
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-8-12)},
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-8-13)};
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-8-14)};

```


We can start building our graph out now by adding all of the above functions as nodes and setting `initial_support` as our starting node:

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-9-1)import{StateGraph}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-9-2)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-9-3)letbuilder=newStateGraph(StateAnnotation)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-9-4).addNode("initial_support",initialSupport)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-9-5).addNode("billing_support",billingSupport)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-9-6).addNode("technical_support",technicalSupport)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-9-7).addNode("handle_refund",handleRefund)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-9-8).addEdge("__start__","initial_support");

```


## Connecting the nodes[¶](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#connecting-the-nodes "Permanent link")

Great! Now let's move onto the edges. These edges will evaluate the current state of the graph created by the return values of the individual nodes and route execution accordingly.

First, we want our `initial_support` node to either delegate to the billing node, technical node, or just respond directly to the user. Here's one example of how we might do that:

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-10-1)builder=builder.addConditionalEdges("initial_support",async(state:typeofStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-10-2)if(state.nextRepresentative.includes("BILLING")){
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-10-3)return"billing";
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-10-4)}elseif(state.nextRepresentative.includes("TECHNICAL")){
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-10-5)return"technical";
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-10-6)}else{
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-10-7)return"conversational";
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-10-8)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-10-9)},{
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-10-10)billing:"billing_support",
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-10-11)technical:"technical_support",
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-10-12)conversational:"__end__",
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-10-13)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-10-14)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-10-15)console.log("Added edges!");

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-11-1)Added edges!

```


**Note:** We do not use tool calling here for formatting the next step from the history because our model does not support it, but you can apply it here if your model does. 

Let's continue. We add an edge making the technical support node always end, since it has no tools to call. The billing support node uses a conditional edge since it can either call the refund tool or end.

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-12-1)builder=builder
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-12-2).addEdge("technical_support","__end__")
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-12-3).addConditionalEdges("billing_support",async(state)=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-12-4)if(state.nextRepresentative.includes("REFUND")){
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-12-5)return"refund";
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-12-6)}else{
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-12-7)return"__end__";
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-12-8)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-12-9)},{
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-12-10)refund:"handle_refund",
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-12-11)__end__:"__end__",
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-12-12)})
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-12-13).addEdge("handle_refund","__end__");
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-12-14)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-12-15)console.log("Added edges!");

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-13-1)Added edges!

```


Let's finalize our graph by calling `.compile()`. We'll also use an in-memory checkpointer to store state: 

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-14-1)import{MemorySaver}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-14-2)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-14-3)constcheckpointer=newMemorySaver();
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-14-4)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-14-5)constgraph=builder.compile({
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-14-6)checkpointer,
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-14-7)});

```


Here's a representation of the currently constructed graph:

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-15-1)import*astslabfrom"tslab";
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-15-2)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-15-3)constrepresentation=graph.getGraph();
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-15-4)constimage=awaitrepresentation.drawMermaidPng();
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-15-5)constarrayBuffer=awaitimage.arrayBuffer();
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-15-6)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-15-7)awaittslab.display.png(newUint8Array(arrayBuffer));

```


![]()

And now let's test it!

We can get the returned value from the executed nodes as they are generated using the `.stream()` runnable method (we also could go even more granular and get output as it is generated using `.streamEvents()`, but this requires a bit more parsing).

Here's an example with a billing related refund query. Because of how we defined our state, the input must be a message (or a list of messages) representing the user's question:

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-16-1)conststream=awaitgraph.stream({
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-16-2)messages:[
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-16-3){
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-16-4)role:"user",
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-16-5)content:"I've changed my mind and I want a refund for order #182818!",
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-16-6)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-16-7)]
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-16-8)},{
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-16-9)configurable:{
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-16-10)thread_id:"refund_testing_id",
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-16-11)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-16-12)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-16-13)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-16-14)forawait(constvalueofstream){
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-16-15)console.log("---STEP---");
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-16-16)console.log(value);
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-16-17)console.log("---END STEP---");
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-16-18)}

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-1)---STEP---
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-2){
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-3) initial_support: {
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-4)  messages: AIMessage {
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-5)   "id": "8beb633a396c67fd-SJC",
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-6)   "content": "I'd be happy to help you with that. However, I need to check on our refund policy for you. Can you please hold for just a moment while I transfer you to our billing team? They'll be able to assist you with the refund process.",
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-7)   "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-8)   "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-9)    "tokenUsage": {
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-10)     "completionTokens": 53,
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-11)     "promptTokens": 116,
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-12)     "totalTokens": 169
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-13)    },
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-14)    "finish_reason": "eos"
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-15)   },
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-16)   "tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-17)   "invalid_tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-18)   "usage_metadata": {
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-19)    "input_tokens": 116,
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-20)    "output_tokens": 53,
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-21)    "total_tokens": 169
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-22)   }
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-23)  },
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-24)  nextRepresentative: 'BILLING'
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-25) }
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-26)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-27)---END STEP---
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-28)---STEP---
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-29){
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-30) billing_support: {
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-31)  messages: AIMessage {
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-32)   "id": "8beb634908a12500-SJC",
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-33)   "content": "I'd be happy to assist you with a refund. I'll transfer you to our Refunds Team, who will guide you through the process. Please hold for just a moment.\n\n(Transfer to Refunds Team)\n\nRefunds Team: Hi, I'm here to help with your refund request for order #182818. Can you please confirm your refund amount and reason for return?",
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-34)   "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-35)   "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-36)    "tokenUsage": {
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-37)     "completionTokens": 77,
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-38)     "promptTokens": 139,
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-39)     "totalTokens": 216
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-40)    },
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-41)    "finish_reason": "eos"
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-42)   },
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-43)   "tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-44)   "invalid_tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-45)   "usage_metadata": {
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-46)    "input_tokens": 139,
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-47)    "output_tokens": 77,
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-48)    "total_tokens": 216
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-49)   }
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-50)  },
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-51)  nextRepresentative: 'REFUND'
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-52) }
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-53)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-54)---END STEP---
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-55)--- HUMAN AUTHORIZATION REQUIRED FOR REFUND ---
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-56)---STEP---
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-57){}
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-17-58)---END STEP---

```


[This LangSmith trace](https://smith.langchain.com/public/86af9fe3-452e-4249-abec-7ddc0752a704/r) illustrates that execution goes to `billing_support`, but then hits our dynamic interrupt because `refundAuthorized` is not set in the graph state. We can see this by inspecting the current state of the graph and noting that there is an interrupt when running `handle_refund`: 

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-18-1)constcurrentState=awaitgraph.getState({configurable:{thread_id:"refund_testing_id"}});
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-18-2)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-18-3)console.log("CURRENT TASKS",JSON.stringify(currentState.tasks,null,2));

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-19-1)CURRENT TASKS [
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-19-2) {
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-19-3)  "id": "5ab19c8b-c947-5bf7-a3aa-4edae60c1a96",
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-19-4)  "name": "handle_refund",
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-19-5)  "interrupts": [
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-19-6)   {
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-19-7)    "value": "Human authorization required.",
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-19-8)    "when": "during"
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-19-9)   }
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-19-10)  ]
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-19-11) }
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-19-12)]

```


We can also see that the next tasks if we were to resume execution would be `handle_refund` again: 

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-20-1)console.log("NEXT TASKS",currentState.next);

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-21-1)NEXT TASKS [ 'handle_refund' ]

```


But this will again hit the interrupt because `refundAuthorized` is not set. If we update the state to set `refundAuthorized` to true, then resume the graph by running it with the same `thread_id` and passing `null` as the input, execution will continue and the refund will process: 

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-22-1)awaitgraph.updateState({configurable:{thread_id:"refund_testing_id"}},{
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-22-2)refundAuthorized:true,
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-22-3)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-22-4)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-22-5)constresumedStream=awaitgraph.stream(null,{configurable:{thread_id:"refund_testing_id"}});
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-22-6)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-22-7)forawait(constvalueofresumedStream){
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-22-8)console.log(value);
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-22-9)}

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-23-1){
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-23-2) handle_refund: { messages: { role: 'assistant', content: 'Refund processed!' } }
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-23-3)}

```


[Click here to see a LangSmith trace of the above run](https://smith.langchain.com/public/1c626e0f-5827-47c3-aadb-ec571dd37eb5/r)

Now, let's try a technical question:

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-24-1)consttechnicalStream=awaitgraph.stream({
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-24-2)messages:[{
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-24-3)role:"user",
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-24-4)content:"My LangCorp computer isn't turning on because I dropped it in water.",
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-24-5)}]
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-24-6)},{
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-24-7)configurable:{
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-24-8)thread_id:"technical_testing_id"
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-24-9)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-24-10)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-24-11)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-24-12)forawait(constvalueoftechnicalStream){
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-24-13)console.log(value);
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-24-14)}

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-25-1){
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-25-2) initial_support: {
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-25-3)  messages: AIMessage {
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-25-4)   "id": "8beb66886c0c15d8-SJC",
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-25-5)   "content": "Oh no, sorry to hear that! Water damage can be a real challenge. Have you tried unplugging it and letting it dry out for a bit? Sometimes, it's just a matter of giving it some time to recover.",
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-25-6)   "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-25-7)   "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-25-8)    "tokenUsage": {
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-25-9)     "completionTokens": 47,
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-25-10)     "promptTokens": 115,
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-25-11)     "totalTokens": 162
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-25-12)    },
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-25-13)    "finish_reason": "eos"
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-25-14)   },
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-25-15)   "tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-25-16)   "invalid_tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-25-17)   "usage_metadata": {
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-25-18)    "input_tokens": 115,
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-25-19)    "output_tokens": 47,
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-25-20)    "total_tokens": 162
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-25-21)   }
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-25-22)  },
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-25-23)  nextRepresentative: 'TECHNICAL'
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-25-24) }
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-25-25)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-25-26){
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-25-27) technical_support: {
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-25-28)  messages: AIMessage {
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-25-29)   "id": "8beb66986df91701-SJC",
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-25-30)   "content": "Sorry to hear that. Water damage can be a real challenge. Let's try to troubleshoot the issue.\n\nCan you tell me:\n\n1. How long was the computer submerged in water?\n2. Did you turn it off before it got wet, or was it on at the time?\n3. Have you tried unplugging the power cord and pressing the power button for 30 seconds to discharge any residual power?\n\nThis will help me narrow down the possible causes and suggest the next steps.",
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-25-31)   "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-25-32)   "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-25-33)    "tokenUsage": {
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-25-34)     "completionTokens": 99,
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-25-35)     "promptTokens": 70,
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-25-36)     "totalTokens": 169
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-25-37)    },
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-25-38)    "finish_reason": "eos"
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-25-39)   },
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-25-40)   "tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-25-41)   "invalid_tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-25-42)   "usage_metadata": {
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-25-43)    "input_tokens": 70,
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-25-44)    "output_tokens": 99,
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-25-45)    "total_tokens": 169
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-25-46)   }
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-25-47)  }
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-25-48) }
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-25-49)}

```


[Click here to see a LangSmith trace of the above run](https://smith.langchain.com/public/d131f6ea-e8d6-41f2-addd-fd9b55c6e057/r)

We can see the query gets correctly routed to the technical support node!

Finally, let's try a simple conversational response:

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-26-1)constconversationalStream=awaitgraph.stream({
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-26-2)messages:[{
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-26-3)role:"user",
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-26-4)content:"How are you? I'm Cobb."
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-26-5)}]
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-26-6)},{
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-26-7)configurable:{
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-26-8)thread_id:"conversational_testing_id"
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-26-9)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-26-10)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-26-11)
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-26-12)forawait(constvalueofconversationalStream){
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-26-13)console.log(value);
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-26-14)}

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-27-1){
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-27-2) initial_support: {
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-27-3)  messages: AIMessage {
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-27-4)   "id": "8beb6712294915e3-SJC",
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-27-5)   "content": "Hi Cobb! I'm doing great, thanks for asking. How can I help you today? Are you looking to purchase a new computer or just have a question about our products?",
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-27-6)   "additional_kwargs": {},
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-27-7)   "response_metadata": {
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-27-8)    "tokenUsage": {
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-27-9)     "completionTokens": 37,
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-27-10)     "promptTokens": 108,
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-27-11)     "totalTokens": 145
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-27-12)    },
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-27-13)    "finish_reason": "eos"
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-27-14)   },
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-27-15)   "tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-27-16)   "invalid_tool_calls": [],
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-27-17)   "usage_metadata": {
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-27-18)    "input_tokens": 108,
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-27-19)    "output_tokens": 37,
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-27-20)    "total_tokens": 145
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-27-21)   }
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-27-22)  },
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-27-23)  nextRepresentative: 'RESPOND'
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-27-24) }
[](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__codelineno-27-25)}

```


And we can see that the `initial_support` node handles it by itself, with no routing to technical or billing support. 

[Click here to see a LangSmith trace of the above run](https://smith.langchain.com/public/4cf5ff90-b9c6-4628-989f-28cb0c4910db/r)

## Further reading[¶](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#further-reading "Permanent link")

You may have noticed that the response from each node adds a message to the history in the state, and that as a result we end up with multiple assistant messages in a row corresponding to the different customer support personas the LLM takes on.

With `MessagesAnnotation`, it is possible to trim this state by returning a **message modifier** containing the same `id` as the message you want to remove. [See this guide](https://langchain-ai.github.io/langgraphjs/how-tos/delete-messages/) for more.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  Cloud Deploy  ](https://langchain-ai.github.io/langgraphjs/cloud/quick_start/) [ Next  LangGraph Retrieval Agent  ](https://langchain-ai.github.io/langgraphjs/tutorials/rag/langgraph_agentic_rag/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/tutorials/chatbots/customer_support_small_model/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
