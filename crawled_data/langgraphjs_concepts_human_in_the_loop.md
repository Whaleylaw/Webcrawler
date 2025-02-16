---
url: https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#human-in-the-loop)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraphjs/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraphjs/)

Human-in-the-loop 

[ ](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/?q= "Share")

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
          * [ Multi-agent Systems  ](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/)
          * Human-in-the-loop  [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/) Table of contents 
            * [ Use cases  ](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#use-cases)
            * [ interrupt  ](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#interrupt)
            * [ Requirements  ](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#requirements)
            * [ Design Patterns  ](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#design-patterns)
              * [ Approve or Reject  ](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#approve-or-reject)
              * [ Review & Edit State  ](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#review-edit-state)
              * [ Review Tool Calls  ](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#review-tool-calls)
              * [ Multi-turn conversation  ](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#multi-turn-conversation)
              * [ Validating human input  ](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#validating-human-input)
            * [ The Command primitive  ](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#the-command-primitive)
            * [ Using with invoke  ](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#using-with-invoke)
            * [ How does resuming from an interrupt work?  ](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#how-does-resuming-from-an-interrupt-work)
            * [ Common Pitfalls  ](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#common-pitfalls)
              * [ Side-effects  ](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#side-effects)
              * [ Subgraphs called as functions  ](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#subgraphs-called-as-functions)
              * [ Using multiple interrupts  ](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#using-multiple-interrupts)
            * [ Additional Resources 📚  ](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#additional-resources)
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

  * [ Use cases  ](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#use-cases)
  * [ interrupt  ](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#interrupt)
  * [ Requirements  ](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#requirements)
  * [ Design Patterns  ](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#design-patterns)
    * [ Approve or Reject  ](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#approve-or-reject)
    * [ Review & Edit State  ](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#review-edit-state)
    * [ Review Tool Calls  ](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#review-tool-calls)
    * [ Multi-turn conversation  ](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#multi-turn-conversation)
    * [ Validating human input  ](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#validating-human-input)
  * [ The Command primitive  ](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#the-command-primitive)
  * [ Using with invoke  ](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#using-with-invoke)
  * [ How does resuming from an interrupt work?  ](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#how-does-resuming-from-an-interrupt-work)
  * [ Common Pitfalls  ](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#common-pitfalls)
    * [ Side-effects  ](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#side-effects)
    * [ Subgraphs called as functions  ](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#subgraphs-called-as-functions)
    * [ Using multiple interrupts  ](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#using-multiple-interrupts)
  * [ Additional Resources 📚  ](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#additional-resources)



  1. [ Home  ](https://langchain-ai.github.io/langgraphjs/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraphjs/how-tos/)
  3. [ Concepts  ](https://langchain-ai.github.io/langgraphjs/concepts/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraphjs/concepts#langgraph)



# Human-in-the-loop[¶](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#human-in-the-loop "Permanent link")

This guide uses the new `interrupt` function.

As of LangGraph 0.2.31, the recommended way to set breakpoints is using the `interrupt`[ function](https://langchain-ai.github.io/langgraphjs/reference/functions/langgraph.interrupt-1.html) as it simplifies **human-in-the-loop** patterns.

If you're looking for the previous version of this conceptual guide, which relied on static breakpoints and `NodeInterrupt` exception, it is available [here](https://langchain-ai.github.io/langgraphjs/concepts/v0-human-in-the-loop/).

A **human-in-the-loop** (or "on-the-loop") workflow integrates human input into automated processes, allowing for decisions, validation, or corrections at key stages. This is especially useful in **LLM-based applications** , where the underlying model may generate occasional inaccuracies. In low-error-tolerance scenarios like compliance, decision-making, or content generation, human involvement ensures reliability by enabling review, correction, or override of model outputs.

## Use cases[¶](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#use-cases "Permanent link")

Key use cases for **human-in-the-loop** workflows in LLM-based applications include:

  1. [**🛠️ Reviewing tool calls**](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#review-tool-calls): Humans can review, edit, or approve tool calls requested by the LLM before tool execution.

  2. **✅ Validating LLM outputs** : Humans can review, edit, or approve content generated by the LLM.

  3. **💡 Providing context** : Enable the LLM to explicitly request human input for clarification or additional details or to support multi-turn conversations.




## `interrupt`[¶](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#interrupt "Permanent link")

The `interrupt`[ function](https://langchain-ai.github.io/langgraphjs/reference/functions/langgraph.interrupt-1.html) in LangGraph enables human-in-the-loop workflows by pausing the graph at a specific node, presenting information to a human, and resuming the graph with their input. This function is useful for tasks like approvals, edits, or collecting additional input. The `interrupt`[ function](https://langchain-ai.github.io/langgraphjs/reference/functions/langgraph.interrupt-1.html) is used in conjunction with the `Command`[](https://langchain-ai.github.io/langgraphjs/reference/classes/langgraph.Command.html) object to resume the graph with a value provided by the human.

```
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-0-1)import{interrupt}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-0-2)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-0-3)functionhumanNode(state:typeofGraphAnnotation.State){
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-0-4)constvalue=interrupt(
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-0-5)// Any JSON serializable value to surface to the human.
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-0-6)// For example, a question or a piece of text or a set of keys in the state
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-0-7){
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-0-8)text_to_revise:state.some_text,
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-0-9)}
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-0-10));
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-0-11)// Update the state with the human's input or route the graph based on the input
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-0-12)return{
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-0-13)some_text:value,
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-0-14)};
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-0-15)}
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-0-16)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-0-17)constgraph=workflow.compile({
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-0-18)checkpointer,// Required for `interrupt` to work
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-0-19)});
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-0-20)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-0-21)// Run the graph until the interrupt
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-0-22)constthreadConfig={configurable:{thread_id:"some_id"}};
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-0-23)awaitgraph.invoke(someInput,threadConfig);
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-0-24)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-0-25)// Below code can run some amount of time later and/or in a different process
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-0-26)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-0-27)// Human input
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-0-28)constvalueFromHuman="...";
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-0-29)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-0-30)// Resume the graph with the human's input
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-0-31)awaitgraph.invoke(newCommand({resume:valueFromHuman}),threadConfig);

```


```
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-1-1){
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-1-2)some_text:"Edited text";
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-1-3)}

```


Full Code

Here's a full example of how to use `interrupt` in a graph, if you'd like to see the code in action.

```
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-2-1)import{MemorySaver,Annotation,interrupt,Command,StateGraph}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-2-2)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-2-3)// Define the graph state
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-2-4)constStateAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-2-5)some_text:Annotation<string>()
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-2-6)});
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-2-7)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-2-8)functionhumanNode(state:typeofStateAnnotation.State){
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-2-9)constvalue=interrupt(
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-2-10)// Any JSON serializable value to surface to the human.
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-2-11)// For example, a question or a piece of text or a set of keys in the state
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-2-12){
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-2-13)text_to_revise:state.some_text
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-2-14)}
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-2-15));
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-2-16)return{
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-2-17)// Update the state with the human's input
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-2-18)some_text:value
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-2-19)};
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-2-20)}
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-2-21)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-2-22)// Build the graph
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-2-23)constworkflow=newStateGraph(StateAnnotation)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-2-24)// Add the human-node to the graph
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-2-25).addNode("human_node",humanNode)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-2-26).addEdge("__start__","human_node")
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-2-27)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-2-28)// A checkpointer is required for `interrupt` to work.
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-2-29)constcheckpointer=newMemorySaver();
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-2-30)constgraph=workflow.compile({
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-2-31)checkpointer
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-2-32)});
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-2-33)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-2-34)// Using stream() to directly surface the `__interrupt__` information.
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-2-35)forawait(constchunkofawaitgraph.stream(
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-2-36){some_text:"Original text"},
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-2-37)threadConfig
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-2-38))){
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-2-39)console.log(chunk);
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-2-40)}
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-2-41)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-2-42)// Resume using Command
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-2-43)forawait(constchunkofawaitgraph.stream(
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-2-44)newCommand({resume:"Edited text"}),
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-2-45)threadConfig
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-2-46))){
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-2-47)console.log(chunk);
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-2-48)}

```


```
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-3-1){
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-3-2)__interrupt__:[
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-3-3){
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-3-4)value:{question:'Please revise the text',some_text:'Original text'},
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-3-5)resumable:true,
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-3-6)ns:['human_node:10fe492f-3688-c8c6-0d0a-ec61a43fecd6'],
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-3-7)when:'during'
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-3-8)}
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-3-9)]
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-3-10)}
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-3-11){human_node:{some_text:'Edited text'}}

```


## Requirements[¶](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#requirements "Permanent link")

To use `interrupt` in your graph, you need to:

  1. [**Specify a checkpointer**](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#checkpoints) to save the graph state after each step.

  2. **Call`interrupt()`** in the appropriate place. See the [Design Patterns](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#design-patterns) section for examples.

  3. **Run the graph** with a [**thread ID**](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#threads) until the `interrupt` is hit.

  4. **Resume execution** using `invoke`/`stream` (see [**The`Command` primitive**](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#the-command-primitive)).




## Design Patterns[¶](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#design-patterns "Permanent link")

There are typically three different **actions** that you can do with a human-in-the-loop workflow:

  1. **Approve or Reject** : Pause the graph before a critical step, such as an API call, to review and approve the action. If the action is rejected, you can prevent the graph from executing the step, and potentially take an alternative action. This pattern often involve **routing** the graph based on the human's input.

  2. **Edit Graph State** : Pause the graph to review and edit the graph state. This is useful for correcting mistakes or updating the state with additional information. This pattern often involves **updating** the state with the human's input.

  3. **Get Input** : Explicitly request human input at a particular step in the graph. This is useful for collecting additional information or context to inform the agent's decision-making process or for supporting **multi-turn conversations**.




Below we show different design patterns that can be implemented using these **actions**.

### Approve or Reject[¶](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#approve-or-reject "Permanent link")

![image](https://langchain-ai.github.io/langgraphjs/concepts/img/human_in_the_loop/approve-or-reject.png)

Depending on the human's approval or rejection, the graph can proceed with the action or take an alternative path.

Pause the graph before a critical step, such as an API call, to review and approve the action. If the action is rejected, you can prevent the graph from executing the step, and potentially take an alternative action.

```
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-4-1)import{interrupt,Command}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-4-2)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-4-3)functionhumanApproval(state:typeofGraphAnnotation.State):Command{
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-4-4)constisApproved=interrupt({
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-4-5)question:"Is this correct?",
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-4-6)// Surface the output that should be
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-4-7)// reviewed and approved by the human.
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-4-8)llm_output:state.llm_output,
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-4-9)});
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-4-10)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-4-11)if(isApproved){
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-4-12)returnnewCommand({goto:"some_node"});
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-4-13)}else{
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-4-14)returnnewCommand({goto:"another_node"});
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-4-15)}
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-4-16)}
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-4-17)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-4-18)// Add the node to the graph in an appropriate location
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-4-19)// and connect it to the relevant nodes.
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-4-20)constgraph=graphBuilder
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-4-21).addNode("human_approval",humanApproval)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-4-22).compile({checkpointer});
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-4-23)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-4-24)// After running the graph and hitting the interrupt, the graph will pause.
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-4-25)// Resume it with either an approval or rejection.
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-4-26)constthreadConfig={configurable:{thread_id:"some_id"}};
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-4-27)awaitgraph.invoke(newCommand({resume:true}),threadConfig);

```


See [how to review tool calls](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls) for a more detailed example.

### Review & Edit State[¶](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#review-edit-state "Permanent link")

![image](https://langchain-ai.github.io/langgraphjs/concepts/img/human_in_the_loop/edit-graph-state-simple.png)

A human can review and edit the state of the graph. This is useful for correcting mistakes or updating the state with additional information. 

```
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-5-1)import{interrupt}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-5-2)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-5-3)functionhumanEditing(state:typeofGraphAnnotation.State):Command{
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-5-4)constresult=interrupt({
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-5-5)// Interrupt information to surface to the client.
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-5-6)// Can be any JSON serializable value.
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-5-7)task:"Review the output from the LLM and make any necessary edits.",
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-5-8)llm_generated_summary:state.llm_generated_summary,
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-5-9)});
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-5-10)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-5-11)// Update the state with the edited text
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-5-12)return{
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-5-13)llm_generated_summary:result.edited_text,
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-5-14)};
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-5-15)}
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-5-16)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-5-17)// Add the node to the graph in an appropriate location
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-5-18)// and connect it to the relevant nodes.
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-5-19)constgraph=graphBuilder
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-5-20).addNode("human_editing",humanEditing)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-5-21).compile({checkpointer});
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-5-22)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-5-23)// After running the graph and hitting the interrupt, the graph will pause.
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-5-24)// Resume it with the edited text.
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-5-25)constthreadConfig={configurable:{thread_id:"some_id"}};
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-5-26)awaitgraph.invoke(
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-5-27)newCommand({resume:{edited_text:"The edited text"}}),
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-5-28)threadConfig
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-5-29));

```


See [How to wait for user input using interrupt](https://langchain-ai.github.io/langgraphjs/how-tos/wait-user-input) for a more detailed example.

### Review Tool Calls[¶](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#review-tool-calls "Permanent link")

![image](https://langchain-ai.github.io/langgraphjs/concepts/img/human_in_the_loop/tool-call-review.png)

A human can review and edit the output from the LLM before proceeding. This is particularly critical in applications where the tool calls requested by the LLM may be sensitive or require human oversight. 

```
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-6-1)import{interrupt,Command}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-6-2)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-6-3)functionhumanReviewNode(state:typeofGraphAnnotation.State):Command{
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-6-4)// This is the value we'll be providing via Command.resume(<human_review>)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-6-5)consthumanReview=interrupt({
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-6-6)question:"Is this correct?",
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-6-7)// Surface tool calls for review
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-6-8)tool_call:toolCall,
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-6-9)});
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-6-10)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-6-11)const[reviewAction,reviewData]=humanReview;
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-6-12)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-6-13)// Approve the tool call and continue
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-6-14)if(reviewAction==="continue"){
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-6-15)returnnewCommand({goto:"run_tool"});
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-6-16)}
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-6-17)// Modify the tool call manually and then continue
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-6-18)elseif(reviewAction==="update"){
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-6-19)constupdatedMsg=getUpdatedMsg(reviewData);
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-6-20)// Remember that to modify an existing message you will need
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-6-21)// to pass the message with a matching ID.
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-6-22)returnnewCommand({
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-6-23)goto:"run_tool",
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-6-24)update:{messages:[updatedMsg]},
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-6-25)});
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-6-26)}
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-6-27)// Give natural language feedback, and then pass that back to the agent
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-6-28)elseif(reviewAction==="feedback"){
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-6-29)constfeedbackMsg=getFeedbackMsg(reviewData);
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-6-30)returnnewCommand({
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-6-31)goto:"call_llm",
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-6-32)update:{messages:[feedbackMsg]},
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-6-33)});
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-6-34)}
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-6-35)}

```


See [how to review tool calls](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls) for a more detailed example.

### Multi-turn conversation[¶](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#multi-turn-conversation "Permanent link")

![image](https://langchain-ai.github.io/langgraphjs/concepts/img/human_in_the_loop/multi-turn-conversation.png)

A **multi-turn conversation** architecture where an **agent** and **human node** cycle back and forth until the agent decides to hand off the conversation to another agent or another part of the system. 

A **multi-turn conversation** involves multiple back-and-forth interactions between an agent and a human, which can allow the agent to gather additional information from the human in a conversational manner.

This design pattern is useful in an LLM application consisting of [multiple agents](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/). One or more agents may need to carry out multi-turn conversations with a human, where the human provides input or feedback at different stages of the conversation. For simplicity, the agent implementation below is illustrated as a single node, but in reality it may be part of a larger graph consisting of multiple nodes and include a conditional edge.

[Using a human node per agent](#__tabbed_1_1)[Sharing human node across multiple agents](#__tabbed_1_2)

In this pattern, each agent has its own human node for collecting user input.

This can be achieved by either naming the human nodes with unique names (e.g., "human for agent 1", "human for agent 2") or by using subgraphs where a subgraph contains a human node and an agent node.

```
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-7-1)import{interrupt}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-7-2)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-7-3)functionhumanInput(state:typeofGraphAnnotation.State){
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-7-4)consthumanMessage=interrupt("human_input");
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-7-5)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-7-6)return{
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-7-7)messages:[
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-7-8){
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-7-9)role:"human",
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-7-10)content:humanMessage
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-7-11)}
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-7-12)]
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-7-13)};
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-7-14)}
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-7-15)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-7-16)functionagent(state:typeofGraphAnnotation.State){
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-7-17)// Agent logic
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-7-18)// ...
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-7-19)}
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-7-20)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-7-21)constgraph=graphBuilder
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-7-22).addNode("human_input",humanInput)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-7-23).addEdge("human_input","agent")
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-7-24).compile({checkpointer});
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-7-25)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-7-26)// After running the graph and hitting the interrupt, the graph will pause.
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-7-27)// Resume it with the human's input.
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-7-28)awaitgraph.invoke(
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-7-29)newCommand({resume:"hello!"}),
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-7-30)threadConfig
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-7-31));

```


In this pattern, a single human node is used to collect user input for multiple agents. The active agent is determined from the state, so after human input is collected, the graph can route to the correct agent.

```
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-8-1)import{interrupt,Command,MessagesAnnotation}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-8-2)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-8-3)functionhumanNode(state:typeofMessagesAnnotation.State):Command{
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-8-4)/**
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-8-5)  * A node for collecting user input.
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-8-6)  */
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-8-7)constuserInput=interrupt("Ready for user input.");
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-8-8)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-8-9)// Determine the **active agent** from the state, so
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-8-10)// we can route to the correct agent after collecting input.
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-8-11)// For example, add a field to the state or use the last active agent.
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-8-12)// or fill in `name` attribute of AI messages generated by the agents.
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-8-13)constactiveAgent=...;
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-8-14)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-8-15)returnnewCommand({
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-8-16)goto:activeAgent,
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-8-17)update:{
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-8-18)messages:[{
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-8-19)role:"human",
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-8-20)content:userInput,
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-8-21)}]
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-8-22)}
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-8-23)});
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-8-24)}

```


See [how to implement multi-turn conversations](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo) for a more detailed example.

### Validating human input[¶](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#validating-human-input "Permanent link")

If you need to validate the input provided by the human within the graph itself (rather than on the client side), you can achieve this by using multiple interrupt calls within a single node.

```
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-9-1)import{interrupt}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-9-2)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-9-3)functionhumanNode(state:typeofGraphAnnotation.State){
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-9-4)/**
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-9-5)  * Human node with validation.
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-9-6)  */
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-9-7)letquestion="What is your age?";
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-9-8)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-9-9)while(true){
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-9-10)constanswer=interrupt(question);
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-9-11)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-9-12)// Validate answer, if the answer isn't valid ask for input again.
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-9-13)if(typeofanswer!=="number"||answer<0){
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-9-14)question=`'${answer}' is not a valid age. What is your age?`;
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-9-15)continue;
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-9-16)}else{
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-9-17)// If the answer is valid, we can proceed.
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-9-18)break;
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-9-19)}
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-9-20)}
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-9-21)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-9-22)console.log(`The human in the loop is ${answer} years old.`);
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-9-23)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-9-24)return{
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-9-25)age:answer,
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-9-26)};
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-9-27)}

```


## The `Command` primitive[¶](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#the-command-primitive "Permanent link")

When using the `interrupt` function, the graph will pause at the interrupt and wait for user input.

Graph execution can be resumed using the [Command](https://langchain-ai.github.io/langgraphjs/reference/classes/langgraph.Command.html) primitive which can be passed through the `invoke` or `stream` methods.

The `Command` primitive provides several options to control and modify the graph's state during resumption:

  1. **Pass a value to the`interrupt`** : Provide data, such as a user's response, to the graph using `new Command({ resume: value })`. Execution resumes from the beginning of the node where the `interrupt` was used, however, this time the `interrupt(...)` call will return the value passed in the `new Command({ resume: value })` instead of pausing the graph.



```
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-10-1)// Resume graph execution with the user's input.
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-10-2)awaitgraph.invoke(newCommand({resume:{age:"25"}}),threadConfig);

```


  1. **Update the graph state** : Modify the graph state using `Command({ goto: ..., update: ... })`. Note that resumption starts from the beginning of the node where the `interrupt` was used. Execution resumes from the beginning of the node where the `interrupt` was used, but with the updated state.



```
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-11-1)// Update the graph state and resume.
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-11-2)// You must provide a `resume` value if using an `interrupt`.
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-11-3)awaitgraph.invoke(
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-11-4)newCommand({resume:"Let's go!!!",update:{foo:"bar"}}),
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-11-5)threadConfig
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-11-6));

```


By leveraging `Command`, you can resume graph execution, handle user inputs, and dynamically adjust the graph's state.

## Using with `invoke`[¶](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#using-with-invoke "Permanent link")

When you use `stream` to run the graph, you will receive an `Interrupt` event that let you know the `interrupt` was triggered.

`invoke` does not return the interrupt information. To access this information, you must use the [getState](https://langchain-ai.github.io/langgraphjs/reference/classes/langgraph.CompiledStateGraph.html#getState) method to retrieve the graph state after calling `invoke`.

```
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-12-1)// Run the graph up to the interrupt
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-12-2)constresult=awaitgraph.invoke(inputs,threadConfig);
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-12-3)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-12-4)// Get the graph state to get interrupt information.
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-12-5)conststate=awaitgraph.getState(threadConfig);
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-12-6)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-12-7)// Print the state values
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-12-8)console.log(state.values);
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-12-9)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-12-10)// Print the pending tasks
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-12-11)console.log(state.tasks);
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-12-12)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-12-13)// Resume the graph with the user's input.
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-12-14)awaitgraph.invoke(newCommand({resume:{age:"25"}}),threadConfig);

```


```
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-13-1){
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-13-2)foo:"bar";
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-13-3)}// State values
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-13-4)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-13-5)[
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-13-6){
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-13-7)id:"5d8ffc92-8011-0c9b-8b59-9d3545b7e553",
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-13-8)name:"node_foo",
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-13-9)path:["__pregel_pull","node_foo"],
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-13-10)error:null,
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-13-11)interrupts:[
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-13-12){
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-13-13)value:"value_in_interrupt",
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-13-14)resumable:true,
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-13-15)ns:["node_foo:5d8ffc92-8011-0c9b-8b59-9d3545b7e553"],
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-13-16)when:"during",
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-13-17)},
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-13-18)],
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-13-19)state:null,
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-13-20)result:null,
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-13-21)},
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-13-22)];// Pending tasks. interrupts

```


## How does resuming from an interrupt work?[¶](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#how-does-resuming-from-an-interrupt-work "Permanent link")

A critical aspect of using `interrupt` is understanding how resuming works. When you resume execution after an `interrupt`, graph execution starts from the **beginning** of the **graph node** where the last `interrupt` was triggered.

**All** code from the beginning of the node to the `interrupt` will be re-executed.

```
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-14-1)letcounter=0;
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-14-2)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-14-3)functionnode(state:State){
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-14-4)// All the code from the beginning of the node to the interrupt will be re-executed
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-14-5)// when the graph resumes.
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-14-6)counter+=1;
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-14-7)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-14-8)console.log(`> Entered the node: ${counter} # of times`);
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-14-9)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-14-10)// Pause the graph and wait for user input.
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-14-11)constanswer=interrupt();
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-14-12)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-14-13)console.log("The value of counter is:",counter);
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-14-14)// ...
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-14-15)}

```


Upon **resuming** the graph, the counter will be incremented a second time, resulting in the following output:

```
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-15-1)>Enteredthenode:2#oftimes
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-15-2)Thevalueofcounteris:2

```


## Common Pitfalls[¶](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#common-pitfalls "Permanent link")

### Side-effects[¶](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#side-effects "Permanent link")

Place code with side effects, such as API calls, **after** the `interrupt` to avoid duplication, as these are re-triggered every time the node is resumed.

[Side effects before interrupt (BAD)](#__tabbed_2_1)[Side effects after interrupt (OK)](#__tabbed_2_2)[Side effects in a separate node (OK)](#__tabbed_2_3)

This code will re-execute the API call another time when the node is resumed from the `interrupt`. This can be problematic if the API call is not idempotent or is just expensive.

```
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-16-1)import{interrupt}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-16-2)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-16-3)functionhumanNode(state:typeofGraphAnnotation.State){
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-16-4)/**
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-16-5)  * Human node with validation.
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-16-6)  */
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-16-7)apiCall();// This code will be re-executed when the node is resumed.
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-16-8)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-16-9)constanswer=interrupt(question);
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-16-10)}

```


```
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-17-1)import{interrupt}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-17-2)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-17-3)functionhumanNode(state:typeofGraphAnnotation.State){
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-17-4)/**
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-17-5)  * Human node with validation.
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-17-6)  */
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-17-7)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-17-8)constanswer=interrupt(question);
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-17-9)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-17-10)apiCall(answer);// OK as it's after the interrupt
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-17-11)}

```


```
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-18-1)import{interrupt}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-18-2)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-18-3)functionhumanNode(state:typeofGraphAnnotation.State){
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-18-4)/**
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-18-5)  * Human node with validation.
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-18-6)  */
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-18-7)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-18-8)constanswer=interrupt(question);
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-18-9)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-18-10)return{
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-18-11)answer
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-18-12)};
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-18-13)}
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-18-14)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-18-15)functionapiCallNode(state:typeofGraphAnnotation.State){
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-18-16)apiCall();// OK as it's in a separate node
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-18-17)}

```


### Subgraphs called as functions[¶](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#subgraphs-called-as-functions "Permanent link")

When invoking a subgraph [as a function](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#as-a-function), the **parent graph** will resume execution from the **beginning of the node** where the subgraph was invoked (and where an `interrupt` was triggered). Similarly, the **subgraph** , will resume from the **beginning of the node** where the `interrupt()` function was called.

For example,

```
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-19-1)asyncfunctionnodeInParentGraph(state:typeofGraphAnnotation.State){
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-19-2)someCode();// <-- This will re-execute when the subgraph is resumed.
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-19-3)// Invoke a subgraph as a function.
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-19-4)// The subgraph contains an `interrupt` call.
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-19-5)constsubgraphResult=awaitsubgraph.invoke(someInput);
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-19-6)...
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-19-7)}

```


**Example: Parent and Subgraph Execution Flow**

Say we have a parent graph with 3 nodes:

**Parent Graph** : `node_1` → `node_2` (subgraph call) → `node_3`

And the subgraph has 3 nodes, where the second node contains an `interrupt`:

**Subgraph** : `sub_node_1` → `sub_node_2` (`interrupt`) → `sub_node_3`

When resuming the graph, the execution will proceed as follows:

  1. **Skip`node_1`** in the parent graph (already executed, graph state was saved in snapshot).
  2. **Re-execute`node_2`** in the parent graph from the start.
  3. **Skip`sub_node_1`** in the subgraph (already executed, graph state was saved in snapshot).
  4. **Re-execute`sub_node_2`** in the subgraph from the beginning.
  5. Continue with `sub_node_3` and subsequent nodes.



Here is abbreviated example code that you can use to understand how subgraphs work with interrupts. It counts the number of times each node is entered and prints the count.

```
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-1)import{
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-2)StateGraph,
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-3)START,
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-4)interrupt,
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-5)Command,
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-6)MemorySaver,
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-7)Annotation
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-8)}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-9)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-10)constGraphAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-11)stateCounter:Annotation<number>({
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-12)reducer:(a,b)=>a+b,
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-13)default:()=>0
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-14)})
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-15)})
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-16)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-17)letcounterNodeInSubgraph=0;
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-18)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-19)functionnodeInSubgraph(state:typeofGraphAnnotation.State){
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-20)counterNodeInSubgraph+=1;// This code will **NOT** run again!
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-21)console.log(`Entered 'nodeInSubgraph' a total of ${counterNodeInSubgraph} times`);
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-22)return{};
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-23)}
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-24)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-25)letcounterHumanNode=0;
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-26)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-27)asyncfunctionhumanNode(state:typeofGraphAnnotation.State){
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-28)counterHumanNode+=1;// This code will run again!
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-29)console.log(`Entered humanNode in sub-graph a total of ${counterHumanNode} times`);
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-30)constanswer=awaitinterrupt("what is your name?");
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-31)console.log(`Got an answer of ${answer}`);
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-32)return{};
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-33)}
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-34)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-35)constcheckpointer=newMemorySaver();
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-36)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-37)constsubgraphBuilder=newStateGraph(GraphAnnotation)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-38).addNode("some_node",nodeInSubgraph)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-39).addNode("human_node",humanNode)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-40).addEdge(START,"some_node")
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-41).addEdge("some_node","human_node")
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-42)constsubgraph=subgraphBuilder.compile({checkpointer});
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-43)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-44)letcounterParentNode=0;
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-45)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-46)asyncfunctionparentNode(state:typeofGraphAnnotation.State){
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-47)counterParentNode+=1;// This code will run again on resuming!
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-48)console.log(`Entered 'parentNode' a total of ${counterParentNode} times`);
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-49)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-50)// Please note that we're intentionally incrementing the state counter
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-51)// in the graph state as well to demonstrate that the subgraph update
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-52)// of the same key will not conflict with the parent graph (until
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-53)constsubgraphState=awaitsubgraph.invoke(state);
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-54)returnsubgraphState;
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-55)}
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-56)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-57)constbuilder=newStateGraph(GraphAnnotation)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-58).addNode("parent_node",parentNode)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-59).addEdge(START,"parent_node")
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-60)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-61)// A checkpointer must be enabled for interrupts to work!
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-62)constgraph=builder.compile({checkpointer});
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-63)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-64)constconfig={
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-65)configurable:{
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-66)thread_id:crypto.randomUUID(),
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-67)}
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-68)};
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-69)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-70)forawait(constchunkofawaitgraph.stream({stateCounter:1},config)){
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-71)console.log(chunk);
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-72)}
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-73)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-74)console.log('--- Resuming ---');
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-75)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-76)forawait(constchunkofawaitgraph.stream(newCommand({resume:"35"}),config)){
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-77)console.log(chunk);
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-20-78)}

