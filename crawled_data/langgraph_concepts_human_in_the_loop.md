---
url: https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop
title: Untitled
date_crawled: 
---

[ Skip to content ](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#human-in-the-loop)

**Join us at[ Interrupt: The Agent AI Conference by LangChain](https://interrupt.langchain.com/) on May 13 & 14 in San Francisco!**

[ ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_dark.svg) ![logo](https://langchain-ai.github.io/langgraph/static/wordmark_light.svg) ](https://langchain-ai.github.io/langgraph/)

Human-in-the-loop 

[ ](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/?q= "Share")

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

Concepts 
        * LangGraph  LangGraph 
          * [ LangGraph  ](https://langchain-ai.github.io/langgraph/concepts#langgraph)
          * [ Why LangGraph?  ](https://langchain-ai.github.io/langgraph/concepts/high_level/)
          * [ LangGraph Glossary  ](https://langchain-ai.github.io/langgraph/concepts/low_level/)
          * [ Agent architectures  ](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/)
          * [ Multi-agent Systems  ](https://langchain-ai.github.io/langgraph/concepts/multi_agent/)
          * [ None  ](https://langchain-ai.github.io/langgraph/concepts/breakpoints)
          * Human-in-the-loop  [ Human-in-the-loop  ](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/) Table of contents 
            * [ Use cases  ](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#use-cases)
            * [ interrupt  ](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#interrupt)
            * [ Requirements  ](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#requirements)
            * [ Design Patterns  ](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#design-patterns)
              * [ Approve or Reject  ](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#approve-or-reject)
              * [ Review & Edit State  ](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#review-edit-state)
              * [ Review Tool Calls  ](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#review-tool-calls)
              * [ Multi-turn conversation  ](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#multi-turn-conversation)
              * [ Validating human input  ](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#validating-human-input)
            * [ The Command primitive  ](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#the-command-primitive)
            * [ Using with invoke and ainvoke  ](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#using-with-invoke-and-ainvoke)
            * [ How does resuming from an interrupt work?  ](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#how-does-resuming-from-an-interrupt-work)
            * [ Common Pitfalls  ](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#common-pitfalls)
              * [ Side-effects  ](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#side-effects)
              * [ Subgraphs called as functions  ](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#subgraphs-called-as-functions)
              * [ Using multiple interrupts  ](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#using-multiple-interrupts)
            * [ Additional Resources 📚  ](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#additional-resources)
          * [ Time Travel ⏱️  ](https://langchain-ai.github.io/langgraph/concepts/time-travel/)
          * [ Persistence  ](https://langchain-ai.github.io/langgraph/concepts/persistence/)
          * [ Memory  ](https://langchain-ai.github.io/langgraph/concepts/memory/)
          * [ Streaming  ](https://langchain-ai.github.io/langgraph/concepts/streaming/)
          * [ Functional API  ](https://langchain-ai.github.io/langgraph/concepts/functional_api/)
        * [ LangGraph Platform  ](https://langchain-ai.github.io/langgraph/concepts#langgraph-platform)
      * [ Tutorials  ](https://langchain-ai.github.io/langgraph/tutorials/)
    * Resources  Resources 
      * [ Prebuilt Agents  ](https://langchain-ai.github.io/langgraph/prebuilt/)
      * [ Adopters  ](https://langchain-ai.github.io/langgraph/adopters/)
      * [ FAQ  ](https://langchain-ai.github.io/langgraph/concepts/faq/)
      * [ Troubleshooting  ](https://langchain-ai.github.io/langgraph/troubleshooting/errors/)
      * [ LangGraph Academy Course  ](https://academy.langchain.com/courses/intro-to-langgraph)
  * [ API reference  ](https://langchain-ai.github.io/langgraph/reference/graphs/)



Table of contents 

  * [ Use cases  ](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#use-cases)
  * [ interrupt  ](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#interrupt)
  * [ Requirements  ](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#requirements)
  * [ Design Patterns  ](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#design-patterns)
    * [ Approve or Reject  ](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#approve-or-reject)
    * [ Review & Edit State  ](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#review-edit-state)
    * [ Review Tool Calls  ](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#review-tool-calls)
    * [ Multi-turn conversation  ](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#multi-turn-conversation)
    * [ Validating human input  ](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#validating-human-input)
  * [ The Command primitive  ](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#the-command-primitive)
  * [ Using with invoke and ainvoke  ](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#using-with-invoke-and-ainvoke)
  * [ How does resuming from an interrupt work?  ](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#how-does-resuming-from-an-interrupt-work)
  * [ Common Pitfalls  ](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#common-pitfalls)
    * [ Side-effects  ](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#side-effects)
    * [ Subgraphs called as functions  ](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#subgraphs-called-as-functions)
    * [ Using multiple interrupts  ](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#using-multiple-interrupts)
  * [ Additional Resources 📚  ](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#additional-resources)



  1. [ Home  ](https://langchain-ai.github.io/langgraph/)
  2. [ Guides  ](https://langchain-ai.github.io/langgraph/how-tos/)
  3. [ Concepts  ](https://langchain-ai.github.io/langgraph/concepts/)
  4. [ LangGraph  ](https://langchain-ai.github.io/langgraph/concepts#langgraph)

[ ](https://github.com/langchain-ai/langgraph/edit/main/docs/docs/concepts/human_in_the_loop.md "Edit this page")

# Human-in-the-loop[¶](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#human-in-the-loop "Permanent link")

This guide uses the new `interrupt` function.

As of LangGraph 0.2.57, the recommended way to set breakpoints is using the `interrupt`[ function](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.interrupt) as it simplifies **human-in-the-loop** patterns.

If you're looking for the previous version of this conceptual guide, which relied on static breakpoints and `NodeInterrupt` exception, it is available [here](https://langchain-ai.github.io/langgraph/concepts/v0-human-in-the-loop/). 

A **human-in-the-loop** (or "on-the-loop") workflow integrates human input into automated processes, allowing for decisions, validation, or corrections at key stages. This is especially useful in **LLM-based applications** , where the underlying model may generate occasional inaccuracies. In low-error-tolerance scenarios like compliance, decision-making, or content generation, human involvement ensures reliability by enabling review, correction, or override of model outputs.

## Use cases[¶](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#use-cases "Permanent link")

Key use cases for **human-in-the-loop** workflows in LLM-based applications include:

  1. [**🛠️ Reviewing tool calls**](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#review-tool-calls): Humans can review, edit, or approve tool calls requested by the LLM before tool execution.
  2. **✅ Validating LLM outputs** : Humans can review, edit, or approve content generated by the LLM.
  3. **💡 Providing context** : Enable the LLM to explicitly request human input for clarification or additional details or to support multi-turn conversations.



## `interrupt`[¶](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#interrupt "Permanent link")

The `interrupt`[ function](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.interrupt) in LangGraph enables human-in-the-loop workflows by pausing the graph at a specific node, presenting information to a human, and resuming the graph with their input. This function is useful for tasks like approvals, edits, or collecting additional input. The `interrupt`[ function](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.interrupt) is used in conjunction with the `Command`[](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Command) object to resume the graph with a value provided by the human.

```
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-0-1)fromlanggraph.typesimport interrupt
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-0-2)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-0-3)defhuman_node(state: State):
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-0-4)  value = interrupt(
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-0-5)    # Any JSON serializable value to surface to the human.
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-0-6)    # For example, a question or a piece of text or a set of keys in the state
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-0-7)    {
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-0-8)     "text_to_revise": state["some_text"]
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-0-9)    }
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-0-10)  )
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-0-11)  # Update the state with the human's input or route the graph based on the input.
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-0-12)  return {
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-0-13)    "some_text": value
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-0-14)  }
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-0-15)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-0-16)graph = graph_builder.compile(
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-0-17)  checkpointer=checkpointer # Required for `interrupt` to work
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-0-18))
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-0-19)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-0-20)# Run the graph until the interrupt
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-0-21)thread_config = {"configurable": {"thread_id": "some_id"}}
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-0-22)graph.invoke(some_input, config=thread_config)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-0-23)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-0-24)# Resume the graph with the human's input
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-0-25)graph.invoke(Command(resume=value_from_human), config=thread_config)

```


API Reference: [interrupt](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.interrupt)

```
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-1-1){'some_text': 'Edited text'}

```


Warning

Interrupts are both powerful and ergonomic. However, while they may resemble Python's input() function in terms of developer experience, it's important to note that they do not automatically resume execution from the interruption point. Instead, they rerun the entire node where the interrupt was used. For this reason, interrupts are typically best placed at the start of a node or in a dedicated node. Please read the [resuming from an interrupt](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#how-does-resuming-from-an-interrupt-work) section for more details. 

Full Code

Here's a full example of how to use `interrupt` in a graph, if you'd like to see the code in action.

```
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-2-1)fromtypingimport TypedDict
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-2-2)importuuid
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-2-3)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-2-4)fromlanggraph.checkpoint.memoryimport MemorySaver
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-2-5)fromlanggraph.constantsimport START
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-2-6)fromlanggraph.graphimport StateGraph
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-2-7)fromlanggraph.typesimport interrupt, Command
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-2-8)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-2-9)classState(TypedDict):
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-2-10)"""The graph state."""
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-2-11)  some_text: str
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-2-12)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-2-13)defhuman_node(state: State):
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-2-14)  value = interrupt(
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-2-15)   # Any JSON serializable value to surface to the human.
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-2-16)   # For example, a question or a piece of text or a set of keys in the state
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-2-17)   {
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-2-18)     "text_to_revise": state["some_text"]
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-2-19)   }
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-2-20)  )
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-2-21)  return {
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-2-22)   # Update the state with the human's input
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-2-23)   "some_text": value
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-2-24)  }
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-2-25)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-2-26)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-2-27)# Build the graph
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-2-28)graph_builder = StateGraph(State)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-2-29)# Add the human-node to the graph
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-2-30)graph_builder.add_node("human_node", human_node)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-2-31)graph_builder.add_edge(START, "human_node")
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-2-32)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-2-33)# A checkpointer is required for `interrupt` to work.
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-2-34)checkpointer = MemorySaver()
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-2-35)graph = graph_builder.compile(
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-2-36)  checkpointer=checkpointer
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-2-37))
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-2-38)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-2-39)# Pass a thread ID to the graph to run it.
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-2-40)thread_config = {"configurable": {"thread_id": uuid.uuid4()}}
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-2-41)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-2-42)# Using stream() to directly surface the `__interrupt__` information.
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-2-43)for chunk in graph.stream({"some_text": "Original text"}, config=thread_config):
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-2-44)  print(chunk)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-2-45)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-2-46)# Resume using Command
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-2-47)for chunk in graph.stream(Command(resume="Edited text"), config=thread_config):
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-2-48)  print(chunk)

```


API Reference: [MemorySaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.MemorySaver) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [interrupt](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.interrupt) | [Command](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Command)

```
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-3-1){'__interrupt__': (
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-3-2)   Interrupt(
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-3-3)     value={'question': 'Please revise the text', 'some_text': 'Original text'}, 
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-3-4)     resumable=True, 
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-3-5)     ns=['human_node:10fe492f-3688-c8c6-0d0a-ec61a43fecd6'], 
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-3-6)     when='during'
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-3-7)   ),
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-3-8)  )
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-3-9)}
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-3-10){'human_node': {'some_text': 'Edited text'}}

```


## Requirements[¶](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#requirements "Permanent link")

To use `interrupt` in your graph, you need to:

  1. [**Specify a checkpointer**](https://langchain-ai.github.io/langgraph/concepts/persistence/#checkpoints) to save the graph state after each step.
  2. **Call`interrupt()`** in the appropriate place. See the [Design Patterns](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#design-patterns) section for examples.
  3. **Run the graph** with a [**thread ID**](https://langchain-ai.github.io/langgraph/concepts/persistence/#threads) until the `interrupt` is hit.
  4. **Resume execution** using `invoke`/`ainvoke`/`stream`/`astream` (see [**The`Command` primitive**](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#the-command-primitive)).



## Design Patterns[¶](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#design-patterns "Permanent link")

There are typically three different **actions** that you can do with a human-in-the-loop workflow:

  1. **Approve or Reject** : Pause the graph before a critical step, such as an API call, to review and approve the action. If the action is rejected, you can prevent the graph from executing the step, and potentially take an alternative action. This pattern often involve **routing** the graph based on the human's input.
  2. **Edit Graph State** : Pause the graph to review and edit the graph state. This is useful for correcting mistakes or updating the state with additional information. This pattern often involves **updating** the state with the human's input.
  3. **Get Input** : Explicitly request human input at a particular step in the graph. This is useful for collecting additional information or context to inform the agent's decision-making process or for supporting **multi-turn conversations**.



Below we show different design patterns that can be implemented using these **actions**.

### Approve or Reject[¶](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#approve-or-reject "Permanent link")

![image](https://langchain-ai.github.io/langgraph/concepts/img/human_in_the_loop/approve-or-reject.png)

Depending on the human's approval or rejection, the graph can proceed with the action or take an alternative path.

Pause the graph before a critical step, such as an API call, to review and approve the action. If the action is rejected, you can prevent the graph from executing the step, and potentially take an alternative action.

```
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-4-1)fromtypingimport Literal
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-4-2)fromlanggraph.typesimport interrupt, Command
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-4-3)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-4-4)defhuman_approval(state: State) -> Command[Literal["some_node", "another_node"]]:
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-4-5)  is_approved = interrupt(
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-4-6)    {
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-4-7)      "question": "Is this correct?",
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-4-8)      # Surface the output that should be
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-4-9)      # reviewed and approved by the human.
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-4-10)      "llm_output": state["llm_output"]
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-4-11)    }
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-4-12)  )
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-4-13)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-4-14)  if is_approved:
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-4-15)    return Command(goto="some_node")
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-4-16)  else:
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-4-17)    return Command(goto="another_node")
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-4-18)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-4-19)# Add the node to the graph in an appropriate location
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-4-20)# and connect it to the relevant nodes.
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-4-21)graph_builder.add_node("human_approval", human_approval)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-4-22)graph = graph_builder.compile(checkpointer=checkpointer)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-4-23)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-4-24)# After running the graph and hitting the interrupt, the graph will pause.
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-4-25)# Resume it with either an approval or rejection.
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-4-26)thread_config = {"configurable": {"thread_id": "some_id"}}
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-4-27)graph.invoke(Command(resume=True), config=thread_config)

```


API Reference: [interrupt](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.interrupt) | [Command](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Command)

See [how to review tool calls](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/) for a more detailed example.

### Review & Edit State[¶](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#review-edit-state "Permanent link")

![image](https://langchain-ai.github.io/langgraph/concepts/img/human_in_the_loop/edit-graph-state-simple.png)

A human can review and edit the state of the graph. This is useful for correcting mistakes or updating the state with additional information. 

```
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-5-1)fromlanggraph.typesimport interrupt
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-5-2)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-5-3)defhuman_editing(state: State):
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-5-4)  ...
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-5-5)  result = interrupt(
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-5-6)    # Interrupt information to surface to the client.
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-5-7)    # Can be any JSON serializable value.
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-5-8)    {
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-5-9)      "task": "Review the output from the LLM and make any necessary edits.",
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-5-10)      "llm_generated_summary": state["llm_generated_summary"]
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-5-11)    }
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-5-12)  )
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-5-13)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-5-14)  # Update the state with the edited text
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-5-15)  return {
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-5-16)    "llm_generated_summary": result["edited_text"] 
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-5-17)  }
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-5-18)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-5-19)# Add the node to the graph in an appropriate location
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-5-20)# and connect it to the relevant nodes.
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-5-21)graph_builder.add_node("human_editing", human_editing)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-5-22)graph = graph_builder.compile(checkpointer=checkpointer)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-5-23)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-5-24)...
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-5-25)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-5-26)# After running the graph and hitting the interrupt, the graph will pause.
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-5-27)# Resume it with the edited text.
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-5-28)thread_config = {"configurable": {"thread_id": "some_id"}}
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-5-29)graph.invoke(
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-5-30)  Command(resume={"edited_text": "The edited text"}), 
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-5-31)  config=thread_config
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-5-32))

```


API Reference: [interrupt](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.interrupt)

See [How to wait for user input using interrupt](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/) for a more detailed example.

### Review Tool Calls[¶](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#review-tool-calls "Permanent link")

![image](https://langchain-ai.github.io/langgraph/concepts/img/human_in_the_loop/tool-call-review.png)

A human can review and edit the output from the LLM before proceeding. This is particularly critical in applications where the tool calls requested by the LLM may be sensitive or require human oversight. 

```
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-6-1)defhuman_review_node(state) -> Command[Literal["call_llm", "run_tool"]]:
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-6-2)  # This is the value we'll be providing via Command(resume=<human_review>)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-6-3)  human_review = interrupt(
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-6-4)    {
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-6-5)      "question": "Is this correct?",
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-6-6)      # Surface tool calls for review
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-6-7)      "tool_call": tool_call
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-6-8)    }
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-6-9)  )
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-6-10)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-6-11)  review_action, review_data = human_review
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-6-12)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-6-13)  # Approve the tool call and continue
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-6-14)  if review_action == "continue":
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-6-15)    return Command(goto="run_tool")
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-6-16)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-6-17)  # Modify the tool call manually and then continue
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-6-18)  elif review_action == "update":
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-6-19)    ...
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-6-20)    updated_msg = get_updated_msg(review_data)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-6-21)    # Remember that to modify an existing message you will need
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-6-22)    # to pass the message with a matching ID.
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-6-23)    return Command(goto="run_tool", update={"messages": [updated_message]})
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-6-24)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-6-25)  # Give natural language feedback, and then pass that back to the agent
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-6-26)  elif review_action == "feedback":
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-6-27)    ...
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-6-28)    feedback_msg = get_feedback_msg(review_data)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-6-29)    return Command(goto="call_llm", update={"messages": [feedback_msg]})

```


See [how to review tool calls](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/review-tool-calls/) for a more detailed example.

### Multi-turn conversation[¶](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#multi-turn-conversation "Permanent link")

![image](https://langchain-ai.github.io/langgraph/concepts/img/human_in_the_loop/multi-turn-conversation.png)

A **multi-turn conversation** architecture where an **agent** and **human node** cycle back and forth until the agent decides to hand off the conversation to another agent or another part of the system. 

A **multi-turn conversation** involves multiple back-and-forth interactions between an agent and a human, which can allow the agent to gather additional information from the human in a conversational manner.

This design pattern is useful in an LLM application consisting of [multiple agents](https://langchain-ai.github.io/langgraph/concepts/multi_agent/). One or more agents may need to carry out multi-turn conversations with a human, where the human provides input or feedback at different stages of the conversation. For simplicity, the agent implementation below is illustrated as a single node, but in reality it may be part of a larger graph consisting of multiple nodes and include a conditional edge.

[Using a human node per agent](#__tabbed_1_1)[Sharing human node across multiple agents](#__tabbed_1_2)

In this pattern, each agent has its own human node for collecting user input. This can be achieved by either naming the human nodes with unique names (e.g., "human for agent 1", "human for agent 2") or by using subgraphs where a subgraph contains a human node and an agent node.

```
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-7-1)fromlanggraph.typesimport interrupt
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-7-2)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-7-3)defhuman_input(state: State):
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-7-4)  human_message = interrupt("human_input")
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-7-5)  return {
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-7-6)    "messages": [
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-7-7)      {
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-7-8)        "role": "human",
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-7-9)        "content": human_message
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-7-10)      }
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-7-11)    ]
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-7-12)  }
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-7-13)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-7-14)defagent(state: State):
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-7-15)  # Agent logic
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-7-16)  ...
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-7-17)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-7-18)graph_builder.add_node("human_input", human_input)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-7-19)graph_builder.add_edge("human_input", "agent")
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-7-20)graph = graph_builder.compile(checkpointer=checkpointer)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-7-21)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-7-22)# After running the graph and hitting the interrupt, the graph will pause.
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-7-23)# Resume it with the human's input.
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-7-24)graph.invoke(
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-7-25)  Command(resume="hello!"),
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-7-26)  config=thread_config
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-7-27))

```


API Reference: [interrupt](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.interrupt)

In this pattern, a single human node is used to collect user input for multiple agents. The active agent is determined from the state, so after human input is collected, the graph can route to the correct agent.

```
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-8-1)fromlanggraph.typesimport interrupt
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-8-2)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-8-3)defhuman_node(state: MessagesState) -> Command[Literal["agent_1", "agent_2", ...]]:
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-8-4)"""A node for collecting user input."""
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-8-5)  user_input = interrupt(value="Ready for user input.")
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-8-6)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-8-7)  # Determine the **active agent** from the state, so 
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-8-8)  # we can route to the correct agent after collecting input.
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-8-9)  # For example, add a field to the state or use the last active agent.
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-8-10)  # or fill in `name` attribute of AI messages generated by the agents.
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-8-11)  active_agent = ... 
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-8-12)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-8-13)  return Command(
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-8-14)    update={
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-8-15)      "messages": [{
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-8-16)        "role": "human",
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-8-17)        "content": user_input,
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-8-18)      }]
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-8-19)    },
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-8-20)    goto=active_agent,
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-8-21)  )

```


API Reference: [interrupt](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.interrupt)

See [how to implement multi-turn conversations](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/) for a more detailed example.

### Validating human input[¶](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#validating-human-input "Permanent link")

If you need to validate the input provided by the human within the graph itself (rather than on the client side), you can achieve this by using multiple interrupt calls within a single node.

```
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-9-1)fromlanggraph.typesimport interrupt
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-9-2)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-9-3)defhuman_node(state: State):
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-9-4)"""Human node with validation."""
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-9-5)  question = "What is your age?"
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-9-6)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-9-7)  while True:
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-9-8)    answer = interrupt(question)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-9-9)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-9-10)    # Validate answer, if the answer isn't valid ask for input again.
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-9-11)    if not isinstance(answer, int) or answer < 0:
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-9-12)      question = f"'{answer} is not a valid age. What is your age?"
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-9-13)      answer = None
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-9-14)      continue
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-9-15)    else:
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-9-16)      # If the answer is valid, we can proceed.
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-9-17)      break
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-9-18)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-9-19)  print(f"The human in the loop is {answer} years old.")
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-9-20)  return {
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-9-21)    "age": answer
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-9-22)  }

```


API Reference: [interrupt](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.interrupt)

## The `Command` primitive[¶](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#the-command-primitive "Permanent link")

When using the `interrupt` function, the graph will pause at the interrupt and wait for user input.

Graph execution can be resumed using the [Command](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Command) primitive which can be passed through the `invoke`, `ainvoke`, `stream` or `astream` methods.

The `Command` primitive provides several options to control and modify the graph's state during resumption:

  1. **Pass a value to the`interrupt`** : Provide data, such as a user's response, to the graph using `Command(resume=value)`. Execution resumes from the beginning of the node where the `interrupt` was used, however, this time the `interrupt(...)` call will return the value passed in the `Command(resume=value)` instead of pausing the graph.

```
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-10-1)# Resume graph execution with the user's input.
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-10-2)graph.invoke(Command(resume={"age": "25"}), thread_config)

```


  2. **Update the graph state** : Modify the graph state using `Command(update=update)`. Note that resumption starts from the beginning of the node where the `interrupt` was used. Execution resumes from the beginning of the node where the `interrupt` was used, but with the updated state.

```
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-11-1)# Update the graph state and resume.
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-11-2)# You must provide a `resume` value if using an `interrupt`.
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-11-3)graph.invoke(Command(update={"foo": "bar"}, resume="Let's go!!!"), thread_config)

```





By leveraging `Command`, you can resume graph execution, handle user inputs, and dynamically adjust the graph's state.

## Using with `invoke` and `ainvoke`[¶](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#using-with-invoke-and-ainvoke "Permanent link")

When you use `stream` or `astream` to run the graph, you will receive an `Interrupt` event that let you know the `interrupt` was triggered. 

`invoke` and `ainvoke` do not return the interrupt information. To access this information, you must use the [get_state](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.graph.CompiledGraph.get_state) method to retrieve the graph state after calling `invoke` or `ainvoke`.

```
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-12-1)# Run the graph up to the interrupt 
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-12-2)result = graph.invoke(inputs, thread_config)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-12-3)# Get the graph state to get interrupt information.
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-12-4)state = graph.get_state(thread_config)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-12-5)# Print the state values
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-12-6)print(state.values)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-12-7)# Print the pending tasks
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-12-8)print(state.tasks)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-12-9)# Resume the graph with the user's input.
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-12-10)graph.invoke(Command(resume={"age": "25"}), thread_config)

```


```
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-13-1){'foo': 'bar'} # State values
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-13-2)(
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-13-3)  PregelTask(
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-13-4)    id='5d8ffc92-8011-0c9b-8b59-9d3545b7e553', 
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-13-5)    name='node_foo', 
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-13-6)    path=('__pregel_pull', 'node_foo'), 
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-13-7)    error=None, 
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-13-8)    interrupts=(Interrupt(value='value_in_interrupt', resumable=True, ns=['node_foo:5d8ffc92-8011-0c9b-8b59-9d3545b7e553'], when='during'),), state=None, 
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-13-9)    result=None
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-13-10)  ),
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-13-11)) # Pending tasks. interrupts 

```


## How does resuming from an interrupt work?[¶](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#how-does-resuming-from-an-interrupt-work "Permanent link")

Warning

Resuming from an `interrupt` is **different** from Python's `input()` function, where execution resumes from the exact point where the `input()` function was called.

A critical aspect of using `interrupt` is understanding how resuming works. When you resume execution after an `interrupt`, graph execution starts from the **beginning** of the **graph node** where the last `interrupt` was triggered.

**All** code from the beginning of the node to the `interrupt` will be re-executed.

```
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-14-1)counter = 0
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-14-2)defnode(state: State):
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-14-3)  # All the code from the beginning of the node to the interrupt will be re-executed
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-14-4)  # when the graph resumes.
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-14-5)  global counter
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-14-6)  counter += 1
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-14-7)  print(f"> Entered the node: {counter} # of times")
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-14-8)  # Pause the graph and wait for user input.
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-14-9)  answer = interrupt()
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-14-10)  print("The value of counter is:", counter)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-14-11)  ...

```


Upon **resuming** the graph, the counter will be incremented a second time, resulting in the following output:

```
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-15-1)> Entered the node: 2 # of times
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-15-2)The value of counter is: 2

```


## Common Pitfalls[¶](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#common-pitfalls "Permanent link")

### Side-effects[¶](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#side-effects "Permanent link")

Place code with side effects, such as API calls, **after** the `interrupt` to avoid duplication, as these are re-triggered every time the node is resumed. 

[Side effects before interrupt (BAD)](#__tabbed_2_1)[Side effects after interrupt (OK)](#__tabbed_2_2)[Side effects in a separate node (OK)](#__tabbed_2_3)

This code will re-execute the API call another time when the node is resumed from the `interrupt`.

This can be problematic if the API call is not idempotent or is just expensive.

```
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-16-1)fromlanggraph.typesimport interrupt
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-16-2)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-16-3)defhuman_node(state: State):
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-16-4)"""Human node with validation."""
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-16-5)  api_call(...) # This code will be re-executed when the node is resumed.
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-16-6)  answer = interrupt(question)

```


API Reference: [interrupt](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.interrupt)

```
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-17-1)fromlanggraph.typesimport interrupt
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-17-2)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-17-3)defhuman_node(state: State):
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-17-4)"""Human node with validation."""
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-17-5)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-17-6)  answer = interrupt(question)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-17-7)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-17-8)  api_call(answer) # OK as it's after the interrupt

```


API Reference: [interrupt](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.interrupt)

```
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-18-1)fromlanggraph.typesimport interrupt
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-18-2)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-18-3)defhuman_node(state: State):
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-18-4)"""Human node with validation."""
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-18-5)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-18-6)  answer = interrupt(question)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-18-7)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-18-8)  return {
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-18-9)    "answer": answer
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-18-10)  }
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-18-11)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-18-12)defapi_call_node(state: State):
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-18-13)  api_call(...) # OK as it's in a separate node

```


API Reference: [interrupt](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.interrupt)

### Subgraphs called as functions[¶](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#subgraphs-called-as-functions "Permanent link")

When invoking a subgraph [as a function](https://langchain-ai.github.io/langgraph/concepts/low_level/#as-a-function), the **parent graph** will resume execution from the **beginning of the node** where the subgraph was invoked (and where an `interrupt` was triggered). Similarly, the **subgraph** , will resume from the **beginning of the node** where the `interrupt()` function was called.

For example,

```
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-19-1)defnode_in_parent_graph(state: State):
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-19-2)  some_code() # <-- This will re-execute when the subgraph is resumed.
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-19-3)  # Invoke a subgraph as a function.
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-19-4)  # The subgraph contains an `interrupt` call.
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-19-5)  subgraph_result = subgraph.invoke(some_input)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-19-6)  ...

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
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-1)importuuid
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-2)fromtypingimport TypedDict
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-3)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-4)fromlanggraph.graphimport StateGraph
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-5)fromlanggraph.constantsimport START
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-6)fromlanggraph.typesimport interrupt, Command
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-7)fromlanggraph.checkpoint.memoryimport MemorySaver
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-8)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-9)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-10)classState(TypedDict):
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-11)"""The graph state."""
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-12)  state_counter: int
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-13)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-14)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-15)counter_node_in_subgraph = 0
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-16)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-17)defnode_in_subgraph(state: State):
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-18)"""A node in the sub-graph."""
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-19)  global counter_node_in_subgraph
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-20)  counter_node_in_subgraph += 1 # This code will **NOT** run again!
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-21)  print(f"Entered `node_in_subgraph` a total of {counter_node_in_subgraph} times")
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-22)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-23)counter_human_node = 0
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-24)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-25)defhuman_node(state: State):
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-26)  global counter_human_node
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-27)  counter_human_node += 1 # This code will run again!
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-28)  print(f"Entered human_node in sub-graph a total of {counter_human_node} times")
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-29)  answer = interrupt("what is your name?")
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-30)  print(f"Got an answer of {answer}")
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-31)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-32)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-33)checkpointer = MemorySaver()
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-34)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-35)subgraph_builder = StateGraph(State)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-36)subgraph_builder.add_node("some_node", node_in_subgraph)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-37)subgraph_builder.add_node("human_node", human_node)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-38)subgraph_builder.add_edge(START, "some_node")
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-39)subgraph_builder.add_edge("some_node", "human_node")
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-40)subgraph = subgraph_builder.compile(checkpointer=checkpointer)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-41)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-42)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-43)counter_parent_node = 0
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-44)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-45)defparent_node(state: State):
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-46)"""This parent node will invoke the subgraph."""
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-47)  global counter_parent_node
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-48)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-49)  counter_parent_node += 1 # This code will run again on resuming!
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-50)  print(f"Entered `parent_node` a total of {counter_parent_node} times")
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-51)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-52)  # Please note that we're intentionally incrementing the state counter
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-53)  # in the graph state as well to demonstrate that the subgraph update
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-54)  # of the same key will not conflict with the parent graph (until
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-55)  subgraph_state = subgraph.invoke(state)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-56)  return subgraph_state
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-57)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-58)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-59)builder = StateGraph(State)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-60)builder.add_node("parent_node", parent_node)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-61)builder.add_edge(START, "parent_node")
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-62)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-63)# A checkpointer must be enabled for interrupts to work!
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-64)checkpointer = MemorySaver()
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-65)graph = builder.compile(checkpointer=checkpointer)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-66)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-67)config = {
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-68)  "configurable": {
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-69)   "thread_id": uuid.uuid4(),
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-70)  }
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-71)}
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-72)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-73)for chunk in graph.stream({"state_counter": 1}, config):
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-74)  print(chunk)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-75)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-76)print('--- Resuming ---')
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-77)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-78)for chunk in graph.stream(Command(resume="35"), config):
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-20-79)  print(chunk)

```


API Reference: [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [interrupt](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.interrupt) | [Command](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Command) | [MemorySaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.MemorySaver)

This will print out

```
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-21-1)--- First invocation ---
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-21-2)In parent node: {'foo': 'bar'}
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-21-3)Entered `parent_node` a total of 1 times
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-21-4)Entered `node_in_subgraph` a total of 1 times
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-21-5)Entered human_node in sub-graph a total of 1 times
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-21-6){'__interrupt__': (Interrupt(value='what is your name?', resumable=True, ns=['parent_node:0b23d72f-aaba-0329-1a59-ca4f3c8bad3b', 'human_node:25df717c-cb80-57b0-7410-44e20aac8f3c'], when='during'),)}
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-21-7)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-21-8)--- Resuming ---
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-21-9)In parent node: {'foo': 'bar'}
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-21-10)Entered `parent_node` a total of 2 times
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-21-11)Entered human_node in sub-graph a total of 2 times
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-21-12)Got an answer of 35
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-21-13){'parent_node': None} 

```


### Using multiple interrupts[¶](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#using-multiple-interrupts "Permanent link")

Using multiple interrupts within a **single** node can be helpful for patterns like [validating human input](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#validating-human-input). However, using multiple interrupts in the same node can lead to unexpected behavior if not handled carefully.

When a node contains multiple interrupt calls, LangGraph keeps a list of resume values specific to the task executing the node. Whenever execution resumes, it starts at the beginning of the node. For each interrupt encountered, LangGraph checks if a matching value exists in the task's resume list. Matching is **strictly index-based** , so the order of interrupt calls within the node is critical.

To avoid issues, refrain from dynamically changing the node's structure between executions. This includes adding, removing, or reordering interrupt calls, as such changes can result in mismatched indices. These problems often arise from unconventional patterns, such as mutating state via `Command(resume=..., update=SOME_STATE_MUTATION)` or relying on global variables to modify the node’s structure dynamically.

Example of incorrect code

```
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-22-1)importuuid
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-22-2)fromtypingimport TypedDict, Optional
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-22-3)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-22-4)fromlanggraph.graphimport StateGraph
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-22-5)fromlanggraph.constantsimport START 
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-22-6)fromlanggraph.typesimport interrupt, Command
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-22-7)fromlanggraph.checkpoint.memoryimport MemorySaver
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-22-8)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-22-9)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-22-10)classState(TypedDict):
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-22-11)"""The graph state."""
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-22-12)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-22-13)  age: Optional[str]
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-22-14)  name: Optional[str]
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-22-15)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-22-16)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-22-17)defhuman_node(state: State):
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-22-18)  if not state.get('name'):
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-22-19)    name = interrupt("what is your name?")
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-22-20)  else:
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-22-21)    name = "N/A"
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-22-22)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-22-23)  if not state.get('age'):
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-22-24)    age = interrupt("what is your age?")
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-22-25)  else:
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-22-26)    age = "N/A"
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-22-27)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-22-28)  print(f"Name: {name}. Age: {age}")
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-22-29)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-22-30)  return {
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-22-31)    "age": age,
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-22-32)    "name": name,
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-22-33)  }
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-22-34)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-22-35)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-22-36)builder = StateGraph(State)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-22-37)builder.add_node("human_node", human_node)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-22-38)builder.add_edge(START, "human_node")
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-22-39)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-22-40)# A checkpointer must be enabled for interrupts to work!
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-22-41)checkpointer = MemorySaver()
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-22-42)graph = builder.compile(checkpointer=checkpointer)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-22-43)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-22-44)config = {
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-22-45)  "configurable": {
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-22-46)    "thread_id": uuid.uuid4(),
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-22-47)  }
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-22-48)}
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-22-49)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-22-50)for chunk in graph.stream({"age": None, "name": None}, config):
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-22-51)  print(chunk)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-22-52)
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-22-53)for chunk in graph.stream(Command(resume="John", update={"name": "foo"}), config):
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-22-54)  print(chunk)

```


API Reference: [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.StateGraph) | [START](https://langchain-ai.github.io/langgraph/reference/constants/#langgraph.constants.START) | [interrupt](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.interrupt) | [Command](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Command) | [MemorySaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.MemorySaver)

```
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-23-1){'__interrupt__': (Interrupt(value='what is your name?', resumable=True, ns=['human_node:3a007ef9-c30d-c357-1ec1-86a1a70d8fba'], when='during'),)}
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-23-2)Name: N/A. Age: John
[](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__codelineno-23-3){'human_node': {'age': 'John', 'name': 'N/A'}}

```


## Additional Resources 📚[¶](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#additional-resources "Permanent link")

  * [**Conceptual Guide: Persistence**](https://langchain-ai.github.io/langgraph/concepts/persistence/#replay): Read the persistence guide for more context on replaying.
  * [**How to Guides: Human-in-the-loop**](https://langchain-ai.github.io/langgraph/how-tos/#human-in-the-loop): Learn how to implement human-in-the-loop workflows in LangGraph.
  * [**How to implement multi-turn conversations**](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-multi-turn-convo/): Learn how to implement multi-turn conversations in LangGraph.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Please help us improve this page by adding to the discussion below. 

## Comments

Back to top  [ Previous  Multi-agent Systems  ](https://langchain-ai.github.io/langgraph/concepts/multi_agent/) [ Next  Time Travel ⏱️  ](https://langchain-ai.github.io/langgraph/concepts/time-travel/)

Copyright © 2025 LangChain, Inc | [Consent Preferences](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/#__consent)

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)

[ ](https://langchain-ai.github.io/langgraphjs/ "langchain-ai.github.io") [ ](https://github.com/langchain-ai/langgraph "github.com") [ ](https://twitter.com/LangChainAI "twitter.com")

#### Cookie consent

We use cookies to recognize your repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find what they're searching for. **Clicking "Accept" makes our documentation better. Thank you!** ❤️

  * Google Analytics 
  * GitHub 



Accept Reject
