---
url: https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#how-to-integrate-langgraph-into-your-react-application)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

How to integrate LangGraph into your React application 

[ ](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/?q= "Share")

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
          * [ Application Structure  ](https://langchain-ai.github.io/langgraph/how-tos#application-structure)
          * [ Deployment  ](https://langchain-ai.github.io/langgraph/how-tos#deployment)
          * [ Authentication & Access Control  ](https://langchain-ai.github.io/langgraph/how-tos#authentication-access-control)
          * [ Assistants  ](https://langchain-ai.github.io/langgraph/how-tos#assistants)
          * [ Threads  ](https://langchain-ai.github.io/langgraph/how-tos#threads)
          * [ Runs  ](https://langchain-ai.github.io/langgraph/how-tos#runs)
          * Streaming  Streaming 
            * [ Streaming  ](https://langchain-ai.github.io/langgraph/how-tos#streaming_1)
            * [ How to stream full state of your graph  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_values/)
            * [ How to stream state updates of your graph  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_updates/)
            * [ How to stream messages from your graph  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_messages/)
            * [ How to stream events  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_events/)
            * [ How to stream debug events  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_debug/)
            * [ How to configure multiple streaming modes at the same time  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_multiple/)
            * How to integrate LangGraph into your React application  [ How to integrate LangGraph into your React application  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/) Table of contents 
              * [ Example  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#example)
              * [ Customizing Your UI  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#customizing-your-ui)
                * [ Loading States  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#loading-states)
                * [ Thread Management  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#thread-management)
                * [ Messages Handling  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#messages-handling)
                * [ Branching Support  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#branching-support)
                * [ TypeScript  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#typescript)
              * [ Event Handling  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#event-handling)
              * [ Learn More  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#learn-more)
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

  * [ Example  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#example)
  * [ Customizing Your UI  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#customizing-your-ui)
    * [ Loading States  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#loading-states)
    * [ Thread Management  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#thread-management)
    * [ Messages Handling  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#messages-handling)
    * [ Branching Support  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#branching-support)
    * [ TypeScript  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#typescript)
  * [ Event Handling  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#event-handling)
  * [ Learn More  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#learn-more)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ How-to Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  4. [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/how-tos#langgraph-platform)
  5. [ Streaming  ](https://langchain-ai.github.io/langgraph/how-tos#streaming_1)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/cloud/how-tos/use_stream_react.md "Edit this page")

# How to integrate LangGraph into your React application[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#how-to-integrate-langgraph-into-your-react-application "Permanent link")

Prerequisites

  * [LangGraph Platform](https://langchain-ai.github.io/langgraph/concepts/langgraph_platform/)
  * [LangGraph Server](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/)



The `useStream()` React hook provides a seamless way to integrate LangGraph into your React applications. It handles all the complexities of streaming, state management, and branching logic, letting you focus on building great chat experiences.

Key features:

  * Messages streaming: Handle a stream of message chunks to form a complete message
  * Automatic state management for messages, loading states, and errors
  * Conversation branching: Create alternate conversation paths from any point in the chat history
  * UI-agnostic design - bring your own components and styling



Let's explore how to use `useStream()` in your React application.

The `useStream()` provides a solid foundation for creating bespoke chat experiences. For pre-built chat components and interfaces, we recommend checking out [CopilotKit](https://docs.copilotkit.ai/coagents/quickstart/langgraph) and [assistant-ui](https://github.com/langchain-ai/assistant-ui).

## Example[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#example "Permanent link")

```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-0-1)"use client";
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-0-2)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-0-3)import{useStream}from"@langchain/langgraph-sdk/react";
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-0-4)importtype{Message}from"@langchain/langgraph-sdk";
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-0-5)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-0-6)exportdefaultfunctionApp(){
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-0-7)constthread=useStream<{messages:Message[]}>({
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-0-8)apiUrl:"http://localhost:2024",
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-0-9)assistantId:"agent",
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-0-10)messagesKey:"messages",
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-0-11)});
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-0-12)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-0-13)return(
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-0-14)<div>
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-0-15)<div>
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-0-16){thread.messages.map((message)=>(
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-0-17)<divkey={message.id}>{message.contentasstring}</div>
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-0-18)))}
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-0-19)</div>
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-0-20)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-0-21)<form
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-0-22)onSubmit={(e)=>{
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-0-23)e.preventDefault();
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-0-24)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-0-25)constform=e.targetasHTMLFormElement;
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-0-26)constmessage=newFormData(form).get("message")asstring;
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-0-27)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-0-28)form.reset();
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-0-29)thread.submit({messages:[{type:"human",content:message}]});
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-0-30)}}
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-0-31)>
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-0-32)<inputtype="text"name="message"/>
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-0-33)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-0-34){thread.isLoading?(
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-0-35)<buttonkey="stop"type="button"onClick={()=>thread.stop()}>
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-0-36)Stop
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-0-37)</button>
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-0-38)):(
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-0-39)<buttonkey="submit"type="submit">
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-0-40)Send
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-0-41)</button>
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-0-42))}
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-0-43)</form>
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-0-44)</div>
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-0-45));
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-0-46)}

```


## Customizing Your UI[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#customizing-your-ui "Permanent link")

The `useStream()` hook takes care of all the complex state management behind the scenes, providing you with simple interfaces to build your UI. Here's what you get out of the box:

  * Thread state management
  * Loading and error states
  * Message handling and updates
  * Branching support



Here are some examples on how to use these features effectively:

### Loading States[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#loading-states "Permanent link")

The `isLoading` property tells you when a stream is active, enabling you to:

  * Show a loading indicator
  * Disable input fields during processing
  * Display a cancel button



```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-1-1)exportdefaultfunctionApp(){
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-1-2)const{isLoading,stop}=useStream<{messages:Message[]}>({
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-1-3)apiUrl:"http://localhost:2024",
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-1-4)assistantId:"agent",
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-1-5)messagesKey:"messages",
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-1-6)});
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-1-7)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-1-8)return(
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-1-9)<form>
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-1-10){isLoading&&(
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-1-11)<buttonkey="stop"type="button"onClick={()=>stop()}>
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-1-12)Stop
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-1-13)</button>
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-1-14))}
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-1-15)</form>
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-1-16));
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-1-17)}

```


### Thread Management[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#thread-management "Permanent link")

Keep track of conversations with built-in thread management. You can access the current thread ID and get notified when new threads are created:

```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-2-1)const[threadId,setThreadId]=useState<string|null>(null);
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-2-2)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-2-3)constthread=useStream<{messages:Message[]}>({
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-2-4)apiUrl:"http://localhost:2024",
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-2-5)assistantId:"agent",
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-2-6)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-2-7)threadId:threadId,
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-2-8)onThreadId:setThreadId,
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-2-9)});

```


We recommend storing the `threadId` in your URL's query parameters to let users resume conversations after page refreshes.

### Messages Handling[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#messages-handling "Permanent link")

To enable messages handling, you need to pass the `messagesKey` option to the `useStream()` hook. 

When enabled, the `useStream()` hook will keep track of the message chunks received from the server and concatenate them together to form a complete message. The completed message chunks can be retrieved via the `messages` property.

```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-3-1)importtype{Message}from"@langchain/langgraph-sdk";
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-3-2)import{useStream}from"@langchain/langgraph-sdk/react";
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-3-3)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-3-4)exportdefaultfunctionHomePage(){
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-3-5)constthread=useStream<{messages:Message[]}>({
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-3-6)apiUrl:"http://localhost:2024",
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-3-7)assistantId:"agent",
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-3-8)messagesKey:"messages",
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-3-9)});
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-3-10)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-3-11)return(
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-3-12)<div>
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-3-13){thread.messages.map((message)=>(
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-3-14)<divkey={message.id}>{message.contentasstring}</div>
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-3-15)))}
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-3-16)</div>
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-3-17));
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-3-18)}

```


### Branching Support[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#branching-support "Permanent link")

To enable branching, you need to enable messages handling. Pass the `messagesKey` option to the `useStream()` hook. For each message, you can use `getMessagesMetadata()` to get the first checkpoint from which the message has been first seen. You can then create a new run from the checkpoint preceding the first seen checkpoint to create a new branch in a thread.

A branch can be created in following ways:

  1. Edit a previous user message.
  2. Request a regeneration of a previous assistant message.



```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-1)/* eslint-disable @typescript-eslint/no-floating-promises */
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-2)"use client";
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-3)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-4)importtype{Message}from"@langchain/langgraph-sdk";
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-5)import{useStream}from"@langchain/langgraph-sdk/react";
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-6)import{
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-7)Annotation,
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-8)MessagesAnnotation,
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-9)typeStateType,
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-10)typeUpdateType,
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-11)}from"@langchain/langgraph/web";
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-12)import{useState}from"react";
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-13)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-14)constAgentState=Annotation.Root({
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-15)...MessagesAnnotation.spec,
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-16)});
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-17)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-18)functionBranchSwitcher({
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-19)branch,
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-20)branchOptions,
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-21)onSelect,
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-22)}:{
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-23)branch:string|undefined;
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-24)branchOptions:string[]|undefined;
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-25)onSelect:(branch:string)=>void;
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-26)}){
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-27)if(!branchOptions||!branch)returnnull;
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-28)constindex=branchOptions.indexOf(branch);
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-29)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-30)return(
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-31)<divclassName="flex items-center gap-2">
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-32)<button
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-33)type="button"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-34)onClick={()=>{
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-35)constprevBranch=branchOptions[index-1];
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-36)if(!prevBranch)return;
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-37)onSelect(prevBranch);
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-38)}}
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-39)>
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-40)Prev
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-41)</button>
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-42)<span>
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-43){index+1}/{branchOptions.length}
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-44)</span>
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-45)<button
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-46)type="button"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-47)onClick={()=>{
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-48)constnextBranch=branchOptions[index+1];
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-49)if(!nextBranch)return;
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-50)onSelect(nextBranch);
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-51)}}
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-52)>
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-53)Next
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-54)</button>
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-55)</div>
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-56));
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-57)}
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-58)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-59)functionEditMessage({
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-60)message,
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-61)onEdit,
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-62)}:{
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-63)message:Message;
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-64)onEdit:(message:Message)=>void;
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-65)}){
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-66)const[editing,setEditing]=useState(false);
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-67)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-68)if(!editing){
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-69)return(
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-70)<buttontype="button"onClick={()=>setEditing(true)}>
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-71)Edit
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-72)</button>
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-73));
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-74)}
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-75)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-76)return(
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-77)<form
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-78)onSubmit={(e)=>{
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-79)e.preventDefault();
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-80)constform=e.targetasHTMLFormElement;
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-81)constcontent=newFormData(form).get("content")asstring;
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-82)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-83)form.reset();
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-84)onEdit({type:"human",content});
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-85)setEditing(false);
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-86)}}
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-87)>
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-88)<inputname="content"defaultValue={message.contentasstring}/>
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-89)<buttontype="submit">Save</button>
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-90)</form>
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-91));
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-92)}
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-93)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-94)exportdefaultfunctionApp(){
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-95)constthread=useStream<
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-96)StateType<typeofAgentState.spec>,
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-97)UpdateType<typeofAgentState.spec>
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-98)>({
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-99)apiUrl:"http://localhost:2024",
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-100)assistantId:"agent",
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-101)messagesKey:"messages",
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-102)});
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-103)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-104)return(
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-105)<div>
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-106)<div>
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-107){thread.messages.map((message)=>{
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-108)constmeta=thread.getMessagesMetadata(message);
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-109)constparentCheckpoint=meta?.firstSeenState?.parent_checkpoint;
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-110)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-111)return(
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-112)<divkey={message.id}>
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-113)<div>{message.contentasstring}</div>
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-114)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-115){message.type==="human"&&(
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-116)<EditMessage
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-117)message={message}
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-118)onEdit={(message)=>
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-119)thread.submit(
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-120){messages:[message]},
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-121){checkpoint:parentCheckpoint}
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-122))
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-123)}
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-124)/>
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-125))}
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-126)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-127){message.type==="ai"&&(
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-128)<button
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-129)type="button"
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-130)onClick={()=>
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-131)thread.submit(undefined,{checkpoint:parentCheckpoint})
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-132)}
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-133)>
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-134)<span>Regenerate</span>
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-135)</button>
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-136))}
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-137)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-138)<BranchSwitcher
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-139)branch={meta?.branch}
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-140)branchOptions={meta?.branchOptions}
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-141)onSelect={(branch)=>thread.setBranch(branch)}
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-142)/>
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-143)</div>
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-144));
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-145)})}
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-146)</div>
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-147)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-148)<form
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-149)onSubmit={(e)=>{
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-150)e.preventDefault();
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-151)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-152)constform=e.targetasHTMLFormElement;
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-153)constmessage=newFormData(form).get("message")asstring;
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-154)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-155)form.reset();
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-156)thread.submit({messages:[message]});
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-157)}}
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-158)>
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-159)<inputtype="text"name="message"/>
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-160)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-161){thread.isLoading?(
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-162)<buttonkey="stop"type="button"onClick={()=>thread.stop()}>
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-163)Stop
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-164)</button>
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-165)):(
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-166)<buttonkey="submit"type="submit">
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-167)Send
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-168)</button>
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-169))}
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-170)</form>
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-171)</div>
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-172));
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-4-173)}

```


### TypeScript[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#typescript "Permanent link")

The `useStream()` hook is fully typed to help catch errors early and provide better IDE support. You can specify types for:

  * State shape
  * Update format
  * Custom events



```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-5-1)// Define your types
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-5-2)typeState={
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-5-3)messages:Message[];
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-5-4)context?:Record<string,unknown>;
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-5-5)};
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-5-6)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-5-7)typeUpdate={
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-5-8)messages:Message[]|Message;
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-5-9)context?:Record<string,unknown>;
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-5-10)};
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-5-11)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-5-12)typeCustomEvent={
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-5-13)type:"progress"|"debug";
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-5-14)payload:unknown;
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-5-15)};
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-5-16)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-5-17)// Use them with the hook
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-5-18)constthread=useStream<State,Update,CustomEvent>({
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-5-19)apiUrl:"http://localhost:2024",
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-5-20)assistantId:"agent",
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-5-21)messagesKey:"messages",
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-5-22)});

```


If you're using LangGraph.js, you can reuse your graph's annotation types:

```
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-6-1)import{
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-6-2)Annotation,
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-6-3)MessagesAnnotation,
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-6-4)typeStateType,
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-6-5)typeUpdateType,
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-6-6)}from"@langchain/langgraph/web";
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-6-7)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-6-8)constAgentState=Annotation.Root({
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-6-9)...MessagesAnnotation.spec,
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-6-10)context:Annotation.Optional(Annotation.Any()),
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-6-11)});
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-6-12)
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-6-13)constthread=useStream<
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-6-14)StateType<typeofAgentState.spec>,
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-6-15)UpdateType<typeofAgentState.spec>
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-6-16)>({
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-6-17)apiUrl:"http://localhost:2024",
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-6-18)assistantId:"agent",
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-6-19)messagesKey:"messages",
[](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__codelineno-6-20)});

```


## Event Handling[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#event-handling "Permanent link")

The `useStream()` hook provides several callback options to help you respond to different events:

  * `onError`: Called when an error occurs.
  * `onFinish`: Called when the stream is finished.
  * `onUpdateEvent`: Called when an update event is received.
  * `onCustomEvent`: Called when a custom event is received. See [Custom events](https://langchain-ai.github.io/langgraph/concepts/streaming/#custom) to learn how to stream custom events.
  * `onMetadataEvent`: Called when a metadata event is received.



## Learn More[¶](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#learn-more "Permanent link")

  * [JS/TS SDK Reference](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/)

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  How to configure multiple streaming modes at the same time  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/stream_multiple/) [ Next  How to Add Breakpoints  ](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