```


This will print out

```
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-21-1)---Firstinvocation---
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-21-2)Inparentnode:{foo:'bar'}
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-21-3)Entered'parentNode'atotalof1times
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-21-4)Entered'nodeInSubgraph'atotalof1times
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-21-5)EnteredhumanNodeinsub-graphatotalof1times
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-21-6){__interrupt__:[{value:'what is your name?',resumable:true,ns:['parent_node:0b23d72f-aaba-0329-1a59-ca4f3c8bad3b','human_node:25df717c-cb80-57b0-7410-44e20aac8f3c'],when:'during'}]}
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-21-7)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-21-8)---Resuming---
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-21-9)Inparentnode:{foo:'bar'}
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-21-10)Entered'parentNode'atotalof2times
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-21-11)EnteredhumanNodeinsub-graphatotalof2times
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-21-12)Gotananswerof35
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-21-13){parent_node:null}

```


### Using multiple interrupts[¶](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#using-multiple-interrupts "Permanent link")

Using multiple interrupts within a **single** node can be helpful for patterns like [validating human input](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#validating-human-input). However, using multiple interrupts in the same node can lead to unexpected behavior if not handled carefully.

When a node contains multiple interrupt calls, LangGraph keeps a list of resume values specific to the task executing the node. Whenever execution resumes, it starts at the beginning of the node. For each interrupt encountered, LangGraph checks if a matching value exists in the task's resume list. Matching is **strictly index-based** , so the order of interrupt calls within the node is critical.

To avoid issues, refrain from dynamically changing the node's structure between executions. This includes adding, removing, or reordering interrupt calls, as such changes can result in mismatched indices. These problems often arise from unconventional patterns, such as mutating state via `Command.resume(...).update(SOME_STATE_MUTATION)` or relying on global variables to modify the node's structure dynamically.

Example of incorrect code

```
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-1)import{v4asuuidv4}from"uuid";
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-2)import{
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-3)StateGraph,
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-4)MemorySaver,
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-5)START,
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-6)interrupt,
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-7)Command,
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-8)Annotation
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-9)}from"@langchain/langgraph";
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-10)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-11)constGraphAnnotation=Annotation.Root({
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-12)name:Annotation<string>(),
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-13)age:Annotation<string>()
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-14)});
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-15)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-16)functionhumanNode(state:typeofGraphAnnotation.State){
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-17)letname;
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-18)if(!state.name){
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-19)name=interrupt("what is your name?");
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-20)}else{
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-21)name="N/A";
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-22)}
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-23)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-24)letage;
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-25)if(!state.age){
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-26)age=interrupt("what is your age?");
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-27)}else{
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-28)age="N/A";
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-29)}
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-30)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-31)console.log(`Name: ${name}. Age: ${age}`);
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-32)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-33)return{
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-34)age,
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-35)name,
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-36)};
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-37)}
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-38)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-39)constbuilder=newStateGraph(GraphAnnotation)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-40).addNode("human_node",humanNode);
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-41).addEdge(START,"human_node");
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-42)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-43)// A checkpointer must be enabled for interrupts to work!
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-44)constcheckpointer=newMemorySaver();
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-45)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-46)constgraph=builder.compile({checkpointer});
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-47)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-48)constconfig={
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-49)configurable:{
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-50)thread_id:uuidv4(),
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-51)}
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-52)};
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-53)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-54)forawait(constchunkofawaitgraph.stream({age:undefined,name:undefined},config)){
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-55)console.log(chunk);
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-56)}
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-57)
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-58)forawait(constchunkofawaitgraph.stream(
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-59)newCommand({resume:"John",update:{name:"foo"}}),
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-60)config
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-61))){
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-62)console.log(chunk);
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-22-63)}

```


```
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-23-1){__interrupt__:[{
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-23-2)value:'what is your name?',
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-23-3)resumable:true,
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-23-4)ns:['human_node:3a007ef9-c30d-c357-1ec1-86a1a70d8fba'],
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-23-5)when:'during'
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-23-6)}]}
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-23-7)Name:N/A.Age:John
[](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__codelineno-23-8){human_node:{age:'John',name:'N/A'}}

```


## Additional Resources 📚[¶](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#additional-resources "Permanent link")

  * [**Conceptual Guide: Persistence**](https://langchain-ai.github.io/langgraphjs/concepts/persistence/#replay): Read the persistence guide for more context on replaying.

  * [**How to Guides: Human-in-the-loop**](https://langchain-ai.github.io/langgraphjs/how-tos/#human-in-the-loop): Learn how to implement human-in-the-loop workflows in LangGraph.

  * [**How to implement multi-turn conversations**](https://langchain-ai.github.io/langgraphjs/how-tos/multi-agent-multi-turn-convo): Learn how to implement multi-turn conversations in LangGraph.


Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

Back to top  [ Previous  Multi-agent Systems  ](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/) [ Next  Persistence  ](https://langchain-ai.github.io/langgraphjs/concepts/persistence/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraph/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraphjs "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
