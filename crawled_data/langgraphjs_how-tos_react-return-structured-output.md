---
url: https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#how-to-return-structured-output-from-the-prebuilt-react-agent)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

How to return structured output from the prebuilt ReAct agent 

[ ](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/?q= "Share")

Initializing search 

[ GitHub  ](https://github.com/langchain-ai/langgraphjs "Go to repository")

  * [ Home ](https://langchain-ai.github.io/langgraphjs/)
  * [ API reference ](https://langchain-ai.github.io/langgraphjs/reference/)
  * [ Versions ](https://langchain-ai.github.io/langgraphjs/versions/)



[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

[ GitHub  ](https://github.com/langchain-ai/langgraphjs "Go to repository")

  * [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  * [ API reference  ](https://langchain-ai.github.io/langgraphjs/reference/)
  * [ Versions  ](https://langchain-ai.github.io/langgraphjs/versions/)



Table of contents 

  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#setup)
  * [ Code  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#code)
  * [ Usage  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#usage)
    * [ Customizing system prompt  ](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#customizing-system-prompt)



# How to return structured output from the prebuilt ReAct agent[¶](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#how-to-return-structured-output-from-the-prebuilt-react-agent "Permanent link")

Prerequisites

  * [Agent Architectures](https://langchain-ai.github.io/langgraphjs/concepts/agentic_concepts/)
  * [Chat Models](https://python.langchain.com/docs/concepts/chat_models/)
  * [Tools](https://python.langchain.com/docs/concepts/tools/)
  * [Structured Output](https://python.langchain.com/docs/concepts/structured_outputs/)



To return structured output from the prebuilt ReAct agent you can provide a response_format parameter with the desired output schema to `createReactAgent`[](https://langchain-ai.github.io/langgraphjs/reference/functions/prebuilt.createReactAgent.html):

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-0-1)import{z}from"zod";
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-0-2)import{createReactAgent}from"@langchain/langgraph/prebuilt";
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-0-3)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-0-4)constresponseFormat=z.object({
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-0-5)// Respond to the user in this format
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-0-6)mySpecialOutput:z.string(),
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-0-7)})
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-0-8)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-0-9)constgraph=createReactAgent({
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-0-10)llm:llm,
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-0-11)tools:tools,
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-0-12)// specify the schema for the structured output using `responseFormat` parameter
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-0-13)responseFormat:responseFormat
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-0-14)})

```


The agent will return the output in the format specified by the `responseFormat` schema by making an additional LLM call at the end of the conversation, once there are no more tool calls to be made. You can read [this guide](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/respond-in-format) to learn about an alternate way - treating the structured output as another tool = to achieve structured output from the agent.

## Setup[¶](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#setup "Permanent link")

First, we need to install the required packages.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-1-1)yarnadd@langchain/langgraph@langchain/openai@langchain/corezod

```


This guide will use OpenAI's GPT-4o model. We will optionally set our API key for [LangSmith tracing](https://smith.langchain.com/), which will give us best-in-class observability.

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-2-1)// process.env.OPENAI_API_KEY = "sk_...";
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-2-2)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-2-3)// Optional, add tracing in LangSmith
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-2-4)// process.env.LANGSMITH_API_KEY = "ls__..."
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-2-5)process.env.LANGSMITH_TRACING="true";
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-2-6)process.env.LANGSMITH_PROJECT="ReAct Agent with system prompt: LangGraphJS";

```


## Code[¶](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#code "Permanent link")

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-3-1)import{ChatOpenAI}from"@langchain/openai";
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-3-2)import{createReactAgent}from"@langchain/langgraph/prebuilt";
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-3-3)import{tool}from"@langchain/core/tools";
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-3-4)import{z}from"zod";
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-3-5)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-3-6)constweatherTool=tool(
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-3-7)async(input):Promise<string>=>{
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-3-8)if(input.city==="nyc"){
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-3-9)return"It might be cloudy in nyc";
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-3-10)}elseif(input.city==="sf"){
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-3-11)return"It's always sunny in sf";
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-3-12)}else{
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-3-13)thrownewError("Unknown city");
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-3-14)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-3-15)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-3-16){
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-3-17)name:"get_weather",
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-3-18)description:"Use this to get weather information.",
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-3-19)schema:z.object({
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-3-20)city:z.enum(["nyc","sf"]).describe("The city to get weather for"),
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-3-21)}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-3-22)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-3-23));
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-3-24)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-3-25)constWeatherResponseSchema=z.object({
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-3-26)conditions:z.string().describe("Weather conditions"),
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-3-27)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-3-28)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-3-29)consttools=[weatherTool];
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-3-30)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-3-31)constagent=createReactAgent({
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-3-32)llm:newChatOpenAI({model:"gpt-4o",temperature:0}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-3-33)tools:tools,
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-3-34)responseFormat:WeatherResponseSchema,
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-3-35)});

```


## Usage[¶](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#usage "Permanent link")

Let's now test our agent:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-4-1)constresponse=awaitagent.invoke({
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-4-2)messages:[
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-4-3){
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-4-4)role:"user",
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-4-5)content:"What's the weather in NYC?",
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-4-6)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-4-7)],
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-4-8)})

```


You can see that the agent output contains a `structuredResponse` key with the structured output conforming to the specified `WeatherResponse` schema, in addition to the message history under `messages` key

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-5-1)response.structuredResponse

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-6-1){ conditions: 'cloudy' }

```


### Customizing system prompt[¶](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#customizing-system-prompt "Permanent link")

You might need to further customize the second LLM call for the structured output generation and provide a system prompt. To do so, you can pass an object with the keys `prompt`, `schema` to the `responseFormat` parameter:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-7-1)constagent=createReactAgent({
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-7-2)llm:newChatOpenAI({model:"gpt-4o",temperature:0}),
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-7-3)tools:tools,
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-7-4)responseFormat:{
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-7-5)prompt:"Always return capitalized weather conditions",
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-7-6)schema:WeatherResponseSchema,
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-7-7)}
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-7-8)});
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-7-9)
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-7-10)constresponse=awaitagent.invoke({
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-7-11)messages:[
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-7-12){
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-7-13)role:"user",
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-7-14)content:"What's the weather in NYC?",
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-7-15)},
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-7-16)],
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-7-17)})

```


You can verify that the structured response now contains a capitalized value:

```
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-8-1)response.structuredResponse

```


```
[](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__codelineno-9-1){ conditions: 'Cloudy' }

```


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top 

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/how-tos/react-return-structured-output/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
