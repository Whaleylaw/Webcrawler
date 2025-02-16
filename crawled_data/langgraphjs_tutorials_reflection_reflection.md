---
url: https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#reflection)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

Reflection 

[ ](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/?q= "Share")

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
            * Reflection  [ Reflection  ](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/) Table of contents 
              * [ Prerequisites  ](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#prerequisites)
              * [ Setup  ](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#setup)
                * [ Load env vars  ](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#load-env-vars)
              * [ Generate  ](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#generate)
                * [ Reflect  ](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#reflect)
                * [ Repeat  ](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#repeat)
              * [ Define graph  ](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#define-graph)
                * [ See the LangSmith trace here  ](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#see-the-langsmith-trace-here)
            * [ Reasoning without Observation  ](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/)
        * [ Evaluation & Analysis  ](https://langchain-ai.github.io/langgraphjs/tutorials#evaluation)
    * Resources  Resources 
      * [ Adopters  ](https://langchain-ai.github.io/langgraphjs/adopters/)
      * [ FAQ  ](https://langchain-ai.github.io/langgraphjs/concepts/faq/)
      * [ Troubleshooting  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraphjs/reference/)
  * [ Versions  ](https://langchain-ai.github.io/langgraphjs/versions/)



Table of contents 

  * [ Prerequisites  ](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#prerequisites)
  * [ Setup  ](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#setup)
    * [ Load env vars  ](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#load-env-vars)
  * [ Generate  ](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#generate)
    * [ Reflect  ](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#reflect)
    * [ Repeat  ](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#repeat)
  * [ Define graph  ](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#define-graph)
    * [ See the LangSmith trace here  ](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#see-the-langsmith-trace-here)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ Tutorials  ](https://langchain-ai.github.io/langgraphjs/tutorials/)
  4. [ Agent Architectures  ](https://langchain-ai.github.io/langgraphjs/tutorials#agent-architectures)
  5. [ Reflection & Critique  ](https://langchain-ai.github.io/langgraphjs/tutorials#reflection-critique)



# Reflection[¶](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#reflection "Permanent link")

In the context of LLM agent building, reflection refers to the process of prompting an LLM to observe its past steps (along with potential observations from tools/the environment) to assess the quality of the chosen actions. This is then used downstream for things like re-planning, search, or evaluation.

![Reflection](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/img/reflection.png)

This notebook demonstrates a very simple form of reflection in LangGraph.

#### Prerequisites[¶](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#prerequisites "Permanent link")

We will be using a basic agent with a search tool here.

## Setup[¶](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#setup "Permanent link")

### Load env vars[¶](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#load-env-vars "Permanent link")

Add a `.env` variable in the root of the repo folder with your variables.

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-0-1)import"dotenv/config";

```


## Generate[¶](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#generate "Permanent link")

For our example, we will create a "5 paragraph essay" generator. First, create the generator:

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-1-1)import{ChatFireworks}from"@langchain/community/chat_models/fireworks";
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-1-2)import{
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-1-3)ChatPromptTemplate,
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-1-4)MessagesPlaceholder,
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-1-5)}from"@langchain/core/prompts";
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-1-6)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-1-7)constprompt=ChatPromptTemplate.fromMessages([
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-1-8)[
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-1-9)"system",
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-1-10)`You are an essay assistant tasked with writing excellent 5-paragraph essays.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-1-11)Generate the best essay possible for the user's request. 
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-1-12)If the user provides critique, respond with a revised version of your previous attempts.`,
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-1-13)],
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-1-14)newMessagesPlaceholder("messages"),
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-1-15)]);
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-1-16)constllm=newChatFireworks({
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-1-17)model:"accounts/fireworks/models/firefunction-v2",
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-1-18)temperature:0,
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-1-19)modelKwargs:{
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-1-20)max_tokens:32768,
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-1-21)},
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-1-22)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-1-23)constessayGenerationChain=prompt.pipe(llm);

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-2-1)import{AIMessage,BaseMessage,HumanMessage}from"@langchain/core/messages";
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-2-2)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-2-3)letessay="";
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-2-4)constrequest=newHumanMessage({
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-2-5)content:
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-2-6)"Write an essay on why the little prince is relevant in modern childhood",
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-2-7)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-2-8)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-2-9)forawait(
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-2-10)constchunkofawaitessayGenerationChain.stream({
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-2-11)messages:[request],
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-2-12)})
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-2-13)){
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-2-14)console.log(chunk.content);
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-2-15)essay+=chunk.content;
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-2-16)}

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-1)The Little
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-2) Prince, a
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-3) novella written
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-4) by Antoine de
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-5) Saint-Ex
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-6)upéry in
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-7) 1943
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-8), has been
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-9) a beloved classic
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-10) for generations of
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-11) children and adults
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-12) alike. Despite
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-13) being written over
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-14) 80 years
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-15) ago,
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-16) the story
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-17) remains remarkably
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-18) relevant to modern
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-19) childhood. This
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-20) essay will explore
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-21) the ways in
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-22) which The Little
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-23) Prince continues to
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-24) resonate with
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-25) children today,
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-26) highlighting its timeless
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-27) themes, rel
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-28)atable characters,
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-29) and poignant commentary
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-30) on the
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-31) human experience.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-32)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-33)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-34)One of the
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-35) primary reasons The
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-36) Little Prince remains
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-37) relevant is its
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-38) exploration of universal
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-39) themes that transcend
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-40) time and culture
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-41). The story
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-42) delves into
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-43) complex emotions such
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-44) as loneliness,
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-45) friendship, and
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-46) the importance of
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-47) human connection.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-48) These themes are
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-49) just as relevant
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-50) today as
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-51) they were
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-52) when the
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-53) book was first
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-54) published. Children
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-55) today face many
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-56) of the same
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-57) challenges as the
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-58) Little Prince,
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-59) including feeling isolated
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-60) and struggling to
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-61) form meaningful relationships
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-62). The nov
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-63)ella's exploration
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-64) of these themes
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-65) provides a rel
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-66)atable and comforting
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-67) narrative for young
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-68) readers.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-69)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-70)The
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-71) characters in The
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-72) Little Prince are
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-73) also remarkably rel
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-74)atable to modern
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-75) children. The
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-76) Little Prince himself
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-77) is a curious
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-78) and adventurous young
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-79) boy who embodies
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-80) the
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-81) sense of
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-82) wonder and
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-83) curiosity that
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-84) defines childhood
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-85). His
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-86) relationships with the
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-87) various characters
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-88) he encounters
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-89) on
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-90) his journey
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-91), including
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-92) the fox and
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-93) the rose,
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-94) serve as powerful
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-95) reminders of the
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-96) importance of empathy
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-97), kindness,
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-98) and understanding.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-99) These characters,
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-100) along with the
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-101) Little Prince,
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-102) provide a diverse
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-103) and inclusive cast
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-104) that reflects the
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-105) complexity of modern
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-106) childhood.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-107)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-108)Furthermore
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-109), The Little
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-110) Prince offers a
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-111) poignant commentary on
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-112) the human experience
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-113) that is just
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-114) as relevant today
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-115) as it was
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-116) when the book
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-117) was first
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-118) published.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-119) The novella
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-120)'s exploration
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-121) of the adult
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-122) world,
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-123) with its
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-124) emphasis on material
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-125) possessions and superficial
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-126) relationships, serves
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-127) as a powerful
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-128) critique of modern
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-129) society. The
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-130) Little Prince
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-131)'s observations
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-132) on
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-133) the adult
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-134) world,
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-135) including his famous
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-136) line "You
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-137) see, grown
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-138)-ups never understand
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-139) anything by themselves
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-140), and it
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-141) is exhausting for
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-142) children
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-143) to be
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-144) always and
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-145) forever explaining things
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-146) to them,"
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-147) remain a
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-148) powerful commentary
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-149) on the challenges
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-150) of growing up
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-151) and navigating the
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-152) complexities of adulthood
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-153).
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-154)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-155)In conclusion
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-156), The Little
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-157) Prince remains a
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-158) remarkably relevant and
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-159) powerful work of
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-160) children's literature
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-161). Its exploration
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-162) of universal themes
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-163), relatable
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-164) characters, and
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-165) poignant commentary on
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-166) the human experience
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-167) make it a
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-168) must-read for
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-169) children today.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-170) As a work
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-171) of literature,
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-172) it continues to
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-173) inspire and comfort
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-174) young readers,
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-175) providing a powerful
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-176) reminder of the
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-177) importance of empathy
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-178), kindness,
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-179) and understanding
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-180). As a
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-181) cultural artifact,
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-182) it serves as
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-183) a powerful commentary
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-184) on the challenges
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-185) of growing up
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-186) and navigating the
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-187) complexities of modern
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-3-188) society.

```


### Reflect[¶](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#reflect "Permanent link")

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-4-1)constreflectionPrompt=ChatPromptTemplate.fromMessages([
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-4-2)[
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-4-3)"system",
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-4-4)`You are a teacher grading an essay submission.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-4-5)Generate critique and recommendations for the user's submission.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-4-6)Provide detailed recommendations, including requests for length, depth, style, etc.`,
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-4-7)],
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-4-8)newMessagesPlaceholder("messages"),
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-4-9)]);
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-4-10)constreflect=reflectionPrompt.pipe(llm);

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-5-1)letreflection="";
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-5-2)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-5-3)forawait(
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-5-4)constchunkofawaitreflect.stream({
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-5-5)messages:[request,newHumanMessage({content:essay})],
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-5-6)})
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-5-7)){
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-5-8)console.log(chunk.content);
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-5-9)reflection+=chunk.content;
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-5-10)}

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-1)The essay
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-2) provides a
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-3) good overview of
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-4) the relevance of
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-5) The Little Prince
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-6) in modern childhood
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-7). However,
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-8) there are some
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-9) areas that need
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-10) improvement. Firstly
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-11), the introduction
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-12) could be stronger
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-13). Instead of
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-14) simply stating that
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-15) the book is
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-16) a classic,
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-17) try to provide
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-18) a more nuanced
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-19) explanation of its
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-20) enduring popularity.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-21) Additionally, the
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-22) body paragraphs could
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-23) be more detailed
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-24) and provide more
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-25) specific examples from
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-26) the text to
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-27) support the arguments
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-28).
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-29)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-30)In terms
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-31) of style,
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-32) the writing is
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-33) clear and concise
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-34), but could
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-35) benefit from more
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-36) varied sentence structures
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-37) and vocabulary.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-38) The use of
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-39) transitions between paragraphs
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-40) could also be
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-41) improved to create
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-42) a
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-43) more cohesive
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-44) flow.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-45)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-46)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-47)One area that
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-48) could be explored
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-49) further is the
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-50) way in which
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-51) The Little Prince
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-52) reflects the experiences
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-53) of modern children
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-54). While the
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-55) essay touches on
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-56) this, it
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-57) could be developed
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-58) more fully to
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-59) provide
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-60) a more
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-61) nuanced understanding
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-62) of how the
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-63) book continues to
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-64) resonate with young
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-65) readers.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-66)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-67)Overall
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-68), the essay
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-69) provides a good
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-70) foundation for exploring
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-71) the relevance of
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-72) The Little Prince
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-73) in modern childhood
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-74). With some
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-75) revisions to address
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-76) the areas mentioned
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-77) above, it
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-78) could be even
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-79) stronger.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-80)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-81)Grade
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-82): B
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-83)+
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-84)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-85)Recommendations
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-86):
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-87)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-88)* Rev
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-89)ise the introduction
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-90) to provide a
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-91) more nuanced explanation
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-92) of the book
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-93)'s enduring popularity
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-94).
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-95)* Provide
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-96) more specific examples
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-97) from the text
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-98) to support the
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-99) arguments
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-100) in the
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-101) body paragraphs
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-102).
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-103)* V
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-104)ary sentence structures
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-105) and vocabulary to
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-106) create a more
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-107) engaging writing style
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-108).
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-109)* Explore
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-110) the way in
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-111) which The Little
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-112) Prince reflects the
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-113) experiences of modern
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-114) children in more
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-115) detail.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-116)*
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-117) Improve transitions between
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-118) paragraphs to create
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-119) a more cohesive
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-120) flow.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-121)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-122)Length
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-123): The essay
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-124) is a good
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-125) length, but
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-126) could be expanded
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-127) to provide more
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-128) detail and examples
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-129).
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-130)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-131)Depth:
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-132) The essay provides
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-133) a good overview
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-134) of the relevance
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-135) of The Little
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-136) Prince, but
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-137) could delve deeper
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-138) into the themes
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-139) and characters to
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-140) provide a more
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-141) nuanced understanding.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-142)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-143)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-144)Style: The
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-145) writing is clear
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-146) and concise
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-147),
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-148) but could
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-149) benefit from
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-150) more varied sentence
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-151) structures and vocabulary
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-152).
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-153)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-154)Overall
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-155), the essay
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-156) provides a good
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-157) foundation for exploring
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-158) the relevance of
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-159) The Little Prince
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-160) in modern childhood
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-161). With some
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-162) revisions to address
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-163) the areas mentioned
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-164) above, it
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-165) could be even
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-6-166) stronger.

