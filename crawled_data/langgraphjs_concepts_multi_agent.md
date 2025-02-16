---
url: https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#multi-agent-systems)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

Multi-agent Systems 

[ ](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/?q= "Share")

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

Concepts 
        * LangGraph  LangGraph 
          * [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/concepts#langgraph)
          * [ Why LangGraph?  ](https://langchain-ai.github.io/langgraphjs/concepts/high_level/)
          * [ LangGraph Glossary  ](https://langchain-ai.github.io/langgraphjs/concepts/low_level/)
          * [ Agent architectures  ](https://langchain-ai.github.io/langgraphjs/concepts/agentic_concepts/)
          * Multi-agent Systems  [ Multi-agent Systems  ](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/) Table of contents 
            * [ Multi-agent architectures  ](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#multi-agent-architectures)
              * [ Handoffs  ](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#handoffs)
              * [ Network  ](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#network)
              * [ Supervisor  ](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#supervisor)
              * [ Custom multi-agent workflow  ](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#custom-multi-agent-workflow)
            * [ Communication between agents  ](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#communication-between-agents)
              * [ Graph state  ](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#graph-state)
              * [ Different state schemas  ](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#different-state-schemas)
              * [ Shared message list  ](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#shared-message-list)
                * [ Share full history  ](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#share-full-history)
                * [ Share final result  ](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#share-final-result)
          * [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/)
          * [ Persistence  ](https://langchain-ai.github.io/langgraphjs/concepts/persistence/)
          * [ Memory  ](https://langchain-ai.github.io/langgraphjs/concepts/memory/)
          * [ Streaming  ](https://langchain-ai.github.io/langgraphjs/concepts/streaming/)
          * [ Functional API  ](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/)
        * [ LangGraph Platform  ](https://langchain-ai.github.io/langgraphjs/concepts#langgraph-platform)
      * [ Tutorials  ](https://langchain-ai.github.io/langgraphjs/tutorials/)
    * Resources  Resources 
      * [ Adopters  ](https://langchain-ai.github.io/langgraphjs/adopters/)
      * [ FAQ  ](https://langchain-ai.github.io/langgraphjs/concepts/faq/)
      * [ Troubleshooting  ](https://langchain-ai.github.io/langgraphjs/troubleshooting/errors/)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraphjs/reference/)
  * [ Versions  ](https://langchain-ai.github.io/langgraphjs/versions/)



Table of contents 

  * [ Multi-agent architectures  ](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#multi-agent-architectures)
    * [ Handoffs  ](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#handoffs)
    * [ Network  ](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#network)
    * [ Supervisor  ](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#supervisor)
    * [ Custom multi-agent workflow  ](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#custom-multi-agent-workflow)
  * [ Communication between agents  ](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#communication-between-agents)
    * [ Graph state  ](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#graph-state)
    * [ Different state schemas  ](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#different-state-schemas)
    * [ Shared message list  ](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#shared-message-list)
      * [ Share full history  ](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#share-full-history)
      * [ Share final result  ](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#share-final-result)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ Concepts  ](https://langchain-ai.github.io/langgraphjs/concepts/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/concepts#langgraph)



# Multi-agent Systems[¶](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#multi-agent-systems "Permanent link")

An [agent](https://langchain-ai.github.io/langgraphjs/concepts/agentic_concepts/#agent-architectures) is _a system that uses an LLM to decide the control flow of an application_. As you develop these systems, they might grow more complex over time, making them harder to manage and scale. For example, you might run into the following problems:

  * agent has too many tools at its disposal and makes poor decisions about which tool to call next
  * context grows too complex for a single agent to keep track of
  * there is a need for multiple specialization areas in the system (e.g. planner, researcher, math expert, etc.)



To tackle these, you might consider breaking your application into multiple smaller, independent agents and composing them into a **multi-agent system**. These independent agents can be as simple as a prompt and an LLM call, or as complex as a [ReAct](https://langchain-ai.github.io/langgraphjs/concepts/agentic_concepts/#react-implementation) agent (and more!).

The primary benefits of using multi-agent systems are:

  * **Modularity** : Separate agents make it easier to develop, test, and maintain agentic systems.
  * **Specialization** : You can create expert agents focused on specific domains, which helps with the overall system performance.
  * **Control** : You can explicitly control how agents communicate (as opposed to relying on function calling).



## Multi-agent architectures[¶](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#multi-agent-architectures "Permanent link")

![](https://langchain-ai.github.io/langgraphjs/concepts/img/multi_agent/architectures.png)

There are several ways to connect agents in a multi-agent system:

  * **Network** : each agent can communicate with every other agent. Any agent can decide which other agent to call next.
  * **Supervisor** : each agent communicates with a single [supervisor](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/) agent. Supervisor agent makes decisions on which agent should be called next.
  * **Hierarchical** : you can define a multi-agent system with a supervisor of supervisors. This is a generalization of the supervisor architecture and allows for more complex control flows.
  * **Custom multi-agent workflow** : each agent communicates with only a subset of agents. Parts of the flow are deterministic, and only some agents can decide which other agents to call next.



### Handoffs[¶](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#handoffs "Permanent link")

In multi-agent architectures, agents can be represented as graph nodes. Each agent node executes its step(s) and decides whether to finish execution or route to another agent, including potentially routing to itself (e.g., running in a loop). A common pattern in multi-agent interactions is handoffs, where one agent hands off control to another. Handoffs allow you to specify:

  * **destination** : target agent to navigate to (e.g., name of the node to go to)
  * **payload** : [information to pass to that agent](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#communication-between-agents) (e.g., state update)



To implement handoffs in LangGraph, agent nodes can return `Command`[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#command) object that allows you to combine both control flow and state updates:

```
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-0-1)constagent=(state:typeofStateAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-0-2)constgoto=getNextAgent(...)// 'agent' / 'another_agent'
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-0-3)returnnewCommand({
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-0-4)// Specify which agent to call next
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-0-5)goto:goto,
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-0-6)// Update the graph state
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-0-7)update:{
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-0-8)foo:"bar",
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-0-9)}
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-0-10)});
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-0-11)};

```


In a more complex scenario where each agent node is itself a graph (i.e., a [subgraph](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#subgraphs)), a node in one of the agent subgraphs might want to navigate to a different agent. For example, if you have two agents, `alice` and `bob` (subgraph nodes in a parent graph), and `alice` needs to navigate to `bob`, you can set `graph=Command.PARENT` in the `Command` object:

```
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-1-1)constsome_node_inside_alice=(state)=>{
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-1-2)returnnewCommand({
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-1-3)goto:"bob",
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-1-4)update:{
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-1-5)foo:"bar",
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-1-6)},
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-1-7)// specify which graph to navigate to (defaults to the current graph)
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-1-8)graph:Command.PARENT,
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-1-9)})
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-1-10)}

```


### Network[¶](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#network "Permanent link")

In this architecture, agents are defined as graph nodes. Each agent can communicate with every other agent (many-to-many connections) and can decide which agent to call next. This architecture is good for problems that do not have a clear hierarchy of agents or a specific sequence in which agents should be called.

```
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-1)import{
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-2)StateGraph,
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-3)Annotation,
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-4)MessagesAnnotation,
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-5)Command
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-6)}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-7)import{ChatOpenAI}from"@langchain/openai";
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-8)
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-9)constmodel=newChatOpenAI({
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-10)model:"gpt-4o-mini",
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-11)});
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-12)
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-13)constagent1=async(state:typeofMessagesAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-14)// you can pass relevant parts of the state to the LLM (e.g., state.messages)
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-15)// to determine which agent to call next. a common pattern is to call the model
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-16)// with a structured output (e.g. force it to return an output with a "next_agent" field)
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-17)constresponse=awaitmodel.withStructuredOutput(...).invoke(...);
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-18)returnnewCommand({
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-19)update:{
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-20)messages:[response.content],
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-21)},
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-22)goto:response.next_agent,
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-23)});
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-24)};
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-25)
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-26)constagent2=async(state:typeofMessagesAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-27)constresponse=awaitmodel.withStructuredOutput(...).invoke(...);
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-28)returnnewCommand({
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-29)update:{
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-30)messages:[response.content],
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-31)},
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-32)goto:response.next_agent,
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-33)});
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-34)};
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-35)
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-36)constagent3=async(state:typeofMessagesAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-37)...
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-38)returnnewCommand({
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-39)update:{
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-40)messages:[response.content],
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-41)},
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-42)goto:response.next_agent,
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-43)});
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-44)};
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-45)
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-46)constgraph=newStateGraph(MessagesAnnotation)
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-47).addNode("agent1",agent1,{
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-48)ends:["agent2","agent3""__end__"],
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-49)})
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-50).addNode("agent2",agent2,{
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-51)ends:["agent1","agent3","__end__"],
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-52)})
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-53).addNode("agent3",agent3,{
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-54)ends:["agent1","agent2","__end__"],
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-55)})
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-56).addEdge("__start__","agent1")
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-2-57).compile();

```


### Supervisor[¶](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#supervisor "Permanent link")

In this architecture, we define agents as nodes and add a supervisor node (LLM) that decides which agent nodes should be called next. We use `Command`[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#command) to route execution to the appropriate agent node based on supervisor's decision. This architecture also lends itself well to running multiple agents in parallel or using [map-reduce](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/) pattern.

```
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-1)import{
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-2)StateGraph,
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-3)MessagesAnnotation,
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-4)Command,
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-5)}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-6)import{ChatOpenAI}from"@langchain/openai";
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-7)
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-8)constmodel=newChatOpenAI({
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-9)model:"gpt-4o-mini",
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-10)});
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-11)
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-12)constsupervisor=async(state:typeofMessagesAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-13)// you can pass relevant parts of the state to the LLM (e.g., state.messages)
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-14)// to determine which agent to call next. a common pattern is to call the model
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-15)// with a structured output (e.g. force it to return an output with a "next_agent" field)
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-16)constresponse=awaitmodel.withStructuredOutput(...).invoke(...);
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-17)// route to one of the agents or exit based on the supervisor's decision
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-18)// if the supervisor returns "__end__", the graph will finish execution
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-19)returnnewCommand({
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-20)goto:response.next_agent,
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-21)});
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-22)};
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-23)
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-24)constagent1=async(state:typeofMessagesAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-25)// you can pass relevant parts of the state to the LLM (e.g., state.messages)
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-26)// and add any additional logic (different models, custom prompts, structured output, etc.)
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-27)constresponse=awaitmodel.invoke(...);
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-28)returnnewCommand({
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-29)goto:"supervisor",
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-30)update:{
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-31)messages:[response],
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-32)},
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-33)});
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-34)};
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-35)
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-36)constagent2=async(state:typeofMessagesAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-37)constresponse=awaitmodel.invoke(...);
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-38)returnnewCommand({
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-39)goto:"supervisor",
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-40)update:{
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-41)messages:[response],
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-42)},
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-43)});
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-44)};
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-45)
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-46)constgraph=newStateGraph(MessagesAnnotation)
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-47).addNode("supervisor",supervisor,{
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-48)ends:["agent1","agent2","__end__"],
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-49)})
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-50).addNode("agent1",agent1,{
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-51)ends:["supervisor"],
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-52)})
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-53).addNode("agent2",agent2,{
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-54)ends:["supervisor"],
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-55)})
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-56).addEdge("__start__","supervisor")
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-3-57).compile();

```


Check out this [tutorial](https://langchain-ai.github.io/langgraphjs/tutorials/multi_agent/agent_supervisor/) for an example of supervisor multi-agent architecture.

### Custom multi-agent workflow[¶](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#custom-multi-agent-workflow "Permanent link")

In this architecture we add individual agents as graph nodes and define the order in which agents are called ahead of time, in a custom workflow. In LangGraph the workflow can be defined in two ways:

  * **Explicit control flow (normal edges)** : LangGraph allows you to explicitly define the control flow of your application (i.e. the sequence of how agents communicate) explicitly, via [normal graph edges](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#normal-edges). This is the most deterministic variant of this architecture above — we always know which agent will be called next ahead of time.

  * **Dynamic control flow (conditional edges)** : in LangGraph you can allow LLMs to decide parts of your application control flow. This can be achieved by using `Command`[](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#command).




```
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-4-1)import{
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-4-2)StateGraph,
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-4-3)MessagesAnnotation,
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-4-4)}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-4-5)import{ChatOpenAI}from"@langchain/openai";
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-4-6)
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-4-7)constmodel=newChatOpenAI({
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-4-8)model:"gpt-4o-mini",
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-4-9)});
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-4-10)
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-4-11)constagent1=async(state:typeofMessagesAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-4-12)constresponse=awaitmodel.invoke(...);
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-4-13)return{messages:[response]};
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-4-14)};
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-4-15)
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-4-16)constagent2=async(state:typeofMessagesAnnotation.State)=>{
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-4-17)constresponse=awaitmodel.invoke(...);
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-4-18)return{messages:[response]};
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-4-19)};
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-4-20)
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-4-21)constgraph=newStateGraph(MessagesAnnotation)
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-4-22).addNode("agent1",agent1)
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-4-23).addNode("agent2",agent2)
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-4-24)// define the flow explicitly
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-4-25).addEdge("__start__","agent1")
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-4-26).addEdge("agent1","agent2")
[](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__codelineno-4-27).compile();

```


## Communication between agents[¶](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#communication-between-agents "Permanent link")

The most important thing when building multi-agent systems is figuring out how the agents communicate. There are few different considerations:

  * What if two agents have [**different state schemas**](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#different-state-schemas)?
  * How to communicate over a [**shared message list**](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#shared-message-list)?



#### Graph state[¶](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#graph-state "Permanent link")

To communicate via graph state, individual agents need to be defined as [graph nodes](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#nodes). These can be added as functions or as entire [subgraphs](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#subgraphs). At each step of the graph execution, agent node receives the current state of the graph, executes the agent code and then passes the updated state to the next nodes.

Typically agent nodes share a single [state schema](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#state). However, you might want to design agent nodes with [different state schemas](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#different-state-schemas).

### Different state schemas[¶](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#different-state-schemas "Permanent link")

An agent might need to have a different state schema from the rest of the agents. For example, a search agent might only need to keep track of queries and retrieved documents. There are two ways to achieve this in LangGraph:

  * Define [subgraph](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#subgraphs) agents with a separate state schema. If there are no shared state keys (channels) between the subgraph and the parent graph, it’s important to [add input / output transformations](https://langchain-ai.github.io/langgraphjs/how-tos/subgraph-transform-state/) so that the parent graph knows how to communicate with the subgraphs.
  * Define agent node functions with a [private input state schema](https://langchain-ai.github.io/langgraphjs/how-tos/pass_private_state/) that is distinct from the overall graph state schema. This allows passing information that is only needed for executing that particular agent.



### Shared message list[¶](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#shared-message-list "Permanent link")

The most common way for the agents to communicate is via a shared state channel, typically a list of messages. This assumes that there is always at least a single channel (key) in the state that is shared by the agents. When communicating via a shared message list there is an additional consideration: should the agents [share the full history](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#share-full-history) of their thought process or only [the final result](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#share-final-result)?

![](https://langchain-ai.github.io/langgraphjs/concepts/img/multi_agent/response.png)

#### Share full history[¶](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#share-full-history "Permanent link")

Agents can **share the full history** of their thought process (i.e. "scratchpad") with all other agents. This "scratchpad" would typically look like a [list of messages](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#why-use-messages). The benefit of sharing full thought process is that it might help other agents make better decisions and improve reasoning ability for the system as a whole. The downside is that as the number of agents and their complexity grows, the "scratchpad" will grow quickly and might require additional strategies for [memory management](https://langchain-ai.github.io/langgraphjs/concepts/memory/#managing-long-conversation-history).

#### Share final result[¶](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#share-final-result "Permanent link")

Agents can have their own private "scratchpad" and only **share the final result** with the rest of the agents. This approach might work better for systems with many agents or agents that are more complex. In this case, you would need to define agents with [different state schemas](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#different-state-schemas)

For agents called as tools, the supervisor determines the inputs based on the tool schema. Additionally, LangGraph allows [passing state](https://langchain-ai.github.io/langgraphjs/how-tos/pass-run-time-values-to-tools/) to individual tools at runtime, so subordinate agents can access parent state, if needed.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  Agent architectures  ](https://langchain-ai.github.io/langgraphjs/concepts/agentic_concepts/) [ Next  Human-in-the-loop  ](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