```


### Repeat[¶](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#repeat "Permanent link")

And... that's all there is too it! You can repeat in a loop for a fixed number of steps, or use an LLM (or other check) to decide when the finished product is good enough.

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-7-1)letstream=awaitessayGenerationChain.stream({
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-7-2)messages:[
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-7-3)request,
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-7-4)newAIMessage({content:essay}),
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-7-5)newHumanMessage({content:reflection}),
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-7-6)],
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-7-7)});
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-7-8)forawait(constchunkofstream){
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-7-9)console.log(chunk.content);
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-7-10)}

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-1)Here is
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-2) a revised
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-3) version of
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-4) the essay that
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-5) addresses the areas
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-6) mentioned above:
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-7)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-8)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-9)The Little Prince
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-10), a nov
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-11)ella written by
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-12) Antoine de Saint
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-13)-Exup
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-14)éry in 
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-15)1943,
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-16) has captivated
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-17) the hearts of
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-18) readers of all
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-19) ages with its
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-20) poignant and timeless
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-21) tale of friendship
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-22), love,
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-23) and the human
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-24) experience. One
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-25) of the primary
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-26) reasons for its enduring
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-27) popularity is its
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-28) ability to tap
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-29) into the universal
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-30) emotions and experiences
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-31) that define childhood
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-32). The story
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-33)'s exploration of
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-34) complex themes such
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-35) as loneliness,
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-36) friendship, and
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-37) the importance of
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-38) human connection reson
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-39)ates deeply with
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-40) children today,
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-41) who face many
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-42) of the same
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-43) challenges as the
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-44) Little Prince.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-45)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-46)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-47)One of the
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-48) most relatable
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-49) aspects of
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-50) The Little
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-51) Prince is
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-52) its
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-53) exploration of
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-54) the complexities
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-55) of human relationships
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-56). The Little
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-57) Prince's journey
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-58) to different planets
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-59), where he
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-60) encounters various strange
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-61) characters,
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-62) serves as
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-63) a powerful metaphor
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-64) for the challenges
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-65) of forming meaningful
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-66) connections with others
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-67). For example
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-68), his relationship
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-69) with the fox
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-70), who teaches
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-71) him the importance
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-72) of human connection
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-73) and the value
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-74) of friendship,
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-75) is a powerful
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-76) reminder of the
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-77) importance of empathy
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-78) and understanding in
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-79) building strong relationships
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-80). This theme
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-81) is particularly relevant
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-82) in modern childhood
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-83), where children
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-84) are often encouraged
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-85) to focus on
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-86) individual achievement and
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-87) success, rather
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-88) than building strong
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-89) relationships with others
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-90).
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-91)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-92)Furthermore,
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-93) The Little Prince
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-94) offers a powerful
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-95) commentary on the
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-96) adult world,
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-97) which is just
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-98) as relevant today
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-99) as it was
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-100) when the book
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-101) was first published
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-102). The nov
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-103)ella's exploration
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-104) of the superficial
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-105)ity of adult
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-106) relationships, where
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-107) people are often
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-108) more concerned with
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-109) material possessions and
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-110) appearances than with
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-111) genuine human connection
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-112), serves as
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-113) a powerful critique
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-114) of modern society
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-115). The Little
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-116) Prince's observations
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-117) on the adult
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-118) world, including
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-119) his famous line
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-120) "You see
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-121), grown-ups
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-122) never understand anything
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-123) by themselves,
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-124) and it is
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-125) exhausting for children
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-126) to be always
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-127) and forever explaining
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-128) things to them
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-129)," remain a
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-130) powerful commentary on
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-131) the challenges of
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-132) growing up and
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-133) navigating the complexities
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-134) of adulthood.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-135)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-136)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-137)In addition to
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-138) its exploration of
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-139) universal themes and
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-140) relatable characters
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-141), The Little
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-142) Prince also reflects
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-143) the experiences of
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-144) modern children in
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-145) a number of
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-146) ways. For
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-147) example, the
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-148) Little Prince's
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-149) sense of wonder
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-150) and curiosity,
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-151) as well as
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-152) his desire for
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-153) adventure and exploration
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-154), are all
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-155) qualities that are
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-156) highly valued in
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-157) modern childhood.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-158) Furthermore, the
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-159) novella's
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-160) exploration of the
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-161) importance of human
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-162) connection and empathy
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-163) is particularly relevant
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-164) in modern childhood
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-165), where children
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-166) are often encouraged
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-167) to
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-168) focus on
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-169) individual achievement
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-170) and success,
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-171) rather than building strong
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-172) relationships with
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-173) others.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-174)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-175)In
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-176) conclusion,
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-177) The Little
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-178) Prince remains a
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-179) remarkably relevant and
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-180) powerful work of
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-181) children's literature
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-182). Its exploration
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-183) of universal themes
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-184), relatable
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-185) characters, and
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-186) poignant commentary on
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-187) the human experience
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-188) make it a
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-189) must-read for
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-190) children today.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-191) As a work
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-192) of literature
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-193), it
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-194) continues to inspire
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-195) and comfort young
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-196) readers, providing
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-197) a powerful reminder
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-198) of the importance
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-199) of empathy,
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-200) kindness, and
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-201) understanding. As
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-202) a cultural artifact
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-203), it serves
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-204) as a powerful
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-205) commentary on the
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-206) challenges of growing
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-207) up and navigating
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-208) the complexities of
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-8-209) modern society.

```


## Define graph[¶](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#define-graph "Permanent link")

Now that we've shown each step in isolation, we can wire it up in a graph.

```
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-1)import{END,MemorySaver,StateGraph,START,Annotation}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-2)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-3)// Define the top-level State interface
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-4)constState=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-5)messages:Annotation<BaseMessage[]>({
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-6)reducer:(x,y)=>x.concat(y),
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-7)})
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-8)})
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-9)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-10)constgenerationNode=async(state:typeofState.State)=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-11)const{messages}=state;
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-12)return{
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-13)messages:[awaitessayGenerationChain.invoke({messages})],
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-14)};
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-15)};
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-16)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-17)constreflectionNode=async(state:typeofState.State)=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-18)const{messages}=state;
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-19)// Other messages we need to adjust
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-20)constclsMap:{[key:string]:new(content:string)=>BaseMessage}={
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-21)ai:HumanMessage,
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-22)human:AIMessage,
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-23)};
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-24)// First message is the original user request. We hold it the same for all nodes
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-25)consttranslated=[
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-26)messages[0],
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-27)...messages
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-28).slice(1)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-29).map((msg)=>newclsMap[msg._getType()](msg.content.toString())),
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-30)];
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-31)constres=awaitreflect.invoke({messages:translated});
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-32)// We treat the output of this as human feedback for the generator
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-33)return{
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-34)messages:[newHumanMessage({content:res.content})],
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-35)};
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-36)};
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-37)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-38)// Define the graph
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-39)constworkflow=newStateGraph(State)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-40).addNode("generate",generationNode)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-41).addNode("reflect",reflectionNode)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-42).addEdge(START,"generate");
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-43)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-44)constshouldContinue=(state:typeofState.State)=>{
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-45)const{messages}=state;
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-46)if(messages.length>6){
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-47)// End state after 3 iterations
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-48)returnEND;
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-49)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-50)return"reflect";
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-51)};
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-52)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-53)workflow
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-54).addConditionalEdges("generate",shouldContinue)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-55).addEdge("reflect","generate");
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-56)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-9-57)constapp=workflow.compile({checkpointer:newMemorySaver()});

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-10-1)constcheckpointConfig={configurable:{thread_id:"my-thread"}};
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-10-2)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-10-3)stream=awaitapp.stream(
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-10-4){
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-10-5)messages:[
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-10-6)newHumanMessage({
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-10-7)content:
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-10-8)"Generate an essay on the topicality of The Little Prince and its message in modern life",
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-10-9)}),
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-10-10)]
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-10-11)},
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-10-12)checkpointConfig,
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-10-13));
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-10-14)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-10-15)forawait(consteventofstream){
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-10-16)for(const[key,_value]ofObject.entries(event)){
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-10-17)console.log(`Event: ${key}`);
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-10-18)// Uncomment to see the result of each step.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-10-19)// console.log(value.map((msg) => msg.content).join("\n"));
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-10-20)console.log("\n------\n");
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-10-21)}
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-10-22)}

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-11-1)Event: generate
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-11-2)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-11-3)------
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-11-4)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-11-5)Event: reflect
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-11-6)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-11-7)------
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-11-8)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-11-9)Event: generate
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-11-10)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-11-11)------
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-11-12)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-11-13)Event: reflect
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-11-14)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-11-15)------
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-11-16)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-11-17)Event: generate
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-11-18)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-11-19)------
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-11-20)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-11-21)Event: reflect
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-11-22)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-11-23)------
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-11-24)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-11-25)Event: generate
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-11-26)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-11-27)------

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-12-1)constsnapshot=awaitapp.getState(checkpointConfig);
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-12-2)console.log(
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-12-3)snapshot.values.messages
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-12-4).map((msg:BaseMessage)=>msg.content)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-12-5).join("\n\n\n------------------\n\n\n"),
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-12-6));

```


```
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-1)Generate an essay on the topicality of The Little Prince and its message in modern life
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-2)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-3)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-4)------------------
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-5)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-6)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-7)The Little Prince, a novella written by Antoine de Saint-Exupéry in 1943, has remained a timeless classic, captivating readers of all ages with its poignant and thought-provoking themes. Despite being written over seven decades ago, the story's message continues to resonate with modern society, making it a topical and relevant work of literature.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-8)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-9)One of the primary reasons for The Little Prince's enduring popularity is its exploration of the human condition. The novella delves into the complexities of adult relationships, highlighting the superficiality and materialism that often characterize them. The Little Prince's encounters with various strange characters on different planets serve as a commentary on the flaws of modern society, where people often prioritize wealth, power, and status over genuine human connections. This critique of modern society remains pertinent today, as people continue to struggle with the pressures of social media, consumerism, and the pursuit of material success.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-10)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-11)Furthermore, The Little Prince's emphasis on the importance of human relationships and emotional connections is a message that resonates deeply with modern audiences. In an era where technology has made it easier to connect with others, yet simultaneously created a sense of isolation and disconnection, the novella's themes of love, friendship, and empathy are more relevant than ever. The story encourages readers to reevaluate their priorities and focus on building meaningful relationships, rather than getting caught up in the superficialities of modern life.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-12)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-13)The Little Prince's exploration of the environment and our responsibility towards it is another aspect of the novella that remains topical today. The character's concern for the well-being of his own planet and his desire to protect it from harm serves as a powerful metaphor for the environmental crises facing our world. As we grapple with the consequences of climate change, deforestation, and pollution, the novella's message about the importance of preserving our planet's natural beauty and resources is more urgent than ever.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-14)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-15)In conclusion, The Little Prince's themes of human relationships, emotional connections, and environmental responsibility continue to resonate with modern audiences, making it a topical and relevant work of literature. As we navigate the complexities of modern life, the novella's message serves as a powerful reminder of the importance of prioritizing what truly matters: love, friendship, and the well-being of our planet.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-16)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-17)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-18)------------------
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-19)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-20)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-21)The essay provides a good overview of the topicality of The Little Prince and its message in modern life. However, there are some areas that need improvement.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-22)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-23)Firstly, the introduction could be stronger. Instead of simply stating that the novella is a timeless classic, the writer could provide more context about its enduring popularity and why it remains relevant today.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-24)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-25)Secondly, the body paragraphs could be more detailed and nuanced. For example, the writer could provide more examples from the novella to support their arguments about the human condition, relationships, and the environment. Additionally, the writer could explore the implications of these themes in more depth, such as how they relate to contemporary issues like social media, consumerism, and climate change.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-26)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-27)Thirdly, the conclusion could be more concise and impactful. Instead of simply restating the main points, the writer could summarize the key takeaways and provide a final thought or call to action.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-28)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-29)In terms of style, the writing is clear and concise, but could benefit from more varied sentence structures and vocabulary. Additionally, the writer could use more transitions to connect the different paragraphs and ideas.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-30)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-31)Overall, the essay provides a good foundation for exploring the topicality of The Little Prince, but could benefit from more depth, nuance, and attention to style.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-32)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-33)Grade: B+
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-34)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-35)Recommendations:
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-36)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-37)* Provide more context and background information in the introduction to set up the essay.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-38)* Use more specific examples and details from the novella to support arguments in the body paragraphs.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-39)* Explore the implications of the themes in more depth and relate them to contemporary issues.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-40)* Use more varied sentence structures and vocabulary to improve style.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-41)* Use transitions to connect the different paragraphs and ideas.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-42)* Summarize key takeaways and provide a final thought or call to action in the conclusion.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-43)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-44)Length: 500-750 words
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-45)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-46)Depth: 7/10
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-47)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-48)Style: 6/10
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-49)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-50)Overall, the essay provides a good foundation for exploring the topicality of The Little Prince, but could benefit from more depth, nuance, and attention to style.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-51)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-52)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-53)------------------
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-54)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-55)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-56)Here is a revised version of the essay that addresses the critique provided:
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-57)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-58)The Little Prince, a novella written by Antoine de Saint-Exupéry in 1943, has captivated readers of all ages with its poignant and thought-provoking themes. Despite being written over seven decades ago, the story's message continues to resonate with modern society, making it a timeless classic that remains relevant today. One of the primary reasons for its enduring popularity is its ability to tap into the universal human experiences of love, friendship, and the search for meaning. As a result, the novella has become a cultural touchstone, with its themes and characters continuing to inspire and influence contemporary art, literature, and popular culture.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-59)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-60)One of the most striking aspects of The Little Prince is its exploration of the human condition. The novella delves into the complexities of adult relationships, highlighting the superficiality and materialism that often characterize them. For example, the character of the businessman, who is so consumed by his own importance that he fails to see the beauty of the stars, serves as a powerful commentary on the flaws of modern society. Similarly, the character of the king, who is so obsessed with his own power and authority that he neglects the needs of his subjects, highlights the dangers of unchecked ambition and the importance of empathy and compassion. These critiques of modern society remain pertinent today, as people continue to struggle with the pressures of social media, consumerism, and the pursuit of material success.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-61)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-62)Furthermore, The Little Prince's emphasis on the importance of human relationships and emotional connections is a message that resonates deeply with modern audiences. In an era where technology has made it easier to connect with others, yet simultaneously created a sense of isolation and disconnection, the novella's themes of love, friendship, and empathy are more relevant than ever. For example, the Little Prince's relationship with the rose, which is characterized by a deep sense of love and responsibility, serves as a powerful metaphor for the importance of nurturing and caring for others. Similarly, the character of the fox, who teaches the Little Prince about the importance of human connection and the value of relationships, highlights the need for empathy and understanding in our interactions with others.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-63)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-64)The Little Prince's exploration of the environment and our responsibility towards it is another aspect of the novella that remains topical today. The character's concern for the well-being of his own planet and his desire to protect it from harm serves as a powerful metaphor for the environmental crises facing our world. As we grapple with the consequences of climate change, deforestation, and pollution, the novella's message about the importance of preserving our planet's natural beauty and resources is more urgent than ever. For example, the character of the lamplighter, who is so consumed by his own routine that he fails to see the beauty of the stars, serves as a powerful commentary on the dangers of complacency and the importance of taking action to protect our planet.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-65)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-66)In conclusion, The Little Prince's themes of human relationships, emotional connections, and environmental responsibility continue to resonate with modern audiences, making it a timeless classic that remains relevant today. As we navigate the complexities of modern life, the novella's message serves as a powerful reminder of the importance of prioritizing what truly matters: love, friendship, and the well-being of our planet. Ultimately, The Little Prince encourages us to reevaluate our priorities and focus on building meaningful relationships, rather than getting caught up in the superficialities of modern life. By doing so, we can create a more compassionate, empathetic, and sustainable world for ourselves and for future generations.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-67)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-68)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-69)------------------
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-70)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-71)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-72)The revised essay provides a more detailed and nuanced exploration of the topicality of The Little Prince and its message in modern life. The writer has addressed the critique provided by adding more specific examples and details from the novella to support their arguments, and by exploring the implications of the themes in more depth.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-73)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-74)One of the strengths of the revised essay is its ability to provide a more detailed and nuanced exploration of the human condition. The writer has done a good job of highlighting the complexities of adult relationships and the dangers of superficiality and materialism. The use of specific examples from the novella, such as the character of the businessman and the king, adds depth and nuance to the argument.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-75)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-76)The revised essay also does a good job of exploring the importance of human relationships and emotional connections in modern life. The writer has provided more specific examples from the novella, such as the Little Prince's relationship with the rose and the character of the fox, to support their argument. The use of these examples adds depth and nuance to the argument and helps to make it more relatable to modern audiences.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-77)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-78)The revised essay also does a good job of exploring the environmental themes in the novella and their relevance to modern life. The writer has provided more specific examples from the novella, such as the character of the lamplighter, to support their argument. The use of these examples adds depth and nuance to the argument and helps to make it more relatable to modern audiences.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-79)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-80)One area for improvement is the conclusion. While the writer has done a good job of summarizing the main points, the conclusion could be more concise and impactful. The writer could consider ending with a more thought-provoking question or a call to action to leave the reader with a lasting impression.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-81)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-82)Overall, the revised essay provides a more detailed and nuanced exploration of the topicality of The Little Prince and its message in modern life. The writer has done a good job of addressing the critique provided and has added more depth and nuance to the argument.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-83)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-84)Grade: A-
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-85)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-86)Recommendations:
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-87)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-88)* Consider ending the conclusion with a more thought-provoking question or a call to action to leave the reader with a lasting impression.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-89)* Use more varied sentence structures and vocabulary to improve style.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-90)* Consider adding more transitions to connect the different paragraphs and ideas.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-91)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-92)Length: 750-1000 words
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-93)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-94)Depth: 9/10
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-95)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-96)Style: 8/10
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-97)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-98)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-99)------------------
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-100)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-101)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-102)Here is a revised version of the essay that addresses the critique provided:
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-103)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-104)The Little Prince, a novella written by Antoine de Saint-Exupéry in 1943, has captivated readers of all ages with its poignant and thought-provoking themes. Despite being written over seven decades ago, the story's message continues to resonate with modern society, making it a timeless classic that remains relevant today. One of the primary reasons for its enduring popularity is its ability to tap into the universal human experiences of love, friendship, and the search for meaning. As a result, the novella has become a cultural touchstone, with its themes and characters continuing to inspire and influence contemporary art, literature, and popular culture.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-105)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-106)One of the most striking aspects of The Little Prince is its exploration of the human condition. The novella delves into the complexities of adult relationships, highlighting the superficiality and materialism that often characterize them. For example, the character of the businessman, who is so consumed by his own importance that he fails to see the beauty of the stars, serves as a powerful commentary on the flaws of modern society. Similarly, the character of the king, who is so obsessed with his own power and authority that he neglects the needs of his subjects, highlights the dangers of unchecked ambition and the importance of empathy and compassion. These critiques of modern society remain pertinent today, as people continue to struggle with the pressures of social media, consumerism, and the pursuit of material success.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-107)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-108)Furthermore, The Little Prince's emphasis on the importance of human relationships and emotional connections is a message that resonates deeply with modern audiences. In an era where technology has made it easier to connect with others, yet simultaneously created a sense of isolation and disconnection, the novella's themes of love, friendship, and empathy are more relevant than ever. For example, the Little Prince's relationship with the rose, which is characterized by a deep sense of love and responsibility, serves as a powerful metaphor for the importance of nurturing and caring for others. Similarly, the character of the fox, who teaches the Little Prince about the importance of human connection and the value of relationships, highlights the need for empathy and understanding in our interactions with others.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-109)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-110)The Little Prince's exploration of the environment and our responsibility towards it is another aspect of the novella that remains topical today. The character's concern for the well-being of his own planet and his desire to protect it from harm serves as a powerful metaphor for the environmental crises facing our world. As we grapple with the consequences of climate change, deforestation, and pollution, the novella's message about the importance of preserving our planet's natural beauty and resources is more urgent than ever. For example, the character of the lamplighter, who is so consumed by his own routine that he fails to see the beauty of the stars, serves as a powerful commentary on the dangers of complacency and the importance of taking action to protect our planet.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-111)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-112)In conclusion, The Little Prince's themes of human relationships, emotional connections, and environmental responsibility continue to resonate with modern audiences, making it a timeless classic that remains relevant today. As we navigate the complexities of modern life, the novella's message serves as a powerful reminder of the importance of prioritizing what truly matters: love, friendship, and the well-being of our planet. Ultimately, The Little Prince encourages us to reevaluate our priorities and focus on building meaningful relationships, rather than getting caught up in the superficialities of modern life. By doing so, we can create a more compassionate, empathetic, and sustainable world for ourselves and for future generations. As we look to the future, we would do well to remember the Little Prince's wise words: "You become responsible, forever, for what you have tamed."
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-113)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-114)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-115)------------------
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-116)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-117)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-118)The revised essay provides a more detailed and nuanced exploration of the topicality of The Little Prince and its message in modern life. The writer has addressed the critique provided by adding more specific examples and details from the novella to support their arguments, and by exploring the implications of the themes in more depth.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-119)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-120)One of the strengths of the revised essay is its ability to provide a more detailed and nuanced exploration of the human condition. The writer has done a good job of highlighting the complexities of adult relationships and the dangers of superficiality and materialism. The use of specific examples from the novella, such as the character of the businessman and the king, adds depth and nuance to the argument.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-121)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-122)The revised essay also does a good job of exploring the importance of human relationships and emotional connections in modern life. The writer has provided more specific examples from the novella, such as the Little Prince's relationship with the rose and the character of the fox, to support their argument. The use of these examples adds depth and nuance to the argument and helps to make it more relatable to modern audiences.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-123)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-124)The revised essay also does a good job of exploring the environmental themes in the novella and their relevance to modern life. The writer has provided more specific examples from the novella, such as the character of the lamplighter, to support their argument. The use of these examples adds depth and nuance to the argument and helps to make it more relatable to modern audiences.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-125)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-126)The conclusion is also well-written and effectively summarizes the main points of the essay. The use of the Little Prince's quote at the end adds a nice touch and helps to drive home the importance of prioritizing what truly matters in life.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-127)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-128)Overall, the revised essay provides a more detailed and nuanced exploration of the topicality of The Little Prince and its message in modern life. The writer has done a good job of addressing the critique provided and has added more depth and nuance to the argument.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-129)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-130)Grade: A
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-131)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-132)Recommendations:
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-133)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-134)* None. The essay is well-written and effectively explores the topicality of The Little Prince and its message in modern life.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-135)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-136)Length: 750-1000 words
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-137)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-138)Depth: 9/10
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-139)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-140)Style: 9/10
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-141)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-142)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-143)------------------
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-144)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-145)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-146)I'm glad to hear that the revised essay meets your expectations. I believe that the essay provides a thorough and nuanced exploration of the topicality of The Little Prince and its message in modern life. The use of specific examples from the novella adds depth and nuance to the argument, and the conclusion effectively summarizes the main points of the essay.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-147)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-148)I'm also pleased to hear that the essay is well-written and effectively explores the themes of the human condition, human relationships, and environmental responsibility. The use of the Little Prince's quote at the end adds a nice touch and helps to drive home the importance of prioritizing what truly matters in life.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-149)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-150)Overall, I'm proud of the work that I've done on this essay, and I'm glad to hear that it meets your expectations. If you have any other requests or need further assistance, please don't hesitate to ask.
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-151)
[](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__codelineno-13-152)Thank you for your feedback and guidance throughout this process. I appreciate your input and look forward to continuing to work with you in the future.

```


> #### See the LangSmith trace [here](https://smith.langchain.com/public/9bf804f7-1df8-46ef-9b40-23b3d3c97756/r)[¶](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#see-the-langsmith-trace-here "Permanent link")

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  Plan-and-Execute  ](https://langchain-ai.github.io/langgraphjs/tutorials/plan-and-execute/plan-and-execute/) [ Next  Reasoning without Observation  ](https://langchain-ai.github.io/langgraphjs/tutorials/rewoo/rewoo/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/tutorials/reflection/reflection/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
